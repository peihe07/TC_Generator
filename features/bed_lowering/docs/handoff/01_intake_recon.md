# 下放包 01 — Bed Lowering Mode 接手盤點（Intake Recon）

日期：2026-08-26
Feature slug：`bed_lowering`（R-BLM1）
觸發：Pei 於 Claude Project 下達「Vehicle Settings feature裡面的Bed Lowering Mode 接手」

---

## 一、來源文件盤點（全表掃描，非抽樣）

### 1. SYS1 需求匯出
- 檔名：`SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_June_21_2021.xlsx`
- 分頁：`Basic Report`（A1:G72，71 資料列）、`Polarion`（A1:B15）、`_polarion`（A3:F84）
- Basic Report：NRL-193686 ~ NRL-193755，共 **70 個 Polarion 需求物件**，Outline 1 ~ 10.2.1
- 欄位：ID / Space-Document / Outline Number / Description / SYSRE_HMI_Source ID / Type / _polarion
- Polarion 與 _polarion 兩分頁尚未展開，Phase 1 recon 時併查（追溯對映用，見 §五-4）

### 2. 037 A03 SWE1 報告
- 檔名：`FMWIFSM037A03N1LSWE1BedLoweringModeHMIV0.1 STLA 報告.xlsx`
- 分頁：封面 / ChangeHistory 修訂履歷 / Product Document 記錄封面頁 / **Analysis Report** / Instructions / 下拉選單設定處
- Analysis Report（A1:T225）：資料列 218 = **42 個 Heading（SWE1-HMI-BLM-001 ~ SWE1-HMI-BLM-042）+ 176 個 leaf Functional Requirement**，已逐列對帳 42 + 176 = 218
- 欄位齊備：SWE-Requirement ID / Source Requirement ID（SYS-HMI-RA-BLM-nnn）/ HMI Source ID / Requirement Title / Requirement Description / Release Version / Categorization / FROP / Sub Categorization / Feasibility 四軸（Feasibility、Impact、Risk Factor、Reusable 各附 Description/Action）/ Priority / Verification Criteria / Verification Method
- Sub Categorization 分佈：HMI 約 119 leaf、Service 約 57 leaf
- FROP 欄全數為 `Vehicle Settings`（程式歸類標籤，不改變本 feature 之獨立 slug 地位，見 R-BLM1）

### 3. 原始規格 PDF
- `Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_June_21_2021.pdf`（FCA HMI/NAFTA，21 頁）
- 內容與 SYS1 Basic Report 逐節對應（Outline 1 ~ 10.2.1）
- Concept screens：Apps menu 選取、選中高亮、status bar truck-lowering icon、Cluster「Lowering Bed」/「Bed Lowering Complete」畫面、Head Unit Fault 流程
- **兩份副本並存，以 `inputs/` 這份為準（R-BLM4，見 §二）**：`spec-index/sources/` 早有同名 PDF，但非同一位元組。二者 21 頁、頁面尺寸、pdftotext 全文（11,349 字元）完全相同，21 頁中 20 頁 render 逐像素相同。

### 4. Sniffer 相容性
與 Display 037 不同，本 037 **有標準命名之 "Analysis Report" 分頁**，`scripts/intake.py` 可正常分類，不觸發 R-DM5 之誤判情境。無需 sniffer 例外處理。

### 5. 檔案取得授權
兩本 xlsx 與 PDF 經 Claude Project 附件授權。analysis 層不代放檔案本體。

**實測落點更正（2026-08-26）**：三檔已由 Pei 落於 `features/bed_lowering/inputs/`（共 784 KB），**不在** `_intake/Bed_Lowering/`——該投遞目錄現時 0 files，連 `INTAKE.md` / `intake.json` 都無。本包原敘述（「放置至 `_intake/Bed_Lowering/`」）與實況不符，已於此更正。

附帶澄清 `_intake/` 之語意：它是暫存投遞區，但**清空並非 intake 完成的通例**。同日實測八個子目錄，只有 `Bed_Lowering` 為 0；`AMFM` / `Comfort` / `Privacy` / `Time_Management` 檔案本體雖已移走，`INTAKE.md` + `intake.json` 仍留原地；`Display` / `SXM` / `Vehicle_Category` 連來源檔本體都還在。故不得以「`_intake/<Feature>/` 是否為空」推定該 feature 之 intake 狀態。

`inputs/` 之版控：本包落檔時 `features/bed_lowering/` 尚無 `.gitignore`（全案另 15 個 feature 皆有），三份客戶來源文件因而處於可被 `git add` 誤納的狀態——根層 `.gitignore` 並無 `features/*/inputs/` 規則，那道防線是每個 feature 自帶的。已補建 `features/bed_lowering/.gitignore`（`inputs/*` + `!inputs/INPUTS.sha256`，形制沿 `vehicle_setting`），並產出 `inputs/INPUTS.sha256`（三檔雜湊，隨包入版控）。

---

## 二、裁定紀錄（2026-08-26，Pei 原話 + 展開全文）

**R-BLM1（Q1，結構歸屬）** — Pei 裁：「甲」。
Bed Lowering Mode 立為獨立 feature，slug = `bed_lowering`，自有工作簿與 `features/bed_lowering/docs/{handoff,upstream}/` 目錄。不併入 `features/vehicle_setting/`，不附掛 VF230 工作簿（該本 438 TC 已寫回、處於 Pei 手動收尾階段，追加有污染風險）。037 之 FROP 欄「Vehicle Settings」僅為上游程式歸類標籤，不構成目錄歸屬依據。

**R-BLM2（Q2，驗證範圍）** — Pei 裁：「Heading 列納入但註明不寫測項」。
覆蓋台帳收錄 Analysis Report 全部 218 列。42 個 Heading 列（SWE1-HMI-BLM-001 ~ 042 母號）納入台帳並標註 `No TC — Heading; refer to child IDs`（其 Verification Criteria 原文即為 "Please refer to the following IDs"），不作為 TC 生成對象。176 個 leaf 為 TC 生成對象。
人因/可視性群（BLM-013 ~ BLM-017，日夜可視性、字體 legibility、手部人因，約 27 leaf）之處置沿本包 §四-3 預設：可功能化改寫為 HMI 可觀察行為者生成 TC；純設計驗證性質（percentile 人因、實車姿態）者不生成，列入 coverage gap disclosure table 隨工作簿交付。此預設 Pei 得於審查時否決改裁。

**R-BLM3（Q3，工作簿基底）** — Pei 裁：「裁」（從屬 Q1 甲案自動成立）。
工作簿自 BLANK + R-G1 模板起建，不沿用任何既有 036 本。

**R-BLM4（PDF 來源本，2026-08-26）** — Pei 授權 analysis 層裁定，裁：**以 `features/bed_lowering/inputs/` 那份為準**。

實測依據：二者 metadata 同源（Title、Author `T6133SW`、Producer `Microsoft: Print To PDF`、CreationDate 2021-06-25 18:46:52 全等），確為同一次輸出之同一份文件。差異來自後手處理——`spec-index/sources/` 那份 ModDate 為 2025-11-04，被線性化（`Optimized: yes`）、加了 metadata stream 與 AcroForm，且 p.3「Change Log」頁被作者 `SD63673` 於 2025-11-04 12:16 加上兩條紅色 Line 標註（寬 3.0，斜跨整頁，實為一個打叉）。`inputs/` 那份無任何 annotation，是未經觸碰的原始輸出。

裁定理由：來源本應取未經後手標註者（標註是他人閱讀痕跡，非交付內容的一部分，且該打叉之意圖無從查證，不得當作規格語意）。檔案大小之差（665,190 vs 664,990 bytes）純為重存所致，非版次差異——本 feature **不存在 PDF 版次問題**，勿誤記為版本衝突。

---

## 三、req_id 與 spec_reference 錨定（依既有全域規則，非新裁）

1. **req_id**：上游 037 已指派 `SWE1-HMI-BLM-{nnn}-{mm}`，逐字沿用（錨定原則：上游交付物正式欄為第一來源），不另裁前綴。
2. **spec_reference**：依 IN §10.7(b)，HMI Logic and Flow 類 → `{檔名}_{章節號}`：
   `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)_{章節號}`
   一個章節號一行，前綴逐行重述，升冪排列。本 feature 無 CFTS 家族。
3. **Requirement or Design ID 欄**：填 leaf 之 `SWE1-HMI-BLM-{nnn}-{mm}`；一 leaf 多 TC 時同 ID 重複列出（IN §8.2.2）。

---

## 四、已知風險與覆蓋議題

1. **速度門檻缺值（確定性缺件）**：規格原文 `*XX MPH`，明載 "Speed threshold to be defined by chassis engineering"。受影響 leaf 約 13 個（BLM-007-01~04、BLM-021-04/05、BLM-022-01~04 等，生成時逐列確認）。依 IN §8.4.3（S6）落 `PENDING: DR-1 BLM operating speed threshold value`，不造值。DR-1 已登記於本 feature `DATA_REQUESTS.md`，由 Pei 決定送出時點。
2. **DT vs DJ/D2 變體軸**：BLM-001（DT：前升後降）與 BLM-002/041（DJ/D2：僅後降）為 PROXI/車型配置分支，屬 IN §8.3 之 mode/variant sibling 軸。車型配置參數之 PROXI 寫法待生成期查 `forms/` 對照（候選 DR）。
3. **人因/設計驗證群（BLM-013 ~ 017）**：見 R-BLM2 展開文。SWE.6 不可執行者入 coverage gap disclosure table，不得無聲吸收亦不得造測。
4. **SYS ↔ 037 追溯縫隙**：037 之 Source Requirement ID（SYS-HMI-RA-BLM-nnn）不出現於 SYS1 xlsx 任何可見欄（SYS1 用 NRL 號 + Outline 號）。對映須經 `_polarion` 分頁驗證；驗證不通則登 DR 向上游索取對照表。**禁止以列序推定對映**（R-VS50′ 精神：未經全表驗證之對映即造值）。
5. **觀察通道與台架能力**：EVIC 文案、Cluster 畫面、車內 chime、air suspension 實體行為、fault 注入（BLM-037/038）、車速模擬 —— 台架可執行性與 CAN 車速/fault 訊號來源為生成期 DR 候選；訊號寫法屆時依 IN §8.7.5 v3 + DBC 查證，查無者依 (d)/(g) 保留來源名。
6. **小異常（不阻斷）**：037 封面 Date = 2020/09/05，早於來源規格發行日 2021/06/21；V0.1，疑為模板殘值。不處理，僅存查。
7. **EVIC 文案引號瑕疵**：規格 slide 7 原文 `""Bed Lowering Unsuccessful – ...` 有連續雙引號；SYS1 Basic Report（NRL-193702）已正規化為單組引號。TC 以 Basic Report 文字為準（來源正式欄優先）。
8. **PDF 副本差異（已裁，不阻斷）**：見 §一-3 與 R-BLM4。差異僅止於 `spec-index/sources/` 那份 p.3（Change Log 頁）被後手加了兩條紅線標註，內文與版面零差異，故頁碼引用、slide 編號、文字擷取皆不受影響。惟 `spec-index/cache/` 之預處理 json（4.07 MB）係自 **xlsx** 而非 PDF 產出，xlsx 兩處 sha256 相同（`6dcdafa4…`），可直接取用，不受本項影響。該 json 之 `source_file` 欄自陳為 xlsx，`entries` = 70，與 §一-1 之 70 個 Polarion 需求物件逐數相符；建於 2026-04-26，embedding model `text-embedding-3-large`。

---

## 五、三層框架草案（Layer 2 待 Pei 裁，未鎖定，framework.md 於裁定後落檔）

Layer 1（Test Group）：`Bed Lowering Mode`（= 規格文件標題，IN §4.1.1）

Layer 2 草案（capability cluster）與 Layer 3（規格章節對映）：

| Layer 2（草案） | Layer 3（Outline） | 對應 Heading |
|---|---|---|
| Feature Entry | 3.1, 4.4~4.6, 7.1~7.2 | 004, 017, 018, 019, 025, 028, 029, 030 |
| Activation Gating | 3.2, 4.7.1, 10.1.4 | 005, 006, 007, 020, 024, 042 |
| Lowering Operation | 1.1, 1.2, 2.1, 4.7.2, 10.1.3 | 001, 002, 003, 021, 035, 041 |
| HU Feedback | 3.3.1, 6.1.2, 7.2.1~7.2.2 | 008, 026, 031, 032, 036 |
| Cluster & EVIC Feedback | 3.3.2~3.3.5, 8.1~8.2 | 009, 010, 012, 033, 034 |
| Fault Handling | 3.3.4, 9.1 | 011, 037, 038 |
| Restore & Exit | 6.1.3, 4.7.2.1 | 022, 027 |
| Ergonomics & Legibility | 4.1~4.3, 4.4.1, 4.8 | 013, 014, 015, 016, 023 |
| System Constraints | 10.1.1~10.1.2 | 039, 040 |

備註：Layer 3 僅存 framework.md，不入工作簿（IN §4.1.5）。Heading 至 Layer 2 之歸位於 framework 鎖定時逐一複核，上表為草案非定案。

---

## 六、下一步（Phase 1 前置）

1. ~~Pei 手動放置三個來源檔至 `_intake/Bed_Lowering/`~~ → **已完成（2026-08-26）**，實際落點 `features/bed_lowering/inputs/`，三檔齊 784 KB，雜湊登錄於 `inputs/INPUTS.sha256`（見 §一-5）
2. Pei 裁 Layer 2 框架（採/改）→ analysis 層落 `framework.md` 鎖定
3. `_polarion` 分頁展開，驗證 SYS-HMI-RA-BLM ↔ NRL 對映（§四-4）
4. 工作簿 BLANK + R-G1 模板起建（R-BLM3），交執行層
5. 首批生成範圍與批量（預設沿全案慣例 50 列/批、3 批一繳）於框架鎖定後併裁

## 七、未結 DR 清單（隨包附列，IN §8.4.3）

| DR | 項目 | 狀態 | 送出日 |
|---|---|---|---|
| DR-1 | BLM operating speed threshold value (spec `*XX MPH`, owner: chassis engineering) | 已登記，未送出 | （空） |
