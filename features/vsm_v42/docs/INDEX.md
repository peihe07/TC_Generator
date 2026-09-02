# INDEX — vsm_v42（Vehicle Setup Management R1 Low）文件索引

FO §8.7：一次往返共用同一 `NN`；下放包由分析層寫，上繳包由執行層寫，
本索引由執行層於每次上繳時更新。

| NN | 下放包（handoff） | 上繳包（upstream） | 日期 | 結果 |
|---|---|---|---|---|
| 00 | `handoff/00_intake_and_rulings.md` | `upstream/00_intake_recon.md` | 2026-09-01 | **停於 W-1** —— `_intake/Vehicle_Setup_VF665/` 0 files，§三 #1–#5 原檔全缺（A-VL1）；W-1 完成（scaffold ＋ feature.yaml），W-2～W-6 未執行 |
| 01 | `handoff/01_sources_recon.md` | `upstream/01_sources_recon.md` | 2026-09-01 | **停於 W-0** —— `docs/fw036/RULINGS.sha.tsv` 仍為 `M`（下放包 01 第 6 節升級條件 1）；併觸 E17（新增列 17 ≠ 14，姊妹線已至 R-VT8）與 E18（R-VL2 節 sha8 因 R-TM13 加註而變，本體 `body_sha8` 未變）。A-VL3；W-1′～W-6 未執行 |
| 02 | `handoff/02_sources_recon.md` | `upstream/02_sources_recon.md` | 2026-09-01 | **W-0～W-6 全數執行**。E1–E25 全數相符／過（B-1 = 0）。sources 落 5 doc_id、`inputs/` 清空；leaves 152 列（128 leaf）；signal_chain 251 列。新開 A-VL5–A-VL9；A-VL1／A-VL3 轉 RESOLVED；DR-VL1 實數 191 |
| 03 | `handoff/03_signal_atlantis.md`（含 2026-09-02 補遺） | `upstream/03_signal_atlantis.md` | 2026-09-02 | **W-5′ v3（Atlantis 欄組 ＋ ATL-Mi DBC）／W-7／P3 前置**。E18″ 11/11、E26 過、E29 0/20、E27′ 98/98 有備註；**解得 98**、訊息名不符 40→7、**E28 = 1（K-1）**。DR-VL3 結案；A-VL8 阻塞面解除；新開 A-VL11（SG_ 5568 vs 844）／A-VL12（三對拼字）。台帳依 R-VL13 待 Pei 重生 |

## 報告（`docs/reports/`）

（無）
