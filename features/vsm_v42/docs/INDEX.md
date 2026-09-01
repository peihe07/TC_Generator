# INDEX — vsm_v42（Vehicle Setup Management R1 Low）文件索引

FO §8.7：一次往返共用同一 `NN`；下放包由分析層寫，上繳包由執行層寫，
本索引由執行層於每次上繳時更新。

| NN | 下放包（handoff） | 上繳包（upstream） | 日期 | 結果 |
|---|---|---|---|---|
| 00 | `handoff/00_intake_and_rulings.md` | `upstream/00_intake_recon.md` | 2026-09-01 | **停於 W-1** —— `_intake/Vehicle_Setup_VF665/` 0 files，§三 #1–#5 原檔全缺（A-VL1）；W-1 完成（scaffold ＋ feature.yaml），W-2～W-6 未執行 |
| 01 | `handoff/01_sources_recon.md` | `upstream/01_sources_recon.md` | 2026-09-01 | **停於 W-0** —— `docs/fw036/RULINGS.sha.tsv` 仍為 `M`（下放包 01 第 6 節升級條件 1）；併觸 E17（新增列 17 ≠ 14，姊妹線已至 R-VT8）與 E18（R-VL2 節 sha8 因 R-TM13 加註而變，本體 `body_sha8` 未變）。A-VL3；W-1′～W-6 未執行 |
| 02 | `handoff/02_sources_recon.md` | `upstream/02_sources_recon.md` | 2026-09-01 | **W-0～W-6 全數執行**。E1–E25 全數相符／過（B-1 = 0）。sources 落 5 doc_id、`inputs/` 清空；leaves 152 列（128 leaf）；signal_chain 251 列。新開 A-VL5–A-VL9；A-VL1／A-VL3 轉 RESOLVED；DR-VL1 實數 191 |

## 報告（`docs/reports/`）

（無）
