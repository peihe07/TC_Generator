# SXM — 202 leaf ↔ CFTS024 §1.5.x 章節分組表

Phase 4 產出，供 Phase 3 framework Part N 起草。來源：`data/stla_to_cfts.json`
（202/202 leaf 精確命中 CFTS024 條款錨點）。

Leaf id 在每一節內幾乎完全連續 —— 037 是照 CFTS024 文件順序編寫的，所以節界
就是天然的批次界，不需要另立分組軸。

| CFTS024 節 | 標題 | n | Leaf ids (SWE-RA-SXM-) |
|---|---|---|---|
| §1.5 | HU Satellite Audio | 1 | 001 |
| §1.5.1 | Seek Up | 8 | 006-013 |
| §1.5.2 | Seek Down | 8 | 014-021 |
| §1.5.3 | Tune Up | 5 | 002, 022-025 |
| §1.5.4 | Tune Down | 5 | 003, 026-029 |
| §1.5.5 | Tune by Direct Number Input | 2 | 030-031 |
| §1.5.6 | Preset Select | 4 | 004, 032-034 |
| §1.5.7 | Preset Save | 4 | 035-038 |
| §1.5.9 | Favorites (Sirius Seek) | 1 | 039 |
| §1.5.9.1 | Favorites - Store/Delete | 16 | 005, 040-054 |
| §1.5.9.2 | Activation | 8 | 055-062 |
| §1.5.10 | Instant Replay | 6 | 063-068 |
| §1.5.10.1 | Pause | 7 | 069-075 |
| §1.5.10.2 | Play | 6 | 076-081 |
| §1.5.10.3 | Rewind | 5 | 082-086 |
| §1.5.10.4 | Fast Forward | 6 | 087-092 |
| §1.5.11 | Sirius Browse | 11 | 093-103 |
| §1.5.12 | Browse All Channels | 3 | 104-106 |
| §1.5.12.1 | Browse Presets | 4 | 107-110 |
| §1.5.12.1.1 | Browse Genre | 2 | 111-112 |
| §1.5.12.1.2 | Browse Game Alerts/ Game Zone | 8 | 113-120 |
| §1.5.12.1.3 | Browse Jump / Browse Traffic/Weather | 3 | 121-123 |
| §1.5.12.1.4 | Browse Favorites (FAV) | 8 | 124-131 |
| §1.5.13 | Scroll Up/Down | 8 | 132-139 |
| §1.5.14 | Page Up/Down | 6 | 140-145 |
| §1.5.15 | Enter or Item Select | 5 | 146-150 |
| §1.5.16 | SiriusXM Traffic & Weather Now | 8 | 151-158 |
| §1.5.17 | Game Alert | 9 | 159-167 |
| §1.5.19 | Parental Skip | 8 | 168-175 |
| §1.5.20 | HU Satellite Audio Error Displays | 7 | 176-182 |
| §1.5.21.2 | Performance Requirements | 2 | 183-184 |
| §1.5.21.2.2 | General | 1 | 185 |
| §1.5.21.2.3 | User Notification During Buffering | 2 | 186-187 |
| §1.5.21.2.4 | Abnormal Transition Delays | 4 | 188-191 |
| §1.5.21.2.5 | Abnormal Display Behavior | 5 | 192-196 |
| §1.5.21.2.6 | Haptic Input | 2 | 197-198 |
| §1.5.21.2.7 | Fit and Finish | 4 | 199-202 |
| **合計** | **37 節** | **202** | |

## 分批提案（Phase 3 裁定）

依節合併成規模相近的批次，粗略對齊 AMFM 的 9–17 leaf/批：

| 提案批次 | 節 | n |
|---|---|---|
| Seek | §1.5.1, §1.5.2 | 16 |
| Tune | §1.5.3, §1.5.4, §1.5.5 | 12 |
| Presets | §1.5.6, §1.5.7 | 8 |
| Favorites | §1.5.9, §1.5.9.1, §1.5.9.2 | 25 |
| Playback | §1.5.10, §1.5.10.1–§1.5.10.4 | 30 |
| Browse | §1.5.11, §1.5.12, §1.5.12.1, §1.5.12.1.1–§1.5.12.1.4 | 39 |
| List Navigation | §1.5.13, §1.5.14, §1.5.15 | 19 |
| Traffic & Weather | §1.5.16 | 8 |
| Game Alert | §1.5.17 | 9 |
| Parental Skip | §1.5.19 | 8 |
| Error Displays | §1.5.20 | 7 |
| Performance & Finish | §1.5.21.2 及其子節 | 20 |
| **合計** | | **202** |

Favorites / Playback / Browse 三批偏大（25/30/39），Phase 3 可再切；
§1.5 的 001 與 §1.5.3/§1.5.4/§1.5.6/§1.5.9.1 各有一條離群 leaf
（001–005 落在文件前段），已併入所屬節。

§1.5.8、§1.5.12.1.5+、§1.5.18、§1.5.21.1、§1.5.21.2.1 無 leaf 認領 —
未配置條款清單見 `data/unallocated_clauses.json`（38 條，32 條為 SFR）。
