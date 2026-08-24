"""W-VF63 —— pilot #1 v4（V25**改寫後之版本**，2026-08-24 10:27）。

  (1) **四條** tc_title 改純句式（去冒號），依 V25 §2 之逐字表
  (2) `listed`／`displayed` 依 V25 §3 統一為**該 leaf 之條文所用之動詞**
      —— 實測十條之條文皆用 `display`，無一用 `list`，故二處皆 `displayed`
  (3) 十條之 `pre_conditions` 增列 `The HU is in the Full-Operation state`，
      **置於 PROXI 設定之前**（其為狀態，PROXI 為配置）
  (5) 產 `vf230_pilot1_v4.json`，`supersedes: vf230_pilot1_v3.json`

**本檔為 38 輪 W-VF63 之歷史腳本，其輸入 `vf230_pilot1_v3.json` 已於 W-VF68
依 V28 §3（Pei 已允）刪除，故本檔已不可重跑。**其產物 `vf230_pilot1_v4.json`
同輪改名為 `vf230_pilot1.json`（定稿）。保留本檔僅為記錄其修改內容，
不作為可執行之重製路徑 —— **具名此為 R-VS53（產物須可自 driver 重製）之一處斷鏈**。

**不重跑選池、不改 leaf 集合、不改 `specification_reference`、
不改 `reasoning` 之 Priority 段。**

> **本檔取代本層先前之同名腳本** —— 前版係依 V25 之**舊版本**所寫
> （十條全改標題、括號別名移除、`listed` 一律改 `displayed` 而未查條文）。
> 該版本已被改寫，前版之產出作廢。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# V25 §2 之逐字表 —— **只此四條**
TITLES = {
 241: "Suspension Service Mode not displayed when CAN node 27 is Absent",
 244: "Power Tailgate Alert modifiable when CAN node 82 is Present",
 246: "Lane Sense Warning modifiable when Lane_Assist is Active Lane Management",
 247: "Suspension Service Mode modifiable when CAN node 27 is Present",
}
CLAIMED = {241: 11, 244: 10, 246: 11, 247: 10}
FULL_OP = "The HU is in the Full-Operation state"


def main() -> None:
    src = json.loads((ROOT / "generated" / "vf230_pilot1_v3.json")
                     .read_text(encoding="utf-8"))
    delta = []
    for t in src["tcs"]:
        seq = t["seq"]
        # (1) 四條標題
        if seq in TITLES and t["tc_title"] != TITLES[seq]:
            delta.append((seq, "tc_title", t["tc_title"], TITLES[seq]))
            t["tc_title"] = TITLES[seq]
        # (2) 動詞取自條文 —— 十條之條文皆用 display
        before = t["test_procedure"]
        t["test_procedure"] = re.sub(r"\bis not listed\b", "is not displayed",
                                     re.sub(r"\bis listed\b", "is displayed", before))
        if before != t["test_procedure"]:
            delta.append((seq, "test_procedure", "…is (not) listed",
                          "…is (not) displayed"))
        # (3) pre_conditions 增列，置於 PROXI 之前
        lines = [x for x in t["pre_conditions"].split("\n") if x.strip()]
        body = [re.sub(r"^\d+\.\s*", "", x) for x in lines]
        if FULL_OP not in t["pre_conditions"]:
            body = [FULL_OP] + body
            t["pre_conditions"] = "\n".join(f"{i}. {b}" for i, b in enumerate(body, 1))
            delta.append((seq, "pre_conditions", "(1 項)", "(2 項，增 Full-Operation)"))

    src["batch"] = "vf230_pilot1_v4"
    src["supersedes"] = "vf230_pilot1_v3.json"
    src["handoff"] = "docs/handoff/V25_pilot1v3_review.md（改寫後之版本，10:27）"
    src["work_order"] = "W-VF63"
    src["revision"] = ("V25 §2：四條 tc_title 改純句式（去冒號）；"
                       "§3：動詞取自條文（十條皆 display，故 proc 之 listed → "
                       "displayed，ER 已為 displayed 不動）；"
                       "§5：十條 pre_conditions 增列 `The HU is in the "
                       "Full-Operation state`，置於 PROXI 之前。"
                       "**leaf 集合、spec_ref、reasoning 皆未動。**")
    (ROOT / "generated" / "vf230_pilot1_v4.json").write_text(
        json.dumps(src, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"delta {len(delta)} 處")
    for seq, col, a, b in delta:
        print(f"  {seq} {col:16} {a[:44]:46} -> {b[:46]}")
    print("\nV25 §2 之字數複驗（len(split())）：")
    for seq, ti in TITLES.items():
        n = len(ti.split())
        print(f"  {seq}  實測 {n:2}  V25 載 {CLAIMED[seq]:2}  "
              f"{'✅' if n == CLAIMED[seq] else '⚠ 以實測為準'}")


if __name__ == "__main__":
    main()
