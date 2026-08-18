"""G113 —— OR 分支涵蓋（R-P161）。

「原文以 `OR` 並列而 TC 只取其一」已重複**七次**
（16 包 `BODY OFF-TIMED`、17 包 `greater`、18 包 `Ignition Pre Off`、22 包四項），
**七次全靠反向涵蓋事後抓到，至今無閘門可攔**。

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
# 分隔符不分大小寫 —— CFTS 原文之連接詞大小寫不一（`While` / `WHEN` / `THEN`）。
# 此為**分隔符層**之處理，R-P161 明許（「`OR` 之大小寫、標點黏連須一併處理」）。
_STOP = r"[.;:]|\b(?:THEN|AND|IF|WHEN|WHILE|UNLESS)\b"
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


KNOWN = [
    ("16 包 `BODY OFF-TIMED`（R-P117(c)）", "b1_before16.json", "SWE-PM-073", "off-tim"),
    ("17 包 `greater` 負分支（A-PW87）", "b1_before17.json", "SWE-PM-073", "greater"),
    ("18 包 `Ignition Pre Off`（A-PW94）", "_batch2_pre043", "SWE-PM-038", "pre"),
    ("22 包 VR 長按（A-PW119）", "_batch3_pre", "SWE-PM-011", "long"),
    ("22 包 Behaviour 1 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-014", "ltm"),
    ("22 包 Behaviour 2 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-014", "ltm"),
    ("22 包 `028` 之 LTM High（A-PW119）", "_batch3_pre", "SWE-PM-028", "ltm"),
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
    """R-P161(d) —— 以七項已知實例為對照，對修補前資料重跑。"""
    print("  G113 驗證條件 —— 七項已知實例之重現\n")
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
    print(f"\n  七項中重現 **{ok} / 7**")
    return 0 if ok else 1


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
