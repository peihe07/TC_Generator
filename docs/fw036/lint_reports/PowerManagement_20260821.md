# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260820.xlsx

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260820.xlsx`（唯讀）
- 資料列數：283
- sheet：`Test Case Specification&Result`（header 第 9 列）
- L 閾值：50 tokens

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 20 | 20 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item) | 3 | 3 | 每次命中 | 已校準 |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 104 | 104 | 每列 | 未校準（M15） |
| J | 行首大寫 | 2 | 2 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 71 | 71 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號記法未用三件組 | 41 | 35 | 每次命中 | 已校準（PM 批 1：41→0） |

**總計：行計 241**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 20／列計 20）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 15 | NR1L-PowerManagement-006 | proc | 禁用動詞 'check whether' | the TLM display to check whether the images are provided |
| 86 | NR1L-PowerManagement-077 | proc | 禁用動詞 'check whether' | TLM_Status.Info to check whether the transition of this clause occurs |
| 128 | NR1L-PowerManagement-119 | proc | 禁用動詞 'check whether' | isplay backlight to check whether it stays off |
| 178 | NR1L-PowerManagement-169 | proc | 禁用動詞 'check whether' | e and the screen to check whether the disclaimer appears |
| 205 | NR1L-PowerManagement-196 | proc | 禁用動詞 'check whether' | the HU behavior to check whether a reset occurs |
| 210 | NR1L-PowerManagement-201 | proc | 禁用動詞 '1. Observe' | 1. Observe the bus traffic while the CAN network stays awake ⏎ 2. Read $Radio_Them |
| 225 | NR1L-PowerManagement-216 | proc | 禁用動詞 '1. Observe' | 1. Observe the bus traffic while the CAN network stays awake ⏎ 2. Read $Radio_Them |
| 238 | NR1L-PowerManagement-228 | proc | 禁用動詞 'check whether' | Read the screen to check whether an animation is played |
| 242 | NR1L-PowerManagement-232 | proc | 禁用動詞 'check whether' | Read the screen to check whether an animation is played |
| 255 | NR1L-PowerManagement-245 | proc | 禁用動詞 'check whether' | the audio output to check whether a new day is granted |
| 256 | NR1L-PowerManagement-246 | proc | 禁用動詞 'check whether' | the audio output to check whether a new day is granted |
| 257 | NR1L-PowerManagement-247 | proc | 禁用動詞 'check whether' | the audio output to check whether a new day is granted |
| 275 | NR1L-PowerManagement-265 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 276 | NR1L-PowerManagement-266 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 277 | NR1L-PowerManagement-267 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 278 | NR1L-PowerManagement-268 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 279 | NR1L-PowerManagement-269 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 280 | NR1L-PowerManagement-270 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 281 | NR1L-PowerManagement-271 | proc | 禁用動詞 'check whether' | Read the screen to check whether the startup screens appear |
| 292 | NR1L-PowerManagement-282 | proc | 禁用動詞 'check whether' | e and the screen to check whether the disclaimer appears |

### C — hedge (test_item)（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 32 | NR1L-PowerManagement-023 | test_item | hedge 'properly' | TLM is able to work properly again and it has to restore the last user settings |
| 39 | NR1L-PowerManagement-030 | test_item | hedge 'properly' | TLM is able to work properly again and it has to restore the last user settings |
| 147 | NR1L-PowerManagement-138 | test_item | hedge 'Successfully' | eft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activation.Req ba |

### I-sibling — 同 Requirement ID 括號行逐字重複（行計 104／列計 104）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 33 | NR1L-PowerManagement-024 | test_item | 與 SWE-PM-011 下另 1 列括號行逐字相同 | (read the HU mode -> The HU is in Full-Operation mode) |
| 38 | NR1L-PowerManagement-029 | test_item | 與 SWE-PM-011 下另 1 列括號行逐字相同 | (read the HU mode -> The HU is in Full-Operation mode) |
| 41 | NR1L-PowerManagement-032 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 42 | NR1L-PowerManagement-033 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 43 | NR1L-PowerManagement-034 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 44 | NR1L-PowerManagement-035 | test_item | 與 SWE-PM-013 下另 3 列括號行逐字相同 | (read $Telematic_Power$ -> $Telematic_Power$ reads "Partial_Operation") |
| 47 | NR1L-PowerManagement-038 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read RemStartFail -> RemStartFail reads "True") |
| 49 | NR1L-PowerManagement-040 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 53 | NR1L-PowerManagement-044 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 55 | NR1L-PowerManagement-046 | test_item | 與 SWE-PM-014 下另 1 列括號行逐字相同 | (read RemStartFail -> RemStartFail reads "True") |
| 56 | NR1L-PowerManagement-047 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 57 | NR1L-PowerManagement-048 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 58 | NR1L-PowerManagement-049 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 59 | NR1L-PowerManagement-050 | test_item | 與 SWE-PM-015 下另 3 列括號行逐字相同 | (read VPLastStatus, TLM_Status.Info and $Telematic_Power$ -> VPLastStatus reads  |
| 62 | NR1L-PowerManagement-053 | test_item | 與 SWE-PM-018 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 63 | NR1L-PowerManagement-054 | test_item | 與 SWE-PM-018 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 64 | NR1L-PowerManagement-055 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read TLM_Status.Info and the screen -> TLM_Status.Info still reads "Idle" and n |
| 65 | NR1L-PowerManagement-056 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read the screen, VPLastStatus and TLM_Status.Info -> VPLastStatus reads "ON", T |
| 66 | NR1L-PowerManagement-057 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read TLM_Status.Info and the screen -> TLM_Status.Info still reads "Idle" and n |
| 67 | NR1L-PowerManagement-058 | test_item | 與 SWE-PM-019 下另 1 列括號行逐字相同 | (read the screen, VPLastStatus and TLM_Status.Info -> VPLastStatus reads "ON", T |
| 75 | NR1L-PowerManagement-066 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the screen -> A popup asking whether to transfer the call is shown to the  |
| 76 | NR1L-PowerManagement-067 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 77 | NR1L-PowerManagement-068 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 78 | NR1L-PowerManagement-069 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the active functionality and TLM_Status.Info -> TLM_Status.Info and $Telem |
| 79 | NR1L-PowerManagement-070 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the screen -> A popup asking whether to transfer the call is shown to the  |
| 80 | NR1L-PowerManagement-071 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 81 | NR1L-PowerManagement-072 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 82 | NR1L-PowerManagement-073 | test_item | 與 SWE-PM-025 下另 1 列括號行逐字相同 | (read the active functionality and TLM_Status.Info -> TLM_Status.Info and $Telem |
| 84 | NR1L-PowerManagement-075 | test_item | 與 SWE-PM-026 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 85 | NR1L-PowerManagement-076 | test_item | 與 SWE-PM-026 下另 1 列括號行逐字相同 | (read TLM_Status.Info -> TLM_Status.Info still reads "Timed" and the TLM stays i |
| 90 | NR1L-PowerManagement-081 | test_item | 與 SWE-PM-028 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 91 | NR1L-PowerManagement-082 | test_item | 與 SWE-PM-028 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 93 | NR1L-PowerManagement-084 | test_item | 與 SWE-PM-029 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 94 | NR1L-PowerManagement-085 | test_item | 與 SWE-PM-029 下另 1 列括號行逐字相同 | (read Timeout1 and then trigger an Ignition On event -> Timeout1 reads "00 minut |
| 95 | NR1L-PowerManagement-086 | test_item | 與 SWE-PM-030 下另 1 列括號行逐字相同 | (read the screen and its duration -> The Splash Screen stays for Response_Wait_T |
| 96 | NR1L-PowerManagement-087 | test_item | 與 SWE-PM-030 下另 1 列括號行逐字相同 | (read the screen and its duration -> The Splash Screen stays for Response_Wait_T |
| 99 | NR1L-PowerManagement-090 | test_item | 與 SWE-PM-033 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 100 | NR1L-PowerManagement-091 | test_item | 與 SWE-PM-033 下另 1 列括號行逐字相同 | (read TLM_Status.Info and $Telematic_Power$ -> TLM_Status.Info and $Telematic_Po |
| 111 | NR1L-PowerManagement-102 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 112 | NR1L-PowerManagement-103 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 113 | NR1L-PowerManagement-104 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 114 | NR1L-PowerManagement-105 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 115 | NR1L-PowerManagement-106 | test_item | 與 SWE-PM-038 下另 1 列括號行逐字相同 | (read the TLM state and the MaxCallTimeout counter -> The TLM is in Timed state  |
| 116 | NR1L-PowerManagement-107 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read TLM_Status.Info and the TLM state -> TLM_Status.Info reads "Standby" and t |
| 117 | NR1L-PowerManagement-108 | test_item | 與 SWE-PM-038 下另 2 列括號行逐字相同 | (read RemStartFail, TLM_Status.Info and the TLM state -> RemStartFail reads "Fal |
| 118 | NR1L-PowerManagement-109 | test_item | 與 SWE-PM-038 下另 1 列括號行逐字相同 | (read the TLM state and the MaxCallTimeout counter -> The TLM is in Timed state  |
| 120 | NR1L-PowerManagement-111 | test_item | 與 SWE-PM-039 下另 1 列括號行逐字相同 | (read Timeout1 against the configured parameter -> Timeout1 reads the "Switch_Of |
| 121 | NR1L-PowerManagement-112 | test_item | 與 SWE-PM-039 下另 1 列括號行逐字相同 | (read Timeout1 against the configured parameter -> Timeout1 reads the "Switch_Of |
| 130 | NR1L-PowerManagement-121 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 131 | NR1L-PowerManagement-122 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 132 | NR1L-PowerManagement-123 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 133 | NR1L-PowerManagement-124 | test_item | 與 SWE-PM-044 下另 3 列括號行逐字相同 | (read the antitheft request and the screen -> A proper Splash Screen is shown fo |
| 154 | NR1L-PowerManagement-145 | test_item | 與 SWE-PM-055 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 155 | NR1L-PowerManagement-146 | test_item | 與 SWE-PM-055 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 175 | NR1L-PowerManagement-166 | test_item | 與 SWE-PM-066 下另 1 列括號行逐字相同 | (read the HU reaction -> The HU behaves as for a Phone call becoming active) |
| 176 | NR1L-PowerManagement-167 | test_item | 與 SWE-PM-066 下另 1 列括號行逐字相同 | (read the HU reaction -> The HU behaves as for a Phone call becoming active) |
| 179 | NR1L-PowerManagement-170 | test_item | 與 SWE-PM-069 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions back to IDLE) |
| 180 | NR1L-PowerManagement-171 | test_item | 與 SWE-PM-069 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions back to IDLE) |
| 189 | NR1L-PowerManagement-180 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the display, HVAC controls, ACN phone state and AUD_LVL -> The display sta |
| 192 | NR1L-PowerManagement-183 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the call audio routing -> The continuing call is routed to the head set an |
| 193 | NR1L-PowerManagement-184 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the call audio routing -> The continuing call is routed to the head set an |
| 194 | NR1L-PowerManagement-185 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the display, HVAC controls, ACN phone state and AUD_LVL -> The display sta |
| 196 | NR1L-PowerManagement-187 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the CAN trace and the volume level -> No AUD_LVL signal carrying a new vol |
| 197 | NR1L-PowerManagement-188 | test_item | 與 SWE-PM-073 下另 1 列括號行逐字相同 | (read the CAN trace and the volume level -> No AUD_LVL signal carrying a new vol |
| 198 | NR1L-PowerManagement-189 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 199 | NR1L-PowerManagement-190 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 200 | NR1L-PowerManagement-191 | test_item | 與 SWE-PM-074 下另 2 列括號行逐字相同 | (read the HU mode and the screen -> The FOTA update available pop-up is displaye |
| 202 | NR1L-PowerManagement-193 | test_item | 與 SWE-PM-075 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions to Standby mode) |
| 203 | NR1L-PowerManagement-194 | test_item | 與 SWE-PM-075 下另 1 列括號行逐字相同 | (read the HU mode -> The HU transitions to Standby mode) |
| 207 | NR1L-PowerManagement-198 | test_item | 與 SWE-PM-078 下另 1 列括號行逐字相同 | (read the applied theme against the brand signal -> The default theme based on t |
| 208 | NR1L-PowerManagement-199 | test_item | 與 SWE-PM-078 下另 1 列括號行逐字相同 | (read the applied theme against the brand signal -> The default theme based on t |
| 235 | NR1L-PowerManagement-225 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 236 | NR1L-PowerManagement-226 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 237 | NR1L-PowerManagement-227 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen -> The HU plays a start-up animation) |
| 238 | NR1L-PowerManagement-228 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen -> The HU skips the start-up animation) |
| 239 | NR1L-PowerManagement-229 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 240 | NR1L-PowerManagement-230 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 241 | NR1L-PowerManagement-231 | test_item | 與 SWE-PM-093 下另 2 列括號行逐字相同 | (read the screen and the power mode -> The HU switches to the required power mod |
| 242 | NR1L-PowerManagement-232 | test_item | 與 SWE-PM-093 下另 1 列括號行逐字相同 | (read the screen -> The HU skips the start-up animation) |
| 255 | NR1L-PowerManagement-245 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 256 | NR1L-PowerManagement-246 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 257 | NR1L-PowerManagement-247 | test_item | 與 SWE-PM-099 下另 2 列括號行逐字相同 | (read the audio output -> A startup sound accompanies the animation for the new  |
| 263 | NR1L-PowerManagement-253 | test_item | 與 SWE-PM-102 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 264 | NR1L-PowerManagement-254 | test_item | 與 SWE-PM-102 下另 1 列括號行逐字相同 | (read the shown Splash Screen -> The Klipsch Splash Screen is displayed) |
| 265 | NR1L-PowerManagement-255 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 266 | NR1L-PowerManagement-256 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 267 | NR1L-PowerManagement-257 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 268 | NR1L-PowerManagement-258 | test_item | 與 SWE-PM-103 下另 3 列括號行逐字相同 | (read the audio path and the display -> The TLM allows only Splash Screen visual |
| 270 | NR1L-PowerManagement-260 | test_item | 與 SWE-PM-104 下另 1 列括號行逐字相同 | (read the screen sequence -> The disclaimer screen is shown) |
| 271 | NR1L-PowerManagement-261 | test_item | 與 SWE-PM-104 下另 1 列括號行逐字相同 | (read the screen sequence -> The disclaimer screen is shown) |
| 272 | NR1L-PowerManagement-262 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 273 | NR1L-PowerManagement-263 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 274 | NR1L-PowerManagement-264 | test_item | 與 SWE-PM-104 下另 2 列括號行逐字相同 | (read the screen -> The disclaimer screen is shown) |
| 275 | NR1L-PowerManagement-265 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 276 | NR1L-PowerManagement-266 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 277 | NR1L-PowerManagement-267 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 278 | NR1L-PowerManagement-268 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 279 | NR1L-PowerManagement-269 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 280 | NR1L-PowerManagement-270 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 281 | NR1L-PowerManagement-271 | test_item | 與 SWE-PM-105 下另 6 列括號行逐字相同 | (read the screen -> The disclaimer and splash screen are temporarily skipped) |
| 287 | NR1L-PowerManagement-277 | test_item | 與 SWE-PM-110 下另 1 列括號行逐字相同 | (read the startup flow against the HMI -> The HU follows the Non-GDPR/Non-Masera |
| 288 | NR1L-PowerManagement-278 | test_item | 與 SWE-PM-110 下另 1 列括號行逐字相同 | (read the startup flow against the HMI -> The HU follows the Non-GDPR/Non-Masera |
| 289 | NR1L-PowerManagement-279 | test_item | 與 SWE-PM-111 下另 1 列括號行逐字相同 | (read the disclaimer wording -> The HU adds the ADAS text to the disclaimer) |
| 290 | NR1L-PowerManagement-280 | test_item | 與 SWE-PM-111 下另 1 列括號行逐字相同 | (read the disclaimer wording -> The HU adds the ADAS text to the disclaimer) |

### J — 行首大寫（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 20 | NR1L-PowerManagement-011 | test_item | 首字小寫 'the' | the R1 HU shall not enter stolen vehicle mode under any condition |
| 204 | NR1L-PowerManagement-195 | test_item | 首字小寫 'the' | the HU shall reset both the main CPU and the CAN micro at the time of the reset |

### L — test_item 上半過長 (>50 tokens)（行計 71／列計 71）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 12 | NR1L-PowerManagement-003 | test_item | 上半 88 tokens > 50 | Full-Operation ⏎ TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT |
| 23 | NR1L-PowerManagement-014 | test_item | 上半 88 tokens > 50 | Timed ⏎ TLM plays the audio active source (Tuner, USB, AUX_IN, SDCARD, BT Music st |
| 29 | NR1L-PowerManagement-020 | test_item | 上半 84 tokens > 50 | Bench ⏎ LTM plays the audio active source (Tuner, USB, AUX_IN or Phone Call, etc) ⏎ |
| 32 | NR1L-PowerManagement-023 | test_item | 上半 59 tokens > 50 | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 39 | NR1L-PowerManagement-030 | test_item | 上半 59 tokens > 50 | After a battery reconnection and also when TLM has to exit INIT state (as soon a |
| 47 | NR1L-PowerManagement-038 | test_item | 上半 188 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 55 | NR1L-PowerManagement-046 | test_item | 上半 188 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2. |
| 58 | NR1L-PowerManagement-049 | test_item | 上半 56 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Pan |
| 59 | NR1L-PowerManagement-050 | test_item | 上半 56 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_ |
| 68 | NR1L-PowerManagement-059 | test_item | 上半 52 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info has |
| 69 | NR1L-PowerManagement-060 | test_item | 上半 68 tokens > 50 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 70 | NR1L-PowerManagement-061 | test_item | 上半 68 tokens > 50 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in P |
| 90 | NR1L-PowerManagement-081 | test_item | 上半 52 tokens > 50 | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 91 | NR1L-PowerManagement-082 | test_item | 上半 52 tokens > 50 | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req ==" |
| 130 | NR1L-PowerManagement-121 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 131 | NR1L-PowerManagement-122 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Panel_ |
| 132 | NR1L-PowerManagement-123 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 133 | NR1L-PowerManagement-124 | test_item | 上半 57 tokens > 50 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PAN |
| 136 | NR1L-PowerManagement-127 | test_item | 上半 55 tokens > 50 | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == |
| 137 | NR1L-PowerManagement-128 | test_item | 上半 55 tokens > 50 | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info == |
| 182 | NR1L-PowerManagement-173 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 183 | NR1L-PowerManagement-174 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 184 | NR1L-PowerManagement-175 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 185 | NR1L-PowerManagement-176 | test_item | 上半 51 tokens > 50 | TLM boot requires following timings: ⏎ After SplashScreen_Time the splash screen i |
| 186 | NR1L-PowerManagement-177 | test_item | 上半 51 tokens > 50 | Any event occurring during the boot must be recognized by TLM and then TLM has t |
| 187 | NR1L-PowerManagement-178 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 188 | NR1L-PowerManagement-179 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 189 | NR1L-PowerManagement-180 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 190 | NR1L-PowerManagement-181 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 191 | NR1L-PowerManagement-182 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 192 | NR1L-PowerManagement-183 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 193 | NR1L-PowerManagement-184 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 194 | NR1L-PowerManagement-185 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 195 | NR1L-PowerManagement-186 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 196 | NR1L-PowerManagement-187 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 197 | NR1L-PowerManagement-188 | test_item | 上半 266 tokens > 50 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are |
| 210 | NR1L-PowerManagement-201 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 211 | NR1L-PowerManagement-202 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 212 | NR1L-PowerManagement-203 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 213 | NR1L-PowerManagement-204 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 214 | NR1L-PowerManagement-205 | test_item | 上半 93 tokens > 50 | The HU shall use $VC_VEH_BRAND$ to determine the correct font to display. Valid |
| 215 | NR1L-PowerManagement-206 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 216 | NR1L-PowerManagement-207 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 217 | NR1L-PowerManagement-208 | test_item | 上半 101 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the correct App icon to |
| 218 | NR1L-PowerManagement-209 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 219 | NR1L-PowerManagement-210 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 220 | NR1L-PowerManagement-211 | test_item | 上半 86 tokens > 50 | The HU shall use the $VC_VEH_BRAND$  signal to determine the list of the branded |
| 221 | NR1L-PowerManagement-212 | test_item | 上半 61 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 222 | NR1L-PowerManagement-213 | test_item | 上半 61 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the$Car_Shape_Configur |
| 223 | NR1L-PowerManagement-214 | test_item | 上半 68 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 224 | NR1L-PowerManagement-215 | test_item | 上半 68 tokens > 50 | CUSW/AtlLo/AtlMi/AtlHi:The HU shall use $VC_VEH_LINE$ and the $Car_Shape_Configu |
| 225 | NR1L-PowerManagement-216 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 226 | NR1L-PowerManagement-217 | test_item | 上半 54 tokens > 50 | When the CAN network is awake, the HU shall send the special package value assoc |
| 235 | NR1L-PowerManagement-225 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 236 | NR1L-PowerManagement-226 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 237 | NR1L-PowerManagement-227 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 238 | NR1L-PowerManagement-228 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 239 | NR1L-PowerManagement-229 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 240 | NR1L-PowerManagement-230 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 241 | NR1L-PowerManagement-231 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 242 | NR1L-PowerManagement-232 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 243 | NR1L-PowerManagement-233 | test_item | 上半 205 tokens > 50 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when d |
| 275 | NR1L-PowerManagement-265 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 276 | NR1L-PowerManagement-266 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 277 | NR1L-PowerManagement-267 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 278 | NR1L-PowerManagement-268 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 279 | NR1L-PowerManagement-269 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 280 | NR1L-PowerManagement-270 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 281 | NR1L-PowerManagement-271 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 282 | NR1L-PowerManagement-272 | test_item | 上半 53 tokens > 50 | The disclaimer and splash screen can be temporarily skipped for incoming/outgoin |
| 291 | NR1L-PowerManagement-281 | test_item | 上半 59 tokens > 50 | For all screen sizes except 7 inch If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Pres |

### P — 訊號記法未用三件組（行計 41／列計 35）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 17 | NR1L-PowerManagement-008 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 41 | NR1L-PowerManagement-032 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 42 | NR1L-PowerManagement-033 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 43 | NR1L-PowerManagement-034 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 44 | NR1L-PowerManagement-035 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| 47 | NR1L-PowerManagement-038 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active" |
| 51 | NR1L-PowerManagement-042 | input | 舊式兩段記法 'STATUS_BH_BCM1.DriverDoorSts' | STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 55 | NR1L-PowerManagement-046 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active" |
| 57 | NR1L-PowerManagement-048 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read VPLas |
| 59 | NR1L-PowerManagement-050 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read VPLas |
| 66 | NR1L-PowerManagement-057 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read TLM_S |
| 67 | NR1L-PowerManagement-058 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read the s |
| 74 | NR1L-PowerManagement-065 | pre | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | er$ read "Timed" ⏎ 3. STATUS_BH_BCM2.RemStActvSts reads "Remote Start Not Active" |
| 79 | NR1L-PowerManagement-070 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read the s |
| 80 | NR1L-PowerManagement-071 | pre | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | is shown after the CLIMATIC_PANEL.Radio_Btn0 press |
| 80 | NR1L-PowerManagement-071 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user ⏎ 2. Read TLM_Status.Inf |
| 81 | NR1L-PowerManagement-072 | pre | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | is shown after the CLIMATIC_PANEL.Radio_Btn0 press |
| 81 | NR1L-PowerManagement-072 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user ⏎ 2. Read TLM_Status.In |
| 82 | NR1L-PowerManagement-073 | proc | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | 1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed" ⏎ 2. Read the a |
| 83 | NR1L-PowerManagement-074 | input | 舊式兩段記法 'STATUS_BH_BCM1.DriverDoorSts' | STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 84 | NR1L-PowerManagement-075 | input | 舊式兩段記法 'STATUS_BH_BCM1.PsngrDoorSts' | STATUS_BH_BCM1.PsngrDoorSts = "Open" |
| 85 | NR1L-PowerManagement-076 | input | 舊式兩段記法 'STATUS_BH_BCM1.DriverDoorSts' | STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 86 | NR1L-PowerManagement-077 | input | 舊式兩段記法 'STATUS_BH_BCM1.DriverDoorSts' | STATUS_BH_BCM1.DriverDoorSts = "Open" |
| 98 | NR1L-PowerManagement-089 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active" |
| 106 | NR1L-PowerManagement-097 | input | 舊式兩段記法 'STATUS_BH_BCM2.RemStActvSts' | STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active" |
| 132 | NR1L-PowerManagement-123 | input | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed" |
| 133 | NR1L-PowerManagement-124 | input | 舊式兩段記法 'CLIMATIC_PANEL.Radio_Btn0' | CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed" |
| 187 | NR1L-PowerManagement-178 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Actv' | STATUS_LIN.PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] ⏎ Starting volume le |
| 187 | NR1L-PowerManagement-178 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Lvl7' | PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] ⏎ Starting volume level: 25 |
| 189 | NR1L-PowerManagement-180 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [1h] ⏎ Starting volume level: 25 |
| 190 | NR1L-PowerManagement-181 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [0h] ⏎ Measurement window: 10 seconds |
| 191 | NR1L-PowerManagement-182 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Actv' | STATUS_LIN.PN14_LS_Actv = [0h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [0h] |
| 191 | NR1L-PowerManagement-182 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Lvl7' | PN14_LS_Actv = [0h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [0h] |
| 192 | NR1L-PowerManagement-183 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Actv' | STATUS_LIN.PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] |
| 192 | NR1L-PowerManagement-183 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Lvl7' | PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] |
| 193 | NR1L-PowerManagement-184 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [1h] |
| 194 | NR1L-PowerManagement-185 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [1h] ⏎ Starting volume level: 25 |
| 195 | NR1L-PowerManagement-186 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [1h] (held) |
| 196 | NR1L-PowerManagement-187 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Actv' | STATUS_LIN.PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] ⏎ Starting volume le |
| 196 | NR1L-PowerManagement-187 | input | 舊式兩段記法 'STATUS_LIN.PN14_LS_Lvl7' | PN14_LS_Actv = [1h] ⏎ STATUS_LIN.PN14_LS_Lvl7 = [1h] ⏎ Starting volume level: 15 |
| 197 | NR1L-PowerManagement-188 | input | 舊式兩段記法 'STATUS_LIN.Batt_ST_Crit' | STATUS_LIN.Batt_ST_Crit = [1h] ⏎ Starting volume level: 15 |

