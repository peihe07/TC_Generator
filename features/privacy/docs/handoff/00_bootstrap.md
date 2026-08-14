# 下放包 00 — Privacy feature bootstrap (Phase 0)

分析層 → 執行層。2026-08-13。自足包：Claude Code 不需任何 chat context。

**落點例外說明**：本包依 charter 應寫入
`features/privacy/docs/handoff/00_bootstrap.md`，但 `scripts/new_feature.py`
在 `features/privacy/` 已存在時會 `sys.exit` 拒絕 scaffold，因此該路徑在本包
執行「之前」不得存在。本包故暫置於 `docs/fw036/`。**執行層 scaffold 完成後，
請把本檔 `git mv` 至 `features/privacy/docs/handoff/00_bootstrap.md`**，此後
所有 Privacy 往返回歸標準路徑。

---

## 0. 授權狀態

Pei 於 2026-08-13 授權本包之兩項動作：scaffold 與素材複製。
**範圍裁決 R-PV01 尚未簽署** —— 本包不得據以縮限或擴張任何 spec 引用範圍；
遇到範圍問題一律登記後停手。

---

## 1. 作業一：素材複製到 `_intake/Privacy/`

來源目錄（唯讀，勿移動原檔，複製即可）：

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/
```

該目錄實測為 6 檔 / 3.76 MB，全數複製：

| 檔名 | size | 分析層預判之 kind |
|---|---|---|
| `SWE1_CFTS_022-Privacy_Features.xlsx` | 62.29 KB | swra_report（有 `Analysis Report` 分頁）|
| `CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx` | 53.03 KB | polarion_export / SYS2 safety export（有 `Basic Report` 分頁）|
| `R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx` | 77.42 KB | cfts_doc |
| `SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` | 3.29 MB | cfts_doc（實為 SYSAD，非 CFTS；見 A-PV05）|
| `Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx` | 143.49 KB | cfts_doc（外部引用 VF）|
| `Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx` | 144.72 KB | cfts_doc（外部引用 VF；擬排除，待 R-PV01）|

## 2. 作業二：scaffold + intake

```bash
cd /Users/peihe/Work_Projects/TC_Generator
python scripts/intake.py Privacy --scaffold
```

Feature 名一律 `Privacy`（目錄將為 `features/privacy/`，符合 2026-08-11 reorg
慣例）。產出 `INTAKE.md` + `intake.json`，並將檔案移入 `features/privacy/inputs/`。

**abbr 警示**：`new_feature.py` 取 `feature[:2].upper()` → `PR`，anomaly 前綴
會變成 `A-PRnn`。分析層本包全程使用 **`A-PVnn`**（Privacy 既有慣稱，且 `PR`
與 Projection 易混）。TC id abbr 亦同此議題（SXM 用 `NR1L-SXM-{NNN}`）。
**這是 Tier 2 裁決，不得自裁** —— scaffold 後照實回報 script 產生的 abbr，
由 chat 帶 Pei 裁定後再統一修正，勿在 scaffold 時手動改。

---

## 3. 分析層已完成之實測（供 intake 交叉驗證，非取代 recon）

以下為分析層在沙箱副本上的唯讀探測結果。**執行層須以 `inputs/` 之實體檔
重驗**，不得直接引用本節數字作為 recon 輸出。

### 3.1 需求全集：10 leaves

`SWE1_CFTS_022-Privacy_Features.xlsx` → `Analysis Report` 分頁（17 列 × 35 欄），
表頭在第 7 列，資料列 8–17 = **10 leaves**，欄位為 037-A03 樣式
（cell AI2 = `FM-WI-FSM-037-A03`）：

| SWE-Requirement ID | Source Requirement ID | Requirement Title（節錄）|
|---|---|---|
| SWE1-HMI-PRIVACY_FEATURES-001 | SYS-RA-PROF-023 | Input Monitoring – Resume After Sleep Mode Exit |
| -002 | SYS-RA-PROF-160 | Personalization Display – Restore on Interior CAN Wake-Up |
| -003 | SYS-RA-PROF-169 | Speed-Controlled Volume – Restore on HU Wake-Up |
| -004 | SYS-RA-PROF-170 | SCV Signal – Transmission on HU Wake-Up |
| -005 | SYS-RA-PROF-171 | SCV Signal – Valid Value Handling |
| -006 | SYS-RA-PROF-172 | SCV – Local Adjustment Without AMP |
| -007 | SYS-RA-PROF-173 | SCV – No Adjustment With AMP Present |
| -008 | SYS-RA-PROF-174 | SCV – Restore on AMP Wake-Up |
| -009 | SYS-RA-PROF-175 | SCV – Update and Store Without AMP |
| -010 | SYS-RA-PROF-176 | SCV – Update and Transmit With AMP Present |

Requirement Status 全為 `New`；Release Version 全為 `V1.00.00`；
Categorization 全為 `Functional Requirement`；Sub Categorization 為
`Service`（001/004/005/010）或 `HMI`（其餘 6 筆）。
封面：版本 C，核准者 劉安哲 AllenACLiu（2026-02-09），審查者 吳冠麒 StanleyKCWu（2026-02-05）。

量測條件：`openpyxl.load_workbook(..., data_only=True)`；逐列掃 A–H 欄；
非空判準為 `not in (None, "")`。

### 3.2 CFTS022 之 ECU/Radio 適用性掃描

來源 `R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification…docx`。
掃描單位：以 `**{artifact_id}: [` 起首之 artifact header 行，共 **336** 行，
其中 **334** 行帶 `[ECU:...]` tag（無 tag 之 2 行為 artifact 4914987、4914997，
皆 Description 型，非反證）。比對 `[ECU:]` × `[Radio:]`，區分大小寫、逗號切詞：

- `Radio` 含 `R1L-R` 且 ECU 集合含 `LTM`：**196** 行
- `Radio` 含 `R1L-R` 且 ECU 為 **LTM-only**：**23** 行
- `Radio` 含 `R1L-R` 且含 `ETM` 但不含 `LTM`：**0** 行

### 3.3 VF651 變體全集（canon §5a rule 9 —— 手上兩份不是全集）

`VF/28HDCC_2A_LTM/LTM/VF - Functional Requirements/` 與
`VF/VF_Split document/HDCC28_Split/` 兩處清單一致，各含 **5** 個 VF651 變體：

| 變體 | 標題 | 分析層是否已開啟 |
|---|---|---|
| V2_R2 | LTM Non-Amplified (Base Audio) | 已全文讀過 |
| V3_R3 | ETM Non-Amplified (Base Audio) | 已全文讀過 |
| V6_R2 | LTM/ETM **Amplified** Audio System | **未開啟** |
| V9_R3 | LTM/ETM Amplified with Internal ANC | **未開啟** |
| V11_R3 | LTM Non-Amplified **with ANC** | **未開啟** |

V2_R2 與 V3_R3 之全文 diff：390 vs 393 非空行，差異 hunk 75 行。實質差異僅
四處 —— V3 之 ECU 清單多列 ETM、多 `Hybrid_Type` PROXI 參數、多
`TELEMATIC_FD_13.AUD_LVL` 訊號、三條 gating 由 FD-CAN3→FD-CAN8 改寫為
BH-CAN1→BH-CAN2；而 **V2 獨有** `CTRL_AMP.SCV_LVLSts`（BH-CAN2→BH-CAN1）
之 SGW gating，V3 無此條。

### 3.4 SYS.2 覆蓋

`9_ASPICE/02_SYS.2 System Requirements Analysis/VF651_Audio_Output_Management/`
下 8 個子目錄：V11、V2_R2、V42_R3、V43_R1、V44_R1、V46_R1、V6_R2、V9_R4。
**無任何 V3**。

---

## 4. 執行層須登記之 anomaly（登記，不裁決）

以 `A-PVnn` 前綴寫入 `features/privacy/ANOMALIES.md`，每條附證據與建議處置，
狀態一律 `PENDING`。

**A-PV01 — 交付目標 workbook 缺席（阻塞級）**
6 份素材中無任何含 `Test Case Specification` 分頁之檔案（分析層以 openpyxl
逐檔驗過分頁名）。因此 `workbook_state` 無法判定，P7 亦無寫回標的。
建議處置：Tier 3 索取 FM-WI-FSM-036-A01 之 Privacy workbook；在其到位前
P1 recon 可跑（037 側完整），P4 之後不得啟動。

**A-PV02 — VF651 變體選擇未決**
手上 2 份僅覆蓋 Non-Amplified 一格，全集為 5 變體（§3.3）。
且 §3.1 之 10 leaves 中，**-007 / -008 / -010（PROF-173/174/176）三筆明文以
「AMP is present」為前提**，另 -006 / -009 以「AMP is not present」為前提。
即 AMP-present 情境確在需求範圍內，Non-Amplified 單一變體不足以支撐。
建議處置：待 R-PV01(c)；若裁定納入，需補 V6_R2（ANC 配置另需 V9_R3 / V11_R3）。

**A-PV03 — ETM V3_R3 疑非本專案適用件**
證據：§3.2（R1L-R × ETM-only = 0 行）+ §3.4（SYS.2 無 V3）。
建議處置：待 R-PV01(a) 裁定排除；在裁定前不得列為 `specification_reference`。

**A-PV04 — 同名不同內容（A-AM09 同型）**
`…VF651_V2_R2.docx` 在同一 release 樹內有兩種 size：

- `10_Reviewing/…/Privacy Mode/` = **146,929**
- `VF/VF_Split document/HDCC28_Split/` = **146,929**
- `VF/28HDCC_2A_LTM/LTM/VF - Functional Requirements/` = **146,899**

量測條件：`get_file_info` 之 size 欄位，**未做 hash**。
執行層作業：對這三份計 SHA256 並回報；差異可能僅為重存，但不得假設。
交付夾那份與 `HDCC28_Split` size 相同，暫視為同源。

**A-PV05 — SYSAD 混入 CFTS 分類**
`SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx` 為 SYS.3 架構設計，
非 CFTS 規格；intake.py 之 `cfts_doc` sniffer 依副檔名分類會把它併入。
其角色是背景理解，**不得作為 `specification_reference`**（§10.7 禁止引用
分析類文件；SYSAD 屬設計非規格）。建議處置：`feature.yaml` 標為 context-only。

**A-PV06 — abbr `PR` vs `PV`**
見 §2。純登記，裁決回 chat。

---

## 5. 執行層須建立之 `DATA_REQUESTS.md` 列

依 `features/amfm/DATA_REQUESTS.md` 之欄位格式建表（# / 檔名 / Status /
Leaves served / Batch impact / Anomaly / Urgency）：

| # | 檔案 | Urgency | Anomaly |
|---|---|---|---|
| 1 | Privacy 之 FM-WI-FSM-036-A01 TC workbook（名稱待 Pei 給定） | **High —— P4 之前必須到位** | A-PV01 |
| 2 | `Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx` | Medium —— 待 R-PV01(c)，若納入則 -007/-008/-010 需要 | A-PV02 |
| 3 | `…with_Internal_ANC_VF651_V9_R3.docx` / `…with_ANC_VF651_V11_R3.docx` | Low —— 僅在 ANC 配置納入範圍時 | A-PV02 |
| 4 | CFTS019 Audio Management（SYSAD 對 PROF-172 之另一引用） | Low —— AMFM `inputs/` 已有同名檔可比對 release | A-PV02 |

**Standing rule（沿用 AMFM）**：任何新發現之外部引用，登記 anomaly 的同時
必須新增一列於此表；且每次 session opener 與 batch gate 都要按 Urgency 回報。

---

## 6. 停手條件（本階段特化）

除 canon §0 六項外，本 feature 加一項：
**任何需要在 5 個 VF651 變體之間做取捨的判斷，一律停手回報**，不得以
「手上只有這兩份」為由默認範圍。此即 A-PV02 之成因。

---

## 7. 上繳包要求

寫入 `features/privacy/docs/upstream/00_bootstrap.md`，須含：

1. `intake.py` 之完整 stdout + `INTAKE.md` / `intake.json` 摘要
2. script 實際產生之 abbr 值（照實回報，勿修正）
3. 六檔之 sniff 結果，與本包 §1 預判之逐項比對（相符／不符各列出）
4. A-PV04 之三份 SHA256
5. `Analysis Report` 分頁之獨立重算 leaf 數，與本包 §3.1 之 10 比對
   —— **不符即停手回報，不得自行調和**
6. **「本包是否仍有該驗而未驗者」之獨立判斷**（此項不得省略）

---

## 8. 本包產生之新條文清單（自檢表）

- [x] A-PV01 交付目標 workbook 缺席 —— §4，區塊形式
- [x] A-PV02 VF651 變體選擇未決 —— §4，區塊形式
- [x] A-PV03 ETM V3_R3 疑非適用件 —— §4，區塊形式
- [x] A-PV04 同名不同內容 —— §4，區塊形式
- [x] A-PV05 SYSAD 混入 CFTS 分類 —— §4，區塊形式
- [x] A-PV06 abbr PR vs PV —— §4，區塊形式
- [x] DATA_REQUESTS 4 列 —— §5，表格形式
- [x] 停手條件加項 —— §6
- [ ] R-PV01(a)(b)(c)(d) —— **尚未簽署**，不在本包生效範圍，僅供執行層知悉
      不得自裁範圍

以上 8 項均已以可直接貼入之區塊或表格形式出現，非夾敘於段落中。

<!-- HANDOFF-LINK: 00 -> upstream:00 -->
