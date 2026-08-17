# B3 — 懸空參照歸屬規則之獨立驗證（R-P53 / G34）

> 受檢規則：「一處參照歸屬於其位置之前最近之需求錨點」（06 包 B1 自訂）。
> 驗證方法依 R-P53：量測與前／後需求錨點之段落序距離；候選限於同一章節內。
> 產生指令：`python features/power/scripts/build_dangling_rulecheck.py`

## 1. G34 結果

| 指標 | 實測 |
|---|---|
| 受檢處數 | 31 |
| **距離後錨點較近者（反例）** | **0** |
| 前後等距者 | 3 |
| 同章節內無前錨點者 | 0 |
| 前距分布 | {1: 27, 2: 4} |
| 後距分布 | {2: 23, None: 8} |

**無反例。**

### 100% 歸屬率之成因（R-P53 要求說明）

前距分布為 **1 ×27、2 ×4**，後距分布為 **2 ×23、無後錨點 ×8** ——
即每一處參照都**緊接在其錨點的後一段**（距離 1），
而下一個錨點最近也在其後兩段。此非巧合，而是 Polarion 匯出之結構：
錨點行為 metadata（`[Artifact Type:…]`），其後緊接該需求之內文，
參照即嵌於該內文中。**故 100% 歸屬率是文件結構之必然，不是規則過度擬合。**

3 個前後等距者（前距 2、後距 2）之歸屬仍取前者 —— 此 tie-break 與 §C rule 2 同一慣例（需求錨點歸屬於其前最近之章節錨點），非本包新創。

## 2. 資源型別 —— 一項訂正

06 包之 A-PW26 與 DR-PW6 稱該等參照為「**RTF 資源**」。實測型別分布：

| 副檔名 | 處數 |
|---|---|
| `.xls` | **15** |
| `.rtf` | **14** |
| `.doc` | **1** |
| `.xlsx` | **1** |

**試算表（`.xls` / `.xlsx`）為多數，非 RTF。**
DR-PW6 向上游索取「缺漏之 RTF 資源」之表述不完整，須訂正為
「缺漏之嵌入資源（RTF / 試算表 / Word 文件）」。登記為 A-PW32。

## 3. 嵌於句中之參照（1 處）

該處之參照前後皆有實質規格文字，即缺漏之資源夾在一句需求敘述之中：

- CFTS009 §1.9.16（錨點 `4942085`）：

  ```
  Can Messages with luminosity sensor.If the luminosity sensor is present, the CAN message from Light Status shall be used to identify if the car is on day or Night Mode CFTSMV009_CIP_R4_O1872_13_inline.rtf WrapperResource   the HU shall use the signal $Day_Night_Mode$ to determine if the car is in Day or Night mode.
  ```

## 4. 逐處明細

| CFTS | 章節 | 段落序 | 前錨點（距離） | 後錨點（距離） | 資源 |
|---|---|---|---|---|---|
| 009 | §1.3.1.1 | 221 | `4941025`（1） | `4941026`（2） | `CFTSMV009_CIP_R4_O599_0_inline.rtf` |
| 009 | §1.3.1.1 | 224 | `4941026`（1） | `4941027`（2） | `CFTSMV009_CIP_R4_O1583_1_inline.rtf` |
| 009 | §1.3.2 | 382 | `4941095`（2） | — | `CFTSMV009_CIP_R4_O683_2_inline.rtf` |
| 009 | §1.3.3.5 | 771 | `4941243`（1） | `4941244`（2） | `CFTSMV009_CIP_R4_O567_Excel_Document.xls` |
| 009 | §1.3.3.5 | 777 | `4941245`（1） | `4941246`（2） | `CFTSMV009_CIP_R4_O722_3_inline.rtf` |
| 009 | §1.6.2.1 | 1044 | `4941354`（1） | `4941355`（2） | `CFTSMV009_CIP_R4_O829_4_inline.rtf` |
| 009 | §1.6.2.1 | 1047 | `4941355`（1） | — | `CFTSMV009_CIP_R4_O1584_5_inline.rtf` |
| 009 | §1.6.4.1 | 2279 | `4941738`（1） | `4941739`（2） | `CFTSMV009_CIP_R4_O1301_6_inline.rtf` |
| 009 | §1.6.4.1 | 2282 | `4941739`（1） | `4941740`（2） | `CFTSMV009_CIP_R4_O1302_7_inline.rtf` |
| 009 | §1.6.4.1 | 2288 | `4941741`（1） | `4941742`（2） | `CFTSMV009_CIP_R4_O1304_8_inline.rtf` |
| 009 | §1.6.4.1 | 2291 | `4941742`（1） | — | `CFTSMV009_CIP_R4_O1305_9_inline.rtf` |
| 009 | §1.9.1 | 2582 | `4941852`（2） | `4941853`（2） | `CFTSMV009_CIP_R4_O1710_Word_Document.doc` |
| 009 | §1.9.7 | 2720 | `4941903`（1） | `4941904`（2） | `CFTSMV009_CIP_R4_O1917_10_inline.rtf` |
| 009 | §1.9.7 | 2723 | `4941904`（1） | `4941905`（2） | `CFTSMV009_CIP_R4_O2243_11_inline.rtf` |
| 009 | §1.9.16 | 3181 | `4942083`（2） | `4942084`（2） | `CFTSMV009_CIP_R4_O1869_12_inline.rtf` |
| 009 | §1.9.16 | 3187 | `4942085`（1） | `4942086`（2） | `CFTSMV009_CIP_R4_O1872_13_inline.rtf` |
| 010 | §1.1 | 112 | `4942194`（1） | `4942195`（2） | `CFTSMV010_CIP_R3_O288_Excel_Worksheet.xlsx` |
| 010 | §1.4.1.1 | 164 | `4942204`（2） | `4942205`（2） | `CFTSMV010_CIP_R3_O374_Excel_Document.xls` |
| 010 | §1.5.2.2.1.1 | 427 | `4942307`（1） | `4942308`（2） | `CFTSMV010_CIP_R3_O418_Excel_Document.xls` |
| 010 | §1.5.2.2.1.1 | 430 | `4942308`（1） | — | `CFTSMV010_CIP_R3_O419_Excel_Document.xls` |
| 010 | §1.5.2.2.1.2 | 434 | `4942310`（1） | `4942311`（2） | `CFTSMV010_CIP_R3_O421_Excel_Document.xls` |
| 010 | §1.5.2.2.1.2 | 437 | `4942311`（1） | — | `CFTSMV010_CIP_R3_O422_Excel_Document.xls` |
| 010 | §1.5.3.2.1.1 | 451 | `4942319`（1） | `4942320`（2） | `CFTSMV010_CIP_R3_O470_Excel_Document.xls` |
| 010 | §1.5.3.2.1.1 | 454 | `4942320`（1） | `4942321`（2） | `CFTSMV010_CIP_R3_O362_Excel_Document.xls` |
| 010 | §1.5.3.2.1.1 | 457 | `4942321`（1） | `4942322`（2） | `CFTSMV010_CIP_R3_O363_Excel_Document.xls` |
| 010 | §1.5.3.2.1.2 | 464 | `4942324`（1） | `4942325`（2） | `CFTSMV010_CIP_R3_O365_Excel_Document.xls` |
| 010 | §1.5.3.2.1.2 | 467 | `4942325`（1） | — | `CFTSMV010_CIP_R3_O366_Excel_Document.xls` |
| 010 | §1.8.2.1.1 | 544 | `4942360`（1） | `4942361`（2） | `CFTSMV010_CIP_R3_O704_Excel_Document.xls` |
| 010 | §1.8.2.1.1 | 547 | `4942361`（1） | — | `CFTSMV010_CIP_R3_O705_Excel_Document.xls` |
| 010 | §1.8.2.1.2 | 552 | `4942363`（1） | `4942364`（2） | `CFTSMV010_CIP_R3_O707_Excel_Document.xls` |
| 010 | §1.8.2.1.2 | 555 | `4942364`（1） | — | `CFTSMV010_CIP_R3_O708_Excel_Document.xls` |
