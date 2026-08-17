"""Power lint —— R-P42 錨點層範圍上界之執行期閘門（R-P52）。

R-P42 規範 Phase 4 撰寫 TC 之行為：某 leaf 之 TC 範圍上界為其
`Source Requirement ID` 所實際引用之需求錨點；未被引用之錨點一律不測。
本檔把該條文變成可機械檢查之閘門。

閘門 `check_rp42_unreferenced_anchor`：

  (a) 任一 TC 之 `specification_reference` 命中黑名單錨點 id → FAIL
  (b) 任一 TC 之內容（`pre_conditions` / `test_procedure` / `expected_result`
      / `test_item` / `input_test_data`）逐字引用黑名單錨點之**特徵字串** → FAIL

**黑名單為腳本導出，非人工維護**（R-P52(c)）——
讀 `data/unreferenced_anchors.tsv`，該檔由 `build_blacklist.py` 自
`layer3_full.tsv` 與兩份 CFTS 之全部錨點導出，leaf 增修時自動跟隨。

### 特徵字串之抽取方式（執行層自裁，見 07 上繳包 §三）

對每個黑名單錨點取其內文，切為句子，保留長度 ≥ MIN_FINGERPRINT 之句子，
再**扣除任何也出現於被引用錨點內文中的句子** —— 剩下者即為該錨點獨有之
特徵字串。扣除這一步是必要的：兩個錨點常共用樣板句（例如
「In the following "Ignition Working Conditions": ...」），
若不扣除，合法引用被引用錨點之 TC 會被誤判。

### 08 包新增四閘（R-P60）

  G37 R-P1  —— `SWE-PM-089` 不得有 TC，其來源欄不得被填補
  G38 R-P2  —— tc_id 格式、唯一、單調遞增、無跳號
  G39 R-P8  —— priority 值域 P0–P3，且不得與 037 `Priority` 呈一對一映射
  G40 R-P35 —— Test Set 須為五個定版值之一、逐 leaf 符 `leaf_testset.tsv`、
                全體分布 63 / 24 / 16 / 8 / 3

**權威來源之一項登記**：`feature.yaml` 自 scaffold 以來未更新 ——
其 `spec_mode: "A"` 與 R-P9 / R-P3′（= D）不符、`test_group: "Power"`
與 R-P2（workbook Test Group = "Power Management"）不符，且無 tc_id 格式欄。
本檔之權威值因此直接取自裁決條文並於此註明，**未逕改 feature.yaml**（見 A-PW36）。

用法：
    python features/power/scripts/lint_tcs.py                # 檢查 generated/*.json
    python features/power/scripts/lint_tcs.py --self-test    # 以合成 fixture 驗全部閘門
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

# 特徵字串之最短長度。過短會與樣板句碰撞，過長會漏抓。
MIN_FINGERPRINT = 40

# 受檢之 TC 內容欄位（R-P52(b)）
CONTENT_FIELDS = (
    "test_item", "pre_conditions", "input_test_data",
    "test_procedure", "expected_result",
)

# `\b` 在底線前不成立（`_` 為 word 字元），而 spec_reference 慣以底線串接，
# 故以「前後皆非數字」界定，勿用 \b —— 此為 G33 fixture (a) 首次執行時抓到之 bug。
ANCHOR_ID_RE = re.compile(r"(?<!\d)\d{6,8}(?!\d)")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.;:])\s+|\n+")

# ── 08 包新增之權威值（取自裁決條文，非 feature.yaml —— 見 docstring / A-PW36）──
BLOCKED_LEAF = "SWE-PM-089"                                   # R-P1
TC_ID_RE = re.compile(r"^NR1L-PowerManagement-(\d{3})$")       # R-P2
VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}                   # R-P8 / §10.2
LOCKED_DISTRIBUTION = {                                       # R-P35
    "Power State": 63, "Startup Display": 24,
    "Branding and Theme": 16, "Timeout Settings": 8, "Power Down": 3,
}
LOCKED_TOTAL = sum(LOCKED_DISTRIBUTION.values())              # 114

# G45 / §10.7：specification_reference 須非空，每項形如 {spec_filename}_{section_id}
SPEC_REF_ITEM_RE = re.compile(r"^\S+_\d+(?:\.\d+)*$")

# G46 / R-P69(c)：feature.yaml 須與裁決條文一致
YAML_EXPECTED = {
    "spec_mode": ("D", "R-P9 / R-P3′"),
    "test_group": ("Power Management", "R-P2（workbook Test Group）"),
    "tc_id_format": ("NR1L-PowerManagement-{NNN}", "R-P2"),
}


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def load_blacklist() -> dict[str, tuple[str, str, str]]:
    """anchor_id -> (cfts, chapter_num, chapter_title)。"""
    path = DATA / "unreferenced_anchors.tsv"
    if not path.exists():
        raise SystemExit(
            f"缺 {path.relative_to(ROOT)} —— 先跑 build_blacklist.py（R-P52(c)：黑名單須腳本導出）"
        )
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            anchor, cfts, num, title, _touched, _tier = line.split("\t")
            out[anchor] = (cfts, num, title)
    return out


def anchor_bodies() -> dict[str, list[str]]:
    """anchor_id -> 其後之內文段落（至下一錨點或章節錨點止）。"""
    bodies: dict[str, list[str]] = {}
    for path in [find("CFTS_009_Wake-up"),
                 next(x for x in IN.iterdir() if x.suffix == ".doc")]:
        current = None
        for plain, bold in paragraphs(path):
            if SEC_RE.match(plain):
                current = None
                continue
            found = REQ_RE.findall(bold)
            if found:
                current = found[0]
                bodies.setdefault(current, [])
            elif current and plain.strip():
                bodies[current].append(plain.strip())
    return bodies


def sentences(text: str) -> list[str]:
    return [s.strip() for s in SENTENCE_SPLIT_RE.split(text) if len(s.strip()) >= MIN_FINGERPRINT]


def build_fingerprints(blacklist: dict, bodies: dict[str, list[str]]) -> dict[str, list[str]]:
    """黑名單錨點獨有之特徵句 —— 扣除任何也出現於被引用錨點內文者。"""
    cited_sentences: set[str] = set()
    for anchor, lines in bodies.items():
        if anchor not in blacklist:
            for line in lines:
                cited_sentences.update(sentences(line))

    out: dict[str, list[str]] = {}
    for anchor in blacklist:
        unique = []
        for line in bodies.get(anchor, []):
            for s in sentences(line):
                if s not in cited_sentences:
                    unique.append(s)
        if unique:
            out[anchor] = unique
    return out


def check_rp42_unreferenced_anchor(
    tcs: list[dict], blacklist: dict, fingerprints: dict[str, list[str]]
) -> list[dict]:
    """回傳 findings；空 list = PASS。"""
    findings = []
    for tc in tcs:
        tc_id = tc.get("tc_id") or tc.get("req_id") or "(無 id)"

        # (a) specification_reference 命中黑名單錨點 id
        for anchor in ANCHOR_ID_RE.findall(str(tc.get("specification_reference", ""))):
            if anchor in blacklist:
                cfts, num, title = blacklist[anchor]
                findings.append({
                    "rule": "R-P42(a)", "tc_id": tc_id, "anchor": anchor,
                    "detail": f"specification_reference 命中未被引用之錨點 "
                              f"`{anchor}`（CFTS{cfts} §{num} {title}）",
                })

        # (b) 內容逐字引用黑名單錨點之特徵字串
        content = "\n".join(str(tc.get(f, "")) for f in CONTENT_FIELDS)
        for anchor, prints in fingerprints.items():
            for fp in prints:
                if fp in content:
                    cfts, num, title = blacklist[anchor]
                    findings.append({
                        "rule": "R-P42(b)", "tc_id": tc_id, "anchor": anchor,
                        "detail": f"內容逐字引用未被引用之錨點 `{anchor}`"
                                  f"（CFTS{cfts} §{num} {title}）之特徵字串："
                                  f"「{fp[:70]}…」",
                    })
                    break
    return findings


def leaf_of(tc: dict) -> str:
    """自 req_id / parent 取 leaf id（`SWE-PM-057-02` → `SWE-PM-057`）。"""
    raw = str(tc.get("req_id") or tc.get("parent") or "")
    m = re.match(r"(SWE-PM-\d+)", raw)
    return m.group(1) if m else raw


def load_leaf_testset() -> dict[str, str]:
    path = DATA / "leaf_testset.tsv"
    return {
        line.split("\t")[0]: line.split("\t")[1]
        for line in path.read_text(encoding="utf-8").splitlines()[1:] if line.strip()
    }


def load_037_priority() -> dict[str, str]:
    """037 `Priority` 欄 —— 僅供 G39 之「不得一對一映射」比對（R-P8）。"""
    import openpyxl
    wb = openpyxl.load_workbook(find("FSM-037"), data_only=True, read_only=True)
    ws = wb["SWE1 Requirements"]
    out = {
        str(r[0]).strip(): str(r[15] or "").strip()
        for r in ws.iter_rows(min_row=8, max_row=145, values_only=True)
        if r[0] and str(r[0]).strip()
    }
    wb.close()
    return out


def check_rp1_blocked_leaf(tcs: list[dict]) -> list[dict]:
    """G37 / R-P1：`SWE-PM-089` 不得有 TC，其來源欄不得被填補。"""
    findings = []
    for tc in tcs:
        tc_id = tc.get("tc_id") or tc.get("req_id") or "(無 id)"
        if leaf_of(tc) == BLOCKED_LEAF:
            findings.append({
                "rule": "R-P1", "tc_id": tc_id,
                "detail": f"{BLOCKED_LEAF} 之 TC 存在 —— R-P1 裁定該 leaf 留空待 DR-PW1",
            })
        elif BLOCKED_LEAF in str(tc.get("specification_reference", "")):
            findings.append({
                "rule": "R-P1", "tc_id": tc_id,
                "detail": f"specification_reference 引用 {BLOCKED_LEAF}，其來源尚未裁定",
            })
    return findings


def check_rp2_tc_id(tcs: list[dict]) -> list[dict]:
    """G38 / R-P2：tc_id 格式、唯一、單調遞增、無跳號。"""
    findings, seen, numbers = [], {}, []
    previous = None
    for tc in tcs:
        tc_id = str(tc.get("tc_id", ""))
        m = TC_ID_RE.match(tc_id)
        if not m:
            findings.append({
                "rule": "R-P2", "tc_id": tc_id or "(空)",
                "detail": f"tc_id 不符 R-P2 之格式 NR1L-PowerManagement-{{NNN}}",
            })
            continue
        n = int(m.group(1))
        if tc_id in seen:
            findings.append({"rule": "R-P2", "tc_id": tc_id,
                             "detail": f"tc_id 重複（前次見於 {seen[tc_id]}）"})
        seen[tc_id] = tc.get("_file", "?")
        if previous is not None and n <= previous:
            findings.append({"rule": "R-P2", "tc_id": tc_id,
                             "detail": f"tc_id 未單調遞增（前一個為 {previous:03d}）"})
        previous = n
        numbers.append(n)
    if numbers:
        expected = set(range(min(numbers), min(numbers) + len(set(numbers))))
        gaps = sorted(expected - set(numbers))
        if gaps:
            findings.append({
                "rule": "R-P2", "tc_id": "(全體)",
                "detail": f"tc_id 有跳號：{', '.join(f'{g:03d}' for g in gaps[:10])}",
            })
    return findings


def check_rp8_priority(tcs: list[dict], leaf_priority: dict[str, str]) -> list[dict]:
    """G39 / R-P8：priority 值域；且不得與 037 `Priority` 呈一對一映射。"""
    findings = []
    for tc in tcs:
        p = str(tc.get("priority", "")).strip()
        if p not in VALID_PRIORITIES:
            findings.append({
                "rule": "R-P8", "tc_id": tc.get("tc_id", "(無 id)"),
                "detail": f"priority `{p}` 不在 P0–P3 之內",
            })

    # 一對一映射偵測：037 之每個 Priority 值是否恰對應單一 TC priority
    mapping: dict[str, set] = defaultdict(set)
    for tc in tcs:
        src = leaf_priority.get(leaf_of(tc))
        p = str(tc.get("priority", "")).strip()
        if src and p in VALID_PRIORITIES:
            mapping[src].add(p)
    live = {k: v for k, v in mapping.items() if v}
    if len(live) >= 2 and all(len(v) == 1 for v in live.values()):
        targets = [next(iter(v)) for v in live.values()]
        if len(set(targets)) == len(targets):
            findings.append({
                "rule": "R-P8", "tc_id": "(全體)",
                "detail": "priority 與 037 `Priority` 欄呈一對一映射（"
                          + "、".join(f"{k}→{next(iter(v))}" for k, v in live.items())
                          + "）—— R-P8 裁定 037 Priority 不具映射權威",
            })
    return findings


def check_rp35_test_set(tcs: list[dict], leaf_testset: dict[str, str]) -> list[dict]:
    """G40 / R-P35：Test Set 值域、逐 leaf 相符、全體分布。"""
    findings = []
    for tc in tcs:
        ts = str(tc.get("test_set", "")).strip()
        tc_id = tc.get("tc_id", "(無 id)")
        if ts not in LOCKED_DISTRIBUTION:
            findings.append({"rule": "R-P35", "tc_id": tc_id,
                             "detail": f"Test Set `{ts}` 不在五個定版值之內"})
            continue
        expected = leaf_testset.get(leaf_of(tc))
        if expected and ts != expected:
            findings.append({
                "rule": "R-P35", "tc_id": tc_id,
                "detail": f"{leaf_of(tc)} 之 Test Set 為 `{ts}`，"
                          f"與 leaf_testset.tsv 之 `{expected}` 不符",
            })

    # R-P68：改為子集檢查 —— 每批皆驗，不再只在 114 齊備時判定
    covered = Counter()
    for tc in tcs:
        ts = str(tc.get("test_set", "")).strip()
        if ts in LOCKED_DISTRIBUTION:
            covered[ts] = len({leaf_of(t) for t in tcs
                               if str(t.get("test_set", "")).strip() == ts})
    for name, want in LOCKED_DISTRIBUTION.items():
        got = covered.get(name, 0)
        if got > want:                                        # (a) 上界
            findings.append({
                "rule": "R-P35", "tc_id": "(全體)",
                "detail": f"Test Set `{name}` 已產出 {got} 個 leaf，超過定版之 {want}",
            })
    leaves = {leaf_of(tc) for tc in tcs if leaf_of(tc) in leaf_testset}
    if len(leaves) == LOCKED_TOTAL:                           # (c) 齊備時驗相等
        for name, want in LOCKED_DISTRIBUTION.items():
            got = covered.get(name, 0)
            if got != want:
                findings.append({
                    "rule": "R-P35", "tc_id": "(全體)",
                    "detail": f"114 leaf 齊備，Test Set `{name}` 涵蓋 {got} 個，定版為 {want}",
                })
    return findings


def check_s107_spec_reference(tcs: list[dict]) -> list[dict]:
    """G45 / §10.7（R-P66）：specification_reference 非空且每項符形態。

    形態 `{spec_filename}_{section_id}` —— 檔名任意非空白，section_id 為
    點分隔之數字串（`1.7.2`、`1.7.1.1.1`）。多項以 `; ` 分隔。
    """
    findings = []
    for tc in tcs:
        tc_id = tc.get("tc_id") or tc.get("req_id") or "(無 id)"
        raw = str(tc.get("specification_reference", "")).strip()
        if not raw:
            findings.append({
                "rule": "§10.7", "tc_id": tc_id,
                "detail": "specification_reference 為空 —— §10.7 要求必填",
            })
            continue
        for item in [x.strip() for x in raw.split(";") if x.strip()]:
            if not SPEC_REF_ITEM_RE.match(item):
                findings.append({
                    "rule": "§10.7", "tc_id": tc_id,
                    "detail": f"specification_reference 之項目 `{item}` "
                              f"不符 {{spec_filename}}_{{section_id}} 形態",
                })
    return findings


def check_feature_yaml_consistency() -> list[dict]:
    """G46 / R-P69(c)：feature.yaml 與裁決條文一致 —— 偵測未來漂移。

    lint 之權威值仍取自裁決條文（R-P69(b)）；本閘只驗二者未分歧。
    """
    path = ROOT / "features/power/feature.yaml"
    if not path.exists():
        return [{"rule": "R-P69", "tc_id": "(feature.yaml)", "detail": "檔案不存在"}]
    text = path.read_text(encoding="utf-8")
    findings = []
    for key, (want, source) in YAML_EXPECTED.items():
        m = re.search(rf'^\s*{re.escape(key)}\s*:\s*"?([^"#\n]+?)"?\s*(?:#.*)?$',
                      text, re.M)
        got = m.group(1).strip() if m else None
        if got != want:
            findings.append({
                "rule": "R-P69", "tc_id": "(feature.yaml)",
                "detail": f"`{key}` 為 {got!r}，裁決條文（{source}）定為 {want!r}",
            })
    if "<" in text and ">" in re.sub(r"#.*", "", text):
        for m in re.finditer(r"^\s*(\w+)\s*:\s*\"?([^\"\n]*<[^>]+>[^\"\n]*)\"?",
                             text, re.M):
            findings.append({
                "rule": "R-P69", "tc_id": "(feature.yaml)",
                "detail": f"`{m.group(1)}` 仍為 scaffold placeholder：{m.group(2).strip()}",
            })
    return findings


def load_tcs(directory: Path) -> list[dict]:
    tcs = []
    for path in sorted(directory.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for tc in data.get("tcs", []):
            tc = dict(tc)
            tc.setdefault("_file", path.name)
            tcs.append(tc)
    return tcs


def make_tc(n: int, leaf: str, test_set: str, **over) -> dict:
    """合成一條合法 TC（不讀 generated/，08 §I）。"""
    tc = {
        "req_id": f"{leaf}-01",
        "tc_id": f"NR1L-PowerManagement-{n:03d}",
        "test_group": "Power Management",
        "test_set": test_set,
        "test_item": "Verify the power state transition is applied.",
        "pre_conditions": "1. [spec-derived] Vehicle in Ignition On",
        "input_test_data": "NA",
        "test_procedure": "1. Set the power mode signal to the target state",
        "expected_result": "1. The head unit applies the corresponding policy",
        "specification_reference": "CFTS009_1.6.2.1.1_4941357",
        "priority": "P2",
    }
    tc.update(over)
    return tc


def synthetic_full_set(leaf_testset: dict[str, str]) -> list[dict]:
    """依 leaf_testset.tsv 合成 114 條 —— 用於 G40 之分布檢查。"""
    return [
        make_tc(i + 1, leaf, ts)
        for i, (leaf, ts) in enumerate(sorted(
            leaf_testset.items(), key=lambda kv: int(re.match(r"SWE-PM-(\d+)", kv[0]).group(1))
        ))
    ]


def self_test(blacklist: dict, fingerprints: dict) -> int:
    """以合成 fixture 驗全部閘門 —— 不以 repo 現況為對照（07 / 08 §I）。"""
    leaf_testset = load_leaf_testset()
    leaf_priority = load_037_priority()
    blacklisted = next(a for a in fingerprints)
    fingerprint = fingerprints[blacklisted][0]
    cited_anchor = next(a for a in anchor_bodies() if a not in blacklist)
    full = synthetic_full_set(leaf_testset)

    cases: list[tuple[str, str, list[dict], list[str]]] = [
        # ── G33 / R-P42（07 包，沿用）──
        ("G33", "應 PASS —— 只引用被引用之錨點",
         [make_tc(1, "SWE-PM-001", "Power State",
                  specification_reference=f"CFTS009_1.6.2.1.1_{cited_anchor}")], []),
        ("G33", "應因 (a) FAIL —— specification_reference 命中黑名單",
         [make_tc(1, "SWE-PM-001", "Power State",
                  specification_reference=f"CFTS009_1.6.2.1.1_{blacklisted}")], ["R-P42(a)"]),
        ("G33", "應因 (b) FAIL —— 內容逐字引用黑名單特徵字串",
         [make_tc(1, "SWE-PM-001", "Power State",
                  test_procedure=f"1. {fingerprint}")], ["R-P42(b)"]),

        # ── G37 / R-P1 ──
        ("G37", "應 PASS —— 未觸及 SWE-PM-089",
         [make_tc(1, "SWE-PM-001", "Power State")], []),
        ("G37", "應 FAIL —— 存在 SWE-PM-089 之 TC",
         [make_tc(1, "SWE-PM-089", "Power State")], ["R-P1"]),
        # 本例同時違反 §10.7（`SWE-PM-089_source_pending` 之 section_id 非數字串），
        # 二閘皆觸發為正確行為，故期望值列出兩者。
        ("G37", "應 FAIL —— specification_reference 引用 SWE-PM-089",
         [make_tc(1, "SWE-PM-001", "Power State",
                  specification_reference="SWE-PM-089_source_pending")],
         ["R-P1", "§10.7"]),

        # ── G38 / R-P2 ──
        ("G38", "應 PASS —— tc_id 格式正確且連號",
         [make_tc(1, "SWE-PM-001", "Power State"),
          make_tc(2, "SWE-PM-002", "Power State")], []),
        ("G38", "應 FAIL —— tc_id 格式錯誤",
         [make_tc(1, "SWE-PM-001", "Power State", tc_id="NR1L-Power-001")], ["R-P2"]),
        ("G38", "應 FAIL —— tc_id 重複",
         [make_tc(1, "SWE-PM-001", "Power State"),
          make_tc(1, "SWE-PM-002", "Power State")], ["R-P2"]),
        ("G38", "應 FAIL —— tc_id 跳號",
         [make_tc(1, "SWE-PM-001", "Power State"),
          make_tc(3, "SWE-PM-002", "Power State")], ["R-P2"]),

        # ── G39 / R-P8 ──
        ("G39", "應 PASS —— priority 為 P0–P3 且非一對一映射",
         [make_tc(1, "SWE-PM-001", "Power State", priority="P1"),
          make_tc(2, "SWE-PM-057", "Timeout Settings", priority="P1"),
          make_tc(3, "SWE-PM-002", "Power State", priority="P2")], []),
        ("G39", "應 FAIL —— priority 為 037 之 `High`",
         [make_tc(1, "SWE-PM-001", "Power State", priority="High")], ["R-P8"]),
        ("G39", "應 FAIL —— 與 037 Priority 呈一對一映射",
         None, ["R-P8"]),   # 於下方依實際 037 值組出

        # ── G45 / §10.7（R-P66）──
        ("G45", "應 PASS —— spec_reference 非空且形態正確",
         [make_tc(1, "SWE-PM-071", "Power Down",
                  specification_reference="CFTS010_1.7.1.1.1; CFTS010_1.7.2")], []),
        ("G45", "應 FAIL —— spec_reference 為空",
         [make_tc(1, "SWE-PM-071", "Power Down", specification_reference="")], ["§10.7"]),
        ("G45", "應 FAIL —— spec_reference 形態不符",
         [make_tc(1, "SWE-PM-071", "Power Down",
                  specification_reference="see the power down chapter")], ["§10.7"]),

        # ── G40 / R-P35（R-P68 之子集檢查）──
        ("G40", "應 PASS —— 完整 114 條，分布符定版",
         full, []),
        ("G40", "應 FAIL —— Test Set 非五個定版值之一",
         [make_tc(1, "SWE-PM-001", "Power Management")], ["R-P35"]),
        ("G40", "應 FAIL —— 某 leaf 之歸屬與 leaf_testset.tsv 不符",
         [make_tc(1, "SWE-PM-057", "Power State")], ["R-P35"]),
        ("G40", "應 FAIL —— 完整 114 條但分布不符定版",
         None, ["R-P35"]),  # 於下方由 full 改一條組出
        ("G40", "應 PASS —— 部分批次（3 條 Power Down），未達上界",
         [make_tc(1, "SWE-PM-071", "Power Down"),
          make_tc(2, "SWE-PM-072", "Power Down"),
          make_tc(3, "SWE-PM-073", "Power Down")], []),
        ("G40", "應 FAIL —— 整批一致地歸錯，超過該 Test Set 之上界（R-P68(a)）",
         None, ["R-P35"]),  # 於下方組出：4 個 leaf 全記 Power Down
    ]

    # G39 一對一映射之違規 fixture：037 之每個 Priority 值對應唯一之 TC priority
    priority_map = {"High": "P1", "Medium": "P3"}
    mapped = [
        make_tc(i + 1, leaf, leaf_testset[leaf],
                priority=priority_map.get(leaf_priority.get(leaf, ""), "P2"))
        for i, leaf in enumerate(sorted(
            leaf_testset, key=lambda x: int(re.match(r"SWE-PM-(\d+)", x).group(1)))[:20])
    ]
    # 分布違規 fixture：把一條 Power State 改記為 Timeout Settings
    skewed = [dict(tc) for tc in full]
    for tc in skewed:
        if tc["test_set"] == "Power State":
            tc["test_set"] = "Timeout Settings"
            break

    # R-P68(a) 之上界違規：4 個 leaf 全記 Power Down（定版僅 3）——
    # 原讀法（僅在 114 齊備時比對）攔不下此情形
    over_cap = [make_tc(i + 1, leaf, "Power Down")
                for i, leaf in enumerate(
                    ["SWE-PM-071", "SWE-PM-072", "SWE-PM-073", "SWE-PM-093"])]

    placeholders = {"G39": mapped}
    seen_g40 = 0
    filled = []
    for gate, label, tcs, expected in cases:
        if tcs is None:
            if gate == "G39":
                tcs = mapped
            else:
                seen_g40 += 1
                tcs = skewed if seen_g40 == 1 else over_cap
        filled.append((gate, label, tcs, expected))

    print("lint fixture 測試（全為合成 TC，未讀 generated/）")
    print(f"  黑名單錨點樣本：{blacklisted}")
    print(f"  特徵字串樣本  ：「{fingerprint[:64]}…」")
    print(f"  被引用錨點樣本：{cited_anchor}\n")

    failures = 0
    for gate, label, tcs, expected in filled:
        findings = (
            check_rp42_unreferenced_anchor(tcs, blacklist, fingerprints)
            + check_rp1_blocked_leaf(tcs)
            + check_rp2_tc_id(tcs)
            + check_rp8_priority(tcs, leaf_priority)
            + check_rp35_test_set(tcs, leaf_testset)
            + check_s107_spec_reference(tcs)
        )
        got = sorted({f["rule"] for f in findings})
        ok = got == sorted(expected)
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] {gate} {label}")
        print(f"          期望 {expected or '（無）'}；實際 {got or '（無）'}")
        for f in findings[:2]:
            print(f"          → {f['rule']} {f['tc_id']}: {f['detail'][:92]}")
    # G46 / R-P69(c) —— 與 tcs 無關，獨立驗證
    yaml_findings = check_feature_yaml_consistency()
    print(f"\n  [{'PASS' if not yaml_findings else '**FAIL**'}] G46 "
          f"feature.yaml 與裁決條文一致")
    for f in yaml_findings:
        print(f"          → {f['rule']} {f['detail'][:96]}")
    failures += bool(yaml_findings)

    print(f"\n  全部 {len(filled)} 個 TC fixture ＋ G46 皆如期："
          f"{'是' if failures == 0 else '否'}")
    return 1 if failures else 0


def main() -> None:
    blacklist = load_blacklist()
    fingerprints = build_fingerprints(blacklist, anchor_bodies())
    print(f"R-P42 黑名單 {len(blacklist)} 個錨點；"
          f"其中 {len(fingerprints)} 個具獨有特徵字串"
          f"（共 {sum(len(v) for v in fingerprints.values())} 句，"
          f"最短 {MIN_FINGERPRINT} 字元）\n")

    if "--self-test" in sys.argv:
        raise SystemExit(self_test(blacklist, fingerprints))

    if not GENERATED.exists() or not any(GENERATED.glob("*.json")):
        print(f"{GENERATED.relative_to(ROOT)} 無 TC —— Phase 4 尚未開始，閘門就位待用。")
        print("以 --self-test 驗證閘門本身。")
        raise SystemExit(0)

    tcs = load_tcs(GENERATED)
    findings = (
        check_rp42_unreferenced_anchor(tcs, blacklist, fingerprints)
        + check_rp1_blocked_leaf(tcs)
        + check_rp2_tc_id(tcs)
        + check_rp8_priority(tcs, load_037_priority())
        + check_rp35_test_set(tcs, load_leaf_testset())
        + check_s107_spec_reference(tcs)
        + check_feature_yaml_consistency()
    )
    print(f"檢查 {len(tcs)} 個 TC —— {'PASS' if not findings else f'**{len(findings)} 項 FAIL**'}")
    for f in findings:
        print(f"  {f['rule']} {f['tc_id']}: {f['detail']}")
    raise SystemExit(1 if findings else 0)


if __name__ == "__main__":
    main()
