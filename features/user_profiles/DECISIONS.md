# DECISIONS — User Profiles (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A
- spec text layer: [AUTO] text-layer: 39242 chars (via pymupdf)
- source files: [AUTO] 4 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 2 checked, 2 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 133 cited sections, all found in a 169-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 180
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 180 (list in recon.json)
- covered nowhere: [AUTO] 180 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_{outline}]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 180 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:

---

# 第十一輪之逐條判讀（R-U46 盲區／R-U47 追蹤）

## D-UP11-01 — PLP 自動判準之盲區：位置指涉之人工判讀（R-U46／R-G11）

**判準**：掃全部 **180 leaf** 之 `pdf_text`，命中
`above` / `listed above` / `see list …` / `see table …` / `below` / `table below`。
**結果**：命中 **17**、未命中 **163**、**餘數 0**（R-G10）。

逐條判讀其位置指涉**指向 PLP 表（spec 3.1–3.5）或別的東西**：

| # | req_id | sec | 指涉字樣 | 指向 | 判讀 |
|---|---|---|---|---|---|
| 1 | `SWE1-HMI-PROF-001-01` | 4.1 | see list of linked content above | **PLP 表** | **是** —— R-U46 已裁（該條亦由自動判準乙側命中）|
| 2 | `SWE1-HMI-PROF-001-02` | 4.1 | 同上（同節同句）| **PLP 表** | **是 —— 新增**，見下 §「同節之其餘 leaf」|
| 3 | `SWE1-HMI-PROF-001-03` | 4.1 | 同上（同節同句）| **PLP 表** | **是 —— 新增** |
| 4 | `SWE1-HMI-PROF-014` | 4.6.1 | as pictured above | 圖（username 圓框之示意）| 否 |
| 5 | `SWE1-HMI-PROF-047` | 6.2 | (see above) | 前段之 default Welcome Popup 流程 | 否 |
| 6 | `SWE1-HMI-PROF-066` | 8.2 | See flow … above | 8.x 之 New Profile 流程 | 否 |
| 7 | `SWE1-HMI-PROF-076-01` | 8.8 | show **above** the "Save & Continue" button | **版面方位，非引用** | 否 |
| 8 | `SWE1-HMI-PROF-076-02` | 8.8 | 同上 | 版面方位 | 否 |
| 9 | `SWE1-HMI-PROF-076-03` | 8.8 | 同上 | 版面方位 | 否 |
| 10 | `SWE1-HMI-PROF-078` | 8.8.2 | an example is pictured above | 圖（7" 分頁示意）| 否 |
| 11 | `SWE1-HMI-PROF-090` | 9.3.1 | any items listed above | **Table EDPR1**（行車限制項目）| 否 |
| 12 | `SWE1-HMI-PROF-091-01` | 9.3.2 | any of the above listed items ／ specified above | 同 11（Table EDPR1 ＋ 9.3.1 之訊息）| 否 |
| 13 | `SWE1-HMI-PROF-091-02` | 9.3.2 | 同上 | 同上 | 否 |
| 14 | `SWE1-HMI-PROF-106` | 10.2 | (see example above | **圖**（Profile Info Page 截圖）| 否（附註見下）|
| 15 | `SWE1-HMI-PROF-108` | 10.3.1 | the info in the chart above ／ Below are some examples | **10.3.1 頁內之 chart**（Nav 等分類範例）| 否（附註見下）|
| 16 | `SWE1-HMI-PROF-111` | 11.4 | See table CPA2 for list items | **Table CPA2**（Connected Account vs Local Profile）| 否 —— 另屬 must_carry |
| 17 | `SWE1-HMI-PROF-134` | 14.1 | Exit Valet Mode process above | 14.x 之流程 | 否 |

**判讀所得：17 命中中 3 條指向 PLP 表，其餘 14 條不是。**

### 同節之其餘 leaf —— 本輪之實質發現

R-U46 之裁定為「**4.1（PRACC1.）之併列 3.x 成立**」。
4.1 底下之 leaf 有**三個**（`001-01`／`001-02`／`001-03`），
而自動判準（甲∪乙）只抓到 `001-01` —— 因為只有它的 037 Description
字面寫了「PLP table」。

- `001-02`「system shall recall stored preferences when profile is activated」
- `001-03`「If a feature is unavailable …, skip storing & recalling that item」

**兩者所 store／recall／skip 的「preferences」，就是 PLP 表那份清單。**
併列 3.x 之理由對三條完全相同，故 `001-02`／`001-03` 一併列入。

**落地方式**：`build_batch_context.py` 以 `PLP_LEAVES_MANUAL` 分列，
**不併入 `PLP_LEAVES_AUTO`**（R-U46 明文）——
自動集合須維持「重跑掃描即可重算得出」之性質。

### 第 14／15 條之附註（判讀有猶豫，具名記下）

`10.2`／`10.3.1` 之「what is linked to a Driver Profile」與
「the chart above」，**語意上與 PLP 表高度重疊**（都在講「Profile 記住哪些偏好」），
但其位置指涉所指之物是 **ch10 頁內之圖／chart**，不是 spec 3.1–3.5 那張表。
依「指涉所指之物」判為**否**；若分析層認為應依「語意所涉之內容」判，
則此二條應改為**是** —— **此為判讀口徑之選擇，不是事實爭議**，故列此待裁。

### 本判準自身之盲區（R-G11）

以字樣掃描仍抓不到者，逐項聲明：

1. **完全無指涉字樣而實質引用 PLP** —— 例如僅寫 "the preferences"
   而不寫 above／list。本判準抓不到；處置：**接受漏失**，
   惟同節之其餘 leaf 已由上述「同節連坐」補上一層。
2. **圖內文字** —— PDF 文字層若未含圖中字，掃不到。處置：接受漏失。
3. **`below` 方向** —— 已納入字樣，本批命中 1 條（`108`）。
4. `above` 之**版面方位**用法（第 7–9 條）會造成偽陽性 ——
   本批以人工判讀濾除，**未改判準**（R-U37：偽陽性可由人工濾，
   偽陰性不行；本判準寧鬆勿緊）。

**故：本判準之「命中 17」不得被當作「全部引用 PLP 者」之全集**（R-G11）。

---

## D-UP11-02 — must_carry 未覆蓋條目之追蹤（R-U47）

**登記處之選擇**：記於 **`DECISIONS.md`**，不記 `DATA_REQUESTS.md`。
理由：`DATA_REQUESTS.md` 之標的為**須向上游索取之缺件**（DR #1–#4 皆屬此類），
而本項七條之內容**已在本地取得並入表**（`data/xlsx_missing_clauses.tsv`），
缺的只是**本地生成之覆蓋**。**把已到手的東西登記成待索取，會使 DR 清單失真。**

### 實測之覆蓋數 —— **與 R-U47 之前提不符，具名回報**

R-U47 載「pilot 僅覆蓋三條（9.3.2／9.8／11.4）」。
以 `--selfcheck` 第 2 項實測（16 leaf 逐一實跑 `must_carry_for()`）：

| outline | 覆蓋之 leaf | 狀態 |
|---|---|---|
| 9.3.2 | `PROF-091-01` | 已覆蓋 |
| 9.8 | `PROF-104` | 已覆蓋 |
| 11.4 | `PROF-111` | 已覆蓋 |
| **11.5** | **`PROF-112-01`** | **已覆蓋 —— R-U47 未計入** |
| 9.1 | — | **未覆蓋** |
| p14 | —（掛回 9.1）| **未覆蓋** |
| p17 | — | **未覆蓋，且見下之缺陷** |

**故實為「覆蓋 4、未覆蓋 3」，非「覆蓋 3、未覆蓋 4」。**
餘數驗證：`4 + 3 = 7` ✓。

### 待追蹤（**第一批正式批次前各至少覆蓋一次**）

| # | outline | 內容 | 覆蓋路徑 |
|---|---|---|---|
| T-1 | **9.1** | Resume Tutorials 之圈號 1 與其移除條件 | 生成 sec 9.1 之 leaf 時自動注入 |
| T-2 | **p14** | Table EDPR1 之列項（含 "Stellantis Account" 等五項）| 已掛回 9.1，隨 T-1 一併注入 |
| T-3 | **p17** | Connected Navigation 之列項（同 11.5 之表）| **見下：現況注入不到** |

### T-3 之缺陷（本輪發現，未自行修改）

`must_carry_for()` 對 `p<N>` 列之掛回條件為
「`section in ("9.1","11.4","11.5")` **且** 該列之 `impact` 字串含該節次」。

- `p14` 之 `impact` 含「9.1 之列項順序」→ **掛得回去**。
- `p17` 之 `impact` 為「**同上**」→ **不含任何節次字樣，掛不回任何節**。

**即：`p17` 在現行程式下，生成任何節次時皆不會被注入。**
`--selfcheck` 第 2 項之所以沒紅，是因為它驗「有注入者是否正確」，
**沒驗「七條是否都有歸宿」** —— 這是該自檢項自身之盲區（R-G11）。

**未自行修改**：把 `p17` 掛到 `11.5` 屬判讀（其歸屬節次 07 輪即載明「未逐一定位」），
依 §9.3 不自裁。**建議之處置**：`p17` 之 `impact` 欄改寫為明含「11.5」，
或於 `must_carry_for()` 增一條顯式對照表。**待裁。**

---

# 第十二輪之判準落地（R-U50／R-U51）

## D-UP12-01 — 同節連坐判準（R-U50，**feature-level，不升 canon**）

**四項條件須同時成立**：

1. 同一 spec section
2. 同一句指涉
3. 同一份被指之清單
4. **併列理由對各 leaf 完全相同**

成立則該節**全部 leaf** 一併列入 `PLP_LEAVES_MANUAL`。

**現行唯一適用之案例**：sec 4.1（`PRACC1.` "see list of linked content above"）
→ `PROF-001-01`／`001-02`／`001-03` 三條全數列入。

| 條件 | 4.1 之核對 |
|---|---|
| 同一 section | 三條之 `section` 皆為 `4.1` ✓ |
| 同一句指涉 | 三條所引之 `pdf_text` 為同一段 `PRACC1.` ✓ |
| 同一份被指之清單 | 皆指 spec 3.1–3.5 之 PLP 表 ✓ |
| 理由完全相同 | store／recall／skip 的都是那份清單，無一條另有別的理由 ✓ |

**不升 canon**：現僅一例。**一例不成通則** ——
登記為**通則候選**，第二例出現時重審。

**本判準之盲區（R-G11）**：
第 4 項「理由完全相同」**無可測形式**，須人工判讀。
故本判準**不得自動套用** —— 它是一張判讀時的核對表，不是一支腳本。
若日後要自動化，須先找到「理由相同」之可測代理，而目前沒有。

---

## D-UP12-02 — 指涉之判讀口徑（R-U51）

**採「指涉所指之物」，非「語意所涉之內容」。**

判準：該指涉字樣（`above`／`see list`／`see table` …）**實際指向之物件**是什麼。

**定案**（維持 11 輪之判讀，D-UP11-01 第 14／15 條之待裁已解）：

| req_id | sec | 指涉所指之物 | 判 |
|---|---|---|---|
| `SWE1-HMI-PROF-106` | 10.2 | Category／Title／Description 三欄表（Profile Info Page）| **否** |
| `SWE1-HMI-PROF-108` | 10.3.1 | 頁內 chart（Nav 等分類範例）| **否** |

**理由（逐字承 R-U51）**：採「語意所涉」則幾乎每條 preference 相關條文皆會
併列 3.x，**判準即失去分辨力**。

**代價明列**：
語意相關而未被指涉者**不併列 3.x**，其 `specification_reference` 不會指向 PLP 表。
**該覆蓋由 canon §8.2.1 之 sibling Req 承擔** —— 即
10.2／10.3.1 之 TC 仍會測到「Profile Info Page 列了哪些項目」，
只是其追溯鏈指向 ch10 而非 ch3。

**這是明知而選的代價，不是疏漏** ——
若日後發現 ch10 之覆蓋確實漏了 PLP 表之某項，該處置為
**補 sibling Req 或另立 leaf**，不是回頭放寬本判準。

---

# 第十六輪之判準落地（F-3／F-4）

## D-UP16-01 — P0 之 tie-break（F-3，**R-U5 之適用釐清，非新政策**）

一條 TC 同時落在 R-U5 之**核心五類**與「**邊界／非主路徑**」兩帶時，
以**失效後果**決定：

- 後果為**核心能力失效或被繞過** → **P0**
- 後果為**輸入體驗或呈現降級** → **P1**

**據此之現狀（不變）**：

| tc_id | leaf | 兩帶之重疊 | 失效後果 | 判 |
|---|---|---|---|---|
| TC-015 | `PROF-128-01`（12.9）| Valet 進出 ＋ 邊界（第 10 次錯誤 PIN）| **Valet Mode 可被繞過** | **P0** |
| TC-016 | `PROF-132-02`（13.2）| Valet 進出 ＋ 負向（主機退出被阻擋）| **Valet Mode 可被繞過** | **P0** |
| TC-003 | `PROF-021-01`（5.2）| profile 建立 ＋ 邊界（上限 5）| 可建出第 6 個 profile —— 呈現與上限管理降級 | **P1** |
| TC-009 | `PROF-073-01`（8.7）| profile 建立 ＋ 邊界（12 字元）| 輸入體驗降級 | **P1** |

### 附一 — 「偏好之儲存與回復」之邊界（C-4，20 包）

R-U5 之核心五類含「偏好之儲存與回復」。**該類之範圍須明文，否則會漂移** ——
下一批很容易出現「某個設定項也算偏好儲存」而被判 P0。

**分野**：

| | 判 | 例 |
|---|---|---|
| **儲存與回復之機制本身** | **P0** | `TC-004`（5.9 偏好之自動儲存）、`TC-031`（9.6 座椅位置之儲存與其歸屬）、`TC-001`（4.1 儲存與回復）|
| **個別設定項之值與其呈現** | **P2** | `TC-032`（9.6.1 Welcome popup 尺寸之預設值）、`TC-046`（12.1.1 狀態列版面）|

**判別問法**：失效時壞掉的是**「東西存不存得住」**，還是**「某一項的值是什麼」**？
前者為機制，後者為設定項。

**其盲區（R-G11）**：兩者之間有灰帶 —— 例如「某設定項之值在 key cycle 後遺失」，
既是該項之值也是儲存機制。**遇之以「該 TC 之受測單位」定**：
若 TC 驗的是該項之值，P2；若驗的是儲存本身（以任一項為載體），P0。

### 附二 — R-U5 之五類為**例示，非窮盡**（K-1，21 包）

R-U5 所列五類（profile 建立／切換／偏好之儲存與回復／Valet Mode 進出／
資料遺失風險）為**本 feature 之具體化**，**不排除 canon §10.2 之其他 P0 條件**
（safety、vehicle-critical CAN signal、boot/recovery、connection、audio output、
data-loss risk）。

**判別問法**：該條失效時，壞掉的是**使用體驗**，還是**車輛或其資產的防線**？
**後者不需要 R-U5 列它才成立。**

**再細一層（本輪為使 73 條可一致套用而立）**：同屬防線之條文，

| 該 TC 之核心斷言 | 判 |
|---|---|
| **防線成立本身**（被擋的東西確實擋住、受保護之資產確實沒動）| **P0** |
| **防線之回饋或呈現**（提示音、訊息、變灰之外觀）| **P2** |

例：`TC-021`（行車中受限項目**不可選取**）為前者 → P0；
`TC-022`（選取時播 bonk 與訊息）為後者 → P2 —— **兩者同節相鄰，判級不同。**

**此釐清使 `R-U5 無安全帶` 之待裁結案**（17→21 輪，四輪）。
**不因 P0 比例上升而回頭調整判準**（J-9 不變）。

**本條之範圍**：只界定 R-U5 之「偏好之儲存與回復」一類，
**不動 D-UP16-01 之 tie-break**（J-9：不因比例調整 rubric）。

**本條之盲區（R-G11）**：「失效後果」無可測形式，須人工判讀。
邊界情形（例如：使用者資料因輸入超長而被截斷 —— 是體驗降級還是資料損失？）
**本判準不自動給答案**，遇之須逐條判並記此處。

---

## D-UP16-02 — TC-004 未驗 5.9 之全稱（F-4，note，本輪不擴充）

5.9（PRACC15）之文為「**任何** Driver Profile linked preference 都不需按
記憶座椅之 set／save 控制」，而 TC-004 取 PLP 表 3.5 之
`Memory Profiles (Seats, mirrors, steering wheel)` **一項為代表**。

**pilot 階段接受**（F-4 明文）。
第一批正式批次時依 §8.2.2（RD sub-id ≠ TC 數）評估是否為 5.9 切多條。

**登記之理由**：這不是「取樣夠不夠」的問題，是**全稱命題以單例驗證**的問題 ——
單例通過不能證全稱成立。真要驗全稱，須 PLP 表五列逐項，
即 1 條 TC 變 5 條（或 1 條 TC 含 5 組資料）。**該決定屬批量規劃，不屬本輪。**

---

# 第十七輪之判準落地（J-1）

## D-UP17-01 — PLP `3.x` 併列之口徑與其代價（J-1，16 包 §7 第 1 項之裁定）

**採「條文對象讀」**：`specification_reference` 併列 `3.1`–`3.5` 之依據為
該需求之對象即整張 PLP 表 —— 4.1 之文為 store **all** preferences
**listed in PLP table**、5.9 之文為 not required to save **any** of the
Driver Profile linked preferences。TC 是對它抽樣。

**駁回嚴格讀之理由**：採「只列本次驗到的列」則追溯欄會隨抽樣而變 ——
**同一條需求的追溯欄因這次抽了哪幾列而不同，那就不是追溯。**

**與 F-1 之區別（不可類推）**：

| | 情形 | 判 |
|---|---|---|
| F-1（TC-013 之 `11.5`）| 11.5 是**另一條需求**（CPA3 之刪除／更新／安裝），與本 TC 無關，入列之唯一理由是**頁面共置** | **移除** |
| J-1（TC-001／004 之 `3.x`）| 3.x 是**同一條需求之對象** | **保留** |

### 代價（**R-G11 之盲區聲明，須隨引用欄一起被讀到**）

> **`specification_reference` 併列 3.1–3.5 不等於該五列皆已被驗證。**
> **覆蓋率稽核不得以引用欄推定覆蓋。**

實況：

| tc_id | 併列 | 實際受測 | 未受測 |
|---|---|---|---|
| TC-001（4.1）| 3.1–3.5 | 3.1／3.2／3.4 | **3.3、3.5** |
| TC-004（5.9）| 3.1–3.5 | 3.5 | **3.1–3.4** |

PLP 各列之實際覆蓋深度由 D-UP16-02（全稱命題以單例驗證）承擔。
本句已同時寫入 `framework.md` §4.1（覆蓋率判準處），
使稽核者在算分子時就讀得到，而不是回頭翻 DECISIONS 才發現。

---

## D-UP22-01 — §11 方括號之 profile-scoped 例外（L-1，22 包，**採 (a)**）

### 所擇：**(a) 立 profile 例外，並以 lint 對照來源驗證**

22 包給的是 (a) 立例外／(b) 改寫。**採 (a)。**

**理由**：9.1.1 之 spec 原文即為

> `8.4" will show the username in the Edit Username line like “Edit username: [username]”`

(b) 之改寫（`as “Edit username:” followed by the username`）**會改掉 spec 之逐字內容**，
而 §8.4.1 禁止改寫。TC-018 之 ER 要斷言的正是「那一行長什麼樣子」——
把 placeholder 拆成散文，斷言的對象就不再是原文那個形式。

**惟 22 包之警語照收**：立一個沒有邊界的例外等於沒有規則。故本例外**與閘同生**，
兩者不得分離 —— 見下。

### 例外之範圍（逐字）

> 逐字引自**該 TC 所引之節**（或其 must_carry）之方括號 token，
> 得於 TC 輸出欄位保留原記法。
> **作者自擬之方括號一律禁止**，包含 UI 標籤（`[Media]`）與
> §4.3 之 placeholder 語法（`[Outcome] when [trigger]`）。

依據：canon §11「Exception (profile-scoped)」逐字載
「lint validates retained tokens against the cited source row instead of
banning them」—— **本例外之形式即該句所指者**。前例：Home A-H10、
Power profile §3.2（訊號值 `[1h]`／`[0h]`）。

### 閘（G19，`scripts/lint_tcs.py`）

**本閘不是禁令，是對照**：每個方括號 token 須在被引之節之原文內逐字找得到，
找不到者轉紅。方向性案例 5 條，其中最關鍵的一條是
**「同一個 token、換一個被引之節 → 須紅」** ——
它守的是「對照的是來源，不是一張 token 白名單」。
若日後有人把本閘改成「`[username]` 一律放行」，紅向仍全過而**那一條會倒**。

### **本條已移入 profile 檔（23 輪 M-1）—— 權威載體變更**

22 輪立本條時具名之記載限制（canon §11 之例外原文為
「when the **feature profile** says so」，而本 feature 無 profile 檔）
**已於 23 輪解除**：

> **權威載體：`docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md` §3.3。**

本節之條文與理由留檔（不刪，R19-2 之同旨：已結輪次不回溯編輯），
但**以 profile 檔為準**；兩者若日後分岔，以 profile 檔為權威。
**自 23 輪起得聲稱本例外係依 canon §11 之形式所立。**

---

## D-UP22-02 — 變體對造之一致判準 V-1（L-3，22 包）

### 條文

> 凡 spec 有**明文之變體覆寫註記**，其所涉字面值出現於某條 TC 之 ER 者，
> **須配該變體之對造**；不配者須於 reasoning 具名理由，
> **且該理由須不適用於已配者**。

### 觸發要件為「明文覆寫」，不是「另有一種配置」

判準之全部重量在這一句。若觸發要件寫成「ER 內容隨配置而異」，
則 `(if applicable)` 之 Navigation、8.4 吋螢幕、有無連網全部要配 ——
**判準會擴張到不可能執行，然後被整個放棄**。

觸發母體取 `data/pdf_starred_notes.tsv` 之 `kind == 變體覆寫註記`，
**現為 4 條**，spec 側新增時閘會紅。

### 不觸發之三例（具名，以便覆核）

| 情形 | 為何不觸發 |
|---|---|
| `Navigation (if applicable)`（10.3.1）| **適用條件**，非覆寫 —— spec 未指定另一個字面值 |
| 8.4 吋螢幕（9.1.1）| 9.1.1 **本身即該尺寸之條文**，非對他節之覆寫 |
| 有無連網（11.3）| 條件式顯示，非字面值覆寫 |

**此三者仍可能各有覆蓋缺口**（例：9.1.1 之另一側版面 —— 大螢幕上
username 與 avatar 顯示於清單左側，現行語料**無人驗**）。
那是**取樣範圍**之問題，不是變體對造之問題；**混為一談會使兩者都查不清**。
已列上繳 22 §6 之待驗項。

### 閘（`scripts/audit_variant_pairs.py`，四項）

其中閘 4 把 L-3 之原話做成可測：**不配之理由以述詞實作**，
閘逐條驗該述詞對不配者為真、**且對已配者為假**。
`absence-only` 之述詞首跑即抓出兩處**述詞自身之錯**（見該檔 docstring）——
**閘沒壞，是我寫的述詞壞了**，兩者輸出形狀相同，靠的是它同時驗兩個方向才分得開。

---

## D-UP24-01 — **description 為需求單位，title 為索引標籤**（P-4，24 包）

### 判準

> 037 之一個 leaf，其**需求內容以 `Description` 欄為準**；
> `Title` 欄為人為擬定之索引標籤，**不是需求單位**。
> 兩者衝突時以 Description 為準，且**衝突本身須登記**（A-UP11）。

19 輪已依此生成 12.8／12.8.1 之七條，但當時只寫「§8.2 之單位權威，
而單位之內容以其 Description 為準 —— 標題不是內容」，**未給證據**。
24 包 P-4 把它升為阻塞第三批之前置，本輪補上證據。

### 證據（180 leaf 全量實測）

| # | 量測 | 結果 |
|---|---|---|
| 1 | Description 以 spec **條款編號**起首（`EDPR1.)`／`PVAL8.)` …）| **105 / 180** |
| 2 | Title 以條款編號起首 | **0 / 180** |
| 3 | Description 之前 60 字元**逐字**見於該節 `pdf_text` | **120 / 180** |
| 4 | 對該節 `pdf_text` 之詞彙涵蓋率（平均）| Desc **0.859** vs Title **0.667** |
| 5 | 逐 leaf 比較 | Desc 較高 **130** ／ Title 較高 29 ／ 平手 21 |

**第 1、2 項是決定性的**：Description 常常**就是條文本身**（連條款編號一併帶入），
Title 則從無一條如此 —— 兩者不是同一種東西。

### **決定性論證：只有 Description 能分割條文**

以 A-UP11 之現場（12.8 / PVAL8）驗之。該條文有六個斷言，
四個 leaf 之 **Description 恰好無重疊、無缺漏地分割它**：

| leaf | 其 Description 所取之斷言 |
|---|---|
| `125-01` | 只有 HVAC／Media 可用 ＋ Media 內 Device Manager 鎖住 |
| `125-02` | Projection／native HFP 停用 ＋ VR 不啟用 ＋ 五個區域鎖住 |
| `125-03` | 狀態列互動受限（僅 Valet Profile 與 HVAC 圖示例外）|
| `125-04` | 所有不可互動項變灰 |

**若改以 Title 為單位，同一組 leaf 會同時產生缺漏與重複**：

- `125-03` 之 Title 為 `Glove Box Lock Prompt on Valet Mode Entry` ——
  **PVAL8 通篇沒有手套箱**；該行為屬 12.8.1。
  即 Title 所指之物**與該 leaf 自己的 `outline` 相衝**。
- 於是 PVAL8 之「狀態列互動受限」**將無任何 leaf**，
  而手套箱提示會**同時有兩個 leaf**（`125-03` 與 `126-01`）。

**一個需求單位不可能指向不屬於自己章節的行為。** Title 會，Description 不會。

### 連帶判定：`TC-057`～`TC-062` **不重生成**

六條皆依 Description 生成，而 Description 即需求單位 ——
**其驗證目標未錯置**。24 包 P-4 所慮之「驗的可能不是該 leaf 所指者」不成立。

**其 TC 標題**由執行層依 Description 另擬（19 輪即如此），**未沿用 037 之錯位標題**，
故亦無標題誤導之殘留。

### 盲區（R-G11）

1. **本判準不使 A-UP11 之錯位消失** —— 只是使它**不影響 TC 內容**。
   任何以 037 `Title` 為索引找 leaf 的人，在 12.8／12.8.1 仍會找錯。
   **A-UP11 因此降為記載瑕疵，但不關閉。**
2. **29 個 leaf 之 Title 涵蓋率高於 Description** —— 多為 Description 係
   split leaf 之改寫者（如 `001-01`）。本判準對它們仍成立
   （改寫者仍是需求內容，Title 仍是標籤），**但第 3、4 項證據對它們較弱**。

---

## D-UP11-01 之 J-15 複核更正（37 輪；**加註，原表不刪**）

20 輪之 `20_batch03.md`（**未被執行之下放包**，36 輪查出）其 J-15 作業 3 要求：
複核 11 輪盲區掃描 17 條命中之其餘 16 條，是否有同型之「**結論對、理由錯**」。
36 輪查出該項從未執行，37 輪補做。**16 條之結論全部不變；理由更正五處。**

| leaf | sec | 原理由 | **正確之指涉** |
|---|---|---|---|
| `047` | 6.2 | 前段之 default Welcome Popup 流程 | **頁內之圖** —— ch6 之前**無任何 Welcome Popup 條文**（6.1 為 R1 High 之 CPA 註記），而 ch7 之 `PRWEL` 在其**下方**；其 037 description 另帶 `(image: …)` |
| `066` | 8.2 | 8.x 之 New Profile 流程 | **頁內之流程圖** —— 同一句之 `not **pictured** here` 即證被指者為圖 |
| `090` | 9.3.1 | Table EDPR1 | **9.3 自身之散文列舉**（`Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info…`）。Table EDPR1 是 9.1 之選項順序表，與行車限制無關 |
| `091-01` | 9.3.2 | Table EDPR1 ＋ 9.3.1 之訊息 | **前半錯、後半對** —— 應為 9.3 之散文列舉 ＋ 9.3.1 之訊息 |
| `091-02` | 9.3.2 | 同上 | 同上 |
| `108` | 10.3.1 | 頁內之 chart（Nav 等分類範例）| **方向正確但未複位** —— 20 輪 C-1 已精確複位為 **PDF p16 之 Table PIP1**（15 列），本輪不另改述 |

**該錯誤理由未流入語料**（37 輪查證）：
`TC-022`（`090`）之 reasoning 逐字為「受限項目之清單**出自 9.3**，故併列該節」——
**寫的是對的**。`TC-011`／`TC-023` 之 remarks 雖提及 Table EDPR1，
但那是指 **9.3.2 之 R1 High 列級覆寫**（其 `****` 標於 p14 之該表某列），
**與本處之指涉是兩件事，且該記載正確**。

> **故：錯的只有上表那三格，TC 本身沒有受影響。**

**原表保留不刪**（同 36 輪 R-2 之先例）——
**刪掉就看不出曾經給過錯的理由**，而「結論對、理由錯」正是本 feature
反覆出現之形態（34 輪之 `phrase_of` bug 亦同型）。

**`047`／`066` 之正確指涉未經版面複位**（未如 `108` 那樣以座標定位）——
其判定依「該章之前無該條文」＋「description 帶 image 標記」＋
「`not pictured here`」三項推得。**兩者皆尚未取樣；取樣時應以版面複位確認。**

---

## D-UP41-01 —— 「解除封鎖」與「使用該解除」不由同一層做（41 包 §一記入）

40 輪之 DV gate 立起並實跑後，R-U14 之解除條件**逐字成就**。
執行層**未**逕行把 A-UP09 改為 RESOLVED，理由記於當時之上繳：

> 解除同時解除「本 feature 之寫回實作不得開工」之封鎖，
> 而 40 包明文「本包只做 gate，不做寫回」。
> **把封鎖之解除與封鎖之啟用者放在同一個人手上，正是 R-U14 當初要避免的事。**

41 包裁：**該分辨成立**，並由分析層落槌。

**本條之適用形態（供日後援引）**：凡一項封鎖之解除條件由**執行層自己**
以其產出滿足者，執行層得回報「條件已成就」並具名其判斷，
**但不得自行改判該封鎖之狀態**。
與此相對，**41 包 §四之 RD 授權則明文授出了逕行修正之權** ——
兩者並不矛盾：前者是**封鎖之狀態**，後者是**條件之內容**。

---

## 版本綁定（R-G45，2026-09-05）

依 `down/20260905_GC-02.md` §一-3 落檔。本節所列為本 feature 之 `inputs/` 內、
屬 R-G45 六類共用參考檔而其 sha256 **不在** `forms/` 同類現行版之 sha 集合者。

| `inputs/` 檔名 | sha8 | `forms/` 同類現行版 | sha8 | 是否影響已交付 TC |
|---|---|---|---|---|
| `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | `b0827f02` | `Pop Up List HMI R1 (26PI).xlsx`<br>`Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `ff47b7be`<br>`dc078763` | ~~**PENDING 分析層判**~~ → **待證 → 傾向不影響** —— 變動之 2 個 PU id grep 命中 **0/2**；對照向：該簿引用 PU id 17/1340，**變動之 2 id 不在該 17 之內**。分母非 0，故本次 0 命中有證據力；仍留待證，因非 key 分頁未查（R-G11）。 |


**「是否影響已交付 TC」之判（分析層，`down/20260905_GC-03_review.md` §四；GC-04 §一-4 抄回）**。前提：本 feature 之 `delivered/` 為空，故以「現存最新工作簿」為對象。原 `PENDING 分析層判` 依 R-TM13 以刪除線保留。

**本 feature 待記 1 檔次**（全域 5 個 feature／13 檔次）。
「是否影響已交付 TC」執行層不判（GC-02 §一-3 明文）；分析層已於 2026-09-05 逐列判訖，見上表右欄。

**查詢式與命中數（R-G50）**——

```text
母體：docs/reports/source_identity_20260905.tsv（220 列，GC-01 §二-1）
篩選：path 符合 ^features/<feat>/inputs/
      且 filename 屬 R-G45 六類之一（DBC=*.dbc；LID=前綴 'Logical Identifiers and CAN Mapping'；
      PROXI=前綴 'PROXI_'；HMI Settings List／Pop Up List=同名前綴；
      Market Config=含 'Market Configuration Table'）
      且 sha256 不在 forms/ 同類之 sha 集合內
命中：1 列（本 feature）／13 列（全域，跨 5 個 feature）
腳本：GC-02 執行層量測腳本，與 up/20260905_GC-01.md 11-3 節同一判準
```
