# 上繳包 09 —— R-SU14 v2／R-SU15 抄錄、A-SU5 更正、統攝語形普查

- 日期：2026-08-27
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/10_umbrella_rulings.md`
  （SHA256 `0f7386295968240c70badf0d7360154b86cc8b27c2e27d0802b8cc2d6736f0ff`，182 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜PENDING 裁決：**0 項**
- **本輪核心發現**：統攝語形之六式掃描聯集僅 **4 / 311（1.3%）**；
  反向探測證明式B/C/D 之 0 命中為**語料真的沒有**，非 regex 太嚴；
  但**同一探測亦揭出兩條漏網路徑**（§2.4）

---

## 1. T23e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU14 v2 | 906 | **OK** | `ba4ab36f66d4` |
| R-SU15 | 831 | **OK** | `852c2f812b7d` |
| A-SU5 處分（入 `ANOMALIES.md`） | 532 | **OK** | `ff02c0915cbf` |

**既有 17 個條文區塊未受影響** —— 逐一回讀比對 sha256，全數不變 ✅。

### 索引表（現行 15 條）

| 條號 | 現行版 | 主旨 | 來源 |
|---|---|---|---|
| R-SU1 | v1 | feature 身分與 test_group | 01 §二 |
| R-SU2 | v1 | 036 母本與 workbook_state = BLANK | 01 §二 |
| R-SU3 | v1 | 驗證母體 311 = FR 307 + NFR 4 | 01 §二 |
| R-SU4 | v2 | spec_reference 雙家族錨點 + 錨點池範圍 | 02 §二 |
| R-SU5 | v2 | 037 Source Requirement ID 欄之三形態 | 03 §2.1 |
| R-SU6 | v2 | HMI 規格為真 PDF，一律機器抽取 | 02 §二 |
| R-SU7 | v2 | Description 不入池；池 574 = 87 + 487 | 04 §1.2 |
| R-SU8 | v1 | RULINGS 現行版判準與索引 | 05 §二 |
| R-SU9 | v1 | recon 產物之重生條件 | 05 §二 |
| R-SU10 | v1 | Layer 2 分群鍵為 Heading id | 06 §二 |
| R-SU11 | v1 | Layer 3 主軸為 CFTS_57；SYS1 以 HMI 87 列橋接 | 06 §二 |
| R-SU12 | v1 | 逐列對照之軸為 Description 全文 × 需求物件全文 | 07 §2.2 |
| R-SU13 | v2 | 驗證三支柱、探針來源限制、自檢四項 | 08 §二 |
| **R-SU14** | **v2** | 兩階段錨定；階段一取**首選之章**，信度由分差 × Heading 章一致性合成 | **10 §三** |
| **R-SU15** | **v1** | 統攝型需求為文本路之結構盲區；有 id 者自證優先 | **10 §四** |

**留存之被取代條文（不得引用）4 條**：`R-SU5`(v1)、`R-SU7`(v1)、
`R-SU13`(v1)、**`R-SU14`(v1)**（其階段一之投票類設想已由回測否定）。

---

## 2. T23a —— 統攝語形之全母體普查

### 各式之 regex（逐一揭露）

| 式 | regex | 說明 |
|---|---|---|
| 式A defined in System Requirement(s) | `defined\s+in\s+(?:the\s+)?System\s+Requirements?\b` | R-SU15(a) 之典型語形，313/315/316 即此式 |
| 式B defined in <section/table> | `defined\s+in\s+(?:the\s+)?(?!System\s+Requirement)(?:section|clause|chapter|table|figure|appendix)\b` | 指涉節/表號而不列 id → (c) 群候選 |
| 式C as listed in / listed below / as follows | `\b(?:as\s+listed\s+in|listed\s+below|as\s+follows|following\s+(?:table|list))\b` | 列舉引導語；其後之列舉未必為 id |
| 式D the <conditions|errors|requirements|steps> in/of | `\bthe\s+(?:conditions?|errors?|requirements?|steps?|scenarios?|states?)\s+(?:defined|described|specified|listed)?\s*(?:in|of|per)\b` | 指涉類語形，涵蓋 R-SU15(a) 所舉之 `the conditions in <節>` |
| 式E described/specified in <ref> | `\b(?:described|specified|referenced|detailed)\s+in\b` | 式B/D 之補集：其他「見某處」語形 |
| 式F 純 id 列舉（≥3 個 490xxxx） | `(?:(?<!\d)490\d{4}(?!\d)\D{0,12}){3,}` | 無統攝動詞但密集列舉 id 者 —— 語形之外的結構線索 |

### 命中總覽

| 式 | 命中次數 | 相異列 |
|---|---:|---:|
| 式A defined in System Requirement(s) | 3 | **2** |
| 式B defined in <section/table> | 0 | **0** |
| 式C as listed in / listed below / as follows | 0 | **0** |
| 式D the <conditions|errors|requirements|steps> in/of | 0 | **0** |
| 式E described/specified in <ref> | 3 | **2** |
| 式F 純 id 列舉（≥3 個 490xxxx） | 2 | **1** |
| **聯集** | — | **4 / 311（1.3%）** |

### R-SU15 之兩群分類（依命中列自身是否列舉 490xxxx）

- **(b) 有 id 群**：**2** 列 —— ['SWE1-FOTA-313', 'SWE1-FOTA-327']
- **(c) 無 id 群**：**2** 列

### 反向探測 —— 檢定「0 命中」之真偽

> 六式中式B／式C／式D 皆 0 命中。0 可能是**語料真的沒有**，也可能是**regex 太嚴**。以下用更寬鬆之裸字串探測區辨。**六式不因本節而修改** —— 改式即為看著結果轉旋鈕。

| 裸字串探測 | 命中列 |
|---|---:|
| `listed` | 0 |
| `as follows` | 0 |
| `following` | 4 |
| `defined in` | 7 |
| `described in` | 0 |
| `specified in` | 2 |
| `refer to` | 0 |
| `\bsee\b` | 0 |
| `\bsection\b` | 0 |
| `\btable\b` | 0 |
| `\bchapter\b` | 0 |
| `\bper the\b` | 0 |
| `in accordance` | 3 |
| `\babove\b` | 3 |
| `\bbelow\b` | 1 |
| `respectiv` | 2 |
| `\bmentioned\b` | 2 |
| `\bshall\b` | 311 |

### 式A defined in System Requirement(s) —— 2 列

| 037 列 | 群 | 原句摘錄 |
|---|---|---|
| `SWE1-FOTA-313` | **(b) 有 id** | * The WiFiUpdateService shall coordinate the handling of the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 by interacting with SWMC |
| `SWE1-FOTA-327` | **(b) 有 id** | …esume the interrupted download when the interruption type satisfies the resume conditions defined in System Requirements 4907683 and 4907684. |

### 式B defined in <section/table> —— 0 列

（無命中）

### 式C as listed in / listed below / as follows —— 0 列

（無命中）

### 式D the <conditions|errors|requirements|steps> in/of —— 0 列

（無命中）

### 式E described/specified in <ref> —— 2 列

| 037 列 | 群 | 原句摘錄 |
|---|---|---|
| `SWE1-FOTA-343` | (c) 無 id | * The SWMC shall request the vehicle conditions specified in the deployment configuration file from the WiFiUpdateService. * The WiFiUpdateService shall provide the vehic… |
| `SWE1-FOTA-382` | (c) 無 id | …y that the current firmware version of the target ECU matches the source firmware version specified in the differential update package before starting the update process. * The WiFi update  |

### 式F 純 id 列舉（≥3 個 490xxxx） —— 1 列

| 037 列 | 群 | 原句摘錄 |
|---|---|---|
| `SWE1-FOTA-313` | **(b) 有 id** | …vice shall coordinate the handling of the error conditions defined in System Requirements 4907672, 4907671, 4907670, 4907669, 4907668, and 4907667 by interacting with SWMC and the appropria |

### 2.4 ⚠ 反向探測揭出之兩條漏網路徑（直接回答 §六.6）

反向探測證實式B／式C／式D 之 0 命中為**語料真的沒有**（`listed` 0、
`as follows` 0、`section` 0、`table` 0、`chapter` 0、`refer to` 0、`see` 0）——
**該三式之零並非 regex 太嚴。** 但同一探測揭出六式**確實會漏**的兩類：

**漏網一：`defined in` 有 7 句、式A 只命中 3 句。**

| 037 列 | 句 | 式A | 性質 |
|---|---|---|---|
| `313`（×2） | `…error conditions defined in System Requirements 4907672, …` | ✅ | 指涉**需求物件** |
| `327` | `…resume conditions defined in System Requirements 4907683 and 4907684.` | ✅ | 指涉**需求物件** |
| `372` | `…software component dependencies defined in **the update metadata**…` | ❌ | 指涉**執行期資料** |
| `382` | `…target firmware image defined in **the update package**…` | ❌ | 指涉**執行期資料** |

式A 未命中之 2 句，其指涉對象為 **update metadata／update package**
——**執行期產物，不是規格中的需求物件**。就 R-SU15 之目的而言，
式A 漏掉它們是**正確的**（它們不是統攝型需求）。
但這證明「`defined in` + 名詞」之語形本身**不足以判別**，
**判別靠的是其後之名詞是否指涉規格物件** —— 而該判別**不是語形問題**。

**漏網二：式C 漏掉 `below mentioned`（語序倒置）。**

`SWE1-FOTA-128`：
> `The SWMC shall use the extracted parameters and metadata from **below mentioned parameters** to control from below and execute the OTA update workflow.`

式C 之 regex 要求 `listed below` / `as follows` 等**固定搭配**，
對 `below mentioned`（形容詞前置）不命中。全母體 `below` 僅 1 列，
即本列。**此為真漏網。**

> **執行層未因此修改六式** —— 改式即為看著結果轉旋鈕（§4.2）。
> 兩條漏網另列於此，供分析層裁定是否補式或改以其他判準。

### 2.5 式E／式F 之命中性質

- **式E**（`described/specified/referenced/detailed in`）2 列：
  `343`（`vehicle conditions specified in the deployment configuration file`）、
  `382`（`source firmware version specified in the differential update package`）
  —— **二者皆指涉執行期資料，非規格物件**，與漏網一同性質。
- **式F**（≥3 個 490xxxx 密集列舉）1 列：`313`，與式A 重疊。
  `327` 只列 2 個 id 故未達門檻 —— **式F 之 `{3,}` 對兩個 id 之列舉不敏感**，
  幸有式A 覆蓋。

### 2.6 兩群分類（R-SU15(b)/(c)）

| 群 | 列數 | 列 |
|---|---:|---|
| **(b) 有 id** | **2** | `SWE1-FOTA-313`、`SWE1-FOTA-327` |
| (c) 無 id | 2 | `SWE1-FOTA-343`、`SWE1-FOTA-382` |

> **執行層只分類語形，未裁定何者為統攝型**（R-SU15 判定屬分析層）。
> 惟依 §2.4／§2.5 之性質分析，(c) 群之 2 列所指涉者皆為**執行期資料**
> 而非規格物件 —— 若分析層認同，則 **(c) 群實為空**，
> 全母體之統攝型需求僅 `313`、`327` 二列，**且二者皆已是自證錨**。

---

## 3. T23b —— A-SU5 更正之 diff

依處分「二」，`ANOMALIES.md` 內 A-SU4 處分條文之正文改為 43／94，
舊值記於更正註（不留於正文）：

```diff
-  **＋** T12 對照表所判定歸屬於該物件之 Description 全文（45 個）。
+  **＋** T12 對照表所判定歸屬於該物件之 Description 全文（43 個）。

-  歸屬於章節物件之 Description（92 個）**不入需求物件語料**。
+  歸屬於章節物件之 Description（94 個）**不入需求物件語料**。

-  併入之 45 個須逐一列出（Description id → 宿主需求物件 id），
+  併入之 43 個須逐一列出（Description id → 宿主需求物件 id），

+> **更正註（A-SU5 處分 §二，2026-08-27）**：本條 §二 原載「45」「92」，
+> 係承 T12「首見為準」歸屬法之誤，實測為 **43**／**94**，
+> 更正依據 A-SU5（上繳包 08 §2.1）。舊值記於本註，不留於正文 ——
+> 該數字為條文之操作參數而非沿革陳述，留舊值將直接導致重建語料時再錯。
```

A-SU5 摘要列與節標題已改記 **RESOLVED**，處分文逐字入節（sha `ff02c0915cbf`）。

### 3.1 處分「四」之落實範圍

處分令「凡以首見定歸屬之產出，其歸屬欄皆須以宣告段位置重驗」。
執行層普查本 feature 之全部產出，**以首見定歸屬者僅一處**：

| 產出 | 是否以首見定歸屬 | 處置 |
|---|---|---|
| `ANCHOR_POOL.md` §六（Description 137 筆之歸屬） | **是** | 已全部以宣告段位置重驗並更正 2 筆 |
| `ANCHOR_POOL.md` §一–§五（分類） | 否 —— 採「宣告優先於文序」 | 不受影響 |
| `scripts/corpus_v2.py` 之語料 v2 | 否 —— 建構時即用宣告段 | 不受影響 |
| `framework_survey.py` 之 T18a/T18c 分群 | 否 —— 以 Heading／章節標題段為分節點 | 不受影響 |

---

## 4. T23c —— 受併宿主之可回測性檢查

受併宿主 **14** 個（A-SU4 所指之同一批）。

| 037 列 | 受併宿主 | 章 | 名次 | 分 |
|---|---|---|---:|---:|
| `SWE1-FOTA-319` | `4907707` | 4.13.1 | 2 | 0.173 |
| `SWE1-FOTA-321` | `4907673` | 4.12 | **1** | 0.220 |
| `SWE1-FOTA-322` | `4907673` | 4.12 | 3 | 0.178 |
| `SWE1-FOTA-268` | `4907355` | 4.5.1 | 2 | 0.361 |

**4 / 30 列**之候選內出現受併宿主（共 4 次），其中 `321` 之受併宿主為**首選**。

**全母體對照：42 / 311 列（13.5%）**之前 5 候選內含受併宿主。

### 4.1 這使 §9.1 之已知未驗項**變成可回測**

30 列擴充樣本一經裁定，即有 **4 列**可用以檢查虛高效應：
若該 4 列之正解**不是**其候選中的受併宿主，而該宿主仍排在高位，
即為虛高之直接證據。`SWE1-FOTA-321`（宿主為首選、分 0.220）最具鑑別力。

> **執行層只檢查出現與否，未預判其正解**（下放包 10 §五 T23c）。
> 4 列之樣本量小，其結論將只能是定性的。

### 4.2 一項須留意的量

全母體 13.5% 之列，其前 5 候選內含那 14 個受併宿主 —— 而該 14 個宿主
只佔 487 個物件之 **2.9%**。若受併與否對排名無影響，期望值應在 2.9%
附近（乘以 5 個候選位，粗略上界約 14%）。**13.5% 落在該粗略上界附近，
不構成虛高之證據，亦不構成無虛高之證據** —— 因為此比較未控制物件長度
與內容之混淆（長文本本就較易入候選，與是否受併無關）。
**列此數是為避免它日後被誤讀為證據。**

---

## 5. T23d —— PLAYBOOK 追加

`PLAYBOOK.md` §7 新增 **(5)**、**(6)**（全文見該檔 `:224`、`:241`）：

- **(5) 閉合式必須拆到被裁定的那個維度上** —— 三次量錯的東西各不相同
  （文字 → 邊界 → 歸屬），每次的閉合式都通過了，每次通過的都是別的維度。
  **總數閉合永遠是最弱的一式。**
- **(6) 指標之選擇本身即可掩蓋問題** —— `313` 於召回 PASS、於涵蓋率 FAIL；
  只報召回時該盲區**不是被隱瞞，是被指標本身濾掉了**。

---

## 6. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

---

## 7. 獨立自評

### 7.1 §六.6 所問：什麼樣的統攝語不會被這六式命中

**已實證兩條**（§2.4）：語序倒置（`below mentioned` vs `listed below`）、
以及**式F 之計數門檻**（`{3,}` 對只列 2 個 id 者不敏感，`327` 幸有式A 覆蓋）。

**另有三條為推理，本語料中未出現，故無法證實或證否**：

1. **代名詞式統攝** —— `The SWMC shall handle **these** conditions…`、
   `**the above** requirements`。六式全部依賴具名之指涉對象，
   對純代名詞回指無能為力。本語料 `above` 3 列、`below` 1 列，
   經目視皆非統攝用法。
2. **隱式統攝** —— 完全不用指涉語，僅以「協調／管理／編排」類動詞
   統攝他處定義之行為（如 `The X shall orchestrate the update workflow.`）。
   **這類在語形上與一般需求毫無差別，任何語形掃描都必然漏。**
   `313` 之所以被抓到，是因為它**恰好**寫了 `defined in System Requirements`
   並列出 id —— 若原作者寫成「shall coordinate error handling」而不列 id，
   六式全滅，且無任何線索。
3. **跨句統攝** —— 統攝語與 id 列舉分置兩句，中間隔句。
   式F 之 `\D{0,12}` 只容 12 個非數字字元，跨句即斷。

**故本輪之 4/311 應理解為「以語形可見之統攝型下界」，不是全集。**
R-SU15(e) 令「全母體普查」，語形掃描能做到的普查僅止於此；
真正的全集需要語意判讀，而那不在執行層權限內。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有一處，在 §2 的「聯集 4/311（1.3%）」。**

那個數字讀起來像是「全母體只有 1.3% 的列是統攝型」，
**而它實際只說「六式語形命中 1.3%」**。§7.1 之第 2 條（隱式統攝）
在語形上與一般需求無異 —— 若語料中存在，它既不在分子也不會被察覺，
**1.3% 這個分數對它完全無感**。

我在 §2.6 與 §7.1 都寫了限定語，但那個百分比仍會被記住而限定語不會。
**能誠實說的是：以語形可見者為 4 列，其中 2 列（`313`／`327`）已是自證錨、
另 2 列經性質分析指涉執行期資料。至於語形不可見者有多少，本輪答不到。**

### 7.3 一項我做了但下放包未要求的事

§4.2 之「全母體 13.5% vs 物件佔比 2.9%」對照。

下放包 T23c 只令檢查 30 列樣本。我另算了全母體，**並非為了佐證什麼，
而是為了防止該數日後被誤讀** —— 13.5% 乍看遠高於 2.9%，很容易被當成
虛高之證據，但它未控制物件長度之混淆（受併宿主本就是長文本，
長文本本就較易入候選）。**先把它連同「這不構成證據」一起寫出來，
比等它日後被單獨引用要好。**

---

## 8. 附錄 —— T23a 之語形命中全表

（各式之逐列原句摘錄見 §2 各式節；本輪命中列僅 4 個，未另立附錄。）
