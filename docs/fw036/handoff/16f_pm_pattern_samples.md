# 下放包 16 附件 F：三型補範例（同構群無既有範例者）

供執行層套用之額外樣式範例。規則同附件 A–E。

---
## 型 (2,2,·,·,Input有值) — 46 列最大群。代表 row 150
**現況**
```
pre  : 1. A LIN and CAN simulation tool is connected ǁ 2. SDARS_Presence reads "Absent"
input: Audio_Brand: "No Audio Brand"
proc : 1. Send the value listed in Input Test Data
       2. Read the shown logos to check the resulting presentation
er   : 1. The brand logo screen is presented
       2. The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone
```
**改寫**
```
PRE:
1. SDARS_Presence is Absent
2. Audio_Brand is No Audio Brand
3. LIN and CAN tool is available on HU

PROC:
1. Power up the TLM and let the brand logo screen be presented
2. Read the TLM screen and check that the brand logo screen is shown
3. Read the shown logos and check that only the vehicle brand logo corresponding to Brand_Configuration_2 is shown

ER:
1. The brand logo screen is presented
2. The brand logo screen is shown on the TLM screen
3. Only the vehicle brand logo corresponding to Brand_Configuration_2 is shown
```
**要點**：Input 之 `Audio_Brand: "No Audio Brand"` 為**配置值**（非驅動值）
→ 移入 PRE（R-11(c)：起始狀態入 Pre-Condition）。
`Send the value listed in Input Test Data` 因而消滅，改為使該配置生效之
實際動作。此型 46 列多屬配置枚舉，一律照此處理。

---
## 型 (3,3,·,·,Input有值) — 7 列。代表 row 187
**現況**
```
input: PN14_LS_Actv in STATUS_LIN on BH-CAN = [1h] ǁ PN14_LS_Lvl7 … = [1h] ǁ Starting volume level: 25
proc : 1. Set the TLM volume level to the starting value listed in Input Test Data
       2. Send the two Load Shed signals listed in Input Test Data
       3. Read AUD_LVL, the audio output and the ICS power state to check the Load Shed action
```
**改寫**
```
PRE:
1. The bench is an Atlantis High configuration
2. Ecall mode is inactive
3. ACN mode is inactive
4. Chimes mode are inactive
5. LIN and CAN tool is available on HU

PROC:
1. Set the TLM volume level to 25
2. Read the TLM volume indicator and check that it shows 25
3. Send the signal $STATUS_LIN.PN14_LS_Actv$ = 1 (Active)
4. Send the signal $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active)
5. Read AUD_LVL and check that the maximum volume is reduced to 20
6. Read the audio output and check that the TLM is muted
7. Read the ICS power state and check that it is off

ER:
1. The TLM volume level is set to 25
2. The TLM volume indicator shows 25
3. The signal $STATUS_LIN.PN14_LS_Actv$ = 1 (Active) is registered without a bus error
4. The signal $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active) is registered without a bus error
5. AUD_LVL carries the reduced maximum volume of 20
6. The TLM audio output is muted
7. The ICS module is off
```
**要點**：(1) Input 之三項全數內聯：數值 `25`／`20` 為來源明載，逐字取用；
(2) `[1h]` 十六進位改 DBC VAL_ 式 `1 (Active)`；
(3) 三件組 `in … on BH-CAN` 為 R-1 v2 殘留，改 v3 `$MESSAGE.Signal$`；
(4) PRE 之 `Ecall, ACN and chimes modes are inactive` 三條件拆行（R-9）。

---
## 型 (1,2,·,·,NA) — 6 列。代表 row 165
**現況**
```
pre : 1. The TLM is in Full-Operation status
proc: 1. Open the timeout setting entry in the TLM menu
      2. Change the offered timeout parameter and read it back to check that the change is accepted
```
**改寫**
```
PRE:
1. The TLM is in Full-Operation state
2. LIN and CAN tool is available on HU

PROC:
1. Open the timeout setting entry in the TLM menu
2. Read the timeout setting entry and check that its controls are enabled
3. Change the offered timeout parameter to another available value
4. Read the timeout parameter and check that it is the newly selected value

ER:
1. The timeout setting entry is opened
2. The timeout setting entry controls are enabled
3. The timeout parameter is changed to another available value
4. The timeout parameter is the newly selected value
```
**要點**：PRE 僅 1 行者一律補工具行至末（R-12(a)）；
`status` → `state` 統一；一步二動作（change + read back）拆為兩步（R-11(a)）。

---
## 執行層通則（三型共通）

1. `A LIN and CAN simulation tool is connected` → `LIN and CAN tool is
   available on HU`，且**移至 PRE 末項**。
2. PRE 首項改為車輛／電源狀態；多條件並列一律拆行編號（R-9）。
3. Input 欄內容按性質移動後，該欄一律 `NA`；
   **配置值 → PRE；驅動值 → PROC 逐值成步；判定值 → ER**。
4. `listed in Input Test Data` 之指涉一律消滅。
5. 訊號一律 `$MESSAGE.Signal$ = <raw> (<VAL_ label>)`；
   三件組 `in … on …` 與 `Send CAN:` 皆為舊式，改 v3。
6. 十六進位 `[1h]`／`[0h]` 改 DBC VAL_ 十進位加標籤。
7. **遇來源未明載之值，標 `PENDING: DR-{n}` 並列入回報，
   不得依情境推定**（Pei 裁定路線 c）。
