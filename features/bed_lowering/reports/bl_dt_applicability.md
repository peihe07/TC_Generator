# Bed Lowering Mode 之 DT 適用性查證（下放包 VS-SL-02 §1）

日期：2026-09-02　層級：Tier 1（執行層）
**只報事實，不下結論。「未提及」不寫成「無」。**
查證對象 8 檔，逐檔一節；末段彙總表。

---

## 檔 1　`Sys3_ProSys_SoftwareSystem-Architecture_Specification_Appendix_BV.xlsx`

**(a) 在磁碟上 —— 兩份副本**

| 路徑 | bytes | SHA256 前 16 |
|---|---:|---|
| `…/OneDrive_1_10-7-2024/FT/ProjectSystemFeature/SYS3/…Appendix_BV.xlsx` | 9,467,390 | `41ce5544e1a8c8e7` |
| `…/OneDrive_1_10-7-2024/FT/ProjectSystemDesign/SYS3/Appendix/…Appendix_BV.xlsx` | 9,467,390 | `637878e1d052fdc7` |

**大小相同、分頁清單逐字相同（127 分頁）、SHA 不同。** 本節讀第一份。
（总控表 `REF Table` r2 所載之 SharePoint 連結：
`https://shiftup.sharepoint.com/:x:/r/sites/R1LProject/_layouts/15/Doc2.aspx?action=edit&sour…`，
本層未開，僅記其存在。）

**(b) 查了什麼**　分頁 `FeatureSet list(Gen4_Gen5)`（283 × 23），全表逐格搜 `Bed Lowering`，命中 r15、r41。

**(c) 命中逐字**

表頭（r3–r5，合併儲存格解出）：

```
N3:O3  Atlantis (Basically use PROXI_XXX_XXX)
P3:S3  PNet  (Basically use PNET_PROXI_XXX_XXX)
N4:N5  Information to use (PROXI, VehicleConfig, etc.)
O4:O5  Logic that returns value in DT          ← Atlantis
P4:P5  Information to use (PROXI, VehicleConfig, etc.)
Q4:Q5  Logic that returns value in DT          ← PNet
R4:R5  Logic that returns value in D2/DJ       ← PNet
S4:S5  Logic that returns value in RU          ← PNet
```

**r41（F 欄 `No` = 36，K 欄 `Feature Name` = `Bed Lowering Mode`）**：

```
N  CAN node 27 (ASM/ASCM)
   Body_Types
O  If "CAN node 27 (ASM/ASCM)" is [Present] and "Body_Types" is ([Type 1] or [Type 4])
   , return value is true.
   Other return values are false.
P  BLM_PRSNT (Bed Lowering Mode Softkey present)
Q  Always false
R  If "BLM_PRSNT (Bed Lowering Mode Softkey present)" is [Set], return value is true.
   Other return values are false.
S  Same as DT
```

r15（`No` = 10，`Controls`）之 Q 欄將 `No.36 Bed Lowering Mode` 列為 Controls 之從屬項之一，
未帶車型陳述。

**(d) 對「DT 有無 Bed Lowering」之陳述：無。**
理由（逐欄）：Atlantis 之 **DT 欄**（O）條件不含 `Type 7`；PNet 之 **DT 欄**（Q）逐字為 `Always false`；
PNet 之 **D2/DJ 欄**（R）方為條件式。**兩個架構的 DT 欄都排除 DT。**

---

## 檔 2　`SYS3_Vehicle_Settings_…SYSAD_v1.0.docx`

**(a) 在磁碟上 —— 7 份副本，其中 6 份 SHA 相同**

| SHA256 前 16 | bytes | 路徑（節錄） |
|---|---:|---|
| `469162b81bf31018` | 16,694,938 | `TC_Generator/features/vehicle_setting/inputs/` |
| `469162b81bf31018` | 16,694,938 | `TC_Generator/sources/raw/vf665_sysad_sys3/` |
| `469162b81bf31018` | 16,694,938 | `Work/02_Project_R1LR/9_ASPICE/SYS.3 …/Vehicle Settings/` |
| `469162b81bf31018` | 16,694,938 | `…/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/**VF665**/` |
| `469162b81bf31018` | 16,694,938 | `…/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/**VF230_V1_R5**/` |
| `469162b81bf31018` | 16,694,938 | `…/ASW-R2/Vehicle Settings/CFTS044/REF/` |
| `1a4293d96d4a10a4` | 16,691,772 | `Work_Projects/R1L_RTM_V3/data/9_ASPICE/03_SYS.3 …/Vehicle Settings/` |

**包內所問之「VF665 目錄有同名副本，先比 SHA 是否同檔」——答：同檔**
（VF665 與 VF230_V1_R5 兩份 SHA 皆為 `469162b81bf31018`）。
另有一份 `R1L_RTM_V3` 之副本 **SHA 不同、bytes 少 3,166**，本層未展開其差異。

**(b) 查了什麼**　`word/document.xml` 去標籤後 1,553 段、64,946 字元，逐段搜
`Bed Lowering`／`BLM`／`Body_Types`／`Type 7`／`Bed_Lowering`。

**(c) 命中逐字**

```
Bed Lowering   2 段
  [474] SYS-RA-VF230_V1-1087
  [475] Bed Lowering Mode          ← 命中段
  [476] SYS-RA-VF230_V1-1093

  [1238] Trailer Tire Pressure Monitoring System
  [1239] Bed Lowering Mode          ← 命中段
  [1240] 4.6.3 ComfortSeat Widget Implementation Clarification

BLM            0 段
Body_Types     0 段
Type 7         0 段
Bed_Lowering   0 段
```

兩處皆為需求 ID 清單／功能名清單中的一個條目，**前後段皆無車型限定語**。

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**

---

## 檔 3　`forms/SR26 Default Settings and PNet ECU Configuration v1_0.xlsx`

**(a)** 在磁碟上。SHA256 前 16：`8f3ae50edd9e8355`。

**(b)** 分頁 `Default Parameters`（268 × 109）與 `PNET ECU Master Configurations`（122 × 16384），
逐格搜 `Bed Lowering`／`BLM`／`Body_Types`／`ASM`／`ASCM`。

**(c) 命中逐字**

- `Default Parameters`：**五個字串皆零命中**。
- `PNET ECU Master Configurations` r65：

```
D  7                     (Start Bit)
E  7                     (Stop Bit)
F  Bed Lowering Mode Softkey present     (Signal)
G  EC_AudTel3B                           (Bus Signal)
H  Table                                 (Coding)
I  0 = Not Set / 1 = Set                 (Table)
J  $BLM_PRSNT$                           (Logical Identifier)
K  CFTS044                               (Requirements Reference)
```

**該分頁無車型欄**（表頭 r2 為 `Parameter`／`Start Byte`／…／`Change Log`，共 13 欄具名），
故「逐欄列 DT 與 DJ/D2 之值」一項**無欄可列**。

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**
（本檔只定義 `$BLM_PRSNT$` 之位元位置與編碼，不作車型分配。）

---

## 檔 4　`forms/SR24 R1 Market Configuration Table v1.6.xlsx`

**(a)** 在磁碟上。SHA256 前 16：`7e865d557e42c8b0`。

**(b)** 分頁 `Market Config - R1`（1001 × 61），逐格搜
`Bed Lowering`／`BLM`／`Body_Types`／`ASM`／`ASCM`。

**(c) 命中逐字**　**五個字串皆零命中。** 故「DT 行之值」**無行可取**。

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**

---

## 檔 5　`forms/PROXI_HDCC27_R3_20250424.xlsx`

**(a)** 在磁碟上。SHA256 前 16：`e7c2020f01c3d58d`。
**注意（包內已提示）：檔名 `HDCC27` = HD 車系，非 DT。**

**(b)** 分頁 `Format`（1060 × 24），`Parameter Name`（F 欄）共 1,058 個具名參數。

**(c) 命中逐字**

`Body_Types` 於 r1019（A 欄 `Car_Configuration_59`，位元 231.0–231.2），I 欄 `Table` 逐字：

```
 0 = Absent
 1 = Type 1 - D2
 2 = Type 2 - DD
 3 = Type 3 - DF
 4 = Type 4 - DJ
 5 = Type 5 - DP
 6 = Type 6 - DX
 7 = Type 7 - DT
```

以 `BLM`／`Bed`／`BDL` 開頭之 `Parameter Name`：**僅 `Bed_Lighting_Presence`（r942）**，
與 Bed Lowering 無關。**無 `BLM_PRSNT`、無 `Bed_Lowering` 之 PROXI 參數。**

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**
（本檔確認 `Type 7 - DT` 為 `Body_Types` 之合法值，但不述 Bed Lowering 之車型分配。）

---

## 檔 6　`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`

**(a)** 在磁碟上。SHA256 前 16：`a01e1679c706cd45`。
（`features/vehicle_setting/inputs/` 另有 `v1_76`，本節依包內所指讀 `v1_78`。）

**(b)** 分頁 `Proxi & Configuration`（449 × 31），搜 `Bed Lowering`／`BLM`／`Body_Types`。

**(c) 命中逐字**

表頭 r2 之欄組：`A LID Information`／`F Powernet`／`K CUSW`／**`P Atlantis & Atlantis High`**／`U Compact`／`Z Comments`

r30：

```
A  BDL_PRSNT                        (Logical Identifier)
B  Bed Lowering Present             (Function)
C  EC_AudTel3B <BDL_PRSNT>          (Object Text)
D  Pnet                             (Arch Basis)
F  EcuCfg16.EC_AudTel3B <BDL_PRSNT> (Powernet Signal Name)
G  CAN-B                            (Powernet CAN)
```

`Body_Types`：零命中。

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**

> **觀察（非該檔之陳述，本層標明為推論，不計入彙總）**：r30 之 `Arch Basis` 欄逐字為 `Pnet`，
> 且 `Atlantis & Atlantis High` 欄組（P–T）**全空**。本檔未就車型作任何陳述，
> 此為訊號架構之記載，非「DT 無 Bed Lowering」之直述。

---

## 檔 7　`features/bed_lowering/inputs/` 之 037 報告與 SYS1_HMI 表

**(a)** 兩檔皆在磁碟上。

| 檔 | SHA256 前 16 |
|---|---|
| `FM-WI-FSM-037-A03-N1L-SWE1-BedLoweringMode-HMI-V0.1 STLA 報告.xlsx` | `8d09ab46e69da3ad` |
| `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021).xlsx` | `487354fa935dbc53` |

（同目錄另有 `Bed Lowering Mode HMI Logic and Flow R1 SR24 1A (June 21 2021).pdf`，665,190 bytes，
本節未展開，其 xlsx 版即上表第二檔。）

**(b)** 037 報告分頁 `Analysis Report`（225 × 20，leaf 218 列，表頭 r7）與
SYS1_HMI 分頁 `Basic Report`（72 × 7），搜 `\bDT\b`／`\bDJ\b`／`\bD2\b`／`Body_Types`／`Type 7`。

**(c) 命中逐字**

**是否有車型適用欄**：兩檔**皆無**。037 之 20 欄為
`SWE-Requirement ID`／`Source Requirement ID`／`HMI Source ID`／`Requirement Title`／
`Requirement Description`／`Release Version`／`Categorization`／`FROP`／`Sub Categorization`／
`Feasibility`／…／`Verification Method`；**無車型欄**。車型資訊寫在 `Requirement Title`／`Description` 之文字內。

SYS1_HMI `Basic Report`：

```
r3 D  DT : An App/Control which raises the front suspension and lowers the rear suspension
      to allow the truck bed to be sprayed out and for the debris and water to run out of t…
r4 D  DJ/D2 : An App/Control which lowers the rear suspension only for the same use cases.
r67 D The current ride height control system (for DT) which operates through use of the
      existing air suspension system is capable of adjusting the front suspension to the highe…
```

**037 報告之 `Requirement Description`／`Title` 含 `DT` 之 leaf 列（10 列，全列）**：

| 列 | `Requirement Title` |
|---:|---|
| r8 | `DT Bed Lowering Control` |
| r9 | `DT Bed Lowering Entry` |
| r10 | `Front Suspension Raise Request` |
| r11 | `Rear Suspension Lower Request` |
| r12 | `Coordinated Lowering Operation` |
| r215 | `DT/DJ-D2 Ride Height Behavior` |
| r216 | `DT Front Off-Road 2 Setting` |
| r217 | `DT Rear Easy Entry Setting` |
| r218 | `DT Combined Ride-Height Strategy` |
| r220 | `No DT Front Raise for DJ/D2` |

含 `DJ`／`D2` 者（10 列）：r13, r14, r15, r16, r17, r18, r19, r215, r219, r220。

r9 之 `Requirement Description` 逐字：

```
The system shall provide a Bed Lowering feature entry for DT vehicle configuration in the
head unit, so that the user can request the Bed Lowering function through the HMI.
```

r10／r11／r12 逐字：

```
r10  When the user triggers the DT Bed Lowering feature entry from the head unit, the system
     shall issue a control request to raise the front suspension.
r11  When the user triggers the DT Bed Lowering feature entry from the head unit, the system
     shall issue a control request to lower the rear suspension.
r12  The system shall coordinate the front-suspension raise action and rear-suspension lower
     action as one Bed Lowering operation for DT.
```

**(d) 對「DT 有無 Bed Lowering」之陳述：有。**
037 報告有 **5 條 DT 專屬需求**（r8–r12）以 `shall` 明述 DT 之 HMI 入口與前升後降動作；
SYS1_HMI r3 之 use case 亦逐字區分 DT 與 DJ/D2。

---

## 檔 8　`features/bed_lowering/output/…_SWQT_BedLowering_20260827.xlsx` 之 T–Z 車型欄

**(a)** 在磁碟上。SHA256 前 16：`efa1da4c8f59c98d`。

**(b)** 分頁 `Test Case Specification 測試用例規範`，資料列 r10–r160（151 列），表頭 r9。

**(c) 命中逐字**　表頭：

```
T  HDCC27 Atl-Hi
U  DT27 Atl-Hi
V  VF(ProMaster)637 Atl-Mid    W  Commander (598) Atl-Mid
X  Regengade (5210) Atl-Mid    Y  Toro(2261) Atl-Mid       Z  Fastack (376) Atl-Mid
```

**151 列之 T–Z 七欄全部為空**（逐列逐欄實測，0／1／空之計數：**空 151、0 為 0、1 為 0**，七欄皆同）。
S–AH 之非空欄僅 `AA Test Case Author` = `PeiPYHsu` × 151。

**(d) 對「DT 有無 Bed Lowering」之陳述：未提及。**

---

## 彙總表

| # | 檔 | 有 | 無 | 未提及 |
|---|---|:--:|:--:|:--:|
| 1 | `…Architecture_Specification_Appendix_BV.xlsx` `FeatureSet list(Gen4_Gen5)` r41 | | **●** | |
| 2 | `SYS3_Vehicle_Settings_…SYSAD_v1.0.docx` | | | **●** |
| 3 | `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | | | **●** |
| 4 | `SR24 R1 Market Configuration Table v1.6.xlsx` | | | **●** |
| 5 | `PROXI_HDCC27_R3_20250424.xlsx` `Format` | | | **●** |
| 6 | `Logical Identifiers and CAN Mapping v1_78.xlsx` `Proxi & Configuration` r30 | | | **●** |
| 7 | `bed_lowering/inputs/` 037 報告（r8–r12）＋ SYS1_HMI（r3/r4/r67） | **●** | | |
| 8 | `…_SWQT_BedLowering_20260827.xlsx` T–Z 欄 | | | **●** |

**計數：有 1／無 1／未提及 6。**

### 兩造之性質差異（事實陳述，非裁定）

- **檔 1（無）** 為**組態架構**文件：其 `Bed Lowering Mode` 之顯示條件依 `Body_Types` 與
  `BLM_PRSNT` 判定，Atlantis-DT 欄與 PNet-DT 欄皆不使該功能為 true。
- **檔 7（有）** 為**需求**文件：其 5 條 DT 專屬 `shall` 描述 DT 之功能行為（前升後降）。
- 二者**未在同一份文件內相互引用**；本層查得之 8 檔中，**無任何一檔同時陳述兩者並作出取捨**。

### 查無而依 R-G13 三要件記載者

| 所查之物 | 何處查 | 如何查 | 結果 |
|---|---|---|---|
| `Body_Types` 於 `SR24 Market Config` | `Market Config - R1` 1001×61 | 逐格不分大小寫子字串 | 零命中 → **未查得** |
| `BLM_PRSNT` 於 `PROXI_HDCC27` | `Format` F 欄 1,058 參數 | 前綴 `BLM`／`Bed`／`BDL` | 僅 `Bed_Lighting_Presence` → **未查得** |
| `Body_Types` 於 `LID v1_78` | `Proxi & Configuration` 449×31 | 逐格不分大小寫子字串 | 零命中 → **未查得** |
| 車型適用欄於 037／SYS1_HMI | 兩檔全部分頁之表頭 | 逐欄具名比對 | 無此欄 → **未查得**（車型資訊在敘述文字內） |

**本節不開 DR**（依包內停止條件，DR 由 Pei 於看過彙總表後決定）。
