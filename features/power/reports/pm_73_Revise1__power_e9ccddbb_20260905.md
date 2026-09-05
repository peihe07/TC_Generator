# lint036 報告：pm_73_Revise1.xlsx

- 來源：`features/power/delivered/pm_73_Revise1.xlsx`（唯讀）
- 資料列數：287
- sheet：`Test Case Specification&Result`（header 第 9 列）
- L 閾值：50 tokens
- profile：`power`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 37 | 30 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 19 | 12 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 10 | 10 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 3 | 3 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 111 | 111 | 每列 | 未校準（M15） |
| J | 行首大寫 | 3 | 3 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 81 | 74 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 72 | 72 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 254 | 142 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 186 | 175 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 30 | 28 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 111 | 68 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 377 | 147 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 285 | 285 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 7 | 5 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 103 | 84 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |

**總計：行計 1689**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 37／列計 30）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PowerManagement-261 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 10 | NR1L-PowerManagement-261 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 13 | NR1L-PowerManagement-263 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 14 | NR1L-PowerManagement-264 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 2. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 17 | NR1L-PowerManagement-267 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 17 | NR1L-PowerManagement-267 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 24 | NR1L-PowerManagement-273 | proc | 禁用動詞 'check whether' | d the bus trace and check whether the HU keeps transmitting the $STATUS_TELEMATI |
| 24 | NR1L-PowerManagement-273 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 24 | NR1L-PowerManagement-273 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 8. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 26 | NR1L-PowerManagement-275 | proc | 禁用動詞 'check whether' | d the bus trace and check whether the HU keeps transmitting the $STATUS_TELEMATI |
| 26 | NR1L-PowerManagement-275 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 26 | NR1L-PowerManagement-275 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 8. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 28 | NR1L-PowerManagement-277 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 28 | NR1L-PowerManagement-277 | proc | 禁用動詞 'Check whether' | ad the bus trace ⏎ 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) wi |
| 34 | NR1L-PowerManagement-044 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 35 | NR1L-PowerManagement-045 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 36 | NR1L-PowerManagement-046 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 136 | NR1L-PowerManagement-135 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 137 | NR1L-PowerManagement-136 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 191 | NR1L-PowerManagement-010 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 195 | NR1L-PowerManagement-014 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 212 | NR1L-PowerManagement-231 | proc | 禁用動詞 '1. Observe' | 1. Observe the bus traffic while the CAN network stays awake ⏎ 2. Read the signal |
| 227 | NR1L-PowerManagement-246 | proc | 禁用動詞 '1. Observe' | 1. Observe the bus traffic while the CAN network stays awake ⏎ 2. Read the signal |
| 250 | NR1L-PowerManagement-255 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 251 | NR1L-PowerManagement-256 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 252 | NR1L-PowerManagement-257 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 253 | NR1L-PowerManagement-258 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 254 | NR1L-PowerManagement-259 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 255 | NR1L-PowerManagement-260 | proc | 禁用動詞 'check whether' | d the recording and check whether the "New Season Animation" or the "Brand Anima |
| 259 | NR1L-PowerManagement-188 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 260 | NR1L-PowerManagement-189 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 261 | NR1L-PowerManagement-190 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them |
| 269 | NR1L-PowerManagement-198 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 270 | NR1L-PowerManagement-199 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 271 | NR1L-PowerManagement-200 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 272 | NR1L-PowerManagement-201 | proc | 禁用動詞 'check whether' | the HU speakers and check whether entertainment audio output is present on them ⏎ |
| 295 | NR1L-PowerManagement-224 | proc | 禁用動詞 'check whether' | d the HU screen and check whether the "Disclaimer" screen or the geolocation pop |

### D — PC 違規 (pre)（行計 19／列計 12）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 209 | NR1L-PowerManagement-228 | pre | 編號行行首動詞 'Set' | 2. Set VC_VEH_BRAND = the configured brand (DR-PW28) |
| 210 | NR1L-PowerManagement-229 | pre | 編號行行首動詞 'Set' | 2. Set VC_VEH_BRAND = the configured brand (DR-PW28) |
| 230 | NR1L-PowerManagement-249 | pre | 編號行行首動詞 'Set' | 3. Set VC_VEH_BRAND = the configured brand (DR-PW28) |
| 231 | NR1L-PowerManagement-286 | pre | 編號行行首動詞 'Set' | 3. Set VC_VEH_BRAND = the configured brand (DR-PW28) |
| 257 | NR1L-PowerManagement-186 | pre | 編號行行首動詞 'Set' | 2. Set Themed_Sound = "Fiat Latam" (DR-PW28) |
| 257 | NR1L-PowerManagement-186 | pre | 編號行行首動詞 'Select' | 3. Select "Welcome Onboard Sound" = "Always" |
| 258 | NR1L-PowerManagement-187 | pre | 編號行行首動詞 'Set' | 2. Set Themed_Sound = "Fiat Latam" (DR-PW28) |
| 258 | NR1L-PowerManagement-187 | pre | 編號行行首動詞 'Select' | 3. Select "Welcome Onboard Sound" = "Once a day" |
| 262 | NR1L-PowerManagement-191 | pre | 編號行行首動詞 'Set' | 2. Set Themed_Sound = "Fiat Latam" (DR-PW28) |
| 262 | NR1L-PowerManagement-191 | pre | 編號行行首動詞 'Select' | 3. Select "Welcome Onboard Sound" = "Never" |
| 287 | NR1L-PowerManagement-216 | pre | 編號行行首動詞 'Set' | 2. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28) |
| 287 | NR1L-PowerManagement-216 | pre | 編號行行首動詞 'Set' | 3. Set TBM_Present = "Present" (DR-PW28) |
| 288 | NR1L-PowerManagement-217 | pre | 編號行行首動詞 'Set' | 2. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28) |
| 288 | NR1L-PowerManagement-217 | pre | 編號行行首動詞 'Set' | 3. Set TBM_Present = "Present" (DR-PW28) |
| 293 | NR1L-PowerManagement-222 | pre | 編號行行首動詞 'Set' | 3. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28) |
| 293 | NR1L-PowerManagement-222 | pre | 編號行行首動詞 'Set' | 4. Set TBM_Present = "Not Present" (DR-PW28) |
| 294 | NR1L-PowerManagement-223 | pre | 編號行行首動詞 'Set' | 3. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28) |
| 295 | NR1L-PowerManagement-224 | pre | 編號行行首動詞 'Set' | 3. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28) |
| 295 | NR1L-PowerManagement-224 | pre | 編號行行首動詞 'Set' | 4. Set TBM_Present = "Present" (DR-PW28) |

### F — 方括號佔位 (proc)（行計 10／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 208 | NR1L-PowerManagement-227 | proc | 方括號佔位 '[PDO Theme Configuration]' | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 209 | NR1L-PowerManagement-228 | proc | 方括號佔位 '[PDO Theme Configuration]' | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 210 | NR1L-PowerManagement-229 | proc | 方括號佔位 '[PDO Theme Configuration]' | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 211 | NR1L-PowerManagement-230 | proc | 方括號佔位 '[PDO Theme Configuration]' | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該元件之預設值與元件清單 |
| 212 | NR1L-PowerManagement-231 | proc | 方括號佔位 '[PDO Theme Configuration]' | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 227 | NR1L-PowerManagement-246 | proc | 方括號佔位 '[PDO Theme Configuration]' | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 234 | NR1L-PowerManagement-251 | proc | 方括號佔位 '[PDO Theme Configuration]' | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 235 | NR1L-PowerManagement-252 | proc | 方括號佔位 '[PDO Theme Configuration]' | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 236 | NR1L-PowerManagement-253 | proc | 方括號佔位 '[PDO Theme Configuration]' | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 237 | NR1L-PowerManagement-254 | proc | 方括號佔位 '[PDO Theme Configuration]' | 2. PENDING: DR-PW27 [PDO Theme Configuration] |

### H — ER 模糊語 (er)（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 186 | NR1L-PowerManagement-005 | er | 關係模糊語 'corresponds to' | PowerSts_Telematic$ corresponds to the last ignition value that was sent |
| 225 | NR1L-PowerManagement-244 | er | 關係模糊語 'matches' | ings "Seat Graphic" matches the assignment for that vehicle line and car shape |
| 226 | NR1L-PowerManagement-245 | er | 關係模糊語 'matches' | ings "Seat Graphic" matches the assignment for that vehicle line and body style |

### I-sibling — 同 Requirement ID 括號行逐字重複（行計 111／列計 111）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 33 | NR1L-PowerManagement-043 | test_item | 與 SWE-PM-011 下另 1 列括號行逐字相同 | (read the HU mode -> The HU is in Full-Operation mode) |
| 38 | NR1L-PowerManagement-048 | test_item | 與 SWE-PM-011 下另 1 列括號行逐字相同 | (read the HU mode -> The HU is in Full-Operation mode) |
| 41 | NR1L-PowerManagement-051 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 42 | NR1L-PowerManagement-052 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 43 | NR1L-PowerManagement-053 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 44 | NR1L-PowerManagement-054 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 47 | NR1L-PowerManagement-057 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby) |
| 49 | NR1L-PowerManagement-059 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 53 | NR1L-PowerManagement-063 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 55 | NR1L-PowerManagement-065 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby) |
| 56 | NR1L-PowerManagement-066 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 57 | NR1L-PowerManagement-067 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 58 | NR1L-PowerManagement-068 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 59 | NR1L-PowerManagement-069 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 62 | NR1L-PowerManagement-072 | test_item | 與 SWE-PM-018 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 63 | NR1L-PowerManagement-073 | test_item | 與 SWE-PM-018 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 64 | NR1L-PowerManagement-074 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read TLM_Status.Info and the screen -> TLM_Status.Info still reads "Idle" and n |
| 65 | NR1L-PowerManagement-075 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read the screen, VPLastStatus and TLM_Status.Info -> VPLastStatus reads "ON", T |
| 66 | NR1L-PowerManagement-076 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read TLM_Status.Info and the screen -> TLM_Status.Info still reads "Idle" and n |
| 67 | NR1L-PowerManagement-077 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read the screen, VPLastStatus and TLM_Status.Info -> VPLastStatus reads "ON", T |
| 75 | NR1L-PowerManagement-085 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the screen -> A popup asking whether to transfer the call is shown to the  |
| 76 | NR1L-PowerManagement-086 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 77 | NR1L-PowerManagement-087 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 78 | NR1L-PowerManagement-088 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the active functionality and TLM_Status.Info -> TLM_Status.Info and $Telem |
| 79 | NR1L-PowerManagement-089 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the screen -> A popup asking whether to transfer the call is shown to the  |
| 80 | NR1L-PowerManagement-090 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 81 | NR1L-PowerManagement-091 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 82 | NR1L-PowerManagement-092 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the active functionality and TLM_Status.Info -> TLM_Status.Info and $Telem |
| 84 | NR1L-PowerManagement-094 | test_item | 與 SWE-PM-026 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 85 | NR1L-PowerManagement-095 | test_item | 與 SWE-PM-026 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 90 | NR1L-PowerManagement-100 | test_item | 與 SWE-PM-028 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 91 | NR1L-PowerManagement-101 | test_item | 與 SWE-PM-028 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 93 | NR1L-PowerManagement-103 | test_item | 與 SWE-PM-029 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 94 | NR1L-PowerManagement-104 | test_item | 與 SWE-PM-029 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 95 | NR1L-PowerManagement-105 | test_item | 與 SWE-PM-030 下另 1 列括號行逐字相同 | (read the screen and its duration -> The Splash Screen stays for Response_Wait_T |
| 96 | NR1L-PowerManagement-106 | test_item | 與 SWE-PM-030 下另 1 列括號行逐字相同 | (read the screen and its duration -> The Splash Screen stays for Response_Wait_T |
| 99 | NR1L-PowerManagement-109 | test_item | 與 SWE-PM-033 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 100 | NR1L-PowerManagement-110 | test_item | 與 SWE-PM-033 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 111 | NR1L-PowerManagement-035 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 112 | NR1L-PowerManagement-036 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 113 | NR1L-PowerManagement-037 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 114 | NR1L-PowerManagement-038 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 115 | NR1L-PowerManagement-039 | test_item | 與 SWE-PM-038 下另 1 列括號行逐字相同 | (read the TLM state and the MaxCallTimeout counter -> The TLM is in Timed state  |
| 116 | NR1L-PowerManagement-040 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 117 | NR1L-PowerManagement-041 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 118 | NR1L-PowerManagement-042 | test_item | 與 SWE-PM-038 下另 1 列括號行逐字相同 | (read the TLM state and the MaxCallTimeout counter -> The TLM is in Timed state  |
| 120 | NR1L-PowerManagement-119 | test_item | 與 SWE-PM-039 下另 1 列括號行逐字相同 | (read Timeout1 against the configured parameter -> Timeout1 reads the "Switch_Of |
| 121 | NR1L-PowerManagement-120 | test_item | 與 SWE-PM-039 下另 1 列括號行逐字相同 | (read Timeout1 against the configured parameter -> Timeout1 reads the "Switch_Of |
| 130 | NR1L-PowerManagement-129 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 131 | NR1L-PowerManagement-130 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 132 | NR1L-PowerManagement-131 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 133 | NR1L-PowerManagement-132 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 154 | NR1L-PowerManagement-153 | test_item | 與 SWE-PM-055 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 155 | NR1L-PowerManagement-154 | test_item | 與 SWE-PM-055 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 175 | NR1L-PowerManagement-159 | test_item | 與 SWE-PM-066 下另 1 列括號行逐字相同 | (read the HU reaction -> The HU behaves as for a Phone call becoming active) |
| 176 | NR1L-PowerManagement-160 | test_item | 與 SWE-PM-066 下另 1 列括號行逐字相同 | (read the HU reaction -> The HU behaves as for a Phone call becoming active) |
| 179 | NR1L-PowerManagement-163 | test_item | 與 SWE-PM-069 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions back to IDLE) |
| 180 | NR1L-PowerManagement-164 | test_item | 與 SWE-PM-069 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions back to IDLE) |
| 189 | NR1L-PowerManagement-008 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the display, HVAC controls, ACN phone state and AUD_LVL -> The display sta |
| 192 | NR1L-PowerManagement-011 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the call audio routing -> The continuing call is routed to the head set an |
| 193 | NR1L-PowerManagement-012 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the call audio routing -> The continuing call is routed to the head set an |
| 194 | NR1L-PowerManagement-013 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the display, HVAC controls, ACN phone state and AUD_LVL -> The display sta |
| 196 | NR1L-PowerManagement-015 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the CAN trace and the volume level -> No AUD_LVL signal carrying a new vol |
| 197 | NR1L-PowerManagement-016 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the CAN trace and the volume level -> No AUD_LVL signal carrying a new vol |
| 198 | NR1L-PowerManagement-166 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 199 | NR1L-PowerManagement-167 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 200 | NR1L-PowerManagement-168 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 201 | NR1L-PowerManagement-169 | test_item | 與 SWE-PM-075 下另 2 列括號行逐字相同 | (read the HU mode after the idle period -> The HU transitions to Standby mode af |
| 202 | NR1L-PowerManagement-170 | test_item | 與 SWE-PM-075 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions to Standby mode) |
| 203 | NR1L-PowerManagement-171 | test_item | 與 SWE-PM-075 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions to Standby mode) |
| 204 | NR1L-PowerManagement-284 | test_item | 與 SWE-PM-075 下另 2 列括號行逐字相同 | (read the HU mode after the idle period -> The HU transitions to Standby mode af |
| 205 | NR1L-PowerManagement-285 | test_item | 與 SWE-PM-075 下另 2 列括號行逐字相同 | (read the HU mode after the idle period -> The HU transitions to Standby mode af |
| 209 | NR1L-PowerManagement-228 | test_item | 與 SWE-PM-078 下另 1 列括號行逐字相同 | (read the applied theme against the brand signal -> The default theme based on t |
| 210 | NR1L-PowerManagement-229 | test_item | 與 SWE-PM-078 下另 1 列括號行逐字相同 | (read the applied theme against the brand signal -> The default theme based on t |
| 230 | NR1L-PowerManagement-249 | test_item | 與 SWE-PM-087 下另 1 列括號行逐字相同 | (read the shown seat graphic against the brand signal -> The HU uses $VC_VEH_BRA |
| 231 | NR1L-PowerManagement-286 | test_item | 與 SWE-PM-087 下另 1 列括號行逐字相同 | (read the shown seat graphic against the brand signal -> The HU uses $VC_VEH_BRA |
| 238 | NR1L-PowerManagement-174 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 239 | NR1L-PowerManagement-175 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 240 | NR1L-PowerManagement-176 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 241 | NR1L-PowerManagement-177 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen -> The HU skips the start-up animation) |
| 242 | NR1L-PowerManagement-178 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 243 | NR1L-PowerManagement-179 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 244 | NR1L-PowerManagement-180 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 245 | NR1L-PowerManagement-181 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen -> The HU skips the start-up animation) |
| 246 | NR1L-PowerManagement-182 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen against the elapsed time -> A start-up animation plays again on |
| 247 | NR1L-PowerManagement-287 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen against the elapsed time -> A start-up animation plays again on |
| 259 | NR1L-PowerManagement-188 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 260 | NR1L-PowerManagement-189 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 261 | NR1L-PowerManagement-190 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 267 | NR1L-PowerManagement-196 | test_item | 與 SWE-PM-102 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 268 | NR1L-PowerManagement-197 | test_item | 與 SWE-PM-102 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 269 | NR1L-PowerManagement-198 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 270 | NR1L-PowerManagement-199 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 271 | NR1L-PowerManagement-200 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 272 | NR1L-PowerManagement-201 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 274 | NR1L-PowerManagement-203 | test_item | 與 SWE-PM-104 下另 1 列括號行逐字相同 | (read the screen sequence -> The disclaimer screen is shown) |
| 275 | NR1L-PowerManagement-204 | test_item | 與 SWE-PM-104 下另 1 列括號行逐字相同 | (read the screen sequence -> The disclaimer screen is shown) |
| 276 | NR1L-PowerManagement-205 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 277 | NR1L-PowerManagement-206 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 278 | NR1L-PowerManagement-207 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 279 | NR1L-PowerManagement-208 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 280 | NR1L-PowerManagement-209 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 281 | NR1L-PowerManagement-210 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 282 | NR1L-PowerManagement-211 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 283 | NR1L-PowerManagement-212 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 284 | NR1L-PowerManagement-213 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 285 | NR1L-PowerManagement-214 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 291 | NR1L-PowerManagement-220 | test_item | 與 SWE-PM-110 下另 1 列括號行逐字相同 | (read the startup flow against the HMI -> The HU follows the Non-GDPR/Non-Masera |
| 292 | NR1L-PowerManagement-221 | test_item | 與 SWE-PM-110 下另 1 列括號行逐字相同 | (read the startup flow against the HMI -> The HU follows the Non-GDPR/Non-Masera |
| 293 | NR1L-PowerManagement-222 | test_item | 與 SWE-PM-111 下另 1 列括號行逐字相同 | (read the disclaimer wording -> The HU adds the ADAS text to the disclaimer) |
| 294 | NR1L-PowerManagement-223 | test_item | 與 SWE-PM-111 下另 1 列括號行逐字相同 | (read the disclaimer wording -> The HU adds the ADAS text to the disclaimer) |

### J — 行首大寫（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 20 | NR1L-PowerManagement-270 | test_item | 首字小寫 'the' | the R1 HU shall not enter stolen vehicle mode under any condition |
| 161 | NR1L-PowerManagement-157 | proc | 首字小寫 'shutdown' | 3. shutdown counter |
| 206 | NR1L-PowerManagement-172 | test_item | 首字小寫 'the' | the HU shall reset both the main CPU and the CAN micro at the time of the reset |

### K — CJK 字元（行計 81／列計 74）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PowerManagement-261 | proc | 含 CJK 字元 | play sub-item  (DTV 影像僅經顯示可見；規格無獨立 DTV 觀察面) |
| 14 | NR1L-PowerManagement-264 | proc | 含 CJK 字元 | play sub-item  (DTV 影像僅經顯示可見；規格無獨立 DTV 觀察面) |
| 17 | NR1L-PowerManagement-267 | proc | 含 CJK 字元 | play sub-item  (DTV 影像僅經顯示可見；規格無獨立 DTV 觀察面) |
| 18 | NR1L-PowerManagement-268 | proc | 含 CJK 字元 | ENDING: DR-PW29 ANC 之刺激與觀察面 ⏎ 3. PENDING: DR-PW29 ACN 之刺激與觀察面 |
| 24 | NR1L-PowerManagement-273 | proc | 含 CJK 字元 | ion sub-item  (FPDM 對應為分析層判斷，非規格明文 ⏎ 5. R-P396(c)，併 DR-PW29) ⏎ 6. Read the HU speake |
| 26 | NR1L-PowerManagement-275 | proc | 含 CJK 字元 | ion sub-item  (FPDM 對應為分析層判斷，非規格明文 ⏎ 5. R-P396(c)，併 DR-PW29) ⏎ 6. Read the HU speake |
| 28 | NR1L-PowerManagement-277 | proc | 含 CJK 字元 | play sub-item  (DTV 影像僅經顯示可見；規格無獨立 DTV 觀察面) |
| 29 | NR1L-PowerManagement-281 | proc | 含 CJK 字元 | ital antenna supply 之 ON 位準值 ⏎ 5. Measure the voltage at each output and check it |
| 29 | NR1L-PowerManagement-281 | er | 含 CJK 字元 | / antenna supply ON 位準值 ⏎ 5. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值 ⏎ 6 |
| 30 | NR1L-PowerManagement-278 | proc | 含 CJK 字元 | witchOn_Setting.Req 之設定項名 ⏎ 6. PENDING: DR-PW23 Antitheft_Activation.Req ⏎ 7. PENDIN |
| 31 | NR1L-PowerManagement-279 | proc | 含 CJK 字元 | NDING: DR-PW26 INIT 觀察量 |
| 39 | NR1L-PowerManagement-049 | proc | 含 CJK 字元 | witchOffSetting.Req 與 Auto_SwitchOn_Setting.Req 之設定項名與讀取方法 |
| 45 | NR1L-PowerManagement-055 | er | 含 CJK 字元 | / antenna supply ON 位準值 ⏎    d. A USB device is not enumerated and the AUX input d |
| 71 | NR1L-PowerManagement-081 | proc | 含 CJK 字元 | _Camera_Enable.Info 之驅動方法（自 "False" 轉 "True"） ⏎ 2. Read the HU screen and check th |
| 90 | NR1L-PowerManagement-100 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法（設為 "00 min"） ⏎ 2. Apply ENTER_TIMED and read the signal |
| 91 | NR1L-PowerManagement-101 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法（設為 "00 min"） ⏎ 2. Apply ENTER_TIMED and read the signal |
| 93 | NR1L-PowerManagement-103 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法（設為 "00 min"） ⏎ 2. Apply ENTER_TIMED and read the signal |
| 94 | NR1L-PowerManagement-104 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法（設為 "00 min"） ⏎ 2. Apply ENTER_TIMED and read the signal |
| 95 | NR1L-PowerManagement-105 | proc | 含 CJK 字元 | Response_Wait_Time 之值 |
| 95 | NR1L-PowerManagement-105 | er | 含 CJK 字元 | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 2. The "Splash Screen" stays |
| 96 | NR1L-PowerManagement-106 | proc | 含 CJK 字元 | Response_Wait_Time 之值 |
| 96 | NR1L-PowerManagement-106 | er | 含 CJK 字元 | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 2. The "Splash Screen" stays |
| 101 | NR1L-PowerManagement-111 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 104 | NR1L-PowerManagement-114 | er | 含 CJK 字元 | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 2. TLM_Status.Info and $Tele |
| 107 | NR1L-PowerManagement-117 | proc | 含 CJK 字元 | PW23 PhoneCall.Info 之驅動方法（使其轉為 "not Active"） ⏎ 2. Read the signal $STATUS_TELEMATI |
| 120 | NR1L-PowerManagement-119 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法 ⏎ 2. Apply ENTER_FULL_OPERATION ⏎ 3. Send CAN: STATUS_BH_B |
| 121 | NR1L-PowerManagement-120 | proc | 含 CJK 字元 | Timeout_Setting.Req 之設定方法 ⏎ 2. Apply ENTER_FULL_OPERATION ⏎ 3. Send CAN: STATUS_BH_B |
| 122 | NR1L-PowerManagement-121 | proc | 含 CJK 字元 | LM HMI documents —— 該態下應不可用之 vehicle setup 項目清單 |
| 123 | NR1L-PowerManagement-122 | proc | 含 CJK 字元 | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 2. PENDING: DR-PW26 Suspend- |
| 124 | NR1L-PowerManagement-123 | er | 含 CJK 字元 | antenna supply OFF 位準值 ⏎    e. A USB device inserted on the bench is not enumerat |
| 126 | NR1L-PowerManagement-125 | proc | 含 CJK 字元 | DING: DR-PW26 Sleep 態之觀察方法（CAN 睡眠後無法以 CAN 讀 $STATUS_TELEMATIC.PowerSts_Telematic |
| 126 | NR1L-PowerManagement-125 | er | 含 CJK 字元 | DING: DR-PW26 Sleep 態之觀察方法 ⏎ 3. FUNC_STATE_SLEEP holds: ⏎    a. No audio source is p |
| 130 | NR1L-PowerManagement-129 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 131 | NR1L-PowerManagement-130 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 132 | NR1L-PowerManagement-131 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 133 | NR1L-PowerManagement-132 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 134 | NR1L-PowerManagement-133 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 135 | NR1L-PowerManagement-134 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 138 | NR1L-PowerManagement-137 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 139 | NR1L-PowerManagement-138 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 144 | NR1L-PowerManagement-143 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 145 | NR1L-PowerManagement-144 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 148 | NR1L-PowerManagement-147 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 157 | NR1L-PowerManagement-017 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 158 | NR1L-PowerManagement-018 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 159 | NR1L-PowerManagement-019 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 160 | NR1L-PowerManagement-156 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 163 | NR1L-PowerManagement-020 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 164 | NR1L-PowerManagement-021 | proc | 含 CJK 字元 | ING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 ⏎ 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 182 | NR1L-PowerManagement-001 | proc | 含 CJK 字元 | 0 SplashScreen_Time 之值 ⏎ 3. Read the HU screen and check the "Splash Screen" again |
| 183 | NR1L-PowerManagement-002 | proc | 含 CJK 字元 | 0 SplashScreen_Time 之值 ⏎ 3. Read the HU screen and check the "Splash Screen" again |
| 184 | NR1L-PowerManagement-003 | proc | 含 CJK 字元 | 0 SplashScreen_Time 之值 ⏎ 3. Read the HU screen and check the "Splash Screen" again |
| 185 | NR1L-PowerManagement-004 | proc | 含 CJK 字元 | 0 SplashScreen_Time 之值 ⏎ 3. Read the HU screen at that time and check that the "Sp |
| 190 | NR1L-PowerManagement-009 | proc | 含 CJK 字元 | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 190 | NR1L-PowerManagement-009 | er | 含 CJK 字元 | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 191 | NR1L-PowerManagement-010 | er | 含 CJK 字元 | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 5. PENDING: DR-PW27 該規格措辭之逐字 |
| 201 | NR1L-PowerManagement-169 | proc | 含 CJK 字元 | TA update available 之建立方法 ⏎ 2. Apply ENTER_TIMED ⏎ 3. Read the HU screen and check t |
| 204 | NR1L-PowerManagement-284 | proc | 含 CJK 字元 | TA update available 之建立方法 ⏎ 2. Apply ENTER_TIMED ⏎ 3. Read the HU screen and check t |
| 205 | NR1L-PowerManagement-285 | proc | 含 CJK 字元 | TA update available 之建立方法 ⏎ 2. Apply ENTER_TIMED with $BCM_FD_27.Comfort_Enable_Ac |
| 209 | NR1L-PowerManagement-228 | proc | 含 CJK 字元 | e Configuration] —— 該品牌之預設 theme |
| 210 | NR1L-PowerManagement-229 | proc | 含 CJK 字元 | e Configuration] —— 該品牌之預設 theme |
| 211 | NR1L-PowerManagement-230 | proc | 含 CJK 字元 | e Configuration] —— 該元件之預設值與元件清單 |
| 213 | NR1L-PowerManagement-232 | proc | 含 CJK 字元 | NG: DR-PW27 <Tsend> 之值 |
| 223 | NR1L-PowerManagement-242 | proc | 含 CJK 字元 | PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 224 | NR1L-PowerManagement-243 | proc | 含 CJK 字元 | PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 225 | NR1L-PowerManagement-244 | proc | 含 CJK 字元 | R-PW27 seat graphic 指派 |
| 226 | NR1L-PowerManagement-245 | proc | 含 CJK 字元 | R-PW27 seat graphic 指派 |
| 228 | NR1L-PowerManagement-247 | proc | 含 CJK 字元 | NG: DR-PW27 <Tsend> 之值 |
| 229 | NR1L-PowerManagement-248 | proc | 含 CJK 字元 | R-PW27 seat graphic 指派 |
| 230 | NR1L-PowerManagement-249 | proc | 含 CJK 字元 | PENDING: DR-PW27 —— 非 M240 之 seat graphic 指派 |
| 232 | NR1L-PowerManagement-250 | proc | 含 CJK 字元 | PENDING: DR-PW27 —— 該 vehicle line 之 gauges 指派 |
| 242 | NR1L-PowerManagement-178 | proc | 含 CJK 字元 | NG: DR-PW29 BODY ON 對應之 PowerSts_Telematic 值（`4941042` Full-Operation 與 `4941039 |
| 242 | NR1L-PowerManagement-178 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 243 | NR1L-PowerManagement-179 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 244 | NR1L-PowerManagement-180 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） ⏎ 3. PENDING: DR-PW27 該規格措辭之逐字 |
| 247 | NR1L-PowerManagement-287 | proc | 含 CJK 字元 | DING: DR-PW26 Sleep 態之觀察方法 ⏎ 4. Let the Body CAN go to sleep and wake it again to |
| 247 | NR1L-PowerManagement-287 | er | 含 CJK 字元 | DING: DR-PW26 Sleep 態之觀察方法 ⏎ 4. PENDING: DR-PW26 Sleep 態之觀察方法 ⏎ 5. The "Start-up Ani |
| 255 | NR1L-PowerManagement-260 | er | 含 CJK 字元 | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 293 | NR1L-PowerManagement-222 | proc | 含 CJK 字元 | ng —— the ADAS text 之逐字定義 |
| 294 | NR1L-PowerManagement-223 | proc | 含 CJK 字元 | ng —— the ADAS text 之逐字定義 |
| 295 | NR1L-PowerManagement-224 | proc | 含 CJK 字元 | wording（ADAS ＋ SOS 之逐字文字） |

### L — test_item 上半過長 (>50 tokens)（行計 72／列計 72）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-PowerManagement-282 | test_item | 上半 88 tokens > 50 | Full-Operation ⏎ TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT |
| 23 | NR1L-PowerManagement-283 | test_item | 上半 88 tokens > 50 | Timed ⏎ TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music st |
| 29 | NR1L-PowerManagement-281 | test_item | 上半 84 tokens > 50 | Bench ⏎ LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc) ⏎ |
| 32 | NR1L-PowerManagement-280 | test_item | 上半 59 tokens > 50 | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 39 | NR1L-PowerManagement-049 | test_item | 上半 59 tokens > 50 | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 47 | NR1L-PowerManagement-057 | test_item | 上半 188 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 55 | NR1L-PowerManagement-065 | test_item | 上半 188 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 58 | NR1L-PowerManagement-068 | test_item | 上半 56 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Pan |
| 59 | NR1L-PowerManagement-069 | test_item | 上半 56 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_ |
| 68 | NR1L-PowerManagement-078 | test_item | 上半 52 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info has |
| 69 | NR1L-PowerManagement-079 | test_item | 上半 68 tokens > 50 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 70 | NR1L-PowerManagement-080 | test_item | 上半 68 tokens > 50 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 90 | NR1L-PowerManagement-100 | test_item | 上半 52 tokens > 50 | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 91 | NR1L-PowerManagement-101 | test_item | 上半 52 tokens > 50 | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 130 | NR1L-PowerManagement-129 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 131 | NR1L-PowerManagement-130 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 132 | NR1L-PowerManagement-131 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 133 | NR1L-PowerManagement-132 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 136 | NR1L-PowerManagement-135 | test_item | 上半 55 tokens > 50 | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == |
| 137 | NR1L-PowerManagement-136 | test_item | 上半 55 tokens > 50 | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == |
| 182 | NR1L-PowerManagement-001 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 183 | NR1L-PowerManagement-002 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 184 | NR1L-PowerManagement-003 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 185 | NR1L-PowerManagement-004 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 186 | NR1L-PowerManagement-005 | test_item | 上半 51 tokens > 50 | Any event occurring during the boot must be recognized by TLM and then TLM has t |
| 187 | NR1L-PowerManagement-006 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 188 | NR1L-PowerManagement-007 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 189 | NR1L-PowerManagement-008 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 190 | NR1L-PowerManagement-009 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 191 | NR1L-PowerManagement-010 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 192 | NR1L-PowerManagement-011 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 193 | NR1L-PowerManagement-012 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 194 | NR1L-PowerManagement-013 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 195 | NR1L-PowerManagement-014 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 196 | NR1L-PowerManagement-015 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 197 | NR1L-PowerManagement-016 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 212 | NR1L-PowerManagement-231 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 213 | NR1L-PowerManagement-232 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 214 | NR1L-PowerManagement-233 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 215 | NR1L-PowerManagement-234 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 216 | NR1L-PowerManagement-235 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 217 | NR1L-PowerManagement-236 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 218 | NR1L-PowerManagement-237 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 219 | NR1L-PowerManagement-238 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 220 | NR1L-PowerManagement-239 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 221 | NR1L-PowerManagement-240 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 222 | NR1L-PowerManagement-241 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 223 | NR1L-PowerManagement-242 | test_item | 上半 61 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 224 | NR1L-PowerManagement-243 | test_item | 上半 61 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 225 | NR1L-PowerManagement-244 | test_item | 上半 68 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 226 | NR1L-PowerManagement-245 | test_item | 上半 68 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 227 | NR1L-PowerManagement-246 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 228 | NR1L-PowerManagement-247 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 238 | NR1L-PowerManagement-174 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 239 | NR1L-PowerManagement-175 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 240 | NR1L-PowerManagement-176 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 241 | NR1L-PowerManagement-177 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 242 | NR1L-PowerManagement-178 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 243 | NR1L-PowerManagement-179 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 244 | NR1L-PowerManagement-180 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 245 | NR1L-PowerManagement-181 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 246 | NR1L-PowerManagement-182 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 247 | NR1L-PowerManagement-287 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 279 | NR1L-PowerManagement-208 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 280 | NR1L-PowerManagement-209 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 281 | NR1L-PowerManagement-210 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 282 | NR1L-PowerManagement-211 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 283 | NR1L-PowerManagement-212 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 284 | NR1L-PowerManagement-213 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 285 | NR1L-PowerManagement-214 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 286 | NR1L-PowerManagement-215 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 295 | NR1L-PowerManagement-224 | test_item | 上半 59 tokens > 50 | For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Pres |

### P — 訊號寫法不合 R-1 v2（行計 254／列計 142）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PowerManagement-261 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 10 | NR1L-PowerManagement-261 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 11 | NR1L-PowerManagement-262 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Apply each ignition working condition listed in Input Test Data in turn by se |
| 11 | NR1L-PowerManagement-262 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. After each one, read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and che |
| 14 | NR1L-PowerManagement-264 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 2. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 17 | NR1L-PowerManagement-267 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM2.RemStActvSts =' | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 17 | NR1L-PowerManagement-267 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 17 | NR1L-PowerManagement-267 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 17 | NR1L-PowerManagement-267 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 20 | NR1L-PowerManagement-270 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and record the value as |
| 20 | NR1L-PowerManagement-270 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 21 | NR1L-PowerManagement-271 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 2. $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) (DR-PW26) |
| 21 | NR1L-PowerManagement-271 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 21 | NR1L-PowerManagement-271 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 3. Hold for the $BCM_FD_27.Comfort_Enable_Time$ value with no phone call active |
| 21 | NR1L-PowerManagement-271 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 21 | NR1L-PowerManagement-271 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 3. The $BCM_FD_27.Comfort_Enable_Time$ value elapses with no phone call active |
| 24 | NR1L-PowerManagement-273 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 24 | NR1L-PowerManagement-273 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 8. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 26 | NR1L-PowerManagement-275 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 26 | NR1L-PowerManagement-275 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 8. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 28 | NR1L-PowerManagement-277 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 5. Check whether $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates |
| 29 | NR1L-PowerManagement-281 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 6  |
| 30 | NR1L-PowerManagement-278 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 32 | NR1L-PowerManagement-280 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 33 | NR1L-PowerManagement-043 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4  |
| 34 | NR1L-PowerManagement-044 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 35 | NR1L-PowerManagement-045 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 36 | NR1L-PowerManagement-046 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 37 | NR1L-PowerManagement-047 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3  |
| 38 | NR1L-PowerManagement-048 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4  |
| 39 | NR1L-PowerManagement-049 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Apply ENTER_FULL_OPERATION and read the signal $STATUS_TELEMATIC.PowerSts_Tel |
| 39 | NR1L-PowerManagement-049 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it equal |
| 39 | NR1L-PowerManagement-049 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ equals State_before |
| 39 | NR1L-PowerManagement-049 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ equals State_before |
| 40 | NR1L-PowerManagement-050 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the bus trace and check that the first $STATUS_TELEMATIC$ frame transmit |
| 40 | NR1L-PowerManagement-050 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. The first $STATUS_TELEMATIC$ frame after the reconnection carries $STATUS_TEL |
| 41 | NR1L-PowerManagement-051 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM2.RemStActvSts =' | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 41 | NR1L-PowerManagement-051 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 41 | NR1L-PowerManagement-051 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 42 | NR1L-PowerManagement-052 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM2.RemStActvSts =' | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 42 | NR1L-PowerManagement-052 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 42 | NR1L-PowerManagement-052 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 43 | NR1L-PowerManagement-053 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM2.RemStActvSts =' | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 43 | NR1L-PowerManagement-053 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 43 | NR1L-PowerManagement-053 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 44 | NR1L-PowerManagement-054 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM2.RemStActvSts =' | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 44 | NR1L-PowerManagement-054 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 44 | NR1L-PowerManagement-054 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 45 | NR1L-PowerManagement-055 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7  |
| 47 | NR1L-PowerManagement-057 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) |
| 47 | NR1L-PowerManagement-057 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM2.RemStActvSts$' | 3. $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) |
| 47 | NR1L-PowerManagement-057 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 47 | NR1L-PowerManagement-057 | test_item(括號下半) | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | (read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby) |
| 49 | NR1L-PowerManagement-059 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = the value under test (D |
| 49 | NR1L-PowerManagement-059 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 49 | NR1L-PowerManagement-059 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ is received without a bu |
| 50 | NR1L-PowerManagement-060 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = the value under test (D |
| 50 | NR1L-PowerManagement-060 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 50 | NR1L-PowerManagement-060 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ is received without a bu |
| 51 | NR1L-PowerManagement-061 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send CAN: STATUS_BH_BCM1.DriverDoorSts = 1 (Open) and send the signal $STATUS |
| 51 | NR1L-PowerManagement-061 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 52 | NR1L-PowerManagement-062 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = the value under test (D |
| 52 | NR1L-PowerManagement-062 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 52 | NR1L-PowerManagement-062 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ is received without a bu |
| 53 | NR1L-PowerManagement-063 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = the value under test (D |
| 53 | NR1L-PowerManagement-063 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 53 | NR1L-PowerManagement-063 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ is received without a bu |
| 54 | NR1L-PowerManagement-064 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = the value under test (D |
| 54 | NR1L-PowerManagement-064 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 54 | NR1L-PowerManagement-064 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ is received without a bu |
| 55 | NR1L-PowerManagement-065 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) |
| 55 | NR1L-PowerManagement-065 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM2.RemStActvSts$' | 3. $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) |
| 55 | NR1L-PowerManagement-065 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 55 | NR1L-PowerManagement-065 | test_item(括號下半) | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | (read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby) |
| 56 | NR1L-PowerManagement-066 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 57 | NR1L-PowerManagement-067 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 57 | NR1L-PowerManagement-067 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 57 | NR1L-PowerManagement-067 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 58 | NR1L-PowerManagement-068 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 59 | NR1L-PowerManagement-069 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 59 | NR1L-PowerManagement-069 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 59 | NR1L-PowerManagement-069 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 62 | NR1L-PowerManagement-072 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 63 | NR1L-PowerManagement-073 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 64 | NR1L-PowerManagement-074 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 65 | NR1L-PowerManagement-075 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 66 | NR1L-PowerManagement-076 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 66 | NR1L-PowerManagement-076 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 66 | NR1L-PowerManagement-076 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 67 | NR1L-PowerManagement-077 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 67 | NR1L-PowerManagement-077 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 67 | NR1L-PowerManagement-077 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 68 | NR1L-PowerManagement-078 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 69 | NR1L-PowerManagement-079 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 70 | NR1L-PowerManagement-080 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 71 | NR1L-PowerManagement-081 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is st |
| 71 | NR1L-PowerManagement-081 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is still re |
| 72 | NR1L-PowerManagement-082 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 73 | NR1L-PowerManagement-083 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = a value other than 2 (I |
| 73 | NR1L-PowerManagement-083 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 74 | NR1L-PowerManagement-084 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = a value other than 2 (I |
| 76 | NR1L-PowerManagement-086 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 77 | NR1L-PowerManagement-087 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 78 | NR1L-PowerManagement-088 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 79 | NR1L-PowerManagement-089 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 79 | NR1L-PowerManagement-089 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 80 | NR1L-PowerManagement-090 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 81 | NR1L-PowerManagement-091 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 82 | NR1L-PowerManagement-092 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'CLIMATIC_PANEL.Radio_Btn0 from' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 82 | NR1L-PowerManagement-092 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" |
| 82 | NR1L-PowerManagement-092 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 83 | NR1L-PowerManagement-093 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 84 | NR1L-PowerManagement-094 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM1.PsngrDoorSts =' | 1. Send the signal STATUS_BH_BCM1.PsngrDoorSts = "Open" |
| 84 | NR1L-PowerManagement-094 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the signal STATUS_BH_BCM1.PsngrDoorSts = "Open" |
| 84 | NR1L-PowerManagement-094 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 85 | NR1L-PowerManagement-095 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 86 | NR1L-PowerManagement-096 | proc | 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'STATUS_BH_BCM1.DriverDoorSts =' | 1. Send the value STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 86 | NR1L-PowerManagement-096 | proc | Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)） | 1. Send the value STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 86 | NR1L-PowerManagement-096 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 89 | NR1L-PowerManagement-099 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 90 | NR1L-PowerManagement-100 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ a |
| 90 | NR1L-PowerManagement-100 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 90 | NR1L-PowerManagement-100 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. Hold for the PROXI Switch_Off_Time value |
| 90 | NR1L-PowerManagement-100 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI Swi |
| 90 | NR1L-PowerManagement-100 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 4. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI Swi |
| 91 | NR1L-PowerManagement-101 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ a |
| 91 | NR1L-PowerManagement-101 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 91 | NR1L-PowerManagement-101 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. Hold for the PROXI Switch_Off_Time value |
| 91 | NR1L-PowerManagement-101 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI Swi |
| 91 | NR1L-PowerManagement-101 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 4. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI Swi |
| 92 | NR1L-PowerManagement-102 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 93 | NR1L-PowerManagement-103 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ a |
| 93 | NR1L-PowerManagement-103 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Hold for the PROXI Switch_Off_Time value, then read the signal $STATUS_TELEMA |
| 93 | NR1L-PowerManagement-103 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. Hold for the PROXI Switch_Off_Time value, then read the signal $STATUS_TELEMA |
| 93 | NR1L-PowerManagement-103 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 3. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI Swi |
| 94 | NR1L-PowerManagement-104 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ a |
| 94 | NR1L-PowerManagement-104 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 3. Hold for the $BCM_FD_27.Comfort_Enable_Time$ (DR-PW26) value, then read the s |
| 94 | NR1L-PowerManagement-104 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Hold for the $BCM_FD_27.Comfort_Enable_Time$ (DR-PW26) value, then read the s |
| 94 | NR1L-PowerManagement-104 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 3. STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the $BCM_FD_2 |
| 97 | NR1L-PowerManagement-107 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 98 | NR1L-PowerManagement-108 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 99 | NR1L-PowerManagement-109 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 100 | NR1L-PowerManagement-110 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 102 | NR1L-PowerManagement-112 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 103 | NR1L-PowerManagement-113 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 104 | NR1L-PowerManagement-114 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 105 | NR1L-PowerManagement-115 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 106 | NR1L-PowerManagement-116 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM2.RemStActvSts$' | 3. $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active) |
| 106 | NR1L-PowerManagement-116 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7  |
| 106 | NR1L-PowerManagement-116 | test_item(括號下半) | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | (read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Partial Operati |
| 107 | NR1L-PowerManagement-117 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 109 | NR1L-PowerManagement-033 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 5. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 111 | NR1L-PowerManagement-035 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 113 | NR1L-PowerManagement-037 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 116 | NR1L-PowerManagement-040 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 119 | NR1L-PowerManagement-118 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Apply ENTER_FULL_OPERATION, send the signal $STATUS_BH_BCM1.OperationalModeSt |
| 119 | NR1L-PowerManagement-118 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and record the value as |
| 119 | NR1L-PowerManagement-118 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 5. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 119 | NR1L-PowerManagement-118 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ after the SNA value is |
| 119 | NR1L-PowerManagement-118 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 5. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ after the SNA value is |
| 120 | NR1L-PowerManagement-119 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 120 | NR1L-PowerManagement-119 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 120 | NR1L-PowerManagement-119 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 5. Hold for the PROXI Switch_Off_Time value |
| 120 | NR1L-PowerManagement-119 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 5. The PROXI Switch_Off_Time value elapses |
| 121 | NR1L-PowerManagement-120 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 121 | NR1L-PowerManagement-120 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 121 | NR1L-PowerManagement-120 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 5. Hold for the PROXI Switch_Off_Time value |
| 121 | NR1L-PowerManagement-120 | er | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 5. The PROXI Switch_Off_Time value elapses |
| 124 | NR1L-PowerManagement-123 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 126 | NR1L-PowerManagement-125 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. PENDING: DR-PW26 Sleep 態之觀察方法（CAN 睡眠後無法以 CAN 讀 $STATUS_TELEMATIC.PowerSts_Tel |
| 134 | NR1L-PowerManagement-133 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 135 | NR1L-PowerManagement-134 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 136 | NR1L-PowerManagement-135 | pre | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 2. The Rear_View_Camera PROXI parameter reads "Present" |
| 137 | NR1L-PowerManagement-136 | pre | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 2. The Rear_View_Camera PROXI parameter reads "Present" |
| 138 | NR1L-PowerManagement-137 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 139 | NR1L-PowerManagement-138 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 140 | NR1L-PowerManagement-139 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 141 | NR1L-PowerManagement-140 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 142 | NR1L-PowerManagement-141 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 143 | NR1L-PowerManagement-142 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 145 | NR1L-PowerManagement-144 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 146 | NR1L-PowerManagement-145 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 147 | NR1L-PowerManagement-146 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 148 | NR1L-PowerManagement-147 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 157 | NR1L-PowerManagement-017 | pre | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 2. The PROXI parameter "Switch_Off_Time" is at 20 minutes |
| 158 | NR1L-PowerManagement-018 | pre | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 2. The PROXI parameter "Switch_Off_Time" is at 60 minutes |
| 159 | NR1L-PowerManagement-019 | pre | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 2. The PROXI parameter "Switch_Off_Time" is at 180 minutes |
| 161 | NR1L-PowerManagement-157 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 170 | NR1L-PowerManagement-027 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 7. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 173 | NR1L-PowerManagement-030 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 174 | NR1L-PowerManagement-031 | pre | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 3. $BCM_FD_27.Comfort_Enable_Time$ is at a value other than 0 (DR-PW26) |
| 174 | NR1L-PowerManagement-031 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 1. Place a second bluetooth call from the paired phone while $BCM_FD_27.Comfort_ |
| 174 | NR1L-PowerManagement-031 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 174 | NR1L-PowerManagement-031 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Time$' | 1. The second bluetooth call reaches the HU before $BCM_FD_27.Comfort_Enable_Tim |
| 175 | NR1L-PowerManagement-159 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Check that the call audio is present on the HU speakers, and read the signal  |
| 176 | NR1L-PowerManagement-160 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Check that the call audio is present on the HU speakers, and read the signal  |
| 177 | NR1L-PowerManagement-161 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Check that the call audio is present on the HU speakers, and read the signal  |
| 178 | NR1L-PowerManagement-162 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 179 | NR1L-PowerManagement-163 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 180 | NR1L-PowerManagement-164 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 186 | NR1L-PowerManagement-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Start the TLM boot sequence and send each ignition value listed in Input Test |
| 186 | NR1L-PowerManagement-005 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it corre |
| 186 | NR1L-PowerManagement-005 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ corresponds to the las |
| 187 | NR1L-PowerManagement-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Actv$' | 1. Set the TLM volume level to the starting value $STATUS_LIN.PN14_LS_Actv$ = 1  |
| 187 | NR1L-PowerManagement-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Lvl7$' | 2. $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active) |
| 187 | NR1L-PowerManagement-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Actv$' | 4. Send the two Load Shed signals $STATUS_LIN.PN14_LS_Actv$ = 1 (Active) |
| 187 | NR1L-PowerManagement-006 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Lvl7$' | 5. $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active) |
| 189 | NR1L-PowerManagement-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 1. Set the TLM volume level to the starting value $STATUS_LIN.Batt_ST_Crit$ = 1  |
| 189 | NR1L-PowerManagement-008 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 3. Send the Battery Critical signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) |
| 190 | NR1L-PowerManagement-009 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 1. Send the recovery signal $STATUS_LIN.Batt_ST_Crit$ = 0 (False) |
| 191 | NR1L-PowerManagement-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Actv$' | 2. Resume the broadcast with the recovery values $STATUS_LIN.PN14_LS_Actv$ = 0 ( |
| 191 | NR1L-PowerManagement-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Lvl7$' | 3. $STATUS_LIN.PN14_LS_Lvl7$ = 0 (Not_Active) |
| 191 | NR1L-PowerManagement-010 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_13.AUD_LVL$' | 4. Read the signal $TELEMATIC_FD_13.AUD_LVL$ and check that it is the expected l |
| 194 | NR1L-PowerManagement-013 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 1. Set the TLM volume level to the starting value $STATUS_LIN.Batt_ST_Crit$ = 1  |
| 194 | NR1L-PowerManagement-013 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 3. Send the Battery Critical signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) |
| 195 | NR1L-PowerManagement-014 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 1. Keep the Battery Critical signal at the value $STATUS_LIN.Batt_ST_Crit$ = 1 ( |
| 195 | NR1L-PowerManagement-014 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_13.AUD_LVL$' | 3. Read the signal $TELEMATIC_FD_13.AUD_LVL$ and check that it is the expected l |
| 196 | NR1L-PowerManagement-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Actv$' | 1. Set the TLM volume level to the starting value $STATUS_LIN.PN14_LS_Actv$ = 1  |
| 196 | NR1L-PowerManagement-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Lvl7$' | 2. $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active) |
| 196 | NR1L-PowerManagement-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Actv$' | 4. Send the two Load Shed signals $STATUS_LIN.PN14_LS_Actv$ = 1 (Active) |
| 196 | NR1L-PowerManagement-015 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.PN14_LS_Lvl7$' | 5. $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active) |
| 197 | NR1L-PowerManagement-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 1. Set the TLM volume level to the starting value $STATUS_LIN.Batt_ST_Crit$ = 1  |
| 197 | NR1L-PowerManagement-016 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_LIN.Batt_ST_Crit$' | 3. Send the Battery Critical signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) |
| 198 | NR1L-PowerManagement-166 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 199 | NR1L-PowerManagement-167 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 200 | NR1L-PowerManagement-168 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 201 | NR1L-PowerManagement-169 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 202 | NR1L-PowerManagement-170 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 203 | NR1L-PowerManagement-171 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 204 | NR1L-PowerManagement-284 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 205 | NR1L-PowerManagement-285 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Act$' | 2. Apply ENTER_TIMED with $BCM_FD_27.Comfort_Enable_Act$ = 1 (DR-PW26) |
| 205 | NR1L-PowerManagement-285 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 5. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1  |
| 205 | NR1L-PowerManagement-285 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$BCM_FD_27.Comfort_Enable_Act$' | 4. The signal value $BCM_FD_27.Comfort_Enable_Act$ = 0 is received |
| 212 | NR1L-PowerManagement-231 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B4.Radio_Theme$' | 2. Read the signal $RADIO_B4.Radio_Theme$ and check its value |
| 213 | NR1L-PowerManagement-232 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B4.Radio_Theme$' | 2. Read the signal $RADIO_B4.Radio_Theme$ and check its value |
| 223 | NR1L-PowerManagement-242 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 1. Apply the configuration: PROXI Car_Shape_Configuration and PROXI Number_of_Do |
| 225 | NR1L-PowerManagement-244 | proc | PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式 | 1. Send the configuration VC_VEH_LINE with the $Car_Shape_Configuration$ and $Nu |
| 227 | NR1L-PowerManagement-246 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B4.Radio_Theme$' | 2. Read the signal $RADIO_B4.Radio_Theme$ and check its value |
| 228 | NR1L-PowerManagement-247 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$RADIO_B4.Radio_Theme$' | 2. Read the signal $RADIO_B4.Radio_Theme$ and check its value |
| 243 | NR1L-PowerManagement-179 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4  |
| 244 | NR1L-PowerManagement-180 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2  |
| 249 | NR1L-PowerManagement-184 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and record the value as |
| 249 | NR1L-PowerManagement-184 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 2. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = a value other than 15 ( |
| 249 | NR1L-PowerManagement-184 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |
| 273 | NR1L-PowerManagement-202 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3  |
| 273 | NR1L-PowerManagement-202 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_STAT$' | 5. Check that $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) and that $TELEMATIC_FD |
| 273 | NR1L-PowerManagement-202 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_X_COORD$' | 5. Check that $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) and that $TELEMATIC_FD |
| 273 | NR1L-PowerManagement-202 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_Y_COORD$' | 5. Check that $TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) and that $TELEMATIC_FD |
| 273 | NR1L-PowerManagement-202 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_X_COORD$' | 4. TELEMATIC_FD_5.CM_TCH_STAT = 1 (TCH_PSD) is sent together with the touch coor |
| 273 | NR1L-PowerManagement-202 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_Y_COORD$' | 4. TELEMATIC_FD_5.CM_TCH_STAT = 1 (TCH_PSD) is sent together with the touch coor |
| 273 | NR1L-PowerManagement-202 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_X_COORD$' | 5. TELEMATIC_FD_5.CM_TCH_STAT = 1 (TCH_PSD) is sent together with the touch coor |
| 273 | NR1L-PowerManagement-202 | er | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$TELEMATIC_FD_5.CM_TCH_Y_COORD$' | 5. TELEMATIC_FD_5.CM_TCH_STAT = 1 (TCH_PSD) is sent together with the touch coor |
| 289 | NR1L-PowerManagement-218 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_BH_BCM1.OperationalModeSts$' | 1. Repeat the ignition cycle listed in Input Test Data 31 times, sending $STATUS |
| 296 | NR1L-PowerManagement-225 | proc | v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$STATUS_TELEMATIC.PowerSts_Telematic$' | 2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is th |

### Q — 不可見字元（NBSP／全形空格／行尾空白）（行計 186／列計 175）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 13 | NR1L-PowerManagement-263 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 14 | NR1L-PowerManagement-264 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 17 | NR1L-PowerManagement-267 | test_item | NBSP | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". Th |
| 25 | NR1L-PowerManagement-274 | test_item | NBSP | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value. |
| 27 | NR1L-PowerManagement-276 | test_item | NBSP | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value. |
| 30 | NR1L-PowerManagement-278 | test_item | NBSP | First default values for TLM are: TLM_Status.Info, $Telematic_Power$ equal to "S |
| 32 | NR1L-PowerManagement-280 | test_item | NBSP | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 35 | NR1L-PowerManagement-045 | test_item | NBSP | If the Carplay device requests audio control and does not request video control, |
| 36 | NR1L-PowerManagement-046 | test_item | NBSP | If the Carplay device does not request audio control and does request video cont |
| 39 | NR1L-PowerManagement-049 | test_item | NBSP | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 40 | NR1L-PowerManagement-050 | test_item | NBSP | Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $ |
| 41 | NR1L-PowerManagement-051 | test_item | NBSP | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". Th |
| 42 | NR1L-PowerManagement-052 | test_item | NBSP | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". Th |
| 43 | NR1L-PowerManagement-053 | test_item | NBSP | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". Th |
| 44 | NR1L-PowerManagement-054 | test_item | NBSP | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". Th |
| 47 | NR1L-PowerManagement-057 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 48 | NR1L-PowerManagement-058 | test_item | NBSP | If Phone_Call.Info == Active, at LTM_OperationalModeSts.Info transition TLM sets |
| 49 | NR1L-PowerManagement-059 | test_item | NBSP | If Phone_Call.Info == Not_Active, at LTM_OperationalModeSts.Info transition TLM  |
| 50 | NR1L-PowerManagement-060 | test_item | NBSP | If Phone_Call.Info == Active, at LTM_OperationalModeSts.Info transition TLM sets |
| 51 | NR1L-PowerManagement-061 | test_item | NBSP | IF Brand_Configuration _2 == "Jeep" AND STATUS_BH_BCM1.DriverDoorSts == "Open" A |
| 52 | NR1L-PowerManagement-062 | test_item | NBSP | ELSE at LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Te |
| 53 | NR1L-PowerManagement-063 | test_item | NBSP | Behaviour 2: "SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN" or ( If Auto_ |
| 54 | NR1L-PowerManagement-064 | test_item | NBSP | Behaviour 1: "SwitchOff_Timeout_Setting.Req == Timeout1 == 00 MIN" or ( If Auto_ |
| 55 | NR1L-PowerManagement-065 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 56 | NR1L-PowerManagement-066 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Pan |
| 57 | NR1L-PowerManagement-067 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_ |
| 58 | NR1L-PowerManagement-068 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Pan |
| 59 | NR1L-PowerManagement-069 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_ |
| 60 | NR1L-PowerManagement-070 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI parameter  |
| 61 | NR1L-PowerManagement-071 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI parameter  |
| 62 | NR1L-PowerManagement-072 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal LTM_OperationalMode |
| 63 | NR1L-PowerManagement-073 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal LTM_OperationalMode |
| 65 | NR1L-PowerManagement-075 | test_item | NBSP | TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo vi |
| 67 | NR1L-PowerManagement-077 | test_item | NBSP | TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo vi |
| 68 | NR1L-PowerManagement-078 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info has |
| 69 | NR1L-PowerManagement-079 | test_item | NBSP | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 70 | NR1L-PowerManagement-080 | test_item | NBSP | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 71 | NR1L-PowerManagement-081 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_View |
| 72 | NR1L-PowerManagement-082 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation” \|\| “Idle”AND signal |
| 73 | NR1L-PowerManagement-083 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal LTM_OperationalMod |
| 74 | NR1L-PowerManagement-084 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND STATUS_BH_BCM2.RemStActvS |
| 83 | NR1L-PowerManagement-093 | test_item | NBSP | IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Inf |
| 86 | NR1L-PowerManagement-096 | test_item | NBSP | IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Inf |
| 87 | NR1L-PowerManagement-097 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 88 | NR1L-PowerManagement-098 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 89 | NR1L-PowerManagement-099 | test_item | NBSP | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it |
| 90 | NR1L-PowerManagement-100 | test_item | NBSP | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 91 | NR1L-PowerManagement-101 | test_item | NBSP | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 92 | NR1L-PowerManagement-102 | test_item | NBSP | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it |
| 93 | NR1L-PowerManagement-103 | test_item | NBSP | IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the v |
| 94 | NR1L-PowerManagement-104 | test_item | NBSP | IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the  |
| 97 | NR1L-PowerManagement-107 | test_item | NBSP | IF Rear_View_Camera PROXI parameter == "Present", according to the value of Rear |
| 98 | NR1L-PowerManagement-108 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND STATUS_BH_BC |
| 101 | NR1L-PowerManagement-111 | test_item | NBSP | THEN TLM has to set signal Antitheft_Activation.Req to "True" value. AND TLM has |
| 102 | NR1L-PowerManagement-112 | test_item | NBSP | Behaviour 1: "Auto_SwitchOn_Setting.Req == Active":TLM has to show a proper Spla |
| 103 | NR1L-PowerManagement-113 | test_item | NBSP | Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":TLM has to set VPLastSta |
| 104 | NR1L-PowerManagement-114 | test_item | NBSP | Behaviour 1: "Auto_SwitchOn_Setting.Req == Active":TLM has to show a proper Spla |
| 105 | NR1L-PowerManagement-115 | test_item | NBSP | Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":TLM has to set VPLastSta |
| 106 | NR1L-PowerManagement-116 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal STATUS_BH_BCM2.Rem |
| 107 | NR1L-PowerManagement-117 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Timed" AND PhoneCall.Info becames " |
| 108 | NR1L-PowerManagement-032 | test_item | NBSP | IF RemStartFail = ”True” TLM has to stop its active functionality (Media audio s |
| 110 | NR1L-PowerManagement-034 | test_item | NBSP | Case 2:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info is still "Active" at "Tim |
| 111 | NR1L-PowerManagement-035 | test_item | NBSP | WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration, TL |
| 112 | NR1L-PowerManagement-036 | test_item | NBSP | WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration, TL |
| 113 | NR1L-PowerManagement-037 | test_item | NBSP | Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeou |
| 114 | NR1L-PowerManagement-038 | test_item | NBSP | Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeou |
| 116 | NR1L-PowerManagement-040 | test_item | NBSP | WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration, TL |
| 117 | NR1L-PowerManagement-041 | test_item | NBSP | Case 2:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info is still "Active" at "Tim |
| 119 | NR1L-PowerManagement-118 | test_item | NBSP | IF TLM receives signal LTM_OperationalModeSts.Info equal to "SNA" value  THEN TL |
| 120 | NR1L-PowerManagement-119 | test_item | NBSP | IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.R |
| 121 | NR1L-PowerManagement-120 | test_item | NBSP | IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting.R |
| 130 | NR1L-PowerManagement-129 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 131 | NR1L-PowerManagement-130 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 132 | NR1L-PowerManagement-131 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 133 | NR1L-PowerManagement-132 | test_item | NBSP | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 134 | NR1L-PowerManagement-133 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 135 | NR1L-PowerManagement-134 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 136 | NR1L-PowerManagement-135 | test_item | NBSP | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info ==  |
| 137 | NR1L-PowerManagement-136 | test_item | NBSP | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info ==  |
| 138 | NR1L-PowerManagement-137 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 139 | NR1L-PowerManagement-138 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 140 | NR1L-PowerManagement-139 | test_item | NBSP | Behaviour 1: "Auto_SwitchOn_Setting.Req == Active"After the LTM_OperationalModeS |
| 141 | NR1L-PowerManagement-140 | test_item | NBSP | Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":         After the LTM_O |
| 142 | NR1L-PowerManagement-141 | test_item | NBSP | Behaviour 1: "Auto_SwitchOn_Setting.Req == Active"After the LTM_OperationalModeS |
| 143 | NR1L-PowerManagement-142 | test_item | NBSP | Behaviour 3: "Auto_SwitchOn_Setting.Req  == Recall_Last":IF VPLastStatus == ON t |
| 144 | NR1L-PowerManagement-143 | test_item | NBSP | Default:         The ex-factory default must be "Auto_SwitchOn_Setting.Req == Re |
| 145 | NR1L-PowerManagement-144 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Ac |
| 146 | NR1L-PowerManagement-145 | test_item | NBSP | ELSE TLM sets VPLastStatus to "Off" value and sets TLM_Status.Info and $Telemati |
| 147 | NR1L-PowerManagement-146 | test_item | NBSP | IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activati |
| 148 | NR1L-PowerManagement-147 | test_item | NBSP | IF Antitheft_Result.Info == "Not_Successfully"THEN TLM has to set Antitheft_Acti |
| 149 | NR1L-PowerManagement-148 | test_item | NBSP | TLM has to read Brand_Configuration_2 PROXI parameter in order to show the vehic |
| 150 | NR1L-PowerManagement-149 | test_item | NBSP | - IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has  |
| 151 | NR1L-PowerManagement-150 | test_item | NBSP | - IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM h |
| 152 | NR1L-PowerManagement-151 | test_item | NBSP | - IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has |
| 154 | NR1L-PowerManagement-153 | test_item | NBSP | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch S |
| 155 | NR1L-PowerManagement-154 | test_item | NBSP | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch S |
| 157 | NR1L-PowerManagement-017 | test_item | NBSP | IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can selec |
| 158 | NR1L-PowerManagement-018 | test_item | NBSP | IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can selec |
| 159 | NR1L-PowerManagement-019 | test_item | NBSP | IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can selec |
| 160 | NR1L-PowerManagement-156 | test_item | NBSP | Default:The ex-factory default must be "SwitchOff_Timeout_Setting.Req == 00 MIN" |
| 163 | NR1L-PowerManagement-020 | test_item | NBSP | For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.R |
| 164 | NR1L-PowerManagement-021 | test_item | NBSP | For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.R |
| 171 | NR1L-PowerManagement-028 | test_item | NBSP | MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Ph |
| 172 | NR1L-PowerManagement-029 | test_item | NBSP | MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Ph |
| 181 | NR1L-PowerManagement-165 | test_item | NBSP | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, |
| 182 | NR1L-PowerManagement-001 | test_item | NBSP | After StandardScreen_Time the standard screen is visualized on TLM screen |
| 183 | NR1L-PowerManagement-002 | test_item | NBSP | After StandardScreen_Time the standard screen is visualized on TLM screen |
| 184 | NR1L-PowerManagement-003 | test_item | NBSP | After StandardScreen_Time the standard screen is visualized on TLM screen |
| 185 | NR1L-PowerManagement-004 | test_item | NBSP | After StandardScreen_Time the standard screen is visualized on TLM screen |
| 187 | NR1L-PowerManagement-006 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 187 | NR1L-PowerManagement-006 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 188 | NR1L-PowerManagement-007 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 188 | NR1L-PowerManagement-007 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 189 | NR1L-PowerManagement-008 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 189 | NR1L-PowerManagement-008 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 190 | NR1L-PowerManagement-009 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 190 | NR1L-PowerManagement-009 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 191 | NR1L-PowerManagement-010 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 191 | NR1L-PowerManagement-010 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 192 | NR1L-PowerManagement-011 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 192 | NR1L-PowerManagement-011 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 193 | NR1L-PowerManagement-012 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 193 | NR1L-PowerManagement-012 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 194 | NR1L-PowerManagement-013 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 194 | NR1L-PowerManagement-013 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 195 | NR1L-PowerManagement-014 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 195 | NR1L-PowerManagement-014 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 196 | NR1L-PowerManagement-015 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 196 | NR1L-PowerManagement-015 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 197 | NR1L-PowerManagement-016 | test_item | NBSP | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are  |
| 197 | NR1L-PowerManagement-016 | test_item | NBSP | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr |
| 201 | NR1L-PowerManagement-169 | test_item | NBSP | If the HU Transitions to Timed mode due to the condition described in CFTS009-18 |
| 202 | NR1L-PowerManagement-170 | test_item | NBSP | If the HU Transitions to Timed mode due to the condition described in CFTS009-18 |
| 203 | NR1L-PowerManagement-171 | test_item | NBSP | If the HU Transitions to Timed mode due to the condition described in CFTS009-18 |
| 204 | NR1L-PowerManagement-284 | test_item | NBSP | If the HU Transitions to Timed mode due to the condition described in CFTS009-18 |
| 205 | NR1L-PowerManagement-285 | test_item | NBSP | If the HU Transitions to Timed mode due to the condition described in CFTS009-18 |
| 208 | NR1L-PowerManagement-227 | test_item | NBSP | $VC_SpecialPKG$ shall be used to determine which theme will be used by the HU. S |
| 209 | NR1L-PowerManagement-228 | test_item | NBSP | If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU |
| 210 | NR1L-PowerManagement-229 | test_item | NBSP | If $VC_SpecialPKG$ = [none] or indicates a value that is not supported by the HU |
| 214 | NR1L-PowerManagement-233 | test_item | NBSP | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid  |
| 215 | NR1L-PowerManagement-234 | test_item | NBSP | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid  |
| 216 | NR1L-PowerManagement-235 | test_item | NBSP | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid  |
| 217 | NR1L-PowerManagement-236 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 218 | NR1L-PowerManagement-237 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 219 | NR1L-PowerManagement-238 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 220 | NR1L-PowerManagement-239 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 221 | NR1L-PowerManagement-240 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 222 | NR1L-PowerManagement-241 | test_item | NBSP | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 223 | NR1L-PowerManagement-242 | test_item | NBSP | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 224 | NR1L-PowerManagement-243 | test_item | NBSP | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 225 | NR1L-PowerManagement-244 | test_item | NBSP | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 226 | NR1L-PowerManagement-245 | test_item | NBSP | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 229 | NR1L-PowerManagement-248 | test_item | NBSP | If $VC_VEH_LINE$ = [M240] The HU Shall use the M240 seat graphics.  If $VC_VEH_L |
| 230 | NR1L-PowerManagement-249 | test_item | NBSP | If $VC_VEH_LINE$ = [M240] The HU Shall use the M240 seat graphics.  If $VC_VEH_L |
| 231 | NR1L-PowerManagement-286 | test_item | NBSP | If $VC_VEH_LINE$ = [M240] The HU Shall use the M240 seat graphics.  If $VC_VEH_L |
| 232 | NR1L-PowerManagement-250 | test_item | NBSP | The HU shall use the $VC_VEH_LINE$ signal to determine the correct performance g |
| 238 | NR1L-PowerManagement-174 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 239 | NR1L-PowerManagement-175 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 240 | NR1L-PowerManagement-176 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 241 | NR1L-PowerManagement-177 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 242 | NR1L-PowerManagement-178 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 243 | NR1L-PowerManagement-179 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 244 | NR1L-PowerManagement-180 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 245 | NR1L-PowerManagement-181 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 246 | NR1L-PowerManagement-182 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 247 | NR1L-PowerManagement-287 | test_item | NBSP | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 249 | NR1L-PowerManagement-184 | test_item | NBSP | As soon as signal LTM_OperationalModeSts.Info becomes different from "SNA" value |
| 263 | NR1L-PowerManagement-192 | test_item | NBSP | - IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM has  |
| 264 | NR1L-PowerManagement-193 | test_item | NBSP | - IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM h |
| 265 | NR1L-PowerManagement-194 | test_item | NBSP | - IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM has |
| 267 | NR1L-PowerManagement-196 | test_item | NBSP | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch S |
| 268 | NR1L-PowerManagement-197 | test_item | NBSP | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch S |
| 269 | NR1L-PowerManagement-198 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 270 | NR1L-PowerManagement-199 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 271 | NR1L-PowerManagement-200 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 272 | NR1L-PowerManagement-201 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 273 | NR1L-PowerManagement-202 | test_item | NBSP | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen v |
| 287 | NR1L-PowerManagement-216 | test_item | NBSP | For all variations of the disclaimer screen and geolocation pop up listed below, |
| 288 | NR1L-PowerManagement-217 | test_item | NBSP | For all variations of the disclaimer screen and geolocation pop up listed below, |
| 290 | NR1L-PowerManagement-219 | test_item | NBSP | If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present]  AND $Country_Code |
| 291 | NR1L-PowerManagement-220 | test_item | NBSP | If  $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR $Country_ |
| 292 | NR1L-PowerManagement-221 | test_item | NBSP | If  $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR $Country_ |
| 293 | NR1L-PowerManagement-222 | test_item | NBSP | For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Pre |
| 294 | NR1L-PowerManagement-223 | test_item | NBSP | For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Pre |
| 295 | NR1L-PowerManagement-224 | test_item | NBSP | For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Pres |
| 297 | NR1L-PowerManagement-226 | test_item | NBSP | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone call, |

### R — Pre-Condition 版面（未編號行／多條件並列）（行計 30／列計 28）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 11 | NR1L-PowerManagement-262 | pre | 未編號行 | The TLM is in Full-Operation |
| 29 | NR1L-PowerManagement-281 | pre | 未編號行 | The ignition working condition is Ignition Off |
| 29 | NR1L-PowerManagement-281 | pre | 未編號行 | The Engineering Line is activated |
| 29 | NR1L-PowerManagement-281 | pre | 未編號行 | TLM_Status.Info reads "Bench" |
| 58 | NR1L-PowerManagement-068 | pre | 多條件並列於同一行 | 4. Rear_View_Camera reads "Present" and the Rear Camera is not active |
| 59 | NR1L-PowerManagement-069 | pre | 多條件並列於同一行 | 4. Rear_View_Camera reads "Present" and the Rear Camera is not active |
| 61 | NR1L-PowerManagement-071 | pre | 多條件並列於同一行 | 3. Rear_View_Camera reads "Present" and the Rear Camera is active |
| 83 | NR1L-PowerManagement-093 | pre | 多條件並列於同一行 | 3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable" |
| 84 | NR1L-PowerManagement-094 | pre | 多條件並列於同一行 | 3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable" |
| 85 | NR1L-PowerManagement-095 | pre | 多條件並列於同一行 | 3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable" |
| 86 | NR1L-PowerManagement-096 | pre | 多條件並列於同一行 | 3. Brand_Configuration_2 reads a value other than "Jeep" and SWITCH_OFF_DOOR rea |
| 91 | NR1L-PowerManagement-101 | pre | 多條件並列於同一行 | 3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN" |
| 208 | NR1L-PowerManagement-227 | pre | 未編號行 | (DR-PW28) |
| 213 | NR1L-PowerManagement-232 | pre | 未編號行 | (DR-PW28) |
| 220 | NR1L-PowerManagement-239 | pre | 未編號行 | (DR-PW28) |
| 221 | NR1L-PowerManagement-240 | pre | 未編號行 | (DR-PW28) |
| 222 | NR1L-PowerManagement-241 | pre | 未編號行 | (DR-PW28) |
| 225 | NR1L-PowerManagement-244 | pre | 未編號行 | (DR-PW28) |
| 226 | NR1L-PowerManagement-245 | pre | 未編號行 | (DR-PW28) |
| 228 | NR1L-PowerManagement-247 | pre | 未編號行 | (DR-PW28) |
| 229 | NR1L-PowerManagement-248 | pre | 未編號行 | (DR-PW28) |
| 245 | NR1L-PowerManagement-181 | pre | 未編號行 | (DR-PW28) |
| 259 | NR1L-PowerManagement-188 | pre | 未編號行 | (DR-PW28) |
| 260 | NR1L-PowerManagement-189 | pre | 未編號行 | (DR-PW28) |
| 261 | NR1L-PowerManagement-190 | pre | 未編號行 | (DR-PW28) |
| 267 | NR1L-PowerManagement-196 | pre | 未編號行 | (DR-PW28) |
| 268 | NR1L-PowerManagement-197 | pre | 未編號行 | (DR-PW28) |
| 290 | NR1L-PowerManagement-219 | pre | 未編號行 | (DR-PW28) |
| 291 | NR1L-PowerManagement-220 | pre | 未編號行 | (DR-PW28) |
| 292 | NR1L-PowerManagement-221 | pre | 未編號行 | (DR-PW28) |

### T — PENDING 說明非英文（行計 111／列計 68）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 18 | NR1L-PowerManagement-268 | proc | PENDING 說明含非 ASCII 字元 ['之', '刺', '激'] | 2. PENDING: DR-PW29 ANC 之刺激與觀察面 |
| 18 | NR1L-PowerManagement-268 | proc | PENDING 說明含非 ASCII 字元 ['之', '刺', '激'] | 3. PENDING: DR-PW29 ACN 之刺激與觀察面 |
| 29 | NR1L-PowerManagement-281 | proc | PENDING 說明含非 ASCII 字元 ['之', '位', '準'] | 4. PENDING: DR-PW27 BoosterOUT / analog and digital antenna supply 之 ON 位準值 |
| 29 | NR1L-PowerManagement-281 | er | PENDING 說明含非 ASCII 字元 ['位', '準', '值'] | 4. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值 |
| 29 | NR1L-PowerManagement-281 | er | PENDING 說明含非 ASCII 字元 ['位', '準', '值'] | 5. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值 |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 5. PENDING: DR-PW25 Auto_SwitchOn_Setting.Req 之設定項名 |
| 31 | NR1L-PowerManagement-279 | proc | PENDING 說明含非 ASCII 字元 ['觀', '察', '量'] | 2. PENDING: DR-PW26 INIT 觀察量 |
| 39 | NR1L-PowerManagement-049 | proc | PENDING 說明含非 ASCII 字元 ['與', '之', '設'] | 5. PENDING: DR-PW25 SwitchOffSetting.Req 與 Auto_SwitchOn_Setting.Req 之設定項名與讀取方法 |
| 45 | NR1L-PowerManagement-055 | er | PENDING 說明含非 ASCII 字元 ['位', '準', '值'] | c. PENDING: DR-PW27 BoosterOUT OFF / antenna supply ON 位準值 |
| 71 | NR1L-PowerManagement-081 | proc | PENDING 說明含非 ASCII 字元 ['之', '驅', '動'] | 1. PENDING: DR-PW23 Rear_Camera_Enable.Info 之驅動方法（自 "False" 轉 "True"） |
| 90 | NR1L-PowerManagement-100 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 90 | NR1L-PowerManagement-100 | proc | PENDING 說明含非 ASCII 字元 ['之', '觀', '察'] | 5. PENDING: DR-PW23 Antitheft_Result.Info 之觀察方法（antitheft 成功） |
| 91 | NR1L-PowerManagement-101 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 91 | NR1L-PowerManagement-101 | proc | PENDING 說明含非 ASCII 字元 ['之', '觀', '察'] | 5. PENDING: DR-PW23 Antitheft_Result.Info 之觀察方法（antitheft 成功） |
| 93 | NR1L-PowerManagement-103 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 94 | NR1L-PowerManagement-104 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 95 | NR1L-PowerManagement-105 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 3. PENDING: DR-PW30 Response_Wait_Time 之值 |
| 95 | NR1L-PowerManagement-105 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 96 | NR1L-PowerManagement-106 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 3. PENDING: DR-PW30 Response_Wait_Time 之值 |
| 96 | NR1L-PowerManagement-106 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 101 | NR1L-PowerManagement-111 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 101 | NR1L-PowerManagement-111 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 104 | NR1L-PowerManagement-114 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 107 | NR1L-PowerManagement-117 | proc | PENDING 說明含非 ASCII 字元 ['之', '驅', '動'] | 1. PENDING: DR-PW23 PhoneCall.Info 之驅動方法（使其轉為 "not Active"） |
| 107 | NR1L-PowerManagement-117 | proc | PENDING 說明含非 ASCII 字元 ['之', '觀', '察'] | 3. PENDING: DR-PW23 RemStartFail 之觀察方法 |
| 120 | NR1L-PowerManagement-119 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法 |
| 121 | NR1L-PowerManagement-120 | proc | PENDING 說明含非 ASCII 字元 ['之', '設', '定'] | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法 |
| 122 | NR1L-PowerManagement-121 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 2. PENDING: DR-PW27 TLM HMI documents —— 該態下應不可用之 vehicle setup 項目清單 |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 說明含非 ASCII 字元 ['觀', '察', '面'] | 2. PENDING: DR-PW26 Suspend-to-RAM 觀察面 |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 說明含非 ASCII 字元 ['對', '應', '之'] | 3. PENDING: DR-PW26 Suspend-to-RAM 對應之 PowerSts_Telematic 值 |
| 124 | NR1L-PowerManagement-123 | er | PENDING 說明含非 ASCII 字元 ['位', '準', '值'] | d. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值 |
| 126 | NR1L-PowerManagement-125 | proc | PENDING 說明含非 ASCII 字元 ['態', '之', '觀'] | 2. PENDING: DR-PW26 Sleep 態之觀察方法（CAN 睡眠後無法以 CAN 讀 $STATUS_TELEMATIC.PowerSts_Tel |
| 126 | NR1L-PowerManagement-125 | er | PENDING 說明含非 ASCII 字元 ['態', '之', '觀'] | 2. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 126 | NR1L-PowerManagement-125 | er | PENDING 說明含非 ASCII 字元 ['位', '準', '值'] | c. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值 |
| 130 | NR1L-PowerManagement-129 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 130 | NR1L-PowerManagement-129 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 131 | NR1L-PowerManagement-130 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 131 | NR1L-PowerManagement-130 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 132 | NR1L-PowerManagement-131 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 132 | NR1L-PowerManagement-131 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 133 | NR1L-PowerManagement-132 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 133 | NR1L-PowerManagement-132 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 134 | NR1L-PowerManagement-133 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 134 | NR1L-PowerManagement-133 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 135 | NR1L-PowerManagement-134 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 135 | NR1L-PowerManagement-134 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 138 | NR1L-PowerManagement-137 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 138 | NR1L-PowerManagement-137 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 138 | NR1L-PowerManagement-137 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 144 | NR1L-PowerManagement-143 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 144 | NR1L-PowerManagement-143 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 145 | NR1L-PowerManagement-144 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 145 | NR1L-PowerManagement-144 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 145 | NR1L-PowerManagement-144 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 148 | NR1L-PowerManagement-147 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 148 | NR1L-PowerManagement-147 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 148 | NR1L-PowerManagement-147 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 157 | NR1L-PowerManagement-017 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 157 | NR1L-PowerManagement-017 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 158 | NR1L-PowerManagement-018 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 158 | NR1L-PowerManagement-018 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 159 | NR1L-PowerManagement-019 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 159 | NR1L-PowerManagement-019 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 160 | NR1L-PowerManagement-156 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 160 | NR1L-PowerManagement-156 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 163 | NR1L-PowerManagement-020 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 163 | NR1L-PowerManagement-020 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 164 | NR1L-PowerManagement-021 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '選'] | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 164 | NR1L-PowerManagement-021 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '讀'] | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 182 | NR1L-PowerManagement-001 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 183 | NR1L-PowerManagement-002 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 184 | NR1L-PowerManagement-003 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 185 | NR1L-PowerManagement-004 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 185 | NR1L-PowerManagement-004 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 4. PENDING: DR-PW30 StandardScreen_Time 之值 |
| 190 | NR1L-PowerManagement-009 | proc | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 190 | NR1L-PowerManagement-009 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 191 | NR1L-PowerManagement-010 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 191 | NR1L-PowerManagement-010 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 5. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 201 | NR1L-PowerManagement-169 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '之'] | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 204 | NR1L-PowerManagement-284 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '之'] | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 205 | NR1L-PowerManagement-285 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '之'] | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 209 | NR1L-PowerManagement-228 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 210 | NR1L-PowerManagement-229 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 211 | NR1L-PowerManagement-230 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該元件之預設值與元件清單 |
| 213 | NR1L-PowerManagement-232 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 3. PENDING: DR-PW27 <Tsend> 之值 |
| 223 | NR1L-PowerManagement-242 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 224 | NR1L-PowerManagement-243 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 225 | NR1L-PowerManagement-244 | proc | PENDING 說明含非 ASCII 字元 ['指', '派'] | 2. PENDING: DR-PW27 seat graphic 指派 |
| 226 | NR1L-PowerManagement-245 | proc | PENDING 說明含非 ASCII 字元 ['指', '派'] | 2. PENDING: DR-PW27 seat graphic 指派 |
| 228 | NR1L-PowerManagement-247 | proc | PENDING 說明含非 ASCII 字元 ['之', '值'] | 3. PENDING: DR-PW27 <Tsend> 之值 |
| 229 | NR1L-PowerManagement-248 | proc | PENDING 說明含非 ASCII 字元 ['指', '派'] | 2. PENDING: DR-PW27 seat graphic 指派 |
| 230 | NR1L-PowerManagement-249 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '非'] | 3. PENDING: DR-PW27 —— 非 M240 之 seat graphic 指派 |
| 232 | NR1L-PowerManagement-250 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '該'] | 3. PENDING: DR-PW27 —— 該 vehicle line 之 gauges 指派 |
| 242 | NR1L-PowerManagement-178 | proc | PENDING 說明含非 ASCII 字元 ['對', '應', '之'] | 3. PENDING: DR-PW29 BODY ON 對應之 PowerSts_Telematic 值（`4941042` Full-Operation 與  |
| 242 | NR1L-PowerManagement-178 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 242 | NR1L-PowerManagement-178 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 243 | NR1L-PowerManagement-179 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 243 | NR1L-PowerManagement-179 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 244 | NR1L-PowerManagement-180 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 244 | NR1L-PowerManagement-180 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 247 | NR1L-PowerManagement-287 | proc | PENDING 說明含非 ASCII 字元 ['態', '之', '觀'] | 3. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 247 | NR1L-PowerManagement-287 | er | PENDING 說明含非 ASCII 字元 ['態', '之', '觀'] | 3. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 247 | NR1L-PowerManagement-287 | er | PENDING 說明含非 ASCII 字元 ['態', '之', '觀'] | 4. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 255 | NR1L-PowerManagement-260 | er | PENDING 說明含非 ASCII 字元 ['該', '規', '格'] | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 293 | NR1L-PowerManagement-222 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '之'] | 3. PENDING: DR-PW27 HMI disclaimer wording —— the ADAS text 之逐字定義 |
| 294 | NR1L-PowerManagement-223 | proc | PENDING 說明含非 ASCII 字元 ['—', '—', '之'] | 3. PENDING: DR-PW27 HMI disclaimer wording —— the ADAS text 之逐字定義 |
| 295 | NR1L-PowerManagement-224 | proc | PENDING 說明含非 ASCII 字元 ['（', '＋', '之'] | 3. PENDING: DR-PW27 HMI disclaimer wording（ADAS ＋ SOS 之逐字文字） |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 377／列計 147）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 18 | NR1L-PowerManagement-268 | proc | PENDING 佔位（DR-PW29） | 2. PENDING: DR-PW29 ANC 之刺激與觀察面 |
| 18 | NR1L-PowerManagement-268 | proc | PENDING 佔位（DR-PW29） | 3. PENDING: DR-PW29 ACN 之刺激與觀察面 |
| 25 | NR1L-PowerManagement-274 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 25 | NR1L-PowerManagement-274 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 25 | NR1L-PowerManagement-274 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 27 | NR1L-PowerManagement-276 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 27 | NR1L-PowerManagement-276 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 27 | NR1L-PowerManagement-276 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 29 | NR1L-PowerManagement-281 | proc | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 BoosterOUT / analog and digital antenna supply 之 ON 位準值 |
| 29 | NR1L-PowerManagement-281 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值 |
| 29 | NR1L-PowerManagement-281 | er | PENDING 佔位（DR-PW27） | 5. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值 |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 VPLastStatus |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 佔位（DR-PW25） | 5. PENDING: DR-PW25 Auto_SwitchOn_Setting.Req 之設定項名 |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 佔位（DR-PW23） | 6. PENDING: DR-PW23 Antitheft_Activation.Req |
| 30 | NR1L-PowerManagement-278 | proc | PENDING 佔位（DR-PW23） | 7. PENDING: DR-PW23 RemStartFail |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 5. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 6. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 30 | NR1L-PowerManagement-278 | er | PENDING 佔位（DR-PW23） | 7. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 31 | NR1L-PowerManagement-279 | proc | PENDING 佔位（DR-PW26） | 2. PENDING: DR-PW26 INIT 觀察量 |
| 32 | NR1L-PowerManagement-280 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 SwitchOffSetting.Req |
| 32 | NR1L-PowerManagement-280 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOffSetting.Req |
| 32 | NR1L-PowerManagement-280 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOffSetting.Req |
| 39 | NR1L-PowerManagement-049 | proc | PENDING 佔位（DR-PW25） | 5. PENDING: DR-PW25 SwitchOffSetting.Req 與 Auto_SwitchOn_Setting.Req 之設定項名與讀取方法 |
| 39 | NR1L-PowerManagement-049 | er | PENDING 佔位（DR-PW25） | 5. PENDING: DR-PW25 SwitchOffSetting.Req / Auto_SwitchOn_Setting.Req |
| 45 | NR1L-PowerManagement-055 | er | PENDING 佔位（DR-PW27） | c. PENDING: DR-PW27 BoosterOUT OFF / antenna supply ON 位準值 |
| 48 | NR1L-PowerManagement-058 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 48 | NR1L-PowerManagement-058 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 48 | NR1L-PowerManagement-058 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 RemStartFail |
| 48 | NR1L-PowerManagement-058 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 48 | NR1L-PowerManagement-058 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 48 | NR1L-PowerManagement-058 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 49 | NR1L-PowerManagement-059 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 49 | NR1L-PowerManagement-059 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 50 | NR1L-PowerManagement-060 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 50 | NR1L-PowerManagement-060 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 51 | NR1L-PowerManagement-061 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 51 | NR1L-PowerManagement-061 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 PhoneCall.Info |
| 52 | NR1L-PowerManagement-062 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 53 | NR1L-PowerManagement-063 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 53 | NR1L-PowerManagement-063 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 Phone_Call.Info |
| 54 | NR1L-PowerManagement-064 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 56 | NR1L-PowerManagement-066 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 56 | NR1L-PowerManagement-066 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 56 | NR1L-PowerManagement-066 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 57 | NR1L-PowerManagement-067 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 57 | NR1L-PowerManagement-067 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 58 | NR1L-PowerManagement-068 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 58 | NR1L-PowerManagement-068 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 58 | NR1L-PowerManagement-068 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 59 | NR1L-PowerManagement-069 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 59 | NR1L-PowerManagement-069 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 60 | NR1L-PowerManagement-070 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 60 | NR1L-PowerManagement-070 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 61 | NR1L-PowerManagement-071 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Audio_Data_Exchange.Info |
| 64 | NR1L-PowerManagement-074 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 64 | NR1L-PowerManagement-074 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 65 | NR1L-PowerManagement-075 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 65 | NR1L-PowerManagement-075 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 65 | NR1L-PowerManagement-075 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 VPLastStatus |
| 66 | NR1L-PowerManagement-076 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 67 | NR1L-PowerManagement-077 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 67 | NR1L-PowerManagement-077 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 VPLastStatus |
| 68 | NR1L-PowerManagement-078 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 68 | NR1L-PowerManagement-078 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 69 | NR1L-PowerManagement-079 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 70 | NR1L-PowerManagement-080 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 71 | NR1L-PowerManagement-081 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Rear_Camera_Enable.Info 之驅動方法（自 "False" 轉 "True"） |
| 71 | NR1L-PowerManagement-081 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 73 | NR1L-PowerManagement-083 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 74 | NR1L-PowerManagement-084 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 74 | NR1L-PowerManagement-084 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 75 | NR1L-PowerManagement-085 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 75 | NR1L-PowerManagement-085 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 76 | NR1L-PowerManagement-086 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 76 | NR1L-PowerManagement-086 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 77 | NR1L-PowerManagement-087 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 77 | NR1L-PowerManagement-087 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 78 | NR1L-PowerManagement-088 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 78 | NR1L-PowerManagement-088 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 79 | NR1L-PowerManagement-089 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 82 | NR1L-PowerManagement-092 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 83 | NR1L-PowerManagement-093 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 PhoneCall.Info |
| 84 | NR1L-PowerManagement-094 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 PhoneCall.Info |
| 86 | NR1L-PowerManagement-096 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 PhoneCall.Info |
| 87 | NR1L-PowerManagement-097 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 87 | NR1L-PowerManagement-097 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 87 | NR1L-PowerManagement-097 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 87 | NR1L-PowerManagement-097 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 88 | NR1L-PowerManagement-098 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Antitheft_Activation.Req |
| 88 | NR1L-PowerManagement-098 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 88 | NR1L-PowerManagement-098 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 88 | NR1L-PowerManagement-098 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 89 | NR1L-PowerManagement-099 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 89 | NR1L-PowerManagement-099 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 89 | NR1L-PowerManagement-099 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 89 | NR1L-PowerManagement-099 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 90 | NR1L-PowerManagement-100 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 90 | NR1L-PowerManagement-100 | proc | PENDING 佔位（DR-PW23） | 5. PENDING: DR-PW23 Antitheft_Result.Info 之觀察方法（antitheft 成功） |
| 90 | NR1L-PowerManagement-100 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 90 | NR1L-PowerManagement-100 | er | PENDING 佔位（DR-PW23） | 5. PENDING: DR-PW23 Antitheft_Result.Info |
| 91 | NR1L-PowerManagement-101 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 91 | NR1L-PowerManagement-101 | proc | PENDING 佔位（DR-PW23） | 5. PENDING: DR-PW23 Antitheft_Result.Info 之觀察方法（antitheft 成功） |
| 91 | NR1L-PowerManagement-101 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 91 | NR1L-PowerManagement-101 | er | PENDING 佔位（DR-PW23） | 5. PENDING: DR-PW23 Antitheft_Result.Info |
| 92 | NR1L-PowerManagement-102 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 92 | NR1L-PowerManagement-102 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 92 | NR1L-PowerManagement-102 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 92 | NR1L-PowerManagement-102 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 93 | NR1L-PowerManagement-103 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 93 | NR1L-PowerManagement-103 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 94 | NR1L-PowerManagement-104 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法（設為 "00 min"） |
| 94 | NR1L-PowerManagement-104 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 95 | NR1L-PowerManagement-105 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 95 | NR1L-PowerManagement-105 | proc | PENDING 佔位（DR-PW30） | 3. PENDING: DR-PW30 Response_Wait_Time 之值 |
| 95 | NR1L-PowerManagement-105 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 96 | NR1L-PowerManagement-106 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 96 | NR1L-PowerManagement-106 | proc | PENDING 佔位（DR-PW30） | 3. PENDING: DR-PW30 Response_Wait_Time 之值 |
| 96 | NR1L-PowerManagement-106 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 97 | NR1L-PowerManagement-107 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 101 | NR1L-PowerManagement-111 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 101 | NR1L-PowerManagement-111 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 101 | NR1L-PowerManagement-111 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 101 | NR1L-PowerManagement-111 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 101 | NR1L-PowerManagement-111 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 102 | NR1L-PowerManagement-112 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 102 | NR1L-PowerManagement-112 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 102 | NR1L-PowerManagement-112 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 102 | NR1L-PowerManagement-112 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 103 | NR1L-PowerManagement-113 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 103 | NR1L-PowerManagement-113 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 103 | NR1L-PowerManagement-113 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 103 | NR1L-PowerManagement-113 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 104 | NR1L-PowerManagement-114 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 104 | NR1L-PowerManagement-114 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 104 | NR1L-PowerManagement-114 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 105 | NR1L-PowerManagement-115 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 105 | NR1L-PowerManagement-115 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 105 | NR1L-PowerManagement-115 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 105 | NR1L-PowerManagement-115 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 107 | NR1L-PowerManagement-117 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 PhoneCall.Info 之驅動方法（使其轉為 "not Active"） |
| 107 | NR1L-PowerManagement-117 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail 之觀察方法 |
| 107 | NR1L-PowerManagement-117 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 PhoneCall.Info |
| 107 | NR1L-PowerManagement-117 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail |
| 108 | NR1L-PowerManagement-032 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail |
| 108 | NR1L-PowerManagement-032 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 Phone_Call.Info |
| 108 | NR1L-PowerManagement-032 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 108 | NR1L-PowerManagement-032 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 108 | NR1L-PowerManagement-032 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 109 | NR1L-PowerManagement-033 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail |
| 109 | NR1L-PowerManagement-033 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 110 | NR1L-PowerManagement-034 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 110 | NR1L-PowerManagement-034 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 111 | NR1L-PowerManagement-035 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Phone_Call.Info |
| 111 | NR1L-PowerManagement-035 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 111 | NR1L-PowerManagement-035 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 112 | NR1L-PowerManagement-036 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 112 | NR1L-PowerManagement-036 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 112 | NR1L-PowerManagement-036 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 112 | NR1L-PowerManagement-036 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 112 | NR1L-PowerManagement-036 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 113 | NR1L-PowerManagement-037 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 114 | NR1L-PowerManagement-038 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail |
| 114 | NR1L-PowerManagement-038 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 Phone_Call.Info |
| 114 | NR1L-PowerManagement-038 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 114 | NR1L-PowerManagement-038 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 115 | NR1L-PowerManagement-039 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 116 | NR1L-PowerManagement-040 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 116 | NR1L-PowerManagement-040 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 117 | NR1L-PowerManagement-041 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 RemStartFail |
| 117 | NR1L-PowerManagement-041 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 Phone_Call.Info |
| 117 | NR1L-PowerManagement-041 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 117 | NR1L-PowerManagement-041 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 RemStartFail |
| 118 | NR1L-PowerManagement-042 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 120 | NR1L-PowerManagement-119 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法 |
| 120 | NR1L-PowerManagement-119 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 121 | NR1L-PowerManagement-120 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法 |
| 121 | NR1L-PowerManagement-120 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req |
| 122 | NR1L-PowerManagement-121 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 TLM HMI documents —— 該態下應不可用之 vehicle setup 項目清單 |
| 122 | NR1L-PowerManagement-121 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 TLM HMI documents |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 佔位（DR-PW26） | 2. PENDING: DR-PW26 Suspend-to-RAM 觀察面 |
| 123 | NR1L-PowerManagement-122 | proc | PENDING 佔位（DR-PW26） | 3. PENDING: DR-PW26 Suspend-to-RAM 對應之 PowerSts_Telematic 值 |
| 124 | NR1L-PowerManagement-123 | er | PENDING 佔位（DR-PW27） | d. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值 |
| 125 | NR1L-PowerManagement-124 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 125 | NR1L-PowerManagement-124 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 126 | NR1L-PowerManagement-125 | proc | PENDING 佔位（DR-PW26） | 2. PENDING: DR-PW26 Sleep 態之觀察方法（CAN 睡眠後無法以 CAN 讀 $STATUS_TELEMATIC.PowerSts_Tel |
| 126 | NR1L-PowerManagement-125 | er | PENDING 佔位（DR-PW26） | 2. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 126 | NR1L-PowerManagement-125 | er | PENDING 佔位（DR-PW27） | c. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值 |
| 127 | NR1L-PowerManagement-126 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 127 | NR1L-PowerManagement-126 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 130 | NR1L-PowerManagement-129 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 130 | NR1L-PowerManagement-129 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 130 | NR1L-PowerManagement-129 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 130 | NR1L-PowerManagement-129 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 130 | NR1L-PowerManagement-129 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 131 | NR1L-PowerManagement-130 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Front_Panel_OnOff.Req |
| 131 | NR1L-PowerManagement-130 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 131 | NR1L-PowerManagement-130 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 131 | NR1L-PowerManagement-130 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 131 | NR1L-PowerManagement-130 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 132 | NR1L-PowerManagement-131 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 132 | NR1L-PowerManagement-131 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 132 | NR1L-PowerManagement-131 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 132 | NR1L-PowerManagement-131 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 133 | NR1L-PowerManagement-132 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 133 | NR1L-PowerManagement-132 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 133 | NR1L-PowerManagement-132 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 133 | NR1L-PowerManagement-132 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 134 | NR1L-PowerManagement-133 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 134 | NR1L-PowerManagement-133 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 134 | NR1L-PowerManagement-133 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 134 | NR1L-PowerManagement-133 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 134 | NR1L-PowerManagement-133 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 135 | NR1L-PowerManagement-134 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 135 | NR1L-PowerManagement-134 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 135 | NR1L-PowerManagement-134 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 135 | NR1L-PowerManagement-134 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 135 | NR1L-PowerManagement-134 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 136 | NR1L-PowerManagement-135 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 136 | NR1L-PowerManagement-135 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 137 | NR1L-PowerManagement-136 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 137 | NR1L-PowerManagement-136 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 137 | NR1L-PowerManagement-136 | er | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 137 | NR1L-PowerManagement-136 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Rear_Camera_Enable.Info |
| 138 | NR1L-PowerManagement-137 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 138 | NR1L-PowerManagement-137 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 138 | NR1L-PowerManagement-137 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 138 | NR1L-PowerManagement-137 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 138 | NR1L-PowerManagement-137 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 138 | NR1L-PowerManagement-137 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 139 | NR1L-PowerManagement-138 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 139 | NR1L-PowerManagement-138 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 139 | NR1L-PowerManagement-138 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 139 | NR1L-PowerManagement-138 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 140 | NR1L-PowerManagement-139 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 140 | NR1L-PowerManagement-139 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 140 | NR1L-PowerManagement-139 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 140 | NR1L-PowerManagement-139 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 141 | NR1L-PowerManagement-140 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 141 | NR1L-PowerManagement-140 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 141 | NR1L-PowerManagement-140 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 141 | NR1L-PowerManagement-140 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 142 | NR1L-PowerManagement-141 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 142 | NR1L-PowerManagement-141 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 143 | NR1L-PowerManagement-142 | pre | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 143 | NR1L-PowerManagement-142 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 144 | NR1L-PowerManagement-143 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 144 | NR1L-PowerManagement-143 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 144 | NR1L-PowerManagement-143 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 144 | NR1L-PowerManagement-143 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 145 | NR1L-PowerManagement-144 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 145 | NR1L-PowerManagement-144 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 145 | NR1L-PowerManagement-144 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 145 | NR1L-PowerManagement-144 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 145 | NR1L-PowerManagement-144 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 145 | NR1L-PowerManagement-144 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 146 | NR1L-PowerManagement-145 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 VPLastStatus |
| 147 | NR1L-PowerManagement-146 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 147 | NR1L-PowerManagement-146 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 147 | NR1L-PowerManagement-146 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 VPLastStatus |
| 147 | NR1L-PowerManagement-146 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 148 | NR1L-PowerManagement-147 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Result.Info |
| 148 | NR1L-PowerManagement-147 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Antitheft_Activation.Req |
| 148 | NR1L-PowerManagement-147 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Antitheft_Activation.Req |
| 148 | NR1L-PowerManagement-147 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 148 | NR1L-PowerManagement-147 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 148 | NR1L-PowerManagement-147 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 157 | NR1L-PowerManagement-017 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 157 | NR1L-PowerManagement-017 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 157 | NR1L-PowerManagement-017 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 157 | NR1L-PowerManagement-017 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 158 | NR1L-PowerManagement-018 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 158 | NR1L-PowerManagement-018 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 158 | NR1L-PowerManagement-018 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 158 | NR1L-PowerManagement-018 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 159 | NR1L-PowerManagement-019 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 159 | NR1L-PowerManagement-019 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 159 | NR1L-PowerManagement-019 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 159 | NR1L-PowerManagement-019 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 160 | NR1L-PowerManagement-156 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 160 | NR1L-PowerManagement-156 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 160 | NR1L-PowerManagement-156 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 160 | NR1L-PowerManagement-156 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 163 | NR1L-PowerManagement-020 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 163 | NR1L-PowerManagement-020 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 163 | NR1L-PowerManagement-020 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 163 | NR1L-PowerManagement-020 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 164 | NR1L-PowerManagement-021 | proc | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑 |
| 164 | NR1L-PowerManagement-021 | proc | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名） |
| 164 | NR1L-PowerManagement-021 | er | PENDING 佔位（DR-PW25） | 1. PENDING: DR-PW25 |
| 164 | NR1L-PowerManagement-021 | er | PENDING 佔位（DR-PW25） | 2. PENDING: DR-PW25 |
| 167 | NR1L-PowerManagement-024 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 167 | NR1L-PowerManagement-024 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 167 | NR1L-PowerManagement-024 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 168 | NR1L-PowerManagement-025 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 168 | NR1L-PowerManagement-025 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 168 | NR1L-PowerManagement-025 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 169 | NR1L-PowerManagement-026 | proc | PENDING 佔位（DR-PW23） | 2. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 169 | NR1L-PowerManagement-026 | proc | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 169 | NR1L-PowerManagement-026 | er | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Auto_SwitchOn_Setting.Req |
| 171 | NR1L-PowerManagement-028 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 172 | NR1L-PowerManagement-029 | pre | PENDING 佔位（DR-PW23） | 3. PENDING: DR-PW23 Phone_Call.Info |
| 172 | NR1L-PowerManagement-029 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 173 | NR1L-PowerManagement-030 | pre | PENDING 佔位（DR-PW23） | 4. PENDING: DR-PW23 Phone_Call.Info |
| 173 | NR1L-PowerManagement-030 | proc | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 173 | NR1L-PowerManagement-030 | er | PENDING 佔位（DR-PW23） | 1. PENDING: DR-PW23 Phone_Call.Info |
| 182 | NR1L-PowerManagement-001 | proc | PENDING 佔位（DR-PW30） | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 183 | NR1L-PowerManagement-002 | proc | PENDING 佔位（DR-PW30） | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 184 | NR1L-PowerManagement-003 | proc | PENDING 佔位（DR-PW30） | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 185 | NR1L-PowerManagement-004 | proc | PENDING 佔位（DR-PW30） | 2. PENDING: DR-PW30 SplashScreen_Time 之值 |
| 185 | NR1L-PowerManagement-004 | proc | PENDING 佔位（DR-PW30） | 4. PENDING: DR-PW30 StandardScreen_Time 之值 |
| 185 | NR1L-PowerManagement-004 | er | PENDING 佔位（DR-PW30） | 2. PENDING: DR-PW30 SplashScreen_Time |
| 185 | NR1L-PowerManagement-004 | er | PENDING 佔位（DR-PW30） | 3. PENDING: DR-PW30 SplashScreen_Time |
| 185 | NR1L-PowerManagement-004 | er | PENDING 佔位（DR-PW30） | 4. PENDING: DR-PW30 StandardScreen_Time |
| 185 | NR1L-PowerManagement-004 | er | PENDING 佔位（DR-PW30） | 5. PENDING: DR-PW30 StandardScreen_Time |
| 190 | NR1L-PowerManagement-009 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 190 | NR1L-PowerManagement-009 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 191 | NR1L-PowerManagement-010 | er | PENDING 佔位（DR-PW27） | 4. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 191 | NR1L-PowerManagement-010 | er | PENDING 佔位（DR-PW27） | 5. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 201 | NR1L-PowerManagement-169 | proc | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 201 | NR1L-PowerManagement-169 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 |
| 204 | NR1L-PowerManagement-284 | proc | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 204 | NR1L-PowerManagement-284 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 |
| 205 | NR1L-PowerManagement-285 | proc | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法 |
| 205 | NR1L-PowerManagement-285 | er | PENDING 佔位（DR-PW27） | 1. PENDING: DR-PW27 CFTS057 |
| 208 | NR1L-PowerManagement-227 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 209 | NR1L-PowerManagement-228 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 209 | NR1L-PowerManagement-228 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 210 | NR1L-PowerManagement-229 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme |
| 210 | NR1L-PowerManagement-229 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 211 | NR1L-PowerManagement-230 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該元件之預設值與元件清單 |
| 211 | NR1L-PowerManagement-230 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 212 | NR1L-PowerManagement-231 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 213 | NR1L-PowerManagement-232 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 <Tsend> 之值 |
| 223 | NR1L-PowerManagement-242 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 223 | NR1L-PowerManagement-242 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI release |
| 224 | NR1L-PowerManagement-243 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI release —— 該組態所對應之 recirc icon 指派 |
| 224 | NR1L-PowerManagement-243 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI release |
| 225 | NR1L-PowerManagement-244 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 seat graphic 指派 |
| 226 | NR1L-PowerManagement-245 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 seat graphic 指派 |
| 227 | NR1L-PowerManagement-246 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 [PDO Theme Configuration] |
| 228 | NR1L-PowerManagement-247 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 <Tsend> 之值 |
| 229 | NR1L-PowerManagement-248 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 seat graphic 指派 |
| 230 | NR1L-PowerManagement-249 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 —— 非 M240 之 seat graphic 指派 |
| 230 | NR1L-PowerManagement-249 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 |
| 232 | NR1L-PowerManagement-250 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 —— 該 vehicle line 之 gauges 指派 |
| 232 | NR1L-PowerManagement-250 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 |
| 234 | NR1L-PowerManagement-251 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 235 | NR1L-PowerManagement-252 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 236 | NR1L-PowerManagement-253 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 237 | NR1L-PowerManagement-254 | proc | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 [PDO Theme Configuration] |
| 242 | NR1L-PowerManagement-178 | proc | PENDING 佔位（DR-PW29） | 3. PENDING: DR-PW29 BODY ON 對應之 PowerSts_Telematic 值（`4941042` Full-Operation 與  |
| 242 | NR1L-PowerManagement-178 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 242 | NR1L-PowerManagement-178 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 243 | NR1L-PowerManagement-179 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 243 | NR1L-PowerManagement-179 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 244 | NR1L-PowerManagement-180 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 244 | NR1L-PowerManagement-180 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 247 | NR1L-PowerManagement-287 | proc | PENDING 佔位（DR-PW26） | 3. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 247 | NR1L-PowerManagement-287 | er | PENDING 佔位（DR-PW26） | 3. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 247 | NR1L-PowerManagement-287 | er | PENDING 佔位（DR-PW26） | 4. PENDING: DR-PW26 Sleep 態之觀察方法 |
| 255 | NR1L-PowerManagement-260 | er | PENDING 佔位（DR-PW27） | 2. PENDING: DR-PW27 該規格措辭之逐字定義（原措辭見 reasoning_note） |
| 290 | NR1L-PowerManagement-219 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 GDPR flow in HMI |
| 291 | NR1L-PowerManagement-220 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 GDPR flow in HMI |
| 292 | NR1L-PowerManagement-221 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 GDPR flow in HMI |
| 293 | NR1L-PowerManagement-222 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording —— the ADAS text 之逐字定義 |
| 293 | NR1L-PowerManagement-222 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording |
| 294 | NR1L-PowerManagement-223 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording —— the ADAS text 之逐字定義 |
| 294 | NR1L-PowerManagement-223 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording |
| 295 | NR1L-PowerManagement-224 | proc | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording（ADAS ＋ SOS 之逐字文字） |
| 295 | NR1L-PowerManagement-224 | er | PENDING 佔位（DR-PW27） | 3. PENDING: DR-PW27 HMI disclaimer wording |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 285／列計 285）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PowerManagement-261 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-PowerManagement-262 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-PowerManagement-282 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-PowerManagement-263 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-PowerManagement-264 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-PowerManagement-265 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-PowerManagement-266 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-PowerManagement-267 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-PowerManagement-268 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-PowerManagement-269 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 20 | NR1L-PowerManagement-270 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 21 | NR1L-PowerManagement-271 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 22 | NR1L-PowerManagement-272 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 23 | NR1L-PowerManagement-283 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 24 | NR1L-PowerManagement-273 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 25 | NR1L-PowerManagement-274 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 26 | NR1L-PowerManagement-275 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 27 | NR1L-PowerManagement-276 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 28 | NR1L-PowerManagement-277 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 29 | NR1L-PowerManagement-281 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 30 | NR1L-PowerManagement-278 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 31 | NR1L-PowerManagement-279 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 32 | NR1L-PowerManagement-280 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 33 | NR1L-PowerManagement-043 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 34 | NR1L-PowerManagement-044 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 35 | NR1L-PowerManagement-045 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 36 | NR1L-PowerManagement-046 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 37 | NR1L-PowerManagement-047 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 38 | NR1L-PowerManagement-048 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 39 | NR1L-PowerManagement-049 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 40 | NR1L-PowerManagement-050 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 41 | NR1L-PowerManagement-051 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 42 | NR1L-PowerManagement-052 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 43 | NR1L-PowerManagement-053 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 44 | NR1L-PowerManagement-054 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 45 | NR1L-PowerManagement-055 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 46 | NR1L-PowerManagement-056 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 47 | NR1L-PowerManagement-057 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 48 | NR1L-PowerManagement-058 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 49 | NR1L-PowerManagement-059 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 51 | NR1L-PowerManagement-061 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 52 | NR1L-PowerManagement-062 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 53 | NR1L-PowerManagement-063 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 54 | NR1L-PowerManagement-064 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 55 | NR1L-PowerManagement-065 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 56 | NR1L-PowerManagement-066 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 57 | NR1L-PowerManagement-067 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 58 | NR1L-PowerManagement-068 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 59 | NR1L-PowerManagement-069 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 60 | NR1L-PowerManagement-070 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 61 | NR1L-PowerManagement-071 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 62 | NR1L-PowerManagement-072 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 63 | NR1L-PowerManagement-073 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 64 | NR1L-PowerManagement-074 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 65 | NR1L-PowerManagement-075 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 66 | NR1L-PowerManagement-076 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 67 | NR1L-PowerManagement-077 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 68 | NR1L-PowerManagement-078 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 69 | NR1L-PowerManagement-079 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 70 | NR1L-PowerManagement-080 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 71 | NR1L-PowerManagement-081 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 72 | NR1L-PowerManagement-082 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 73 | NR1L-PowerManagement-083 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 74 | NR1L-PowerManagement-084 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 75 | NR1L-PowerManagement-085 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 76 | NR1L-PowerManagement-086 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 77 | NR1L-PowerManagement-087 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 78 | NR1L-PowerManagement-088 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 79 | NR1L-PowerManagement-089 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 80 | NR1L-PowerManagement-090 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 81 | NR1L-PowerManagement-091 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 82 | NR1L-PowerManagement-092 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 83 | NR1L-PowerManagement-093 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 84 | NR1L-PowerManagement-094 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 85 | NR1L-PowerManagement-095 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 86 | NR1L-PowerManagement-096 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 87 | NR1L-PowerManagement-097 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 88 | NR1L-PowerManagement-098 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 89 | NR1L-PowerManagement-099 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 90 | NR1L-PowerManagement-100 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 91 | NR1L-PowerManagement-101 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 92 | NR1L-PowerManagement-102 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 93 | NR1L-PowerManagement-103 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 94 | NR1L-PowerManagement-104 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 95 | NR1L-PowerManagement-105 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 96 | NR1L-PowerManagement-106 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 97 | NR1L-PowerManagement-107 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 98 | NR1L-PowerManagement-108 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 99 | NR1L-PowerManagement-109 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 100 | NR1L-PowerManagement-110 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 101 | NR1L-PowerManagement-111 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 102 | NR1L-PowerManagement-112 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 103 | NR1L-PowerManagement-113 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 104 | NR1L-PowerManagement-114 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 105 | NR1L-PowerManagement-115 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 106 | NR1L-PowerManagement-116 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 107 | NR1L-PowerManagement-117 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 108 | NR1L-PowerManagement-032 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 109 | NR1L-PowerManagement-033 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 110 | NR1L-PowerManagement-034 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 111 | NR1L-PowerManagement-035 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 112 | NR1L-PowerManagement-036 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 113 | NR1L-PowerManagement-037 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 114 | NR1L-PowerManagement-038 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 115 | NR1L-PowerManagement-039 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 116 | NR1L-PowerManagement-040 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 118 | NR1L-PowerManagement-042 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 119 | NR1L-PowerManagement-118 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 120 | NR1L-PowerManagement-119 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 121 | NR1L-PowerManagement-120 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 122 | NR1L-PowerManagement-121 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 123 | NR1L-PowerManagement-122 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 124 | NR1L-PowerManagement-123 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 125 | NR1L-PowerManagement-124 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 126 | NR1L-PowerManagement-125 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 127 | NR1L-PowerManagement-126 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 128 | NR1L-PowerManagement-127 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 129 | NR1L-PowerManagement-128 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 130 | NR1L-PowerManagement-129 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 131 | NR1L-PowerManagement-130 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 132 | NR1L-PowerManagement-131 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 133 | NR1L-PowerManagement-132 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 134 | NR1L-PowerManagement-133 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 135 | NR1L-PowerManagement-134 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 136 | NR1L-PowerManagement-135 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 137 | NR1L-PowerManagement-136 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 138 | NR1L-PowerManagement-137 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 139 | NR1L-PowerManagement-138 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 140 | NR1L-PowerManagement-139 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 141 | NR1L-PowerManagement-140 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 142 | NR1L-PowerManagement-141 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 143 | NR1L-PowerManagement-142 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 144 | NR1L-PowerManagement-143 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 145 | NR1L-PowerManagement-144 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 146 | NR1L-PowerManagement-145 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 147 | NR1L-PowerManagement-146 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 148 | NR1L-PowerManagement-147 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 149 | NR1L-PowerManagement-148 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 150 | NR1L-PowerManagement-149 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 151 | NR1L-PowerManagement-150 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 152 | NR1L-PowerManagement-151 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 153 | NR1L-PowerManagement-152 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 154 | NR1L-PowerManagement-153 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 155 | NR1L-PowerManagement-154 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 156 | NR1L-PowerManagement-155 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 157 | NR1L-PowerManagement-017 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 158 | NR1L-PowerManagement-018 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 159 | NR1L-PowerManagement-019 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 160 | NR1L-PowerManagement-156 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 161 | NR1L-PowerManagement-157 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 162 | NR1L-PowerManagement-158 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 163 | NR1L-PowerManagement-020 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 164 | NR1L-PowerManagement-021 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 165 | NR1L-PowerManagement-022 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 166 | NR1L-PowerManagement-023 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 167 | NR1L-PowerManagement-024 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 168 | NR1L-PowerManagement-025 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 169 | NR1L-PowerManagement-026 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 170 | NR1L-PowerManagement-027 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 171 | NR1L-PowerManagement-028 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 172 | NR1L-PowerManagement-029 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 173 | NR1L-PowerManagement-030 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 174 | NR1L-PowerManagement-031 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 175 | NR1L-PowerManagement-159 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 176 | NR1L-PowerManagement-160 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 177 | NR1L-PowerManagement-161 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 178 | NR1L-PowerManagement-162 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 179 | NR1L-PowerManagement-163 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 180 | NR1L-PowerManagement-164 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 181 | NR1L-PowerManagement-165 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 182 | NR1L-PowerManagement-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 183 | NR1L-PowerManagement-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 184 | NR1L-PowerManagement-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 185 | NR1L-PowerManagement-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 186 | NR1L-PowerManagement-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 187 | NR1L-PowerManagement-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 188 | NR1L-PowerManagement-007 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 189 | NR1L-PowerManagement-008 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 190 | NR1L-PowerManagement-009 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 191 | NR1L-PowerManagement-010 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 192 | NR1L-PowerManagement-011 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 193 | NR1L-PowerManagement-012 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 194 | NR1L-PowerManagement-013 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 195 | NR1L-PowerManagement-014 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 196 | NR1L-PowerManagement-015 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 197 | NR1L-PowerManagement-016 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 198 | NR1L-PowerManagement-166 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 199 | NR1L-PowerManagement-167 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 200 | NR1L-PowerManagement-168 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 201 | NR1L-PowerManagement-169 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 202 | NR1L-PowerManagement-170 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 203 | NR1L-PowerManagement-171 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 204 | NR1L-PowerManagement-284 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 205 | NR1L-PowerManagement-285 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 206 | NR1L-PowerManagement-172 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 207 | NR1L-PowerManagement-173 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 208 | NR1L-PowerManagement-227 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 209 | NR1L-PowerManagement-228 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 210 | NR1L-PowerManagement-229 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 211 | NR1L-PowerManagement-230 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 212 | NR1L-PowerManagement-231 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 213 | NR1L-PowerManagement-232 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 214 | NR1L-PowerManagement-233 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 215 | NR1L-PowerManagement-234 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 216 | NR1L-PowerManagement-235 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 217 | NR1L-PowerManagement-236 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 218 | NR1L-PowerManagement-237 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 219 | NR1L-PowerManagement-238 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 220 | NR1L-PowerManagement-239 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 221 | NR1L-PowerManagement-240 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 222 | NR1L-PowerManagement-241 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 223 | NR1L-PowerManagement-242 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 224 | NR1L-PowerManagement-243 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 225 | NR1L-PowerManagement-244 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 226 | NR1L-PowerManagement-245 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 227 | NR1L-PowerManagement-246 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 228 | NR1L-PowerManagement-247 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 229 | NR1L-PowerManagement-248 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 230 | NR1L-PowerManagement-249 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 231 | NR1L-PowerManagement-286 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 232 | NR1L-PowerManagement-250 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 234 | NR1L-PowerManagement-251 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 235 | NR1L-PowerManagement-252 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 236 | NR1L-PowerManagement-253 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 237 | NR1L-PowerManagement-254 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 238 | NR1L-PowerManagement-174 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 239 | NR1L-PowerManagement-175 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 240 | NR1L-PowerManagement-176 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 241 | NR1L-PowerManagement-177 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 242 | NR1L-PowerManagement-178 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 243 | NR1L-PowerManagement-179 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 244 | NR1L-PowerManagement-180 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 245 | NR1L-PowerManagement-181 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 246 | NR1L-PowerManagement-182 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 247 | NR1L-PowerManagement-287 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 248 | NR1L-PowerManagement-183 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 249 | NR1L-PowerManagement-184 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 250 | NR1L-PowerManagement-255 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 251 | NR1L-PowerManagement-256 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 252 | NR1L-PowerManagement-257 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 253 | NR1L-PowerManagement-258 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 254 | NR1L-PowerManagement-259 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 255 | NR1L-PowerManagement-260 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 256 | NR1L-PowerManagement-185 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 257 | NR1L-PowerManagement-186 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 258 | NR1L-PowerManagement-187 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 259 | NR1L-PowerManagement-188 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 260 | NR1L-PowerManagement-189 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 261 | NR1L-PowerManagement-190 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 262 | NR1L-PowerManagement-191 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 263 | NR1L-PowerManagement-192 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 264 | NR1L-PowerManagement-193 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 265 | NR1L-PowerManagement-194 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 266 | NR1L-PowerManagement-195 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 267 | NR1L-PowerManagement-196 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 268 | NR1L-PowerManagement-197 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 269 | NR1L-PowerManagement-198 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 270 | NR1L-PowerManagement-199 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 271 | NR1L-PowerManagement-200 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 272 | NR1L-PowerManagement-201 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 273 | NR1L-PowerManagement-202 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 274 | NR1L-PowerManagement-203 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 275 | NR1L-PowerManagement-204 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 276 | NR1L-PowerManagement-205 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 277 | NR1L-PowerManagement-206 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 278 | NR1L-PowerManagement-207 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 279 | NR1L-PowerManagement-208 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 280 | NR1L-PowerManagement-209 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 281 | NR1L-PowerManagement-210 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 282 | NR1L-PowerManagement-211 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 283 | NR1L-PowerManagement-212 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 284 | NR1L-PowerManagement-213 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 285 | NR1L-PowerManagement-214 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 286 | NR1L-PowerManagement-215 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 287 | NR1L-PowerManagement-216 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 288 | NR1L-PowerManagement-217 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 289 | NR1L-PowerManagement-218 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 290 | NR1L-PowerManagement-219 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 291 | NR1L-PowerManagement-220 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 292 | NR1L-PowerManagement-221 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 293 | NR1L-PowerManagement-222 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 294 | NR1L-PowerManagement-223 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 295 | NR1L-PowerManagement-224 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 296 | NR1L-PowerManagement-225 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 297 | NR1L-PowerManagement-226 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 7／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 39 | NR1L-PowerManagement-049 | er | 比較關係 'equals'，而 test_item 上半無數值 | PowerSts_Telematic$ equals State_before ⏎ 4. The signal value $STATUS_TELEMATIC.Po |
| 39 | NR1L-PowerManagement-049 | er | 比較關係 'equals'，而 test_item 上半無數值 | PowerSts_Telematic$ equals State_before ⏎ 5. PENDING: DR-PW25 SwitchOffSetting.Req |
| 119 | NR1L-PowerManagement-118 | er | 比較關係 'same as'，而 test_item 上半無數值 | he SNA value is the same as State_ignoff ⏎ 5. The signal value $STATUS_TELEMATIC.P |
| 119 | NR1L-PowerManagement-118 | er | 比較關係 'same as'，而 test_item 上半無數值 | he SNA value is the same as State_ignoff |
| 186 | NR1L-PowerManagement-005 | er | 比較關係 'corresponds to'，而 test_item 上半無數值 | PowerSts_Telematic$ corresponds to the last ignition value that was sent |
| 225 | NR1L-PowerManagement-244 | er | 比較關係 'matches'，而 test_item 上半無數值 | ings "Seat Graphic" matches the assignment for that vehicle line and car shape |
| 226 | NR1L-PowerManagement-245 | er | 比較關係 'matches'，而 test_item 上半無數值 | ings "Seat Graphic" matches the assignment for that vehicle line and body style |

### X — 導航路徑無固定入口（§5.8／R-G71）（行計 103／列計 84）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PowerManagement-261 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Touch the screen and read the bus trace |
| 14 | NR1L-PowerManagement-264 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Touch the screen and read the bus trace |
| 17 | NR1L-PowerManagement-267 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Touch the screen and read the bus trace |
| 22 | NR1L-PowerManagement-272 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Attempt to open a Customer setting screen to check that it is disabled |
| 24 | NR1L-PowerManagement-273 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 7. Touch the screen and read the bus trace |
| 26 | NR1L-PowerManagement-275 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 7. Touch the screen and read the bus trace |
| 28 | NR1L-PowerManagement-277 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Touch the screen and read the bus trace |
| 71 | NR1L-PowerManagement-081 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Rear View Camera" video is shown on it |
| 95 | NR1L-PowerManagement-105 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 96 | NR1L-PowerManagement-106 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 128 | NR1L-PowerManagement-127 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Leave the HU in Standby mode without requesting an HMI screen |
| 128 | NR1L-PowerManagement-127 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Display Backlight" is off while no HMI |
| 129 | NR1L-PowerManagement-128 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Request an HMI screen to be displayed while the HU is in Standby mode |
| 129 | NR1L-PowerManagement-128 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Display Backlight" is off while no HMI |
| 136 | NR1L-PowerManagement-135 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Rear View Camera" video is shown on it |
| 137 | NR1L-PowerManagement-136 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Rear View Camera" video is shown on it |
| 149 | NR1L-PowerManagement-148 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 149 | NR1L-PowerManagement-148 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 150 | NR1L-PowerManagement-149 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 150 | NR1L-PowerManagement-149 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 151 | NR1L-PowerManagement-150 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 151 | NR1L-PowerManagement-150 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 152 | NR1L-PowerManagement-151 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 152 | NR1L-PowerManagement-151 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 153 | NR1L-PowerManagement-152 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 153 | NR1L-PowerManagement-152 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 154 | NR1L-PowerManagement-153 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 155 | NR1L-PowerManagement-154 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 156 | NR1L-PowerManagement-155 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Apply ENTER_FULL_OPERATION and read the "Brand Logo Screen" |
| 165 | NR1L-PowerManagement-022 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the timeout setting entry in the TLM menu |
| 166 | NR1L-PowerManagement-023 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the timeout setting entry in the TLM menu |
| 167 | NR1L-PowerManagement-024 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the timeout setting entry in the TLM menu |
| 168 | NR1L-PowerManagement-025 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the timeout setting entry in the TLM menu |
| 169 | NR1L-PowerManagement-026 | proc | 導航標的 'menu' 而同 TC 無固定入口 | 1. Open the timeout setting entry in the TLM menu |
| 170 | NR1L-PowerManagement-027 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 2. Read the "Call Screen" on the paired phone and check that it shows the call a |
| 170 | NR1L-PowerManagement-027 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Read the HU screen and check that the "Incoming Call" pop-up is shown on it |
| 175 | NR1L-PowerManagement-159 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Call Screen" is shown on it |
| 176 | NR1L-PowerManagement-160 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Call Screen" is shown on it |
| 177 | NR1L-PowerManagement-161 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Call Screen" is shown on it |
| 181 | NR1L-PowerManagement-165 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Bring the HU to FULL OPERATION again and read the screen to check the disclai |
| 182 | NR1L-PowerManagement-001 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check the "Splash Screen" against that time on the rec |
| 183 | NR1L-PowerManagement-002 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check the "Splash Screen" against that time on the rec |
| 184 | NR1L-PowerManagement-003 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check the "Splash Screen" against that time on the rec |
| 185 | NR1L-PowerManagement-004 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen at that time and check that the "Splash Screen" is shown o |
| 185 | NR1L-PowerManagement-004 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Read the HU screen before and after that time and check that the "Standard Sc |
| 192 | NR1L-PowerManagement-011 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 4. Read the "Call Screen" on the paired phone and check that it still shows the  |
| 193 | NR1L-PowerManagement-012 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Call Screen" on the paired phone and check that it still shows the  |
| 201 | NR1L-PowerManagement-169 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check that the "FOTA update available" pop-up is shown |
| 201 | NR1L-PowerManagement-169 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Read the HU screen and check that the "FOTA update available" pop-up is still |
| 202 | NR1L-PowerManagement-170 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 1. Dismiss the FOTA pop-up on the screen |
| 204 | NR1L-PowerManagement-284 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check that the "FOTA update available" pop-up is shown |
| 204 | NR1L-PowerManagement-284 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Read the HU screen and check that the "FOTA update available" pop-up is no lo |
| 205 | NR1L-PowerManagement-285 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check that the "FOTA update available" pop-up is shown |
| 207 | NR1L-PowerManagement-173 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that it goes dark and then shows the "Splash Scr |
| 209 | NR1L-PowerManagement-228 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Theme" applied on the HU screen |
| 210 | NR1L-PowerManagement-229 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Theme" applied on the HU screen |
| 211 | NR1L-PowerManagement-230 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "PDO Branded Element" shown on the HU screen |
| 214 | NR1L-PowerManagement-233 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the branded text on the HU screen and check that it is rendered in the " |
| 215 | NR1L-PowerManagement-234 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the branded text on the HU screen and check that it is rendered in the " |
| 216 | NR1L-PowerManagement-235 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the branded text on the HU screen and check that it is rendered in the " |
| 220 | NR1L-PowerManagement-239 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Profile" screen and check that its avatar list is the "<Brand> avat |
| 221 | NR1L-PowerManagement-240 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Profile" screen and check that its avatar list is the "<Brand> avat |
| 222 | NR1L-PowerManagement-241 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Profile" screen and check that its avatar list is the "<Brand> avat |
| 223 | NR1L-PowerManagement-242 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen and check which "Recirc Icon" is shown on it |
| 224 | NR1L-PowerManagement-243 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the climate screen and check which "Recirc Icon" is shown on it |
| 230 | NR1L-PowerManagement-249 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Read the seat settings screen and check which "Seat Graphic" is shown on it |
| 231 | NR1L-PowerManagement-286 | proc | 導航標的 'settings' 而同 TC 無固定入口 | 2. Read the seat settings screen and check that the "M240 seat graphics" are sho |
| 232 | NR1L-PowerManagement-250 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Performance Gauges" screen and check which "Performance Gauges" are |
| 242 | NR1L-PowerManagement-178 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation" is no longer playe |
| 243 | NR1L-PowerManagement-179 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation" is no longer playe |
| 244 | NR1L-PowerManagement-180 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation" is no longer playe |
| 246 | NR1L-PowerManagement-182 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation" is not played on i |
| 246 | NR1L-PowerManagement-182 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Read the HU screen and check that the "Start-up Animation" is played on it |
| 247 | NR1L-PowerManagement-287 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation" is not played on i |
| 247 | NR1L-PowerManagement-287 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 5. Repeat the door event and read the HU screen |
| 248 | NR1L-PowerManagement-183 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation", the "Splash Scree |
| 249 | NR1L-PowerManagement-184 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Read the HU screen and check that the "Splash Screen" is not shown on it |
| 256 | NR1L-PowerManagement-185 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Apply ENTER_FULL_OPERATION and read the "Brand Logo Screen" |
| 263 | NR1L-PowerManagement-192 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 263 | NR1L-PowerManagement-192 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 264 | NR1L-PowerManagement-193 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 264 | NR1L-PowerManagement-193 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 265 | NR1L-PowerManagement-194 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 265 | NR1L-PowerManagement-194 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 266 | NR1L-PowerManagement-195 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown |
| 266 | NR1L-PowerManagement-195 | proc | 導航標的 'Screen' 而同 TC 無固定入口 | 3. Read the "Brand Logo Screen" and check which of the named logos is shown on i |
| 267 | NR1L-PowerManagement-196 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 268 | NR1L-PowerManagement-197 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Splash Screen" is shown on it |
| 273 | NR1L-PowerManagement-202 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Read the HU screen and check that only the "Splash Screen" is shown on it and |
| 273 | NR1L-PowerManagement-202 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 4. Touch the screen and read the bus trace |
| 274 | NR1L-PowerManagement-203 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation", the "Splash Scree |
| 275 | NR1L-PowerManagement-204 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Start-up Animation", the "Splash Scree |
| 287 | NR1L-PowerManagement-216 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Disclaimer" screen text and check that it contains "SOS" |
| 288 | NR1L-PowerManagement-217 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Disclaimer" screen text and check that it contains "Help" and does  |
| 289 | NR1L-PowerManagement-218 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. After each cycle, read the HU screen and record whether the "Disclaimer" scre |
| 289 | NR1L-PowerManagement-218 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 3. Count the cycles in which the "Disclaimer" screen was shown |
| 290 | NR1L-PowerManagement-219 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on  |
| 291 | NR1L-PowerManagement-220 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on  |
| 292 | NR1L-PowerManagement-221 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on  |
| 293 | NR1L-PowerManagement-222 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Disclaimer" screen text and check the added text |
| 294 | NR1L-PowerManagement-223 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the "Disclaimer" screen text and check the added text |
| 295 | NR1L-PowerManagement-224 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Read the HU screen and check whether the "Disclaimer" screen or the geolocati |
| 297 | NR1L-PowerManagement-226 | proc | 導航標的 'screen' 而同 TC 無固定入口 | 2. Bring the HU to FULL OPERATION again and read the screen to check the disclai |

