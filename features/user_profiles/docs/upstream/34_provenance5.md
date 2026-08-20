# 第四批之 ER 出處對照（34 包作業 2）


<!-- fingerprint:begin -->
## 語料指紋（G-F，45 包）—— 標記輪次：**59**

> **本表是本檔之保鮮期。** 引用本檔前先跑：`stamp_static_doc.py --verify <本檔>`；
> **不符即「已過期，拒絕採信」**，須重出後再引。
> 指紋之範圍為**全欄**（保守）—— 誤判過期只是多重出一次，誤判新鮮則是拿舊資料下判斷。

| tc_id | digest |
|---|---|
| `NR1L-UserProfiles-109` | `3f5edc65289f` |
| `NR1L-UserProfiles-110` | `0004731b79bf` |
| `NR1L-UserProfiles-111` | `1f51bdce1512` |
| `NR1L-UserProfiles-112` | `fc703babed64` |
| `NR1L-UserProfiles-113` | `9c306996d5cb` |
| `NR1L-UserProfiles-114` | `c1eb068a0163` |
| `NR1L-UserProfiles-115` | `2117868c9e94` |
| `NR1L-UserProfiles-116` | `9a4af0c2805a` |
| `NR1L-UserProfiles-117` | `7594e6c46247` |
| `NR1L-UserProfiles-118` | `a83e61e5218a` |
| `NR1L-UserProfiles-119` | `1db3c64c1a68` |
| `NR1L-UserProfiles-120` | `ab06e87dd6d3` |
| `NR1L-UserProfiles-121` | `27a8842ad6b4` |
| `NR1L-UserProfiles-122` | `d4df1f4cc518` |
| `NR1L-UserProfiles-123` | `eb36770838b0` |
| `NR1L-UserProfiles-124` | `af9357d28ffb` |
| `NR1L-UserProfiles-125` | `402280009eb4` |
| `NR1L-UserProfiles-126` | `95787d01c9a5` |
| `NR1L-UserProfiles-127` | `72254e0cd918` |
| `NR1L-UserProfiles-128` | `555af39b3d2a` |
| `NR1L-UserProfiles-129` | `400feaf338ba` |
| `NR1L-UserProfiles-130` | `914d85d805e4` |
| `NR1L-UserProfiles-131` | `cdbed6b2bc85` |
| `NR1L-UserProfiles-132` | `32f037b45c8c` |
| `NR1L-UserProfiles-133` | `dbaf307afae4` |
| `NR1L-UserProfiles-134` | `d1e2c09a8ebc` |

<!-- fingerprint:end -->

- 產出層：執行層｜2026-08-18｜對象：分析層
- 範圍：`NR1L-UserProfiles-109` ～ `134`（**26 條**）
- 對照對象：`expected_result` 與 `pre_conditions` 之字面值，及各條之**變體／配置範圍層級**

> 本檔查的是「這句話有沒有來源」，不是「這句話對不對」——
> 後者為 `34_review_pack_26.md`。

## 0. 總計

| 項 | 數 |
|---|---|
| 引號字面值（ER ＋ pre_conditions）| **30** |
| 逐字溯得到被引之節或其 must_carry | **24** |
| 經 `UI_LOCATORS` 登記表溯源（`“All Profiles”`／`“Edit Profile”`）| **6** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **8 條** |

### 0.1 本批唯一需要併列他節者：`TC-115`（5.2）

5.2 之條文以**指涉**帶入 PRACC7.2 之字串
（`the icon and the string **described in note PRACC7.2**`），**未逐字重複**。
`TC-115` 之 ER 逐字寫出該字串，故其引用欄併列 **5.1.2**
（`REF_EXTRA`，J-10 要求該節之 `provides` 字面值確實出現在該 TC 內 —— 即該字串）。

**這是 D-3／C-1 之同型第四例**（指涉他節內容），處置與前三例一致：
**補列來源節，不改寫條文**。

**連帶**：`lint_tcs._ref_allowlist()` 原只讀 pilot／batch01／batch02 三支之
`REF_EXTRA`，**第三、四批之登記讀不到** —— 已擴，並以 `getattr` 容許無該表之批次。
**若未擴，本批之併列會被 G17 判為未登記之多引。**

---

## 1. 逐條字面值對照

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-109` | 5.1 | 「All Profiles」| ER | 逐字見於 **5.1** |
| `NR1L-UserProfiles-110` | 5.1 | 「Edit Profile」| ER | 逐字見於 **5.1** |
| `NR1L-UserProfiles-110` | 5.1 | 「Edit Profile」| ER | 逐字見於 **5.1** |
| `NR1L-UserProfiles-111` | 5.1 | 「Edit Profile」| ER | 逐字見於 **5.1** |
| `NR1L-UserProfiles-111` | 5.1 | 「All Profiles」| ER | 逐字見於 **5.1** |
| `NR1L-UserProfiles-111` | 5.1 | 「Edit Profile」| pre | 逐字見於 **5.1** |
| `NR1L-UserProfiles-112` | 5.1.1 | 「All Profiles」| ER | 逐字見於 **5.1.1** |
| `NR1L-UserProfiles-113` | 5.1.2 | 「All Profiles」| ER | 逐字見於 **5.1.2** |
| `NR1L-UserProfiles-113` | 5.1.2 | 「This icon is associated to settings that are specific to your profile and are not shared across the vehicle」| ER | 逐字見於 **5.1.2** |
| `NR1L-UserProfiles-114` | 5.1.2 | 「My Profile」| ER | 逐字見於 **5.1.2** |
| `NR1L-UserProfiles-114` | 5.1.2 | 「My Profile」| pre | 逐字見於 **5.1.2** |
| `NR1L-UserProfiles-115` | 5.2 | 「All Profiles」| ER | 逐字見於 **5.2／5.1.2** |
| `NR1L-UserProfiles-115` | 5.2 | 「This icon is associated to settings that are specific to your profile and are not shared across the vehicle」| ER | 逐字見於 **5.2／5.1.2** |
| `NR1L-UserProfiles-116` | 5.2 | 「All Profiles」| ER | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-116` | 5.2 | 「Max Profiles reached. Delete to create a new one.」| ER | 逐字見於 **5.2** |
| `NR1L-UserProfiles-119` | 5.3.2 | 「All Profiles」| ER | 逐字見於 **5.3.2** |
| `NR1L-UserProfiles-119` | 5.3.2 | 「Edit Profile」| pre | 逐字見於 **5.3.2** |
| `NR1L-UserProfiles-121` | 5.4 | 「Edit Profile」| ER | 逐字見於 **5.4** |
| `NR1L-UserProfiles-121` | 5.4 | 「All Profiles」| pre | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-122` | 5.5 | 「All Profiles」| ER | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-123` | 5.5 | 「All Profiles」| ER | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-125` | 5.6 | 「All Profiles」| ER | 逐字見於 **5.6** |
| `NR1L-UserProfiles-126` | 5.6.1 | 「Add New」| ER | 逐字見於 **5.6.1** |
| `NR1L-UserProfiles-126` | 5.6.1 | 「Add New」| ER | 逐字見於 **5.6.1** |
| `NR1L-UserProfiles-126` | 5.6.1 | 「Function not available while vehicle in Motion.」| ER | 逐字見於 **5.6.1** |
| `NR1L-UserProfiles-126` | 5.6.1 | 「All Profiles」| pre | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-134` | 5.7 | 「All Profiles」| ER | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-127` | 5.7 | 「Edit Profile」| ER | 逐字見於 **5.7** |
| `NR1L-UserProfiles-132` | 5.10.1 | 「None」| ER | 逐字見於 **5.10.1** |
| `NR1L-UserProfiles-133` | 5.10.1 | 「None」| ER | 逐字見於 **5.10.1** |


**無引號字面值之 8 條**：`NR1L-UserProfiles-117`、`NR1L-UserProfiles-118`、`NR1L-UserProfiles-120`、`NR1L-UserProfiles-124`、`NR1L-UserProfiles-128`、`NR1L-UserProfiles-129`、`NR1L-UserProfiles-130`、`NR1L-UserProfiles-131`

—— 其 ER 皆為行為敘述（`The new Driver Profile is created`、
`No memory seat is linked to Driver Profile A`），非畫面上之逐字文字。

---

## 2. 變體／配置之範圍層級

**本批無任何 R1 High／China market 變體條件** —— 與 25／29 輪取樣清單之預告一致
（V-1 之 6 個 axis 落在 6.1／8.1／9.1／10.3.1／11.4，**ch5 一個都沒有**）。

| tc_id | 條件 | 層級 | 依據 |
|---|---|---|---|
| `113`／`114` | 螢幕**大於 7 吋** | **條文級（適用條件）** | 5.1.2 之 `This logic is not applicable for 7” screens` —— M-3 已判為適用條件而非覆寫 |
| `115` | 螢幕大於 7 吋 | **條文級（間接）** | 其斷言「圖示不在」須以「圖示原本會在」為前提；7 吋上圖示本就不顯示，**屆時該斷言證不了任何事** |
| `109` | 該 profile 從未開過 Profile 區 | **方法級（§5.6 基準線）** | 5.1 之 latch 會蓋過預設值，故須排除 |
| `118` | 目標 profile 之 welcome popup 已開啟 | **條文級** | 5.3.1 之 `(if turned on for that Profile)` |
| `119` | 新 profile 之上次分頁為 “Edit Profile” | **條文級（關鍵）** | 5.3.2 括號明言 `even if last known Profile tab was “Edit Profile”` —— **不設此前提則本條與 latch 無從分辨** |
| `122` | 該 profile 已連座椅 | 條文級 | 5.5 之 `each **applicable** Profile` |
| `123` | 車上 **3** 個記憶座椅且皆已連走 | **條文級（數值取自條文）** | 5.5 之 `currently up to 3` |
| `126` | profile 數未達上限 | 條文級 | 5.2 之上限使入口消失 |
| `127`／`134` | 現用 profile 尚未連座椅、且有空位 | 方法級 | 使「連上了」若發生即可見 |
| `128` | 現用 profile 原本無座椅 | **條文級（分支）** | 5.7 之 `will not automatically save to the active Profile` |
| `129` | 兩 profile 各連**不同**座椅位置 | 方法級 | 位置相同則「座椅未動」與「本來就一樣」無從分辨 |
| `132` | 現用 profile 原**無**座椅 | **條文級（分支）** | 5.10.1 之 `if there is no seat position already linked` |
| `133` | 現用 profile 原**有**座椅，且另有無座椅之 profile | **條文級（分支）** | 5.10.1 之 `if they already have a memory seat position` ＋ `next available Profile` |
| `112` | 車上三個 profile | **測試設置（J-12）** | 5.1.1 只寫 `all available users`，**未指定數目**；取 3 是為使「其他人」為複數 |
| `120` | 車上三個 profile | **測試設置（J-12）** | 5.3.3 只寫 `another profile`；取 3 是為使「載入中之目標」與「被擋之目標」不同 |

**兩個測試設置（`112`／`120`）之數目已於各該 remarks 具名** ——
**它們不是條文來的**，故不得被讀成需求。

---

## 3. 本對照之盲區（R-G11）

| # | 盲區 | 說明 |
|---|---|---|
| 1 | **只查引號內** | 未加引號之逐字引用由 Q-1 反向掃描承擔（本批新增 2 處待判，皆判為行為敘述）|
| 2 | **`UI_LOCATORS` 之 6 處為登記表溯源** | 非直接見於被引之節；登記表自身之正確性由 G18 末段自檢守 |
| 3 | **未查 `test_procedure` 之字面值** | 34 包指定之對照對象為 ER 與 pre-condition。`126` 之 `“Add New”`、`131` 之 `PU0588` 落在 procedure，**本對照未涵蓋**（其逐字見於 5.6.1／5.10.1，已人工確認）|
| 4 | **`TC-129` 之 popup 無 PU id** | 5.8 未給該 popup 之編號，故 ER 只述其**內容要旨**；**若日後 Pop Up List 補上該 id，ER 得補**（同 DR #4 之形態）|
