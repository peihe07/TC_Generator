# VehicleCategory dry-run **v2** 摘要（VS-SL-02 §2.5）

日期：2026-09-02　**dry-run，未寫回**　明細：`vc_settings_dryrun_v2.tsv`（126 列）

## §A　實測

| 項 | v1 | **v2** |
|---|---:|---:|
| 報告列 | 126 | **126**（自檢 1 PASS） |
| `PROSE_PRECOND` | 71 | 71 |
| `NO_MAPPING` | 53 | **43** |
| `PROSE_KEPT`（新，§2.5：保留散文、移除 `NO_MAPPING`） | — | **16** |
| `ALWAYS_FALSE` | 4 | 4 |

`PROSE_KEPT` 16 列 = `Controls buttons under test` 4 ＋ `Specialty features` 4 ＋
`portrait display` 4 ＋ `landscape display` 3 ＋ 1 列同時含二句。
依審閱 §4-9：**無 PROXI 可表述者，散文即正確形態，不開 DR。**

## §B　`Camera App` 2 列之判定（審閱 §4-8：讀需求原文，不由分析層猜）

| 列 | D 欄 | `test_item` 逐字 |
|---|---|---|
| r23 | `SWE1-HMI-VC-008` | `VC3.) If the vehicle has the Camera App (see Camera HMI Logic and Flow), Cameras will appear as a tab.`　（括號下半：`Presence of the Cameras tab, delegating the Camera App behaviour itself`） |
| r24 | `SWE1-HMI-VC-009` | `VC3.1.) If the Camera tab is present, remove Cameras from the Controls tab.`　（括號下半：`Suppression inside the Controls list, the second consequence of the same trigger`） |

**判定：指 `Cam App`，非 `Backup Cam`。**
理由（逐字證據）：原文寫 `the Camera App`，與总控表 **No.196 `Cam App`** 同名；
且明指 `see Camera HMI Logic and Flow`，為 App 層而非後視鏡頭訊號。
`Backup Cam`（总控表 No.7，`Rear_View_Camera` = 1 (Present)）**在該 2 列原文中未出現**。

**惟仍有矛盾，故列入 DR**：总控表 No.196 `Cam App` 之 Atlantis 欄逐字為 `Always false`，
若成立則 Cameras tab 永不出現，與 `Cameras will appear as a tab` 相衝。
依 R-VS85 不出負向；正向 2 列之 PROXI 因需求原文無 `$var$` 而為 `PENDING`。

## §C　仍列 DR 者

`Vehicle Category feature` 之「具備與否」16 列（`Vehicle_Category` 為列舉值 M1／M2／N1／N2，
非存在性參數，依 R-13 不得代入）＋ §B 之 2 列。見 `features/vehicle_setting/DATA_REQUESTS.md` 之未取號 DR 草稿。
