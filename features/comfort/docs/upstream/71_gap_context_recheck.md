# 71 — Comfort HMI / 20 個缺口之五層查證

- 產出層：執行層｜2026-08-17｜對象：分析層
- 對應：`docs/handoff/92_gap_context_recheck.md`（撰寫中）
- **未生成 TC、未改 RD-1、未寫回。**

---

## 0. 結論先講

**20 條之判定全部不變。** 但五層查證帶出三項此前未被說出的事實，
其中兩項改變了**問題該怎麼問**（非該不該問）：

| # | 事實 | 影響 |
|---|---|---|
| 1 | `some` 於 129 節**恰出現 5 次，其中 4 次是缺口之源頭** | §6.1 —— 缺口有一個可辨識之語言形態 |
| 2 | `019-02`／`-03` 之內容**第四層找到了**（`16.13` ICE12 逐項列出 MAX A/C 之參數），而 §8.2.1 禁止移植 | §4 —— 「找到而不得用」與「找不到」是兩種狀態，交付說明現在把它們寫成同一種 |
| 3 | `equipment type` 於 129 節**恰出現 1 次**（`2.12.1`），即該詞從未被定義 | §3 —— 九條之分割是**不完全分割**，其不完全處是條文自己寫的 `some` |

---

## 1. 查證方法

五層逐 leaf 機械執行（唯讀）：

| 層 | 所讀 |
|---|---|
| 一 | 該 leaf 對應之句 |
| 二 | 該節 `full_text` 全文（`data/section_fulltext.tsv`，不截斷）|
| 三 | **前一節、後一節、該章第一節**（依 129 節之 outline 排序取鄰）|
| 四 | `data/ch16_mirror_map.tsv` 與 `data/ch2_ch7_mirror_map.tsv` 之對造節全文 |
| 五 | 該節全文中之「暗示他處有定義」之詞（`equipment type`／`configuration`／`vehicle line`／`variant`／`as applicable`／`some vehicles`／`depending on`／`if equipped`／`if available`），**逐詞追其在全 129 節之其他出現處** |

---

## 2. `2.1` —— `001-01`／`001-02`（tab 集合與其順序）

| 層 | 所得 |
|---|---|
| 一 | `The comfort category will have **up to 4 tabs depending on vehicle configuration**` |
| 二 | 同節另三句：tab 之順序（`Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati), Massage, Rear`）、`If only Front climate is available in a specific vehicle the tabs will not be displayed`、以及指向 Massage Seats 文件 —— **順序有了，配置對照仍無** |
| 三 | 前節無（`2.1` 即章首）；後節 `2.2` 述硬控與觸控之同步，無關 |
| 四 | **兩張鏡射表皆 `no-counterpart`** —— ch16 十八節與 ch7 十一節皆無 tab 之存在或順序之對應節 |
| 五 | `configuration` 全 129 節 9 句（他節 8），逐句讀畢**無一給 tab 之對照**（其餘者為 MTC／dual AUTO／3 state recirc／single zone 等各自之配置）；`depending on` 2 句，他節 1 句為 `2.10` 之 `depending on equipment`，指 defrost 而非 tab |
| **附加** | `WS`／`R1 Low`／`Maserati` 三個車型代號於 129 節之出現：**`R1 Low` 與 `Maserati` 各 1 次、皆在 `2.1` 本句**；`WS` 2 次（`2.1` 與 `11.11` 之 `For vehicle programs such as WS that have haptic … buttons placed on the side of the radio`）—— **`11.11` 給了 WS 之一項性質，但那是按鍵位置，不是 tab 集合** |

**判定不變。** 條文具名了三個車型代號而**從未在他處定義其 tab 集合**。

---

## 3. `2.12` ／ `2.12.2` —— 九條（`016-01`…`-03`、`018-01`…`-06`）

| 層 | 所得 |
|---|---|
| 一 | `C13.) There are **4 Airflow Mode** displayed in this order…`（`2.12`）／`C13.1) If the Mode hard control is pressed…`（`2.12.2`）|
| 二 | 兩節全文讀畢：`2.12` 另述高亮、放大、主控顯示、一次一個；`2.12.2` 述循環順序、長按只跳一格、於 Climate main 內外之呈現差異 —— **兩節皆無適用車型之陳述** |
| 三 | **關鍵在後節**：`2.12.1` 之 `C13.0) **In some non-tri mode equipment types**, airflow modes has 5 states…` —— 條件寫在**下一節**，且它限定的是 5 狀態那一組，不是 C13 |
| 四 | `16.12`（ICE11）**5 狀態**，鏡射表記其為 `partial` 並明載「未涵蓋：C13 之**四模式**清單與其順序」；`7.8`（CR8）**3 狀態**（後排），記為 `mirrored` 惟模式數不同 |
| 五 | **`equipment type` 於全 129 節恰出現 1 次**，即 `2.12.1` 本句 —— **該詞從未被定義**；`tri-mode` 2 次：`2.12.1` 與 `3.1`（`On vehicles with Tri-Mode climate, there are 3 airflow mode buttons`）|

### 3.1 由第五層得出之一項較準確的描述

條文給的是一個**不完全分割**：

| 組 | 條文 | 適用者 |
|---|---|---|
| 3 個模式 | `3.1`（C19）| **Tri-Mode climate 之車輛**（有具名）|
| 5 個狀態 | `2.12.1`（C13.0）| **`some` non-tri mode equipment types**（有限定而不完全）|
| **4 個模式** | `2.12` （C13）| **無任何陳述** |

**其不完全處是條文自己寫的 `some`** —— 不是「非 tri-mode 者皆為 5 狀態」，
而是「某些非 tri-mode 者是 5 狀態」。**故連「剩下的就是 4 模式」這個推論
也推不出來**，因為 `some` 之補集裡有什麼，條文沒說。

**判定不變**，惟 RD-1 第 2 問若再修，此表比現行措辭更能讓上游一眼看見缺口在哪。

---

## 4. `2.13` —— `019-02`／`019-03`（MAX A/C）

| 層 | 所得 |
|---|---|
| 一 | `MAX A/C modifies multiple climate parameters. On/Off logic should follow requirements from **VF HVAC document**.` |
| 二 | 同節另述 CCM 轉達 MAX A/C 之存在、on/off 於畫面之高亮 —— **參數一項未列** |
| 三 | 前節 `2.12.2`（Mode 硬控）、後節 `2.14`（MTC）—— 皆無關 |
| 四 | **找到了**：`16.13`（ICE12）鏡射表記為 **`mirrored`**，而其全文逐項列出 —— `automatically turns on A/C, changes airflow modes to Face, increases fan speed at highest setting (7/7)…` |
| 五 | 該節無暗示詞 |

### 4.1 這一條之狀態與其他十八條不同

**第四層找到了內容，而 §8.2.1 禁止把它移植回 ch2。**
（上繳 38 §6.3 已記該不對稱：ch16 側因有明文而生成，ch2 側因委派而停下。）

**故 `019-02`／`-03` 不是「找不到」，是「找到而不得用」。**

現行交付說明將此二條與其餘十八條寫成同一句
（`hands its content to a document we do not have`），
**而「我們沒有那份文件」與「同一件事的另一面在別章寫著、但我們不得跨章移植」
是兩件不同的事**。前者是上游之缺件，後者是我方之方法論。

**建議**（不逕改）：交付說明就此二條另立一句，說明 EMEA ICS 章
（chapter 16）之對應行為**已被測試**，未測者為 chapter 2 委派出去的 on/off 邏輯。

---

## 5. 其餘四組

### 5.1 `2.5` —— `006-04`（recirc icon）

| 層 | 所得 |
|---|---|
| 二 | 同節另述 on/off、灰化、可自動開 AC、偵測不到車型時顯示通用符號 —— **通用符號那一半可驗，車型專屬那一半無對照** |
| 三 | 前節 `2.4`（AC）、後節 `2.5.1`（3 state recirc）、章首 `2.1` —— 無一給 icon 對照 |
| 四 | `16.4` `partial`（只涵蓋 on/off）；`16.5` `partial` —— **其措辭更具體**：`as displayed in the **Climate Main page table**`，**仍不是那張表** |
| 五 | 無暗示詞 |

**判定不變。** 第四層把「the table」變成「Climate Main page table」——
**多了一個名字，仍沒有那張表。**

### 5.2 `9.1` —— `039`（額外後排控制）

| 層 | 所得 |
|---|---|
| 二 | 該節**只有一句**（`CR11.`），無其他句 |
| 三 | 前節 `7.10`（4 Zone Climate 之兩溫區）、後節 `9.2`（**該變體之替代 fan popup**）—— **後節在描述該變體之行為，卻同樣不說誰是該變體** |
| 四 | **無對造** |
| 五 | `some vehicles` 全 129 節 4 句（他節 3：`2.3.1` dual AUTO、`2.5.1` 3 state recirc、`2.7.1` fan 1-8）—— **無一定義其所指之車輛** |

**判定不變**，且此前之 CFTS043 查證（17 列全部 `Scope = None`）仍為其外部側之陰性。

### 5.3 `14.15` —— `099`（可用之 comfort controls）

| 層 | 所得 |
|---|---|
| 二 | 該節**只有一句** |
| 三 | 前節 `14.14`（dual zone popup）、後節 `14.16`（座椅狀態列）、章首 `14.1`（pop-up list）—— 無一給對照 |
| 四 | **無對造** |
| 五 | `configuration` 9 句。**其中一句最接近**：`11.11`（R1HVS4）`Heated/vented seat, heated wheel **will not be displayed in the comfort section if the vehicle is configured with hard buttons for comfort controls**` —— 這是一個**顯示規則**（何時不顯示），不是**配置 → 可用控制項之對照** |

**判定不變**，惟第五層之所得值得記：**條文有一個相關的配置條件，
而它回答的是另一個問題。**

### 5.4 `16.16` —— `122-02`（座椅 off icon）

| 層 | 所得 |
|---|---|
| 二 | 同節另述 `Always show 'Driver' or 'Passenger'`、文字顏色、進入畫面時顯示現況 —— **這些已由他條涵蓋，缺者只有 icon 一項** |
| 三 | 前節 `16.15`（後視鏡除霧）、後節 `16.17`（VR 降風速）、章首 `16.2` —— 無關 |
| 四 | **`no-counterpart`** —— ch2／ch3 無對應節 |
| 五 | `configuration` 9 句，同 §5.3，無一為 icon 對照 |

**判定不變。** 其 `(see Climate section)` 於第二至五層皆未指向任何具體節。

### 5.5 `18.1` —— `129-01`…`-03`

| 層 | 所得 |
|---|---|
| 二 | 該節**只有一句**（`W0.)`）|
| 三 | **前節為 `17.5`（章 17 之末節）；無後節；`18.1` 自身即章首** —— 即**章 18 在 129 節內只有這一節**，`18.2`～`18.4` 未產出 leaf（profile §5.4 之 R-C16 缺口）。**「該章第一節之適用性宣告」在此不存在，因為沒有第二節可供宣告** |
| 四 | **無對造** |
| 五 | 無暗示詞 |

**判定不變。** 且第三層給出一項可寫進 RD-1 之事實：
**`17.5`（CW4）為章 17 帶了一個配置條件**（`For dual zone climate with dual
airflow modes equipped vehicles…`），**而章 18 一個都沒有** ——
兩章之不對稱不只在標題。

---

## 6. 兩項橫向發現

### 6.1 `some` —— 缺口有一個可辨識之語言形態

`some` 於全 129 節**恰出現 5 次**：

| 節 | 句 | 現況 |
|---|---|---|
| `2.3.1` | `**Some vehicles** with dual zone climate with dual airflow mode can have a configuration for dual AUTO modes` | 有 TC（其配置條件即該句自身，§8.5）|
| `2.5.1` | `**Some vehicles** have a configuration for a 3 state toggle recirc button` | 有 TC（同上）|
| `2.7.1` | `In **some vehicles** fan speed ranges for front hvac are: Off, 1-8` | 有 TC（同上）|
| `2.12.1` | `In **some** non-tri mode equipment types, airflow modes has 5 states` | **九條缺口之源頭** |
| `9.1` | `On **some vehicles** (See CFTS043 for details), there are additional Rear Climate controls and shortcuts` | **`039` 之缺口** |

**五句同一形態，三句有 TC、兩句是缺口。** 其分野不在 `some` 本身，
而在**該句有沒有同時給出可觀察之行為**：
前三句各自帶著行為（dual AUTO／三態 recirc／1-8 風速），故該 `some` 可作
§8.5 之條文自帶觸發條件；後兩句只宣告變體之存在，行為在別處或無。

**這使「哪些條文會變成缺口」在事前可預測** —— 掃 `some`／`certain`／
`in some vehicles` 之句，逐句問「它有沒有同時給行為」。
**本 feature 之 129 節已掃畢，5 句已全部有處置。**

### 6.2 第三層之空與第四層之空，意義不同

十組之中：

- **第三層（鄰節與章首）空者 6 組** —— 鄰節在講別的事，這是常態
- **第四層（鏡射對造）空者 5 組**（`2.1`／`9.1`／`14.15`／`16.16`／`18.1`）——
  **`no-counterpart` 是鏡射表自己記過的判定**，其依據欄逐條寫著為何無對造

**第四層之空是有依據的空，第三層之空只是空。** 前者可引為證據，後者不可。

---

## 7. 判定總表

| leaf | 節 | 判定 | 五層中最有價值之一項 |
|---|---|---|---|
| `001-01`／`-02` | 2.1 | **不變** | 三個車型代號（WS／R1 Low／Maserati）於 129 節僅出現於本句 |
| `006-04` | 2.5 | **不變** | 第四層把「the table」變成「Climate Main page table」—— 多一個名字，仍沒有那張表 |
| `016-01`…`-03` | 2.12 | **不變** | `equipment type` 全文僅 1 次；分割不完全，其不完全處是條文自己的 `some` |
| `018-01`…`-06` | 2.12.2 | **不變** | 同上（其循環依四模組而立）|
| `019-02`／`-03` | 2.13 | **不變** | **第四層找到了**（`16.13` 逐項列出），而 §8.2.1 禁止移植 —— 「找到而不得用」 |
| `039` | 9.1 | **不變** | 後節 `9.2` 描述該變體之行為，卻同樣不說誰是該變體 |
| `099` | 14.15 | **不變** | `11.11` 有一個相關之配置條件，而它回答的是另一個問題 |
| `122-02` | 16.16 | **不變** | `no-counterpart`，且 `(see Climate section)` 五層皆未指向任何節 |
| `129-01`…`-03` | 18.1 | **不變** | 章 18 在 129 節內只有這一節，**沒有第二節可供宣告適用性**；而章 17 之 `17.5` 帶了配置條件 |

**20 / 20 不變。**

---

## 8. 建議（不逕行）

1. **交付說明**：`019-02`／`-03` 另立一句（§4.1）—— 現行措辭把「沒有那份文件」
   與「有而不得跨章移植」寫成同一件事
2. **RD-1 第 2 問**：若再修，可附 §3.1 之三列分割表
3. **RD-1 第 6 問**：可補 §5.5 之不對稱（章 17 有配置條件、章 18 無）
4. **`RUNBOOK.md`**：§6.1 之 `some` 形態與 §6.2 之「兩種空」值得留檔 ——
   待分析層裁定是否寫入

**未做**：未生成 TC、未改 RD-1 與交付說明、未寫回、未動交付夾；git 未執行。
