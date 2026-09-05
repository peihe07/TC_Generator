# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleSetupManagementR1Low_20260902_Revise1.xlsx

- 來源：`features/vsm_v42/delivered/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleSetupManagementR1Low_20260902_Revise1.xlsx`（唯讀）
- 資料列數：17
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`vsm_v42`（P 採 R-1 v3；另跑 Q／R／T）

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
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 47 | 15 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 6 | 3 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 17 | 17 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 0 | 0 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 6 | 3 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |

**總計：行計 76**（列計不加總——同一列可觸發多項檢查）

## 明細

### P — 訊號寫法不合 R-1 v2（行計 47／列計 15）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-VSM42-003 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 13 | NR1L-VSM42-004 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 0 (Off) |
| 13 | NR1L-VSM42-004 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. Read the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and check that it is |
| 13 | NR1L-VSM42-004 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered wi |
| 14 | NR1L-VSM42-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 14 | NR1L-VSM42-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2 |
| 14 | NR1L-VSM42-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2 is registered withou |
| 15 | NR1L-VSM42-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 15 | NR1L-VSM42-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 3 |
| 15 | NR1L-VSM42-006 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 3 is registered withou |
| 16 | NR1L-VSM42-007 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 16 | NR1L-VSM42-007 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 4 |
| 16 | NR1L-VSM42-007 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 4 is registered withou |
| 17 | NR1L-VSM42-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 17 | NR1L-VSM42-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 5 |
| 17 | NR1L-VSM42-008 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 5 is registered withou |
| 18 | NR1L-VSM42-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 18 | NR1L-VSM42-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 6 |
| 18 | NR1L-VSM42-009 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 6 is registered withou |
| 19 | NR1L-VSM42-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$' | 1. Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB |
| 19 | NR1L-VSM42-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 2. Suppress transmission of $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and $IPC_VE |
| 19 | NR1L-VSM42-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Suppress transmission of $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and $IPC_VE |
| 19 | NR1L-VSM42-010 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 2. No value of $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ or $IPC_VEHICLE_SETUP2.E |
| 19 | NR1L-VSM42-010 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. No value of $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ or $IPC_VEHICLE_SETUP2.E |
| 20 | NR1L-VSM42-011 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On) |
| 20 | NR1L-VSM42-011 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 1. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 8 |
| 20 | NR1L-VSM42-011 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 1. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 8 is registered withou |
| 21 | NR1L-VSM42-012 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On) |
| 21 | NR1L-VSM42-012 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 9 |
| 21 | NR1L-VSM42-012 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 9 is registered withou |
| 22 | NR1L-VSM42-013 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On) |
| 22 | NR1L-VSM42-013 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10 |
| 22 | NR1L-VSM42-013 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 10 is registered witho |
| 23 | NR1L-VSM42-014 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On) |
| 23 | NR1L-VSM42-014 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 11 |
| 23 | NR1L-VSM42-014 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 11 is registered witho |
| 24 | NR1L-VSM42-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 2. Read the signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ and check that it is |
| 24 | NR1L-VSM42-015 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered wi |
| 25 | NR1L-VSM42-016 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 2. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On) |
| 25 | NR1L-VSM42-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64 |
| 25 | NR1L-VSM42-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 2. Read the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ and check that it is 64 |
| 25 | NR1L-VSM42-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 3. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 65 |
| 25 | NR1L-VSM42-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64 is registered without a bus |
| 25 | NR1L-VSM42-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 2. The signal value $STATUS_CCAN3.VehicleSpeedVSOSig$ = 64 is received |
| 25 | NR1L-VSM42-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_CCAN3.VehicleSpeedVSOSig$' | 3. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 65 is registered without a bus |
| 26 | NR1L-VSM42-017 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 1. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On) is registered wi |
| 26 | NR1L-VSM42-017 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$' | 3. The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 0 (Off) is registered w |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 6／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 24 | NR1L-VSM42-015 | proc | PENDING 佔位（DR-VL4） | 3. PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info |
| 24 | NR1L-VSM42-015 | er | PENDING 佔位（DR-VL4） | 3. PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info |
| 25 | NR1L-VSM42-016 | proc | PENDING 佔位（DR-VL4） | 5. PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info |
| 25 | NR1L-VSM42-016 | er | PENDING 佔位（DR-VL4） | 5. PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info |
| 26 | NR1L-VSM42-017 | proc | PENDING 佔位（DR-VL4） | 5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info |
| 26 | NR1L-VSM42-017 | er | PENDING 佔位（DR-VL4） | 5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 17／列計 17）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VSM42-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-VSM42-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-VSM42-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-VSM42-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-VSM42-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-VSM42-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-VSM42-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-VSM42-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-VSM42-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-VSM42-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-VSM42-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-VSM42-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-VSM42-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-VSM42-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-VSM42-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-VSM42-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-VSM42-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 6／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-VSM42-001 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Read the named UI element "Vehicle Settings" menu list and check that it does |
| 10 | NR1L-VSM42-001 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Attempt to select "EPB Maintenance Mode" in the "Vehicle Settings" menu list |
| 11 | NR1L-VSM42-002 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 1. Read the named UI element "Vehicle Settings" menu list and check that it cont |
| 11 | NR1L-VSM42-002 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Select "EPB Maintenance Mode" in the "Vehicle Settings" menu list |
| 26 | NR1L-VSM42-017 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 2. Read the named UI element "EPB Maintenance Mode" status text in the "Vehicle  |
| 26 | NR1L-VSM42-017 | proc | 導航標的 'Settings' 而同 TC 無固定入口 | 4. Read the named UI element "EPB Maintenance Mode" status text in the "Vehicle  |

