# 裁決台帳（FW036 全案）
欄位：編號｜日期｜標題｜狀態｜出處包｜適用範圍
狀態：ACTIVE / [DEFAULT] / SUPERSEDED / WITHDRAWN
規則：條文全文僅於本台帳落檔一次，各包引用編號不重抄。
撤銷之裁決以刪除線保留並附區塊引註，不得刪除（R-TM13）。

| 編號 | 日期 | 標題 | 狀態 | 出處 | 範圍 |
|---|---|---|---|---|---|
| R-1 | 2026-08-21 | 訊號記法三層 | ACTIVE | 01a | 全案 |
| R-2 | 2026-08-21 | spec_reference 家族分流 | ACTIVE | 01a | 全案 |
| R-3 | 2026-08-21 | test_item 上半 50 token | ACTIVE | 01a | 全案 |
| R-4 | 2026-08-21 | verbatim 首字轉大寫 | ACTIVE | 01a | 全案 |
| R-5 | 2026-08-21 | 雙語制合法化不回修 | [DEFAULT] | 01a | BT/Projection |
| S1 | 2026-08-21 | 舊規 superseded | ACTIVE | 01b | 09_ 目錄 |
| S2 | 2026-08-21 | §11 收斂 | ACTIVE | 01a | 全案 |
| S3 | 2026-08-21 | lint 出貨 gate | ACTIVE | 01b | pipeline |
| S4 | 2026-08-21 | test_item 括號下半 | ACTIVE | 01a | 全案 |
| S5 | 2026-08-21 | 裁決台帳制 | ACTIVE | 01b | 流程 |
| S6 | 2026-08-21 | 缺件 PENDING 佔位 | ACTIVE | 01a | 全案 |
| N-1 | 2026-08-21 | N 規制單位為 item，子步驟與續行同受規制 | ACTIVE | 00c/00d | lint |

## 條文落檔位置

| 編號 | 條文全文所在 |
|---|---|
| R-1 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5 |
| R-2 | 同上 §10.7 |
| R-3 | 同上 §4.3.1 |
| R-4 | 同上 §4.3.1 |
| R-5 | 同上 §1（`[OVERRIDE-R5][DEFAULT]`） |
| S1 | 本檔（標記行為見 `docs/fw036/upstream/01b_mechanism_setup.md`） |
| S2 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |
| S3 | `scripts/lint036.py` module docstring |
| S4 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §4.3.1 |
| S5 | `docs/fw036/FEATURE_ONBOARDING.md` §8.9 ＋ 本檔 |
| S6 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.4.3 |
| N-1 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |
