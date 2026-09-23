# 欄級 diff — CAM-07 → CAM-08（四目錄 72 列之句式修正）

下放包 `down/20260923_CAM-08.md` §2 ／ 審閱 `down/20260923_CAM-07_review.md` §二（五型）。
**變動 21 列**（pilot02 3／batch01 1／batch01b 3／batch02a 14）；其餘 51 列逐字未動。
本檔置於 `generated/` 根目錄 —— 其範圍跨四個批次目錄。

---

## 型 1 —— CAN source 行之適用條件（R-CAM3(f)，selfcheck 第 5 項）

掃描 72 列，**命中 17 列**，全數處置：

| TC | 目錄 | 命中理由 | 處置 |
|---|---|---|---|
| `-005`／`-006` | pilot02 | 無 `Send CAN` 步 | 刪該行，其後各行順延 |
| `-008` | pilot02 | 未同時勾兩 EE（只 2261／376）| **刪該行 ＋ 補正訊息名**（見下）|
| `-022` | batch01 | 無 `Send CAN` 步 | 刪該行 |
| `-045` | batch01b | 無 `Send CAN` 步 | 刪該行 |
| `-058`／`-059`／`-060`／`-061`／`-064` | batch02a | 未同時勾兩 EE（只 2261）| 刪該行 |
| `-062`／`-063` | batch02a | 未同時勾兩 EE ＋ 無 `Send CAN` 步 | 刪該行 |
| `-066` | batch02a | 未同時勾兩 EE（只 637）| 刪該行 |
| `-069`／`-070` | batch02a | 未同時勾兩 EE（只 Atl-Hi）| 刪該行 |
| `-071`／`-072` | batch02a | 未同時勾兩 EE（只三 Atl-Mi）| 刪該行 |

**`NR1L-RVC-008` 為實質缺陷，非版面**：該列只勾 `Toro(2261)`／`Fastack (376)`（Atl-Mi），
而 Procedure 步 5／6 誤用 Atl-Hi 之訊息名。

| 欄 | CAM-07 | CAM-08 |
|---|---|---|
| `test_procedure` 步 5 | `Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)` | **`Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)`** |
| `test_procedure` 步 6 | `Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D)` | **`Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)`** |
| `pre_conditions` 第 3 行 | `CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)` | **（刪）** |

其 sibling `NR1L-RVC-007`（勾 HDCC27／DT27／637，跨兩 EE 且有 `Send CAN` 步）
**未命中，CAN source 行保留** —— 即本條所欲保護之正例。

## 型 2 —— 設定操作句式（canon §5.8(e)，selfcheck 第 6 項）

掃描 72 列，**命中 6 筆 ／ 4 列**：

| TC | CAM-07 | CAM-08 |
|---|---|---|
| `-062` | `Select "Rear View Camera Active Guidelines" and set it to on` | `Set "Rear View Camera Active Guidelines" = "On"` |
| `-063` | 同上 `… to off` | `Set "Rear View Camera Active Guidelines" = "Off"` |
| `-067` | `Select "ParkView Backup Camera Delay" and set it to on／off`（兩步）| `Set "ParkView Backup Camera Delay" = "On"／"Off"` |
| `-068` | `Select "Rear View Camera with Rear Door" and set it to on／off`（兩步）| `Set "Rear View Camera with Rear Door" = "On"／"Off"` |

ER 同步：`The "<label>" setting is on／off` → **`The "<label>" setting is set to "On"／"Off"`**。
`"On"`／`"Off"` 之大小寫取 `HMI Settings List` `Settings` 分頁該列 `D` 欄
`On/Off Checkbox`（row 467／468／470），與 pilot `NR1L-RVC-007` 步 4 之既有寫法一致。

`NR1L-RVC-048` 之 ER `The Surround View camera setting is off` **不改** ——
該列依 §8.4.1 刻意不指名 label（審閱 §四-1 確認正確），無 `"<label>"` 可套句式。

## 型 3 —— CAN 讀取句式（§8.7.5(d)）與 `is transmitted` → `is sent`

| TC | 欄 | CAM-07 | CAM-08 |
|---|---|---|---|
| `-062` | proc 步 4 | `Read the bus analyzer recording and check TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req` | `Read TELEMATIC_VEHICLE_SETUP.DynamicGrid_Req and check that it is 1 (Dynamic Gridlines ON)` |
| `-063` | proc 步 4 | 同上 | `… and check that it is 0 (Dynamic Gridlines OFF)` |
| `-045` | proc 步 3 | `Read the bus analyzer recording and check RADIO_B3.CameraDisplaySts and the time …` | `Read RADIO_B3.CameraDisplaySts and check that it is 3 (View_3), and check the time …` |

`is transmitted` → `is sent`：**9 列** —— `-038`／`-040`／`-045`／`-062`／`-063`／
`-069`／`-070`／`-071`／`-072`（各 1 處）。

**未改為 §8.7.5(d) 者**：`-038`／`-043`（`SVC_SoftBtn_Rq`／`TGW_DISP_STAT` 之值為
`PENDING: DR-CAM-j`，無 raw 可寫）與 `-069`～`-072`（`PowerShutDownNotifcation` 為 LVDS，
非 CAN，四本 DBC 無其 `VAL_`）—— 維持 bus analyzer 之讀取措辭，於上繳包 §2 具名。

## 型 4 —— `Hold for <n>` 獨立成步（§8.7.5(f)）

`-069`／`-072` 兩列：

| 欄 | CAM-07 | CAM-08 |
|---|---|---|
| `test_procedure` | `3. Hold for 5 s and check the supply to the RVCM on the LVDS link`（3 步）| `3. Hold for 5 s`<br>`4. Read the LVDS supply to the RVCM and check that it is still present`（**4 步**）|
| `expected_result` | `3. The HU keeps supplying power to the RVCM over LVDS for 5 s`（3 項）| `3. The signal is held for 5 s`<br>`4. The HU is still supplying power to the RVCM over LVDS`（**4 項**）|

proc/er 行數維持對齊（lint `E` ＝ 0）。

## 型 5 —— 品牌行之濫用（R-CAM5(e)）

| TC | 欄 | 處置 |
|---|---|---|
| `-068` | `pre_conditions` | **刪** `The vehicle brand is Ram (HDCC27, DT27, 637)`，其後一行順延 |

依據：其所操作之 `HMI Settings List` row 470 `Rear View Camera with Rear Door` **無 `*`**，
不涉品牌軸。`-062`／`-063`（row 468 有 `*`）與 `-067`（row 467 有 `*`）之品牌行**保留**；
pilot `-007`／`-008`（row 467）亦保留。

---

## 未動之列

**變動之 21 列**：`-005`／`-006`／`-008`（pilot02）、`-022`（batch01）、
`-038`／`-040`／`-045`（batch01b）、`-058`～`-064`／`-066`～`-072`（batch02a 14 列）。

**未動之 51 列**：
pilot02 `-001`～`-004`、`-007`、`-009`、`-010`（7 列）
batch01 `-011`～`-021`、`-023`～`-033`（22 列）
batch01b `-034`～`-037`、`-039`、`-041`～`-044`、`-046`（10 列）
batch02a `-047`～`-057`、`-065`（12 列）
