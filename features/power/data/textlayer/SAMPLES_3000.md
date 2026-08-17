# §C 文字層樣本（各取前 3000 字元）
依 02 下放包 §C 末：上繳實際文字層樣本，供分析層核對正則適用面。
產生指令：`python features/power/scripts/extract_textlayer.py`

---

## cfts009_plain.txt（前 3000 字元）

```
Requirement Specification Report

R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up

Published On: 2025-9-9













“Confidential. This document and/or the contents herein must not be reproduced or divulged in whole, or in part, to any third party without the prior written permission of Stellantis.”
Table of Contents
1 Wake-up and Power-up [CFTSMV009_CIP_R4] {4941006}6
1.1 Revision Notes {4941007}6
1.2 Introduction {4941017}6
1.3 Functional requirements - PNet and CUSW {4941020}7
1.3.1 A&T System Power Definitions {4941021}7
1.3.1.1 BODY OFF and BODY ON MODE GROUPS {4941023}7
1.3.1.2 SLEEP MODE {4941031}8
1.3.1.3 STANDBY MODE {4941036}8
1.3.1.4 IDLE MODE {4941038}8
1.3.1.5 FULL OPERATION MODE {4941041}9
1.3.1.6 PARTIAL OPERATION MODE {4941043}9
1.3.1.7 STOLEN VEHICLE MODE {4941050}10
1.3.1.8 TIMED MODE {4941053}11
1.3.1.9 BENCH MODE {4941060}12
1.3.1.10 LOGISTICS MODE {4941062}12
1.3.1.11 HU State Chart (Common Power Management State-Chart) {4941066}13
1.3.1.11.1 HU State Chart {4941067}13
1.3.1.11.2 RESET MODE {4941069}13
1.3.1.11.3 NORMAL OPERATION MODE GROUP {4941071}13
1.3.1.12 Asynchronous CAN network operation {4941085}14
1.3.1.13 Error handling {4941087}14
1.3.1.13.1 SW watchdog {4941088}14
1.3.1.13.2 HW watchdog {4941091}15
1.3.2 ECU CAN Architecture Configuration (If Equipped) {4941094}15
1.3.3 System Wake Up and Power Up Conditions {4941096}15
1.3.3.1 STANDBY MODE {4941099}15
1.3.3.1.1 Radios {4941109}16
1.3.3.1.2 Amp {4941118}17
1.3.3.1.3 Integrated Center Stack (ICS) {4941124}18
1.3.3.1.4 VES3 {4941126}18
1.3.3.1.5 VES2 {4941132}18
1.3.3.1.6 External CD Player {4941139}19
1.3.3.1.7 DTV {4941144}19
1.3.3.1.8 ANC {4941149}20
1.3.3.1.9 Disassociated Center Stack Display (DCSD) {4941152}20
1.3.3.1.10 Telematics Box Module {4941154}20
1.3.3.2 Body ON Mode {4941159}21
1.3.3.2.1 Radio {4941161}21
1.3.3.2.2 Disassociated Center Stack Display (DCSD) {4941169}22
1.3.3.2.3 Integrated Center Stack (ICS) {4941173}22
1.3.3.2.4 Amp {4941175}22
1.3.3.2.5 VES3 {4941179}23
1.3.3.2.6 VES2 {4941184}23
1.3.3.2.7 Remote DVD Player {4941189}24
1.3.3.2.8 DTV {4941196}25
1.3.3.2.9 ANC {4941200}25
1.3.3.2.10 Telematic Box Module (TBM) {4941202}25
1.3.3.3 General Sleep and Wakeup Requirements for CAN-I {4941205}26
1.3.3.3.1 ICS Wakeup Reasons {4941208}26
1.3.3.3.2 HU Wakeup using Power Button {4941211}26
1.3.3.3.3 HU Wakeup from Ecall/Assist call {4941213}26
1.3.3.3.4 HU Wakeup By Door Lock/Unlock {4941215}27
1.3.3.3.5 Other HU Wakeup Requirements {4941217}27
1.3.3.3.6 HUs with CAN-C Connection {4941230}29
1.3.3.4 Body Remote Start Mode (PARTIAL OPERATION MODE) {4941232}29
1.3.3.5 Power up Sequence {4941240}30
1.3.3.5.1 PDO Theme Elements {4941264}33
1.3.4 Shipping Mode/Logistics Mode {4941289}37
1.3.5 Start-Up and Shut Down Animations {4941293}37
1.3.6 Resume Mode {4941314}43
1.4 Diagnosis and recovery {4941319}44
1.4.1 Diagnosis and recovery description {4941320}44
1.4.2 General Diagnostic Requirements {4941321}44
1.4.2.1 Igni
```

---

## cfts009_bold.txt（前 3000 字元）

```
**Requirement Specification Report**

**R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up**

Published On: 2025-9-9













**“Confidential. This document and/or the contents herein must not be reproduced or divulged in whole, or in part, to any third party without the prior written permission of Stellantis.”**
**Table of Contents**
1 Wake-up and Power-up [CFTSMV009_CIP_R4] {4941006}6
1.1 Revision Notes {4941007}6
1.2 Introduction {4941017}6
1.3 Functional requirements - PNet and CUSW {4941020}7
1.3.1 A&T System Power Definitions {4941021}7
1.3.1.1 BODY OFF and BODY ON MODE GROUPS {4941023}7
1.3.1.2 SLEEP MODE {4941031}8
1.3.1.3 STANDBY MODE {4941036}8
1.3.1.4 IDLE MODE {4941038}8
1.3.1.5 FULL OPERATION MODE {4941041}9
1.3.1.6 PARTIAL OPERATION MODE {4941043}9
1.3.1.7 STOLEN VEHICLE MODE {4941050}10
1.3.1.8 TIMED MODE {4941053}11
1.3.1.9 BENCH MODE {4941060}12
1.3.1.10 LOGISTICS MODE {4941062}12
1.3.1.11 HU State Chart (Common Power Management State-Chart) {4941066}13
1.3.1.11.1 HU State Chart {4941067}13
1.3.1.11.2 RESET MODE {4941069}13
1.3.1.11.3 NORMAL OPERATION MODE GROUP {4941071}13
1.3.1.12 Asynchronous CAN network operation {4941085}14
1.3.1.13 Error handling {4941087}14
1.3.1.13.1 SW watchdog {4941088}14
1.3.1.13.2 HW watchdog {4941091}15
1.3.2 ECU CAN Architecture Configuration (If Equipped) {4941094}15
1.3.3 System Wake Up and Power Up Conditions {4941096}15
1.3.3.1 STANDBY MODE {4941099}15
1.3.3.1.1 Radios {4941109}16
1.3.3.1.2 Amp {4941118}17
1.3.3.1.3 Integrated Center Stack (ICS) {4941124}18
1.3.3.1.4 VES3 {4941126}18
1.3.3.1.5 VES2 {4941132}18
1.3.3.1.6 External CD Player {4941139}19
1.3.3.1.7 DTV {4941144}19
1.3.3.1.8 ANC {4941149}20
1.3.3.1.9 Disassociated Center Stack Display (DCSD) {4941152}20
1.3.3.1.10 Telematics Box Module {4941154}20
1.3.3.2 Body ON Mode {4941159}21
1.3.3.2.1 Radio {4941161}21
1.3.3.2.2 Disassociated Center Stack Display (DCSD) {4941169}22
1.3.3.2.3 Integrated Center Stack (ICS) {4941173}22
1.3.3.2.4 Amp {4941175}22
1.3.3.2.5 VES3 {4941179}23
1.3.3.2.6 VES2 {4941184}23
1.3.3.2.7 Remote DVD Player {4941189}24
1.3.3.2.8 DTV {4941196}25
1.3.3.2.9 ANC {4941200}25
1.3.3.2.10 Telematic Box Module (TBM) {4941202}25
1.3.3.3 General Sleep and Wakeup Requirements for CAN-I {4941205}26
1.3.3.3.1 ICS Wakeup Reasons {4941208}26
1.3.3.3.2 HU Wakeup using Power Button {4941211}26
1.3.3.3.3 HU Wakeup from Ecall/Assist call {4941213}26
1.3.3.3.4 HU Wakeup By Door Lock/Unlock {4941215}27
1.3.3.3.5 Other HU Wakeup Requirements {4941217}27
1.3.3.3.6 HUs with CAN-C Connection {4941230}29
1.3.3.4 Body Remote Start Mode (PARTIAL OPERATION MODE) {4941232}29
1.3.3.5 Power up Sequence {4941240}30
1.3.3.5.1 PDO Theme Elements {4941264}33
1.3.4 Shipping Mode/Logistics Mode {4941289}37
1.3.5 Start-Up and Shut Down Animations {4941293}37
1.3.6 Resume Mode {4941314}43
1.4 Diagnosis and recovery {4941319}44
1.4.1 Diagnosis and recovery description {4941320}44
1.4.2 General Diagnostic Requirements {4941321
```

---

## cfts010_plain.txt（前 3000 字元）

```
Requirement Specification Report

R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down

Published On: 2025-9-9













“Confidential. This document and/or the contents herein must not be reproduced or divulged in whole, or in part, to any third party without the prior written permission of Stellantis.”
Table of ContentsTOC \o "1,5" \h \z \t 
 HYPERLINK \l "_Toc256000088" 1 Power Down [CFTSMV010_CIP_R3] {4942192}	 PAGEREF _Toc256000088 \h 4
 HYPERLINK \l "_Toc256000089" 1.1 Revision Notes {4942193}	 PAGEREF _Toc256000089 \h 4
 HYPERLINK \l "_Toc256000090" 1.2 Introduction {4942196}	 PAGEREF _Toc256000090 \h 4
 HYPERLINK \l "_Toc256000091" 1.3 Functional Requirements {4942199}	 PAGEREF _Toc256000091 \h 5
 HYPERLINK \l "_Toc256000092" 1.4 Functional requirements - PNet and CUSW {4942201}	 PAGEREF _Toc256000092 \h 5
 HYPERLINK \l "_Toc256000093" 1.4.1 Battery Voltage Level and Battery Reset {4942202}	 PAGEREF _Toc256000093 \h 5
 HYPERLINK \l "_Toc256000094" 1.4.1.1 Voltage Level Behavior {4942203}	 PAGEREF _Toc256000094 \h 5
 HYPERLINK \l "_Toc256000095" 1.4.1.2 Low Voltage Behavior {4942207}	 PAGEREF _Toc256000095 \h 5
 HYPERLINK \l "_Toc256000096" 1.4.1.2.1 Low Voltage Measured by the System {4942209}	 PAGEREF _Toc256000096 \h 5
 HYPERLINK \l "_Toc256000097" 1.4.1.2.2 Battery Cutoff Switch State {4942214}	 PAGEREF _Toc256000097 \h 6
 HYPERLINK \l "_Toc256000098" 1.4.1.2.3 Powernet Limp-Home Cutoff State {4942220}	 PAGEREF _Toc256000098 \h 7
 HYPERLINK \l "_Toc256000099" 1.4.1.3 High Voltage Behavior {4942223}	 PAGEREF _Toc256000099 \h 8
 HYPERLINK \l "_Toc256000100" 1.4.1.4 System Voltage Out-Of-Range Behavior for Different Modes {4942251}	 PAGEREF _Toc256000100 \h 11
 HYPERLINK \l "_Toc256000101" 1.4.1.5 High temperature Behavior {4942256}	 PAGEREF _Toc256000101 \h 12
 HYPERLINK \l "_Toc256000102" 1.4.1.5.1 High temperature of the disk drives and HDD drives {4942257}	 PAGEREF _Toc256000102 \h 12
 HYPERLINK \l "_Toc256000103" 1.4.1.6 Load Shed {4942260}	 PAGEREF _Toc256000103 \h 13
 HYPERLINK \l "_Toc256000104" 1.4.2 System Power Down Conditions {4942271}	 PAGEREF _Toc256000104 \h 14
 HYPERLINK \l "_Toc256000105" 1.4.3 System Power Down Conditions {4942285}	 PAGEREF _Toc256000105 \h 17
 HYPERLINK \l "_Toc256000106" 1.5 Diagnosis and recovery {4942298}	 PAGEREF _Toc256000106 \h 19
 HYPERLINK \l "_Toc256000107" 1.5.1 Diagnosis and recovery description {4942299}	 PAGEREF _Toc256000107 \h 19
 HYPERLINK \l "_Toc256000108" 1.5.2 DTC Requirements {4942300}	 PAGEREF _Toc256000108 \h 19
 HYPERLINK \l "_Toc256000109" 1.5.2.1 DTC Enable Criteria {4942301}	 PAGEREF _Toc256000109 \h 19
 HYPERLINK \l "_Toc256000110" 1.5.2.2 DTC Maturation Criteria {4942303}	 PAGEREF _Toc256000110 \h 20
 HYPERLINK \l "_Toc256000111" 1.5.2.2.1 Supply Voltage DTC's {4942305}	 PAGEREF _Toc256000111 \h 20
 HYPERLINK \l "_Toc256000112" 1.5.3 DTC Requirements {4942312}	 PAGEREF _Toc256000112 \h 20
 HYPERLINK \l "_Toc256000113" 1.5.3.1 DTC Enable Criteria {4942313}	 
```

---

## cfts010_bold.txt（前 3000 字元）

```
**Requirement Specification Report**

**R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down**

Published On: 2025-9-9













**“Confidential. This document and/or the contents herein must not be reproduced or divulged in whole, or in part, to any third party without the prior written permission of Stellantis.”**
**Table of Contents**TOC \o "1,5" \h \z \t 
 HYPERLINK \l "_Toc256000088" 1 Power Down [CFTSMV010_CIP_R3] {4942192}	 PAGEREF _Toc256000088 \h 4
 HYPERLINK \l "_Toc256000089" 1.1 Revision Notes {4942193}	 PAGEREF _Toc256000089 \h 4
 HYPERLINK \l "_Toc256000090" 1.2 Introduction {4942196}	 PAGEREF _Toc256000090 \h 4
 HYPERLINK \l "_Toc256000091" 1.3 Functional Requirements {4942199}	 PAGEREF _Toc256000091 \h 5
 HYPERLINK \l "_Toc256000092" 1.4 Functional requirements - PNet and CUSW {4942201}	 PAGEREF _Toc256000092 \h 5
 HYPERLINK \l "_Toc256000093" 1.4.1 Battery Voltage Level and Battery Reset {4942202}	 PAGEREF _Toc256000093 \h 5
 HYPERLINK \l "_Toc256000094" 1.4.1.1 Voltage Level Behavior {4942203}	 PAGEREF _Toc256000094 \h 5
 HYPERLINK \l "_Toc256000095" 1.4.1.2 Low Voltage Behavior {4942207}	 PAGEREF _Toc256000095 \h 5
 HYPERLINK \l "_Toc256000096" 1.4.1.2.1 Low Voltage Measured by the System {4942209}	 PAGEREF _Toc256000096 \h 5
 HYPERLINK \l "_Toc256000097" 1.4.1.2.2 Battery Cutoff Switch State {4942214}	 PAGEREF _Toc256000097 \h 6
 HYPERLINK \l "_Toc256000098" 1.4.1.2.3 Powernet Limp-Home Cutoff State {4942220}	 PAGEREF _Toc256000098 \h 7
 HYPERLINK \l "_Toc256000099" 1.4.1.3 High Voltage Behavior {4942223}	 PAGEREF _Toc256000099 \h 8
 HYPERLINK \l "_Toc256000100" 1.4.1.4 System Voltage Out-Of-Range Behavior for Different Modes {4942251}	 PAGEREF _Toc256000100 \h 11
 HYPERLINK \l "_Toc256000101" 1.4.1.5 High temperature Behavior {4942256}	 PAGEREF _Toc256000101 \h 12
 HYPERLINK \l "_Toc256000102" 1.4.1.5.1 High temperature of the disk drives and HDD drives {4942257}	 PAGEREF _Toc256000102 \h 12
 HYPERLINK \l "_Toc256000103" 1.4.1.6 Load Shed {4942260}	 PAGEREF _Toc256000103 \h 13
 HYPERLINK \l "_Toc256000104" 1.4.2 System Power Down Conditions {4942271}	 PAGEREF _Toc256000104 \h 14
 HYPERLINK \l "_Toc256000105" 1.4.3 System Power Down Conditions {4942285}	 PAGEREF _Toc256000105 \h 17
 HYPERLINK \l "_Toc256000106" 1.5 Diagnosis and recovery {4942298}	 PAGEREF _Toc256000106 \h 19
 HYPERLINK \l "_Toc256000107" 1.5.1 Diagnosis and recovery description {4942299}	 PAGEREF _Toc256000107 \h 19
 HYPERLINK \l "_Toc256000108" 1.5.2 DTC Requirements {4942300}	 PAGEREF _Toc256000108 \h 19
 HYPERLINK \l "_Toc256000109" 1.5.2.1 DTC Enable Criteria {4942301}	 PAGEREF _Toc256000109 \h 19
 HYPERLINK \l "_Toc256000110" 1.5.2.2 DTC Maturation Criteria {4942303}	 PAGEREF _Toc256000110 \h 20
 HYPERLINK \l "_Toc256000111" 1.5.2.2.1 Supply Voltage DTC's {4942305}	 PAGEREF _Toc256000111 \h 20
 HYPERLINK \l "_Toc256000112" 1.5.3 DTC Requirements {4942312}	 PAGEREF _Toc256000112 \h 20
 HYPERLINK \l "_Toc256000113" 1.5.3.1 DTC Enable Crit
```
