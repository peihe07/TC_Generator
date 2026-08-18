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
