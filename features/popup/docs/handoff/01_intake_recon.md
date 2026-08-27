# 下放包 01 — Popup 接手盤點（Intake Recon）

日期：2026-08-27
Feature slug：`popup`（R-POP1）
觸發：Pei 於 Claude Project 下達「Pop-Up Queue and Priority Management 接手」，
同日「准」五項提案（見 §二）。

## 禁區

- git 一切操作屬 Pei（R-G5）；執行層只準備不執行
- `sources/raw/` 落檔後不得改動（R-G27：內容爭議以 raw 為準）
- 不得以 openpyxl `wb.save()` 寫回任何 036 母本衍生簿（R-G1 註記、R-G3）

---

## 一、來源文件盤點（分析層對 Claude Project 附件實測，2026-08-27）

**指紋警語（FO §9.1 通則 5）**：下表 sha256 為 Claude Project 附件副本所測。
其中 PDF 一件已確認經 Project 管線預處理（見 §一-3），其位元組必不同於
Pei 本機原檔 —— **本表指紋僅供分析層自證所讀為何，不作 intake 比對基準**。
intake 之基準為 Pei 投遞入 `_intake/Popup/` 之原檔重測值。

### 1. 037 A03 SWE1 報告
- 附件檔名：`FMWIFSM037A03N1LSWE1PopupHMIV0_2_STLA_報告.xlsx`
  （Project 附件檔名之 `V0_2` 疑為上傳正規化；Pei 本機實際檔名以投遞為準，
  文件自身版次為 V0.2）
- 附件 sha256（前 16）：`cdf0812fb9f74b71`；真 xlsx
- 分頁：封面／ChangeHistory 修訂履歷／Product Document 記錄封面頁／
  **Analysis Report**／Instructions／下拉選單設定處 —— 標準命名，
  `scripts/intake.py` sniffer 可正常分類
- Analysis Report（A1:T14）：表頭 r7，**資料列 7（r8–r14，逐列，A 欄非空）**
  = Heading 2（SWE1-POP-001、SWE1-POP-002）+ **Functional Requirement leaf 5**
  （SWE1-POP-002-01 ～ -002-05）
- 全數 Source Requirement ID = SYS-HMI-RA-CORE-041／042；
  HMI Source ID 僅兩值：`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.5`／`_5.6`
- 五 leaf 一覽：-002-01 time-out／-002-02 press second time／
  -002-03 touch outside／-002-04 selection／-002-05 selection exception
- 異常一：POP-001（GP3）為 Heading 且 K8 逐字「Duplicated feature of
  SWE1-POP-002-02」→ 台帳處置見 R-POP5
- 異常二：POP-002 之 VC（S9）逐字引用 `SWE1-POP-004-01`～`-05`，
  該五號本簿不存在 → DR-POP3
- 小異常（不阻斷，存查）：D4 Date = 2020/09/05，早於來源規格 2023/02/02，
  疑為模板殘值（同 bed_lowering §四-6 形態）

### 2. SYS1 需求匯出
- 附件檔名：`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_February_2_2023.xlsx`
- 附件 sha256（前 16）：`d9a16eed89203e4c`；真 xlsx
- 分頁：`Basic Report`（A1:G169）、`Polarion`（A1:B15）、`_polarion`（A3:F181）
- Basic Report：**A 欄非空資料列 167**（NRL-168247 ～ NRL-168413），
  Outline 1 ～ 15.6 —— 為 Core HMI Logic and Flow **全文件**匯出，
  popup 僅其中第 5 章
- 第 5 章（General Popup Behavior）：**7 項**（5、5.1～5.6；
  NRL-168282 ～ NRL-168288）。5.3=GP1、5.4=GP2、5.5=GP3、5.6=GP4
- `_polarion` 分頁載 NRL 逐項 Revision（10259）與 Checksum，追溯對映用

### 3. 規格 PDF（附件為預處理副本，非原檔）
- 附件檔名：`Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_February_2_2023.pdf`
- 附件實測：**非 PDF** —— ZIP，43 members = 21 JPEG（952×1260）+
  21 個 0-byte txt + `manifest.json`（含 page_uuid、has_visual_content 欄）
  → 此為 Claude Project 附件管線之頁面渲染產物，**不是 Pei 本機檔案之形態**
- 因此「無文字層」為附件副本之屬性，**原檔是否具文字層未定** ——
  intake 時以 `pdftotext` yield test 實測（Tier 0），
  spec_mode 之 B／C 面據此定案；A 面（SYS1 export 為文字權威）先行成立
- 圖面可用性已初驗：附件頁 8（規格頁碼 8，General Popup Behavior）
  之 GP1～GP4 圖面文字與 SYS1 export 5.3～5.6 逐句相符（人工比對一次，
  範圍限第 5 章；他章未比對 —— R-G11 盲區聲明：Mode A 掉句風險於本
  feature 僅第 5 章相關，該章已比；全文件層級之掉句檢查不在本 feature 射程）

### 4. 檔案取得授權
三件素材經 Claude Project 附件授權。分析層不代放檔案本體（G-L：
「到齊」以 `_intake/Popup/` 投遞檔之路徑 + SHA 為準，見 §六-1）。

---

## 二、裁定紀錄（2026-08-27，Pei「准」五項）

全文落於 `features/popup/RULINGS.md`（R-G13：引用者自 repo 讀原文）：

- **R-POP1** slug = `popup`；`features/popup/`、`_intake/Popup/`（已建妥，
  list_directory 實測存在 —— R-G24）
- **R-POP2** 生成範圍照 037 V0.2 之 5 leaf；queue／priority 缺口
  （GP2 = 5.4 與 Priority Matrix 行為無任何 SWE1 列）RD-1 具名上報，
  不自行擴充（IN §8.2.1／§8.4.2）
- **R-POP3** DR 三件開立（DR-POP1／2／3），登錄於 `DATA_REQUESTS.md`
- **R-POP4** Test Group = `Popup`；Test Set 單一 `Pop-up Close`
- **R-POP5 [DEFAULT]** Heading 2 列納台帳標 No TC（沿 R-BLM2 形制，
  待 Pei 追認）

## 三、req_id 與 spec_reference 錨定（依既有全域規則，非新裁）

1. **req_id**：逐字沿用 037 之 `SWE1-POP-{nnn}-{mm}`
2. **spec_reference**：IN §10.7(b) HMI Logic and Flow 類 →
   `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_{章節號}`
   —— 取 037 C 欄逐字形（含 `(February_2_2023)` 括號）；一章節號一行，
   前綴逐行重述，升冪。本 feature 無 CFTS 家族
3. **Requirement or Design ID 欄**：填 leaf 之 SWE1-POP-002-{mm}；
   一 leaf 多 TC 同 ID 重複列出（IN §8.2.2）

## 四、已知風險與覆蓋議題

1. **timeout 缺值（確定性缺件）**：GP4-1 之 timeout 值定義於
   `HMI Popup List` 文件，該文件不在素材內。-002-01 之 TC 落
   `PENDING: DR-POP1 popup timeout value` 佔位（IN §8.4.3）。
   VC 之 "e.g., 5 seconds" 為舉例，依 IN §8.4.1 不得採值。
2. **multi-task popup 之選定（-002-05）**：例外清單（search keyboard 之外
   還有哪些）無來源 —— 同繫 DR-POP1。TC 得以 search keyboard（GP4 原文
   明載之例）先行，其餘實例不得自行列舉。
3. **-002-03（touch outside）之適用性**：037 K12 自陳該機制
   「default to disable, requester should call the API to enable」——
   哪些 popup 啟用 touch-outside 無來源（Popup List 文件射程），
   TC 之受測 popup 選定同繫 DR-POP1；生成時若無可具名之啟用實例，
   落 PENDING 而非造例。
4. **範圍缺口（R-POP2）**：GP1（5.3，7" 無 medium 模板）、GP2（5.4，
   small=priority 1／large=priority 2）無 SWE1 列；queue／priority
   本體行為無 SWE1 列。記 `COVERAGE_GAPS.md`，RD-1 具名上報。
5. **一 leaf 之 sibling 軸預估**：-002-02 之觸發鍵含 H/K 與 UI 按鈕兩型
   （037 S11 逐字 "physical hard button or a specific UI button"）——
   屬 IN §8.3 device 軸，生成時評估拆分；其餘 leaf 預估 1 TC。

## 五、三層框架草案（R-POP4 已裁 Layer 1／2；Layer 3 於 framework.md 鎖定）

| Layer | 值 |
|---|---|
| Layer 1（Test Group） | `Popup` |
| Layer 2（Test Set） | `Pop-up Close`（單一） |
| Layer 3 | `PC1` = spec 5.5～5.6（GP3／GP4 條族） |

Layer 3 僅存 framework.md，不入工作簿（IN §4.1.5）。

## 六、作業清單（執行層，Phase 0→1）

前置：**Pei 投遞三份原檔至 `_intake/Popup/`**（目錄已建妥）。投遞前本包
§六-2 以下不得起跑。

1. 投遞檔 `shasum -a 256` 實測，產 `_intake/Popup/INTAKE.sha256`；
   xlsx 兩件與本包 §一指紋比對（**預期相符**；不符即停下回報，不調和）；
   PDF 一件**不比對**（§一-3 警語），僅登錄實測值
2. PDF 身分實測：`file` + `pdftotext` yield test → 回報原檔是否具文字層，
   spec_mode B／C 面定案（Tier 0，結果記 RECON.md）
3. 依 R-G27 落 `sources/`：`raw/<doc_id>/` 收三原檔、
   `extracted/<doc_id>/` 收逐 sheet tsv／文字形（附來源 sha 對照）、
   `MANIFEST.tsv` 增列。doc_id 提案 [DEFAULT]：`core_hmi_lf_sys1`／
   `core_hmi_lf_pdf`／`popup_037_v0_2`（執行層得依既有慣例微調，回報即可）
4. `scripts/new_feature.py` scaffold `features/popup/`（既有 docs/、
   RULINGS.md、DATA_REQUESTS.md 不得覆寫）；feature.yaml 以 doc_id
   引用來源（R-G27），不存原檔副本
5. RECON.md 產出：workbook_state = BLANK（無既存工作簿）、欄位對映、
   下拉詞彙抽取、7 列台帳（含 R-POP5 之 Heading 標記）
6. 工作簿自 R-G1 母本起建，落 `sandbox/`（R-G25；xlsx 只准在此修改）

**預期數字**（[MANUAL]，本 feature 尚無 feature.yaml 可供
`expected_numbers.py` 推導）：

| 項 | 預期 | 量測條件 |
|---|---|---|
| 037 Analysis Report 資料列 | 7 | r8–r14，逐列，A 欄非空 |
| 其中 Functional Requirement leaf | 5 | G 欄 = `Functional Requirement`，逐列 |
| 其中 Heading | 2 | G 欄 = `Heading`，逐列 |
| SYS1 Basic Report 資料列 | 167 | 逐列，A 欄非空 |
| SYS1 第 5 章項數 | 7 | Outline 欄 = `5` 或以 `5.` 起始，字串比對區分大小寫 |
| xlsx 指紋相符件數 | 2/2 | 全檔 sha256 |

## 七、上繳要求

- 預期數字對照（相符者亦列）；不符者停下回報不調和（FO §8.2）
- R-G13 引用回報：本包引用之裁決為 R-POP1～R-POP5、R-G1、R-G3、R-G5、
  R-G24、R-G25、R-G27（R-POP 系列同包新立，讀 `features/popup/RULINGS.md`
  現行文即可；sha8 自 `RULINGS.sha.tsv` 之增列待 `rulings_hash.py` 本輪併跑）
- PDF 身分實測結果（§六-2）與 doc_id 定案
- 三分法清單、掃描條件揭露、獨立判斷、四支 gate 實跑輸出（FO §8.2）
- 新開 anomaly 與 DR 成對

## 八、升級條件

- 投遞 xlsx 指紋與本包不符
- 037 或 SYS1 之列數／leaf 數與預期不符
- `sources/` 既有內容與 R-G27 落點衝突（MANIFEST 現為僅表頭，預期無衝突）
- scaffold 與既存檔案衝突（RULINGS.md／DATA_REQUESTS.md 已先行落檔）

## 九、未結 DR 清單（IN §8.4.3，隨包附列）

DR-POP1（HMI Popup List）／DR-POP2（Priority Matrix）／DR-POP3
（POP-004 懸空引用），全文見 `features/popup/DATA_REQUESTS.md`，
皆「已登記，未送出」。
