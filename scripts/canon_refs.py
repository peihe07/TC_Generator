#!/usr/bin/env python3
"""canon 引用之唯一可解析性（R-G57）。

掃全 repo 之 canon 引用，驗每一引用**唯一命中一份 canon 之一個落點**。
`unresolved` 或 `ambiguous` > 0 即 FAIL。每 feature close-out 必跑。

**本專案有兩份 canon**（R-G57 首跑所揭；「canon §X」之歧義主要源於此）：

| 代號 | 檔 | 管什麼 |
|---|---|---|
| `FO` | `docs/fw036/FEATURE_ONBOARDING.md` | 流程、下放／上繳契約、全域裁決 |
| `IN` | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` | TC 撰寫規則、欄位、自查表 |

`## 9.` 於兩份中皆有（FO 之通則／全域慣例、IN 之 Self-Check），
故裸「canon §9」為**三重歧義**。以 `FO §9.2`／`IN §9` 之前綴消歧。

**引用之型**（量測條件；`--report` 逐筆列出）：

| 型 | 形態 | 解析對象 |
|---|---|---|
| `section` | `canon §9.2`、`FO §5a`、`IN §10.4` | canon 標題編號 |
| `item`    | `canon §5a 第 9 條`、`§10.4-2` | 該節內之條號（表列或編號條列）|
| `ruling`  | `R-G51` | FO §9.2 之全域條文編號（全域命名空間）|

**qualified 之判準**（盲區宣告，R-G11）：**逐處**取該 `§` 之前
`QUALIFIER_WINDOW`（30）字元，找**最近**之標記：
`canon`／`FO`／`IN`／`FEATURE_ONBOARDING`／`ASPICE_SWE6` → canon 引用；
`包`／`輪`／`W-`／`V<n>`／`上繳`／`.md`／`.py`／`profile`／`framework`
／`PLAYBOOK` 等**下放包或他檔之指稱** → 非 canon 引用。
兩類皆無、或非 canon 者較近 → `unqualified`，**不計入 FAIL**。

> **首版以「同一行內有無 `canon`」判之，為行級啟發式。** W-P2 逐處判讀
> `vehicle_setting` 之 35 處時實測：**19 處（54%）指下放包節號**
> （`26 包 §2`、`W-VF68 §2.1`、`V17 §3`、`` `00_intake_and_rulings.md` §3 ``），
> 因同行另有 `canon` 而被誤判為 canon 引用。改為逐處就近判定。
> **本工具之盲區仍在**：未加前綴而實指 canon 者驗不到（其形態見
> `ANOMALIES.md` 之 `§8.7.5 §0 之衝突條款` —— 該 `§0` 實指 FO §0 而無前綴）。

**waiver（R-G57 之修訂版，24 包 §C 裁定 2）**：歷史 handoff / upstream 檔
不追改，其既有 unresolved / ambiguous 逐檔逐行列於
`docs/fw036/CANON_REFS_WAIVER.tsv`（欄：`source line kind target reason`）。
閘判準：**waiver 清單外**之 unresolved 或 ambiguous > 0 即 FAIL；
**waiver 只減不增** —— 清單內而現已不存在之列記為 `stale`（僅回報，不 FAIL），
清單外之新引用即紅。

**掃描面**：治理文件與程式碼（`docs/`、`features/**/docs/`、
`features/*/RULINGS.md` 等四本、`scripts/`、`features/**/scripts/`）。
**排除** `archive/`、`sandbox/`、`data/`、`generated/`、`inputs/`
—— 其 `§` 多為 spec 內文，非 canon 引用。

唯讀，不寫入任何檔案。
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

CANONS = {
    "FO": "docs/fw036/FEATURE_ONBOARDING.md",
    "IN": "docs/runtime/ASPICE_SWE6_AI_Instruction.md",
}
GOVERNANCE_FILES = {"RULINGS.md", "ANOMALIES.md", "DATA_REQUESTS.md", "DECISIONS.md"}
WAIVER_DEFAULT = "docs/fw036/CANON_REFS_WAIVER.tsv"
# 鍵為 `(source, kind, target, line_sha8)`；`line` 降為輔助欄（顯示用，不參與比對）。
# **改鍵之理由**（26 上繳 §五-1，本輪失效兩次）：以行號為鍵者，
# **任何在被豁免行之上插入一行即製造一次假性新增** —— 而 R-G57 令
# 「waiver 只減不增，新增即紅」，遂使每次正當之增補都要手動維護行號。
# 內容雜湊之語意為「**這一行的這個引用**」：行移動不失效，行內容改動即失效
# ——後者正確，因為內容改了本來就該重判。
WAIVER_COLUMNS = ["source", "kind", "target", "line_sha8", "line", "reason"]
# 歷史檔：作成當時之正確紀錄，不追改（R-VF18 之精神；24 包 §C 裁定 2）。
# 判準為**路徑成分**，非子串 —— `docs/fw036/upstream/` 不含 `docs/upstream/`，
# 以子串比對會把 `docs/fw036/` 下之歷史包誤分為活躍（本判準之首個實測缺陷）。
HISTORICAL_PARTS = {"handoff", "upstream"}
# R-G16 補充：排除集集中於 `scripts/measure_common.py`，不逐檔各記。
# 本檔於測試中以檔案路徑載入（`spec_from_file_location`），`scripts/` 未必在 sys.path，
# 故先把本檔所在目錄補上再 import —— 不補則測試在收集階段即 ImportError。
sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure_common import is_measurement_output
from ruling_anchor import anchor_ruling_numbers

SCAN_SUFFIXES = {".md", ".py", ".yaml", ".yml"}
SKIP_PARTS = {
    ".git", "__pycache__", "node_modules", ".venv", "spec-index",
    "archive", "sandbox", "data", "generated", "inputs", "_intake", "forms",
}
QUALIFIER_WINDOW = 30
# --- 使用／提及之二分（R-G57 之精度；27 包 §三）------------------------------
#
# **一篇說明某引用為何歧義的文字，其本身不該成為一個歧義引用。**
# 26 上繳 §五-2 實測本層於一節之內連續誤踩四次 —— 其非不小心，
# 是判準要求作者在寫作時持續維持一種不自然的迴避。
#
# 判準：**圍籬優先於動詞**。被引號／反引號／code fence／[SUPERSEDED]
# 區塊包住者一律為「提及」，縱使其**內部**有規範性動詞（第 2 例即此形）。
# 未被包住而有規範性動詞引導者為「使用」，計入解析義務。
NORMATIVE = re.compile(r"依據|依照|違反|適用|豁免|依|照|見|據|按")
# 詞彙型「提及」標記：其後之節號是被談論的對象，不是被援引的依據
MENTION = re.compile(r"之條文|所述|該節|原文|提及|所指|字串|寫作|複寫|逐字複")
RE_SUPERSEDED_MARK = re.compile(r"\[SUPERSEDED")
RE_CANON_MARK = re.compile(r"canon|FEATURE_ONBOARDING|ASPICE_SWE6|Instruction|\bFO\b|\bIN\b")
# 下放包／輪次／他檔之指稱 —— 其後之 `§N` 為該物之節號，非 canon 之節號
RE_OTHER_MARK = re.compile(
    r"包|輪|上繳|下放|W-[\w()（）]+|\bV\d+|"
    r"\.md|\.py|\.tsv|\.yaml|profile|PLAYBOOK|framework|RUNBOOK|"
    r"RULINGS|ANOMALIES|DECISIONS|DATA_REQUESTS"
)

SEC = r"[0-9]+[a-z]?(?:\.[0-9]+){0,2}"
RE_ITEM_CN = re.compile(rf"§(?P<sec>{SEC})\s*第\s*(?P<n>[0-9]+)\s*[條項點]")
RE_ITEM_DASH = re.compile(rf"§(?P<sec>{SEC})\s*[-‑–]\s*(?P<n>[0-9]+)(?![0-9.])")
RE_SEC = re.compile(rf"(?P<doc>\b(?:FO|IN)\s+)?§(?P<sec>{SEC})")
RE_RULING = re.compile(r"(?<![0-9A-Za-z-])R-G(?P<n>[0-9]+)(?:-[0-9]+)?(?![0-9A-Za-z])")
RE_HEADING = re.compile(rf"^(?P<hashes>#{{1,6}})\s+(?P<sec>{SEC})[.．]?\s")
RE_TABLE_N = re.compile(r"^>?\s*\|\s*\**\s*(?P<n>[0-9]+)\s*\**\s*\|")
RE_LIST_N = re.compile(r"^\s{0,3}(?P<n>[0-9]+)[.)]\s")


@dataclass(frozen=True)
class Ref:
    kind: str        # section | item | ruling | unqualified
    target: str
    verdict: str     # resolved | unresolved | ambiguous
    hits: tuple      # 命中之 (canon代號, 節號) —— ambiguous 時列全部
    source: str
    line: int
    text: str
    usage: str = "use"   # use（計入解析義務）| mention（不計）
    line_sha8: str = ""  # 該行內容之 sha8 —— waiver 鍵之一部分（27 包 §四）


@dataclass
class CanonIndex:
    """單一 canon 之節號與節內條號。"""

    code: str
    sections: Counter = field(default_factory=Counter)
    items: dict = field(default_factory=dict)
    rulings: set = field(default_factory=set)

    @classmethod
    def build(cls, code: str, path: Path) -> "CanonIndex":
        idx = cls(code)
        current = ""
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = RE_HEADING.match(line)
            if m:
                current = m.group("sec")
                idx.sections[current] += 1
            for rm in RE_RULING.finditer(line):
                idx.rulings.add(rm.group("n"))
            if not current:
                continue
            for pat in (RE_TABLE_N, RE_LIST_N):
                im = pat.match(line)
                if im:
                    n = int(im.group("n"))
                    idx.items[current] = max(idx.items.get(current, 0), n)
                    break
        return idx


# ruling 型之解析面（R-G43(d)，Pei 2026-09-05「裁」）：除兩份 canon 外，
# 台帳亦為條文之落點 —— 不索引台帳則「有指紋而解析不到」（A-GC15 實測 963 處）。
# 錨點判準與 `rulings_hash` 共用 `ruling_anchor.RE_ANCHOR`，不各寫一份。
RULING_SOURCES = dict(CANONS, LEDGER="docs/fw036/RULINGS_LEDGER.md")


class Resolver:
    def __init__(self, root: Path):
        self.canons = {c: CanonIndex.build(c, root / p) for c, p in CANONS.items()}
        # 兩份 canon 之 ruling 索引維持既有取法（行內提及亦算，見 CanonIndex.build）——
        # 本輪只**增**台帳這個來源，不改 canon 側之判準（改之則 FO 之索引由 50 號縮為錨點數，
        # 實測反使 unresolved 由 963 升為 1682）。台帳側以錨點為準（R-G43(c)）。
        self.ruling_anchors = {c: set(idx.rulings) for c, idx in self.canons.items()}
        for c, rel in RULING_SOURCES.items():
            if c in self.ruling_anchors:
                continue
            f = root / rel
            # 檔不在即視為無錨點（測試之最小 repo 無台帳；缺檔不得使解析器整支炸掉）
            self.ruling_anchors[c] = (
                anchor_ruling_numbers(f.read_text(encoding="utf-8")) if f.exists() else set()
            )

    def section_hits(self, sec: str, doc: str | None) -> list[tuple[str, int]]:
        """回傳 [(canon代號, 該節於該 canon 之出現次數)]，只含次數 ≥1 者。"""
        scope = [doc] if doc in self.canons else list(self.canons)
        return [(c, self.canons[c].sections[sec]) for c in scope
                if self.canons[c].sections[sec] > 0]

    def resolve_section(self, sec: str, doc: str | None) -> tuple[str, tuple]:
        hits = self.section_hits(sec, doc)
        total = sum(n for _, n in hits)
        target = tuple(f"{c}§{sec}" + (f"×{n}" if n > 1 else "") for c, n in hits)
        if total == 0:
            return "unresolved", ()
        return ("resolved", target) if total == 1 else ("ambiguous", target)

    def resolve_item(self, sec: str, n: int, doc: str | None) -> tuple[str, tuple]:
        verdict, target = self.resolve_section(sec, doc)
        if verdict != "resolved":
            return verdict, target
        code = target[0][:2]
        cap = self.canons[code].items.get(sec, 0)
        if 1 <= n <= cap:
            return "resolved", (f"{code}§{sec} 第{n}（上限 {cap}）",)
        return "unresolved", (f"{code}§{sec} 條號上限 {cap}，引用 {n}",)

    def resolve_ruling(self, n: str) -> tuple[str, tuple]:
        """條號唯一即已可解析（Pei 2026-09-05「裁」，GC-06 補遺 §1）。

        同號在兩側皆有錨者（`R-G42`／`R-G4`／`R-G7`）判 **resolved**，不判 ambiguous：
        引用寫的是條號，條號指得到落點就解析得了；兩側本體之差異由
        `rulings_hash` 之撞號表管，不是引用解析器的事。
        """
        hits = [c for c, ns in self.ruling_anchors.items() if n in ns]
        if not hits:
            return "unresolved", ()
        return "resolved", tuple(f"{c}:R-G{n}" for c in hits)


def enclosing_spans(line: str) -> list:
    """該行中之引號／反引號區間 —— 落於其內者為「提及」。"""
    spans, stack = [], {}
    for i, ch in enumerate(line):
        if ch == "「":
            stack.setdefault("「", []).append(i)
        elif ch == "」" and stack.get("「"):
            spans.append((stack["「"].pop(), i))
        elif ch == "『":
            stack.setdefault("『", []).append(i)
        elif ch == "』" and stack.get("『"):
            spans.append((stack["『"].pop(), i))
    for quote in ("`", '"', "“"):
        pass
    # 反引號與直引號成對掃描
    for ch, close in (("`", "`"), ('"', '"'), ("“", "”")):
        idx, open_at = 0, None
        while idx < len(line):
            c = line[idx]
            if open_at is None and c == ch:
                open_at = idx
            elif open_at is not None and c == close and idx > open_at:
                spans.append((open_at, idx))
                open_at = None
            idx += 1
    return spans


def usage_of(line: str, pos: int, in_fence: bool, in_superseded: bool) -> str:
    """單一 `§` 之使用／提及判定。**圍籬優先於動詞。**"""
    if in_fence or in_superseded:
        return "mention"
    if any(a < pos < b for a, b in enclosing_spans(line)):
        return "mention"
    # 圍籬外：取窗內**最近**之標記；兩者皆無則預設為使用
    window = line[max(0, pos - QUALIFIER_WINDOW):pos]
    m_at = max((m.end() for m in MENTION.finditer(window)), default=-1)
    n_at = max((m.end() for m in NORMATIVE.finditer(window)), default=-1)
    return "mention" if m_at > n_at else "use"


def is_canon_ref(line: str, pos: int) -> bool:
    """逐處判定：該 `§` 之前 30 字元內，**最近**之標記是否為 canon。"""
    window = line[max(0, pos - QUALIFIER_WINDOW):pos]
    canon_at = max((m.end() for m in RE_CANON_MARK.finditer(window)), default=-1)
    other_at = max((m.end() for m in RE_OTHER_MARK.finditer(window)), default=-1)
    return canon_at > other_at


def scan_line(rs: Resolver, source: str, lineno: int, line: str,
              in_fence: bool = False, in_superseded: bool = False) -> list[Ref]:
    """單行之引用抽取；先吃 item 型，其區段不再計為 section。"""
    out: list[Ref] = []
    used: list[tuple[int, int]] = []

    lsha = line_sha8(line)

    def usage_at(pos: int) -> str:
        return usage_of(line, pos, in_fence, in_superseded)

    def free(m: re.Match) -> bool:
        return not any(a <= m.start() < b for a, b in used)

    for pat, label in ((RE_ITEM_CN, "cn"), (RE_ITEM_DASH, "dash")):
        for m in pat.finditer(line):
            if not free(m):
                continue
            used.append((m.start(), m.end()))
            sec, n = m.group("sec"), int(m.group("n"))
            if not is_canon_ref(line, m.start()):
                out.append(Ref("unqualified", f"§{sec}-{n}", "resolved", (), source, lineno, m.group(0), usage_at(m.start()), lsha))
                continue
            verdict, hits = rs.resolve_item(sec, n, None)
            sep = " 第" if label == "cn" else "-"
            out.append(Ref("item", f"§{sec}{sep}{n}", verdict, hits, source, lineno, m.group(0), usage_at(m.start()), lsha))

    for m in RE_SEC.finditer(line):
        if not free(m):
            continue
        used.append((m.start(), m.end()))
        sec = m.group("sec")
        doc = (m.group("doc") or "").strip() or None
        if doc is None and not is_canon_ref(line, m.start()):
            out.append(Ref("unqualified", f"§{sec}", "resolved", (), source, lineno, m.group(0), usage_at(m.start()), lsha))
            continue
        verdict, hits = rs.resolve_section(sec, doc)
        label = f"{doc} §{sec}" if doc else f"§{sec}"
        out.append(Ref("section", label, verdict, hits, source, lineno, m.group(0), usage_at(m.start()), lsha))

    for m in RE_RULING.finditer(line):
        verdict, hits = rs.resolve_ruling(m.group("n"))
        out.append(Ref("ruling", f"R-G{m.group('n')}", verdict, hits, source, lineno, m.group(0), usage_at(m.start()), lsha))
    return out


def is_historical(source: str) -> bool:
    """歷史 handoff／upstream 檔 —— 其引用入 waiver，不追改。"""
    return bool(HISTORICAL_PARTS & set(Path(source).parts))


def fenced_lines(root: Path, source: str) -> set:
    """該檔中落在 ``` 圍籬內之行號 —— 條文逐字轉錄多在其內。"""
    try:
        lines = (root / source).read_text(encoding="utf-8").splitlines()
    except OSError:
        return set()
    out, inside = set(), False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if inside:
            out.add(i)
    return out


def waiver_reason(root: Path, r: "Ref", fence_cache: dict) -> str:
    """waiver 之三類理由。`active-backlog` 為**暫時**豁免，待裁後改寫。"""
    if is_historical(r.source):
        return "historical-record"
    if r.source in CANONS.values():
        if r.source not in fence_cache:
            fence_cache[r.source] = fenced_lines(root, r.source)
        if r.line in fence_cache[r.source]:
            return "verbatim-ruling-text"
    return "active-backlog"


def line_sha8(text: str) -> str:
    """該行內容之 sha8（去尾端空白）—— waiver 鍵之一部分。"""
    return hashlib.sha256(text.rstrip().encode("utf-8")).hexdigest()[:8]


def waiver_key(r: "Ref") -> tuple:
    return (r.source, r.kind, r.target, r.line_sha8)


def load_waiver(path: Path) -> dict:
    """讀 waiver tsv → {key: (reason, line)}；檔不存在時回空 dict。

    **相容舊格式**（`source line kind target reason`）：其無 `line_sha8`，
    以 `legacy` 佔位載入，由 `--migrate-waiver` 一次性遷移。
    """
    if not path.exists():
        return {}
    out = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return {}
    header = lines[0].split("\t")
    legacy = "line_sha8" not in header
    for line in lines[1:]:
        if not line.strip():
            continue
        c = line.split("\t")
        if legacy and len(c) >= 5:
            out[(c[0], c[2], c[3], "legacy")] = (c[4], c[1])
        elif not legacy and len(c) >= 6:
            out[(c[0], c[1], c[2], c[3])] = (c[5], c[4])
    return out


def waiver_hit(waived: dict, r: "Ref") -> str | None:
    """查該引用是否已豁免。舊格式以 `legacy` 鍵 fallback（遷移期）。"""
    v = waived.get(waiver_key(r))
    if v is not None:
        return v[0]
    v = waived.get((r.source, r.kind, r.target, "legacy"))
    return v[0] if v is not None else None


def in_scan_surface(rel: Path) -> bool:
    parts = rel.parts
    if is_measurement_output(rel):        # R-G16 補充：量測產出不入母體
        return False
    if any(p in SKIP_PARTS for p in parts):
        return False
    if rel.suffix.lower() not in SCAN_SUFFIXES:
        return False
    if parts[0] == "docs" or parts[0] == "scripts":
        return True
    if parts[0] == "features":
        return "docs" in parts or "scripts" in parts or rel.name in GOVERNANCE_FILES \
            or rel.name.endswith((".yaml", ".yml")) or len(parts) == 3 and rel.suffix == ".md"
    return False


def collect(root: Path) -> tuple[Resolver, list[Ref], int]:
    rs = Resolver(root)
    refs: list[Ref] = []
    n_files = 0
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if not in_scan_surface(rel):
            continue
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        n_files += 1
        in_fence = False
        in_sup = False
        for lineno, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if RE_SUPERSEDED_MARK.search(line):
                in_sup = True
            elif in_sup and not line.lstrip().startswith(">") and line.strip():
                in_sup = False          # blockquote 結束即離開 [SUPERSEDED] 區
            if "§" not in line and "R-G" not in line:
                continue
            refs.extend(scan_line(rs, str(rel), lineno, line, in_fence, in_sup))
    return rs, refs, n_files


def main() -> int:
    ap = argparse.ArgumentParser(description="canon 引用解析器（R-G57）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--report", action="store_true", help="逐筆列出 unresolved／ambiguous")
    ap.add_argument("--top", type=int, default=40, help="--report 時列出之 target 數上限")
    ap.add_argument("--waiver", nargs="?", const=WAIVER_DEFAULT, default=None,
                    help=f"以 waiver tsv 排除既有引用（預設 {WAIVER_DEFAULT}）")
    ap.add_argument("--emit-waiver", metavar="PATH",
                    help="產出 waiver tsv：歷史檔之 unresolved／ambiguous 逐檔逐行")
    ap.add_argument("--gate", action="store_true", help="unresolved + ambiguous > 0 時 exit 1")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    rs, refs, n_files = collect(root)

    for code, path in CANONS.items():
        idx = rs.canons[code]
        dup = sorted(s for s, n in idx.sections.items() if n > 1)
        print(f"{code}  {path}")
        print(f"    節號 {len(idx.sections)}，重複 {len(dup)}" + (f" → {dup}" if dup else ""))
        print(f"    具條號索引之節 {len(idx.items)}，R-G 編號（行內提及）{len(idx.rulings)}")
    dup_cross = sorted(set(rs.canons["FO"].sections) & set(rs.canons["IN"].sections))
    print(f"\n兩 canon 共用之節號（裸引用即歧義）{len(dup_cross)} 個：{dup_cross}")

    qualified = [r for r in refs if r.kind != "unqualified"]
    bad_all = [r for r in qualified if r.verdict != "resolved"]

    if args.emit_waiver:
        cache: dict = {}
        seen: set = set()
        rows = []
        for r in bad_all:                       # 同一行同一 target 重複者去重（鍵相同）
            if r.usage == "mention":            # 提及非使用，不入 waiver（27 包 §三）
                continue
            if waiver_key(r) in seen:
                continue
            seen.add(waiver_key(r))
            rows.append((r, waiver_reason(root, r, cache)))
        rows.sort(key=lambda x: (x[0].source, x[0].line, x[0].target))
        body = "\n".join(
            ["\t".join(WAIVER_COLUMNS)]
            + [f"{r.source}\t{r.kind}\t{r.target}\t{r.line_sha8}\t{r.line}\t{reason}"
               for r, reason in rows]
        ) + "\n"
        out = root / args.emit_waiver
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        tally: dict = {}
        for _, reason in rows:
            tally[reason] = tally.get(reason, 0) + 1
        print(f"產出 waiver {args.emit_waiver}：{len(rows)} 列 / "
              f"{len({r.source for r, _ in rows})} 檔")
        for reason, n in sorted(tally.items()):
            print(f"    {reason:<22} {n:>5}")
        print("    ↑ `active-backlog` 為**暫時**豁免（§F-5 待裁），非永久\n")

    waived: dict = {}
    stale: list = []
    if args.waiver:
        wpath = root / args.waiver
        waived = load_waiver(wpath)
        live = {waiver_key(r) for r in bad_all if r.usage == "use"}
        stale = [k for k in waived if k not in live and k[3] != "legacy"]

    mentions = [r for r in qualified if r.verdict != "resolved" and r.usage == "mention"]
    unresolved = [r for r in qualified if r.verdict == "unresolved"
                  and r.usage == "use" and waiver_hit(waived, r) is None]
    ambiguous = [r for r in qualified if r.verdict == "ambiguous"
                 and r.usage == "use" and waiver_hit(waived, r) is None]
    unqualified = [r for r in refs if r.kind == "unqualified"]

    print(f"\n掃描 {n_files} 檔，引用 {len(refs)} 處"
          f"（qualified {len(qualified)}／unqualified {len(unqualified)}）")
    for kind in ("section", "item", "ruling"):
        sub = [r for r in qualified if r.kind == kind]
        print(f"  {kind:<9}{len(sub):>6}   unresolved "
              f"{sum(1 for r in sub if r.verdict == 'unresolved'):>5}   ambiguous "
              f"{sum(1 for r in sub if r.verdict == 'ambiguous'):>5}")
    if args.waiver:
        n_waived = sum(1 for r in bad_all if waiver_hit(waived, r) is not None)
        print(f"\nwaiver {args.waiver}：{len(waived)} 列，本跑命中 {n_waived} 處，"
              f"stale {len(stale)} 列（清單內而現已不存在；只減不增，不 FAIL）")
    print(f"\nunresolved  = {len(unresolved)}   （waiver 外）" if args.waiver
          else f"\nunresolved  = {len(unresolved)}")
    print(f"ambiguous   = {len(ambiguous)}" + ("   （waiver 外）" if args.waiver else ""))
    print(f"mention     = {len(mentions)}   （提及非使用，不計入 FAIL；27 包 §三）")
    print(f"unqualified = {len(unqualified)}   （盲區，不計入 FAIL）")

    if args.report:
        for verdict, group in (("unresolved", unresolved), ("ambiguous", ambiguous)):
            buckets: dict[str, list[Ref]] = defaultdict(list)
            for r in group:
                buckets[f"{r.kind} {r.target}"].append(r)
            print(f"\n--- {verdict}：{len(buckets)} 個 target ---")
            for key, g in sorted(buckets.items(), key=lambda kv: -len(kv[1]))[:args.top]:
                hits = g[0].hits
                print(f"  {len(g):>5}  {key}" + (f"   命中 {list(hits)}" if hits else ""))
                for r in g[:3]:
                    print(f"           {r.source}:{r.line}")
            if len(buckets) > args.top:
                print(f"  … 另 {len(buckets) - args.top} 個 target")

    fail = len(unresolved) + len(ambiguous)
    print(f"\n{'FAIL' if fail else 'PASS'}: unresolved + ambiguous = {fail}")
    return 1 if (args.gate and fail) else 0


if __name__ == "__main__":
    sys.exit(main())
