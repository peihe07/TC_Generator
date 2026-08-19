# B2 —— 「無對應」之相異行逐字與抽樣（R-P290）

> **本檔不作判定、不作摘要，逐字呈現。**
> 母體：「無對應」**36** 條，扣除 R-P288 之 **8** 條（施加相同而觀察／ER 相異）= **28** 條。
> 抽樣 **6** 條 = **21.4%**（≥ 20%），種子 `random.Random(43)`。
> **複核之問題**：該相異行是否應歸五值之某一（`boundary` / `timing` / `trigger_state` / `mode` / `input_data`）？

**抽樣清單**：`…-049`、`…-091`、`…-167`、`…-173`、`…-213`、`…-215`

## 一、全 28 條之相異行逐字

| tc | leaf | 對照 | 相異行 |
|---|---|---|---|
| `…-044` | `SWE-PM-011` | `…-049` | 1. Press the VR button with a short press and release it<br>1. Press the VR button with a long press and release it |
| `…-049` | `SWE-PM-011` | `…-044` | 1. Press the VR button with a long press and release it<br>1. Press the VR button with a short press and release it |
| `…-080` | `SWE-PM-020` | `…-081` | 3. TLM_Display.GUI is in Phone Main Screen<br>3. TLM_Display.GUI is on a screen other than Phone Main Screen |
| `…-081` | `SWE-PM-020` | `…-080` | 3. TLM_Display.GUI is on a screen other than Phone Main Screen<br>3. TLM_Display.GUI is in Phone Main Screen |
| `…-091` | `SWE-PM-025` | `…-092` | 1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user<br>1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user |
| `…-092` | `SWE-PM-025` | `…-091` | 1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user<br>1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user |
| `…-162` | `SWE-PM-066` | `…-163` | An SOS call is placed<br>An Assist call is placed |
| `…-163` | `SWE-PM-066` | `…-162` | An Assist call is placed<br>An SOS call is placed |
| `…-166` | `SWE-PM-069` | `…-167` | 3. The display is on the phone main screen<br>3. The display is on the phone projection call UI |
| `…-167` | `SWE-PM-069` | `…-166` | 3. The display is on the phone projection call UI<br>3. The display is on the phone main screen |
| `…-169` | `SWE-PM-074` | `…-170` | A FOTA update available for the Radio<br>A FOTA update available for the TBM |
| `…-170` | `SWE-PM-074` | `…-171` | A FOTA update available for the TBM<br>A FOTA update available for the ROV |
| `…-171` | `SWE-PM-074` | `…-170` | A FOTA update available for the ROV<br>A FOTA update available for the TBM |
| `…-172` | `SWE-PM-075` | `…-173` | 1. Leave the FOTA pop-up without any user interaction<br>1. Dismiss the FOTA pop-up on the screen |
| `…-173` | `SWE-PM-075` | `…-172` | 1. Dismiss the FOTA pop-up on the screen<br>1. Leave the FOTA pop-up without any user interaction |
| `…-177` | `SWE-PM-076` | `…-175` | 2. The HU is currently installing a firmware image<br>2. The HU is not installing a firmware image |
| `…-191` | `SWE-PM-099` | `…-193` | 4. The HU has not yet played the startup sound that day<br>4. The HU has already played the startup sound that day<br>1. Bring the HU through a startup that plays the animation<br>1. Let the clock pass midnight and start the HU again |
| `…-192` | `SWE-PM-099` | `…-194` | A manual time adjustment that changes the customer selected date<br>An automatic adjustment due to time zones or Daylight Savings Time |
| `…-194` | `SWE-PM-099` | `…-192` | An automatic adjustment due to time zones or Daylight Savings Time<br>A manual time adjustment that changes the customer selected date |
| `…-207` | `SWE-PM-104` | `…-208` | 1. Bring the HU to Timed mode for the first time in the bus cycle<br>1. Bring the HU to Full Operation mode for the first time in the bus cycle |
| `…-208` | `SWE-PM-104` | `…-207` | 1. Bring the HU to Full Operation mode for the first time in the bus cycle<br>1. Bring the HU to Timed mode for the first time in the bus cycle |
| `…-212` | `SWE-PM-105` | `…-218` | An ongoing call at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-213` | `SWE-PM-105` | `…-218` | A backup camera view at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-214` | `SWE-PM-105` | `…-218` | An incoming call at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-215` | `SWE-PM-105` | `…-218` | An outgoing call at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-216` | `SWE-PM-105` | `…-218` | A climate pop-up at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-217` | `SWE-PM-105` | `…-218` | An SOS or Assist call at the moment of the transition<br>A FOTA pop up at the moment of the transition |
| `…-218` | `SWE-PM-105` | `…-212` | A FOTA pop up at the moment of the transition<br>An ongoing call at the moment of the transition |

---

## 二、抽樣 6 條之全欄逐字

### 1 / 6 —— `NR1L-PowerManagement-049`（`SWE-PM-011`）

**`tc_title`**：VR button long press in IDLE mode transitions the HU to Full-Operation

**對照條 `NR1L-PowerManagement-044`**：VR button press in IDLE mode transitions the HU to Full-Operation

**相異行**：
```
1. Press the VR button with a long press and release it
1. Press the VR button with a short press and release it
```

**`test_procedure`**

本條：
```
1. Press the VR button with a long press and release it
2. Read the HU mode to check the transition to Full-Operation
```

對照：
```
1. Press the VR button with a short press and release it
2. Read the HU mode to check the transition to Full-Operation
```


### 2 / 6 —— `NR1L-PowerManagement-091`（`SWE-PM-025`）

**`tc_title`**：Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby

**對照條 `NR1L-PowerManagement-092`**：Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed

**相異行**：
```
1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user
1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user
```

**`test_procedure`**

本條：
```
1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

對照：
```
1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user
2. Read TLM_Status.Info to check that Timed state is kept
```


### 3 / 6 —— `NR1L-PowerManagement-167`（`SWE-PM-069`）

**`tc_title`**：The HU returns to IDLE when the call ends on the phone projection call UI

**對照條 `NR1L-PowerManagement-166`**：The HU returns to IDLE when the call ends on the phone main screen

**相異行**：
```
3. The display is on the phone projection call UI
3. The display is on the phone main screen
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone projection call UI
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone main screen
```


### 4 / 6 —— `NR1L-PowerManagement-173`（`SWE-PM-075`）

**`tc_title`**：The HU leaves Timed when the FOTA pop-up is dismissed

**對照條 `NR1L-PowerManagement-172`**：The HU leaves Timed one minute after the FOTA pop-up is left untouched

**相異行**：
```
1. Dismiss the FOTA pop-up on the screen
1. Leave the FOTA pop-up without any user interaction
```

**`test_procedure`**

本條：
```
1. Dismiss the FOTA pop-up on the screen
2. Read the HU mode to check the transition after the dismissal
```

對照：
```
1. Leave the FOTA pop-up without any user interaction
2. Read the HU mode after the idle period to check the transition
```


### 5 / 6 —— `NR1L-PowerManagement-213`（`SWE-PM-105`）

**`tc_title`**：A backup camera view temporarily skips the disclaimer and splash screens

**對照條 `NR1L-PowerManagement-218`**：A FOTA pop up temporarily skips the disclaimer and splash screens

**相異行**：
```
A backup camera view at the moment of the transition
A FOTA pop up at the moment of the transition
```

**`input_test_data`**

本條：
```
A backup camera view at the moment of the transition
```

對照：
```
A FOTA pop up at the moment of the transition
```


### 6 / 6 —— `NR1L-PowerManagement-215`（`SWE-PM-105`）

**`tc_title`**：An outgoing call temporarily skips the disclaimer and splash screens

**對照條 `NR1L-PowerManagement-218`**：A FOTA pop up temporarily skips the disclaimer and splash screens

**相異行**：
```
An outgoing call at the moment of the transition
A FOTA pop up at the moment of the transition
```

**`input_test_data`**

本條：
```
An outgoing call at the moment of the transition
```

對照：
```
A FOTA pop up at the moment of the transition
```

