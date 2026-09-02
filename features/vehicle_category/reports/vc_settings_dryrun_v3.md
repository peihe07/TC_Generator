# VehicleCategory dry-run **v3** 摘要（VS-SL-03 §1）

日期：2026-09-02　明細：`vc_settings_dryrun_v3.tsv`（126 列）

本 feature 之列不經別名綁定，**v3 與 v2 之報告內容相同**：

| 項 | 數 |
|---|---:|
| 報告列 | **126**（自檢 PASS） |
| `PROSE_PRECOND` | 71 |
| `NO_MAPPING` | 43 |
| `PROSE_KEPT` | 16 |
| `ALWAYS_FALSE` | 4 |

`Camera App` 2 列（r23／r24）判為 `Cam App`（非 `Backup Cam`），逐字證據與其
與总控表 No.196 `Always false` 之衝突，見 DR 稿第二節。

沙盒寫回稿：`features/vehicle_category/sandbox/vssl/vc_vssl.xlsx`
—— Glove Box／Mirror Dimmer 等可對應者已補 PROXI（Pre 改 71 列）；
`PROSE_KEPT` 16 列不動；`Camera App` 2 列 PENDING。
