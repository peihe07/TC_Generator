# Project Profile — FW036 / R1L SWE1 User Profiles (Personal Account HMI Logic and Flow, Stellantis newR1L)

> **建立 2026-08-18，依 23 下放包 M-1。** User Profiles 原為九個 feature 中
> 唯一無 runtime profile 者 —— 22 輪立 §11 之方括號例外時具名了這一點：
> canon §11 之例外原文為 **when the feature profile says so**，而本 feature
> 無此檔，故該例外當時落在 `features/user_profiles/DECISIONS.md`，
> 並聲明**不宣稱已依 canon 形式立例外**。本檔補上該依據。

> **PRECEDENCE：本 profile 於與泛用 ASPICE SWE.6 指令衝突處 OVERRIDE 之。**
> 泛用規則於本 profile 未觸及之處仍全部有效。標 **[OVERRIDE]** 者取代特定泛用規則
> （被取代者逐條引用）；標 **[ADD]** 者為專案特有之增補。
>
> 結構條款參照 `FW036_R1L_Power_Profile.md`（最近之同類 —— 同為 BLANK 工作簿、
> 同為後補之 profile）。**結構條款可繼承，內容條款不可。**
> User Profiles 與 Power 無共同規格文件、無共同 037 家族，
> 故每一項內容條款皆自 User Profiles 自身之裁決重新導出。

---

## 0. Project identity [ADD]

- Program：Stellantis newR1L；範圍 **User Profiles**（Personal Account HMI）
- 生成母體 **180 leaf**（R-U4／R-U8）：`Categorization == Functional Requirement`
  逐列計數 **180**、`Heading` **25**、`Out of scope` **2**
  （`SWE1-HMI-PROF-017`／`035` 不生成 TC、不計入覆蓋率分母）
- **葉節點 182 之 ID 前綴形態值為對照輸出，不作閘**（R-U8）——
  依據 Comfort R-C3「逐字禁止以 ID 形態判定 leaf」
- **範圍上界＝該 180 leaf 母體（R-U56，26 輪 Pei 裁定）[ADD]**：
  **spec 有內容而 037 未為其產出 leaf 者，不生成 TC、不列覆蓋缺口、
  不向上游索取釐清** —— 我方不代 037 決定「什麼該是需求」，
  那屬 SWE.1／SWE.5（§8.2 之延伸）。
  據此 DR #3／DR #7 關閉為 **OUT-OF-SCOPE**、A-UP02 改列同類。
  **`3.1`–`3.5` 之使用不受影響**（R-U22／R-U46：其為 `PROF-001-01` 之
  in-scope 依據，繼續併列）。
  **本條為 feature-level；升為全域須 Pei 另行一句**（R-U13，不自推）。
  條文逐字見 `features/user_profiles/RULINGS.md` R-U56。
  **適用範圍之窄化（Z-1，38 輪）**：R-U56 只管「**037 未產出 leaf**」者。
  若該行為寫在**某個已存在之 leaf 之 description 內**（即使是本 TC 自己的），
  **那不是範圍外，是該 leaf 之斷言未被驗完**（§6）。
  掃描：`audit_consistency.py` 之 **Z-1**。
- **RD 答覆不回頭改已生成之 TC（R-U57，39 輪 Pei 裁定）[ADD]**：
  RD #5／#6 之答覆**只及於其後生成者**；已生成者不返工。
  **所免除者為字面形式之返工，不含判定翻轉** ——
  若答覆顯示某條會**假失敗或假通過**，須具名上報再議，
  **不得逕行套用本條**。條文逐字見 `RULINGS.md` R-U57。
- `tc_id` 形態 `NR1L-UserProfiles-{NNN}`；Test Group 欄 = `User Profiles`（R-U1／R-U2）
- **workbook_state = BLANK**（R-U6）；style authority = Home 之 done region
  （Arif 144 列），標 `cross-feature: style only`
- 交付工作簿母本：`…_SWQT_20260817_ext.xlsx`（R-G1 之全域母本）

### 0.1 語料現況（2026-08-18，28 輪）

| | |
|---|---|
| 已生成 | **108 條**（pilot 001–016、batch01 017–044、batch02 045–073、對造補洞 074–078、**batch03 079–108**）|
| leaf 覆蓋 | **100 / 180** |
| 未經第二人覆核 | **30 條**（`079`–`108`）|
| 第四批 | **未取樣** —— 待第三批覆核 |

**批界之寫法（R-4，28 包）**：第三批一律記為
**「ch4 剩餘 26 ＋ A-UP13 附掛 3」**（另加 `009` 之負向配對 1，共 30 條），
**不寫「第三批 ＝ ch4」** —— 附掛之三項落在 ch6／ch7，
**批界是被修訂，不是被稀釋。**

## 1. Requirements authority chain [ADD]

- **spec_mode = A**（R-U3；`R-U25` 修訂其解讀而非其模式）
- **spec 基線之雙載體（R-U25）**：**xlsx 為結構、PDF 為內文**。
  `SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_(February_10_2023).xlsx`
  提供節次結構與 Source ID namespace；**內文以同名 PDF 為準**。
  理由：xlsx 之 `Description` 側**掉句**（`data/xlsx_missing_clauses.tsv`）——
  9.3.2 之 `****R1 High Only: "Stellantis Account" to be replaced with
  "Connected Account"` 即只存在於 PDF。**只讀 xlsx 會寫出錯的字面值。**
- `specification_reference` 一律用 Source ID 字串
  `Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_{section}`
  （R-U1）—— **不用檔名之 `R1L-R (February_10_2023)` 形式**
- **覆蓋率不得以 `specification_reference` 推定**（J-1／D-UP17-01）——
  併列 `3.1`–`3.5` 不等於該五列皆已被驗證
- **覆蓋率是分母的性質，不是分子的品質**（42 包 §三）[ADD] ——
  「180 / 180」說的是**037 之每個 leaf 都有一條 TC**，
  不是「每個 leaf 都驗完了」。第六批即有四處於 remarks 具名
  「本條不保證」之留白（清單見 `framework.md` §4.2）。
  **交付說明引用覆蓋率時，須同時載明此句。**

### 1.1 037 之 leaf：**Description 為需求單位**（D-UP24-01）[ADD]

> 一個 leaf 之需求內容以 **`Description` 欄**為準；`Title` 欄為索引標籤，
> **不是需求單位**。兩者衝突時以 Description 為準，衝突本身須登記。

實測依據（180 leaf 全量）：Description 以 spec 條款編號起首者 **105 / 180**，
Title **0 / 180**；Description 前 60 字元逐字見於節文者 **120 / 180**；
對節文之詞彙涵蓋率 Desc **0.859** vs Title **0.667**。

**決定性論證**：只有 Description 能無重疊無缺漏地分割條文。
以 12.8（PVAL8）為例，四個 leaf 之 Description 恰好取其六個斷言；
若改以 Title 為單位，PVAL8 之「狀態列互動受限」將無 leaf，
而手套箱提示會有兩個 —— 且 `125-03` 之 Title 所指行為不在 12.8，
**與該 leaf 自己的 `outline` 相衝**。

現存錯位：**僅 12.8／12.8.1 之七個 leaf**（A-UP11，23 輪全量掃描確認）。

## 2. Test Set vocabulary [OVERRIDE — 取代泛用之自由形式標籤]

Layer 1 Test Group = `User Profiles`（R-U1）。
Layer 2 **已定版，八個值**（R-U20，採 B 案）：

```
Profile Basics / Switching / Preference Storage / New Profile /
Welcome Popup / Editing / Connected Account / Valet Mode
```

逐 leaf 之歸屬由 `scripts/build_batch_context.py` 依 037 之 Test Set 欄導出。

## 3. FW036 User Profiles house style（欄位規則）

### 3.1 Priority rubric [OVERRIDE — 取代 canon §10.2 之預設帶]

依 `docs/runtime/TEST_CASE_PRIORITY.md` **本文**，非 canon §10.2 摘要（R-U5）。

| 級 | 範圍 |
|---|---|
| **P0** | 本 feature 核心主流程：profile 建立、切換、偏好之儲存與回復、Valet Mode 進出、資料遺失風險項 |
| P1 | 主要功能之次要／進階操作、邊界與變化路徑、非主路徑分支 |
| P2 | 輔助功能，失敗對主功能影響有限 |
| P3 | UI 強化、罕用情境 |

**037 之 High/Medium/Low 僅為先驗**；衝突時以 rubric 為準，偏離須於 reasoning 具名。

**三層適用釐清**（條文本身未改，均見 `DECISIONS.md` D-UP16-01）：

1. **F-3（16 包）**：同時落核心五類與「邊界／非主路徑」兩帶時，以失效後果決定 ——
   核心能力失效或被繞過 → P0；輸入體驗或呈現降級 → P1
2. **附一（C-4，20 包）**：「偏好之儲存與回復」之邊界 ——
   **機制本身** → P0；**個別設定項之值與其呈現** → P2
3. **附二（K-1，21 包）**：**五類為例示，非窮盡** —— 不排除 canon §10.2 之其他
   P0 條件。再細一層：**防線成立本身 → P0；防線之回饋或呈現 → P2**

**J-9：不因 P0 比例上升而回頭調整判準。** 現況 P0 = 24 / 78。

**與 canon §8.7.4 之交互（P-1，24 包）**：§8.7.4 逐字載
`A visual state (greyed-out, dimmed) does NOT imply non-operability`。
故**「變灰」永遠只是呈現，不得據以判為防護機制** ——
一條只驗變灰之 TC，其判級上限為 P2（附二之「呈現」帶），
不論該變灰在語意上多像一道防線。防護本身須由「操作不生效／狀態未變」之
ER 承擔，該 ER 所在之 TC 方得判 P0。
先例：`TC-062`（變灰，P2）↔ `TC-063`（按下不生效、鎖定狀態未變，P0）。

**判級取其核心斷言，非取各 ER 之平均**：一條 TC 兼有防護與呈現兩種 ER 時，
以其核心斷言定級，不「取中」（21 輪之「兩者各半，取中」為誤，24 包 P-1 指出）。

### 3.2 Design Method [OVERRIDE — 限制 §12 之輸出字串]

值須為母本下拉選單九詞條之一（與 Power profile §3.3 同一機制，各自實測）：

```
功能測試 (Functional based ; no specific technique)
狀態轉換 (State Transition Testing)
決策表 (Decision Table Testing)
等價劃分 (Equivalence Partitioning, EP)
邊界值分析 (Boundary Value Analysis, BVA)
負向測試 (Negative Testing)
情境 / 用例 (Scenario / Use Case)
基礎故障注入 (Fault Injection)
探索性測試 (Exploratory Testing)
```

**形態一致性由 `scripts/audit_consistency.py` 之 K-4a 稽核**：
BVA 須有邊界對、狀態轉換須有 A→B、負向須有無效輸入或非法操作
（**其非法性得顯示於 ER 而非 procedure**）、情境須跨 ≥3 步或 ≥3 功能。

### 3.3 Square brackets [ADD — §11 之 profile-scoped 例外]

**canon §11 禁止方括號於 TC 輸出欄位，本 profile 對下列情形 OVERRIDE：**

> 逐字引自**該 TC 所引之節**（或其 must_carry）之方括號 token，
> 得於 TC 輸出欄位保留原記法。
> **作者自擬之方括號一律禁止**，含 UI 標籤（`[Media]`）與
> §4.3 之 placeholder 語法（`[Outcome] when [trigger]`）。

依據：`9.1.1`（EDPR1.1）之 spec 原文即為

> `8.4" will show the username in the Edit Username line like
> “Edit username: [username]”`

改寫為散文會改掉 spec 之逐字內容（§8.4.1），而 **TC-018 之 ER 要斷言的
正是「那一行長什麼樣子」** —— 拆成散文，斷言的對象就不再是原文那個形式。

**本例外與其閘同生，不得分離**：`lint_tcs.py` 之 **G19** 逐 token 對照被引之節，
溯不到者轉紅。**故本條不是禁令之豁免，是禁令之換一種驗法。**

前例：Home A-H10（Pop Up List 之 `<OK>`／`[OK, X]`）、
Power profile §3.2（訊號值 `[1h]`／`[0h]`）。
canon §11 逐字：`lint validates retained tokens against the cited source row
instead of banning them`。

**UI 標籤仍一律用雙引號**，不得用方括號、單引號、角括號。

### 3.3.1 Quoting boundary for display text [ADD — R-3，28 包]

> **測試者會在畫面上逐字讀到的一句文字，或可點擊元件之 label → 加雙引號。**
> **我方以清單形式轉錄之表格列項 → 不加。**

例：`TC-075`（散文中內嵌 spec 之顯示描述）**須加**、已加；
`TC-039`（Table PIP1 之 15 列）與 `TC-013`（Table CPA2 之 4 列）
為逐列轉錄，**不必改** —— 列表形式本身即標示其為轉錄。

反向掃描為 `audit_consistency.py` 之 **Q-1**（G18 只查引號**內**之字面值，
查不到「該加而未加」）。

**盲區（R-G11）**：Q-1 之 **≥7 詞閾值係看了結果才定**
（N=6 得 19 處／N=7 得 8 處／N=8 得 7 處）——
**短於 7 詞之未加引號顯示文字，本掃描看不見。**

### 3.4 Variant label overrides [ADD — R-U35 (c)]

`9.3.2` 之 PDF 註記 `****R1 High Only: "Stellantis Account" to be replaced
with "Connected Account"`：**於 R1 High 適用之 TC，其字面值不得出現
`Stellantis Account`**。

- 屬**字面值錯誤**（§8.7.3 之 market/variant label override），非風格分歧
- **R1 Low 不適用** —— 那些車上該 label 確實是 `Stellantis Account`
- **variant 之判定只掃條件陳述欄位**（`pre_conditions`／`test_procedure`，J-11）；
  **禁用字串之檢查仍及於 `remarks`** —— 兩者是兩件事
- 閘：`scripts/lint_variant_labels.py`
- **其適用範圍是否及於 ch9 全章之同名 label 尚未確定** —— RD #5，待上游

### 3.5 Variant pairing criterion V-1 [ADD — D-UP22-02]

> 凡 spec 有**明文之變體覆寫註記**，其所涉字面值出現於某條 TC 之 ER 者，
> **須配該變體之對造**；不配者須具名理由，**且該理由須不適用於已配者**。

- **觸發要件為「明文覆寫」，不是「另有一種配置」** ——
  否則 `(if applicable)`、螢幕尺寸、有無連網全部要配，判準會擴張到不可能執行
- 母體：`data/override_notes_m3.tsv` 之 `verdict == 覆寫`（現為 **6 個 axis**）
- 三分法：**覆寫**（指定另一字面值／另一種適用性）／**適用條件**（未指定替代物）／
  **狀態條件**（條件為執行期狀態而非變體）
- 閘：`scripts/audit_variant_pairs.py`（四項，含
  **「不配之理由須對已配者為假」之述詞實測**）

### 3.6 Delegation must name a leaf [ADD — 23 輪 M-2，A-UP12 之成因]

> `reasoning`／`remarks` 中之委派（「由…承擔」）**一律指名
> leaf id（`SWE1-HMI-PROF-…`）或 tc_id**，不得只指節次。

**理由**：節是一段文字，「那段文字含不含這個行為」要判讀，故不可測；
A-UP12（`TC-020` ↔ `TC-040` 之互指委派）因此不可能被任何既有閘攔下 ——
G17 驗引用欄、G18 驗字面值，**兩者都不讀那句話**。

閘：`scripts/audit_delegation.py`（D-1 指名／D-2 存在／D-3 節文含詞串）。
**D-3 為啟發式，其「黃」不等於「綠」**（見該檔之盲區聲明）。

## 4. Known upstream gaps [ADD]

| # | 項 | 狀態 |
|---|---|---|
| DR #3 | `3.1`–`3.5` 等 8 條無 leaf（037 側）| **CLOSED — OUT-OF-SCOPE (R-U56)**；記載保留 |
| DR #4 | `PU1087`／`PU1088` 之 popup 內文 | MEDIUM |
| RD #5 | R1 High label 覆寫之適用範圍（列級 vs 全章）| PENDING —— **獨立送出**（26 輪拆分）|
| RD #6 | 「有 app 之區域 × 不支援 connected profile 功能」是否可佈署 | PENDING —— **獨立送出**（26 輪拆分）|
| RD #7 | `9.1.1` 之另一側無 leaf（大螢幕版面）| **CLOSED — OUT-OF-SCOPE (R-U56)**；佐證保留 |
| A-UP11 | 037 之 title↔description 錯位 | **降為記載瑕疵，不關閉**（24 輪 P-4）—— 範圍僅 12.8／12.8.1；Description 為需求單位故 TC 內容未受影響 |
| A-UP12 | 互指之委派 | RESOLVED（22 輪）|
| A-UP13 | 外推之假委派（`TC-005`／`TC-007`）| PENDING —— 記載已更正，**覆蓋未補** |

## 5. Write-back [ADD]

- ~~**write-back 尚未執行**（R-U14 之解除條件未成立）~~
  **41 輪 A-UP09 RESOLVED，封鎖解除**；42 輪程式就位，43 輪實跑探針三段全綠。
  **尚未產出交付件** —— 未決 1（T:Z）待 Pei。
- `openpyxl` + `wb.save()` **禁用** —— 對 rev C 工作簿會摧毀 R 欄 x14
  dataValidation（R-G3，A-UP09 實測）。須以 `xlsx_surgical splice`
- **不得呼叫 `diff_cells()`**（41 包 §二）—— 其對本母本之 TC 分頁逾 100 秒
  未完成，而我方本就知道要寫哪些格
- 寫回起點：自首個資料列 append（R-U6 之 BLANK 綁定）
- **列序依 `req_id` 遞增**（Comfort 96 §1 之 Pei 裁定；42 輪具名此與 41 輪
  草案之偏離，抽為 `row_order` 參數）

### 5.1 宣告與生效須分得開（G-C，43 包）[ADD]

> **一個沒有被任何程式讀取的設定值，會一直看起來像是決定過的。**

`feature.yaml` 之 `write_back` 段，凡「值 ＋ 是否生效」成對之項目一律寫成
`<name>: {value, applied, why}`；`scripts/write_back.py` **只讀
`applied: true` 者**，並以 **WB-0** 驗「`applied: false` 之欄確實沒被寫」。

**宣告不刪** —— 它是一段有來歷的決定；刪掉就看不出曾經決定過什麼。

**`why` 為必填**（44 包 §三-2）。理由是本 feature 自己的對照：
`lint.popup_ids`（20 個 vs 現測 21 個）與 `done_region.style_authority`
（BLANK 之下無 done region 可保護）**同樣是宣告了而不生效**，
而它們比 `author_value` 好 —— **差別只在於前兩者寫了為什麼**。
`applied: false` 而 `why` 空白者，與「還沒想好」無法分辨；
**「經實測後選擇不做」與「沒做」在 yaml 裡長得一樣，只有 `why` 分得開。**

## 7. 方法：閘與人讀之分工 [ADD — 43 包 §一]

### 7.1 待判清單之讀法（G-D）

`audit_pending` 之報表**固定輸出被抑制之條數與其分組**。

> **一個永遠空的清單與一個壞掉的清單，輸出相同。**

故：「抑制 43 條」是**掃描仍活著的證據**，不是可以略過的意思。
**若某輪該數字歸零而語料未縮，須先查掃描本身**，不得逕自當作「沒有待判」。

### 7.2 可測範圍已到底（G-E）

30–41 輪每輪皆有缺陷產出；42 輪三支新程式一條 TC 都沒動。

> **那不是品質變好的證明，是可測範圍到底的訊號。**

自 43 輪起，**第五、六批 55 條之人工覆核為品質判斷之主要承擔者**，
**不得因「16 支閘全綠」而縮減其深度**。
閘所驗者為欄位內部之性質與跨欄之對應關係；
「這句話說的是不是對的事」不在其射程內。

### 7.3 上繳格式：「會轉紅」之斷言須指名案例（44 包 §三-1）[ADD]

> **凡上繳中出現「某情形會使某閘轉紅」之斷言，須指名是哪一個方向性案例
> 驗過它；指不出來者，改寫為「推測」。**

**成因是一次真實的錯誤**：41／42 兩輪寫「T:Z 不填則 WB-5 會紅」，
而 42 輪自我測試之第 ① 案（`vehicle_columns=None`）本來就是綠的 ——
**同一份上繳裡同時寫了「7/7 PASS」與「不填會紅」，兩者沒有被對起來**。

其結構性原因：**「未決」段是推論，「方向性案例」段是實測，
兩段之間沒有任何機制要求彼此一致**。本條即該機制。

### 7.4 無先例之判斷：先查他 feature 之交付件（44 包 §三-3）[ADD]

> **遇「無先例」之判斷，先查他 feature 之交付件，再論裁示。**

T:Z 七欄被送成裁示題，而答案就在 Comfort 已交付的檔案裡
（466 資料列逐列為空，且其 `NEVER_WRITE` 逐字列有該七欄）——
**查的成本是一支唯讀腳本、三十秒。**

**查的對象是交付件，不是他 feature 之 `feature.yaml`**（N-XF02 之教訓：
yaml 宣告了交付件並不帶的值）。**唯讀，且不得寫入他 feature 任何檔**
（R-U24／R-U30）。

**邊界（G-H，45 包）**：

> **他 feature 之先例可用，前提是兩者用的是同一份表單母本。
> 若其用的是別的表單，其填法不構成先例，只是參考。**

Comfort 之 T:Z 先例之所以成立，是因為兩個 feature 同用
`FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx`（rev C）。
**查之前先確認母本同一** —— 欄位字母、DV 範圍與 `allowBlank` 皆隨 revision 變動
（rev A/B 之 Q 欄尚未插入，其後各欄左移一格）。

### 7.5 靜態轉錄之時效（AA-1／G-F／G-G，44–45 包）[ADD]

**時效性不是「檢查」之性質，是任何靜態轉錄之性質。**
凡本 feature 產出而供他人據以判斷之靜態檔，一律加指紋：

| 類 | 工具 | 指紋範圍 |
|---|---|---|
| review pack | `build_review_pack.py --verify` | pack 所印之每一欄 |
| RD 查詢單、各批 ER 出處對照 | `stamp_static_doc.py --verify` | **全欄（保守）** |

**保守之方向是安全的**：誤判過期只是多重出一次，
誤判新鮮則是拿舊資料下判斷。**兩種錯之代價不對稱。**

**已 WITHDRAWN 之文件不標指紋** —— 指紋標的是「仍供人據以判斷之文件」，
標了反而使其看起來像現行版（`26_rd_queries.md` 即此）。

與 `audit_pending` 之 digest **方向相反**：那個防「改了不重判」，
這個防「判了舊的」。

#### 7.5.1 `--verify` 由產出方在上繳時附結果（G-G，45 包）

指紋之價值全在**覆核前真的跑一次**，而它不像其他閘會被例行跑到。
**每輪上繳一律附現行四份 pack 之當前 `--verify` 結果** ——
較「由讀者記得跑」可靠，因為**它不依賴另一層記得做一件事**。

若當輪有 TC 變動而致某份 pack 過期，**於同輪重出**，不留給下一輪。

## 6. 歸位清單 —— **本檔建立時，哪些條款移入、哪些留在原處**

23 包 M-1 要求「其餘 feature 級 `[OVERRIDE]`／`[ADD]` 條款一併歸位，
逐條說明其原載體與新載體」。

**移入本檔（原載體改為指向本檔）**：

| 條款 | 原載體 | 本檔 | 說明 |
|---|---|---|---|
| §11 方括號例外 | `DECISIONS.md` D-UP22-01 | **§3.3** | **本輪之主要目的** —— canon §11 明指載體為 feature profile |

**於本檔重述（原載體為裁決權威，不改、不搬）**：

| 條款 | 原載體 | 本檔 |
|---|---|---|
| Priority rubric 與三層釐清 | `RULINGS.md` R-U5＋`DECISIONS.md` D-UP16-01 | §3.1 |
| Test Set 八值 | `RULINGS.md` R-U20 | §2 |
| spec 雙載體（xlsx 結構／PDF 內文）| `RULINGS.md` R-U25 | §1 |
| variant label override | `RULINGS.md` R-U35 (c) | §3.4 |
| V-1 變體對造判準 | `DECISIONS.md` D-UP22-02 | §3.5 |
| 委派指名 leaf | 23 輪 M-2（本輪新立）| §3.6 |
| workbook BLANK 與 style authority | `RULINGS.md` R-U6 | §0 |
| 生成母體 180／閘值 | `RULINGS.md` R-U4／R-U8 | §0 |

**為何是「重述」而不是「搬移」**：`RULINGS.md` 為 Pei 裁決之**逐字登記**
（R19-2：原文貼入，不改寫不摘要）。**把裁決條文搬出裁決檔，會使裁決失去其權威載體。**
profile 是 runtime 之規則覆蓋層，兩者用途不同 ——
**唯一真正移入者是 D-UP22-01**，因為 canon §11 明文指定 profile 為其載體。

**未移入（判定為非 profile 條款）**：

| 條款 | 為何不移 |
|---|---|
| D-UP11-01／11-02（PLP 判準與 must_carry 追蹤）| 生成期之**素材處理**判準，非輸出格式規則 |
| D-UP12-01（同節連坐）／D-UP12-02（指涉口徑）| **判讀口徑**，屬 feature 之 spec 解讀，非 runtime 覆蓋 |
| D-UP16-02／D-UP17-01 之代價聲明 | **盲區聲明**，其位置須與被限制之判準相鄰才讀得到 |
| R-U7／R-U9／R-U12–R-U19 等流程條文 | 一次性之 Phase 0/1 流程裁決，非常設規則 |
