"""G202 —— 三欄全同而 `expected_result` 相異之偵測（R-P288）。

42 §八第 2 項：「無對應」中有數條之相異行為空 —— 其差異全在 `expected_result`。

**R-P288 之裁定**：`axis` 之本義為「二條藉何者**區分**」；
若二條之三欄全同而僅 ER 相異，則**依其內文執行，二條之操作完全相同** ——
此即 R-P257 所處置之 `SWE-PM-025` 形態（內文未寫入其宣稱之區分）。

**與既有二閘之關係**：

| 閘 | 判準 | 抓到之形態 |
|---|---|---|
| G178 | **四欄**逐字全同 | 內文與結果皆同 → 真重複或內文未寫入區分 |
| **G202** | **三欄**全同而 **ER 相異** | **操作相同而觀察不同** → 應合為一條多 ER，或內文漏寫其區分 |
| G168 C5 | `delta` 逐字相同 | 描述欄未區分（文件缺陷） |

**G178 抓不到本形態** —— 其要求 ER 亦相同。

用法：
    python features/power/scripts/verify_er_only_distinct.py
    python features/power/scripts/verify_er_only_distinct.py --self-test
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

THREE = ("pre_conditions", "input_test_data", "test_procedure")
BASE = re.compile(r"(SWE-PM-\d+)")


def three_sig(tc: dict) -> tuple[str, ...]:
    """三欄之逐字簽章。**不正規化空白** —— 逐字即逐字。"""
    return tuple(str(tc.get(f, "")) for f in THREE)


def run(tcs: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        groups[three_sig(t)].append(t)
    out = []
    for sig, group in groups.items():
        if len(group) < 2:
            continue
        ers = {str(t.get("expected_result", "")) for t in group}
        if len(ers) < 2:
            continue                      # ER 亦同 → 屬 G178 之範圍，本閘不重複報
        out.append({
            "tcs": [t["tc_id"] for t in group],
            "leaves": sorted({BASE.match(t["req_id"]).group(1) for t in group}),
            "same_leaf": len({BASE.match(t["req_id"]).group(1) for t in group}) == 1,
            "n_er": len(ers),
        })
    return out


def self_test() -> int:
    """R-P288 —— fixture 證明本閘會 FAIL。fixture 自撰，不取自本語料。"""
    failures = 0

    def tc(tid: str, proc: str, er: str, req: str = "SWE-PM-900") -> dict:
        return {"tc_id": tid, "req_id": req, "tc_title": tid,
                "pre_conditions": "1. The rig is powered",
                "input_test_data": "NA", "test_procedure": proc,
                "expected_result": er}

    def case(label: str, tcs: list[dict], want: int) -> None:
        nonlocal failures
        r = run(tcs)
        ok = len(r) == want
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G202 {label}")
        print(f"          期望 {want} 組；實測 {len(r)} 組")

    case("應 PASS —— 三欄相異", [tc("X-1", "1. Press A", "1. A responds"),
                                 tc("X-2", "1. Press B", "1. B responds")], 0)
    case("應 FAIL —— 三欄全同而 ER 相異（本閘之標的）",
         [tc("X-1", "1. Press A", "1. The count matches"),
          tc("X-2", "1. Press A", "1. Every item is processed")], 1)
    case("應 PASS —— 三欄全同且 ER 亦同（屬 G178 之範圍，本閘不重複報）",
         [tc("X-1", "1. Press A", "1. Same"), tc("X-2", "1. Press A", "1. Same")], 0)
    case("應 FAIL —— **跨 leaf** 之三欄全同而 ER 相異",
         [tc("X-1", "1. Press A", "1. Outcome one", "SWE-PM-900"),
          tc("X-2", "1. Press A", "1. Outcome two", "SWE-PM-901")], 1)
    case("應 PASS —— 僅差一個空白（逐字比對，不正規化）",
         [tc("X-1", "1. Press A", "1. Outcome one"),
          tc("X-2", "1. Press  A", "1. Outcome two")], 0)
    print(f"\n  G202 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    r = run(tcs)

    out = ["# G202 —— 三欄全同而 `expected_result` 相異（R-P288）\n",
           "\n> 判準：`pre_conditions` / `input_test_data` / `test_procedure` "
           "**三欄逐字全同**而 `expected_result` **相異**。\n",
           "> **G178 抓不到本形態**（其要求 ER 亦相同）。\n",
           "> 其意義：**依內文執行，二條之操作完全相同，而所觀察者不同** ——\n",
           "> 或應合為一條多 ER（§5.7），或內文漏寫其區分（R-P257 之形態）。\n",
           f"\n## 實測 —— **{len(r)}** 組（{sum(len(x['tcs']) for x in r)} 條）\n\n"
           "| TC | leaf | 同 leaf | 相異之 ER 數 |\n|---|---|---|---|\n"]
    for x in sorted(r, key=lambda y: y["tcs"]):
        out.append(f"| {'、'.join('`…-' + i[-3:] + '`' for i in x['tcs'])} | "
                   f"{'、'.join('`' + l + '`' for l in x['leaves'])} | "
                   f"{'是' if x['same_leaf'] else '**否**'} | {x['n_er']} |\n")
    if not r:
        out.append("| （無） | | | |\n")

    r2 = run_actual(tcs)
    out.append(f"\n## 二、實際形態之補量 —— **{len(r2)}** 組"
               f"（{sum(len(x['tcs']) for x in r2)} 條）\n\n"
               "> R-P288 將該形態表述為「三欄全同而 ER 相異」，全批實測為 **0 組**。\n"
               "> 逐對實讀後其**實際形態**為：`pre_conditions` / `input_test_data` 全同，\n"
               "> `test_procedure` 之**施加步驟**逐字相同，僅**觀察步驟**與 ER 相異 ——\n"
               "> 即「依內文執行，二條之**施測操作**完全相同，只是讀不同的東西」。\n\n"
               "| TC | leaf | 同 leaf |\n|---|---|---|\n")
    for x in sorted(r2, key=lambda y: y["tcs"]):
        out.append(f"| {'、'.join('`…-' + i[-3:] + '`' for i in x['tcs'])} | "
                   f"{'、'.join('`' + l + '`' for l in x['leaves'])} | "
                   f"{'是' if x['same_leaf'] else '**否**'} |\n")

    p = DATA / "g202_er_only_distinct.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"G202（條文判準：三欄全同）：{len(r)} 組")
    print(f"G202 補量（實際形態：施加相同、觀察與 ER 相異）："
          f"**{len(r2)} 組（{sum(len(x['tcs']) for x in r2)} 條）**")
    for x in sorted(r2, key=lambda y: y["tcs"]):
        print(f"   {[i[-3:] for i in x['tcs']]}  {x['leaves']}")
    for x in sorted(r, key=lambda y: y["tcs"]):
        print(f"   {[i[-3:] for i in x['tcs']]}  {x['leaves']}  同leaf={x['same_leaf']}")
    raise SystemExit(1 if r else 0)


# ── 實際形態之補量（43 包）──
#
# R-P288 將該形態表述為「三欄全同而 ER 相異」，而全批實測為 **0 組**。
# 逐對實讀後，其**實際形態**為：
#   **`pre_conditions` / `input_test_data` 全同，`test_procedure` 之
#     「施加步驟」逐字相同，僅「觀察步驟」與 `expected_result` 相異。**
# 即「依內文執行，二條之**施測操作**完全相同，只是讀不同的東西」——
# 此正為 R-P288 所慮者，惟其判準之表述須修正方能命中。
ACT_FIELDS = ("pre_conditions", "input_test_data")


def act_sig(tc: dict) -> tuple:
    """施加簽章＝前二欄 ＋ `test_procedure` 之**非觀察步驟**。"""
    import re as _re
    obs = _re.compile(r"^\s*\d+\.\s*(?:Read|Check|Observe|Verify|Confirm)\b", _re.I)
    acts = tuple(x.strip() for x in str(tc.get("test_procedure", "")).split("\n")
                 if x.strip() and not obs.search(x))
    return tuple(str(tc.get(f, "")) for f in ACT_FIELDS) + acts


def run_actual(tcs: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        groups[act_sig(t)].append(t)
    out = []
    for _, group in groups.items():
        if len(group) < 2:
            continue
        if len({str(t.get("expected_result", "")) for t in group}) < 2:
            continue
        out.append({"tcs": [t["tc_id"] for t in group],
                    "leaves": sorted({BASE.match(t["req_id"]).group(1) for t in group}),
                    "same_leaf": len({BASE.match(t["req_id"]).group(1)
                                      for t in group}) == 1})
    return out


if __name__ == "__main__":
    main()
