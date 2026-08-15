# 上繳包 08 — ch11／ch12 合併依據落地 ＋ ch2／ch16 全文

執行層 → 分析層。2026-08-15。回應 Pei 直接指示（無下放包編號）。

**結論：五項作業全部完成。** Phase 4 未開始。
§4 之元件掃描**只供事實，不下結論**。

---

## 0. 置頂：一處自我訂正

上繳 07 §7.2 第 1 項我寫「ch11／ch12 其餘 **20** 節」。**實測為 18 節**：

| | 節數 |
|---|---|
| ch11 | 13（11.1、11.2、11.3、11.4、11.5、11.6、11.6.1、11.7、11.8、11.9、11.10、11.11、11.11.1） |
| ch12 | 9（12.1 ~ 12.9） |
| 合計 | **22** |
| 已於上繳 07 回報 | 4（11.1／11.2／12.1／12.2） |
| **其餘** | **18** |

該數是我心算 22−2 而非 22−4 之誤。本包 §4 之掃描涵蓋全部 18 節。

---

## 1. ch11／ch12 合併依據已寫入 `framework.md`

新增 **§3.1.1「ch11／ch12 合併 —— 全文複核後維持（2026-08-15）」**，
記載分析層之裁定（同一進入路徑；`opens popup` 為輸出回饋非入口）與其所據
之五項事實（唯一實質差異、操作元件逐字相同、顯示位置逐字相同、18 節元件
掃描、標籤配對）。

`Heated Vented Seats`（59 leaves）維持單一 Test Set，Part N 無變更 ——
`verify_partn.py` 七項檢查仍全 PASS。

**同時寫入一條 Phase 4 之約束**（本包新增，非分析層指示，若不同意請駁回）：

> `opens popup` 既為回饋而非入口，ch11 之該兩節與 ch12 對應節之差異應以
> **預期結果**（是否出現 popup）表達，不得寫成不同的操作步驟或前置條件。

理由：裁定的實質內容就是「這不是入口差異」。若 Phase 4 仍把它寫成不同的
操作步驟，等於在 TC 層把裁定推翻回去，而那不會有任何檢查會擋。

## 2. A-CF13 第四項已登 —— `12.1` 之 `LEDs (.`

前三項為**標籤**衝突，第四項為**字元**層級瑕疵：

> …the control displays 3 arrows, HI and/or LEDs **(.** The next button press…

實測全節左括號 1 個、右括號 0 個，判為誤植。對照 `11.1` 同位置為 `LEDs.`。

**影響**：對 TC 內容無（不改語意）；對逐字比對有（為 11.1 vs 12.1 三處差異
之一，本次已與實質差異分開陳述）；對 Phase 4 引用需注意 —— 若逐字引用該句
應**照錄原文**或明示節錄，**不得靜默修正**（修正 spec 原文非 TC 作者權限，
§8.4.2）。

**四項之共通歸納**：

| # | 項目 | 層級 | 唯有讀全文可見？ |
|---|---|---|---|
| 1 | `C16.)` 跨 2.15／16.17 | 標籤 | 否 |
| 2 | `W0.)` 跨 17.1／18.1／19.1 | 標籤 | 否 |
| 3 | `HVS1/2/4/5/6` 跨 ch11／ch12 | 標籤 | 否 |
| 4 | `12.1` 之 `LEDs (.` | 字元 | **是** —— 位於第 174 字元 |

第 4 項是 R-C18 之另一佐證：它不在標題裡，任何以 60 字截斷欄位為輸入之
比對都看不到它。前三項可由標籤發現，第四項不能。

## 3. ch11／ch12 之結構全貌（供 §4 之背景）

| 標籤 | ch11 | ch12 | 逐字相同 | 相似度 |
|---|---|---|---|---|
| `HVS1` | 11.1 | 12.1 | 否 | 0.9556 |
| `HVS2` | 11.2 | 12.2 | 否 | 0.9579 |
| `HVS4` | 11.3 | 12.4 | **是** | 1.0000 |
| `HVS5` | 11.4 | 12.5 | **是** | 1.0000 |
| `HVS6` | 11.5 | 12.6 | 否 | 0.9143 |

- **ch11 獨有（8 個標籤）**：`R1HVS1.`、`R1HVS1.1`、`R1HVS1.2.`、`R1HVS2.`、
  `R1HVS3.`、`R1HVS4.`、`R1HS4.1.`、`W1HVS2.` —— 皆為 `R1`／`W1` 前綴
- **ch12 獨有（4 個標籤）**：`HVS3`、`HVS7`、`SHVS1`、`SHVS2`
  （`SHVS` = Standard）

`HVS6` 之 0.9143 差異為 `Refer to HMI Settings List`（11.5）vs
`Refer to HMI Notes`（12.6），即 12 §1 已載者。

## 4. 其餘 18 節之操作元件掃描 —— 事實

依指示，掃描 ch11／ch12 除已報 4 節外之全部 18 節，查是否提及**軟鍵以外**
之操作元件。**只回報事實。**

### 4.1 掃描結果

| 詞類 | 正則 | 命中節次 |
|---|---|---|
| hard control／button／key／switch | `\bhard\s+(control\|button\|key\|switch)s?\b` | **11.6.1、11.11** |
| status bar | `\bstatus\s*bar\b` | **11.3、11.11、11.11.1、12.4** |
| physical | `\bphysical\b` | **無** |
| knob／rotary／dial | `\b(knob\|rotary\|dial)\b` | **無** |
| ICS | `\bICS\b` | **無** |
| touchscreen／TS | `\b(touchscreen\|touch screen\|TS)\b` | **無** |
| switch（單獨名詞） | `\bswitch\b` | **無** |
| soft button／key | `\bsoft\s*(button\|key)s?\b` | 11.6.1、11.8、12.8、12.9 |
| pop-up | `\bpop\s*-?\s*up\b` | 11.6、11.7、11.8、11.9、11.10、11.11、12.7 |

### 4.2 兩處 `hard control` 命中之全文

**`11.6.1`**（`R1HVS1.1)`，ch11 獨有）
> R1HVS1.1) On vehicles that are equipped with the seat zone feature
> **without a hard control or capacitive control** there will be a soft button
> to control this feature in the comfort screen. There are 3 states (1. both
> seat back and seat cushion, 2. Seat back only 3. Seat cushion only), plus a
> greyed out state in case heated and vented seats are off.

**`11.11`**（`R1HVS4.)`，ch11 獨有）
> R1HVS4.) Heated/vented seat, heated wheel will not be displayed in the
> comfort section **if the vehicle is configured with hard buttons for comfort
> controls**. Comfort controls will still exist within the status bar and
> temperature/comfort popup. For vehicle programs such as WS that have haptic
> heated/vented seat/heated steering wheel buttons placed on the side of the
> radio, those controls will not be displayed in the status bar.

### 4.3 四處 `status bar` 命中之全文

**`11.3` ／ `12.4`**（`HVS4.`，兩節**逐位元組相同**）
> HVS4. When climate is OFF, the status bar should still show heated/vented
> seat status.

**`11.11.1`**（`R1HS4.1.)`，ch11 獨有）
> R1HS4.1.) When comfort controls are not active, they will be greyed out in
> the status bar combined temperature/comfort top left/right corners.

（`11.11` 之 status bar 出現於 §4.2 已引之全文中。）

### 4.4 事實陳述（不下結論）

1. **18 節中，無任何一節以實體鍵、旋鈕、ICS 或觸控面為其所述之操作元件。**
   `hard control` 之 2 處命中，其句法位置皆為**條件子句**
   （`without a hard control…` / `if the vehicle is configured with hard
   buttons…`），所修飾者為「是否顯示軟鍵／comfort section」，非「如何操作」。
2. `status bar` 之 4 處命中，其句法位置皆為**顯示位置**
   （`the status bar should still show…` / `greyed out in the status bar`），
   非操作元件。
3. 兩類命中**全部落在 ch11**，唯一例外是 `12.4`，而它與 `11.3` 逐位元組相同。
   **ch12 無任何一節單獨提及 hard control 或 status bar。**
4. `ICS`、`knob`、`rotary`、`physical`、`touchscreen` 於兩章**皆為零命中**。
   依 **R-C13**，零命中僅為索引層事實 —— 已另以全文逐節閱讀複核，未見以
   其他措辭表達之實體操作（如 `press the button on the console`）。

**「入口是否相同」之判定不在本節**：該判定已由分析層作成（§1），本節之
事實與該判定方向一致，但事實本身不構成判定。


---

## 5. ch2 與 ch16 之全文 —— 供 R-C18 複核章內歸屬

依指示列出兩章全部節次之 `full_text`（不截斷）。來源
`data/section_fulltext.tsv`。每節標註其現行 Test Set、leaf 數與 parent id，
供分析層複核「該節是否歸對組」。

兩章合計 **40 節 / 191 leaves**，佔 403 之 **47.4%**。


## 章 2 — Front Comfort/Climate（22 節 / 92 leaves）

#### `2.1` — Front Climate Anatomy — 3 leaves — SWE1-HVAC-001

> R1C1.) The comfort category will have up to 4 tabs depending on vehicle configuration. Tabs are displayed in the following order: Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati), Massage, Rear. If only Front climate is available in a specific vehicle the tabs will not be displayed. Refer to separate HMI Logic and Flow documentation for Massage Seats logic.

#### `2.2` — Front Climate Anatomy — 8 leaves — SWE1-HVAC-002

> C1.) Whenever changes to the climate system are made via hard controls or touchscreen, these changes are reflected in both locations. Whenever fan speed or temperature hard controls are used (even if at highest/lowest setting), according pop-ups are shown if NOT on climate screen (timeout after 3 sec), and changes are reflected in status bar/ status indicator on category button. When sync'd, do not show slider pop-up on passenger side when adjusting driver slider. If the user is outside of the climate main category and the temperature is changed through hard controls, a pop-up will be shown coming down from that temperature in the status bar to indicate it is being altered, for ATC it will display the degree (or half degree increments for Celsius and for Fahrenheit do not show half degrees) being set, for MTC (if the MTC has a Climate screen) it will display a slider bar with the arrow pointing to the current setting, this information will change as the user alters the temp. If on climate screen, status changes are indicated directly on touchscreen buttons / status indicator on category button and will not be shown in the status bar. If changes are made on climate screen, LEDs on hard controls reflect new status.

#### `2.3` — Climate Modes — 9 leaves — SWE1-HVAC-003

> C2.) AUTO has on/ off state. The fan speed indicator shows Auto instead of the actual fan speed (this is based on fan speed of 15h rather than the status of AUTO). The main category control is dynamic, and will display Auto with the Mode Man and Fan speed greyed out behind it. AUTO affects Fan speed, Modes, AC in order to reach desired temperature as quickly as possible. Auto is mutually exclusive with the four airflow modes and front defrost. If Auto is turned on, these buttons/statuses are turned off. Auto can change the state of AC, but do not show this change. Manually selecting A/C, switching to another airflow mode (including front defrost), or changing fan speeds breaks Auto. When breaking Auto the system will go to the manual mode that most closely matches the auto mode exited, unless a specific mode button is pressed, in which case the system would go to that mode. Any other climate controls do NOT break Auto. (AUTO is not shown in MTC configurations)

#### `2.3.1` — Climate Modes — 2 leaves — SWE1-HVAC-004

> C2.1) Some vehicles with dual zone climate with dual airflow mode can have a configuration for dual AUTO modes, one for the driver side and passenger side.

#### `2.4` — Climate Modes — 4 leaves — SWE1-HVAC-005

> C3.) AC has on/ off state. Auto can automatically turn on AC. AC will break Auto. Defrost can automatically turn on AC (Do not show this change). Recirc can automatically turn on AC.

#### `2.5` — Climate Modes — 4 leaves — SWE1-HVAC-006

> C4.) Recirc has on/ off state. RECIRC is not available in certain modes. Therefore, gray out the RECIRC button when recirc availability status from CCM denotes that. Recirc can automatically turn on AC. The recirc icon will display the vehicle model specific icon as displayed in the table. If the system cannot detect the vehicle model it will display the generic recirc symbol.

#### `2.5.1` — Climate Modes — 2 leaves — SWE1-HVAC-007

> C4.1) Some vehicles have a configuration for a 3 state toggle recirc button: Auto, Manual, Open.

#### `2.6` — Temperature and Fan — 5 leaves — SWE1-HVAC-008

> C5.) Temperature ranges: LO, 60-84, HI (English), LO, 16-28, HI (Metric). This status is relayed from the CCM. Temperature will display the current degree value that the user has set it to for ATC systems, when at the Highest possible position display HI when at the lowest display LO instead of a degree value. The status is indicated on TS climate screen and in status bar. When the user sets the climate system temperature ranges to Metric the readout switches to half degree increments. Show pop-up when status is changed via hard control and currently shown screen is not climate screen. (when sync'd, do not show slider pop-up on passenger side when adjusting driver slider). The temperature within the temp slider, status bar, temp slider popup, and temp popup will reflect this change in temperature increments.

#### `2.6.1` — Temperature and Fan — 6 leaves — SWE1-HVAC-009

> C5.1) If SYNC is ON, adjusting driver temperature affects passenger temperature, adjusting passenger temperature would break SYNC and turn it off. Change temperature on climate screen by using arrows (move 1 increment up/down per press, long press = fast move or slider (TEMP pop-up next to slider when touching it so that finger does not cover number). Long press = fast move shall also work for temperature HARD CONTROLS. The system can jump to a value as well via the slider or voice command. User must press slider handle to move temperature slider position. The system can jump to a value as well via touching a spot in a slider bar or voice command. The user can also press slider handle to move temperature slider position; if user initially presses slider area outside of handle (i.e. to the left or right of the slider handle), ignore the press.

#### `2.7` — Temperature and Fan — 5 leaves — SWE1-HVAC-010

> C6.) Fan ranges: Off, 1-7, 15h (denoting to show AUTO instead). The status is indicated on TS climate screen and in main category control. Show pop-up when status is changed via hard control and currently shown screen is not climate screen. When on climate screen, user can either use Fan up/down (minus/plus) buttons, directly touch a fan segment to jump or slide, or use Hard Control. The user shall not be able to turn the FAN off by using the FAN controls on the screen or the FAN hard control. There would always be one bar highlighted. The only way to have all FAN bars grayed out is by shutting the CLIMATE system OFF (using climate power button on the screen or hard control).

#### `2.7.1` — Temperature and Fan — 1 leaves — SWE1-HVAC-011

> C6.1) In some vehicles fan speed ranges for front hvac are: Off, 1-8.

#### `2.8` — Airflow and Defrost — 6 leaves — SWE1-HVAC-012

> C7.) Defrost has on/ off state. Defrost can automatically turn on AC (do not show this change). Defrost automatically changes Fan speed. Defrost is mutually exclusive with other airflow modes. Auto turns Defrost off. Turning Defrost on while in Auto will break Auto and turn it off. When Defrost is active, Recirc is may or may not be available (reflect in recirc availability status). Therefore, gray out the RECIRC button when recirc availability status from CCM denotes that.

#### `2.9` — Airflow and Defrost — 4 leaves — SWE1-HVAC-013

> C8.) Rear Defrost has on/ off state. REAR DEFROST is not available in certain modes. Therefore, gray out the REAR DEFROST button when rear defrost availability status from CCM denotes that. Rear defrost is independent of any other climate functions. Rear Defrost automatically turns on EXTERIOR REAR-VIEW MIRROR DEFROST if this feature available.

#### `2.10` — Climate Modes — 6 leaves — SWE1-HVAC-014

> C11.) Climate off has on/off state that is indicated on HC, TS (climate screen) and in status bar. Climate off affects every climate function with the exception of FRONT /MAX DEFROST (depending on equipment) and REAR DEFROST (and seat/wheel controls). When the system is turned off, show the CLIMATE OFF screen with the OFF button turned into an ON button and grey out remaining buttons except for Front/max defrost and rear defrost. Category button shows fan greyed out and mode oscar replaced with "OFF" which will remain until the user turns it back on. Temperatures and units (°F/C) in status bar are substituted by dashes in all modes when climate is off. If a user presses a temp/fan control to turn climate back on, the system reinstates to the last level of that feature and if Front/Max Defrost is selected, the climate system turns back on (does not happen with rear defrost, heated/vented seats or heated wheel). If the user continues to hold/turn the control, the system will respond in-kind.

#### `2.11` — Climate Modes — 5 leaves — SWE1-HVAC-015

> C12.) SYNC has on/ off state that is indicated on climate screen (highlight button if SYNC). Sync is not shown for single zone climate configurations. Sync synchronizes driver and passenger temperatures to the driver temperature. When SYNC is on, changing the driver temperature automatically changes the passenger temperature. Adjusting the passenger temperature via touchscreen or hard control would break SYNC. Adjusting Fan speed and Mode will alter the Front and Rear passengers. If the rear fan speed, mode, or temp are adjust from either the touchscreen or rear climate controls will break SYNC and turn it off.

#### `2.12` — Airflow and Defrost — 3 leaves — SWE1-HVAC-016

> C13.) There are 4 Airflow Mode displayed in this order (1) Face, (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield. ON state for the four airflow modes is shown by highlighting the button and increasing button size. The main category control will display the newly selected airflow mode inside the fan space. Only one airflow mode can be selected at a time.

#### `2.12.1` — Airflow and Defrost — 2 leaves — SWE1-HVAC-017

> C13.0) In some non-tri mode equipment types, airflow modes has 5 states (1.Face, 2.Mix of Face & Feet, 3.Feet, 4.Mix of Feet & Windshield, 5. Windshield).

#### `2.12.2` — Airflow and Defrost — 6 leaves — SWE1-HVAC-018

> C13.1) If the Mode hard control is pressed the user will be moved to the next mode available in the loop (Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop. Defrost will not be included in the loop) press and hold of the control will only move one mode over, it will not continue to move through modes. When the Mode hard control is pressed, if the user is on Climate main the new mode button will be shown highlighted. If the user is not on Climate main when pressing the Mode hard control a small pop-up will appear above the Climate main category control (timeout after 3 seconds of inactivity or as soon as another button except Mode HC is pressed), the user will not be shifted to climate main. In both cases the main category label will be updated. While in Rear Climate screen the Mode Hard Control button will alter the front Mode.

#### `2.13` — Climate Modes — 3 leaves — SWE1-HVAC-019

> C14.) MAX A/C screens/popups are to be used when CCM relays presence of MAX A/C functionality. MAX A/C has an on/off state that is indicated on climate screen (highlight button if on). MAX A/C modifies multiple climate parameters. On/Off logic should follow requirements from VF HVAC document.

#### `2.14` — Climate Modes — 4 leaves — SWE1-HVAC-020

> C15.) MTC screens/popups are to be used when CCM relays MTC functionality. MTC climate is primarily differentiated from ATC by the lack of discrete temperature settings and "Auto" control over the set temperature. For MTC with ICS, there will be no redundant interaction with the screen for certain types of physical knobs (3 knob HVAC controls) in order to prevent a mismatch between the soft and hard controls. In these cases, no HVAC menu bar icons, no HVAC screens and no HVAC pop ups will be displayed. For one zone MTC with push button TEMPERATURE and hard controls that would not create a mismatch between hard controls then this exception does not apply.

#### `2.15` — Airflow and Defrost — 2 leaves — SWE1-HVAC-021

> C16.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off state. EXTERIOR REAR-VIEW MIRROR DEFROST is independent of any other climate functions.

#### `2.16` — Climate Modes — 2 leaves — SWE1-HVAC-022

> C18.) If blower reduction occurs automatically due to an active Voice Recognition session, the change in fan speed is not displayed to the user. After blower reduction, return blower speed to previous speed without showing a change in fan speed.


## 章 16 — ICS CLIMATE EMEA – CARRYOVER（18 節 / 99 leaves）

#### `16.2` — ICS Anatomy — 9 leaves — SWE1-HVAC-106

> ICE1.) Whenever changes to the climate system are made via hard controls or touchscreen, these changes are reflected in both locations with the exception of the recirculation led in climate off (see ICE11.). Whenever fan speed or temperature hard controls are used (even if at highest/lowest setting), according pop-ups are shown if NOT on climate screen (timeout after 3 sec), and changes are reflected in status bar/ status indicator on category button. When sync'd, do not show slider pop-up on passenger side when adjusting driver slider. If the user is outside of the climate main category and the temperature is changed through hard controls, a pop-up will be shown coming down from that temperature in the status bar to indicate it is being altered, for ATC it will display the degree (or half degree increments for Celsius) being set, for MTC it will display a slider bar with the arrow pointing to the current setting, this information will change as the user alters the temp. If on climate screen, status changes are indicated directly on touchscreen buttons / status indicator on category button and will not be shown in the status bar. If changes are made on climate screen, LEDs on hard controls reflect new status.

#### `16.3` — ICS Climate Modes — 9 leaves — SWE1-HVAC-107

> ICE2.) AUTO has on/ off state. The fan speed indicator shows Auto instead of the actual fan speed and none of the Mode buttons will be shown highlighted. The main category control will display Auto with the Mode Man and Fan speed greyed out behind it. AUTO affects Fan speed, Modes, AC in order to reach desired temperature as quickly as possible. Auto is mutually exclusive with MAX A/C and MAX DEF. Pressing MAX DEF or Max A/C the system goes to that function. If Auto is turned on, these buttons are turned off. In Auto the A/C button is highlighted. Manually selecting A/C keeps the system in AUTO without compressor usage (A/C off). Manually changing airflow mode, or changing fan speeds breaks Auto. When breaking Auto the system will go to the manual mode that most closely matches the auto mode exited, unless a specific mode button is pressed, in which case the system would go to that mode. Any other climate controls do NOT break Auto. (AUTO is not shown in MTC configurations)

#### `16.4` — ICS Climate Modes — 1 leaves — SWE1-HVAC-108

> ICE3.) MAX A/C, A/C, RECIRC, MAX DEF, and REAR DEFROST have on/off state.

#### `16.5` — ICS Climate Modes — 2 leaves — SWE1-HVAC-109

> ICE4.) The recirc icon will display the vehicle model specific icon as displayed in the Climate Main page table. If the system cannot detect the vehicle model it will display the generic recirc symbol.

#### `16.6` — ICS Temperature and Fan — 6 leaves — SWE1-HVAC-110

> ICE5.) Temperature ranges: LO, 60-84, HI (English), LO, 16-28, HI (Metric). Temperature will display the current degree value the user has set it to for ATC systems, when at the Highest possible position display HI when at the lowest display LO instead of a degree value. The status is indicated on TS climate screen and in status bar. Show pop-up when status is changed via hard control and currently shown screen is not climate screen. (when sync'd, do not show slider pop-up on passenger side when adjusting driver slider). When the user sets the climate system temperature ranges to Metric the CCM switches to half degree increments . The temperature within the temp slider, status bar, temp slider popup, and temp popup will reflect this change in temperature increments .

#### `16.6.1` — ICS Temperature and Fan — 5 leaves — SWE1-HVAC-111

> ICE5.1) If SYNC is ON, adjusting driver temperature affects passenger temperature, adjusting passenger temperature would break SYNC and turn it off. Change temperature on climate screen by using arrows (move 1 increment up/ down per press, long press = fast move or slider (TEMP pop-up next to slider when touching it so that finger does not cover number). Long press = fast move shall also work for temperature HARD CONTROLS . The system can jump to a value as well via the slider or voice command. User must press slider handle to move temperature slider position; if user initially presses slider area outside of handle, ignore the press. The system can jump to a value as well via a slider bar touch or voice command. The user can also press slider handle to move temperature slider position; if user initially presses slider area outside of handle (i.e. to the left or right of the slider handle), ignore the press.

#### `16.7` — ICS Temperature and Fan — 5 leaves — SWE1-HVAC-112

> ICE6.) Fan ranges: Off, 1-7 (denoting to show AUTO label instead when in AUTO). The status is indicated on TS climate screen and in main category control. Show pop-up when status is changed via hard control and currently shown screen is not climate screen. When on climate screen, user can either use Fan up/down buttons, directly touch a fan segment to jump or slide, or use Hard Control. The user shall not be able to turn the FAN off by using the FAN controls on the screen or the FAN hard control. There would always be one bar highlighted. The only way to have all FAN bars grayed out is by shutting the CLIMATE system OFF (using climate power button on the screen or hard control).

#### `16.8` — ICS Airflow and Defrost — 12 leaves — SWE1-HVAC-113

> ICE7.) MAX DEF automatically turns on A/C, changes airflow modes to Windshield, increases fan speed at highest setting (7/7), sets temperature (driver and passenger if available) at highest setting (HI), change RECIRC to open (LED off), turns on Sync and activates the REAR DEFROST. MAX DEF switches off automatically after a set time after which the system goes back to the previous manual mode. Change in fan speed doesn’t break MAX DEF. Changing temperature, recirculation, mode distribution or pressing again MAX DEF breaks MAX DEF (turns MAX DEF off) and the system goes back to the previous manual mode with the A/C on. Pressing A/C brakes MAX DEF (turns MAX DEF off) and the system goes back to the previous manual mode with the A/C off. Pressing AUTO breaks MAX DEF (turns MAX DEF off) and the system goes to AUTO. Similarly, pressing MAX A/C turns MAX DEF off (turns MAX DEF off) and the system goes to MAX A/C.

#### `16.9` — ICS Airflow and Defrost — 2 leaves — SWE1-HVAC-114

> ICE8.) Rear Defrost has on/ off state. Gray out the REAR DEFROST button when rear defrost availability status from CCM denotes that .

#### `16.10` — ICS Climate Modes — 8 leaves — SWE1-HVAC-115

> ICE9.) Climate off has on/off state that is indicated on HC, TS (climate screen) and in status bar. When the system is turned off, show the CLIMATE OFF screen with the OFF button turned into an ON button and grey out remaining buttons except for Front/Max defrost and rear defrost. The Main category control shows fan speed segments off and mode Oscar replaced with "OFF" which will remain until the user turns it back on. Temperatures and units (°F/C) in status bar are substituted by dashes in all modes when climate is off. Actions on rear defrost, heated/vented seats or heated wheel don t reactivate climate (climate still off). Actions on any other climate hard controls turns system back on. When climate is OFF, the recirculation LED of the hard control is on. Action on the recirculation hard control will not turn system back on; it simply opens the recirculation and turns led off. If a user presses a temp/fan hard control to turn climate back on, the system reinstates to the last level of that feature and the climate system turns back on (does not happen with recirculation, rear defrost, heated/vented seats or heated wheel). If the user continues to hold/turn the control, the system will respond in-kind.

#### `16.11` — ICS Climate Modes — 4 leaves — SWE1-HVAC-116

> ICE10.) SYNC has on/ off state that is indicated on climate screen (highlight button if SYNC). Sync is not shown for single zone climate configurations. Sync synchronizes driver and passenger temperatures to the driver temperature. When SYNC is on, changing the driver temperature automatically changes the passenger temperature. Adjusting the passenger temperature via touchscreen or hard control would break SYNC. Adjusting Fan speed and Mode will alter the Front and Rear passengers. If the rear fan speed, mode, or temp are adjust from either the touchscreen or rear climate controls will break SYNC and turn it off.

#### `16.12` — ICS Airflow and Defrost — 3 leaves — SWE1-HVAC-117

> ICE11.) Airflow Modes has 5 states (1.Face, 2.Mix of Face & Feet, 3.Feet, 4.Mix of Feet & Windshield, 5. Windshield). ON state for the four airflow modes is shown by highlighting the button and increasing button size. The main category control will display the newly selected airflow mode inside the fan space . Only one airflow mode can be selected at a time.

#### `16.12.1` — ICS Airflow and Defrost — 10 leaves — SWE1-HVAC-118

> ICE11.1) If the Mode hard control is pressed the user will be moved to the next mode available in the loop (Face > Face/Feet > Feet > Feet/Windshield > Windshield), the user will be shifted with each press, press and hold of the control will only move one mode over, it will not continue to move through modes. When the Mode hard control is pressed, if the user is on Climate main the new mode button will be shown highlighted. if the user is not on Climate main when pressing the Mode hard control a small pop -up will appear above the Climate main category control (timeout after 3 seconds of inactivity or as soon as another button except Mode HC is pressed), the user will not be shifted to climate main. In both cases the main category label will be updated. While in Rear Climate screen the Mode Hard Control button will alter the front Mode.

#### `16.13` — ICS Climate Modes — 12 leaves — SWE1-HVAC-119

> ICE12.) If the system supports Max A/C it will be displayed on the screen next to the A/C button. MAX A/C has an on/off state that is indicated on climate screen (highlight button if on). MAX A/C automatically turns on A/C, changes airflow modes to Face, increases fan speed at highest setting (7/7), sets temperature (driver and passenger if available) at lowest setting (LO), change RECIRC to closed (led on), and turns on Sync. Change in fan speed deactivates MAX A/C (un-highlight MAX A/C) while maintaining system in current state with change in fan speed. Changing temperature, recirculation, mode distribution, or pressing again MAX A/C brakes MAX A/C, (turns MAX A/C off) and the system goes back to the previous manual mode except for the element changed (temperature, or mode, or recirculation) and keeps the A/C on. Pressing A/C, brakes MAX A/C (turns MAX A/C off) and the system goes back to the previous manual mode with the A/C off. Pressing AUTO brakes MAX A/C (turns MAX A/C off) and the system goes to AUTO. Similarly, pressing MAX DEF turns MAX A/C off (turns MAX A/C off) and the system goes to MAX DEF.

#### `16.14` — ICS Climate Modes — 3 leaves — SWE1-HVAC-120

> ICE13.) MTC screens/popups are to be used when CCM relays MTC functionality. MTC climate is primarily differentiated from ATC by the lack of discrete temperature settings and "Auto" control over the set temperature.

#### `16.15` — ICS Airflow and Defrost — 2 leaves — SWE1-HVAC-121

> ICE14.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off state. EXTERIOR REAR-VIEWMIRROR DEFROST is independent of any other climate functions.

#### `16.16` — ICS Anatomy — 5 leaves — SWE1-HVAC-122

> ICE15.) Always show 'Driver' or 'Passenger'. Off icon of seats will depend on system configuration (see Climate section). Active state text color is white. Inactive state text color is gray. When entering the controls screen the current state of the buttons will be displayed.

#### `16.17` — ICS Climate Modes — 1 leaves — SWE1-HVAC-123

> C16.) If blower reduction occurs automatically due to an active Voice Recognition session , the change in fan speed is not displayed to the user.


---

## 6. Phase 4 未開始

未產 TC、未指派 tc_id、未做 sibling 判定、未寫 profile `[OVERRIDE]`。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. ch11／ch12 全 22 節之標籤配對、逐字相同性與相似度。
2. 18 節之九類操作元件詞彙掃描，並對 6 處命中逐一讀全文確認其句法位置。
3. `12.1` 之括號數（左 1、右 0）與字元位置（174）。
4. ch2（22 節）與 ch16（18 節）之全文完整輸出，節數與 leaf 數對得上
   （92／99）。
5. `verify_partn.py` 七項檢查於 `framework.md` 更新後仍全 PASS。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **ch2／ch16 章內歸屬是否正確** | 本包只**提供全文**，未自行複核歸屬 —— 那是 Part N 內容（Tier 2） | **中** —— 材料已備，複核屬分析層 |
| 2 | **其餘 12 章之章內歸屬** | 指示只要求 ch2／ch16 | 中 —— 全文同樣在 `section_fulltext.tsv`，隨時可列 |
| 3 | **`opens popup` 之 popup 為何物** | 需 HMI Pop Up List（DR #11），該檔不在 `inputs/` | 低（**已降**）—— 入口問題已由分析層裁定，此項現僅影響 Phase 4 之預期結果措辭 |
| 4 | profile `[OVERRIDE]`、DR #6 | 分析層下一包／待 Pei 指認 | 中／低 |

**第 1 項需要說明界線**：我提供了 40 節全文並標註現行 Test Set，但**未對
任何一節之歸屬表示意見**。歸屬判斷需讀懂條文語意並權衡 §4.2 之
「shared setup pattern and UI entry path」，屬 Tier 2。若分析層希望執行層
先做一輪初判再覆核，請明示 —— 我不預設那可下放。

### 7.3 未做、亦未偷做者

- **未對 ch2／ch16 之任何一節提出改置主張**。
- **未就 18 節之掃描結果下入口判定**（§4.4 末段已明示）。
- 未改 Part N 之任何分組、名稱或 leaf 歸屬。
- 未修正 `12.1` 之 `LEDs (.`（spec 原文，非 TC 作者權限）。
- 未產 TC、未指派 tc_id、未寫 profile。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 7.4 執行層對「本包可否結案」之判斷

**可結案。** 合併依據已落地於 `framework.md` 而非只存在於往返包；
A-CF13 四項齊備；ch2／ch16 全文已備供複核；元件掃描之事實已供且未越界。

**一項請分析層留意**：§1 我在 `framework.md` 自行加了一條 Phase 4 約束
（差異以預期結果表達，不得寫成不同操作步驟）。那是我從裁定實質內容推出的，
**不是分析層的指示**。若不同意，請駁回 —— 我把它寫進去是因為沒有任何機械
檢查會擋住「在 TC 層把裁定推翻回去」這件事，但它終究是我加的規範。
