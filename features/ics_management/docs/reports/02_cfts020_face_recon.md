# CFTS020 三面偵察 — 逐物件三軸實值與 R-ICS2 判定

> 下放包 02 作業 D。**不生 TC**（R-ICS9(e)）。
> 本檔由 `scripts/gen_face_recon.py` 產生，表格非人工謄寫。
> 抽取與判定條件見 `scripts/cfts020_probe.py` 檔頭。
> 判準（R-ICS2）：`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}`
> ∧ `EE ∋ {Atlantis High, All}`。軸不存在者標 **WARN-軸缺**，
> 不以章節標題之屬性代替（R-ICS9(b)）。

## §0 全文件母數（掃描條件見上）

- 物件總數 **2180**，相異 ObjectID **2180**
- `ECU` 軸不存在者 **1916**（87%）
- `Radio` 軸不存在 **10**、`EE Architecture` 軸不存在 **11**
- 判定分佈：{'不適用': 1916, 'WARN-軸缺': 236, '適用': 28}
- Artifact Type：{'Description': 160, 'Subsystem Functional Requirement': 2020}

## §A Display Control（SWRA 006／007／(011)）

### §1.5.1.1.1 HU behavior in response to ICS POWER hardkey pressed events {4819385}

物件 3 個，判定分佈 {'不適用': 3}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819386 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819387 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819388 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |

<details><summary>逐物件本文（逐字）</summary>

- **4819386**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819387**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note PITA4, "Screen Off and HU Power button selections shall be ignored while backup cam is being shown."
- **4819388**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.

</details>

### §1.5.1.1.2 HU behavior in response to ICS SCREEN OFF hardkey press events {4819389}

物件 1 個，判定分佈 {'不適用': 1}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819390 | 1.5.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |

<details><summary>逐物件本文（逐字）</summary>

- **4819390**（Subsystem Functional Requirement）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."

</details>

### §1.8.1.1.1 HU behavior in response to ICS POWER hardkey pressed events {4819556}

物件 8 個，判定分佈 {'不適用': 2, 'WARN-軸缺': 6}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819557 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, VP484, VP384 | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819558 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, VP384, VP5R120, VP4R84, R1L, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819559 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, VP484, VP4R84, R1L, R1L-R, R1H | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819560 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, VP384, R1L-R, VP4R84, VP484, R1H, R1M | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819561 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, VP5R120, R1L-R, VP484, R1L, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819562 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819563 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP484, VP5R120, VP384, R1H, R1M, VP4R84, R1L-R | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819564 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP4R84, R1L, R1L-R, VP5R120, R1M, R1H, VP384 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |

<details><summary>逐物件本文（逐字）</summary>

- **4819557**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819558**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819559**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819560**（Subsystem Functional Requirement）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819561**（Subsystem Functional Requirement）：If $Telematic_Power$ = [Full_Operation] and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity]. See {CFTS009-829}.
- **4819562**（Subsystem Functional Requirement）：During the '3-second' time period if the ICS Power button is pressed the HU shall cancel the "3-second" screen timer, shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and shall return to the previous 'HU Screen On' screen.
- **4819563**（Subsystem Functional Requirement）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819564**（Subsystem Functional Requirement）：If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen. See {CFTS009-829}.

</details>

### §1.8.1.1.3 HU behavior in response to ICS SCREEN OFF hardkey press events {4819570}

物件 6 個，判定分佈 {'WARN-軸缺': 6}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819571 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, VP5R120, VP484, VP4R84, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819572 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, R1M, R1H, VP384, VP5R120, VP484, R1L-R | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819573 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, R1L-R, R1H, VP484, R1M, VP5R120, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819574 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, R1L-R, VP5R120, R1H, R1M | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819575 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, VP384, VP4R84, R1L-R, VP5R120, VP484, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819576 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, VP484, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |

<details><summary>逐物件本文（逐字）</summary>

- **4819571**（Subsystem Functional Requirement）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819572**（Subsystem Functional Requirement）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS SCREEN OFF hardkey should be responded to, then the HU shall continue to send $TGW_DISP_STAT$ = [DISP_NORMAL], and $RQ_DISP_INTS$ <> [0% Intensity] until the 3 second "TOUCH SCREEN TO TURN ON" timer expires as defined in the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4.
- **4819573**（Subsystem Functional Requirement）：During the '3-second' time period if the ICS SCREEN OFF hardkey is pressed the HU shall cancel the "TOUCH SCREEN TO TURN ON" screen timer, the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819574**（Subsystem Functional Requirement）：After the '3-second' time period is complete, the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819575**（Subsystem Functional Requirement）：For the pop-ups stated in HMI core specification requirement H4; the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity] for the duration of the pop-up and then send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] once the pop-up expires.
- **4819576**（Subsystem Functional Requirement）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS SCREEN OFF hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.

</details>

## §B Browse Control（SWRA 003／004）

### §1.8.1.2 Rotary Knob Data Transfer {4819577}

物件 9 個，判定分佈 {'WARN-軸缺': 9}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819578 | 1.8.1.2 | Description | **軸缺** | VP484, VP384, R1L-R, R1M, VP4R84, R1H, R1L | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819579 | 1.8.1.2 | Description | **軸缺** | R1M, R1H, R1L-R, VP484, VP4R84, R1L, VP384 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819580 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, VP4R84, VP484, R1M, VP384 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819581 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP484, VP384, R1M, VP4R84, R1H | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819582 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L, VP384, VP4R84, VP484 | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819583 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819584 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, VP4R84, R1H, VP484, R1M, VP384 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819585 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, VP384, VP4R84, R1M, VP484, R1H, R1L-R | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819586 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP4R84, R1H, R1M, VP384, R1L, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |

<details><summary>逐物件本文（逐字）</summary>

- **4819578**（Description）：The ICS will send signals on the BH-CAN to communicate the status of the rotary knobs.
- **4819579**（Description）：This section describes the signals to be used to support the communication of knob rotations to the HU. Refer to the feature sections that describe specific features to determine how the knob information supports those features.
- **4819580**（Subsystem Functional Requirement）：The ICS shall send the $ICS_KNOB<n>_DIR$ and $ICS_KNOB<n>_VAL$ signals to indicate the periodic and on-change status of any physical knob on the ICS. Within the scope of this section the value of "<n>" will represent a value of 1 or 2 for the assigned knobs.
- **4819581**（Subsystem Functional Requirement）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$$ICS_KNOB2_DIR$ and $ICS_KNOB2_VAL$
- **4819582**（Subsystem Functional Requirement）：When a physical knob is not rotated, the ICS shall send the $ICS_KNOB<n>_DIR$ = [no change] signal. For this state, the value of $ICS_KNOB<n>_VAL$ shall be ignored by the receiving components and no action taken on the value.
- **4819583**（Subsystem Functional Requirement）：While a knob is being rotated, the ICS shall count the relative number of detents rotated through in <TPeriodToCountKnobDetents> seconds. The ICS shall send the information in a pair of on-change messages using the $ICS_KNOB<n>_DIR$ = [increment or  decrement] and $ICS_KNOB<n>_VAL$ = [1 to 63] signals and values and then within <TPeriodToSendNoChange> seconds send the $ICS_KNOB<n>_DIR$ = [Knob_no_change] and $ICS_KNOB<n>_VAL$ = [0] signals and values.
- **4819584**（Subsystem Functional Requirement）：When the ICS determines no change in the rotation direction or value, the ICS shall send $ICS_KNOB<n>_DIR$ = [no change] and $ICS_KNOB<n>_VAL$ = [0] signals and values at the scheduled periodic rate until the knob is rotated again.
- **4819585**（Subsystem Functional Requirement）：When the HU receives the $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$ signals it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819586**（Subsystem Functional Requirement）：When the HU receives $ICS_KNOB2_DIR$ and $ICS_KNOB2_VAL$ signals it shall determine the corresponding HMI screen to 'flow' to (Browse), if any, HMI screen to update (Scroll) or change in Entertainment Audio state ('Tune').

</details>

## §C Menu Navigation（SWRA 008／009）

### §1.8.1.1 Push Button Data Transfer {4819542}（僅 Enter／Back 相關物件另標）

物件 31 個，判定分佈 {'WARN-軸缺': 22, '不適用': 9}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819543 | 1.8.1.1 | Description | **軸缺** | R1M, VP4R84, R1L, VP484, R1H, VP384, R1L-R | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819544 | 1.8.1.1 | Description | FPDM | R1L-R, VP4R84, VP384, R1H, VP484, R1L, R1M | Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819545 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819546 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP484 | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819547 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, VP484, R1M, R1L, R1L-R, R1H | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819548 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, R1M, R1H, R1L-R, VP384, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819549 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, R1L, VP4R84, R1H, R1L-R, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819550 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1M, VP384, R1H, VP4R84, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819551 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, VP484, R1M, R1L-R, R1H, VP384 | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819552 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819553 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP384, R1H, VP484, R1M, VP4R84 | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819554 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, VP484 | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819555 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, VP484, VP384, R1L-R, VP4R84, R1M | Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819557 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, VP484, VP384 | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819558 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, VP384, VP5R120, VP4R84, R1L, VP484 | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819559 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, VP484, VP4R84, R1L, R1L-R, R1H | PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819560 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, VP384, R1L-R, VP4R84, VP484, R1H, R1M | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819561 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, VP5R120, R1L-R, VP484, R1L, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819562 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819563 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP484, VP5R120, VP384, R1H, R1M, VP4R84, R1L-R | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819564 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP4R84, R1L, R1L-R, VP5R120, R1M, R1H, VP384 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819566 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819567 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819568 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819569 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819571 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, VP5R120, VP484, VP4R84, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819572 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, R1M, R1H, VP384, VP5R120, VP484, R1L-R | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819573 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, R1L-R, R1H, VP484, R1M, VP5R120, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819574 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, R1L-R, VP5R120, R1H, R1M | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819575 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, VP384, VP4R84, R1L-R, VP5R120, VP484, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819576 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, VP484, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |

<details><summary>逐物件本文（逐字）</summary>

- **4819543**（Description）：The ICS will send signals on the BH-CAN to communicate the status of the mechanical push buttons. Note: Some signals may not be used for various pushbuttons based on the version of the ICS module that is present.
- **4819544**（Description）：This section describes the signals to be used to support the communication of button presses to the HU and the FPDM.  Refer to the sections that describe specific features to determine the specific requirements to support these features. See Section {CFTS022-679} for a discussion of Stuck Button Behavior.
- **4819545**（Subsystem Functional Requirement）：The ICS shall send the ICS signals to indicate the periodic and on-change status of any physical button on the ICS.
- **4819546**（Subsystem Functional Requirement）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICSMuteButton$$Enter_Button$$ICSScreenOffButton$$Back_Button$
- **4819547**（Subsystem Functional Requirement）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICSMuteButton$$Enter_Button$$ICSScreenOffButton$$ICSPowerButton$
- **4819548**（Subsystem Functional Requirement）：For all ICS buttons, the [not pressed] value shall be sent when the button is not pressed.
- **4819549**（Subsystem Functional Requirement）：When a physical button is pressed, the ICS shall send an on-change[pressed] signal value within a time period of <Tbutton>.
- **4819550**（Subsystem Functional Requirement）：As a physical button is pressed and held, the ICS shall continue to send the[pressed] value at a rate of <Tbutton> until the button is released.
- **4819551**（Subsystem Functional Requirement）：After a physical button press is released, the ICS shall send an on-change [not pressed] signal value.
- **4819552**（Subsystem Functional Requirement）：It may be possible that several buttons can be pressed at the same time. Each button event change (press or release) shall cause the ICS to send an on-change message with updated button status within the time period of <Tbutton>.
- **4819553**（Subsystem Functional Requirement）：When the HU receives $ICSMuteButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819554**（Subsystem Functional Requirement）：When the HU receives $Enter_Button$ = [pressed] or$Back_Button$ = [pressed] it shall determine the corresponding HMI screen to 'flow' to, if any.
- **4819555**（Subsystem Functional Requirement）：When the HU receives $Enter_Button$ = [pressed] it shall determine the corresponding HMI screen to 'flow' to, if any.
- **4819557**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819558**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819559**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819560**（Subsystem Functional Requirement）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819561**（Subsystem Functional Requirement）：If $Telematic_Power$ = [Full_Operation] and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity]. See {CFTS009-829}.
- **4819562**（Subsystem Functional Requirement）：During the '3-second' time period if the ICS Power button is pressed the HU shall cancel the "3-second" screen timer, shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and shall return to the previous 'HU Screen On' screen.
- **4819563**（Subsystem Functional Requirement）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819564**（Subsystem Functional Requirement）：If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen. See {CFTS009-829}.
- **4819566**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819567**（Subsystem Functional Requirement）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event for the Front Passenger Display or respond to it based on the current power On/Off state and screen priority state.  See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom.
- **4819568**（Subsystem Functional Requirement）：If the HU/Front Passenger Display is in the 'Front Passenger Display Screen ON' state ($TGW_FPDM_DISP_STAT$ = [DISP_NORMAL] and $FPDM_RQ_DISP_INTS$ <> [0% Intensity]) and the FPDM Screen is in the 'FPDM Screen ON' state ($FPDM_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_FPDM_DISP_STAT$ = [DISP_OFF], and send $FPDM_RQ_DISP_INTS$ = [0% Intensity].
- **4819569**（Subsystem Functional Requirement）：When the Front Passenger Display is in the 'Front Passenger Display Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_FPDM_DISP_STAT$ = [DISP_NORMAL] and $FPDM_RQ_DISP_INTS$ = [current non-zero value] and the Front Passenger Display shall return to the previous 'Front Passenger Display Screen ON' screen.
- **4819571**（Subsystem Functional Requirement）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819572**（Subsystem Functional Requirement）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS SCREEN OFF hardkey should be responded to, then the HU shall continue to send $TGW_DISP_STAT$ = [DISP_NORMAL], and $RQ_DISP_INTS$ <> [0% Intensity] until the 3 second "TOUCH SCREEN TO TURN ON" timer expires as defined in the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4.
- **4819573**（Subsystem Functional Requirement）：During the '3-second' time period if the ICS SCREEN OFF hardkey is pressed the HU shall cancel the "TOUCH SCREEN TO TURN ON" screen timer, the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819574**（Subsystem Functional Requirement）：After the '3-second' time period is complete, the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819575**（Subsystem Functional Requirement）：For the pop-ups stated in HMI core specification requirement H4; the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity] for the duration of the pop-up and then send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] once the pop-up expires.
- **4819576**（Subsystem Functional Requirement）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS SCREEN OFF hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.

</details>

### §1.8.1.3 Button Press Events {4819587}

物件 24 個，判定分佈 {'WARN-軸缺': 1, '不適用': 23}

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |
|---|---|---|---|---|---|---|---|
| 4819588 | 1.8.1.3 | Description | **軸缺** | VP384, R1M, R1L, VP484, R1L-R, R1H, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)） |
| 4819589 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819590 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP4R84, R1L, R1L-R, VP484, VP384, R1M, R1H | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819591 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP384, R1H, R1L-R, VP484, R1M, VP4R84, R1L | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819593 | 1.8.1.3.1 | Description | FPDM | VP4R84, VP484, R1L, R1H, R1L-R, R1M, VP384 | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819594 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP484, VP4R84 | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819595 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L, R1L-R, R1M, VP4R84, R1H, VP484, VP384 | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819596 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819597 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L-R, R1L, R1M, R1H, VP484, VP4R84, VP384 | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819599 | 1.8.1.3.2 | Description | FPDM, CCDMF | VP4R84, R1H, R1L, R1L-R, R1M, VP484, VP384 | Atlantis Mid, PowerNet, Atlantis High | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819600 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1H | Atlantis High | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ |
| 4819601 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP484, R1M, R1L-R, VP384, R1H, R1L, VP4R84 | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819602 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | VP384, R1H, VP4R84, R1M, R1L-R, VP484, R1L | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819603 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP384, R1L-R, VP484, R1L, R1H, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819604 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP384, R1M, VP484, R1L, VP4R84, R1H, R1L-R | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819605 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | R1L-R, VP4R84, R1M, VP384, R1H, VP484, R1L | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819606 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | R1H, R1M, R1L-R, R1L, VP4R84, VP484, VP384 | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819607 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819608 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP4R84, VP384, R1L-R, R1L, R1H, VP484, R1M | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819610 | 1.8.1.3.3 | Description | FPDM | VP4R84, VP484, R1L-R, R1M, R1L, R1H, VP384 | Atlantis Mid, PowerNet, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819611 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1H, VP4R84, R1L-R, VP484, VP384, R1L, R1M | PowerNet, Atlantis High, Atlantis Mid | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819612 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1M, R1L-R, R1H, VP484, VP384, R1L, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |
| 4819613 | 1.8.1.3.3 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）；Radio ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ |
| 4819614 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1L, VP384, VP484, R1L-R, VP4R84, R1H, R1M | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅ |

<details><summary>逐物件本文（逐字）</summary>

- **4819588**（Description）：There are several button press events that can be applied to the physical (hardkeys) and virtual (touchscreen) softkey presses. These events are described below. Refer to specific sections in this specification for the applied behavior related to these events.
- **4819589**（Subsystem Functional Requirement）：If the user touches a region of the screen that has no active screen object and then slides their finger onto an active screen object; regardless of whether the screen object has related 'Short Press', 'Long Press' or 'Press and Move' behavior, the HU/Front Passenger Display shall not play the softkey pressed tone Conf1 (See {CFTS019-723}) and shall determine that no 'Press' event has occurred (during the 'not pressed' to 'pressed' transition the user must press the screen within the boundary of the active screen object in order to determine that a Press event has occurred).
- **4819590**（Subsystem Functional Requirement）：Upon the initial transition to the pressed state, the HU/Front Passenger Display shall play the softkey pressed tone; either Conf1 for 'active' controls or Conf2 for 'inactive' controls (See {CFTS019-723}) and the HU/Front Passenger Display shall show the screen object in the 'pressed' state.
- **4819591**（Subsystem Functional Requirement）：The HU/Front Passenger Display shall determine which screen object (control) has been pressed and whether the object has 'Short Press', 'Long Press and Hold' or 'Press and Move' behavior.
- **4819593**（Description）：A short press event will be used by the HU/Front Passenger Display for hardkey or touch screen HMI controls that have behavior that is not related to how long the control is pressed or controls that can be moved ('dragged'). I.e. those that are not related to any Long Press or any Press and Move features.
- **4819594**（Subsystem Functional Requirement）：For 'active' controls, when a 'Short Press' event occurs, the HU shall immediately implement the action associated with the control (example actions are transitioning to some other state and displaying a corresponding screen) - See HMI Rule MCCA6. For 'inactive' controls no action is taken when the control is pressed (other than remaining on the same screen and, for touchscreen HUs, showing the softkey in the pressed state).
- **4819595**（Subsystem Functional Requirement）：For 'active' controls, when a 'Short Press' event occurs, the HU/Front Passenger Display shall immediately implement the action associated with the control (example actions are transitioning to some other state and displaying a corresponding screen). For 'inactive' controls no action is taken when the control is pressed (other than remaining on the same screen and, for touchscreen HUs/Front Passenger Display, showing the softkey in the pressed state).
- **4819596**（Subsystem Functional Requirement）：During the time that the HU senses that the control is pressed, all other control presses shall be ignored.
- **4819597**（Subsystem Functional Requirement）：When the HU determines the control is no longer being touched, the HU/Front Passenger Display shall prepare to act on the next control pressed event.
- **4819599**（Description）：A Long Press (or Press and Hold) event will be used by the HU/DCSD/CCDMF/Front Passenger Display for hardkey or touch screen HMI controls (ex. 'Line/Page Up/Down Accelerated List Scrolling', 'Storing Presets/Favorites', HVAC Temperature Up/Down, HVAC Blower Speed Up/Down, etc.) that have behavior that differs based on how long a control is pressed and the action to be taken for that screen control.
- **4819600**（Subsystem Functional Requirement）：The below requirements for long press event are only applicable for DCSD if $VC_VEH_LINE$ = [EJ]. These requirements shall be applied for the HVAC controls present in CFTS043 referring CFTS020 for long press event behavior.
- **4819601**（Subsystem Functional Requirement）：For some screen objects that have 'Long Press' control, the related action to take occurs after the initial time period has elapsed and then no further action is taken. For the 'Preset/Favorite Store' screen controls, the HU/DCSD/CCDMF/Front Passenger Display shall not act on the initial press event (leading edge) and shall wait to determine if the object has been pressed continuously for a period of <Tpress>. Once the time period of <Tpress> has elapsed, the HU/Front Passenger Display shall act on the press and hold event.
- **4819602**（Subsystem Functional Requirement）：For some screen objects that have 'Long Press' control, the related action to take occurs as soon as the button is pressed and again after the initial time period has elapsed and the action can be repeated if the control is continuously held. For the 'HVAC Temperature/Blower' screen controls, upon the initial transition to the pressed state, the HVAC shall act on the initial press event (leading edge) and shall wait to determine if the object has been pressed continuously for a period of <Tpress>. Once the time period of <Tpress> has elapsed, the HVAC shall act again and then shall repeat the action until the control is released, the user moves their finger to a region outside of the boundary of that screen object or until some other reason to stop is encountered (ex. Maximum Temperature reached and there is no wraparound behavior for this control).
- **4819603**（Subsystem Functional Requirement）：For screen objects that exhibit Long Press behavior, if the user is pressing the screen object and the <Tpress> time has not elapsed yet and the user moves their finger to a region outside of the boundary of that screen object, the HU/DCSD/CCDMF/Front Passenger Display shall cancel the Long Press timer (and shall not act upon this screen press event). In addition if the user moves to a region of the screen that has no active screen object and moves onto some other active screen object, the HU/DCSD/CCDMF/Front Passenger Display shall not act upon the other screen object (the user must release their finger from the screen before the HU/Front Passenger Display will act upon other screen objects).
- **4819604**（Subsystem Functional Requirement）：For controls that have a single action behavior, such as a Preset Storage behavior, when the <Tpress> timer has expired, the HU/DCSD/CCDMF/Front Passenger Display shall play the Confirmation Tone Conf3 (See {CFTS019-723} and HMI Rule RHP2), implement the action associated with the control (store the preset value) and theHU/DCSD/CCDMF/Front Passenger Display shall remain on the same screen but shall update the associated screen object as appropriate (ex. Radio Preset softkey label/background will change from 'HOLD to Set' to '89.7' and the softkey is shown in the 'currently selected' state).
- **4819605**（Subsystem Functional Requirement）：For screen objects that have a continuous action behavior, if the user slides off the screen object the HU/DCSD/CCDMF/Front Passenger Display shall treat this as if the user has released their finger from the screen - the user must release their finger from the screen and repress the screen object to start another Press and Hold event (if they slide back onto the object do not resume the action associated with the screen object).
- **4819606**（Subsystem Functional Requirement）：The value of <Tpress> shall be determined by the specific function that uses the long press event. Refer to the specific feature section for the <Tpress> timing.
- **4819607**（Subsystem Functional Requirement）：After the HU determines the initial press event applies to a screen control with long press behavior then; while that screen object continues to be pressed, it shall ignore all other screen press events.
- **4819608**（Subsystem Functional Requirement）：When the HU/DCSD/CCDMF/Front Passenger Display determines the control with long press behavior is no longer being touched, the HU/DCSD/CCDMF/Front Passenger Display shall prepare to act on the next control pressed event.
- **4819610**（Description）：A Press and Move event will be used by the HU/Front Passenger Display for all touch screen HMI controls (ex. 'Playtime Position Slider' for SAT Replay or Player sources that support playtime repositioning, 'List Slider', 'Audio Balance/Fade slider') that allow the customer to press and move their finger across the display.
- **4819611**（Subsystem Functional Requirement）：If the HU/Front Passenger Display determines that the screen object is a 'Press and Move' control, the HU/Front Passenger Display shall act on the initial press event (leading edge). The HU/Front Passenger Display shall react to the movement on the screen until the point where the screen is no longer being pressed.
- **4819612**（Subsystem Functional Requirement）：For screen objects that exhibit single direction Press and Move behavior (Vertical only or Horizontal only), if the user is pressing and moving the screen object in the adjustment direction and the user then moves their finger perpendicular to the adjustment direction and transitions to a region outside of the boundary of the screen object, the HU/Front Passenger Display shall terminate the Press and Move event (and shall not act any further upon this screen press event). The user must release their finger from the screen and repress the screen object to start another Press and Move event (if they slide back onto the object do not resume the action associated with the screen object).
- **4819613**（Subsystem Functional Requirement）：After the HU determines the initial press event applies to a screen control with press and move behavior then; while that screen object continues to be pressed, it shall ignore all other screen press events.
- **4819614**（Subsystem Functional Requirement）：When the HU/Front Passenger Display determines the control with press and move behavior is no longer being touched, the HU/Front Passenger Display shall prepare to act on the next control pressed event.

</details>

