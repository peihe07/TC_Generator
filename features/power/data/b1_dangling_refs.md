# B1 — 懸空 `WrapperResource` 參照之 leaf 層交叉（R-P45 / G29）

> 05 包 G24 測得 31 處分布於 16 章，未知 leaf 層影響面。本檔補齊。
> 歸屬規則：一處參照歸屬於其位置之前最近之**需求錨點**（與 §C rule 2 同構）；位於章節錨點後、任何需求錨點前者，明示為「不可判定」。
> **不解析任何 RTF 或 OLE stream 之內容**（R-P39 / R-P48）。
> 產生指令：`python features/power/scripts/build_dangling.py`

## 1. 彙總（G29）

| 指標 | 實測 |
|---|---|
| 懸空參照總處數 | **31** |
| ├ CFTS009 | 16 |
| └ CFTS010 | 15 |
| 分布章節數 | **16** |
| 可歸屬至某需求錨點者 | 31 |
| 不可判定（無所屬錨點） | 0 |
| **受影響之被引用錨點數** | **2** |
| **受影響之 leaf 數** | **9** / 114 |

**受影響之 leaf 清單**：`SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009`

**受影響之 Test Set 分布**：

| Test Set | 受影響 leaf 數 |
|---|---|
| Power State | 9 |

## 2. 逐處明細（31 處）

| # | CFTS | 章節 | 章節標題 | 所屬錨點 | 被引用 | 引用之 leaf | 參照之資源檔名 |
|---|---|---|---|---|---|---|---|
| 1 | 009 | §1.3.1.1 | BODY OFF and BODY ON MODE GROUPS | `4941025` | 否 | — | `CFTSMV009_CIP_R4_O599_0_inline.rtf` |
| 2 | 009 | §1.3.1.1 | BODY OFF and BODY ON MODE GROUPS | `4941026` | 否 | — | `CFTSMV009_CIP_R4_O1583_1_inline.rtf` |
| 3 | 009 | §1.3.2 | ECU CAN Architecture Configuration | `4941095` | 否 | — | `CFTSMV009_CIP_R4_O683_2_inline.rtf` |
| 4 | 009 | §1.3.3.5 | Power up Sequence | `4941243` | 否 | — | `CFTSMV009_CIP_R4_O567_Excel_Document.xls` |
| 5 | 009 | §1.3.3.5 | Power up Sequence | `4941245` | 否 | — | `CFTSMV009_CIP_R4_O722_3_inline.rtf` |
| 6 | 009 | §1.6.2.1 | TLM algorithm requirements | `4941354` | **是** | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | `CFTSMV009_CIP_R4_O829_4_inline.rtf` |
| 7 | 009 | §1.6.2.1 | TLM algorithm requirements | `4941355` | **是** | `SWE-PM-001`, `SWE-PM-002`, `SWE-PM-003`, `SWE-PM-004`, `SWE-PM-005`, `SWE-PM-006`, `SWE-PM-007`, `SWE-PM-008`, `SWE-PM-009` | `CFTSMV009_CIP_R4_O1584_5_inline.rtf` |
| 8 | 009 | §1.6.4.1 | TLM algorithm requirements | `4941738` | 否 | — | `CFTSMV009_CIP_R4_O1301_6_inline.rtf` |
| 9 | 009 | §1.6.4.1 | TLM algorithm requirements | `4941739` | 否 | — | `CFTSMV009_CIP_R4_O1302_7_inline.rtf` |
| 10 | 009 | §1.6.4.1 | TLM algorithm requirements | `4941741` | 否 | — | `CFTSMV009_CIP_R4_O1304_8_inline.rtf` |
| 11 | 009 | §1.6.4.1 | TLM algorithm requirements | `4941742` | 否 | — | `CFTSMV009_CIP_R4_O1305_9_inline.rtf` |
| 12 | 009 | §1.9.1 | Loss of Communication Behavior | `4941852` | 否 | — | `CFTSMV009_CIP_R4_O1710_Word_Document.doc` |
| 13 | 009 | §1.9.7 | Passenger Display Power Moding | `4941903` | 否 | — | `CFTSMV009_CIP_R4_O1917_10_inline.rtf` |
| 14 | 009 | §1.9.7 | Passenger Display Power Moding | `4941904` | 否 | — | `CFTSMV009_CIP_R4_O2243_11_inline.rtf` |
| 15 | 009 | §1.9.16 | Contextual Theme | `4942083` | 否 | — | `CFTSMV009_CIP_R4_O1869_12_inline.rtf` |
| 16 | 009 | §1.9.16 | Contextual Theme | `4942085` | 否 | — | `CFTSMV009_CIP_R4_O1872_13_inline.rtf` |
| 17 | 010 | §1.1 | Revision Notes | `4942194` | 否 | — | `CFTSMV010_CIP_R3_O288_Excel_Worksheet.xlsx` |
| 18 | 010 | §1.4.1.1 | Voltage Level Behavior | `4942204` | 否 | — | `CFTSMV010_CIP_R3_O374_Excel_Document.xls` |
| 19 | 010 | §1.5.2.2.1.1 | System Voltage | `4942307` | 否 | — | `CFTSMV010_CIP_R3_O418_Excel_Document.xls` |
| 20 | 010 | §1.5.2.2.1.1 | System Voltage | `4942308` | 否 | — | `CFTSMV010_CIP_R3_O419_Excel_Document.xls` |
| 21 | 010 | §1.5.2.2.1.2 | ECU Local Voltage | `4942310` | 否 | — | `CFTSMV010_CIP_R3_O421_Excel_Document.xls` |
| 22 | 010 | §1.5.2.2.1.2 | ECU Local Voltage | `4942311` | 否 | — | `CFTSMV010_CIP_R3_O422_Excel_Document.xls` |
| 23 | 010 | §1.5.3.2.1.1 | System Voltage | `4942319` | 否 | — | `CFTSMV010_CIP_R3_O470_Excel_Document.xls` |
| 24 | 010 | §1.5.3.2.1.1 | System Voltage | `4942320` | 否 | — | `CFTSMV010_CIP_R3_O362_Excel_Document.xls` |
| 25 | 010 | §1.5.3.2.1.1 | System Voltage | `4942321` | 否 | — | `CFTSMV010_CIP_R3_O363_Excel_Document.xls` |
| 26 | 010 | §1.5.3.2.1.2 | ECU Local Voltage | `4942324` | 否 | — | `CFTSMV010_CIP_R3_O365_Excel_Document.xls` |
| 27 | 010 | §1.5.3.2.1.2 | ECU Local Voltage | `4942325` | 否 | — | `CFTSMV010_CIP_R3_O366_Excel_Document.xls` |
| 28 | 010 | §1.8.2.1.1 | System Voltage | `4942360` | 否 | — | `CFTSMV010_CIP_R3_O704_Excel_Document.xls` |
| 29 | 010 | §1.8.2.1.1 | System Voltage | `4942361` | 否 | — | `CFTSMV010_CIP_R3_O705_Excel_Document.xls` |
| 30 | 010 | §1.8.2.1.2 | ECU Local Voltage | `4942363` | 否 | — | `CFTSMV010_CIP_R3_O707_Excel_Document.xls` |
| 31 | 010 | §1.8.2.1.2 | ECU Local Voltage | `4942364` | 否 | — | `CFTSMV010_CIP_R3_O708_Excel_Document.xls` |

## 3. 逐章彙總

| CFTS | 章節 | 標題 | 參照處數 | 受影響之被引用錨點 | 受影響 leaf 數 |
|---|---|---|---|---|---|
| 009 | §1.3.1.1 | BODY OFF and BODY ON MODE GROUPS | 2 | — | 0 |
| 009 | §1.3.2 | ECU CAN Architecture Configuration | 1 | — | 0 |
| 009 | §1.3.3.5 | Power up Sequence | 2 | — | 0 |
| 009 | §1.6.2.1 | TLM algorithm requirements | 2 | `4941354`, `4941355` | 9 |
| 009 | §1.6.4.1 | TLM algorithm requirements | 4 | — | 0 |
| 009 | §1.9.1 | Loss of Communication Behavior | 1 | — | 0 |
| 009 | §1.9.16 | Contextual Theme | 2 | — | 0 |
| 009 | §1.9.7 | Passenger Display Power Moding | 2 | — | 0 |
| 010 | §1.1 | Revision Notes | 1 | — | 0 |
| 010 | §1.4.1.1 | Voltage Level Behavior | 1 | — | 0 |
| 010 | §1.5.2.2.1.1 | System Voltage | 2 | — | 0 |
| 010 | §1.5.2.2.1.2 | ECU Local Voltage | 2 | — | 0 |
| 010 | §1.5.3.2.1.1 | System Voltage | 3 | — | 0 |
| 010 | §1.5.3.2.1.2 | ECU Local Voltage | 2 | — | 0 |
| 010 | §1.8.2.1.1 | System Voltage | 2 | — | 0 |
| 010 | §1.8.2.1.2 | ECU Local Voltage | 2 | — | 0 |
