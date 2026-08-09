# batches-home.md — 62 leaf 批次分組表(7 批)

| Batch | 主題 | 條數 | Req IDs | Context 注入來源 |
|---|---|---|---|---|
| B1 | CarPlay Template + Default Layout | 5 | 020, 021, 032, 033, 034 | PDF p.8 HSD5.6/5.7/8.4-8.6; Pop Up List PU1291 |
| B2 | Shortcuts Edit | 10 | 048-01, 048-02, 048-03, 048-04, 048-05, 048-06, 049-01, 049-02, 050, 051 | PDF p.15 HSS4~4.3; LSW05/SW06 圖 |
| B3 | Shortcuts Lockout + Exclusion | 9 | 052-01, 052-02, 053, 054, 055-01, 055-02, 055-03, 056, 057 | PDF p.15 HSS2/5/6/6.1/6.2/7; A-H02 適用 055-03 |
| B4 | Shortcut Availability + Actions | 7 | 058, 059-01, 059-02, 059-03, 059-04, 060, 061 | PDF p.15 HSS8-10, p.17 SW7 表; Pop Up List PU1274 |
| B5 | Navigation Shortcuts | 12 | 062, 063, 064, 065, 066, 067, 068, 069, 066-01, 066-02, 070, 071 | PDF p.16 SNS1-10; A-H01 適用 066 |
| B6 | Brand Pages + Locking | 4 | 072, 073, 074, 075 | PDF p.18-19 BSP1-4; A-H04 適用 073 |
| B7 | Last Mode (BLOCKED until spec) | 15 | 076, 077, 078, 079, 080, 081, 082, 083, 084, 085, 086, 087, 088, 089, 090 | Last Mode Table L&F 缺檔; A-H03 |

總計 62 條(= 62 驗證)

## 各批附帶指示
- 每批 context = 037 該批原文列 + framework-home.md 對應 Test Set 節 + PDF 對應頁文字 + Arif 同類 exemplar 2–3 列 + sibling rows(含 Arif 區全部同 spec-section 列)
- B7 於 Last Mode spec 取得前僅產 blocked 標記列,不產 TC 內文
- popup 文字(PU0091/PU1274/PU1291/PU0942)一律由 Pop Up List 欄位原文注入,禁止 paraphrase