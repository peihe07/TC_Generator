# DATA_REQUESTS — Vehicle Setup Management R1 Low（VF665 V42）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VLn`），表列摘要與條目同步更新（R-ICS29 型教訓：不得雙表）。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中 190 列無 037 覆蓋（覆蓋揭露） | no | 母體外 190 列 | 已登記，未送出 | | |

---

## DR-VL1 —— V42 SYSRA 未被 037 覆蓋之 Functional 列

- **來源**：intake 實測（2026-09-01）。`FMWIFSM035A02_VF665_V42_…SYSRA_VF665_V42_Released.xlsx`
  `Analysis Report` 分頁 Functional Requirement 318 列；037 兩份之 Source Requirement ID
  （`Sys-RA-VF665_V42_VSM-nnn`）去重後對應 128 列（待 recon 逐 ID 對帳，本數為
  037 Functional 列數 68 ＋ 60 之和，未扣重複、未驗 ID 落點）。
- **問題**：其餘約 190 列 Functional 無 SWE1 分析（037），依 R-VL4 不入 TC 範圍。
  請上游確認：(a) 該 190 列是否另有 037 報告在途；(b) 或其為刻意不分析之範圍
  （如 Out of Scope 之漏標）。
- **阻塞**：否。母體 128 之生成不受影響。
- **本地處置**：覆蓋台帳列出該 190 列之 `Sys-RA-Feature-ID` 與 `Chapter for VF`，
  標 `No 037 — out of mother set (R-VL4)`；交付說明揭露。
- **請求動作**：Pei 決定是否送出；送出則向 SWE1 報告作者索取在途清單。
