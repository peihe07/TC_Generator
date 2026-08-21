# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS012_DealerMode_20260417(done).xlsx

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/DealerMode/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS012_DealerMode_20260417(done).xlsx`（唯讀）
- 資料列數：125
- sheet：`Test Case Specification&Result`（header 第 9 列）
- L 閾值：50 tokens

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 6 | 6 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 22 | 16 | 每次命中 | 已校準 |
| C | hedge (test_item) | 0 | 0 | 每次命中 | 已校準 |
| D | PC 違規 (pre) | 6 | 6 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 1 | 1 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 129 | 120 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 6 | 6 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 29 | 29 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 54 | 54 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 1304 | 125 | 每行 | 已校準 |

**總計：行計 1557**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 6／列計 6）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 76 | newR1L-DealerMode-067 | proc | 禁用動詞 'check whether' | Demo Video" App to check whether the video exists. |
| 77 | newR1L-DealerMode-068 | proc | 禁用動詞 'check whether' | Demo Video" app to check whether the video exists. |
| 78 | newR1L-DealerMode-069 | proc | 禁用動詞 'check whether' | Demo Video" app to check whether the video exists. ⏎ |
| 79 | newR1L-DealerMode-070 | proc | 禁用動詞 'check whether' | Demo Video" app to check whether the video exists. |
| 80 | newR1L-DealerMode-071 | proc | 禁用動詞 'check whether' | Demo Video" app to check whether the video exists. ⏎ 8. Select the uploaded video |
| 100 | newR1L-DealerMode-091 | proc | 禁用動詞 'check whether' | Demo Video” app to check whether the .mov video exists. |

### B — ER 情態詞 (er)（行計 22／列計 16）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-DealerMode-001 | er | 情態詞 'shall' | System information shall include: ⏎ a. Radio Part Information ⏎   - FCA Hardware pa |
| 11 | newR1L-DealerMode-002 | er | 情態詞 'shall' | System information shall include: ⏎ a. Radio Part Information ⏎   - FCA Hardware pa |
| 12 | newR1L-DealerMode-003 | er | 情態詞 'shall' | System information shall include: ⏎ a. Radio Part Information ⏎   - FCA Hardware pa |
| 13 | newR1L-DealerMode-004 | er | 情態詞 'shall' | System information shall include: ⏎ a. Radio Part Information ⏎   - FCA Hardware pa |
| 31 | newR1L-DealerMode-022 | er | 情態詞 'shall' | ⏎ 7. DealerMode page shall force the language to be set to English. |
| 36 | newR1L-DealerMode-027 | er | 情態詞 'shall' | displayed. ⏎ 4. Music shall playing normally on Dealer Mode page. |
| 37 | newR1L-DealerMode-028 | er | 情態詞 'shall' | Mode page. ⏎ 3. Music shall playing normally on Dealer Mode page. ⏎ 4. Sysyem Inorma |
| 37 | newR1L-DealerMode-028 | er | 情態詞 'shall' | . Radio Information shall include: ⏎ - FCA Hardware part number ⏎ - Software version |
| 70 | newR1L-DealerMode-061 | er | 情態詞 'shall' | e Log write process shall finish within 10 secs. |
| 75 | newR1L-DealerMode-066 | er | 情態詞 'shall' | ccess message popup shall appear after the upload finishes. ⏎ 6. Return to Home pa |
| 75 | newR1L-DealerMode-066 | er | 情態詞 'shall' | loaded from the USB shall be present and playable on the Showroom Demo Video pag |
| 76 | newR1L-DealerMode-067 | er | 情態詞 'shall' | fail message popup shall appear during the upload process. ⏎ 6. Return to Home pa |
| 77 | newR1L-DealerMode-068 | er | 情態詞 'shall' | ccess message popup shall appear after the upload finishes. ⏎ 6. Return to Home pa |
| 77 | newR1L-DealerMode-068 | er | 情態詞 'shall' | is less than 200MB shall be present and playable. |
| 78 | newR1L-DealerMode-069 | er | 情態詞 'shall' | ccess message popup shall appear after the upload finishes. ⏎ 6. Return to Home pa |
| 78 | newR1L-DealerMode-069 | er | 情態詞 'shall' | h is equal to 200MB shall be present and playable. |
| 79 | newR1L-DealerMode-070 | er | 情態詞 'shall' | fail message popup shall appear during the upload process. ⏎ 6. Return to Home pa |
| 79 | newR1L-DealerMode-070 | er | 情態詞 'shall' | s larger than 200MB shall not be present on Showroom demo video page. |
| 80 | newR1L-DealerMode-071 | er | 情態詞 'shall' | ccess message popup shall appear after the upload finishes. ⏎ 6. Return to Home pa |
| 80 | newR1L-DealerMode-071 | er | 情態詞 'shall' | The uploaded video shall load and play without error. |
| 81 | newR1L-DealerMode-072 | er | 情態詞 'shall' | ccess message popup shall appear after the Data message cleared. ⏎ 5. App Drawer p |
| 100 | newR1L-DealerMode-091 | er | 情態詞 'shall' | fail message popup shall appear during the upload process and return previous p |

### D — PC 違規 (pre)（行計 6／列計 6）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 75 | newR1L-DealerMode-066 | pre | 編號行行首動詞 'Connect' | 2. Connect a USB drive that includes the valid Showroom demo video file. |
| 76 | newR1L-DealerMode-067 | pre | 編號行行首動詞 'Connect' | 2. Connect a USB drive that includes the invalid video file. |
| 77 | newR1L-DealerMode-068 | pre | 編號行行首動詞 'Connect' | 3. Connect a USB drive that includes the video file less than 200MB |
| 78 | newR1L-DealerMode-069 | pre | 編號行行首動詞 'Connect' | 2. Connect a USB drive that includes the video file eqaul to 200MB |
| 79 | newR1L-DealerMode-070 | pre | 編號行行首動詞 'Connect' | 2. Connect a USB drive that includes the video file larger than 200MB |
| 80 | newR1L-DealerMode-071 | pre | 編號行行首動詞 'Connect' | 2. Connect a USB drive that includes the valid Showroom demo video file. |

### E — proc/er 編號行數不對齊（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 15 | newR1L-DealerMode-006 | proc/er | proc 6 步 vs er 5 步 |  |

### F — 方括號佔位 (proc)（行計 129／列計 120）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-DealerMode-001 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 11 | newR1L-DealerMode-002 | proc | 方括號佔位 '[Screen off]' | oot HU ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 12 | newR1L-DealerMode-003 | proc | 方括號佔位 '[Screen off]' | le HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 13 | newR1L-DealerMode-004 | proc | 方括號佔位 '[Screen off]' | ched" ⏎  ⏎ 6. Press H/K [Screen off] button to turn off the HU screen. ⏎ 7. Press and |
| 14 | newR1L-DealerMode-005 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 15 | newR1L-DealerMode-006 | proc | 方括號佔位 '[Screen off]' | ot HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 16 | newR1L-DealerMode-007 | proc | 方括號佔位 '[Screen off]' | le HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 17 | newR1L-DealerMode-008 | proc | 方括號佔位 '[Screen off]' | ched" ⏎  ⏎ 6. Press H/K [Screen off] button to turn off the HU screen. ⏎ 7. Press and |
| 18 | newR1L-DealerMode-009 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 19 | newR1L-DealerMode-010 | proc | 方括號佔位 '[Screen off]' | ot HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 20 | newR1L-DealerMode-011 | proc | 方括號佔位 '[Screen off]' | le HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 21 | newR1L-DealerMode-012 | proc | 方括號佔位 '[Screen off]' | ched" ⏎  ⏎ 6. Press H/K [Screen off] button to turn off the HU screen. ⏎ 7. Press and |
| 22 | newR1L-DealerMode-013 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 22 | newR1L-DealerMode-013 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 4. Check Screen |
| 23 | newR1L-DealerMode-014 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 23 | newR1L-DealerMode-014 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 4. Check Screen |
| 24 | newR1L-DealerMode-015 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 24 | newR1L-DealerMode-015 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 8. Check Screen |
| 25 | newR1L-DealerMode-016 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 26 | newR1L-DealerMode-017 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 27 | newR1L-DealerMode-018 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 28 | newR1L-DealerMode-019 | proc | 方括號佔位 '[Screen off]' | ot HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 29 | newR1L-DealerMode-020 | proc | 方括號佔位 '[Screen off]' | le HU. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 30 | newR1L-DealerMode-021 | proc | 方括號佔位 '[Screen off]' | glish  ⏎ 5. Press H/K [Screen off] button to turn off the HU screen. ⏎ 6. Press and |
| 31 | newR1L-DealerMode-022 | proc | 方括號佔位 '[Screen off]' | encis  ⏎ 5. Press H/K [Screen off] button to turn off the HU screen. ⏎ 6. Press and |
| 32 | newR1L-DealerMode-023 | proc | 方括號佔位 '[Screen off]' | page. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 33 | newR1L-DealerMode-024 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 34 | newR1L-DealerMode-025 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 35 | newR1L-DealerMode-026 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 36 | newR1L-DealerMode-027 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 37 | newR1L-DealerMode-028 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 38 | newR1L-DealerMode-029 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 39 | newR1L-DealerMode-030 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 40 | newR1L-DealerMode-031 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 41 | newR1L-DealerMode-032 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 42 | newR1L-DealerMode-033 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 43 | newR1L-DealerMode-034 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 44 | newR1L-DealerMode-035 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 45 | newR1L-DealerMode-036 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 46 | newR1L-DealerMode-037 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 47 | newR1L-DealerMode-038 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 48 | newR1L-DealerMode-039 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 49 | newR1L-DealerMode-040 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 50 | newR1L-DealerMode-041 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 51 | newR1L-DealerMode-042 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 52 | newR1L-DealerMode-043 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 53 | newR1L-DealerMode-044 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 54 | newR1L-DealerMode-045 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 55 | newR1L-DealerMode-046 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 56 | newR1L-DealerMode-047 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 57 | newR1L-DealerMode-048 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 58 | newR1L-DealerMode-049 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 59 | newR1L-DealerMode-050 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 60 | newR1L-DealerMode-051 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 61 | newR1L-DealerMode-052 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 62 | newR1L-DealerMode-053 | proc | 方括號佔位 '[Screen off]' | ction. ⏎ 3. Press H/K [Screen off] button to turn off the HU screen. ⏎ 4. Press and |
| 63 | newR1L-DealerMode-054 | proc | 方括號佔位 '[Screen off]' | apps. ⏎ 4. Press H/K [Screen off] button to turn off the HU screen. ⏎ 5. Press and |
| 64 | newR1L-DealerMode-055 | proc | 方括號佔位 '[Screen off]' | lizer. ⏎ 5. Press H/K [Screen off] button to turn off the HU screen. ⏎ 6. Press and |
| 65 | newR1L-DealerMode-056 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 65 | newR1L-DealerMode-056 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 3. Check Screen |
| 66 | newR1L-DealerMode-057 | proc | 方括號佔位 '[POWER]' | em log: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K[MUTE] within 3 seconds aft |
| 66 | newR1L-DealerMode-057 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K[MUTE] within 3 seconds after Step a. ⏎ 3. Check System log in |
| 67 | newR1L-DealerMode-058 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 67 | newR1L-DealerMode-058 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 68 | newR1L-DealerMode-059 | proc | 方括號佔位 '[POWER]' | em log: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K[MUTE] within 3 seconds aft |
| 68 | newR1L-DealerMode-059 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K[MUTE] within 3 seconds after Step a. |
| 71 | newR1L-DealerMode-062 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 71 | newR1L-DealerMode-062 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 3. Check the im |
| 72 | newR1L-DealerMode-063 | proc | 方括號佔位 '[POWER]' | enshot: ⏎  a. Hold H/K[POWER] for 2 secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 |
| 72 | newR1L-DealerMode-063 | proc | 方括號佔位 '[MUTE]' | secs. ⏎  b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. ⏎ 3. Check the im |
| 73 | newR1L-DealerMode-064 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 74 | newR1L-DealerMode-065 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 75 | newR1L-DealerMode-066 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 76 | newR1L-DealerMode-067 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 77 | newR1L-DealerMode-068 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 78 | newR1L-DealerMode-069 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 79 | newR1L-DealerMode-070 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 80 | newR1L-DealerMode-071 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 84 | newR1L-DealerMode-075 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 85 | newR1L-DealerMode-076 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 86 | newR1L-DealerMode-077 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 87 | newR1L-DealerMode-078 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 88 | newR1L-DealerMode-079 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 89 | newR1L-DealerMode-080 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 90 | newR1L-DealerMode-081 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 91 | newR1L-DealerMode-082 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 92 | newR1L-DealerMode-083 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 93 | newR1L-DealerMode-084 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 94 | newR1L-DealerMode-085 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 95 | newR1L-DealerMode-086 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 96 | newR1L-DealerMode-087 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 97 | newR1L-DealerMode-088 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 98 | newR1L-DealerMode-089 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 99 | newR1L-DealerMode-090 | proc | 方括號佔位 '[Screen Off]' | 1.Press H/K [Screen Off] button to turn off the screen. ⏎ 2. Press and hold the to |
| 100 | newR1L-DealerMode-091 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 101 | newR1L-DealerMode-092 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 102 | newR1L-DealerMode-093 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 103 | newR1L-DealerMode-094 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 104 | newR1L-DealerMode-095 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 105 | newR1L-DealerMode-096 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 106 | newR1L-DealerMode-097 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 107 | newR1L-DealerMode-098 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 108 | newR1L-DealerMode-099 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 109 | newR1L-DealerMode-100 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 110 | newR1L-DealerMode-101 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 111 | newR1L-DealerMode-102 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 112 | newR1L-DealerMode-103 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 113 | newR1L-DealerMode-104 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 114 | newR1L-DealerMode-105 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 115 | newR1L-DealerMode-106 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 116 | newR1L-DealerMode-107 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 117 | newR1L-DealerMode-108 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 118 | newR1L-DealerMode-109 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 119 | newR1L-DealerMode-110 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 120 | newR1L-DealerMode-111 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the screen. ⏎ 2. Press and Hold the t |
| 121 | newR1L-DealerMode-112 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 122 | newR1L-DealerMode-113 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 123 | newR1L-DealerMode-114 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 124 | newR1L-DealerMode-115 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 125 | newR1L-DealerMode-116 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 126 | newR1L-DealerMode-117 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 127 | newR1L-DealerMode-118 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 128 | newR1L-DealerMode-119 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and Hold th |
| 129 | newR1L-DealerMode-120 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 130 | newR1L-DealerMode-121 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 131 | newR1L-DealerMode-122 | proc | 方括號佔位 '[Screen off]' | etion. ⏎ 2. Press H/K [Screen off] button to turn off the HU screen. ⏎ 3. Press and |
| 132 | newR1L-DealerMode-123 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 133 | newR1L-DealerMode-124 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |
| 134 | newR1L-DealerMode-125 | proc | 方括號佔位 '[Screen off]' | 1. Press H/K [Screen off] button to turn off the HU screen. ⏎ 2. Press and hold th |

### H — ER 模糊語 (er)（行計 6／列計 6）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 105 | newR1L-DealerMode-096 | er | 模糊語 'as expected' | executed and fails as expected. ⏎ 5. A visible Fail result indication is displaye |
| 108 | newR1L-DealerMode-099 | er | 模糊語 'as expected' | cessfully and fails as expected. ⏎ 6. A Fail result indication with the message "I |
| 109 | newR1L-DealerMode-100 | er | 模糊語 'as expected' | cessfully and fails as expected. ⏎ 7. A Fail result indication with the message "I |
| 110 | newR1L-DealerMode-101 | er | 模糊語 'as expected' | cessfully and fails as expected. ⏎ 7. A Fail result indication with the message "I |
| 111 | newR1L-DealerMode-102 | er | 模糊語 'as expected' | cessfully and fails as expected. ⏎ 6. A Fail result indication with the message "E |
| 112 | newR1L-DealerMode-103 | er | 模糊語 'as expected' | cessfully and fails as expected. ⏎ 7. A Fail result indication with the message "E |

### I — test_item 括號下半缺失（行計 29／列計 29）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-DealerMode-001 | test_item | 缺括號下半 | The radio HU shall allow a user to see system information |
| 14 | newR1L-DealerMode-005 | test_item | 缺括號下半 | The radio HU shall allow a user to download data. |
| 18 | newR1L-DealerMode-009 | test_item | 缺括號下半 | The radio HU shall allow a user to restore data. |
| 36 | newR1L-DealerMode-027 | test_item | 缺括號下半 | When the HU enters dealer mode, the HU shall continue to operate in normal mode |
| 37 | newR1L-DealerMode-028 | test_item | 缺括號下半 | When the HU enters dealer mode, the HU shall continue to operate in normal mode |
| 38 | newR1L-DealerMode-029 | test_item | 缺括號下半 | If Dealer Mode has an "X" button, the HU shall exit through the "X" button inste |
| 40 | newR1L-DealerMode-031 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ Stellantis Ha |
| 41 | newR1L-DealerMode-032 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ Software vers |
| 42 | newR1L-DealerMode-033 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ Serial number |
| 43 | newR1L-DealerMode-034 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ HD tuner firm |
| 44 | newR1L-DealerMode-035 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ DAB tuner fir |
| 45 | newR1L-DealerMode-036 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ EQ version |
| 46 | newR1L-DealerMode-037 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎ Android versi |
| 47 | newR1L-DealerMode-038 | test_item | 缺括號下半 | The display shall include the following information as applicable: ⏎  Security Ser |
| 48 | newR1L-DealerMode-039 | test_item | 缺括號下半 | The HU shall collect the information locally within the HU assembly. |
| 49 | newR1L-DealerMode-040 | test_item | 缺括號下半 | The display shall include the following SDAR information as applicable: ⏎ SDAR har |
| 50 | newR1L-DealerMode-041 | test_item | 缺括號下半 | The display shall include the following SDAR information as applicable: ⏎ SDAR fir |
| 52 | newR1L-DealerMode-043 | test_item | 缺括號下半 | The HU shall collect the information locally within the HU assembly. |
| 53 | newR1L-DealerMode-044 | test_item | 缺括號下半 | The display shall include the flash loader version. |
| 54 | newR1L-DealerMode-045 | test_item | 缺括號下半 | The display shall include the following navigation information or equivalent ver |
| 55 | newR1L-DealerMode-046 | test_item | 缺括號下半 | The display shall allow the user to select to download user data from flash memo |
| 56 | newR1L-DealerMode-047 | test_item | 缺括號下半 | The following information shall be stored: ⏎  Media Presets |
| 57 | newR1L-DealerMode-048 | test_item | 缺括號下半 | The following information shall be stored: ⏎  SXM Favorites |
| 58 | newR1L-DealerMode-049 | test_item | 缺括號下半 | The following information shall be stored: ⏎  Driver User EQ Settings |
| 69 | newR1L-DealerMode-060 | test_item | 缺括號下半 | The write process to the storage media shall start within 2 seconds. |
| 70 | newR1L-DealerMode-061 | test_item | 缺括號下半 | The write process to the storage media shall finish within 10 seconds. |
| 71 | newR1L-DealerMode-062 | test_item | 缺括號下半 | The screenshot file shall be saved in a commonly used format (e.g. BMP, JPEG, PN |
| 72 | newR1L-DealerMode-063 | test_item | 缺括號下半 | The filename of the screenshot shall contain the date and time when the screensh |
| 80 | newR1L-DealerMode-071 | test_item | 缺括號下半 | The HU shall load and play the Demo Video. |

### M — 空欄三態（行計 54／列計 54）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-DealerMode-001 | pre | 空欄（非 NA、非 PENDING:） |  |
| 11 | newR1L-DealerMode-002 | pre | 空欄（非 NA、非 PENDING:） |  |
| 12 | newR1L-DealerMode-003 | pre | 空欄（非 NA、非 PENDING:） |  |
| 14 | newR1L-DealerMode-005 | pre | 空欄（非 NA、非 PENDING:） |  |
| 15 | newR1L-DealerMode-006 | pre | 空欄（非 NA、非 PENDING:） |  |
| 16 | newR1L-DealerMode-007 | pre | 空欄（非 NA、非 PENDING:） |  |
| 25 | newR1L-DealerMode-016 | pre | 空欄（非 NA、非 PENDING:） |  |
| 26 | newR1L-DealerMode-017 | pre | 空欄（非 NA、非 PENDING:） |  |
| 27 | newR1L-DealerMode-018 | pre | 空欄（非 NA、非 PENDING:） |  |
| 28 | newR1L-DealerMode-019 | pre | 空欄（非 NA、非 PENDING:） |  |
| 29 | newR1L-DealerMode-020 | pre | 空欄（非 NA、非 PENDING:） |  |
| 30 | newR1L-DealerMode-021 | pre | 空欄（非 NA、非 PENDING:） |  |
| 31 | newR1L-DealerMode-022 | pre | 空欄（非 NA、非 PENDING:） |  |
| 32 | newR1L-DealerMode-023 | pre | 空欄（非 NA、非 PENDING:） |  |
| 33 | newR1L-DealerMode-024 | pre | 空欄（非 NA、非 PENDING:） |  |
| 34 | newR1L-DealerMode-025 | pre | 空欄（非 NA、非 PENDING:） |  |
| 35 | newR1L-DealerMode-026 | pre | 空欄（非 NA、非 PENDING:） |  |
| 38 | newR1L-DealerMode-029 | pre | 空欄（非 NA、非 PENDING:） |  |
| 39 | newR1L-DealerMode-030 | pre | 空欄（非 NA、非 PENDING:） |  |
| 40 | newR1L-DealerMode-031 | pre | 空欄（非 NA、非 PENDING:） |  |
| 41 | newR1L-DealerMode-032 | pre | 空欄（非 NA、非 PENDING:） |  |
| 42 | newR1L-DealerMode-033 | pre | 空欄（非 NA、非 PENDING:） |  |
| 43 | newR1L-DealerMode-034 | pre | 空欄（非 NA、非 PENDING:） |  |
| 44 | newR1L-DealerMode-035 | pre | 空欄（非 NA、非 PENDING:） |  |
| 45 | newR1L-DealerMode-036 | pre | 空欄（非 NA、非 PENDING:） |  |
| 46 | newR1L-DealerMode-037 | pre | 空欄（非 NA、非 PENDING:） |  |
| 47 | newR1L-DealerMode-038 | pre | 空欄（非 NA、非 PENDING:） |  |
| 48 | newR1L-DealerMode-039 | pre | 空欄（非 NA、非 PENDING:） |  |
| 49 | newR1L-DealerMode-040 | pre | 空欄（非 NA、非 PENDING:） |  |
| 50 | newR1L-DealerMode-041 | pre | 空欄（非 NA、非 PENDING:） |  |
| 51 | newR1L-DealerMode-042 | pre | 空欄（非 NA、非 PENDING:） |  |
| 52 | newR1L-DealerMode-043 | pre | 空欄（非 NA、非 PENDING:） |  |
| 53 | newR1L-DealerMode-044 | pre | 空欄（非 NA、非 PENDING:） |  |
| 54 | newR1L-DealerMode-045 | pre | 空欄（非 NA、非 PENDING:） |  |
| 55 | newR1L-DealerMode-046 | pre | 空欄（非 NA、非 PENDING:） |  |
| 56 | newR1L-DealerMode-047 | pre | 空欄（非 NA、非 PENDING:） |  |
| 57 | newR1L-DealerMode-048 | pre | 空欄（非 NA、非 PENDING:） |  |
| 58 | newR1L-DealerMode-049 | pre | 空欄（非 NA、非 PENDING:） |  |
| 59 | newR1L-DealerMode-050 | pre | 空欄（非 NA、非 PENDING:） |  |
| 69 | newR1L-DealerMode-060 | pre | 空欄（非 NA、非 PENDING:） |  |
| 70 | newR1L-DealerMode-061 | pre | 空欄（非 NA、非 PENDING:） |  |
| 73 | newR1L-DealerMode-064 | pre | 空欄（非 NA、非 PENDING:） |  |
| 86 | newR1L-DealerMode-077 | pre | 空欄（非 NA、非 PENDING:） |  |
| 107 | newR1L-DealerMode-098 | pre | 空欄（非 NA、非 PENDING:） |  |
| 108 | newR1L-DealerMode-099 | pre | 空欄（非 NA、非 PENDING:） |  |
| 111 | newR1L-DealerMode-102 | pre | 空欄（非 NA、非 PENDING:） |  |
| 112 | newR1L-DealerMode-103 | pre | 空欄（非 NA、非 PENDING:） |  |
| 128 | newR1L-DealerMode-119 | pre | 空欄（非 NA、非 PENDING:） |  |
| 129 | newR1L-DealerMode-120 | pre | 空欄（非 NA、非 PENDING:） |  |
| 130 | newR1L-DealerMode-121 | pre | 空欄（非 NA、非 PENDING:） |  |
| 131 | newR1L-DealerMode-122 | pre | 空欄（非 NA、非 PENDING:） |  |
| 132 | newR1L-DealerMode-123 | pre | 空欄（非 NA、非 PENDING:） |  |
| 133 | newR1L-DealerMode-124 | pre | 空欄（非 NA、非 PENDING:） |  |
| 134 | newR1L-DealerMode-125 | pre | 空欄（非 NA、非 PENDING:） |  |

### N — 行尾多餘句號（行計 1304／列計 125）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-DealerMode-001 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 10 | newR1L-DealerMode-001 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 10 | newR1L-DealerMode-001 | proc | 行尾多餘句號 | 3. Select "System Information" and check all displayed information. |
| 11 | newR1L-DealerMode-002 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 11 | newR1L-DealerMode-002 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 11 | newR1L-DealerMode-002 | proc | 行尾多餘句號 | 4. Select "System Information" and check all displayed information. |
| 11 | newR1L-DealerMode-002 | er | 行尾多餘句號 | 1. HU cold boots normally without error. |
| 12 | newR1L-DealerMode-003 | proc | 行尾多餘句號 | 1. Power Cycle HU. |
| 12 | newR1L-DealerMode-003 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 12 | newR1L-DealerMode-003 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 12 | newR1L-DealerMode-003 | proc | 行尾多餘句號 | 4. Select "System Information" and check all displayed information. |
| 12 | newR1L-DealerMode-003 | er | 行尾多餘句號 | 1. HU reconnects normally without error. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 1. Access adb to trigger the low memory environment. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 2. Check the Current RAM memory storge. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 3. Create a Mount tmpfs Memory storage file(1GB) to the system. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 4. Input data into the tmpfs file to occupy actual RAM storage. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 5. Check the Current RAM memory storge again to make sure the Memery Available i |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 6. Press H/K [Screen off] button to turn off the HU screen. |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 7. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 13 | newR1L-DealerMode-004 | proc | 行尾多餘句號 | 8. Select "System Information" and check all displayed information is displayed  |
| 13 | newR1L-DealerMode-004 | er | 行尾多餘句號 | 1. adb shell is accessed. |
| 13 | newR1L-DealerMode-004 | er | 行尾多餘句號 | 2. RAM memory storage usage is visible. |
| 13 | newR1L-DealerMode-004 | er | 行尾多餘句號 | 3. Mount tmpfs Memory storage file is established. |
| 13 | newR1L-DealerMode-004 | er | 行尾多餘句號 | 4. Data is inputed in tmpfs file. |
| 13 | newR1L-DealerMode-004 | er | 行尾多餘句號 | 5. Memery Available storage is decreased. |
| 14 | newR1L-DealerMode-005 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 14 | newR1L-DealerMode-005 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 14 | newR1L-DealerMode-005 | proc | 行尾多餘句號 | 3. Insert a USB/SD card storage device to download data to USB/SD card. |
| 14 | newR1L-DealerMode-005 | proc | 行尾多餘句號 | 4. Select "Data Download" to export data to USB or SD card. |
| 14 | newR1L-DealerMode-005 | proc | 行尾多餘句號 | 5. Check the exported data on the storage device. |
| 14 | newR1L-DealerMode-005 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 14 | newR1L-DealerMode-005 | er | 行尾多餘句號 | 4. Data is successfully exported to the storage device. |
| 14 | newR1L-DealerMode-005 | er | 行尾多餘句號 | 5. Exported data is correct and usable. |
| 15 | newR1L-DealerMode-006 | proc | 行尾多餘句號 | 1. Cold boot HU. |
| 15 | newR1L-DealerMode-006 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 15 | newR1L-DealerMode-006 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 15 | newR1L-DealerMode-006 | proc | 行尾多餘句號 | 4. Insert a USB/SD card storage device to download data to USB/SD card. |
| 15 | newR1L-DealerMode-006 | proc | 行尾多餘句號 | 5. Select "Data Download" to export data to USB or SD card. |
| 15 | newR1L-DealerMode-006 | er | 行尾多餘句號 | 1. HU cold boots normally without error. |
| 15 | newR1L-DealerMode-006 | er | 行尾多餘句號 | 4. Data is successfully exported to the storage device. |
| 15 | newR1L-DealerMode-006 | er | 行尾多餘句號 | 5. Exported data is correct and usable. |
| 16 | newR1L-DealerMode-007 | proc | 行尾多餘句號 | 1. Power Cycle HU. |
| 16 | newR1L-DealerMode-007 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 16 | newR1L-DealerMode-007 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 16 | newR1L-DealerMode-007 | proc | 行尾多餘句號 | 4. Insert a USB/SD card storage device to download data to USB/SD card. |
| 16 | newR1L-DealerMode-007 | proc | 行尾多餘句號 | 5. Select "Data Download" to export data to USB or SD card. |
| 16 | newR1L-DealerMode-007 | er | 行尾多餘句號 | 1. HU reconnects normally without error. |
| 16 | newR1L-DealerMode-007 | er | 行尾多餘句號 | 4. The USB storage device is detected by the system. |
| 16 | newR1L-DealerMode-007 | er | 行尾多餘句號 | 5. Data is successfully exported to the storage device. |
| 16 | newR1L-DealerMode-007 | er | 行尾多餘句號 | 6. Exported data is correct and usable. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 1. Access adb to trigger the low memory environment. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 2. Check the Current RAM memory storge. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 3. Create a Mount tmpfs Memory storage file(1GB) to the system. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 4. Input data into the tmpfs file to occupy actual RAM storage. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 5. Check the Current RAM memory storge again to make sure the Memery Available i |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 6. Press H/K [Screen off] button to turn off the HU screen. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 7. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 8. Insert a USB/SD card storage device. |
| 17 | newR1L-DealerMode-008 | proc | 行尾多餘句號 | 9. Select "Data Download" to export data to USB or SD card. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 1. adb shell is accessed. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 2. RAM memory storage usage is visible. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 3. Mount tmpfs Memory storage file is established. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 4. Data is inputed in tmpfs file. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 5. Memery Available storage is decreased. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 8. The USB storage device is detected by the system. |
| 17 | newR1L-DealerMode-008 | er | 行尾多餘句號 | 9. Data is successfully exported to the storage device. |
| 18 | newR1L-DealerMode-009 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 18 | newR1L-DealerMode-009 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 18 | newR1L-DealerMode-009 | proc | 行尾多餘句號 | 3. Insert a USB/SD card storage device. |
| 18 | newR1L-DealerMode-009 | proc | 行尾多餘句號 | 4. Select "Data Restore" to restore data from USB or SD card. |
| 18 | newR1L-DealerMode-009 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 18 | newR1L-DealerMode-009 | er | 行尾多餘句號 | 4. System data is correctly restored. |
| 19 | newR1L-DealerMode-010 | proc | 行尾多餘句號 | 1. Cold boot HU. |
| 19 | newR1L-DealerMode-010 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 19 | newR1L-DealerMode-010 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 19 | newR1L-DealerMode-010 | proc | 行尾多餘句號 | 4. Insert a USB/SD card storage device. |
| 19 | newR1L-DealerMode-010 | proc | 行尾多餘句號 | 5. Select "Data Restore" to restore data from USB or SD card. |
| 19 | newR1L-DealerMode-010 | er | 行尾多餘句號 | 1. HU cold boots normally without error. |
| 19 | newR1L-DealerMode-010 | er | 行尾多餘句號 | 4. The USB storage device is detected by the system. |
| 19 | newR1L-DealerMode-010 | er | 行尾多餘句號 | 5. System data is correctly restored. |
| 20 | newR1L-DealerMode-011 | proc | 行尾多餘句號 | 1. Power Cycle HU. |
| 20 | newR1L-DealerMode-011 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 20 | newR1L-DealerMode-011 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 20 | newR1L-DealerMode-011 | proc | 行尾多餘句號 | 4. Insert a USB/SD card storage device. |
| 20 | newR1L-DealerMode-011 | proc | 行尾多餘句號 | 5. Select "Data Restore" to restore data from USB or SD card. |
| 20 | newR1L-DealerMode-011 | er | 行尾多餘句號 | 1. HU reconnects normally without error. |
| 20 | newR1L-DealerMode-011 | er | 行尾多餘句號 | 4. The USB storage device is detected by the system. |
| 20 | newR1L-DealerMode-011 | er | 行尾多餘句號 | 5. System data is correctly restored. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 1. Access adb to trigger the low memory environment. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 2. Check the Current RAM memory storge. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 3. Create a Mount tmpfs Memory storage file(1GB) to the system. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 4. Input data into the tmpfs file to occupy actual RAM storage. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 5. Check the Current RAM memory storge again to make sure the Memery Available i |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 6. Press H/K [Screen off] button to turn off the HU screen. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 7. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 8. Insert a USB/SD card storage device. |
| 21 | newR1L-DealerMode-012 | proc | 行尾多餘句號 | 9. Select "Data Restore" to check system shall restore data from USB or SD card  |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 1. adb shell is accessed. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 2. RAM memory storage usage is visible. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 3. Mount tmpfs Memory storage file is established. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 4. Data is inputed in tmpfs file. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 5. Memery Available storage is decreased. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 8. The USB storage device is detected by the system. |
| 21 | newR1L-DealerMode-012 | er | 行尾多餘句號 | 9. System data is correctly restored in Low Memory environment. |
| 22 | newR1L-DealerMode-013 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 22 | newR1L-DealerMode-013 | proc | 行尾多餘句號 | 1. Cold boot HU. |
| 22 | newR1L-DealerMode-013 | proc | 行尾多餘句號 | 2. Insert a USB card storage device. |
| 22 | newR1L-DealerMode-013 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 22 | newR1L-DealerMode-013 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 22 | newR1L-DealerMode-013 | proc | 行尾多餘句號 | 4. Check Screenshot in USB. |
| 22 | newR1L-DealerMode-013 | er | 行尾多餘句號 | 1. HU cold boots normally without error. |
| 22 | newR1L-DealerMode-013 | er | 行尾多餘句號 | 2. The USB storage device is detected by the system. |
| 22 | newR1L-DealerMode-013 | er | 行尾多餘句號 | 3. Display Screenshot successful pop up. |
| 22 | newR1L-DealerMode-013 | er | 行尾多餘句號 | 4. The Screenshot is saved to the USB. |
| 23 | newR1L-DealerMode-014 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 23 | newR1L-DealerMode-014 | proc | 行尾多餘句號 | 1. Power Cycle HU. |
| 23 | newR1L-DealerMode-014 | proc | 行尾多餘句號 | 2. Insert a USB card storage device. |
| 23 | newR1L-DealerMode-014 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 23 | newR1L-DealerMode-014 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 23 | newR1L-DealerMode-014 | proc | 行尾多餘句號 | 4. Check Screenshot in USB. |
| 23 | newR1L-DealerMode-014 | er | 行尾多餘句號 | 1. HU reconnects normally without error. |
| 23 | newR1L-DealerMode-014 | er | 行尾多餘句號 | 2. The USB storage device is detected by the system. |
| 23 | newR1L-DealerMode-014 | er | 行尾多餘句號 | 3. Display Screenshot successful pop up. |
| 23 | newR1L-DealerMode-014 | er | 行尾多餘句號 | 4. The Screenshot is saved to the USB. |
| 24 | newR1L-DealerMode-015 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 1. Access adb to trigger the low memory environment. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 2. Check the Current RAM memory storge. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 3. Create a Mount tmpfs Memory storage file(1GB) to the system. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 4. Input data into the tmpfs file to occupy actual RAM storage. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 5. Check the Current RAM memory storge again to make sure the Memery Available i |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 6. Insert a USB card storage device. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 24 | newR1L-DealerMode-015 | proc | 行尾多餘句號 | 8. Check Screenshot in USB. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 1. adb shell is accessed. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 2. RAM memory storage usage is visible. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 3. Mount tmpfs Memory storage file is established. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 4. Data is inputed in tmpfs file. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 5. Memery Available storage is decreased. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 6. Insert a USB card storage device. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 7. Display Screenshot successful pop up. |
| 24 | newR1L-DealerMode-015 | er | 行尾多餘句號 | 8. The Screenshot is saved to the USB. |
| 25 | newR1L-DealerMode-016 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 25 | newR1L-DealerMode-016 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 26 | newR1L-DealerMode-017 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 26 | newR1L-DealerMode-017 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 26 | newR1L-DealerMode-017 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 26 | newR1L-DealerMode-017 | er | 行尾多餘句號 | 2. Display Dealer Mode page. |
| 27 | newR1L-DealerMode-018 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 27 | newR1L-DealerMode-018 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 27 | newR1L-DealerMode-018 | er | 行尾多餘句號 | 2. Not display Dealer Mode page. |
| 28 | newR1L-DealerMode-019 | proc | 行尾多餘句號 | 1. Cold boot HU. |
| 28 | newR1L-DealerMode-019 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 28 | newR1L-DealerMode-019 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 28 | newR1L-DealerMode-019 | er | 行尾多餘句號 | 1. HU reconnects normally without error. |
| 28 | newR1L-DealerMode-019 | er | 行尾多餘句號 | 2. HU screen is OFF. |
| 28 | newR1L-DealerMode-019 | er | 行尾多餘句號 | 3. Display Dealer Mode page. |
| 29 | newR1L-DealerMode-020 | proc | 行尾多餘句號 | 1. Power Cycle HU. |
| 29 | newR1L-DealerMode-020 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 29 | newR1L-DealerMode-020 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 29 | newR1L-DealerMode-020 | er | 行尾多餘句號 | 2. HU screen is OFF. |
| 29 | newR1L-DealerMode-020 | er | 行尾多餘句號 | 3. Display Dealer Mode page. |
| 30 | newR1L-DealerMode-021 | proc | 行尾多餘句號 | 1. Press "Vehicle Settings" on menu bar. |
| 30 | newR1L-DealerMode-021 | proc | 行尾多餘句號 | 2. Press "My Profile" menu item. |
| 30 | newR1L-DealerMode-021 | proc | 行尾多餘句號 | 5. Press H/K [Screen off] button to turn off the HU screen. |
| 30 | newR1L-DealerMode-021 | proc | 行尾多餘句號 | 6. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 30 | newR1L-DealerMode-021 | proc | 行尾多餘句號 | 7. Check the language display of Dealer Mode page. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 1. Vehicle Settings page is displayed. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 2. My Profile settings page is displayed. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 3. Language page is displayed. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 4. NA English has been switched. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 5. HU screen is OFF. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 6. Display Dealer Mode page. |
| 30 | newR1L-DealerMode-021 | er | 行尾多餘句號 | 7. Display English language on Dealer Mode page. |
| 31 | newR1L-DealerMode-022 | proc | 行尾多餘句號 | 1. Press "Vehicle Settings" on menu bar. |
| 31 | newR1L-DealerMode-022 | proc | 行尾多餘句號 | 2. Press "My Profile" menu item. |
| 31 | newR1L-DealerMode-022 | proc | 行尾多餘句號 | 5. Press H/K [Screen off] button to turn off the HU screen. |
| 31 | newR1L-DealerMode-022 | proc | 行尾多餘句號 | 6. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 31 | newR1L-DealerMode-022 | proc | 行尾多餘句號 | 7. Check the language display of Dealer Mode page. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 1. Vehicle Settings page is displayed. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 2. My Profile settings page is displayed. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 3. Language page is displayed. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 4. Francis has been switched. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 5. HU screen is OFF. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 6. Display Dealer Mode page. |
| 31 | newR1L-DealerMode-022 | er | 行尾多餘句號 | 7. DealerMode page shall force the language to be set to English. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 1. Press "Apps" on menu bar to go to App Drawer page. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 3. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 4. Check the current display page. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 5. Press "X" button to exit Dealer Mode page. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 6. Press "Media" on menu bar to go to Media page. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 7. Launch Dealer Mode again. |
| 32 | newR1L-DealerMode-023 | proc | 行尾多餘句號 | 8. Check the current display page. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 2. HU screen is OFF. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 3. Display Dealer Mode main page. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 5. Return to App Drawer page. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 6. Media page is displayed. |
| 32 | newR1L-DealerMode-023 | er | 行尾多餘句號 | 7. Display Dealer Mode main page. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 3. Press "System Information" menu item. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 4. Press "←" button to return to previous page. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 5. Press "X" button to exit Dealer Mode page. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 6. Launch Dealer Mode again. |
| 33 | newR1L-DealerMode-024 | proc | 行尾多餘句號 | 7. Check the current display page. |
| 33 | newR1L-DealerMode-024 | er | 行尾多餘句號 | 3. Sysyem Inormation page is displayed. |
| 33 | newR1L-DealerMode-024 | er | 行尾多餘句號 | 4. Return to Dealer Mode Main page. |
| 33 | newR1L-DealerMode-024 | er | 行尾多餘句號 | 5. Return to Home page. |
| 33 | newR1L-DealerMode-024 | er | 行尾多餘句號 | 6. Display Dealer Mode main page. |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 3. Press "System Information" menu item. |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 4. Press "←" button to return to previous page. |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 5. Press "Supplier Specific" menu item. |
| 34 | newR1L-DealerMode-025 | proc | 行尾多餘句號 | 6. Press "←" button to return to previous page. |
| 34 | newR1L-DealerMode-025 | er | 行尾多餘句號 | 3. Sysyem Inormation page is displayed. |
| 34 | newR1L-DealerMode-025 | er | 行尾多餘句號 | 4. Return to Dealer Mode Main page. |
| 34 | newR1L-DealerMode-025 | er | 行尾多餘句號 | 5. Supplier Specific page is displayed. |
| 34 | newR1L-DealerMode-025 | er | 行尾多餘句號 | 6. Return to Dealer Mode Main page. |
| 35 | newR1L-DealerMode-026 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 35 | newR1L-DealerMode-026 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 35 | newR1L-DealerMode-026 | proc | 行尾多餘句號 | 3. Press "System Information" menu item. |
| 35 | newR1L-DealerMode-026 | proc | 行尾多餘句號 | 4. Press "←" button to return to previous page. |
| 35 | newR1L-DealerMode-026 | er | 行尾多餘句號 | 3. Sysyem Inormation page is displayed. |
| 35 | newR1L-DealerMode-026 | er | 行尾多餘句號 | 4. Return to Dealer Mode Main page. |
| 36 | newR1L-DealerMode-027 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 36 | newR1L-DealerMode-027 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 36 | newR1L-DealerMode-027 | proc | 行尾多餘句號 | 3. Check the Currunt page display. |
| 36 | newR1L-DealerMode-027 | proc | 行尾多餘句號 | 4. Check the Music Playing status while in Dealaer Mode. |
| 36 | newR1L-DealerMode-027 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 36 | newR1L-DealerMode-027 | er | 行尾多餘句號 | 2. Display Dealer Mode page. |
| 36 | newR1L-DealerMode-027 | er | 行尾多餘句號 | 3. Dealer Mode main page is displayed. |
| 36 | newR1L-DealerMode-027 | er | 行尾多餘句號 | 4. Music shall playing normally on Dealer Mode page. |
| 37 | newR1L-DealerMode-028 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 37 | newR1L-DealerMode-028 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 37 | newR1L-DealerMode-028 | proc | 行尾多餘句號 | 3. Check the Music Playing status while in Dealaer Mode. |
| 37 | newR1L-DealerMode-028 | proc | 行尾多餘句號 | 4. Press "System Information" menu item. |
| 37 | newR1L-DealerMode-028 | proc | 行尾多餘句號 | 5. Press "Radio Information" menu item to check the information display. |
| 37 | newR1L-DealerMode-028 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 37 | newR1L-DealerMode-028 | er | 行尾多餘句號 | 2. Display Dealer Mode page. |
| 37 | newR1L-DealerMode-028 | er | 行尾多餘句號 | 3. Music shall playing normally on Dealer Mode page. |
| 37 | newR1L-DealerMode-028 | er | 行尾多餘句號 | 4. Sysyem Inormation page is displayed. |
| 38 | newR1L-DealerMode-029 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 38 | newR1L-DealerMode-029 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 39 | newR1L-DealerMode-030 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 39 | newR1L-DealerMode-030 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 39 | newR1L-DealerMode-030 | proc | 行尾多餘句號 | 4. Tap the "Back" button on the Sub-page. |
| 39 | newR1L-DealerMode-030 | er | 行尾多餘句號 | 3. A visible "Back" virtual button is present on the opened Sub-page. |
| 39 | newR1L-DealerMode-030 | er | 行尾多餘句號 | 4. Return immediately to the Main Menu without exiting Dealer Mode. |
| 40 | newR1L-DealerMode-031 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 40 | newR1L-DealerMode-031 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 40 | newR1L-DealerMode-031 | proc | 行尾多餘句號 | 4. Select Radio Part Information to check the "Hardware Part Number" field. |
| 41 | newR1L-DealerMode-032 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 41 | newR1L-DealerMode-032 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 41 | newR1L-DealerMode-032 | proc | 行尾多餘句號 | 4. Select Radio Part Information to check the "Software Version Number" field. |
| 42 | newR1L-DealerMode-033 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 42 | newR1L-DealerMode-033 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 42 | newR1L-DealerMode-033 | proc | 行尾多餘句號 | 4. Select Radio Part Information to check the "Serial Number" field. |
| 43 | newR1L-DealerMode-034 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 43 | newR1L-DealerMode-034 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 44 | newR1L-DealerMode-035 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 44 | newR1L-DealerMode-035 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 45 | newR1L-DealerMode-036 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 45 | newR1L-DealerMode-036 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 46 | newR1L-DealerMode-037 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 46 | newR1L-DealerMode-037 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 47 | newR1L-DealerMode-038 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 47 | newR1L-DealerMode-038 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 48 | newR1L-DealerMode-039 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 48 | newR1L-DealerMode-039 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 48 | newR1L-DealerMode-039 | proc | 行尾多餘句號 | 3. Select "System Information" menu to check  "Radio Part Information" infomatio |
| 49 | newR1L-DealerMode-040 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 49 | newR1L-DealerMode-040 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 49 | newR1L-DealerMode-040 | proc | 行尾多餘句號 | 4. Select "System Information" menu to check  "SDAR hardware version" field. |
| 50 | newR1L-DealerMode-041 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 50 | newR1L-DealerMode-041 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 50 | newR1L-DealerMode-041 | proc | 行尾多餘句號 | 4. Select "System Information" menu to check  "SDAR firmware version" field. |
| 51 | newR1L-DealerMode-042 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 51 | newR1L-DealerMode-042 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 51 | newR1L-DealerMode-042 | proc | 行尾多餘句號 | 4. Select "System Information" menu to check  "SDAR Audio/Traffic/Data on demand |
| 52 | newR1L-DealerMode-043 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 52 | newR1L-DealerMode-043 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 53 | newR1L-DealerMode-044 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 53 | newR1L-DealerMode-044 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 53 | newR1L-DealerMode-044 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 53 | newR1L-DealerMode-044 | er | 行尾多餘句號 | 2. Display Dealer Mode page. |
| 54 | newR1L-DealerMode-045 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 54 | newR1L-DealerMode-045 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 54 | newR1L-DealerMode-045 | proc | 行尾多餘句號 | 3. Select "System Information" menu to check "Map database version" field. |
| 54 | newR1L-DealerMode-045 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 54 | newR1L-DealerMode-045 | er | 行尾多餘句號 | 2. Display Dealer Mode page. |
| 54 | newR1L-DealerMode-045 | er | 行尾多餘句號 | 3. Map database version is displayed on system information. |
| 55 | newR1L-DealerMode-046 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 55 | newR1L-DealerMode-046 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 55 | newR1L-DealerMode-046 | proc | 行尾多餘句號 | 3. Insert a USB card storage device. |
| 55 | newR1L-DealerMode-046 | proc | 行尾多餘句號 | 4. Select "User data download" to download data to USB. |
| 55 | newR1L-DealerMode-046 | proc | 行尾多餘句號 | 5. Check the User data content on USB. |
| 55 | newR1L-DealerMode-046 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 55 | newR1L-DealerMode-046 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 55 | newR1L-DealerMode-046 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 55 | newR1L-DealerMode-046 | er | 行尾多餘句號 | 4. User data can be downloaded to USB. |
| 55 | newR1L-DealerMode-046 | er | 行尾多餘句號 | 5. User data is stored on USB. |
| 56 | newR1L-DealerMode-047 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 56 | newR1L-DealerMode-047 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 56 | newR1L-DealerMode-047 | proc | 行尾多餘句號 | 3. Insert a USB card storage device. |
| 56 | newR1L-DealerMode-047 | proc | 行尾多餘句號 | 4. Select "Copy User data to SD/USB". |
| 56 | newR1L-DealerMode-047 | proc | 行尾多餘句號 | 5. Check the "User data" content. |
| 56 | newR1L-DealerMode-047 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 56 | newR1L-DealerMode-047 | er | 行尾多餘句號 | 4. User data is downloaded. |
| 56 | newR1L-DealerMode-047 | er | 行尾多餘句號 | 5. Presets user data is stored on USB. |
| 57 | newR1L-DealerMode-048 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 57 | newR1L-DealerMode-048 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 57 | newR1L-DealerMode-048 | proc | 行尾多餘句號 | 3. Insert a USB storage device. |
| 57 | newR1L-DealerMode-048 | proc | 行尾多餘句號 | 4. Select "Copy User data to SD/USB". |
| 57 | newR1L-DealerMode-048 | proc | 行尾多餘句號 | 5. Check the "User data" content. |
| 57 | newR1L-DealerMode-048 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 57 | newR1L-DealerMode-048 | er | 行尾多餘句號 | 4. User data is downloaded. |
| 57 | newR1L-DealerMode-048 | er | 行尾多餘句號 | 5. SXM Favorites is stored on USB. |
| 58 | newR1L-DealerMode-049 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 58 | newR1L-DealerMode-049 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 58 | newR1L-DealerMode-049 | proc | 行尾多餘句號 | 3. Insert a USB storage device. |
| 58 | newR1L-DealerMode-049 | proc | 行尾多餘句號 | 4. Select "Download User EQ Settings to SD/USB". |
| 58 | newR1L-DealerMode-049 | proc | 行尾多餘句號 | 5. Check the "EQ Settings" content. |
| 58 | newR1L-DealerMode-049 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 58 | newR1L-DealerMode-049 | er | 行尾多餘句號 | 4. EQ Settings is downloaded. |
| 58 | newR1L-DealerMode-049 | er | 行尾多餘句號 | 5. Driver User EQ Settings is stored on USB. |
| 59 | newR1L-DealerMode-050 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 59 | newR1L-DealerMode-050 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 59 | newR1L-DealerMode-050 | proc | 行尾多餘句號 | 3. Insert a USB storage device. |
| 59 | newR1L-DealerMode-050 | proc | 行尾多餘句號 | 4. Select "Restore User Data from SD/USB" to check the Restore Process. |
| 59 | newR1L-DealerMode-050 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 59 | newR1L-DealerMode-050 | er | 行尾多餘句號 | 4. Pop up "No USB Device connected" notification. |
| 60 | newR1L-DealerMode-051 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 60 | newR1L-DealerMode-051 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 60 | newR1L-DealerMode-051 | proc | 行尾多餘句號 | 3. Insert a USB storage device. |
| 60 | newR1L-DealerMode-051 | proc | 行尾多餘句號 | 4. Select "Restore User Data from SD/USB" to check the Restore Process. |
| 60 | newR1L-DealerMode-051 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 60 | newR1L-DealerMode-051 | er | 行尾多餘句號 | 4. Pop up "Competible file not found" notification. |
| 61 | newR1L-DealerMode-052 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 61 | newR1L-DealerMode-052 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 61 | newR1L-DealerMode-052 | proc | 行尾多餘句號 | 3. Insert a USB storage device. |
| 61 | newR1L-DealerMode-052 | proc | 行尾多餘句號 | 4. Select "Restore User Data from SD/USB" to check the Restore Process. |
| 61 | newR1L-DealerMode-052 | er | 行尾多餘句號 | 3. The USB storage device is detected by the system. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 1.  Factory Reset HU. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 2. Open "Radio" page to check the Radio Preset Section. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 3. Press H/K [Screen off] button to turn off the HU screen. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 4. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 5. Insert a USB storage device. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 6. Select "Restore User Data from SD/USB" to import the User Data (Preset Data)  |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 7. Press "X" button to exit Dealer Mode. |
| 62 | newR1L-DealerMode-053 | proc | 行尾多餘句號 | 8. Open "Radio" page to check the Radio Preset Section. |
| 62 | newR1L-DealerMode-053 | er | 行尾多餘句號 | 1. User Data has been reset. |
| 62 | newR1L-DealerMode-053 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 62 | newR1L-DealerMode-053 | er | 行尾多餘句號 | 6. User Data Restore completed. |
| 62 | newR1L-DealerMode-053 | er | 行尾多餘句號 | 7. Return to Home page. |
| 62 | newR1L-DealerMode-053 | er | 行尾多餘句號 | 8. The "Blank" preset has been changed to" FM87.7". |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 1.  Factory Reset HU. |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 2. Press "Apps" on menu bar. |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 3. Press "Favorites" category to check the default Favortes apps. |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 4. Press H/K [Screen off] button to turn off the HU screen. |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 5. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 6. Insert a USB storage device. |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 7. Select "Restore User Data from SD/USB" to import the User Data (Favorites dat |
| 63 | newR1L-DealerMode-054 | proc | 行尾多餘句號 | 8. Open app drawer to check the Favorite section. |
| 63 | newR1L-DealerMode-054 | er | 行尾多餘句號 | 1. User Data has been reset. |
| 63 | newR1L-DealerMode-054 | er | 行尾多餘句號 | 2. App Drawer page is displayed. |
| 63 | newR1L-DealerMode-054 | er | 行尾多餘句號 | 6. The USB storage device is detected by the system. |
| 63 | newR1L-DealerMode-054 | er | 行尾多餘句號 | 7. User Data Restore completed. |
| 63 | newR1L-DealerMode-054 | er | 行尾多餘句號 | 8. The "Tire Pressure" apps is added on Favorite section. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 1.  Factory Reset HU. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 2. Press "Vehicle Settings" on menu bar. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 3. Press "Audio" tab. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 4. Press "Equalizer" menu item to check the default Audio Equalizer. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 5. Press H/K [Screen off] button to turn off the HU screen. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 6. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 7. Insert a USB storage device. |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 8. Select "Restore User Data from SD/USB" to import the User Data (EQ Settings)  |
| 64 | newR1L-DealerMode-055 | proc | 行尾多餘句號 | 9. Press "X" button to exit Dealer Mode. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 1. User Data has been reset. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 2. Settings page is displayed. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 3. Audio settings page is displayed. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 6. Dealer Mode page is displayed. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 7. The USB storage device is detected by the system. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 8. User Data Restore completed. |
| 64 | newR1L-DealerMode-055 | er | 行尾多餘句號 | 9. Return to Audio Settings page. |
| 65 | newR1L-DealerMode-056 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 65 | newR1L-DealerMode-056 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 65 | newR1L-DealerMode-056 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 65 | newR1L-DealerMode-056 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 65 | newR1L-DealerMode-056 | proc | 行尾多餘句號 | 3. Check Screenshot in USB. |
| 65 | newR1L-DealerMode-056 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 65 | newR1L-DealerMode-056 | er | 行尾多餘句號 | 2. Display Screenshot successful pop up. |
| 65 | newR1L-DealerMode-056 | er | 行尾多餘句號 | 3. The Screenshot is saved to the USB. |
| 66 | newR1L-DealerMode-057 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 66 | newR1L-DealerMode-057 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 66 | newR1L-DealerMode-057 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 66 | newR1L-DealerMode-057 | proc | 行尾多餘句號 | b. Press H/K[MUTE] within 3 seconds after Step a. |
| 66 | newR1L-DealerMode-057 | proc | 行尾多餘句號 | 3. Check System log in USB. |
| 66 | newR1L-DealerMode-057 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 66 | newR1L-DealerMode-057 | er | 行尾多餘句號 | 2. Display Screenshot successful pop up. |
| 66 | newR1L-DealerMode-057 | er | 行尾多餘句號 | 3. The System log is saved to the USB. |
| 67 | newR1L-DealerMode-058 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 67 | newR1L-DealerMode-058 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 67 | newR1L-DealerMode-058 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 67 | newR1L-DealerMode-058 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 67 | newR1L-DealerMode-058 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 67 | newR1L-DealerMode-058 | er | 行尾多餘句號 | 2. The screenshot is saved to the USB within 5 seconds. |
| 68 | newR1L-DealerMode-059 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 68 | newR1L-DealerMode-059 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 68 | newR1L-DealerMode-059 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 68 | newR1L-DealerMode-059 | proc | 行尾多餘句號 | b. Press H/K[MUTE] within 3 seconds after Step a. |
| 68 | newR1L-DealerMode-059 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 68 | newR1L-DealerMode-059 | er | 行尾多餘句號 | 2. The System Log is saved to the USB within 5 seconds. |
| 69 | newR1L-DealerMode-060 | proc | 行尾多餘句號 | 1. Insert USB to HU. |
| 69 | newR1L-DealerMode-060 | er | 行尾多餘句號 | 1. The Log write process start within 2 secs. |
| 70 | newR1L-DealerMode-061 | proc | 行尾多餘句號 | 1. Insert USB to HU. |
| 70 | newR1L-DealerMode-061 | proc | 行尾多餘句號 | 2. Wait for 10 secs. |
| 70 | newR1L-DealerMode-061 | er | 行尾多餘句號 | 1. The Log write process start within 2 secs. |
| 70 | newR1L-DealerMode-061 | er | 行尾多餘句號 | 2. The Log write process shall finish within 10 secs. |
| 71 | newR1L-DealerMode-062 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 71 | newR1L-DealerMode-062 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 71 | newR1L-DealerMode-062 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 71 | newR1L-DealerMode-062 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 71 | newR1L-DealerMode-062 | proc | 行尾多餘句號 | 3. Check the image format of the saved screenshot. |
| 71 | newR1L-DealerMode-062 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 71 | newR1L-DealerMode-062 | er | 行尾多餘句號 | 2. Display Screenshot successful pop up. |
| 71 | newR1L-DealerMode-062 | er | 行尾多餘句號 | 3. The saved screenshot file's format is one of the acceptable types: BMP, PNG,  |
| 72 | newR1L-DealerMode-063 | pre | 行尾多餘句號 | 1. USB drive that includes the __getSnapshotToUSB file. |
| 72 | newR1L-DealerMode-063 | proc | 行尾多餘句號 | 1. Insert a USB storage device. |
| 72 | newR1L-DealerMode-063 | proc | 行尾多餘句號 | a. Hold H/K[POWER] for 2 secs. |
| 72 | newR1L-DealerMode-063 | proc | 行尾多餘句號 | b. Press H/K [MUTE] for 1 sec within 3 secs after Step a. |
| 72 | newR1L-DealerMode-063 | proc | 行尾多餘句號 | 3. Check the image format of the saved screenshot. |
| 72 | newR1L-DealerMode-063 | er | 行尾多餘句號 | 1. The USB storage device is detected by the system. |
| 72 | newR1L-DealerMode-063 | er | 行尾多餘句號 | 2. Display Screenshot successful pop up. |
| 72 | newR1L-DealerMode-063 | er | 行尾多餘句號 | 3. Make sure the file name includes the date and time of capture. |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 4. Turn on "Showroom Demo Mode". |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 5. Press "X" button to exit Dealer Mode. |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 6. Click  App drawer on menu bar. |
| 73 | newR1L-DealerMode-064 | proc | 行尾多餘句號 | 7. Check the Showroom Demo app. |
| 73 | newR1L-DealerMode-064 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 73 | newR1L-DealerMode-064 | er | 行尾多餘句號 | 4. "Showroom Demo Mode" is checked. |
| 73 | newR1L-DealerMode-064 | er | 行尾多餘句號 | 5. Return to Home page. |
| 73 | newR1L-DealerMode-064 | er | 行尾多餘句號 | 6. App drawer page is displayed. |
| 73 | newR1L-DealerMode-064 | er | 行尾多餘句號 | 7. Showroom Demo app is enabled. |
| 74 | newR1L-DealerMode-065 | pre | 行尾多餘句號 | 1. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 4. Turn off "Showroom Demo Mode". |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 5. Press "X" button to exit Dealer Mode. |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 6. Click  App drawer on menu bar. |
| 74 | newR1L-DealerMode-065 | proc | 行尾多餘句號 | 7. Check the Showroom Demo app. |
| 74 | newR1L-DealerMode-065 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 74 | newR1L-DealerMode-065 | er | 行尾多餘句號 | 4. "Showroom Demo Mode" is unchecked. |
| 74 | newR1L-DealerMode-065 | er | 行尾多餘句號 | 5. Return to Home page. |
| 74 | newR1L-DealerMode-065 | er | 行尾多餘句號 | 6. App drawer page is displayed. |
| 74 | newR1L-DealerMode-065 | er | 行尾多餘句號 | 7. Showroom Demo app is disabled. |
| 75 | newR1L-DealerMode-066 | pre | 行尾多餘句號 | 1. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 75 | newR1L-DealerMode-066 | pre | 行尾多餘句號 | 2. Connect a USB drive that includes the valid Showroom demo video file. |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 6. Tap "X" to exit Dealer Mode. |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 7. Select App Drawer. |
| 75 | newR1L-DealerMode-066 | proc | 行尾多餘句號 | 8. Select "Showroom Demo Video" app to check the uploaded video. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 5. A success message popup shall appear after the upload finishes. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 6. Return to Home page. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 7. App Drawer page is displayed. |
| 75 | newR1L-DealerMode-066 | er | 行尾多餘句號 | 8. The video file uploaded from the USB shall be present and playable on the Sho |
| 76 | newR1L-DealerMode-067 | pre | 行尾多餘句號 | 1. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 76 | newR1L-DealerMode-067 | pre | 行尾多餘句號 | 2. Connect a USB drive that includes the invalid video file. |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 6. Tap "X" button to exit Dealer Mode. |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 7. Select App Drawer. |
| 76 | newR1L-DealerMode-067 | proc | 行尾多餘句號 | 8. Select "Showroom Demo Video" App to check whether the video exists. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 5. A fail message popup shall appear during the upload process. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 6. Return to Home page. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 7. App Drawer page is displayed. |
| 76 | newR1L-DealerMode-067 | er | 行尾多餘句號 | 8. Showroom Demo video was not uploaded on Showroom Demo video page. |
| 77 | newR1L-DealerMode-068 | pre | 行尾多餘句號 | 2. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 6. Tap "X" button to exit Dealer Mode. |
| 77 | newR1L-DealerMode-068 | proc | 行尾多餘句號 | 7. Select the "Showroom Demo Video" app to check whether the video exists. |
| 77 | newR1L-DealerMode-068 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 77 | newR1L-DealerMode-068 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 77 | newR1L-DealerMode-068 | er | 行尾多餘句號 | 5. A success message popup shall appear after the upload finishes. |
| 77 | newR1L-DealerMode-068 | er | 行尾多餘句號 | 6. Return to Home page. |
| 77 | newR1L-DealerMode-068 | er | 行尾多餘句號 | 7. The uploaded video which is less than 200MB shall be present and playable. |
| 78 | newR1L-DealerMode-069 | pre | 行尾多餘句號 | 1. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 6. Tap "X" button to exit Dealer Mode. |
| 78 | newR1L-DealerMode-069 | proc | 行尾多餘句號 | 7. Select the "Showroom Demo Video" app to check whether the video exists. |
| 78 | newR1L-DealerMode-069 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 78 | newR1L-DealerMode-069 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 78 | newR1L-DealerMode-069 | er | 行尾多餘句號 | 5. A success message popup shall appear after the upload finishes. |
| 78 | newR1L-DealerMode-069 | er | 行尾多餘句號 | 6. Return to Home page. |
| 78 | newR1L-DealerMode-069 | er | 行尾多餘句號 | 7. The uploaded video which is equal to 200MB shall be present and playable. |
| 79 | newR1L-DealerMode-070 | pre | 行尾多餘句號 | 1. "Showroom Demo Mode" is enabled in Dealer Mode settings. |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 6. Tap "X" button to exit Dealer Mode. |
| 79 | newR1L-DealerMode-070 | proc | 行尾多餘句號 | 7. Select the "Showroom Demo Video" app to check whether the video exists. |
| 79 | newR1L-DealerMode-070 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 79 | newR1L-DealerMode-070 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 79 | newR1L-DealerMode-070 | er | 行尾多餘句號 | 5. A fail message popup shall appear during the upload process. |
| 79 | newR1L-DealerMode-070 | er | 行尾多餘句號 | 6. Return to Home page. |
| 79 | newR1L-DealerMode-070 | er | 行尾多餘句號 | 7. The uploaded video which is larger than 200MB shall not be present on Showroo |
| 80 | newR1L-DealerMode-071 | pre | 行尾多餘句號 | 2. Connect a USB drive that includes the valid Showroom demo video file. |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 5. Select "Upload the Showroom Demo Video from USB" to upload the Video to Showr |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 6. Tap "X" button to exit Dealer Mode. |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 7. Select the "Showroom Demo Video" app to check whether the video exists. |
| 80 | newR1L-DealerMode-071 | proc | 行尾多餘句號 | 8. Select the uploaded video to check the Demo Video loads and play normally. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 5. A success message popup shall appear after the upload finishes. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 6. Return to Home page. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 7. The uploaded video be present on Showroom demo video page. |
| 80 | newR1L-DealerMode-071 | er | 行尾多餘句號 | 8. The uploaded video shall load and play without error. |
| 81 | newR1L-DealerMode-072 | pre | 行尾多餘句號 | 2. A valid Demo Video is uploaded in File Browser and plays normally. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 1. Press Vehicle Setting on menu bar. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 2. Select the "Reset" tab. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 3. Select "Clear Personal Data". |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 4. Select "Yes" button to clear the personal data. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 5. Select App Drawer on menu bar. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 6. Select "Showroom Demo Mode" app. |
| 81 | newR1L-DealerMode-072 | proc | 行尾多餘句號 | 7. Check the Demo Video status. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 1. Vehicle Setting page is displayed. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 2. "Reset" category is displayed. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 3. Pop up message to inform user whether to Clear Data. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 4. A success message popup shall appear after the Data message cleared. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 5. App Drawer page is displayed. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 6. Launch Showroom Demo app. |
| 81 | newR1L-DealerMode-072 | er | 行尾多餘句號 | 7. The uploaded Demo Video has been removed. |
| 82 | newR1L-DealerMode-073 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 1. Press Vehicle Setting on menu bar. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 2. Select the "Reset" tab. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 3. Select "Clear Personal Data". |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 4. Select "Yes" button to start the clear the personal data. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 5. While the clearing process is in progress, force reboot the HU. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 6. After the HU reboots, open the App Drawer. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 7. Launch the Showroom Demo Mode app. |
| 82 | newR1L-DealerMode-073 | proc | 行尾多餘句號 | 8. Check the Demo Video status. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 1. Vehicle Setting page is displayed. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 2. "Reset" category is displayed. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 3. Pop up message to inform user whether to Clear Data. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 4. The Clear Personal Data process starts after confirmation. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 5. HU reboots normally without errors. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 6. App Drawer opens successfully. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 7. Showroom Demo Mode app launches normally. |
| 82 | newR1L-DealerMode-073 | er | 行尾多餘句號 | 8. The uploaded Demo Video has been removed; no video is available for playback. |
| 83 | newR1L-DealerMode-074 | pre | 行尾多餘句號 | 2. A valid Demo Video is uploaded in File Browser and plays normally. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 1. Press Vehicle Setting on menu bar. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 2. Select the "Reset" tab. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 3. Select "Clear Personal Data". |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 4. Select "Yes" button to start the clear the personal data. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 5. Reboot the HU. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 6. After reboot, open the App Drawer. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 7. Launch the Showroom Demo Mode app. |
| 83 | newR1L-DealerMode-074 | proc | 行尾多餘句號 | 8. Check the Demo Video status. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 1. Vehicle Setting page is displayed. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 2. "Reset" category is displayed. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 3. Pop up message to inform user whether to Clear Data. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 4. The Personal Data is cleared. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 5. HU reboots normally without errors. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 6. App Drawer opens successfully. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 7. Showroom Demo Mode app launches normally. |
| 83 | newR1L-DealerMode-074 | er | 行尾多餘句號 | 8. The uploaded Demo Video has been removed; no video is available for playback. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 4. Check the "Showroom Demo Mode" function is Enabled. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 5. Press Vehicle Setting on menu bar. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 6. Select the "Reset" tab. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 7. Select "Clear Personal Data". |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 8. Select "Yes" button to start the clear the personal data. |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 9. Open Showroom Demo Mode settings page again to check the function is disabled |
| 84 | newR1L-DealerMode-075 | proc | 行尾多餘句號 | 10. Exit Dealer Mode and Check Showroom demo app is disabled on App Drawer page. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 5. Vehicle Setting page is displayed. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 6. "Reset" category is displayed. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 7. Pop up message to inform user whether to Clear Data. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 8. The Personal Data is cleared. |
| 84 | newR1L-DealerMode-075 | er | 行尾多餘句號 | 10. Showroom demo app is disabled on App Drawer page. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 4. Check the "Showroom Demo Mode" function is Enabled. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 5. Reboot the HU. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 6. Launch Dealer Mode again. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 7. Check the "Showroom Demo Mode" function is Enabled after reboot. |
| 85 | newR1L-DealerMode-076 | proc | 行尾多餘句號 | 8. Exit Dealer Mode and Check Showroom demo app is enabled on App Drawer page. |
| 85 | newR1L-DealerMode-076 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 85 | newR1L-DealerMode-076 | er | 行尾多餘句號 | 5. HU reboots normally without errors. |
| 85 | newR1L-DealerMode-076 | er | 行尾多餘句號 | 8. Showroom demo app is enabled on App Drawer page. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 3. Check the function that do not rely on personal data is enabled. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 4. Press Vehicle Setting on menu bar. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 5. Select the "Reset" tab. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 6. Select "Clear Personal Data". |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 7. Select "Yes" button to start the clear the personal data. |
| 86 | newR1L-DealerMode-077 | proc | 行尾多餘句號 | 8. Open Dealer Mode to check the function that do not rely on personal data is e |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 3. The function that do not rely on personal data is enabled. |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 4. Vehicle Setting page is displayed. |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 5. "Reset" category is displayed. |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 6. Pop up message to inform user whether to Clear Data. |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 7. The Personal Data is cleared. |
| 86 | newR1L-DealerMode-077 | er | 行尾多餘句號 | 8. The function that do not rely on personal data is enabled. |
| 87 | newR1L-DealerMode-078 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 6. Click  App drawer on menu bar. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 7. Click "Showroom Demo Mode" app. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 8. Select and start the Showroom Demo Video. |
| 87 | newR1L-DealerMode-078 | proc | 行尾多餘句號 | 9. During video playback, attempt to click the "Exit" / "Home" button to exit th |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to enabled. |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 6. App drawer page is displayed. |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 7. Showroom Demo app launches. |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 8. The demo video loads and plays normally. |
| 87 | newR1L-DealerMode-078 | er | 行尾多餘句號 | 9. User cannot manually exit or interrupt the video playback. |
| 88 | newR1L-DealerMode-079 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 6. Click  App drawer on menu bar. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 7. Click "Showroom Demo Mode" app. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 8. Select and start the Showroom Demo Video. |
| 88 | newR1L-DealerMode-079 | proc | 行尾多餘句號 | 9. Wait for the video playback to finish, then manually exit. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to enabled. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 6. App drawer page is displayed. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 7. Showroom Demo app launches. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 8. The demo video loads and plays normally. |
| 88 | newR1L-DealerMode-079 | er | 行尾多餘句號 | 9. Return to the last HU screen. |
| 89 | newR1L-DealerMode-080 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 6. Click  App drawer on menu bar. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 7. Click "Showroom Demo Mode" app. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 8. Select and start the Showroom Demo Video. |
| 89 | newR1L-DealerMode-080 | proc | 行尾多餘句號 | 9. During video playback, attempt to click the "Exit" / "Home" button to exit th |
| 89 | newR1L-DealerMode-080 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to disabled. |
| 89 | newR1L-DealerMode-080 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 89 | newR1L-DealerMode-080 | er | 行尾多餘句號 | 6. App drawer page is displayed. |
| 89 | newR1L-DealerMode-080 | er | 行尾多餘句號 | 7. Showroom Demo app launches. |
| 89 | newR1L-DealerMode-080 | er | 行尾多餘句號 | 8. The demo video loads and plays normally. |
| 90 | newR1L-DealerMode-081 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 6. Open App Drawer and launch "Showroom Demo" app. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 7. Select the Showroom Demo Video. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 8. Enable Repeat / Loop playback. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 9. Start video playback. |
| 90 | newR1L-DealerMode-081 | proc | 行尾多餘句號 | 10. During playback, press "Exit"/"/Home" to exit. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to enabled. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 6. Showroom Demo app launches. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 7. Showroom Demo Video is loaded and ready for playback. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 8. Repeat / Loop playback is enabled for the selected video. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 9. The demo video starts playing successfully. |
| 90 | newR1L-DealerMode-081 | er | 行尾多餘句號 | 10. The video remains in playback, and no exit action is triggered. |
| 91 | newR1L-DealerMode-082 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 6. Open App Drawer and launch "Showroom Demo" app. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 7. Select the Showroom Demo Video. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 8. Enable Repeat / Loop playback. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 9. Start video playback. |
| 91 | newR1L-DealerMode-082 | proc | 行尾多餘句號 | 10. During playback, press "Exit"/"/Home" to exit. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to disabled. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 6. Showroom Demo app launches. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 7. Showroom Demo Video is loaded and ready for playback. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 8. Repeat / Loop playback is enabled for the selected video. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 9. The demo video starts playing successfully. |
| 91 | newR1L-DealerMode-082 | er | 行尾多餘句號 | 10. Return to the last HU screen. |
| 92 | newR1L-DealerMode-083 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 6. Open App Drawer and launch "Showroom Demo" app. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 7. Select the Showroom Demo Video. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 8. Enable Repeat / Loop playback. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 9. Start video playback. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 10. During playback, Disable Repeat / Loop playback. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 11. Wait for the video playback to finish. |
| 92 | newR1L-DealerMode-083 | proc | 行尾多餘句號 | 12. Press "Exit" / "Home" button to exit the Video. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to enabled. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 6. Showroom Demo app launches. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 7. Showroom Demo Video is loaded and ready for playback. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 8. Repeat / Loop playback is enabled for the selected video. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 9. The demo video starts playing successfully. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 10. Repeat / Loop playback is disabled for the selected video. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 11. Playback is completed and stay on playback page. |
| 92 | newR1L-DealerMode-083 | er | 行尾多餘句號 | 12. User cannot manually exit the video playback. |
| 93 | newR1L-DealerMode-084 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 5. Tap "X" button to exit Dealer Mode. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 6. Open App Drawer and launch "Showroom Demo" app. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 7. Select the Showroom Demo Video. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 8. Enable Repeat / Loop playback. |
| 93 | newR1L-DealerMode-084 | proc | 行尾多餘句號 | 9. Launch Dealer Mode during Video playback is playing. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 4. "Not allow user to exit the Video" option is set to enabled. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 5. Return to Home Page. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 6. Showroom Demo app launches. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 7. Showroom Demo Video is loaded and ready for playback. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 8. Repeat / Loop playback is enabled for the selected video. |
| 93 | newR1L-DealerMode-084 | er | 行尾多餘句號 | 9. Exit the Demo video and Dealer Mode page is displayed. |
| 94 | newR1L-DealerMode-085 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .mp4 video file. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 7. Select the .mp4 video file and confirm upload. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 94 | newR1L-DealerMode-085 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .mp4 video. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 7. The selected .mp4 video file is accepted for upload. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 94 | newR1L-DealerMode-085 | er | 行尾多餘句號 | 10. The uploaded .mp4 video is displayed and playback starts successfully. |
| 95 | newR1L-DealerMode-086 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .avi video file. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 7. Select the .avi video file and confirm upload. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 95 | newR1L-DealerMode-086 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .avi video. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 7. The selected .avi video file is accepted for upload. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 95 | newR1L-DealerMode-086 | er | 行尾多餘句號 | 10. The uploaded .avi video is displayed and playback starts successfully. |
| 96 | newR1L-DealerMode-087 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .mpg video file. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 7. Select the .mpg video file and confirm upload. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 96 | newR1L-DealerMode-087 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .mpg video. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 7. The selected .mpg video file is accepted for upload. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 96 | newR1L-DealerMode-087 | er | 行尾多餘句號 | 10. The uploaded .mpg video is displayed and playback starts successfully. |
| 97 | newR1L-DealerMode-088 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .wmv video file. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 7. Select the .wmv video file and confirm upload. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 97 | newR1L-DealerMode-088 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .wmv video. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 7. The selected .wmv video file is accepted for upload. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 97 | newR1L-DealerMode-088 | er | 行尾多餘句號 | 10. The uploaded .wmv video is displayed and playback starts successfully. |
| 98 | newR1L-DealerMode-089 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .3gp video file. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 7. Select the .3gp video file and confirm upload. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 98 | newR1L-DealerMode-089 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .3gp video. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 7. The selected .3gp video file is accepted for upload. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 98 | newR1L-DealerMode-089 | er | 行尾多餘句號 | 10. The uploaded .3gp video is displayed and playback starts successfully. |
| 99 | newR1L-DealerMode-090 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mp4, .avi, .mpg, |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 1.Press H/K [Screen Off] button to turn off the screen. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 3. Select “Showroom Demo Mode information”. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 4. Select “File Browser”. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .mkv video file. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 7. Select the .mkv video file and confirm upload. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 99 | newR1L-DealerMode-090 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” and start playback of the uploaded .mkv video. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 1. The screen is turned off. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 3. Showroom Demo Mode information page is displayed. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 4. File Browser page is displayed. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 7. The selected .mkv video file is accepted for upload. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 99 | newR1L-DealerMode-090 | er | 行尾多餘句號 | 10. The uploaded .mkv video is displayed and playback starts successfully. |
| 100 | newR1L-DealerMode-091 | pre | 行尾多餘句號 | 1. A USB device containing video files with supported formats (.mov) is prepared |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 4. Select "File Browser". |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 5. Insert a USB storage device containing a .mov video file. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 6. Select “Upload Showroom Demo Video from USB”. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 7. Select the .mov video file and confirm upload. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 8. Tap “X” to exit Dealer Mode. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 9. Open App Drawer. |
| 100 | newR1L-DealerMode-091 | proc | 行尾多餘句號 | 10. Select “Showroom Demo Video” app to check whether the .mov video exists. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 4. File Browser interface is displayed. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 5. The USB storage device is detected by the system. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 6. The upload option for Showroom Demo Video is available and selectable. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 7. A fail message popup shall appear during the upload process and return previo |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 8. Dealer Mode is exited and the previous screen is displayed. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 9.App Drawer page is displayed. |
| 100 | newR1L-DealerMode-091 | er | 行尾多餘句號 | 10. Showroom Demo video (.mov) was not uploaded on Showroom Demo video page. |
| 101 | newR1L-DealerMode-092 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 4. Select and start the Showroom Demo Video. |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF while the demo video is playing or after playback h |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON. |
| 101 | newR1L-DealerMode-092 | proc | 行尾多餘句號 | 7. Check that the no demo video playback is triggered automatically after system |
| 101 | newR1L-DealerMode-092 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 101 | newR1L-DealerMode-092 | er | 行尾多餘句號 | 4. The demo video loads and plays normally. |
| 101 | newR1L-DealerMode-092 | er | 行尾多餘句號 | 6. Dealer Mode Main page is displayed. |
| 101 | newR1L-DealerMode-092 | er | 行尾多餘句號 | 7. Demo video playback state is reset and does not resume automatically. |
| 102 | newR1L-DealerMode-093 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 4. Select and start the Showroom Demo Video. |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF while the demo video is playing or after playback h |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON. |
| 102 | newR1L-DealerMode-093 | proc | 行尾多餘句號 | 7. Check if the initial screen displayed after system startup is the Dealer Mode |
| 102 | newR1L-DealerMode-093 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 102 | newR1L-DealerMode-093 | er | 行尾多餘句號 | 4. The demo video loads and plays normally. |
| 102 | newR1L-DealerMode-093 | er | 行尾多餘句號 | 6. Dealer Mode page is displayed. |
| 102 | newR1L-DealerMode-093 | er | 行尾多餘句號 | 7. The Dealer Mode Main screen is displayed after system startup, and no demo vi |
| 103 | newR1L-DealerMode-094 | pre | 行尾多餘句號 | 1. A valid Demo Video is uploaded in File Browser and plays normally. |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 3. Select "Showroom Demo Mode information". |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 4. Select and start the Showroom Demo Video. |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF while the demo video is playing or after playback h |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON. |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 7. Repeat ignition OFF/ON cycle once more. |
| 103 | newR1L-DealerMode-094 | proc | 行尾多餘句號 | 8. Check if any demo video playback session state is retained after each ignitio |
| 103 | newR1L-DealerMode-094 | er | 行尾多餘句號 | 3. Showroom demo mode information page is displayed. |
| 103 | newR1L-DealerMode-094 | er | 行尾多餘句號 | 4. The demo video loads and plays normally. |
| 103 | newR1L-DealerMode-094 | er | 行尾多餘句號 | 6. Dealer Mode page is displayed. |
| 103 | newR1L-DealerMode-094 | er | 行尾多餘句號 | 7. System starts up successfully after the repeated ignition cycle. |
| 103 | newR1L-DealerMode-094 | er | 行尾多餘句號 | 8. No demo video playback session state is retained across ignition cycles. |
| 104 | newR1L-DealerMode-095 | pre | 行尾多餘句號 | 1. Wifi is connected. |
| 104 | newR1L-DealerMode-095 | pre | 行尾多餘句號 | 2. Certificate server is available and responds successfully. |
| 104 | newR1L-DealerMode-095 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 104 | newR1L-DealerMode-095 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 104 | newR1L-DealerMode-095 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 104 | newR1L-DealerMode-095 | proc | 行尾多餘句號 | 4. Select "ECU ID Certificate from Server" to trigger certificate download. |
| 104 | newR1L-DealerMode-095 | proc | 行尾多餘句號 | 5. Check the result indication displayed for the ECU ID Certificate download ope |
| 104 | newR1L-DealerMode-095 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 104 | newR1L-DealerMode-095 | er | 行尾多餘句號 | 4. ECU ID Certificate download process is executed successfully. |
| 104 | newR1L-DealerMode-095 | er | 行尾多餘句號 | 5. A visible Pass result indication is displayed on the screen. |
| 105 | newR1L-DealerMode-096 | pre | 行尾多餘句號 | 1. Wifi is connected. |
| 105 | newR1L-DealerMode-096 | pre | 行尾多餘句號 | 2. Certificate server is available and responds successfully. |
| 105 | newR1L-DealerMode-096 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 105 | newR1L-DealerMode-096 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 105 | newR1L-DealerMode-096 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 105 | newR1L-DealerMode-096 | proc | 行尾多餘句號 | 4. Select "ECU ID Certificate from Server" to trigger certificate download. |
| 105 | newR1L-DealerMode-096 | proc | 行尾多餘句號 | 5. Check the result indication displayed for the ECU ID Certificate download ope |
| 105 | newR1L-DealerMode-096 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 105 | newR1L-DealerMode-096 | er | 行尾多餘句號 | 4. ECU ID Certificate download process is executed and fails as expected. |
| 105 | newR1L-DealerMode-096 | er | 行尾多餘句號 | 5. A visible Fail result indication is displayed on the screen. |
| 106 | newR1L-DealerMode-097 | pre | 行尾多餘句號 | 1. A valid ECU ID Certificate file is available for import. |
| 106 | newR1L-DealerMode-097 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 106 | newR1L-DealerMode-097 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 106 | newR1L-DealerMode-097 | proc | 行尾多餘句號 | 4. Insert a USB device with a valid ECU ID Certificate. |
| 106 | newR1L-DealerMode-097 | proc | 行尾多餘句號 | 6. Press "Import ECU ID Certificate from USB" button. |
| 106 | newR1L-DealerMode-097 | proc | 行尾多餘句號 | 7. Check the result indication displayed for the import operation. |
| 106 | newR1L-DealerMode-097 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 106 | newR1L-DealerMode-097 | er | 行尾多餘句號 | 4. USB device is detected successfully. |
| 106 | newR1L-DealerMode-097 | er | 行尾多餘句號 | 5. The "Import ECU ID Certificate from USB" function is available and selectable |
| 106 | newR1L-DealerMode-097 | er | 行尾多餘句號 | 6. The ECU ID Certificate import operation is triggered successfully. |
| 106 | newR1L-DealerMode-097 | er | 行尾多餘句號 | 7. A Pass result indication with the message "Import ECU Certificate Success" is |
| 107 | newR1L-DealerMode-098 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 107 | newR1L-DealerMode-098 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 107 | newR1L-DealerMode-098 | proc | 行尾多餘句號 | 4. Insert a USB storage device. |
| 107 | newR1L-DealerMode-098 | proc | 行尾多餘句號 | 7. Check the result indication displayed for the export operation. |
| 107 | newR1L-DealerMode-098 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 107 | newR1L-DealerMode-098 | er | 行尾多餘句號 | 4. USB device is detected successfully. |
| 107 | newR1L-DealerMode-098 | er | 行尾多餘句號 | 5. The "Export ECU ID Certificate to USB" function is available and selectable. |
| 107 | newR1L-DealerMode-098 | er | 行尾多餘句號 | 6. The ECU ID Certificate export operation is triggered successfully. |
| 107 | newR1L-DealerMode-098 | er | 行尾多餘句號 | 7. A Pass result indication with the message "Export ECU Certificate Success" is |
| 108 | newR1L-DealerMode-099 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 108 | newR1L-DealerMode-099 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 108 | newR1L-DealerMode-099 | proc | 行尾多餘句號 | 3. Press "ECU ID Certificate Management". |
| 108 | newR1L-DealerMode-099 | proc | 行尾多餘句號 | 5. Press "Import ECU ID Certificate from USB" button without USB connected. |
| 108 | newR1L-DealerMode-099 | proc | 行尾多餘句號 | 6.  Check the result indication displayed for the import operation. |
| 108 | newR1L-DealerMode-099 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 108 | newR1L-DealerMode-099 | er | 行尾多餘句號 | 5. The ECU ID Certificate import operation is triggered successfully and fails a |
| 108 | newR1L-DealerMode-099 | er | 行尾多餘句號 | 6. A Fail result indication with the message "Import ECU Certificate Failed" is  |
| 109 | newR1L-DealerMode-100 | pre | 行尾多餘句號 | 1. An invalid ECU ID Certificate file is available for import. |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 3. Press "ECU ID Certificate Management". |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 4. Insert a USB device with an invalid ECU ID Certificate. |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 6. Press "Import ECU ID Certificate from USB" button without USB connected. |
| 109 | newR1L-DealerMode-100 | proc | 行尾多餘句號 | 7.  Check the result indication displayed for the import operation. |
| 109 | newR1L-DealerMode-100 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 109 | newR1L-DealerMode-100 | er | 行尾多餘句號 | 4. USB device is detected successfully. |
| 109 | newR1L-DealerMode-100 | er | 行尾多餘句號 | 6. The ECU ID Certificate import operation is triggered successfully and fails a |
| 109 | newR1L-DealerMode-100 | er | 行尾多餘句號 | 7. A Fail result indication with the message "Import ECU Certificate Failed" is  |
| 110 | newR1L-DealerMode-101 | pre | 行尾多餘句號 | 1. A valid ECU ID Certificate file is available for import. |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 3. Press "ECU ID Certificate Management". |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 4. Insert a USB device with an valid ECU ID Certificate. |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 6. Press "Import ECU ID Certificate from USB" button and remove the USB device d |
| 110 | newR1L-DealerMode-101 | proc | 行尾多餘句號 | 7.  Check the result indication displayed for the import operation. |
| 110 | newR1L-DealerMode-101 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 110 | newR1L-DealerMode-101 | er | 行尾多餘句號 | 4. USB device is detected successfully. |
| 110 | newR1L-DealerMode-101 | er | 行尾多餘句號 | 6. The ECU ID Certificate import operation is triggered successfully and fails a |
| 110 | newR1L-DealerMode-101 | er | 行尾多餘句號 | 7. A Fail result indication with the message "Import ECU Certificate Failed" is  |
| 111 | newR1L-DealerMode-102 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 111 | newR1L-DealerMode-102 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 111 | newR1L-DealerMode-102 | proc | 行尾多餘句號 | 6. Check the result indication displayed for the export operation. |
| 111 | newR1L-DealerMode-102 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 111 | newR1L-DealerMode-102 | er | 行尾多餘句號 | 4. The "Export ECU ID Certificate to USB" function is available and selectable. |
| 111 | newR1L-DealerMode-102 | er | 行尾多餘句號 | 5. The ECU ID Certificate export operation is triggered successfully and fails a |
| 111 | newR1L-DealerMode-102 | er | 行尾多餘句號 | 6. A Fail result indication with the message "Export ECU Certificate Failed" is  |
| 112 | newR1L-DealerMode-103 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 112 | newR1L-DealerMode-103 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 112 | newR1L-DealerMode-103 | proc | 行尾多餘句號 | 4. Inset a USB device that ECU ID Certificate file is available for Export. |
| 112 | newR1L-DealerMode-103 | proc | 行尾多餘句號 | 6. Press "Export ECU ID Certificate to USB" button and remove the USB device dur |
| 112 | newR1L-DealerMode-103 | proc | 行尾多餘句號 | 7. Check the result indication displayed for the export operation. |
| 112 | newR1L-DealerMode-103 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 112 | newR1L-DealerMode-103 | er | 行尾多餘句號 | 4. USB device is detected successfully. |
| 112 | newR1L-DealerMode-103 | er | 行尾多餘句號 | 5. The "Export ECU ID Certificate to USB" function is available and selectable. |
| 112 | newR1L-DealerMode-103 | er | 行尾多餘句號 | 6. The ECU ID Certificate export operation is triggered successfully and fails a |
| 112 | newR1L-DealerMode-103 | er | 行尾多餘句號 | 7. A Fail result indication with the message "Export ECU Certificate Failed" is  |
| 113 | newR1L-DealerMode-104 | pre | 行尾多餘句號 | 1. Invalid certificate files (corrupted / missing fields / cryptographically inv |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 3. Select ECU ID Certificate Management. |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 4. Insert a USB device containing a corrupted certificate file. |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 5. Select “Invalid Certificate Verification”. |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 6. Select the corrupted certificate file and start verification. |
| 113 | newR1L-DealerMode-104 | proc | 行尾多餘句號 | 7. Check the verification result indication displayed. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 4. USB storage device is detected successfully. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 5. Invalid Certificate Verification is executed for the selected file. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 6. The corrupted certificate is rejected. |
| 113 | newR1L-DealerMode-104 | er | 行尾多餘句號 | 7. A visible Fail result indication with an explicit error/failure message is di |
| 114 | newR1L-DealerMode-105 | pre | 行尾多餘句號 | 1. Invalid certificate files (corrupted / missing fields / cryptographically inv |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 3. Select ECU ID Certificate Management. |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 4. Insert a USB device containing a missing fields certificate file. |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 5. Select “Invalid Certificate Verification”. |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 6. Select the missing fields certificate file and start verification. |
| 114 | newR1L-DealerMode-105 | proc | 行尾多餘句號 | 7. Check the verification result indication displayed. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 4. USB storage device is detected successfully. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 5. Invalid Certificate Verification is executed for the selected file. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 6. The certificate with missing fields is rejected. |
| 114 | newR1L-DealerMode-105 | er | 行尾多餘句號 | 7. A visible Fail result indication with an explicit error/failure message is di |
| 115 | newR1L-DealerMode-106 | pre | 行尾多餘句號 | 1. Invalid certificate files (corrupted / missing fields / cryptographically inv |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 3. Select ECU ID Certificate Management. |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 4. Insert a USB device containing a Cryptographically invalid certificate file. |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 5. Select “Invalid Certificate Verification”. |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 6. Select the Cryptographically invalid certificate file and start verification. |
| 115 | newR1L-DealerMode-106 | proc | 行尾多餘句號 | 7. Check the verification result indication displayed. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 4. USB storage device is detected successfully. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 5. Invalid Certificate Verification is executed for the selected file. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 6. The Cryptographically invalid certificate file is rejected. |
| 115 | newR1L-DealerMode-106 | er | 行尾多餘句號 | 7. A visible Fail result indication with an explicit error/failure message is di |
| 116 | newR1L-DealerMode-107 | pre | 行尾多餘句號 | 1. Invalid certificate files (corrupted / missing fields / cryptographically inv |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 4. Insert a USB device containing an invalid certificate file (e.g., corrupted c |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 5. Select “Invalid Certificate Verification”. |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 6. Select the invalid certificate file and start verification. |
| 116 | newR1L-DealerMode-107 | proc | 行尾多餘句號 | 7. Return to ECU ID Certificate Management and check the certificate list/status |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 4. USB storage device is detected successfully. |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 5.Invalid Certificate Verification is executed for the selected file. |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 6. The invalid certificate verification is executed and the invalid certificate  |
| 116 | newR1L-DealerMode-107 | er | 行尾多餘句號 | 7. No invalid certificate is saved/installed/listed, existing valid ECU ID Certi |
| 117 | newR1L-DealerMode-108 | pre | 行尾多餘句號 | 1. No ECU ID Certificate is installed in the system. |
| 117 | newR1L-DealerMode-108 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 117 | newR1L-DealerMode-108 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 117 | newR1L-DealerMode-108 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 117 | newR1L-DealerMode-108 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 117 | newR1L-DealerMode-108 | er | 行尾多餘句號 | 1. The HU screen is turned off. |
| 117 | newR1L-DealerMode-108 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 117 | newR1L-DealerMode-108 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 117 | newR1L-DealerMode-108 | er | 行尾多餘句號 | 4. The ECU ID Certificate status is displayed as “Certificate not present”. |
| 118 | newR1L-DealerMode-109 | pre | 行尾多餘句號 | 1. An ECU ID Certificate is installed in the system. |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 4. Delete the installed ECU ID Certificate. |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 5. Remain to ECU ID Certificate Management page. |
| 118 | newR1L-DealerMode-109 | proc | 行尾多餘句號 | 6. Check the ECU ID Certificate status field displayed on the screen. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 1. The HU screen is turned off. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 4. The ECU ID Certificate is deleted successfully. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 5. ECU ID Certificate Management page is displayed normally after deletion. |
| 118 | newR1L-DealerMode-109 | er | 行尾多餘句號 | 6. The ECU ID Certificate status is updated and displayed as “Certificate not pr |
| 119 | newR1L-DealerMode-110 | pre | 行尾多餘句號 | 1. No ECU ID Certificate is installed in the system. |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 4. Turn vehicle Ignition OFF. |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition ON and wait for system startup to complete. |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 6. Select ECU ID Certificate Management again. |
| 119 | newR1L-DealerMode-110 | proc | 行尾多餘句號 | 7. Check the ECU ID Certificate status field displayed on the screen. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 1. The HU screen is turned off. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | ECU ID Certificate Management page is displayed. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 3. System powers off successfully. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 4. System powers on and completes startup. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 5. Dealer Mode is entered after ignition cycle. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 6. ECU ID Certificate Management page is displayed. |
| 119 | newR1L-DealerMode-110 | er | 行尾多餘句號 | 7. The ECU ID Certificate status is retained and displayed as “Certificate not p |
| 120 | newR1L-DealerMode-111 | pre | 行尾多餘句號 | 1. CSR is not present in the system. |
| 120 | newR1L-DealerMode-111 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the screen. |
| 120 | newR1L-DealerMode-111 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 120 | newR1L-DealerMode-111 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 120 | newR1L-DealerMode-111 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 120 | newR1L-DealerMode-111 | er | 行尾多餘句號 | 1. HU screen is OFF. |
| 120 | newR1L-DealerMode-111 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 120 | newR1L-DealerMode-111 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 120 | newR1L-DealerMode-111 | er | 行尾多餘句號 | 4. The status field displays “CSR not present”. |
| 121 | newR1L-DealerMode-112 | pre | 行尾多餘句號 | 1. A valid ECU ID Certificate is installed in the system. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON and wait for system startup. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 7. Enter Dealer Mode again. |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 8. Select "ECU ID Certificate Management". |
| 121 | newR1L-DealerMode-112 | proc | 行尾多餘句號 | 9. Check the ECU ID Certificate status field again. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 4. The status field displays “CSR not present”. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 5. System powers off successfully. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 6. System powers on and completes startup. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 7. Dealer Mode is entered after ignition cycle. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 8. ECU ID Certificate Management page is displayed. |
| 121 | newR1L-DealerMode-112 | er | 行尾多餘句號 | 9. The status field is retained and displays “CSR not present”. |
| 122 | newR1L-DealerMode-113 | pre | 行尾多餘句號 | 1. A valid ECU ID Certificate is installed in the system. |
| 122 | newR1L-DealerMode-113 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 122 | newR1L-DealerMode-113 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 122 | newR1L-DealerMode-113 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 122 | newR1L-DealerMode-113 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 122 | newR1L-DealerMode-113 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 122 | newR1L-DealerMode-113 | er | 行尾多餘句號 | 4. The status field displays “Certificate present”. |
| 123 | newR1L-DealerMode-114 | pre | 行尾多餘句號 | 1. No ECU ID Certificate is installed in the system. |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field. |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 5. Insert a USB device containing a valid ECU ID Certificate. |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 6. Perform Import ECU ID Certificate from USB. |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 7. Return to "ECU ID Certificate Management". |
| 123 | newR1L-DealerMode-114 | proc | 行尾多餘句號 | 8. Check the ECU ID Certificate status field again. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 4. The status field displays “Certificate not present”. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 5. USB device is detected successfully. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 6. ECU ID Certificate import completes successfully. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 7. ECU ID Certificate Management page is displayed. |
| 123 | newR1L-DealerMode-114 | er | 行尾多餘句號 | 8. The status field is updated and displays “Certificate present”. |
| 124 | newR1L-DealerMode-115 | pre | 行尾多餘句號 | 1. Invalid certificate files (corrupted / missing fields / cryptographically inv |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF. |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON and wait for system startup. |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 7. Enter Dealer Mode again. |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 8. Select "ECU ID Certificate Management". |
| 124 | newR1L-DealerMode-115 | proc | 行尾多餘句號 | 9. Check the ECU ID Certificate status field again. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 4. The status field displays “Certificate present”. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 5. System powers off successfully. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 6. System powers on and completes startup. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 7. Dealer Mode is entered after ignition cycle. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 8. ECU ID Certificate Management page is displayed. |
| 124 | newR1L-DealerMode-115 | er | 行尾多餘句號 | 9. The status field is retained and displays “Certificate present”. |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 4. Insert a USB device containing an invalid ECU ID Certificate file. |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 5. Select "Invalid Certificate Verification". |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 6. Select the invalid certificate file and start verification. |
| 125 | newR1L-DealerMode-116 | proc | 行尾多餘句號 | 7. Check the certificate status field displayed after verification. |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 4. USB storage device is detected successfully. |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 5. Invalid Certificate Verification is executed for the selected file. |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 6. The invalid certificate is rejected during verification and is not imported a |
| 125 | newR1L-DealerMode-116 | er | 行尾多餘句號 | 7. The certificate status field displays "Certificate invalid" to reflect the ve |
| 126 | newR1L-DealerMode-117 | pre | 行尾多餘句號 | 1. An ECU ID Certificate is present, but the corresponding private key is not pr |
| 126 | newR1L-DealerMode-117 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 126 | newR1L-DealerMode-117 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 126 | newR1L-DealerMode-117 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 126 | newR1L-DealerMode-117 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 126 | newR1L-DealerMode-117 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 126 | newR1L-DealerMode-117 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 126 | newR1L-DealerMode-117 | er | 行尾多餘句號 | 4. The status field displays "Private key not present". |
| 127 | newR1L-DealerMode-118 | pre | 行尾多餘句號 | 1. An ECU ID Certificate is present, but the corresponding private key is not pr |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 3. Select "ECU ID Certificate Management". |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 4. Check the ECU ID Certificate status field displayed on the screen. |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF. |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON and wait for system startup. |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 7. Enter Dealer Mode again. |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 8. Select "ECU ID Certificate Management". |
| 127 | newR1L-DealerMode-118 | proc | 行尾多餘句號 | 9. Check the ECU ID Certificate status field again. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 3. ECU ID Certificate Management page is displayed. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 4. The status field displays "Private key not present". |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 5. System powers off successfully. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 6. System powers on and completes startup. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 7. Dealer Mode is entered after ignition cycle. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 8. ECU ID Certificate Management page is displayed. |
| 127 | newR1L-DealerMode-118 | er | 行尾多餘句號 | 9. The status field displays "Private key not present". |
| 128 | newR1L-DealerMode-119 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 128 | newR1L-DealerMode-119 | proc | 行尾多餘句號 | 2. Press and Hold the top right and bottom left corners of the screen for 5 seco |
| 128 | newR1L-DealerMode-119 | proc | 行尾多餘句號 | 3. Check the Dealer Mode main page is displayed. |
| 128 | newR1L-DealerMode-119 | proc | 行尾多餘句號 | 4. Navigate through each Dealer Mode main menu item and open each corresponding  |
| 128 | newR1L-DealerMode-119 | proc | 行尾多餘句號 | 5. For each opened page, check the required UI elements/labels are displayed. |
| 128 | newR1L-DealerMode-119 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 128 | newR1L-DealerMode-119 | er | 行尾多餘句號 | 3. Dealer Mode main page is displayed. |
| 128 | newR1L-DealerMode-119 | er | 行尾多餘句號 | 4. Each Dealer Mode menu item can be opened and its subpage is displayed. |
| 128 | newR1L-DealerMode-119 | er | 行尾多餘句號 | 5. Required UI elements/labels are displayed on each Dealer Mode page/subpage. |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 3. Open System Information page. |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 4. Check system information is displayed. |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 5. Press "←" button to back to Dealer Mode main page. |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 6. Select "USB Data Download/Restore" menu item to trigger a Download or Restore |
| 129 | newR1L-DealerMode-120 | proc | 行尾多餘句號 | 7. Press "X" button to exit Dealer Mode. |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 3. System Information page is displayed. |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 4. System information is displayed successfully (no blank/incorrect page). |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 5. Return to Dealer Mode Main page. |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 6. The selected Download/Restore action is triggered successfully and provides a |
| 129 | newR1L-DealerMode-120 | er | 行尾多餘句號 | 7. Dealer Mode exit flow completes successfully and system returns to the expect |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 3. Open any Dealer Mode subpage (e.g., System Information). |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 4. Press "←" button to back to previous page. |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 5. Repeat step 2–3 for at least two different subpages. |
| 130 | newR1L-DealerMode-121 | proc | 行尾多餘句號 | 6. From a subpage, navigate back to the Dealer Mode main menu. |
| 130 | newR1L-DealerMode-121 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 130 | newR1L-DealerMode-121 | er | 行尾多餘句號 | 3. The selected subpage is displayed. |
| 130 | newR1L-DealerMode-121 | er | 行尾多餘句號 | 4. Back navigation returns to the expected previous screen without UI freeze/cra |
| 130 | newR1L-DealerMode-121 | er | 行尾多餘句號 | 5. Back navigation behaves consistently across different subpages. |
| 130 | newR1L-DealerMode-121 | er | 行尾多餘句號 | 6. Dealer Mode main menu is reachable via expected navigation flow. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 1. Perform a cold boot (system boot from power-off state) and wait for startup c |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 2. Press H/K [Screen off] button to turn off the HU screen. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 3. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 4. Open one Dealer Mode subpage and confirm it displays normally. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 5. Turn vehicle Ignition OFF. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 6. Turn vehicle Ignition ON and wait for startup completion. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 7. Enter Dealer Mode again. |
| 131 | newR1L-DealerMode-122 | proc | 行尾多餘句號 | 8. Check Dealer Mode main menu and open the same subpage again. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 1. System completes cold boot successfully. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 3. Dealer Mode page is displayed after cold boot. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 4. Dealer Mode subpage is displayed normally (no missing UI / no crash). |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 5. System powers off successfully. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 6. System powers on and completes startup successfully. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 7. Dealer Mode page is displayed successfully after ignition cycle. |
| 131 | newR1L-DealerMode-122 | er | 行尾多餘句號 | 8. Dealer Mode main menu and the selected subpage are displayed normally after i |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 3. Check the Dealer Mode main page is displayed. |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 4. Press "X" button to exit Dealer Mode. |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 5. Confirm the system returns to the expected non-Dealer Mode screen. |
| 132 | newR1L-DealerMode-123 | proc | 行尾多餘句號 | 6. Enter Dealer Mode again. |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 1. HU screen is turned off. |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 2. Dealer Mode is entered successfully. |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 3. Dealer Mode main page is displayed. |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 4. Dealer Mode exit flow is triggered successfully. |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 5. System exits Dealer Mode and returns to the expected non-Dealer Mode screen w |
| 132 | newR1L-DealerMode-123 | er | 行尾多餘句號 | 6. Dealer Mode can be entered again successfully. |
| 133 | newR1L-DealerMode-124 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 133 | newR1L-DealerMode-124 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 133 | newR1L-DealerMode-124 | proc | 行尾多餘句號 | 3. Open the Dealer Mode main menu. |
| 133 | newR1L-DealerMode-124 | proc | 行尾多餘句號 | 4. Record the displayed order of all listed Dealer Mode features. |
| 133 | newR1L-DealerMode-124 | er | 行尾多餘句號 | 3. Dealer Mode main menu is displayed. |
| 133 | newR1L-DealerMode-124 | er | 行尾多餘句號 | 4. All Dealer Mode features are listed and visible. |
| 134 | newR1L-DealerMode-125 | proc | 行尾多餘句號 | 1. Press H/K [Screen off] button to turn off the HU screen. |
| 134 | newR1L-DealerMode-125 | proc | 行尾多餘句號 | 2. Press and hold the top-right and bottom-left corners of the screen for 5 seco |
| 134 | newR1L-DealerMode-125 | proc | 行尾多餘句號 | 3. Open the corresponding feature information page / panel. |
| 134 | newR1L-DealerMode-125 | proc | 行尾多餘句號 | 4. Record the displayed order of information items on the page. |
| 134 | newR1L-DealerMode-125 | proc | 行尾多餘句號 | 5. Repeat steps 3–4 for all applicable Dealer Mode features. |
| 134 | newR1L-DealerMode-125 | er | 行尾多餘句號 | 1. HU screen is turned off. |
| 134 | newR1L-DealerMode-125 | er | 行尾多餘句號 | 2. Dealer Mode page is displayed. |
| 134 | newR1L-DealerMode-125 | er | 行尾多餘句號 | 3. Selected Dealer Mode feature page is displayed. |
| 134 | newR1L-DealerMode-125 | er | 行尾多餘句號 | 4. Feature information items are displayed correctly. |
| 134 | newR1L-DealerMode-125 | er | 行尾多餘句號 | 5. Information items are displayed in a consistent order within the page. |

