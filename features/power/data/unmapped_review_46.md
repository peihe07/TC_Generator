# B1 —— 殘留「無對應」之複核素材（R-P305）

> **本檔不作判定、不作摘要，逐字呈現。**
> 母體 **6** 條（45 包：36 → 6）。**全數列出，非抽樣。**

> **複核之問題**：該相異行是否應歸五值之某一（`boundary` / `timing` / `trigger_state` / `mode` / `input_data`）？
> - 判**確無可歸** → 維持「無對應」，入驗證邊界
> - 判**謂詞不足** → **停，不寫回**，另包訂正（R-P305(b)）

> ⚠ 45 包自陳：分析層前次所舉之二例，其**成因診斷有誤**（判為謂詞不足，實為 `input_test_data` 之內容不當驅動判定），
> **而其結論（不應為「無對應」）正確** —— 診斷之誤不使結論失效，惟其推論不得沿用（R-P305 併記）。

**清單**：`…-001`、`…-004`、`…-163`、`…-164`、`…-203`、`…-204`

---

## 1 / 6 —— `NR1L-PowerManagement-001`（`SWE-PM-071`）

**對照條**：`NR1L-PowerManagement-004`

**相異行逐字**（已排除觀察步驟）：
```
1. Start the suspend-resume boot sequence
1. Start the suspend-resume boot sequence and let it progress normally
```

### 本條全欄

**`tc_title`**
```
Splash screen shown after SplashScreen_Time on normal boot
```

**`pre_conditions`**
```
1. A suspend-resume boot sequence is available on the bench
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Start the suspend-resume boot sequence
2. Read the TLM display before and after SplashScreen_Time to check that the splash screen is loaded
```

**`expected_result`**
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears before SplashScreen_Time has elapsed, and the splash screen is loaded once it has
```

### 對照條全欄

**`tc_title`**
```
Standard screen shown after StandardScreen_Time
```

**`pre_conditions`**
```
1. A suspend-resume boot sequence is available on the bench
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content before and after StandardScreen_Time to check that the standard screen is visualized
```

**`expected_result`**
```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized before StandardScreen_Time has elapsed, and it is visualized once that time has passed
```


## 2 / 6 —— `NR1L-PowerManagement-004`（`SWE-PM-071`）

**對照條**：`NR1L-PowerManagement-001`

**相異行逐字**（已排除觀察步驟）：
```
1. Start the suspend-resume boot sequence and let it progress normally
1. Start the suspend-resume boot sequence
```

### 本條全欄

**`tc_title`**
```
Standard screen shown after StandardScreen_Time
```

**`pre_conditions`**
```
1. A suspend-resume boot sequence is available on the bench
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content before and after StandardScreen_Time to check that the standard screen is visualized
```

**`expected_result`**
```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized before StandardScreen_Time has elapsed, and it is visualized once that time has passed
```

### 對照條全欄

**`tc_title`**
```
Splash screen shown after SplashScreen_Time on normal boot
```

**`pre_conditions`**
```
1. A suspend-resume boot sequence is available on the bench
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Start the suspend-resume boot sequence
2. Read the TLM display before and after SplashScreen_Time to check that the splash screen is loaded
```

**`expected_result`**
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears before SplashScreen_Time has elapsed, and the splash screen is loaded once it has
```


## 3 / 6 —— `NR1L-PowerManagement-163`（`SWE-PM-069`）

**對照條**：`NR1L-PowerManagement-164`

**相異行逐字**（已排除觀察步驟）：
```
3. The display is on the phone main screen
3. The display is on the phone projection call UI
```

### 本條全欄

**`tc_title`**
```
The HU returns to IDLE when the call ends on the phone main screen
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone main screen
```

**`input_test_data`**
```
An incoming phone call that then becomes inactive
```

**`test_procedure`**
```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```

**`expected_result`**
```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```

### 對照條全欄

**`tc_title`**
```
The HU returns to IDLE when the call ends on the phone projection call UI
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone projection call UI
```

**`input_test_data`**
```
An incoming phone call that then becomes inactive
```

**`test_procedure`**
```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```

**`expected_result`**
```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```


## 4 / 6 —— `NR1L-PowerManagement-164`（`SWE-PM-069`）

**對照條**：`NR1L-PowerManagement-163`

**相異行逐字**（已排除觀察步驟）：
```
3. The display is on the phone projection call UI
3. The display is on the phone main screen
```

### 本條全欄

**`tc_title`**
```
The HU returns to IDLE when the call ends on the phone projection call UI
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone projection call UI
```

**`input_test_data`**
```
An incoming phone call that then becomes inactive
```

**`test_procedure`**
```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```

**`expected_result`**
```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```

### 對照條全欄

**`tc_title`**
```
The HU returns to IDLE when the call ends on the phone main screen
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone main screen
```

**`input_test_data`**
```
An incoming phone call that then becomes inactive
```

**`test_procedure`**
```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```

**`expected_result`**
```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```


## 5 / 6 —— `NR1L-PowerManagement-203`（`SWE-PM-104`）

**對照條**：`NR1L-PowerManagement-204`

**相異行逐字**（已排除觀察步驟）：
```
1. Bring the HU to Timed mode for the first time in the bus cycle
1. Bring the HU to Full Operation mode for the first time in the bus cycle
```

### 本條全欄

**`tc_title`**
```
The splash and disclaimer screens appear on the first transition to Timed
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Bring the HU to Timed mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```

**`expected_result`**
```
1. The splash screen is shown
2. The disclaimer screen is shown
```

### 對照條全欄

**`tc_title`**
```
The splash and disclaimer screens appear on the first transition to Full Operation
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Bring the HU to Full Operation mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```

**`expected_result`**
```
1. The splash screen is shown
2. The disclaimer screen is shown
```


## 6 / 6 —— `NR1L-PowerManagement-204`（`SWE-PM-104`）

**對照條**：`NR1L-PowerManagement-203`

**相異行逐字**（已排除觀察步驟）：
```
1. Bring the HU to Full Operation mode for the first time in the bus cycle
1. Bring the HU to Timed mode for the first time in the bus cycle
```

### 本條全欄

**`tc_title`**
```
The splash and disclaimer screens appear on the first transition to Full Operation
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Bring the HU to Full Operation mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```

**`expected_result`**
```
1. The splash screen is shown
2. The disclaimer screen is shown
```

### 對照條全欄

**`tc_title`**
```
The splash and disclaimer screens appear on the first transition to Timed
```

**`pre_conditions`**
```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```

**`input_test_data`**
```
NA
```

**`test_procedure`**
```
1. Bring the HU to Timed mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```

**`expected_result`**
```
1. The splash screen is shown
2. The disclaimer screen is shown
```

