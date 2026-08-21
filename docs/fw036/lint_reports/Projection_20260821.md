# lint036 報告：FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Projection_20260623.xlsx

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Projection_20260623.xlsx`（唯讀）
- 資料列數：653
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 5 | 5 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item) | 2 | 2 | 每次命中 | 已校準 |
| D | PC 違規 (pre) | 20 | 20 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 5 | 5 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 1 | 1 | 每次命中 | 已校準 |
| G | Test Set 空值 | 1 | 1 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 2 | 2 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 2 | 2 | 每列 | 未校準（M15） |
| J | 行首大寫 | 4 | 4 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 648 | 648 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 91 | 91 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 96 | 92 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 1 | 1 | 每行 | 已校準 |

**總計：行計 878**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 5／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 96 | NR1L-PROJ-087 | proc | 禁用動詞 'Check whether' | nd the INFO icon ⏎ 6. Check whether a scroll bar is shown when the device list exc |
| 105 | NR1L-PROJ-096 | proc | 禁用動詞 'Check whether' | nd the INFO icon ⏎ 6. Check whether a scroll bar is shown when the device list exc |
| 157 | NR1L-PROJ-148 | proc | 禁用動詞 '3. Observe' | roid Auto media app ⏎ 3. Observe the playback on the HU for at least 30 seconds ⏎ 4. |
| 237 | NR1L-PROJ-228 | proc | 禁用動詞 '1. Inspect' | 1. Inspect the vehicle hardware |
| 551 | NR1L-PROJ-540 | proc | 禁用動詞 'check whether' | AP protocol log and check whether the HU sends a ByeByeRequest message with the |

### C — hedge (test_item)（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 613 |  | test_item | hedge 'properly' | nables and disables properly. ⏎  ⏎ (Shuffle toggle 5 times) |
| 617 |  | test_item | hedge 'properly' | nables and disables properly. ⏎  ⏎ (Repeat toggle 5 times) |

### D — PC 違規 (pre)（行計 20／列計 20）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 246 | NR1L-PROJ-237 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 247 | NR1L-PROJ-238 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 248 | NR1L-PROJ-239 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 249 | NR1L-PROJ-240 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 250 | NR1L-PROJ-241 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 251 | NR1L-PROJ-242 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Apple CarPlay-supporte |
| 254 | NR1L-PROJ-245 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 255 | NR1L-PROJ-246 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 256 | NR1L-PROJ-247 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 257 | NR1L-PROJ-248 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 258 | NR1L-PROJ-249 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 259 | NR1L-PROJ-250 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and reaches the home screen ⏎ 2. An Android Auto-supported |
| 367 | NR1L-PROJ-358 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 368 | NR1L-PROJ-359 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 369 | NR1L-PROJ-360 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 370 | NR1L-PROJ-361 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 371 | NR1L-PROJ-362 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 372 | NR1L-PROJ-363 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 373 | NR1L-PROJ-364 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |
| 374 | NR1L-PROJ-365 | pre | 通電前提 'HU is powered on' | 1. The HU is powered on and no USB media device is connected to the HMI USB Sour |

### E — proc/er 編號行數不對齊（行計 5／列計 5）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 43 | NR1L-PROJ-034 | proc/er | proc 5 步 vs er 1 步 |  |
| 191 | NR1L-PROJ-182 | proc/er | proc 5 步 vs er 4 步 |  |
| 362 | NR1L-PROJ-353 | proc/er | proc 5 步 vs er 4 步 |  |
| 526 | NR1L-PROJ-516 | proc/er | proc 5 步 vs er 9 步 |  |
| 661 |  | proc/er | proc 1 步 vs er 3 步 |  |

### F — 方括號佔位 (proc)（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 381 | NR1L-PROJ-372 | proc | 方括號佔位 '[ResolutionDistToTurn]' | eroPointZeroOne:100}[ResolutionDistToTurn] |

### G — Test Set 空值（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 571 | Customer EA app待釐清 | test_set | Test Set 為空 |  |

### I — test_item 括號下半缺失（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 237 | NR1L-PROJ-228 | test_item | 缺括號下半 | HU support CarPlay connection must have GPS antenna and module. ⏎  ⏎ 支持CarPlay连接的车辆必 |
| 569 | NR1L-PROJ-558 | test_item | 缺括號下半 | Accessories with the ability to connect to a device using Bluetooth and a wired |

### I-sibling — 同 Requirement ID 括號行逐字重複（行計 2／列計 2）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 418 | NR1L-PROJ-409 | test_item | 與 SWE1-PROJ-168 下另 1 列括號行逐字相同 | (Two new Android Auto devices on Hub B → lowest port number device launches proj |
| 419 | NR1L-PROJ-410 | test_item | 與 SWE1-PROJ-168 下另 1 列括號行逐字相同 | (Two new Android Auto devices on Hub B → lowest port number device launches proj |

### J — 行首大寫（行計 4／列計 4）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 429 | NR1L-PROJ-419 | test_item | 首字小寫 'if' | if the current audio source of the HU is a projection device, the HU shall set $ |
| 430 | NR1L-PROJ-420 | test_item | 首字小寫 'if' | if the current audio source of the HU is a projection device, the HU shall set $ |
| 431 | NR1L-PROJ-421 | test_item | 首字小寫 'if' | if the current audio source of the HU is a projection device, the HU shall set $ |
| 432 | NR1L-PROJ-422 | test_item | 首字小寫 'if' | if the current audio source of the HU is a projection device, the HU shall set $ |

### K — CJK 字元（行計 648／列計 648）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-PROJ-001 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (C |
| 11 | NR1L-PROJ-002 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (N |
| 12 | NR1L-PROJ-003 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (A |
| 13 | NR1L-PROJ-004 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (A |
| 14 | NR1L-PROJ-005 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (A |
| 15 | NR1L-PROJ-006 | test_item | 含 CJK 字元 | e pairing process. ⏎  ⏎ 当用户选择将设备与蓝牙配对时，HU应确定设备是否支持无线投屏。如果设备支持无线投屏，HU应提示用户继续配对过程。 ⏎  ⏎ (C |
| 16 | NR1L-PROJ-007 | test_item | 含 CJK 字元 | ewly paired device ⏎  ⏎ 无线投屏配对流程完成后，车机应连接并启动新配对设备的投屏。 ⏎  ⏎ (Launch CarPlay projection af |
| 17 | NR1L-PROJ-008 | test_item | 含 CJK 字元 | ewly paired device ⏎  ⏎ 无线投屏配对流程完成后，车机应连接并启动新配对设备的投屏。 ⏎  ⏎ (Launch Android Auto projecti |
| 18 | NR1L-PROJ-009 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 19 | NR1L-PROJ-010 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 20 | NR1L-PROJ-011 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 21 | NR1L-PROJ-012 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 22 | NR1L-PROJ-013 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 23 | NR1L-PROJ-014 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 24 | NR1L-PROJ-015 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 25 | NR1L-PROJ-016 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 26 | NR1L-PROJ-017 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 27 | NR1L-PROJ-018 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 28 | NR1L-PROJ-019 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 29 | NR1L-PROJ-020 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 30 | NR1L-PROJ-021 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 31 | NR1L-PROJ-022 | test_item | 含 CJK 字元 | reless Projection. ⏎  ⏎ 当用户选择使用Android Auto/CarPlay时，车机应将启用功能设为投屏，并禁用蓝牙电话和蓝牙音频，然后开始连 |
| 32 | NR1L-PROJ-023 | test_item | 含 CJK 字元 | ring requirements. ⏎  ⏎ 当用户不选择连接使用CarPlay时，车机应继续按正常流程进行蓝牙配对。详见{CFTS026}及[HMI Logic a |
| 33 | NR1L-PROJ-024 | test_item | 含 CJK 字元 | ring requirements. ⏎  ⏎ 当用户不选择连接使用CarPlay时，车机应继续按正常流程进行蓝牙配对。详见{CFTS026}及[HMI Logic a |
| 34 | NR1L-PROJ-025 | test_item | 含 CJK 字元 | ring requirements. ⏎  ⏎ 当用户不选择连接使用Android Auto时，车机应继续按正常流程进行蓝牙配对。详见{CFTS026}及[HMI Lo |
| 35 | NR1L-PROJ-026 | test_item | 含 CJK 字元 | ring requirements. ⏎  ⏎ 当用户不选择连接使用Android Auto时，车机应继续按正常流程进行蓝牙配对。详见{CFTS026}及[HMI Lo |
| 36 | NR1L-PROJ-027 | test_item | 含 CJK 字元 | h pairing process. ⏎  ⏎ 如果设备不支持无线投屏，HU应继续进行蓝牙配对流程。 ⏎  ⏎ (Non-CarPlay phone → BT pairing |
| 37 | NR1L-PROJ-028 | test_item | 含 CJK 字元 | h pairing process. ⏎  ⏎ 如果设备不支持无线投屏，HU应继续进行蓝牙配对流程。 ⏎  ⏎ (Non-Android-Auto phone → BT pai |
| 38 | NR1L-PROJ-029 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 39 | NR1L-PROJ-030 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 40 | NR1L-PROJ-031 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 41 | NR1L-PROJ-032 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 42 | NR1L-PROJ-033 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 43 | NR1L-PROJ-034 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 44 | NR1L-PROJ-035 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 45 | NR1L-PROJ-036 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 46 | NR1L-PROJ-037 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 47 | NR1L-PROJ-038 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 48 | NR1L-PROJ-039 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 如果用户选择手动断开正在进行的无线投屏会话，或HU与无线投屏设备失去连接，HU应终止连接，并按照HMI逻辑和流程规范更新 |
| 49 | NR1L-PROJ-040 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 若车机因非用户选择的原因失去连接，车机应按照{CFTS026}规定的寻呼算法继续寻呼已断开的设备。 ⏎  ⏎ (HU loses |
| 50 | NR1L-PROJ-041 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 若车机因非用户选择的原因失去连接，车机应按照{CFTS026}规定的寻呼算法继续寻呼已断开的设备。 ⏎  ⏎ (HU loses |
| 51 | NR1L-PROJ-042 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 若车机因非用户选择的原因失去连接，车机应按照{CFTS026}规定的寻呼算法继续寻呼已断开的设备。 ⏎  ⏎ (HU loses |
| 52 | NR1L-PROJ-043 | test_item | 含 CJK 字元 | fied in {CFTS026}. ⏎  ⏎ 若车机因非用户选择的原因失去连接，车机应按照{CFTS026}规定的寻呼算法继续寻呼已断开的设备。 ⏎  ⏎ (HU loses |
| 53 | NR1L-PROJ-044 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User disconnects |
| 54 | NR1L-PROJ-045 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User deletes pair |
| 55 | NR1L-PROJ-046 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User disconnects |
| 56 | NR1L-PROJ-047 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User unpairs HU f |
| 57 | NR1L-PROJ-048 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User disconnects |
| 58 | NR1L-PROJ-049 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User deletes pair |
| 59 | NR1L-PROJ-050 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User disconnects |
| 60 | NR1L-PROJ-051 | test_item | 含 CJK 字元 | sconnected device. ⏎  ⏎ 若因用户主动操作导致HU断开连接，HU不应对该已断开的设备发起寻呼(page)。 ⏎  ⏎ (User unpairs HU f |
| 61 | NR1L-PROJ-052 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wired A |
| 62 | NR1L-PROJ-053 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wired A |
| 63 | NR1L-PROJ-054 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wired A |
| 64 | NR1L-PROJ-055 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wireles |
| 65 | NR1L-PROJ-056 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wireles |
| 66 | NR1L-PROJ-057 | test_item | 含 CJK 字元 | e HMI for details. ⏎  ⏎ 当车机正在尝试连接Android Auto设备时，车机应显示连接进行中的指示。具体样式见HMI文档。 ⏎  ⏎ (Wireles |
| 67 | NR1L-PROJ-058 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (PU0252 d |
| 68 | NR1L-PROJ-059 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (PU0252 d |
| 69 | NR1L-PROJ-060 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (CarPlay |
| 70 | NR1L-PROJ-061 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (CarPlay |
| 71 | NR1L-PROJ-062 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (No popup |
| 72 | NR1L-PROJ-063 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (PU0252 d |
| 73 | NR1L-PROJ-064 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (PU0252 d |
| 74 | NR1L-PROJ-065 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (Android |
| 75 | NR1L-PROJ-066 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (Android |
| 76 | NR1L-PROJ-067 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (PU0254 d |
| 77 | NR1L-PROJ-068 | test_item | 含 CJK 字元 | tooth connections. ⏎  ⏎ 当用户选择连接投屏设备时，HU应在断开任何活动的投屏或蓝牙连接之前，按照HMI指示向用户发出警告。 ⏎  ⏎ (No popup |
| 78 | NR1L-PROJ-069 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 79 | NR1L-PROJ-070 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 80 | NR1L-PROJ-071 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 81 | NR1L-PROJ-072 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 82 | NR1L-PROJ-073 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 83 | NR1L-PROJ-074 | test_item | 含 CJK 字元 | to specifications. ⏎  ⏎ 当用户请求对未连接USB端口的设备发起CarPlay或Android Auto连接，或HU寻呼算法发起连接时，HU应按照 |
| 84 | NR1L-PROJ-075 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 85 | NR1L-PROJ-076 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 86 | NR1L-PROJ-077 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 87 | NR1L-PROJ-078 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 88 | NR1L-PROJ-079 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 89 | NR1L-PROJ-080 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 如果用户在当前已禁用无线CarPlay设置的设备上请求连接无线投屏，HU应仅在用户接受HMI逻辑和流程中描述的HMI警告 |
| 90 | NR1L-PROJ-081 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 91 | NR1L-PROJ-082 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 92 | NR1L-PROJ-083 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 93 | NR1L-PROJ-084 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 94 | NR1L-PROJ-085 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 95 | NR1L-PROJ-086 | test_item | 含 CJK 字元 | d specific screens ⏎  ⏎ 如果在超时之前无法建立无线投屏连接，HU应提示连接失败。超时时间和具体界面详见[投屏设备HMI逻辑和流程]。 ⏎  ⏎ (PU0 |
| 96 | NR1L-PROJ-087 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Device Manager main screen displays the d |
| 97 | NR1L-PROJ-088 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Function icons for a CarPlay-supporting p |
| 98 | NR1L-PROJ-089 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing an Available CarPlay function ic |
| 99 | NR1L-PROJ-090 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing an Active CarPlay function icon |
| 100 | NR1L-PROJ-091 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Newly connected CarPlay device is automat |
| 101 | NR1L-PROJ-092 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing "Add Device" on the Device Manag |
| 102 | NR1L-PROJ-093 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the favorite icon toggles the de |
| 103 | NR1L-PROJ-094 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the Back button on the Device Ma |
| 104 | NR1L-PROJ-095 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the INFO (i) button on the Devic |
| 105 | NR1L-PROJ-096 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Device Manager main screen displays the d |
| 106 | NR1L-PROJ-097 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Function icons for an Android Auto-suppor |
| 107 | NR1L-PROJ-098 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing an Available Android Auto functi |
| 108 | NR1L-PROJ-099 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing an Active Android Auto function |
| 109 | NR1L-PROJ-100 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Newly connected Android Auto device is au |
| 110 | NR1L-PROJ-101 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing "Add Device" on the Device Manag |
| 111 | NR1L-PROJ-102 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the favorite icon toggles the de |
| 112 | NR1L-PROJ-103 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the Back button on the Device Ma |
| 113 | NR1L-PROJ-104 | test_item | 含 CJK 字元 | MI Logic and Flow. ⏎  ⏎ 按照客户提供的UI，实现设备列表 ⏎  ⏎ (Pressing the INFO (i) button on the Devic |
| 114 | NR1L-PROJ-105 | test_item | 含 CJK 字元 | hm, see {CFTS026}. ⏎  ⏎ 蓝牙寻呼算法详见{CFTS026}。 ⏎  ⏎ (Non-user wireless CarPlay disconnect → |
| 115 | NR1L-PROJ-106 | test_item | 含 CJK 字元 | hm, see {CFTS026}. ⏎  ⏎ 蓝牙寻呼算法详见{CFTS026}。 ⏎  ⏎ (Non-user wireless Android Auto disconne |
| 116 | NR1L-PROJ-107 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Wir |
| 117 | NR1L-PROJ-108 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Car |
| 118 | NR1L-PROJ-109 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Wir |
| 119 | NR1L-PROJ-110 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Wir |
| 120 | NR1L-PROJ-111 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Wir |
| 121 | NR1L-PROJ-112 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (And |
| 122 | NR1L-PROJ-113 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (And |
| 123 | NR1L-PROJ-114 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (And |
| 124 | NR1L-PROJ-115 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (And |
| 125 | NR1L-PROJ-116 | test_item | 含 CJK 字元 | ss Android Auto. ⏎  ⏎ HU应满足Apple和Google为无线CarPlay和无线Android Auto提供的规范中的所有性能要求。 ⏎  ⏎ (Wir |
| 126 | NR1L-PROJ-117 | test_item | 含 CJK 字元 | n the 2.4GHz range ⏎  ⏎ 如果Apple/Google要求禁用蓝牙，当投屏在2.4GHz频段运行时，HU应禁用蓝牙子系统。 ⏎  ⏎ (Wireless |
| 127 | NR1L-PROJ-118 | test_item | 含 CJK 字元 | n the 2.4GHz range ⏎  ⏎ 如果Apple/Google要求禁用蓝牙，当投屏在2.4GHz频段运行时，HU应禁用蓝牙子系统。 ⏎  ⏎ (Wireless |
| 128 | NR1L-PROJ-119 | test_item | 含 CJK 字元 | n the 2.4GHz range ⏎  ⏎ 如果Apple/Google要求禁用蓝牙，当投屏在2.4GHz频段运行时，HU应禁用蓝牙子系统。 ⏎  ⏎ (Wireless |
| 129 | NR1L-PROJ-120 | test_item | 含 CJK 字元 | n the 2.4GHz range ⏎  ⏎ 如果Apple/Google要求禁用蓝牙，当投屏在2.4GHz频段运行时，HU应禁用蓝牙子系统。 ⏎  ⏎ (Wireless |
| 130 | NR1L-PROJ-121 | test_item | 含 CJK 字元 | and Flow for HMI. ⏎  ⏎ 无线投屏连接应满足与USB投屏连接相同的HMI和技术要求。USB技术要求详见上述需求，HMI要求详见投屏设备HMI逻辑和 |
| 131 | NR1L-PROJ-122 | test_item | 含 CJK 字元 | and Flow for HMI. ⏎  ⏎ 无线投屏连接应满足与USB投屏连接相同的HMI和技术要求。USB技术要求详见上述需求，HMI要求详见投屏设备HMI逻辑和 |
| 132 | NR1L-PROJ-123 | test_item | 含 CJK 字元 | and Flow for HMI. ⏎  ⏎ 无线投屏连接应满足与USB投屏连接相同的HMI和技术要求。USB技术要求详见上述需求，HMI要求详见投屏设备HMI逻辑和 |
| 133 | NR1L-PROJ-124 | test_item | 含 CJK 字元 | and Flow for HMI. ⏎  ⏎ 无线投屏连接应满足与USB投屏连接相同的HMI和技术要求。USB技术要求详见上述需求，HMI要求详见投屏设备HMI逻辑和 |
| 134 | NR1L-PROJ-125 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Long |
| 135 | NR1L-PROJ-126 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Shor |
| 136 | NR1L-PROJ-127 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Long |
| 137 | NR1L-PROJ-128 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (VR a |
| 138 | NR1L-PROJ-129 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Non- |
| 139 | NR1L-PROJ-130 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Inco |
| 140 | NR1L-PROJ-131 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Long |
| 141 | NR1L-PROJ-132 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Shor |
| 142 | NR1L-PROJ-133 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Long |
| 143 | NR1L-PROJ-134 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (VR a |
| 144 | NR1L-PROJ-135 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Non- |
| 145 | NR1L-PROJ-136 | test_item | 含 CJK 字元 | ogle specification ⏎  ⏎ 用户应能够通过按住方向盘启动手机的 VR 引擎来开启 VR 会话。按住时间应在苹果/谷歌的规范中予以定义。 ⏎  ⏎ (Inco |
| 146 | NR1L-PROJ-137 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Subsequent requests stil |
| 147 | NR1L-PROJ-138 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Hardware voice button wa |
| 148 | NR1L-PROJ-139 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Long press during active |
| 149 | NR1L-PROJ-140 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Press and release dispat |
| 150 | NR1L-PROJ-141 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Native VR short press ca |
| 151 | NR1L-PROJ-142 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Incoming call cancels ac |
| 152 | NR1L-PROJ-143 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Short press steering whe |
| 153 | NR1L-PROJ-144 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Long press during active |
| 154 | NR1L-PROJ-145 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Press and release dispat |
| 155 | NR1L-PROJ-146 | test_item | 含 CJK 字元 | aidu requirements. ⏎  ⏎ 在一次活跃的VR会话中，按钮按压行为应遵循苹果/谷歌/百度的要求。 ⏎  ⏎ (Subsequent requests stil |
| 156 | NR1L-PROJ-147 | test_item | 含 CJK 字元 | oma subsampling. ⏎  ⏎ HU必须实现H.264解码器，能够使用YCbCr 4:2:0色度子采样，以60fps（High Profile 3.1）支持 |
| 157 | NR1L-PROJ-148 | test_item | 含 CJK 字元 | oma subsampling. ⏎  ⏎ HU必须实现H.264解码器，能够使用YCbCr 4:2:0色度子采样，以60fps（High Profile 3.1）支持 |
| 158 | NR1L-PROJ-149 | test_item | 含 CJK 字元 | fuel notification. ⏎  ⏎ 当HCP_DISP2.Est_Range_BEV <= [24 km]且$VC_VEH_Line$ = [332]时，H |
| 159 | NR1L-PROJ-150 | test_item | 含 CJK 字元 | fuel notification. ⏎  ⏎ 当HCP_DISP2.Est_Range_BEV <= [24 km]且$VC_VEH_Line$ = [332]时，H |
| 160 | NR1L-PROJ-151 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 161 | NR1L-PROJ-152 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 162 | NR1L-PROJ-153 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 163 | NR1L-PROJ-154 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 164 | NR1L-PROJ-155 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 165 | NR1L-PROJ-156 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 166 | NR1L-PROJ-157 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 167 | NR1L-PROJ-158 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 168 | NR1L-PROJ-159 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 169 | NR1L-PROJ-160 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 170 | NR1L-PROJ-161 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 171 | NR1L-PROJ-162 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 172 | NR1L-PROJ-163 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 173 | NR1L-PROJ-164 | test_item | 含 CJK 字元 | put to projection. ⏎  ⏎ 当 $VC_Veh_Line$ =[ 363或376或332或250或637或M189或M182或M240或TIPO或S |
| 174 | NR1L-PROJ-165 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$FuelLvlLow$信号来确定何时显示低燃油指示。 ⏎  ⏎ (Range threshold triggers lo |
| 175 | NR1L-PROJ-166 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$FuelLvlLow$信号来确定何时显示低燃油指示。 ⏎  ⏎ (Range threshold triggers lo |
| 176 | NR1L-PROJ-167 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay receives $Day |
| 177 | NR1L-PROJ-168 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay receives $Day |
| 178 | NR1L-PROJ-169 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay UI switches t |
| 179 | NR1L-PROJ-170 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay UI switches t |
| 180 | NR1L-PROJ-171 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay reconnection |
| 181 | NR1L-PROJ-172 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay reconnection |
| 182 | NR1L-PROJ-173 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay map graphics |
| 183 | NR1L-PROJ-174 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay HMI component |
| 184 | NR1L-PROJ-175 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay theme switch |
| 185 | NR1L-PROJ-176 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay maintains cur |
| 186 | NR1L-PROJ-177 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (CarPlay UI remains st |
| 187 | NR1L-PROJ-178 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto receives |
| 188 | NR1L-PROJ-179 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto receives |
| 189 | NR1L-PROJ-180 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto UI switc |
| 190 | NR1L-PROJ-181 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto UI switc |
| 191 | NR1L-PROJ-182 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto reconnec |
| 192 | NR1L-PROJ-183 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto reconnec |
| 193 | NR1L-PROJ-184 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto map grap |
| 194 | NR1L-PROJ-185 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto HMI comp |
| 195 | NR1L-PROJ-186 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto theme sw |
| 196 | NR1L-PROJ-187 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto maintain |
| 197 | NR1L-PROJ-188 | test_item | 含 CJK 字元 | CarPlay/Android Auto应使用$Day_Night_Mode$信号来确定何时切换到夜间模式图形。 ⏎  ⏎ (Android Auto UI remai |
| 198 | NR1L-PROJ-189 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch CarPlay songs on H |
| 199 | NR1L-PROJ-190 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 200 | NR1L-PROJ-191 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch CarPlay songs on D |
| 201 | NR1L-PROJ-192 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 202 | NR1L-PROJ-193 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch CarPlay songs on C |
| 203 | NR1L-PROJ-194 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 204 | NR1L-PROJ-195 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch CarPlay songs on R |
| 205 | NR1L-PROJ-196 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 206 | NR1L-PROJ-197 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎ (Knob can switch CarPlay songs on To |
| 207 | NR1L-PROJ-198 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎ (Knob enter button can select curren |
| 208 | NR1L-PROJ-199 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot switch CarPlay songs on Fas |
| 209 | NR1L-PROJ-200 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot select CarPlay song on Fast |
| 210 | NR1L-PROJ-201 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot switch CarPlay songs on Pro |
| 211 | NR1L-PROJ-202 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot select CarPlay song on ProM |
| 212 | NR1L-PROJ-203 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch Android Auto songs |
| 213 | NR1L-PROJ-204 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 214 | NR1L-PROJ-205 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch Android Auto songs |
| 215 | NR1L-PROJ-206 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 216 | NR1L-PROJ-207 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch Android Auto songs |
| 217 | NR1L-PROJ-208 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 218 | NR1L-PROJ-209 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob can switch Android Auto songs |
| 219 | NR1L-PROJ-210 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 221 | NR1L-PROJ-212 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Knob enter button can select curre |
| 222 | NR1L-PROJ-213 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot switch Android Auto songs o |
| 223 | NR1L-PROJ-214 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot select Android Auto song on |
| 224 | NR1L-PROJ-215 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot switch Android Auto songs o |
| 225 | NR1L-PROJ-216 | test_item | 含 CJK 字元 | n projection mode. ⏎  ⏎ 在投屏模式下，调谐器旋钮应滚动列表并选择媒体。 ⏎  ⏎ (Cannot select Android Auto song on |
| 226 | NR1L-PROJ-217 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 227 | NR1L-PROJ-218 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 228 | NR1L-PROJ-219 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 229 | NR1L-PROJ-220 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 230 | NR1L-PROJ-221 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 231 | NR1L-PROJ-222 | test_item | 含 CJK 字元 | Specification]. ⏎  ⏎ HU 应采用全球导航卫星系统（GNSS）模式。不得采用传感器模式。请参阅 [苹果 MFi 配件接口规范] 第 35 节“位置信 |
| 232 | NR1L-PROJ-223 | test_item | 含 CJK 字元 | evice over iAP2. ⏎  ⏎ HU应通过iAP2向Apple设备提供以下美国国家海洋电子协会（NMEA）语句。 ⏎  ⏎ (NMEA sentences (GPR |
| 233 | NR1L-PROJ-224 | test_item | 含 CJK 字元 | the Apple device. ⏎  ⏎ 仅需向Apple设备提供Apple要求的信号。 ⏎  ⏎ (Apple-required signals are present |
| 234 | NR1L-PROJ-225 | test_item | 含 CJK 字元 | the Apple device. ⏎  ⏎ 仅需向Apple设备提供Apple要求的信号。 ⏎  ⏎ (Signals not required by Apple are |
| 237 | NR1L-PROJ-228 | test_item | 含 CJK 字元 | ntenna and module. ⏎  ⏎ 支持CarPlay连接的车辆必须GPS天线和模组 |
| 238 | NR1L-PROJ-229 | test_item | 含 CJK 字元 | audio focus state. ⏎  ⏎ 当连接到Android Auto设备时，HU应提供车辆传感器和导航数据。无论视频或音频焦点状态如何，数据都应可用于And |
| 239 | NR1L-PROJ-230 | test_item | 含 CJK 字元 | audio focus state. ⏎  ⏎ 当连接到Android Auto设备时，HU应提供车辆传感器和导航数据。无论视频或音频焦点状态如何，数据都应可用于And |
| 240 | NR1L-PROJ-231 | test_item | 含 CJK 字元 | audio focus state. ⏎  ⏎ 当连接到Android Auto设备时，HU应提供车辆传感器和导航数据。无论视频或音频焦点状态如何，数据都应可用于And |
| 241 | NR1L-PROJ-232 | test_item | 含 CJK 字元 | audio focus state. ⏎  ⏎ 当连接到Android Auto设备时，HU应提供车辆传感器和导航数据。无论视频或音频焦点状态如何，数据都应可用于And |
| 244 | NR1L-PROJ-235 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Country code configured to |
| 245 | NR1L-PROJ-236 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Country code configured to |
| 246 | NR1L-PROJ-237 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Menu Bar CarPlay icon appea |
| 247 | NR1L-PROJ-238 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap Menu Bar CarPlay icon l |
| 248 | NR1L-PROJ-239 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (App Drawer CarPlay icon app |
| 249 | NR1L-PROJ-240 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap App Drawer CarPlay icon |
| 250 | NR1L-PROJ-241 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Media Sources CarPlay entry |
| 251 | NR1L-PROJ-242 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap Media Sources CarPlay e |
| 252 | NR1L-PROJ-243 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Country code configured to |
| 253 | NR1L-PROJ-244 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Country code configured to |
| 254 | NR1L-PROJ-245 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Menu Bar Android Auto icon |
| 255 | NR1L-PROJ-246 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap Menu Bar Android Auto i |
| 256 | NR1L-PROJ-247 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (App Drawer Android Auto ico |
| 257 | NR1L-PROJ-248 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap App Drawer Android Auto |
| 258 | NR1L-PROJ-249 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Media Sources Android Auto |
| 259 | NR1L-PROJ-250 | test_item | 含 CJK 字元 | Auto and CarPlay. ⏎  ⏎ 车机应支持Android Auto and CarPlay。 ⏎  ⏎ (Tap Media Sources Android A |
| 260 | NR1L-PROJ-251 | test_item | 含 CJK 字元 | additonal details. ⏎  ⏎ 当CarPlay设备连接到USB端口时，HU应将该设备连接到CarPlay，无论设备管理器中的用户设置如何。更多详情请参 |
| 261 | NR1L-PROJ-252 | test_item | 含 CJK 字元 | additonal details. ⏎  ⏎ 当CarPlay设备连接到USB端口时，HU应将该设备连接到CarPlay，无论设备管理器中的用户设置如何。更多详情请参 |
| 262 | NR1L-PROJ-253 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 263 | NR1L-PROJ-254 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 264 | NR1L-PROJ-255 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 265 | NR1L-PROJ-256 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 266 | NR1L-PROJ-257 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 267 | NR1L-PROJ-258 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 268 | NR1L-PROJ-259 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 269 | NR1L-PROJ-260 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 270 | NR1L-PROJ-261 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 271 | NR1L-PROJ-262 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 272 | NR1L-PROJ-263 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 273 | NR1L-PROJ-264 | test_item | 含 CJK 字元 | shown in quotes. ⏎  ⏎ HU应根据下面映射的$VC_Veh_Brand$参数，在Android Auto设备的服务发现响应中填充“Vehicle m |
| 274 | NR1L-PROJ-265 | test_item | 含 CJK 字元 | he device manager. ⏎  ⏎ 当HU收到当前已连接蓝牙设备的无线Android Auto连接请求时，HU应连接该设备，并按照HMI流程执行，如同用户从 |
| 275 | NR1L-PROJ-266 | test_item | 含 CJK 字元 | he device manager. ⏎  ⏎ 当HU收到当前已连接蓝牙设备的无线Android Auto连接请求时，HU应连接该设备，并按照HMI流程执行，如同用户从 |
| 276 | NR1L-PROJ-267 | test_item | 含 CJK 字元 | he device manager. ⏎  ⏎ 当HU收到当前已连接蓝牙设备的无线Android Auto连接请求时，HU应连接该设备，并按照HMI流程执行，如同用户从 |
| 277 | NR1L-PROJ-268 | test_item | 含 CJK 字元 | . ⏎  ⏎ “ModelIdentifier”字段应根据以下列表中的内容填写相应的子信息。 ⏎  Automotive_Manufacture: FCA ⏎  Make: B |
| 278 | NR1L-PROJ-269 | test_item | 含 CJK 字元 | . ⏎  ⏎ “ModelIdentifier”字段应根据以下列表中的内容填写相应的子信息。 ⏎  Automotive_Manufacture: FCA ⏎  Make: B |
| 279 | NR1L-PROJ-270 | test_item | 含 CJK 字元 | ing information. ⏎  ⏎ HU应使用以下信息填充iAP2设备信息。 ⏎ Name: Uconnect ⏎ ModelIdentifier: Automotiv |
| 280 | NR1L-PROJ-271 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当通过显示屏上的“断开连接”软按钮或Android Auto切换按钮使无线或有线的安卓车载系统会话断开时，主机单元（HU |
| 281 | NR1L-PROJ-272 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当通过显示屏上的“断开连接”软按钮或Android Auto切换按钮使无线或有线的安卓车载系统会话断开时，主机单元（HU |
| 282 | NR1L-PROJ-273 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当通过显示屏上的“断开连接”软按钮或Android Auto切换按钮使无线或有线的安卓车载系统会话断开时，主机单元（HU |
| 283 | NR1L-PROJ-274 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当通过显示屏上的“断开连接”软按钮或Android Auto切换按钮使无线或有线的安卓车载系统会话断开时，主机单元（HU |
| 284 | NR1L-PROJ-275 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当无线或有线Android Auto会话通过显示屏上的软"断开连接"按钮以外的方式断开，且HU收到来自设备的"ByeBy |
| 285 | NR1L-PROJ-276 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当无线或有线Android Auto会话通过显示屏上的软"断开连接"按钮以外的方式断开，且HU收到来自设备的"ByeBy |
| 286 | NR1L-PROJ-277 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当无线或有线Android Auto会话通过显示屏上的软"断开连接"按钮以外的方式断开，且HU收到来自设备的"ByeBy |
| 287 | NR1L-PROJ-278 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当无线或有线Android Auto会话通过显示屏上的软"断开连接"按钮以外的方式断开，且HU收到来自设备的"ByeBy |
| 288 | NR1L-PROJ-279 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当有线 Android Auto 发生异常断开（如 USB 数据中断且未收到 ByeBye 消息）时，系统应释放投屏资源 |
| 289 | NR1L-PROJ-280 | test_item | 含 CJK 字元 | won't be affected. ⏎  ⏎ 当有线 Android Auto 发生异常断开（如 USB 数据中断且未收到 ByeBye 消息）时，系统应释放投屏资源 |
| 290 | NR1L-PROJ-281 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (CarPlay |
| 291 | NR1L-PROJ-282 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (CarPlay |
| 292 | NR1L-PROJ-283 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (CarPlay |
| 293 | NR1L-PROJ-284 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (CarPlay |
| 294 | NR1L-PROJ-285 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Same Car |
| 295 | NR1L-PROJ-286 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Differen |
| 296 | NR1L-PROJ-287 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Android |
| 297 | NR1L-PROJ-288 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Android |
| 298 | NR1L-PROJ-289 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Android |
| 299 | NR1L-PROJ-290 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Android |
| 300 | NR1L-PROJ-291 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Same And |
| 301 | NR1L-PROJ-292 | test_item | 含 CJK 字元 | ection manager. ⏎  ⏎ HU 应将与每个端口号以及 HMI USB 源相连接的所有投屏设备都置于投屏管理器可供选择的设备列表中。 ⏎  ⏎ (Differen |
| 302 | NR1L-PROJ-293 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 303 | NR1L-PROJ-294 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 304 | NR1L-PROJ-295 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 305 | NR1L-PROJ-296 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 306 | NR1L-PROJ-297 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 307 | NR1L-PROJ-298 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 308 | NR1L-PROJ-299 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 309 | NR1L-PROJ-300 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 310 | NR1L-PROJ-301 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 311 | NR1L-PROJ-302 | test_item | 含 CJK 字元 | s face the rear. ⏎  ⏎ HU应禁用任何后排USB集线器（前排座椅后方，面向第二排/第三排座椅）上的CarPlay。Refresh车机应参考USB主机 |
| 312 | NR1L-PROJ-303 | test_item | 含 CJK 字元 | tion established ⏎  ⏎ HU应根据首次建立的连接来确定哪个媒体设备连接到HMI USB源。 ⏎  ⏎ (Front USB-A → first-connec |
| 313 | NR1L-PROJ-304 | test_item | 含 CJK 字元 | tion established ⏎  ⏎ HU应根据首次建立的连接来确定哪个媒体设备连接到HMI USB源。 ⏎  ⏎ (Front USB-B → first-connec |
| 314 | NR1L-PROJ-305 | test_item | 含 CJK 字元 | tion established ⏎  ⏎ HU应根据首次建立的连接来确定哪个媒体设备连接到HMI USB源。 ⏎  ⏎ (Rear USB-A → first-connect |
| 315 | NR1L-PROJ-306 | test_item | 含 CJK 字元 | tion established ⏎  ⏎ HU应根据首次建立的连接来确定哪个媒体设备连接到HMI USB源。 ⏎  ⏎ (Rear USB-B → first-connect |
| 316 | NR1L-PROJ-307 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 317 | NR1L-PROJ-308 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 318 | NR1L-PROJ-309 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 319 | NR1L-PROJ-310 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 320 | NR1L-PROJ-311 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 321 | NR1L-PROJ-312 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 322 | NR1L-PROJ-313 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 323 | NR1L-PROJ-314 | test_item | 含 CJK 字元 | USB Source. ⏎  ⏎ USB HUB没有连接投屏设备，当有投屏设备插入时，在没有无线投屏设备连接的情况下，自动连接插入的投屏设备，并禁用该HUB下的USB口 |
| 324 | NR1L-PROJ-315 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 325 | NR1L-PROJ-316 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 326 | NR1L-PROJ-317 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 327 | NR1L-PROJ-318 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 328 | NR1L-PROJ-319 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 329 | NR1L-PROJ-320 | test_item | 含 CJK 字元 | ch devices” pop-up ⏎  ⏎ 如果存在正在使用的投屏设备，且有新的投屏设备连接到任何端口，HU 应弹窗提示“您想要切换设备吗”。 ⏎  ⏎ (Active p |
| 330 | NR1L-PROJ-321 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 331 | NR1L-PROJ-322 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 332 | NR1L-PROJ-323 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 333 | NR1L-PROJ-324 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 334 | NR1L-PROJ-325 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 335 | NR1L-PROJ-326 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 336 | NR1L-PROJ-327 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 337 | NR1L-PROJ-328 | test_item | 含 CJK 字元 | ll be charge only. ⏎  ⏎ 如果主机上有正在活跃的投屏会话，该HMI USB源上的任何媒体设备都应处于「仅充电（Charge only）」状态 ⏎  ⏎ ( |
| 338 | NR1L-PROJ-329 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 339 | NR1L-PROJ-330 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 340 | NR1L-PROJ-331 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 341 | NR1L-PROJ-332 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 342 | NR1L-PROJ-333 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 343 | NR1L-PROJ-334 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 344 | NR1L-PROJ-335 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 345 | NR1L-PROJ-336 | test_item | 含 CJK 字元 | hat HMI USB Source ⏎  ⏎ 如果用户选择连接投屏设备。即使已经有设备已有线连接，投屏设备也应可供选择，设备可以做切换 ⏎  ⏎ (Media device |
| 346 | NR1L-PROJ-337 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 347 | NR1L-PROJ-338 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 348 | NR1L-PROJ-339 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 349 | NR1L-PROJ-340 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 350 | NR1L-PROJ-341 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 351 | NR1L-PROJ-342 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 352 | NR1L-PROJ-343 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 353 | NR1L-PROJ-344 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 354 | NR1L-PROJ-345 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 355 | NR1L-PROJ-346 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 356 | NR1L-PROJ-347 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 357 | NR1L-PROJ-348 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 358 | NR1L-PROJ-349 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 359 | NR1L-PROJ-350 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 360 | NR1L-PROJ-351 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 361 | NR1L-PROJ-352 | test_item | 含 CJK 字元 | evice as a source. ⏎  ⏎ 当 USB HUB 上激活的媒体或投屏设备断开后，系统应更新 HMI 列表，将另一个端口上已连接的设备状态设置为可选 ( |
| 362 | NR1L-PROJ-353 | test_item | 含 CJK 字元 | lay associated HMI. ⏎ 如果CarPlay设备连接到后部USB端口之一，HU应仅将其视为媒体设备/ipod，不得显示任何与CarPlay相关的H |
| 363 | NR1L-PROJ-354 | test_item | 含 CJK 字元 | lay associated HMI. ⏎ 如果CarPlay设备连接到后部USB端口之一，HU应仅将其视为媒体设备/ipod，不得显示任何与CarPlay相关的H |
| 364 | NR1L-PROJ-355 | test_item | 含 CJK 字元 | lay associated HMI. ⏎ 如果CarPlay设备连接到后部USB端口之一，HU应仅将其视为媒体设备/ipod，不得显示任何与CarPlay相关的H |
| 365 | NR1L-PROJ-356 | test_item | 含 CJK 字元 | lay associated HMI. ⏎ 如果CarPlay设备连接到后部USB端口之一，HU应仅将其视为媒体设备/ipod，不得显示任何与CarPlay相关的H |
| 366 | NR1L-PROJ-357 | test_item | 含 CJK 字元 | lay associated HMI. ⏎ 如果CarPlay设备连接到后部USB端口之一，HU应仅将其视为媒体设备/ipod，不得显示任何与CarPlay相关的H |
| 367 | NR1L-PROJ-358 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Front USB-A-1 m |
| 368 | NR1L-PROJ-359 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Front USB-A-2 m |
| 369 | NR1L-PROJ-360 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Front USB-B-1 m |
| 370 | NR1L-PROJ-361 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Front USB-B-2 m |
| 371 | NR1L-PROJ-362 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Rear USB-A-1 me |
| 372 | NR1L-PROJ-363 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Rear USB-A-2 me |
| 373 | NR1L-PROJ-364 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Rear USB-B-1 me |
| 374 | NR1L-PROJ-365 | test_item | 含 CJK 字元 | that HMI USB Sourc ⏎  ⏎ 若USB HUB已经连接着媒体设备，该HUB的其他USB口连接媒体设备只能做充电功能 ⏎  ⏎ (Rear USB-B-2 me |
| 375 | NR1L-PROJ-366 | test_item | 含 CJK 字元 | eference document. ⏎  ⏎ 仪表导航卡片需显示TBT信息 ⏎  ⏎ (CarPlay navigation active → instrument clus |
| 376 | NR1L-PROJ-367 | test_item | 含 CJK 字元 | eference document. ⏎  ⏎ 仪表导航卡片需显示TBT信息 ⏎  ⏎ (Android Auto navigation active → instrument |
| 377 | NR1L-PROJ-368 | test_item | 含 CJK 字元 | efined in VF176. ⏎  ⏎ HU应根据“Name of the Arrow”列和VF176中定义的相应枚举将上述值映射到图形中。 ⏎  ⏎ (CarPlay r |
| 378 | NR1L-PROJ-369 | test_item | 含 CJK 字元 | efined in VF176. ⏎  ⏎ HU应根据“Name of the Arrow”列和VF176中定义的相应枚举将上述值映射到图形中。 ⏎  ⏎ (Android A |
| 379 | NR1L-PROJ-370 | test_item | 含 CJK 字元 | defined in VF176. ⏎  ⏎ 对于CarPlay，HU应使用设备提供的ManeuverType、DrivingSide、JunctionType、Ju |
| 380 | NR1L-PROJ-371 | test_item | 含 CJK 字元 | in VF176. ⏎  ⏎ CarPlay 经过IAP协议接收DistanceToNextManeuverUnits导航相关信息 ⏎  ⏎ (CarPlay next-ma |
| 381 | NR1L-PROJ-372 | test_item | 含 CJK 字元 | in VF176. ⏎  ⏎ CarPlay 经过IAP协议接收DistanceToNextManeuverDisplayStr导航相关信息 ⏎  ⏎ (CarPlay ne |
| 382 | NR1L-PROJ-373 | test_item | 含 CJK 字元 | in VF176. ⏎  ⏎ CarPlay 经过IAP协议接收 AfterManeuverRoadName导航相关信息 ⏎  ⏎ (CarPlay AfterManeuve |
| 383 | NR1L-PROJ-374 | test_item | 含 CJK 字元 | defined in VF176. ⏎  ⏎ 对于Android Auto，HU应使用设备提供的Next Turn Enum、Next Turn Side、Turn |
| 384 | NR1L-PROJ-375 | test_item | 含 CJK 字元 | Signals in VF176. ⏎  ⏎ 对于Android Auto，HU应在VF176中的距离CAN信号中Next Turn Rounded Distanc。 |
| 385 | NR1L-PROJ-376 | test_item | 含 CJK 字元 | defined in VF176. ⏎  ⏎ 对于Android Auto，HU应在VF176中定义的道路名称文本CAN信号中填充Next Turn Road Nam |
| 386 | NR1L-PROJ-377 | test_item | 含 CJK 字元 | defined in VF176. ⏎  ⏎ 对于Android Auto，HU应在VF176中定义的单位CAN信号中填充Rounded Distance Units |
| 387 | NR1L-PROJ-378 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Cold rest |
| 388 | NR1L-PROJ-379 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Warm rest |
| 389 | NR1L-PROJ-380 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Cold rest |
| 390 | NR1L-PROJ-381 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Warm rest |
| 391 | NR1L-PROJ-382 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Cold rest |
| 392 | NR1L-PROJ-383 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Warm rest |
| 393 | NR1L-PROJ-384 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Cold rest |
| 394 | NR1L-PROJ-385 | test_item | 含 CJK 字元 | that is available. ⏎  ⏎ 当HU重新启动时，应尝试连接HU关机前已连接的设备。如果该设备不可用，则应连接到最高优先级设备。 ⏎  ⏎ (Warm rest |
| 395 | NR1L-PROJ-386 | test_item | 含 CJK 字元 | rity non-favorite. ⏎  ⏎ 非最喜爱设备连接成功后，它自动成为除去最喜爱设备之外的最高优先级设备 ⏎  ⏎ (CarPlay non-favorite de |
| 396 | NR1L-PROJ-387 | test_item | 含 CJK 字元 | rity non-favorite. ⏎  ⏎ 非最喜爱设备连接成功后，它自动成为除去最喜爱设备之外的最高优先级设备 ⏎  ⏎ (Android Auto non-favori |
| 397 | NR1L-PROJ-388 | test_item | 含 CJK 字元 | in the App drawer ⏎  ⏎ 这些设置可在手机设置中找到，也可通过 App drawer 中的图标访问。 ⏎  ⏎ (Device Manager acces |
| 398 | NR1L-PROJ-389 | test_item | 含 CJK 字元 | in the App drawer ⏎  ⏎ 这些设置可在手机设置中找到，也可通过 App drawer 中的图标访问。 ⏎  ⏎ (Device Manager acces |
| 399 | NR1L-PROJ-390 | test_item | 含 CJK 字元 | in the App drawer ⏎  ⏎ 这些设置可在手机设置中找到，也可通过 App drawer 中的图标访问。 ⏎  ⏎ (Device Manager acces |
| 400 | NR1L-PROJ-391 | test_item | 含 CJK 字元 | in the App drawer ⏎  ⏎ 这些设置可在手机设置中找到，也可通过 App drawer 中的图标访问。 ⏎  ⏎ (Device Manager acces |
| 401 | NR1L-PROJ-392 | test_item | 含 CJK 字元 | o lowest priority. ⏎  ⏎ 投屏设备应按优先级从高到低列出。 ⏎  ⏎ (Mixed favorite and non-favorite devices → |
| 402 | NR1L-PROJ-393 | test_item | 含 CJK 字元 | o lowest priority. ⏎  ⏎ 投屏设备应按优先级从高到低列出。 ⏎  ⏎ (Three non-favorite devices, no favorite s |
| 403 | NR1L-PROJ-394 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (CarPlay |
| 404 | NR1L-PROJ-395 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (CarPlay |
| 405 | NR1L-PROJ-396 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (Four pre |
| 406 | NR1L-PROJ-397 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (Android |
| 407 | NR1L-PROJ-398 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (Android |
| 408 | NR1L-PROJ-399 | test_item | 含 CJK 字元 | ice. Refer to HMI. ⏎  ⏎ 投屏设备设置应显示投屏设备列表。当用户选择一个设备时，他们应该能够更改该设备的设置。请参阅HMI。 ⏎  ⏎ (Four pre |
| 409 | NR1L-PROJ-400 | test_item | 含 CJK 字元 | highest priority. ⏎  ⏎ 如果有最喜欢的设备，则该设备应具有最高优先级。 ⏎  ⏎ (CarPlay Device B set as Favorite 1 |
| 410 | NR1L-PROJ-401 | test_item | 含 CJK 字元 | highest priority. ⏎  ⏎ 如果有最喜欢的设备，则该设备应具有最高优先级。 ⏎  ⏎ (CarPlay Device B removed from favo |
| 411 | NR1L-PROJ-402 | test_item | 含 CJK 字元 | highest priority. ⏎  ⏎ 如果有最喜欢的设备，则该设备应具有最高优先级。 ⏎  ⏎ (Android Auto Device B set as Favor |
| 412 | NR1L-PROJ-403 | test_item | 含 CJK 字元 | highest priority. ⏎  ⏎ 如果有最喜欢的设备，则该设备应具有最高优先级。 ⏎  ⏎ (Android Auto Device B removed from |
| 413 | NR1L-PROJ-404 | test_item | 含 CJK 字元 | evice to the list. ⏎  ⏎ 如果投屏设备列表已满，并且连接了新的启用投屏的设备，则HU应删除优先级最低的设备，然后将新设备添加到列表中。 ⏎  ⏎ (Car |
| 414 | NR1L-PROJ-405 | test_item | 含 CJK 字元 | evice to the list. ⏎  ⏎ 如果投屏设备列表已满，并且连接了新的启用投屏的设备，则HU应删除优先级最低的设备，然后将新设备添加到列表中。 ⏎  ⏎ (And |
| 415 | NR1L-PROJ-406 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 416 | NR1L-PROJ-407 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 417 | NR1L-PROJ-408 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 418 | NR1L-PROJ-409 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 419 | NR1L-PROJ-410 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 420 | NR1L-PROJ-411 | test_item | 含 CJK 字元 | USB port number. ⏎  ⏎  ⏎ 如果同时检测到多个新的投屏设备，当不存在last device时HU应在连接到最低USB端口号的设备上启动投屏模式；若存 |
| 421 | NR1L-PROJ-412 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 422 | NR1L-PROJ-413 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 423 | NR1L-PROJ-414 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 424 | NR1L-PROJ-415 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 425 | NR1L-PROJ-415 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 426 | NR1L-PROJ-416 | test_item | 含 CJK 字元 | d phone functions. ⏎  ⏎ 如果未对某一设备勾选“启用投屏模式”，则该设备将无法作为投屏设备进行连接。但该设备仍可充电，并能作为本地媒体和手机功能的 |
| 427 | NR1L-PROJ-417 | test_item | 含 CJK 字元 | projection device. ⏎  ⏎ 如果对某一设备勾选了“启用投屏模式”选项，那么该设备就可作为投屏设备进行连接。 ⏎  ⏎ (CarPlay device con |
| 428 | NR1L-PROJ-418 | test_item | 含 CJK 字元 | projection device. ⏎  ⏎ 如果对某一设备勾选了“启用投屏模式”选项，那么该设备就可作为投屏设备进行连接。 ⏎  ⏎ (Android Auto devic |
| 429 | NR1L-PROJ-419 | test_item | 含 CJK 字元 | = [Apps_Selected]. ⏎  ⏎ 如果 HU 当前的音频源是投屏设备，则 HU 应将 $HUModeStatus$ 设置为 [Apps_Selected] |
| 430 | NR1L-PROJ-420 | test_item | 含 CJK 字元 | = [Apps_Selected]. ⏎  ⏎ 如果 HU 当前的音频源是投屏设备，则 HU 应将 $HUModeStatus$ 设置为 [Apps_Selected] |
| 431 | NR1L-PROJ-421 | test_item | 含 CJK 字元 | = [Apps_Selected]. ⏎  ⏎ 如果 HU 当前的音频源是投屏设备，则 HU 应将 $HUModeStatus$ 设置为 [Apps_Selected] |
| 432 | NR1L-PROJ-422 | test_item | 含 CJK 字元 | = [Apps_Selected]. ⏎  ⏎ 如果 HU 当前的音频源是投屏设备，则 HU 应将 $HUModeStatus$ 设置为 [Apps_Selected] |
| 433 | NR1L-PROJ-423 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 434 | NR1L-PROJ-424 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 435 | NR1L-PROJ-425 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 436 | NR1L-PROJ-426 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 437 | NR1L-PROJ-427 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 438 | NR1L-PROJ-428 | test_item | 含 CJK 字元 | Flow] document. ⏎  ⏎ HMI要求在最新版本的[VP4R 8.4"投屏设备逻辑和流程]或[VP5 12"投屏设备HMI逻辑和流程]或[R1 7"投屏设 |
| 439 | NR1L-PROJ-429 | test_item | 含 CJK 字元 | 80 to 1278 x 704 ⏎  ⏎ HU将从800 x 480扩展到1278 x 704 ⏎  ⏎ (CarPlay 800x480 source scaled up |
| 440 | NR1L-PROJ-430 | test_item | 含 CJK 字元 | 80 to 1278 x 704 ⏎  ⏎ HU将从800 x 480扩展到1278 x 704 ⏎  ⏎ (Android Auto 800x480 source scale |
| 441 | NR1L-PROJ-431 | test_item | 含 CJK 字元 | 0 to 1024 x 562. ⏎  ⏎ HU将从800 x 480扩展到1024 x 562。 ⏎  ⏎ (CarPlay 800x480 source scaled up |
| 442 | NR1L-PROJ-432 | test_item | 含 CJK 字元 | 0 to 1024 x 562. ⏎  ⏎ HU将从800 x 480扩展到1024 x 562。 ⏎  ⏎ (Android Auto 800x480 source scal |
| 443 | NR1L-PROJ-433 | test_item | 含 CJK 字元 | from the phone. ⏎  ⏎ HU应支持手机投屏空间的最小分辨率为800 x 480。 ⏎  ⏎ (CarPlay minimum 800x480 source |
| 444 | NR1L-PROJ-434 | test_item | 含 CJK 字元 | from the phone. ⏎  ⏎ HU应支持手机投屏空间的最小分辨率为800 x 480。 ⏎  ⏎ (Android Auto minimum 800x480 so |
| 445 | NR1L-PROJ-435 | test_item | 含 CJK 字元 | ti-touch gestures. ⏎  ⏎ 显示器应为使用多点触控手势的电容式触摸屏。 ⏎  ⏎ (CarPlay single-touch input tracked o |
| 446 | NR1L-PROJ-436 | test_item | 含 CJK 字元 | ti-touch gestures. ⏎  ⏎ 显示器应为使用多点触控手势的电容式触摸屏。 ⏎  ⏎ (Android Auto single-touch swipe and |
| 447 | NR1L-PROJ-437 | test_item | 含 CJK 字元 | ti-touch gestures. ⏎  ⏎ 显示器应为使用多点触控手势的电容式触摸屏。 ⏎  ⏎ (Android Auto multiple simultaneous t |
| 448 | NR1L-PROJ-438 | test_item | 含 CJK 字元 | h a 60 Hz refresh. ⏎  ⏎ 颜色应为每像素24位RGB颜色，刷新频率为60 Hz。 ⏎  ⏎ (CarPlay projected output refre |
| 449 | NR1L-PROJ-439 | test_item | 含 CJK 字元 | h a 60 Hz refresh. ⏎  ⏎ 颜色应为每像素24位RGB颜色，刷新频率为60 Hz。 ⏎  ⏎ (CarPlay projected output rende |
| 450 | NR1L-PROJ-440 | test_item | 含 CJK 字元 | h a 60 Hz refresh. ⏎  ⏎ 颜色应为每像素24位RGB颜色，刷新频率为60 Hz。 ⏎  ⏎ (Android Auto projection displa |
| 451 | NR1L-PROJ-441 | test_item | 含 CJK 字元 | s are recommended. ⏎  ⏎ 所有像素必须对最终用户可见。建议使用方形像素。 ⏎  ⏎ (CarPlay Display Protocol → all pix |
| 452 | NR1L-PROJ-442 | test_item | 含 CJK 字元 | s are recommended. ⏎  ⏎ 所有像素必须对最终用户可见。建议使用方形像素。 ⏎  ⏎ (Android Auto projection display re |
| 453 | NR1L-PROJ-443 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (CarPlay Phon |
| 454 | NR1L-PROJ-444 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (CarPlay Musi |
| 455 | NR1L-PROJ-445 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (CarPlay Mess |
| 456 | NR1L-PROJ-446 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (CarPlay Navi |
| 457 | NR1L-PROJ-447 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (CarPlay Medi |
| 458 | NR1L-PROJ-448 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (Android Auto |
| 459 | NR1L-PROJ-449 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (Android Auto |
| 460 | NR1L-PROJ-450 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (Android Auto |
| 461 | NR1L-PROJ-451 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (Android Auto |
| 462 | NR1L-PROJ-452 | test_item | 含 CJK 字元 | CarPlay、Android Auto和Baidu CarLife应支持以下任务和功能：电话、音乐、消息、导航和媒体等应用程序。 ⏎  ⏎ (Android Auto |
| 463 | NR1L-PROJ-453 | test_item | 含 CJK 字元 | lity audio codecs. ⏎  ⏎ 音频应使用24KHz采样率的高质量音频编解码器进行处理。 ⏎  ⏎ (CarPlay Test App Audio Playba |
| 464 | NR1L-PROJ-454 | test_item | 含 CJK 字元 | lity audio codecs. ⏎  ⏎ 音频应使用24KHz采样率的高质量音频编解码器进行处理。 ⏎  ⏎ (Android Auto media, VR, and n |
| 465 | NR1L-PROJ-455 | test_item | 含 CJK 字元 | ed USB 2.0 Spec. ⏎  ⏎ HU应使用高速USB 2.0规范与iPhone通信。 ⏎  ⏎ (Wired CarPlay over USB 2.0 cable |
| 466 | NR1L-PROJ-456 | test_item | 含 CJK 字元 | ed USB 2.0 Spec. ⏎  ⏎ HU应使用高速USB 2.0规范与iPhone通信。 ⏎  ⏎ (Wired Android Auto over USB 2.0 c |
| 467 | NR1L-PROJ-457 | test_item | 含 CJK 字元 | USB Role Switch. ⏎  ⏎ HU必须支持USB Host模式并允许USB Role Switch. ⏎  ⏎ (USB Host mode → external |
| 468 | NR1L-PROJ-458 | test_item | 含 CJK 字元 | USB Role Switch. ⏎  ⏎ HU必须支持USB Host模式并允许USB Role Switch. ⏎  ⏎ (USB Role Switch → wired |
| 469 | NR1L-PROJ-459 | test_item | 含 CJK 字元 | USB Role Switch. ⏎  ⏎ HU必须支持USB Host模式并允许USB Role Switch. ⏎  ⏎ (USB Role Switch → wired |
| 470 | NR1L-PROJ-460 | test_item | 含 CJK 字元 | eposition the map. ⏎  ⏎ 用户应能够使用滑动手势重新定位地图。 ⏎  ⏎ (Single-finger swipe repositions the map |
| 471 | NR1L-PROJ-461 | test_item | 含 CJK 字元 | eposition the map. ⏎  ⏎ 用户应能够使用滑动手势重新定位地图。 ⏎  ⏎ (Single-finger swipe repositions the map |
| 472 | NR1L-PROJ-462 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Two-finger pinch zooms out the map i |
| 473 | NR1L-PROJ-463 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Two-finger spread zooms in the map i |
| 474 | NR1L-PROJ-464 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Map zoom-out stops at minimum zoom l |
| 475 | NR1L-PROJ-465 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Map zoom-in stops at maximum zoom le |
| 476 | NR1L-PROJ-466 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Two-finger pinch zooms out the map i |
| 477 | NR1L-PROJ-467 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Two-finger spread zooms in the map i |
| 478 | NR1L-PROJ-468 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Map zoom-out stops at minimum zoom l |
| 479 | NR1L-PROJ-469 | test_item | 含 CJK 字元 | he map in and out. ⏎  ⏎ 用户应能够使用多点触控手势放大和缩小地图。 ⏎  ⏎ (Map zoom-in stops at maximum zoom le |
| 480 | NR1L-PROJ-470 | test_item | 含 CJK 字元 | point of interest. ⏎  ⏎ 用户可以通过激活 Siri 并输入地址或兴趣点来设定路线。 ⏎  ⏎ (Siri route entry by point of |
| 481 | NR1L-PROJ-471 | test_item | 含 CJK 字元 | point of interest. ⏎  ⏎ 用户可以通过激活 Siri 并输入地址或兴趣点来设定路线。 ⏎  ⏎ (Siri route entry by point of |
| 482 | NR1L-PROJ-472 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (CarPlay |
| 483 | NR1L-PROJ-473 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (CarPlay |
| 484 | NR1L-PROJ-474 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (CarPlay |
| 485 | NR1L-PROJ-475 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (Android |
| 486 | NR1L-PROJ-476 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (Android |
| 487 | NR1L-PROJ-477 | test_item | 含 CJK 字元 | udio requirements. ⏎  ⏎ 一旦选定路线，逐段的导航指示就会发送至车辆的音响系统。有关导航音频的要求，请参考{CFTS019}。 ⏎  ⏎ (Android |
| 488 | NR1L-PROJ-478 | test_item | 含 CJK 字元 | le USB hub. ⏎  ⏎ iPhone 可通过车载 USB 集线器与 HU 进行连接。 ⏎  ⏎ (iPhone inserted via USB hub → CarP |
| 489 | NR1L-PROJ-479 | test_item | 含 CJK 字元 | 0 specification. ⏎  ⏎ HU应支持iAP2客户端和USB 2.0规范。 ⏎  ⏎ (USB ATS capture → HU sends iAP2 iden |
| 490 | NR1L-PROJ-480 | test_item | 含 CJK 字元 | ce Class UUIDs. ⏎  ⏎ EIR数据包必须包含128位CarPlay服务UUID（0xEC884348CD4140A29727575D50BF1FD3） |
| 491 | NR1L-PROJ-481 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 492 | NR1L-PROJ-482 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 493 | NR1L-PROJ-483 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 494 | NR1L-PROJ-484 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 495 | NR1L-PROJ-485 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 496 | NR1L-PROJ-486 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 497 | NR1L-PROJ-487 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 498 | NR1L-PROJ-488 | test_item | 含 CJK 字元 | he same way ⏎  ⏎ CarPlay必须参与附件内置用户体验中可用的UI配置概念。如果内置功能UI的大小和/或位置可以由用户调整（多UI布局配置），则Car |
| 499 | NR1L-PROJ-489 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (CarPlay entertainment audio meets |
| 500 | NR1L-PROJ-490 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (Local media ducks and mixes durin |
| 501 | NR1L-PROJ-491 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (CarPlay media ducks and mixes dur |
| 502 | NR1L-PROJ-492 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (CarPlay text message alert tone a |
| 503 | NR1L-PROJ-493 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (CarPlay phone call audio provides |
| 504 | NR1L-PROJ-494 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (Local music source preempts CarPl |
| 505 | NR1L-PROJ-495 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (CarPlay music source preempts loc |
| 506 | NR1L-PROJ-496 | test_item | 含 CJK 字元 | Section 3.2.7.2  ⏎  ⏎ HU应支持章节3.2.7.2中提到的所有Must需求 ⏎  ⏎ (Audio source focus stays correct |
| 507 | NR1L-PROJ-497 | test_item | 含 CJK 字元 | item on a device. ⏎  ⏎ 正在播放功能使配件能够显示有关当前“正在播放”的信息 ⏎ 设备上的媒体源和媒体项目。 ⏎  ⏎ (Instrument cluste |
| 508 | NR1L-PROJ-498 | test_item | 含 CJK 字元 | item on a device. ⏎  ⏎ 正在播放功能使配件能够显示有关当前“正在播放”的信息 ⏎ 设备上的媒体源和媒体项目。 ⏎  ⏎ (Media app list di |
| 509 | NR1L-PROJ-499 | test_item | 含 CJK 字元 | item on a device. ⏎  ⏎ 正在播放功能使配件能够显示有关当前“正在播放”的信息 ⏎ 设备上的媒体源和媒体项目。 ⏎  ⏎ (Status bar displa |
| 510 | NR1L-PROJ-500 | test_item | 含 CJK 字元 | item on a device. ⏎  ⏎ 正在播放功能使配件能够显示有关当前“正在播放”的信息 ⏎ 设备上的媒体源和媒体项目。 ⏎  ⏎ (Widget displays C |
| 511 | NR1L-PROJ-501 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 512 | NR1L-PROJ-502 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 513 | NR1L-PROJ-503 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 514 | NR1L-PROJ-504 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 515 | NR1L-PROJ-505 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 516 | NR1L-PROJ-506 | test_item | 含 CJK 字元 | o/from the device. ⏎  ⏎ 通信功能包括以下子功能： ⏎ ●呼叫状态更新为附件提供有关支持以下功能的设备上呼叫状态的更新 ⏎ 电话和/或FaceTime音频 |
| 517 | NR1L-PROJ-507 | test_item | 含 CJK 字元 | s state at a time. ⏎  ⏎ 电话呼叫：实体正在进行电话呼叫。一次只能有一个实体处于此状态。 ⏎  ⏎ (Local music pauses during |
| 518 | NR1L-PROJ-508 | test_item | 含 CJK 字元 | s state at a time. ⏎  ⏎ 电话呼叫：实体正在进行电话呼叫。一次只能有一个实体处于此状态。 ⏎  ⏎ (CarPlay music pauses durin |
| 519 | NR1L-PROJ-509 | test_item | 含 CJK 字元 | s state at a time. ⏎  ⏎ 电话呼叫：实体正在进行电话呼叫。一次只能有一个实体处于此状态。 ⏎  ⏎ (Bluetooth call unavailable |
| 520 | NR1L-PROJ-510 | test_item | 含 CJK 字元 | s state at a time. ⏎  ⏎ 电话呼叫：实体正在进行电话呼叫。一次只能有一个实体处于此状态。 ⏎  ⏎ (CarPlay call unavailable w |
| 521 | NR1L-PROJ-511 | test_item | 含 CJK 字元 | s state at a time. ⏎  ⏎ 电话呼叫：实体正在进行电话呼叫。一次只能有一个实体处于此状态。 ⏎  ⏎ (Call state stays correct a |
| 522 | NR1L-PROJ-512 | test_item | 含 CJK 字元 | via A2DP (R06-210) ⏎  ⏎ 如果在连接 AAP 时，MD已连接至高级音频分发规范（A2DP）设备（包括主机单元（HU）），则媒体设备将保持 A2DP |
| 523 | NR1L-PROJ-513 | test_item | 含 CJK 字元 | via A2DP (R06-210) ⏎  ⏎ 如果在连接 AAP 时，MD已连接至高级音频分发规范（A2DP）设备（包括主机单元（HU）），则媒体设备将保持 A2DP |
| 524 | NR1L-PROJ-514 | test_item | 含 CJK 字元 | ssions (R05-450) ⏎  ⏎ HU不得支持多个并发投屏会话 ⏎  ⏎ (Second projection request rejected when user |
| 525 | NR1L-PROJ-515 | test_item | 含 CJK 字元 | ssions (R05-450) ⏎  ⏎ HU不得支持多个并发投屏会话 ⏎  ⏎ (First session terminated and switched to seco |
| 526 | NR1L-PROJ-516 | test_item | 含 CJK 字元 | media (R08-050) ⏎  ⏎ AAP媒体流必须与原生媒体互斥 ⏎  ⏎ (Native media preempts Android Auto music; And |
| 527 | NR1L-PROJ-517 | test_item | 含 CJK 字元 | media (R08-050) ⏎  ⏎ AAP媒体流必须与原生媒体互斥 ⏎  ⏎ (Android Auto music preempts native media; nat |
| 528 | NR1L-PROJ-518 | test_item | 含 CJK 字元 | media (R08-050) ⏎  ⏎ AAP媒体流必须与原生媒体互斥 ⏎  ⏎ (Media focus stays exclusive after repeated An |
| 529 | NR1L-PROJ-519 | test_item | 含 CJK 字元 | and other purposes ⏎  ⏎ 麦克风输入音频流：使用车辆内置麦克风捕获麦克风音频，并将该音频传输到MD，MD可将其用于自动语音识别（ASR）和其他用途 |
| 530 | NR1L-PROJ-520 | test_item | 含 CJK 字元 | for 16-bit samples ⏎  ⏎ 必须设置音频输入灵敏度 ⏎ 标准：90 dB SPL @ 1000 Hz → RMS = 2500（16位采样） ⏎  ⏎ (Mic |
| 531 | NR1L-PROJ-521 | test_item | 含 CJK 字元 | dB SPL input level ⏎  ⏎ 应该小于1%（总谐波失真） ⏎ 频率范围：100 Hz - 4000 Hz ⏎ 测试条件：90 dB SPL输入电平 ⏎  ⏎ 音訊輸入 |
| 532 | NR1L-PROJ-522 | test_item | 含 CJK 字元 | ut and audio outpu ⏎  ⏎ 车辆必须配备麦克风。自动语音识别（ASR）假定为对话式，涉及连续的音频输入和音频输出。 ⏎  ⏎ (Conversational |
| 533 | NR1L-PROJ-523 | test_item | 含 CJK 字元 | HFP v1.5 or later ⏎  ⏎ 为了在原生和投屏用户界面上提供一致的免提电话体验，AAP使用蓝牙免提配置文件（HFP），并设计为与HU OEM HMI共 |
| 534 | NR1L-PROJ-524 | test_item | 含 CJK 字元 | HFP v1.5 or later ⏎  ⏎ 为了在原生和投屏用户界面上提供一致的免提电话体验，AAP使用蓝牙免提配置文件（HFP），并设计为与HU OEM HMI共 |
| 535 | NR1L-PROJ-525 | test_item | 含 CJK 字元 | HFP v1.5 or later ⏎  ⏎ 为了在原生和投屏用户界面上提供一致的免提电话体验，AAP使用蓝牙免提配置文件（HFP），并设计为与HU OEM HMI共 |
| 536 | NR1L-PROJ-526 | test_item | 含 CJK 字元 | HFP v1.5 or later ⏎  ⏎ 为了在原生和投屏用户界面上提供一致的免提电话体验，AAP使用蓝牙免提配置文件（HFP），并设计为与HU OEM HMI共 |
| 537 | NR1L-PROJ-527 | test_item | 含 CJK 字元 | HFP v1.5 or later ⏎  ⏎ 为了在原生和投屏用户界面上提供一致的免提电话体验，AAP使用蓝牙免提配置文件（HFP），并设计为与HU OEM HMI共 |
| 538 | NR1L-PROJ-528 | test_item | 含 CJK 字元 | connected over AAP ⏎  ⏎ 在仪表盘、抬头显示等位置显示仅通过HFP连接的MD的电话数据的车辆，也必须显示通过AAP连接的手机的电话数据 ⏎  ⏎ (Ins |
| 539 | NR1L-PROJ-529 | test_item | 含 CJK 字元 | connected over AAP ⏎  ⏎ 在仪表盘、抬头显示等位置显示仅通过HFP连接的MD的电话数据的车辆，也必须显示通过AAP连接的手机的电话数据 ⏎  ⏎ (Sta |
| 540 | NR1L-PROJ-530 | test_item | 含 CJK 字元 | connected over AAP ⏎  ⏎ 在仪表盘、抬头显示等位置显示仅通过HFP连接的MD的电话数据的车辆，也必须显示通过AAP连接的手机的电话数据 ⏎  ⏎ (Wid |
| 541 | NR1L-PROJ-531 | test_item | 含 CJK 字元 | us and/or metadata ⏎  ⏎ 在仪表盘等位置显示原生媒体播放状态和/或元数据的车辆，也必须显示AAP媒体播放状态和/或元数据 ⏎  ⏎ (Instrument |
| 542 | NR1L-PROJ-532 | test_item | 含 CJK 字元 | us and/or metadata ⏎  ⏎ 在仪表盘等位置显示原生媒体播放状态和/或元数据的车辆，也必须显示AAP媒体播放状态和/或元数据 ⏎  ⏎ (Media app |
| 543 | NR1L-PROJ-533 | test_item | 含 CJK 字元 | us and/or metadata ⏎  ⏎ 在仪表盘等位置显示原生媒体播放状态和/或元数据的车辆，也必须显示AAP媒体播放状态和/或元数据 ⏎  ⏎ (Status bar |
| 544 | NR1L-PROJ-534 | test_item | 含 CJK 字元 | us and/or metadata ⏎  ⏎ 在仪表盘等位置显示原生媒体播放状态和/或元数据的车辆，也必须显示AAP媒体播放状态和/或元数据 ⏎  ⏎ (Native wid |
| 545 | NR1L-PROJ-535 | test_item | 含 CJK 字元 | -397 respectively. ⏎  ⏎ 在活跃的AAP会话期间，如果用户在软件中使HU显示屏静音或以其他方式黑屏，则HU必须重新打开显示屏并批准视频焦点请求，条 |
| 546 | NR1L-PROJ-536 | test_item | 含 CJK 字元 | -397 respectively. ⏎  ⏎ 在活跃的AAP会话期间，如果用户在软件中使HU显示屏静音或以其他方式黑屏，则HU必须重新打开显示屏并批准视频焦点请求，条 |
| 547 | NR1L-PROJ-537 | test_item | 含 CJK 字元 | -397 respectively. ⏎  ⏎ 在活跃的AAP会话期间，如果用户在软件中使HU显示屏静音或以其他方式黑屏，则HU必须重新打开显示屏并批准视频焦点请求，条 |
| 548 | NR1L-PROJ-538 | test_item | 含 CJK 字元 | mplete ⏎  ⏎ Android Auto将在应用启动器视图中显示自定义的车辆品牌Logo退出图标,OEM必须在HU认证完成前提供Logo ⏎  ⏎ (App launc |
| 549 | NR1L-PROJ-539 | test_item | 含 CJK 字元 | mplete ⏎  ⏎ Android Auto将在应用启动器视图中显示自定义的车辆品牌Logo退出图标,OEM必须在HU认证完成前提供Logo ⏎  ⏎ (Tapping t |
| 550 | NR1L-PROJ-540 | test_item | 含 CJK 字元 | h said MD(R04-462) ⏎  ⏎ 当HU在行程结束时进入低功耗、睡眠或待机状态，且其显示屏对用户呈现非瞬时关闭时，HU必须： ⏎ 通过发送ByeByeRequ |
| 551 | NR1L-PROJ-540 | test_item | 含 CJK 字元 | h said MD(R04-462) ⏎  ⏎ 当HU在行程结束时进入低功耗、睡眠或待机状态，且其显示屏对用户呈现非瞬时关闭时，HU必须： ⏎ 通过发送ByeByeRequ |
| 552 | NR1L-PROJ-541 | test_item | 含 CJK 字元 | or suspend-to-RAM) ⏎  ⏎ 对于在上次行程结束时AAP是最后可见上下文的任何显示屏（例如，当HU关机或进入低功耗模式如待机/空闲或挂起到RAM时）， |
| 553 | NR1L-PROJ-542 | test_item | 含 CJK 字元 | or suspend-to-RAM) ⏎  ⏎ 对于在上次行程结束时AAP是最后可见上下文的任何显示屏（例如，当HU关机或进入低功耗模式如待机/空闲或挂起到RAM时）， |
| 554 | NR1L-PROJ-543 | test_item | 含 CJK 字元 | or suspend-to-RAM) ⏎  ⏎ 对于在上次行程结束时AAP是最后可见上下文的任何显示屏（例如，当HU关机或进入低功耗模式如待机/空闲或挂起到RAM时）， |
| 555 | NR1L-PROJ-544 | test_item | 含 CJK 字元 | ation data from AAP ⏎ 在仪表盘、抬头显示、原生widget或其他设备上显示原生导航解决方案导航数据的车辆：必须显示来自AAP的导航数据 ⏎  ⏎ 儀表 |
| 556 | NR1L-PROJ-545 | test_item | 含 CJK 字元 | ation data from AAP ⏎ 在仪表盘、抬头显示、原生widget或其他设备上显示原生导航解决方案导航数据的车辆：必须显示来自AAP的导航数据 ⏎  ⏎ 儀表 |
| 557 | NR1L-PROJ-546 | test_item | 含 CJK 字元 | ation data from AAP ⏎ 在仪表盘、抬头显示、原生widget或其他设备上显示原生导航解决方案导航数据的车辆：必须显示来自AAP的导航数据 ⏎  ⏎ 儀表 |
| 558 | NR1L-PROJ-547 | test_item | 含 CJK 字元 | is True. ⏎  ⏎ oemIcon: 数据类型，可选* ⏎ 104 x 104像素PNG数据，代表车厂制造商的logo。图标应为纯白色，带有透明的alpha通道背 |
| 559 | NR1L-PROJ-548 | test_item | 含 CJK 字元 | is True. ⏎  ⏎ oemIcon: 数据类型，可选* ⏎ 104 x 104像素PNG数据，代表车厂制造商的logo。图标应为纯白色，带有透明的alpha通道背 |
| 560 | NR1L-PROJ-549 | test_item | 含 CJK 字元 | rship (page 160)). ⏎  ⏎ 在汽车的典型应用中，CarPlay 架构具有两个共用资源： ⏎ • 屏幕：汽车主机屏幕。 ⏎ • 主音频：全双工（输入和输出）音 |
| 561 | NR1L-PROJ-550 | test_item | 含 CJK 字元 | rship (page 160)). ⏎  ⏎ 在汽车的典型应用中，CarPlay 架构具有两个共用资源： ⏎ • 屏幕：汽车主机屏幕。 ⏎ • 主音频：全双工（输入和输出）音 |
| 562 | NR1L-PROJ-551 | test_item | 含 CJK 字元 | rship (page 160)). ⏎  ⏎ 在汽车的典型应用中，CarPlay 架构具有两个共用资源： ⏎ • 屏幕：汽车主机屏幕。 ⏎ • 主音频：全双工（输入和输出）音 |
| 563 | NR1L-PROJ-552 | test_item | 含 CJK 字元 | rship (page 160)). ⏎  ⏎ 在汽车的典型应用中，CarPlay 架构具有两个共用资源： ⏎ • 屏幕：汽车主机屏幕。 ⏎ • 主音频：全双工（输入和输出）音 |
| 564 | NR1L-PROJ-553 | test_item | 含 CJK 字元 | rship (page 160)). ⏎  ⏎ 在汽车的典型应用中，CarPlay 架构具有两个共用资源： ⏎ • 屏幕：汽车主机屏幕。 ⏎ • 主音频：全双工（输入和输出）音 |
| 565 | NR1L-PROJ-554 | test_item | 含 CJK 字元 | -375 (#R07-375) ). ⏎  ⏎ 当视频聚焦设置为“原生”模式以适用于某一显示器时，该主机必须不显示该显示器的投屏界面（R07-360（#R07-360） |
| 566 | NR1L-PROJ-555 | test_item | 含 CJK 字元 | -375 (#R07-375) ). ⏎  ⏎ 当视频聚焦设置为“原生”模式以适用于某一显示器时，该主机必须不显示该显示器的投屏界面（R07-360（#R07-360） |
| 567 | NR1L-PROJ-556 | test_item | 含 CJK 字元 | -375 (#R07-375) ). ⏎  ⏎ 当视频聚焦设置为“原生”模式以适用于某一显示器时，该主机必须不显示该显示器的投屏界面（R07-360（#R07-360） |
| 568 | NR1L-PROJ-557 | test_item | 含 CJK 字元 | -375 (#R07-375) ). ⏎  ⏎ 当视频聚焦设置为“原生”模式以适用于某一显示器时，该主机必须不显示该显示器的投屏界面（R07-360（#R07-360） |
| 569 | NR1L-PROJ-558 | test_item | 含 CJK 字元 | connection setup. ⏎  ⏎ 具备通过蓝牙及有线传输方式与设备连接功能的配件应采用“Out-of-Band ”功能，以简化蓝牙连接的设置过程。 ⏎  ⏎ US |
| 570 | NR1L-PROJ-559 | test_item | 含 CJK 字元 | connection setup. ⏎  ⏎ 具备通过蓝牙及有线传输方式与设备连接功能的配件应采用“Out-of-Band ”功能，以简化蓝牙连接的设置过程。 ⏎  ⏎ (W |
| 571 | Customer EA app待釐清 | test_item | 含 CJK 字元 | nd the accessory.  ⏎  ⏎ 外部配件（EA）框架为配件提供了与一个或多个应用程序进行通信的手段，通过 EA 会话实现通信，并提供读/写字节流接口。配 |
| 572 |  | test_item | 含 CJK 字元 | 前排 USB 連接埠可正常建立 iPod 連線 ⏎ Front USB Port Can Establish iPod Connection Normally. ⏎  ⏎ |
| 573 |  | test_item | 含 CJK 字元 | 中控 USB 連接埠可正常建立 iPod 連線 ⏎ Center console USB port can establish iPod connection no |
| 574 |  | test_item | 含 CJK 字元 | 後排 USB 連接埠可正常建立 iPod 連線 ⏎ Rear USB port can establish iPod connection normally. ⏎  ⏎ ( |
| 575 |  | test_item | 含 CJK 字元 | 拔掉數據線iPod自動斷開 ⏎ iPod automatically disconnects when unplugging data cable. ⏎  ⏎ (Data |
| 576 |  | test_item | 含 CJK 字元 | 多次插拔設備功能正常 ⏎ The device functions normally after being plugged and unplugged multi |
| 577 |  | test_item | 含 CJK 字元 | iAP2信息顯示正確 ⏎ iAP2 information is displayed correctly. ⏎  ⏎ (Initial USB connection → i |
| 578 |  | test_item | 含 CJK 字元 | 手機端修改信息，車機端可同步更新 ⏎ Modify information on the mobile device, the head unit can sync |
| 579 |  | test_item | 含 CJK 字元 | 手機關機清除所有信息 ⏎ Turn off your phone and clear all information. ⏎  ⏎ (Phone powered off → |
| 580 |  | test_item | 含 CJK 字元 | 異常斷開後無需重啓即可重連 ⏎ After abnormal disconnection, you can reconnect without restarting |
| 581 |  | test_item | 含 CJK 字元 | 設備識別爲CarPlay而非iPod ⏎ Device recognized as CarPlay instead of iPod. ⏎  ⏎ (CarPlay enabl |
| 582 |  | test_item | 含 CJK 字元 | 設備識別爲iPod而非CarPlay ⏎ Device recognized as iPod instead of CarPlay. ⏎  ⏎ (CarPlay disab |
| 583 |  | test_item | 含 CJK 字元 | 同一設備CarPlay和iPod互斥 ⏎ CarPlay and iPod are mutually exclusive for the same device. ⏎ |
| 584 |  | test_item | 含 CJK 字元 | 媒體庫8類分類顯示正確 ⏎ The 8 categories of the media library are displayed correctly. ⏎  ⏎ (iPo |
| 585 |  | test_item | 含 CJK 字元 | 支持播放列表所有子類功能 ⏎ Supports all subcategories of playlist functions. ⏎  ⏎ (Playlist subcat |
| 586 |  | test_item | 含 CJK 字元 | 支持新建播放列表功能 ⏎ Supports creating a new playlist. ⏎  ⏎ (New playlist after device creatio |
| 587 |  | test_item | 含 CJK 字元 | 支持藝術家列表所有子類功能 ⏎ Supports all subcategory functions of artist list. ⏎  ⏎ (Artist subcat |
| 588 |  | test_item | 含 CJK 字元 | 支持專輯列表所有子類功能 ⏎ Supports all subcategory functions of album list. ⏎  ⏎ (Album subcatego |
| 589 |  | test_item | 含 CJK 字元 | 支持流派列表所有子類功能 ⏎ Supports all subcategory functions of the genre list. ⏎  ⏎ (Genre subca |
| 590 |  | test_item | 含 CJK 字元 | 支持作曲家列表所有子類功能 ⏎ Supports all subcategory functions of composer list. ⏎  ⏎ (Composer su |
| 591 |  | test_item | 含 CJK 字元 | 支持有聲讀物列表所有子類功能 ⏎ Supports all subcategory functions of audiobook list. ⏎  ⏎ (Audiobook |
| 592 |  | test_item | 含 CJK 字元 | 支持播客列表所有子類功能 ⏎ Supports all subcategory functions of podcast list. ⏎  ⏎ (Podcast subca |
| 593 |  | test_item | 含 CJK 字元 | 支持播放列表搜索功能 ⏎ Support playlist search function. ⏎  ⏎ (Playlist search with partial keyw |
| 594 |  | test_item | 含 CJK 字元 | 支持藝術家列表搜索功能 ⏎ Support artist list search function. ⏎  ⏎ (Artist search with partial ke |
| 595 |  | test_item | 含 CJK 字元 | 支持專輯列表搜索功能 ⏎ Support album list search function. ⏎  ⏎ (Album search with partial keywo |
| 596 |  | test_item | 含 CJK 字元 | 支持流派列表搜索功能 ⏎ Supports genre list search function. ⏎  ⏎ (Genre search with partial keyw |
| 597 |  | test_item | 含 CJK 字元 | 支持作曲家列表搜索功能 ⏎ Support composer list search function. ⏎  ⏎ (Composer search with partia |
| 598 |  | test_item | 含 CJK 字元 | 支持歌曲列表搜索功能 ⏎ Support song list search function. ⏎  ⏎ (Song search with partial keyword |
| 599 |  | test_item | 含 CJK 字元 | 支持有聲讀物列表搜索功能 ⏎ Support audiobook list search function. ⏎  ⏎ (Audiobook search with par |
| 600 |  | test_item | 含 CJK 字元 | 支持播客列表搜索功能 ⏎ Support podcast list search function. ⏎  ⏎ (Podcast search with partial k |
| 601 |  | test_item | 含 CJK 字元 | 支持媒體庫歌曲選擇 ⏎ Support media library song selection. ⏎  ⏎ (Media library repeated song se |
| 602 |  | test_item | 含 CJK 字元 | 大量歌曲穩定性 ⏎ Massive song stability. ⏎  ⏎ (Media library with 3000 songs) |
| 603 |  | test_item | 含 CJK 字元 | 支持播放功能 ⏎ Support playback function. ⏎  ⏎ (Paused song → playback resumes) |
| 604 |  | test_item | 含 CJK 字元 | 支持暫停功能 ⏎ Support pause function. ⏎  ⏎ (Playing song → pause stops playback) |
| 605 |  | test_item | 含 CJK 字元 | 支持上一曲功能 ⏎ Support previous song function. ⏎  ⏎ (Previous track button → previous song) |
| 606 |  | test_item | 含 CJK 字元 | 支持下一曲功能 ⏎ Support next song function. ⏎  ⏎ (Next track button → next song) |
| 607 |  | test_item | 含 CJK 字元 | 播放/暫停/上下曲功能隨機切換依然可用 ⏎ Random switching of play/pause/up and down song functions is |
| 608 |  | test_item | 含 CJK 字元 | 支持快退功能 ⏎ Support rewind function. ⏎  ⏎ (Long press previous button → rewind) |
| 609 |  | test_item | 含 CJK 字元 | 支持快進功能 ⏎ Support fast forward function. ⏎  ⏎ (Long press next button → fast forward) |
| 610 |  | test_item | 含 CJK 字元 | 快進/快退隨機切換依然可用 ⏎ Fast forward/rewind random switching is still available. ⏎  ⏎ (Random |
| 611 |  | test_item | 含 CJK 字元 | 支持開啓隨機功能 ⏎ Supports enabling shuffle function. ⏎  ⏎ (Shuffle off → shuffle playback en |
| 612 |  | test_item | 含 CJK 字元 | 支持關閉隨機功能 ⏎ Supports disabling shuffle function. ⏎  ⏎ (Shuffle on → sequential playback |
| 613 |  | test_item | 含 CJK 字元 | 隨機功能開啓關閉功能正常 ⏎ Shuffle function enables and disables properly. ⏎  ⏎ (Shuffle toggle 5 |
| 614 |  | test_item | 含 CJK 字元 | 支持列表重複功能 ⏎ Support list repeat function. ⏎  ⏎ (List repeat on last track) |
| 615 |  | test_item | 含 CJK 字元 | 支持單曲重複功能 ⏎ Support single repeat function. ⏎  ⏎ (Single repeat current track) |
| 616 |  | test_item | 含 CJK 字元 | 支持關閉重複功能 ⏎ Supports disabling repeat function. ⏎  ⏎ (Repeat off on last track) |
| 617 |  | test_item | 含 CJK 字元 | 重複功能開啓關閉功能正常 ⏎ Repeat function enables and disables properly. ⏎  ⏎ (Repeat toggle 5 ti |
| 618 |  | test_item | 含 CJK 字元 | 支持方控暫停功能 ⏎ Supports steering wheel control pause function. ⏎  ⏎ (Pause button → audio |
| 619 |  | test_item | 含 CJK 字元 | 支持方控播放功能 ⏎ Supports steering wheel control play function. ⏎  ⏎ (From paused state, Pla |
| 620 |  | test_item | 含 CJK 字元 | 支持方控上一曲功能 ⏎ Supports steering wheel control previous track function. ⏎  ⏎ (Previous tr |
| 621 |  | test_item | 含 CJK 字元 | 支持方控下一曲功能 ⏎ Supports steering wheel control next track function. ⏎  ⏎ (Next track butt |
| 622 |  | test_item | 含 CJK 字元 | 支持方控音量增加功能 ⏎ Supports steering wheel control volume up function. ⏎  ⏎ (Volume up butto |
| 623 |  | test_item | 含 CJK 字元 | 支持方控音量降低功能 ⏎ Supports steering wheel control volume down function. ⏎  ⏎ (Volume down b |
| 624 |  | test_item | 含 CJK 字元 | 方控播放/暫停/上下曲/音量加減功能隨機切換依然可用 ⏎ Steering wheel controls for play/pause/previous/next/ |
| 625 |  | test_item | 含 CJK 字元 | 支持進度條拖拽到中間位置 ⏎ Supports dragging the progress bar to the middle position. ⏎  ⏎ (Drag t |
| 626 |  | test_item | 含 CJK 字元 | 支持進度條拖拽到末尾位置 ⏎ Supports dragging the progress bar to the end position. ⏎  ⏎ (Drag to e |
| 627 |  | test_item | 含 CJK 字元 | 支持進度條拖拽到起點位置 ⏎ Supports dragging the progress bar to the starting position. ⏎  ⏎ (Drag |
| 628 |  | test_item | 含 CJK 字元 | 支持進度條隨機切換到任意位置 ⏎ Support progress bar to switch to any position randomly. ⏎  ⏎ (Drag t |
| 629 |  | test_item | 含 CJK 字元 | 超長字符顯示規則 ⏎ Extra long character display rules. ⏎  ⏎ (Extra-long title displayed across |
| 630 |  | test_item | 含 CJK 字元 | 特殊符號顯示規則 ⏎ Special symbol display rules. ⏎  ⏎ (Special characters displayed across med |
| 631 |  | test_item | 含 CJK 字元 | Emoji / 生僻字顯示規則 ⏎ Emoji/rare word display rules. ⏎  ⏎ (Emoji and rare characters displ |
| 632 |  | test_item | 含 CJK 字元 | 媒體正在播放界面播放狀態實時更新 ⏎ The playing status of the media playing interface is updated in |
| 633 |  | test_item | 含 CJK 字元 | Widget界面播放狀態實時更新 ⏎ Widget interface playback status updated in real time. ⏎  ⏎ (Widget |
| 634 |  | test_item | 含 CJK 字元 | 狀態欄播放狀態實時更新 ⏎ Status bar playback status updated in real time. ⏎  ⏎ (Status bar title |
| 635 |  | test_item | 含 CJK 字元 | 狀態欄音樂信息點擊可跳轉 ⏎ Tap music info on status bar to navigate to playback interface. ⏎  ⏎ (T |
| 636 |  | test_item | 含 CJK 字元 | 儀表界面播放狀態實時更新 ⏎ Instrument cluster interface playback status updated in real time. ⏎ |
| 637 |  | test_item | 含 CJK 字元 | 存在專輯封面正常更新 ⏎ The album cover is updated normally. ⏎  ⏎ (With cover art → album cover d |
| 638 |  | test_item | 含 CJK 字元 | 無專輯封面顯示默認製造商圖標 ⏎ No album cover shows default manufacturer icon. ⏎  ⏎ (No cover art → |
| 639 |  | test_item | 含 CJK 字元 | 專輯封面實時更新 ⏎ Album cover updated in real time. ⏎  ⏎ (Cover refresh during track switch) |
| 640 |  | test_item | 含 CJK 字元 | 支持平衡器功能 ⏎ Support balancer function. ⏎  ⏎ (Balancer adjustment changes speaker output |
| 641 |  | test_item | 含 CJK 字元 | 支持均衡器功能 ⏎ Support equalizer function. ⏎  ⏎ (Equalizer adjustment changes treble mids a |
| 642 |  | test_item | 含 CJK 字元 | 32KHz音頻適配 ⏎ 32KHz audio adaptation support. ⏎  ⏎ (Play 32KHz audio → clear playback on |
| 643 |  | test_item | 含 CJK 字元 | 44.1KHz音頻適配 ⏎ 44.1KHz audio adaptation support. ⏎  ⏎ (Play 44.1KHz audio → clear playb |
| 644 |  | test_item | 含 CJK 字元 | 48KHz音頻適配 ⏎ 48KHz audio adaptation support. ⏎  ⏎ (Play 48KHz audio → clear playback on |
| 645 |  | test_item | 含 CJK 字元 | iPod音頻與電話互斥 ⏎ iPod audio and phone calls are mutually exclusive. ⏎  ⏎ (Phone call duri |
| 646 |  | test_item | 含 CJK 字元 | iPod音頻與藍牙音頻互斥 ⏎ iPod audio and Bluetooth audio are mutually exclusive. ⏎  ⏎ (Switch be |
| 647 |  | test_item | 含 CJK 字元 | iPod音頻與FM音頻互斥 ⏎ iPod audio and FM audio are mutually exclusive. ⏎  ⏎ (Switch between i |
| 648 |  | test_item | 含 CJK 字元 | iPod音頻與AM音頻互斥 ⏎ iPod audio and AM audio are mutually exclusive. ⏎  ⏎ (Switch between i |
| 649 |  | test_item | 含 CJK 字元 | iPod音頻與USB音樂互斥 ⏎ iPod audio and USB music are mutually exclusive. ⏎  ⏎ (Switch between |
| 650 |  | test_item | 含 CJK 字元 | 主界面入口可用 ⏎ The main interface entrance is available. ⏎  ⏎ (iPod connected → main interf |
| 651 |  | test_item | 含 CJK 字元 | 無設備連接時主界面不顯示入口 ⏎ The main interface does not display the entrance when there is no |
| 652 |  | test_item | 含 CJK 字元 | 主界面圖標多次進入退出均正常 ⏎ The main interface icon is normal after entering and exiting mult |
| 653 |  | test_item | 含 CJK 字元 | 媒體列表入口可用 ⏎ Media list entry available. ⏎  ⏎ (iPod connected → media list entry availab |
| 654 |  | test_item | 含 CJK 字元 | 無設備連接時媒體列表不顯示入口 ⏎ Media list does not display entry when no device is connected. ⏎  ⏎ |
| 655 |  | test_item | 含 CJK 字元 | 媒體列表圖標多次進入退出均正常 ⏎ The media list icon is normal after entering and exiting multipl |
| 656 |  | test_item | 含 CJK 字元 | iPod播放界面適配白天模式 ⏎ iPod playback interface adapted to day mode. ⏎  ⏎ (Night to day mode |
| 657 |  | test_item | 含 CJK 字元 | iPod播放界面適配黑夜模式 ⏎ iPod playback interface adapts to dark mode. ⏎  ⏎ (Day to night mode |
| 658 |  | test_item | 含 CJK 字元 | 日夜模式多次切換均顯示正常 ⏎ The day and night mode displays normal after multiple switches. ⏎  ⏎ ( |
| 659 |  | test_item | 含 CJK 字元 | 系統關機iPod正常斷開 ⏎ iPod disconnects normally when system powers off. ⏎  ⏎ (System power of |
| 660 |  | test_item | 含 CJK 字元 | 系統重新上電iPod自動連接 ⏎ When the system is powered on again, the iPod automatically conne |
| 661 |  | test_item | 含 CJK 字元 | 系統進入STR狀態iPod正常斷開 ⏎ The system enters the STR state and the iPod is disconnected n |
| 662 |  | test_item | 含 CJK 字元 | 系統退出STR狀態iPod自動連接 ⏎ The system exits the STR state and the iPod automatically conn |

### L — test_item 上半過長 (>50 tokens)（行計 91／列計 91）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 38 | NR1L-PROJ-029 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 39 | NR1L-PROJ-030 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 40 | NR1L-PROJ-031 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 41 | NR1L-PROJ-032 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 42 | NR1L-PROJ-033 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 43 | NR1L-PROJ-034 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 44 | NR1L-PROJ-035 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 45 | NR1L-PROJ-036 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 46 | NR1L-PROJ-037 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 47 | NR1L-PROJ-038 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 48 | NR1L-PROJ-039 | test_item | 上半 58 tokens > 50 | If the user selects to manually disconnect an active Wireless Projection session |
| 78 | NR1L-PROJ-069 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 79 | NR1L-PROJ-070 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 80 | NR1L-PROJ-071 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 81 | NR1L-PROJ-072 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 82 | NR1L-PROJ-073 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 83 | NR1L-PROJ-074 | test_item | 上半 59 tokens > 50 | When the user requests to initiate a CarPlay or Android Auto connection to a dev |
| 160 | NR1L-PROJ-151 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 161 | NR1L-PROJ-152 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 162 | NR1L-PROJ-153 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 163 | NR1L-PROJ-154 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 164 | NR1L-PROJ-155 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 165 | NR1L-PROJ-156 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 166 | NR1L-PROJ-157 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 167 | NR1L-PROJ-158 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 168 | NR1L-PROJ-159 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 169 | NR1L-PROJ-160 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 170 | NR1L-PROJ-161 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 171 | NR1L-PROJ-162 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 172 | NR1L-PROJ-163 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 173 | NR1L-PROJ-164 | test_item | 上半 57 tokens > 50 | When $VC_Veh_Line$ = [363 OR 376 OR 332 OR 250 OR 637 OR M189 OR M182 OR M240 OR |
| 262 | NR1L-PROJ-253 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 263 | NR1L-PROJ-254 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 264 | NR1L-PROJ-255 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 265 | NR1L-PROJ-256 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 266 | NR1L-PROJ-257 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 267 | NR1L-PROJ-258 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 268 | NR1L-PROJ-259 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 269 | NR1L-PROJ-260 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 270 | NR1L-PROJ-261 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 271 | NR1L-PROJ-262 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 272 | NR1L-PROJ-263 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 273 | NR1L-PROJ-264 | test_item | 上半 103 tokens > 50 | The HU shall populate the "Vehicle make" field in the service discovery response |
| 284 | NR1L-PROJ-275 | test_item | 上半 54 tokens > 50 | When a wireless or wired Android Auto session is disconnected via a method other |
| 285 | NR1L-PROJ-276 | test_item | 上半 54 tokens > 50 | When a wireless or wired Android Auto session is disconnected via a method other |
| 286 | NR1L-PROJ-277 | test_item | 上半 54 tokens > 50 | When a wireless or wired Android Auto session is disconnected via a method other |
| 287 | NR1L-PROJ-278 | test_item | 上半 54 tokens > 50 | When a wireless or wired Android Auto session is disconnected via a method other |
| 302 | NR1L-PROJ-293 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 303 | NR1L-PROJ-294 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 304 | NR1L-PROJ-295 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 305 | NR1L-PROJ-296 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 306 | NR1L-PROJ-297 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 307 | NR1L-PROJ-298 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 308 | NR1L-PROJ-299 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 309 | NR1L-PROJ-300 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 310 | NR1L-PROJ-301 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 311 | NR1L-PROJ-302 | test_item | 上半 58 tokens > 50 | The HU shall disable CarPlay on any rear USB hubs (behind the front row seats, f |
| 383 | NR1L-PROJ-374 | test_item | 上半 60 tokens > 50 | For Android Auto, the HU shall use a combination of the Next Turn Enum, Next Tur |
| 433 | NR1L-PROJ-423 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 434 | NR1L-PROJ-424 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 435 | NR1L-PROJ-425 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 436 | NR1L-PROJ-426 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 437 | NR1L-PROJ-427 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 438 | NR1L-PROJ-428 | test_item | 上半 61 tokens > 50 | HMI requirements are defined in the latest release of the [VP4R 8.4" Projection |
| 491 | NR1L-PROJ-481 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 492 | NR1L-PROJ-482 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 493 | NR1L-PROJ-483 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 494 | NR1L-PROJ-484 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 495 | NR1L-PROJ-485 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 496 | NR1L-PROJ-486 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 497 | NR1L-PROJ-487 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 498 | NR1L-PROJ-488 | test_item | 上半 55 tokens > 50 | CarPlay must participate in the UI configuration concepts available in the acces |
| 522 | NR1L-PROJ-512 | test_item | 上半 55 tokens > 50 | If the MD is connected to an Advanced Audio Distribution Profile (A2DP) device ( |
| 523 | NR1L-PROJ-513 | test_item | 上半 55 tokens > 50 | If the MD is connected to an Advanced Audio Distribution Profile (A2DP) device ( |
| 533 | NR1L-PROJ-523 | test_item | 上半 51 tokens > 50 | To provide a consistent hands-free telephony experience across both the native a |
| 534 | NR1L-PROJ-524 | test_item | 上半 51 tokens > 50 | To provide a consistent hands-free telephony experience across both the native a |
| 535 | NR1L-PROJ-525 | test_item | 上半 51 tokens > 50 | To provide a consistent hands-free telephony experience across both the native a |
| 536 | NR1L-PROJ-526 | test_item | 上半 51 tokens > 50 | To provide a consistent hands-free telephony experience across both the native a |
| 537 | NR1L-PROJ-527 | test_item | 上半 51 tokens > 50 | To provide a consistent hands-free telephony experience across both the native a |
| 545 | NR1L-PROJ-535 | test_item | 上半 98 tokens > 50 | In case the HU display is quieted or otherwise blanked in software by the user d |
| 546 | NR1L-PROJ-536 | test_item | 上半 98 tokens > 50 | In case the HU display is quieted or otherwise blanked in software by the user d |
| 547 | NR1L-PROJ-537 | test_item | 上半 98 tokens > 50 | In case the HU display is quieted or otherwise blanked in software by the user d |
| 550 | NR1L-PROJ-540 | test_item | 上半 64 tokens > 50 | When the HU enters a low-power, sleep, or standby state at the end of a drive, a |
| 551 | NR1L-PROJ-540 | test_item | 上半 64 tokens > 50 | When the HU enters a low-power, sleep, or standby state at the end of a drive, a |
| 558 | NR1L-PROJ-547 | test_item | 上半 149 tokens > 50 | oemIcon: data, N* ⏎ PNG data for 104 x 104 pixel icon representing the accessory m |
| 559 | NR1L-PROJ-548 | test_item | 上半 149 tokens > 50 | oemIcon: data, N* ⏎ PNG data for 104 x 104 pixel icon representing the accessory m |
| 560 | NR1L-PROJ-549 | test_item | 上半 85 tokens > 50 | In its typical embodiment in an automobile, the CarPlay architecture has two sha |
| 561 | NR1L-PROJ-550 | test_item | 上半 85 tokens > 50 | In its typical embodiment in an automobile, the CarPlay architecture has two sha |
| 562 | NR1L-PROJ-551 | test_item | 上半 85 tokens > 50 | In its typical embodiment in an automobile, the CarPlay architecture has two sha |
| 563 | NR1L-PROJ-552 | test_item | 上半 85 tokens > 50 | In its typical embodiment in an automobile, the CarPlay architecture has two sha |
| 564 | NR1L-PROJ-553 | test_item | 上半 85 tokens > 50 | In its typical embodiment in an automobile, the CarPlay architecture has two sha |

### M — 空欄三態（行計 96／列計 92）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 571 | Customer EA app待釐清 | pre | 空欄（非 NA、非 PENDING:） |  |
| 571 | Customer EA app待釐清 | proc | 空欄（非 NA、非 PENDING:） |  |
| 571 | Customer EA app待釐清 | er | 空欄（非 NA、非 PENDING:） |  |
| 571 | Customer EA app待釐清 | spec | 空欄（非 NA、非 PENDING:） |  |
| 572 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 573 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 574 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 575 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 576 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 577 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 578 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 579 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 580 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 581 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 582 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 583 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 584 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 585 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 586 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 587 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 588 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 589 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 590 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 591 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 592 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 593 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 594 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 595 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 596 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 597 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 598 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 599 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 600 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 601 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 602 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 603 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 604 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 605 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 606 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 607 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 608 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 609 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 610 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 611 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 612 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 613 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 614 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 615 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 616 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 617 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 618 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 619 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 620 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 621 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 622 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 623 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 624 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 625 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 626 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 627 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 628 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 629 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 630 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 631 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 632 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 633 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 634 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 635 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 636 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 637 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 638 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 639 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 640 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 641 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 642 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 643 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 644 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 645 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 646 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 647 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 648 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 649 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 650 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 651 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 652 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 653 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 654 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 655 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 656 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 657 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 658 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 659 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 660 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 661 |  | spec | 空欄（非 NA、非 PENDING:） |  |
| 662 |  | er | 空欄（非 NA、非 PENDING:） |  |
| 662 |  | spec | 空欄（非 NA、非 PENDING:） |  |

### N — 行尾多餘句號（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 237 | NR1L-PROJ-228 | er | 行尾多餘句號 | 1. The vehicle hardware includes GPS antenna and module. |

