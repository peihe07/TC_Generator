# 上繳 10 — User Profiles / Phase 2 前置與 pilot 取樣（**補落檔**）

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`10a_rulings.md`（R-U42～R-U45、R-G10）＋ `10b_tasks.md`（前置 1–3、作業 4–6）
- **落檔時點**：11 輪（依 R-U48）。10 輪之上繳僅以聊天貼出而未落檔，
  且該貼文於傳輸中多處截斷 —— **本檔之全部內容自實際產物重出，未以貼文為據**

> **R-U48 之要求**：上繳須寫入本檔方為交付，聊天貼文不算，
> 亦不得作為覆核之依據；**生成不得在落檔前開始**。
> 本輪（11）未生成任何 TC，`generated/` 仍為空。

---

## 0. 本檔之重出方式（逐項具名）

| § | 內容 | 重出來源（**非貼文**）|
|---|---|---|
| 1 | 六條標記 | `grep -nE "^R-(U3\|U15\|U22\|U36\|G4\|G7) \[" RULINGS.md` |
| 2 | gitignore／BASELINE | `git check-ignore -q`（exit code）、`git status --short`、`shasum -a 256 -c` |
| 3 | 自檢六項 | `python3 scripts/build_batch_context.py --selfcheck` 重跑 |
| 3.1 | 判準三版之經過 | `scripts/build_batch_context.py` 之原始碼註解（v1／v2／v3 逐條記於程式內）|
| 4 | 取樣 16 列 | `/tmp/sample.json` 之產生腳本重跑，逐列理由自該腳本之 `SAMPLE` 常數 |
| 5 | PLP 三讀法 | 重跑掃描，母體 180、三組命中逐條列出 |

---

## 1. 前置 1 — 條文入庫與標記修正（R-U42／R-U43）

R-U42～R-U45、R-G10 已逐字追加於 `RULINGS.md` 第十輪條文段。

### 1.1 六條標記之改動 —— **原文一字未改，僅首行插入標記**

| 條 | 改後之首行（自 `RULINGS.md` 讀出）|
|---|---|
| `R-U3`（L62）| `R-U3 [PARTIALLY SUPERSEDED by R-U25 — 「證據＝內文完整」之解讀；spec 基線檔名與 spec_mode = A 仍生效]  spec 基線 = SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_` |
| `R-U15`（L223）| `R-U15 [PARTIALLY SUPERSEDED by R-U27 — 阻斷範圍；其餘三項判讀仍生效] DR #4（PU1087／PU1088）之阻斷範圍` |
| `R-G4`（L286）| `R-G4 [PARTIALLY SUPERSEDED by R-G4-1 — 讀者數 2 更正為 3；檔名歸屬與不得無聲覆寫仍生效]  recon.py 之輸出檔名歸屬（全域）` |
| `R-U22`（L348）| `R-U22 [PARTIALLY SUPERSEDED by R-U39(2) — 引用範圍之限縮；「先驗可讀性」與「037 沒引用不等於 spec 沒寫」仍生效] PROF-001-01（PLP 表）之處置 —— 先驗可讀性，不逕列阻斷` |
| `R-G7`（L379）| `R-G7 [EXTENDED by R-G7-1 — 增補第二用途；第一用途未推翻]  反向驗證之對照組（全域慣例）` |
| `R-U36`（L589）| `R-U36 [PREMISE CORRECTED by R-U40 — 前提錯（斷字在 xlsx 側非 PDF 側），產出有效] 字內斷字之全量掃描` |

**`[SUPERSEDED by X]`（全稱）之用例為 0** —— 與 R-U42 之判定「整條失效者為 0」相符。

**原文未改之驗證方式**：標記插入於條號與其後之空白之間，
條文本體（第二行起）未被觸碰；上表所引之首行尾段即原文之開頭。

### 1.2 R-U43 —— `R-U8` 歸 B

`R-U8` 歸 **B 類（feature-specific）**，其註記已寫入 `RULINGS.md`：

| 部分 | 性質 | 權威 |
|---|---|---|
| 三閘之值 180／25／2、182 降對照輸出 | feature-specific | 本條（R-U8）|
| 「不得以 ID 形態判定 leaf」「閘值須以同一單位計」 | 通則 | **Comfort `R-C3`** —— R-U8 係引用，不重複升格 |

---

## 2. 前置 2 — R-U45 落地（`outline_map.json` 納入版控）

### 2.1 `.gitignore` 之修改

原 pattern **保留**，其後加 `!` 例外 —— 保留是為了看得出這條改過：

```
data/outline_map.json
!data/outline_map.json
```

原註解（「可由 build_outline_map.py 重建」）保留並標為**已失效**，
另記其失效之處：該檔現含 `pdf_text`（R-U25／R-U35(a) 之判讀基準）、
`divergence`（07 輪逐節稽核）與 `__meta__`，**三者皆非 `build_outline_map.py`
所能產出**，重建成本為 07／08 兩輪之工作量。

### 2.2 實測 —— 該檔已不再被忽略

```
$ git check-ignore -q features/user_profiles/data/outline_map.json ; echo $?
1

$ git status --short features/user_profiles/data/outline_map.json
?? features/user_profiles/data/outline_map.json
```

`exit=1` 表示**不被忽略**；`git status` 已將其列為未追蹤檔。

### 2.3 `BASELINE.sha256` —— 7 / 7 OK

```
$ shasum -a 256 -c BASELINE.sha256
inputs/…_SWQT_20260817_ext.xlsx: OK
../../spec-index/cache/SYS1_HMI_Personal_Account…(February_10_2023).xlsx: OK
../../spec-index/cache/SYS1_HMI_Personal_Account…(February_10_2023).json: OK
../../spec-index/sources/Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf: OK
inputs/FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx: OK
inputs/SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_(February_10_2023).xlsx: OK
data/outline_map.json: OK
```

**7 行 OK**（另有 3 行 improperly-formatted 警告，來自註解區塊，exit code 0）。

### 2.4 **待 Pei 執行之 git 指令清單（完整，未截斷）**

> **R-U48 明文**：11 輪之貼文於傳輸中截斷（`git add` 斷於
> `features/user_profiles/BA`），**該截斷版不得被執行或引用**。
> 以下為自本檔讀取之完整版。

```
git add features/user_profiles/.gitignore
git add features/user_profiles/BASELINE.sha256
git add features/user_profiles/data/outline_map.json
```

三行分列，**不以續行或萬用字元表述** —— 截斷之所以危險，
正是因為一條被截斷的 `git add` 仍是一條合法指令。

**執行層未執行任何 `git add`／`commit`**（R-G5／10b）。

---

## 3. 前置 3 — 生成前之組裝自檢：**6 / 6 PASS**

工具：`scripts/build_batch_context.py --selfcheck`（可重跑）。
10b 明文「逐項回報，不得以『已設定』帶過」，故每項皆印**實際注入之內容**。

### 3.1 第 1 項 —— `pdf_text` 而非 `text`，**判準改過兩次**

**現行判準（v3）以不變量驗，非以字串命中數驗**：

```
(i)  呼叫 `_outline()` 之函式 = ['selfcheck', 'spec_body']
     → 生產路徑僅 `spec_body`；`selfcheck` 為本檢查自身
(ii) `spec_body` 對 outline dict 取用之鍵 = ['pdf_text']
(iii) 抽樣 9.8：spec_body == pdf_text ? True ；== text ? False
```

**實證（9.8 之兩側尾 90 字）**：

```
pdf_text : …s changed, a popup will indicate that it has been changed for the active Profile (PU0609).
text     : …left the Profile section and will not have a back button to return to the Profile section.
```

**兩者之差就是 9.8 那句掉句本身**（`PU0609` 之整句條文，07 輪測得之真掉句之一）。

**判準之三版，逐版記其錯在哪**（原始碼註解為權威，此處轉錄）：

| 版 | 判準 | 為何錯 |
|---|---|---|
| **v1** | 掃全檔之 `['text']` | **8 處命中全在 `selfcheck` 自己** —— 它故意讀 `text` 以證明兩者不同。一個「不得讀 text」之檢查，把「證明 text 不同」那段也算進去，**永遠會紅** |
| **v2** | 改掃「生產路徑」（`_outline()` 至 selfcheck 之前）| **仍有 2 處**：`spec_body` 之 **docstring**、`assemble` 之 `m["text"]`（那是**補句表**之欄，不是 outline_map 之欄）。**字串比對把三個不同的 `text` 鍵混為一談** |
| **v3（現行）** | **改問真正的不變量** —— 只有 `spec_body()` 得觸碰 outline_map，且其取用之鍵只有 `pdf_text` | 可判定；字串命中數不可 |

**處置同 R-U37：改判準，不改案例。**

### 3.2 第 2 項 —— `must_carry` 之實際注入點（16 leaf 中 4 個）

| req_id | sec | 注入內容（前 60 字）| affected_field | pdf_source |
|---|---|---|---|---|
| `SWE1-HMI-PROF-091-01` | 9.3.2 | `****R1 High Only: "Stellantis Account" to be replaced with "…` | label 字面值（§8.7.3 variant）| PDF p14 |
| `SWE1-HMI-PROF-104` | 9.8 | `If a setting linked to the Profile is changed, a popup will …` | ER 列舉 ＋ PU 清單 | PDF p15 |
| `SWE1-HMI-PROF-111` | 11.4 | `Table CPA2.) Connected Account vs Local Profile` | ER 列舉（CPA2 表之身分）| PDF p17 |
| `SWE1-HMI-PROF-112-01` | 11.5 | `Connected FCA Account \| Local Profile \| Personalization \| Pr…` | ER 列舉（CPA2 表之列項）| PDF p17 |

**注入點**：`assemble()` 之 `must_carry` 鍵，由 `must_carry_for(section)` 取自
`data/xlsx_missing_clauses.tsv` 之 `must_carry == "yes"` 列。

**驗證方式**：`--selfcheck` 對 16 個抽樣 leaf 實跑 `assemble()`，
印出其 `must_carry` 陣列之長度與內容 —— **不是印「已設定」**。

### 3.3 第 3–6 項

| # | 項 | 實測 |
|---|---|---|
| 3 | Test Group／Test Set | Test Group = `{'User Profiles'}`（單一）；Test Set 實得 **8 組**：`Connected Account`／`Defaults`／`Editing`／`Preference Storage`／`Profile List`／`Setup Flow`／`Valet Mode`／`Welcome Flow` —— 與 framework §2 逐字相符 |
| 4 | `tc_id` 格式 | `NR1L-UserProfiles-{n:03d}`，樣例 `NR1L-UserProfiles-001`。**本檔不指派號碼**，指派為生成器之事 |
| 5 | `specification_reference` | 樣例（`111`，sec 11.4）＝ `Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.4`；含 `R1L-R` 檔名形式？ **False** |
| 6 | PLP 之 `3.x` 併列 | 當時 `PLP_ENABLED = False`（待裁）；抽樣中屬 `PLP_LEAVES` 者 `PROF-001-01`／`PROF-032`，其 spec_ref 皆不含 `3.` |

> 第 6 項於本輪（11）依 **R-U46** 已啟用，見上繳 11 §3。

---

## 4. 作業 4 — pilot 取樣清單（16 leaf，8 組各 2）

| Test Set | req_id | sec | Sub | 037 Priority | 選它的理由 |
|---|---|---|---|---|---|
| Preference Storage | `SWE1-HMI-PROF-001-01` | 4.1 | Service | High | **Service B 群 ＋ PLP 引用（乙側命中）** —— 一次覆兩項必含 |
| Preference Storage | `SWE1-HMI-PROF-002-03` | **4.1.1** | Service | Low | **spec 4.1.1** —— 驗 R-U27「可生成但不寫 popup 內文」（其內容即 PU1088）|
| Profile List | `SWE1-HMI-PROF-021-01` | 5.2 | HMI | High | 上限 5 之邊界（BVA 候選），驗數字取自 `pdf_text` 而非推定 |
| Profile List | `SWE1-HMI-PROF-032` | 5.9 | Service | High | **Service B 群 ＋ PLP 引用（甲∩乙皆命中）** |
| Defaults | `SWE1-HMI-PROF-048` | 6.2.1 | HMI | Medium | ch6 一般行為條（不強制先客製化 default）|
| Defaults | `SWE1-HMI-PROF-053` | 6.4.1 | HMI | Medium | ch6 popup 條 —— 其 PU0585 於 xlsx 側有、PU0575／0576 為 `pdf_only` |
| Welcome Flow | `SWE1-HMI-PROF-059-01` | 7.2.1 | HMI | Medium | 大型 welcome popup 之內容列舉 |
| Welcome Flow | `SWE1-HMI-PROF-062-02` | 7.4 | HMI | Medium | 30 秒逾時 —— 驗時間值取自條文 |
| Setup Flow | `SWE1-HMI-PROF-073-01` | 8.7 | HMI | High | username 12 字元上限之邊界 |
| Setup Flow | `SWE1-HMI-PROF-070` | 8.4.1 | Service | High | **Service B 群**（輸入 → 儲存 → 讀回）|
| Editing | `SWE1-HMI-PROF-091-01` | 9.3.2 | HMI | High | **must_carry 9.3.2**（R1 High label 覆寫）＋ 驗 `lint_variant_labels` |
| Editing | `SWE1-HMI-PROF-104` | 9.8 | HMI | Medium | **must_carry 9.8**（掉句：PU0609 之整句條文）|
| Connected Account | `SWE1-HMI-PROF-111` | 11.4 | HMI | Low | **must_carry 11.4**（Table CPA2 之標題與列項）|
| Connected Account | `SWE1-HMI-PROF-112-01` | 11.5 | HMI | High | ch11 App Store 行為 |
| Valet Mode | `SWE1-HMI-PROF-128-01` | 12.9 | HMI | High | 10 次錯誤 ＋ 30 分鐘鎖定之邊界 |
| Valet Mode | `SWE1-HMI-PROF-132-02` | 13.2 | Service | High | **Service B 群** ＋ SPAAK 變體（遠端解除）|

### 4.1 R-G10 餘數驗證

```
8 組各 2：{Preference Storage: 2, Profile List: 2, Defaults: 2, Welcome Flow: 2,
          Setup Flow: 2, Editing: 2, Connected Account: 2, Valet Mode: 2}
組數 8 / 應 8；每組皆 2 → True
相異 leaf 16 / 16；**餘數 0**
四項必含：{Service B 群: 4, must_carry: 3, 4.1.1: 1, PLP: 2} → 全數 ≥ 1
```

### 4.2 選樣過程中之一次更正

初版選 `SWE1-HMI-PROF-045` 為 `Defaults` 之一，**餘數驗證抓出其 Test Set 歸屬不符**
（`PROF-045` 之 sec 為 `5.16` → `Profile List`，非 ch6）。已換為
`SWE1-HMI-PROF-048`（sec 6.2.1）。**R-U47 已記錄並核可此更動。**

> **這正是 R-G10 之用途**：逐項讀過去看不出「這一條的組別填錯了」，
> 以 `Counter` 求各組之數才會露出來。

---

## 5. 作業 5 — R-U39(2) 之 PLP 前置掃描（生成前跑完）

**母體**：180 個 `Categorization == Functional Requirement` 之 leaf。
**判準字樣**：`PLP` 或 `Profile Linked Preferences`（不分大小寫）。

### 5.1 三種讀法，三個答案

**甲 —— 該 leaf 所引 spec section 之 `pdf_text` 含 PLP：2 個**

| req_id | sec | 命中脈絡 |
|---|---|---|
| `SWE1-HMI-PROF-012` | 4.5.4 | `…When default Driver 1-2 Profiles are restored, all Profile linked preferences are restored to the default state…` |
| `SWE1-HMI-PROF-032` | 5.9 | `…is not required to save any of the Driver Profile linked preferences. The Driver Profile Preferences will be…` |

**乙 —— 該 leaf 自身之 037 Description／Verification Criteria 含 PLP：4 個**

| req_id | sec | 命中欄 | 命中脈絡 |
|---|---|---|---|
| `SWE1-HMI-PROF-001-01` | 4.1 | Description | `…system shall store all profile-linked preferences listed in PLP table.` |
| `SWE1-HMI-PROF-005` | 4.3.1 | **Verification Criteria** | `…In the PLP table for Profile A, the newly changed preferences should be…` |
| `SWE1-HMI-PROF-012` | 4.5.4 | Description | 同甲 |
| `SWE1-HMI-PROF-032` | 5.9 | Description | 同甲 |

**甲 ∩ 乙** ＝ `PROF-012`、`PROF-032`
**甲 ∪ 乙** ＝ **4 個**

**R-G10 餘數**：`180 − 4（命中）− 176（未命中）= 0`

### 5.2 當時之回報：判準有歧義，且單採甲會排除起因

R-U39(2) 之字面為「掃全部 180 leaf 之 `pdf_text`」——
**照字面（甲）會排除 `PROF-001-01`，而該條正是催生 R-U22 與 R-U39(2) 之起因。**

且 `4.1` 之 `pdf_text` 為：

> `PRACC1.) The system will store and recall each unique Driver Profile's
> preferences: **see list of linked content above**. If a feature is
> unavailable for a vehicle or region, ignore requirement.`

**spec 確實指了 PLP 表，只是以位置（`above`）指涉而非以名字。**
字串判準抓不到這一種。

**故當時停下未生成，`PLP_ENABLED` 保持 `False`。**
本輪（11）之 **R-U46** 已裁：採**甲 ∪ 乙**，並將位置指涉列為**盲區**逐條人工判讀。

---

## 6. 本包（10 輪）之獨立判斷

| # | 事項 | 現況 |
|---|---|---|
| 1 | **PLP 判準之歧義** | 已由 R-U46 裁定（採聯集 ＋ 盲區人工判讀）|
| 2 | **位置指涉之盲區未掃** | 11 輪執行，見上繳 11 §3.2 |
| 3 | **`must_carry` 七條中 pilot 僅覆蓋三條** | R-U47 已裁：pilot 不要求全覆蓋，**餘四條須登記追蹤**；11 輪執行 |
| 4 | **本上繳包未落檔** | **本檔即其補正**（R-U48）|

---

## 7. 動作清單 —— 與 git 陳述逐項對照（R-G6）

**10 輪之動作**：

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案追加／首行加標記 | `RULINGS.md`（＋五條、六條標記改動）| 否 |
| 2 | **檔案編輯** | `.gitignore`（加 `!` 例外，原 pattern 與註解保留）| 否 |
| 3 | 檔案追加 | `BASELINE.sha256`（＋`data/outline_map.json`）| 否 |
| 4 | 檔案新建 | `scripts/build_batch_context.py` | 否 |
| 5 | **唯讀** | `git check-ignore`、`git status`（**唯讀，不改狀態**）| **是（唯讀）** |
| 6 | 唯讀 | spec PDF／xlsx、037、`data/*` | 否 |

**未執行任何會改變 repo 狀態之 git**：`add`／`commit`／`push`／`checkout`／
`restore`／`reset`／`stash`／`clean`／`rm`。
**已執行之唯讀 git**：`check-ignore`、`status` —— 用於驗證 R-U45 之落地。

**未動**：`framework.md`、`feature.yaml`、`generated/`（**未生成任何 TC**）、
`ANOMALIES.md`、`DATA_REQUESTS.md`、`DECISIONS.md`、
`data/` 之其餘檔、`inputs/`、**他 feature 之任何檔**。
