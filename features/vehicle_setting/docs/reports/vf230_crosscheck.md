# VF230 跨源驗核 —— 037 × 035 SYSRA（DR-28 之替代來源）

**量測條件**：`scripts/vf230_crosscheck.py`。
來源：`FM-WI-FSM-035-A02_VF230_HDCC_DT_STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_VF230_V4_Released.xlsx`
（`Basic Report` 分頁，表頭列 0，逐 `SYS2 Sys-RA-Feature-ID` 建索引）。
037 側為 11 份分報告之全 745 列，判準同 `vf230_leaves.py`。

## 0. 為何此檔可替代 SYS2

其 `Basic Report` 之欄位與 CFTS044 之 SYS2 export **同型**：
`SYS2 Sys-RA-Feature-ID`／`SYS2 分類 Category`／`SYS2 VF章節 Chapter for VF`／
`SYS2 EE Architecture`／`SYS2 限定地區 Region`。**`分類 Category` 即 Part 1
於 01 輪用於 537 列對帳之同一欄**。

- 035 之列（有 Sys-RA 者）：**2655**
- 其 Category 分布：`Functional Requirement` 1087／`Out of Scope` 682／`Information` 606／`Heading` 280

**另有一份 `SYS2_VF230.xlsx`**（`9_ASPICE/SYS.2 System Requirements Analysis/
Z.QS YuShen 260423/08.[SYS2]Vehicle Settings/`），schema 相同但列數較少
（2626），且**缺 037 之 6 個 `E-Save` leaf**；035 則涵蓋全部 619。
**本輪採 035**，其已在 `inputs/` 內（R-VS61 之補入由 Pei 執行）。

## 1. 正向對帳 —— 037 之判定是否為 035 所支持

| 037 側 | 列 | 命中 035 | 未命中 | 035 之 Category |
|---|---:|---:|---:|---|
| Functional（leaf） | 619 | 619 | 0 | `Functional Requirement` 619 |
| Heading | 126 | 126 | 0 | `Heading` 118／`Functional Requirement` 8 |

**leaf 側零錯配**：619 個 037 判 Functional 者，035 亦全數判
`Functional Requirement`（反向錯配 0）。

## 2. 錯配（8）—— 037 判 Heading 而 035 判 Functional

**此即 DR-28 所稱「A-VS01 型之錯配無從偵測」之標的。已偵得。**

| SWE ID | Sys-RA | 037 之條文（前 90 字） |
|---|---|---|
| `SWE1-VC-SWITCH3PowerMode-014` | `SYS-RA-VF230_V1-2271` | The HMI layer shall capture the customer selection for the SWITCH 3 Power Mode setting and |
| `SWE1-VC-SWITCH6PowerMode-026` | `SYS-RA-VF230_V1-2283` | The HMI layer shall capture the customer selection for the SWITCH 6 Power Mode setting and |
| `SWE1-VC-SWITCH3Type-039` | `SYS-RA-VF230_V1-2296` | HW supplier shall notify the IPC_VEHICLE_SETUP2.AUX3_TYPE signal via VHAL interface. CarPr |
| `SWE1-VC-SWITCH5Type-045` | `SYS-RA-VF230_V1-2302` | The HMI layer shall capture the customer selection for the SWITCH 5 Type setting and send  |
| `SWE1-VC-SWITCH6Type-051` | `SYS-RA-VF230_V1-2308` | HW supplier shall notify the IPC_VEHICLE_SETUP2.AUX6_TYPE signal via VHAL interface. CarPr |
| `SWE1-VC-SWITCH2HoldLastState-058` | `SYS-RA-VF230_V1-2314` | The HMI layer shall capture the customer selection for the SWITCH 2 Hold Last State settin |
| `SWE1-VC-SWITCH3HoldLastState-063` | `SYS-RA-VF230_V1-2319` | The HMI layer shall capture the customer selection for the SWITCH 3 Hold Last State settin |
| `SWE1-VC-SWITCH6HoldLastState-076` | `SYS-RA-VF230_V1-2332` | HW supplier shall notify the IPC_VEHICLE_SETUP2.AUX6_HLEnbl signal via VHAL interface. Car |

上列八條之 037 條文皆為 `The HMI layer shall …`／
`HW supplier shall notify …` 之形態 —— **其為需求，非節標題**。
037 之 Categorization 判 `Heading` 與其自身條文形態不符。

**本層未改 leaf 母體**：`data/vf230_leaves.tsv` 維持 619。
改判會使母體成為 627，屬裁定事項（Part 1 於 01 輪之 A-VS01 亦經裁定方除役）。

## 3. 反向覆蓋 —— 035 判 Functional 而 037 未收（460）

- 035 之 `Functional Requirement` 合計 **1087**
- 其中為 037 之 745 列所收者 **627**（57.7%）
- **未收 460**（42.3%）

未收者之屬性分布：

- EE Architecture：`ATL-Hi` 460
- Region：`NA` 460
- VF章節：59 個相異值，前六為 `01.10.01.01.75` 33／`01.10.01.01.76` 23／`01.10.01.01.70` 22／`01.10.01.01.63` 16／`01.10.01.01.42` 15／`01.10.01.01.67` 14

**同一章節內既有收錄亦有未收**（例如 `01.10.01.01.74` 於 037 收 14、
未收 33），故此非「整章委派他 feature」之乾淨切分。

**全樹搜尋確認 VF230 之 037 分報告僅此 11 份**
（`find /Users/peihe/Work -iname '*FM-WI-FSM-037*' -iname '*VF230*'`），
故未收之部分**在上游尚無 SWE.1 分析**，非本層漏收。

樣本（前 8）：

| Sys-RA | VF章節 | 條文（前 80 字） |
|---|---|---|
| `SYS-RA-VF230_V1-1000` | `01.10.01.01.72` | When Trailer_Light_Check is equal to Absent, the LTM/ETM shall not display the A |
| `SYS-RA-VF230_V1-1001` | `01.10.01.01.72` | When Trailer_Light_Check is equal to Present, the LTM/ETM shall display the Auto |
| `SYS-RA-VF230_V1-1002` | `01.10.01.01.72` | When the customer chooses to set the Automatic Trailer Light Check setting to Di |
| `SYS-RA-VF230_V1-1003` | `01.10.01.01.72` | When the customer chooses to set the Automatic Trailer Light Check setting to En |
| `SYS-RA-VF230_V1-1004` | `01.10.01.01.72` | When the LTM or ETM receives the IPC_VEHICLE_SETUP2.Trailer_Light_Check signal,  |
| `SYS-RA-VF230_V1-1006` | `01.10.01.01.73` | When Blindspot_Trailer_Detection is equal to Absent, the LTM/ETM shall not displ |
| `SYS-RA-VF230_V1-1007` | `01.10.01.01.73` | When Blindspot_Trailer_Detection is equal to Present, the LTM/ETM shall display  |
| `SYS-RA-VF230_V1-1008` | `01.10.01.01.73` | When the customer chooses to set the Blind Spot with Trailer Detection setting t |

## 4. 安全屬性（ASIL）

035 為技術安全需求分析報告，其 `SYS2 ASIL 等級 (ASIL)` 欄於 037 之 619 個命中 leaf 上之分布：`NA` 615／`(空)` 4

→ **VF230 之 leaf 無任何具 ASIL 等級者**，安全分析層不進入其 trace chain。
此與 Part 1 一致（CFTS044 之 037 亦無 ASIL 欄）。

