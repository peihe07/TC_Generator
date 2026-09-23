# Test Case Framework — FW036 Camera

本檔為 `docs/fw036/framework.md` 之 **Part VIII**，依 CAM-04 §1(e)（Pei 2026-09-16）
自全域檔整段搬入；全域檔原處留一行指標。條號與內文逐字未改。
process canon 仍為 `docs/fw036/FEATURE_ONBOARDING.md`。

---
## Part VIII — Camera (two books: SWRA Service + RVC-HMI)

**狀態：已簽核並鎖定。** Pei 於 2026-09-16 簽核（CAM-02 審閱 §三-5，Tier 2）。
**重開一次（Tier 2，Pei 2026-09-23，下放包 CAM-06 §1）**：A 本 Layer 2 加第 10 組
`Auxiliary Cameras`（9 → 10 組），`SWE-CAM-017` 自 `State Handling` 改歸該組。
重開前 sha16 `c4fc9d2e5b7d1f44`，重開後 sha16 `ee74d26960d6c281`
（量測法：本檔全文，但本行之該欄位以 16 個 `0` 代入後取 sha256 前 16 碼 —— 自指之故）。
重開範圍僅及 VIII.2 之組表與本狀態行；VIII.3～VIII.8 未動。

```
Layer 1  `Rear View Camera`（R-CAM4(a)）
Layer 2  A 本 10 組 25／B 本 8 組 230；未歸屬 0、歧義 0（A 本第 10 組為 CAM-06 重開所增）
Layer 3  A 本 = VF 章節號（V4 依 R-CAM7）＋ CFTS092 §1.3.x；B 本 = SYS1 Outline Number（RVC+PAM 依 R-CAM6）
```

簽核**不涵蓋**：TC 內容（pilot review）、`-023` 交集承接之實測結果、未結 DR。
重開條件同 `vehicle_setting` 之例；重開屬 Tier 2（Pei）。

Ruled by Pei 2026-09-16：feature 名 `Camera`、目錄 slug `camera`（CAM-01 §4 任務 1）；
workbook Test Group 值 **`Rear View Camera`**，A、B 兩本同值（**R-CAM4(a)**）。
TC ID 分兩組序號：A 本 `NR1L-RVC-{nnn}`、B 本 `NR1L-RVCHMI-{nnn}`，
各自自 001 起連號（**R-CAM4(b)**）；交叉參考索引以 SWE ID 互指，
不以 TC ID 互指（**R-CAM4(c)**）。

本 Part 之特殊性：**單一 feature 出兩本工作簿**（R-CAM1(a)），A 本先、B 本後，
兩本互為步驟來源 —— A 本之畫面入口／設定 hop 引 B 本之 SYS1 匯出，
B 本之訊號／PROXI 前提沿用 A 本已定之寫法（R-CAM1(b)）；
追溯各歸各母體，互參只參考寫法，不複製對方之 `spec_reference`（R-CAM1(c)）。

RD source：
- **A 本**（Service 層，25 leaf，`SWE-CAM-001…025`）——
  `SWE1_CAMERA_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_V02.xlsx`
  （doc_id `camera_037_swra_v02`，sha16 `cae0df17016b3532`）。
- **B 本**（HMI 層，230 列 ＝ 203 leaf ＋ 27 umbrella，`SWE1-RVC-001…159` 含 `-NN-nn` 子項）——
  `FM-WI-FSM-037-A03-N1L-SWE1-RVC-HMI-V0.1 STLA 報告.xlsx`
  （doc_id `camera_037_rvc_hmi_v0_1`，sha16 `6d5812a03da1d148`）。

spec_mode **A**（`intake.py` 判定：SYS1 spec export present, no PDF）。
執行計畫 `features/camera/RUNBOOK.md`；rulings `features/camera/RULINGS.md`
（R-CAM1–R-CAM9）；anomalies 同目錄 `ANOMALIES.md`（A-CA01–A-CA20）。
profile `docs/runtime/profiles/FW036_R1L_Camera_Profile.md`。

**Workbook state**: 未投遞（CAM-01／CAM-02 止於 Phase 0–2）。

### VIII.1 Layer 1 — Test Group

`Rear View Camera` —— A、B 兩本同值（R-CAM4(a)，R-VF9 前例形制）。

B 本 037 標題作 `SWE1-RVC-HMI`；依 PH-01 R-PH 前例，`HMI` 為文件類別尾綴，
不入 Test Group。CAM-01 曾提 `Camera`、審閱曾提以 `Camera` 定案，
**兩者皆經 Pei 改為 `Rear View Camera`**。

### VIII.2 Layer 2 — A 本（Service 層，25 leaf）

Sub Categorization ∩ VF 章節之交集。**十組**（CAM-06 重開），**實測 25/25、未歸屬 0**
（逐列 `features/camera/data/layer2_assign.tsv`，`book` 欄 = `A`）。

| # | Test Set | SWE-CAM | Sub Cat | leaf | 主要 VF 章 |
|---:|---|---|---|---:|---|
| 1 | `Startup and Shutdown` | 001, 012, 014 | Daemon／NCD HAL | 3 | V33 1.11.1.2、V2 1.14.1、V3 1.10.2 |
| 2 | `Configuration` | 002, 005 | Daemon／EVS HAL | 2 | V2 1.13.1、V3 1.10.2.1、V42 1.11.2.1 |
| 3 | `State Handling` | 003 | Daemon | 1 | V42 1.11.1.2 |
| 4 | `Diagnostics` | 004, 013 | Daemon／NCD HAL | 2 | V2 1.10.2.1、V42 1.13.2.1.2.0.x |
| 5 | `LVDS Messaging` | 007, 008, 009, 010, 011 | NCD HAL | 5 | V2 1.13.1、V2 1.10.3.2、V42 1.11.2.1 |
| 6 | `Video Pipeline` | 006, 019 | EVS HAL／Daemon | 2 | V42 1.11.1.2.0.3.2、V33 1.11.1.2.2 |
| 7 | `Display Arbitration` | 015, 016, 018, 020 | Daemon／App | 4 | V2 1.13.2.1.x、V3 1.10.2.2/3、CFTS092 §1.3.6 |
| 8 | `HMI Overlays` | 021, 022, 023, 025 | App | 4 | V2 1.13.2.1.4～8、V2 1.13.2.2.x |
| 9 | `AUX Camera` | 024 | App | 1 | VF617_V5（**缺件，DR-CAM-a**）|
| 10 | `Auxiliary Cameras` | 017 | Daemon | 1 | CFTS092 §1.3.5／§1.3.7／§1.3.8／§1.3.9 |
| | **合計** | | | **25** | |

25 列之 `Categorization` 實測全為 `Functional Requirement`（無 Heading 列），
故 leaf ＝ 列。

註：
- ~~`-017` 依其 Description（`CameraDisplaySts`）歸 `State Handling`；其 VC/VM
  講 Air Suspension PROXI 與 4X→1X reset，與描述不對齊（**A-CA03**），
  RD 對齊後可能改歸 `HMI Overlays`。~~
  **CAM-06 重開改歸 `Auxiliary Cameras`** —— `-017` 之 `CameraDisplaySts` 條文
  （CFTS092 `SYS-RA-CAM-097`／`-098`）位於 Forward Facing 節（§1.3.8），
  與新組之 Layer 3 對齊；VC/VM 錯位之 A-CA03 不因重開而結，改登 RDF-02。
- **第 10 組 `Auxiliary Cameras` 之 Test Set 值不只由 `-017` 產出** ——
  依 **R-CAM13(c)**，他列（現為 `SWE-CAM-016`）所引之 Cargo/CHMSL、Surround View、
  Forward Facing 節條文，其 TC 之 `Test Set` 亦寫 `Auxiliary Cameras`，
  而該 SWE 列於本表仍歸其原組（`-016` 仍在 `Display Arbitration`）。
  本表之「組 ↔ SWE 列」對應與「TC ↔ Test Set」對應於此分離，為本 feature 之唯一例外。
- `AUX Camera` 為單列 Test Set，屬 §4.2「genuine outlier」，且**全數待 DR-CAM-a**
  （12/12 來源皆 `VF617_V5`，不可解析）。
- `-014` 之 Sub Cat 為 `NormalCameraDaemon` 而 Description 以「NCD HAL shall…」
  起首（**A-CA08**）；本表依 `I` 欄逐字歸類。

### VIII.3 Layer 2 — B 本（HMI 層，230 列）

依 CAM-01 審閱 §四之修訂案重切（CAM-01 §5 之原八組表作廢）。
**實測 230/230、未歸屬 0、歧義 0**，與修訂案逐組全合。

| # | Test Set | 章節（逐字前綴）| 列 | leaf | umbrella |
|---:|---|---|---:|---:|---:|
| 1 | `PAM Integration` | RVC+PAM 6.2(5)、6.3(1)、6.4(1)、6.5(1)、8.8(1)、11.1(1) | 10 | 9 | 1 |
| 2 | `Activation and Exit` | HU 6.1(4)、6.5(6)、6.7(5)、6.10(1)；RVC+PAM 7.1(3)、7.2(7)、7.3(4)、7.4(5)、7.5(7)、8.1(6)、8.6(1)、8.7(1) | 50 | 43 | 7 |
| 3 | `Camera Settings` | HU 6.2(5) | 5 | 4 | 1 |
| 4 | `Warning Banners` | RVC+PAM 8.2(1)、8.3(4)、8.4(4)、9.2(4) | 13 | 12 | 1 |
| 5 | `AUX Camera Access` | HU 27.1–27.8(41)、34.1(5)、34.3(1)、34.4(3)、34.6(4)、34.7(4)、34.8(4) | 62 | 60 | 2 |
| 6 | `Camera View Switching` | HU 28.1(1)、28.2(4)、28.3(4)、28.4(2)、28.6(2)、28.7(14)、28.8(4) | 31 | 25 | 6 |
| 7 | `Wireless Camera Pairing` | HU 33.1(5)、33.2(1) | 6 | 5 | 1 |
| 8 | `AUX Camera Settings` | HU 29.1(6)、29.2(7)、30.1(11)、31.1(12)、34.9(14)、34.10(3) | 53 | 45 | 8 |
| | **合計** | | **230** | **203** | **27** |

**HU 章 1／3／4／18–22／26／32 不入** —— B 本 230 列一列未引（**A-CA12**）。
CAM-01 §5 草案所設之 `Camera App`（HU 18–22）因而**撤組**（實測 0 列）。
`Camera View Switching`（HU 28）為審閱新設，其 setup 型態與 `AUX Camera Access`
不同（More Cams／More AUX 之切換 vs 進入 AUX）。
`Wireless Camera Pairing` 6 列為 genuine outlier（pairing 流程之 setup 與其餘
AUX 組皆異）。

umbrella 27 列即 B 本 `Sub Categorization` 欄為空之列（`Categorization` = `Heading`），
不出 TC，於覆蓋台帳標 `No TC — Heading; refer to child IDs`（bed_lowering
R-BLM2／popup R-POP5 前例形制）。

### VIII.4 Layer 3 — spec 章節

**不入工作簿**（§4.1.5）。

- **A 本** —— 以 SYS2 `VF章節`(I) 欄逐字為 Layer 3；跨 VF 家族之同章節依平台
  分列（R-CAM3）。CFTS092 來源（33 列）該欄全空，改以 §1.3.x 章名
  （`Cargo/CHMSL Camera`／`Rear Camera`／`Surround View Camera`／
  `Forward Facing Camera`／`Vehicle Camera App`）。
  **VF551_V4 之 I 欄 321/321 全空**（A-CA02），依 **R-CAM7** 取 `Description`(D) 欄
  前導章節號（60 個 heading 列）向下繼承 —— 321/321 覆蓋、60 個相異章節；
  A 本實際引用之 44 列 V4 全落 5 章（`1.10`／`1.10.2`／`1.10.2.1`／
  `1.10.2.2`／`1.10.2.3`）。逐列 `features/camera/data/layer3_a_vf_chapters.tsv`。
- **B 本** —— 以 SYS1 `Outline Number` 逐字為 Layer 3；B 本 `HMI Source ID`
  已內建該號。母體：HeadUnitCameraSystems 取 `spec-index/cache/` 本
  （sha16 `0df5da9186d761e3`，1044 列）；RVC+PAM 依 **R-CAM6** 取
  `spec-index/cache/` 本（sha16 `1a0bef53c6de975c`，64 列）。
  **對映率 100.00%（230/230）**。以 REF 本（`5a1c0ab24991dcb1`，55 列）為母體
  則為 98.70% —— `SWE1-RVC-016`／`-017`／`-018` 所引之 `7.3.1`–`7.3.3`
  只存在於 cache 本（A-CA14）。

### VIII.5 軸（§8.3 sibling 軸，非層）

| 軸 | 判準 | 條文 |
|---|---|---|
| 車型軸（**外層**）| PROXI 前提值／觸發訊號名（Atl-Hi vs Atl-Mi）／ER 可觀察結果任一因車型而異即拆 | R-CAM3 |
| 品牌軸 | hop label 因品牌而異即拆；Pre-Conditions 首行寫明品牌 | R-CAM5(b) |

二軸同時成立時以車型軸為外層（R-CAM5(d)）。
`Vehicle Model` 七欄以 `1`／`0` 填寫，`Commander (598)`／`Regengade (5210)`
一律 `0`（R-CAM2）；lint `Z` 施檢（profile §2）。

品牌軸於本 feature 實際**只有兩分支**（RAM 系 vs 其餘）—— 見 profile §3.2；
其來源為 PROXI `Brand_Configuration_2` 之實測，R-CAM5(c) 所指定之
`SR24 R1 Market Configuration Table v1.6.xlsx` 查無此對照（DR-CAM-e）。

### VIII.6 交叉參考索引 — `SWE-CAM ↔ SWE1-RVC`

逐列 `features/camera/data/crossref_a_b.tsv`（68 筆，含 `relation`／`status`／
`verdict_reason` 三欄）。核對準則：`same-point`（同一驗證點）與
`precondition-or-hop`（非同一驗證點但為該 A 列之前置或導航 hop 之逐字來源）
判 `[VERIFIED]`，其餘 `[REJECTED]`。

| A 本 | B 本（配對範圍）| 依據 | `[VERIFIED]` | `[REJECTED]` |
|---|---|---|---:|---:|
| `-015` | `RVC-008`, `-019`, `-020`～`-023`, `-045` | reverse 進出與 Delay | 7 | 0 |
| `-018` | 同上 | 同上 | 7 | 0 |
| `-016` | `RVC-048`, `-050`, `-051` | 手動入口 | 3 | 0 |
| `-021` | `RVC-026`～`-031` | banner／overlay | 4 | 2 |
| `-023` | `RVC-026`～`-031` | banner／overlay | 4 | 2 |
| `-024` | `RVC-053`～`-062`, `-084`～`-108` | AUX | 26 | 9 |
| `-025` | `RVC-036`～`-039` | fault banner | 2 | 2 |
| | **合計** | | **53** | **15** |

`[REJECTED]` 15 筆之成因分三類：**退出／delay 行為被誤配到疊層列**
（`-021`／`-023` × `RVC-029`／`-030`，4 筆）、**純交叉引用列無可驗證行為**
（`RVC-086`／`-091`／`-102`，3 筆）、**跨線誤配**（配對線 `RVC-057`／`-058`、
lockout `RVC-056`、影像編輯線 `RVC-103`～`-105`、訊息不同之
`RVC-037`／`-038`，8 筆）。

B 本 230 列中被 A 本任一列配對者 **55**，**未配對 175 列**
（`features/camera/data/crossref_b_unpaired.tsv`）—— 即 B 本之獨有範圍，
供 Phase 3 判「B 本獨有」之依據。

### VIII.7 已知異常與未決

- **DR-CAM-a（高）**：`VF617_V5` 缺件 —— A 本 119 個來源引用不可追，
  `SWE-CAM-024` 整組 BLOCKED。
- `SWE-CAM-023` 與 6 列有來源交集（A-CA07）；依 §8.2.1 以 037 為準不合併，
  每組交集之來源只由一列承接、reasoning 註明委派，**承接順位待 framework
  鎖定時定**（審閱 §三-10）。
- `Out of Scope` 之 32 個來源不作 `spec_reference` 錨（**R-CAM9**）；
  其中 `SYS-RA-VF551_V2-578`／`-580` 得作 `-010`／`-017`／`-023` 之
  Pre-Condition 措辭來源，reasoning 註明出處。
- A-CA19（Abarth 無 Brand-Specific 欄）、A-CA20（`-025` 之畫面文字兩側不一致）
  待裁。

### VIII.8 Workbook sync

Test Group `Rear View Camera` 與本 Part 之 Test Set 值寫入每一生成列之 G／H 欄
（兩本皆然）。`Vehicle Model` 七欄（T–Z）逐列填 `1`／`0`（R-CAM2）。

**寫回一律走 `backend/xlsx_surgical.py`**（R-G3 全域；母本 R 欄 design_method
下拉為 x14 擴充，openpyxl 存回即摧毀且損壞為選擇性）。
