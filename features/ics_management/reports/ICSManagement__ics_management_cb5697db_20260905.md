# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_ICSManagement_20260830.xlsx

- 來源：`features/ics_management/delivered/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_ICSManagement_20260830.xlsx`（唯讀）
- 資料列數：31
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`ics_management`（P 採 R-1 v3；另跑 Q／R／T）

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
| P | 訊號寫法不合 R-1 v2 | 119 | 28 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 1 | 1 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 6 | 6 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 31 | 31 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 3 | 3 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 29 | 15 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |

**總計：行計 189**（列計不加總——同一列可觸發多項檢查）

## 明細

### P — 訊號寫法不合 R-1 v2（行計 119／列計 28）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-ICS-003 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_DIR$' | 1. Read the signal $CLIMATIC_PANEL.Radio_Knob1_DIR$ on the CAN trace and check t |
| 12 | NR1L-ICS-003 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_DIR$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob1_DIR$ on the CAN trace and check t |
| 12 | NR1L-ICS-003 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_VAL$' | 4. Read the signal $CLIMATIC_PANEL.Radio_Knob1_VAL$ in the same message and chec |
| 12 | NR1L-ICS-003 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_DIR$' | 1. The signal value $CLIMATIC_PANEL.Radio_Knob1_DIR$ = 0 (Knob_no_change) is obs |
| 12 | NR1L-ICS-003 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_DIR$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob1_DIR$ = 1 (Knob_increment) is obs |
| 12 | NR1L-ICS-003 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob1_VAL$' | 4. The signal value $CLIMATIC_PANEL.Radio_Knob1_VAL$ = 1 is observed in the same |
| 14 | NR1L-ICS-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 2. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 1 (Knob |
| 14 | NR1L-ICS-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ and check that it is 1 |
| 14 | NR1L-ICS-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ 2 seconds after the rotation |
| 14 | NR1L-ICS-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 5. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ 2 seconds after the rotation |
| 14 | NR1L-ICS-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 2. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 14 | NR1L-ICS-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 1 is received |
| 14 | NR1L-ICS-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 0 (Knob_no_change) is rec |
| 14 | NR1L-ICS-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 5. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 0 is received |
| 15 | NR1L-ICS-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 2. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 2 (Knob |
| 15 | NR1L-ICS-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ and check that it is 1 |
| 15 | NR1L-ICS-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ 2 seconds after the rotation |
| 15 | NR1L-ICS-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 5. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ 2 seconds after the rotation |
| 15 | NR1L-ICS-006 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 2. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 2 (Knob_decrement) is rec |
| 15 | NR1L-ICS-006 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 1 is received |
| 15 | NR1L-ICS-006 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 0 (Knob_no_change) is rec |
| 15 | NR1L-ICS-006 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 5. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 0 is received |
| 16 | NR1L-ICS-007 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 1. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 0 (Knob |
| 16 | NR1L-ICS-007 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ again and check that it is s |
| 16 | NR1L-ICS-007 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 1. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 0 (Knob_no_change) is rec |
| 16 | NR1L-ICS-007 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 0 (Knob_no_change) is rec |
| 17 | NR1L-ICS-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 1. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 0 (Knob |
| 17 | NR1L-ICS-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 2. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ and check that it is 0 |
| 17 | NR1L-ICS-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. Rotate the ICS knob 2 one detent position clock-wise and check that $CLIMATIC |
| 17 | NR1L-ICS-008 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 1. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 0 (Knob_no_change) is rec |
| 17 | NR1L-ICS-008 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 2. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 0 is received |
| 17 | NR1L-ICS-008 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 18 | NR1L-ICS-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 1. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ and check that it is 0 |
| 18 | NR1L-ICS-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_VAL$ and check that it is 3 |
| 18 | NR1L-ICS-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 1 (Knob |
| 18 | NR1L-ICS-009 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 1. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 0 is received |
| 18 | NR1L-ICS-009 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_VAL$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_VAL$ = 3 is received |
| 18 | NR1L-ICS-009 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 4. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 19 | NR1L-ICS-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 1 (Knob |
| 19 | NR1L-ICS-010 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 20 | NR1L-ICS-011 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 1 (Knob |
| 20 | NR1L-ICS-011 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 21 | NR1L-ICS-012 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. Read the signal $CLIMATIC_PANEL.Radio_Knob2_DIR$ and check that it is 1 (Knob |
| 21 | NR1L-ICS-012 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_Knob2_DIR$' | 3. The signal value $CLIMATIC_PANEL.Radio_Knob2_DIR$ = 1 (Knob_increment) is rec |
| 22 | NR1L-ICS-013 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn4$ on the CAN trace and check that i |
| 22 | NR1L-ICS-013 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 1 (Pressed) is observed on the |
| 23 | NR1L-ICS-014 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn4$ on the CAN trace and check that i |
| 23 | NR1L-ICS-014 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 1 (Pressed) is observed on the |
| 24 | NR1L-ICS-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and re |
| 24 | NR1L-ICS-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed) |
| 24 | NR1L-ICS-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 24 | NR1L-ICS-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 5. Read the signal $RADIO_B3.RQ_DISP_INTS$ on the CAN trace and check that it is |
| 24 | NR1L-ICS-015 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is o |
| 24 | NR1L-ICS-015 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the |
| 24 | NR1L-ICS-015 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is o |
| 24 | NR1L-ICS-015 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 5. The signal value $RADIO_B3.RQ_DISP_INTS$ = 0 (0 %) is observed on the CAN tra |
| 25 | NR1L-ICS-016 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. $STATUS_TELEMATIC.PowerSts_Telematic$ is 4 (Full_Operation) |
| 25 | NR1L-ICS-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and re |
| 25 | NR1L-ICS-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed) |
| 25 | NR1L-ICS-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 25 | NR1L-ICS-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 5. Read the signal $RADIO_B3.RQ_DISP_INTS$ on the CAN trace and check that it is |
| 25 | NR1L-ICS-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ is recorded on the CAN |
| 25 | NR1L-ICS-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the |
| 25 | NR1L-ICS-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is o |
| 25 | NR1L-ICS-016 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 5. The signal value $RADIO_B3.RQ_DISP_INTS$ = 0 (0 %) is observed on the CAN tra |
| 26 | NR1L-ICS-017 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and re |
| 26 | NR1L-ICS-017 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 4. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed) |
| 26 | NR1L-ICS-017 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 5. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 26 | NR1L-ICS-017 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is o |
| 26 | NR1L-ICS-017 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 4. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the |
| 26 | NR1L-ICS-017 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 5. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is o |
| 27 | NR1L-ICS-018 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. $STATUS_TELEMATIC.PowerSts_Telematic$ is 3 (Idle) |
| 27 | NR1L-ICS-018 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed) |
| 27 | NR1L-ICS-018 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 27 | NR1L-ICS-018 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the |
| 27 | NR1L-ICS-018 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is o |
| 28 | NR1L-ICS-019 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 1. Read the signals $CLIMATIC_PANEL.Radio_btn0$ and $CLIMATIC_PANEL.Radio_btn2$  |
| 28 | NR1L-ICS-019 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 1. Read the signals $CLIMATIC_PANEL.Radio_btn0$ and $CLIMATIC_PANEL.Radio_btn2$  |
| 28 | NR1L-ICS-019 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 4. Read the signal $CLIMATIC_PANEL.Radio_btn0$ on the CAN trace and check that i |
| 28 | NR1L-ICS-019 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 5. Read the signal $CLIMATIC_PANEL.Radio_btn2$ in the same message and check tha |
| 28 | NR1L-ICS-019 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 1. The signal values $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed) and $CLIMATIC |
| 28 | NR1L-ICS-019 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 1. The signal values $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed) and $CLIMATIC |
| 28 | NR1L-ICS-019 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn0$' | 4. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the |
| 28 | NR1L-ICS-019 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 5. The signal value $CLIMATIC_PANEL.Radio_btn2$ = 1 (Pressed) is observed in the |
| 29 | NR1L-ICS-020 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 2. Read the signal $CLIMATIC_PANEL.Radio_btn2$ and check that it is 1 (Pressed) |
| 29 | NR1L-ICS-020 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 3. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 1 seco |
| 29 | NR1L-ICS-020 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 2 seco |
| 29 | NR1L-ICS-020 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 2. The signal value $CLIMATIC_PANEL.Radio_btn2$ = 1 (Pressed) is observed on the |
| 29 | NR1L-ICS-020 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 3. The "TOUCH SCREEN TO TURN ON" graphic is shown, and the signal value $TELEMAT |
| 29 | NR1L-ICS-020 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The "TOUCH SCREEN TO TURN ON" graphic is shown, and the signal value $TELEMAT |
| 30 | NR1L-ICS-021 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 5 seco |
| 30 | NR1L-ICS-021 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is o |
| 31 | NR1L-ICS-022 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 3. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 31 | NR1L-ICS-022 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 4. Read the signal $RADIO_B3.RQ_DISP_INTS$ on the CAN trace and check that it is |
| 31 | NR1L-ICS-022 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 3. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is o |
| 31 | NR1L-ICS-022 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B3.RQ_DISP_INTS$' | 4. The signal value $RADIO_B3.RQ_DISP_INTS$ = 0 (0 %) is observed on the CAN tra |
| 32 | NR1L-ICS-023 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn2$ and check that it is 1 (Pressed) |
| 32 | NR1L-ICS-023 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and ch |
| 32 | NR1L-ICS-023 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn2$ = 1 (Pressed) is observed on the |
| 32 | NR1L-ICS-023 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$' | 4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is o |
| 33 | NR1L-ICS-024 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 2. Read the first frame carrying $CLIMATIC_PANEL.Radio_btn2$ = 1 (Pressed) and r |
| 33 | NR1L-ICS-024 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 5. Read the first frame carrying $CLIMATIC_PANEL.Radio_btn2$ = 0 (Not_Pressed) a |
| 33 | NR1L-ICS-024 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 2. A frame carrying $CLIMATIC_PANEL.Radio_btn2$ = 1 (Pressed) is observed on the |
| 33 | NR1L-ICS-024 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn2$' | 5. A frame carrying $CLIMATIC_PANEL.Radio_btn2$ = 0 (Not_Pressed) is observed no |
| 34 | NR1L-ICS-025 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn1$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn1$ and check that it is 1 (Pressed) |
| 34 | NR1L-ICS-025 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn1$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn1$ = 1 (Pressed) is received |
| 35 | NR1L-ICS-026 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn3$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn3$ on the CAN trace and check that i |
| 35 | NR1L-ICS-026 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn3$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn3$ = 1 (Pressed) is observed on the |
| 36 | NR1L-ICS-027 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 4. Read the signal $CLIMATIC_PANEL.Radio_btn4$ and check that it is 0 (Not_Press |
| 36 | NR1L-ICS-027 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 4. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 0 (Not_Pressed) is received pe |
| 37 | NR1L-ICS-028 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. Keep the button pressed and check that $CLIMATIC_PANEL.Radio_btn4$ is 0 (Not_ |
| 37 | NR1L-ICS-028 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 0 (Not_Pressed) is received wh |
| 38 | NR1L-ICS-029 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 5. Press and release the ICS "Mute" button and check that $CLIMATIC_PANEL.Radio_ |
| 38 | NR1L-ICS-029 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 5. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 1 (Pressed) is received, then  |
| 38 | NR1L-ICS-029 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 5. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 1 (Pressed) is received, then  |
| 39 | NR1L-ICS-030 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 4. Read the signal $CLIMATIC_PANEL.Radio_btn4$ and check that it is 1 (Pressed) |
| 39 | NR1L-ICS-030 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 4. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 1 (Pressed) is received |
| 40 | NR1L-ICS-031 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. Read the signal $CLIMATIC_PANEL.Radio_btn4$ and check that it is 0 (Not_Press |
| 40 | NR1L-ICS-031 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$CLIMATIC_PANEL.Radio_btn4$' | 3. The signal value $CLIMATIC_PANEL.Radio_btn4$ = 0 (Not_Pressed) is received |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 21 | NR1L-ICS-012 | pre | 多條件並列於同一行 | 3. The HU is on a tuner source for which a tune action is defined for knob 2 (so |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 6／列計 6）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 13 | NR1L-ICS-004 | pre | PENDING 佔位（DR-ICS4） | 2. The current audio level is at least three levels below the maximum audio leve |
| 19 | NR1L-ICS-010 | pre | PENDING 佔位（DR-ICS6） | 3. The HU shows a screen for which a browse action is defined for knob 2 (screen |
| 20 | NR1L-ICS-011 | pre | PENDING 佔位（DR-ICS6） | 3. The HU shows a screen for which a scroll action is defined for knob 2 (screen |
| 21 | NR1L-ICS-012 | pre | PENDING 佔位（DR-ICS6） | 3. The HU is on a tuner source for which a tune action is defined for knob 2 (so |
| 34 | NR1L-ICS-025 | pre | PENDING 佔位（DR-ICS6） | 3. The HU shows a screen for which an Enter action is defined (screen identified |
| 35 | NR1L-ICS-026 | pre | PENDING 佔位（DR-ICS6） | 3. The HU shows a screen for which a Back action is defined (screen identified p |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 31／列計 31）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-ICS-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-ICS-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-ICS-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-ICS-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-ICS-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-ICS-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-ICS-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-ICS-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-ICS-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-ICS-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-ICS-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-ICS-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-ICS-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-ICS-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-ICS-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-ICS-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-ICS-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-ICS-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-ICS-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-ICS-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-ICS-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-ICS-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-ICS-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-ICS-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-ICS-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-ICS-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-ICS-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-ICS-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-ICS-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-ICS-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-ICS-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 34 | NR1L-ICS-025 | er | 比較關係 'differs from'，而 test_item 上半無數值 | 4. The screen shown differs from the screen recorded in step 1 |
| 35 | NR1L-ICS-026 | er | 比較關係 'differs from'，而 test_item 上半無數值 | 4. The screen shown differs from the screen recorded in step 1 |
| 39 | NR1L-ICS-030 | er | 比較關係 'same as'，而 test_item 上半無數值 | The HU state is the same as the baseline recorded in step 2 |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 29／列計 15）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 16 | NR1L-ICS-007 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that the HU screen content is unchanged during the 5 seconds |
| 19 | NR1L-ICS-010 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen currently shown on the HU |
| 20 | NR1L-ICS-011 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen content currently shown on the HU |
| 20 | NR1L-ICS-011 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that the screen content has changed from the content recorded in step 1 |
| 24 | NR1L-ICS-015 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 6. Check that the HU screen is dark and shows no content |
| 25 | NR1L-ICS-016 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 6. Check that the HU screen is dark and shows no content |
| 26 | NR1L-ICS-017 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Record the screen that was shown before the HU entered the "HU Screen OFF" st |
| 26 | NR1L-ICS-017 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 6. Check that the screen shown is the same as the screen recorded in step 2 |
| 27 | NR1L-ICS-018 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen that was shown before the HU entered the "HU Screen OFF" st |
| 27 | NR1L-ICS-018 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Check that the screen shown is the same as the screen recorded in step 1 |
| 28 | NR1L-ICS-019 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Press the ICS "Screen Off" button while the "Power" button is still held |
| 29 | NR1L-ICS-020 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 1. Press the ICS "Screen Off" button |
| 29 | NR1L-ICS-020 | proc | 導航標的 'SCREEN' 而同 TC 無固定入口 | 5. Check that the "TOUCH SCREEN TO TURN ON" graphic is still shown 2 seconds aft |
| 30 | NR1L-ICS-021 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen currently shown on the HU |
| 30 | NR1L-ICS-021 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 2. Press the ICS "Screen Off" button |
| 30 | NR1L-ICS-021 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Press the ICS "Screen Off" button again 1 second after the first press |
| 30 | NR1L-ICS-021 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Check that the screen shown is the same as the screen recorded in step 1 |
| 31 | NR1L-ICS-022 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 1. Press the ICS "Screen Off" button |
| 31 | NR1L-ICS-022 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Wait for the 3 second period to complete without touching the screen |
| 31 | NR1L-ICS-022 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Check that the HU screen is dark and shows no content |
| 32 | NR1L-ICS-023 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen that was shown before the HU entered the "HU Screen OFF" st |
| 32 | NR1L-ICS-023 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 2. Press the ICS "Screen Off" button |
| 32 | NR1L-ICS-023 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Check that the screen shown is the same as the screen recorded in step 1 |
| 33 | NR1L-ICS-024 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 1. Press the ICS "Screen Off" button and record the time of the press |
| 33 | NR1L-ICS-024 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 4. Release the ICS "Screen Off" button and record the time of the release |
| 34 | NR1L-ICS-025 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen currently shown on the HU |
| 34 | NR1L-ICS-025 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that the screen shown has changed from the screen recorded in step 1 |
| 35 | NR1L-ICS-026 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Record the screen currently shown on the HU |
| 35 | NR1L-ICS-026 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Check that the screen shown has changed from the screen recorded in step 1 |

