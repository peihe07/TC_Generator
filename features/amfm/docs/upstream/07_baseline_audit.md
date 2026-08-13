# 上繳包 07 — R21 基準稽核（(c) 完成，(a) 因停手條件未執行）

執行層 → 分析層。2026-08-13。回應 `docs/handoff/07_baseline_audit.md` §4 之六項要求。

> ## ⛔ 停手條件 1 觸發
>
> 2.1 稽核出現 **一個 `NO_MATCH`**：
> `features/media/inputs/FM-WI-FSM-036-A01 …_SWQT_MediaHMI_20260625.xlsx`
> 之 SHA256 與客戶樹唯一同名候選不符。
>
> 依 07 包 §3.1：**停止 2.3 之程式碼變更**，續行 2.2 之登記，立即回報。
> `backend/api_server.py` **一字未改**。
>
> 依同條「執行層不得自行評估『這個 `NO_MATCH` 應該無害』」——
> 本包**不對成因作任何判斷**，只列量測值。

---

## 1. §4.1 —— 2.1 完整逐檔表與量測條件

### 1.1 量測條件（逐項）

| 項目 | 實際採用 |
|---|---|
| 掃描範圍 | `features/{amfm,home,sxm,media,projection,privacy}/inputs/` 之全部檔案，**不限副檔名**；排除 dotfile |
| 檔數 | **84**（amfm 16 / home 6 / sxm 15 / media 5 / projection 34 / privacy 8）|
| 對照來源 | `/Users/peihe/Work/` 全樹遞迴，排除 dot 目錄 |
| 比對方法 | **SHA256**（`hashlib`，1 MiB 分塊）。**未以檔名、大小或 mtime 代替**（R15-5）|
| 同名候選蒐集 | 以 basename 索引整棵客戶樹；84 個 inputs 檔去重後 **77 個相異檔名**，客戶樹命中 **208 個候選**，涵蓋 **75 個檔名** |
| 多候選處置 | 對每個 inputs 檔列出**所有**同名候選之 SHA256；命中任一即 `MATCH`，並列出命中者路徑。**未取「最相似」或「最可能」之單一候選作結論** |
| 讀寫模式 | **全程唯讀**。未移動、改名、覆寫、刪除任何 `inputs/` 或客戶樹檔案；未要求任何寫入權限（停手條件 3 未觸發）|

### 1.2 判定計數彙總

| 判定 | 檔數 | 說明 |
|---|---|---|
| `MATCH` | **81** | hash 命中至少一個同名候選 |
| `NO_MATCH` | **1** | 有同名候選，但 hash 全部不符 |
| `NO_COUNTERPART` | **2** | 客戶樹內無同名檔 |
| 合計 | **84** | |

逐 feature：

| feature | 檔數 | MATCH | NO_MATCH | NO_COUNTERPART |
|---|---|---|---|---|
| amfm | 16 | 16 | 0 | 0 |
| home | 6 | 5 | 0 | 1 |
| sxm | 15 | 14 | 0 | 1 |
| media | 5 | 4 | **1** | 0 |
| projection | 34 | 34 | 0 | 0 |
| privacy | 8 | 8 | 0 | 0 |

### 1.3 逐檔表

| feature | 檔名 | inputs SHA256 | 候選數 | 判定 | 命中路徑 |
|---|---|---|---|---|---|
| amfm | `4874049- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | `3fd31f9482b7d660…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/4874049- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls（另 1 個同 hash 副本） |
| amfm | `4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | `55666213fdbef997…` | 6 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls（另 1 個同 hash 副本） |
| amfm | `CIP_Radio_Tables_v6.7.xlsx` | `05e5a1f20763a9fc…` | 7 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/CIP_Radio_Tables_v6.7.xlsx（另 1 個同 hash 副本） |
| amfm | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS024_Radio_20260129.xlsx` | `987cdead37757663…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Radio/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS024_Radio_20260129.xlsx |
| amfm | `FM-WI-SW-RAD-SWRA-A02.xlsx` | `faabdc8ba0409d1a…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Radio/FM-WI-SW-RAD-SWRA-A02.xlsx |
| amfm | `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | `b0827f02c1a0a69b…` | 12 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx（另 1 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_004_General Diagnostic Requirements_SR26_20250909-1658.docx` | `7cebc2fdd29f6644…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_004_General Diagnostic Requirements_SR26_20250909-1658.docx（另 1 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_011_Radio Engineering Mode_SR26_20250909-1658.docx` | `91f9f53d5cbec538…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_011_Radio Engineering Mode_SR26_20250909-1658.docx（另 1 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx` | `5a549719a8c6ac03…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx（另 1 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.doc` | `e1971036b8db918b…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Media/Media/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.doc（另 2 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.docx` | `e5c12e9e0d0f3dd9…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SiriusXM/REF/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.docx（另 1 個同 hash 副本） |
| amfm | `R1LR_Atl-H_25PI3.5_Speech and Personal Assistant_CFTS_28 Voice Recognition_SR26_20250909_1250.docx` | `328a149b7fc14be0…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/R1LR_Atl-H_25PI3.5_Speech and Personal Assistant_CFTS_28 Voice Recognition_SR26_20250909_1250.docx（另 1 個同 hash 副本） |
| amfm | `SR24 R1 Market Configuration Table v1.6.xlsx` | `ae4cf0b929b033ac…` | 7 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/SR24 R1 Market Configuration Table v1.6.xlsx（另 1 個同 hash 副本） |
| amfm | `SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323.xlsx` | `acb0fa0ddeb107ce…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323.xlsx（另 1 個同 hash 副本） |
| amfm | `SYS2_CFTS024_Tuner_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CFTS024_Tuner_V01.xlsx` | `b3e8fcd3fa9638d8…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/SYS2_CFTS024_Tuner_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CFTS024_Tuner_V01.xlsx |
| amfm | `SYS3_AMFM_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_v0.2_20260629.docx` | `679dfc256b6f47a7…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/SYS3_AMFM_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_v0.2_20260629.docx |
| home | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Home_20260720.xlsx` | `0e72b1eca33883ff…` | 0 | **NO_COUNTERPART** | — |
| home | `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx` | `ca6cb06c99213750…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Core HMI/HomeHMI/FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx |
| home | `Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023).pdf` | `a43f8daa4d2df271…` | 4 | **MATCH** | …/01_Project_R1L/Spec/Spec-Core/Core Specifications/SR24/04 - EE Component Requirements/$HMI/Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023).pdf（另 3 個同 hash 副本） |
| home | `Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021).xlsx` | `3b59ba353899d7e0…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Core HMI/HomeHMI/Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021).xlsx（另 1 個同 hash 副本） |
| home | `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | `c144e926fc19df63…` | 12 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx（另 4 個同 hash 副本） |
| home | `SYS1_HMI_Home_Screen_HMI_Logic_and_Flow_R1_SR24_Post_2A_(March_17_2023).xlsx` | `f992e2381f2970d3…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Core HMI/HomeHMI/SYS1_HMI_Home_Screen_HMI_Logic_and_Flow_R1_SR24_Post_2A_(March_17_2023).xlsx（另 2 個同 hash 副本） |
| sxm | `CIP_Radio_Tables_v6.7.xlsx` | `05e5a1f20763a9fc…` | 7 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/CIP_Radio_Tables_v6.7.xlsx（另 1 個同 hash 副本） |
| sxm | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_SXM_20260810.xlsx` | `cd876c202c71e74b…` | 0 | **NO_COUNTERPART** | — |
| sxm | `R1LR Atl-H 25PI3.5-Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1226.reqifz` | `6a5b81a5f8bf9b62…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Sub System/Multimedia Radio and Audio/R1LR Atl-H 25PI3.5-Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1226.reqifz |
| sxm | `R1LR Atl-H 25PI3.5-Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1224.reqifz` | `325dba60d1c91760…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Sub System/Multimedia Radio and Audio/R1LR Atl-H 25PI3.5-Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1224.reqifz |
| sxm | `R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD _SR26_20250909-1852.doc` | `f2004bd79bda6581…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Sub System/Cabin/R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD _SR26_20250909-1852.doc |
| sxm | `R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD_20250910_1124.reqifz` | `c9bbd3b895758502…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Sub System/Cabin/R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD_20250910_1124.reqifz |
| sxm | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx` | `5a549719a8c6ac03…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/AMFM/REF/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.docx（另 1 個同 hash 副本） |
| sxm | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.docx` | `e5c12e9e0d0f3dd9…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SiriusXM/REF/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.docx（另 1 個同 hash 副本） |
| sxm | `SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406.xlsx` | `1f7108ba62f23cdc…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SiriusXM/REF/SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406.xlsx（另 1 個同 hash 副本） |
| sxm | `SX-9845-0526_SOA_360L_Feature_List.xlsx` | `f06ca80600017b38…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SiriusXM/REF/SX-9845-0526_SOA_360L_Feature_List.xlsx（另 1 個同 hash 副本） |
| sxm | `SYS1_HMI_SiriusXM_360L_SAT_Only_HMI Logic and_Flow_R1_SR24_1A(May_24_2021).xlsx` | `05297338c2067e31…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SiriusXM/REF/SYS1_HMI_SiriusXM_360L_SAT_Only_HMI Logic and_Flow_R1_SR24_1A(May_24_2021).xlsx（另 2 個同 hash 副本） |
| sxm | `SYS3_SXM_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_v0.2_20260629.docx` | `9acb9eb2d1de3b6f…` | 2 | **MATCH** | …/02_Project_R1LR/9_ASPICE/03_SYS.3 System Architectural Design/Radio/SYS3_SXM_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_v0.2_20260629.docx |
| sxm | `SiriusXM 360L HMI Logic and Flow R1 Change Log.xlsx` | `cee52353219f2537…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/HMI/SiriusXM 360L HMI Logic and Flow R1 Change Log.xlsx |
| sxm | `SiriusXM 360L HMI Logic and Flow R1.pdf` | `ee6a8efb5f3420cd…` | 1 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/HMI/SiriusXM 360L HMI Logic and Flow R1.pdf |
| sxm | `SiriusXM 360L SAT Only HMI Logic and Flow R1 SR24 1A (May 24 2021).pdf` | `e52c329e801ea08a…` | 7 | **MATCH** | …/01_Project_R1L/Spec/Spec-Core/Core Specifications/SR24/04 - EE Component Requirements/$HMI/SiriusXM 360L SAT Only HMI Logic and Flow R1 SR24 1A (May 24 2021).pdf（另 6 個同 hash 副本） |
| media | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_MediaHMI_20260625.xlsx` | `7d88be94fc03ba38…` | 1 | **NO_MATCH** | — |
| media | `FM-WI-FSM-037-A03-N1L-SWE1-Media-HMI-V0.1 STLA 報告.xlsx` | `a73d78e7dc4ef9a2…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Media/Media/FM-WI-FSM-037-A03-N1L-SWE1-Media-HMI-V0.1 STLA 報告.xlsx |
| media | `Media HMI Logic and Flow R1 SR24 Post 2A (July 25th, 2023).pdf` | `c3d66a7961b564ba…` | 5 | **MATCH** | …/01_Project_R1L/Spec/Spec-Core/Core Specifications/SR24/04 - EE Component Requirements/$HMI/Media HMI Logic and Flow R1 SR24 Post 2A (July 25th, 2023).pdf（另 4 個同 hash 副本） |
| media | `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | `c144e926fc19df63…` | 12 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx（另 4 個同 hash 副本） |
| media | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.doc` | `e1971036b8db918b…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Media/Media/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 024_Specific HU Radio Functions_20250910_1239.doc（另 2 個同 hash 副本） |
| projection | `ATS 8.10 README.rtf` | `03ca0f9eb0e47e69…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/ATS 8.10.0/ATS 8.10 README.rtf |
| projection | `ATS User Guide.pdf` | `0f5797211ba74d1d…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/ATS 8.10.0/ATS User Guide.pdf（另 1 個同 hash 副本） |
| projection | `Accessory Interface Specification CarPlay Addendum R10.docx` | `6fc6d1fcb6b174e0…` | 1 | **MATCH** | …/02_Project_R1LR/9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/Accessory Interface Specification CarPlay Addendum R10.docx |
| projection | `Accessory Interface Specification CarPlay Addendum R10.pdf` | `b8d4d6e1b8add3db…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Bluetooth/REF/Accessory Interface Specification CarPlay Addendum R10.pdf（另 1 個同 hash 副本） |
| projection | `CarPlay Tests 2.19.4 README.rtf` | `302ddb72f6bc85a1…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CarPlay TestApp/CarPlay Tests App Test Files and README/CarPlay Tests 2.19.4 README.rtf |
| projection | `CarPlay Tests User Manual R2.19.4.pdf` | `b0d64ccd78d30a65…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CarPlay TestApp/CarPlay Tests User Manual R2.19.4.pdf |
| projection | `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf` | `cd5bbfbd378ad91e…` | 8 | **MATCH** | …/01_Project_R1L/Spec/Spec-Core/Core Specifications/SR24/04 - EE Component Requirements/$HMI/Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf（另 7 個同 hash 副本） |
| projection | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_SWC_20260708.xlsx` | `134552e815fb71b9…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/SWC/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_SWC_20260708.xlsx |
| projection | `FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA-CPAA_0521.xlsx` | `ad7d0abc148e170a…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA-CPAA_0521.xlsx |
| projection | `HUIG 4.5.pdf` | `4cad660843e3ca98…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Bluetooth/REF/HUIG 4.5.pdf（另 2 個同 hash 副本） |
| projection | `Logical Identifiers and CAN Mapping v1_76.xlsx` | `82e3f3b4aae1f118…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/Logical Identifiers and CAN Mapping v1_76.xlsx |
| projection | `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` | `b16debb7bc609e39…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/NR1L_GEN1(HDCC)_Ver_20260813.xlsx |
| projection | `Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx` | `c92cc3ddda2cd87a…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx（另 2 個同 hash 副本） |
| projection | `PHDCC27_E2A_R1_BHCAN.dbc` | `70aaa730604f4d0a…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/PHDCC27_E2A_R1_BHCAN.dbc（另 1 個同 hash 副本） |
| projection | `PHDCC27_E2A_R1_FDCAN8.dbc` | `706982bcccb86036…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/PHDCC27_E2A_R1_FDCAN8.dbc（另 2 個同 hash 副本） |
| projection | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | 4 | **MATCH** | …/03_Tools/PROXI Tool/NR1L_UDSTool/PROXI_HDCC27_R3_20250424.xlsx（另 3 個同 hash 副本） |
| projection | `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | `c144e926fc19df63…` | 12 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx（另 4 個同 hash 副本） |
| projection | `Projection Device HMI Change Log R1 SR24 Post 2A (May 3 2023).xlsx` | `61338e3be17a2760…` | 3 | **MATCH** | …/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/HMI/Projection Device HMI Change Log R1 SR24 Post 2A (May 3 2023).xlsx |
| projection | `Projection Device HMI Logic and Flow R1 SR24 Post 2A (May 3 2023).pdf` | `36e585c300517d37…` | 3 | **MATCH** | …/01_Project_R1L/Spec/Spec-Core/Core Specifications/SR24/04 - EE Component Requirements/$HMI/Projection Device HMI Logic and Flow R1 SR24 Post 2A (May 3 2023).pdf（另 2 個同 hash 副本） |
| projection | `Projection Device R1L-R HMI Logic and Flow (February 5 2026).pdf` | `edc1e4d676471130…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/Projection Device R1L-R HMI Logic and Flow (February 5 2026).pdf（另 3 個同 hash 副本） |
| projection | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.doc` | `8fef8da9809f77f6…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.doc（另 1 個同 hash 副本） |
| projection | `R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.doc` | `9417aa715c7a5b2e…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.doc（另 1 個同 hash 副本） |
| projection | `R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.docx` | `4b20abf4860d394e…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.docx |
| projection | `SWE1_PROJ_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_MD20260324.xlsx` | `2f836a27029a17dc…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/SWE1_PROJ_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_MD20260324.xlsx（另 1 個同 hash 副本） |
| projection | `SYS1_Accessory Interface Specification CarPlay Addendum R10.xlsx` | `5665820f1889cf44…` | 1 | **MATCH** | …/02_Project_R1LR/9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/SYS1_Accessory Interface Specification CarPlay Addendum R10.xlsx |
| projection | `SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023).xlsx` | `4b351960a55eae92…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023).xlsx（另 1 個同 hash 副本） |
| projection | `SYS1_HMI_Projection_Device_HMI _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx` | `530274f8c0afed9a…` | 1 | **MATCH** | …/02_Project_R1LR/9_ASPICE/01_SYS.1 Requirement Elicitation/SYS1_HMI/Archive/SYS1_HMI_Projection_Device_HMI _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx |
| projection | `SYS1_HMI_Projection_Device_R1L-R_HMI_Logic_and_Flow_(February_5_2026).xlsx` | `d88b1072f18f2c9d…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/SYS1_HMI_Projection_Device_R1L-R_HMI_Logic_and_Flow_(February_5_2026).xlsx |
| projection | `SYS1_HUIG4.5.xlsx` | `5df67a2a4565e9cc…` | 1 | **MATCH** | …/02_Project_R1LR/9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/SYS1_HUIG4.5.xlsx |
| projection | `SYS2_CFTS085_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CFTS085_V01.xlsx` | `ea7f4953e7bfe2b6…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/SYS2_CFTS085_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CFTS085_V01.xlsx（另 1 個同 hash 副本） |
| projection | `SYS2_CP.R10_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CP.R10_V01.xlsx` | `60a71a7a0d05c125…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/SYS2_CP.R10_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CP.R10_V01.xlsx（另 2 個同 hash 副本） |
| projection | `SYS2_HUIG_4_5_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_HUIG_4_5_V01.xlsx` | `659202c10947c800…` | 4 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/DeviceManager/REF/SYS2_HUIG_4_5_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_HUIG_4_5_V01.xlsx（另 3 個同 hash 副本） |
| projection | `SYS3_PROJ_FM-WI-FSM-011-A01 Xi Tong Jia Gou She Ji  System Architectural Design_SYSAD.docx` | `29ffc7c818aa09f7…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/REF/SYS3_PROJ_FM-WI-FSM-011-A01 Xi Tong Jia Gou She Ji  System Architectural Design_SYSAD.docx（另 1 個同 hash 副本） |
| projection | `pcts_verifier_release_signed - 922397802.apk` | `dd7b26a6a4cd14ce…` | 1 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/PCTS/pcts_verifier_release_signed - 922397802.apk |
| privacy | `Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx` | `c54f700f81c4c70e…` | 3 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx（另 1 個同 hash 副本） |
| privacy | `Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx` | `49dd3c31405fb0c3…` | 7 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx（另 1 個同 hash 副本） |
| privacy | `Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx` | `d5813bb7ccd6f721…` | 7 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx（另 1 個同 hash 副本） |
| privacy | `CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx` | `f46d15ca29b6a75d…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx |
| privacy | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx` | `cd876c202c71e74b…` | 2 | **MATCH** | …/02_Project_R1LR/9_ASPICE/SWE.6 Software Validation/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx |
| privacy | `R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx` | `5eb0dd739f002fe0…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx（另 1 個同 hash 副本） |
| privacy | `SWE1_CFTS_022-Privacy_Features.xlsx` | `190e6f3ebaee5fe7…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/SWE1_CFTS_022-Privacy_Features.xlsx |
| privacy | `SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` | `e534afa55710547f…` | 2 | **MATCH** | …/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx |


---

## 2. §4.2 —— `NO_MATCH` 與 `NO_COUNTERPART` 逐檔說明

### 2.1 `NO_MATCH`（1 件）—— Media 之 FW036 工作簿

| | 值 |
|---|---|
| `inputs/` 路徑 | `features/media/inputs/FM-WI-FSM-036-A01 …_SWQT_MediaHMI_20260625.xlsx` |
| `inputs/` SHA256 | `7d88be94fc03…` |
| 客戶樹候選數 | **1** |
| 候選路徑 | `…/02_Project_R1LR/10_Reviewing/00_TestCase/Media/Media/FM-WI-FSM-036-A01 …_SWQT_MediaHMI_20260625.xlsx` |
| 候選 SHA256 | `e39bc0ce07f6…` |

**補充量測（唯讀，供裁定用）**：

| | 客戶樹候選 | `inputs/` 這份 |
|---|---|---|
| bytes | 319,910 | 330,660 |
| zip members | 51 | **51** |
| classic DV / x14 DV | 4 / 2 | **4 / 2** |
| 相對候選 lost / added | — | **0 / 0** |

分頁逐格比對（10 個分頁）：

| 分頁 | 列數 | cell 差異 |
|---|---|---|
| `Test Case Specification 測試用例規範` | 755 → 755 | **5,682** |
| 其餘 9 個分頁 | 不變 | **0** |

首處差異：`D333` `'SWE1-MEDIA-PLA-062-01'` → `'SWE1-MEDIA-PLA-062'`。

**成因不判定。** 依 §3.1，執行層不得推斷原因。可陳述者僅為：
zip 成員集合與 DV 計數**與候選完全一致**（0 lost / 0 added、4/2 對 4/2），
因此**這一個特定機制**（openpyxl 存檔路徑之容器破壞，其指紋為成員遺失）
與本次差異的形態不符。這排除的是一個機制，**不是**「無害」——
差異集中在 TC 分頁的 5,682 格資料上，那正是內容層，而內容層的差異
是否可接受、由誰造成、哪一份才是基準，皆非執行層可裁。

**對停手條件之影響**：§3.1 之條件文字為「出現任一 `NO_MATCH`」，
不以成因或嚴重性為條件。故無論上述補充量測如何，2.3 一律停止。

### 2.2 `NO_COUNTERPART`（2 件）—— 皆為 FW036 工作簿，客戶樹內無同名檔

| feature | 檔名 | `inputs/` SHA256 | 同名候選數 |
|---|---|---|---|
| home | `…_SWQT_Home_20260720.xlsx` | `0e72b1eca338…` | **0** |
| sxm | `…_SWQT_SXM_20260810.xlsx` | `cd876c202c71…` | **0** |

**SXM 那份值得單獨指出**：其 SHA256 `cd876c202c71…` 與
`features/privacy/inputs/` 的 FW036 **空白範本**（`…_SWQT_20260121.xlsx`，
下放包 00 記載之 `cd876c202c71e74b…`）**完全相同**。
即 SXM 的 `inputs/` 工作簿就是那份通用空白範本，只是以 feature 名重新命名 ——
與 SXM 之 `workbook_state = BLANK` 一致。客戶樹內之所以查無同名檔，
是因為原檔在客戶樹裡叫 `…_SWQT_20260121.xlsx`（位於
`9_ASPICE/SWE.6 Software Validation/`），檔名不同故 basename 索引不命中。

Home 那份同理為「客戶樹內無同名檔」，本包**未再往下追**其對應來源
—— 追蹤改名後的對應關係需要跨檔名比對全樹 hash，屬另一項量測，
不在本包範圍。**照實登記為 `NO_COUNTERPART`，未推斷。**

**方法學上的限制須明說**：本次比對以 **basename 索引**建立候選集。
`NO_COUNTERPART` 的語意因此嚴格為「客戶樹內無**同名**檔」，
**不等於**「客戶樹內無對應檔」。SXM 那件即為反例 —— 對應檔存在，
只是改了名。若分析層要的是「有無對應」而非「有無同名對應」，
需改以全樹 hash 反查，是另一次量測。

---

## 3. §4.3 —— 2.2 之清單現況

`tests/test_single_write_path.py` 之 `KNOWN_VIOLATIONS`（R20-2 ratchet，
只減不增）現況 **7 個檔案 / 11 個呼叫點**：

| 檔案 | 呼叫數 | 行號 | status | 性質 |
|---|---|---|---|---|
| `features/home/scripts/write_back.py` | 1 | 475 | `QUARANTINED` | 交付件產出（Home），R18-1 凍結 |
| `features/sxm/scripts/write_back.py` | 1 | 478 | `QUARANTINED` | 交付件產出（SXM），R18-1 凍結 |
| `features/media/scripts/write_back.py` | 1 | 349 | `QUARANTINED` | 交付件產出（Media），交付件狀態**未量** |
| `features/projection/scripts/writeback.py` | 1 | 290 | `QUARANTINED` | 交付件產出（Projection）|
| `backend/writer.py` | 4 | 363/404/468/487 | `ACTIVE` | app 寫回主路徑 |
| `backend/api_server.py` | 2 | 2370/2410 | **`HAZARD`** | 2370 匯出下載（ACTIVE）；**2410 見下** |
| `scripts/translate_xlsx.py` | 1 | 303 | `ACTIVE` | 翻譯後工作簿產出 |

`api_server.py:2410` 之 `HAZARD` 說明（R21-2 逐字）：

> overwrites the source file in place; destroys the baseline that all
> structural comparisons depend on, not merely the output

並補一句本 repo 的具體暴露面：AMFM 21/10、Home 14/10、SXM 11/10
這三組結構結論，全部是對著這條路徑可以無聲改寫的檔案量出來的。

**行號說明**：測試比對的是**每檔呼叫數**而非行號，行號僅為文件。
理由是 R20-3 的封存標頭本身就使四支腳本行號位移 6 列 —— 若以行號為判準，
加標頭當場就會讓測試誤報。因此作業順序也對調為「先加標頭、再入庫測試」。

---

## 4. §4.4 —— 2.3 之變更與測試結果

**未執行。** 停手條件 1 觸發（§3.1），`backend/api_server.py` 一字未改，
亦未新增「呼叫後 `source_path` 之 SHA256 不變」之測試（該測試是變更的
配套，變更未做則測試無標的）。

已完成之測試現況：

```
tests/test_single_write_path.py ....                    4 passed
全套                                                     959 passed
```

四項為：新增呼叫點即 FAIL、清單陳舊即 FAIL（只減不增之雙向約束）、
白名單與 `pixmap.save` 不誤判之陽性對照、每筆清單項須有 nature 與 status。

**待 2.3 解禁後應一併補的兩件事**（不在本包執行）：

1. 變更後自 `KNOWN_VIOLATIONS` 移除 `2410` 之 `HAZARD` 標記，
   但 `backend/api_server.py` 該項**不得自清單移除**（R21-3：其 openpyxl
   存檔缺陷未解，`calls` 由 2 保持 2，僅 status 由 `HAZARD` 降為 `ACTIVE`）
2. 補「呼叫後 `source_path` 之 SHA256 不變」之測試（07 包 §2.3 末項）

---

## 5. §4.5 —— 為 Pei 準備之 commit message（未執行）

```
feat(writer): ratchet the single-write-path rule; audit input baselines

R20-2 lands the guard without waiting for a clean repo: the 11 existing
openpyxl save call sites are grandfathered by file and count, and the test
fails on the 12th. The baseline only shrinks — a stale entry fails as
loudly as a new call site.

- add tests/test_single_write_path.py (AST-based, so pixmap.save and
  python-docx document.save cannot masquerade as violations)
- quarantine the four feature write_back scripts per R20-3: header only,
  no rewrite, no program-level guard
- record R20, R21, and backfilled R17 in RULINGS.md
- register Media A-034: script quarantined, artefact state UNMEASURED
- mark api_server.py:2410 HAZARD — it overwrites the source file, not
  just the output

R21-1 baseline audit (read-only, SHA256, all same-name candidates listed):
84 input files across six features — 81 MATCH, 2 NO_COUNTERPART,
1 NO_MATCH (features/media FW036 workbook). Per stop condition 1 the
api_server.py:2410 fix is NOT applied and no production code was touched.
```

---

## 6. §4.6 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。**

1. **`NO_COUNTERPART` 的語意被 basename 索引限縮，兩件都沒真正追到底。**
   §2.2 已說明：SXM 那件證明了「無同名檔」不等於「無對應檔」。
   Home 那件目前是未知 —— 可能同樣是改名，也可能是別的。要回答
   「客戶樹裡到底有沒有這份檔的來源」，需要**全樹 hash 反查**
   （對整棵客戶樹計 hash 建反向索引），那是一次完全不同量級的量測，
   本包未做。**在做之前，不能說 Home / SXM 的 inputs 已驗明來源。**

2. **稽核只證明「現在相符」，不證明「從未被覆寫」。** 81 個 `MATCH`
   說的是此刻 hash 相同。若 `api_server.py:2410` 曾覆寫某個 `inputs/` 檔，
   而該檔隨後又被人從客戶樹重新複製一次，稽核會顯示 `MATCH`。
   要排除這種情形需要 mtime／檔案系統事件／備份比對，皆非本包範圍。
   **這一點對停手條件的判讀有直接影響**：稽核「乾淨」不等於危害從未發生。

3. **客戶樹的掃描範圍未加限定。** 我掃了 `/Users/peihe/Work/` 全樹並以
   basename 命中，208 個候選散布在多個專案目錄（含 `01_Project_R1L`
   等非 R1LR 專案）。同名檔跨專案存在時，`MATCH` 可能命中的是**別的專案**
   的同名檔。逐檔表已列出命中路徑供核對，但**我沒有逐筆確認命中路徑
   是否屬於正確的專案樹**。84 筆全查一次是可行的，但屬另一輪作業。

4. **Media 那筆 `NO_MATCH` 的 5,682 格差異未做分類。** 只取了首處差異
   （`D333` 的 req id 少了 `-01` 後綴）。這 5,682 格是集中在少數欄、
   還是散布全表？是系統性的 id 改寫、還是實質內容重寫？沒有分析。
   §3.1 禁止的是「評估無害」，不禁止描述差異的形狀 —— 但那需要時間，
   且分類方式本身會暗示成因，我選擇停在原始量測，把判斷留給裁定。

5. **`translate_xlsx.py` 與 `api_server.py:2370` 的產出是否為交付件，
   從未被裁定過。** 兩者都在 `KNOWN_VIOLATIONS` 裡標 `ACTIVE`，
   是我依「產出會交到人手上」推定的。若分析層認為翻譯稿或匯出下載
   不算交付件，它們應該進白名單而非既存違規清單 —— 兩者的差別在於
   前者永久豁免、後者是待清償的債。**這個分類我是自己下的，未經裁定。**
