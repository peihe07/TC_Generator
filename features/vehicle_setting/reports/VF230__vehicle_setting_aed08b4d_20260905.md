# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VF230_20260902.xlsx

- 來源：`features/vehicle_setting/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VF230_20260902.xlsx`（唯讀）
- 資料列數：438
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`vehicle_setting`（P 採 R-1 v3；另跑 Q／R／T）

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
| K | CJK 字元 | 25 | 25 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 1003 | 279 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 25 | 25 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 25 | 25 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 278 | 278 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 361 | 198 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |

**總計：行計 1717**（列計不加總——同一列可觸發多項檢查）

## 明細

### K — CJK 字元（行計 25／列計 25）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 81 | NR1L-VS-072 | pre | 含 CJK 字元 | o On ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 82 | NR1L-VS-073 | pre | 含 CJK 字元 | Off ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 83 | NR1L-VS-074 | pre | 含 CJK 字元 | open ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 140 | NR1L-VS-131 | pre | 含 CJK 字元 | tate ⏎ 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 154 | NR1L-VS-145 | pre | 含 CJK 字元 | tate ⏎ 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 155 | NR1L-VS-146 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 162 | NR1L-VS-153 | pre | 含 CJK 字元 | o On ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 163 | NR1L-VS-154 | pre | 含 CJK 字元 | Off ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 164 | NR1L-VS-155 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 167 | NR1L-VS-158 | pre | 含 CJK 字元 | sual ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 168 | NR1L-VS-159 | pre | 含 CJK 字元 | Off ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 169 | NR1L-VS-160 | pre | 含 CJK 字元 | Off ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 170 | NR1L-VS-161 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 180 | NR1L-VS-171 | pre | 含 CJK 字元 | dium ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 181 | NR1L-VS-172 | pre | 含 CJK 字元 | Low ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 182 | NR1L-VS-173 | pre | 含 CJK 字元 | Low ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 183 | NR1L-VS-174 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 184 | NR1L-VS-175 | pre | 含 CJK 字元 | dium ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 185 | NR1L-VS-176 | pre | 含 CJK 字元 | Low ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 186 | NR1L-VS-177 | pre | 含 CJK 字元 | Low ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 187 | NR1L-VS-178 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 330 | NR1L-VS-321 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 355 | NR1L-VS-346 | pre | 含 CJK 字元 | o On ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 356 | NR1L-VS-347 | pre | 含 CJK 字元 | Off ⏎ 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 357 | NR1L-VS-348 | pre | 含 CJK 字元 | bled ⏎ 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |

### P — 訊號寫法不合 R-1 v3（行計 1003／列計 279）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 17 | NR1L-VS-008 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req =' | 2. Set the "Auto Fold Mirrors" customer setting to Off and check that TELEMATIC_ |
| 17 | NR1L-VS-008 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req = 0 (Off) is sent |
| 18 | NR1L-VS-009 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req =' | 2. Set the "Auto Fold Mirrors" customer setting to On and check that TELEMATIC_V |
| 18 | NR1L-VS-009 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Auto_Fold_Mirr_Req = 1 (On) is sent |
| 19 | NR1L-VS-010 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Auto_Fold_Mirr =' | IPC_VEHICLE_SETUP.Auto_Fold_Mirr = one of [0 (Off), 1 (On)] |
| 19 | NR1L-VS-010 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 1 (On) |
| 19 | NR1L-VS-010 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Auto_Fold_Mirr =' | 1. Send CAN: IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 1 (On) |
| 19 | NR1L-VS-010 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 0 (Off) |
| 19 | NR1L-VS-010 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Auto_Fold_Mirr =' | 2. Send CAN: IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 0 (Off) |
| 19 | NR1L-VS-010 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Auto_Fold_Mirr =' | 1. IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 1 (On) is sent |
| 19 | NR1L-VS-010 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Auto_Fold_Mirr =' | 2. IPC_VEHICLE_SETUP.Auto_Fold_Mirr = 0 (Off) is sent |
| 22 | NR1L-VS-013 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req =' | 2. Set the "Auto High Beam" customer setting to Not_Enable and check that TELEMA |
| 22 | NR1L-VS-013 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req =' | 2. TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req = 0 (Not_Enable) is sent |
| 23 | NR1L-VS-014 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req =' | 2. Set the "Auto High Beam" customer setting to Enable and check that TELEMATIC_ |
| 23 | NR1L-VS-014 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req =' | 2. TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req = 1 (Enable) is sent |
| 24 | NR1L-VS-015 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoHighBeamEnable =' | IPC_VEHICLE_SETUP.AutoHighBeamEnable = one of [0 (Not_Enable), 1 (Enable)] |
| 24 | NR1L-VS-015 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.AutoHighBeamEnable = 1 (Enable) |
| 24 | NR1L-VS-015 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoHighBeamEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.AutoHighBeamEnable = 1 (Enable) |
| 24 | NR1L-VS-015 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.AutoHighBeamEnable = 0 (Not_Enable) |
| 24 | NR1L-VS-015 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoHighBeamEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.AutoHighBeamEnable = 0 (Not_Enable) |
| 24 | NR1L-VS-015 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoHighBeamEnable =' | 1. IPC_VEHICLE_SETUP.AutoHighBeamEnable = 1 (Enable) is sent |
| 24 | NR1L-VS-015 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoHighBeamEnable =' | 2. IPC_VEHICLE_SETUP.AutoHighBeamEnable = 0 (Not_Enable) is sent |
| 26 | NR1L-VS-017 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. Set the "Auto On Driver Comfort - 2 Option" customer setting to Off and check |
| 26 | NR1L-VS-017 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req = 0 (Off) is sent |
| 27 | NR1L-VS-018 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. Set the "Auto On Driver Comfort - 2 Option" customer setting to Normal_Start_ |
| 27 | NR1L-VS-018 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req = 3 (Normal_Start_Only) is sent |
| 28 | NR1L-VS-019 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | IPC_VEHICLE_SETUP.RemStNrmlStEnbl = one of [0 (Off), 1 (Remote_Start_Only), 2 (R |
| 28 | NR1L-VS-019 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) |
| 28 | NR1L-VS-019 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) |
| 28 | NR1L-VS-019 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) |
| 28 | NR1L-VS-019 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) |
| 28 | NR1L-VS-019 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 1. IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) is sent |
| 28 | NR1L-VS-019 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 2. IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) is sent |
| 31 | NR1L-VS-022 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. Set the "Auto On Driver Comfort - 3 Option" customer setting to Off and check |
| 31 | NR1L-VS-022 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req = 0 (Off) is sent |
| 32 | NR1L-VS-023 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. Set the "Auto On Driver Comfort - 3 Option" customer setting to Remote_Start_ |
| 32 | NR1L-VS-023 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req = 1 (Remote_Start_Only) is sent |
| 33 | NR1L-VS-024 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. Set the "Auto On Driver Comfort - 3 Option" customer setting to Remote_And_No |
| 33 | NR1L-VS-024 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req =' | 3. TELEMATIC_VEHICLE_SETUP.RemStNrmlStEnbl_Req = 2 (Remote_And_Normal_Start ) is |
| 34 | NR1L-VS-025 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | IPC_VEHICLE_SETUP.RemStNrmlStEnbl = one of [0 (Off), 1 (Remote_Start_Only), 2 (R |
| 34 | NR1L-VS-025 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) |
| 34 | NR1L-VS-025 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) |
| 34 | NR1L-VS-025 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) |
| 34 | NR1L-VS-025 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) |
| 34 | NR1L-VS-025 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 1. IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 1 (Remote_Start_Only) is sent |
| 34 | NR1L-VS-025 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemStNrmlStEnbl =' | 2. IPC_VEHICLE_SETUP.RemStNrmlStEnbl = 0 (Off) is sent |
| 37 | NR1L-VS-028 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req =' | 3. Set the "Auto Park Brake" customer setting to Off and check that TELEMATIC_VE |
| 37 | NR1L-VS-028 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req =' | 3. TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req = 1 (Off) is sent |
| 38 | NR1L-VS-029 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req =' | 3. Set the "Auto Park Brake" customer setting to On and check that TELEMATIC_VEH |
| 38 | NR1L-VS-029 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req =' | 3. TELEMATIC_VEHICLE_SETUP.AutoParkBrake_Req = 0 (On) is sent |
| 39 | NR1L-VS-030 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoParkBrake =' | IPC_VEHICLE_SETUP.AutoParkBrake = one of [0 (On), 1 (Off)] |
| 39 | NR1L-VS-030 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.AutoParkBrake = 1 (Off) |
| 39 | NR1L-VS-030 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoParkBrake =' | 1. Send CAN: IPC_VEHICLE_SETUP.AutoParkBrake = 1 (Off) |
| 39 | NR1L-VS-030 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.AutoParkBrake = 0 (On) |
| 39 | NR1L-VS-030 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoParkBrake =' | 2. Send CAN: IPC_VEHICLE_SETUP.AutoParkBrake = 0 (On) |
| 39 | NR1L-VS-030 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoParkBrake =' | 1. IPC_VEHICLE_SETUP.AutoParkBrake = 1 (Off) is sent |
| 39 | NR1L-VS-030 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoParkBrake =' | 2. IPC_VEHICLE_SETUP.AutoParkBrake = 0 (On) is sent |
| 42 | NR1L-VS-033 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req =' | 3. Set the "Auto Unlock on Exit" customer setting to Not_Enable and check that T |
| 42 | NR1L-VS-033 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req =' | 3. TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req = 0 (Not_Enable) is sent |
| 43 | NR1L-VS-034 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req =' | 3. Set the "Auto Unlock on Exit" customer setting to Enable and check that TELEM |
| 43 | NR1L-VS-034 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req =' | 3. TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req = 1 (Enable) is sent |
| 44 | NR1L-VS-035 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoUnlockDoorExit =' | IPC_VEHICLE_SETUP.AutoUnlockDoorExit = one of [0 (Not_Enable), 1 (Enable)] |
| 44 | NR1L-VS-035 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 1 (Enable) |
| 44 | NR1L-VS-035 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoUnlockDoorExit =' | 1. Send CAN: IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 1 (Enable) |
| 44 | NR1L-VS-035 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 0 (Not_Enable) |
| 44 | NR1L-VS-035 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoUnlockDoorExit =' | 2. Send CAN: IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 0 (Not_Enable) |
| 44 | NR1L-VS-035 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoUnlockDoorExit =' | 1. IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 1 (Enable) is sent |
| 44 | NR1L-VS-035 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.AutoUnlockDoorExit =' | 2. IPC_VEHICLE_SETUP.AutoUnlockDoorExit = 0 (Not_Enable) is sent |
| 47 | NR1L-VS-038 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req =' | 2. Set the "Automatic Trailer Light Check" customer setting to Disable and check |
| 47 | NR1L-VS-038 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req = 0 (Disable) is sent |
| 48 | NR1L-VS-039 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req =' | 2. Set the "Automatic Trailer Light Check" customer setting to Enable and check  |
| 48 | NR1L-VS-039 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Auto_Trailer_Light_Check_Req = 1 (Enable) is sent |
| 49 | NR1L-VS-040 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Trailer_Light_Check =' | IPC_VEHICLE_SETUP2.Trailer_Light_Check = one of [0 (Disable), 1 (Enable)] |
| 49 | NR1L-VS-040 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Trailer_Light_Check = 1 (Enable) |
| 49 | NR1L-VS-040 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Trailer_Light_Check =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Trailer_Light_Check = 1 (Enable) |
| 49 | NR1L-VS-040 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Trailer_Light_Check = 0 (Disable) |
| 49 | NR1L-VS-040 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Trailer_Light_Check =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Trailer_Light_Check = 0 (Disable) |
| 49 | NR1L-VS-040 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Trailer_Light_Check =' | 1. IPC_VEHICLE_SETUP2.Trailer_Light_Check = 1 (Enable) is sent |
| 49 | NR1L-VS-040 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Trailer_Light_Check =' | 2. IPC_VEHICLE_SETUP2.Trailer_Light_Check = 0 (Disable) is sent |
| 52 | NR1L-VS-043 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req =' | 2. Set the "Blind Spot with Trailer Detection" customer setting to Auto and chec |
| 52 | NR1L-VS-043 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req = 0 (Auto) is sent |
| 53 | NR1L-VS-044 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req =' | 2. Set the "Blind Spot with Trailer Detection" customer setting to Max and check |
| 53 | NR1L-VS-044 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trailer_detection_blind_spot_Req = 1 (Max) is sent |
| 54 | NR1L-VS-045 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot =' | IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = one of [0 (Auto), 1 (Max)] |
| 54 | NR1L-VS-045 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 1 (Max) |
| 54 | NR1L-VS-045 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot =' | 1. Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 1 (Max) |
| 54 | NR1L-VS-045 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 0 (Auto) |
| 54 | NR1L-VS-045 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot =' | 2. Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 0 (Auto) |
| 54 | NR1L-VS-045 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot =' | 1. IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 1 (Max) is sent |
| 54 | NR1L-VS-045 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot =' | 2. IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 0 (Auto) is sent |
| 57 | NR1L-VS-048 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. Set the "Blind Spot Alert" customer setting to Not_Enable and check that TELE |
| 57 | NR1L-VS-048 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. TELEMATIC_VEHICLE_SETUP.BSDEnable_Req = 0 (Not_Enable) is sent |
| 58 | NR1L-VS-049 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. Set the "Blind Spot Alert" customer setting to Enable_LED and check that TELE |
| 58 | NR1L-VS-049 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. TELEMATIC_VEHICLE_SETUP.BSDEnable_Req = 1 (Enable_LED) is sent |
| 59 | NR1L-VS-050 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. Set the "Blind Spot Alert" customer setting to Enable_ LED_Chime and check th |
| 59 | NR1L-VS-050 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req =' | 3. TELEMATIC_VEHICLE_SETUP.BSDEnable_Req = 2 (Enable_ LED_Chime) is sent |
| 60 | NR1L-VS-051 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.BSDEnable =' | IPC_VEHICLE_SETUP.BSDEnable = one of [0 (Not_Enable), 1 (Enable_LED), 2 (Enable_ |
| 60 | NR1L-VS-051 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.BSDEnable = 1 (Enable_LED) |
| 60 | NR1L-VS-051 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.BSDEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.BSDEnable = 1 (Enable_LED) |
| 60 | NR1L-VS-051 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.BSDEnable = 0 (Not_Enable) |
| 60 | NR1L-VS-051 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.BSDEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.BSDEnable = 0 (Not_Enable) |
| 60 | NR1L-VS-051 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.BSDEnable =' | 1. IPC_VEHICLE_SETUP.BSDEnable = 1 (Enable_LED) is sent |
| 60 | NR1L-VS-051 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.BSDEnable =' | 2. IPC_VEHICLE_SETUP.BSDEnable = 0 (Not_Enable) is sent |
| 63 | NR1L-VS-054 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. Set the "Charge Power Level" customer setting to Level1 and check that TELEMA |
| 63 | NR1L-VS-054 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. TELEMATIC_VEHICLE_SETUP.PwrLevReq = 0 (Level1) is sent |
| 64 | NR1L-VS-055 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. Set the "Charge Power Level" customer setting to Level2 and check that TELEMA |
| 64 | NR1L-VS-055 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. TELEMATIC_VEHICLE_SETUP.PwrLevReq = 1 (Level2) is sent |
| 65 | NR1L-VS-056 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. Set the "Charge Power Level" customer setting to Level3 and check that TELEMA |
| 65 | NR1L-VS-056 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. TELEMATIC_VEHICLE_SETUP.PwrLevReq = 2 (Level3) is sent |
| 66 | NR1L-VS-057 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. Set the "Charge Power Level" customer setting to Level4 and check that TELEMA |
| 66 | NR1L-VS-057 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. TELEMATIC_VEHICLE_SETUP.PwrLevReq = 3 (Level4) is sent |
| 67 | NR1L-VS-058 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. Set the "Charge Power Level" customer setting to Level5 and check that TELEMA |
| 67 | NR1L-VS-058 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PwrLevReq =' | 2. TELEMATIC_VEHICLE_SETUP.PwrLevReq = 4 (Level5) is sent |
| 68 | NR1L-VS-059 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PwrLev =' | IPC_VEHICLE_SETUP.PwrLev = one of [0 (Level1), 1 (Level2), 2 (Level3), 3 (Level4 |
| 68 | NR1L-VS-059 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PwrLev = 1 (Level2) |
| 68 | NR1L-VS-059 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PwrLev =' | 1. Send CAN: IPC_VEHICLE_SETUP.PwrLev = 1 (Level2) |
| 68 | NR1L-VS-059 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PwrLev = 0 (Level1) |
| 68 | NR1L-VS-059 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PwrLev =' | 2. Send CAN: IPC_VEHICLE_SETUP.PwrLev = 0 (Level1) |
| 68 | NR1L-VS-059 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PwrLev =' | 1. IPC_VEHICLE_SETUP.PwrLev = 1 (Level2) is sent |
| 68 | NR1L-VS-059 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PwrLev =' | 2. IPC_VEHICLE_SETUP.PwrLev = 0 (Level1) is sent |
| 72 | NR1L-VS-063 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.CorneringEnable =' | IPC_VEHICLE_SETUP.CorneringEnable = one of [0 (True), 1 (False)] |
| 72 | NR1L-VS-063 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.CorneringEnable = 1 (False) |
| 72 | NR1L-VS-063 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.CorneringEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.CorneringEnable = 1 (False) |
| 72 | NR1L-VS-063 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.CorneringEnable = 0 (True) |
| 72 | NR1L-VS-063 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.CorneringEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.CorneringEnable = 0 (True) |
| 72 | NR1L-VS-063 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.CorneringEnable =' | 1. IPC_VEHICLE_SETUP.CorneringEnable = 1 (False) is sent |
| 72 | NR1L-VS-063 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.CorneringEnable =' | 2. IPC_VEHICLE_SETUP.CorneringEnable = 0 (True) is sent |
| 75 | NR1L-VS-066 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DRLEnable_Req =' | 3. Set the "Daytime Running Lights" customer setting to True and check that TELE |
| 75 | NR1L-VS-066 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DRLEnable_Req =' | 3. TELEMATIC_VEHICLE_SETUP.DRLEnable_Req = 0 (True) is sent |
| 76 | NR1L-VS-067 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 76 | NR1L-VS-067 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 76 | NR1L-VS-067 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 1 (False) |
| 76 | NR1L-VS-067 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 1 (False) |
| 76 | NR1L-VS-067 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 1. IPC_VEHICLE_SETUP.DRLEnable = 0 (True) is sent |
| 76 | NR1L-VS-067 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 2. IPC_VEHICLE_SETUP.DRLEnable = 1 (False) is sent |
| 77 | NR1L-VS-068 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 77 | NR1L-VS-068 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 77 | NR1L-VS-068 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 77 | NR1L-VS-068 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.DRLEnable = 0 (True) |
| 77 | NR1L-VS-068 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 1. IPC_VEHICLE_SETUP.DRLEnable = 0 (True) is sent |
| 77 | NR1L-VS-068 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DRLEnable =' | 2. IPC_VEHICLE_SETUP.DRLEnable = 0 (True) is sent |
| 81 | NR1L-VS-072 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req =' | 2. Set the "Driver Easy Exit Seat" customer setting to Off and check that TELEMA |
| 81 | NR1L-VS-072 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req = 0 (Off) is sent |
| 82 | NR1L-VS-073 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req =' | 2. Set the "Driver Easy Exit Seat" customer setting to On and check that TELEMAT |
| 82 | NR1L-VS-073 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Easy_Exit_D_Req = 1 (On) is sent |
| 83 | NR1L-VS-074 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Easy_Exit_D =' | IPC_VEHICLE_SETUP.Easy_Exit_D = one of [0 (Off), 1 (On)] |
| 83 | NR1L-VS-074 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Easy_Exit_D = 1 (On) |
| 83 | NR1L-VS-074 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Easy_Exit_D =' | 1. Send CAN: IPC_VEHICLE_SETUP.Easy_Exit_D = 1 (On) |
| 83 | NR1L-VS-074 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Easy_Exit_D = 0 (Off) |
| 83 | NR1L-VS-074 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Easy_Exit_D =' | 2. Send CAN: IPC_VEHICLE_SETUP.Easy_Exit_D = 0 (Off) |
| 83 | NR1L-VS-074 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Easy_Exit_D =' | 1. IPC_VEHICLE_SETUP.Easy_Exit_D = 1 (On) is sent |
| 83 | NR1L-VS-074 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Easy_Exit_D =' | 2. IPC_VEHICLE_SETUP.Easy_Exit_D = 0 (Off) is sent |
| 86 | NR1L-VS-077 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. Set the "Engine Off Power Delay" customer setting to Zero and check that TELE |
| 86 | NR1L-VS-077 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req = 0 (Zero) is sent |
| 87 | NR1L-VS-078 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. Set the "Engine Off Power Delay" customer setting to Five_Min and check that  |
| 87 | NR1L-VS-078 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req = 2 (Five_Min) is sent |
| 88 | NR1L-VS-079 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. Set the "Engine Off Power Delay" customer setting to Ten_Min and check that T |
| 88 | NR1L-VS-079 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Eng_Off_Pwr_Delay_Req = 3 (Ten_Min) is sent |
| 89 | NR1L-VS-080 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay =' | IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = one of [0 (Zero), 1 (Fourty_Five_Sec), 2 ( |
| 89 | NR1L-VS-080 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 1 (Fourty_Five_Sec) |
| 89 | NR1L-VS-080 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay =' | 1. Send CAN: IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 1 (Fourty_Five_Sec) |
| 89 | NR1L-VS-080 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 0 (Zero) |
| 89 | NR1L-VS-080 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay =' | 2. Send CAN: IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 0 (Zero) |
| 89 | NR1L-VS-080 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay =' | 1. IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 1 (Fourty_Five_Sec) is sent |
| 89 | NR1L-VS-080 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay =' | 2. IPC_VEHICLE_SETUP.Eng_Off_Pwr_Delay = 0 (Zero) is sent |
| 92 | NR1L-VS-083 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Display_Synch_Req =' | 2. Set the "Enhanced Display Synchronization" customer setting to ON and check t |
| 92 | NR1L-VS-083 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Display_Synch_Req =' | 2. TELEMATIC_FD_1.Display_Synch_Req = 1 (ON) is sent |
| 93 | NR1L-VS-084 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Display_Synch_Req =' | 2. Set the "Enhanced Display Synchronization" customer setting to OFF and check  |
| 93 | NR1L-VS-084 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Display_Synch_Req =' | 2. TELEMATIC_FD_1.Display_Synch_Req = 0 (OFF) is sent |
| 94 | NR1L-VS-085 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Display_Synch =' | IPC_VEHICLE_SETUP2.Display_Synch = one of [0 (OFF), 1 (ON)] |
| 94 | NR1L-VS-085 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Display_Synch = 1 (ON) |
| 94 | NR1L-VS-085 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Display_Synch =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Display_Synch = 1 (ON) |
| 94 | NR1L-VS-085 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Display_Synch = 0 (OFF) |
| 94 | NR1L-VS-085 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Display_Synch =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Display_Synch = 0 (OFF) |
| 94 | NR1L-VS-085 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Display_Synch =' | 1. IPC_VEHICLE_SETUP2.Display_Synch = 1 (ON) is sent |
| 94 | NR1L-VS-085 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Display_Synch =' | 2. IPC_VEHICLE_SETUP2.Display_Synch = 0 (OFF) is sent |
| 98 | NR1L-VS-089 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req =' | 2. Set the "Flash Light With Lock" customer setting to Off and check that TELEMA |
| 98 | NR1L-VS-089 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req = 0 (Off) is sent |
| 99 | NR1L-VS-090 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req =' | 2. Set the "Flash Light With Lock" customer setting to On and check that TELEMAT |
| 99 | NR1L-VS-090 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req = 1 (On) is sent |
| 100 | NR1L-VS-091 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FlashLightWLock =' | IPC_VEHICLE_SETUP.FlashLightWLock = one of [0 (Off), 1 (On)] |
| 100 | NR1L-VS-091 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.FlashLightWLock = 1 (On) |
| 100 | NR1L-VS-091 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FlashLightWLock =' | 1. Send CAN: IPC_VEHICLE_SETUP.FlashLightWLock = 1 (On) |
| 100 | NR1L-VS-091 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.FlashLightWLock = 0 (Off) |
| 100 | NR1L-VS-091 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FlashLightWLock =' | 2. Send CAN: IPC_VEHICLE_SETUP.FlashLightWLock = 0 (Off) |
| 100 | NR1L-VS-091 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FlashLightWLock =' | 1. IPC_VEHICLE_SETUP.FlashLightWLock = 1 (On) is sent |
| 100 | NR1L-VS-091 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FlashLightWLock =' | 2. IPC_VEHICLE_SETUP.FlashLightWLock = 0 (Off) is sent |
| 103 | NR1L-VS-094 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusSetting =' | IPC_VEHICLE_SETUP.FSFCWPlusSetting = one of [0 (Off), 1 (Audio), 2 (Brake), 3 (A |
| 103 | NR1L-VS-094 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusSetting = 1 (Audio) |
| 103 | NR1L-VS-094 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusSetting =' | 1. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusSetting = 1 (Audio) |
| 103 | NR1L-VS-094 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusSetting = 0 (Off) |
| 103 | NR1L-VS-094 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusSetting =' | 2. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusSetting = 0 (Off) |
| 103 | NR1L-VS-094 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusSetting =' | 1. IPC_VEHICLE_SETUP.FSFCWPlusSetting = 1 (Audio) is sent |
| 103 | NR1L-VS-094 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusSetting =' | 2. IPC_VEHICLE_SETUP.FSFCWPlusSetting = 0 (Off) is sent |
| 106 | NR1L-VS-097 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusActivationMode =' | IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = one of [0 (Near), 1 (Med), 2 (Far)] |
| 106 | NR1L-VS-097 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 1 (Med) |
| 106 | NR1L-VS-097 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusActivationMode =' | 1. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 1 (Med) |
| 106 | NR1L-VS-097 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 0 (Near) |
| 106 | NR1L-VS-097 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusActivationMode =' | 2. Send CAN: IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 0 (Near) |
| 106 | NR1L-VS-097 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusActivationMode =' | 1. IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 1 (Med) is sent |
| 106 | NR1L-VS-097 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.FSFCWPlusActivationMode =' | 2. IPC_VEHICLE_SETUP.FSFCWPlusActivationMode = 0 (Near) is sent |
| 109 | NR1L-VS-100 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.GreetingLightsEnable =' | IPC_VEHICLE_SETUP.GreetingLightsEnable = one of [0 (True), 1 (False)] |
| 109 | NR1L-VS-100 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.GreetingLightsEnable = 1 (False) |
| 109 | NR1L-VS-100 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.GreetingLightsEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.GreetingLightsEnable = 1 (False) |
| 109 | NR1L-VS-100 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.GreetingLightsEnable = 0 (True) |
| 109 | NR1L-VS-100 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.GreetingLightsEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.GreetingLightsEnable = 0 (True) |
| 109 | NR1L-VS-100 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.GreetingLightsEnable =' | 1. IPC_VEHICLE_SETUP.GreetingLightsEnable = 1 (False) is sent |
| 109 | NR1L-VS-100 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.GreetingLightsEnable =' | 2. IPC_VEHICLE_SETUP.GreetingLightsEnable = 0 (True) is sent |
| 112 | NR1L-VS-103 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. Set the "Headlights Off Delay" customer setting to 0sec and check that TELEMA |
| 112 | NR1L-VS-103 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req = 0 (0sec) is sent |
| 113 | NR1L-VS-104 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. Set the "Headlights Off Delay" customer setting to 30sec and check that TELEM |
| 113 | NR1L-VS-104 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req = 1 (30sec) is sent |
| 114 | NR1L-VS-105 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. Set the "Headlights Off Delay" customer setting to 60sec and check that TELEM |
| 114 | NR1L-VS-105 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req = 2 (60sec) is sent |
| 115 | NR1L-VS-106 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. Set the "Headlights Off Delay" customer setting to 90sec and check that TELEM |
| 115 | NR1L-VS-106 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HeadlightsOffDelay_Req = 3 (90sec) is sent |
| 116 | NR1L-VS-107 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 116 | NR1L-VS-107 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 116 | NR1L-VS-107 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 0 (0sec) |
| 116 | NR1L-VS-107 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 0 (0sec) |
| 116 | NR1L-VS-107 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) is sent |
| 116 | NR1L-VS-107 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 0 (0sec) is sent |
| 117 | NR1L-VS-108 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 117 | NR1L-VS-108 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 117 | NR1L-VS-108 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 117 | NR1L-VS-108 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 117 | NR1L-VS-108 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) is sent |
| 117 | NR1L-VS-108 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) is sent |
| 118 | NR1L-VS-109 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 118 | NR1L-VS-109 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) |
| 118 | NR1L-VS-109 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 2 (60sec) |
| 118 | NR1L-VS-109 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. Send CAN: IPC_VEHICLE_SETUP.HeadlightsOffDelay = 2 (60sec) |
| 118 | NR1L-VS-109 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 1. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 1 (30sec) is sent |
| 118 | NR1L-VS-109 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadlightsOffDelay =' | 2. IPC_VEHICLE_SETUP.HeadlightsOffDelay = 2 (60sec) is sent |
| 121 | NR1L-VS-112 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req =' | 3. Set the "Headlights with Wipers" customer setting to Off and check that TELEM |
| 121 | NR1L-VS-112 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req =' | 3. TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req = 0 (Off) is sent |
| 122 | NR1L-VS-113 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req =' | 3. Set the "Headlights with Wipers" customer setting to On and check that TELEMA |
| 122 | NR1L-VS-113 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req =' | 3. TELEMATIC_VEHICLE_SETUP.HeadLightWipers_Req = 1 (On) is sent |
| 123 | NR1L-VS-114 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadLightWipers =' | IPC_VEHICLE_SETUP.HeadLightWipers = one of [0 (Off), 1 (On)] |
| 123 | NR1L-VS-114 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HeadLightWipers = 1 (On) |
| 123 | NR1L-VS-114 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadLightWipers =' | 1. Send CAN: IPC_VEHICLE_SETUP.HeadLightWipers = 1 (On) |
| 123 | NR1L-VS-114 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HeadLightWipers = 0 (Off) |
| 123 | NR1L-VS-114 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadLightWipers =' | 2. Send CAN: IPC_VEHICLE_SETUP.HeadLightWipers = 0 (Off) |
| 123 | NR1L-VS-114 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadLightWipers =' | 1. IPC_VEHICLE_SETUP.HeadLightWipers = 1 (On) is sent |
| 123 | NR1L-VS-114 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HeadLightWipers =' | 2. IPC_VEHICLE_SETUP.HeadLightWipers = 0 (Off) is sent |
| 126 | NR1L-VS-117 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req =' | 3. Set the "Hill Start Assist" customer setting to Off and check that TELEMATIC_ |
| 126 | NR1L-VS-117 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req = 0 (Off) is sent |
| 127 | NR1L-VS-118 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req =' | 3. Set the "Hill Start Assist" customer setting to On and check that TELEMATIC_V |
| 127 | NR1L-VS-118 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Hill_Start_Assist_Req = 1 (On) is sent |
| 128 | NR1L-VS-119 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Hill_Start_Assist =' | IPC_VEHICLE_SETUP.Hill_Start_Assist = one of [0 (Off), 1 (On)] |
| 128 | NR1L-VS-119 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Hill_Start_Assist = 1 (On) |
| 128 | NR1L-VS-119 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Hill_Start_Assist =' | 1. Send CAN: IPC_VEHICLE_SETUP.Hill_Start_Assist = 1 (On) |
| 128 | NR1L-VS-119 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Hill_Start_Assist = 0 (Off) |
| 128 | NR1L-VS-119 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Hill_Start_Assist =' | 2. Send CAN: IPC_VEHICLE_SETUP.Hill_Start_Assist = 0 (Off) |
| 128 | NR1L-VS-119 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Hill_Start_Assist =' | 1. IPC_VEHICLE_SETUP.Hill_Start_Assist = 1 (On) is sent |
| 128 | NR1L-VS-119 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Hill_Start_Assist =' | 2. IPC_VEHICLE_SETUP.Hill_Start_Assist = 0 (Off) is sent |
| 131 | NR1L-VS-122 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. Set the "Horn With Lock" customer setting to Off and check that TELEMATIC_VEH |
| 131 | NR1L-VS-122 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req = 0 (Off) is sent |
| 132 | NR1L-VS-123 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. Set the "Horn With Lock" customer setting to 1st Press and check that TELEMAT |
| 132 | NR1L-VS-123 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req = 1 (1st Press) is sent |
| 133 | NR1L-VS-124 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. Set the "Horn With Lock" customer setting to 2nd Press and check that TELEMAT |
| 133 | NR1L-VS-124 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SoundHornLock_Req = 2 (2nd Press) is sent |
| 134 | NR1L-VS-125 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornLock =' | IPC_VEHICLE_SETUP.SoundHornLock = one of [0 (Off), 1 (1st Press), 2 (2nd Press)] |
| 134 | NR1L-VS-125 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.SoundHornLock = 1 (1st Press) |
| 134 | NR1L-VS-125 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornLock =' | 1. Send CAN: IPC_VEHICLE_SETUP.SoundHornLock = 1 (1st Press) |
| 134 | NR1L-VS-125 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.SoundHornLock = 0 (Off) |
| 134 | NR1L-VS-125 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornLock =' | 2. Send CAN: IPC_VEHICLE_SETUP.SoundHornLock = 0 (Off) |
| 134 | NR1L-VS-125 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornLock =' | 1. IPC_VEHICLE_SETUP.SoundHornLock = 1 (1st Press) is sent |
| 134 | NR1L-VS-125 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornLock =' | 2. IPC_VEHICLE_SETUP.SoundHornLock = 0 (Off) is sent |
| 137 | NR1L-VS-128 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req =' | 2. Set the "Horn With Remote Start" customer setting to Off and check that TELEM |
| 137 | NR1L-VS-128 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req = 1 (Off) is sent |
| 138 | NR1L-VS-129 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req =' | 2. Set the "Horn With Remote Start" customer setting to On and check that TELEMA |
| 138 | NR1L-VS-129 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SoundHornRemoteStart_Req = 0 (On) is sent |
| 139 | NR1L-VS-130 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornRemoteStart =' | IPC_VEHICLE_SETUP.SoundHornRemoteStart = one of [0 (On), 1 (Off)] |
| 139 | NR1L-VS-130 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.SoundHornRemoteStart = 1 (Off) |
| 139 | NR1L-VS-130 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornRemoteStart =' | 1. Send CAN: IPC_VEHICLE_SETUP.SoundHornRemoteStart = 1 (Off) |
| 139 | NR1L-VS-130 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.SoundHornRemoteStart = 0 (On) |
| 139 | NR1L-VS-130 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornRemoteStart =' | 2. Send CAN: IPC_VEHICLE_SETUP.SoundHornRemoteStart = 0 (On) |
| 139 | NR1L-VS-130 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornRemoteStart =' | 1. IPC_VEHICLE_SETUP.SoundHornRemoteStart = 1 (Off) is sent |
| 139 | NR1L-VS-130 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SoundHornRemoteStart =' | 2. IPC_VEHICLE_SETUP.SoundHornRemoteStart = 0 (On) is sent |
| 143 | NR1L-VS-134 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. Set the "Illuminated Approach" customer setting to Zero and check that TELEMA |
| 143 | NR1L-VS-134 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 0 (Zero) is sent |
| 144 | NR1L-VS-135 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. Set the "Illuminated Approach" customer setting to Thirty and check that TELE |
| 144 | NR1L-VS-135 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 1 (Thirty) is sent |
| 145 | NR1L-VS-136 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. Set the "Illuminated Approach" customer setting to Sixty and check that TELEM |
| 145 | NR1L-VS-136 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 2 (Sixty) is sent |
| 146 | NR1L-VS-137 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. Set the "Illuminated Approach" customer setting to Ninety and check that TELE |
| 146 | NR1L-VS-137 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 3 (Ninety) is sent |
| 147 | NR1L-VS-138 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Illuminated_Approach =' | IPC_VEHICLE_SETUP.Illuminated_Approach = one of [0 (Zero), 1 (Thirty), 2 (Sixty) |
| 147 | NR1L-VS-138 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Illuminated_Approach = 1 (Thirty) |
| 147 | NR1L-VS-138 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Illuminated_Approach =' | 1. Send CAN: IPC_VEHICLE_SETUP.Illuminated_Approach = 1 (Thirty) |
| 147 | NR1L-VS-138 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Illuminated_Approach = 0 (Zero) |
| 147 | NR1L-VS-138 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Illuminated_Approach =' | 2. Send CAN: IPC_VEHICLE_SETUP.Illuminated_Approach = 0 (Zero) |
| 147 | NR1L-VS-138 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Illuminated_Approach =' | 1. IPC_VEHICLE_SETUP.Illuminated_Approach = 1 (Thirty) is sent |
| 147 | NR1L-VS-138 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Illuminated_Approach =' | 2. IPC_VEHICLE_SETUP.Illuminated_Approach = 0 (Zero) is sent |
| 150 | NR1L-VS-141 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Intensity =' | IPC_VEHICLE_SETUP.LDW_Intensity = one of [0 (Low), 1 (Med), 2 (High)] |
| 150 | NR1L-VS-141 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.LDW_Intensity = 1 (Med) |
| 150 | NR1L-VS-141 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Intensity =' | 1. Send CAN: IPC_VEHICLE_SETUP.LDW_Intensity = 1 (Med) |
| 150 | NR1L-VS-141 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.LDW_Intensity = 0 (Low) |
| 150 | NR1L-VS-141 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Intensity =' | 2. Send CAN: IPC_VEHICLE_SETUP.LDW_Intensity = 0 (Low) |
| 150 | NR1L-VS-141 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Intensity =' | 1. IPC_VEHICLE_SETUP.LDW_Intensity = 1 (Med) is sent |
| 150 | NR1L-VS-141 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Intensity =' | 2. IPC_VEHICLE_SETUP.LDW_Intensity = 0 (Low) is sent |
| 153 | NR1L-VS-144 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Sensibility =' | IPC_VEHICLE_SETUP.LDW_Sensibility = one of [0 (Early), 1 (Med), 2 (Late)] |
| 153 | NR1L-VS-144 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.LDW_Sensibility = 1 (Med) |
| 153 | NR1L-VS-144 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Sensibility =' | 1. Send CAN: IPC_VEHICLE_SETUP.LDW_Sensibility = 1 (Med) |
| 153 | NR1L-VS-144 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.LDW_Sensibility = 0 (Early) |
| 153 | NR1L-VS-144 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Sensibility =' | 2. Send CAN: IPC_VEHICLE_SETUP.LDW_Sensibility = 0 (Early) |
| 153 | NR1L-VS-144 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Sensibility =' | 1. IPC_VEHICLE_SETUP.LDW_Sensibility = 1 (Med) is sent |
| 153 | NR1L-VS-144 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LDW_Sensibility =' | 2. IPC_VEHICLE_SETUP.LDW_Sensibility = 0 (Early) is sent |
| 155 | NR1L-VS-146 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LanguageSelection =' | IPC_VEHICLE_SETUP.LanguageSelection = one of [0 (Italian), 1 (Deutsch), 2 (Engli |
| 155 | NR1L-VS-146 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.LanguageSelection = 1 (Deutsch) |
| 155 | NR1L-VS-146 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LanguageSelection =' | 1. Send CAN: IPC_VEHICLE_SETUP.LanguageSelection = 1 (Deutsch) |
| 155 | NR1L-VS-146 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.LanguageSelection = 0 (Italian) |
| 155 | NR1L-VS-146 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LanguageSelection =' | 2. Send CAN: IPC_VEHICLE_SETUP.LanguageSelection = 0 (Italian) |
| 155 | NR1L-VS-146 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LanguageSelection =' | 1. IPC_VEHICLE_SETUP.LanguageSelection = 1 (Deutsch) is sent |
| 155 | NR1L-VS-146 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.LanguageSelection =' | 2. IPC_VEHICLE_SETUP.LanguageSelection = 0 (Italian) is sent |
| 157 | NR1L-VS-148 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req =' | 2. Set the "Max Power Level" customer setting to Level1 and check that TELEMATIC |
| 157 | NR1L-VS-148 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req = 0 (Level1) is sent |
| 158 | NR1L-VS-149 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req =' | 2. Set the "Max Power Level" customer setting to Level2 and check that TELEMATIC |
| 158 | NR1L-VS-149 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req =' | 2. TELEMATIC_VEHICLE_SETUP.SOC_Max_Lev_Req = 1 (Level2) is sent |
| 159 | NR1L-VS-150 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SOC_Max_Lev =' | IPC_VEHICLE_SETUP.SOC_Max_Lev = one of [0 (Level1), 1 (Level2)] |
| 159 | NR1L-VS-150 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.SOC_Max_Lev = 1 (Level2) |
| 159 | NR1L-VS-150 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SOC_Max_Lev =' | 1. Send CAN: IPC_VEHICLE_SETUP.SOC_Max_Lev = 1 (Level2) |
| 159 | NR1L-VS-150 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.SOC_Max_Lev = 0 (Level1) |
| 159 | NR1L-VS-150 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SOC_Max_Lev =' | 2. Send CAN: IPC_VEHICLE_SETUP.SOC_Max_Lev = 0 (Level1) |
| 159 | NR1L-VS-150 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SOC_Max_Lev =' | 1. IPC_VEHICLE_SETUP.SOC_Max_Lev = 1 (Level2) is sent |
| 159 | NR1L-VS-150 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.SOC_Max_Lev =' | 2. IPC_VEHICLE_SETUP.SOC_Max_Lev = 0 (Level1) is sent |
| 162 | NR1L-VS-153 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req =' | 3. Set the "Navigation Turn by Turn" customer setting to Off and check that TELE |
| 162 | NR1L-VS-153 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req =' | 3. TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req = 1 (Off) is sent |
| 163 | NR1L-VS-154 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req =' | 3. Set the "Navigation Turn by Turn" customer setting to On and check that TELEM |
| 163 | NR1L-VS-154 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req =' | 3. TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req = 0 (On) is sent |
| 164 | NR1L-VS-155 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.NavRepetition =' | IPC_VEHICLE_SETUP.NavRepetition = one of [0 (Absent), 1 (Present)] |
| 164 | NR1L-VS-155 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.NavRepetition = 1 (Present) |
| 164 | NR1L-VS-155 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.NavRepetition =' | 1. Send CAN: IPC_VEHICLE_SETUP.NavRepetition = 1 (Present) |
| 164 | NR1L-VS-155 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.NavRepetition = 0 (Absent) |
| 164 | NR1L-VS-155 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.NavRepetition =' | 2. Send CAN: IPC_VEHICLE_SETUP.NavRepetition = 0 (Absent) |
| 164 | NR1L-VS-155 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.NavRepetition =' | 1. IPC_VEHICLE_SETUP.NavRepetition = 1 (Present) is sent |
| 164 | NR1L-VS-155 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.NavRepetition =' | 2. IPC_VEHICLE_SETUP.NavRepetition = 0 (Absent) is sent |
| 167 | NR1L-VS-158 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. Set the "New Speed Zone Indication" customer setting to Off and check that TE |
| 167 | NR1L-VS-158 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req = 0 (Off) is sent |
| 168 | NR1L-VS-159 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. Set the "New Speed Zone Indication" customer setting to Visual and check that |
| 168 | NR1L-VS-159 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req = 1 (Visual) is sent |
| 169 | NR1L-VS-160 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. Set the "New Speed Zone Indication" customer setting to Visual_Chime and chec |
| 169 | NR1L-VS-160 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req =' | 3. TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req = 3 (Visual_Chime) is sent |
| 170 | NR1L-VS-161 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.New_Spd_Zone_Ind =' | IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = one of [0 (Off), 1 (Visual), 2 (Chime), 3 ( |
| 170 | NR1L-VS-161 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 1 (Visual) |
| 170 | NR1L-VS-161 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.New_Spd_Zone_Ind =' | 1. Send CAN: IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 1 (Visual) |
| 170 | NR1L-VS-161 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 0 (Off) |
| 170 | NR1L-VS-161 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.New_Spd_Zone_Ind =' | 2. Send CAN: IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 0 (Off) |
| 170 | NR1L-VS-161 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.New_Spd_Zone_Ind =' | 1. IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 1 (Visual) is sent |
| 170 | NR1L-VS-161 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.New_Spd_Zone_Ind =' | 2. IPC_VEHICLE_SETUP.New_Spd_Zone_Ind = 0 (Off) is sent |
| 173 | NR1L-VS-164 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req =' | 2. Set the "Paddle Shifter" customer setting to Off and check that TELEMATIC_VEH |
| 173 | NR1L-VS-164 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req = 0 (Off) is sent |
| 174 | NR1L-VS-165 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req =' | 2. Set the "Paddle Shifter" customer setting to On and check that TELEMATIC_VEHI |
| 174 | NR1L-VS-165 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Paddle_Shifter_Req = 1 (On) is sent |
| 175 | NR1L-VS-166 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Paddle_Shifter =' | IPC_VEHICLE_SETUP.Paddle_Shifter = one of [0 (Off), 1 (On)] |
| 175 | NR1L-VS-166 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Paddle_Shifter = 1 (On) |
| 175 | NR1L-VS-166 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Paddle_Shifter =' | 1. Send CAN: IPC_VEHICLE_SETUP.Paddle_Shifter = 1 (On) |
| 175 | NR1L-VS-166 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Paddle_Shifter = 0 (Off) |
| 175 | NR1L-VS-166 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Paddle_Shifter =' | 2. Send CAN: IPC_VEHICLE_SETUP.Paddle_Shifter = 0 (Off) |
| 175 | NR1L-VS-166 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Paddle_Shifter =' | 1. IPC_VEHICLE_SETUP.Paddle_Shifter = 1 (On) is sent |
| 175 | NR1L-VS-166 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Paddle_Shifter =' | 2. IPC_VEHICLE_SETUP.Paddle_Shifter = 0 (Off) is sent |
| 180 | NR1L-VS-171 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. Set the "Park Sense Front Volume" customer setting to Low and check that TELE |
| 180 | NR1L-VS-171 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req = 0 (Low) is sent |
| 181 | NR1L-VS-172 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. Set the "Park Sense Front Volume" customer setting to Medium and check that T |
| 181 | NR1L-VS-172 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req = 1 (Medium) is sent |
| 182 | NR1L-VS-173 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. Set the "Park Sense Front Volume" customer setting to High and check that TEL |
| 182 | NR1L-VS-173 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req = 2 (High) is sent |
| 183 | NR1L-VS-174 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeFront =' | IPC_VEHICLE_SETUP.PamChimeVolumeFront = one of [0 (Low), 1 (Medium), 2 (High)] |
| 183 | NR1L-VS-174 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeFront = 1 (Medium) |
| 183 | NR1L-VS-174 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeFront =' | 1. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeFront = 1 (Medium) |
| 183 | NR1L-VS-174 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeFront = 0 (Low) |
| 183 | NR1L-VS-174 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeFront =' | 2. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeFront = 0 (Low) |
| 183 | NR1L-VS-174 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeFront =' | 1. IPC_VEHICLE_SETUP.PamChimeVolumeFront = 1 (Medium) is sent |
| 183 | NR1L-VS-174 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeFront =' | 2. IPC_VEHICLE_SETUP.PamChimeVolumeFront = 0 (Low) is sent |
| 184 | NR1L-VS-175 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. Set the "Park Sense Rear Volume" customer setting to Low and check that TELEM |
| 184 | NR1L-VS-175 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req = 0 (Low) is sent |
| 185 | NR1L-VS-176 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. Set the "Park Sense Rear Volume" customer setting to Medium and check that TE |
| 185 | NR1L-VS-176 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req = 1 (Medium) is sent |
| 186 | NR1L-VS-177 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. Set the "Park Sense Rear Volume" customer setting to High and check that TELE |
| 186 | NR1L-VS-177 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req = 2 (High) is sent |
| 187 | NR1L-VS-178 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeRear =' | IPC_VEHICLE_SETUP.PamChimeVolumeRear = one of [0 (Low), 1 (Medium), 2 (High)] |
| 187 | NR1L-VS-178 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeRear = 1 (Medium) |
| 187 | NR1L-VS-178 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeRear =' | 1. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeRear = 1 (Medium) |
| 187 | NR1L-VS-178 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeRear = 0 (Low) |
| 187 | NR1L-VS-178 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeRear =' | 2. Send CAN: IPC_VEHICLE_SETUP.PamChimeVolumeRear = 0 (Low) |
| 187 | NR1L-VS-178 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeRear =' | 1. IPC_VEHICLE_SETUP.PamChimeVolumeRear = 1 (Medium) is sent |
| 187 | NR1L-VS-178 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PamChimeVolumeRear =' | 2. IPC_VEHICLE_SETUP.PamChimeVolumeRear = 0 (Low) is sent |
| 190 | NR1L-VS-181 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req =' | 3. Set the "Passive Entry" customer setting to Off and check that TELEMATIC_VEHI |
| 190 | NR1L-VS-181 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req = 1 (Off) is sent |
| 191 | NR1L-VS-182 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req =' | 3. Set the "Passive Entry" customer setting to On and check that TELEMATIC_VEHIC |
| 191 | NR1L-VS-182 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req = 0 (On) is sent |
| 192 | NR1L-VS-183 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PassiveEntry =' | IPC_VEHICLE_SETUP.PassiveEntry = one of [0 (On), 1 (Off)] |
| 192 | NR1L-VS-183 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PassiveEntry = 1 (Off) |
| 192 | NR1L-VS-183 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PassiveEntry =' | 1. Send CAN: IPC_VEHICLE_SETUP.PassiveEntry = 1 (Off) |
| 192 | NR1L-VS-183 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PassiveEntry = 0 (On) |
| 192 | NR1L-VS-183 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PassiveEntry =' | 2. Send CAN: IPC_VEHICLE_SETUP.PassiveEntry = 0 (On) |
| 192 | NR1L-VS-183 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PassiveEntry =' | 1. IPC_VEHICLE_SETUP.PassiveEntry = 1 (Off) is sent |
| 192 | NR1L-VS-183 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PassiveEntry =' | 2. IPC_VEHICLE_SETUP.PassiveEntry = 0 (On) is sent |
| 195 | NR1L-VS-186 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act =' | IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = one of [0 (Off), 1 (On)] |
| 195 | NR1L-VS-186 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 1 (On) |
| 195 | NR1L-VS-186 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act =' | 1. Send CAN: IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 1 (On) |
| 195 | NR1L-VS-186 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 0 (Off) |
| 195 | NR1L-VS-186 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act =' | 2. Send CAN: IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 0 (Off) |
| 195 | NR1L-VS-186 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act =' | 1. IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 1 (On) is sent |
| 195 | NR1L-VS-186 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act =' | 2. IPC_VEHICLE_SETUP.Ped_EM_Brk_Warn_Act = 0 (Off) is sent |
| 198 | NR1L-VS-189 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req =' | 4. Set the "Phone Repetition" customer setting to Off and check that TELEMATIC_V |
| 198 | NR1L-VS-189 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req =' | 4. TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req = 1 (Off) is sent |
| 199 | NR1L-VS-190 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req =' | 4. Set the "Phone Repetition" customer setting to On and check that TELEMATIC_VE |
| 199 | NR1L-VS-190 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req =' | 4. TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req = 0 (On) is sent |
| 200 | NR1L-VS-191 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PhoneRepetition =' | IPC_VEHICLE_SETUP.PhoneRepetition = one of [0 (Absent), 1 (Present)] |
| 200 | NR1L-VS-191 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PhoneRepetition = 1 (Present) |
| 200 | NR1L-VS-191 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PhoneRepetition =' | 1. Send CAN: IPC_VEHICLE_SETUP.PhoneRepetition = 1 (Present) |
| 200 | NR1L-VS-191 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PhoneRepetition = 0 (Absent) |
| 200 | NR1L-VS-191 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PhoneRepetition =' | 2. Send CAN: IPC_VEHICLE_SETUP.PhoneRepetition = 0 (Absent) |
| 200 | NR1L-VS-191 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PhoneRepetition =' | 1. IPC_VEHICLE_SETUP.PhoneRepetition = 1 (Present) is sent |
| 200 | NR1L-VS-191 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PhoneRepetition =' | 2. IPC_VEHICLE_SETUP.PhoneRepetition = 0 (Absent) is sent |
| 203 | NR1L-VS-194 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req =' | 3. Set the "Power Liftgate/Tailgate Alert" customer setting to Off and check tha |
| 203 | NR1L-VS-194 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PLGAlert_Req = 0 (Off) is sent |
| 204 | NR1L-VS-195 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req =' | 3. Set the "Power Liftgate/Tailgate Alert" customer setting to On and check that |
| 204 | NR1L-VS-195 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req =' | 3. TELEMATIC_VEHICLE_SETUP.PLGAlert_Req = 1 (On) is sent |
| 205 | NR1L-VS-196 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PLGAlert =' | IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off), 1 (On)] |
| 205 | NR1L-VS-196 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.PLGAlert = 1 (On) |
| 205 | NR1L-VS-196 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PLGAlert =' | 1. Send CAN: IPC_VEHICLE_SETUP.PLGAlert = 1 (On) |
| 205 | NR1L-VS-196 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.PLGAlert = 0 (Off) |
| 205 | NR1L-VS-196 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PLGAlert =' | 2. Send CAN: IPC_VEHICLE_SETUP.PLGAlert = 0 (Off) |
| 205 | NR1L-VS-196 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PLGAlert =' | 1. IPC_VEHICLE_SETUP.PLGAlert = 1 (On) is sent |
| 205 | NR1L-VS-196 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.PLGAlert =' | 2. IPC_VEHICLE_SETUP.PLGAlert = 0 (Off) is sent |
| 209 | NR1L-VS-200 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req =' | 3. Set the "Power Side Step" customer setting to Auto and check that TELEMATIC_V |
| 209 | NR1L-VS-200 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req = 0 (Auto) is sent |
| 210 | NR1L-VS-201 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req =' | 3. Set the "Power Side Step" customer setting to Store and check that TELEMATIC_ |
| 210 | NR1L-VS-201 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Power_Side_Step_Req = 1 (Store) is sent |
| 211 | NR1L-VS-202 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Power_Side_Step =' | IPC_VEHICLE_SETUP.Power_Side_Step = one of [0 (Auto), 1 (Store)] |
| 211 | NR1L-VS-202 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Power_Side_Step = 1 (Store) |
| 211 | NR1L-VS-202 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Power_Side_Step =' | 1. Send CAN: IPC_VEHICLE_SETUP.Power_Side_Step = 1 (Store) |
| 211 | NR1L-VS-202 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Power_Side_Step = 0 (Auto) |
| 211 | NR1L-VS-202 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Power_Side_Step =' | 2. Send CAN: IPC_VEHICLE_SETUP.Power_Side_Step = 0 (Auto) |
| 211 | NR1L-VS-202 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Power_Side_Step =' | 1. IPC_VEHICLE_SETUP.Power_Side_Step = 1 (Store) is sent |
| 211 | NR1L-VS-202 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Power_Side_Step =' | 2. IPC_VEHICLE_SETUP.Power_Side_Step = 0 (Auto) is sent |
| 214 | NR1L-VS-205 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Power_Tailgate_Enable =' | IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = one of [0 (Disabled), 1 (Enabled)] |
| 214 | NR1L-VS-205 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 1 (Enabled) |
| 214 | NR1L-VS-205 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Power_Tailgate_Enable =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 1 (Enabled) |
| 214 | NR1L-VS-205 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 0 (Disabled) |
| 214 | NR1L-VS-205 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Power_Tailgate_Enable =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 0 (Disabled) |
| 214 | NR1L-VS-205 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Power_Tailgate_Enable =' | 1. IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 1 (Enabled) is sent |
| 214 | NR1L-VS-205 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Power_Tailgate_Enable =' | 2. IPC_VEHICLE_SETUP2.Power_Tailgate_Enable = 0 (Disabled) is sent |
| 218 | NR1L-VS-209 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. Set the "Power Unit" customer setting to HP and check that TELEMATIC_VEHICLE_ |
| 218 | NR1L-VS-209 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HP_Unit_Req = 0 (HP) is sent |
| 219 | NR1L-VS-210 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. Set the "Power Unit" customer setting to PS and check that TELEMATIC_VEHICLE_ |
| 219 | NR1L-VS-210 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HP_Unit_Req = 2 (PS) is sent |
| 220 | NR1L-VS-211 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. Set the "Power Unit" customer setting to kW and check that TELEMATIC_VEHICLE_ |
| 220 | NR1L-VS-211 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.HP_Unit_Req =' | 2. TELEMATIC_VEHICLE_SETUP.HP_Unit_Req = 1 (kW) is sent |
| 221 | NR1L-VS-212 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | IPC_VEHICLE_SETUP.HP_Unit = one of [0 (HP), 1 (kW), 2 (PS)] |
| 221 | NR1L-VS-212 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) |
| 221 | NR1L-VS-212 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 1. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) |
| 221 | NR1L-VS-212 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) |
| 221 | NR1L-VS-212 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 2. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) |
| 221 | NR1L-VS-212 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 1. IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) is sent |
| 221 | NR1L-VS-212 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 2. IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) is sent |
| 224 | NR1L-VS-215 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. Set the "Pressure Unit" customer setting to psi and check that TELEMATIC_VEHI |
| 224 | NR1L-VS-215 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req = 1 (psi) is sent |
| 225 | NR1L-VS-216 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. Set the "Pressure Unit" customer setting to KPa and check that TELEMATIC_VEHI |
| 225 | NR1L-VS-216 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req = 0 (KPa) is sent |
| 226 | NR1L-VS-217 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. Set the "Pressure Unit" customer setting to bar and check that TELEMATIC_VEHI |
| 226 | NR1L-VS-217 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req =' | 4. TELEMATIC_VEHICLE_SETUP.TyrePress_Unit_Req = 2 (bar) is sent |
| 227 | NR1L-VS-218 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.TyrePress_Unit =' | IPC_VEHICLE_SETUP.TyrePress_Unit = one of [0 (KPa), 1 (psi), 2 (bar)] |
| 227 | NR1L-VS-218 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.TyrePress_Unit = 1 (psi) |
| 227 | NR1L-VS-218 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.TyrePress_Unit =' | 1. Send CAN: IPC_VEHICLE_SETUP.TyrePress_Unit = 1 (psi) |
| 227 | NR1L-VS-218 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.TyrePress_Unit = 0 (KPa) |
| 227 | NR1L-VS-218 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.TyrePress_Unit =' | 2. Send CAN: IPC_VEHICLE_SETUP.TyrePress_Unit = 0 (KPa) |
| 227 | NR1L-VS-218 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.TyrePress_Unit =' | 1. IPC_VEHICLE_SETUP.TyrePress_Unit = 1 (psi) is sent |
| 227 | NR1L-VS-218 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.TyrePress_Unit =' | 2. IPC_VEHICLE_SETUP.TyrePress_Unit = 0 (KPa) is sent |
| 230 | NR1L-VS-221 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req =' | 2. Set the "RKE Linked to Memory" customer setting to Off and check that TELEMAT |
| 230 | NR1L-VS-221 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req =' | 2. TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req = 0 (Off) is sent |
| 231 | NR1L-VS-222 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req =' | 2. Set the "RKE Linked to Memory" customer setting to On and check that TELEMATI |
| 231 | NR1L-VS-222 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req =' | 2. TELEMATIC_VEHICLE_SETUP.RKEMemoryLinkEnable_Req = 1 (On) is sent |
| 232 | NR1L-VS-223 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RKEMemoryLinkEnable =' | IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = one of [0 (Off), 1 (On)] |
| 232 | NR1L-VS-223 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 1 (On) |
| 232 | NR1L-VS-223 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RKEMemoryLinkEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 1 (On) |
| 232 | NR1L-VS-223 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 0 (Off) |
| 232 | NR1L-VS-223 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RKEMemoryLinkEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 0 (Off) |
| 232 | NR1L-VS-223 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RKEMemoryLinkEnable =' | 1. IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 1 (On) is sent |
| 232 | NR1L-VS-223 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RKEMemoryLinkEnable =' | 2. IPC_VEHICLE_SETUP.RKEMemoryLinkEnable = 0 (Off) is sent |
| 235 | NR1L-VS-226 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RainSensorLevel =' | IPC_VEHICLE_SETUP.RainSensorLevel = one of [0 (Not_Enable), 1 (Enable)] |
| 235 | NR1L-VS-226 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.RainSensorLevel = 1 (Enable) |
| 235 | NR1L-VS-226 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RainSensorLevel =' | 1. Send CAN: IPC_VEHICLE_SETUP.RainSensorLevel = 1 (Enable) |
| 235 | NR1L-VS-226 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.RainSensorLevel = 0 (Not_Enable) |
| 235 | NR1L-VS-226 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RainSensorLevel =' | 2. Send CAN: IPC_VEHICLE_SETUP.RainSensorLevel = 0 (Not_Enable) |
| 235 | NR1L-VS-226 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RainSensorLevel =' | 1. IPC_VEHICLE_SETUP.RainSensorLevel = 1 (Enable) is sent |
| 235 | NR1L-VS-226 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RainSensorLevel =' | 2. IPC_VEHICLE_SETUP.RainSensorLevel = 0 (Not_Enable) is sent |
| 238 | NR1L-VS-229 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req =' | 3. Set the "Ready to Drive Pop-Up" customer setting to Off and check that TELEMA |
| 238 | NR1L-VS-229 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req = 0 (Off) is sent |
| 239 | NR1L-VS-230 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req =' | 3. Set the "Ready to Drive Pop-Up" customer setting to On and check that TELEMAT |
| 239 | NR1L-VS-230 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Rdy_To_Drive_Req = 1 (On) is sent |
| 240 | NR1L-VS-231 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Rdy_To_Drive =' | IPC_VEHICLE_SETUP.Rdy_To_Drive = one of [0 (Off), 1 (On)] |
| 240 | NR1L-VS-231 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Rdy_To_Drive = 1 (On) |
| 240 | NR1L-VS-231 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Rdy_To_Drive =' | 1. Send CAN: IPC_VEHICLE_SETUP.Rdy_To_Drive = 1 (On) |
| 240 | NR1L-VS-231 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Rdy_To_Drive = 0 (Off) |
| 240 | NR1L-VS-231 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Rdy_To_Drive =' | 2. Send CAN: IPC_VEHICLE_SETUP.Rdy_To_Drive = 0 (Off) |
| 240 | NR1L-VS-231 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Rdy_To_Drive =' | 1. IPC_VEHICLE_SETUP.Rdy_To_Drive = 1 (On) is sent |
| 240 | NR1L-VS-231 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Rdy_To_Drive =' | 2. IPC_VEHICLE_SETUP.Rdy_To_Drive = 0 (Off) is sent |
| 243 | NR1L-VS-234 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req =' | 2. Set the "Rear Guidance Light Status" customer setting to OFF and check that T |
| 243 | NR1L-VS-234 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req =' | 2. TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req = 0 (OFF) is sent |
| 244 | NR1L-VS-235 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req =' | 2. Set the "Rear Guidance Light Status" customer setting to ON and check that TE |
| 244 | NR1L-VS-235 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req =' | 2. TELEMATIC_FD_8.Rear_Guidance_Light_Status_Req = 1 (ON) is sent |
| 245 | NR1L-VS-236 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status =' | IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = one of [0 (OFF), 1 (ON)] |
| 245 | NR1L-VS-236 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 1 (ON) |
| 245 | NR1L-VS-236 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 1 (ON) |
| 245 | NR1L-VS-236 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 0 (OFF) |
| 245 | NR1L-VS-236 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 0 (OFF) |
| 245 | NR1L-VS-236 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status =' | 1. IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 1 (ON) is sent |
| 245 | NR1L-VS-236 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status =' | 2. IPC_VEHICLE_SETUP2.Rear_Guidance_Light_Status = 0 (OFF) is sent |
| 248 | NR1L-VS-239 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Lights_with_Approach_Req =' | 2. Set the "Rear Guidance Lighting with Approach" customer setting to Off_with_A |
| 248 | NR1L-VS-239 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Lights_with_Approach_Req =' | 2. TELEMATIC_FD_8.Rear_Lights_with_Approach_Req = 0 (Off_with_Approach) is sent |
| 249 | NR1L-VS-240 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Lights_with_Approach_Req =' | 2. Set the "Rear Guidance Lighting with Approach" customer setting to On_with_Ap |
| 249 | NR1L-VS-240 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_8.Rear_Lights_with_Approach_Req =' | 2. TELEMATIC_FD_8.Rear_Lights_with_Approach_Req = 1 (On_with_Approach) is sent |
| 250 | NR1L-VS-241 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach =' | IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = one of [0 (Off_with_Approach), 1  |
| 250 | NR1L-VS-241 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 1 (On_with_Approach) |
| 250 | NR1L-VS-241 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 1 (On_with_Approach) |
| 250 | NR1L-VS-241 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 0 (Off_with_Approach |
| 250 | NR1L-VS-241 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 0 (Off_with_Approach |
| 250 | NR1L-VS-241 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach =' | 1. IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 1 (On_with_Approach) is sent |
| 250 | NR1L-VS-241 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach =' | 2. IPC_VEHICLE_SETUP2.Rear_Lights_with_Approach = 0 (Off_with_Approach) is sent |
| 253 | NR1L-VS-244 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req =' | 2. Set the "Rear Guidance Lights with Cargo Lights" customer setting to Disable  |
| 253 | NR1L-VS-244 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req =' | 2. TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req = 0 (Disable) is sent |
| 254 | NR1L-VS-245 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req =' | 2. Set the "Rear Guidance Lights with Cargo Lights" customer setting to Enable a |
| 254 | NR1L-VS-245 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req =' | 2. TELEMATIC_FD_1.Rear_G_LGT_with_Cargo_Lights_Req = 1 (Enable) is sent |
| 255 | NR1L-VS-246 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights =' | IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = one of [0 (Disable), 1 (Enable |
| 255 | NR1L-VS-246 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 1 (Enable) |
| 255 | NR1L-VS-246 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 1 (Enable) |
| 255 | NR1L-VS-246 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 0 (Disable) |
| 255 | NR1L-VS-246 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 0 (Disable) |
| 255 | NR1L-VS-246 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights =' | 1. IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 1 (Enable) is sent |
| 255 | NR1L-VS-246 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights =' | 2. IPC_VEHICLE_SETUP2.Rear_G_LGT_with_Cargo_Lights = 0 (Disable) is sent |
| 256 | NR1L-VS-247 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req =' | 3. Set the "Rear Seat Reminder" customer setting to Off and check that TELEMATIC |
| 256 | NR1L-VS-247 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req =' | 3. TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req = 0 (Off) is sent |
| 257 | NR1L-VS-248 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.FOA_Alert_Type =' | IPC_VEHICLE_SETUP2.FOA_Alert_Type = one of [0 (Off), 1 (Cluster_Warning), 2 (Clu |
| 257 | NR1L-VS-248 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.FOA_Alert_Type = 1 (Cluster_Warning) |
| 257 | NR1L-VS-248 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.FOA_Alert_Type =' | 1. Send CAN: IPC_VEHICLE_SETUP2.FOA_Alert_Type = 1 (Cluster_Warning) |
| 257 | NR1L-VS-248 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.FOA_Alert_Type = 0 (Off) |
| 257 | NR1L-VS-248 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.FOA_Alert_Type =' | 2. Send CAN: IPC_VEHICLE_SETUP2.FOA_Alert_Type = 0 (Off) |
| 257 | NR1L-VS-248 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.FOA_Alert_Type =' | 1. IPC_VEHICLE_SETUP2.FOA_Alert_Type = 1 (Cluster_Warning) is sent |
| 257 | NR1L-VS-248 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.FOA_Alert_Type =' | 2. IPC_VEHICLE_SETUP2.FOA_Alert_Type = 0 (Off) is sent |
| 258 | NR1L-VS-249 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req =' | 3. Set the "Rear Seat Reminder" customer setting to Cluster_Warning and check th |
| 258 | NR1L-VS-249 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req =' | 3. TELEMATIC_VEHICLE_SETUP.FOA_Alert_Type_Req = 1 (Cluster_Warning) is sent |
| 261 | NR1L-VS-252 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req =' | 2. Set the "Rearview Camera Delay" customer setting to Off and check that TELEMA |
| 261 | NR1L-VS-252 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req = 0 (Off) is sent |
| 262 | NR1L-VS-253 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req =' | 2. Set the "Rearview Camera Delay" customer setting to On and check that TELEMAT |
| 262 | NR1L-VS-253 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Backup_Cam_Delay_Req = 1 (On) is sent |
| 263 | NR1L-VS-254 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Backup_Cam_Delay =' | IPC_VEHICLE_SETUP.Backup_Cam_Delay = one of [0 (Off), 1 (On)] |
| 263 | NR1L-VS-254 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Backup_Cam_Delay = 1 (On) |
| 263 | NR1L-VS-254 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Backup_Cam_Delay =' | 1. Send CAN: IPC_VEHICLE_SETUP.Backup_Cam_Delay = 1 (On) |
| 263 | NR1L-VS-254 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Backup_Cam_Delay = 0 (Off) |
| 263 | NR1L-VS-254 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Backup_Cam_Delay =' | 2. Send CAN: IPC_VEHICLE_SETUP.Backup_Cam_Delay = 0 (Off) |
| 263 | NR1L-VS-254 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Backup_Cam_Delay =' | 1. IPC_VEHICLE_SETUP.Backup_Cam_Delay = 1 (On) is sent |
| 263 | NR1L-VS-254 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Backup_Cam_Delay =' | 2. IPC_VEHICLE_SETUP.Backup_Cam_Delay = 0 (Off) is sent |
| 266 | NR1L-VS-257 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req =' | 2. Set the "Rearview Camera Dynamic Guidelines" customer setting to Dynamic Grid |
| 266 | NR1L-VS-257 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req =' | 2. TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req = 0 (Dynamic Gridlines OFF) is sent |
| 267 | NR1L-VS-258 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req =' | 2. Set the "Rearview Camera Dynamic Guidelines" customer setting to Dynamic Grid |
| 267 | NR1L-VS-258 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req =' | 2. TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req = 1 (Dynamic Gridlines ON) is sent |
| 268 | NR1L-VS-259 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DynamicGrid =' | IPC_VEHICLE_SETUP.DynamicGrid = one of [0 (Dynamic Gridlines OFF), 1 (Dynamic Gr |
| 268 | NR1L-VS-259 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) |
| 268 | NR1L-VS-259 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DynamicGrid =' | 1. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) |
| 268 | NR1L-VS-259 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 0 (Dynamic Gridlines OFF) |
| 268 | NR1L-VS-259 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DynamicGrid =' | 2. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 0 (Dynamic Gridlines OFF) |
| 268 | NR1L-VS-259 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DynamicGrid =' | 1. IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) is sent |
| 268 | NR1L-VS-259 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.DynamicGrid =' | 2. IPC_VEHICLE_SETUP.DynamicGrid = 0 (Dynamic Gridlines OFF) is sent |
| 271 | NR1L-VS-262 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req =' | 2. Set the "Remote Door Unlock" customer setting to Driver and check that TELEMA |
| 271 | NR1L-VS-262 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req = 0 (Driver) is sent |
| 272 | NR1L-VS-263 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req =' | 2. Set the "Remote Door Unlock" customer setting to All and check that TELEMATIC |
| 272 | NR1L-VS-263 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req =' | 2. TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock_Req = 1 (All) is sent |
| 273 | NR1L-VS-264 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemoteDoorUnlock =' | IPC_VEHICLE_SETUP.RemoteDoorUnlock = one of [0 (Driver), 1 (All)] |
| 273 | NR1L-VS-264 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.RemoteDoorUnlock = 1 (All) |
| 273 | NR1L-VS-264 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemoteDoorUnlock =' | 1. Send CAN: IPC_VEHICLE_SETUP.RemoteDoorUnlock = 1 (All) |
| 273 | NR1L-VS-264 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.RemoteDoorUnlock = 0 (Driver) |
| 273 | NR1L-VS-264 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemoteDoorUnlock =' | 2. Send CAN: IPC_VEHICLE_SETUP.RemoteDoorUnlock = 0 (Driver) |
| 273 | NR1L-VS-264 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemoteDoorUnlock =' | 1. IPC_VEHICLE_SETUP.RemoteDoorUnlock = 1 (All) is sent |
| 273 | NR1L-VS-264 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.RemoteDoorUnlock =' | 2. IPC_VEHICLE_SETUP.RemoteDoorUnlock = 0 (Driver) is sent |
| 274 | NR1L-VS-265 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_HLEnbl_Req =' | 4. Set the "SWITCH 1 Hold Last State" customer setting to Disable and check that |
| 274 | NR1L-VS-265 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX1_HLEnbl_Req = 0 (Disable) is sent |
| 275 | NR1L-VS-266 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_HLEnbl_Req =' | 4. Set the "SWITCH 1 Hold Last State" customer setting to Enable and check that  |
| 275 | NR1L-VS-266 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX1_HLEnbl_Req = 1 (Enable) is sent |
| 276 | NR1L-VS-267 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX1_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 276 | NR1L-VS-267 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 1 (Enable) |
| 276 | NR1L-VS-267 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 1 (Enable) |
| 276 | NR1L-VS-267 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 0 (Disable) |
| 276 | NR1L-VS-267 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 0 (Disable) |
| 276 | NR1L-VS-267 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 1 (Enable) is sent |
| 276 | NR1L-VS-267 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX1_HLEnbl = 0 (Disable) is sent |
| 277 | NR1L-VS-268 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_PWRMD_Req =' | 4. Set the "SWITCH 1 Power Mode" customer setting to Ignition and check that TEL |
| 277 | NR1L-VS-268 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX1_PWRMD_Req = 0 (Ignition) is sent |
| 278 | NR1L-VS-269 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_PWRMD_Req =' | 4. Set the "SWITCH 1 Power Mode" customer setting to Battery and check that TELE |
| 278 | NR1L-VS-269 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX1_PWRMD_Req = 1 (Battery) is sent |
| 279 | NR1L-VS-270 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_PWRMD =' | IPC_VEHICLE_SETUP2.AUX1_PWRMD = one of [0 (Ignition), 1 (Battery)] |
| 279 | NR1L-VS-270 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_PWRMD = 1 (Battery) |
| 279 | NR1L-VS-270 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_PWRMD = 1 (Battery) |
| 279 | NR1L-VS-270 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_PWRMD = 0 (Ignition) |
| 279 | NR1L-VS-270 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_PWRMD = 0 (Ignition) |
| 279 | NR1L-VS-270 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX1_PWRMD = 1 (Battery) is sent |
| 279 | NR1L-VS-270 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX1_PWRMD = 0 (Ignition) is sent |
| 280 | NR1L-VS-271 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_TYPE_Req =' | 4. Set the "SWITCH 1 Type" customer setting to Momentary and check that TELEMATI |
| 280 | NR1L-VS-271 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX1_TYPE_Req = 1 (Momentary) is sent |
| 281 | NR1L-VS-272 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_TYPE =' | IPC_VEHICLE_SETUP2.AUX1_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 281 | NR1L-VS-272 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_TYPE = 1 (Momentary) |
| 281 | NR1L-VS-272 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX1_TYPE = 1 (Momentary) |
| 281 | NR1L-VS-272 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_TYPE = 0 (Latching) |
| 281 | NR1L-VS-272 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX1_TYPE = 0 (Latching) |
| 281 | NR1L-VS-272 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX1_TYPE = 1 (Momentary) is sent |
| 281 | NR1L-VS-272 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX1_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX1_TYPE = 0 (Latching) is sent |
| 282 | NR1L-VS-273 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_TYPE_Req =' | 4. Set the "SWITCH 1 Type" customer setting to Latching and check that TELEMATIC |
| 282 | NR1L-VS-273 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX1_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX1_TYPE_Req = 0 (Latching) is sent |
| 283 | NR1L-VS-274 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_HLEnbl_Req =' | 4. Set the "SWITCH 2 Hold Last State" customer setting to Disable and check that |
| 283 | NR1L-VS-274 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX2_HLEnbl_Req = 0 (Disable) is sent |
| 284 | NR1L-VS-275 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_HLEnbl_Req =' | 4. Set the "SWITCH 2 Hold Last State" customer setting to Enable and check that  |
| 284 | NR1L-VS-275 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX2_HLEnbl_Req = 1 (Enable) is sent |
| 285 | NR1L-VS-276 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX2_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 285 | NR1L-VS-276 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 1 (Enable) |
| 285 | NR1L-VS-276 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 1 (Enable) |
| 285 | NR1L-VS-276 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 0 (Disable) |
| 285 | NR1L-VS-276 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 0 (Disable) |
| 285 | NR1L-VS-276 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 1 (Enable) is sent |
| 285 | NR1L-VS-276 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX2_HLEnbl = 0 (Disable) is sent |
| 286 | NR1L-VS-277 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_PWRMD_Req =' | 4. Set the "SWITCH 2 Power Mode" customer setting to Ignition and check that TEL |
| 286 | NR1L-VS-277 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX2_PWRMD_Req = 0 (Ignition) is sent |
| 287 | NR1L-VS-278 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_PWRMD_Req =' | 4. Set the "SWITCH 2 Power Mode" customer setting to Battery and check that TELE |
| 287 | NR1L-VS-278 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX2_PWRMD_Req = 1 (Battery) is sent |
| 288 | NR1L-VS-279 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_PWRMD =' | IPC_VEHICLE_SETUP2.AUX2_PWRMD = one of [0 (Ignition), 1 (Battery)] |
| 288 | NR1L-VS-279 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_PWRMD = 1 (Battery) |
| 288 | NR1L-VS-279 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_PWRMD = 1 (Battery) |
| 288 | NR1L-VS-279 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_PWRMD = 0 (Ignition) |
| 288 | NR1L-VS-279 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_PWRMD = 0 (Ignition) |
| 288 | NR1L-VS-279 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX2_PWRMD = 1 (Battery) is sent |
| 288 | NR1L-VS-279 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX2_PWRMD = 0 (Ignition) is sent |
| 289 | NR1L-VS-280 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_TYPE_Req =' | 4. Set the "SWITCH 2 Type" customer setting to Latching and check that TELEMATIC |
| 289 | NR1L-VS-280 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX2_TYPE_Req = 0 (Latching) is sent |
| 290 | NR1L-VS-281 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_TYPE_Req =' | 4. Set the "SWITCH 2 Type" customer setting to Momentary and check that TELEMATI |
| 290 | NR1L-VS-281 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX2_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX2_TYPE_Req = 1 (Momentary) is sent |
| 291 | NR1L-VS-282 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_TYPE =' | IPC_VEHICLE_SETUP2.AUX2_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 291 | NR1L-VS-282 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_TYPE = 1 (Momentary) |
| 291 | NR1L-VS-282 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX2_TYPE = 1 (Momentary) |
| 291 | NR1L-VS-282 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_TYPE = 0 (Latching) |
| 291 | NR1L-VS-282 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX2_TYPE = 0 (Latching) |
| 291 | NR1L-VS-282 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX2_TYPE = 1 (Momentary) is sent |
| 291 | NR1L-VS-282 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX2_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX2_TYPE = 0 (Latching) is sent |
| 292 | NR1L-VS-283 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_HLEnbl_Req =' | 4. Set the "SWITCH 3 Hold Last State" customer setting to Disable and check that |
| 292 | NR1L-VS-283 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX3_HLEnbl_Req = 0 (Disable) is sent |
| 293 | NR1L-VS-284 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_HLEnbl_Req =' | 4. Set the "SWITCH 3 Hold Last State" customer setting to Enable and check that  |
| 293 | NR1L-VS-284 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX3_HLEnbl_Req = 1 (Enable) is sent |
| 294 | NR1L-VS-285 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX3_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 294 | NR1L-VS-285 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 1 (Enable) |
| 294 | NR1L-VS-285 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 1 (Enable) |
| 294 | NR1L-VS-285 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 0 (Disable) |
| 294 | NR1L-VS-285 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 0 (Disable) |
| 294 | NR1L-VS-285 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 1 (Enable) is sent |
| 294 | NR1L-VS-285 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX3_HLEnbl = 0 (Disable) is sent |
| 295 | NR1L-VS-286 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_PWRMD_Req =' | 4. Set the "SWITCH 3 Power Mode" customer setting to Ignition and check that TEL |
| 295 | NR1L-VS-286 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX3_PWRMD_Req = 0 (Ignition) is sent |
| 296 | NR1L-VS-287 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_PWRMD_Req =' | 4. Set the "SWITCH 3 Power Mode" customer setting to Battery and check that TELE |
| 296 | NR1L-VS-287 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX3_PWRMD_Req = 1 (Battery) is sent |
| 297 | NR1L-VS-288 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_PWRMD =' | IPC_VEHICLE_SETUP2.AUX3_PWRMD = one of [0 (Ignition), 1 (Battery)] |
| 297 | NR1L-VS-288 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_PWRMD = 1 (Battery) |
| 297 | NR1L-VS-288 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_PWRMD = 1 (Battery) |
| 297 | NR1L-VS-288 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_PWRMD = 0 (Ignition) |
| 297 | NR1L-VS-288 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_PWRMD = 0 (Ignition) |
| 297 | NR1L-VS-288 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX3_PWRMD = 1 (Battery) is sent |
| 297 | NR1L-VS-288 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX3_PWRMD = 0 (Ignition) is sent |
| 298 | NR1L-VS-289 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_TYPE_Req =' | 4. Set the "SWITCH 3 Type" customer setting to Latching and check that TELEMATIC |
| 298 | NR1L-VS-289 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX3_TYPE_Req = 0 (Latching) is sent |
| 299 | NR1L-VS-290 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_TYPE_Req =' | 4. Set the "SWITCH 3 Type" customer setting to Momentary and check that TELEMATI |
| 299 | NR1L-VS-290 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX3_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX3_TYPE_Req = 1 (Momentary) is sent |
| 300 | NR1L-VS-291 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_TYPE =' | IPC_VEHICLE_SETUP2.AUX3_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 300 | NR1L-VS-291 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_TYPE = 1 (Momentary) |
| 300 | NR1L-VS-291 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX3_TYPE = 1 (Momentary) |
| 300 | NR1L-VS-291 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_TYPE = 0 (Latching) |
| 300 | NR1L-VS-291 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX3_TYPE = 0 (Latching) |
| 300 | NR1L-VS-291 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX3_TYPE = 1 (Momentary) is sent |
| 300 | NR1L-VS-291 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX3_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX3_TYPE = 0 (Latching) is sent |
| 301 | NR1L-VS-292 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_HLEnbl_Req =' | 4. Set the "SWITCH 4 Hold Last State" customer setting to Disable and check that |
| 301 | NR1L-VS-292 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX4_HLEnbl_Req = 0 (Disable) is sent |
| 302 | NR1L-VS-293 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_HLEnbl_Req =' | 4. Set the "SWITCH 4 Hold Last State" customer setting to Enable and check that  |
| 302 | NR1L-VS-293 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX4_HLEnbl_Req = 1 (Enable) is sent |
| 303 | NR1L-VS-294 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX4_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 303 | NR1L-VS-294 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 1 (Enable) |
| 303 | NR1L-VS-294 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 1 (Enable) |
| 303 | NR1L-VS-294 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 0 (Disable) |
| 303 | NR1L-VS-294 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 0 (Disable) |
| 303 | NR1L-VS-294 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 1 (Enable) is sent |
| 303 | NR1L-VS-294 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX4_HLEnbl = 0 (Disable) is sent |
| 304 | NR1L-VS-295 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_PWRMD_Req =' | 4. Set the "SWITCH 4 Power Mode" customer setting to Ignition and check that TEL |
| 304 | NR1L-VS-295 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX4_PWRMD_Req = 0 (Ignition) is sent |
| 305 | NR1L-VS-296 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_PWRMD_Req =' | 4. Set the "SWITCH 4 Power Mode" customer setting to Battery and check that TELE |
| 305 | NR1L-VS-296 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX4_PWRMD_Req = 1 (Battery) is sent |
| 306 | NR1L-VS-297 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_PWRMD =' | IPC_VEHICLE_SETUP2.AUX4_PWRMD = one of [0 (Ignition), 1 (Battery)] |
| 306 | NR1L-VS-297 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_PWRMD = 1 (Battery) |
| 306 | NR1L-VS-297 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_PWRMD = 1 (Battery) |
| 306 | NR1L-VS-297 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_PWRMD = 0 (Ignition) |
| 306 | NR1L-VS-297 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_PWRMD = 0 (Ignition) |
| 306 | NR1L-VS-297 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX4_PWRMD = 1 (Battery) is sent |
| 306 | NR1L-VS-297 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX4_PWRMD = 0 (Ignition) is sent |
| 307 | NR1L-VS-298 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_TYPE_Req =' | 4. Set the "SWITCH 4 Type" customer setting to Latching and check that TELEMATIC |
| 307 | NR1L-VS-298 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX4_TYPE_Req = 0 (Latching) is sent |
| 308 | NR1L-VS-299 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_TYPE_Req =' | 4. Set the "SWITCH 4 Type" customer setting to Momentary and check that TELEMATI |
| 308 | NR1L-VS-299 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX4_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX4_TYPE_Req = 1 (Momentary) is sent |
| 309 | NR1L-VS-300 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_TYPE =' | IPC_VEHICLE_SETUP2.AUX4_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 309 | NR1L-VS-300 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_TYPE = 1 (Momentary) |
| 309 | NR1L-VS-300 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX4_TYPE = 1 (Momentary) |
| 309 | NR1L-VS-300 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_TYPE = 0 (Latching) |
| 309 | NR1L-VS-300 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX4_TYPE = 0 (Latching) |
| 309 | NR1L-VS-300 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX4_TYPE = 1 (Momentary) is sent |
| 309 | NR1L-VS-300 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX4_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX4_TYPE = 0 (Latching) is sent |
| 310 | NR1L-VS-301 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_HLEnbl_Req =' | 4. Set the "SWITCH 5 Hold Last State" customer setting to Disable and check that |
| 310 | NR1L-VS-301 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX5_HLEnbl_Req = 0 (Disable) is sent |
| 311 | NR1L-VS-302 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_HLEnbl_Req =' | 4. Set the "SWITCH 5 Hold Last State" customer setting to Enable and check that  |
| 311 | NR1L-VS-302 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX5_HLEnbl_Req = 1 (Enable) is sent |
| 312 | NR1L-VS-303 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX5_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 312 | NR1L-VS-303 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 1 (Enable) |
| 312 | NR1L-VS-303 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 1 (Enable) |
| 312 | NR1L-VS-303 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 0 (Disable) |
| 312 | NR1L-VS-303 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 0 (Disable) |
| 312 | NR1L-VS-303 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 1 (Enable) is sent |
| 312 | NR1L-VS-303 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX5_HLEnbl = 0 (Disable) is sent |
| 313 | NR1L-VS-304 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_PWRMD_Req =' | 4. Set the "SWITCH 5 Power Mode" customer setting to IGNITION and check that TEL |
| 313 | NR1L-VS-304 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX5_PWRMD_Req = 0 (IGNITION) is sent |
| 314 | NR1L-VS-305 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_PWRMD_Req =' | 4. Set the "SWITCH 5 Power Mode" customer setting to BATTERY and check that TELE |
| 314 | NR1L-VS-305 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX5_PWRMD_Req = 1 (BATTERY) is sent |
| 315 | NR1L-VS-306 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_PWRMD =' | IPC_VEHICLE_SETUP2.AUX5_PWRMD = one of [0 (IGNITION), 1 (BATTERY)] |
| 315 | NR1L-VS-306 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 1 (BATTERY) |
| 315 | NR1L-VS-306 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 1 (BATTERY) |
| 315 | NR1L-VS-306 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 0 (IGNITION) |
| 315 | NR1L-VS-306 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 0 (IGNITION) |
| 315 | NR1L-VS-306 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX5_PWRMD = 1 (BATTERY) is sent |
| 315 | NR1L-VS-306 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX5_PWRMD = 0 (IGNITION) is sent |
| 316 | NR1L-VS-307 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_TYPE_Req =' | 4. Set the "SWITCH 5 Type" customer setting to Latching and check that TELEMATIC |
| 316 | NR1L-VS-307 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX5_TYPE_Req = 0 (Latching) is sent |
| 317 | NR1L-VS-308 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_TYPE_Req =' | 4. Set the "SWITCH 5 Type" customer setting to Momentary and check that TELEMATI |
| 317 | NR1L-VS-308 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX5_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX5_TYPE_Req = 1 (Momentary) is sent |
| 318 | NR1L-VS-309 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_TYPE =' | IPC_VEHICLE_SETUP2.AUX5_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 318 | NR1L-VS-309 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_TYPE = 1 (Momentary) |
| 318 | NR1L-VS-309 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_TYPE = 1 (Momentary) |
| 318 | NR1L-VS-309 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_TYPE = 0 (Latching) |
| 318 | NR1L-VS-309 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_TYPE = 0 (Latching) |
| 318 | NR1L-VS-309 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX5_TYPE = 1 (Momentary) is sent |
| 318 | NR1L-VS-309 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX5_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX5_TYPE = 0 (Latching) is sent |
| 319 | NR1L-VS-310 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_HLEnbl_Req =' | 4. Set the "SWITCH 6 Hold Last State" customer setting to Disable and check that |
| 319 | NR1L-VS-310 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX6_HLEnbl_Req = 0 (Disable) is sent |
| 320 | NR1L-VS-311 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_HLEnbl_Req =' | 4. Set the "SWITCH 6 Hold Last State" customer setting to Enable and check that  |
| 320 | NR1L-VS-311 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_HLEnbl_Req =' | 4. TELEMATIC_FD_1.AUX6_HLEnbl_Req = 1 (Enable) is sent |
| 321 | NR1L-VS-312 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_HLEnbl =' | IPC_VEHICLE_SETUP2.AUX6_HLEnbl = one of [0 (Disable), 1 (Enable)] |
| 321 | NR1L-VS-312 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 1 (Enable) |
| 321 | NR1L-VS-312 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_HLEnbl =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 1 (Enable) |
| 321 | NR1L-VS-312 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 0 (Disable) |
| 321 | NR1L-VS-312 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_HLEnbl =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 0 (Disable) |
| 321 | NR1L-VS-312 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_HLEnbl =' | 1. IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 1 (Enable) is sent |
| 321 | NR1L-VS-312 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_HLEnbl =' | 2. IPC_VEHICLE_SETUP2.AUX6_HLEnbl = 0 (Disable) is sent |
| 322 | NR1L-VS-313 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_PWRMD_Req =' | 4. Set the "SWITCH 6 Power Mode" customer setting to IGNITION and check that TEL |
| 322 | NR1L-VS-313 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX6_PWRMD_Req = 0 (IGNITION) is sent |
| 323 | NR1L-VS-314 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_PWRMD_Req =' | 4. Set the "SWITCH 6 Power Mode" customer setting to BATTERY and check that TELE |
| 323 | NR1L-VS-314 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_PWRMD_Req =' | 4. TELEMATIC_FD_1.AUX6_PWRMD_Req = 1 (BATTERY) is sent |
| 324 | NR1L-VS-315 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_PWRMD =' | IPC_VEHICLE_SETUP2.AUX6_PWRMD = one of [0 (IGNITION), 1 (BATTERY)] |
| 324 | NR1L-VS-315 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_PWRMD = 1 (BATTERY) |
| 324 | NR1L-VS-315 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_PWRMD =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_PWRMD = 1 (BATTERY) |
| 324 | NR1L-VS-315 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_PWRMD = 0 (IGNITION) |
| 324 | NR1L-VS-315 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_PWRMD =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_PWRMD = 0 (IGNITION) |
| 324 | NR1L-VS-315 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_PWRMD =' | 1. IPC_VEHICLE_SETUP2.AUX6_PWRMD = 1 (BATTERY) is sent |
| 324 | NR1L-VS-315 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_PWRMD =' | 2. IPC_VEHICLE_SETUP2.AUX6_PWRMD = 0 (IGNITION) is sent |
| 325 | NR1L-VS-316 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_TYPE_Req =' | 4. Set the "SWITCH 6 Type" customer setting to Latching and check that TELEMATIC |
| 325 | NR1L-VS-316 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX6_TYPE_Req = 0 (Latching) is sent |
| 326 | NR1L-VS-317 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_TYPE_Req =' | 4. Set the "SWITCH 6 Type" customer setting to Momentary and check that TELEMATI |
| 326 | NR1L-VS-317 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.AUX6_TYPE_Req =' | 4. TELEMATIC_FD_1.AUX6_TYPE_Req = 1 (Momentary) is sent |
| 327 | NR1L-VS-318 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_TYPE =' | IPC_VEHICLE_SETUP2.AUX6_TYPE = one of [0 (Latching), 1 (Momentary)] |
| 327 | NR1L-VS-318 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_TYPE = 1 (Momentary) |
| 327 | NR1L-VS-318 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_TYPE =' | 1. Send CAN: IPC_VEHICLE_SETUP2.AUX6_TYPE = 1 (Momentary) |
| 327 | NR1L-VS-318 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_TYPE = 0 (Latching) |
| 327 | NR1L-VS-318 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_TYPE =' | 2. Send CAN: IPC_VEHICLE_SETUP2.AUX6_TYPE = 0 (Latching) |
| 327 | NR1L-VS-318 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_TYPE =' | 1. IPC_VEHICLE_SETUP2.AUX6_TYPE = 1 (Momentary) is sent |
| 327 | NR1L-VS-318 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.AUX6_TYPE =' | 2. IPC_VEHICLE_SETUP2.AUX6_TYPE = 0 (Latching) is sent |
| 330 | NR1L-VS-321 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.SignatureLightingEnable =' | IPC_VEHICLE_SETUP2.SignatureLightingEnable = one of [0 (DISABLE), 1 (ENABLE)] |
| 330 | NR1L-VS-321 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.SignatureLightingEnable = 1 (ENABLE) |
| 330 | NR1L-VS-321 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.SignatureLightingEnable =' | 1. Send CAN: IPC_VEHICLE_SETUP2.SignatureLightingEnable = 1 (ENABLE) |
| 330 | NR1L-VS-321 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.SignatureLightingEnable = 0 (DISABLE) |
| 330 | NR1L-VS-321 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.SignatureLightingEnable =' | 2. Send CAN: IPC_VEHICLE_SETUP2.SignatureLightingEnable = 0 (DISABLE) |
| 330 | NR1L-VS-321 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.SignatureLightingEnable =' | 1. IPC_VEHICLE_SETUP2.SignatureLightingEnable = 1 (ENABLE) is sent |
| 330 | NR1L-VS-321 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.SignatureLightingEnable =' | 2. IPC_VEHICLE_SETUP2.SignatureLightingEnable = 0 (DISABLE) is sent |
| 340 | NR1L-VS-331 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Default_Ride_Height_Req =' | 3. Set the "Suspension Default Ride Height" customer setting to Normal and check |
| 340 | NR1L-VS-331 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Default_Ride_Height_Req =' | 3. TELEMATIC_FD_1.Default_Ride_Height_Req = 0 (Normal) is sent |
| 341 | NR1L-VS-332 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Default_Ride_Height_Req =' | 3. Set the "Suspension Default Ride Height" customer setting to Aerodynamic and  |
| 341 | NR1L-VS-332 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.Default_Ride_Height_Req =' | 3. TELEMATIC_FD_1.Default_Ride_Height_Req = 1 (Aerodynamic) is sent |
| 342 | NR1L-VS-333 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Default_Ride_Height =' | IPC_VEHICLE_SETUP2.Default_Ride_Height = one of [0 (Normal), 1 (Aerodynamic)] |
| 342 | NR1L-VS-333 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.Default_Ride_Height = 1 (Aerodynamic) |
| 342 | NR1L-VS-333 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Default_Ride_Height =' | 1. Send CAN: IPC_VEHICLE_SETUP2.Default_Ride_Height = 1 (Aerodynamic) |
| 342 | NR1L-VS-333 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.Default_Ride_Height = 0 (Normal) |
| 342 | NR1L-VS-333 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Default_Ride_Height =' | 2. Send CAN: IPC_VEHICLE_SETUP2.Default_Ride_Height = 0 (Normal) |
| 342 | NR1L-VS-333 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Default_Ride_Height =' | 1. IPC_VEHICLE_SETUP2.Default_Ride_Height = 1 (Aerodynamic) is sent |
| 342 | NR1L-VS-333 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.Default_Ride_Height =' | 2. IPC_VEHICLE_SETUP2.Default_Ride_Height = 0 (Normal) is sent |
| 345 | NR1L-VS-336 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req =' | 2. Set the "Suspension Display Messages" customer setting to All and check that  |
| 345 | NR1L-VS-336 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req = 0 (All) is sent |
| 346 | NR1L-VS-337 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req =' | 2. Set the "Suspension Display Messages" customer setting to Warnings_Only and c |
| 346 | NR1L-VS-337 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Disp_Message_Req = 1 (Warnings_Only) is sent |
| 347 | NR1L-VS-338 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Disp_Message =' | IPC_VEHICLE_SETUP.Susp_Disp_Message = one of [0 (All), 1 (Warnings_Only)] |
| 347 | NR1L-VS-338 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Disp_Message = 1 (Warnings_Only) |
| 347 | NR1L-VS-338 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Disp_Message =' | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Disp_Message = 1 (Warnings_Only) |
| 347 | NR1L-VS-338 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Disp_Message = 0 (All) |
| 347 | NR1L-VS-338 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Disp_Message =' | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Disp_Message = 0 (All) |
| 347 | NR1L-VS-338 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Disp_Message =' | 1. IPC_VEHICLE_SETUP.Susp_Disp_Message = 1 (Warnings_Only) is sent |
| 347 | NR1L-VS-338 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Disp_Message =' | 2. IPC_VEHICLE_SETUP.Susp_Disp_Message = 0 (All) is sent |
| 350 | NR1L-VS-341 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req =' | 2. Set the "Suspension Flash Lights With Lower" customer setting to Off and chec |
| 350 | NR1L-VS-341 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req = 0 (Off) is sent |
| 351 | NR1L-VS-342 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req =' | 2. Set the "Suspension Flash Lights With Lower" customer setting to On and check |
| 351 | NR1L-VS-342 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Flsh_Lght_Low_Req = 1 (On) is sent |
| 352 | NR1L-VS-343 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low =' | IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = one of [0 (Off), 1 (On)] |
| 352 | NR1L-VS-343 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 1 (On) |
| 352 | NR1L-VS-343 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low =' | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 1 (On) |
| 352 | NR1L-VS-343 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 0 (Off) |
| 352 | NR1L-VS-343 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low =' | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 0 (Off) |
| 352 | NR1L-VS-343 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low =' | 1. IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 1 (On) is sent |
| 352 | NR1L-VS-343 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low =' | 2. IPC_VEHICLE_SETUP.Susp_Flsh_Lght_Low = 0 (Off) is sent |
| 355 | NR1L-VS-346 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req =' | 3. Set the "Suspension Service Mode" customer setting to Off and check that TELE |
| 355 | NR1L-VS-346 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req = 0 (Off) is sent |
| 356 | NR1L-VS-347 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req =' | 3. Set the "Suspension Service Mode" customer setting to On and check that TELEM |
| 356 | NR1L-VS-347 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req = 1 (On) is sent |
| 357 | NR1L-VS-348 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Tire_Jack =' | IPC_VEHICLE_SETUP.Susp_Tire_Jack = one of [0 (Off), 1 (On)] |
| 357 | NR1L-VS-348 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 1 (On) |
| 357 | NR1L-VS-348 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Tire_Jack =' | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 1 (On) |
| 357 | NR1L-VS-348 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 0 (Off) |
| 357 | NR1L-VS-348 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Tire_Jack =' | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 0 (Off) |
| 357 | NR1L-VS-348 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Tire_Jack =' | 1. IPC_VEHICLE_SETUP.Susp_Tire_Jack = 1 (On) is sent |
| 357 | NR1L-VS-348 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Tire_Jack =' | 2. IPC_VEHICLE_SETUP.Susp_Tire_Jack = 0 (Off) is sent |
| 360 | NR1L-VS-351 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req =' | 2. Set the "Suspension Sound Horn With Lower" customer setting to Off and check  |
| 360 | NR1L-VS-351 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req = 0 (Off) is sent |
| 361 | NR1L-VS-352 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req =' | 2. Set the "Suspension Sound Horn With Lower" customer setting to On and check t |
| 361 | NR1L-VS-352 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Susp_Sound_Hrn_Low_Req = 1 (On) is sent |
| 362 | NR1L-VS-353 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low =' | IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = one of [0 (Off), 1 (On)] |
| 362 | NR1L-VS-353 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 1 (On) |
| 362 | NR1L-VS-353 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low =' | 1. Send CAN: IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 1 (On) |
| 362 | NR1L-VS-353 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 0 (Off) |
| 362 | NR1L-VS-353 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low =' | 2. Send CAN: IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 0 (Off) |
| 362 | NR1L-VS-353 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low =' | 1. IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 1 (On) is sent |
| 362 | NR1L-VS-353 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low =' | 2. IPC_VEHICLE_SETUP.Susp_Sound_Hrn_Low = 0 (Off) is sent |
| 367 | NR1L-VS-358 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req =' | 2. Set the "Tilt Mirror in Reverse" customer setting to Off and check that TELEM |
| 367 | NR1L-VS-358 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req = 0 (Off) is sent |
| 368 | NR1L-VS-359 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req =' | 2. Set the "Tilt Mirror in Reverse" customer setting to On and check that TELEMA |
| 368 | NR1L-VS-359 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Tilt_Mirr_Rev_Req = 1 (On) is sent |
| 369 | NR1L-VS-360 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tilt_Mirr_Rev =' | IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = one of [0 (Off), 1 (On)] |
| 369 | NR1L-VS-360 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 1 (On) |
| 369 | NR1L-VS-360 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tilt_Mirr_Rev =' | 1. Send CAN: IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 1 (On) |
| 369 | NR1L-VS-360 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 0 (Off) |
| 369 | NR1L-VS-360 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tilt_Mirr_Rev =' | 2. Send CAN: IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 0 (Off) |
| 369 | NR1L-VS-360 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tilt_Mirr_Rev =' | 1. IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 1 (On) is sent |
| 369 | NR1L-VS-360 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tilt_Mirr_Rev =' | 2. IPC_VEHICLE_SETUP.Tilt_Mirr_Rev = 0 (Off) is sent |
| 375 | NR1L-VS-366 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req =' | 2. Set the "Tire Fill Alert" customer setting to Off and check that TELEMATIC_VE |
| 375 | NR1L-VS-366 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req = 0 (Off) is sent |
| 376 | NR1L-VS-367 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req =' | 2. Set the "Tire Fill Alert" customer setting to On and check that TELEMATIC_VEH |
| 376 | NR1L-VS-367 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Tire_Fill_Alert_Req = 1 (On) is sent |
| 377 | NR1L-VS-368 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tire_Fill_Alert =' | IPC_VEHICLE_SETUP.Tire_Fill_Alert = one of [0 (Off), 1 (On)] |
| 377 | NR1L-VS-368 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Tire_Fill_Alert = 1 (On) |
| 377 | NR1L-VS-368 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tire_Fill_Alert =' | 1. Send CAN: IPC_VEHICLE_SETUP.Tire_Fill_Alert = 1 (On) |
| 377 | NR1L-VS-368 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Tire_Fill_Alert = 0 (Off) |
| 377 | NR1L-VS-368 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tire_Fill_Alert =' | 2. Send CAN: IPC_VEHICLE_SETUP.Tire_Fill_Alert = 0 (Off) |
| 377 | NR1L-VS-368 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tire_Fill_Alert =' | 1. IPC_VEHICLE_SETUP.Tire_Fill_Alert = 1 (On) is sent |
| 377 | NR1L-VS-368 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Tire_Fill_Alert =' | 2. IPC_VEHICLE_SETUP.Tire_Fill_Alert = 0 (Off) is sent |
| 380 | NR1L-VS-371 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req =' | 2. Set the "Torque Unit" customer setting to lb_ft and check that TELEMATIC_VEHI |
| 380 | NR1L-VS-371 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req = 1 (lb_ft) is sent |
| 381 | NR1L-VS-372 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req =' | 2. Set the "Torque Unit" customer setting to Nm and check that TELEMATIC_VEHICLE |
| 381 | NR1L-VS-372 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Torque_Unit_Req = 0 (Nm) is sent |
| 382 | NR1L-VS-373 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | IPC_VEHICLE_SETUP.HP_Unit = one of [0 (HP), 1 (kW), 2 (PS)] |
| 382 | NR1L-VS-373 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) |
| 382 | NR1L-VS-373 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 1. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) |
| 382 | NR1L-VS-373 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) |
| 382 | NR1L-VS-373 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 2. Send CAN: IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) |
| 382 | NR1L-VS-373 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 1. IPC_VEHICLE_SETUP.HP_Unit = 1 (kW) is sent |
| 382 | NR1L-VS-373 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.HP_Unit =' | 2. IPC_VEHICLE_SETUP.HP_Unit = 0 (HP) is sent |
| 385 | NR1L-VS-376 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 0 an |
| 385 | NR1L-VS-376 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 0 (0) is sent |
| 386 | NR1L-VS-377 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 1 an |
| 386 | NR1L-VS-377 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 1 (1) is sent |
| 387 | NR1L-VS-378 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 2 an |
| 387 | NR1L-VS-378 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 2 (2) is sent |
| 388 | NR1L-VS-379 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 3 an |
| 388 | NR1L-VS-379 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 3 (3) is sent |
| 389 | NR1L-VS-380 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 4 an |
| 389 | NR1L-VS-380 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 4 (4) is sent |
| 390 | NR1L-VS-381 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 5 an |
| 390 | NR1L-VS-381 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 5 (5) is sent |
| 391 | NR1L-VS-382 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 6 an |
| 391 | NR1L-VS-382 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 6 (6) is sent |
| 392 | NR1L-VS-383 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 7 an |
| 392 | NR1L-VS-383 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 7 (7) is sent |
| 393 | NR1L-VS-384 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 8 an |
| 393 | NR1L-VS-384 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 8 (8) is sent |
| 394 | NR1L-VS-385 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 9 an |
| 394 | NR1L-VS-385 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 9 (9) is sent |
| 395 | NR1L-VS-386 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 10 a |
| 395 | NR1L-VS-386 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Mph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Mph_Req = 10 (10) is sent |
| 396 | NR1L-VS-387 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Mph =' | IPC_VEHICLE_SETUP2.TSI_Offset_Mph = one of [0 (0), 1 (1), 2 (2), 3 (3), 4 (4), 5 |
| 396 | NR1L-VS-387 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 1 (1) |
| 396 | NR1L-VS-387 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Mph =' | 1. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 1 (1) |
| 396 | NR1L-VS-387 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 0 (0) |
| 396 | NR1L-VS-387 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Mph =' | 2. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 0 (0) |
| 396 | NR1L-VS-387 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Mph =' | 1. IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 1 (1) is sent |
| 396 | NR1L-VS-387 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Mph =' | 2. IPC_VEHICLE_SETUP2.TSI_Offset_Mph = 0 (0) is sent |
| 397 | NR1L-VS-388 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 0 an |
| 397 | NR1L-VS-388 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 0 (0) is sent |
| 398 | NR1L-VS-389 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 1 an |
| 398 | NR1L-VS-389 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 1 (1) is sent |
| 399 | NR1L-VS-390 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 2 an |
| 399 | NR1L-VS-390 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 2 (2) is sent |
| 400 | NR1L-VS-391 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 3 an |
| 400 | NR1L-VS-391 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 3 (3) is sent |
| 401 | NR1L-VS-392 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 4 an |
| 401 | NR1L-VS-392 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 4 (4) is sent |
| 402 | NR1L-VS-393 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 5 an |
| 402 | NR1L-VS-393 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 5 (5) is sent |
| 403 | NR1L-VS-394 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 6 an |
| 403 | NR1L-VS-394 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 6 (6) is sent |
| 404 | NR1L-VS-395 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 7 an |
| 404 | NR1L-VS-395 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 7 (7) is sent |
| 405 | NR1L-VS-396 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 8 an |
| 405 | NR1L-VS-396 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 8 (8) is sent |
| 406 | NR1L-VS-397 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 9 an |
| 406 | NR1L-VS-397 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 9 (9) is sent |
| 407 | NR1L-VS-398 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 10 a |
| 407 | NR1L-VS-398 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 10 (10) is sent |
| 408 | NR1L-VS-399 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 11 a |
| 408 | NR1L-VS-399 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 11 (11) is sent |
| 409 | NR1L-VS-400 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 12 a |
| 409 | NR1L-VS-400 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 12 (12) is sent |
| 410 | NR1L-VS-401 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 13 a |
| 410 | NR1L-VS-401 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 13 (13) is sent |
| 411 | NR1L-VS-402 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 14 a |
| 411 | NR1L-VS-402 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 14 (14) is sent |
| 412 | NR1L-VS-403 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. Set the "Traffic Sign Assist Offset - NAFTA Setting" customer setting to 15 a |
| 412 | NR1L-VS-403 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_1.TSI_Offset_Kph_Req =' | 3. TELEMATIC_FD_1.TSI_Offset_Kph_Req = 15 (15) is sent |
| 413 | NR1L-VS-404 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Kph =' | IPC_VEHICLE_SETUP2.TSI_Offset_Kph = one of [0 (0), 1 (1), 2 (2), 3 (3), 4 (4), 5 |
| 413 | NR1L-VS-404 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 1 (1) |
| 413 | NR1L-VS-404 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Kph =' | 1. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 1 (1) |
| 413 | NR1L-VS-404 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 0 (0) |
| 413 | NR1L-VS-404 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Kph =' | 2. Send CAN: IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 0 (0) |
| 413 | NR1L-VS-404 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Kph =' | 1. IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 1 (1) is sent |
| 413 | NR1L-VS-404 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.TSI_Offset_Kph =' | 2. IPC_VEHICLE_SETUP2.TSI_Offset_Kph = 0 (0) is sent |
| 416 | NR1L-VS-407 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. Set the "Traffic Sign Warning" customer setting to Off and check that TELEMAT |
| 416 | NR1L-VS-407 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req = 0 (Off) is sent |
| 417 | NR1L-VS-408 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. Set the "Traffic Sign Warning" customer setting to Visual and check that TELE |
| 417 | NR1L-VS-408 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req = 1 (Visual) is sent |
| 418 | NR1L-VS-409 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. Set the "Traffic Sign Warning" customer setting to Visual_Chime and check tha |
| 418 | NR1L-VS-409 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req =' | 3. TELEMATIC_VEHICLE_SETUP.Traffic_Sign_Warn_Req = 2 (Visual_Chime) is sent |
| 419 | NR1L-VS-410 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Traffic_Sign_Warn =' | IPC_VEHICLE_SETUP.Traffic_Sign_Warn = one of [0 (Off), 1 (Visual), 2 (Visual_Chi |
| 419 | NR1L-VS-410 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 1 (Visual) |
| 419 | NR1L-VS-410 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Traffic_Sign_Warn =' | 1. Send CAN: IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 1 (Visual) |
| 419 | NR1L-VS-410 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 0 (Off) |
| 419 | NR1L-VS-410 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Traffic_Sign_Warn =' | 2. Send CAN: IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 0 (Off) |
| 419 | NR1L-VS-410 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Traffic_Sign_Warn =' | 1. IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 1 (Visual) is sent |
| 419 | NR1L-VS-410 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Traffic_Sign_Warn =' | 2. IPC_VEHICLE_SETUP.Traffic_Sign_Warn = 0 (Off) is sent |
| 422 | NR1L-VS-413 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Brk_Type =' | IPC_VEHICLE_SETUP.Trail_Brk_Type = one of [0 (Light_Electric), 1 (Heavy_Electric |
| 422 | NR1L-VS-413 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Brk_Type = 1 (Heavy_Electric) |
| 422 | NR1L-VS-413 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Brk_Type =' | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Brk_Type = 1 (Heavy_Electric) |
| 422 | NR1L-VS-413 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Brk_Type = 0 (Light_Electric) |
| 422 | NR1L-VS-413 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Brk_Type =' | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Brk_Type = 0 (Light_Electric) |
| 422 | NR1L-VS-413 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Brk_Type =' | 1. IPC_VEHICLE_SETUP.Trail_Brk_Type = 1 (Heavy_Electric) is sent |
| 422 | NR1L-VS-413 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Brk_Type =' | 2. IPC_VEHICLE_SETUP.Trail_Brk_Type = 0 (Light_Electric) is sent |
| 425 | NR1L-VS-416 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Name =' | IPC_VEHICLE_SETUP.Trail_Name = one of [0 (Trailer), 1 (Boat), 2 (Car), 3 (Cargo) |
| 425 | NR1L-VS-416 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Name = 1 (Boat) |
| 425 | NR1L-VS-416 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Name =' | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Name = 1 (Boat) |
| 425 | NR1L-VS-416 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Name = 0 (Trailer) |
| 425 | NR1L-VS-416 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Name =' | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Name = 0 (Trailer) |
| 425 | NR1L-VS-416 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Name =' | 1. IPC_VEHICLE_SETUP.Trail_Name = 1 (Boat) is sent |
| 425 | NR1L-VS-416 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Name =' | 2. IPC_VEHICLE_SETUP.Trail_Name = 0 (Trailer) is sent |
| 428 | NR1L-VS-419 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. Set the "Trailer Number" customer setting to One and check that TELEMATIC_VEH |
| 428 | NR1L-VS-419 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trail_Num_Req = 0 (One) is sent |
| 429 | NR1L-VS-420 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. Set the "Trailer Number" customer setting to Two and check that TELEMATIC_VEH |
| 429 | NR1L-VS-420 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trail_Num_Req = 1 (Two) is sent |
| 430 | NR1L-VS-421 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. Set the "Trailer Number" customer setting to Three and check that TELEMATIC_V |
| 430 | NR1L-VS-421 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trail_Num_Req = 2 (Three) is sent |
| 431 | NR1L-VS-422 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. Set the "Trailer Number" customer setting to Four and check that TELEMATIC_VE |
| 431 | NR1L-VS-422 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_VEHICLE_SETUP.Trail_Num_Req =' | 2. TELEMATIC_VEHICLE_SETUP.Trail_Num_Req = 3 (Four) is sent |
| 432 | NR1L-VS-423 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Num =' | IPC_VEHICLE_SETUP.Trail_Num = one of [0 (One), 1 (Two), 2 (Three), 3 (Four)] |
| 432 | NR1L-VS-423 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Num = 1 (Two) |
| 432 | NR1L-VS-423 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Num =' | 1. Send CAN: IPC_VEHICLE_SETUP.Trail_Num = 1 (Two) |
| 432 | NR1L-VS-423 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Num = 0 (One) |
| 432 | NR1L-VS-423 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Num =' | 2. Send CAN: IPC_VEHICLE_SETUP.Trail_Num = 0 (One) |
| 432 | NR1L-VS-423 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Num =' | 1. IPC_VEHICLE_SETUP.Trail_Num = 1 (Two) is sent |
| 432 | NR1L-VS-423 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP.Trail_Num =' | 2. IPC_VEHICLE_SETUP.Trail_Num = 0 (One) is sent |
| 440 | NR1L-VS-431 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req =' | 2. Set the "Warnings for Low Fuel Inverter Shutdown - Visual Warning" customer s |
| 440 | NR1L-VS-431 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req =' | 2. TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req = 0 (OFF) is sent |
| 441 | NR1L-VS-432 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req =' | 2. Set the "Warnings for Low Fuel Inverter Shutdown - Visual Warning" customer s |
| 441 | NR1L-VS-432 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req =' | 2. TELEMATIC_FD_5.WorksiteINVM_Visual_LFW_Req = 1 (ON) is sent |
| 442 | NR1L-VS-433 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW =' | IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = one of [0 (OFF), 1 (ON)] |
| 442 | NR1L-VS-433 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 1 (ON) |
| 442 | NR1L-VS-433 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW =' | 1. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 1 (ON) |
| 442 | NR1L-VS-433 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 0 (OFF) |
| 442 | NR1L-VS-433 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW =' | 2. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 0 (OFF) |
| 442 | NR1L-VS-433 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW =' | 1. IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 1 (ON) is sent |
| 442 | NR1L-VS-433 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW =' | 2. IPC_VEHICLE_SETUP2.WorksiteINVM_Visual_LFW = 0 (OFF) is sent |
| 445 | NR1L-VS-436 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req =' | 2. Set the "Warnings for Low Fuel Inverter Shutdown - Audible Warning" customer  |
| 445 | NR1L-VS-436 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req =' | 2. TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req = 0 (OFF) is sent |
| 446 | NR1L-VS-437 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req =' | 2. Set the "Warnings for Low Fuel Inverter Shutdown - Audible Warning" customer  |
| 446 | NR1L-VS-437 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req =' | 2. TELEMATIC_FD_5.WorksiteINVM_Audible_LFW_Req = 1 (ON) is sent |
| 447 | NR1L-VS-438 | input | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW =' | IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = one of [0 (OFF), 1 (ON)] |
| 447 | NR1L-VS-438 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 1. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 1 (ON) |
| 447 | NR1L-VS-438 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW =' | 1. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 1 (ON) |
| 447 | NR1L-VS-438 | proc | `Send CAN:` 為 R-1 v2 舊式，v3 改 `Send the signal $MSG.Sig$ = …` | 2. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 0 (OFF) |
| 447 | NR1L-VS-438 | proc | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW =' | 2. Send CAN: IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 0 (OFF) |
| 447 | NR1L-VS-438 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW =' | 1. IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 1 (ON) is sent |
| 447 | NR1L-VS-438 | er | 訊號賦值未以 `$` 包覆全名（R-1 v3(a)）：'IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW =' | 2. IPC_VEHICLE_SETUP2.WorksiteINVM_Audible_LFW = 0 (OFF) is sent |

### T — PENDING 說明非英文（行計 25／列計 25）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 81 | NR1L-VS-072 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 82 | NR1L-VS-073 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 83 | NR1L-VS-074 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 140 | NR1L-VS-131 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 154 | NR1L-VS-145 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 155 | NR1L-VS-146 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 162 | NR1L-VS-153 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 163 | NR1L-VS-154 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 164 | NR1L-VS-155 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 167 | NR1L-VS-158 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 168 | NR1L-VS-159 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 169 | NR1L-VS-160 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 170 | NR1L-VS-161 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 180 | NR1L-VS-171 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 181 | NR1L-VS-172 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 182 | NR1L-VS-173 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 183 | NR1L-VS-174 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 184 | NR1L-VS-175 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 185 | NR1L-VS-176 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 186 | NR1L-VS-177 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 187 | NR1L-VS-178 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 330 | NR1L-VS-321 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 355 | NR1L-VS-346 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 356 | NR1L-VS-347 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 357 | NR1L-VS-348 | pre | PENDING 說明含非 ASCII 字元 ['（', '未', '取'] | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 25／列計 25）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 81 | NR1L-VS-072 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 82 | NR1L-VS-073 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 83 | NR1L-VS-074 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 140 | NR1L-VS-131 | pre | PENDING 佔位（DR） | 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 154 | NR1L-VS-145 | pre | PENDING 佔位（DR） | 2. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 155 | NR1L-VS-146 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 162 | NR1L-VS-153 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 163 | NR1L-VS-154 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 164 | NR1L-VS-155 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 167 | NR1L-VS-158 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 168 | NR1L-VS-159 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 169 | NR1L-VS-160 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 170 | NR1L-VS-161 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 180 | NR1L-VS-171 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 181 | NR1L-VS-172 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 182 | NR1L-VS-173 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 183 | NR1L-VS-174 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 184 | NR1L-VS-175 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 185 | NR1L-VS-176 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 186 | NR1L-VS-177 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 187 | NR1L-VS-178 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 330 | NR1L-VS-321 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 355 | NR1L-VS-346 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 356 | NR1L-VS-347 | pre | PENDING 佔位（DR） | 4. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |
| 357 | NR1L-VS-348 | pre | PENDING 佔位（DR） | 3. PENDING: DR（未取號，依審閱 §2.2：未送出前不佔號） |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 278／列計 278）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 13 | NR1L-VS-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-VS-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-VS-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-VS-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-VS-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-VS-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-VS-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-VS-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-VS-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-VS-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-VS-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-VS-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-VS-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-VS-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-VS-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-VS-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-VS-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-VS-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-VS-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-VS-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | NR1L-VS-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 42 | NR1L-VS-033 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 43 | NR1L-VS-034 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | NR1L-VS-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | NR1L-VS-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | NR1L-VS-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | NR1L-VS-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 56 | NR1L-VS-047 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | NR1L-VS-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | NR1L-VS-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | NR1L-VS-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 60 | NR1L-VS-051 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 61 | NR1L-VS-052 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | NR1L-VS-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | NR1L-VS-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 70 | NR1L-VS-061 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 71 | NR1L-VS-062 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | NR1L-VS-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | NR1L-VS-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | NR1L-VS-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | NR1L-VS-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | NR1L-VS-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | NR1L-VS-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | NR1L-VS-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | NR1L-VS-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 94 | NR1L-VS-085 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | NR1L-VS-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 101 | NR1L-VS-092 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | NR1L-VS-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 103 | NR1L-VS-094 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | NR1L-VS-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | NR1L-VS-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | NR1L-VS-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | NR1L-VS-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | NR1L-VS-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 117 | NR1L-VS-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | NR1L-VS-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | NR1L-VS-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | NR1L-VS-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | NR1L-VS-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | NR1L-VS-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | NR1L-VS-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | NR1L-VS-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | NR1L-VS-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | NR1L-VS-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 127 | NR1L-VS-118 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | NR1L-VS-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 134 | NR1L-VS-125 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 139 | NR1L-VS-130 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | NR1L-VS-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 147 | NR1L-VS-138 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 150 | NR1L-VS-141 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 153 | NR1L-VS-144 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 154 | NR1L-VS-145 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 155 | NR1L-VS-146 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 159 | NR1L-VS-150 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 160 | NR1L-VS-151 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 161 | NR1L-VS-152 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 162 | NR1L-VS-153 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 163 | NR1L-VS-154 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 164 | NR1L-VS-155 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 165 | NR1L-VS-156 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 166 | NR1L-VS-157 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 167 | NR1L-VS-158 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 168 | NR1L-VS-159 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 169 | NR1L-VS-160 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 170 | NR1L-VS-161 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 175 | NR1L-VS-166 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 178 | NR1L-VS-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 179 | NR1L-VS-170 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 180 | NR1L-VS-171 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 181 | NR1L-VS-172 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 182 | NR1L-VS-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 183 | NR1L-VS-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 184 | NR1L-VS-175 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 185 | NR1L-VS-176 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 186 | NR1L-VS-177 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 187 | NR1L-VS-178 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 188 | NR1L-VS-179 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 189 | NR1L-VS-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 190 | NR1L-VS-181 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 191 | NR1L-VS-182 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 192 | NR1L-VS-183 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 193 | NR1L-VS-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 194 | NR1L-VS-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 195 | NR1L-VS-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 196 | NR1L-VS-187 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 197 | NR1L-VS-188 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 198 | NR1L-VS-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 199 | NR1L-VS-190 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 200 | NR1L-VS-191 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 201 | NR1L-VS-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 202 | NR1L-VS-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 203 | NR1L-VS-194 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 204 | NR1L-VS-195 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 205 | NR1L-VS-196 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 206 | NR1L-VS-197 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 207 | NR1L-VS-198 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 208 | NR1L-VS-199 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 209 | NR1L-VS-200 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 210 | NR1L-VS-201 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 211 | NR1L-VS-202 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 212 | NR1L-VS-203 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 213 | NR1L-VS-204 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 214 | NR1L-VS-205 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 215 | NR1L-VS-206 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 221 | NR1L-VS-212 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 222 | NR1L-VS-213 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 223 | NR1L-VS-214 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 224 | NR1L-VS-215 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 225 | NR1L-VS-216 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 226 | NR1L-VS-217 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 227 | NR1L-VS-218 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 232 | NR1L-VS-223 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 233 | NR1L-VS-224 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 234 | NR1L-VS-225 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 235 | NR1L-VS-226 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 236 | NR1L-VS-227 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 237 | NR1L-VS-228 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 238 | NR1L-VS-229 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 239 | NR1L-VS-230 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 240 | NR1L-VS-231 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 245 | NR1L-VS-236 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 250 | NR1L-VS-241 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 255 | NR1L-VS-246 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 256 | NR1L-VS-247 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 257 | NR1L-VS-248 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 258 | NR1L-VS-249 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 263 | NR1L-VS-254 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 268 | NR1L-VS-259 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 273 | NR1L-VS-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 274 | NR1L-VS-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 275 | NR1L-VS-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 276 | NR1L-VS-267 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 277 | NR1L-VS-268 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 278 | NR1L-VS-269 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 279 | NR1L-VS-270 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 280 | NR1L-VS-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 281 | NR1L-VS-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 282 | NR1L-VS-273 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 283 | NR1L-VS-274 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 284 | NR1L-VS-275 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 285 | NR1L-VS-276 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 286 | NR1L-VS-277 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 287 | NR1L-VS-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 288 | NR1L-VS-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 289 | NR1L-VS-280 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 290 | NR1L-VS-281 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 291 | NR1L-VS-282 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 292 | NR1L-VS-283 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 293 | NR1L-VS-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 294 | NR1L-VS-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 295 | NR1L-VS-286 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 296 | NR1L-VS-287 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 297 | NR1L-VS-288 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 298 | NR1L-VS-289 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 299 | NR1L-VS-290 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 300 | NR1L-VS-291 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 301 | NR1L-VS-292 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 302 | NR1L-VS-293 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 303 | NR1L-VS-294 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 304 | NR1L-VS-295 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 305 | NR1L-VS-296 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 306 | NR1L-VS-297 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 307 | NR1L-VS-298 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 308 | NR1L-VS-299 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 309 | NR1L-VS-300 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 310 | NR1L-VS-301 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 311 | NR1L-VS-302 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 312 | NR1L-VS-303 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 313 | NR1L-VS-304 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 314 | NR1L-VS-305 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 315 | NR1L-VS-306 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 316 | NR1L-VS-307 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 317 | NR1L-VS-308 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 318 | NR1L-VS-309 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 319 | NR1L-VS-310 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 320 | NR1L-VS-311 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 321 | NR1L-VS-312 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 322 | NR1L-VS-313 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 323 | NR1L-VS-314 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 324 | NR1L-VS-315 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 325 | NR1L-VS-316 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 326 | NR1L-VS-317 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 327 | NR1L-VS-318 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 328 | NR1L-VS-319 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 329 | NR1L-VS-320 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 330 | NR1L-VS-321 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 332 | NR1L-VS-323 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 333 | NR1L-VS-324 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 334 | NR1L-VS-325 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 335 | NR1L-VS-326 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 336 | NR1L-VS-327 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 337 | NR1L-VS-328 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 338 | NR1L-VS-329 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 339 | NR1L-VS-330 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 340 | NR1L-VS-331 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 341 | NR1L-VS-332 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 342 | NR1L-VS-333 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 347 | NR1L-VS-338 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 352 | NR1L-VS-343 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 353 | NR1L-VS-344 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 354 | NR1L-VS-345 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 355 | NR1L-VS-346 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 356 | NR1L-VS-347 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 357 | NR1L-VS-348 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 362 | NR1L-VS-353 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 369 | NR1L-VS-360 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 377 | NR1L-VS-368 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 382 | NR1L-VS-373 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 383 | NR1L-VS-374 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 384 | NR1L-VS-375 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 385 | NR1L-VS-376 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 386 | NR1L-VS-377 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 387 | NR1L-VS-378 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 388 | NR1L-VS-379 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 389 | NR1L-VS-380 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 390 | NR1L-VS-381 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 391 | NR1L-VS-382 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 392 | NR1L-VS-383 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 393 | NR1L-VS-384 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 394 | NR1L-VS-385 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 395 | NR1L-VS-386 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 396 | NR1L-VS-387 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 397 | NR1L-VS-388 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 398 | NR1L-VS-389 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 399 | NR1L-VS-390 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 400 | NR1L-VS-391 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 401 | NR1L-VS-392 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 402 | NR1L-VS-393 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 403 | NR1L-VS-394 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 404 | NR1L-VS-395 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 405 | NR1L-VS-396 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 406 | NR1L-VS-397 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 407 | NR1L-VS-398 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 408 | NR1L-VS-399 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 409 | NR1L-VS-400 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 410 | NR1L-VS-401 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 411 | NR1L-VS-402 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 412 | NR1L-VS-403 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 413 | NR1L-VS-404 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 414 | NR1L-VS-405 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 415 | NR1L-VS-406 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 416 | NR1L-VS-407 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 417 | NR1L-VS-408 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 418 | NR1L-VS-409 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 419 | NR1L-VS-410 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 422 | NR1L-VS-413 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 423 | NR1L-VS-414 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 424 | NR1L-VS-415 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 425 | NR1L-VS-416 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 432 | NR1L-VS-423 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 433 | NR1L-VS-424 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 434 | NR1L-VS-425 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 435 | NR1L-VS-426 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 436 | NR1L-VS-427 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 442 | NR1L-VS-433 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 447 | NR1L-VS-438 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 361／列計 198）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VS-001 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 10 | NR1L-VS-001 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "4 AUX Switches" customer s |
| 11 | NR1L-VS-002 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 11 | NR1L-VS-002 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "6 Aux Switches" customer s |
| 12 | NR1L-VS-003 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 12 | NR1L-VS-003 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "6 Aux Switches" customer s |
| 15 | NR1L-VS-006 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 15 | NR1L-VS-006 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto Fold Mirrors" custome |
| 16 | NR1L-VS-007 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 16 | NR1L-VS-007 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto Fold Mirrors" custome |
| 17 | NR1L-VS-008 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 17 | NR1L-VS-008 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto Fold Mirrors" setting |
| 18 | NR1L-VS-009 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 18 | NR1L-VS-009 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto Fold Mirrors" setting |
| 19 | NR1L-VS-010 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto Fold Mirrors" setting |
| 20 | NR1L-VS-011 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 20 | NR1L-VS-011 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto High Beam" customer s |
| 21 | NR1L-VS-012 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 21 | NR1L-VS-012 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto High Beam" customer s |
| 22 | NR1L-VS-013 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 22 | NR1L-VS-013 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto High Beam" setting is |
| 23 | NR1L-VS-014 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 23 | NR1L-VS-014 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto High Beam" setting is |
| 24 | NR1L-VS-015 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Auto High Beam" setting is |
| 45 | NR1L-VS-036 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 45 | NR1L-VS-036 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Automatic Trailer Light Ch |
| 46 | NR1L-VS-037 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 46 | NR1L-VS-037 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Automatic Trailer Light Ch |
| 47 | NR1L-VS-038 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 47 | NR1L-VS-038 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Automatic Trailer Light Ch |
| 48 | NR1L-VS-039 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 48 | NR1L-VS-039 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Automatic Trailer Light Ch |
| 49 | NR1L-VS-040 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Automatic Trailer Light Ch |
| 50 | NR1L-VS-041 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 50 | NR1L-VS-041 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Blind Spot with Trailer De |
| 51 | NR1L-VS-042 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 51 | NR1L-VS-042 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Blind Spot with Trailer De |
| 52 | NR1L-VS-043 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 52 | NR1L-VS-043 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Blind Spot with Trailer De |
| 53 | NR1L-VS-044 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 53 | NR1L-VS-044 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Blind Spot with Trailer De |
| 54 | NR1L-VS-045 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Blind Spot with Trailer De |
| 63 | NR1L-VS-054 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 63 | NR1L-VS-054 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 64 | NR1L-VS-055 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 64 | NR1L-VS-055 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 65 | NR1L-VS-056 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 65 | NR1L-VS-056 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 66 | NR1L-VS-057 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 66 | NR1L-VS-057 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 67 | NR1L-VS-058 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 67 | NR1L-VS-058 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 68 | NR1L-VS-059 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Charge Power Level" settin |
| 69 | NR1L-VS-060 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 69 | NR1L-VS-060 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the Vehicle Settings menu and check that the "Consumption Unit" customer |
| 78 | NR1L-VS-069 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 78 | NR1L-VS-069 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the Vehicle Settings menu and check that the "Distance Unit" customer se |
| 79 | NR1L-VS-070 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 79 | NR1L-VS-070 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Driver Easy Exit Seat" cus |
| 80 | NR1L-VS-071 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 80 | NR1L-VS-071 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Driver Easy Exit Seat" cus |
| 81 | NR1L-VS-072 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 81 | NR1L-VS-072 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Driver Easy Exit Seat" set |
| 82 | NR1L-VS-073 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 82 | NR1L-VS-073 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Driver Easy Exit Seat" set |
| 83 | NR1L-VS-074 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Driver Easy Exit Seat" set |
| 84 | NR1L-VS-075 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 84 | NR1L-VS-075 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "E-Save" customer setting i |
| 85 | NR1L-VS-076 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 85 | NR1L-VS-076 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "E-Save" customer setting i |
| 86 | NR1L-VS-077 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 86 | NR1L-VS-077 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Engine Off Power Delay" se |
| 87 | NR1L-VS-078 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 87 | NR1L-VS-078 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Engine Off Power Delay" se |
| 88 | NR1L-VS-079 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 88 | NR1L-VS-079 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Engine Off Power Delay" se |
| 89 | NR1L-VS-080 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Engine Off Power Delay" se |
| 90 | NR1L-VS-081 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 90 | NR1L-VS-081 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 91 | NR1L-VS-082 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 91 | NR1L-VS-082 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 92 | NR1L-VS-083 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 92 | NR1L-VS-083 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 93 | NR1L-VS-084 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 93 | NR1L-VS-084 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 94 | NR1L-VS-085 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 95 | NR1L-VS-086 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 95 | NR1L-VS-086 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Enhanced Display Synchroni |
| 96 | NR1L-VS-087 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 96 | NR1L-VS-087 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Flash Light With Lock" cus |
| 97 | NR1L-VS-088 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 97 | NR1L-VS-088 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Flash Light With Lock" cus |
| 98 | NR1L-VS-089 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 98 | NR1L-VS-089 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Flash Light With Lock" set |
| 99 | NR1L-VS-090 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 99 | NR1L-VS-090 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Flash Light With Lock" set |
| 100 | NR1L-VS-091 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Flash Light With Lock" set |
| 104 | NR1L-VS-095 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 104 | NR1L-VS-095 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Forward Collision Warning  |
| 105 | NR1L-VS-096 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 105 | NR1L-VS-096 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Forward Collision Warning  |
| 106 | NR1L-VS-097 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Forward Collision Warning  |
| 110 | NR1L-VS-101 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 110 | NR1L-VS-101 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" cust |
| 111 | NR1L-VS-102 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 111 | NR1L-VS-102 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" cust |
| 112 | NR1L-VS-103 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 112 | NR1L-VS-103 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 113 | NR1L-VS-104 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 113 | NR1L-VS-104 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 114 | NR1L-VS-105 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 114 | NR1L-VS-105 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 115 | NR1L-VS-106 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 115 | NR1L-VS-106 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 116 | NR1L-VS-107 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 117 | NR1L-VS-108 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 118 | NR1L-VS-109 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Headlights Off Delay" sett |
| 129 | NR1L-VS-120 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 129 | NR1L-VS-120 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" customer s |
| 130 | NR1L-VS-121 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 130 | NR1L-VS-121 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" customer s |
| 131 | NR1L-VS-122 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 131 | NR1L-VS-122 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" setting is |
| 132 | NR1L-VS-123 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 132 | NR1L-VS-123 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" setting is |
| 133 | NR1L-VS-124 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 133 | NR1L-VS-124 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" setting is |
| 134 | NR1L-VS-125 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Lock" setting is |
| 135 | NR1L-VS-126 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 135 | NR1L-VS-126 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Remote Start" cu |
| 136 | NR1L-VS-127 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 136 | NR1L-VS-127 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Remote Start" cu |
| 137 | NR1L-VS-128 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 137 | NR1L-VS-128 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Remote Start" se |
| 138 | NR1L-VS-129 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 138 | NR1L-VS-129 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Remote Start" se |
| 139 | NR1L-VS-130 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Horn With Remote Start" se |
| 141 | NR1L-VS-132 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 141 | NR1L-VS-132 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" cust |
| 142 | NR1L-VS-133 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 142 | NR1L-VS-133 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" cust |
| 143 | NR1L-VS-134 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 143 | NR1L-VS-134 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" sett |
| 144 | NR1L-VS-135 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 144 | NR1L-VS-135 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" sett |
| 145 | NR1L-VS-136 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 145 | NR1L-VS-136 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" sett |
| 146 | NR1L-VS-137 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 146 | NR1L-VS-137 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" sett |
| 147 | NR1L-VS-138 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Illuminated Approach" sett |
| 148 | NR1L-VS-139 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 148 | NR1L-VS-139 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Strength" custo |
| 149 | NR1L-VS-140 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 149 | NR1L-VS-140 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Strength" custo |
| 150 | NR1L-VS-141 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Strength" setti |
| 151 | NR1L-VS-142 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 151 | NR1L-VS-142 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Warning" custom |
| 152 | NR1L-VS-143 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 152 | NR1L-VS-143 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Warning" custom |
| 153 | NR1L-VS-144 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Lane Sense Warning" settin |
| 156 | NR1L-VS-147 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 156 | NR1L-VS-147 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Max Power Level" customer  |
| 157 | NR1L-VS-148 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 157 | NR1L-VS-148 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Max Power Level" setting i |
| 158 | NR1L-VS-149 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 158 | NR1L-VS-149 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Max Power Level" setting i |
| 159 | NR1L-VS-150 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Max Power Level" setting i |
| 171 | NR1L-VS-162 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 171 | NR1L-VS-162 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Paddle Shifter" customer s |
| 172 | NR1L-VS-163 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 172 | NR1L-VS-163 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Paddle Shifter" customer s |
| 173 | NR1L-VS-164 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 173 | NR1L-VS-164 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Paddle Shifter" setting is |
| 174 | NR1L-VS-165 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 174 | NR1L-VS-165 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Paddle Shifter" setting is |
| 175 | NR1L-VS-166 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Paddle Shifter" setting is |
| 176 | NR1L-VS-167 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 176 | NR1L-VS-167 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Park Sense" customer setti |
| 177 | NR1L-VS-168 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 177 | NR1L-VS-168 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Park Sense" customer setti |
| 216 | NR1L-VS-207 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 216 | NR1L-VS-207 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" customer setti |
| 217 | NR1L-VS-208 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 217 | NR1L-VS-208 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" customer setti |
| 218 | NR1L-VS-209 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 218 | NR1L-VS-209 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" setting is dis |
| 219 | NR1L-VS-210 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 219 | NR1L-VS-210 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" setting is dis |
| 220 | NR1L-VS-211 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 220 | NR1L-VS-211 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" setting is dis |
| 221 | NR1L-VS-212 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Power Unit" setting is dis |
| 228 | NR1L-VS-219 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 228 | NR1L-VS-219 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "RKE Linked to Memory" cust |
| 229 | NR1L-VS-220 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 229 | NR1L-VS-220 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "RKE Linked to Memory" cust |
| 230 | NR1L-VS-221 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 230 | NR1L-VS-221 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the RKE Linked to Memory settin |
| 231 | NR1L-VS-222 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 231 | NR1L-VS-222 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the RKE Linked to Memory settin |
| 232 | NR1L-VS-223 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the RKE Linked to Memory settin |
| 241 | NR1L-VS-232 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 241 | NR1L-VS-232 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Light Status |
| 242 | NR1L-VS-233 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 242 | NR1L-VS-233 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Light Status |
| 243 | NR1L-VS-234 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 243 | NR1L-VS-234 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Light Status |
| 244 | NR1L-VS-235 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 244 | NR1L-VS-235 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Light Status |
| 245 | NR1L-VS-236 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Light Status |
| 246 | NR1L-VS-237 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 246 | NR1L-VS-237 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lighting wit |
| 247 | NR1L-VS-238 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 247 | NR1L-VS-238 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lighting wit |
| 248 | NR1L-VS-239 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 248 | NR1L-VS-239 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lighting wit |
| 249 | NR1L-VS-240 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 249 | NR1L-VS-240 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lighting wit |
| 250 | NR1L-VS-241 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lighting wit |
| 251 | NR1L-VS-242 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 251 | NR1L-VS-242 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lights with  |
| 252 | NR1L-VS-243 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 252 | NR1L-VS-243 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lights with  |
| 253 | NR1L-VS-244 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 253 | NR1L-VS-244 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lights with  |
| 254 | NR1L-VS-245 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 254 | NR1L-VS-245 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lights with  |
| 255 | NR1L-VS-246 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rear Guidance Lights with  |
| 259 | NR1L-VS-250 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 259 | NR1L-VS-250 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Delay" cus |
| 260 | NR1L-VS-251 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 260 | NR1L-VS-251 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Delay" cus |
| 261 | NR1L-VS-252 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 261 | NR1L-VS-252 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Delay" set |
| 262 | NR1L-VS-253 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 262 | NR1L-VS-253 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Delay" set |
| 263 | NR1L-VS-254 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Delay" set |
| 264 | NR1L-VS-255 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 264 | NR1L-VS-255 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Dynamic Gu |
| 265 | NR1L-VS-256 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 265 | NR1L-VS-256 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Dynamic Gu |
| 266 | NR1L-VS-257 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 266 | NR1L-VS-257 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Dynamic Gu |
| 267 | NR1L-VS-258 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 267 | NR1L-VS-258 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Dynamic Gu |
| 268 | NR1L-VS-259 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Rearview Camera Dynamic Gu |
| 269 | NR1L-VS-260 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 269 | NR1L-VS-260 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Remote Door Unlock" custom |
| 270 | NR1L-VS-261 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 270 | NR1L-VS-261 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Remote Door Unlock" custom |
| 271 | NR1L-VS-262 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 271 | NR1L-VS-262 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Remote Door Unlock" settin |
| 272 | NR1L-VS-263 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 272 | NR1L-VS-263 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Remote Door Unlock" settin |
| 273 | NR1L-VS-264 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Remote Door Unlock" settin |
| 331 | NR1L-VS-322 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 331 | NR1L-VS-322 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the Vehicle Settings menu and check that the "Speed Unit" customer setti |
| 343 | NR1L-VS-334 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 343 | NR1L-VS-334 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Display Message |
| 344 | NR1L-VS-335 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 344 | NR1L-VS-335 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Display Message |
| 345 | NR1L-VS-336 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 345 | NR1L-VS-336 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Display Message |
| 346 | NR1L-VS-337 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 346 | NR1L-VS-337 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Display Message |
| 347 | NR1L-VS-338 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Display Message |
| 348 | NR1L-VS-339 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 348 | NR1L-VS-339 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Flash Lights Wi |
| 349 | NR1L-VS-340 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 349 | NR1L-VS-340 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Flash Lights Wi |
| 350 | NR1L-VS-341 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 350 | NR1L-VS-341 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Flash Lights Wi |
| 351 | NR1L-VS-342 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 351 | NR1L-VS-342 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Flash Lights Wi |
| 352 | NR1L-VS-343 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Flash Lights Wi |
| 358 | NR1L-VS-349 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 358 | NR1L-VS-349 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Sound Horn With |
| 359 | NR1L-VS-350 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 359 | NR1L-VS-350 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Sound Horn With |
| 360 | NR1L-VS-351 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 360 | NR1L-VS-351 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Sound Horn With |
| 361 | NR1L-VS-352 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 361 | NR1L-VS-352 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Sound Horn With |
| 362 | NR1L-VS-353 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Suspension Sound Horn With |
| 363 | NR1L-VS-354 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 363 | NR1L-VS-354 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Temperature Unit" customer |
| 364 | NR1L-VS-355 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 364 | NR1L-VS-355 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Temperature Unit" customer |
| 365 | NR1L-VS-356 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 365 | NR1L-VS-356 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tilt Mirror in Reverse" cu |
| 366 | NR1L-VS-357 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 366 | NR1L-VS-357 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tilt Mirror in Reverse" cu |
| 367 | NR1L-VS-358 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 367 | NR1L-VS-358 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Tilt Mirror in Reverse sett |
| 368 | NR1L-VS-359 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 368 | NR1L-VS-359 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Tilt Mirror in Reverse sett |
| 369 | NR1L-VS-360 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Tilt Mirror in Reverse sett |
| 370 | NR1L-VS-361 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 370 | NR1L-VS-361 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the Vehicle Settings menu and check that the "Time and Date Settings" cu |
| 370 | NR1L-VS-361 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Select the "Time and Date Settings" customer setting and check that its optio |
| 370 | NR1L-VS-361 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 4. Select an option other than the current one and check that the "Time and Date |
| 371 | NR1L-VS-362 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 371 | NR1L-VS-362 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Time and Date Settings" cu |
| 372 | NR1L-VS-363 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 372 | NR1L-VS-363 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Time and Date Settings" cu |
| 372 | NR1L-VS-363 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 4. Select the "Time and Date Settings" customer setting and check that its value |
| 373 | NR1L-VS-364 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 373 | NR1L-VS-364 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tire Fill Alert" customer  |
| 374 | NR1L-VS-365 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 374 | NR1L-VS-365 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tire Fill Alert" customer  |
| 375 | NR1L-VS-366 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 375 | NR1L-VS-366 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tire Fill Alert" setting i |
| 376 | NR1L-VS-367 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 376 | NR1L-VS-367 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tire Fill Alert" setting i |
| 377 | NR1L-VS-368 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Tire Fill Alert" setting i |
| 378 | NR1L-VS-369 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 378 | NR1L-VS-369 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Torque Unit" customer sett |
| 379 | NR1L-VS-370 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 379 | NR1L-VS-370 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Torque Unit" customer sett |
| 380 | NR1L-VS-371 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 380 | NR1L-VS-371 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Torque Unit" setting is di |
| 381 | NR1L-VS-372 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 381 | NR1L-VS-372 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Torque Unit" setting is di |
| 382 | NR1L-VS-373 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Torque Unit" setting is di |
| 420 | NR1L-VS-411 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 420 | NR1L-VS-411 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Brake Type" custom |
| 421 | NR1L-VS-412 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 421 | NR1L-VS-412 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Brake Type" custom |
| 422 | NR1L-VS-413 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Brake Type" settin |
| 426 | NR1L-VS-417 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 426 | NR1L-VS-417 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" customer s |
| 427 | NR1L-VS-418 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 427 | NR1L-VS-418 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" customer s |
| 428 | NR1L-VS-419 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 428 | NR1L-VS-419 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" setting is |
| 429 | NR1L-VS-420 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 429 | NR1L-VS-420 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" setting is |
| 430 | NR1L-VS-421 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 430 | NR1L-VS-421 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" setting is |
| 431 | NR1L-VS-422 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 431 | NR1L-VS-422 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" setting is |
| 432 | NR1L-VS-423 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Trailer Number" setting is |
| 437 | NR1L-VS-428 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 437 | NR1L-VS-428 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Unit Energy" customer sett |
| 438 | NR1L-VS-429 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 438 | NR1L-VS-429 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Warnings for Low Fuel Inve |
| 439 | NR1L-VS-430 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 439 | NR1L-VS-430 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Warnings for Low Fuel Inve |
| 440 | NR1L-VS-431 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 440 | NR1L-VS-431 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |
| 441 | NR1L-VS-432 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 441 | NR1L-VS-432 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |
| 442 | NR1L-VS-433 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |
| 443 | NR1L-VS-434 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 443 | NR1L-VS-434 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Warnings for Low Fuel Inve |
| 444 | NR1L-VS-435 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Open the Vehicle Settings menu and wait until it is fully rendered |
| 444 | NR1L-VS-435 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the "Warnings for Low Fuel Inve |
| 445 | NR1L-VS-436 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 445 | NR1L-VS-436 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |
| 446 | NR1L-VS-437 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Open the Vehicle Settings menu and wait until it is fully rendered |
| 446 | NR1L-VS-437 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |
| 447 | NR1L-VS-438 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 3. Read the Vehicle Settings menu and check that the Warnings for Low Fuel Inver |

