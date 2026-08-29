# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleCategory_20260827_working.xlsx

- 來源：`features/vehicle_category/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleCategory_20260827_working.xlsx`（唯讀）
- 資料列數：126
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 5 | 5 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |

**總計：行計 5**（列計不加總——同一列可觸發多項檢查）

## 明細

### L — test_item 上半過長 (>50 tokens)（行計 5／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 34 | newR1L-VC-025 | test_item | 上半 55 tokens > 50 | CO2.) Possible items to be placed in the Controls tab include, but are not limit |
| 47 | newR1L-VC-038 | test_item | 上半 61 tokens > 50 | Rear Sunshade \| Activates Feature (button only highlights when pressed ) ⏎  ⏎ Screen |
| 48 | newR1L-VC-039 | test_item | 上半 60 tokens > 50 | Mirror Dimmer \| Off, On (if unavailable – greyed out) ⏎  ⏎ Headrest Fold - 2nd Row \| |
| 49 | newR1L-VC-040 | test_item | 上半 68 tokens > 50 | (Pass Screen Screen Off) \| Pass Screen Screen On/Pass Screen Screen Off Turns Pa |
| 50 | newR1L-VC-041 | test_item | 上半 74 tokens > 50 | Bed Lowering \| Activates Feature (button highlights when feature engaged) ⏎  ⏎ Drive |

