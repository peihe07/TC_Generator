# G257 —— Procedure 步驟字數 lint（73 包 / R-P398(b)）

> IN §5.2 之字數限制**約束 Procedure**；ER 無字數上限（IN §6 / §6.1）。
> §5.2A 一般步 ≤12、§5.2B 末步 ≤18、§5.2C 帶 `to …` 之 setup 步 ≤18。

> ⚠ 72 包站④-1 量之為 **ER 末步**，欄位量錯（R-P398(b)），已撤銷。

## 逾限步 **146** 步（涉 111 條 TC）

| 類 | 步數 |
|---|---|
| §5.2A 一般 | 105 |
| §5.2B 末步 | 31 |
| §5.2C `to …` | 10 |

| tc_id | 步 | 共 | 字 | 上限 | 類 | 步文 |
|---|---|---|---|---|---|---|
| `NR1L-PowerManagement-187` | 3 | 3 | **35** | 18 | §5.2B 末步 | Read the recording and check that the startup sound is present on the HU speaker |
| `NR1L-PowerManagement-159` | 2 | 2 | **31** | 18 | §5.2B 末步 | Read the HU screen and check that the "Call Screen" is shown on it, and check th |
| `NR1L-PowerManagement-160` | 2 | 2 | **31** | 18 | §5.2B 末步 | Read the HU screen and check that the "Call Screen" is shown on it, and check th |
| `NR1L-PowerManagement-161` | 2 | 2 | **31** | 18 | §5.2B 末步 | Read the HU screen and check that the "Call Screen" is shown on it, and check th |
| `NR1L-PowerManagement-173` | 2 | 2 | **31** | 18 | §5.2B 末步 | Read the HU screen and check that it goes dark and then shows the "Splash Screen |
| `NR1L-PowerManagement-004` | 3 | 3 | **28** | 18 | §5.2B 末步 | PENDING: DR-PW30 StandardScreen_Time 之值 —— read the HU screen before and after t |
| `NR1L-PowerManagement-186` | 3 | 3 | **28** | 18 | §5.2B 末步 | Read the recording and check that the startup sound is present on the HU speaker |
| `NR1L-PowerManagement-027` | 2 | 5 | **26** | 12 | §5.2A 一般 | Read the paired phone screen and check that it shows the call as connected, and  |
| `NR1L-PowerManagement-155` | 3 | 3 | **26** | 18 | §5.2B 末步 | Apply ENTER_FULL_OPERATION and read the "Brand Logo Screen", and check that the  |
| `NR1L-PowerManagement-169` | 4 | 5 | **26** | 12 | §5.2A 一般 | Hold for 60000 ms with no user interaction, then read the HU screen and check th |
| `NR1L-PowerManagement-185` | 3 | 3 | **26** | 18 | §5.2B 末步 | Apply ENTER_FULL_OPERATION and read the "Brand Logo Screen", and check that the  |
| `NR1L-PowerManagement-005` | 1 | 3 | **25** | 12 | §5.2A 一般 | Start the TLM boot sequence and send each ignition value listed in Input Test Da |
| `NR1L-PowerManagement-119` | 4 | 4 | **25** | 18 | §5.2B 末步 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Ti |
| `NR1L-PowerManagement-120` | 4 | 4 | **25** | 18 | §5.2B 末步 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Ti |
| `NR1L-PowerManagement-202` | 3 | 4 | **25** | 12 | §5.2A 一般 | Read the HU screen and check that only the "Splash Screen" is shown on it and no |
| `NR1L-PowerManagement-268` | 1 | 2 | **25** | 12 | §5.2A 一般 | Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and check that the  |
| `NR1L-PowerManagement-281` | 4 | 5 | **25** | 12 | §5.2A 一般 | PENDING: DR-PW27 BoosterOUT / analog and digital antenna supply 之 ON 位準值 —— meas |
| `NR1L-PowerManagement-281` | 5 | 5 | **25** | 18 | §5.2B 末步 | Insert a USB device and check that it is enumerated and can be played, and check |
| `NR1L-PowerManagement-202` | 4 | 4 | **24** | 18 | §5.2B 末步 | Touch the screen and read the bus trace, and check that $TELEMATIC_FD_5.CM_TCH_S |
| `NR1L-PowerManagement-271` | 1 | 3 | **24** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Ti |
| `NR1L-PowerManagement-284` | 4 | 5 | **24** | 12 | §5.2A 一般 | Dismiss the "FOTA update available" pop-up through the HMI, then read the HU scr |
| `NR1L-PowerManagement-118` | 3 | 3 | **23** | 18 | §5.2B 末步 | Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 15 (SNA) (DR-PW26), then r |
| `NR1L-PowerManagement-182` | 3 | 3 | **23** | 18 | §5.2B 末步 | Hold for 1800000 ms, repeat the door event, then read the HU screen and check th |
| `NR1L-PowerManagement-219` | 2 | 2 | **23** | 18 | §5.2B 末步 | Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on it  |
| `NR1L-PowerManagement-220` | 2 | 2 | **23** | 18 | §5.2B 末步 | Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on it  |
| `NR1L-PowerManagement-221` | 2 | 2 | **23** | 18 | §5.2B 末步 | Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on it  |
| `NR1L-PowerManagement-004` | 2 | 3 | **22** | 12 | §5.2A 一般 | PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen at that time and che |
| `NR1L-PowerManagement-183` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-203` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-204` | 2 | 2 | **22** | 18 | §5.2B 末步 | Read the HU screen and check that the "Start-up Animation", the "Splash Screen"  |
| `NR1L-PowerManagement-287` | 3 | 4 | **22** | 18 | §5.2C `to …` | PENDING: DR-PW26 Sleep 態之觀察方法 —— let the Body CAN go to sleep and wake it again  |
| `NR1L-PowerManagement-118` | 1 | 3 | **21** | 12 | §5.2A 一般 | Apply ENTER_FULL_OPERATION, send the signal $STATUS_BH_BCM1.OperationalModeSts$  |
| `NR1L-PowerManagement-213` | 1 | 2 | **21** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An SOS or Assist call at the moment o |
| `NR1L-PowerManagement-218` | 1 | 3 | **21** | 12 | §5.2A 一般 | Repeat the ignition cycle listed in Input Test Data 31 times, sending $STATUS_BH |
| `NR1L-PowerManagement-001` | 2 | 2 | **20** | 18 | §5.2B 末步 | PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen and check the "Splas |
| `NR1L-PowerManagement-002` | 2 | 2 | **20** | 18 | §5.2B 末步 | PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen and check the "Splas |
| `NR1L-PowerManagement-003` | 2 | 2 | **20** | 18 | §5.2B 末步 | PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen and check the "Splas |
| `NR1L-PowerManagement-050` | 3 | 3 | **20** | 18 | §5.2B 末步 | Read the bus trace and check that the first $STATUS_TELEMATIC$ frame transmitted |
| `NR1L-PowerManagement-055` | 4 | 4 | **20** | 18 | §5.2B 末步 | Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and check that the  |
| `NR1L-PowerManagement-191` | 3 | 3 | **20** | 18 | §5.2B 末步 | Read the recording and check that no startup sound is present on the HU speakers |
| `NR1L-PowerManagement-209` | 1 | 2 | **20** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A backup camera view at the moment of |
| `NR1L-PowerManagement-214` | 1 | 2 | **20** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A FOTA pop up at the moment of the tr |
| `NR1L-PowerManagement-042` | 1 | 2 | **19** | 18 | §5.2C `to …` | Keep the call active and switch the ignition working condition to the value Igni |
| `NR1L-PowerManagement-049` | 3 | 4 | **19** | 12 | §5.2A 一般 | Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On) (DR-PW26), |
| `NR1L-PowerManagement-190` | 1 | 2 | **19** | 18 | §5.2C `to …` | Send the adjustment An automatic adjustment due to time zones or Daylight Saving |
| `NR1L-PowerManagement-208` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An ongoing call at the moment of the  |
| `NR1L-PowerManagement-210` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An incoming call at the moment of the |
| `NR1L-PowerManagement-211` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event An outgoing call at the moment of the |
| `NR1L-PowerManagement-212` | 1 | 2 | **19** | 18 | §5.2C `to …` | Bring the HU to Timed mode while the event A climate pop-up at the moment of the |
| `NR1L-PowerManagement-236` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Chrysler App icon" is s |
| `NR1L-PowerManagement-237` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Jeep App icon" is shown |
| `NR1L-PowerManagement-238` | 2 | 2 | **19** | 18 | §5.2B 末步 | Read the App Drawer on the HU screen and check that the "Fiat App icon" is shown |
| `NR1L-PowerManagement-287` | 4 | 4 | **19** | 18 | §5.2B 末步 | Repeat the door event and read the HU screen, and check that the "Start-up Anima |
| `NR1L-PowerManagement-027` | 4 | 5 | **18** | 12 | §5.2A 一般 | Read the HU screen and check that the "Incoming Call" pop-up is shown on it, the |
| `NR1L-PowerManagement-061` | 1 | 2 | **18** | 12 | §5.2A 一般 | Send the signal $STATUS_BH_BCM1.DriverDoorSts$ = 1 (Open) and send the signal $S |
| `NR1L-PowerManagement-100` | 3 | 4 | **18** | 12 | §5.2A 一般 | Hold for the PROXI Switch_Off_Time value, then read the signal $STATUS_TELEMATIC |
| `NR1L-PowerManagement-101` | 3 | 4 | **18** | 12 | §5.2A 一般 | Hold for the PROXI Switch_Off_Time value, then read the signal $STATUS_TELEMATIC |
| `NR1L-PowerManagement-188` | 1 | 2 | **18** | 12 | §5.2A 一般 | Send the adjustment A manual time adjustment that changes the customer selected  |
| `NR1L-PowerManagement-163` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-164` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-165` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-172` | 2 | 3 | **17** | 12 | §5.2A 一般 | Read the HU screen and check that it goes dark and then shows the "Splash Screen |
| `NR1L-PowerManagement-226` | 1 | 2 | **17** | 12 | §5.2A 一般 | Let the bench place and then end the call An incoming phone call that then becom |
| `NR1L-PowerManagement-261` | 4 | 5 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-264` | 1 | 2 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-267` | 4 | 5 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-273` | 6 | 7 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-275` | 6 | 7 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-277` | 4 | 5 | **17** | 12 | §5.2A 一般 | Touch the screen and read the bus trace, and check whether $TELEMATIC_FD_5.CM_TC |
| `NR1L-PowerManagement-011` | 3 | 4 | **16** | 12 | §5.2A 一般 | Read the HU speakers and check that the call audio is no longer present on them |
| `NR1L-PowerManagement-012` | 2 | 3 | **16** | 12 | §5.2A 一般 | Read the HU speakers and check that the call audio is no longer present on them |
| `NR1L-PowerManagement-081` | 2 | 3 | **16** | 12 | §5.2A 一般 | Read the HU screen and check that the "Rear View Camera" video is shown on it |
| `NR1L-PowerManagement-224` | 2 | 3 | **16** | 12 | §5.2A 一般 | Read the HU screen and check whether the "Disclaimer" screen or the geolocation  |
| `NR1L-PowerManagement-262` | 1 | 3 | **16** | 12 | §5.2A 一般 | Apply each ignition working condition listed in Input Test Data in turn by sendi |
| `NR1L-PowerManagement-030` | 2 | 3 | **15** | 12 | §5.2A 一般 | Read the source indicator and record its value, then check it against the record |
| `NR1L-PowerManagement-031` | 1 | 3 | **15** | 12 | §5.2A 一般 | Place a second bluetooth call from the paired phone while $BCM_FD_27.Comfort_Ena |
| `NR1L-PowerManagement-031` | 2 | 3 | **15** | 12 | §5.2A 一般 | Answer the call and check that the call audio is present on the HU speakers |
| `NR1L-PowerManagement-033` | 3 | 4 | **15** | 12 | §5.2A 一般 | Read the source indicator and record its value, then check it against the record |
| `NR1L-PowerManagement-047` | 1 | 2 | **15** | 12 | §5.2A 一般 | Let the CarPlay Device issue the request CarPlay request: neither audio control  |
| `NR1L-PowerManagement-182` | 2 | 3 | **15** | 12 | §5.2A 一般 | Read the HU screen and check that the "Start-up Animation" is not played on it |
| `NR1L-PowerManagement-218` | 2 | 3 | **15** | 12 | §5.2A 一般 | After each cycle, read the HU screen and record whether the "Disclaimer" screen  |
| `NR1L-PowerManagement-255` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes December, 21 |
| `NR1L-PowerManagement-256` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes March, 20th |
| `NR1L-PowerManagement-257` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes June, 21st |
| `NR1L-PowerManagement-258` | 1 | 2 | **15** | 12 | §5.2A 一般 | Bring the HU through the event An Ignition On after the date passes September, 2 |
| `NR1L-PowerManagement-281` | 3 | 5 | **15** | 12 | §5.2A 一般 | Read the HU speakers and check that the audio active source is playing on them |
| `NR1L-PowerManagement-287` | 2 | 4 | **15** | 12 | §5.2A 一般 | Read the HU screen and check that the "Start-up Animation" is not played on it |
| `NR1L-PowerManagement-009` | 2 | 3 | **14** | 12 | §5.2A 一般 | Measurement window: 10 seconds and start a timer at the moment the signal change |
| `NR1L-PowerManagement-044` | 1 | 4 | **14** | 12 | §5.2A 一般 | Let the CarPlay Device issue the request CarPlay request: audio control and vide |
| `NR1L-PowerManagement-044` | 3 | 4 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-045` | 3 | 4 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-046` | 3 | 4 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-100` | 2 | 4 | **14** | 12 | §5.2A 一般 | Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and  |
| `NR1L-PowerManagement-101` | 2 | 4 | **14** | 12 | §5.2A 一般 | Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and  |
| `NR1L-PowerManagement-103` | 2 | 3 | **14** | 12 | §5.2A 一般 | Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and  |
| `NR1L-PowerManagement-104` | 2 | 3 | **14** | 12 | §5.2A 一般 | Apply ENTER_TIMED and read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and  |
| `NR1L-PowerManagement-169` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU screen and check that the "FOTA update available" pop-up is shown |
| `NR1L-PowerManagement-182` | 1 | 3 | **14** | 12 | §5.2A 一般 | Set Door_Ajar_Status = "Open" then "Closed" again within the same CAN wakeup cyc |
| `NR1L-PowerManagement-198` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-199` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-200` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-201` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-249` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the seat settings screen and check which "Seat Graphic" is shown on it |
| `NR1L-PowerManagement-250` | 2 | 3 | **14** | 12 | §5.2A 一般 | Read the "Performance Gauges" screen and check which "Performance Gauges" are sh |
| `NR1L-PowerManagement-261` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-262` | 2 | 3 | **14** | 12 | §5.2A 一般 | After each one, read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check  |
| `NR1L-PowerManagement-263` | 1 | 2 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-267` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-273` | 2 | 7 | **14** | 12 | §5.2A 一般 | Read the bus trace and check whether the HU keeps transmitting the $STATUS_TELEM |
| `NR1L-PowerManagement-273` | 4 | 7 | **14** | 12 | §5.2A 一般 | Apply FUNC_STATE_Standby and check its Display / Illumination sub-item  (FPDM 對應 |
| `NR1L-PowerManagement-273` | 5 | 7 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-275` | 2 | 7 | **14** | 12 | §5.2A 一般 | Read the bus trace and check whether the HU keeps transmitting the $STATUS_TELEM |
| `NR1L-PowerManagement-275` | 4 | 7 | **14** | 12 | §5.2A 一般 | Apply FUNC_STATE_Sleep and check its Display / Illumination sub-item  (FPDM 對應為分 |
| `NR1L-PowerManagement-275` | 5 | 7 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-277` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU speakers and check whether entertainment audio output is present on  |
| `NR1L-PowerManagement-282` | 2 | 3 | **14** | 12 | §5.2A 一般 | Select BT Music streaming as the audio active source and read the played source |
| `NR1L-PowerManagement-283` | 2 | 3 | **14** | 12 | §5.2A 一般 | Select BT Music streaming as the audio active source and read the played source |
| `NR1L-PowerManagement-284` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU screen and check that the "FOTA update available" pop-up is shown |
| `NR1L-PowerManagement-285` | 3 | 5 | **14** | 12 | §5.2A 一般 | Read the HU screen and check that the "FOTA update available" pop-up is shown |
| `NR1L-PowerManagement-287` | 1 | 4 | **14** | 12 | §5.2A 一般 | Set Door_Ajar_Status = "Open" then "Closed" again within the same CAN wakeup cyc |
| `NR1L-PowerManagement-014` | 1 | 4 | **13** | 12 | §5.2A 一般 | Keep the Battery Critical signal at the value $STATUS_LIN.Batt_ST_Crit$ = 1 (Tru |
| `NR1L-PowerManagement-044` | 2 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-045` | 2 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-046` | 2 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-062` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-074` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-076` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-137` | 3 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-138` | 3 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-144` | 3 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-145` | 1 | 3 | **13** | 12 | §5.2A 一般 | Bring the TLM through the switch on sequence with that condition not met |
| `NR1L-PowerManagement-147` | 3 | 4 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-157` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-162` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-166` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-167` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-168` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-184` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-225` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-242` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the climate screen and check which "Recirc Icon" is shown on it |
| `NR1L-PowerManagement-243` | 2 | 3 | **13** | 12 | §5.2A 一般 | Read the climate screen and check which "Recirc Icon" is shown on it |
| `NR1L-PowerManagement-261` | 1 | 5 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-267` | 2 | 5 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-273` | 1 | 7 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-275` | 1 | 7 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
| `NR1L-PowerManagement-278` | 2 | 7 | **13** | 12 | §5.2A 一般 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is the e |
