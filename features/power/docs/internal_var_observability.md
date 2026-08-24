# 內部變數觀察途徑對照（來源：SYS3 SYSAD v1.1.0，2026-08-21）

Pei 裁定：觀察途徑翻閱內部資料夾。實查
`features/power/inputs/SYS3_CFTS_009_Power_Management_FM-WI-FSM-011-A01_
System Architectural Design_SYSAD_v1.1.0.docx`，逐字摘錄各變數之
定義與可觀察行為。**改寫原則：內部變數之檢查改寫為其 SYSAD 所載
行為後果之檢查（行為化）；有 HMI 設定畫面者直接讀畫面；
SYSAD 明載診斷指令者用診斷指令。**

## 定義（SYSAD「Feature Specific」節逐字）

| 變數 | SYSAD 定義 | 觀察途徑 |
|---|---|---|
| `Phone_Call.Info` | Internal variable used to identify if there is active phone call ongoing | 行為化：通話畫面／通話音訊存在與否 |
| `Rear_Camera_Enable.Info` | Internal variable to say Rear Camera View Image feature is activated or deactivated (shall not be misunderstood with feature enable/disable) | 行為化：倒車影像是否顯示 |
| `Antitheft_Activation.Req` | The variable to manage whether Antitheft is active | 行為化：見下 |
| `Antitheft_Result.Info` | Manages the Antitheft state | 行為化：Antitheft HMI screen |
| `RemStartFail` | The internal variable to manage the success or failure of remote start | 行為化：見下 |
| `Timeout1` | Timeout value specify maximum time vehicle can stay in Timed power state. Controlled by SwitchOff_Timeout_Setting.Req user selectable setting | **HMI 設定畫面**（timeout setting entry） |
| `STR_TIME` | The maximum time the vehicle stays in STR state. **Configurable through diagnostic command** | 診斷指令 |
| `SwitchOff_Timeout_Setting.Req` | user selectable setting（控制 Timeout1） | **HMI 設定畫面** |
| `Auto_SwitchOn_Setting.Req` | user selectable setting（V-CPU 於開機評估） | **HMI 設定畫面** |
| `VPLastStatus` | V-CPU 於開機評估之變數 | 行為化：見下 |

## 行為化改寫對照（SYSAD 行為條文逐字依據）

**`Antitheft_Activation.Req`**
- SYSAD：「HU shall set Antitheft_Activation.Req = True and show
  Splash Screen when power button or Radio_Btn0 is pressed in
  Standby/Sleep with Engineering Line deactivated」
- SYSAD：「If Antitheft_Result == Successfully from Standby/Sleep,
  HU shall apply Switch_Off_Time if needed and transition to Timed」
- `= True` 之可觀察後果：自 Standby/Sleep 按電源鍵 → 顯示
  Antitheft HMI screen（Timeout1 期間）
- `= False` 之可觀察後果：同操作直接正常開機，無 Antitheft 畫面
- 改寫式：`Press the power button and check that the Antitheft HMI
  screen is shown`（True）／`...check that the HU powers up without
  the Antitheft HMI screen`（False）

**`VPLastStatus`**
- SYSAD：「OperationalModeSts transitions from Ignition Off to
  another value... V-CPU evaluates Auto_SwitchOn_Setting.Req and
  VPLastStatus. If Auto_SwitchOn == ON, or Auto_SwitchOn ==
  Recall_Last AND VPLastStatus == ON, Early Splash component shows
  splash screen from splash partition for Response_Wait_Time」
- `= ON` 之可觀察後果：（Auto_SwitchOn=Recall_Last 前提下）下次
  ignition 轉出 Ignition_Off 時 HU 自動開機並顯示 splash
- `= OFF`：同條件下 HU 不自動開機
- 改寫式：`Send the signal $STATUS_BH_BCM1.OperationalModeSts$ =
  4 (Ignition_On) and check that the HU powers up automatically
  and shows the splash screen`（ON）

**`RemStartFail`**
- SYSAD：「(PhoneCall becomes NotActive && RemStartFail==True)
  /set RemStartFail=False」——與 Phone_Call 聯動之內部旗標
- 可觀察後果薄弱（無直接 HMI）。**維持變數名 + 行為間接驗證**：
  其 True 之效果由後續狀態轉移路徑體現（CFTS009-4941468 Timed
  分支）。改寫式：以「後續轉移至 Timed／Standby 之路徑」代
  直接讀值；無法間接驗證之列標 `PENDING: DR-PW23`

**`Phone_Call.Info`**
- `= Active`：`Place a phone call from the paired device and check
  that the call screen is shown`；`= Not_Active`：`End the call and
  check that the call screen is dismissed`

**`Timeout1`／`SwitchOff_Timeout_Setting.Req`／`Auto_SwitchOn_Setting.Req`**
- 讀值：`Open the <setting> entry in the HU menu and read the
  <setting> value`（row 165 已為此式）
- 作為 PRE 之設定：`HMI: "<setting>" is set to <值>`（SWC 句式）

**`Front_Panel_OnOff.Req`**
- SYSAD 無此名；相關者為 `$ICSPowerButton$`（「HW supplier shall
  ignore $ICSPowerButton$ transition」）。研判為實體電源鍵之
  內部表徵。改寫式：`Press the HU power button`（實體操作），
  觀察側依各列 ER。登記 **DR-PW24**：`Front_Panel_OnOff.Req` 與
  `$ICSPowerButton$` 之對應待上游確認。
