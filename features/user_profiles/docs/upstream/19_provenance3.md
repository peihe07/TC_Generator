# 上繳 19（作業 6）— 第二批 29 條之 ER 出處對照

- 產出層：執行層｜2026-08-18｜對象：分析層（**判讀由分析層為之**）
- 對照對象：`generated/` 之 TC-045 ～ TC-073，**共 92 句 ER**
- 格式同 18 輪；四類來源依 J-4／J-12：`spec`／`方法`／`裁決`／`測試設置`

## 0. 總計

| 關係 | 句數 |
|---|---|
| 逐字引用 | 21 |
| 改寫自 | 38 |
| 由該句推得 | 12 |
| 無直接出處（步）步驟回聲 | 19 |
| **無直接出處（方法）** | **1**（TC-066 ER2，§5.6 界前值）|
| **無直接出處（測試設置）** | **1**（TC-056 ER1／ER3 之座椅編號，計為一處）|
| **無直接出處（真缺口）** | **0** |
| 合計 | **92** |

**「方法」與「測試設置」不再計入真缺口** —— 依 J-4／J-12，
它們是**已具名之非 spec 來源**，不是找不到出處。

---

## 1. 逐條對照

### 12.1–12.4（TC-045 ～ TC-053）

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 045 | 1 | —— | 步 |
| 045 | 2 | 12.1 `activating Valet Mode like creating a new Profile from the default preferences` | 改寫自 |
| 045 | 3 | 12.1 `store any updated preferences until Valet Mode is exited` | 改寫自 |
| 045 | 4 | —— | 步 |
| 045 | 5 | 12.1 `treat Exiting Valet Mode like deleting the profile` | **由該句推得**（刪除該 profile ⇒ 原 profile 之偏好回來）|
| 046 | 1 | —— | 步 |
| 046 | 2 | —— | 步 |
| 046 | 3 | 12.1.1 `Status bar will always need to return to the default status bar setup when Valet Mode is active so the Profile icon is always visible` | **逐字引用** |
| 047 | 1–2 | 12.2 `can only be activated through the button on the All Profiles tab` | **由該句推得**（「只能」之反面）|
| 047 | 3 | 12.2 同上 | **逐字引用** |
| 048 | 1 | —— | 步 |
| 048 | 2 | —— | 步 |
| 048 | 3 | 12.2.1 `Valet Mode button is greyed out while the vehicle is in motion` | **逐字引用** |
| 048 | 4 | 12.2.1 `a popup will indicate that the function is not available (Pop-up ID PU0091)` | **逐字引用**（PU0091）|
| 049 | 1 | —— | 步 |
| 049 | 2 | 12.3 `a 4 digit one-time PIN is required to be entered` | 改寫自 |
| 049 | 3–4 | 12.3 同上 | 改寫自／由該句推得 |
| 050 | 1 | —— | 步 |
| 050 | 2 | 12.3.1 `the same 4 digit PIN needs to be entered` | **由該句推得**（不同之 PIN 應被拒）|
| 050 | 3–4 | 12.3.1 同上 | **逐字引用**（`same … 4 digit PIN`）|
| 051 | 1–2 | —— | 步 |
| 051 | 3 | 12.3.2 `Disconnecting the battery will override and reset Valet mode and the system will load the last known Driver Profile at the next key on` | **逐字引用** |
| 052 | 1–3 | —— | 步 |
| 052 | 4 | 12.3.3 `should return to previous Profile after exiting/deactivating Valet Mode` | 改寫自 |
| 053 | 1 | —— | 步 |
| 053 | 2 | 12.4 `treat as a cancel command` | **逐字引用** |
| 053 | 3 | 12.4 同上 | **由該句推得**（取消 ⇒ 未進入）|

### 12.5–12.8（TC-054 ～ TC-060）

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 054 | 1 | —— | 步（基準線）|
| 054 | 2 | —— | 步 |
| 054 | 3 | 12.5 `indicated in the status bar with a lock symbol combined with the Profile icon` | **逐字引用** |
| 055 | 1 | —— | 步 |
| 055 | 2 | 12.6 `“Function not available while in Valet Mode. Do you want to deactivate Valet Mode”` | **逐字引用**（含原文未加問號）|
| 056 | 1 | —— | 步；**`memory seat 1` 之編號為測試設置（J-12）** |
| 056 | 2 | —— | 步 |
| 056 | 3 | 12.7 `pushing the memory seat buttons will only change the seat position but will not load the associated Driver Profile` | 改寫自 |
| 057 | 1 | 12.8 `Only HVAC and Media sections will be available` | **由該句推得**（Media 可用為對照）|
| 057 | 2–3 | 12.8 `In Media, the Device Manager will be locked out` | 改寫自 |
| 058 | 1 | 12.8 `Projection mode and native HFP will be disabled` | **逐字引用** |
| 058 | 2 | 12.8 同上 | **逐字引用** |
| 058 | 3 | 12.8 `VR will not be active` | **逐字引用** |
| 058 | 4 | 12.8 `Only HVAC and Media sections will be available` | 改寫自（§7 之對照）|
| 059 | 1–2 | 12.8 `It will not be possible to interact with the Status Bar with the exception of the Valet Profile and HVAC icons` | 改寫自 |
| 059 | 3 | 12.8 同上（例外側）| **由該句推得** |
| 060 | 1 | —— | 步 |
| 060 | 2 | 12.8 `All non interactable items will be greyed out` | **逐字引用** |

### 12.8.1–12.10.1（TC-061 ～ TC-068）

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 061 | 1 | —— | 步 |
| 061 | 2 | 12.8.1 `show PU0832 when prompting to enter Valet Mode` ＋ `Valet Mode will enable “electronic” Glove Box Lock` | 改寫自 |
| 062 | 1 | —— | 步（基準線）|
| 062 | 2 | —— | 步 |
| 062 | 3 | 12.8.1 `Glove Box Lock button is greyed out when Valet Mode is activated` | **逐字引用** |
| 063 | 1 | 12.8.1 `If the Glove Box Lock button is pushed while greyed out` | **由該句推得**（按壓不生效）|
| 063 | 2 | 12.8.1 `PU0833 will indicate that function is not available while in Valet Mode` | **逐字引用** |
| 064 | 1–3 | —— | 步 |
| 064 | 4 | 12.8.2 `the glove box will return to its last state upon deactivating Valet Mode` | 改寫自 |
| 065 | 1 | —— | 步 |
| 065 | 2 | 12.9 `10 attempts … before system cancels the deactivation` | 改寫自 |
| 065 | 3 | —— | 步 |
| 065 | 4 | 12.9 `The user can try again in 30min` | **由該句推得**（30 分鐘內不受理）|
| 066 | 1 | 12.9 同上 | 改寫自 |
| 066 | **2** | —— | **無直接出處（方法）** —— 29 分鐘仍鎖定為 §5.6 之界前基準線 |
| 066 | 3 | 12.9 `The user can try again in 30min` | 改寫自 |
| 066 | 4 | 12.9 同上 | **由該句推得**（可再試 ⇒ 計數已重置）|
| 067 | 1 | 12.10 `grey out the Go button until 4 digits are entered` | **逐字引用**；**3 碼為測試設置** |
| 067 | 2 | 12.10 `If Go is pressed while greyed out` | 由該句推得 |
| 067 | 3 | 12.10 `play Bonk tone and display the popup “PIN must be 4 digits”` | **逐字引用** |
| 067 | 4 | 12.10 `until 4 digits are entered` | **由該句推得**（對照）|
| 068 | 1 | 12.10.1 `Once 4 digits are entered` | 由該句推得（基準線）|
| 068 | 2 | —— | 步 |
| 068 | 3 | 12.10.1 `grey out all numeric buttons` | **逐字引用** |

### ch13–ch14（TC-069 ～ TC-073）

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 069 | 1 | 13.1 `when it detects a SPAAK key with Valet Mode permissions` | **逐字引用** |
| 069 | 2 | 13.1 `no PIN code will be required to enter or exit Valet Mode` ＋ `will automatically activate` | 改寫自 |
| 070 | 1–2 | 13.2 `The SPAAK user cannot exit Valet Mode from the head unit` | 改寫自 |
| 070 | 3 | 13.2 `Any screens or popups that may allow a user to exit Valet Mode must be blocked (PU0934, etc)` | **逐字引用** |
| 071 | 1 | 13.3 `If the SPAAK user presses the Profiles icon with the lock` | **逐字引用** |
| 071 | 2 | 13.3 `popup PU1573 will display` | **逐字引用** |
| 072 | 1 | 14.1 | 步 |
| 072 | 2 | 14.1 `the welcome popup will indicate the vehicle is in Valet mode, with a button to deactivate it` | 改寫自 |
| 072 | 3 | **12.3.1**（`above` 之實際指涉，本輪複位）`the same 4 digit PIN needs to be entered` | **由該句推得** |
| 073 | 1 | —— | 步 |
| 073 | 2 | 14.2 `If Profile section is attempted to be accessed while in Valet Mode while the vehicle is in motion` | 改寫自 |
| 073 | 3 | 14.2 `the user will see a popup (Pop-up ID PU0394)` ＋ `cannot be deactivated while the vehicle is in motion` | **逐字引用** |

---

## 2. `pre_conditions` 之字面值與範圍層級（J-5）

### 2.1 字面值

| 字面值 | 出現於 | 出處 | 關係 |
|---|---|---|---|
| `4-digit PIN` | 049／050／065／066 | 12.3 `4 digit one-time PIN` | 逐字 |
| `SPAAK key with Valet Mode permissions` | 069 | 13.1 同字串 | **逐字** |
| `electronic Glove Box Lock` | 061／062／063／064 | 12.8.1 `“electronic” Glove Box Lock` | 逐字（引號為 spec 原樣）|
| `memory seat 1` | 056 | —— | **測試設置**（12.7 只說 `the memory seat buttons`）|
| `30 minutes`／`29 min` | 066 | 12.9 `30min` ／ **方法** | 逐字／§5.6 |
| `10 attempts` | 065／066 | 12.9 同字串 | 逐字 |
| `3 digits`／`4 digits` | 067／068 | 12.10／12.10.1 `4 digits`；**3 為測試設置** | 逐字／測試設置 |
| `projection-capable device` | 058 | 12.8 `Projection mode` | 由該句推得 |
| `Valet Mode is active`／`not active` | 全批 | ch12 各節 | 逐字 |

### 2.2 變體／排除條款之範圍層級

| 條款 | 出處 | 層級 | 依據 |
|---|---|---|---|
| `If vehicle is equipped with Glove Box Lock` | 12.8.1 | **句級** | 僅約束 PU0832 之顯示；同節其餘句（按鈕變灰、PU0833）以「配備」為隱含前提，故 062／063 亦列該 pre-condition |
| `When Valet mode is enabled by SPAAK` | 13.1 | **節級** | 整條 PVALSPK1 為 SPAAK 情境 |
| SPAAK 情境（13.2／13.3）| 13.2／13.3 | **節級** | 兩節皆以 SPAAK 為主詞 |
| `with the exception of the Valet Profile and HVAC icons` | 12.8 | **句級** | 僅約束狀態列互動該句，非整條 PVAL8 |
| `In Media, the Device Manager will be locked out` | 12.8 | **句級** | 例外之例外 —— Media 可用而其中一項不可用 |

**本批無表級／列級之變體條款** —— ch12–14 無表格。

---

## 3. 本表之盲區（R-G11）

1. **`spec` 與「由該句推得」之界線仍由人判**，同 17／18 輪。
2. **「只能／不得」類之條文，其反面 ER 一律落在「由該句推得」** ——
   本批有 047（只能經 All Profiles 啟用）、050（須相同 PIN）、
   059（例外項仍可用）三處。**它們的推理方向相同**：
   由「只有 X」推出「非 X 者無」。**若該推理不成立，三條會一起錯。**
3. **未查 `test_procedure` 之字面值**（同前兩輪；J-5 只擴及 `pre_conditions`）。
4. **12.8 之四條 leaf 共用同一段 `pdf_text`** ——
   其 ER 之出處皆指向該段之不同句子，**本表以句為單位標示**，
   但 `specification_reference` 只能記到節（`12.8`），
   **無法在引用欄裡分辨四條各驗其中哪一句**。
