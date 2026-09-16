| TC | 欄 | CAM-04 版 | CAM-05 版 |
|---|---|---|---|
| `NR1L-RVC-001` | 來源列 | SYS-RA-CAM-062 | SYS-RA-CAM-075 |
| `NR1L-RVC-001` | spec_reference | CFTS092-4781627 | CFTS092-4781640 |
| `NR1L-RVC-001` | pre_conditions | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STA… | 1. The HU is in Standby state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2… |
| `NR1L-RVC-003` | verbatim | · When all of the following conditions hold True: - BCM_FD_10.CmdIgnSts = RUN - RVC image active - Shift Lever changes to Reverse ShiftLever… | · When all of the following conditions hold true: - BCM_FD_10.CmdIgnSts = RUN, - ShiftLeverPosition = R > Reverse_Deb. the Head Unit shall d… |
| `NR1L-RVC-003` | 來源列 | SYS-RA-VF551_V2-488 | SYS-RA-VF551_V2-498 |
| `NR1L-RVC-003` | spec_reference | VF551_V2_PHDCC27_VF_484 | VF551_V2_PHDCC27_VF_1378 |
| `NR1L-RVC-003` | pre_conditions | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. The r… | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. No ca… |
| `NR1L-RVC-004` | verbatim | · When STATUS_BH_BCM2.CmdIgnSts = [RUN], RVC image active, Shift Lever chagne to Reverse Gear_Stat.info = [REVERSE] > Reverse_Deb, the Head … | The Head Unit shall be in Automatic Display Mode when STATUS_BH_BCM2.CmdIgnSts = [RUN] AND Gear_Stat.info = [REVERSE] > Reverse_Deb, the Hea… |
| `NR1L-RVC-004` | 來源列 | SYS-RA-VF551_V3-266 | SYS-RA-VF551_V3-260 |
| `NR1L-RVC-004` | spec_reference | VF551_V3_P363_VF_484 | VF551_V3_P363_VF_92 |
| `NR1L-RVC-004` | pre_conditions | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. The rear view camera image is displayed in Manual Di… | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. No camera image is displayed ⏎ 4. The shift lever is… |
| `NR1L-RVC-007` | expected_result | 1. The App Drawer is displayed ⏎ 2. The Settings screen is displayed ⏎ 3. The "Camera" settings screen is displayed ⏎ 4. The "ParkView Backu… | 1. The App Drawer is displayed ⏎ 2. The "Settings" screen is displayed ⏎ 3. The "Camera" settings screen is displayed ⏎ 4. The "ParkView Bac… |
| `NR1L-RVC-008` | expected_result | 1. The App Drawer is displayed ⏎ 2. The Settings screen is displayed ⏎ 3. The "Camera" settings screen is displayed ⏎ 4. The "Rear View Came… | 1. The App Drawer is displayed ⏎ 2. The "Settings" screen is displayed ⏎ 3. The "Camera" settings screen is displayed ⏎ 4. The "Rear View Ca… |
| `NR1L-RVC-009` | pre_conditions | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. The "… | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. The c… |
| `NR1L-RVC-010` | pre_conditions | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. The "… | 1. The HU is in the Full-Operation state ⏎ 2. PROXI Rear_View_Camera = 1 (Present) ⏎ 3. PROXI Rear_View_Camera_Type = 1 (Digital) ⏎ 4. The c… |
