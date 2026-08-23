# 61 — VF230 進場（Part 2）：裁決落檔、素材清冊、P0/P1 指示

下放包 NN=61。對應上繳：`docs/upstream/61_vf230_intake.md`。
本包新增 **R-VS59–R-VS62**（4 條）、**W-102–W-107**（6 項工單）、**DR-27**（1 件草稿）。

---

## 1. 背景

Vehicle Setting Part 2 = **VF230**。素材根目錄：

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/VF230_V1_R5
```

Pei 已裁定 **併入既有 `features/vehicle_setting/`**，不另開 feature slug。
本包為 VF230 之 P0 進場，不動 Part 1（CFTS044）之任何既有交付內容。

---

## 2. 分析層實測（2026-08-23）

### 2.1 VF230 素材清冊

**量測條件**：`Filesystem:list_directory_with_sizes` 對上列根目錄一層，
含 `.DS_Store`；不遞迴（`output/` 另計）。

| 類別 | 數 | 備註 |
|---|---:|---|
| `FM-WI-FSM-037-A03*.xlsx` | **11** | 分報告，檔名見 §5.1 |
| `FM-WI-FSM-036-A01*.xlsx` | 1 | `..._SWQT_VF230_20260819.xlsx`，80.53 KB |
| spec | 1 | `C-VF230_V1_R5_PDT27.doc` —— **`.doc` 非 `.docx`** |
| SYSAD | 1 | `SYS3_Vehicle_Settings_..._SYSAD_v1.0.docx`，15.92 MB；與 `CFTS044/REF/` 內**同名**，**未比對 hash** |
| `output/`（Pei 先前整理） | 3 | 見 §2.4 |

`VF230_V1_R5/` 內**無 `REF/` 子目錄**（CFTS044 有）。

### 2.2 VF230 之 036 workbook 狀態

**量測條件**：`openpyxl`（`read_only=True, data_only=True`），
分頁 `Test Case Specification 測試用例規範`，表頭列 9，掃描列 10–246（237 列），
判準為「該列任一儲存格非空」。

```
非空資料列 = 0 / 237
```

表頭列 9 之 34 欄（B–AH）與 CFTS044 **逐欄相同**。

→ `workbook_state: BLANK`（真空白，非「預填但無 TC 內容」）。

`Cover 封面`：版本 `C`，核准者 `劉安哲 AllenACLiu`，審查者 `張愷霏 ErinKFChang`，
作者欄空。`Product Document 記錄封面頁`：專案代號 `NR1L`，版本 `V1.0`，
修訂歷史僅一列 `V1.0 / Initial Release 初版發布 / 2026-08-10`。
`Test Case Framework` 分頁 max_row=1（空）。

### 2.3 CFTS044 交付路徑上之 036 狀態（續號基準）

**量測條件**：同上，對
`.../Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 ..._SWQT_CFTS044_Vehicle Controls_20260819.xlsx`，
列 10–246，逐欄計「非空儲存格數」。

```
B  序號              237        L  測試程序        191
D  需求/設計 ID      237        M  預期結果        191
H  Test Set          237        其餘 27 欄        0
I  Test Item         237
N  規格參考          237
```

**歸零欄含 F（Test Case ID）、G（Test Group）、O（TC Ref ID）、
P（Priority）、R（Design Method）、AA（Author）、AH（Remarks）。**

末列 246：`B = 237`，`D = SWE1-VC-StopStartSystemBehavior-056`，
`H = Stop Start System Behavior`。

**推論（非量測）**：Part 1 之產出尚未 `--write` 回寫至交付路徑，與 PLAYBOOK
§6「P7 未完成」一致。**本包不據此更動 Part 1 之任何狀態。**

### 2.4 `output/` 之定位

Pei 已裁定：該三檔為**其先前自行整理之 VF230 項目彙整**，
非本 pipeline 產物。

```
output/fw036_vf230_from_fw037_functional_requirements.xlsx        201.49 KB
output/fw036_vf230_from_fw037_functional_requirements_audit.csv   644.53 KB
output/validation/fw036_vf230_from_fw037_functional_requirements.xlsx  163.23 KB
```

---

## 3. 本包之新條文（Pei 裁定 2026-08-23）

### R-VS59 —— VF230 之 B 欄序號自 238 起

```
R-VS59（VF230 序號基準，Pei 裁定 2026-08-23）

VF230 之 036 workbook，B 欄「No.#/序號」自 **238** 起連續遞增，
不自 1 起。

基準來源：CFTS044 交付路徑之 036，列 10–246，B 欄末值 = 237（實測，61 包 §2.3）。

配套約束：
1. B 欄自此進入寫回範圍。`feature.yaml` 之 `workbook.columns` 需新增
   `seq: "B"`，且該映射**僅對 VF230 之 workbook 生效**。
2. **CFTS044 之 B 欄（1–237）為凍結欄**，任何寫回不得觸及。
3. 續號為跨 workbook 之連續序號：VF230 之 B 欄末值 = 237 + VF230 列數。
   該末值於上繳時具名回報。
4. F 欄「Test Case ID」兩本 workbook 皆為 0 filled；R-VS59 **不**新增
   TC ID 之產出，F 欄維持不寫。
```

### R-VS60 —— VF230 併入 `vehicle_setting`，不另開 feature

```
R-VS60（VF230 之 feature 歸屬，Pei 裁定 2026-08-23）

VF230 併入既有 `features/vehicle_setting/`，不建立新 feature slug。

分析層曾建議另開 slug（理由：Part 1 framework 已鎖、5 個 DR 待覆、
DR-15 影響 160 leaf）；Pei 裁定併入。該建議作廢，不再提起。

併入所生之技術後果，逐項處置見 61 包 §4。
```

### R-VS61 —— 素材補入由 Pei 執行

```
R-VS61（VF230 素材補入，Pei 裁定 2026-08-23）

VF230 素材位於 repo 既定根目錄之外，補入 `features/vehicle_setting/inputs/`
之動作由 **Pei 親自執行**；分析層與執行層皆只列清單，不搬檔。

缺件清單見 61 包 §5.2；補入後由執行層以 W-102 驗核 sha256 並更新
INPUTS.sha256。
```

### R-VS62 —— `output/` 之證據位階

```
R-VS62（Pei 先前彙整之證據位階，Pei 裁定 2026-08-23）

`VF230_V1_R5/output/` 之三檔為 Pei 先前自行整理之 VF230 項目彙整。

位階：**參考素材，非權威來源**。
- 得用於交叉比對（例如 leaf 全集之對帳、命名族群之提示）
- **不得**作為 leaf 母體、需求文字、規格參考之來源
- 其與 037 分報告不符者，037 勝；不符處登記為 anomaly，不逕行採用
- 其所含之任何列序，**不**構成 R-VS59 之續號依據
```

---

## 4. 併入（R-VS60）之技術後果與處置

以下六項為併入所必然引發、且 canon 未預設之情形。**逐項為執行層之工單**，
非待裁項；有爭議者停下登記。

### 4.1 一個 feature，兩本 workbook

`feature.yaml` 之 `paths.workbook` 為**單值**，目前指向 CFTS044 之 036。
VF230 為第二本。

**處置（W-102）**：`paths` 改為具名多本，例如

```yaml
paths:
  workbook_cfts044: "inputs/... _SWQT_CFTS044_Vehicle Controls_20260819.xlsx"
  workbook_vf230:   "inputs/... _SWQT_VF230_20260819.xlsx"
```

保留 `workbook` 鍵指向 CFTS044 以免既有腳本斷裂，或於同一 commit 內
一併改所有引用點——**擇一，不得半改**。改動前後以既有 Part 1 批次
dry-run 驗證輸出位元相同（回歸證明），結果具名回報。

### 4.2 framework 已鎖（2026-08-22）

VF230 之 Layer 2 尚不存在於 `framework.md`。

**處置（W-103）**：VF230 之 Layer 2 為 **P3 重開，但範圍限於新增**。
Part 1 之既有 Layer 1/2/3 **一律不得更動**（含拼寫、順序、合併）。
執行層於 P1 recon 後提出 VF230 之 Layer 2 候選（依 canon §4.1.2 之
「spec 目次 ∩ 037 分組」交集法），回上繳待 Pei 核可後方得鎖。

### 4.3 Test Group 之值

Part 1 之 G 欄實測 0 filled；`write_back.fill_test_group_set: false`。
VF230 之 Test Group 是否等同 `Vehicle Setting`，**尚未確立**——
VF230 之 11 份 037 涵蓋 Aux Switches／Suspension／Lighting／Park Sense 等，
其 spec 文件名為 `C-VF230_V1_R5_PDT27`，非 `Vehicle Controls`。

**處置（W-104）**：**停下項**。執行層於 recon 時實測 VF230 spec 之模組名，
依 R-C6 先例（feature 身分取自 spec 模組名，非交付資料夾標籤）提出
Test Group 候選，**不自行決定**，回上繳待裁。

### 4.4 done region

`done_region.detection: "author"`，`author_value: "Arif"`。
兩本 workbook 之 AA 欄皆 **0 filled** → **done region 於兩本皆為空集合**。

**處置**：VF230 之風格權威**不存在於其自身 workbook**。
沿用 Part 1 已鎖之風格（SWC 0708 為風格權威，R-1 v2 之訊號書寫規則、
`test_item` 須含括號下半等）。**不得**因 VF230 為新文件而重議風格。

### 4.5 CFTS044 預填 vs VF230 全空 —— 作業型態不同

CFTS044 之 036 進場時已預填 D/H/I/N（237 列）與 L/M（191 列）；
**VF230 之 036 為 0 列**。

**這是 Part 2 與 Part 1 最大之作業差異**：VF230 之需求列（B/D/H/I/N）
需自 11 份 037 分報告**產生**，而非自 workbook 讀取。

**處置（W-105）**：recon 之 leaf 母體來源為 037 分報告，
`recon.py` 之「036 既有列比對」步驟於 VF230 無對應輸入 ——
**不得**以 036 空白推得「leaf 母體為 0」或「覆蓋率 0%」。
該類比率於 VF230 之 P1 階段**無分母**，一律不報。

### 4.6 Part 1 之 open DR 是否波及 VF230

Part 1 現有 5 件待覆（DR-15/17/14′/19/20）、多件待送（DR-18/8/11/12/21/25/26）。
其中 DR-15 影響 160 leaf。

**處置**：**不預設**波及與否。VF230 之 recon 完成後，執行層逐 DR 判定
其提問是否落在 VF230 之 leaf 上，於上繳以表列出「波及／不波及／待判」。
在該判定產出前，**不得**以 DR-15 為由阻塞 VF230 之 P1。

---

## 5. 執行層工單（P0/P1）

### 5.1 W-102 — 素材驗核

Pei 補入 `features/vehicle_setting/inputs/` 後執行。
**11 份 037 分報告之檔名（逐字）**：

```
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA__6 Aux Switches, SWITCH 1 Power Mode and E-Save features.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA_Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense_features.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA_Cornering Lights_lane_features.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA_Daytime_Running_Light And Headlights_Off_Delay features^.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA_Pressure_Unit , Power_Unit And Torque_Unit features.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA STLA Report_SWRA_Time_Date_Autodoor_Camera_features.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_Illuminated_Approach - Trailer_Number_Report.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode Features_Report.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_Suspension_Service_Mode - Headlights_with_Wipers Features_Report.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_SWITCH_1_Type - SWITCH 4 Hold_Last_State Features_Report.xlsx
FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_Trailer_Name - Max_Power_Level_Report.xlsx
```

注意第 4 檔檔名含 `^`、第 5 檔含 ` , `（空格逗號空格）、多檔含 ` - `。
**glob 與 pathspec 一律加引號**；`features/vehicle_setting*` 之 glob 亦會命中
其他目錄，pathspec 用完整目錄名。

逐檔 sha256 → 更新 `INPUTS.sha256`（VF230 區塊另立，不混入 CFTS044 區塊）。

### 5.2 W-103 — leaf 母體建置

11 份 037 逐份解析 → `data/vf230_leaves.tsv`。
**每份分別報列數與 leaf 數，不先合併**；合併後之總數自各份重算（canon §5a）。
報告：每份之 `Categorization` 分布（Functional / 非 Functional / Heading）。

### 5.3 W-104 — Test Group 判定（停下項，見 §4.3）

### 5.4 W-105 — Layer 2 候選（見 §4.2）

### 5.5 W-106 — `feature.yaml` 多 workbook 改造（見 §4.1，含回歸證明）

### 5.6 W-107 — DR 波及判定（見 §4.6）

---

## 6. Pei 需補之素材（R-VS61）

| # | 缺件 | 現況 | 可否代用 |
|---|---|---|---|
| 1 | **SYS2 ICS export（VF230）** | `VF230_V1_R5/` 內無 | **不可代用**。CFTS044 之 SYS2 為該 CFTS 專屬。→ **DR-27** |
| 2 | spec `.doc` → `.docx` | `C-VF230_V1_R5_PDT27.doc` | 需轉檔；`.doc` 之解析路徑與 Part 1 不同 |
| 3 | DBC（`PDT27_E2A_R4_BHCAN.dbc` / `..._R5_FDCAN8.dbc`） | 在 `CFTS044/REF/` | **推定可代用**（專案級）——**待 Pei 確認** |
| 4 | `Logical Identifiers and CAN Mapping v1_76.xlsx` | 在 `CFTS044/REF/` | 同上，待確認 |
| 5 | `PDO Theme Config V3.4.xlsx` / `PDO Graphics Release ....pdf` | 在 `CFTS044/REF/` | 同上，待確認 |
| 6 | SYSAD | `VF230_V1_R5/` 內有同名檔（15.92 MB） | **未比對 hash**；補入時請指明採用哪一份 |

第 3–5 項若 Pei 確認可代用，**不需重複複製**，於 `feature.yaml` 以既有
CFTS044 inputs 路徑引用即可；請於補入時明示。

---

## 7. DR-27 草稿（待 Pei 核可後送出）

```
DR-27（新，Urgency 待定 —— VF230 缺 SYS2 ICS export；61 包 §6 開立）

型別（R-VS45）：型 C —— 素材缺件。

CFTS044 之素材含 SYS2 ICS export
（`SYS2  R1LR_Atl-H_25PI1.1_Activation and Configuration_CFTS_044_
Vehicle Controls_SR26_20250815-1022_20260324_Version3_Released.xlsx`），
VF230 之交付資料夾 `VF230_V1_R5/` 內無對應檔案。

請提供：VF230（`C-VF230_V1_R5_PDT27`）對應之 SYS2 ICS and DCSD export
（Released 版）。

影響：SYS2 為 Part 1 之 Category 交叉驗核來源（01 輪唯一之跨源檢驗，
537 列對帳、零錯配）。VF230 缺此來源者，其 leaf 之
Functional/Heading 判定將無第二來源可核，A-VS01 型之錯配無從偵測。

狀態：未送出。
```

---

## 8. 本包產生之新條文清單（自檢）

| 條文 | 型別 | 是否以可貼入區塊出現 |
|---|---|---|
| R-VS59（VF230 B 欄自 238 起） | Pei 裁定 | ✅ §3 |
| R-VS60（併入 `vehicle_setting`） | Pei 裁定 | ✅ §3 |
| R-VS61（素材補入由 Pei 執行） | Pei 裁定 | ✅ §3 |
| R-VS62（`output/` 為參考素材，非權威） | Pei 裁定 | ✅ §3 |
| DR-27（VF230 缺 SYS2） | DR 草稿 | ✅ §7 |

工單：W-102（素材驗核）／W-103（leaf 母體）／W-104（Test Group，停下項）／
W-105（Layer 2 候選）／W-106（`feature.yaml` 多 workbook，含回歸證明）／
W-107（DR 波及判定）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
**`INDEX.md` 現僅記至 NN=01，實際已至 NN=60；上繳時一併補齊或具名說明未補之範圍。**
