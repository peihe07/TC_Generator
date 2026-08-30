# G257 —— Procedure 步驟字數 lint（73 包 / R-P398(b)）

> IN §5.2 之字數限制**約束 Procedure**；ER 無字數上限（IN §6 / §6.1）。
> §5.2A 一般步 ≤12、§5.2B 末步 ≤18、§5.2C 帶 `to …` 之 setup 步 ≤18。

> ⚠ 72 包站④-1 量之為 **ER 末步**，欄位量錯（R-P398(b)），已撤銷。

## 逾限步 **47** 步（涉 46 條 TC）

| 類 | 步數 |
|---|---|
| §5.2A 一般 | 26 |
| §5.2B 末步 | 12 |
| §5.2C `to …` | 9 |

| tc_id | 步 | 共 | 字 | 上限 | 類 | 步文 |
|---|---|---|---|---|---|---|
| `NR1L-PowerManagement-187` | 3 | 3 | **35** | 18 | §5.2B 末步 | Read the recording and check that the startup sound is present on the HU speaker |
| `NR1L-PowerManagement-186` | 3 | 3 | **28** | 18 | §5.2B 末步 | Read the recording and check that the startup sound is present on the HU speaker |
| `NR1L-PowerManagement-005` | 1 | 3 | **25** | 12 | §5.2A 一般 | Start the TLM boot sequence and send each ignition value listed in Input Test Da |
| `NR1L-PowerManagement-202` | 3 | 5 | **25** | 18 | §5.2A 一般 | Read the HU screen and check that only the "Splash Screen" is shown on it and no |
| `NR1L-PowerManagement-004` | 5 | 5 | **23** | 18 | §5.2B 末步 | Read the HU screen before and after that time and check that the "Standard Scree |
| `NR1L-PowerManagement-183` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-203` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-204` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-213` | 1 | 2 | **21** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An SOS or Assist call at the moment o |
| `NR1L-PowerManagement-218` | 1 | 3 | **21** | 12 | §5.2A 一般 | Repeat the ignition cycle listed in Input Test Data 31 times, sending $STATUS_BH |
| `NR1L-PowerManagement-050` | 3 | 3 | **20** | 18 | §5.2B 末步 | Read the bus trace and check that the first $STATUS_TELEMATIC$ frame transmitted |
| `NR1L-PowerManagement-055` | 4 | 4 | **20** | 18 | §5.2B 末步 | Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and check that the  |
| `NR1L-PowerManagement-191` | 3 | 3 | **20** | 18 | §5.2B 末步 | Read the recording and check that no startup sound is present on the HU speakers |
| `NR1L-PowerManagement-209` | 1 | 2 | **20** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A backup camera view at the moment of |
| `NR1L-PowerManagement-214` | 1 | 2 | **20** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A FOTA pop up at the moment of the tr |
| `NR1L-PowerManagement-268` | 1 | 3 | **20** | 18 | §5.2A 一般 | Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and check that the  |
| `NR1L-PowerManagement-042` | 1 | 2 | **19** | 18 | §5.2C `to …` | Keep the call active and switch the ignition working condition to the value Igni |
| `NR1L-PowerManagement-190` | 1 | 2 | **19** | 18 | §5.2C `to …` | Send the adjustment An automatic adjustment due to time zones or Daylight Saving |
| `NR1L-PowerManagement-208` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An ongoing call at the moment of the  |
| `NR1L-PowerManagement-210` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An incoming call at the moment of the |
| `NR1L-PowerManagement-211` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An outgoing call at the moment of the |
| `NR1L-PowerManagement-212` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A climate pop-up at the moment of the |
| `NR1L-PowerManagement-236` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Chrysler App icon" is s |
| `NR1L-PowerManagement-237` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Jeep App icon" is shown |
| `NR1L-PowerManagement-238` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Fiat App icon" is shown |
| `NR1L-PowerManagement-061` | 1 | 2 | **18** | 12 | §5.2A 一般 | Send the signal $STATUS_BH_BCM1.DriverDoorSts$ = 1 (Open) and send the signal $S |
| `NR1L-PowerManagement-188` | 1 | 2 | **18** | 12 | §5.2A 一般 | Send the adjustment A manual time adjustment that changes the customer selected  |
| `NR1L-PowerManagement-163` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-164` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-165` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-226` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-262` | 1 | 3 | **16** | 12 | §5.2A 一般 | Apply each ignition working condition listed in Input Test Data in turn by sendi |
| `NR1L-PowerManagement-031` | 1 | 3 | **15** | 12 | §5.2A 一般 | Place a second bluetooth call from the paired phone while $BCM_FD_27.Comfort_Ena |
| `NR1L-PowerManagement-047` | 1 | 2 | **15** | 12 | §5.2A 一般 | Let the CarPlay Device issue the request CarPlay request: neither audio control  |
| `NR1L-PowerManagement-218` | 2 | 3 | **15** | 12 | §5.2A 一般 | After each cycle, read the HU screen and record whether the "Disclaimer" screen  |
| `NR1L-PowerManagement-255` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes December, 21 |
| `NR1L-PowerManagement-256` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes March, 20th |
| `NR1L-PowerManagement-257` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes June, 21st |
| `NR1L-PowerManagement-258` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes September, 2 |
| `NR1L-PowerManagement-009` | 2 | 3 | **14** | 12 | §5.2A 一般 | Measurement window: 10 seconds and start a timer at the moment the signal change |
| `NR1L-PowerManagement-044` | 1 | 4 | **14** | 12 | §5.2A 一般 | Let the CarPlay Device issue the request CarPlay request: audio control and vide |
| `NR1L-PowerManagement-182` | 1 | 4 | **14** | 12 | §5.2A 一般 | Set Door_Ajar_Status = "Open" then "Closed" again within the same CAN wakeup cyc |
| `NR1L-PowerManagement-282` | 2 | 3 | **14** | 12 | §5.2A 一般 | Select BT Music streaming as the audio active source and read the played source |
| `NR1L-PowerManagement-283` | 2 | 3 | **14** | 12 | §5.2A 一般 | Select BT Music streaming as the audio active source and read the played source |
| `NR1L-PowerManagement-287` | 1 | 6 | **14** | 12 | §5.2A 一般 | Set Door_Ajar_Status = "Open" then "Closed" again within the same CAN wakeup cyc |
| `NR1L-PowerManagement-014` | 1 | 4 | **13** | 12 | §5.2A 一般 | Keep the Battery Critical signal at the value $STATUS_LIN.Batt_ST_Crit$ = 1 (Tru |
| `NR1L-PowerManagement-145` | 1 | 3 | **13** | 12 | §5.2A 一般 | Bring the TLM through the switch on sequence with that condition not met |
