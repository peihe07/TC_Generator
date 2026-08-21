# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS026_HandsFreePhone_20260316(Refine).xlsx

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/HandsFreePhone/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS026_HandsFreePhone_20260316(Refine).xlsx`（唯讀）
- 資料列數：159
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 31 | 24 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 18 | 18 | 每次命中 | 已校準 |
| C | hedge (test_item) | 0 | 0 | 每次命中 | 已校準 |
| D | PC 違規 (pre) | 21 | 18 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 5 | 5 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 3 | 2 | 每次命中 | 已校準 |
| G | Test Set 空值 | 29 | 29 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 28 | 28 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 2 | 2 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 45 | 40 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 44 | 44 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 39 | 25 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 2111 | 158 | 每行 | 已校準 |

**總計：行計 2376**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 31／列計 24）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 11 | newR1L-HFP-002 | proc | 禁用動詞 '4. Observe' | ation is completed. ⏎ 4. Observe any system notification during synchronization. ⏎ 5 |
| 42 | newR1L-HFP-032 | proc | 禁用動詞 '3. Monitor' | og synchronization. ⏎ 3. Monitor HU log / BT trace during synchronization. ⏎ 4. Wait |
| 48 | newR1L-HFP-038 | proc | 禁用動詞 '3. Monitor' | og synchronization. ⏎ 3. Monitor HU log / BT trace during synchronization. ⏎ 4. Wait |
| 54 | newR1L-HFP-044 | proc | 禁用動詞 '3. Monitor' | og synchronization. ⏎ 3. Monitor HU log / BT trace during synchronization. ⏎ 4. Wait |
| 58 | newR1L-HFP-048 | proc | 禁用動詞 '5. Verify' | s screen on the HU. ⏎ 5. Verify that Outgoing / Incoming / Missed records are all |
| 60 | newR1L-HFP-050 | proc | 禁用動詞 '6. Verify' | d call log entries. ⏎ 6. Verify that the call log list contains only the latest 18 |
| 62 | newR1L-HFP-052 | proc | 禁用動詞 '7. Verify' | d call log entries. ⏎ 7. Verify that the new call log entry is displayed and the o |
| 64 | newR1L-HFP-054 | proc | 禁用動詞 '5. Verify' | k screen on the HU. ⏎ 5. Verify the transferred phone book data. |
| 65 | newR1L-HFP-055 | proc | 禁用動詞 '8. Verify' | he “Mobile” folder. ⏎ 8. Verify the displayed phone number entries. |
| 66 | newR1L-HFP-056 | proc | 禁用動詞 '6. Verify' | nebook folder list. ⏎ 6. Verify the presence of the “Favorites” folder in the fold |
| 67 | newR1L-HFP-057 | proc | 禁用動詞 '7. Verify' | “Favorites” folder. ⏎ 7. Verify the displayed contact information. ⏎ 8. Unmark Conta |
| 68 | newR1L-HFP-058 | proc | 禁用動詞 'Check whether' | avorites folder. ⏎ 5. Check whether an entry named “Emergency” is displayed in Fav |
| 68 | newR1L-HFP-058 | proc | 禁用動詞 'Check whether' | ed in Favorites. ⏎ 6. Check whether an entry named “Towing Assistance” or “Roadsid |
| 69 | newR1L-HFP-059 | proc | 禁用動詞 '5. Verify' | / Favorites folder. ⏎ 5. Verify that an entry named “Emergency” exists in Favorite |
| 69 | newR1L-HFP-059 | proc | 禁用動詞 '6. Verify' | orites by default.  ⏎ 6. Verify that an entry named “Towing Assistance” exists in |
| 72 | newR1L-HFP-062 | proc | 禁用動詞 '5. Verify' | ncy” entry details. ⏎ 5. Verify the phone number type of the “Emergency” entry.  ⏎ 6 |
| 72 | newR1L-HFP-062 | proc | 禁用動詞 '8. Verify' | nce” entry details. ⏎ 8. Verify the phone number type of the “Towing Assistance” e |
| 73 | newR1L-HFP-063 | proc | 禁用動詞 '1. Verify' | 1. Verify that the E-Call/Assist-Call support status is Not Supported. ⏎ 2. Naviga |
| 73 | newR1L-HFP-063 | proc | 禁用動詞 '5. Verify' | ncy” entry details. ⏎ 5. Verify the phone number type of the “Emergency” entry. ⏎ 6. |
| 73 | newR1L-HFP-063 | proc | 禁用動詞 '9. Verify' | nce” entry details. ⏎ 9. Verify the phone number type of the “Towing Assistance” e |
| 74 | newR1L-HFP-064 | proc | 禁用動詞 '5. Observe' | timeout is reached. ⏎ 5. Observe the HU behavior and collect system logs during th |
| 75 | newR1L-HFP-065 | proc | 禁用動詞 '4. Observe' | d keep the HU idle. ⏎ 4. Observe whether the HU enters sleep mode after X seconds |
| 90 | newR1L-HFP-080 | proc | 禁用動詞 '2. Observe' | ce Manager” screen. ⏎ 2. Observe the device list content. ⏎ 3. Observe the UI messag |
| 90 | newR1L-HFP-080 | proc | 禁用動詞 '3. Observe' | evice list content. ⏎ 3. Observe the UI message displayed when the list is empty. |
| 123 |  | proc | 禁用動詞 'Check whether' | e phone numbers. ⏎ 6. Check whether all stored phone numbers for the selected cont |
| 126 |  | proc | 禁用動詞 '5. Verify' | r the Contact page. ⏎ 5. Verify that Search field, Alpha Jump, and Sort controls a |
| 134 |  | proc | 禁用動詞 '3. Verify' | BTSA internal data. ⏎ 3. Verify that the HU displays a Generic Error notification. |
| 135 |  | proc | 禁用動詞 '3. Verify' | oth module antenna. ⏎ 3. Verify that the HU displays a Generic Error notification. |
| 135 |  | proc | 禁用動詞 '6. Verify' | s the audio source. ⏎ 6. Verify USB playback behavior. ⏎ 7. Switch to FM source. ⏎ 8. |
| 136 | newR1L-HFP-068 | proc | 禁用動詞 '3. Verify' | BTSA internal data. ⏎ 3. Verify that the HU displays a Generic Error notification. |
| 137 | newR1L-HFP-069 | proc | 禁用動詞 '3. Verify' | oth module antenna. ⏎ 3. Verify that the HU displays a Generic Error notification. |

### B — ER 情態詞 (er)（行計 18／列計 18）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 122 | newR1L-HFP-061 | er | 情態詞 'shall' | ed. ⏎ 7. Contact list shall jump to the first contact starting with the Alpha L. ⏎  ⏎ |
| 127 | newR1L-HFP-063 | er | 情態詞 'shall' | splayed. ⏎ 3. HU name shall displayed as "Uconnect" on the Bluetooth Pairing scree |
| 128 | newR1L-HFP-064 | er | 情態詞 'shall' | splayed. ⏎ 3. HU name shall displayed as "Uconnect" on the Bluetooth Pairing scree |
| 138 | newR1L-HFP-070 | er | 情態詞 'shall' | isplayed. ⏎ 6. The HU shall support the following Bluetooth Profiles:  ⏎ a. A2DP Sin |
| 155 | newR1L-HFP-082 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display the Uconnect phone website URL.  ⏎ 5. The pop-up |
| 156 | newR1L-HFP-083 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 157 | newR1L-HFP-084 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 158 | newR1L-HFP-085 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 159 | newR1L-HFP-086 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 160 | newR1L-HFP-087 | er | 情態詞 'shall' | screen.  ⏎ 7. Pop up shall display the Uconnect phone website URL.  ⏎ 7. The pop-up |
| 161 | newR1L-HFP-088 | er | 情態詞 'shall' | screen.  ⏎ 7. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 162 | newR1L-HFP-089 | er | 情態詞 'shall' | screen.  ⏎ 7. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 163 | newR1L-HFP-090 | er | 情態詞 'shall' | screen.  ⏎ 7. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 164 | newR1L-HFP-091 | er | 情態詞 'shall' | screen.  ⏎ 7. Pop up shall display the Uconnect phone website URL.  ⏎ (For device c |
| 165 | newR1L-HFP-092 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display a generic text message.  ⏎ (Visit vehicle websit |
| 166 | newR1L-HFP-093 | er | 情態詞 'shall' | U Screen. ⏎ 5. Pop up shall display a generic text message.  ⏎ (Visit vehicle websit |
| 167 | newR1L-HFP-094 | er | 情態詞 'shall' | U Screen. ⏎ 7. Pop up shall display a generic text message.  ⏎ (Visit vehicle websit |
| 168 | newR1L-HFP-095 | er | 情態詞 'shall' | U Screen. ⏎ 7. Pop up shall display a generic text message.  ⏎ (Visit vehicle websit |

### D — PC 違規 (pre)（行計 21／列計 18）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 120 | newR1L-HFP-059 | pre | 編號行行首動詞 'Set' | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 121 | newR1L-HFP-060 | pre | 編號行行首動詞 'Set' | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 122 | newR1L-HFP-061 | pre | 編號行行首動詞 'Set' | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 125 | newR1L-HFP-062 | pre | 編號行行首動詞 'Set' | 3. Set PROXI "Browsing Enable" is in Absence mode. |
| 155 | newR1L-HFP-082 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Chrysler] |
| 156 | newR1L-HFP-083 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Dodge] |
| 157 | newR1L-HFP-084 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Jeep] |
| 158 | newR1L-HFP-085 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [RAM] |
| 159 | newR1L-HFP-086 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Viper] |
| 160 | newR1L-HFP-087 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Chrysler] |
| 161 | newR1L-HFP-088 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Dodge] |
| 162 | newR1L-HFP-089 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Jeep] |
| 163 | newR1L-HFP-090 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [RAM] |
| 164 | newR1L-HFP-091 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Viper] |
| 165 | newR1L-HFP-092 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Fiat] |
| 166 | newR1L-HFP-093 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Chrysler] |
| 166 | newR1L-HFP-093 | pre | 編號行行首動詞 'Set' | 3. Set Proxi $Market_Area$ = [EMEA] |
| 167 | newR1L-HFP-094 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Chrysler] |
| 167 | newR1L-HFP-094 | pre | 編號行行首動詞 'Set' | 3. Set Proxi $Market_Area$ = [EMEA] |
| 168 | newR1L-HFP-095 | pre | 編號行行首動詞 'Set' | 2. Set Proxi $Brand_Configuration_2$ = [Chrysler] |
| 168 | newR1L-HFP-095 | pre | 編號行行首動詞 'Set' | 3. Set Proxi $Market_Area$ = [EMEA] |

### E — proc/er 編號行數不對齊（行計 5／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 97 | newR1L-HFP-047 | proc/er | proc 15 步 vs er 14 步 |  |
| 143 | newR1L-HFP-075 | proc/er | proc 12 步 vs er 11 步 |  |
| 149 | newR1L-HFP-078 | proc/er | proc 9 步 vs er 10 步 |  |
| 152 | newR1L-HFP-080 | proc/er | proc 15 步 vs er 12 步 |  |
| 155 | newR1L-HFP-082 | proc/er | proc 7 步 vs er 8 步 |  |

### F — 方括號佔位 (proc)（行計 3／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 121 | newR1L-HFP-060 | proc | 方括號佔位 '[A]' | d start search(e.g. [A]) ⏎  ⏎ 1. Pair a phone with the HU. ⏎ 2. Open the Phone applica |
| 121 | newR1L-HFP-060 | proc | 方括號佔位 '[A]' | t characters. (e.g. [A]) ⏎ 6. Check the search result list. |
| 122 | newR1L-HFP-061 | proc | 方括號佔位 '[L]' | search field (e.g. [L]) ⏎  ⏎ 1. Pair a phone with the HU. ⏎ 2. Open the Phone applica |

### G — Test Set 空值（行計 29／列計 29）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 74 | newR1L-HFP-064 | test_set | Test Set 為空 |  |
| 75 | newR1L-HFP-065 | test_set | Test Set 為空 |  |
| 76 | newR1L-HFP-066 | test_set | Test Set 為空 |  |
| 77 | newR1L-HFP-067 | test_set | Test Set 為空 |  |
| 78 | newR1L-HFP-068 | test_set | Test Set 為空 |  |
| 99 |  | test_set | Test Set 為空 |  |
| 101 |  | test_set | Test Set 為空 |  |
| 102 |  | test_set | Test Set 為空 |  |
| 103 |  | test_set | Test Set 為空 |  |
| 104 |  | test_set | Test Set 為空 |  |
| 105 |  | test_set | Test Set 為空 |  |
| 106 |  | test_set | Test Set 為空 |  |
| 113 |  | test_set | Test Set 為空 |  |
| 114 |  | test_set | Test Set 為空 |  |
| 115 |  | test_set | Test Set 為空 |  |
| 117 | newR1L-HFP-057 | test_set | Test Set 為空 |  |
| 119 |  | test_set | Test Set 為空 |  |
| 123 |  | test_set | Test Set 為空 |  |
| 124 |  | test_set | Test Set 為空 |  |
| 126 |  | test_set | Test Set 為空 |  |
| 130 |  | test_set | Test Set 為空 |  |
| 131 |  | test_set | Test Set 為空 |  |
| 134 |  | test_set | Test Set 為空 |  |
| 135 |  | test_set | Test Set 為空 |  |
| 144 |  | test_set | Test Set 為空 |  |
| 146 |  | test_set | Test Set 為空 |  |
| 148 |  | test_set | Test Set 為空 |  |
| 151 |  | test_set | Test Set 為空 |  |
| 153 |  | test_set | Test Set 為空 |  |

### I — test_item 括號下半缺失（行計 28／列計 28）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 63 | newR1L-HFP-053 | test_item | 缺括號下半 | The HU shall support the transfer of an 'External Downloaded Phone Book' (a.k.a. |
| 107 | newR1L-HFP-050 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 108 | newR1L-HFP-051 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 109 | newR1L-HFP-052 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 110 | newR1L-HFP-053 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 111 | newR1L-HFP-054 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 112 | newR1L-HFP-055 | test_item | 缺括號下半 | The HU shall display a touchscreen softkey (labeled with a Microphone Icon) and |
| 134 |  | test_item | 缺括號下半 | During this error condition the user shall be able to switch to another entertai |
| 135 |  | test_item | 缺括號下半 | During this error condition the user shall be able to switch to another entertai |
| 138 | newR1L-HFP-070 | test_item | 缺括號下半 | The most current Bluetooth Automotive SIG release of Bluetooth Profiles that sup |
| 139 | newR1L-HFP-071 | test_item | 缺括號下半 | The HU shall provide a HU HMI to allow adding an un-paired Bluetooth CE device. |
| 140 | newR1L-HFP-072 | test_item | 缺括號下半 | The HU shall provide a HU HMI to allow deleting a previously paired Bluetooth de |
| 141 | newR1L-HFP-073 | test_item | 缺括號下半 | The HU shall connect to the device depending on the enabled functions and the cu |
| 151 |  | test_item | 缺括號下半 | The HU shall provide a softkey to request to CALL a phone number from the list. |
| 155 | newR1L-HFP-082 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 156 | newR1L-HFP-083 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 157 | newR1L-HFP-084 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 158 | newR1L-HFP-085 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 159 | newR1L-HFP-086 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 160 | newR1L-HFP-087 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 161 | newR1L-HFP-088 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 162 | newR1L-HFP-089 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 163 | newR1L-HFP-090 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 164 | newR1L-HFP-091 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 165 | newR1L-HFP-092 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 166 | newR1L-HFP-093 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 167 | newR1L-HFP-094 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 168 | newR1L-HFP-095 | test_item | 缺括號下半 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |

### I-sibling — 同 Requirement ID 括號行逐字重複（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 75 | newR1L-HFP-065 | test_item | 與 SWE1-HFP-007 下另 1 列括號行逐字相同 | (Idle timeout (X seconds) triggers sleep under no active call) |
| 77 | newR1L-HFP-067 | test_item | 與 SWE1-HFP-007 下另 1 列括號行逐字相同 | (Idle timeout (X seconds) triggers sleep under no active call) |

### K — CJK 字元（行計 45／列計 40）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 42 | newR1L-HFP-032 | pre | 含 CJK 字元 | capture is enabled. ⏎ 想一下有無什麼工具可以確認log 真的停止download |
| 48 | newR1L-HFP-038 | pre | 含 CJK 字元 | capture is enabled. ⏎ 想一下有無什麼工具可以確認log 真的停止download |
| 54 | newR1L-HFP-044 | pre | 含 CJK 字元 | capture is enabled. ⏎ 想一下有無什麼工具可以確認log 真的停止download |
| 74 | newR1L-HFP-064 | proc | 含 CJK 字元 | d sleep transition. ⏎ 寫清楚log查詢的步驟 |
| 74 | newR1L-HFP-064 | er | 含 CJK 字元 | it or block reason. 寫清楚log顯示的文字內容 |
| 75 | newR1L-HFP-065 | test_item | 含 CJK 字元 | o active call)  ⏎  ⏎ RD 需求分析Criteria 沒有定義，但我們還是要測試 請再和RD確認他們預計多久(幾秒後)進入sleep mode |
| 75 | newR1L-HFP-065 | proc | 含 CJK 字元 | d sleep transition. ⏎ 一樣實作確認、寫清楚Collect logs方法 |
| 75 | newR1L-HFP-065 | er | 含 CJK 字元 | sleep entry timing. ⏎ 寫清楚log顯示的內容 |
| 76 | newR1L-HFP-066 | er | 含 CJK 字元 | agement State-Chart.寫清楚log顯示的內容 |
| 95 | newR1L-HFP-045 | proc | 含 CJK 字元 | s the active phone. ⏎ 我不確定是不是active phone 才顯示或是任何一台聯接的都能確認info狀態 ⏎ 4. Check the phon |
| 100 | newR1L-HFP-049 | proc | 含 CJK 字元 | to trigger the VR. ⏎ 你的測試(描述)就是在講測試micro soft key但是測試最後樓歪，起手想法很好 先確認UI 但維持單一目的，測項 |
| 101 |  | proc | 含 CJK 字元 | microphone softkey. ⏎ 我想知道當Call Hold時我按microphone softkey會怎樣 ⏎ 結果是反灰不能按 還是什麼的?? |
| 102 |  | proc | 含 CJK 字元 | microphone softkey. ⏎ 我想確認電話由Hold > Resume mute/unmute功能是否正常 |
| 104 |  | pre | 含 CJK 字元 | 你沒有單純測試 按softkey 去控制mute/unmute |
| 104 |  | proc | 含 CJK 字元 | y again to unmute. ⏎  ⏎ 我有點疑惑按microphon邏輯上應該是mute/unmute但我看你上一條寫怎麼像按了去觸發VR ⏎  ⏎ 而且邏輯上VR不 |
| 107 | newR1L-HFP-050 | test_item | 含 CJK 字元 | s).  ⏎  ⏎ Incoming Call 你這幾條都在測試透過VR mute/unmute ⏎ 而且你思考一下 在通話中確認語音功能能否控制mute/unmute需要 |
| 108 | newR1L-HFP-051 | test_item | 含 CJK 字元 | s).  ⏎  ⏎ Outgoing Call 你這幾條都在測試透過VR mute/unmute |
| 109 | newR1L-HFP-052 | test_item | 含 CJK 字元 | gress).  ⏎  ⏎ Hold Call 你這幾條都在測試VR功能和主軸混淆 |
| 113 |  | pre | 含 CJK 字元 | 需求要顯示CallerID 要懂得思考 ⏎ Unknown number → display phone number ⏎ Contact exists → displ |
| 115 |  | er | 含 CJK 字元 | Unknown / Private) 確認一下文件這種情況顯示結果 |
| 116 | newR1L-HFP-056 | test_set | 含 CJK 字元 | 12-01需求重點不是只是看電話號碼格式 |
| 118 | newR1L-HFP-058 | er | 含 CJK 字元 | f the phone number. 這是我想確認的重點 電話簿裡聯絡人有名子會顯示名子優先於電話號碼 |
| 119 |  | pre | 含 CJK 字元 | 測試要有深度 多思考如果電話簿沒同步前顯示號碼 同步後顯示名子 也是一種優先度確認方式 |
| 124 |  | test_item | 含 CJK 字元 | set to Presence) ⏎ RD分析有提到 ⏎ [Steps]  ⏎ - Enable/Disable the Browsing parameter and v |
| 124 |  | proc | 含 CJK 字元 | ontact list order. ⏎  ⏎ 確認實際操作行為 |
| 132 | newR1L-HFP-066 | pre | 含 CJK 字元 | eena is connected. ⏎  ⏎ 不要一條測項塞這麼多測試東西 |
| 133 | newR1L-HFP-067 | er | 含 CJK 字元 | Error notification. ⏎ 如果知道Error notification. 寫進來 |
| 141 | newR1L-HFP-073 | proc | 含 CJK 字元 | Unpair All Devices. 你用unpair資料就清空 步驟6如何reconnect  ⏎ 6. Reconnect All Devices and c |
| 143 | newR1L-HFP-075 | proc | 含 CJK 字元 | rect format issue.  你要重開機才會進入paging 所以應該是步驟5 ⏎ 4. Remove the HU bonding informatio |
| 144 |  | er | 含 CJK 字元 | ected device logic. ⏎ 實作一下多台手機重連結果然後把預期結果寫清楚 我先寫connect device logic |
| 150 | newR1L-HFP-079 | proc | 含 CJK 字元 | to initial a call. 這步驟我不確定實際操作是否這樣 確認一下在重新寫過 |
| 152 | newR1L-HFP-080 | proc | 含 CJK 字元 | lphabetical order.  ⏎ 你步驟5-7沒測試到你 ( ) 內的主題 !! 如果你要把softkey enable 與電話簿內容確認放在同一條測項 |
| 153 |  | proc | 含 CJK 字元 | 確認一下有無Sorting功能 |
| 156 | newR1L-HFP-083 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 157 | newR1L-HFP-084 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 158 | newR1L-HFP-085 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 159 | newR1L-HFP-086 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 161 | newR1L-HFP-088 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 162 | newR1L-HFP-089 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 163 | newR1L-HFP-090 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 164 | newR1L-HFP-091 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 165 | newR1L-HFP-092 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 166 | newR1L-HFP-093 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 167 | newR1L-HFP-094 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |
| 168 | newR1L-HFP-095 | proc | 含 CJK 字元 | content of pop up. ⏎ 自行優化 |

### L — test_item 上半過長 (>50 tokens)（行計 44／列計 44）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 40 | newR1L-HFP-030 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 41 | newR1L-HFP-031 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 42 | newR1L-HFP-032 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 43 | newR1L-HFP-033 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 44 | newR1L-HFP-034 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 45 | newR1L-HFP-035 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-OutgoingCallLogEntries> Outgoing Ca |
| 46 | newR1L-HFP-036 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 47 | newR1L-HFP-037 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 48 | newR1L-HFP-038 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 49 | newR1L-HFP-039 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 50 | newR1L-HFP-040 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 51 | newR1L-HFP-041 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-IncomingCallLogEntries> Incoming Ca |
| 52 | newR1L-HFP-042 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 53 | newR1L-HFP-043 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 54 | newR1L-HFP-044 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 55 | newR1L-HFP-045 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 56 | newR1L-HFP-046 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 57 | newR1L-HFP-047 | test_item | 上半 51 tokens > 50 | The HU shall retrieve a maximum of <MaxCount-MissedCallLogEntries> Missed Call L |
| 72 | newR1L-HFP-062 | test_item | 上半 79 tokens > 50 | If E-Call/Assist-Call features are not supported, HU shall provide two entries w |
| 73 | newR1L-HFP-063 | test_item | 上半 81 tokens > 50 | If E-Call/Assist-Call features are not supported, HU shall provide two entries w |
| 95 | newR1L-HFP-045 | test_item | 上半 67 tokens > 50 | If the currently selected Bluetooth™ enabled phone device has the ability to rep |
| 96 | newR1L-HFP-046 | test_item | 上半 69 tokens > 50 | If the currently selected Bluetooth™ enabled phone device has the ability to rep |
| 97 | newR1L-HFP-047 | test_item | 上半 65 tokens > 50 | If the currently selected Bluetooth™ enabled phone device has the ability to rep |
| 98 | newR1L-HFP-048 | test_item | 上半 68 tokens > 50 | If the currently selected Bluetooth™ enabled phone device has the ability to rep |
| 99 |  | test_item | 上半 61 tokens > 50 | If the currently selected Bluetooth™ enabled phone device has the ability to rep |
| 136 | newR1L-HFP-068 | test_item | 上半 64 tokens > 50 | During this error condition the user shall be able to switch to another entertai |
| 137 | newR1L-HFP-069 | test_item | 上半 61 tokens > 50 | During this error condition the user shall be able to switch to another entertai |
| 152 | newR1L-HFP-080 | test_item | 上半 55 tokens > 50 | The HU shall also present a touchscreen Phonebook/Contacts softkey to allow the |
| 153 |  | test_item | 上半 55 tokens > 50 | The HU shall also present a touchscreen Phonebook/Contacts softkey to allow the |
| 154 | newR1L-HFP-081 | test_item | 上半 55 tokens > 50 | The HU shall also present a touchscreen Phonebook/Contacts softkey to allow the |
| 155 | newR1L-HFP-082 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 156 | newR1L-HFP-083 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 157 | newR1L-HFP-084 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 158 | newR1L-HFP-085 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 159 | newR1L-HFP-086 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 160 | newR1L-HFP-087 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 161 | newR1L-HFP-088 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 162 | newR1L-HFP-089 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 163 | newR1L-HFP-090 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 164 | newR1L-HFP-091 | test_item | 上半 64 tokens > 50 | If $VC_VEH_BRAND$ = [Chrysler], [Dodge], [Jeep], [RAM] or [Viper] the HU shall d |
| 165 | newR1L-HFP-092 | test_item | 上半 72 tokens > 50 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 166 | newR1L-HFP-093 | test_item | 上半 73 tokens > 50 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 167 | newR1L-HFP-094 | test_item | 上半 72 tokens > 50 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |
| 168 | newR1L-HFP-095 | test_item | 上半 73 tokens > 50 | If $VC_VEH_BRAND$ <> [Chrysler], [Dodge], [Jeep], [RAM], [Viper] or [Maserati] t |

### M — 空欄三態（行計 39／列計 25）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 77 | newR1L-HFP-067 | pre | 空欄（非 NA、非 PENDING:） |  |
| 78 | newR1L-HFP-068 | pre | 空欄（非 NA、非 PENDING:） |  |
| 99 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 101 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 101 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 102 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 102 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 103 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 103 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 104 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 105 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 105 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 106 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 106 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 113 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 114 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 114 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 115 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 115 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 119 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 123 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 124 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 126 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 130 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 130 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 131 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 131 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 134 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 134 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 135 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 135 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 144 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 146 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 148 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 148 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 151 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 153 |  | pre | 空欄（非 NA、非 PENDING:） |  |
| 153 |  | er | 空欄（非 NA、非 PENDING:） |  |
| 153 |  | spec | 空欄（非 NA、非 PENDING:） |  |

### N — 行尾多餘句號（行計 2111／列計 158）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | newR1L-HFP-001 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 10 | newR1L-HFP-001 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 10 | newR1L-HFP-001 | proc | 行尾多餘句號 | 2. Accept the phonebook access/download request on the device. |
| 10 | newR1L-HFP-001 | proc | 行尾多餘句號 | 3. Wait until phonebook synchronization is completed. |
| 10 | newR1L-HFP-001 | proc | 行尾多餘句號 | 4. Open the Phonebook screen on the HU. |
| 10 | newR1L-HFP-001 | proc | 行尾多餘句號 | 5. Open one contact detail and return to the phonebook list. |
| 10 | newR1L-HFP-001 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 10 | newR1L-HFP-001 | er | 行尾多餘句號 | 2. Phonebook synchronization starts successfully. |
| 10 | newR1L-HFP-001 | er | 行尾多餘句號 | 3. Phonebook synchronization completes successfully without error, warning, or l |
| 10 | newR1L-HFP-001 | er | 行尾多餘句號 | 4. The HU phonebook displays exactly 5,000 entries. |
| 10 | newR1L-HFP-001 | er | 行尾多餘句號 | 5. The contact detail opens correctly and the phonebook remains readable and fun |
| 11 | newR1L-HFP-002 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 2. Accept the phonebook access/download request on the device. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 3. Wait until phonebook synchronization is completed. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 4. Observe any system notification during synchronization. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 5. Open the Phonebook screen on the HU. |
| 11 | newR1L-HFP-002 | proc | 行尾多餘句號 | 6. Open one contact detail and return to the phonebook list. |
| 11 | newR1L-HFP-002 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 11 | newR1L-HFP-002 | er | 行尾多餘句號 | 2. Phonebook synchronization starts successfully. |
| 11 | newR1L-HFP-002 | er | 行尾多餘句號 | 3. Phonebook synchronization completes successfully. |
| 11 | newR1L-HFP-002 | er | 行尾多餘句號 | 5. The HU phonebook displays exactly 5,000 entries. |
| 11 | newR1L-HFP-002 | er | 行尾多餘句號 | 6. The phonebook remains readable and functional (no blank or corrupted entries) |
| 12 | newR1L-HFP-003 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 2. Check the HU phonebook contains exactly 5,000 entries. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 3. Add one new contact on the device. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 4. Trigger phonebook synchronization/update. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 5. Wait until phonebook synchronization/update is completed. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 6. Open the Phonebook screen on the HU. |
| 12 | newR1L-HFP-003 | proc | 行尾多餘句號 | 7. Search for the newly added contact. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 2. HU phonebook displays exactly 5,000 entries. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 3. The new contact is successfully created on the device. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 4. Phonebook synchronization/update starts successfully. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 5. Phonebook synchronization/update completes successfully. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 6. The HU phonebook entry count remains exactly 5,000. |
| 12 | newR1L-HFP-003 | er | 行尾多餘句號 | 7. The newly added contact is not found in the HU phonebook. |
| 13 | newR1L-HFP-004 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 2. Check the HU phonebook contains exactly 5,000 entries. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 3. Delete Contact_A on the device. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 4. Trigger phonebook synchronization/update. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 5. Wait until phonebook synchronization/update is completed. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 6. Open the Phonebook screen on the HU. |
| 13 | newR1L-HFP-004 | proc | 行尾多餘句號 | 7. Search for Contact_A. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 2. HU phonebook displays exactly 5,000 entries. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 3. Contact_A is successfully deleted from the device. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 4. Phonebook synchronization/update starts successfully. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 5. Phonebook synchronization/update completes successfully. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 6.The HU phonebook entry count becomes 4,999. |
| 13 | newR1L-HFP-004 | er | 行尾多餘句號 | 7.Contact_A is not found in the HU phonebook. |
| 14 | newR1L-HFP-005 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 14 | newR1L-HFP-005 | pre | 行尾多餘句號 | 2. HU phonebook entry count is 4,999 after a deletion update. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 2. Check the HU phonebook contains exactly 4,999 entries. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 3. Add Contact_ReAdd on the device. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 4. Trigger phonebook synchronization/update. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 5. Wait until phonebook synchronization/update is completed. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 6. Open the Phonebook screen on the HU. |
| 14 | newR1L-HFP-005 | proc | 行尾多餘句號 | 7. Search for Contact_ReAdd. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 2. HU phonebook displays exactly 4,999 entries. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 3. Contact_ReAdd is successfully created on the device. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 4. Phonebook synchronization/update starts successfully. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 5. Phonebook synchronization/update completes successfully. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 6. The HU phonebook entry count becomes exactly 5,000. |
| 14 | newR1L-HFP-005 | er | 行尾多餘句號 | 7. Contact_ReAdd is found in the HU phonebook. |
| 15 | newR1L-HFP-006 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 15 | newR1L-HFP-006 | pre | 行尾多餘句號 | 2. HU phonebook has already been synchronized to 4,999 entries. |
| 15 | newR1L-HFP-006 | pre | 行尾多餘句號 | 3. Contact_A already exists in the HU phonebook. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 2. Add a duplicate contact (Contact_A) on the device. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 3. Trigger phonebook synchronization/update. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 4. Wait until phonebook synchronization/update is completed. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 5. Open the Phonebook screen on the HU. |
| 15 | newR1L-HFP-006 | proc | 行尾多餘句號 | 6. Search for Contact_A on the HU. |
| 15 | newR1L-HFP-006 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 15 | newR1L-HFP-006 | er | 行尾多餘句號 | 2. The duplicate contact is successfully created on the device. |
| 15 | newR1L-HFP-006 | er | 行尾多餘句號 | 3. Phonebook synchronization/update starts successfully. |
| 15 | newR1L-HFP-006 | er | 行尾多餘句號 | 4. Phonebook synchronization/update completes successfully without error. |
| 15 | newR1L-HFP-006 | er | 行尾多餘句號 | 5. The Phonebook screen opens successfully and remains usable. |
| 16 | newR1L-HFP-007 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 16 | newR1L-HFP-007 | pre | 行尾多餘句號 | 2. The device contains exactly 60 outgoing call log entries. |
| 16 | newR1L-HFP-007 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 16 | newR1L-HFP-007 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 16 | newR1L-HFP-007 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 16 | newR1L-HFP-007 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 16 | newR1L-HFP-007 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 16 | newR1L-HFP-007 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 16 | newR1L-HFP-007 | er | 行尾多餘句號 | 3. The Outgoing Call Log screen opens successfully. |
| 16 | newR1L-HFP-007 | er | 行尾多餘句號 | 4. The HU displays exactly 60 outgoing call log entries. |
| 17 | newR1L-HFP-008 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 17 | newR1L-HFP-008 | pre | 行尾多餘句號 | 2. The device contains more than 60 outgoing call log entries. |
| 17 | newR1L-HFP-008 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 17 | newR1L-HFP-008 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 17 | newR1L-HFP-008 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 17 | newR1L-HFP-008 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 17 | newR1L-HFP-008 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 17 | newR1L-HFP-008 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 17 | newR1L-HFP-008 | er | 行尾多餘句號 | 3. The Outgoing Call Log screen opens successfully. |
| 17 | newR1L-HFP-008 | er | 行尾多餘句號 | 4. The HU displays no more than 60 outgoing call log entries.. |
| 18 | newR1L-HFP-009 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 18 | newR1L-HFP-009 | pre | 行尾多餘句號 | 2. The device contains more than 60 outgoing call log entries with clearly disti |
| 18 | newR1L-HFP-009 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 18 | newR1L-HFP-009 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 18 | newR1L-HFP-009 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 18 | newR1L-HFP-009 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 18 | newR1L-HFP-009 | proc | 行尾多餘句號 | 5. Review the timestamps of the displayed outgoing call log entries. |
| 18 | newR1L-HFP-009 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 18 | newR1L-HFP-009 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 18 | newR1L-HFP-009 | er | 行尾多餘句號 | 3. The Outgoing Call Log screen opens successfully. |
| 18 | newR1L-HFP-009 | er | 行尾多餘句號 | 4. The HU displays exactly 60 outgoing call log entries. |
| 18 | newR1L-HFP-009 | er | 行尾多餘句號 | 5. The displayed entries correspond to the most recent outgoing call logs on the |
| 19 | newR1L-HFP-010 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 19 | newR1L-HFP-010 | pre | 行尾多餘句號 | 2. The device contains exactly 60 outgoing call log entries. |
| 19 | newR1L-HFP-010 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 19 | newR1L-HFP-010 | proc | 行尾多餘句號 | 2. Generate one new outgoing call on the device. |
| 19 | newR1L-HFP-010 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 19 | newR1L-HFP-010 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 19 | newR1L-HFP-010 | proc | 行尾多餘句號 | 5. Open the Outgoing Call Log screen on the HU. |
| 19 | newR1L-HFP-010 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 19 | newR1L-HFP-010 | er | 行尾多餘句號 | 2. A new outgoing call log is generated on the device. |
| 19 | newR1L-HFP-010 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 19 | newR1L-HFP-010 | er | 行尾多餘句號 | 4. The Outgoing Call Log screen opens successfully. |
| 19 | newR1L-HFP-010 | er | 行尾多餘句號 | 5. The HU outgoing call log entry count remains at 60. |
| 20 | newR1L-HFP-011 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 20 | newR1L-HFP-011 | pre | 行尾多餘句號 | 2. The device contains exactly 60 outgoing call log entries. |
| 20 | newR1L-HFP-011 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 20 | newR1L-HFP-011 | proc | 行尾多餘句號 | 2. Delete one outgoing call log entry on the device. |
| 20 | newR1L-HFP-011 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 20 | newR1L-HFP-011 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 20 | newR1L-HFP-011 | proc | 行尾多餘句號 | 5. Open the Outgoing Call Log screen on the HU. |
| 20 | newR1L-HFP-011 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 20 | newR1L-HFP-011 | er | 行尾多餘句號 | 2. The selected outgoing call log entry is deleted on the device. |
| 20 | newR1L-HFP-011 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 20 | newR1L-HFP-011 | er | 行尾多餘句號 | 4. The Outgoing Call Log screen opens successfully. |
| 20 | newR1L-HFP-011 | er | 行尾多餘句號 | 5. The HU outgoing call log displays 59 entries. |
| 21 | newR1L-HFP-012 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 21 | newR1L-HFP-012 | pre | 行尾多餘句號 | 2. The HU outgoing call log contains less than 60 entries. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 2. Generate one new outgoing call on the device. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 5. Open the Outgoing Call Log screen on the HU. |
| 21 | newR1L-HFP-012 | proc | 行尾多餘句號 | 6. Search the newly generated outgoing call log entry. |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 2. A new outgoing call log is generated on the device. |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 4. The Outgoing Call Log screen opens successfully. |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 5. The HU outgoing call log entry count increases accordingly and does not excee |
| 21 | newR1L-HFP-012 | er | 行尾多餘句號 | 6. The newly generated outgoing call log entry is displayed on the HU. |
| 22 | newR1L-HFP-013 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 22 | newR1L-HFP-013 | pre | 行尾多餘句號 | 2. The device contains exactly 60 incoming call log entries. |
| 22 | newR1L-HFP-013 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 22 | newR1L-HFP-013 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 22 | newR1L-HFP-013 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 22 | newR1L-HFP-013 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 22 | newR1L-HFP-013 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 22 | newR1L-HFP-013 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 22 | newR1L-HFP-013 | er | 行尾多餘句號 | 3. The Incoming Call Log screen opens successfully. |
| 22 | newR1L-HFP-013 | er | 行尾多餘句號 | 4. The HU displays exactly 60 Incoming call log entries. |
| 23 | newR1L-HFP-014 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 23 | newR1L-HFP-014 | pre | 行尾多餘句號 | 2. The device contains more than 60 incoming call log entries. |
| 23 | newR1L-HFP-014 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 23 | newR1L-HFP-014 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 23 | newR1L-HFP-014 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 23 | newR1L-HFP-014 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 23 | newR1L-HFP-014 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 23 | newR1L-HFP-014 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 23 | newR1L-HFP-014 | er | 行尾多餘句號 | 3. The Incoming Call Log screen opens successfully. |
| 23 | newR1L-HFP-014 | er | 行尾多餘句號 | 4. The HU displays no more than 60 Incoming call log entries.. |
| 24 | newR1L-HFP-015 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 24 | newR1L-HFP-015 | pre | 行尾多餘句號 | 2. The device contains more than 60 incoming call log entries with clearly disti |
| 24 | newR1L-HFP-015 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 24 | newR1L-HFP-015 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 24 | newR1L-HFP-015 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 24 | newR1L-HFP-015 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 24 | newR1L-HFP-015 | proc | 行尾多餘句號 | 5. Review the timestamps of the displayed Incoming call log entries. |
| 24 | newR1L-HFP-015 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 24 | newR1L-HFP-015 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 24 | newR1L-HFP-015 | er | 行尾多餘句號 | 3. The Incoming Call Log screen opens successfully. |
| 24 | newR1L-HFP-015 | er | 行尾多餘句號 | 4. The HU displays exactly 60 Incoming call log entries. |
| 24 | newR1L-HFP-015 | er | 行尾多餘句號 | 5. The displayed entries correspond to the most recent Incoming call logs on the |
| 25 | newR1L-HFP-016 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 25 | newR1L-HFP-016 | pre | 行尾多餘句號 | 2. The device contains exactly 60 incoming call log entries. |
| 25 | newR1L-HFP-016 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 25 | newR1L-HFP-016 | proc | 行尾多餘句號 | 2. Generate one new incoming call on the device. |
| 25 | newR1L-HFP-016 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 25 | newR1L-HFP-016 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 25 | newR1L-HFP-016 | proc | 行尾多餘句號 | 5. Open the Incoming Call Log screen on the HU. |
| 25 | newR1L-HFP-016 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 25 | newR1L-HFP-016 | er | 行尾多餘句號 | 2. A new incoming call log is generated on the device. |
| 25 | newR1L-HFP-016 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 25 | newR1L-HFP-016 | er | 行尾多餘句號 | 4. The Incoming Call Log screen opens successfully. |
| 25 | newR1L-HFP-016 | er | 行尾多餘句號 | 5. The HU incoming call log entry count remains at 60. |
| 26 | newR1L-HFP-017 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 26 | newR1L-HFP-017 | pre | 行尾多餘句號 | 2. The device contains exactly 60 incoming call log entries. |
| 26 | newR1L-HFP-017 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 26 | newR1L-HFP-017 | proc | 行尾多餘句號 | 2. Delete one incoming call log entry on the device. |
| 26 | newR1L-HFP-017 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 26 | newR1L-HFP-017 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 26 | newR1L-HFP-017 | proc | 行尾多餘句號 | 5. Open the Incoming Call Log screen on the HU. |
| 26 | newR1L-HFP-017 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 26 | newR1L-HFP-017 | er | 行尾多餘句號 | 2. The selected incoming call log entry is deleted on the device. |
| 26 | newR1L-HFP-017 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 26 | newR1L-HFP-017 | er | 行尾多餘句號 | 4. The Incoming Call Log screen opens successfully. |
| 26 | newR1L-HFP-017 | er | 行尾多餘句號 | 5. The HU incoming call log displays 59 entries. |
| 27 | newR1L-HFP-018 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 27 | newR1L-HFP-018 | pre | 行尾多餘句號 | 2. The HU Incoming call log contains less than 60 entries. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 2. Generate one new incoming call on the device. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 5. Open the Incoming Call Log screen on the HU. |
| 27 | newR1L-HFP-018 | proc | 行尾多餘句號 | 6. Search the newly generated incoming call log entry. |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 2. A new incoming call log is generated on the device. |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 4. The Incoming Call Log screen opens successfully. |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 5. The HU incoming call log entry count increases accordingly and does not excee |
| 27 | newR1L-HFP-018 | er | 行尾多餘句號 | 6. The newly generated incoming call log entry is displayed on the HU. |
| 28 | newR1L-HFP-019 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 28 | newR1L-HFP-019 | pre | 行尾多餘句號 | 2. The device contains exactly 60 missed call log entries. |
| 28 | newR1L-HFP-019 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 28 | newR1L-HFP-019 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 28 | newR1L-HFP-019 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 28 | newR1L-HFP-019 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 28 | newR1L-HFP-019 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 28 | newR1L-HFP-019 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 28 | newR1L-HFP-019 | er | 行尾多餘句號 | 3. The Missed Call Log screen opens successfully. |
| 28 | newR1L-HFP-019 | er | 行尾多餘句號 | 4. The HU displays exactly 60 missed call log entries. |
| 29 | newR1L-HFP-020 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 29 | newR1L-HFP-020 | pre | 行尾多餘句號 | 2. The device contains more than 60 missed call log entries. |
| 29 | newR1L-HFP-020 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 29 | newR1L-HFP-020 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 29 | newR1L-HFP-020 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 29 | newR1L-HFP-020 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 29 | newR1L-HFP-020 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 29 | newR1L-HFP-020 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 29 | newR1L-HFP-020 | er | 行尾多餘句號 | 3. The Missed Call Log screen opens successfully. |
| 29 | newR1L-HFP-020 | er | 行尾多餘句號 | 4. The HU displays no more than 60 Missed call log entries.. |
| 30 | newR1L-HFP-021 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 30 | newR1L-HFP-021 | pre | 行尾多餘句號 | 2. The device contains more than 60 missed call log entries with clearly disting |
| 30 | newR1L-HFP-021 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 30 | newR1L-HFP-021 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 30 | newR1L-HFP-021 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 30 | newR1L-HFP-021 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 30 | newR1L-HFP-021 | proc | 行尾多餘句號 | 5. Review the timestamps of the displayed missed call log entries. |
| 30 | newR1L-HFP-021 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 30 | newR1L-HFP-021 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 30 | newR1L-HFP-021 | er | 行尾多餘句號 | 3. The Missed Call Log screen opens successfully. |
| 30 | newR1L-HFP-021 | er | 行尾多餘句號 | 4. The HU displays exactly 60 Missed call log entries. |
| 30 | newR1L-HFP-021 | er | 行尾多餘句號 | 5. The displayed entries correspond to the most recent missed call logs on the d |
| 31 | newR1L-HFP-022 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 31 | newR1L-HFP-022 | pre | 行尾多餘句號 | 2. The device contains exactly 60 missed call log entries. |
| 31 | newR1L-HFP-022 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 31 | newR1L-HFP-022 | proc | 行尾多餘句號 | 2. Generate one new missed call on the device. |
| 31 | newR1L-HFP-022 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 31 | newR1L-HFP-022 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 31 | newR1L-HFP-022 | proc | 行尾多餘句號 | 5. Open the Missed Call Log screen on the HU. |
| 31 | newR1L-HFP-022 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 31 | newR1L-HFP-022 | er | 行尾多餘句號 | 2. A new missed call log is generated on the device. |
| 31 | newR1L-HFP-022 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 31 | newR1L-HFP-022 | er | 行尾多餘句號 | 4. The Missed Call Log screen opens successfully. |
| 31 | newR1L-HFP-022 | er | 行尾多餘句號 | 5. The HU imissed call log entry count remains at 60. |
| 32 | newR1L-HFP-023 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 32 | newR1L-HFP-023 | pre | 行尾多餘句號 | 2. The device contains exactly 60 missed call log entries. |
| 32 | newR1L-HFP-023 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 32 | newR1L-HFP-023 | proc | 行尾多餘句號 | 2. Delete one missed call log entry on the device. |
| 32 | newR1L-HFP-023 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 32 | newR1L-HFP-023 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 32 | newR1L-HFP-023 | proc | 行尾多餘句號 | 5. Open the Missed Call Log screen on the HU. |
| 32 | newR1L-HFP-023 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 32 | newR1L-HFP-023 | er | 行尾多餘句號 | 2. The selected missed call log entry is deleted on the device. |
| 32 | newR1L-HFP-023 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 32 | newR1L-HFP-023 | er | 行尾多餘句號 | 4. The Missed Call Log screen opens successfully. |
| 32 | newR1L-HFP-023 | er | 行尾多餘句號 | 5. The HU Missed call log displays 59 entries. |
| 33 | newR1L-HFP-023 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 33 | newR1L-HFP-023 | pre | 行尾多餘句號 | 2. The HU Missed call log contains less than 60 entries. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 2. Generate one new missed call on the device. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 5. Open the Missed Call Log screen on the HU. |
| 33 | newR1L-HFP-023 | proc | 行尾多餘句號 | 6. Search the newly generated missed call log entry. |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 2. A new missed call log is generated on the device. |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 4. The Missed Call Log screen opens successfully. |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 5. The HU missed call log entry count increases accordingly and does not exceed  |
| 33 | newR1L-HFP-023 | er | 行尾多餘句號 | 6. The newly generated missed call log entry is displayed on the HU. |
| 34 | newR1L-HFP-024 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 34 | newR1L-HFP-024 | pre | 行尾多餘句號 | 2. The device contains exactly 180 call log entries. |
| 34 | newR1L-HFP-024 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 34 | newR1L-HFP-024 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 34 | newR1L-HFP-024 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 34 | newR1L-HFP-024 | proc | 行尾多餘句號 | 4. Open the All Call Log screen on the HU. |
| 34 | newR1L-HFP-024 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 34 | newR1L-HFP-024 | er | 行尾多餘句號 | 2. Call log synchronization starts successfully. |
| 34 | newR1L-HFP-024 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 34 | newR1L-HFP-024 | er | 行尾多餘句號 | 4. The All Call Log screen opens successfully and the HU displays exactly 180 ca |
| 35 | newR1L-HFP-025 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 35 | newR1L-HFP-025 | pre | 行尾多餘句號 | 2. The device contains more than 180 call log entries. |
| 35 | newR1L-HFP-025 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 35 | newR1L-HFP-025 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 35 | newR1L-HFP-025 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 35 | newR1L-HFP-025 | proc | 行尾多餘句號 | 4. Open the All Call Log screen on the HU. |
| 35 | newR1L-HFP-025 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 35 | newR1L-HFP-025 | er | 行尾多餘句號 | 2. Call log synchronization starts successfully. |
| 35 | newR1L-HFP-025 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 35 | newR1L-HFP-025 | er | 行尾多餘句號 | 4. The All Call Log screen opens successfully and the HU displays no more than 1 |
| 36 | newR1L-HFP-026 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 36 | newR1L-HFP-026 | pre | 行尾多餘句號 | 2. The device contains more than 180 call log entries with clearly distinguishab |
| 36 | newR1L-HFP-026 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 36 | newR1L-HFP-026 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 36 | newR1L-HFP-026 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 36 | newR1L-HFP-026 | proc | 行尾多餘句號 | 4. Open the All Call Log screen on the HU. |
| 36 | newR1L-HFP-026 | proc | 行尾多餘句號 | 5. Review the timestamps of the displayed call log entries. |
| 36 | newR1L-HFP-026 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 36 | newR1L-HFP-026 | er | 行尾多餘句號 | 2. Call log synchronization starts successfully. |
| 36 | newR1L-HFP-026 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 36 | newR1L-HFP-026 | er | 行尾多餘句號 | 4. The All Call Log screen opens successfully and the HU displays exactly 180 ca |
| 36 | newR1L-HFP-026 | er | 行尾多餘句號 | 5. The displayed entries correspond to the most recent call logs on the device. |
| 37 | newR1L-HFP-027 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 37 | newR1L-HFP-027 | pre | 行尾多餘句號 | 2. The device contains exactly 180 call log entries. |
| 37 | newR1L-HFP-027 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 37 | newR1L-HFP-027 | proc | 行尾多餘句號 | 2. Generate one new call log on the device. |
| 37 | newR1L-HFP-027 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 37 | newR1L-HFP-027 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 37 | newR1L-HFP-027 | proc | 行尾多餘句號 | 5. Open the All Call Log screen on the HU. |
| 37 | newR1L-HFP-027 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 37 | newR1L-HFP-027 | er | 行尾多餘句號 | 2. A new call log entry is generated on the device. |
| 37 | newR1L-HFP-027 | er | 行尾多餘句號 | 3. Call log synchronization starts successfully. |
| 37 | newR1L-HFP-027 | er | 行尾多餘句號 | 4. Call log synchronization completes successfully. |
| 37 | newR1L-HFP-027 | er | 行尾多餘句號 | 5. The All Call Log screen opens successfully and the HU call log entry count re |
| 38 | newR1L-HFP-028 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 38 | newR1L-HFP-028 | pre | 行尾多餘句號 | 2. The device contains exactly 180 call log entries. |
| 38 | newR1L-HFP-028 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 38 | newR1L-HFP-028 | proc | 行尾多餘句號 | 2. Delete one call log entry on the device. |
| 38 | newR1L-HFP-028 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 38 | newR1L-HFP-028 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 38 | newR1L-HFP-028 | proc | 行尾多餘句號 | 5. Open the All Call Log screen on the HU. |
| 38 | newR1L-HFP-028 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 38 | newR1L-HFP-028 | er | 行尾多餘句號 | 2. The selected call log entry is deleted on the device. |
| 38 | newR1L-HFP-028 | er | 行尾多餘句號 | 3. Call log synchronization starts successfully. |
| 38 | newR1L-HFP-028 | er | 行尾多餘句號 | 4. Call log synchronization completes successfully. |
| 38 | newR1L-HFP-028 | er | 行尾多餘句號 | 5. The All Call Log screen opens successfully and the HU displays 179 call log e |
| 39 | newR1L-HFP-029 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 39 | newR1L-HFP-029 | pre | 行尾多餘句號 | 2. The HU All Call Log contains less than 180 entries. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 2. Generate one new call log on the device. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 3. Trigger call log synchronization. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 5. Open the All Call Log screen on the HU. |
| 39 | newR1L-HFP-029 | proc | 行尾多餘句號 | 6. Search the newly generated call log entry. |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 2. A new call log entry is generated on the device. |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 3. Call log synchronization starts successfully. |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 4. Call log synchronization completes successfully. |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 5. The All Call Log screen opens successfully and the HU call log entry count in |
| 39 | newR1L-HFP-029 | er | 行尾多餘句號 | 6. The newly generated call log entry is displayed on the HU. |
| 40 | newR1L-HFP-030 | pre | 行尾多餘句號 | 1. PBAP-supported device is available. |
| 40 | newR1L-HFP-030 | pre | 行尾多餘句號 | 2. The device contains exactly 60 outgoing call log records. |
| 40 | newR1L-HFP-030 | pre | 行尾多餘句號 | 3. HU contains no outgoing call log records from this device. |
| 40 | newR1L-HFP-030 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 40 | newR1L-HFP-030 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization. |
| 40 | newR1L-HFP-030 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 40 | newR1L-HFP-030 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 40 | newR1L-HFP-030 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 40 | newR1L-HFP-030 | er | 行尾多餘句號 | 2. Outgoing call log synchronization is triggered successfully. |
| 40 | newR1L-HFP-030 | er | 行尾多餘句號 | 3. Outgoing call log synchronization completes successfully. |
| 40 | newR1L-HFP-030 | er | 行尾多餘句號 | 4. The HU displays exactly 60 outgoing call log records. |
| 41 | newR1L-HFP-031 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 41 | newR1L-HFP-031 | pre | 行尾多餘句號 | 2. The device contains more than 60 outgoing call log records. |
| 41 | newR1L-HFP-031 | pre | 行尾多餘句號 | 3. HU contains no outgoing call log records from this device. |
| 41 | newR1L-HFP-031 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 41 | newR1L-HFP-031 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization. |
| 41 | newR1L-HFP-031 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 41 | newR1L-HFP-031 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 41 | newR1L-HFP-031 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 41 | newR1L-HFP-031 | er | 行尾多餘句號 | 2. Outgoing call log synchronization is triggered successfully. |
| 41 | newR1L-HFP-031 | er | 行尾多餘句號 | 3. Outgoing call log synchronization completes successfully. |
| 41 | newR1L-HFP-031 | er | 行尾多餘句號 | 4. The HU displays exactly 60 outgoing call log records. |
| 42 | newR1L-HFP-032 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 42 | newR1L-HFP-032 | pre | 行尾多餘句號 | 2. The device contains more than 60 outgoing call log records. |
| 42 | newR1L-HFP-032 | pre | 行尾多餘句號 | 3. HU logging / BT trace capture is enabled. |
| 42 | newR1L-HFP-032 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 42 | newR1L-HFP-032 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization. |
| 42 | newR1L-HFP-032 | proc | 行尾多餘句號 | 3. Monitor HU log / BT trace during synchronization. |
| 42 | newR1L-HFP-032 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 42 | newR1L-HFP-032 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 42 | newR1L-HFP-032 | er | 行尾多餘句號 | 2. Outgoing call log synchronization is triggered successfully. |
| 42 | newR1L-HFP-032 | er | 行尾多餘句號 | 3. HU log / BT trace shows no further outgoing call log retrieval after 60 recor |
| 42 | newR1L-HFP-032 | er | 行尾多餘句號 | 4. Synchronization completes without continuous download requests beyond the max |
| 43 | newR1L-HFP-033 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 43 | newR1L-HFP-033 | pre | 行尾多餘句號 | 2. The device contains more than 60 outgoing call log records with distinguishab |
| 43 | newR1L-HFP-033 | pre | 行尾多餘句號 | 3. HU contains no outgoing call log records from this device. |
| 43 | newR1L-HFP-033 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 43 | newR1L-HFP-033 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization. |
| 43 | newR1L-HFP-033 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 43 | newR1L-HFP-033 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 43 | newR1L-HFP-033 | proc | 行尾多餘句號 | 5. Check the display order of the outgoing call log list. |
| 43 | newR1L-HFP-033 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 43 | newR1L-HFP-033 | er | 行尾多餘句號 | 2. Outgoing call log synchronization is triggered successfully. |
| 43 | newR1L-HFP-033 | er | 行尾多餘句號 | 3. Outgoing call log synchronization completes successfully. |
| 43 | newR1L-HFP-033 | er | 行尾多餘句號 | 4. The Outgoing Call Log screen opens successfully. |
| 43 | newR1L-HFP-033 | er | 行尾多餘句號 | 5. The HU displays only the first set of outgoing call log records in received o |
| 44 | newR1L-HFP-034 | pre | 行尾多餘句號 | 1. Two PBAP-supported devices (Device A and Device B) are available. |
| 44 | newR1L-HFP-034 | pre | 行尾多餘句號 | 2. Device A contains more than 60 outgoing call log records. |
| 44 | newR1L-HFP-034 | pre | 行尾多餘句號 | 3. Device B contains more than 60 outgoing call log records. |
| 44 | newR1L-HFP-034 | pre | 行尾多餘句號 | 4. HU contains no outgoing call log records from either device. |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 1. Pair Device A with the HU via Bluetooth. |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization for Device A and wait until complet |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 3. Open the Outgoing Call Log screen for Device A. |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 4. Pair Device B with the HU via Bluetooth. |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 5. Trigger outgoing call log synchronization for Device B and wait until complet |
| 44 | newR1L-HFP-034 | proc | 行尾多餘句號 | 6. Open the Outgoing Call Log screen for Device B. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 1. Device A is successfully paired and connected to the HU. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 2. Device A outgoing call log synchronization completes successfully. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 3. The HU displays exactly 60 outgoing call log records for Device A. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 4. Device B is successfully paired and connected to the HU. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 5. Device B outgoing call log synchronization completes successfully. |
| 44 | newR1L-HFP-034 | er | 行尾多餘句號 | 6. The HU displays exactly 60 outgoing call log records for Device B. |
| 45 | newR1L-HFP-035 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 45 | newR1L-HFP-035 | pre | 行尾多餘句號 | 2. The device contains fewer than 60 outgoing call log records. |
| 45 | newR1L-HFP-035 | pre | 行尾多餘句號 | 3. HU contains no outgoing call log records from this device. |
| 45 | newR1L-HFP-035 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 45 | newR1L-HFP-035 | proc | 行尾多餘句號 | 2. Trigger outgoing call log synchronization. |
| 45 | newR1L-HFP-035 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 45 | newR1L-HFP-035 | proc | 行尾多餘句號 | 4. Open the Outgoing Call Log screen on the HU. |
| 45 | newR1L-HFP-035 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 45 | newR1L-HFP-035 | er | 行尾多餘句號 | 2. Outgoing call log synchronization is triggered successfully. |
| 45 | newR1L-HFP-035 | er | 行尾多餘句號 | 3. Outgoing call log synchronization completes successfully. |
| 45 | newR1L-HFP-035 | er | 行尾多餘句號 | 4. The HU displays all outgoing call log records from the device (fewer than 60) |
| 46 | newR1L-HFP-036 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 46 | newR1L-HFP-036 | pre | 行尾多餘句號 | 2. The device contains exactly 60 incoming call log records. |
| 46 | newR1L-HFP-036 | pre | 行尾多餘句號 | 3. HU contains no incoming call log records from this device. |
| 46 | newR1L-HFP-036 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 46 | newR1L-HFP-036 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization. |
| 46 | newR1L-HFP-036 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 46 | newR1L-HFP-036 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 46 | newR1L-HFP-036 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 46 | newR1L-HFP-036 | er | 行尾多餘句號 | 2. Incoming call log synchronization is triggered successfully. |
| 46 | newR1L-HFP-036 | er | 行尾多餘句號 | 3. Incoming call log synchronization completes successfully. |
| 46 | newR1L-HFP-036 | er | 行尾多餘句號 | 4. The HU displays exactly 60 incoming call log records. |
| 47 | newR1L-HFP-037 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 47 | newR1L-HFP-037 | pre | 行尾多餘句號 | 2. The device contains more than 60 incoming call log records. |
| 47 | newR1L-HFP-037 | pre | 行尾多餘句號 | 3. HU contains no incoming call log records from this device. |
| 47 | newR1L-HFP-037 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 47 | newR1L-HFP-037 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization. |
| 47 | newR1L-HFP-037 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 47 | newR1L-HFP-037 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 47 | newR1L-HFP-037 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 47 | newR1L-HFP-037 | er | 行尾多餘句號 | 2. Incoming call log synchronization is triggered successfully. |
| 47 | newR1L-HFP-037 | er | 行尾多餘句號 | 3. Incoming call log synchronization completes successfully. |
| 47 | newR1L-HFP-037 | er | 行尾多餘句號 | 4. The HU displays exactly 60 incoming call log records. |
| 48 | newR1L-HFP-038 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 48 | newR1L-HFP-038 | pre | 行尾多餘句號 | 2. The device contains more than 60 incoming call log records. |
| 48 | newR1L-HFP-038 | pre | 行尾多餘句號 | 3. HU logging / BT trace capture is enabled. |
| 48 | newR1L-HFP-038 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 48 | newR1L-HFP-038 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization. |
| 48 | newR1L-HFP-038 | proc | 行尾多餘句號 | 3. Monitor HU log / BT trace during synchronization. |
| 48 | newR1L-HFP-038 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 48 | newR1L-HFP-038 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 48 | newR1L-HFP-038 | er | 行尾多餘句號 | 2. Incoming call log synchronization is triggered successfully. |
| 48 | newR1L-HFP-038 | er | 行尾多餘句號 | 3. HU log / BT trace shows no further incoming call log retrieval after 60 recor |
| 48 | newR1L-HFP-038 | er | 行尾多餘句號 | 4. Synchronization completes without continuous download requests beyond the max |
| 49 | newR1L-HFP-039 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 49 | newR1L-HFP-039 | pre | 行尾多餘句號 | 2. The device contains more than 60 incoming call log records with distinguishab |
| 49 | newR1L-HFP-039 | pre | 行尾多餘句號 | 3. HU contains no incoming call log records from this device. |
| 49 | newR1L-HFP-039 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 49 | newR1L-HFP-039 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization. |
| 49 | newR1L-HFP-039 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 49 | newR1L-HFP-039 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 49 | newR1L-HFP-039 | proc | 行尾多餘句號 | 5. Check the display order of the incoming call log list. |
| 49 | newR1L-HFP-039 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 49 | newR1L-HFP-039 | er | 行尾多餘句號 | 2. Incoming call log synchronization is triggered successfully. |
| 49 | newR1L-HFP-039 | er | 行尾多餘句號 | 3. Incoming call log synchronization completes successfully. |
| 49 | newR1L-HFP-039 | er | 行尾多餘句號 | 4. The Incoming Call Log screen opens successfully. |
| 49 | newR1L-HFP-039 | er | 行尾多餘句號 | 5. The HU displays only the first set of incoming call log records in received o |
| 50 | newR1L-HFP-040 | pre | 行尾多餘句號 | 1. Two PBAP-supported devices (Device A and Device B) are available. |
| 50 | newR1L-HFP-040 | pre | 行尾多餘句號 | 2. Device A contains more than 60 incoming call log records. |
| 50 | newR1L-HFP-040 | pre | 行尾多餘句號 | 3. Device B contains more than 60 incoming call log records. |
| 50 | newR1L-HFP-040 | pre | 行尾多餘句號 | 4. HU contains no incoming call log records from either device. |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 1. Pair Device A with the HU via Bluetooth. |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization for Device A and wait until complet |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 3. Open the Incoming Call Log screen for Device A. |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 4. Pair Device B with the HU via Bluetooth. |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 5. Trigger incoming call log synchronization for Device B and wait until complet |
| 50 | newR1L-HFP-040 | proc | 行尾多餘句號 | 6. Open the Incoming Call Log screen for Device B. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 1. Device A is successfully paired and connected to the HU. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 2. Device A incoming call log synchronization completes successfully. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 3. The HU displays exactly 60 incoming call log records for Device A. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 4. Device B is successfully paired and connected to the HU. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 5. Device B incoming call log synchronization completes successfully. |
| 50 | newR1L-HFP-040 | er | 行尾多餘句號 | 6. The HU displays exactly 60 incoming call log records for Device B. |
| 51 | newR1L-HFP-041 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 51 | newR1L-HFP-041 | pre | 行尾多餘句號 | 2. The device contains fewer than 60 incoming call log records. |
| 51 | newR1L-HFP-041 | pre | 行尾多餘句號 | 3. HU contains no incoming call log records from this device. |
| 51 | newR1L-HFP-041 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 51 | newR1L-HFP-041 | proc | 行尾多餘句號 | 2. Trigger incoming call log synchronization. |
| 51 | newR1L-HFP-041 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 51 | newR1L-HFP-041 | proc | 行尾多餘句號 | 4. Open the Incoming Call Log screen on the HU. |
| 51 | newR1L-HFP-041 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 51 | newR1L-HFP-041 | er | 行尾多餘句號 | 2. Incoming call log synchronization is triggered successfully. |
| 51 | newR1L-HFP-041 | er | 行尾多餘句號 | 3. Incoming call log synchronization completes successfully. |
| 51 | newR1L-HFP-041 | er | 行尾多餘句號 | 4. The HU displays all incoming call log records from the device (fewer than 60) |
| 52 | newR1L-HFP-042 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 52 | newR1L-HFP-042 | pre | 行尾多餘句號 | 2. The device contains exactly 60 missed call log records. |
| 52 | newR1L-HFP-042 | pre | 行尾多餘句號 | 3. HU contains no missed call log records from this device. |
| 52 | newR1L-HFP-042 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 52 | newR1L-HFP-042 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization. |
| 52 | newR1L-HFP-042 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 52 | newR1L-HFP-042 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 52 | newR1L-HFP-042 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 52 | newR1L-HFP-042 | er | 行尾多餘句號 | 2. Missed call log synchronization is triggered successfully. |
| 52 | newR1L-HFP-042 | er | 行尾多餘句號 | 3. Missed call log synchronization completes successfully. |
| 52 | newR1L-HFP-042 | er | 行尾多餘句號 | 4. The HU displays exactly 60 missed call log records. |
| 53 | newR1L-HFP-043 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 53 | newR1L-HFP-043 | pre | 行尾多餘句號 | 2. The device contains more than 60 missed call log records. |
| 53 | newR1L-HFP-043 | pre | 行尾多餘句號 | 3. HU contains no missed call log records from this device. |
| 53 | newR1L-HFP-043 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 53 | newR1L-HFP-043 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization. |
| 53 | newR1L-HFP-043 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 53 | newR1L-HFP-043 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 53 | newR1L-HFP-043 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 53 | newR1L-HFP-043 | er | 行尾多餘句號 | 2. Missed call log synchronization is triggered successfully. |
| 53 | newR1L-HFP-043 | er | 行尾多餘句號 | 3. Missed call log synchronization completes successfully. |
| 53 | newR1L-HFP-043 | er | 行尾多餘句號 | 4. The HU displays exactly 60 missed call log records. |
| 54 | newR1L-HFP-044 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 54 | newR1L-HFP-044 | pre | 行尾多餘句號 | 2. The device contains more than 60 missed call log records. |
| 54 | newR1L-HFP-044 | pre | 行尾多餘句號 | 3. HU logging / BT trace capture is enabled. |
| 54 | newR1L-HFP-044 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 54 | newR1L-HFP-044 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization. |
| 54 | newR1L-HFP-044 | proc | 行尾多餘句號 | 3. Monitor HU log / BT trace during synchronization. |
| 54 | newR1L-HFP-044 | proc | 行尾多餘句號 | 4. Wait until synchronization is completed. |
| 54 | newR1L-HFP-044 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 54 | newR1L-HFP-044 | er | 行尾多餘句號 | 2. Missed call log synchronization is triggered successfully. |
| 54 | newR1L-HFP-044 | er | 行尾多餘句號 | 3. HU log / BT trace shows no further missed call log retrieval after 60 records |
| 54 | newR1L-HFP-044 | er | 行尾多餘句號 | 4. Synchronization completes without continuous download requests beyond the max |
| 55 | newR1L-HFP-045 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 55 | newR1L-HFP-045 | pre | 行尾多餘句號 | 2. The device contains more than 60 missed call log records with distinguishable |
| 55 | newR1L-HFP-045 | pre | 行尾多餘句號 | 3. HU contains no missed call log records from this device. |
| 55 | newR1L-HFP-045 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 55 | newR1L-HFP-045 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization. |
| 55 | newR1L-HFP-045 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 55 | newR1L-HFP-045 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 55 | newR1L-HFP-045 | proc | 行尾多餘句號 | 5. Check the display order of the missed call log list. |
| 55 | newR1L-HFP-045 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 55 | newR1L-HFP-045 | er | 行尾多餘句號 | 2. Missed call log synchronization is triggered successfully. |
| 55 | newR1L-HFP-045 | er | 行尾多餘句號 | 3. Missed call log synchronization completes successfully. |
| 55 | newR1L-HFP-045 | er | 行尾多餘句號 | 4. The Missed Call Log screen opens successfully. |
| 55 | newR1L-HFP-045 | er | 行尾多餘句號 | 5. The HU displays only the first set of missed call log records in received ord |
| 56 | newR1L-HFP-046 | pre | 行尾多餘句號 | 1. Two PBAP-supported devices (Device A and Device B) are available. |
| 56 | newR1L-HFP-046 | pre | 行尾多餘句號 | 2. Device A contains more than 60 missed call log records. |
| 56 | newR1L-HFP-046 | pre | 行尾多餘句號 | 3. Device B contains more than 60 missed call log records. |
| 56 | newR1L-HFP-046 | pre | 行尾多餘句號 | 4. HU contains no missed call log records from either device. |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 1. Pair Device A with the HU via Bluetooth. |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization for Device A and wait until completed |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 3. Open the Missed Call Log screen for Device A. |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 4. Pair Device B with the HU via Bluetooth. |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 5. Trigger missed call log synchronization for Device B and wait until completed |
| 56 | newR1L-HFP-046 | proc | 行尾多餘句號 | 6. Open the Missed Call Log screen for Device B. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 1. Device A is successfully paired and connected to the HU. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 2. Device A missed call log synchronization completes successfully. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 3. The HU displays exactly 60 missed call log records for Device A. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 4. Device B is successfully paired and connected to the HU. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 5. Device B missed call log synchronization completes successfully. |
| 56 | newR1L-HFP-046 | er | 行尾多餘句號 | 6. The HU displays exactly 60 missed call log records for Device B. |
| 57 | newR1L-HFP-047 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 57 | newR1L-HFP-047 | pre | 行尾多餘句號 | 2. The device contains fewer than 60 missed call log records. |
| 57 | newR1L-HFP-047 | pre | 行尾多餘句號 | 3. HU contains no missed call log records from this device. |
| 57 | newR1L-HFP-047 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 57 | newR1L-HFP-047 | proc | 行尾多餘句號 | 2. Trigger missed call log synchronization. |
| 57 | newR1L-HFP-047 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 57 | newR1L-HFP-047 | proc | 行尾多餘句號 | 4. Open the Missed Call Log screen on the HU. |
| 57 | newR1L-HFP-047 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 57 | newR1L-HFP-047 | er | 行尾多餘句號 | 2. Missed call log synchronization is triggered successfully. |
| 57 | newR1L-HFP-047 | er | 行尾多餘句號 | 3. Missed call log synchronization completes successfully. |
| 57 | newR1L-HFP-047 | er | 行尾多餘句號 | 4. The HU displays all missed call log records from the device (fewer than 60). |
| 58 | newR1L-HFP-048 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 58 | newR1L-HFP-048 | pre | 行尾多餘句號 | 3. HU has no existing call logs for this device. |
| 58 | newR1L-HFP-048 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 58 | newR1L-HFP-048 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 58 | newR1L-HFP-048 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 58 | newR1L-HFP-048 | proc | 行尾多餘句號 | 4. Open the All Call Logs screen on the HU. |
| 58 | newR1L-HFP-048 | proc | 行尾多餘句號 | 5. Verify that Outgoing / Incoming / Missed records are all present in the list. |
| 58 | newR1L-HFP-048 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 58 | newR1L-HFP-048 | er | 行尾多餘句號 | 2. Call log synchronization is triggered successfully. |
| 58 | newR1L-HFP-048 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 58 | newR1L-HFP-048 | er | 行尾多餘句號 | 4. The All Call Logs list is displayed and sorted by timestamp (most recent firs |
| 58 | newR1L-HFP-048 | er | 行尾多餘句號 | 5. Outgoing, Incoming, and Missed call log records are all merged and visible in |
| 59 | newR1L-HFP-049 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 59 | newR1L-HFP-049 | pre | 行尾多餘句號 | 3. HU has no existing call logs for this device. |
| 59 | newR1L-HFP-049 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 59 | newR1L-HFP-049 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 59 | newR1L-HFP-049 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 59 | newR1L-HFP-049 | proc | 行尾多餘句號 | 4. Open the All Call Logs screen on the HU. |
| 59 | newR1L-HFP-049 | proc | 行尾多餘句號 | 5. Check the top 6 entries order in the All Call Logs list. |
| 59 | newR1L-HFP-049 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 59 | newR1L-HFP-049 | er | 行尾多餘句號 | 2. Call log synchronization is triggered successfully. |
| 59 | newR1L-HFP-049 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 59 | newR1L-HFP-049 | er | 行尾多餘句號 | 4. The All Call Logs screen opens successfully. |
| 59 | newR1L-HFP-049 | er | 行尾多餘句號 | Missed(T6) → Outgoing(T5) → Incoming(T4) → Missed(T3) → Incoming(T2) → Outgoing( |
| 60 | newR1L-HFP-050 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 60 | newR1L-HFP-050 | pre | 行尾多餘句號 | 2. Prepare more than 180 call log records on the device (e.g. 200 records). |
| 60 | newR1L-HFP-050 | pre | 行尾多餘句號 | 3. Call logs include mixed call types (Outgoing / Incoming / Missed) with valid  |
| 60 | newR1L-HFP-050 | pre | 行尾多餘句號 | 4. The HU has no existing call logs for this device. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 4. Open the All Call Logs screen on the HU. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 5. Check the total number of displayed call log entries. |
| 60 | newR1L-HFP-050 | proc | 行尾多餘句號 | 6. Verify that the call log list contains only the latest 180 records, and that  |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 2. Call log synchronization is triggered successfully. |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 3. Call log synchronization completes successfully. |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 4. The All Call Logs screen opens successfully. |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 5. The number of displayed call log entries is limited to 180. |
| 60 | newR1L-HFP-050 | er | 行尾多餘句號 | 6. Only the most recent 180 call log records are displayed; records older than t |
| 61 | newR1L-HFP-051 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 61 | newR1L-HFP-051 | pre | 行尾多餘句號 | 2. Prepare exactly 180 call log records on the device. |
| 61 | newR1L-HFP-051 | pre | 行尾多餘句號 | 3. The HU has no existing call logs for this device. |
| 61 | newR1L-HFP-051 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 61 | newR1L-HFP-051 | proc | 行尾多餘句號 | 2. Trigger call log synchronization. |
| 61 | newR1L-HFP-051 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 61 | newR1L-HFP-051 | proc | 行尾多餘句號 | 4. Open the All Call Logs screen on the HU. |
| 61 | newR1L-HFP-051 | proc | 行尾多餘句號 | 5. Check the total number of displayed call log entries. |
| 61 | newR1L-HFP-051 | er | 行尾多餘句號 | 1. The device is successfully paired and connected. |
| 61 | newR1L-HFP-051 | er | 行尾多餘句號 | 2. Call log synchronization completes successfully. |
| 61 | newR1L-HFP-051 | er | 行尾多餘句號 | 3. The All Call Logs screen opens successfully. |
| 61 | newR1L-HFP-051 | er | 行尾多餘句號 | 4. Exactly 180 call log records are displayed. |
| 61 | newR1L-HFP-051 | er | 行尾多餘句號 | 5. No call log record is missing or discarded. |
| 62 | newR1L-HFP-052 | pre | 行尾多餘句號 | 1. A PBAP-supported device is available. |
| 62 | newR1L-HFP-052 | pre | 行尾多餘句號 | 2. The device contains exactly 180 call log records. |
| 62 | newR1L-HFP-052 | pre | 行尾多餘句號 | 3. The HU has no existing call logs for this device. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 2. Ensure the HU has already synchronized and displays 180 call log entries. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 3. Generate a new call log entry on the device with a newer timestamp. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 4. Trigger call log synchronization or wait for automatic synchronization. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 5. Open the All Call Logs screen on the HU. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 6. Check the total number of displayed call log entries. |
| 62 | newR1L-HFP-052 | proc | 行尾多餘句號 | 7. Verify that the new call log entry is displayed and the oldest call log entry |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 2. The HU displays 180 call log entries before the new update. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 3. A new call log entry is generated successfully on the device. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 4. Call log synchronization completes successfully. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 5. The All Call Logs screen opens successfully. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 6. The number of displayed call log entries remains 180. |
| 62 | newR1L-HFP-052 | er | 行尾多餘句號 | 7. The newly generated call log entry is displayed, and the previously oldest ca |
| 63 | newR1L-HFP-053 | pre | 行尾多餘句號 | 1. A Bluetooth device is available. |
| 63 | newR1L-HFP-053 | pre | 行尾多餘句號 | 2. The Bluetooth device supports PBAP. |
| 63 | newR1L-HFP-053 | pre | 行尾多餘句號 | • If PBAP is not supported, the device supports OBEX. |
| 63 | newR1L-HFP-053 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 63 | newR1L-HFP-053 | proc | 行尾多餘句號 | 2. Initiate the external phonebook transfer from the device. |
| 63 | newR1L-HFP-053 | proc | 行尾多餘句號 | 3. Wait until the transfer is completed. |
| 63 | newR1L-HFP-053 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 63 | newR1L-HFP-053 | er | 行尾多餘句號 | 2. The HU starts receiving the External Downloaded Phone Book. |
| 63 | newR1L-HFP-053 | er | 行尾多餘句號 | 3. The External Downloaded Phone Book is successfully transferred to the HU. |
| 64 | newR1L-HFP-054 | pre | 行尾多餘句號 | 1. A Bluetooth device supporting PBAP and/or OBEX profiles is available. |
| 64 | newR1L-HFP-054 | pre | 行尾多餘句號 | 2. The Bluetooth device contains an External Downloaded Phone Book (Mobile phone |
| 64 | newR1L-HFP-054 | proc | 行尾多餘句號 | 1. Pair the Bluetooth device with the HU via Bluetooth. |
| 64 | newR1L-HFP-054 | proc | 行尾多餘句號 | 2. Trigger phone book transfer using PBAP or OBEX. |
| 64 | newR1L-HFP-054 | proc | 行尾多餘句號 | 3. Wait until the phone book transfer is completed. |
| 64 | newR1L-HFP-054 | proc | 行尾多餘句號 | 4. Open the Phone Book screen on the HU. |
| 64 | newR1L-HFP-054 | proc | 行尾多餘句號 | 5. Verify the transferred phone book data. |
| 64 | newR1L-HFP-054 | er | 行尾多餘句號 | 1. The Bluetooth device is successfully paired and connected to the HU. |
| 64 | newR1L-HFP-054 | er | 行尾多餘句號 | 2. Phone book transfer is triggered successfully via PBAP or OBEX. |
| 64 | newR1L-HFP-054 | er | 行尾多餘句號 | 3. Phone book transfer completes successfully without error. |
| 64 | newR1L-HFP-054 | er | 行尾多餘句號 | 4. The Phone Book screen opens successfully. |
| 64 | newR1L-HFP-054 | er | 行尾多餘句號 | 5. The External Downloaded Phone Book is transferred successfully, and the phone |
| 65 | newR1L-HFP-055 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device containing phonebook data is available. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 2. Trigger phone book synchronization. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 4. Open the Phonebook interface on the HU. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 5. Access the phonebook folder list. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 6. Locate the folder named “Mobile”. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 7. Open the Phone Book folder list and locate the “Mobile” folder. |
| 65 | newR1L-HFP-055 | proc | 行尾多餘句號 | 8. Verify the displayed phone number entries. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 1. The Bluetooth device is successfully paired and connected to the HU. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 2. Phone book synchronization is triggered successfully. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 3. Phone book synchronization completes successfully without error. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 4. The Phonebook interface opens successfully. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 5. The phonebook folder list is displayed. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 6. A folder named “Mobile” is present. |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 7. The “Mobile” folder is present in the Phone Book folder list and can be opene |
| 65 | newR1L-HFP-055 | er | 行尾多餘句號 | 8. Phone numbers from the external downloaded phone book are displayed correctly |
| 66 | newR1L-HFP-056 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device containing phonebook data is available. |
| 66 | newR1L-HFP-056 | pre | 行尾多餘句號 | 2. No contacts are marked as “Favorite” on the HU (Favorites list is empty). |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 2. Trigger phone book synchronization. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 4. Open the Phonebook interface on the HU. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 5. Access the phonebook folder list. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 6. Verify the presence of the “Favorites” folder in the folder list. |
| 66 | newR1L-HFP-056 | proc | 行尾多餘句號 | 7. Open the “Favorites” folder. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 1. The Bluetooth device is successfully paired and connected to the HU. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 2. Phone book synchronization is triggered successfully. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 3. Phone book synchronization completes successfully without error. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 4. The Phonebook interface opens successfully. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 5. The phonebook folder list is displayed. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 6. The “Favorites” folder is displayed in the phonebook folder list. |
| 66 | newR1L-HFP-056 | er | 行尾多餘句號 | 7. The “Favorites” folder opens successfully and shows an empty list (no favorit |
| 67 | newR1L-HFP-057 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device containing phonebook data is available. |
| 67 | newR1L-HFP-057 | pre | 行尾多餘句號 | 2. At least one contact is available on the Bluetooth device (e.g., Contact A). |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 2. Trigger phone book synchronization. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 3. Wait until synchronization is completed. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 4. Open the Phonebook interface on the HU. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 5. Mark Contact A as a “Favorite”. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 6. Open the “Favorites” folder. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 7. Verify the displayed contact information. |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 8. Unmark Contact A (remove from “Favorite”). |
| 67 | newR1L-HFP-057 | proc | 行尾多餘句號 | 9. Re-open the “Favorites” folder. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 1. The Bluetooth device is successfully paired and connected to the HU. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 2. Phone book synchronization is triggered successfully. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 3. Phone book synchronization completes successfully without error. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 4. The Phonebook interface opens successfully. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 5. Contact A is successfully marked as “Favorite”. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 6. The “Favorites” folder opens successfully. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 7. Contact A is displayed in the “Favorites” folder with correct phone number in |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 8. Contact A is successfully removed from “Favorite”. |
| 67 | newR1L-HFP-057 | er | 行尾多餘句號 | 9. The “Favorites” folder reflects the update and no longer shows Contact A. |
| 68 | newR1L-HFP-058 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status can be verified via system configuration. |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 1. Open the “App Drawer” on the menu bar. |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 2. Confirm there is a SOS app in App Drawer to verify that the E-Call/Assist-Cal |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 3. Launch the Phone application on the HU. |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 4. Navigate to the Favorites phonebook / Favorites folder. |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 5. Check whether an entry named “Emergency” is displayed in Favorites. |
| 68 | newR1L-HFP-058 | proc | 行尾多餘句號 | 6. Check whether an entry named “Towing Assistance” or “Roadside Assistance” is  |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 2. The SOS app is displayed in App Drawer. |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 3. The Phone application is launched successfully. |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 4. The Favorites phonebook / Favorites folder is displayed successfully. |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 5. The “Emergency” entry is not displayed in the Favorites folder. |
| 68 | newR1L-HFP-058 | er | 行尾多餘句號 | 6. The “Towing Assistance” and “Roadside Assistance” entry is not displayed in t |
| 69 | newR1L-HFP-059 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status can be verified via system configuration. |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 1. Open the “App Drawer” on the menu bar. |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 2. Confirm there is no SOS in App Drawer to make sure the E-Call/Assist-Call sta |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 3. Launch the Phone application on the HU. |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 4. Navigate to the Favorites phonebook / Favorites folder. |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 5. Verify that an entry named “Emergency” exists in Favorites by default. |
| 69 | newR1L-HFP-059 | proc | 行尾多餘句號 | 6. Verify that an entry named “Towing Assistance” exists in Favorites by default |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 2. The SOS app is not displayed in App Drawer. |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 3. The Phone application is launched successfully. |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 4. The Favorites phonebook / Favorites folder is displayed successfully. |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 5. The “Emergency” entry is present by default in the Favorites phonebook. |
| 69 | newR1L-HFP-059 | er | 行尾多餘句號 | 6. The “Towing Assistance” entry is present by default in the Favorites phoneboo |
| 70 | newR1L-HFP-060 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status can be verified via system configuration. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 1. Open the “App Drawer” on the menu bar. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 2. Confirm there is no SOS in App Drawer to make sure the E-Call/Assist-Call sta |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 3. Launch the Phone application on the HU. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 4. Navigate to the Favorites phonebook / Favorites folder. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 5. Select the “Emergency” entry and open the entry details. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 6. Attempt to edit and save the name field of the “Emergency” entry. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 7. Select the “Towing Assistance” entry and open the entry details. |
| 70 | newR1L-HFP-060 | proc | 行尾多餘句號 | 8. Attempt to edit and save the name field of the “Towing Assistance” entry. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 2. The SOS app is not displayed in App Drawer. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 3. The Phone application is launched successfully. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 4. The Favorites phonebook / Favorites folder is displayed successfully. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 5. The “Emergency” entry details are displayed successfully. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 6. Editing the name field of the “Emergency” entry is not allowed, and the name  |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 7. The “Towing Assistance” entry details are displayed successfully. |
| 70 | newR1L-HFP-060 | er | 行尾多餘句號 | 8. Editing the name field of the “Towing Assistance” entry is not allowed, and t |
| 71 | newR1L-HFP-061 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status can be verified via system configuration. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 1. Open the “App Drawer” on the menu bar. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 2. Confirm there is no SOS in App Drawer to make sure the E-Call/Assist-Call sta |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 3. Launch the Phone application on the HU. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 4. Navigate to the Favorites phonebook / Favorites folder. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 5. Select the “Emergency” entry and open the entry options. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 6. Attempt to delete the “Emergency” entry. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 7. Select the “Towing Assistance” entry and open the entry options. |
| 71 | newR1L-HFP-061 | proc | 行尾多餘句號 | 8. Attempt to delete the “Towing Assistance” entry. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 2. The SOS app is not displayed in App Drawer. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 3. The Phone application is launched successfully. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 4. The Favorites phonebook / Favorites folder is displayed successfully. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 5. The “Emergency” entry options are displayed successfully. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 6. The “Emergency” entry cannot be deleted and remains in the Favorites phoneboo |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 7. The “Towing Assistance” entry options are displayed successfully. |
| 71 | newR1L-HFP-061 | er | 行尾多餘句號 | 8. The “Towing Assistance” entry cannot be deleted and remains in the Favorites  |
| 72 | newR1L-HFP-062 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status is Not Supported. |
| 72 | newR1L-HFP-062 | pre | 行尾多餘句號 | 2. Market Configuration Table is available for reference. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 1. Open the “App Drawer” on the menu bar. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 2. Confirm there is no SOS in App Drawer to make sure the E-Call/Assist-Call sta |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 3. Navigate to the Favorites phonebook / Favorites folder. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 4. Open the “Emergency” entry details. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 5. Verify the phone number type of the “Emergency” entry. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 6. Compare the phone number of the “Emergency” entry with the Market Configurati |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 7. Open the “Towing Assistance” entry details. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 8. Verify the phone number type of the “Towing Assistance” entry. |
| 72 | newR1L-HFP-062 | proc | 行尾多餘句號 | 9. Compare the phone number of the “Towing Assistance” entry with the Market Con |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 2. The SOS app is not displayed in App Drawer. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 3. The Favorites phonebook / Favorites folder is displayed successfully. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 4. The “Emergency” entry details are displayed successfully. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 5. The phone number type of the “Emergency” entry is Other. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 6. The “Emergency” phone number matches the default value defined in the Market  |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 7. The “Towing Assistance” entry details are displayed successfully. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 8. The phone number type of the “Towing Assistance” entry is Other. |
| 72 | newR1L-HFP-062 | er | 行尾多餘句號 | 9. The “Towing Assistance” phone number matches the default value defined in the |
| 73 | newR1L-HFP-063 | pre | 行尾多餘句號 | 1. E-Call/Assist-Call support status is Not Supported. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 1. Verify that the E-Call/Assist-Call support status is Not Supported. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 2. Navigate to the Favorites phonebook / Favorites folder. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 3. Navigate to the Favorites phonebook / Favorites folder. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 4. Open the “Emergency” entry details. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 5. Verify the phone number type of the “Emergency” entry. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 6. Edit the phone number field of the “Emergency” entry to a new value and save. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 7. Re-open the “Emergency” entry details. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 8. Open the “Towing Assistance” entry details. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 9. Verify the phone number type of the “Towing Assistance” entry. |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 10. Edit the phone number field of the “Towing Assistance” entry to a new value  |
| 73 | newR1L-HFP-063 | proc | 行尾多餘句號 | 11. Re-open the “Towing Assistance” entry details. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 1. The App Drawer page is displayed. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 2. The SOS app is not displayed in App Drawer. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 3. The Favorites phonebook / Favorites folder is displayed successfully. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 4. The “Emergency” entry details are displayed successfully. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 5. The phone number type of the “Emergency” entry is Other. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 6. Editing the “Emergency” phone number field is allowed, and the new value is s |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 7. The “Emergency” phone number field shows the updated value. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 8. The “Towing Assistance” entry details are displayed successfully. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 9. The phone number type of the “Towing Assistance” entry is Other. |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 10. Editing the “Towing Assistance” phone number field is allowed, and the new v |
| 73 | newR1L-HFP-063 | er | 行尾多餘句號 | 11. The “Towing Assistance” phone number field shows the updated value. |
| 74 | newR1L-HFP-064 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device is available. |
| 74 | newR1L-HFP-064 | pre | 行尾多餘句號 | 2. No Call In Progress on both HU and the paired device. |
| 74 | newR1L-HFP-064 | pre | 行尾多餘句號 | 3. Power management logs are enabled. |
| 74 | newR1L-HFP-064 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 74 | newR1L-HFP-064 | proc | 行尾多餘句號 | 2. Confirm there is no call in progress on both the HU and the paired device. |
| 74 | newR1L-HFP-064 | proc | 行尾多餘句號 | 3. Stop all user interactions and keep the HU idle. |
| 74 | newR1L-HFP-064 | proc | 行尾多餘句號 | 4. Wait until the configured idle timeout is reached. |
| 74 | newR1L-HFP-064 | proc | 行尾多餘句號 | 5. Observe the HU behavior and collect system logs during the idle period and sl |
| 74 | newR1L-HFP-064 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 74 | newR1L-HFP-064 | er | 行尾多餘句號 | 2. The HU indicates no active call and remains in a normal operational state. |
| 74 | newR1L-HFP-064 | er | 行尾多餘句號 | 3. The HU remains idle without abnormal wake-up or blocking behavior. |
| 74 | newR1L-HFP-064 | er | 行尾多餘句號 | 4. After the idle timeout expires, the HU enters sleep mode as defined in the Co |
| 75 | newR1L-HFP-065 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device is available. |
| 75 | newR1L-HFP-065 | pre | 行尾多餘句號 | 2. No Call In Progress on both HU and the paired device. |
| 75 | newR1L-HFP-065 | pre | 行尾多餘句號 | 3. Power management logs are enabled. |
| 75 | newR1L-HFP-065 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 75 | newR1L-HFP-065 | proc | 行尾多餘句號 | 2. Confirm there is no call in progress on both the HU and the paired device. |
| 75 | newR1L-HFP-065 | proc | 行尾多餘句號 | 3. Stop all user interactions and keep the HU idle. |
| 75 | newR1L-HFP-065 | proc | 行尾多餘句號 | 4. Observe whether the HU enters sleep mode after X seconds of idle time and rec |
| 75 | newR1L-HFP-065 | proc | 行尾多餘句號 | 5. Collect logs covering the idle period and sleep transition. |
| 75 | newR1L-HFP-065 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 75 | newR1L-HFP-065 | er | 行尾多餘句號 | 2. The HU remains in a normal power management state under no-call condition. |
| 75 | newR1L-HFP-065 | er | 行尾多餘句號 | 3. After X seconds of idle time, the HU enters sleep mode. |
| 75 | newR1L-HFP-065 | er | 行尾多餘句號 | 4. The observed sleep entry timing is consistent with the defined idle timeout d |
| 75 | newR1L-HFP-065 | er | 行尾多餘句號 | 5. Logs confirm the Idle → Sleep transition and provide timestamp evidence of th |
| 76 | newR1L-HFP-066 | pre | 行尾多餘句號 | 1. A PBAP-supported Bluetooth device is available. |
| 76 | newR1L-HFP-066 | pre | 行尾多餘句號 | 2. No Call In Progress on both HU and the paired device. |
| 76 | newR1L-HFP-066 | pre | 行尾多餘句號 | 3. Power management logs are enabled. |
| 76 | newR1L-HFP-066 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 76 | newR1L-HFP-066 | proc | 行尾多餘句號 | 2. Confirm no call is in progress on both the HU and the paired device. |
| 76 | newR1L-HFP-066 | proc | 行尾多餘句號 | 3. Capture current power state and related logs. |
| 76 | newR1L-HFP-066 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 76 | newR1L-HFP-066 | er | 行尾多餘句號 | 2. No call in progress is indicated on both the HU and the paired device. |
| 77 | newR1L-HFP-067 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU via Bluetooth. |
| 77 | newR1L-HFP-067 | proc | 行尾多餘句號 | 2. Confirm no call is in progress on both the HU and the paired device. |
| 77 | newR1L-HFP-067 | proc | 行尾多餘句號 | 3. Stop all user interactions and keep the HU idle. |
| 77 | newR1L-HFP-067 | proc | 行尾多餘句號 | 4. Maintain idle condition for X seconds and record sleep entry timestamp. |
| 77 | newR1L-HFP-067 | proc | 行尾多餘句號 | 5. Extract logs covering idle-to-sleep transition. |
| 77 | newR1L-HFP-067 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 77 | newR1L-HFP-067 | er | 行尾多餘句號 | 2. No call in progress is indicated on both the HU and the paired device. |
| 77 | newR1L-HFP-067 | er | 行尾多餘句號 | 3. HU remains in defined normal power management state during idle. |
| 77 | newR1L-HFP-067 | er | 行尾多餘句號 | 4. HU enters sleep mode after X seconds; sleep entry timestamp is recorded. |
| 77 | newR1L-HFP-067 | er | 行尾多餘句號 | 5. Logs show Idle → Sleep transition with timestamp evidence consistent with X s |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 1. Pair the PBAP-supported device with the HU. |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 2. Establish an active call session. |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 3. Stop user interaction and allow idle timeout duration (X seconds). |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 4. Terminate the call. |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 5. Allow idle timeout duration (X seconds). |
| 78 | newR1L-HFP-068 | proc | 行尾多餘句號 | 6. Capture power state transition logs. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 1. The device is successfully paired and connected. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 2. Active call session is established. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 3. Sleep transition is not triggered while call is active. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 4. Call termination event is recorded. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 5. Sleep transition occurs after idle timeout once call flag = FALSE. |
| 78 | newR1L-HFP-068 | er | 行尾多餘句號 | 6. Logs show state transition sequence aligned with Common Power Management Stat |
| 79 | newR1L-HFP-069 | pre | 行尾多餘句號 | 1. A Bluetooth device supporting hands-free profile is available. |
| 79 | newR1L-HFP-069 | pre | 行尾多餘句號 | 2. Power management and Bluetooth logs are enabled. |
| 79 | newR1L-HFP-069 | proc | 行尾多餘句號 | 1. Pair the Bluetooth device with the HU. |
| 79 | newR1L-HFP-069 | proc | 行尾多餘句號 | 2. Establish an active hands-free call. |
| 79 | newR1L-HFP-069 | proc | 行尾多餘句號 | 3. Transition ignition state from ON to Ignition Pre-Off. |
| 79 | newR1L-HFP-069 | proc | 行尾多餘句號 | 4. Transition ignition state from Ignition Pre-Off to Ignition Off. |
| 79 | newR1L-HFP-069 | proc | 行尾多餘句號 | 5. Capture call status, Bluetooth state, and power-state logs. |
| 79 | newR1L-HFP-069 | er | 行尾多餘句號 | 1. The Bluetooth device is connected with HFP profile established. |
| 79 | newR1L-HFP-069 | er | 行尾多餘句號 | 2. The call session state changes to ACTIVE. |
| 79 | newR1L-HFP-069 | er | 行尾多餘句號 | 3. The call remains ongoing during Ignition Pre-Off. |
| 79 | newR1L-HFP-069 | er | 行尾多餘句號 | 4. The call remains ongoing during Ignition Off. |
| 79 | newR1L-HFP-069 | er | 行尾多餘句號 | 5. The Bluetooth HFP connection state remains CONNECTED throughout the ignition  |
| 80 | newR1L-HFP-070 | pre | 行尾多餘句號 | 1. A Bluetooth device supporting hands-free profile is available. |
| 80 | newR1L-HFP-070 | pre | 行尾多餘句號 | 2. Power management and Bluetooth logs are enabled. |
| 80 | newR1L-HFP-070 | proc | 行尾多餘句號 | 1. Pair the Bluetooth device with the HU. |
| 80 | newR1L-HFP-070 | proc | 行尾多餘句號 | 2. Confirm no call is in progress. |
| 80 | newR1L-HFP-070 | proc | 行尾多餘句號 | 3. Transition ignition state from ON to Ignition Pre-Off. |
| 80 | newR1L-HFP-070 | proc | 行尾多餘句號 | 4. Transition ignition state from Ignition Pre-Off to Ignition Off. |
| 80 | newR1L-HFP-070 | proc | 行尾多餘句號 | 5. Capture power-state logs during transitions. |
| 80 | newR1L-HFP-070 | er | 行尾多餘句號 | 1. The Bluetooth device is connected successfully. |
| 80 | newR1L-HFP-070 | er | 行尾多餘句號 | 2. Call state remains IDLE. |
| 80 | newR1L-HFP-070 | er | 行尾多餘句號 | 3. HU transitions to the defined power state for Ignition Pre-Off. |
| 80 | newR1L-HFP-070 | er | 行尾多餘句號 | 4. HU transitions to the defined power state for Ignition Off. |
| 80 | newR1L-HFP-070 | er | 行尾多餘句號 | 5. No call-related event blocks the ignition state transitions. |
| 81 | newR1L-HFP-071 | pre | 行尾多餘句號 | 1. A Bluetooth device supporting hands-free profile is available. |
| 81 | newR1L-HFP-071 | pre | 行尾多餘句號 | 2. Power management and Bluetooth logs are enabled. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 1. Pair the Bluetooth device with the HU. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 2. Establish an active hands-free call. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 3. Transition ignition state to Ignition Off. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 4. Terminate the active call. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 5. Wait for the configured power-down delay. |
| 81 | newR1L-HFP-071 | proc | 行尾多餘句號 | 6. Capture Bluetooth and power-state logs. |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 1. The Bluetooth device is connected with HFP profile established. |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 2. The call session state changes to ACTIVE. |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 3. The call remains ongoing after Ignition Off transition. |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 4. The call state changes from ACTIVE to TERMINATED. |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 5. The Bluetooth HFP connection state changes from CONNECTED to DISCONNECTED aft |
| 81 | newR1L-HFP-071 | er | 行尾多餘句號 | 6. HU transitions to the lowest power state after call termination. |
| 82 | newR1L-HFP-072 | pre | 行尾多餘句號 | 1. No HFP-capable device is paired with the HU. |
| 82 | newR1L-HFP-072 | proc | 行尾多餘句號 | 1. Access the “Phone Devices” screen. |
| 82 | newR1L-HFP-072 | proc | 行尾多餘句號 | 2. Check the displayed UI state. |
| 82 | newR1L-HFP-072 | er | 行尾多餘句號 | 1. The device list screen is displayed. |
| 82 | newR1L-HFP-072 | er | 行尾多餘句號 | 2. The UI displays the the empty-state message “Go to Device Manager to add or c |
| 83 | newR1L-HFP-073 | pre | 行尾多餘句號 | 1. An HFP-capable Bluetooth device is available. |
| 83 | newR1L-HFP-073 | pre | 行尾多餘句號 | 2. Bluetooth capability detection logs are enabled. |
| 83 | newR1L-HFP-073 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 83 | newR1L-HFP-073 | proc | 行尾多餘句號 | 2. Access the “Device Manager” screen. |
| 83 | newR1L-HFP-073 | proc | 行尾多餘句號 | 3. Check the displayed device list. |
| 83 | newR1L-HFP-073 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 83 | newR1L-HFP-073 | er | 行尾多餘句號 | 2. The device list screen is displayed. |
| 83 | newR1L-HFP-073 | er | 行尾多餘句號 | 3. The paired HFP-capable device is shown in the list. |
| 84 | newR1L-HFP-074 | pre | 行尾多餘句號 | 1. A non-HFP Bluetooth device is available (e.g., A2DP-only). |
| 84 | newR1L-HFP-074 | pre | 行尾多餘句號 | 2. Bluetooth capability detection logs are enabled. |
| 84 | newR1L-HFP-074 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 84 | newR1L-HFP-074 | proc | 行尾多餘句號 | 2. Access the “Device Manager” screen. |
| 84 | newR1L-HFP-074 | proc | 行尾多餘句號 | 3. Check the displayed device list. |
| 84 | newR1L-HFP-074 | er | 行尾多餘句號 | 1. The non-HFP device is paired successfully. |
| 84 | newR1L-HFP-074 | er | 行尾多餘句號 | 2. The device list screen is displayed. |
| 84 | newR1L-HFP-074 | er | 行尾多餘句號 | 3. The paired non-HFP device is not shown in the list. |
| 85 | newR1L-HFP-075 | pre | 行尾多餘句號 | 1. A mixed-profile Bluetooth device is available (HFP + other profiles). |
| 85 | newR1L-HFP-075 | pre | 行尾多餘句號 | 2. Bluetooth capability detection logs are enabled. |
| 85 | newR1L-HFP-075 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 85 | newR1L-HFP-075 | proc | 行尾多餘句號 | 2. Access the “Device Manager” screen. |
| 85 | newR1L-HFP-075 | proc | 行尾多餘句號 | 3. Check the displayed device list. |
| 85 | newR1L-HFP-075 | er | 行尾多餘句號 | 1. The mixed-profile device is paired successfully. |
| 85 | newR1L-HFP-075 | er | 行尾多餘句號 | 2. The device list screen is displayed. |
| 85 | newR1L-HFP-075 | er | 行尾多餘句號 | 3. The paired mixed-profile device is shown in the list. |
| 86 | newR1L-HFP-076 | pre | 行尾多餘句號 | 2. Bluetooth capability detection logs are enabled. |
| 86 | newR1L-HFP-076 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 86 | newR1L-HFP-076 | proc | 行尾多餘句號 | 2. Pair the non-HFP device with the HU. |
| 86 | newR1L-HFP-076 | proc | 行尾多餘句號 | 3. Pair the mixed-profile device with the HU. |
| 86 | newR1L-HFP-076 | proc | 行尾多餘句號 | 4. Access the “Device Manager” screen. |
| 86 | newR1L-HFP-076 | proc | 行尾多餘句號 | 5. Check the displayed device list. |
| 86 | newR1L-HFP-076 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 86 | newR1L-HFP-076 | er | 行尾多餘句號 | 2. The non-HFP device is paired successfully. |
| 86 | newR1L-HFP-076 | er | 行尾多餘句號 | 3. The mixed-profile device is paired successfully. |
| 86 | newR1L-HFP-076 | er | 行尾多餘句號 | 4. The device list screen is displayed. |
| 86 | newR1L-HFP-076 | er | 行尾多餘句號 | 5. The list shows only the HFP-capable device and the mixed-profile device; the  |
| 87 | newR1L-HFP-077 | pre | 行尾多餘句號 | 1. HFP-capable Bluetooth devices are available. |
| 87 | newR1L-HFP-077 | proc | 行尾多餘句號 | 1. Access the “Phone Devices” screen. |
| 87 | newR1L-HFP-077 | proc | 行尾多餘句號 | 2. Pair a new HFP-capable device with the HU. |
| 87 | newR1L-HFP-077 | proc | 行尾多餘句號 | 3. Remain on the device list screen. |
| 87 | newR1L-HFP-077 | proc | 行尾多餘句號 | 4. Check the updated device list. |
| 87 | newR1L-HFP-077 | er | 行尾多餘句號 | 1. The device list screen is displayed. |
| 87 | newR1L-HFP-077 | er | 行尾多餘句號 | 2. The new HFP-capable device is paired successfully. |
| 87 | newR1L-HFP-077 | er | 行尾多餘句號 | 3. The device list refreshes automatically. |
| 87 | newR1L-HFP-077 | er | 行尾多餘句號 | 4. The newly paired HFP-capable device appears in the list without manual refres |
| 88 | newR1L-HFP-078 | pre | 行尾多餘句號 | 1. An HFP-capable Bluetooth device is available. |
| 88 | newR1L-HFP-078 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 88 | newR1L-HFP-078 | proc | 行尾多餘句號 | 2. Access the “Phone Devices” screen. |
| 88 | newR1L-HFP-078 | proc | 行尾多餘句號 | 3. Confirm the paired HFP device appears in the list. |
| 88 | newR1L-HFP-078 | proc | 行尾多餘句號 | 4. Remove (Forget) the selected HFP device from the HU. |
| 88 | newR1L-HFP-078 | proc | 行尾多餘句號 | 5. Check the updated device list. |
| 88 | newR1L-HFP-078 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 88 | newR1L-HFP-078 | er | 行尾多餘句號 | 2. The device list screen is displayed. |
| 88 | newR1L-HFP-078 | er | 行尾多餘句號 | 3. The paired HFP device is shown in the list. |
| 88 | newR1L-HFP-078 | er | 行尾多餘句號 | 4. The device is removed successfully from the HU. |
| 88 | newR1L-HFP-078 | er | 行尾多餘句號 | 5. The device list refreshes automatically and the removed device no longer appe |
| 89 | newR1L-HFP-079 | pre | 行尾多餘句號 | 1. An HFP-capable Bluetooth device is available. |
| 89 | newR1L-HFP-079 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 89 | newR1L-HFP-079 | proc | 行尾多餘句號 | 2. Access the “Phone Devices” screen. |
| 89 | newR1L-HFP-079 | proc | 行尾多餘句號 | 3. Confirm the paired HFP device appears in the list. |
| 89 | newR1L-HFP-079 | proc | 行尾多餘句號 | 4. On the mobile device, remove (unpair) the HU from Bluetooth settings. |
| 89 | newR1L-HFP-079 | proc | 行尾多餘句號 | 5. Check the updated device list. |
| 89 | newR1L-HFP-079 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 89 | newR1L-HFP-079 | er | 行尾多餘句號 | 2. The device list screen is displayed. |
| 89 | newR1L-HFP-079 | er | 行尾多餘句號 | 3. The paired HFP device is shown in the list. |
| 89 | newR1L-HFP-079 | er | 行尾多餘句號 | 4. The Bluetooth bond state changes to unpaired. |
| 89 | newR1L-HFP-079 | er | 行尾多餘句號 | 5. The device list refreshes automatically and the unpaired device no longer app |
| 90 | newR1L-HFP-080 | pre | 行尾多餘句號 | 1. No Bluetooth devices supporting HFP are paired with the HU. |
| 90 | newR1L-HFP-080 | proc | 行尾多餘句號 | 1. Access the “Device Manager” screen. |
| 90 | newR1L-HFP-080 | proc | 行尾多餘句號 | 2. Observe the device list content. |
| 90 | newR1L-HFP-080 | proc | 行尾多餘句號 | 3. Observe the UI message displayed when the list is empty. |
| 90 | newR1L-HFP-080 | er | 行尾多餘句號 | 1. The Device Manager screen is displayed. |
| 90 | newR1L-HFP-080 | er | 行尾多餘句號 | 2. No HFP-capable Bluetooth device is listed. |
| 90 | newR1L-HFP-080 | er | 行尾多餘句號 | 3. The system displays an empty-state list. |
| 91 | newR1L-HFP-081 | pre | 行尾多餘句號 | 1. At least one HFP-capable Bluetooth device is available. |
| 91 | newR1L-HFP-081 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 91 | newR1L-HFP-081 | proc | 行尾多餘句號 | 2. Access the “Phone Devices” screen. |
| 91 | newR1L-HFP-081 | proc | 行尾多餘句號 | 3. Select the listed HFP-capable device. |
| 91 | newR1L-HFP-081 | proc | 行尾多餘句號 | 4. Initiate an outgoing call. |
| 91 | newR1L-HFP-081 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 91 | newR1L-HFP-081 | er | 行尾多餘句號 | 2. The device appears in the list. |
| 91 | newR1L-HFP-081 | er | 行尾多餘句號 | 3. The selected device is marked as active in the UI. |
| 91 | newR1L-HFP-081 | er | 行尾多餘句號 | 4. The outgoing call audio is routed through the selected HFP device. |
| 92 | newR1L-HFP-082 | pre | 行尾多餘句號 | 1. At least one HFP-capable Bluetooth device is available. |
| 92 | newR1L-HFP-082 | proc | 行尾多餘句號 | 1. Pair the HFP-capable device with the HU. |
| 92 | newR1L-HFP-082 | proc | 行尾多餘句號 | 2. Access the “Phone Devices” screen. |
| 92 | newR1L-HFP-082 | proc | 行尾多餘句號 | 3. Select the listed HFP-capable device. |
| 92 | newR1L-HFP-082 | proc | 行尾多餘句號 | 4. Trigger an incoming call to the paired mobile device. |
| 92 | newR1L-HFP-082 | er | 行尾多餘句號 | 1. The HFP-capable device is paired successfully. |
| 92 | newR1L-HFP-082 | er | 行尾多餘句號 | 2. The device appears in the list. |
| 92 | newR1L-HFP-082 | er | 行尾多餘句號 | 3. The selected device is marked as active in the UI. |
| 92 | newR1L-HFP-082 | er | 行尾多餘句號 | 4. The incoming call audio is routed through the selected HFP device. |
| 93 | newR1L-HFP-083 | pre | 行尾多餘句號 | 1. At least two HFP-capable Bluetooth devices are available. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 1. Pair the first HFP-capable device with the HU. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 2. Pair the second HFP-capable device with the HU. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 3. Access the “Phone Devices” screen. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 4. Select the first device. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 5. Initiate an outgoing call and end the call. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 6. Select the second device. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 7. Confirm the active indicator status for both devices. |
| 93 | newR1L-HFP-083 | proc | 行尾多餘句號 | 8. Initiate another outgoing call. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 1. Both HFP-capable devices are paired successfully. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 2. Both devices appear in the list. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 3. The device list screen is displayed. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 4. The first selected device is marked as active. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 5. The outgoing call audio is routed through the first device and the call ends  |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 6. The second selected device is marked as active. |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 7. Only the second device is marked as active; the first device is not marked as |
| 93 | newR1L-HFP-083 | er | 行尾多餘句號 | 8. The outgoing call audio is routed through the second device. |
| 94 | newR1L-HFP-084 | pre | 行尾多餘句號 | 1. At least two HFP-capable Bluetooth devices are available. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 1. Pair the first HFP-capable device with the HU. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 2. Pair the second HFP-capable device with the HU. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 3. Access the “Phone Devices” screen. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 4. Select the first device. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 5. Trigger an incoming call to the first paired mobile device and end the call. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 6. Select the second device. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 7. Confirm the active indicator status for both devices. |
| 94 | newR1L-HFP-084 | proc | 行尾多餘句號 | 8. Trigger an incoming call to the second paired mobile device. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 1. Both HFP-capable devices are paired successfully. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 2. Both devices appear in the list. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 3. The device list screen is displayed. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 4. The first selected device is marked as active. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 5. The incoming call audio is routed through the first device and the call ends  |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 6. The second selected device is marked as active. |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 7. Only the second device is marked as active; the first device is not marked as |
| 94 | newR1L-HFP-084 | er | 行尾多餘句號 | 8. The incoming call audio is routed through the second device. |
| 95 | newR1L-HFP-045 | pre | 行尾多餘句號 | 2. A Bluetooth device that does not support phone status reporting is available. |
| 95 | newR1L-HFP-045 | pre | 行尾多餘句號 | 2. A Bluetooth device that supports phone status reporting is available. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 3. Pairing a phone that supports status information via Bluetooth. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 4. Press "Phone" app on menu bar to go to Phone page. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 6. Check the content of the Phone status information bar. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 1. Pair the supported device with the HU. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 2. Open the Phone application page. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 3. Confirm the paired device is set as the active phone. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 4. Check the phone status information area on the Phone page. |
| 95 | newR1L-HFP-045 | proc | 行尾多餘句號 | 5. Compare the displayed battery and signal values with the actual phone status. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 3. The Phone is paired and Bluetooth is connected. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 5. Phone status information bar is displayed at the bottom of the phone page. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 1. The device is paired successfully and Bluetooth is connected. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 3. The selected device is set as the active phone. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 4. The phone status information area is displayed on the Phone page. |
| 95 | newR1L-HFP-045 | er | 行尾多餘句號 | 5. The battery level and cellular signal strength icons are displayed and match  |
| 96 | newR1L-HFP-046 | pre | 行尾多餘句號 | 2. A Bluetooth device that does not support phone status reporting is available. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 1. Pairing a phone that Not supports status information via Bluetooth. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 4. Press "Phone" app on menu bar to go to Phone page. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 6. Check the content of the Phone status information bar. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 1. Pair the unsupported device with the HU. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 2. Open the Phone application page. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 3. Confirm the paired device is set as the active phone. |
| 96 | newR1L-HFP-046 | proc | 行尾多餘句號 | 4. Check the phone status information area on the Phone page. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 5. Phone status information bar is displayed at the bottom of the phone page. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 6. No status information icon displayed on Phone status information bar. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 2. The Phone application page is displayed. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 3. The device is set as the active phone. |
| 96 | newR1L-HFP-046 | er | 行尾多餘句號 | 4. No battery or cellular signal icons are displayed, or the default behavior de |
| 97 | newR1L-HFP-047 | pre | 行尾多餘句號 | 2. A Bluetooth device that supports phone status reporting is available. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 1. Pair the supported device with the HU. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 4. Set the device's battery level to 90%. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 5. Press "Phone" app to check the Battery level icon. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 6. Set the device's battery level to 20%. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 7. Check the Battery level icon. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 8. Charge the device and check the battery level icon. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 1. Pair the supported device with the HU. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 2. Ensure the device is selected as the active phone. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 3. Set the phone battery level to a high level (e.g., ~90%) by charging the devi |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 4. Check that the corresponding battery icon is displayed on the HU. |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 5. Allow the battery level to decrease (e.g., ~20%). |
| 97 | newR1L-HFP-047 | proc | 行尾多餘句號 | 6. Check the battery icon on the HU updates accordingly. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 4. Battery level is set to 90%. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 5. The battery level is displayed as a 90% icon. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 6. Battery level is set to 20%. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 7. The battery level is displayed as a 20% icon. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 8. The battery level is displayed as a green charging icon. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 2. The paired device is set as the active phone. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 3. The phone battery level is reported to the HU. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 4. The HU displays the corresponding battery level icon according to the reporte |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 5. The updated battery level information is received from the phone. |
| 97 | newR1L-HFP-047 | er | 行尾多餘句號 | 6. The battery level icon on the HU is updated accordingly to reflect the change |
| 98 | newR1L-HFP-048 | pre | 行尾多餘句號 | 2. A Bluetooth device that supports phone status reporting is available. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 4. Send the Excellent Signal from device. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 5. Press "Phone" app to check the Signal Strength icon. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 6. Send the Weak Signal from device and check the Signal Strength icon. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 7. Send the Roam Signal from device and check the Signal Strength icon. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 1. Pair the supported device with the HU. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 2. Ensure the device is selected as the active phone. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 3. Place the phone in a location with strong signal strength. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 4. Check that the corresponding signal strength icon is displayed on the HU. |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 5. Move the phone to a location with weak signal strength (e.g., shield the devi |
| 98 | newR1L-HFP-048 | proc | 行尾多餘句號 | 6. Check the signal strength icon on the HU updates accordingly. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 4. Excellent Signal is sent by Device. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 5. The Signal Strength icon displayed in Excellent status. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 6. The Signal Strength icon displayed in Weak status. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 7. The Signal Strength icon displayed in Roaming status. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 1. The device is successfully paired and connected to the HU. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 2. The paired device is set as the active phone. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 3. The phone reports signal strength information to the HU. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 4. The HU displays the corresponding signal strength icon based on the reported  |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 5. Updated signal strength information is received from the phone. |
| 98 | newR1L-HFP-048 | er | 行尾多餘句號 | 6. The signal strength icon on the HU updates dynamically to reflect the changed |
| 99 |  | pre | 行尾多餘句號 | 2. Two Bluetooth devices that support phone status reporting is available. |
| 99 |  | proc | 行尾多餘句號 | 1. Pair both supported devices with the HU. |
| 99 |  | proc | 行尾多餘句號 | 2. Open the Phone application page. |
| 99 |  | proc | 行尾多餘句號 | 3. Confirm both paired devices are shown as available devices. |
| 99 |  | proc | 行尾多餘句號 | 4. Select the first device as the active phone. |
| 99 |  | proc | 行尾多餘句號 | 5. Check that the displayed phone status icons correspond to the first device. |
| 99 |  | proc | 行尾多餘句號 | 6. Select the second device as the active phone. |
| 99 |  | proc | 行尾多餘句號 | 7. Check that the displayed phone status icons correspond to the second device. |
| 99 |  | er | 行尾多餘句號 | 1. Both devices are successfully paired and connected to the HU. |
| 99 |  | er | 行尾多餘句號 | 2. The Phone application page is displayed. |
| 99 |  | er | 行尾多餘句號 | 3. Both devices are shown as available devices. |
| 99 |  | er | 行尾多餘句號 | 4. The first device is set as the active phone. |
| 99 |  | er | 行尾多餘句號 | 5. The displayed battery and signal icons correspond to the first device status. |
| 99 |  | er | 行尾多餘句號 | 6. The second device becomes the active phone. |
| 99 |  | er | 行尾多餘句號 | 7. The displayed battery and signal icons update to reflect the second device st |
| 100 | newR1L-HFP-049 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 4. Make a Call. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 5. Press "Microphone" soft key to trigger the VR. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 你的測試(描述)就是在講測試micro soft key但是測試最後樓歪，起手想法很好 先確認UI 但維持單一目的，測項初衷。 |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 1. Pair a Bluetooth phone with the HU. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 2. Initiate or receive a phone call. |
| 100 | newR1L-HFP-049 | proc | 行尾多餘句號 | 3. Check the in-call screen. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 4. Call is connected. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 5. VR has been launched. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 2. The call is established. |
| 100 | newR1L-HFP-049 | er | 行尾多餘句號 | 3. A microphone softkey with a microphone icon is displayed on the touchscreen. |
| 101 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 101 |  | proc | 行尾多餘句號 | 2. Press the Hold button. |
| 101 |  | proc | 行尾多餘句號 | 3. Confirm the call state changes to Hold. |
| 101 |  | proc | 行尾多餘句號 | 4. Press the microphone softkey. |
| 101 |  | er | 行尾多餘句號 | 1. The call is established. |
| 101 |  | er | 行尾多餘句號 | 2. The call enters Hold state. |
| 101 |  | er | 行尾多餘句號 | 3. The UI indicates that the call is on hold. |
| 101 |  | er | 行尾多餘句號 | 4. The microphone state does not change while the call is on hold. |
| 102 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 102 |  | proc | 行尾多餘句號 | 2.  Press the Hold button. |
| 102 |  | proc | 行尾多餘句號 | 3. Resume the call. |
| 102 |  | proc | 行尾多餘句號 | 4. Press the microphone softkey. |
| 102 |  | er | 行尾多餘句號 | 1. The call is established. |
| 102 |  | er | 行尾多餘句號 | 2. The call enters Hold state. |
| 102 |  | er | 行尾多餘句號 | 3. The call resumes. |
| 102 |  | er | 行尾多餘句號 | 4. |
| 103 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 103 |  | proc | 行尾多餘句號 | 2. Confirm the microphone softkey is displayed. |
| 103 |  | proc | 行尾多餘句號 | 3. End the call. |
| 103 |  | proc | 行尾多餘句號 | 4. Check the end-call screen. |
| 103 |  | er | 行尾多餘句號 | 1. The call is active. |
| 103 |  | er | 行尾多餘句號 | 2. The microphone softkey is displayed. |
| 103 |  | er | 行尾多餘句號 | 3. The call is terminated. |
| 103 |  | er | 行尾多餘句號 | 4. The microphone softkey (microphone icon) is no longer displayed on the touchs |
| 104 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 104 |  | proc | 行尾多餘句號 | 2. Press the "Microphone" softkey to mute. |
| 104 |  | proc | 行尾多餘句號 | 3. Press the "Microphone" softkey again to unmute. |
| 104 |  | er | 行尾多餘句號 | 1. The call is active and the in-call screen is displayed. |
| 104 |  | er | 行尾多餘句號 | 2. The microphone state changes to Mute and the UI reflects the muted status. |
| 104 |  | er | 行尾多餘句號 | 3. The microphone state changes to Unmute and the UI reflects the unmuted status |
| 105 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 105 |  | proc | 行尾多餘句號 | 2. Say "Mute" to mute the microphone. |
| 105 |  | proc | 行尾多餘句號 | 3. Say "Unmute" to unmute the microphone. |
| 105 |  | er | 行尾多餘句號 | 1. The call is active and the in-call screen is displayed. |
| 105 |  | er | 行尾多餘句號 | 2. The microphone state changes to Mute and the UI reflects the muted status. |
| 105 |  | er | 行尾多餘句號 | 3. The microphone state changes to Unmute and the UI reflects the unmuted status |
| 106 |  | proc | 行尾多餘句號 | 1. Establish a phone call. |
| 106 |  | proc | 行尾多餘句號 | 2. Say "Mute" to mute the microphone. |
| 106 |  | proc | 行尾多餘句號 | 3. Press the "Microphone" softkey to unmute. |
| 106 |  | er | 行尾多餘句號 | 1. The call is active and the in-call screen is displayed. |
| 106 |  | er | 行尾多餘句號 | 2. The microphone state changes to Mute and the UI reflects the muted status. |
| 106 |  | er | 行尾多餘句號 | 3. The microphone state changes to Unmute and the UI reflects the unmuted status |
| 107 | newR1L-HFP-050 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 4. Receive an Incoming Call. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 5. Press "Microphone" soft key to trigger the VR. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 6. Say "Mute" to Microphone. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 7. Press "Microphone" soft key again to trigger the VR. |
| 107 | newR1L-HFP-050 | proc | 行尾多餘句號 | 8. Say "Unmute" to Microphone. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 4. Call is connected. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 5. VR has been launched. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 6. The Phone Call status is muted. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 7. VR has been launched. |
| 107 | newR1L-HFP-050 | er | 行尾多餘句號 | 8. The Phone Call status is Unmuted. |
| 108 | newR1L-HFP-051 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 4. Make an Outgoing Call. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 5. Press "Microphone" soft key to trigger the VR. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 6. Say "Mute" to Microphone. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 7. Press "Microphone" soft key again to trigger the VR. |
| 108 | newR1L-HFP-051 | proc | 行尾多餘句號 | 8. Say "Unmute" to Microphone. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 4. Call is connected. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 5. VR has been launched. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 6. The Phone Call status is muted. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 7. VR has been launched. |
| 108 | newR1L-HFP-051 | er | 行尾多餘句號 | 8. The Phone Call status is Unmuted. |
| 109 | newR1L-HFP-052 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 4. Make an Outgoing Call. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 6. Press "Microphone" soft key to trigger the VR. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 7. Say "Mute" to Microphone. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 8. Press "Microphone" soft key again to trigger the VR. |
| 109 | newR1L-HFP-052 | proc | 行尾多餘句號 | 9. Say "Unmute" to Microphone. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 4. Call is connected. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 5. The Call is held. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 6. VR has been launched. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 7. The Phone Call status is muted. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 8. VR has been launched. |
| 109 | newR1L-HFP-052 | er | 行尾多餘句號 | 9. The Phone Call status is Unmuted. |
| 110 | newR1L-HFP-053 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 4. Receive an Incoming Call. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 5. Press "Microphone" soft key to trigger the VR. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 6. Say "Mute" to Microphone. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 7. Press "Microphone" soft key again to trigger the VR. |
| 110 | newR1L-HFP-053 | proc | 行尾多餘句號 | 8. Say "Unmute" to Microphone. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 4. Call is connected. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 5. VR has been launched. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 6. The Phone Call status is muted. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 7. VR has been launched. |
| 110 | newR1L-HFP-053 | er | 行尾多餘句號 | 8. The Phone Call status is Unmuted. |
| 111 | newR1L-HFP-054 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 4. Make an Outgoing Call. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 5. Press "Microphone" soft key to trigger the VR. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 6. Say "Mute" to Microphone. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 7. Press "Microphone" soft key again to trigger the VR. |
| 111 | newR1L-HFP-054 | proc | 行尾多餘句號 | 8. Say "Unmute" to Microphone. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 4. Call is connected. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 5. VR has been launched. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 6. The Phone Call status is muted. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 7. VR has been launched. |
| 111 | newR1L-HFP-054 | er | 行尾多餘句號 | 8. The Phone Call status is Unmuted. |
| 112 | newR1L-HFP-055 | pre | 行尾多餘句號 | 2. Microphone is conneced. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 4. Make an Outgoing Call. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 6. Press "Microphone" soft key to trigger the VR. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 7. Say "Mute" to Microphone. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 8. Press "Microphone" soft key again to trigger the VR. |
| 112 | newR1L-HFP-055 | proc | 行尾多餘句號 | 9. Say "Unmute" to Microphone. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 4. Call is connected. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 5. The Call is held. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 6. VR has been launched. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 7. The Phone Call status is muted. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 8. VR has been launched. |
| 112 | newR1L-HFP-055 | er | 行尾多餘句號 | 9. The Phone Call status is Unmuted. |
| 113 |  | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 113 |  | proc | 行尾多餘句號 | 2. Ensure the incoming phone number is not stored in the phonebook. |
| 113 |  | proc | 行尾多餘句號 | 3. Receive an incoming call from the device. |
| 113 |  | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen. |
| 113 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 113 |  | er | 行尾多餘句號 | 2. The incoming phone number is not stored in the phonebook. |
| 113 |  | er | 行尾多餘句號 | 3. The incoming call is received. |
| 113 |  | er | 行尾多餘句號 | 4. The Radio display shows the phone number of the caller. |
| 114 |  | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 114 |  | proc | 行尾多餘句號 | 2. Ensure the phone number is stored in the phonebook with a contact name. |
| 114 |  | proc | 行尾多餘句號 | 3. Receive an incoming call from the contact. |
| 114 |  | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen. |
| 114 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 114 |  | er | 行尾多餘句號 | 2. The phone number exists in the phonebook. |
| 114 |  | er | 行尾多餘句號 | 3. The incoming call is received. |
| 114 |  | er | 行尾多餘句號 | 4. The Radio display shows the contact name. |
| 115 |  | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 115 |  | proc | 行尾多餘句號 | 2. Receive an incoming call with an unknown or private number. |
| 115 |  | proc | 行尾多餘句號 | 3. Check the Caller ID displayed on the Radio screen. |
| 115 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 115 |  | er | 行尾多餘句號 | 2. The incoming call is received. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 4. Receive a call from a non-contact and check the pop up. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 2. Set the region configuration to NAFTA. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 3. Receive an incoming call from a phone number not stored in the phonebook. |
| 116 | newR1L-HFP-056 | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 2. The region configuration is set to NAFTA. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 3. The incoming call is received. |
| 116 | newR1L-HFP-056 | er | 行尾多餘句號 | 4. The phone number is displayed in the format xxx-xxx-xxxx. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 4. Receive a call from a non-contact and check the pop up. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 2. Set the region configuration to Non-NAFTA. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 3. Receive an incoming call from a phone number not stored in the phonebook. |
| 117 | newR1L-HFP-057 | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 2. The region configuration is set to Non-NAFTA. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 3. The incoming call is received. |
| 117 | newR1L-HFP-057 | er | 行尾多餘句號 | 4. The phone number is displayed as a continuous string xxxxxxxxxx. |
| 118 | newR1L-HFP-058 | pre | 行尾多餘句號 | 2. At least one Contact in the device. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 4. Receive a call from a Contact and check the pop up. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 2. Ensure the phone number exists in the phonebook with a contact name. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 3. Receive an incoming call from the contact. |
| 118 | newR1L-HFP-058 | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 4. Contact Name is displayed on incoming call pop up. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 2. The phone number exists in the phonebook. |
| 118 | newR1L-HFP-058 | er | 行尾多餘句號 | 3. The incoming call is received. |
| 119 |  | proc | 行尾多餘句號 | 1. Pair a mobile phone with the HU. |
| 119 |  | proc | 行尾多餘句號 | 2. Ensure the phone number exists in the phonebook with a contact name. |
| 119 |  | proc | 行尾多餘句號 | 3. Receive an incoming call before phonebook synchronization is completed. |
| 119 |  | proc | 行尾多餘句號 | 4. Check the Caller ID displayed on the Radio screen after synchronization is co |
| 119 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 119 |  | er | 行尾多餘句號 | 2. The phone number exists in the phonebook. |
| 119 |  | er | 行尾多餘句號 | 3. The incoming call is received. |
| 119 |  | er | 行尾多餘句號 | 4. The display updates from phone number to contact name after synchronization. |
| 120 | newR1L-HFP-059 | pre | 行尾多餘句號 | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 120 | newR1L-HFP-059 | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 120 | newR1L-HFP-059 | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Presence mode. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 4. Press "Phone" app to go to Phone page. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 6. Check the "Search field" and "Alpha jump" button are displayed in contact pag |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 4. Check the Search field is displayed. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 5. Check the Alpha Jump control is displayed. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 6. Check the Sort function is displayed. |
| 120 | newR1L-HFP-059 | proc | 行尾多餘句號 | 7. Check the contact list can be browsed normally. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 5. Contact page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 6. "Search field" and "Alpha jump button" are displayed in contact page. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 4. The Search field is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 5. The Alpha Jump control is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 6. The Sort function is displayed. |
| 120 | newR1L-HFP-059 | er | 行尾多餘句號 | 7. The contact list is available for browsing. |
| 121 | newR1L-HFP-060 | pre | 行尾多餘句號 | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 121 | newR1L-HFP-060 | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 121 | newR1L-HFP-060 | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Presence mode. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 4. Press "Phone" app to go to Phone page. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 6. Press Search bar on Contact page. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 4. Select the Search field. |
| 121 | newR1L-HFP-060 | proc | 行尾多餘句號 | 6. Check the search result list. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 5. Contact page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 6. Keyboard is extended. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 7. The results related to the inputed Alpha(s) is displayed in the contact list. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 4. The Search field is editable. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 5. The input is accepted. |
| 121 | newR1L-HFP-060 | er | 行尾多餘句號 | 6. Contacts matching the input characters are displayed. |
| 122 | newR1L-HFP-061 | pre | 行尾多餘句號 | 3. Set PROXI "Browsing Enable" is in Presence mode. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 4. Press "Phone" app to go to Phone page. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 4. Select the Alpha Jump control. |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 5. Input or select a target alphabet (for example: L). |
| 122 | newR1L-HFP-061 | proc | 行尾多餘句號 | 6. Check the contact list position. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 5. Contact page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 6. Keyboard is extended. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 7. Contact list shall jump to the first contact starting with the Alpha L. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 4. The Alpha Jump control is available. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 5. The alphabet input is accepted. |
| 122 | newR1L-HFP-061 | er | 行尾多餘句號 | 6. The list jumps to the first contact starting with the selected alphabet. |
| 123 |  | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 123 |  | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Presence mode. |
| 123 |  | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 123 |  | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 123 |  | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 123 |  | proc | 行尾多餘句號 | 4. Scroll through the contact list. |
| 123 |  | proc | 行尾多餘句號 | 5. Select a contact that contains multiple phone numbers. |
| 123 |  | proc | 行尾多餘句號 | 6. Check whether all stored phone numbers for the selected contact are displayed |
| 123 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 123 |  | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 123 |  | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 123 |  | er | 行尾多餘句號 | 4. The contact list can be browsed normally. |
| 123 |  | er | 行尾多餘句號 | 5. The selected contact is opened successfully. |
| 123 |  | er | 行尾多餘句號 | 6. All available phone numbers for the selected contact are displayed. |
| 124 |  | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 124 |  | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Presence mode. |
| 124 |  | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 124 |  | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 124 |  | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 124 |  | proc | 行尾多餘句號 | 4. Select the Sort function. |
| 124 |  | proc | 行尾多餘句號 | 5. Change the sorting order. |
| 124 |  | proc | 行尾多餘句號 | 6. Check the contact list order. |
| 124 |  | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 124 |  | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 124 |  | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 124 |  | er | 行尾多餘句號 | 4. The Sort function is available. |
| 124 |  | er | 行尾多餘句號 | 5. The selected sorting option is applied. |
| 124 |  | er | 行尾多餘句號 | 6. The contact list order is updated according to the selected sorting rule. |
| 125 | newR1L-HFP-062 | pre | 行尾多餘句號 | 3. Set PROXI "Browsing Enable" is in Absence mode. |
| 125 | newR1L-HFP-062 | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 125 | newR1L-HFP-062 | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Absence mode. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 3. Pairing a phone via Bluetooth. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 4. Press "Phone" app to go to Phone page. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 6. Check the "Search field" and "Alpha jump" button are Not displayed in contact |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 1. Pair a phone with the HU. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 2. Open the Phone application. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 3. Enter the Contact page. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 4. Check the Search field is displayed. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 5. Check the Alpha Jump control is displayed. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 6. Check the Sort function is displayed. |
| 125 | newR1L-HFP-062 | proc | 行尾多餘句號 | 7. Check the browsing-related functions are accessible. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 3. The Phone is paired. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 5. Contact page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 6. "Search field" and "Alpha jump button" are Not displayed in contact page. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 1. The phone is paired successfully. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 2. The Phone page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 3. The Contact page is displayed. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 4. The Search field is not displayed or is disabled. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 5. The Alpha Jump control is not displayed or is disabled. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 6. The Sort function is not displayed or is disabled. |
| 125 | newR1L-HFP-062 | er | 行尾多餘句號 | 7. Browsing-related functions are not available. |
| 126 |  | pre | 行尾多餘句號 | 2. At least 5 contacts exist in the phonebook. |
| 126 |  | pre | 行尾多餘句號 | 3. PROXI parameter Browsing Enable is set to Presence mode. |
| 126 |  | proc | 行尾多餘句號 | 1. Set Browsing Enable to Absence mode. |
| 126 |  | proc | 行尾多餘句號 | 2. Pair a phone with the HU. |
| 126 |  | proc | 行尾多餘句號 | 3. Open the Phone application. |
| 126 |  | proc | 行尾多餘句號 | 4. Enter the Contact page. |
| 126 |  | proc | 行尾多餘句號 | 5. Verify that Search field, Alpha Jump, and Sort controls are not displayed. |
| 126 |  | proc | 行尾多餘句號 | 6. Change Browsing Enable to Presence mode. |
| 126 |  | proc | 行尾多餘句號 | 7. Re-enter the Contact page. |
| 126 |  | proc | 行尾多餘句號 | 8. Check the browsing-related controls again. |
| 126 |  | er | 行尾多餘句號 | 1. Browsing Enable is set to Absence mode. |
| 126 |  | er | 行尾多餘句號 | 2. The phone is paired successfully. |
| 126 |  | er | 行尾多餘句號 | 3. The Phone page is displayed. |
| 126 |  | er | 行尾多餘句號 | 4. The Contact page is displayed. |
| 126 |  | er | 行尾多餘句號 | 5. The Search field, Alpha Jump, and Sort controls are not displayed. |
| 126 |  | er | 行尾多餘句號 | 6. Browsing Enable is changed to Presence mode. |
| 126 |  | er | 行尾多餘句號 | 7. The Contact page is displayed again. |
| 126 |  | er | 行尾多餘句號 | 8. The Search field, Alpha Jump, and Sort controls are displayed and available. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 3. Press "Add Device" button on Device Manager. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 1. Enable Bluetooth on the HU. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 2. Set the HU to discoverable mode. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 3. Scan for Bluetooth devices from an external device. |
| 127 | newR1L-HFP-063 | proc | 行尾多餘句號 | 4. Check the discovered device list. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 3. HU name shall displayed as "Uconnect" on the Bluetooth Pairing screen. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 1. Bluetooth is enabled on the HU. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 2. The HU enters discoverable mode. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 3. The external device scans for nearby devices. |
| 127 | newR1L-HFP-063 | er | 行尾多餘句號 | 4. The HU appears as "Uconnect" in the discovered device list. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 3. Press "Add Device" button on Device Manager. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 4. Scan the Bluetooth from external device. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 1. Enable Bluetooth on the HU. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 2. Open the Bluetooth device search page on the HU. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 3. Initiate the device discovery process. |
| 128 | newR1L-HFP-064 | proc | 行尾多餘句號 | 4. Check the HU name displayed during pairing. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 3. HU name shall displayed as "Uconnect" on the Bluetooth Pairing screen. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 1. The Bluetooth device search page is displayed. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 2. The pairing process is initiated. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 3. The HU name is displayed. |
| 128 | newR1L-HFP-064 | er | 行尾多餘句號 | 4. The name is shown as "Uconnect". |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 3. Start pairing the Phone via Bluetooth. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 1. Pair an external device with the HU. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 2. Complete the Bluetooth pairing process. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 3. Open the paired device list on the external device. |
| 129 | newR1L-HFP-065 | proc | 行尾多餘句號 | 4. Check the device name in the list. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 3. Phone is paired. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 4. The paired Bluetooth name device is displayed as “Uconnect”. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 1. The device is paired successfully. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 2. The connection between the HU and the device is established. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 3. The paired device list is displayed. |
| 129 | newR1L-HFP-065 | er | 行尾多餘句號 | 4. The HU name is displayed as "Uconnect". |
| 130 |  | proc | 行尾多餘句號 | 1. Pair a mobile device with the HU. |
| 130 |  | proc | 行尾多餘句號 | 2. Disconnect the Bluetooth connection from the mobile device. |
| 130 |  | proc | 行尾多餘句號 | 3. Reconnect the mobile device to the HU. |
| 130 |  | proc | 行尾多餘句號 | 4. Check the device name displayed on the mobile device. |
| 130 |  | er | 行尾多餘句號 | 1. The device is successfully paired with the HU. |
| 130 |  | er | 行尾多餘句號 | 2. The Bluetooth connection between the HU and the device is disconnected. |
| 130 |  | er | 行尾多餘句號 | 3. The device reconnects successfully to the HU. |
| 130 |  | er | 行尾多餘句號 | 4. The HU is displayed with the Bluetooth name "Uconnect". |
| 131 |  | proc | 行尾多餘句號 | 1. Pair a mobile device with the HU. |
| 131 |  | proc | 行尾多餘句號 | 2. Restart the HU system. |
| 131 |  | proc | 行尾多餘句號 | 3. Enable Bluetooth again. |
| 131 |  | proc | 行尾多餘句號 | 4. Scan for Bluetooth devices from the mobile device. |
| 131 |  | er | 行尾多餘句號 | 1. The HU restarts successfully. |
| 131 |  | er | 行尾多餘句號 | 2. Bluetooth becomes available. |
| 131 |  | er | 行尾多餘句號 | 3. The external device scans for nearby devices. |
| 131 |  | er | 行尾多餘句號 | 4. The HU appears as "Uconnect". |
| 132 | newR1L-HFP-066 | pre | 行尾多餘句號 | 2. USB is connected within music file. |
| 132 | newR1L-HFP-066 | pre | 行尾多餘句號 | 3. Radio Anteena is connected. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 3. Start pairing the phone via Bluetooth. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 4. Press "Media" button on menu bar. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 5. Press "Bluetooth" source. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 6. Forget the Bluetooth of HU from device to trigger the incorrect format issue  |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 8. Check the Bluetooth source playing status. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 9. Press "USB" source. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 10. Check the USB source playing status. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 11. Press "FM" source. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 12. Check the FM source playing status. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 2. Trigger a BTSA software error (e.g., corrupt internal BTSA data). |
| 132 | newR1L-HFP-066 | proc | 行尾多餘句號 | 3. Check the HU display. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 3. Phone and BTSA (Bluetooth Stream Audio) is connected. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 4. Media page is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 5. Bluetooth playing tab is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 6. Pop up "Generic Error" notification to inform user can't loading BTSA device. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 7. Return to Bluetooth playing tab. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 8. Bluetooth music cannot be played. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 9. "USB" playing tab is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 10. USB music playing without error. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 11. "FM" playing tab is displayed. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 12. FM radio playing without error. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 2. A BTSA software error occurs. |
| 132 | newR1L-HFP-066 | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification indicating the BTSA device canno |
| 133 | newR1L-HFP-067 | pre | 行尾多餘句號 | 2. USB is connected within music file. |
| 133 | newR1L-HFP-067 | pre | 行尾多餘句號 | 3. Radio Antenna is connected. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 3. Start pairing the phone via Bluetooth. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 4. Press "Media" button on menu bar. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 5. Press "Bluetooth" source. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 6. Disconnect the Bluetooth module antenna to trigger the issue on BTSA. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 8. Check the Bluetooth source playing status. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 9. Press "USB" source. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 10. Check the USB source playing status. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 11. Press "FM" source. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 12. Check the FM source playing status. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 2. Trigger a BTSA hardware error (e.g., simulate Bluetooth module read failure). |
| 133 | newR1L-HFP-067 | proc | 行尾多餘句號 | 3. Check the HU display. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 3. Phone and BTSA (Bluetooth Stream Audio) is connected. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 4. Media page is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 5. Bluetooth playing tab is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 6. Pop up "Generic Error" notification to inform user can't loading BTSA device. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 7. Return to Bluetooth playing tab. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 8. Bluetooth music cannot be played. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 9. "USB" playing tab is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 10. USB music playing without error. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 11. "FM" playing tab is displayed. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 12. FM radio playing without error. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 2. A BTSA hardware error occurs. |
| 133 | newR1L-HFP-067 | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification. |
| 134 |  | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 134 |  | proc | 行尾多餘句號 | 2. Trigger a BTSA software error by intentionally corrupting the BTSA internal d |
| 134 |  | proc | 行尾多餘句號 | 3. Verify that the HU displays a Generic Error notification. |
| 134 |  | proc | 行尾多餘句號 | 4. Press OK on the error notification. |
| 134 |  | proc | 行尾多餘句號 | 5. Check the BTSA playback status. |
| 134 |  | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 134 |  | er | 行尾多餘句號 | 2. The BTSA device reading error is triggered. |
| 134 |  | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification. |
| 134 |  | er | 行尾多餘句號 | 4. The system returns to the Bluetooth playback screen after acknowledging the e |
| 134 |  | er | 行尾多餘句號 | 5. BTSA audio playback remains unavailable. |
| 135 |  | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 135 |  | proc | 行尾多餘句號 | 2. Trigger a BTSA hardware error by disconnecting the Bluetooth module antenna. |
| 135 |  | proc | 行尾多餘句號 | 3. Verify that the HU displays a Generic Error notification. |
| 135 |  | proc | 行尾多餘句號 | 4. Press OK on the error notification. |
| 135 |  | proc | 行尾多餘句號 | 5. Select USB as the audio source. |
| 135 |  | proc | 行尾多餘句號 | 6. Verify USB playback behavior. |
| 135 |  | proc | 行尾多餘句號 | 7. Switch to FM source. |
| 135 |  | proc | 行尾多餘句號 | 8. Check FM playback behavior. |
| 135 |  | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 135 |  | er | 行尾多餘句號 | 2. The BTSA hardware error is triggered. |
| 135 |  | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification. |
| 135 |  | er | 行尾多餘句號 | 4. The error notification can be acknowledged. |
| 135 |  | er | 行尾多餘句號 | 5. The system switches to the USB source. |
| 135 |  | er | 行尾多餘句號 | 6. USB playback operates normally. |
| 135 |  | er | 行尾多餘句號 | 7. The system switches to the FM source. |
| 135 |  | er | 行尾多餘句號 | 8. FM radio playback operates normally. |
| 136 | newR1L-HFP-068 | pre | 行尾多餘句號 | 2. USB is connected within music file. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 3. Start pairing the phone via Bluetooth. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 4. Press "Media" button on menu bar. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 5. Press "Bluetooth" source. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 6. Forget the Bluetooth of HU from device to trigger the incorrect format issue  |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 8. Check the Bluetooth source playing status. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 9. Press "USB" source. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 10. Start pairing the phone again. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 11. Press "Bluetooth" source and check the playing status. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 2. Trigger a BTSA software error by intentionally corrupting the BTSA internal d |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 3. Verify that the HU displays a Generic Error notification. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 4. Press OK on the error notification. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 5. Switch to another audio source (e.g., USB). |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 6. Restore the BTSA software condition (recover the BTSA internal data). |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 7. Reconnect or pair the mobile device again. |
| 136 | newR1L-HFP-068 | proc | 行尾多餘句號 | 8. Select the Bluetooth audio source. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 3. Phone and BTSA (Bluetooth Stream Audio) is connected. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 4. Media page is displayed. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 5. Bluetooth playing tab is displayed. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 6. Pop up "Generic Error" notification to inform user can't loading BTSA device. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 7. Return to Bluetooth playing tab. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 8. Bluetooth music cannot be played. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 9. "USB" playing tab is displayed. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 10. Phone and BTSA is connected. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 11. Bluetooth playing without error. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 2. The BTSA software error occurs. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 4. The error notification can be acknowledged. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 5. Another audio source plays normally. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 6. The BTSA error condition is resolved. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 7. The Bluetooth device reconnects successfully. |
| 136 | newR1L-HFP-068 | er | 行尾多餘句號 | 8. BTSA audio playback resumes normally. |
| 137 | newR1L-HFP-069 | pre | 行尾多餘句號 | 2. USB is connected within music file. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 1. Press "Apps" button on menu bar. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 2. Press "Device Manager" app. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 3. Start pairing the phone via Bluetooth. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 4. Press "Media" button on menu bar. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 5. Press "Bluetooth" source. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 6. Disconnect the Bluetooth module antenna to trigger the issue on BTSA. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 8. Check the Bluetooth source playing status. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 9. Press "USB" source. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 10. Start pairing the phone again. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 11. Press "Bluetooth" source and check the playing status. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 1. Connect a mobile device to the HU and start BTSA playback. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 2. Trigger a BTSA hardware error by disconnecting the Bluetooth module antenna. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 3. Verify that the HU displays a Generic Error notification. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 4. Press OK on the error notification. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 5. Switch to another audio source (e.g., FM). |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 6. Restore the Bluetooth hardware condition (reconnect the Bluetooth module ante |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 7. Reconnect the mobile device to the HU. |
| 137 | newR1L-HFP-069 | proc | 行尾多餘句號 | 8. Select the Bluetooth audio source. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 3. Phone and BTSA (Bluetooth Stream Audio) is connected. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 4. Media page is displayed. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 5. Bluetooth playing tab is displayed. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 6. Pop up "Generic Error" notification to inform user can't loading BTSA device. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 7. Return to Bluetooth playing tab. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 8. Bluetooth music cannot be played. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 9. "USB" playing tab is displayed. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 10. Phone and BTSA is connected. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 11. Bluetooth playing without error. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 1. BTSA playback starts successfully. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 2. The BTSA hardware error occurs. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 3. The HU displays a Generic Error notification. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 4. The error notification can be acknowledged. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 5. Another audio source plays normally. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 6. The hardware condition is restored. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 7. The Bluetooth device reconnects successfully. |
| 137 | newR1L-HFP-069 | er | 行尾多餘句號 | 8. BTSA audio playback resumes normally. |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 1. Release the Automotive SIG profile version. |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 2. Turn off the screen via UI or H/W key. |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 3. Press and hold the top-left and bottom-right corners for 5 seconds to enter E |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 4. Press "System Information" menu item. |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 5. Press "Bluetooth Information" menu item. |
| 138 | newR1L-HFP-070 | proc | 行尾多餘句號 | 6. Check Automotive SIG profile version. |
| 138 | newR1L-HFP-070 | er | 行尾多餘句號 | 1. Version has been released. |
| 138 | newR1L-HFP-070 | er | 行尾多餘句號 | 2. Screen Off. |
| 138 | newR1L-HFP-070 | er | 行尾多餘句號 | 3. Display EngMode home screen. |
| 138 | newR1L-HFP-070 | er | 行尾多餘句號 | 4. System Information page is displayed. |
| 138 | newR1L-HFP-070 | er | 行尾多餘句號 | 5. Bluetooth Information page is displayed. |
| 139 | newR1L-HFP-071 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 139 | newR1L-HFP-071 | er | 行尾多餘句號 | 9. "Pixel 7 Pro" device is displayed on Device Manager page. |
| 140 | newR1L-HFP-072 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 140 | newR1L-HFP-072 | er | 行尾多餘句號 | 5. After return to Device Manager page, the "Pixel 7 Pro" device has been delete |
| 141 | newR1L-HFP-073 | pre | 行尾多餘句號 | - Device C: BTSA is connected. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 3. Start pairing the three prepared devices. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 6. Reconnect All Devices and check the enabled profile on each profiles. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 1. Press Apps on the HU menu bar. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 3. Pair Device A, Device B, and Device C with the HU. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 4. Check that devices connect according to their supported profiles. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 5. Disable Bluetooth on all devices to disconnect them from the HU. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 6. Re-enable Bluetooth on all devices. |
| 141 | newR1L-HFP-073 | proc | 行尾多餘句號 | 7. Check the reconnection behavior and profile assignment. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 3. Three Devices has been paired. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 5. All Devices are unpaired. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 3. Three devices are paired successfully. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 5. All devices are disconnected. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 6. Devices become available again. |
| 141 | newR1L-HFP-073 | er | 行尾多餘句號 | 7. The HU reconnects devices according to the enabled profiles and connection lo |
| 142 | newR1L-HFP-074 | pre | 行尾多餘句號 | 2. Prepare a device with enable HFP, BTSA. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 3. Check the connention status of current device on Device Manager page. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 4. Reboot the HU. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 6. Check the connention status of current device on Device Manager page. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 1. Press Apps on the menu bar. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 3. Check that the previously paired device is listed. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 4. Restart the HU to trigger the Bluetooth reconnect procedure. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 5. Wait for the HU to perform Bluetooth paging. |
| 142 | newR1L-HFP-074 | proc | 行尾多餘句號 | 6. Check the device connection status in Device Manager. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 3. A device is connected with enable HFP, BTSA profile. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 4. Return to Home Screen without error. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 5. The Device Manager page is displayed. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 6. A device is connected automatically with enable HFP, BTSA profile. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 3. The previously paired device is shown in the device list. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 4. The HU restarts successfully. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 5. The device responds to paging and authentication succeeds. |
| 142 | newR1L-HFP-074 | er | 行尾多餘句號 | 6. The HU automatically connects to the device with the supported profiles. |
| 143 | newR1L-HFP-075 | pre | 行尾多餘句號 | 2. Prepare a device is connected with enable HFP, BTSA. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 3. Check the connention status of current device on Device Manager page. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 3. Check that the previously paired device is listed. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 4. Remove the HU bonding information from the mobile device. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 5. Reboot the HU. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 5. Restart the HU to trigger the Bluetooth reconnect procedure. |
| 143 | newR1L-HFP-075 | proc | 行尾多餘句號 | 7. Check the connention status of current device on Device Manager page. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 3. A device is connected with enable HFP, BTSA profile. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 3. The previously paired device is shown in the device list. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 4. HU's Bluetooth has been forgotten by the device. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 4. The bonding information between the HU and device is invalidated. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 5. Return to Home Screen without error. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 5. The HU starts the reconnect process after reboot. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 6. The Device Manager page is displayed. |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 7. The device ignores connections from authenticated devices when authentication |
| 143 | newR1L-HFP-075 | er | 行尾多餘句號 | 7. The HU performs Bluetooth paging, but the device authentication fails ; no Bl |
| 144 |  | proc | 行尾多餘句號 | 1. Press Apps on the menu bar. |
| 144 |  | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 144 |  | proc | 行尾多餘句號 | 3. Check that the previously paired device is listed. |
| 144 |  | proc | 行尾多餘句號 | 4. Restart the HU to trigger the Bluetooth reconnect procedure. |
| 144 |  | proc | 行尾多餘句號 | 5. Wait for the HU to perform Bluetooth paging. |
| 144 |  | proc | 行尾多餘句號 | 6. Check the device connection status in Device Manager. |
| 144 |  | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 144 |  | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 144 |  | er | 行尾多餘句號 | 3. The previously paired device is shown in the device list. |
| 144 |  | er | 行尾多餘句號 | 4. The HU restarts successfully. |
| 144 |  | er | 行尾多餘句號 | 5. The device responds to paging and authentication succeeds. |
| 144 |  | er | 行尾多餘句號 | 6. The HU connects to the device according to the defined connection priority or |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 3. Check the connention status of current device on Device Manager page. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 4. Reboot the HU. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 6. Check the connention status of current device on Device Manager page. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 1. Press Apps on the HU menu bar. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 3. Check the previously paired device supports Bluetooth Phone (HFP). |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 4. Ensure the HU is not currently connected to Projection or HFP. |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 5. Trigger the Bluetooth reconnect procedure (e.g., reboot HU or enable device B |
| 145 | newR1L-HFP-076 | proc | 行尾多餘句號 | 6. Check the Bluetooth connection status in Device Manager. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 3. A device is connected with enable HFP profile. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 4. Return to Home Screen without error. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 5. The Device Manager page is displayed. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 3. The device is connected with enable HFP profile. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 4. The HU is not connected to Projection or HFP. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 5. The device responds to paging and authentication succeeds. |
| 145 | newR1L-HFP-076 | er | 行尾多餘句號 | 6. The device is connected automatically with enable HFP. |
| 146 |  | proc | 行尾多餘句號 | 1. Press Apps on the HU menu bar. |
| 146 |  | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 146 |  | proc | 行尾多餘句號 | 3. Check the device does not have Bluetooth Phone (HFP) enabled. |
| 146 |  | proc | 行尾多餘句號 | 4. Ensure the HU is not currently connected to Projection or HFP. |
| 146 |  | proc | 行尾多餘句號 | 5. Trigger the Bluetooth reconnect procedure (e.g., reboot HU or enable device B |
| 146 |  | proc | 行尾多餘句號 | 6. Check the Bluetooth connection status in Device Manager. |
| 146 |  | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 146 |  | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 146 |  | er | 行尾多餘句號 | 3. The device does not provide the HFP profile. |
| 146 |  | er | 行尾多餘句號 | 4. The HU is not connected to Projection or HFP. |
| 146 |  | er | 行尾多餘句號 | 5. The HU attempts Bluetooth connection but does not establish an HFP connection |
| 146 |  | er | 行尾多餘句號 | 6. The device remains without HFP connection status. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 3. Check the connention status of current device on Device Manager page. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 4. Reboot the HU. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 6. Check the connention status of current device on Device Manager page. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 1. Press "Apps" on the HU menu bar. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 3. Check the previously paired device supports BTSA. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 4. Ensure the HU is not connected to BTSA or Projection. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 5. Trigger the Bluetooth reconnect procedure. |
| 147 | newR1L-HFP-077 | proc | 行尾多餘句號 | 6. Check the Bluetooth connection status. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 3. A device is connected with enable BTSA profile. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 4. Return to Home Screen without error. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 5. The Device Manager page is displayed. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 3. The device supports BTSA profile. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 4. The HU is not connected to BTSA or Projection. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 5. The device responds to paging and authentication succeeds. |
| 147 | newR1L-HFP-077 | er | 行尾多餘句號 | 6. The device is connected automatically with enable BTSA. |
| 148 |  | proc | 行尾多餘句號 | 1. Press Apps on the HU menu bar. |
| 148 |  | proc | 行尾多餘句號 | 2. Open Device Manager. |
| 148 |  | proc | 行尾多餘句號 | 3. Check another device is already connected via BTSA or Projection. |
| 148 |  | proc | 行尾多餘句號 | 4. Trigger the Bluetooth reconnect procedure for the second device. |
| 148 |  | proc | 行尾多餘句號 | 5. Check the Bluetooth connection status in Device Manager. |
| 148 |  | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 148 |  | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 148 |  | er | 行尾多餘句號 | 3. Another BTSA or Projection connection is active. |
| 148 |  | er | 行尾多餘句號 | 4. The second device responds to paging. |
| 148 |  | er | 行尾多餘句號 | 5. The HU does not establish a BTSA connection with the second device. |
| 149 | newR1L-HFP-078 | pre | 行尾多餘句號 | 3. At least one contact having multiple numbers. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 3. Open the Contacts list. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 4. Press "Contact" which having multiple numbers. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 4. Select a contact that contains multiple phone numbers. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 5. Check the “List All Numbers” softkey is displayed. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 6. Press the "List All Phone Number" softkey. |
| 149 | newR1L-HFP-078 | proc | 行尾多餘句號 | 7. Check the displayed phone number list. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 3. Contact page is displayed. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 3. Contacts list is displayed. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 4. Contact info page is displayed. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 5. Display all associated phone numbers. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 4. The selected contact contains multiple phone numbers. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 5. The “List All Numbers” softkey is displayed. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 6. The number list is expanded successfully. |
| 149 | newR1L-HFP-078 | er | 行尾多餘句號 | 7. All associated phone numbers and labels (e.g., Mobile, Home, Work) are displa |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 3. Open the Contacts list. |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 4. Press "Contact" to view the Contact info page. |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 4. Select a contact that contains multiple phone numbers. |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 5. Press "Phone Number" button of contact to initial the call. |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 5. Press the "List All Phone Number" softkey. |
| 150 | newR1L-HFP-079 | proc | 行尾多餘句號 | 6. Select one phone number from the list. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 3. Contact page is displayed. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 3. Contacts list is displayed. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 4. Contact info page is displayed. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 5. Call is initialed and  HMI transitioning to Dialing/Phone page. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 4. The selected contact contains multiple phone numbers. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 5. The “List All Numbers” softkey is displayed. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 6. The selected number is highlighted. |
| 150 | newR1L-HFP-079 | er | 行尾多餘句號 | 7.Call is initialed and  HMI transitioning to Dialing/Phone page. |
| 151 |  | proc | 行尾多餘句號 | 3. Open the Contacts list. |
| 151 |  | proc | 行尾多餘句號 | 4. Select a contact with multiple phone numbers. |
| 151 |  | proc | 行尾多餘句號 | 5. Press the “List All Numbers” softkey. |
| 151 |  | proc | 行尾多餘句號 | 6. Check the Call softkey is enabled. |
| 151 |  | proc | 行尾多餘句號 | 7. Disable Bluetooth on the mobile device to disconnect HFP. |
| 151 |  | proc | 行尾多餘句號 | 8. Check the Call softkey status. |
| 151 |  | proc | 行尾多餘句號 | 9. Re-enable Bluetooth on the mobile device and reconnect HFP. |
| 151 |  | proc | 行尾多餘句號 | 10. Check the Call softkey status again. |
| 151 |  | er | 行尾多餘句號 | 1. App Drawer page is displayed. |
| 151 |  | er | 行尾多餘句號 | 3. Contacts list is displayed. |
| 151 |  | er | 行尾多餘句號 | 4. The selected contact contains multiple phone numbers. |
| 151 |  | er | 行尾多餘句號 | 5. The number list is displayed. |
| 151 |  | er | 行尾多餘句號 | 6. The Call softkey is enabled when HFP is connected. |
| 151 |  | er | 行尾多餘句號 | 7. The Bluetooth connection is disconnected. |
| 151 |  | er | 行尾多餘句號 | 8. The Call softkey becomes disabled immediately. |
| 151 |  | er | 行尾多餘句號 | 9. The Bluetooth device reconnects successfully. |
| 151 |  | er | 行尾多餘句號 | 10. The Call softkey becomes enabled again without requiring screen refresh. |
| 152 | newR1L-HFP-080 | pre | 行尾多餘句號 | 2. Prepare a device with at least 5 contacts. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 3. Press "Add Device" to start device pairing and download the phonebook. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 4. Press "Phone" app from App drawer. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 5. Check the "Contact" menu item is visibled and enabled. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 7. Check the contacts are listed in alphabetical order. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 3. Tap "Add Device" to start device pairing and download the phonebook. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 4. Access "Phone" app from App drawer to check the synced phonebook. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 5. Check the Phonebook/Contacts softkey. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 6. Press the Phonebook/Contacts softkey. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 7. Check the displayed phonebook entries. |
| 152 | newR1L-HFP-080 | proc | 行尾多餘句號 | 8. Scroll through the contact list. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 3. Device is paired with Phone Book downloaded. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 5. "Contact " menu item is enabled. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 6. Contact list page is displayed. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 7. Contacts are listed in alphabetical order. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 4. Phone application page is displayed. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 5. The Phonebook/Contacts softkey is visible and enabled. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 6. The phonebook view is opened successfully. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 7. Entries from the external downloaded phonebook are displayed correctly. |
| 152 | newR1L-HFP-080 | er | 行尾多餘句號 | 8. The contact list can be browsed smoothly without UI issues. |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 3. Press "Add Device" to start device pairing without download the phonebook. |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 4. Press "Phone" app from App drawer. |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 5. Check the "Contact" menu item is disabled. |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 3. Pair a Bluetooth device without allowing phonebook download (or use a device  |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 4. Access the Phone application from the App drawer. |
| 154 | newR1L-HFP-081 | proc | 行尾多餘句號 | 5. Check the Phonebook/Contacts softkey. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 3. Device is paired without Phone Book downloaded. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 4. Phone page is displayed. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 5. "Contact " menu item is disabled. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 1. App drawer page is displayed. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 2. Device Manager page is displayed. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 3. The device pairing succeeds but phonebook data is not available. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 4. Phone application page is displayed. |
| 154 | newR1L-HFP-081 | er | 行尾多餘句號 | 5. The Phonebook/Contacts softkey is disabled. |
| 155 | newR1L-HFP-082 | proc | 行尾多餘句號 | 3. Press "Add Deivce" to start Bluetooth pairing. |
| 155 | newR1L-HFP-082 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 155 | newR1L-HFP-082 | proc | 行尾多餘句號 | 4. Reject the paring request from the mobile drive during the pairing process. |
| 155 | newR1L-HFP-082 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 155 | newR1L-HFP-082 | proc | 行尾多餘句號 | 5. Check the content of the "Pairing Not Successful" pop-up message. |
| 155 | newR1L-HFP-082 | er | 行尾多餘句號 | 3. Bluetooth pairing process is initiated. |
| 155 | newR1L-HFP-082 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 155 | newR1L-HFP-082 | er | 行尾多餘句號 | 4. The "Paring Not Successful" notification is displayed on HU Screen. |
| 155 | newR1L-HFP-082 | er | 行尾多餘句號 | 5. Pop up shall display the Uconnect phone website URL. |
| 155 | newR1L-HFP-082 | er | 行尾多餘句號 | 5. The pop-up displays the Uconnect phone website URL correctly for the Chrysler |
| 156 | newR1L-HFP-083 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 156 | newR1L-HFP-083 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 156 | newR1L-HFP-083 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 156 | newR1L-HFP-083 | er | 行尾多餘句號 | 5. Pop up shall display the Uconnect phone website URL. |
| 157 | newR1L-HFP-084 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 157 | newR1L-HFP-084 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 157 | newR1L-HFP-084 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 157 | newR1L-HFP-084 | er | 行尾多餘句號 | 5. Pop up shall display the Uconnect phone website URL. |
| 158 | newR1L-HFP-085 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 158 | newR1L-HFP-085 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 158 | newR1L-HFP-085 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 158 | newR1L-HFP-085 | er | 行尾多餘句號 | 5. Pop up shall display the Uconnect phone website URL. |
| 159 | newR1L-HFP-086 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 159 | newR1L-HFP-086 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 159 | newR1L-HFP-086 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 159 | newR1L-HFP-086 | er | 行尾多餘句號 | 5. Pop up shall display the Uconnect phone website URL. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 3. Pair a mobile phone via Bluetooth. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 4. Disable the Message function on the mobile device. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 160 | newR1L-HFP-087 | proc | 行尾多餘句號 | 7. Check the content of the "Messaging Not Supported" pop-up message. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 3. Phone is connected successfully via Bluetooth. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 4. The messaging function on the connected device is disabled. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU screen. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 6. A "Messaging Not Supported" notification is displayed on the HU screen. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 7. Pop up shall display the Uconnect phone website URL. |
| 160 | newR1L-HFP-087 | er | 行尾多餘句號 | 7. The pop-up displays the Uconnect phone website URL correctly for the Chrysler |
| 161 | newR1L-HFP-088 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 161 | newR1L-HFP-088 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 161 | newR1L-HFP-088 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 161 | newR1L-HFP-088 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 161 | newR1L-HFP-088 | er | 行尾多餘句號 | 3. Phone is connected. |
| 161 | newR1L-HFP-088 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 161 | newR1L-HFP-088 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 161 | newR1L-HFP-088 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU screen. |
| 161 | newR1L-HFP-088 | er | 行尾多餘句號 | 7. Pop up shall display the Uconnect phone website URL. |
| 162 | newR1L-HFP-089 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 162 | newR1L-HFP-089 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 162 | newR1L-HFP-089 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 162 | newR1L-HFP-089 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 162 | newR1L-HFP-089 | er | 行尾多餘句號 | 3. Phone is connected. |
| 162 | newR1L-HFP-089 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 162 | newR1L-HFP-089 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 162 | newR1L-HFP-089 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU screen. |
| 162 | newR1L-HFP-089 | er | 行尾多餘句號 | 7. Pop up shall display the Uconnect phone website URL. |
| 163 | newR1L-HFP-090 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 163 | newR1L-HFP-090 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 163 | newR1L-HFP-090 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 163 | newR1L-HFP-090 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 163 | newR1L-HFP-090 | er | 行尾多餘句號 | 3. Phone is connected. |
| 163 | newR1L-HFP-090 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 163 | newR1L-HFP-090 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 163 | newR1L-HFP-090 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU screen. |
| 163 | newR1L-HFP-090 | er | 行尾多餘句號 | 7. Pop up shall display the Uconnect phone website URL. |
| 164 | newR1L-HFP-091 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 164 | newR1L-HFP-091 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 164 | newR1L-HFP-091 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 164 | newR1L-HFP-091 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 164 | newR1L-HFP-091 | er | 行尾多餘句號 | 3. Phone is connected. |
| 164 | newR1L-HFP-091 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 164 | newR1L-HFP-091 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 164 | newR1L-HFP-091 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU screen. |
| 164 | newR1L-HFP-091 | er | 行尾多餘句號 | 7. Pop up shall display the Uconnect phone website URL. |
| 165 | newR1L-HFP-092 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 165 | newR1L-HFP-092 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 165 | newR1L-HFP-092 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 165 | newR1L-HFP-092 | er | 行尾多餘句號 | 5. Pop up shall display a generic text message. |
| 166 | newR1L-HFP-093 | proc | 行尾多餘句號 | 4. Cancel pairing from the device during the pairing process. |
| 166 | newR1L-HFP-093 | proc | 行尾多餘句號 | 5. Check the content of pop up. |
| 166 | newR1L-HFP-093 | er | 行尾多餘句號 | 4. Pop up Pairing not successful notification on HU Screen. |
| 166 | newR1L-HFP-093 | er | 行尾多餘句號 | 5. Pop up shall display a generic text message. |
| 167 | newR1L-HFP-094 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 167 | newR1L-HFP-094 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 167 | newR1L-HFP-094 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 167 | newR1L-HFP-094 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 167 | newR1L-HFP-094 | er | 行尾多餘句號 | 3. Phone is connected. |
| 167 | newR1L-HFP-094 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 167 | newR1L-HFP-094 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 167 | newR1L-HFP-094 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU Screen. |
| 167 | newR1L-HFP-094 | er | 行尾多餘句號 | 7. Pop up shall display a generic text message. |
| 168 | newR1L-HFP-095 | proc | 行尾多餘句號 | 3. Start pairing phone via Bluetooth. |
| 168 | newR1L-HFP-095 | proc | 行尾多餘句號 | 5. Press "Phone" app from App drawer. |
| 168 | newR1L-HFP-095 | proc | 行尾多餘句號 | 6. Press "Message" menu item on Phone page. |
| 168 | newR1L-HFP-095 | proc | 行尾多餘句號 | 7. Check the content of pop up. |
| 168 | newR1L-HFP-095 | er | 行尾多餘句號 | 3. Phone is connected. |
| 168 | newR1L-HFP-095 | er | 行尾多餘句號 | 4. Message function is disabled. |
| 168 | newR1L-HFP-095 | er | 行尾多餘句號 | 5. Phone page is displayed. |
| 168 | newR1L-HFP-095 | er | 行尾多餘句號 | 6. Pop up Messaging not supported notification on HU Screen. |
| 168 | newR1L-HFP-095 | er | 行尾多餘句號 | 7. Pop up shall display a generic text message. |

