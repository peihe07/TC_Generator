# 52 下放包 — 上游素材補入與缺件清單之收斂

**本包無裁決條文。**

## 一、素材

| 檔 | 缺件項 | 狀態 |
|---|---|---|
| `Pop_Up_List_HMI_R1_SR24_Post_2A__Dec_15__2023_.xlsx` | 第 4 項 | 待驗 |
| `Tutorials_HMI_Logic_and_Flow_R1_SR24_Post_2A_CR22839__March_20_2023_.pdf` | 第 5 項 | **到齊** |

**作業**：兩檔落 `inputs/`，`shasum -a 256` 列入 `BASELINE.sha256`，
`shasum -c` 全綠並附輸出。Tutorials 之 PDF 依 R-U25 之雙面原則處理
（**本 feature 之 spec 基線不變** —— 它是被引用之外部 spec，非基線之一面）。

## 二、DR #4 —— 實測確認為真缺口（分析層已量）

對上傳之 Pop Up List 全三分頁逐格掃 `PU_?\d{3,4}`，大小寫敏感：

| 項 | 值 |
|---|---|
| 檔內唯一 PU id 總數 | **1341** |
| `PU1087` / `PU1088` | **0 / 0** |
| `PU1089` / `PU1090` / `PU1091` | 1 / 1 / 1 |
| `PU0626`／`PU_0129`／`PU0588`／`PU0580`／`PU0841`／`PU0611`／`PU0091` | 各 1 |

**證據強度提升**：先前為「Comfort 副本 18/20」，現為
**「權威文件之 1341 個 id 中無此二者，而相鄰之 1089–1091 在」**。
**不是拿錯版本，是這一版沒有這兩列。**

**作業**：DR #4 更新其證據與索取標的
（「載有 PU1087／PU1088 之版本，或該二 popup 之內文」）。

## 三、Tutorials L&F 之三處 —— 依 Pei 本輪裁示

**範圍界線**：Tutorials 自身之行為屬其 spec 之 SWE 需求，**我方不驗**（§8.4.2）。
本文件之用途限於使我方既有 TC 之 ER 可觀察。

### 3.1 `TC-167` 之 ER4 —— **做**

現行 `Tutorials begin` 無可觀察形式。
依 `INTR3.)`：Video Bank 標題 `Tutorials`、副標 `Learn about new features`。

**作業**：ER4 補其可觀察形式；`specification_reference` 併列 Tutorials L&F 之節。
**不驗影片內容、不驗播放控制、不驗 4 支之數目** —— 那些是 Tutorials 之需求。

### 3.2 `INTR2.)`（下載既有 → 不進 Tutorials）—— **不追，但具名**

Pei 裁示：無法確定，不追。
037 未為其切 leaf，依 R-U56 為 OUT-OF-SCOPE。

**作業**：**具名於交付說明之留白清單**，寫法：
> Tutorials L&F `INTR2.)` 所述之行為（下載既有 profile 時 Tutorials 不顯示），
> 037 未為其產出需求項，本次交付未涵蓋。

**不是靜靜略過** —— 看的人要能自己判斷要不要補。

### 3.3 `Table EDPR1` 與 `INTR1.1)` 之比對 —— **做**

`INTR1.1)`（刪改後）：`“Tutorials” will be a list item in the “Edit Profile” section`。

**作業**：以 `render_spec_region.py` 重讀 p14 之 Table EDPR1，逐列比對是否含 `Tutorials`。
- **含而我方 ER 未列** → `TC-017`／`TC-074` 之 ER 有遺漏，屬 **defect**
- **不含** → 兩份 spec 記載不一致，登記 **anomaly** 並列入 RD 查詢；
  **不自行裁決何者為準**

## 四、缺件清單之收斂 —— 由 6 項改為 4 項

**分析層自陳**：第 6 項（車型 ↔ 變體條件對照）**列為缺件是列錯的**。
T:Z 已依 Comfort 先例定為留空，**交付不需要它**；
它是「若日後有人要求填 T:Z 才需要」之選配，非本次交付之缺件。

| # | 項 | 狀態 |
|---|---|---|
| 1 | `PU1087`／`PU1088` 之內文 | **缺**（本輪確認為真缺口）|
| 2 | R1 High label 覆寫之範圍（RD #5）| **缺**，查詢單已備未寄 |
| 3 | 車輛組合是否可佈署（RD #6）| **缺**，查詢單已備未寄 |
| 4 | Pop Up List 之逐步對映（`8.3`）| **待驗** —— 檔已到，能否支援須查 |
| ~~5~~ | Tutorials L&F | **到齊** |
| ~~6~~ | 車型 ↔ 變體條件對照 | **改列選配**，非缺件 |

### 第 6 項若日後需要，其問法（已具體化，不必漫找）

Tutorials L&F 之 Assumptions 頁載：
`Differences between Regions will be specified. If not specified,
refer to the **Market Config Table**.`

**該表即所需之文件類別。** 其最小充分形式為 **7 × 5**：
`HDCC27`／`DT27`／`VF(ProMaster)637`／`Commander(598)`／`Regengade(5210)`／
`Toro(2261)`／`Fastack(376)` 七個專案 ×
（是否搭載 User Profiles／R1 High 或 Low／螢幕尺寸／有無記憶座椅／有無連網）。

**給不了整份表，回覆該三十五格亦足。** 記入 `DATA_REQUESTS.md` 之選配段。

## 五、作業（另）

- 第 4 項之查驗：Pop Up List 是否含 New Profile Setup 之**逐步對映**
  （`8.3` 所需）。有則 `TC-169` 得補其 popup id；無則維持只驗形態，並具名。
- `DATA_REQUESTS.md` 改為單一清單，每項附：卡住哪幾條 TC、替代作法、
  答覆會改變什麼。

## 六、不在本包授權範圍

- 交付、RD 寄出 —— 屬 Pei
- 任何寫入性 git（R-G5／R-G12）
- 驗證 Tutorials 自身之行為
- remarks 之變更 —— 待 51 輪量測與 Pei 裁定

## 七、上繳

`docs/upstream/52_upstream_materials.md`，更新 `docs/INDEX.md`，附獨立判斷。
