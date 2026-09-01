# DATA_REQUESTS — Vehicle Setup Management R1 Low（VF665 V42）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VLn`），表列摘要與條目同步更新（R-ICS29 型教訓：不得雙表）。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中 **191** 列無 037 覆蓋（覆蓋揭露） | no | 母體外 191 列 | 已登記，未送出 | | |

---

## DR-VL1 —— V42 SYSRA 未被 037 覆蓋之 Functional 列

- **來源**：intake 實測（2026-09-01）。`FMWIFSM035A02_VF665_V42_…SYSRA_VF665_V42_Released.xlsx`
  `Analysis Report` 分頁 Functional Requirement 318 列；037 兩份之 Source Requirement ID
  （`Sys-RA-VF665_V42_VSM-nnn`）去重後對應 128 列。
- **實數回填（2026-09-01，下放包 02 W-4 跨源對帳）**：037 之 128 個 Functional
  Source ID **128／128 全數命中** SYSRA `Sys-RA-Feature-ID`（E16 相符）；惟其中
  **1 列**（`Sys-RA-VF665_V42_VSM-857`）於 SYSRA 之 `分類 Category` 為 `Heading`
  而非 Functional（A-VL7）。故被 037 覆蓋之 SYSRA **Functional** 列實為 **127**，
  未覆蓋為 **318 − 127 = 191**（原估「約 190」）。
  掃描條件：SYSRA `Analysis Report` 表頭列 5，`分類 Category` 全等
  `Functional Requirement`；037 兩檔表頭列 7／8，`Categorization` 全等
  `Functional Requirement`；比對為 Source ID 逐字。
- **問題**：其餘 **191** 列 Functional 無 SWE1 分析（037），依 R-VL4 不入 TC 範圍。
  請上游確認：(a) 該 190 列是否另有 037 報告在途；(b) 或其為刻意不分析之範圍
  （如 Out of Scope 之漏標）。
- **阻塞**：否。母體 128 之生成不受影響。
- **本地處置**：覆蓋台帳列出該 190 列之 `Sys-RA-Feature-ID` 與 `Chapter for VF`，
  標 `No 037 — out of mother set (R-VL4)`；交付說明揭露。
- **另記（A-VL6）**：該 318 列中 112 列之 `EE Architecture` 與 `Document ID`
  兩欄同時為空，無從判其是否適用本線（ATL-Mi／`VF665_V42_P637MCA`）；
  與本 DR 之交集未另計，不合併。
- **請求動作**：Pei 決定是否送出；送出則向 SWE1 報告作者索取在途清單。
