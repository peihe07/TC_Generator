"""W-105 之 Sibling Rows 處置 —— batch13 之階數配置補入 pre_conditions。

batch14 之 ThreeStages 各列與 batch13 之 TwoStages 各列，**來源條文逐字相同**
（僅節號 `1.3.3.3.2.1` vs `1.3.3.3.3.1` 與階數配置相異）。
batch13 之 pre_conditions 第 1 項為「equipped with heated/vented front seats」，
**未指明階數** —— 二者因而不可分辨。

本檔僅改 pre_conditions 第 1 項，其餘九欄不動；產 `batch13_v2`，原版保留。
既有慣例見已交付之 `ThreeStagesHeatedSeat-080`／`TwoStagesHeatedSeat-057`
（「The vehicle is configured for two/three heated seat states」）。
"""
from __future__ import annotations

import json
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
FIX = {"The vehicle is equipped with heated front seats":
       "The vehicle is configured for two heated seat states",
       "The vehicle is equipped with vented front seats":
       "The vehicle is configured for two vented seat states"}


def main() -> None:
    src = FEAT / "generated/batch13.json"
    d = json.loads(src.read_text(encoding="utf-8"))
    n = 0
    for tc in d["tcs"]:
        for old, new in FIX.items():
            if old in tc["pre_conditions"]:
                tc["pre_conditions"] = tc["pre_conditions"].replace(old, new)
                n += 1
        assert "configured for two" in tc["pre_conditions"], tc["leaf_id"]
    d["revision"] = ("W-105（37 輪）之 Sibling Rows 處置：pre_conditions 補階數配置，"
                     "以與 batch14 之 ThreeStages 各列分辨。其餘九欄不動。")
    (FEAT / "generated/batch13_v2.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch13_v2：{n} 條之 pre_conditions 第 1 項已補階數配置")


if __name__ == "__main__":
    main()
