# 第三批之 ER 出處對照（28 包作業 6）


<!-- fingerprint:begin -->
## 語料指紋（G-F，45 包）—— 標記輪次：**45**

> **本表是本檔之保鮮期。** 引用本檔前先跑：`stamp_static_doc.py --verify <本檔>`；
> **不符即「已過期，拒絕採信」**，須重出後再引。
> 指紋之範圍為**全欄**（保守）—— 誤判過期只是多重出一次，誤判新鮮則是拿舊資料下判斷。

| tc_id | digest |
|---|---|
| `NR1L-UserProfiles-079` | `14590d6574dc` |
| `NR1L-UserProfiles-080` | `e679ab6e949e` |
| `NR1L-UserProfiles-081` | `461cdbacdda8` |
| `NR1L-UserProfiles-082` | `86015249c520` |
| `NR1L-UserProfiles-083` | `c0a238b21805` |
| `NR1L-UserProfiles-084` | `546d60446efc` |
| `NR1L-UserProfiles-085` | `a5df30148a8c` |
| `NR1L-UserProfiles-086` | `a83785f45987` |
| `NR1L-UserProfiles-087` | `a708497ed07a` |
| `NR1L-UserProfiles-088` | `e53d7851b854` |
| `NR1L-UserProfiles-089` | `1d5510ec546b` |
| `NR1L-UserProfiles-090` | `c0a11924a0a0` |
| `NR1L-UserProfiles-091` | `936616a5cb1d` |
| `NR1L-UserProfiles-092` | `d0a9bdd93dd0` |
| `NR1L-UserProfiles-093` | `4b65b81c0370` |
| `NR1L-UserProfiles-094` | `da22df3abaa2` |
| `NR1L-UserProfiles-095` | `c74a25a1f87f` |
| `NR1L-UserProfiles-096` | `753b0bbee8c4` |
| `NR1L-UserProfiles-097` | `51538e31c953` |
| `NR1L-UserProfiles-098` | `272af1b2e2ab` |
| `NR1L-UserProfiles-099` | `f6b2ad112f1f` |
| `NR1L-UserProfiles-100` | `b712da5a60db` |
| `NR1L-UserProfiles-101` | `895a1c45471a` |
| `NR1L-UserProfiles-102` | `71d78163e9e9` |
| `NR1L-UserProfiles-103` | `246a8de1d36d` |
| `NR1L-UserProfiles-104` | `b5121a79a3a0` |
| `NR1L-UserProfiles-105` | `6a56cee2f68c` |
| `NR1L-UserProfiles-106` | `decadab1b2bf` |
| `NR1L-UserProfiles-107` | `dfbfd54c9387` |
| `NR1L-UserProfiles-108` | `e7b86c21fe7d` |

<!-- fingerprint:end -->

- 產出層：執行層｜2026-08-18｜對象：分析層
- 範圍：`NR1L-UserProfiles-079` ～ `108`（**30 條**）
- 對照對象：**`expected_result` 與 `pre_conditions` 之字面值**，
  以及各條之**變體／配置範圍層級**

> **本檔查的是「這句話有沒有來源」，不是「這句話對不對」。**
> 後者屬內容覆核（同 21／23 輪之 review pack），本輪未做。

---

## 0. 總計

| 項 | 數 |
|---|---|
| 引號字面值（`expected_result` ＋ `pre_conditions`）| **15** |
| 逐字溯得到被引之節或其 must_carry | **13** |
| 經 `UI_LOCATORS` 登記表溯源（`“All Profiles”`）| **2** |
| **未溯得者** | **0** |
| 全條無引號字面值者 | **22 條** |

### 0.1 **一項只有本對照查得到的發現**

**`G18` 只掃 `expected_result`，不掃 `pre_conditions`。**

本對照依 28 包指示併掃 pre-condition，於 `NR1L-UserProfiles-100`（4.5.4）
抓到 `“Driver 2”` **溯不到 4.5.4** —— 該節寫的是
`default **Driver 1-2** Profiles`，而 `Driver 2` 單獨出現在 **4.5.1**。

**處置**：改用本節自己的寫法（`“Driver 1-2”`），
**未另引 4.5.1** —— 引之即為多引（G17 之 J-10 判準）。

**這是本輪唯一由出處對照抓出而閘抓不到者**，故單獨列。
是否把 `G18` 擴及 `pre_conditions`，見 §3 第 1 項。

---

## 1. 逐條字面值對照（有引號者）

| tc_id | 節 | 字面值 | 欄位 | 出處 |
|---|---|---|---|---|
| `NR1L-UserProfiles-092` | 4.5 | 「All Profiles」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-092` | 4.5 | 「Driver 1」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-093` | 4.5 | 「All Profiles」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-093` | 4.5 | 「Driver 1」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-093` | 4.5 | 「Driver 1」| pre | 逐字見於 **4.5** |
| `NR1L-UserProfiles-094` | 4.5 | 「All Profiles」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-094` | 4.5 | 「Driver 1」| ER | 逐字見於 **4.5** |
| `NR1L-UserProfiles-095` | 4.5.1 | 「All Profiles」| ER | `UI_LOCATORS` 登記表（來源 5.1） |
| `NR1L-UserProfiles-095` | 4.5.1 | 「Driver 1」| ER | 逐字見於 **4.5.1** |
| `NR1L-UserProfiles-095` | 4.5.1 | 「Driver 2」| ER | 逐字見於 **4.5.1** |
| `NR1L-UserProfiles-097` | 4.5.3 | 「All Profiles」| pre | 逐字見於 **4.5.3** |
| `NR1L-UserProfiles-098` | 4.5.3 | 「All Profiles」| ER | 逐字見於 **4.5.3** |
| `NR1L-UserProfiles-100` | 4.5.4 | 「Driver 1-2」| pre | 逐字見於 **4.5.4** |
| `NR1L-UserProfiles-107` | 7.2.1 | 「More Options」| ER | 逐字見於 **7.2.1** |
| `NR1L-UserProfiles-107` | 7.2.1 | 「Edit Profile」| ER | 逐字見於 **7.2.1** |



**無引號字面值之 22 條**：`NR1L-UserProfiles-079`、`NR1L-UserProfiles-080`、`NR1L-UserProfiles-081`、`NR1L-UserProfiles-082`、`NR1L-UserProfiles-083`、`NR1L-UserProfiles-084`、`NR1L-UserProfiles-085`、`NR1L-UserProfiles-086`、`NR1L-UserProfiles-087`、`NR1L-UserProfiles-088`、`NR1L-UserProfiles-089`、`NR1L-UserProfiles-090`、`NR1L-UserProfiles-091`、`NR1L-UserProfiles-096`、`NR1L-UserProfiles-099`、`NR1L-UserProfiles-101`、`NR1L-UserProfiles-102`、`NR1L-UserProfiles-103`、`NR1L-UserProfiles-104`、`NR1L-UserProfiles-105`、`NR1L-UserProfiles-106`、`NR1L-UserProfiles-108`

—— 其 ER 皆為行為敘述（`Driver Profile B is active`、
`The preference matches the value recorded in step 1`），
**非畫面上之逐字文字**，依 Q-1 之界線（profile §3.3.1）不加引號。

---

## 2. 變體／配置之範圍層級

**本批無任何 R1 High／China market 變體條件** ——
與 25 包取樣清單之預告一致（V-1 之 6 個 axis 全落在 6.1／8.1／9.1／10.3.1／11.4，
**ch4 一個都沒有**）。本批之範圍條件皆為**配置**或**條文自帶之例外**：

| tc_id | 條件 | 層級 | 依據 |
|---|---|---|---|
| `079`／`080` | 受測功能於本車／本區域可用（或不可用）| **條文級** | 4.1 之 `If a feature is unavailable for a vehicle or region` |
| `089` | 排除 key fob 偵測與記憶座椅鍵 | **條文級** | 4.4 之 `unless a different Profile is detected or initiated` —— 覆寫條件即條文所載 |
| `092`／`093`／`094` | 記憶座椅鍵**少於 2 個** | **條文級（例外）** | 4.5 之 `(unless there are 2 or more memory seat buttons)` |
| `095` | 記憶座椅鍵**為 2 個** | **條文級（例示）** | 4.5.1 之 `e.g., if there are 2 memory seat buttons` —— 數字取自條文之例，非自擬 |
| `102` | avatar 為**純色**（無圖像）| **條文級（分支）** | 4.6.1 之 `if the avatar is just a color` |
| `104` | Profile 按鈕**已被移除** | **條文級（前提）** | 4.6.3 之 `If the Profile button is removed from the status bar` |
| `107`／`108` | **大型** welcome popup | **條文級** | 7.2.1 之 `The large welcome popup` |
| `086` | 記憶座椅鍵編號 **2** | **測試設置（J-12）** | 4.3 只寫 `through memory seat buttons`，**未給編號** |
| `091` | 記憶座椅鍵編號 **1** | **測試設置（J-12）** | 4.4 只寫 `memory seat buttons` |
| `105` | 記憶座椅位置編號 **1** | **測試設置（J-12）** | 4.5.2 只寫 `per memory seat position` |
| `083` | 受測之兩個功能（Media、Climate）| **測試設置（J-12）** | 4.2 只寫 `use/interact with the head unit` |

**三個編號（`086`／`091`／`105`）已登記於 `lint_tcs.py` 之 `TEST_SETUP_NUMERALS`**，
並於各該 remarks 具名 —— **否則 G18 會把它們判為溯不到源，而那個判定是對的**：
它們確實不在條文裡。

---

## 3. 本對照之盲區（R-G11）

| # | 盲區 | 說明 |
|---|---|---|
| 1 | **`G18` 不掃 `pre_conditions`** | §0.1 之發現即出自此。**本輪未擴 G18** —— pre-condition 常含測試設置之描述（`Two Driver Profiles exist`），擴之會大量誤報；**但這表示同型缺陷若只落在 pre-condition，現行閘看不見**，須靠出處對照。**建議下包裁示是否擴。** |
| 2 | **只查引號內** | 未加引號之逐字引用由 `audit_consistency` 之 Q-1 反向掃描承擔（本批新增 2 處待判，皆判為行為敘述非顯示值）|
| 3 | **`UI_LOCATORS` 之 2 處為登記表溯源** | 非直接見於被引之節；其登記表自身之正確性由 G18 之末段自檢守（「登記表有誤」會轉紅）|
| 4 | **未查 `test_procedure` 之字面值** | 28 包指定之對照對象為 ER 與 pre-condition。`081`／`082` 之 `“Restore Settings to Default”` 落在 procedure，**本對照未涵蓋**（其逐字見於 4.1.1，已人工確認）|
