# 雙向規格比對 —— PDF ↔ SYS1 匯出（R-PMH51）

- 產出：`scripts/bidirectional_spec_diff.py`
- PDF：11 頁，正規化後 15,171 字元
- SYS1 `Basic Report`：52 則，正規化後 8,416 字元
- 句長門檻：25 字元（短於此者不作句級比對，另計）

## 方向一 —— SYS1 之每一句是否出現於 PDF（01 包已做，本輪複算）

| outline | 句數 | 命中 | 未命中 |
|---|---:|---:|---:|
| 1.1 | 1 | 1 | 0 |
| 1.2 | 1 | 1 | 0 |
| 1.3 | 1 | 1 | 0 |
| 1.4 | 1 | 1 | 0 |
| 1.5 | 1 | 1 | 0 |
| 2 | 1 | 1 | 0 |
| 2.1 | 1 | 0 | **1** |
| 3 | 1 | 1 | 0 |
| 3.1 | 1 | 0 | **1** |
| 4 | 1 | 1 | 0 |
| 4.1 | 1 | 0 | **1** |
| 5 | 1 | 1 | 0 |
| 5.1 | 1 | 0 | **1** |
| 6.1 | 1 | 0 | **1** |
| 7.1 | 8 | 7 | **1** |
| 7.1.1 | 2 | 2 | 0 |
| 7.2 | 2 | 2 | 0 |
| 7.3 | 1 | 1 | 0 |
| 7.4 | 2 | 2 | 0 |
| 7.5 | 5 | 5 | 0 |
| 7.5.1 | 1 | 1 | 0 |
| 7.6 | 3 | 3 | 0 |
| 7.7 | 2 | 2 | 0 |
| 7.8 | 2 | 2 | 0 |
| 7.9 | 1 | 1 | 0 |
| 8.1 | 3 | 3 | 0 |
| 8.2 | 1 | 1 | 0 |
| 8.2.1 | 1 | 1 | 0 |
| 8.2.2 | 1 | 1 | 0 |
| 8.2.3 | 1 | 1 | 0 |
| 8.3 | 1 | 1 | 0 |
| 9.1 | 10 | 1 | **9** |
| 10 | 1 | 1 | 0 |
| 10.1 | 1 | 1 | 0 |
| 10.2 | 3 | 3 | 0 |
| 10.3 | 2 | 2 | 0 |
| 10.4 | 2 | 2 | 0 |
| 10.5 | 1 | 1 | 0 |
| 10.6 | 3 | 3 | 0 |
| 10.7 | 1 | 1 | 0 |
| 11 | 1 | 1 | 0 |
| 11.1 | 4 | 2 | **2** |
| 12.1 | 1 | 1 | 0 |
| 12.2 | 1 | 1 | 0 |
| 12.3 | 1 | 1 | 0 |
| 12.4 | 1 | 0 | **1** |

**方向一未命中之 outline：['2.1', '3.1', '4.1', '5.1', '6.1', '7.1', '9.1', '11.1', '12.4']**

## 方向二 —— **PDF 之每一句是否出現於 SYS1**（本輪新增，抓漏句）

| PDF 頁 | 句數 | 命中 | **未命中（漏句候選）** |
|---|---:|---:|---:|
| p1 | 4 | 0 | **4** |
| p2 | 5 | 0 | **5** |
| p3 | 4 | 0 | **4** |
| p4 | 5 | 0 | **5** |
| p5 | 4 | 0 | **4** |
| p6 | 4 | 0 | **4** |
| p7 | 2 | 0 | **2** |
| p8 | 38 | 34 | **4** |
| p9 | 15 | 0 | **15** |
| p10 | 19 | 12 | **7** |
| p11 | 3 | 2 | **1** |

**方向二未命中合計：55 句**（分布於 p[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]）

## 方向二之未命中逐句（漏句候選）

### p1

- `R1 ‐ Power Moding HMI Logic and Flow SR24 Post 2A.`
- `DCR22412 January 24, 2023 HMI Lead: Paolo Visconti paolo.visconti@external.stellantis.com HMI: Marcella Guagliumi (Infotainment), Cecilia Ruspa (HMI Manager SE Europe) NOTE: All graphics are place holders.`
- `See PDO release for official graphics.`
- `Use HMI logic and flow for all official text strings and behavior.`

### p2

- `Assumptions • This specification covers the requirements for the R1 Low 7", R1 Low 8.4", R1 Low 10.1", R1 Low 10.25", R1 Low 12.3", R1 High 8.4", R1 High 10.1", R1 High 10.25", R1 High 12", R1 High 12" Portrait and R1 High 14.46" portait (CR19385), and R1 High 12.3" radios.`
- `• Differences between the radios will be specified.`
- `• Unless otherwise specified, the 12" user interface will be a scaled up version of the 10.1".`
- `• Unless otherwise specified, the 12.3" user interface will be a scaled up version of 10.25".`
- `• Reference PDO release for all official graphics and animation examples.`

### p3

- `Headunit Startup - Non-GDPR/NonMaserati Black Screen (open the door) IF Radio OFF + If disclaimer screen is Power ON button skipped go directly to last mode screen Ignition ON before driver If disclaimer screen is skipped see door close CFTS009 for Instant ON System Loading Splash If vehicle supports Vehicle Start Up Animation, starts with driver door closed only one Splash screen ON OR Recall Last and 1.5 sec Last = ON timeout Ignition ON ≤ 3 sec.`
- `OFF OR Recall Last and If vehicle supports more than 1 Splash Last = OFF screen, toggle them one after another with a 1.5 timeout each Black Screen Ign.`
- `OFF If disclaimer screen is Radio > 3 sec.`
- `skipped go directly to Power On last mode screen System Ready Last Mode Screen Ignition ON or 5 secs IF Radio OFF + Power ON button Black Screen (door closed, ignition OFF) 3`

### p4

- `Headunit Startup - GDPR/Non-Maserati Black Screen (open the door) If disclaimer screen is skipped go directly to Geolocation + SOS IF Radio OFF + last mode screen, Popup (refer to TBM Power ON button showing GDPR/SOS Geolocation L&F for popup first more detailed If disclaimer screen is information) Ignition ON if driver door skipped see CFTS009 for removed/not present/open Instant ON User Acceptance System Loading or Timeout Splash If vehicle supports Vehicle Start Up Animation, starts with driver door closed only one Splash ON OR screen Recall Last and 1.5 sec.`
- `Last = ON Ignition ON ≤ 3 sec.`
- `OFF OR Recall Last and If vehicle supports more than 1 Splash Last = OFF screen, toggle them one after another with a 1.5 timeout each Black Screen Ign.`
- `Radio wakes up for Geolocation + SOS Timeout OR Popup (refer to TBM User Geolocation L&F for Acceptance more detailed information) Ignition ON or IF Radio OFF + If disclaimer screen is skipped go Radio Power On Power ON button directly to last mode screen Last Mode Screen System Ready Geolocation + SOS Popup (refer to TBM Black Screen (door closed, Geolocation L&F for User ignition OFF) more detailed Acceptance 5 sec.`
- `or Timeout information) Note: do not show popup again if popup was shown at Radio Off.`

### p5

- `Headunit Startup - Maserati/Non-GDPR Black Screen (open the door) IF Radio OFF + Power ON button Ignition ON if driver door removed/not present/open System Loading Splash If vehicle supports Vehicle Start Up Animation, starts with driver door closed only one Splash ON OR screen Recall Last and 1.5 sec.`
- `Last = ON Ignition ON ≤ 3 sec.`
- `OFF OR Recall Last and If vehicle supports more than 1 Splash Last = OFF screen, toggle them one after another with a 1.5 timeout each Ign.`
- `Black Screen System Ready Last Mode Screen Radio Ignition ON or Power On IF Radio OFF + Power ON button Requires User Black Screen (door closed, Acceptance ignition OFF) 5`

### p6

- `Headunit Startup - GDPR/Maserati Black Screen (open the door) IF Radio OFF + Power ON button Ignition ON if driver door removed/not present/open System Loading Splash If vehicle supports Vehicle Start Up Animation, starts with driver door closed only one Splash ON OR screen Recall Last and 1.5 sec.`
- `Last = ON Ignition ON ≤ 3 sec.`
- `OFF OR Recall Last and If vehicle supports more than 1 Splash Last = OFF screen, toggle them one after another with a 1.5 timeout each Ign.`
- `Black Screen Radio wakes up for Geolocation + SOS Timeout OR Popup (refer to TBM User Geolocation L&F for Acceptance more detailed Ignition ON or information) IF Radio OFF + Power ON button Radio Power On Last Mode Screen System Ready Black Screen (door closed, ignition OFF) User Acceptance 6`

### p7

- `Passenger Screen Startup Black Screen (open the door) Passenger Screen Off Vehicle Start Up Animation, starts with driver door closed Ignition ON ≤ 3 sec.`
- `Power Hard Key Ignition ON if driver door removed/not present/open Screen On 7`

### p8

- `Startup Notes: SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), after the animation (3 sec) a splash screen is presented timeout (1.5 each).`
- `SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle SU9.) Pressing "Screen Off" or "Power Off" hard key will not do anything when pressed during animation.`
- `SU9.1) Pressing Power Off or Screen Off hard keys during the splash screen(s) or disclaimer will reset the timeout and the radio shall display the screen the next time the screen turns on.`
- `(DCR20015) R1Low Only SSND 1) If start-up sounds are supported, it will start upon driver door close and sync with the start-up animation.`

### p9

- `Power Moding Please refer to Power Moding State Matrix for further specifications.`
- `HEADUNIT POWER HEADUNIT POWER OFF ON ICS Hard Controls : ICS Hard Controls: Power Button only is functional Fully functional HVAC Knobs: HVAC Knobs: KEY ON Fully functional.`
- `Fully functional ENGINE ON Climate GUI: Climate GUI: Not Visibile due to power off Fully functional Headunit: Headunit: VR HK to activate SIRI/Voice assistants shall OFF be functional (See CTS009) (DCR19385) Fully functional ICS Hard Controls: ICS Hard Controls: Power Button only is functional Only headunit-related controls functional PM1) In the event that there are popups to show at IGN OFF but the user has KEY ON HVAC Knobs: HVAC Knobs: set Power Accessory Delay to 0 seconds, the head unit should 'stay awake' ENGINE OFF Fully functional.`
- `Fully functional for 60 seconds up to 2.5 minutes to display the popup(s).`
- `If the user does not (ACC or Climate GUI: Climate GUI: RUN) interact with the popup within 60 seconds the timeout defined in pop-up list, Not Visibile due to power off Fully functional (compressor and heater not working) the radio should shut Off the popup should close aofnd if no other popups Headunit: Headunit: VR HK to activate SIRI/Voice assistants shall are to be shown the radio should shut off.`
- `[CR22412] OFF be functional (See CTS009) (DCR19385) Full on, some limited functionality If the user interacts with the FOTA [CR22412] popup the radio shall 'stay ICS Hard Controls: ICS Hard Controls: Power Button only is functional Only headunit-related controls functional awake' until the user has not interacted with the popup for 60 seconds.`
- `HVAC Knobs: HVAC Knobs: Maximum time the radio can 'stay awake' because of these popups is 10 KEY OFF OFF OFF minutes.`
- `(No ACC Climate GUI: Climate GUI: position) OFF Forced OFF The priority of the popups which occur at IGN OFF are as follows: Headunit: Headunit: 1.`
- `FOTA update available - OFF Full on, some limited functionality If user accepts FOTA popup, start update and dismiss FOTA via Wi-Fi / Charge Now (if applicable) ICS Hard Controls: If user schedules an update time or dismisses update, display FOTA via Wi-Fi / Power Button is functional until power ICS Hard Controls: Charge Now (if applicable).`
- `KEY OFF accessory delay expires Only headunit-related controls functional (ACC HVAC Knobs: HVAC Knobs: 2.`
- `FOTA via Wi-Fi configuration - OFF OFF position If user chooses to configure Wi-Fi, display Charge Now (if applicable) when Climate GUI: Climate GUI: available) Wi-Fi configuration is complete.`
- `OFF Forced OFF Headunit: If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if Headunit: Full on, some limited functionality applicable).`
- `OFF OFF after power accessory delay expires 3.`
- `Charge Now - XEV key off-Pop-ups Charge Now/Summary; Preconditioning.`
- `Shut the radio down if user dismisses Charge Now XEV key off Pop-ups.`

### p10

- `Power Moding Additional Power Moding Behavior Notes: POWER BUTTON: PITA4: Screen Off and HU Power button selections shall be ignored while backup cam is being shown.`
- `KEY OFF, HEADUNIT POWER ON: PITA8: During Key OFF (with no ACC position available), HU power ON, all headunit functionality is expected to have the same functionality as key on, except for controls that communicate with modules external to the headunit which are not functional during Key OFF.`
- `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS: VRLP1: VR hard key to activate SIRI/non-native Voice Assistants (eg.`
- `Radio status after interaction with SIRI depends on outcome of the interaction: Screen Off and Audio OFF (i.e.`
- `radio back to off), Screen ON and Audio OFF, Screen Off, and Audio ON, Screen ON and Audio ON.`
- `(DCR19385) POWER MODING STATE MATRIX: Power Moding behavior shall not be developed without following the Power Moding State Matrix, which is in a separate Excel document.`
- `If this document is not available, please request a copy from the author of this logic and flow document.`

### p11

- `Power Moding - Off Road+ Customer presses X or back arrow X Customer presses Customer presses Off Road + button Headunit is On Customer presses Headunit is On power button power button Headunit is Headunit is On Forward Facing "Off" (Idle) Forward Facing (Headunit setting Camera Camera set to have Off Launches Remains Active Road + button launching Forward Facing Customer presses Camera) power button Customer presses X X Customer presses or back arrow Customer presses Off Road + button Customer presses power button Headunit is On power button Headunit is Headunit is Headunit is On "Off" (Idle) "Off" (Idle) (Headunit setting Off Road Pages set to have Off Launches Road + button launch Off Road Pages App) Customer presses power button OFF1.) If vehicle is in Off Road state prior to pressing Off Road+ hard control head unit will not initiate wake up (Power Button On).`

