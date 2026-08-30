# CFTS Embedded Objects — 全 feature 查核表（R-G28 追溯適用第一段）

> **本表全部為事後補查，日期 2026-08-30。**
> 其產物為**今天之事實**，**不表述為「當時已查」**（`FO §9.2 R-G28` 追溯適用之拘束，
> 下放包 56 §二 #3）。既有各 feature 之「未記明」**不追改為「已查」**，其洞具名留著。

- 掃描對象：`~/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/
  Reference Documents/CFTS Embedded Objects/`
- 該路徑下共 **9 個目錄、151 個嵌入物件檔**
- 判準：以各 feature 之 `feature.yaml`／`RECON.md` 所載之**母 CFTS 編號**對照該目錄

---

## 1. 目錄側（供對照）

| 目錄 | 檔數 | 被哪個 feature 認領 |
|---|---:|---|
| `CFTS001` | 2 | **無人認領** |
| `CFTS013` | 13 | **無人認領**（`display` 之次要來源提及 CFTS013） |
| `CFTS019` | **31** | `audio_mgmt`（母）、`projection`（次要） |
| `CFTS024` | **16** | `amfm`（母）、`sxm`（母） |
| `CFTS025` | **46** | `projection`（DR#8 之標的，非母） |
| `CFTS028` | 12 | **無人認領** |
| `CFTS036` | 2 | **無人認領** |
| `CFTS057` | **6** | **`sw_update`（母）—— 已辦**（上繳包 46） |
| `CFTS069` | 23 | **無人認領** |

---

## 2. feature 側（20 個）

| feature | 母 CFTS | 目錄存在？ | 檔數 | 第二段（出表）之時程 |
|---|---|:--:|---:|---|
| `amfm` | **CFTS024** | ✅ | **16** | **待辦** —— 隨其下一批 |
| `audio_mgmt` | **CFTS019** | ✅ | **31** | **待辦** —— 隨其下一批 |
| `sxm` | **CFTS024** | ✅ | **16** | **待辦**（與 `amfm` 同目錄，出表可共用） |
| `projection` | CFTS085（母）／CFTS025（DR#8） | ✅（`CFTS025`） | **46** | **待辦** —— 惟其為 DR 標的非母 spec，優先序由該線裁 |
| **`sw_update`** | **CFTS057** | ✅ | 6 | **已辦**（上繳包 46；由圖找列見上繳包 47 §3.1、48 §DR-SU4） |
| `display` | CFTS020 | ❌ | — | 已查、無此目錄 |
| `ics_management` | CFTS020 | ❌ | — | 已查、無此目錄 |
| `driver_distraction` | CFTS022 | ❌ | — | 已查、無此目錄 |
| `privacy` | CFTS022 | ❌ | — | 已查、無此目錄 |
| `power` | CFTS009／CFTS010 | ❌ | — | 已查、無此目錄 |
| `power_moding` | CFTS044 | ❌ | — | 已查、無此目錄 |
| `vehicle_setting` | CFTS044 | ❌ | — | 已查、無此目錄 |
| `time_management` | CFTS015 | ❌ | — | 已查、無此目錄 |
| `bed_lowering` | **無母 CFTS**（HMI Logic and Flow ＋ 037） | — | — | 不適用 |
| `comfort` | **無母 CFTS**（HMI Settings List ＋ 037） | — | — | 不適用 |
| `home` | **無母 CFTS** | — | — | 不適用 |
| `media` | **無母 CFTS** | — | — | 不適用 |
| `popup` | **無母 CFTS**（跨 feature 台帳） | — | — | 不適用 |
| `user_profiles` | **無母 CFTS** | — | — | 不適用 |
| `vehicle_category` | **無母 CFTS**（VF507／VF352） | — | — | 不適用 |

---

## 3. 結果

| 類 | feature 數 |
|---|---:|
| **有嵌入物件、待出表** | **4**（`amfm`／`audio_mgmt`／`sxm`／`projection`） |
| 有嵌入物件、已出表 | **1**（`sw_update`） |
| 已查、其母 CFTS 無此目錄 | **8** |
| 無母 CFTS，不適用 | **7** |
| **合計** | **20** |

> ### ⚠ 兩項須注意
>
> 1. **`CFTS019`（31 檔）與 `CFTS025`（46 檔）之規模是 `CFTS057`（6 檔）的 5–8 倍。**
>    sw_update 之六物件中有二張載有未見於 docx 之數值（四個門檻、一段 UDS 序列）——
>    **若其比率相近，`audio_mgmt` 與 `projection` 各有約十張圖可能載有規格值。**
> 2. **四個目錄無人認領**（`CFTS001`／`CFTS013`／`CFTS028`／`CFTS036`，共 29 檔）——
>    **其可能對應到尚未開案之 feature，亦可能對應到某 feature 之次要來源。**
>    **本表不推定，只記其為未認領。**

---

## 4. 未辦事項（本表不代辦）

- **各 feature 側之記錄**：R-G28 令記入「各該 feature 之 `RECON.md` 或等價處」。
  **執行層未逕改他 feature 之台帳** —— `ics_management`／`driver_distraction` 等線
  正由平行 session 編輯中，逕改會與其衝突。**本表為全域落點，各線引用即可。**
- **第二段（出表）**：四個待辦 feature 之「由圖找列」二欄表，隨其各自之下一批。
