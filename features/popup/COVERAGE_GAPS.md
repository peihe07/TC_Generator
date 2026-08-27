# COVERAGE_GAPS — Popup

R-POP2 令記之範圍缺口。落檔依下放包 01 §四-4。

**本表之意義**：規格 `Core HMI Logic and Flow` 第 5 章（General Popup
Behavior）之條目中，**037 V0.2 未給任何 SWE1 列**者。無 SWE1 列即無 leaf，
無 leaf 即本工作簿不生成 TC —— 依 R-POP2 **不自行擴充**，以 RD-1 具名上報。

**與 `DATA_REQUESTS.md` 之區別**：DR 是「有 leaf、驗得了，但缺一份文件才能
填出具體值」（TC 生成而落 PENDING 佔位）；本表是「連 leaf 都沒有」
（TC 不生成）。兩者混談會把「上游沒寫需求」講成「缺一份文件」。

**與 `bed_lowering/COVERAGE_GAPS.md` 之形態差異**：該表為 leaf 側
（leaf 存在但 SWE.6 層驗不了）；本表為**規格側**（規格有條文而 037 無 leaf）。
本 feature 之 5 個 leaf **全部生成 TC，無 leaf 側缺口**。

## 量測條件

- 規格側母體：`sources/extracted/core_hmi_lf_sys1/Basic_Report.tsv`，
  `Outline Number` 欄值 `5` 或以 `5.` 起始者，字串比對區分大小寫 → **7 項**
  （NRL-168282 ～ NRL-168288）
- leaf 側引用：`sources/extracted/popup_037_v0_2/Analysis_Report.tsv`，
  `Categorization` = `Functional Requirement` 之 5 列，取 `HMI Source ID`
  末段章節號 → 相異值 **1**（`5.6`）
- 逐項條文為 SYS1 export `Description` 欄逐字（`_x000D_` 為匯出之換行殘留，
  照錄不整理）

## 規格側缺口（第 5 章 7 項中 6 項無 SWE1 列）

| outline | NRL | 規格條文（逐字摘）| 037 有無 SWE1 列 | 處置 |
|---|---|---|---|---|
| 5 | NRL-168282 | `General Popup Behavior` | 無 | 章標題，非行為條文 —— 不列為缺口 |
| 5.1 | NRL-168283 | `Examples of Popups` ／ `- See HM/ Popup List Priority Matrix for popup priorities` ／ `- See HM/ Popup List for all popup text strings/timeouts/exit conditions/templates/use cases if not covered in a specific feature logic and flow` | 無 | **缺口**。本項為 queue／priority 之唯一具名上游來源指向；其標的兩件之 repo 側候選見 A-POP2 |
| 5.2 | NRL-168284 | `Examples of Items That Are Not A Popup` | 無 | 反例說明（純圖），非可測行為 —— 不列為缺口 |
| 5.3 | NRL-168285 | `GP1.) The 7" low radio will not have medium popup templates, but all other radio variants will.` | 無 | **缺口 GAP-POP1**（下放包 §四-4 之 GP1）|
| 5.4 | NRL-168286 | `GP2.) For Android Dialogs, to meet CCD requirements for certification, large popup templates are to be used, and have a priority 2. For Android Toasts, small templates should be used and have a priority of 1.` | 無 | **缺口 GAP-POP2**（下放包 §四-4 之 GP2；priority 行為之唯一條文）|
| 5.5 | NRL-168287 | `GP3.) If a button opens a custom pop up (example: Status Bar Temperature/Comfort Controls Popup), pressing the button a second time will close the popup.` | 有，惟為 Heading `SWE1-POP-001`（R-POP5 標 No TC）| **非缺口** —— 行為與 5.6 之第 2 途徑相同，由 `SWE1-POP-002-02` 之 TC 涵蓋。見 A-POP3 |
| 5.6 | NRL-168288 | `GP4.) Pop-ups can be closed in the following ways: 1) after time-out … 2) after pressing button that opened pop-up again … 3) when touching screen outside of pop-up 4) after making a selection inside the pop-up …` | 有，leaf 5 列 | 全數生成 TC |

**對帳**：7 項 = 生成來源 1（5.6）＋ 缺口 2（5.3、5.4）＋ 由他項涵蓋 1（5.5）
＋ 非行為條文 2（5、5.2）＋ 指向外部文件 1（5.1）。未歸屬 0。

## queue／priority 本體

下放包 §四-4 稱「queue／priority 本體行為無 SWE1 列」。實測支持之：
第 5 章唯一提及 priority 者為 5.1（指向 `HM/ Popup List Priority Matrix`）
與 5.4（GP2 之 priority 1／2），兩者皆無 SWE1 列。
**`queue` 一詞於 SYS1 export `Description` 欄掃描命中 0 次** ——
第 5 章 7 項 0 次，**全文件 167 列亦 0 次**（`re.findall("queue", …, re.I)`，
不分大小寫、不限詞界；`priorit` 於第 5 章同法命中 4 次）。亦即 feature
工單名稱中的 "Queue" 在**整份 Core HMI Logic and Flow 匯出內**無對應字樣。

**盲區聲明（R-G11）**：此掃描之對象為 SYS1 export 之 `Description` 欄文字。
規格 PDF 無文字層（本包實測，pdftotext／pdfplumber／pymupdf 三工具皆得 0
非空白字元），故**圖面內之文字未進入本次掃描** —— 若 queue 行為僅存在於
圖面，本掃描測不到。第 5 章之圖面（5.1／5.2）之判讀不在本包射程。

## RD-1 具名上報候選

- GAP-POP1（5.3 / GP1）：7" low radio 無 medium popup 模板
- GAP-POP2（5.4 / GP2）：Android Dialog = large / priority 2；
  Android Toast = small / priority 1
- 5.1 所指之兩份外部文件（DR-POP1／DR-POP2；repo 側候選見 A-POP2）
- 工單名稱之 "Queue and Priority Management" 與規格第 5 章之涵蓋範圍不一致

**本表不決定上報與否** —— RD-1 之送出屬 Pei（Tier 3）。
