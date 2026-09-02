#!/usr/bin/env python3
"""VS-SL-06 §2 —— TC ID 與 TestRail 對照表（R-G42）。

**先量再斷**。實測結果使賦號無法逕行，兩處依包內 §2-4「停下來報，不硬套」：

  阻斷 1  `feature.yaml` 之 `delivery.tc_id_abbr` **全庫無任一 feature 宣告**
          （vehicle_setting／bed_lowering／vehicle_category／ics_management／sw_update 皆無
          `delivery:` 區塊）。R-G42 二令 F 欄為 `NR1L-{ABBR}-{nnn}` 且
          ABBR 須等於該鍵；未宣告者 `lint_delivery_spec` 判紅。
          **本層不自訂 ABBR**（自訂即造規），vf230 之 438 列記 `BLOCKED`。

  阻斷 2  BL／VC 之 F 欄已有號，惟前綴為 **`newR1L-`**（如 `newR1L-BLM-001`），
          不合 R-G42 之 `NR1L-`（現行 `delivered/` 之 ICS 為 `NR1L-ICS-001`）。
          包內令「F 欄已有者不改號」，故記 `kept` 並於 `note` 具名其不合形制。

`status`：`kept`／`assigned`／`RETIRED`／**`BLOCKED`**（本層新增之值，供上述阻斷 1）。
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402

ROOT = v1.ROOT
COLS = ["row", "req_id", "old_E", "old_F", "new_F", "status", "note"]

BOOKS = {
    "vehicle_setting": ("features/vehicle_setting/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_"
                        "SWQT STLA Test Case Specification & Result_SWQT_VF230_20260902.xlsx",
                        "features/vehicle_setting/reports/testrail_id_map_vehicle_setting.tsv"),
    "bed_lowering": ("features/bed_lowering/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_"
                     "SWQT STLA Test Case Specification & Result_SWQT_BedLowering_20260902.xlsx",
                     "features/bed_lowering/reports/testrail_id_map_bed_lowering.tsv"),
    "vehicle_category": ("features/vehicle_category/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_"
                         "SWQT STLA Test Case Specification & Result_SWQT_VehicleCategory_20260902_working.xlsx",
                         "features/vehicle_category/reports/testrail_id_map_vehicle_category.tsv"),
}
REMOVED = "features/vehicle_setting/reports/vf230_removed_non_nafta.tsv"

BLOCK_NOTE = ("BLOCKED：feature.yaml 無 `delivery.tc_id_abbr`（全庫無任一 feature 宣告），"
              "R-G42 二之 ABBR 無據；本層不自訂")
KEPT_NOTE = ("kept（包內令已有者不改號）；**前綴 `newR1L-` 不合 R-G42 二之 `NR1L-`**，"
             "現行 delivered/ 之形制為 `NR1L-{ABBR}-{nnn}`")


def build(slug: str) -> dict:
    book, out = BOOKS[slug]
    ws, g = v1.cells(ROOT / book)
    rows = v1.data_rows(ws, g)
    recs = []
    for r in rows:
        old_f = g(r, 6).strip()
        if old_f:
            recs.append({"row": r, "req_id": g(r, 4), "old_E": g(r, 5).strip(),
                         "old_F": old_f, "new_F": old_f, "status": "kept",
                         "note": KEPT_NOTE if not old_f.startswith("NR1L-") else ""})
        else:
            recs.append({"row": r, "req_id": g(r, 4), "old_E": g(r, 5).strip(),
                         "old_F": "", "new_F": "", "status": "BLOCKED",
                         "note": BLOCK_NOTE})

    retired = 0
    if slug == "vehicle_setting":
        for x in csv.DictReader(open(ROOT / REMOVED), delimiter="\t"):
            recs.append({"row": x["row"], "req_id": x["req_id"], "old_E": "",
                         "old_F": "", "new_F": "", "status": "RETIRED",
                         "note": f"{x['reason']}（VS-SL-03 §2 移除，未入轉正本）"})
            retired += 1

    p = ROOT / out
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t")
        w.writeheader()
        w.writerows(recs)

    stat = {"slug": slug, "path": out, "rows_in_book": len(rows),
            "retired": retired, "map_rows": len(recs),
            "E_filled": sum(1 for r in rows if g(r, 5).strip()),
            "E_empty": sum(1 for r in rows if not g(r, 5).strip()),
            "F_filled": sum(1 for r in rows if g(r, 6).strip()),
            "F_empty": sum(1 for r in rows if not g(r, 6).strip())}
    assert stat["map_rows"] == stat["rows_in_book"] + retired, "對照表列數不符"
    return stat


def main() -> int:
    print(f"{'feature':<18} {'本內列':>6} {'RETIRED':>8} {'對照表':>7}  "
          f"{'E 空/非空':>10}  {'F 空/非空':>10}")
    for slug in BOOKS:
        s = build(slug)
        print(f"{s['slug']:<18} {s['rows_in_book']:>6} {s['retired']:>8} {s['map_rows']:>7}  "
              f"{s['E_empty']:>5}/{s['E_filled']:<4}  {s['F_empty']:>5}/{s['F_filled']:<4}"
              f"  （assert PASS）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
