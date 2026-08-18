"""G178 —— 四欄逐字全同而 `tc_title` 相異之偵測（R-P257）。

36 §B2 之發現：`SWE-PM-025` 之 `…-087` ≡ `…-091`、`…-088` ≡ `…-092` ——
`pre_conditions` / `input_test_data` / `test_procedure` / `expected_result`
**逐字全同**，而 `tc_title` 分載二個不同觸發訊號。
**依現行內文執行，二條之操作完全相同** —— 此為
「TC 內文未實現其宣稱之區分」。

**G168 之 C5 抓不到此形態** —— C5 只比 `distinguishing_axis.delta`。
本閘補之，且判準與 C5 互補：

  C5   `delta` 相同而內文不同  → 描述欄未區分（文件缺陷）
  G178 內文相同而 `tc_title` 不同 → **內文未區分（事實缺陷）**

後者較前者嚴重：前者只是描述不精確，後者使二條 TC 實際上測同一件事。

**掃描範圍為全批，非僅同一 leaf** —— `…-087` 與 `…-091` 恰同 leaf，
惟跨 leaf 之同型重複同樣使其一為冗餘，故不設 leaf 限制。

用法：
    python features/power/scripts/verify_content_distinct.py
    python features/power/scripts/verify_content_distinct.py --self-test
"""

from __future__ import annotations

import collections
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

BODY = ("pre_conditions", "input_test_data", "test_procedure", "expected_result")


def body_sig(tc: dict) -> tuple[str, ...]:
    """四欄之逐字簽章。**不正規化空白** —— 逐字即逐字。"""
    return tuple(str(tc.get(f, "")) for f in BODY)


def run(tcs: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        groups[body_sig(t)].append(t)
    out = []
    for sig, group in groups.items():
        if len(group) < 2:
            continue
        titles = {t["tc_title"] for t in group}
        out.append({
            "tcs": [t["tc_id"] for t in group],
            "titles": sorted(titles),
            "title_differs": len(titles) > 1,
            "same_leaf": len({t["req_id"] for t in group}) == 1,
        })
    return out


def self_test() -> int:
    """R-P257 —— fixture 證明本閘會 FAIL。fixture 自撰，不取自本語料。"""
    failures = 0

    def tc(tid: str, title: str, proc: str, req: str = "SWE-PM-900") -> dict:
        return {"tc_id": tid, "req_id": req, "tc_title": title,
                "pre_conditions": "1. The rig is powered",
                "input_test_data": "NA", "test_procedure": proc,
                "expected_result": "1. The unit responds"}

    def case(label: str, tcs: list[dict], want_n: int, want_diff: bool | None) -> None:
        nonlocal failures
        r = run(tcs)
        ok = len(r) == want_n and (want_diff is None
                                   or (r and r[0]["title_differs"] == want_diff))
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G178 {label}")
        print(f"          期望 {want_n} 組 / title_differs={want_diff}；"
              f"實測 {len(r)} 組"
              + (f" / title_differs={r[0]['title_differs']}" if r else ""))

    case("應 PASS —— 內文相異", [tc("X-1", "A", "1. Press A"),
                                 tc("X-2", "B", "1. Press B")], 0, None)
    case("應 FAIL —— 內文全同而 title 相異（`087`/`091` 之形態）",
         [tc("X-1", "Accept via A", "1. Accept the popup"),
          tc("X-2", "Accept via B", "1. Accept the popup")], 1, True)
    case("應觸發 —— 內文全同且 title 亦同（真重複）",
         [tc("X-1", "same", "1. Accept the popup"),
          tc("X-2", "same", "1. Accept the popup")], 1, False)
    case("應 FAIL —— **跨 leaf** 之內文全同",
         [tc("X-1", "Accept via A", "1. Accept the popup", "SWE-PM-900"),
          tc("X-2", "Accept via B", "1. Accept the popup", "SWE-PM-901")], 1, True)
    case("應 PASS —— 僅差一個空白（逐字比對，不正規化）",
         [tc("X-1", "A", "1. Accept the popup"),
          tc("X-2", "B", "1. Accept  the popup")], 0, None)
    print(f"\n  G178 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    r = run(tcs)
    diff = [x for x in r if x["title_differs"]]
    same = [x for x in r if not x["title_differs"]]

    out = ["# G178 —— 四欄逐字全同之偵測（R-P257）\n",
           "\n> 判準：`pre_conditions` / `input_test_data` / `test_procedure` /\n",
           "> `expected_result` **四欄逐字全同**（不正規化空白）。\n",
           "> **與 G168 之 C5 互補**：C5 為「`delta` 同而內文異」（文件缺陷）；\n",
           "> 本閘為「內文同而 `tc_title` 異」（**事實缺陷** —— 二條實測同一件事）。\n",
           "> 掃描範圍為**全批**，不限同一 leaf。\n",
           f"\n## 一、實測（{len(tcs)} 條）\n\n| 項 | 組數 |\n|---|---|\n",
           f"| 內文全同而 `tc_title` **相異** | **{len(diff)}** |\n",
           f"| 內文全同且 `tc_title` 亦同（真重複） | **{len(same)}** |\n"]
    if r:
        out.append("\n## 二、逐組\n\n| TC | 同 leaf | `tc_title` |\n|---|---|---|\n")
        for x in r:
            out.append(f"| {'、'.join('`…-' + i[-3:] + '`' for i in x['tcs'])} | "
                       f"{'是' if x['same_leaf'] else '**否**'} | "
                       f"{'<br>'.join(x['titles'])} |\n")
    else:
        out.append("\n**全批無命中。**\n")

    p = DATA / "g178_content_distinct.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"G178：內文全同而 title 相異 {len(diff)} 組；title 亦同 {len(same)} 組")
    for x in r:
        print(f"   {[i[-3:] for i in x['tcs']]}  同leaf={x['same_leaf']}  {x['titles']}")
    raise SystemExit(1 if r else 0)


if __name__ == "__main__":
    main()
