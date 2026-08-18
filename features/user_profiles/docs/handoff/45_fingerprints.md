# 45 下放包 — 第五批覆核完成與靜態轉錄之時效

**本包無裁決條文。** 44 輪上繳**核可**。

## 覆核進度

- 本輪讀畢 `TC-150`～`TC-156`（**6 條**，`24b` 後段）
- 累計 **147 / 189**；餘 **42 條**（`24b` 前段 5 ＋ `33a` 17 ＋ `33b` 16 ＋ 校正 4）

## 發現

### AB-1（defect）`TC-154` 之 ER4 未指明所讀之對象，其斷言恆真

6.4（NOPR3）逐字：

> `Pressing “Get Started” will initiate the New Profile Setup
> (but **carry-over all current preferences linked to the active Profile**,
> without a popup to confirm).`

條文之重點為**新建之 profile 繼承現用者之偏好**。而本條：

| | |
|---|---|
| 步驟 4 | `Read the preferences and compare them with those recorded in step 1` |
| ER4 | `The preferences are unchanged from those recorded in step 1` |

**未指明所讀者為誰之偏好。** 若讀成「現用（預設）profile 之偏好未被動到」，
該斷言在任何實作下皆真 —— 包括一個**起始設定但完全不帶入偏好**之實作。
§7 之 false pass。

**改**：步驟 4 與 ER4 指明所讀者為**設定流程中之新 profile 之偏好**，
ER4 斷言其與步驟 1 所記者**相同**（carry-over 成立），
而非「未改變」。

**連帶自檢**：全批凡 ER 以「unchanged／remains the same／differs from」
與前步之紀錄比對者，逐條確認**比對之兩端各屬何物**已於 procedure 明指。
兩端同物者為恆真，兩端未指名者為歧義。**命中 0 亦回報。**

## 已讀 6 條中值得記下的三處

1. **`TC-153` 之 ER3 為逐 profile 之隔離** ——
   條文寫 `turn off the setting … for that Profile`；
   一個把該設定存成**全域**之實作，只驗 A 不再顯示會通過。
   **與 `018-02` 之 Z-1 完全同形，而這次是生成當下就寫對的。**
2. **`TC-155` 之 pre-condition 刻意把上次分頁設為 `Edit Profile`** ——
   否則 5.1 之 latch 與本條之「固定到 All Profiles」給出相同結果，
   兩者不可分辨。**同一設置同時使 `054` 與 `055` 各自成立。**
3. **`TC-152` 之 ER2 為缺席斷言，且其判定不依賴二次 popup 之內容** ——
   故不因 RD #5 之 label 答覆而變（J-7 之正確套用）。

## 採納 44 輪三項獨立判斷

### G-F：靜態轉錄一律加指紋（§5-1）

執行層自陳：對「重生成會使 X 過期」想了兩輪，兩輪都沒想到 X = review pack。
**成因是把時效性當成「檢查」之性質，而它是任何靜態轉錄之性質。**

**現已加指紋者**：四份 review pack。
**尚未加而同型者**：`26_rd_queries` 系列、`34_provenance5` 及其後之各批出處對照。
**本輪補齊**，逐份具名其指紋所涵蓋之內容。

### G-G：`--verify` 由產出方在上繳時附結果（§5-2）

指紋之價值全在**覆核前真的跑一次**，而它不像其他 16 支閘會被例行跑到。
**由執行層於每輪上繳附四份 pack 之當前 `--verify` 結果** ——
較「分析層記得跑」可靠，因為它不依賴另一層記得做一件事。

### G-H：他 feature 之先例，須先確認母本同一（§5-3）

44 輪 §三之常規（無先例則先查他 feature 交付件）補一句邊界：

> **Comfort 之先例可用，是因為兩個 feature 用的是同一份表單母本。
> 若他 feature 用的是別的表單，其填法不構成先例，只是參考。**

## 作業

1. AB-1：`TC-154` 修正 ＋ 比對兩端之全批自檢
2. G-F：`26_rd_queries` 系列與各批出處對照加指紋
3. G-G：上繳格式加「四份 pack 之 `--verify` 結果」
4. G-H：補入 profile 之該常規
5. 重跑全閘，貼輸出

## 不在本包授權範圍

- 交付、RD 寄出 —— 屬 Pei
- 任何寫入性 git（R-G5／R-G12）

## 上繳

`docs/upstream/45_fingerprints.md`，更新 `docs/INDEX.md`，附獨立判斷。
