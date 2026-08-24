"""W-VF63 —— pilot #1 v4（V25 §6）。**兩項字串取代，無判斷餘地。**

  §6.1  `tc_title` 十條全改，依 **R-VF70**：純句式、無冒號、括號別名不入標題、
        正負向句式固定（正向用 `modifiable`，非 `can be modified`）
  §6.2  procedure 之 `is listed`／`is not listed` → `is displayed`／
        `is not displayed`，依 **R-VF71 一**（動詞取自條文）。**ER 不動。**

**不重跑選池、不改 leaf 集合、不改 `specification_reference`、
不改 `reasoning`。** 自 v3 逐欄複製，只改上列二處。

字數以 `len(title.split())` 計（R-VF71 二）；與 V25 §6.1 之表不符者
**以實測為準並回報**（該條末句）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# R-VF70 三之句式；別名已自標題移除（保留於其餘欄位）
TITLES = {
 238: 'Power Tailgate Alert is not displayed when CAN node 82 is "Absent"',
 239: 'Blind Spot Alert is not displayed when Blind_Spot_Monitoring is "Absent"',
 240: 'Lane Sense Warning is not displayed when Lane_Assist is "Not Present"',
 241: 'Suspension Service Mode is not displayed when CAN node 27 is "Absent"',
 242: 'Blind Spot with Trailer Detection is not displayed when '
      'Blindspot_Trailer_Detection is "Absent"',
 243: 'Park Sense is not displayed when CAN Node 24 is "Absent"',
 244: 'Power Tailgate Alert is displayed and modifiable when CAN node 82 is "Present"',
 245: 'Blind Spot Alert is displayed and modifiable when Blind_Spot_Monitoring '
      'is "Present"',
 246: 'Lane Sense Warning is displayed and modifiable when Lane_Assist is '
      '"Active Lane Management"',
 247: 'Suspension Service Mode is displayed and modifiable when CAN node 27 is '
      '"Present"',
}
CLAIMED = {238: 12, 239: 11, 240: 11, 241: 12, 242: 12,
           243: 11, 244: 13, 245: 12, 246: 13, 247: 13}


def main() -> None:
    src = json.loads((ROOT / "generated" / "vf230_pilot1_v3.json")
                     .read_text(encoding="utf-8"))
    delta = []
    for t in src["tcs"]:
        seq = t["seq"]
        old_title = t["tc_title"]
        t["tc_title"] = TITLES[seq]
        if old_title != TITLES[seq]:
            delta.append((seq, "tc_title"))
        # §6.2：只改 procedure，ER 不動
        before = t["test_procedure"]
        t["test_procedure"] = re.sub(r"\bis not listed\b", "is not displayed",
                                     re.sub(r"\bis listed\b", "is displayed",
                                            t["test_procedure"]))
        if before != t["test_procedure"]:
            delta.append((seq, "test_procedure"))

    src["batch"] = "vf230_pilot1_v4"
    src["supersedes"] = "vf230_pilot1_v3.json"
    src["handoff"] = "docs/handoff/V25_pilot1v3_review.md"
    src["work_order"] = "W-VF63"
    src["revision"] = ("V25 §6：`tc_title` 依 R-VF70 全改（純句式、無冒號、"
                       "括號別名不入標題）；procedure 之 `listed` → `displayed` "
                       "依 R-VF71 一。**ER、reasoning、spec_ref、leaf 集合皆未動。**")
    (ROOT / "generated" / "vf230_pilot1_v4.json").write_text(
        json.dumps(src, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"寫入 vf230_pilot1_v4.json；delta {len(delta)} 處")
    print(f"{'seq':>4} {'字':>3} {'V25 載':>6}  判")
    bad = []
    for seq, ti in TITLES.items():
        n = len(ti.split())
        ok = n == CLAIMED[seq]
        if not ok:
            bad.append((seq, CLAIMED[seq], n))
        print(f"{seq:4} {n:3} {CLAIMED[seq]:6}  {'✅' if ok else '⚠ 以實測為準'}")
    print(f"\n與 V25 §6.1 不符 {len(bad)} 項：{bad}")
    print(f"逾 14 字者：{[s for s, ti in TITLES.items() if len(ti.split()) > 14]}")


if __name__ == "__main__":
    main()
