# INDEX — vsm_v42（Vehicle Setup Management R1 Low）文件索引

FO §8.7：一次往返共用同一 `NN`；下放包由分析層寫，上繳包由執行層寫，
本索引由執行層於每次上繳時更新。

| NN | 下放包（handoff） | 上繳包（upstream） | 日期 | 結果 |
|---|---|---|---|---|
| 00 | `handoff/00_intake_and_rulings.md` | `upstream/00_intake_recon.md` | 2026-09-01 | **停於 W-1** —— `_intake/Vehicle_Setup_VF665/` 0 files，§三 #1–#5 原檔全缺（A-VL1）；W-1 完成（scaffold ＋ feature.yaml），W-2～W-6 未執行 |
| 01 | `handoff/01_sources_recon.md` | `upstream/01_sources_recon.md` | 2026-09-01 | **停於 W-0** —— `docs/fw036/RULINGS.sha.tsv` 仍為 `M`（下放包 01 第 6 節升級條件 1）；併觸 E17（新增列 17 ≠ 14，姊妹線已至 R-VT8）與 E18（R-VL2 節 sha8 因 R-TM13 加註而變，本體 `body_sha8` 未變）。A-VL3；W-1′～W-6 未執行 |
| 02 | `handoff/02_sources_recon.md` | `upstream/02_sources_recon.md` | 2026-09-01 | **W-0～W-6 全數執行**。E1–E25 全數相符／過（B-1 = 0）。sources 落 5 doc_id、`inputs/` 清空；leaves 152 列（128 leaf）；signal_chain 251 列。新開 A-VL5–A-VL9；A-VL1／A-VL3 轉 RESOLVED；DR-VL1 實數 191 |
| 03 | `handoff/03_signal_atlantis.md`（含 2026-09-02 補遺） | `upstream/03_signal_atlantis.md` | 2026-09-02 | **W-5′ v3（Atlantis 欄組 ＋ ATL-Mi DBC）／W-7／P3 前置**。E18″ 11/11、E26 過、E29 0/20、E27′ 98/98 有備註；**解得 98**、訊息名不符 40→7、**E28 = 1（K-1）**。DR-VL3 結案；A-VL8 阻塞面解除；新開 A-VL11（SG_ 5568 vs 844）／A-VL12（三對拼字）。台帳依 R-VL13 待 Pei 重生 |
| 04 | `handoff/04_p3_framework.md` | `upstream/04_p3_framework.md` | 2026-09-02 | **P3：W-8～W-12**。R-VL15/16 落地（v3 就地更新 9 列）→ **E32 B-1 = 0、解得 99**；framework Layer 3 回填 **21/24**（3 家族未對映）；**E34 十組全相符（128）**；E36 六條；leaves 加 `test_set`；新建 val_tables（98 訊號/300 值）與 ba_sendtype（99 列）；DECISIONS 待簽。**W-9 未照字面辦**（三件 xlsx 早由 power 登錄，改補 R-G15 反向記載）。E33/E37 各一項不符公式，已歸因 |
| 05 | `handoff/05_pilot_epb.md` | `upstream/05_pilot_epb.md` | 2026-09-02 | **P4/P5 pilot：EPB Maintenance Mode 17 leaf**。W-0 GenSigSendType 列舉查得（1=OnWrite/3=OnChange/7=NoSigSendType）；W-1 規格節 1047–1117 切出、17/17 對映；**W-2 產出 17 TC**（generated/b1_epb，35 檔）；**E38–E45 全過**、§9 機讀 14 項全 PASS。PENDING 6（3 內部訊號，DR-VL4）。§K 四項待裁。**未寫工作簿、未寫 delivered/**（R-VL20） |

## 報告（`docs/reports/`）

（無）
