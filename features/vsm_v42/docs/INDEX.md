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
| 06 | `handoff/06_pilot_rev.md` | `upstream/06_pilot_rev.md` | 2026-09-02 | **pilot b1 修訂輪（R-VL21 REV-1/2/4）**。-046 刪不可觀察之 timer 步與 bus-error ER、補 status On ER；Fdbk 族 9 條補前置發起步、削回讀步（族內一致）。**E46/E47/E48/E49 過**（改 20 檔、不動 14 檔 diff = 0）；**E50 = 1** —— 與 E46 在 -053 上衝突，依明文範圍不動並回報。新增 §K K-5（退出側請求路徑規格未載）／K-6（-054 歸屬）。R-VL21 body_sha8 `fde2fc91` |
| 07 | `handoff/07_b1_freeze.md` | `upstream/07_b1_freeze.md` | 2026-09-02 | **b1 微修（R-VL22）**。-053 ER1 改 is received；-054 量測後判 **in-mode 型**（段 1092–1096 掃 entering/exiting/request 命中 0，對照 1066/1099 有詞）刪發起步；-046 design_method → 功能測試。**E53/E54/E55 過**（改 6 檔，其餘 diff = 0）；**E56 = 16/17** —— -059 之 test_item 上半為句內剪接（本執行層於 05 所造），修法備妥但該條不在範圍，未改。**b1 凍結聲明附條件保留**，待 -059 一列裁定。R-VL22 body_sha8 `1d91e1b5` |
| 08 | `handoff/08_freeze.md` | `upstream/08_freeze.md` | 2026-09-02 | **-059 一列（R-VL23 A 路）→ `b1 FROZEN`**。test_item 上半改 037 完整原句 verbatim（42 token，逐字子字串 True）；括號下半／Procedure／ER／PENDING／remarks 一字未動。**E62/E63/E64 全過**（E63 = 17/17；改 2 檔，其餘 33 檔 diff = 0）。INDEX 落凍結表（34 檔 sha8）。R-VL23 body_sha8 `a9b6218d` |
| 09 | `handoff/09_writeback_method.md` | `upstream/09_writeback_method.md` | 2026-09-02 | **寫回工法查證（未寫回）**。實測：openpyxl `save()` **即使不改一格也毀 x14 DV**（members 48→47、x14 1→0）；`surgical_save` 保住（members 48、x14 節點逐字含 GUID，只有目標分頁 XML 變動，B 欄公式未被覆蓋）。**lint 本線首跑**（假資料件，9 紅全為假資料產物）；揭出文字形自檢未涵蓋之 7+ 項，b1 對其唯讀預檢 12 項全 0。`writeback_map_b1.tsv` 落檔（列 10–26／NR1L-VSM42-001–017）。**E69–E72 全過**；`sandbox/base` 一位元不動 |

## 報告（`docs/reports/`）

（無）
