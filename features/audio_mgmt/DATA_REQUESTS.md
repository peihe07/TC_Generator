# DATA REQUESTS — Audio Management (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/audio_mgmt/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

## 一、置檔清單（03 包 §一；執行層開工前置）

實測 2026-08-26：`inputs/` 為 scaffold 新建之空目錄，以下五件**全部未在位**。
03 包 §一 明訂「缺件即停，回報分析層」，故 B1 現為 BLOCKED。

| # | 檔案 — 全名 | Status | Batch impact | Urgency |
|---|---|---|---|---|
| 1 | `SWE_1_Audio_Management_Pending_For_Review.xlsx` | MISSING | 需求主源；缺則無 test_item 上半 verbatim 來源（R-S4） | 阻塞 B1 |
| 2 | `CFTS019AudioManagementPart1_released_20260415.xlsx` | MISSING | 錨源 Part 1（R-AM2） | 阻塞 B1 |
| 3 | `CFTS_019_Part2_All_AcceptedExceptDTCrework.xlsx` | MISSING | 錨源 Part 2（R-AM2）；B1 全 50 葉之錨落在此本 | 阻塞 B1 |
| 4 | `R1LR_Atl-H_25PI3_5_Multimedia_-_Radio_and_Audio_CFTS_019_Audio_Management_20250910_1235.pdf`（實為純文字，非 PDF） | MISSING | 章節上下文查閱 | 阻塞 B1 |
| 5 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | MISSING（**03 包 §一漏列**） | R-G1 母本複本 = 新簿基底（R-AM3）；缺則無簿可寫回。母本在 repo `forms/` 下，但 `resolve_path` 之 glob 基準為本 feature 目錄，故須複製一份進 `inputs/` | 阻塞寫回 |

## 二、上游資料請求（DR；01 包 §五、03 包 §七）

DR 送出屬 Pei；分析層僅代擬。

| DR | 內容 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-AM1 | SYS-RA-AMM-082..1111 ↔ CFTS019 ObjectID 正式對照表缺失（SYS2 CFTS019 主體分析報告未在案；Basic Report 橋接欄全空）。請上游提供對照或補件 | 待 Pei 送出 | 全 318 葉 | **不卡批** —— 過渡採 R-AM2 內容對位＋`PENDING: DR-AM1` 並行，回件後末站統一回填校正 | — | 中（回件前每批累積回填債） |
| DR-AM2 | SWE1_AMM_076 編號碰撞（SYS-RA-AMM-242 與 -246 同號）。請上游改號 | 待 Pei 送出 | 2 葉（076 兩條） | **不卡 B1** —— 076 不在 B1；B3 遇之依 R-AM6 照抄 `SWE1_AMM_076` | — | 低（B3 前送出即可） |
