# ANOMALIES — FW036 Diagnostics HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-DIAGnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

| 標記 | 事由 | 出處 | 型 | 狀態 |
|---|---|---|---|---|
| `[A-DIAG01]` | R-DIAG5(c) 之 NRC／SID 適用空白：230 列 negative／unsupported 中 205 列（89%）CFTS004 與 037 皆無 NRC 值；I/O Control SID `0x2F` CFTS004 零命中、SYSAD 零命中、僅 037 之 24 列明載 | 本包實測 `data/nrc_coverage.tsv`、`data/sysad_uds_tables.md` | 條文適用空白 | **PENDING** — 阻斷 CDD-02 之 negative／unsupported 批次；DECISIONS §2、DR-DIAG-1 |
| `[A-DIAG02]` | `R-DIAG` 四字母前綴不被 `scripts/ruling_anchor.py` 之 `RE_ANCHOR`（`R-[A-Z]{0,3}\d+`）接受，九條無法進 `RULINGS.sha.tsv`，R-G52 引用制對本 feature 失效 | `rulings_hash.py --target` 回報 0 錨點 | 全域工具 | **PENDING** — 升級 Pei；DECISIONS §6 |
| `[A-DIAG03]` | SYSAD 無 UDS 位元組序列表與 NRC 表；唯一序列表為 DTC 流程，而 037 之 DTC 提及列 = 0 | `data/sysad_uds_tables.md` §2 | 來源缺件 | **PENDING** — 不阻斷；DR-DIAG-2 |
| `[A-DIAG04]` | 598／5210 之前例衝突：R-DIAG7(b) 引 R-CAM2(b)「一律 0」，而已交付之 SWC 0708 工作簿 285 列中 202 列填 `1` | SWC 0708 `Test Case Specification` T..Z 欄實測 | 前例衝突 | **PENDING** — DECISIONS §3 保留事項 (2) |
| `[A-DIAG05]` | SWC 0708 自身欄位錯位：10 列之作者名 `PeiPYHsu` 落入 `T` 欄（HDCC27 Atl-Hi），車型七欄整體右移一格 | 同上 | 外部工作簿瑕疵 | **記錄** — 非本 feature 產物，不修；供 SWC 線參考 |

## Assumption markers

None yet（本包未產 TC）。Inline format in generated JSON reasoning: `[ASSUMPTION A-DIAGnn]`.
