"""B1 —— `test_item` 全批重寫（R-P343 / R-P344 / R-P336 / R-P333）。

形式（R-P333）：

    <規格原句>
    <空行>
    (<操作> -> <預期結果>)

首段（R-P343）：**該 TC 所直接驗證之錨點之文字，逐字**，不切句、不省略、不重組。
歸屬取自 `data/anchor_attribution_53.json`（`propose_anchor_53.py` 所提案）。
**不加前綴**（R-P336）—— Comfort 之前綴係其規格原句自帶，Power 之 CFTS 本文無之。

逾 **1,000 字元**之錨點（R-P343(c)）：取對應該 TC 之**連續片段**，
以**段落**為窗（`anchor_bodies()` 之分段即原文之分段），
並將起訖字元位置寫入 `reasoning_note`。**1,000 為分界，非品質門檻。**
`4941453` 之表格依 R-P344 照原分隔逐字取，**不加 `=`、不加 `,`、不重排欄序**。

後段：`(<操作> -> <預期結果>)`，英文、一行、無句末句點（R-P333(c)）。
操作取 `test_procedure` 之末步（去序號與其 `to check …` 查核子句），
預期結果取 `expected_result` 之末行（去序號）。
**Comfort 實測**：465/465 以 `(` 起 `)` 止、461/465 含 ` -> `、0 筆含換行、
0 筆末句點、**465/465 之操作段首字為小寫** —— 末項依樣採用。

用法：
    python features/power/scripts/build_test_item_53.py --dry-run
    python features/power/scripts/build_test_item_53.py --apply
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402
from propose_anchor_53 import words  # noqa: E402

FRAGMENT_ABOVE = 1000          # R-P343(c) 之分界，非 FAIL 判準
CHECK_CLAUSE = re.compile(r"\s+(?:to check|and check|to verify)\b.*$", re.I)


def fragment(paras: list[str], tc: dict) -> tuple[str, int, int]:
    """自段落序列取對應該 TC 之連續窗；回傳（片段、起、訖）字元位置。"""
    target = words(" ".join((tc.get("tc_title", ""), tc.get("expected_result", ""),
                             tc.get("test_procedure", ""),
                             str(tc.get("split_reason", "")))))
    offs, pos = [], 0
    for p in paras:                       # 段落於串接體中之字元起點
        offs.append(pos)
        pos += len(p) + 1                 # +1 為分隔之換行
    best = (None, -1.0)
    for i in range(len(paras)):
        for w in range(1, 10):
            if i + w > len(paras):
                break
            seg = "\n".join(paras[i:i + w])
            cw = words(seg)
            if not cw:
                continue
            inter = len(cw & target)
            if not inter:
                continue
            rec, pre = inter / max(len(target), 1), inter / len(cw)
            f1 = 2 * rec * pre / (rec + pre)
            if f1 > best[1]:
                best = ((i, w, seg), f1)
    if best[0] is None:
        return "\n".join(paras), 0, len("\n".join(paras))
    i, w, seg = best[0]
    return seg, offs[i], offs[i] + len(seg)


def second_segment(tc: dict) -> str:
    proc = [l for l in str(tc.get("test_procedure", "")).split("\n") if l.strip()]
    er = [l for l in str(tc.get("expected_result", "")).split("\n") if l.strip()]
    act = re.sub(r"^\s*\d+\.\s*", "", proc[-1]).strip() if proc else ""
    act = CHECK_CLAUSE.sub("", act).strip().rstrip(".")
    exp = re.sub(r"^\s*\d+\.\s*", "", er[-1]).strip().rstrip(".") if er else ""
    act = " ".join(act.split())
    exp = " ".join(exp.split())
    # Comfort 實測 465 / 465 之操作段首字皆小寫；依樣採用（R-P333 未定，取實測）。
    # 專有識別字（`TLM`／`$Telematic_Power$` 等全大寫或含 `_`/`$` 者）不動。
    head = act.split(" ", 1)[0] if act else ""
    if head and head[0].isupper() and head.isalpha() and not head.isupper():
        act = act[0].lower() + act[1:]
    return f"({act} -> {exp})"


def main() -> int:
    apply = "--apply" in sys.argv
    bodies = anchor_bodies()
    attr = {r["tc_id"]: r for r in
            json.loads((DATA / "anchor_attribution_53.json").read_text(encoding="utf-8"))}
    frag_n = 0
    for f in sorted(GENERATED.glob("batch_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for tc in d["tcs"]:
            a = attr[tc["tc_id"]]["anchor"]
            paras = bodies.get(a, [])
            full = "\n".join(paras)
            note = ""
            if len(full) > FRAGMENT_ABOVE:
                first, lo, hi = fragment(paras, tc)
                frag_n += 1
                note = (f"**首段取自錨點 `{a}` 之連續片段**（R-P343(c)）——"
                        f"該錨點 {len(full)} 字元逾 1,000；片段起訖字元位置 {lo}–{hi}。")
            else:
                first = full
            item = f"{first}\n\n{second_segment(tc)}"
            if apply:
                tc["test_item"] = item
                if note:
                    rn = str(tc.get("reasoning_note", "") or "")
                    tc["reasoning_note"] = (rn + "\n\n" + note).strip() if rn else note
        if apply:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n",
                         encoding="utf-8")
    print(f"取連續片段者：{frag_n}")
    print("已寫入" if apply else "（--dry-run，未寫入）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
