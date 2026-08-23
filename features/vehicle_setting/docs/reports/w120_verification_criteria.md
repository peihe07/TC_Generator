# W-120 —— 037 之 `Verification Criteria`／`Verification Method` 二欄

**62 包 §5.5 之工單。逐事回報，未採用。**

## 1. 兩份 037 皆有此二欄，且皆 100% 非空

| 037 | leaf | `Verification Criteria` 非空 | `Verification Method` 非空 |
|---|---:|---:|---:|
| CFTS044（Part 1，4 份） | 237 | 237（100.0%） | 237（100.0%） |
| VF230（Part 2，11 份） | 619 | 619（100.0%） | 619（100.0%） |

→ **此二欄非 VF230 獨有**。Part 1 自 00 輪起即有，且同為 100% 非空。

`Verification Method` 之相異值（CFTS044，18 種）：

- `Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test
 validation test` — 88
- `Document/spec review
HU screen observation in vehicle` — 61
- `Document/spec review
HMI screen observation in vehicle.
 Unit test
 Integration test
 validation test` — 46
- `Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test` — 19
- `Requirement is not clear for HU and System handling part` — 10
- `Requirement is not clear. Need More information` — 1
- `* Confirm if Heated_Steering_Wheel == "Present" in PROXI` — 1
- `* Set $DriverSide$ = [Left Side] through CAN simulation
* In HMI Heated / Vented Seats screen, Heated Steering Wheel Icon shall be on left side` — 1
- `* Set $DriverSide$ = [Left Side] through CAN simulation
* In HMI Heated / Vented Seats screen, Heated Steering Wheel Icon shall be on right side` — 1
- `heated steering wheel icons shall be displayed on HMI` — 1
- `* Set below signal to the values through CAN simulation
$HSW_Stat$ == "OFF"
STATUS_CSWM.HSW_StatFailSts == "Fail_Not_Present"
SteeringWheelHeating.Req to "Requested"
* verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"` — 1
- `* Set below signal to the values through CAN simulation
$HSW_Stat$ == "ON"
STATUS_CSWM.HSW_StatFailSts == "Fail_Not_Present"
SteeringWheelHeating.Req to "Requested"
* verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF"` — 1
- `* Set below signal to the values through CAN simulation
STATUS_CSWM.FL_HS_STATFailSts == "Fail_Present"
SteeringWheelHeating.Req to "Requested"
* Verify HMI has to show proper error message according to HMI documents` — 1
- `* Set below signal through CAN simulation
* Verify the status gets updated in HMI` — 1
- `* Change signal value through CAN simulation
$HSW_Stat$ passes to "ON"
* HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"` — 1
- `* Change signal value through CAN simulation
$HSW_Stat$ passes to "OFF"
* HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF"` — 1
- `* Change the value STATUS_CSWM.HSW_StatFailSts  to "Fail_Present"
* Regardless of $HSW_Stat$, TLM_Display.GUI shall show corresponding icon as per HMI documents` — 1
- `Requirement is not clear` — 1

## 2. 既有作業從未取用此二欄 —— 零命中

**量測條件**：對下列標的以 `grep -rin` 搜 `verification criteria`／`verification method`（大小寫不分）。

| 標的 | 命中 |
|---|---:|
| `RULINGS.md`（63 條） | 0 |
| `framework.md` | 0 |
| `PLAYBOOK.md`／`RUNBOOK.md` | 0 |
| `features/vehicle_setting/scripts/`（28 支） | 0 |
| repo 根 `scripts/`（含 `recon.py`／`lint036.py`） | 0 |
| `docs/runtime/`（canon 與本 feature 之 profile） | 0 |
| `docs/handoff/`＋`docs/upstream/`（62 包與上繳 61 除外） | 0 |

`recon.py::survey_a03` 自 037 抽取之欄僅四：`categorization`／`asil`／`ftti`／`hmi source`(或 `source`)。**此二欄不在其列。**

唯一之全庫命中為他 feature 之 profile（`docs/runtime/profiles/FW036_R1L_BT_Profile.md:82`），其令「`Verification Method` 所述之情形須有明示之 recovery phase」——**證明該欄在別處已被視為可用之輸入**。

## 3. 取樣 10 個已交付 leaf —— VC 與實寫 ER 之並陳

**取樣條件**：`generated/batch*.json` 之 `tcs[].leaf_id` 於 CFTS044 037 有非空 `Verification Criteria` 者，依 `leaf_id` 升冪取前 10；同 leaf 取其最後出現之批次。

### `SWE1-VC-HeatedSteeringWheel-003`（batch04_v6.json）

- **037 `Verification Criteria`**：1. Power cycle the HU and verify heated steering wheel switch defaults to OFF state before any CAN signal is received.
2. Confirm the default OFF state is displayed in HMI within <Tdisplay>.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. The HU enters a sleep state on the BH-CAN bus
2. The heated steering wheel state is OFF

### `SWE1-VC-HeatedSteeringWheel-006`（batch04_v6.json）

- **037 `Verification Criteria`**：CAN signal shall be trigger
 with invalid values
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 1 (Heated_steering_wheel_low) is sent
2. HSW_display_initial is recorded as low
3. The heated steering wheel is still displayed as low, unchanged from HSW_display_initial

### `SWE1-VC-HeatedSteeringWheel-007`（batch05_v4.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI and also read the memory and check it contains the proper updated values.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 0 (Heated_steering_wheel_off) is sent
2. HSW_display_initial is recorded as off
3. The heated steering wheel is displayed as high

### `SWE1-VC-HeatedSteeringWheel-011`（batch05_v4.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent
2. The heated steering wheel switch reads selectable
3. The heated steering wheel switch is greyed out and shows a status of OFF

### `SWE1-VC-HeatedSteeringWheel-015`（batch06_v5.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI and also read the memory and check it contains the proper updated values.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CSWM.HSW_StatSts = 0 (OFF) is sent
2. The heated steering wheel reads off
3. The heated steering wheel is displayed as on

### `SWE1-VC-HeatedSteeringWheel-016`（batch07_v5.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI and also read the memory and check it contains the proper updated values.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CSWM.HSW_StatSts = 1 (ON) is sent
2. The heated steering wheel reads on
3. The heated steering wheel is displayed as off

### `SWE1-VC-HeatedSteeringWheel-021`（batch07_v5.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI and also read the memory and check it contains the proper updated values.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CSWM.HSW_StatSts = 0 (OFF) is sent
2. The heated steering wheel reads off
3. The heated steering wheel is displayed as on

### `SWE1-VC-HeatedSteeringWheel-022`（batch07_v5.json）

- **037 `Verification Criteria`**：CAN signal to be trigger
System update CAN value to HMI and also read the memory and check it contains the proper updated values.
- **037 `Verification Method`**：`Document/spec review
HU screen observation in vehicle.
 Unit test
 Integration test`
- **已交付 `expected_result`**：1. STATUS_CSWM.HSW_StatSts = 1 (ON) is sent
2. The heated steering wheel reads on
3. The heated steering wheel is displayed as off

### `SWE1-VC-HeatedSteeringWheelManagement-025`（batch11_v4.json）

- **037 `Verification Criteria`**：* Correct PROXI must be flashed
- **037 `Verification Method`**：`* Confirm if Heated_Steering_Wheel == "Present" in PROXI`
- **已交付 `expected_result`**：1. HSW_control_initial is recorded as not present
2. PROXI Heated_Steering_Wheel = 1 (Present) is accepted
3. The HU completes start-up
4. The heated steering wheel control is present on the Heated / Vented Seats screen

### `SWE1-VC-HeatedSteeringWheelManagement-026`（batch18_v3.json）

- **037 `Verification Criteria`**：HU is on
- **037 `Verification Method`**：`* Set $DriverSide$ = [Left Side] through CAN simulation
* In HMI Heated / Vented Seats screen, Heated Steering Wheel Icon shall be on left side`
- **已交付 `expected_result`**：1. PROXI Driver_Side = 0 (Left Side) is accepted
2. The HU completes start-up
3. PENDING: DR-5-B

## 5. 兩類離群值 —— 該欄承載之內容不齊一

| | CFTS044（237 leaf） | VF230（619 leaf） |
|---|---:|---:|
| 上游自述 `not clear` | 14（5.9%） | 90（14.5%） |
| VC/VM 含訊號路徑引用（`X.Y` 形態） | 6（2.5%） | 232（37.5%） |
| VC/VM 含 `CAN simulation` | 8 | 1 |

→ **VF230 之該欄遠比 CFTS044 豐富**（訊號引用 37.5% 對 2.5%），
  但同時上游自述 `not clear` 者亦達 90（14.5%）。
  **該欄之內容品質不齊一，不可整欄一體採信。**

## 6. 一個決定性之實例 —— A-VS118 之 4 leaf

A-VS118（37 輪 W-106）判定：`HSW_Cmd_Tlm` 於 LID 之 `Atlantis` 與
`Atlantis High` 兩欄組皆無值域、於 DBC 之 `SG_` 命中 0，故其 4 個 leaf
「訊號名可寫而值無從書寫」，於 38 輪 W-108(1) 判 **W2／`B6-value-absent`**。

**該 4 leaf 與「037 之 VC/VM 提及 `HSW_Cmd_Tlm` 者」為同一組**（各 4 個，逐一相符）：

| leaf | reqid | 037 `Verification Method` 之末行（逐字） |
|---|---|---|
| `SWE1-VC-HeatedSteeringWheelManagement-029` | 4859496 | * verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON" |
| `SWE1-VC-HeatedSteeringWheelManagement-030` | 4859497 | * verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF" |
| `SWE1-VC-HeatedSteeringWheelManagement-033` | 4859500 | * HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON" |
| `SWE1-VC-HeatedSteeringWheelManagement-034` | 4859501 | * HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF" |

→ **`TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"／"OFF"` 逐字載於上游 037**。

A-VS118 之結論建立於「查 LID 與 DBC 二源皆無」——
**該二源確實無，而值在 037 之一個從未被讀取之欄內**。
此非 A-VS118 判斷有誤，是其**搜尋範圍未含此欄**
（因全庫無人知其存在，見 §2）。

**本層未改該 4 leaf 之分級**：由 W2 轉 W0 須先裁定該欄之位階
（R-VS9(1)′ 令拼寫以 DBC 為權威、R-VS57(4) 令 WARN 須名與值域皆有來源，
二者皆未預設 037 之 VC/VM 為值域來源）。**請裁。**

## 4. 判斷 —— 是否為一個未被使用之權威來源

**是一個未被使用之來源；其是否為「權威」則不由本層認定。**

三項事實已足以支持前半：

1. 二欄於兩份 037 皆 100% 非空，且 **Part 1 之 237 leaf 亦然** ——  故此非 VF230 之新情形，而是**自 00 輪起即存在而未被察覺之輸入**。
2. 全庫零命中：63 條 R-VS、`framework.md`、全部腳本、canon 與本 feature 之 profile 皆未提及。**其未被取用不是裁定之結果，是從未進入視野。**
3. 同一欄在他 feature（BT）之 profile 中**已被立為書寫依據**，  故其非「不可用之欄」。

**後半（是否權威）須裁**，理由：

- `Verification Criteria` 為**上游 SWE.1 作者對「如何驗證此需求」之陳述**，  而 TC 之 `expected_result` 為**執行層對「可觀察之結果」之書寫**。  二者同指一事而位階不同 —— 若判前者為權威，則現行全部已交付 TC 之 ER   皆須回頭對照，**其影響及於 Part 1 之 86 條已交付 TC**（含已過 pilot #2 者）。
- 採用與否屬 **TC 內容書寫慣例之變更**（62 包 §5.5 末句），非執行層可自裁。

**本層未採用、未改任何 TC、未改任何條文。**

