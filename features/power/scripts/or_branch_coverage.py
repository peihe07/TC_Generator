"""G113 —— OR 分支涵蓋（R-P161）。

「原文以 `OR` 並列而 TC 只取其一」已重複**五次**（R-P170 訂正 R-P161 之「七次」）
（16 包 `BODY OFF-TIMED`、18 包 `Ignition Pre Off`、22 包 LTM High ×3），
**五次全靠反向涵蓋事後抓到**；第八、第九例（`SWE-PM-014` / `SWE-PM-018`）
則已由本閘於現況資料上前瞻攔下，另計。

本閘之判準：

  （a）自 `source_clause` 抽出 `OR` / `or` / `either … or` / `nor` 之並列結構，
       以其為**分支組**（不限二元，`A OR B OR C` 拆為三支）
  （b）逐支比對該 leaf 之**全部 TC**（分支得由不同 TC 承擔），
       以該支之**獨有實詞**（該支有而其 sibling 支皆無者）為判準
  （c）任一支之獨有實詞未見於任何 TC → 列入輸出，
       **不判 FAIL**，入 R-P76 之待人工裁決類

判準之理由：「只取其一」之特徵，正是**未取之支其獨有詞完全不出現**
（`BODY OFF-TIMED` 之 `off-tim`、`Ignition Pre Off` 之 `pre`）。
獨有詞為空之支不判（二支語詞完全重疊者無從分辨）。

**正規化限於分隔符層**（R-P161）：`minutesOR` 之黏連拆為 `minutes OR`，
大小寫統一供比對。**不擴及語義。**

用法：
    python features/power/scripts/or_branch_coverage.py
    python features/power/scripts/or_branch_coverage.py --self-test
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reverse_coverage import normalize, tc_text, words  # noqa: E402

# 分隔符層之正規化：黏連之 OR / NOR（`minutesOR`、`valueOR`）補回空白。
GLUED_OR_RE = re.compile(r"(?<=[a-z0-9\"'])(OR|NOR)(?=[A-Z(\"' ])")
# 並列連接詞。`nor` 一併納入（R-P161 明列）。
OR_TOKEN_RE = re.compile(r"\b(?:OR|or|NOR|nor)\b")
# 分支之左右邊界：句末標點、分號、冒號、THEN/AND 之大寫連接詞
# 運算元定界之分隔符集合。
#
# **結構性依據（R-P169(a)：須寫成結構性依據，不得以「改後通過」為理由）**：
# `OR` 之兩個運算元為**同一階層之並列成分**，其邊界應由
#   （1）標點（`.` `;` `:`）—— 成分或句子之結束
#   （2）**對等連接詞**（`AND`）與**後件標記**（`THEN`）—— 銜接同階層之另一成分
# 界定。
#
# **`IF` / `WHEN` / `WHILE` / `UNLESS` 為從屬連接詞**（subordinator），
# 其所引之子句**依附於它所修飾的那個成分**，**是該運算元的一部分**，
# 而非把運算元與其 sibling 分開之界線。
# `… "Active" (If LTM High is present: "Timeout1" = "00 minutes")` 即為適例 ——
# 括號內之 `If` 子句限定 `"Active"` 這一支，屬該支之內容。
# **將從屬連接詞當作對等成分之邊界，會把運算元截斷於其自身之限定語之前**，
# 此為分詞器之錯誤分類，非門檻或判準問題（R-P169 之判別）。
#
# 故自邊界集合移除 `IF` / `WHEN` / `WHILE` / `UNLESS`，保留標點與 `AND` / `THEN`。
# **OR 之辨識規則（`OR_TOKEN_RE`）未動**（R-P169(c)）。
# **標點須為句讀而非識別子之一部分**（同屬 R-P169 之分詞器錯誤分類）：
# `Auto_SwitchOn_Setting.Req` / `Phone_Call.Info` 之 `.` **夾在字元之間，
# 是識別子之組成**，非成分邊界；句讀之 `.` 後必接空白或字串結尾。
# 故標點僅在其後為空白或結尾時方視為分隔符。
_STOP = r"[.;:](?=\s|$)|\b(?:THEN|AND)\b"
LEFT_STOP_RE = re.compile(_STOP, re.I)
RIGHT_STOP_RE = re.compile(_STOP, re.I)
MIN_BRANCH_WORDS = 2


def prepare(text: str) -> str:
    """換行視為句界 —— 錨點原文之段落間常無句末標點（`… still active` 直接換行）。
    此亦為分隔符層之處理。"""
    return GLUED_OR_RE.sub(r" \1 ", normalize(text.replace("\n", ". ")))


def _trim_left(seg: str) -> str:
    """左運算元：取其最後一個分隔符之後之尾段。"""
    last = None
    for m in LEFT_STOP_RE.finditer(seg):
        last = m
    return (seg[last.end():] if last else seg).strip(" ,()\"'")


def _trim_right(seg: str) -> str:
    """右運算元：取其第一個分隔符之前之首段。"""
    m = RIGHT_STOP_RE.search(seg)
    return (seg[:m.start()] if m else seg).strip(" ,()\"'")


def or_groups(clause: str) -> list[list[str]]:
    """回傳分支組清單；每組為 ≥2 支之字串。

    實作註：初版以「自 OR 位置向左反轉搜尋分隔符」定界，
    **反轉字串配上正向之詞邊界樣式（`THEN` / `AND`）永不匹配**，
    致左界一路退到句首，七項已知實例全數未重現（0 / 7）。
    此為**實作瑕疵，非判準問題** —— 判準（OR 並列 ＋ 獨有實詞）一字未改。
    現版改為正向掃描取「最後一個分隔符之後」。見上繳 §一。
    """
    groups = []
    for sentence in re.split(r"(?<=[.;])\s+", prepare(clause)):
        hits = list(OR_TOKEN_RE.finditer(sentence))
        if not hits:
            continue
        segs, prev = [], 0
        for m in hits:
            segs.append(sentence[prev:m.start()])
            prev = m.end()
        segs.append(sentence[prev:])
        # 連續之 OR（其間之區段無分隔符）視為同一組：A OR B OR C
        group, i = [_trim_left(segs[0])], 0
        for i in range(1, len(segs)):
            mid = segs[i]
            right = _trim_right(mid)
            group.append(right)
            if i < len(segs) - 1 and LEFT_STOP_RE.search(mid):
                # 該區段內有分隔符 —— 本組到此為止，另起一組
                parts = [p for p in group if len(p.split()) >= MIN_BRANCH_WORDS]
                if len(parts) >= 2:
                    groups.append(parts)
                group = [_trim_left(mid)]
        parts = [p for p in group if len(p.split()) >= MIN_BRANCH_WORDS]
        if len(parts) >= 2:
            groups.append(parts)
    return groups


def analyse(batch: dict) -> dict:
    by_leaf: dict[str, list[dict]] = {}
    for tc in batch.get("tcs", []):
        by_leaf.setdefault(tc["req_id"], []).append(tc)
    out = {}
    for leaf in batch.get("leaves", []):
        parent = leaf["parent"]
        tcs = by_leaf.get(parent, [])
        tc_words: set[str] = set()
        for tc in tcs:
            tc_words |= words(tc_text(tc))
        rows = []
        for gi, group in enumerate(or_groups(str(leaf.get("source_clause", ""))), 1):
            wsets = [words(p) for p in group]
            for bi, (part, w) in enumerate(zip(group, wsets), 1):
                others: set[str] = set()
                for j, other in enumerate(wsets):
                    if j != bi - 1:
                        others |= other
                distinctive = w - others
                if not distinctive:
                    rows.append({"group": gi, "branch": bi, "text": part,
                                 "distinctive": [], "missing": [],
                                 "verdict": "無獨有實詞 —— 不判"})
                    continue
                missing = sorted(distinctive - tc_words)
                rows.append({"group": gi, "branch": bi, "text": part,
                             "distinctive": sorted(distinctive), "missing": missing,
                             # 全部獨有詞皆缺 → 未覆蓋；部分缺 → 部分未覆蓋。
                             # **二者皆入待人工裁決**（R-P161(c)）。
                             "verdict": "**未覆蓋**" if missing == sorted(distinctive)
                                        else ("**部分未覆蓋**" if missing else "已覆蓋")})
        out[parent] = rows
    return out


def uncovered(res: dict) -> list[tuple[str, dict]]:
    return [(lf, r) for lf, rows in res.items() for r in rows
            if r["verdict"].endswith("未覆蓋**")]


def render(res: dict, label: str) -> str:
    out = [f"\n## {label}\n"]
    tot = und = 0
    for lf, rows in res.items():
        if not rows:
            continue
        tot += len(rows)
        und += sum(1 for r in rows if r["verdict"].endswith("未覆蓋**"))
        out.append(f"\n### `{lf}` —— 分支 {len(rows)}\n\n"
                   "| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |\n"
                   "|---|---|---|---|---|---|\n")
        for r in rows:
            out.append(f"| {r['group']} | {r['branch']} | {r['text'][:56]} | "
                       f"{'、'.join('`'+w+'`' for w in r['distinctive'][:6]) or '—'} | "
                       f"{'、'.join('`'+w+'`' for w in r['missing'][:6]) or '—'} | "
                       f"{r['verdict']} |\n")
    out.append(f"\n**合計分支 {tot}，未覆蓋 **{und}**。**\n")
    return "".join(out)


# **G113 之驗證條件 —— 五項 OR 結構實例**（R-P170 訂正）。
#
# R-P161 原稱「已重複七次」，為錯誤歸納：下列 NOT_OR 之二項**根本不是 OR 結構**，
# 不應由本閘捕獲，卻被寫入驗證條件，致驗證條件本身建立於錯誤前提上。
KNOWN = [
    ("16 包 `BODY OFF-TIMED`（R-P117(c)）", "b1_before16.json", "SWE-PM-073", "off-tim"),
    ("18 包 `Ignition Pre Off`（A-PW94）", "_batch2_pre043", "SWE-PM-038", "pre"),
    ("22 包 Behaviour 1 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-014", "ltm"),
    ("22 包 Behaviour 2 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-014", "ltm"),
    ("22 包 `028` 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-028", "ltm"),
]

# **未機械化之缺陷類**（R-P170）—— 不併入 G113，其捕獲仍賴反向涵蓋與人讀。
# 二者之原文皆無並列連接詞 `OR`／`nor`，故本閘之辨識規則（OR_TOKEN_RE）
# 依定義不可能命中；欲令其命中只能擴張辨識規則，而 R-P169(c) 明禁。
NOT_OR = [
    ("17 包 `greater` 負分支（A-PW87）", "條件並列",
     '`and if the volume was greater …` —— 從屬條件句，非並列運算元'),
    ("22 包 VR 長按（A-PW119）", "操作變體",
     '`both short and long presses` —— `both … and` 之對等並列，非選言'),
]

# **前瞻捕獲**（R-P170）—— 由閘門於現況資料上攔下，非事後補救；另計，不入驗證條件。
FORWARD = [
    ("`SWE-PM-014`", "4941504", "`Ignition Pre Off` OR `Ignition Off`"),
    ("`SWE-PM-018`", "4941548", "`Ignition Pre Off` OR `Ignition Off`"),
]


def _reconstruct(kind: str) -> dict:
    """18 / 22 包無快照 —— 自現況移除當時所補之 TC 以重建修補前資料。
    被移除者以 `reasoning_note` 內之裁決標記辨識，非憑印象挑選。"""
    if kind == "_batch2_pre043":
        b = json.loads((GENERATED / "batch_002_timeout_settings.json")
                       .read_text(encoding="utf-8"))
        b["tcs"] = [t for t in b["tcs"]
                    if "R-P118 反向涵蓋盲測" not in str(t.get("reasoning_note", ""))]
        return b
    b = json.loads((GENERATED / "batch_003_power_state_a.json").read_text(encoding="utf-8"))
    b["tcs"] = [t for t in b["tcs"]
                if "R-P118(d) 反向涵蓋裁決" not in str(t.get("reasoning_note", ""))]
    return b


def self_test() -> int:
    """R-P170 訂正後之驗證條件 —— **五項 OR 結構實例全數重現**。"""
    print("  G113 驗證條件（R-P170 訂正後）—— 五項 OR 結構實例之重現\n")
    cache: dict[str, dict] = {}
    ok = 0
    for label, src, leaf, marker in KNOWN:
        if src not in cache:
            cache[src] = (_reconstruct(src) if src.startswith("_")
                          else json.loads((DATA / src).read_text(encoding="utf-8")))
        res = analyse(cache[src])
        hit = [r for r in res.get(leaf, [])
               if r["verdict"].endswith("未覆蓋**")
               and any(marker in w for w in r["missing"])]
        ok += bool(hit)
        print(f"  [{'重現' if hit else '**未重現**'}] {label}")
        if hit:
            print(f"          分支「{hit[0]['text'][:64]}」 缺 {hit[0]['missing'][:5]}")
    print(f"\n  五項中重現 **{ok} / {len(KNOWN)}**"
          f"{'' if ok == len(KNOWN) else '  —— **未達 R-P174(a) 之啟動條件**'}")

    print("\n  未機械化之缺陷類（R-P170，不併入 G113、不計入驗證條件）：")
    for label, kind, why in NOT_OR:
        print(f"    - {label}：{kind} —— {why}")
    print("\n  前瞻捕獲（另計）：")
    for leaf, anchor, text in FORWARD:
        print(f"    - {leaf} 錨點 {anchor}：{text}")
    return 0 if ok == len(KNOWN) else 1


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    batches = [json.loads(p.read_text(encoding="utf-8"))
               for p in sorted(GENERATED.glob("*.json"))]
    lines = ["# G113 —— OR 分支涵蓋（R-P161）\n",
             "\n> **不判 FAIL**：未覆蓋之分支入 R-P76 之待人工裁決類，逐支裁決三選一。\n",
             "> 正規化限於分隔符層（黏連之 `OR` 補回空白、大小寫統一），**不擴及語義**。\n"]
    total = 0
    for b in batches:
        res = analyse(b)
        total += len(uncovered(res))
        lines.append(render(res, f"批次 `{b.get('batch', '?')}`"))
    (DATA / "g113_or_branch.md").write_text("".join(lines), encoding="utf-8")
    print(f"wrote {(DATA / 'g113_or_branch.md').relative_to(ROOT)}")
    for b in batches:
        res = analyse(b)
        u = uncovered(res)
        print(f"  {b.get('batch','?')}: 未覆蓋分支 {len(u)}")
        for lf, r in u:
            print(f"     {lf} 組{r['group']}支{r['branch']} 缺{r['missing'][:4]} | {r['text'][:60]}")
    print(f"\nG113 未覆蓋分支合計 {total}（不判 FAIL，待人工裁決）")


if __name__ == "__main__":
    main()
