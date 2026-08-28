# 上繳包 16 —— 孤島列材料、孤島檢查腳本化、外科式寫回移植

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/17_islands.md`
  （SHA256 `b7b5c680bd6420e947ab87e05dd1b243e81c4502262455aac20a0d5ffe76af81`，213 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**
- 新腳本：`scripts/islands.py`、`scripts/write_back_036.py`；`scripts/layer2_close.py` 增 T30c

## 本輪四個主結果

1. **R-SU22.3 之實測翻轉了一個「缺項」**：驗證母體 **311 列之 Priority 空白為 0 列**
   （271 High + 34 Medium + 6 Low = 311）。上繳包 15 §4.2 把「空白 72 列之處置未裁」
   列為硬缺 —— **那 72 列全部落在 311 之外**（Heading 等非範圍列）。
   **該缺項不成立，本包更正。**
2. **R-SU21(b) 稱 0 列群「8 群」並列舉 8 個，實測為 9** ——
   `SWE1-FOTA-085`（`FOTA ROV Reflash Requirements`）未列。
   **一條專為 0 列群而設的條文，自己漏掉一個 0 列群** ——
   正是 PLAYBOOK §7(13) 所述之盲區在條文層的再現。
3. **孤島列檢查種子回測 7/7 通過，且 R-SU20(d) 可部分機器化** ——
   「組名實詞出現於該列標題」為可機器測之量，本輪 **5/7** 命中。
   但它測得的是**循環之風險**，非循環之事實：`339`／`358` 皆被標記，
   而下放包 17 §四裁定二者**維持**。§6.1 據此回答 §七.5。
4. **外科式寫回之空寫回：48 個部件逐 byte 全同，0 個相異。**
   另加一項下放包未要求之**探針**（以 `_set_row` 實寫 1 列），
   證實其保全 `<row>` 屬性、34 個儲存格與全部 `s=` 樣式索引 —— §5.2。

---

## 1. T30f —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU20 | 876 | **OK** | `2a86828b0cad` |
| R-SU21 | 752 | **OK** | `f344f9917a52` |
| R-SU22 | 555 | **OK** | `cd40d94eed36` |

三條逐字 append，**既有 31 個條文區塊未受影響** ✅（現 34 塊）。
索引表現行 **22 條**（新增 R-SU20／R-SU21／R-SU22）；留存 **12 條**（無變動）。
與下放包 17 §六 T30f 所定之「22 條現行」一致。

`PLAYBOOK.md` §7 追加 **(14)**「已知某資訊不足以判斷，仍用該資訊下判斷 ——
比單純判錯嚴重」，並記其形狀：**那不是新錯，是舊警告失效**，
故查錯者不會回頭查它；作法為「交付前掃一次自己上一包之不足／未知清單」。

---

## 2. T30a —— 孤島列與其比較基準列之 Description 全文（9 列）

> **僅全文**（下放包 17 §六）：不附分數、不附候選。**執行層不裁定其歸屬。**

### 甲 —— 五個 `PROVISIONAL-ROW`


---

#### `SWE1-FOTA-338` — Pre-Deployment Package Authenticity Verification

- 現置 Test Set：`Integrity Verification`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> * The SWMC shall verify the authenticity of the deployment package after the download is completed. * The WiFiUpdateService shall verify the authenticity of the deployment package after user acceptance or when the scheduled installation time is reached, before initiating the deployment.


---

#### `SWE1-FOTA-357` — Installation Interruption State Management

- 現置 Test Set：`Interruption Handling`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> * The Wifi Update service shall save the installation state when an interruption occurs before successful completion of the installation and shall resume the installation when the interruption condition is cleared. * The wifiupdate service shall report the installation status, including success, failure, or resumed state, to the SWMC.


---

#### `SWE1-FOTA-359` — OTA Flow Concurrency Control

- 現置 Test Set：`Session Management`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The SWMC shall ignore any request to start a new OTA update flow when an OTA update session is already active and shall ensure that the current session is not interrupted.


---

#### `SWE1-FOTA-360` — Download Interruption Recovery

- 現置 Test Set：`Interruption Handling`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The SWMC shall detect interruptions occurring during any step of the download process before completion, shall save the current download state, and shall resume the download when the interruption condition is cleared.


---

#### `SWE1-FOTA-361` — Server-Initiated OTA Background Execution

- 現置 Test Set：`Session Management`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The SWMC and wifiupdateservice shall execute server-initiated OTA update flows in the background without blocking foreground system operations.


### 乙 —— 五個比較基準列


---

#### `SWE1-FOTA-312` — Deployment Package Integrity Verification

- 用途：Integrity 之基準（GT 正解 `4907514`，章 4.8.3）｜現置 Test Set：`Integrity Verification`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> SWMC shall download the deployment package from the OTA Server and provide the downloaded deployment package to WiFiUpdateService. WiFiUpdateService shall perform the integrity verification of the deployment package immediately after receiving the package


---

#### `SWE1-FOTA-321` — Interruption Recovery Handling

- 用途：Interruption 之基準（近義標題群）｜現置 Test Set：`Interruption Handling`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The WiFiUpdateService shall detect the resolution of an interruption and notify SWMC to continue the OTA update session based on the current session state. The SWMC shall gracefully handle the interruption and continue operation in accordance with the session state.


---

#### `SWE1-FOTA-325` — Download Interruption Handling

- 用途：Interruption 之基準（近義標題群）｜現置 Test Set：`Interruption Handling`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The SWMC shall suspend the OTA update session, record the interruption in the log, and wait until the download can be resumed when an interruption occurs before the download is completed.


---

#### `SWE1-FOTA-323` — Concurrent NIA Handling

- 用途：Concurrent NIA（`359` 之疑似同族）｜現置 Test Set：`Interruption Handling`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> The SWMC shall queue an incoming NIA received during an active OTA update session without interrupting the current session and shall process the queued NIA after the active session is completed.


---

#### `SWE1-FOTA-337` — Deployment Flow Initiation

- 用途：Deployment Flow Initiation（`338` 之前鄰）｜現置 Test Set：`Deployment Conditions`｜Sub Cat：Service｜Priority：High

**Requirement Description 全文**：

> * The SWMC shall make the deployment package available to the WiFiUpdateService upon successful completion of the download. * The WiFiUpdateService shall receive the deployment notification from the SWMC and initiate the deployment workflow.


---

## 3. T30b —— Priority／Sub Cat 空白之實測

### Priority 之分布 —— 驗證母體 311 vs 全 383 資料列

| Priority | 驗證母體 311 | 全 383 資料列 | 差（= Heading 等非範圍列） |
|---|---:|---:|---:|
| `High` | **271** | 271 | 0 |
| `Medium` | **34** | 34 | 0 |
| `Low` | **6** | 6 | 0 |
| `(blank)` | **0** | 72 | 72 |
| **合計** | **311** | 383 | 72 |

> 上繳包 01 §之「空白 72」為**全 383 資料列**之數；**驗證母體 311 列中之空白為 0 列**（R-SU22.3 所令之實測）。

### Priority 空白之列（0）

**無**


### Sub Categorization 空白之列（1）

`SWE1-FOTA-260`


### 二者是否同列

- Priority 空白 ∩ SubCat 空白：**0** —— **空集**
- 僅 Priority 空白：**0**
- 僅 SubCat 空白：**1** —— `SWE1-FOTA-260`

### 3.1 ⚠ 本包更正上繳包 15 §4.2 之一處缺項

上繳包 15 §4.2 稱 `priority` 為「**硬缺**」，並列二項待裁，其第 2 項為
「**空白 72 列之處置未裁**」。

**該項不成立。** 72 列之空白**全部**落在驗證母體 311 之外
（383 − 311 = 72，即 Heading 等非 in-scope 列）。
**311 列之 Priority 無一空白**：271 + 34 + 6 = 311，閉合。

成因與 PLAYBOOK §7(9) 同型：上繳包 01 之「空白 72」是**全 383 資料列**之數，
上繳包 15 引用時未對**本文之母體（311）**重算，逕當成 311 之內的問題。
R-SU22.3 令實測，一測即翻。

**故 §4.2 之待裁項只剩一項**：`High`／`Medium`／`Low` → `P0`–`P3` 之對應 ——
而 **R-SU22 已裁其不作機械映射**，改依 IN §10.2 rubric 逐 TC 判。
**即：`priority` 一項已無缺。**

（`Sub Categorization` 空白仍為 1 列：`SWE1-FOTA-260`，與 Priority 空白**無交集**。
上繳包 01 §之「Priority 空白 72 全在 SubCat 空白 73 之內」為全 383 列之陳述，
於 311 母體上二者皆近乎清空，該重合關係在母體內不復存在。）

---

## 4. T30c —— 孤島列檢查之腳本化（R-SU20）

### 種子回測（R-SU20 之偵測器；未過即停）

已知種子（上繳包 15 §6.1，`309` 群內之 7 個孤島）：`338`、`339`、`357`、`358`、`359`、`360`、`361`

- 本偵測器（strict）抓到 **7** 個；其中種子 **7/7**
- 種子未被抓到者：**0** ✅
- 種子外之新發現：**0**（無）

**種子回測通過** —— 7 個已知孤島全數重現。

### ⚠ 「前鄰與後鄰皆不同」之解讀（須分析層確認）

| 解讀 | 孤島數 | 說明 |
|---|---:|---|
| **strict（採）**：只取內部列（前後鄰皆存在） | **7** | 群首／群尾／單列群無法評估此條件，故不計 |
| loose：缺鄰視為「不同」 | 15 | 使**每個單列群與每個群首／群尾**只要與鄰居不同即成孤島 —— 其中多數為 Test Set 之正常邊界，非證據 |

二者相差 **8** 列。strict 之產出全落於 `SWE1-FOTA-309` 等跨章群之內部，即 R-SU20(b) 所指「被自連續段中抽出」之情形。

### (a) 孤島清單，含 R-SU20(d) 之循環風險機器檢查

| 037 列 | 標題 | 其組 | 前鄰 | 後鄰 | 組名實詞見於標題 |
|---|---|---|---|---|---|
| `338` | Pre-Deployment Package Authenticity Verifica | `Integrity Verification` | 337(`Deployment Conditions`) | 339(`Status Reporting`) | **⚠ verification** |
| `339` | OTA Status Reporting via Backchannel | `Status Reporting` | 338(`Integrity Verification`) | 340(`Deployment Conditions`) | **⚠ status／reporting** |
| `357` | Installation Interruption State Management | `Interruption Handling` | 356(`Session Management`) | 358(`Status Reporting`) | **⚠ interruption** |
| `358` | Update Status Reporting to SWMC | `Status Reporting` | 357(`Interruption Handling`) | 359(`Session Management`) | **⚠ status／reporting** |
| `359` | OTA Flow Concurrency Control | `Session Management` | 358(`Status Reporting`) | 360(`Interruption Handling`) | — |
| `360` | Download Interruption Recovery | `Interruption Handling` | 359(`Session Management`) | 361(`Session Management`) | **⚠ interruption** |
| `361` | Server-Initiated OTA Background Execution | `Session Management` | 360(`Interruption Handling`) | 363(`Telematics Client`) | — |

**5/7** 個孤島之組名實詞出現於其標題。

> ⚠ **此檢查測得的是「循環之風險」，不是「循環之事實」**（見上繳包 16 §自評）：關鍵詞相符**未必**表示依據是關鍵詞 —— 下放包 17 §四即裁 `339`／`358` 之依據為「其對象為回報訊息」而**維持**，儘管二者皆被本檢查標記。

### (b) 各組於各跨章 Heading 群內之連續段數

| Heading 群 | Test Set | 段數 | 各段 |
|---|---|---:|---|
| `SWE1-FOTA-170` | `Integrity Verification` | 1 | 171–174 |
| `SWE1-FOTA-170` | `Silent Update` | 1 | 175–177 |
| `SWE1-FOTA-309` | `Session Management` | **4** | 347–356、359、361、368–369 |
| `SWE1-FOTA-309` | `Interruption Handling` | **3** | 313–329、357、360 |
| `SWE1-FOTA-309` | `Status Reporting` | **3** | 330–334、339、358 |
| `SWE1-FOTA-309` | `Integrity Verification` | **2** | 310–312、338 |
| `SWE1-FOTA-309` | `Deployment Conditions` | **2** | 336–337、340–346 |
| `SWE1-FOTA-309` | `Telematics Client` | 1 | 363–367 |
| `SWE1-FOTA-309` | `Update Agent` | 1 | 370–383 |

### (c) 聚集分佈

| 聚集 | 037 列 | 個數 | 跨度 |
|---:|---|---:|---:|
| 1 | `338`、`339` | 2 | 2 列 |
| 2 | `357`、`358`、`359`、`360`、`361` | 5 | 5 列 |

**7 個孤島聚為 2 處**（判準：孤島間之 037 列距 ≤ 2）。若切分照能力，錯誤應散開；**聚於少數幾處表示該段有系統性成因**（R-SU20(c)）。

> **R-SU20(e) 之限度（隨檢查一併陳述）**：孤島列指出「該處之依據需高於相鄰之先驗」，**不是「該處錯了」**。規格作者確有可能在連續數列中交替寫數種能力。判其對錯仍須讀該列之描述。

---

## 5. T30e —— 外科式寫回腳本之移植與空寫回

- 來源（不動）：`inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case…`
- 輸出：`output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case…`（`.gitignore` 內）
- sheet xml：`xl/worksheets/sheet6.xml`｜寫入列數：**0**（空寫回）

| 量 | 母本（基線） | 輸出 | 上繳包 15 §4.4 | |
|---|---:|---:|---:|:--:|
| `zip 部件總數` | 48 | 48 | 48 | ✅ |
| `worksheet 數` | 9 | 9 | 9 | ✅ |
| `<dataValidation （sheet6，標準）` | 3 | 3 | 3 | ✅ |
| `<x14:dataValidation （sheet6）` | 1 | 1 | 1 | ✅ |
| `<extLst>（sheet6）` | 1 | 1 | 1 | ✅ |
| `<conditionalFormatting（全簿）` | 0 | 0 | 0 | ✅ ⚠ |
| `printerSettings` | 5 | 5 | 5 | ✅ |
| `media` | 2 | 2 | 2 | ✅ |
| `drawing 相關部件` | 13 | 13 | 13 | ✅ |
| `t="shared"` | 1401 | 1401 | 1401 | ✅ |
| **母本 SHA256 前後** | `6372fb6be02f…` | `6372fb6be02f…` | 未變 | ✅ |

> ⚠ **`<conditionalFormatting` 之計數為 0** —— 本母本無條件式格式，**該項前後相等恆真通過，在本 feature 不具鑑別力**（上繳包 15 §4.4）。R-SU2 令比對故仍跑，但**其通過不得計為證據**。

- sheet6 之 XML 是否逐字未變：**是**（空寫回應為「是」）
- 逐部件 byte 比對：**0 / 48** 個部件內容相異 ✅
- 部件名稱與順序：**相同**

**空寫回結果：全部通過 ✅**

### 5.1 移植之邊界（「只移植不改行為」之逐項交代）

| 部分 | 處置 |
|---|---|
| `esc()` | **逐字移植** |
| `_set_row()` | **逐字移植** —— 保留 `<row>` 之 `spans`／`s`／`customFormat`／`ht`、各儲存格原 `s=` 樣式索引；未列於 vals 之儲存格逐 byte 留存 |
| zip 逐 byte 重打包迴圈 | **逐字移植** |
| 母本檔名、sheet 名、`HEADER_ROW` | 換為本 feature 之值（`feature.yaml` §workbook） |
| `COLS` | 依 `feature.yaml` §workbook.columns 重列（15 欄）。**B 欄不寫** —— 共用公式之宿主（`t="shared"` 1401 處），理由同 display 之 R-DM15 |
| `_leaf_order()`／`BATCHES`／TC 組裝 | **未移植** —— 本 feature 之 `generated/` 為空，且 TC ID 命名未裁（缺項 4）。現階段只支援 `--empty` |

**未改任何外科式之機制**；改動全落在「哪一份檔、哪些欄」。

### 5.2 一項下放包未要求之探針 —— 空寫回驗不到 `_set_row`

**空寫回之 0/48 相異證明的是「重打包無損」，不是「寫入無損」** ——
`written` 為空時 `_set_row` **一次都沒被呼叫**，
而它正是唯一會動 XML 的那段。故另跑一次**探針**（`/tmp` 副本，非交付物）：
以 `_set_row` 對第 10 列寫入 15 欄佔位值，再量同一組指標。

| 量 | 母本 | 探針（實寫 1 列） | |
|---|---:|---:|:--:|
| zip 部件總數 | 48 | 48 | ✅ |
| `<dataValidation `（sheet6） | 3 | 3 | ✅ |
| `<x14:dataValidation `（sheet6） | 1 | 1 | ✅ |
| `<extLst>`（sheet6） | 1 | 1 | ✅ |
| printerSettings / media / drawing | 5 / 2 / 13 | 5 / 2 / 13 | ✅ |
| `t="shared"` | **1401** | **1401** | ✅ |
| 相異部件 | — | **僅 `xl/worksheets/sheet6.xml`** | ✅ |

第 10 列之逐項比對：

| 項 | 原 | 寫入後 |
|---|---|---|
| `<row>` 開標籤 | `<row r="10" spans="1:34" s="84" customFormat="1">` | **完全相同** |
| 儲存格數 | 34 | **34** |
| `s=` 樣式索引集合 | `80,81,82,83,84` | **完全相同** |

母本 SHA256 前後未變（`6372fb6be02f…`）。

**這一步是 PLAYBOOK §7(8)（偵測器須先對種子回測）之同型**：
空寫回是一個「不觸發被測機制」的驗收，其全綠對 `_set_row` 完全無鑑別力。

---

## 6. T30d —— `framework.md` 更新

已更新（270 行）。變更：

| 項 | 內容 |
|---|---|
| 效力分級表 | Layer 2 加註「**5 列標 `PROVISIONAL-ROW`**」 |
| 切分原則 | 原則 2 加 R-SU21(a) 之射程限制；新增原則 6（R-SU20 孤島列檢查必跑） |
| 新節「孤島列檢查」 | 7 列全表 + 逐列裁定 + 2 處聚集 + R-SU20(e) 限度 |
| 新節「`PROVISIONAL-ROW`」 | 5 列、其待決候選組、分析層之傾向、**R-SU20(f)：本 feature 尚不得寫回 Layer 2** |
| 新節「0 列 Heading 群」 | **實測 9 群**（非條文之 8），逐群標所屬 Test Set，載 R-SU21(c) 之逐字加註 |
| Layer 3 | `Integrity Verification` 已列 `4.8.2` + `4.8.3` 二章（R-SU21(a) 配套）；「GT 支持者」採 **8** |

### 6.1 ⚠ R-SU21(b) 之「8 群」實測為 9 群

R-SU21(b)：「本案 45 群中有 **8** 群所轄 in-scope 列為 0
（`016`,`017`,`020`,`022`,`072`,`073`,`074`,`076`）。」

實測（`framework_survey.group_by_heading`）：**9 群**。
未列者為 **`SWE1-FOTA-085`（`FOTA ROV Reflash Requirements`，0 列，
屬 `ROV Installation`）**。上繳包 14 §T28c 之對照表該列即已載「列數 0」。

**此事之形狀值得記**：R-SU21(b) 是**專為 0 列群而設的條文**，
而它自己漏掉一個 0 列群。PLAYBOOK §7(13) 說「以量為準之檢查對零無感」——
本例顯示**條文之列舉也是一種以量為準的清點**，同樣會漏零。
`framework.md` 採 9，並記 R-SU21(b)(c) 之效力一體適用於 `085`。

---

## 7. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

### 待分析層確認之事項（非 DR，無外部資料需求）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **R-SU20(a)「前鄰與後鄰皆不同」之解讀**：strict（只取內部列，採，得 7）vs loose（缺鄰視為不同，得 15） | §4 |
| 2 | **R-SU21(b) 之「8 群」應為 9 群**（漏 `085`） | §6.1 |
| 3 | **五個 `PROVISIONAL-ROW` 之定案**（材料已備於 §2） | §2、`framework.md` |
| 4 | **TC ID 之命名未裁**（缺項 4，未因本輪改變）—— 且其未裁使 `write_back_036.py` 之 TC 組裝段無法移植 | §5.1 |

---

## 8. 獨立自評

### 8.1 §七.5 所問：孤島檢查腳本化後，「聚集分佈」之判讀是否需要人；若需要，該檢查之機器化程度實際為何

**分三段回答，因為這個檢查的三個部分機器化程度差很多。**

**(a) 孤島之偵測 —— 全機器化，無需人。**
輸入是 037 之列序與 Layer 2 之歸屬，二者皆為結構化資料；
判準（前後鄰皆不同）是純比較。種子回測 7/7 通過，
且**種子外 0 個新發現** —— 即偵測器在本輪之產出與人工結果完全一致。
唯一需人的是**「連續」之解讀**（strict/loose，7 vs 15），
而那是一次性的定義選擇，不是逐次判讀。

**(b) 聚集分佈之計算機器化，其判讀需要人 —— 且需要的不只是判讀。**

計算端：把 7 個孤島依列距 ≤ 2 分堆得 2 堆，這是機械的。
**但「聚集」要成為證據，需要一個對照基準，而本輪沒有基準。**

R-SU20(c) 之推論為「若切分照能力，錯誤應散開；聚於一段表示有系統性成因」。
**這句話的效力取決於「散開會長什麼樣」，而那需要零假設** ——
7 個點落在 70 個位置上，隨機分佈時聚成 2 堆的機率是多少？
**本輪沒算，也沒有可算的基礎**（孤島之產生非獨立事件：
`358` 之所以是孤島，正因為 `357`／`359` 是孤島）。

**故：聚集分佈目前不是統計證據，是一個描述。**
它之所以仍有用，是因為 2 堆的**位置**恰好落在
`338`–`339`（Integrity/Deployment 之邊界）與 `357`–`361`
（三組交替之段），而那二處**另有獨立理由**可疑
—— 但那個「另有理由」是人讀出來的，不是聚集算出來的。

**(c) R-SU20(d)（依據不得為關鍵詞相符）—— 可機器化，但只到「風險」為止。**

本輪把它實作為：**組名之實詞是否出現於該列標題**。這是可算的，
本輪 **5/7** 命中（`338` verification、`339` status/reporting、
`357` interruption、`358` status/reporting、`360` interruption）。

**但它測不到條文真正禁止的東西。** R-SU20(d) 禁的是
「**以**關鍵詞相符**為依據**」，而機器只看得到「關鍵詞相符」這個**事實**。
下放包 17 §四本身就是反例：`339`／`358` 二者關鍵詞全中，
而分析層裁定其依據為「其對象為回報訊息之通道」並**維持** ——
**依據不是關鍵詞，儘管關鍵詞相符。**

**故本檢查之正確用法是「舉證責任之觸發器」，不是判準**：
命中者須在 `framework.md` 給出一個**不引用該關鍵詞**的記名依據；
給得出即通過。給不出才是違反 (d)。

**綜合回答**：孤島檢查之機器化程度為
**偵測 100%／舉證觸發 100%／判讀 0%**。
它把「哪幾列需要交代」從人的直覺變成了機器的清單（這是真收益，
且該清單是**完備**的 —— 不會漏），
但**每一列該怎麼交代，仍然是逐列人裁**，
且其中最像結論的那一格（聚集）目前只是描述而非證據。

**能誠實說的是**：R-SU20 沒有把 Layer 2 之正確性變成可機器驗證的東西，
它做到的是**把不可機器驗證的部分精確地圈出來，並強制其留下記名依據**。
以上繳包 15 §6.2 之話說：正確性維度仍然只有弱先驗；
本輪的進展是**弱先驗被寫成了條文與腳本，且其限度被寫在同一頁上**。

### 8.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §5 之「48 個部件逐 byte 全同，0 個相異」。**

那是本輪數字最漂亮的一格，而**它證明的事幾乎是空的**：
空寫回時 `_set_row` 一次都沒被呼叫，
所以「輸出與母本逐 byte 相同」的正確解讀是
**「把一份 zip 解開再打包回去，內容不變」** —— 這當然。

真正該驗的是寫入路徑，而空寫回**在設計上就繞過了它**。
我補了 §5.2 之探針才把該路徑蓋到。
若只交空寫回那張全綠表，讀者會合理推論「外科式寫回已驗證」，
而實際上被驗證的只有重打包。

**這與 §8.1(c) 是同一種病的兩個位置**：
一個檢查全綠，而它綠的地方不是問題所在。

### 8.3 一項我做了而下放包未要求的事

**§3.1 —— 回頭查上繳包 15 自己列的「硬缺」，發現它不成立。**

T30b 只令「驗證母體 311 列中 Priority 空白之 id 與列數」。
跑出來是 0 列，照理寫「0 列」就結束了。
但上繳包 15 §4.2 是**我自己**寫的，它把「空白 72 列之處置未裁」
列為 `priority` 之二項待裁之一，並標其為「硬缺」——
而 0 列的意思是**那一項從來不存在**。

成因是我引用上繳包 01 之「空白 72」時，**沒有對本文之母體（311）重算**
—— 正是 PLAYBOOK §7(9) 所禁，而該條是我自己在上繳包 12 提議寫進去的。

**記明此事**，因為它與本輪新增之 §7(14) 恰好構成一對：
(14) 是「用了已知不足的資訊」，本例是「用了未經本文重驗的分母」。
**二者都不是算錯，都是把別人的（或自己上一包的）前提當成常數搬運。**
而本例更該記的一點是：**這一次是條文（R-SU22.3）令我去測，我才發現的** ——
不是我自己回頭查的。若 R-SU22 沒有那一句「其列數須實測」，
那個不存在的缺項會一直掛在待辦上。
