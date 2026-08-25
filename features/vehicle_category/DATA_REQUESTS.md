# DATA REQUESTS — Vehicle Category (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/vehicle_category/inputs/`; each landing closes or advances the linked
DR。**DR 由 Pei 發出（Tier 3）；本檔僅登記，執行層不發送。**

來源：下放包 01 §六（`docs/handoff/01_intake_recon.md`）。序號於 01 包編定。
下放包 02 §四之裁定已併入：A-VC2 附於 DR-VC2，不單獨發。

| DR | 狀態 | 標的 | 阻斷範圍 |
|---|---|---|---|
| DR-VC1 | **未結** | 037 作者 | 僅 `SWE1-HMI-VC-021` |
| DR-VC2 | **未結** | 037 作者 | 不阻斷生成；交付前須有答覆 |
| DR-VC3 | **未結** | 037 作者 | 不阻斷本次交付；表 B 措辭取決於此 |
| DR-VC4 | **未結** | 規格作者 | 條件性 —— 待 DR-VC3 回覆 |
| DR-VC5 | **未結** | 037 作者 | 不阻斷（R-VC3 已裁全取）|

五筆全為未結。

---

## DR-VC1 —— Privacy Lock 彈窗之實際 PU 編號

- **標的**：037 作者
- **狀態**：未結
- **內容**：規格 §3.6（CO13）之 Privacy Lock 彈窗 id 於**規格原文即為字面
  `PUXXXX`**，非實 id；037 `SWE1-HMI-VC-021` 原樣沿用。請提供實際 PU 編號。
- **阻斷範圍**：僅 `SWE1-HMI-VC-021`。缺件期間該 TC 之對應欄填
  `PENDING: DR-VC1 Privacy Lock popup ID`（IN §8.4.3），不得留空、不得填 NA。

## DR-VC2 —— `SYS-HMI-RA-VC-###` 之來源系統與對應關係

- **標的**：037 作者
- **狀態**：未結
- **內容**：`Source Requirement ID` 欄之 `SYS-HMI-RA-VC-###`（61 個相異值）
  在 SYS1 export 全簿命中 0。請說明該 id 之來源系統，及其對 SYS1
  `NRL-######` 之對應關係。
- **阻斷範圍**：不阻斷生成（R-VC5(c)）。**交付前須有答覆**以完成雙向追溯。
- **實測佐證**：T4／T12 重測確認 `SYS-HMI-RA` 於 SYS1 三分頁
  （`Basic Report` / `Polarion` / `_polarion`）全儲存格出現次數為 **0**。
- **附帶一問（A-VC2，下放包 02 §四裁定）**：037 封面 `Reviewer：` 為空、
  `Date：` 為 `2020/09/05`，與修訂履歷（2025-12-26 ~ 2026-04-27）矛盾。
  請確認封面欄位是否為表單樣板殘留。**不單獨發 DR** —— 封面欄位不阻斷任何
  Phase，單獨往返一輪之成本高於其資訊價值。

## DR-VC3 —— 18 節有內容而 037 零涵蓋

- **標的**：037 作者
- **狀態**：未結
- **內容**：規格 §8.1–8.5、§9.1–9.2、§10.1–10.2、§11.9–11.9.3、§14.2、§15、
  §16.1、§16.2.1、§16.2.2 共 **18 節**有實質需求內容而 037 無對應需求。
  請確認係「刻意排除」或「分析遺漏」；若為前者，請提供排除依據與承接單位。
- **阻斷範圍**：不阻斷本次交付（R-VC3）。惟表 B 之措辭取決於此答覆。
- **關聯**：A-VC3 併入本 DR，不單獨發。
- **措辭依據（R-VC7）**：18 節之內容摘要**已於 T17 以 repo 內權威素材逐節
  重驗**（結果見上繳包 02 §7）。下放包 01 §4.2(b) 之原摘要係讀 Project 附件
  之衍生 PDF 所寫，**不得引為本 DR 之措辭依據，亦不得寫入表 B**；
  發出時一律採 T17 重驗後之內容。
- **T17 之實質發現（發出前須知）**：18 節中 **§15 與 §10.1／10.2 之關鍵內容
  在 repo 之權威素材中不可得** —— 其為圖檔，SYS1 `Description` 僅存
  `(image: imageNN.png)` 佔位。故本 DR 對該三節之提問應改為
  「該節內容僅存於圖，SYS1 匯出未帶文字」，而非引述任何摘要文字。

## DR-VC4 —— VF507 / VF352 兩份未附文件

- **標的**：規格作者
- **狀態**：未結
- **內容**：規格 §8.4 之 Cabrio 前提條件引 **VF507**、§14 之 EPB 逾時引
  **VF352**，二文件未附。
- **阻斷範圍**：**條件性** —— DR-VC3 回覆為「應補」時始為必要素材。
  DR-VC3 回覆前不催。

## DR-VC5 —— FROP 跨域 17 列之承接單位

- **標的**：037 作者
- **狀態**：未結
- **內容**：`FROP` 欄之 `Power Management`（16 列）與 `Audio Management`
  （1 列）共 17 列：其 TC 應由本 feature 產出，或由 FROP 所指之 feature 承接？
- **阻斷範圍**：不阻斷（R-VC3 已裁全取）。答覆到後若需縮限，以 `[OVERRIDE]`
  處理，不得回頭默默扣列。
- **本輪實測佐證**：T5 已測 —— 該 17 列與 `features/power/`、
  `features/power_moding/` 之既有 req_id 與 spec_reference **重疊 0 筆**。
