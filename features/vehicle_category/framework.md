# FW036 Vehicle Category HMI — Framework Part N

- 裁決依據：**R-VC16**（Pei 2026-08-26，下放包 07 §一）——
  Layer 2 邊界准、#5 名稱采 `Settings List`。
- 母體標註依 **R-VC15**：本檔凡引用計數必標母體，限
  `145 列` ／ `117 leaf` ／ `66 section` ／ `108 outline` 四者。
- 驗算腳本：`scripts/verify_partn.py`（五個 assertion，見 §5）。
- 分組規則之單一實作：`scripts/partn.py` 之 `test_set()`。
  **規則為權威，本檔之節次清單為其展開結果**（R-VC16）。

---

## 1. 三層之定義與去向

| Layer | 本 feature 之值 | 去向 |
|---|---|---|
| Layer 1 — Test Group | `Vehicle Category`（R-VC1）| 工作簿 **G 欄** |
| Layer 2 — Test Set | **8 組**（§2）| 工作簿 **H 欄** |
| Layer 3 — spec section | 66 section（**66 section 母體**）| **不入工作簿** |

### Layer 3 之二禁（IN §4.1.5）

1. **不得存為任何欄值。** Layer 3 是分組與追溯的內部座標，不是交付欄位。
2. **不得串接進 Test Set 名稱。** 不寫 `Settings List 12.3`；
   H 欄之值恆為 §2 表之八個名稱之一，無後綴、無章節號。

section 與 TC 之關聯由 **`specification_reference`（工作簿 N 欄）**承載，
其值逐字取 037 `HMI Source ID` 欄原值（R-VC4）。
**那是 traceability 欄位，不是 Layer 3 欄位** —— 二者形似而職能不同：
前者答「這條 TC 追溯到規格何處」，後者答「這條 leaf 歸哪一組」。

---

## 2. Layer 2 —— 8 個 Test Set

| # | Test Set | leaf | section | 節範圍 | `Sub Categorization` |
|---|---|---|---|---|---|
| 1 | `Category Structure` | 24 | 13 | 2.2 – 2.6.3 | HMI |
| 2 | `Controls` | 17 | 12 | 3.1 – 3.9 | HMI |
| 3 | `Glove Box` | 12 | 8 | 4.1 – 7.1 | HMI |
| 4 | `Settings Behavior` | 15 | 6 | 11.1 – 11.6 | **Service** |
| 5 | `Settings List` | 30 | 17 | 11.7 – 12.8 | HMI |
| 6 | `Ignition Availability` | 16 | 8 | 13.1 – 13.5 | **Service** |
| 7 | `Brake Service` | 2 | 1 | 14.1 | HMI |
| 8 | `Cabrio Widget` | 1 | 1 | 16.2 | HMI |
| | **合計** | **117 leaf** | **66 section** | | |

leaf 之區間 1–30；排除 #7／#8 後為 12–30。

### 邊界規則（R-VC16，規則為權威）

```
章 2                → Category Structure
章 3                → Controls
章 4 / 5 / 6 / 7    → Glove Box
章 11，次級節號 ≤ 6 → Settings Behavior
章 11，次級節號 ≥ 7 → Settings List
章 12               → Settings List
章 13               → Ignition Availability
章 14               → Brake Service
章 16               → Cabrio Widget
```

「章」取 037 `HMI Source ID` 尾段章節號之首段；
「次級節號」取其第二段（`11.7.1` 之次級節號為 **7**）。

---

## 3. 分組判準

### 3.1 §4.1.2 之二來源：先退化，再由 `Sub Categorization` 救回

IN §4.1.2 要求 Layer 2 候選取二來源之交集：
(i) spec table of contents、(ii) RD analysis report grouping。

本 feature 之 (ii) 起初退化 —— 037 之 `HMI Source ID` 就是規格章節號，
兩來源同源，交集法失去交叉驗證作用。

**但 037 另有一個獨立於章節之分群軸：`Sub Categorization`。**
其於 **117 leaf 母體**之分布為 HMI 101 ／ Service 16，
**章 11 為唯一混章**，且其切分連續、`Sub Categorization` 之切換次數 = 1：

```
11.1 – 11.6     → Service（15 leaf）    設定項之行為與可用性
11.7 – 11.8.1   → HMI    （ 5 leaf）    清單之版面與呈現
```

即 037 作者在章 11 內部，把「設定做什麼」與「清單長什麼樣」切開了 ——
**這是規格目次看不見的邊界**，二來源於此不同源，交集法恢復作用。

### 3.2 ⚠ 弱點揭露（R-VC16(b)，不得因已簽署而略去）

| Test Set 邊界 | 支撐來源 |
|---|---|
| **#4 / #5 之分界（11.6 ｜ 11.7）** | **二來源**（規格目次 ＋ `Sub Categorization`）|
| 其餘 **7 個**邊界 | **單一來源**（規格目次）|

**8 組之中只有 1 個邊界有交叉驗證。**
`Sub Categorization` 除章 11 外與章界完全重合，未提供額外資訊
（十一章中十章為章內單一值）。

此弱點於 Layer 2 簽署後**依然存在** —— 簽署解決的是「採哪一個切分」，
不是「該切分有幾個來源背書」。記於此，以免日後被讀成已消解。

### 3.3 #5 之合併（11.7–11.8.1 併入章 12）

二者同為 `Sub Cat = HMI`、同為 Settings 頁籤之呈現與互動，
setup pattern 與 UI entry path 共用。若獨立成組僅 5 leaf，觸 §4.1.3
「too granular」。依 §4.2「Prefer broader shared capability when unsure」
→ 合併。

### 3.4 已排除之三個替代案

| 替代 | 內容 | 不採之理由 |
|---|---|---|
| 甲 | `Brake Service` 併入 `Ignition Availability`，成 `Conditional Availability`（18 leaf）| 形態雖近（狀態阻擋＋彈窗），但 037 之 `Sub Categorization` 將二者分屬 HMI／Service —— **二來源皆指向分立**，合併等於推翻上游分群 |
| 乙 | 章 11 不切，`Settings`（20 leaf）＋ `Settings Interaction`（25 leaf）| 章 11／12 之邊界僅有規格目次支撐；而 11.1–11.6 與 11.7–11.8.1 之分界有二來源。**捨強從弱** |
| 丙 | `Cabrio Widget` 併入 `Category Structure` | widget 位於 Home Screen，非 Vehicle Category 頁籤內，setup 與 entry path 皆不共用 |

### 3.5 命名

八個名稱皆為 §4.2 所要之英文名詞片語、無 Test Group 前綴、無動作標籤。
#5 之 `Settings List` 為 Pei 2026-08-26 所采（候選另有
`Settings Presentation`、`Settings Interaction`）——
`Presentation` 偏窄（章 12 之內容以互動為主）、`Interaction` 則丟失
11.7–11.8.1 之版面成分；`Settings List` 與 #4 之 `Settings Behavior`
形成「設定項之行為 ↔ 設定清單這個物件」之對比。

### 3.6 FROP 之對應（R-VC16(e)）

- `FROP = Power Management` 之 **16 列（145 列母體）**，
  其章別分布為 `{'13': 16}`，即全部落在 **#6 `Ignition Availability`**。
- `FROP = Audio Management` 之 **1 列（145 列母體）**
  （`SWE1-HMI-VC-048-02`，§12.3.2）落在 **#5 `Settings List`**。

R-VC3 之表 A 據此編製。**此為成員集合之比對結果，非計數相等之推論**
（R-VC15）。

**成員比對方法（R-VC17 之書寫要求）**：取 145 列母體中
`FROP == "Power Management"` 之列，以其 `HMI Source ID` 尾段章節號之
首段分群，得 `Counter({'13': 16})` —— 即該集合之**每一個成員**皆落於
章 13，非「二者各有 16 個」。`Audio Management` 之 1 列同法逐列確認。

> 反例留存：於 **117 leaf 母體**上，章 13 為 `Power Management` 12
> ＋ `Vehicle Settings` 4，**不是** 16 ＋ 0。
> 「章 13 之 16 leaf 恰等於 FROP=PM 之 16 列」曾被寫入下放包 05 §2.3，
> 為跨母體互援，已由 R-VC15 作廢（`docs/REVISIONS.md` REV-11）。

---

## 4. 待補節對 #7／#8 之影響（R-VC16(c)）

#7（2 leaf）與 #8（1 leaf）觸 §4.1.3 之「filter 後應得有意義之群」測試。
**其保留非 outlier 特許**，而係二者皆為「待補節會使其長大」之組：

| 組 | 現有（117 leaf 母體）| 表 B 中之待補節（66 section 母體外之未引用節）| 補後規模 |
|---|---|---|---|
| #7 `Brake Service` | 2 leaf | §14.2（彈窗優先序）、§15（EPB 彈窗）| 2 + N |
| #8 `Cabrio Widget` | 1 leaf | §16.2.1、§16.2.2 | 3 |
| （另）Cabrio 本體 | 0 leaf | §8.1–8.5、§9.1、§9.2（7 節）| 7 節 |

**現在把它們併入他組，等於為一個已知會逆轉的狀態做結構調整。**

DR-VC3 回覆為「應補」時，此二組之邊界**須重審**：屆時章 8／9 之
Cabrio 本體應**另立 `Cabrio Rooftop`，不得併入 #8** —— 二者之
setup 與 entry path 不同（widget 在 Home Screen，本體在 Controls）。

### 4.1 11.9 群之條件性歸屬（R-VC16(d)）

11.9 群（11.9／11.9.1／11.9.2／11.9.3）現為 037 零涵蓋，落於表 B 之
**17 section**（66 section 母體外）。若 DR-VC3 回覆「應補」而該群進入範圍：

**歸 #5 `Settings List`，非 #4 `Settings Behavior`。**
§2 之規則「章 11，次級節號 ≥ 7」已涵蓋之，不需另設例外。

依據（下放包 06 §二，以權威複本 SYS1 `Description` 實測）：
11.9 是觸控之通則，12.3 是同一能力之具體規格（並增旋鈕路徑）；
二者之驗證標的同為「使用者對一個設定列做出動作後發生什麼」，
非 #4 之標的（設定項本身做什麼）。

連帶之行為重疊（11.9.1 ↔ 12.3、11.9.3 ↔ 12.3.1）已登記 **A-VC12**，
屆時須裁其分工以免觸 IN §8.2.1 之重複追溯。

---

## 5. 驗算（`scripts/verify_partn.py`）

分組以 `partn.test_set()`（R-VC16 之規則）實作，**不硬編 leaf 清單**。

| # | assertion | 判 |
|---|---|---|
| 1 | leaf 合計 == 117（117 leaf 母體）| PASS |
| 2 | section 合計 == 66（66 section 母體）| PASS |
| 3 | 各組 leaf 數與 section 數與 R-VC16 驗算目標逐組相符 | PASS |
| 4 | 無 leaf 落於二組或零組 | PASS |
| 5 | 各組 `Sub Categorization` 為單一值 | PASS |

**5 checked / 0 failed。** 原始輸出見 `docs/upstream/07_framework.md` §4。

資料件：`data/layer3_map.tsv`（117 列，117 leaf 母體）、
`data/test_set_map.tsv`（66 列，66 section 母體）。

---

## 6. Layer 3 對照表 —— 逐 Test Set 之 section 明細

> **本節為規則之展開結果，非權威。** 二者若不一致，以 §2 之規則為準，
> 並視為本節已過期（重跑 `scripts/build_partn_maps.py` 即可重生）。
> req_id 之 `SWE1-HMI-VC-` 前綴於本節省略。

### 1. `Category Structure` — 13 sections / 24 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 2.2 | 3 | `001-01`, `001-02`, `001-03` | Vehicle Category screen exposes the Controls and Settings tabs as its pr |
| 2.3 | 1 | `002` | When the vehicle is equipped with Specialty features, render them as tab |
| 2.3.1 | 1 | `003` | Order the Vehicle Category tabs by the fixed priority: 1) My Car, 2) Cam |
| 2.3.2 | 1 | `004` | The user-visible label for the Controls tab is the literal string 'Contr |
| 2.3.3 | 1 | `005` | The user-visible label for the Vehicle Settings tab is the literal strin |
| 2.3.4 | 1 | `006` | Specialty features eligible to appear as tabs include Off Road, PHEV, an |
| 2.4 | 5 | `007-01`, `007-02`, `007-03`, `007-04`, `007-05` | Adopt the Vehicle Tab Label and Order mapping table as the authoritative |
| 2.5 | 1 | `008` | When the vehicle is equipped with the Camera App, surface Cameras as a t |
| 2.5.1 | 1 | `009` | When the Cameras tab is present at the Vehicle Category level, suppress  |
| 2.6 | 1 | `010` | Filter the Dashboard tab so only the apps for which the vehicle is actua |
| 2.6.1 | 1 | `011` | Within the Dashboard tab, display the applicable content in the fixed or |
| 2.6.2 | 3 | `012-01`, `012-02`, `012-03` | On landscape displays |
| 2.6.3 | 4 | `013-01`, `013-02`, `013-03`, `013-04` | On portrait displays |

### 2. `Controls` — 12 sections / 17 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 3.1 | 1 | `014` | Items eligible to appear in the Controls tab include (not limited to) He |
| 3.1.1 | 1 | `015` | When the vehicle has two or more of Cargo Camera, Backup Camera, or Surr |
| 3.1.2 | 1 | `016` | The Settings entry only appears as a Controls item when the Settings tab |
| 3.2 | 1 | `017` | Reflect Controls-state changes both on the CONTROLS screen and, where ap |
| 3.3 | 1 | `018` | Expose a shortcut to Settings from the App drawer so the user can reach  |
| 3.4 | 2 | `019-01`, `019-02` | The Headrest Fold button is a stateless action button; it does not surfa |
| 3.5 | 1 | `020` | When the vehicle is equipped with a hard control for Exhaust Sound, the  |
| 3.6 | 1 | `021` | When the Glove Box Lock button is pressed, open the Privacy Lock popup ( |
| 3.7 | 1 | `022` | On vehicles equipped with a lower non-articulating screen, remove from t |
| 3.8 | 1 | `023` | Electrochromic glass state does not latch across key cycles; on each new |
| 3.8.1 | 1 | `024` | When the roof is open, mark Electrochromic as unavailable and render its |
| 3.9 | 5 | `025-01`, `025-02`, `025-03`, `025-04`, `025-05` | Adopt the Controls Button Table as the authoritative source for each Con |

### 3. `Glove Box` — 8 sections / 12 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 4.1 | 3 | `026-01`, `026-02`, `026-03` | On selecting the 'Glove Box' option |
| 4.2 | 1 | `027` | After the activation PIN has been entered twice and matched, display the |
| 5.1 | 2 | `028-01`, `028-02` | When the user enters a wrong PIN on the second Glove Box activation atte |
| 5.2 | 1 | `029` | When the user finally enters the correct (first-entered) PIN after any n |
| 6.1 | 1 | `030` | To begin Glove Box deactivation, tapping the 'Glove Box' button within C |
| 6.2 | 1 | `031` | After the deactivation PIN has been accepted, display the 'Glove Box Mod |
| 6.3 | 1 | `032` | When the user presses 'OK' on the Glove Box confirmation popup, dismiss  |
| 7.1 | 2 | `033-01`, `033-02` | After three sequential wrong PINs during Glove Box deactivation |

### 4. `Settings Behavior` — 6 sections / 15 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 11.1 | 2 | `034-01`, `034-02` | Hide from a vehicle's Settings list any setting that does not apply to t |
| 11.2 | 3 | `035-01`, `035-02`, `035-03` | Selecting 'Yes' on the restore-defaults prompt resets the user's setting |
| 11.3 | 2 | `036-01`, `036-02` | Selecting 'Yes' on the clear-personal-data prompt clears the user's pers |
| 11.4 | 2 | `037-01`, `037-02` | Under Suspension |
| 11.5 | 5 | `038-01`, `038-02`, `038-03`, `038-04`, `038-05` | On a language change |
| 11.6 | 1 | `039` | When the user changes language to Chinese, display the 'Language updates |

### 5. `Settings List` — 17 sections / 30 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 11.7 | 1 | `040` | When the Settings List layout includes a Left Menu Rail, use the HMI Set |
| 11.7.1 | 1 | `041` | When the Settings List layout does not include a Left Menu Rail, surface |
| 11.8 | 2 | `042-01`, `042-02` | If a Setting's option text would truncate |
| 11.8.1 | 1 | `043` | When a Setting has been moved to a sub-level via the arrow (>), show the |
| 12.1 | 1 | `044` | Render the Settings list following the HMI Settings List order rather th |
| 12.2 | 1 | `045` | SETTINGS screens do not time out when idle and do not close after a sele |
| 12.3 | 5 | `046-01`, `046-02`, `046-03`, `046-04`, `046-05` | Select an item in the Settings list by pressing on it |
| 12.3.1 | 4 | `047-01`, `047-02`, `047-03`, `047-04` | When the cursor is on a single-checkbox line |
| 12.3.2 | 2 | `048-01`, `048-02` | When the user selects an object in the Settings list |
| 12.3.3 | 1 | `049` | For Clock, Equalizer, Balance/Fade, Engine Off Idle Timer, and Fleet Veh |
| 12.4 | 1 | `050` | For Brightness settings, a press-and-hold longer than 500 ms shall incre |
| 12.5 | 3 | `051-01`, `051-02`, `051-03` | When the user selects a setting |
| 12.6 | 2 | `052-01`, `052-02` | When the user enters Settings or enters a subcategory |
| 12.7 | 1 | `053` | When a Setting has an associated Definition, render an info icon (an 'i' |
| 12.7.1 | 1 | `054` | When the user presses a Setting's info icon, open a popup containing the |
| 12.7.2 | 1 | `055` | The Setting info icon and its corresponding info popup remain available  |
| 12.8 | 2 | `056-01`, `056-02` | Allow the user to change the setting option directly from the info popup |

### 6. `Ignition Availability` — 8 sections / 16 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 13.1 | 1 | `057` | The Settings tab is unavailable while the vehicle is in Key Off, Timed M |
| 13.1.1 | 3 | `058-01`, `058-02`, `058-03` | When the user attempts to open the Settings tab while in Key Off |
| 13.2 | 2 | `059-01`, `059-02` | Allow the user to access Phone settings through the Phone screens |
| 13.3 | 2 | `060-01`, `060-02` | Allow the user to access Audio settings through the Media screens |
| 13.4 | 1 | `061` | Software Updates remain available while the vehicle is in Key Off or ACC |
| 13.4.1 | 2 | `062-01`, `062-02` | When the user presses 'Software Downloads Over Wi-Fi' while the vehicle  |
| 13.4.2 | 2 | `063-01`, `063-02` | When the vehicle starts moving while the user is mid-flow in FOTA via Wi |
| 13.5 | 3 | `064-01`, `064-02`, `064-03` | When a Settings tab or category that is unavailable in Key Off/Timed Mod |

### 7. `Brake Service` — 1 sections / 2 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 14.1 | 2 | `065-01`, `065-02` | While the vehicle is in motion |

### 8. `Cabrio Widget` — 1 sections / 1 leaves

| section | leaf | req_id | 標的 |
|---|---|---|---|
| 16.2 | 1 | `066` | The widget title for the Vehicle Category feature is the literal string  |

---

## 7. 未入 Part N 者

**未引用之 42 section（108 outline 母體中之 42）不入 Part N** ——
其中 25 節為非需求性質、17 節為「有實質內容而 037 零涵蓋」
（R-VC12 一之修訂計數）。後者為 R-VC3 之表 B 母體，
草稿見 `data/tableB_draft.md`，最終措辭待 DR-VC3 回覆。

**未入 Part N 不等於不存在** —— 表 B 之職能正是使這 17 節浮現
（IN §8.4.2「真覆蓋洞須浮現、不得默默吸收」）。
