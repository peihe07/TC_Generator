# 上繳包 02 —— 母本改定、workbook_state 改判與 Phase 1 前置

- 日期：2026-08-23
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/02_baseline_switch.md`
- 前一包：[upstream/01_intake.md](01_intake.md)
- 執行狀態：**步驟 1–10 全部執行完畢。** 停止條件均未觸發（逐條見 §12）。
  **零寫回工作簿內容**；git 之改狀態操作零次。

---

## 1. §二六條之抄錄核對表（步驟 1）

抄錄方式同 01 包：`re.findall` 自 handoff §二之 fenced block 直接取字串寫入，
未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立再抽取**
後計 SHA256。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH7 | 交付母本為 forms ext；客戶那份降為來源複本 | 545 | `78b740e423d40164` | `78b740e423d40164` | 逐字相符 |
| R-PMH8 | `workbook_state` = `BLANK`；撤回 `PREFILLED_DRAFT` | 400 | `533aac08d7e1c3da` | `533aac08d7e1c3da` | 逐字相符 |
| R-PMH9 | 欄位對應作廢重測，四方交叉佐證 | 325 | `e32121320838363a` | `e32121320838363a` | 逐字相符 |
| R-PMH10 | D3／D4／D5 一律留空 | 304 | `885070968235b262` | `885070968235b262` | 逐字相符 |
| R-PMH11 | `MANIFEST.sha256` 入版控 | 347 | `bbba2810887e6e96` | `bbba2810887e6e96` | 逐字相符 |
| R-PMH12 | 跨表列號以 id 實測，不以位移推算 | 146 | `e56341f8ea5c4b56` | `e56341f8ea5c4b56` | 逐字相符 |

### 1.1 R-PMH6 勘誤附註之落實證明（原文 SHA256 未變）

`RULINGS.md` 之 01 包六條，於本輪加入 R-PMH6 勘誤附註**之後**再度獨立抽取：

| 條號 | SHA256（前 16） | 與 01 包上繳所記 |
|---|---|---|
| R-PMH1 | `468fc43132ac1b9f` | 相同 |
| R-PMH2 | `19f57d23b1cf9800` | 相同 |
| R-PMH3 | `84acd49a1fc7f6ae` | 相同 |
| R-PMH4 | `04d87eb139a11e2b` | 相同 |
| R-PMH5 | `e589281f93426f27` | 相同 |
| **R-PMH6** | **`5bb6ebe395b25187`** | **相同** |

勘誤附註以獨立引用段落置於 R-PMH6 之 fenced block **之外**，
故原文一字未動。**A-PMH01 → RESOLVED**（狀態已於 `ANOMALIES.md` 更新）。

---

## 2. 步驟 3 —— 客戶那份 036 之三個附屬分頁全 dump

量測對象：`inputs/…_SWQT_PowerModingHMI_20260819.xlsx`（SHA256
`2be63feb…664625a54`，`shasum -c` OK）。以下為**全部非空儲存格**，未摘要、未判讀。

### 2.1 `Test Case Framework` —— **完全空白**

| 項 | 值 |
|---|---|
| `dims` | **`A1:A1`** |
| `max_row` × `max_col` | 1 × 1 |
| **非空儲存格** | **0** |
| 合併儲存格 | 無 |

**Q8 得解：該分頁為空。** 與 Power Management 之 A-PW56 前例（實測 0 非空
儲存格）同型。依 Q8 之分析層提案，**R-PMH6 之輸入維持兩項**（FROP 12 值、
規格目次），不新增第三個輸入。

此項同時清償 01 包 §9 第 6 項（執行層自評風險最高者）。**結果為陰性** ——
該分頁不含客戶側之 Test Group／Test Set 期望值。停止條件 8 未觸發。

### 2.2 `Reference` —— 35 個非空儲存格

`dims=A1:F20`，無合併。

| 座標 | 值 |
|---|---|
| B3 | `No.#` |
| C3 | `Test Case Design Methods` |
| B4 / C4 | `1` / `功能測試 (Functional based ; no specific technique)` |
| B5 / C5 | `2` / `狀態轉換 (State Transition Testing)` |
| D5 | `有模式 / 流程的功能（播放、暫停、鎖定等）。` |
| E5 | `例：Stopped + Play → Playing；Stopped + Resume 應被拒。` |
| B6 / C6 | `3` / `決策表 (Decision Table Testing)` |
| D6 | `條件×結果矩陣；多規則決定動作時用。` |
| B7 / C7 | `4` / `等價劃分 (Equivalence Partitioning, EP)` |
| D7 | `將行為相同的輸入分組，每組取代表值（含有效/無效）。` |
| E7 | `例：本機/USB/BT/串流；格式：支援/不支援。` |
| B8 / C8 | `5` / `邊界值分析 (Boundary Value Analysis, BVA)` |
| D8 | `錯最常發生在邊界；測上下限與**±1**；有範圍/閾值就用。` |
| E8 | `例：音量 0、1、99、100、101。` |
| B9 / C9 | `6` / `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)` |
| D9 | `兩兩 / 三三組合覆蓋交互；參數 / 組態很多且彼此影響。` |
| E9 | `例：機型×語言×來源×格式。` |
| B10 / C10 | `7` / `情境 / 用例 (Scenario / Use Case Testing)` |
| D10 | `按真實流程端到端驗證；跨模組時用。` |
| E10 | `例：插USB→掃描→播放→來電中斷→掛斷自動恢復播放。` |
| B11 / C11 | `8` / `負向測試 (Negative / Invalid)` |
| D11 | `故意做錯（錯的值 / 錯順序 / 缺前置），看系統會不會擋住＋提示。` |
| B12 / C12 | `9` / `基礎故障注入 (Fault Injection Lite)` |
| D12 | `把環境/依賴弄壞（斷網、逾時、拔裝置），看系統是否可恢復。` |
| C19 | `動態測試用的測試設計技術類型：` |
| C20 | `https://www.astralweb.com.tw/test-design-technology-equivalence-partitioning-introduction-and-application/` |

⚠ **C9 之字串為 `Pair-wise / N-wise`，而 `下拉選單!A6` 為 `Pairwise / t-wise`**
—— 同一方法在兩個分頁之寫法不同。`design_method` 之 lint 權威為
`下拉選單`（x14 DV 之 source 範圍），非 `Reference`。詳見 §6。

### 2.3 `QS Suggestion` —— 19 個非空儲存格

`dims=A1:B10`，合併 `A1:B1`。

| 座標 | 值 |
|---|---|
| A1 | `25/10/15 QS確認後建議` |
| A2 / B2 | `1` / `表單 : 增加中文敘述` |
| A3 / B3 | `2` / `表單 : 增加Functional safety 功能安全辨別欄位；為符合公司有ISO26262` |
| A4 / B4 | `3` / `表單 : 增加時間紀錄欄位；為符合ASPICE SWE6.BP4 13-50 工作產品特性` |
| A5 / B5 | `4` / `表單 : Priority與SWRA分法統一呈現，高High，中Medium，低Low，不適用NA` |
| A6 / B6 | `5` / `程序書 : Table3 測試案例設計方法修改為所更新方法 (黃標)` |
| A7 / B7 | `6` / `程序書 : 6.2.6.b~e，修改為更新後時間紀錄項描述 (黃標)` |
| A8 / B8 | `7` / `程序書 : 刪除i、J、l (黃標黑字刪除線)` |
| A9 / B9 | `8` / `程序書 : Table7 測試案例範本更新 (黃標)` |
| A10 / B10 | `9` / `SWUV、IT、QT表格內容排版相似，我們一起找其他流程owner討論，看是否跟進共用。以一個體系共同架構為目標。` |

⚠ **B5 述及 Priority 之取值為「高High，中Medium，低Low，不適用NA」** ——
而 037 之 `Priority` 欄實測值即為 `High` 等，二者一致。本包未實測母本
`P10:Q1411` DV 之**列舉值**（只實測其 sqref 範圍），故未能判定該 DV 是否
已依此建議更新。列為 §11 之該驗而未驗者。

---

## 3. 步驟 4 —— 母本結構登記（R-PMH7）

量測對象：`forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx`。
**未以 `openpyxl` 存回**（停止條件 9 未觸發）；DV 之實測直接讀
`xl/worksheets/sheet6.xml` 之原始 XML。

| # | 項 | 實測值 |
|---|---|---|
| 1 | **SHA256** | **`6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`** —— 與 R-PMH7 條文所載**逐字相同** |
| 2 | 檔案大小／mtime | 200,650 bytes ／ 2026-08-17T09:46:09 |
| 3 | **zip 成員數** | **48** |
| 4 | **分頁清單（9 個）** | `Cover_old`／`ChangeHistory_old`／`Cover 封面`／`ChangeHistory 修訂履歷`／`Product Document 記錄封面頁`／`Test Case Specification 測試用例規範`／`Reference`／`QS Suggestion`／`下拉選單` |
| 5 | r9 表頭 | **A–AH 共 34 欄**，34 格非空（A9 空）。全欄見 §4.1 |
| 6 | 合併儲存格 | `A1:AE1`／`B7:AA7`／`AB7:AH7`／`T8:Z8` |
| 7 | **DV（標準）** | `P10:Q1411`／`T10:Z1411`／`AF10:AF1411`（3 個 `<dataValidation>`） |
| 8 | **DV（x14 擴充）** | **有，1 個** —— `<xm:sqref>R10:R1411</xm:sqref>`，`<xm:f>下拉選單!$A$1:$A$9</xm:f>`；`<extLst>` 存在 |
| 9 | B 欄公式 | `=IF(ISBLANK($D10),"",ROW()-9)`（B10 起，逐列遞推） |
| 10 | **`last_capacity_row`** | **1411** —— B 欄公式止於 B1411（**B1412 為 `None`**），四組 DV 之 sqref 亦皆止於 1411，二證同值 |
| 11 | 凍結窗格 | **無**（`freeze_panes = None`） |
| 12 | 欄寬 | A 2.8／B 8.8／C 24.5／D 26.8／E 18.2／F 19.8／G 14.5／H 13.7／I 16.5／J 17.8／K 13.8／L 17.8／M 18.5／N 15.5／P 16.7／Q 16.2／R 19.2／S 14.3／T 12.3／U 10.5／V 19.8／W 15.7／X 14.3／Y 14.7／Z 11.8／AA 13.2／AB 9.7／AC 15.3／AD 15.3／AE 10.8／AF 14.5／AG 10.8／AH 11.8／AI 9.0 —— **`O` 無自訂欄寬**（採預設）；**`AI` 有欄寬 9.0 卻在 `max_col=AH` 之外**（殘留之欄格式，無表頭、無 DV） |
| 13 | **資料區非空** | **0** —— 掃 r10–r1411 × A–AH，扣除 B 欄公式後**零個非空儲存格**。此為 R-PMH8 `BLANK` 之直接佐證 |
| 14 | D3／D4／D5 | 皆 `None`（R-PMH10 之母本側佐證） |

**R-PMH7 之判準驗證**：條文載「交付副本之 r9 表頭欄數為 34（A–AH），
`Estimated Test Time (mins)` 恰出現一次」。實測：**欄數 34、
`Estimated Test Time` 出現 1 次（Q 欄）**。→ **通過**。

反向對照：客戶那份為 **35 欄（A–AI）、`Estimated Test Time` 出現 2 次
（P 與 R）**，依同一判準即判為「非本條所定之母本」。判準有鑑別力。

### 3.1 母本與客戶那份之結構差異（Q2 之定案佐證）

| 項 | 母本 20260817_ext | 客戶 20260819 |
|---|---|---|
| 分頁數 | **9** | **10**（多 `Test Case Framework`，且為空白） |
| 目標分頁名 | `Test Case Specification 測試用例規範` | 同 |
| r9 欄數 | **34（A–AH）** | **35（A–AI）** |
| `Estimated Test Time` | 1 次（Q） | 2 次（P、R） |
| 合併儲存格 | `A1:AE1`／`B7:AA7`／`AB7:AH7`／`T8:Z8` | `A1:AF1`／`B7:AB7`／`AC7:AI7`／`U8:AA8`／**`D5:F5`** |
| 資料列 | 0 | 48（r10–57） |
| x14 DV | 有（`R10:R1411`） | 有（`openpyxl` 讀取時丟出擴充警告） |

**`Test Case Framework` 分頁只存在於客戶那份**（分析層 §1 第 3 點所述屬實），
且其內容為空 —— 故 R-PMH7 將客戶那份之用途限於「三個附屬分頁之內容取得」
在本輪實際取得的是：**`Reference` 與 `QS Suggestion` 兩頁有內容，
`Test Case Framework` 為空**。

---

## 4. 步驟 5 —— 欄位對應重測與四方交叉佐證（R-PMH9）

### 4.1 母本 r9 表頭全欄（34 欄）

| 欄 | 表頭 | 欄 | 表頭 |
|---|---|---|---|
| A | *(空)* | R | `Test Case Design \nMethods\n測試用例設計方法` |
| B | `No.#\n序號` | S | `Functional Safety\n功能安全` |
| C | `Requirement or Design\nID (Polarion)\n設計/需求 ID (Polarion)` | T | `HDCC27\nAtl-Hi\n` |
| D | `Requirement or Design ID\n需求/設計 ID` | U | `DT27\nAtl-Hi\n` |
| E | `Test Case ID (TestRail)\n測試用例 ID (TestRail)` | V | `VF(ProMaster)637\nAtl-Mi` |
| F | `Test Case ID\n測試用例ID` | W | `Commander (598)\nAtl-Mi` |
| G | `Test Group\n測試組` | X | `Regengade (5210)\nAtl-Mi` |
| H | `Test Set\n測試集` | Y | `Toro(2261)\nAtl-Mi` |
| I | `Test Item\n測試項目` | Z | `Fastack (376)\nAtl-Mi` |
| J | `Pre-Conditions\n先前條件` | AA | `Test Case Author\n測試案例作者` |
| K | `Input Test Data\n輸入條件` | AB | `Test Version\n測試版號` |
| L | `Test procedure\n測試程序` | AC | `Test Vehicle\n(Bench)\n測試車型(Bench)` |
| M | `Expected Result\n預期結果` | AD | `Test Period\n測試期間` |
| N | `Specification Reference \n規格參考` | AE | `Tester\n測試者` |
| O | `Test Case Reference ID\n測項參考ID` | AF | `Test Result\n測試結果` |
| P | `Test Case Priority\n測試用例優先級別` | AG | `Defect ID\n缺陷ID` |
| Q | `Estimated Test Time (mins)\n預估測試時間\n（分鐘）` | AH | `Remarks\n備註` |

### 4.2 16 鍵重測結果：**16/16，零歧義**

比對方法同 01 包（換行前英文段、空白正規化、小寫、逐字相等）。

| 鍵 | 母本 | 01 包（作廢） | 差 |
|---|---|---|---|
| req_id | D | D | — |
| tc_id | F | F | — |
| test_group | G | G | — |
| test_set | H | H | — |
| test_item | I | I | — |
| pre_conditions | J | J | — |
| input_test_data | K | K | — |
| test_procedure | L | L | — |
| expected_result | M | M | — |
| spec_reference | N | N | — |
| tc_ref_id | O | O | — |
| **priority** | **P** | Q | **−1** |
| **design_method** | **R** | S | **−1** |
| **functional_safety** | **S** | T | **−1** |
| **author** | **AA** | AB | **−1** |
| **remarks** | **AH** | AI | **−1** |

01 包之五個錯位鍵已依 R-PMH9 作廢並更正。其成因非量測錯誤，
而是**量測對象錯誤**（35 欄之離群版面）。

### 4.3 四方交叉佐證（R-PMH9，G-H）

| 來源 | 欄數 | `Estimated Test Time` 次數 | r9 逐欄與母本相等 |
|---|---|---|---|
| **母本 20260817_ext** | 34 (AH) | 1 | —（基準） |
| User Profiles 20260820 | 34 (AH) | 1 | **✅ 34/34 逐欄相等** |
| Comfort 20260817 | 34 (AH) | 1 | **✅ 34/34 逐欄相等** |
| Time Management 20260822 | 34 (AH) | 1 | **✅ 34/34 逐欄相等** |

**四者全等，停止條件 7 未觸發。** 三份為唯讀來源，未寫入、未搬入 `inputs/`。

### 4.4 盲區聲明（R-G11）與排除向（R-G9）

**盲區**：本比對只認「換行前英文段逐字相等」。若某欄之英文段被改寫，
本法判為未命中而非誤配 —— **失效方向是漏，不是錯配**。16/16 全命中，
本輪無漏。此盲區之處置路徑：由 §4.3 之四方比對兜底 —— 若母本表頭被改，
三份已交付件會與之不等而觸發停止條件 7。

**排除向（證明不該轉紅者不轉紅）**：

| 近似欄 | 正規化值 | 是否被誤配 |
|---|---|---|
| `C` = `Requirement or Design\nID (Polarion)\n…` | `requirement or design` | 至 `req_id`：**否** |
| `E` = `Test Case ID (TestRail)\n…` | `test case id (testrail)` | 至 `tc_id`：**否** |
| 重複表頭 | **無**（母本之 `Estimated Test Time` 僅 Q 一欄） | — |

### 4.5 R-PMH10 之語料複驗（5/5 皆空）

| 來源 | D3 | D4 | D5 |
|---|---|---|---|
| 母本 20260817_ext | `None` | `None` | `None` |
| User Profiles 20260820 | `None` | `None` | `None` |
| Comfort 20260817 | `None` | `None` | `None` |
| Time Management 20260822 | `None` | `None` | `None` |
| Power Management 20260821 | `None` | `None` | `None` |

**5/5 無一填寫**，與 R-PMH10 之依據相符。

⚠ Power Management 20260821 之分頁名為 **`Test Case Specification&Result`**
（rev A/B 名），與其餘四者之 `Test Case Specification 測試用例規範` 不同；
其欄數同為 34。此差異不影響 R-PMH10 之結論（該三格皆空），惟顯示
**「分頁名」與「欄數版面」是兩個獨立變數**，未來以分頁名推斷版面會出錯。

**連帶：01 包 Q3 之提案作廢。** Q3 提案於 `D5` 填規格文件全名；
R-PMH10 裁定該三欄一律留空，且母本之 `D5` 本無 `D5:F5` 合併
（該合併只存在於客戶那份）。`feature.yaml` 已記
`preamble_cells_keep_blank: [D3, D4, D5]` 與 `write_back.keep_blank`。

---

## 5. 步驟 6 —— 更新後之 `feature.yaml`

全文見 `features/power_moding/feature.yaml`（YAML 可解析；`columns` 16 鍵、
`design_method_vocabulary` 9 項、`data_validation` 4 組）。

**母本工作副本已建立**：`cp -p` 至 `inputs/`，SHA256 實測
`6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`
—— 與 `forms/` 母本及 R-PMH7 條文三方相同。`inputs/MANIFEST.sha256`
已重建（5 個項目），`shasum -c` **全 OK**。

**宣告值與生效值分開記（G-C）**：

| 鍵 | 值 | 身分 |
|---|---|---|
| `feature` / `slug` | `Power Moding` / `power_moding` | **生效**（R-PMH2） |
| `test_group` | `Power Moding` | **宣告** —— workbook 實寫值待 Phase 3（R-PMH6），且**前例有矛盾**（A-PMH07） |
| `tc_id_pattern` | `TBD` | **待 Q7**；語料見 §8 |
| `paths.workbook` | 母本工作副本 | **生效**（R-PMH7） |
| `paths.customer_source_copy` | 客戶那份 | **生效** —— 新增鍵，用途限 R-PMH7 所列二項 |
| `spec_mode` | `A+B` | **生效**（02 §1.2 核可） |
| `spec_reference_template` | `Power Moding HMI Logic and Flow R1 SR24 2A_{outline}` | **生效** —— 三方同構已驗 |
| `workbook.columns`（16 鍵） | §4.2 | **生效** —— 母本重測 ＋ 四方佐證 |
| `workbook.last_capacity_row` | `1411` | **生效** —— 二證同值（§3 第 10 項） |
| `workbook.data_validation` | 4 組（含 x14） | **生效** —— 讀原始 XML 所得 |
| `workbook.b_column_formula` / `freeze_panes` / `merged_cells` | §3 | **生效** |
| `workbook_state` | `BLANK` | **生效**（R-PMH8） |
| `done_region.author_value` / `invariant` | `null` / `null` | **生效**（R-PMH8 —— 不適用） |
| `write_back.first_row` / `mode` | `10` / `append` | **生效**（R-PMH8） |
| `write_back.author_value` | `PeiPYHsu` | **生效** —— Comfort 交付件 AA 欄實測值 |
| `write_back.fill_test_group_set` | `true` | **生效** —— BLANK 之 canon §2 綁定；**實值**待 Phase 3 |
| `lint.design_method_vocabulary` | 9 項 | **生效** —— §6 實測 |

---

## 6. 步驟 7 —— `下拉選單` vocabulary 全集與差異

| # | 母本 20260817_ext `A{n}` | 客戶 20260819 `A{n}` |
|---|---|---|
| 1 | `功能測試 (Functional based ; no specific technique)` | 同 |
| 2 | `狀態轉換 (State Transition Testing)` | 同 |
| 3 | `決策表 (Decision Table Testing)` | 同 |
| 4 | `等價劃分 (Equivalence Partitioning, EP)` | 同 |
| 5 | `邊界值分析 (Boundary Value Analysis, BVA)` | 同 |
| 6 | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` | 同 |
| 7 | `情境 / 用例 (Scenario / Use Case Testing)` | 同 |
| 8 | `負向測試 (Negative / Invalid)` | 同 |
| 9 | `基礎故障注入 (Fault Injection Lite)` | 同 |

兩者 `dims` 皆為 `A1:A11`，非空 9 格，**A1:A9 逐項相等（`==` 為 True）**。
A10／A11 為空 —— 即 `dims` 之上界大於實際內容，DV 之 source 明載
`$A$1:$A$9`，故 vocabulary 全集**恰為 9 項**，無外溢。

`lint.design_method_source` 由 01 包之「沿用預設」改為 **實測**，
並將 9 項全集寫入 `feature.yaml` 之 `design_method_vocabulary`
（01 包 §9 第 3 項清償）。

**差異（跨分頁，非跨檔）**：`Reference!C9` 為
`組合測試 (Combinatorial Testing ; Pair-wise / N-wise)`，而
`下拉選單!A6` 為 `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` ——
**`Pair-wise / N-wise` vs `Pairwise / t-wise`**。二者在母本與客戶那份
**皆各自如此**，即此不一致源自表單本身而非任一交付件。
**lint 之權威取 `下拉選單`**（它才是 x14 DV 之 source 範圍，
是 Excel 實際會驗的那一份）；`Reference` 為說明性頁面。

---

## 7. 步驟 8 —— PDF 圖像抽取能力實測（§9.1 通則 6，A-PMH04）

工具：`pdftoppm`（poppler 25.05.0），PNG 輸出。
**只驗能力，未抽內容、未寫任何 TC 依據。**

### 7.1 outline → PDF 頁次（6 則圖片佔位）

以 SYS1 之章 `Description` 與 PDF 頁首**逐字相等**建立：

| outline | 章 | 章標題（= PDF 頁首） | PDF 頁 |
|---|---|---|---|
| 2.1 | 2 | `Headunit Startup – Non-GDPR/NonMaserati` | **p3** |
| 3.1 | 3 | `Headunit Startup – GDPR/Non-Maserati` | **p4** |
| 4.1 | 4 | `Headunit Startup – Maserati/Non-GDPR` | **p5** |
| 5.1 | 5 | `Headunit Startup – GDPR/Maserati` | **p6** |
| 6.1 | 6 | `Passenger Screen Startup` | **p7** |
| 12.4 | 12 | `Power Moding – Off Road+` | **p11** |

六者之章標題與 PDF 頁首**逐字相等**，無歧義。

### 7.2 render 規格與判定

| DPI | 像素尺寸 | 檔案大小（p3） | 判定 |
|---|---|---|---|
| 150 | 1650 × 1275 | 341 KB | 向量流程圖**完全可辨讀** |
| 300 | 3300 × 2550 | 838 KB | 上述再加內嵌 UI 截圖之內文可辨讀 |

**逐項判定**：

| 項 | 150 DPI | 300 DPI |
|---|---|---|
| 節點方塊標籤（`Black Screen (open the door)`、`Splash`、`System Loading`、`Last Mode Screen`…） | **可辨讀** | 可辨讀 |
| 轉移標籤（`Ignition ON ≤ 3 sec.`、`1.5 sec timeout`、`5 secs`、`Ign. OFF > 3 sec.`） | **可辨讀** | 可辨讀 |
| 向量線條與箭頭方向 | **可分辨**（含跨頁長箭頭之起訖） | 可分辨 |
| 分支條件文字（`IF Radio OFF + Power ON button`、`ON OR Recall Last and Last = ON`） | **可辨讀** | 可辨讀 |
| **內嵌 UI 截圖之內文**（Uconnect disclaimer 之免責條款全文、`Loading…`、`Drive Modes / Custom / Track / Sport`） | **勉強／不可靠** —— `IMPORTANT` 可辨，正文各行僅能看出行數 | **可辨讀**（逐字） |

**結論**：**可 render 且可辨讀，A-PMH04 之「不判 export 不可讀」成立。**
建議 Phase 4 之 render 規格為 **150 DPI 供流程判讀、300 DPI 供內嵌截圖判讀**；
若只取一種，取 300 DPI。

**§9.1 通則 6 之跨形式試驗至此完備**：xlsx（SYS1 匯出）、PDF 文字層、
PDF 圖像三種形式皆已實測抽取能力，無一以「沒去抽那一份」充當「抽不出來」。

**render 產物**落於 `sandbox/render/`（12 個 PNG），**不入版控**
（`sandbox/` 已加入 `.gitignore`）。Phase 4 之正式產物將另置於 `data/`。

---

## 8. 步驟 9 —— `{abbr}` 對應關係表（**不含提案**）

四份已交付件之 `F` 欄（Test Case ID）與 `G` 欄（Test Group）實測：

| feature | 交付夾名 | 檔名之 tag | **`F` 欄形態** | `F` 欄非空列數 | **`G` 欄實際值** |
|---|---|---|---|---|---|
| User Profiles | `User Profiles` | `UserProfiles` | `NR1L-UserProfiles-{NNN}` | 189 | `User Profiles` |
| Comfort | `Climate Control Interface` | `Comfort` | **`NR1L-ComfortHMI-{NNN}`** | 465 | **`Climate Control Interface`** |
| Time Management | `Time Management` | *(無 tag)* | `NR1L-TimeManagement-{NNN}` | 59 | `Time Management` |
| Power Management | `Power Management` | `PowerManagement` | `NR1L-PowerManagement-{NNN}` | 283 | `Power Management` |

各件之 `F` 欄形態皆**單一**（無混用）；`G` 欄相異值皆**只有一個**。

**三者關係之逐項觀察（描述，非提案）**：

1. **前綴 `NR1L-` 四份一致。**
2. **`{abbr}` 為無空白之 PascalCase**，四份一致。
3. **`{abbr}` 與 `G` 欄之關係**：三份相等（去空白後）；**Comfort 不相等**
   —— `{abbr}` = `ComfortHMI`，`G` = `Climate Control Interface`。
4. **`{abbr}` 與交付夾名之關係**：三份相等（去空白後）；**Comfort 不相等**。
5. **`{abbr}` 與檔名 tag 之關係**：三份相等；**Comfort 不相等**
   （tag `Comfort`，abbr `ComfortHMI` —— 多一個 `HMI` 後綴）。
6. **Comfort 之 `{abbr}` 唯一相符者為「規格標題模組名 ＋ `HMI`」**：
   spec 標題為 `Comfort HMI Logic and Flow`。
7. 本 feature 之對照量：交付夾名 `Disclaimer screen`；
   檔名 tag **`PowerModingHMI`**；規格標題模組名 `Power Moding`；
   規格標題 `Power Moding HMI Logic and Flow R1 SR24 2A`。
   **本 feature 之檔名 tag 已自帶 `HMI` 後綴**，與 Comfort 之檔名 tag
   （`Comfort`，無 `HMI`）形態不同。

**執行層不提案、不採用**（下放包步驟 9 明載）。惟須指出：分析層於 Q7 所擬之
`NR1L-PowerModing-{NNN}`，與依 Comfort 前例類推之 `NR1L-PowerModingHMI-{NNN}`
**皆與語料相容**，語料本身不足以在二者間判別。

---

## 9. 步驟 10 —— `data/outline_map.json`

### 9.1 29/29 之重現（先算後比）

| 項 | 01 包 §5.2（對照向） | 本輪重算 | 結果 |
|---|---|---|---|
| 037 之 leaf 數 | 48 | **48** | 相符 |
| leaf 引用之相異章節數 | 29 | **29** | 相符 |
| 於 SYS1 `Outline Number` 之命中 | 29/29 | **29/29** | 相符 |
| SYS1 outline 總數 | 52 | **52** | 相符 |
| 未解 outline | — | **0** | — |
| 未解 pdf_page | — | **0** | — |

### 9.2 定位方法與其兩次失敗（fail-loud，見 A-PMH08）

| # | 方法 | 結果 | 否決理由 |
|---|---|---|---|
| 1 | 章 `Description` **逐字等於** PDF 頁首 | 21/48 leaf **未解** | SYS1 有 12 章而 PDF 只有 11 頁首；ch 8／10／11 是**頁內小標** |
| 2 | 章 `Description` **子字串包含**於頁文字 | 48/48 全解，**但有錯** | 短通用詞誤命中：ch7 `Startup` → p3（實為 p8）、ch9 `Power Moding` → p1（實為 p9）。**assert 通過而資料錯誤** |
| 3 | **採用** —— 該節自身 `Description` 首 N 字**唯一命中**，N 依 `80→60→40` 遞減 | **48/48 全解，0 未解** | — |

方法 3 需要階梯之原因：`pdftotext -layout` 在多欄頁會於句中插入斷點 ——
outline `9.1` 之 80 字探針命中 0 頁、60 字探針唯一命中 p9。固定長度會誤判為未解。

**探針長度分布**：80 字 39 筆／60 字 7 筆／40 字 2 筆。
**命中 >1 頁即判未解，不取首個**（不以「多數命中」通過，R-G7-1）。

**盲區聲明（R-G11）**：40 字探針理論上可能在別頁偶然唯一命中。
使用 40 字者之 2 筆已逐筆記於 JSON 之 `probe_len` 欄，可人工複核。

### 9.3 章 ↔ 頁對照（由 48 leaf 反推，自洽）

| 章 | PDF 頁 | 頁首 |
|---|---|---|
| 7 | p8 | `Startup` |
| 8 | p8 | `Startup`（`Starup R1Low Only` 為頁內小標） |
| 9 | p9 | `Power Moding` |
| 10 | p10 | `Power Moding`（`Additional Power Moding Behavior Notes:` 為頁內小標） |
| 11 | p10 | `Power Moding`（`VR HARD KEY FOR SIRI/…` 為頁內小標） |
| 12 | p11 | `Power Moding – Off Road+` |

**leaf 之 PDF 頁分布**：p8 = 25、p9 = 5、p10 = 15、p11 = 3（合計 48）。

**與 A-PMH04 之互相印證**：48 leaf **無一落在 p3–p7 之流程圖頁**。
此結果由「內文唯一命中」路徑得出，與 A-PMH04 由「037 之 29 章節不含
2.1–6.1」路徑得出者一致 —— **兩條獨立路徑同結論**。

### 9.4 JSON 之欄位

每 leaf 記：`swe_req_id`／`row_037`／`row_036_customer`／`hmi_source_id`／
`outline`／`polarion_id`／`outline_in_sys1`／`pdf_page`／`pdf_page_heading`／
`page_resolution_method`／`probe_len`。另有 `method`（含 `rejected_methods`
與 `blind_spot`）、`sources`（三份素材之 SHA256）、`counts`、`page_headings`。

**`data/outline_map.json` 入版控** —— 理由同 `.gitignore` 對
`data/spec_id_to_outline.tsv` 所述：它是唯一之追溯表，且其 `sources` 欄
記著三份素材之 SHA256，素材一換 diff 就會顯示出來。

---

## 10. `A-PMH{n}` 更新

| 條號 | 主旨 | 狀態 | 複核時點 |
|---|---|---|---|
| A-PMH01 | 037 `FROP` 相異值 13 vs 12 | **RESOLVED**（02 §1.1 採認，R-PMH6 勘誤附註已落實且原文 SHA256 未變） | — |
| A-PMH02 | scaffold marker 前綴 `A-PO` | RESOLVED（01 包） | — |
| A-PMH03 | SYS1 匯出相對 PDF 之內文偏離 | **PENDING** | **Phase 4** —— 對 `outline == 7.1` 之 5 leaf（`pdf_page` 皆為 p8）逐一以 PDF 原文複核語句順序 |
| A-PMH04 | 6 則 outline 為圖片佔位 | **PENDING** | **Phase 4** —— 實際 render 並取用 p3–p7／p11 時。本輪已完成其前置（圖像抽取能力實測，§7），且已確定**不阻斷任何 leaf**（§9.3） |
| A-PMH05 | 雜湊檔未入版控 | **RESOLVED**（R-PMH11，已實施並雙向實測） | — |
| **A-PMH06** | **R-PMH11 所指定之 `.gitignore` 寫法無效** | **PENDING**（須追認執行層之等效改寫） | 見 §11 |
| **A-PMH07** | **R-PMH2 所引之 Comfort R-C6 前例，於交付件上未實現** | **PENDING** | **Phase 3 之前** |
| A-PMH08 | outline→PDF 頁次之兩種先驗方法皆失敗 | RESOLVED（方法已更換並驗證） | — |

### 10.1 A-PMH06 —— R-PMH11 之實施方式不可行（須追認）

R-PMH11 逐字指定「於 `inputs/` 排除規則後增列否定規則
`!inputs/MANIFEST.sha256`」。照此實施後**實測仍被忽略**：

```
$ git check-ignore -v features/power_moding/inputs/MANIFEST.sha256
features/power_moding/.gitignore:2:inputs/	features/power_moding/inputs/MANIFEST.sha256
```

**成因**：git 之既有行為 —— 目錄一旦被排除，git 不再遞迴進入該目錄，
其內之否定規則不會被求值。`inputs/` 排除的是「目錄」，
`inputs/*` 排除的才是「目錄內容」。**R-PMH11 之目的可達成，其所述之方法不可行。**

**執行層之處置**：改寫為 `inputs/*` ＋ `!inputs/MANIFEST.sha256`，雙向實測：

| 向 | 對象 | 結果 |
|---|---|---|
| 正向 | `inputs/MANIFEST.sha256` | 命中 `.gitignore:7:!inputs/MANIFEST.sha256` → **不再被忽略** |
| 反向 | 四份素材（3 xlsx ＋ 1 pdf） | 全數命中 `.gitignore:6:inputs/*` → **仍被忽略** |
| 反向 | `features/power/inputs` | 命中其自身 `.gitignore:2:inputs/` → **未受影響** |
| 實效 | `git add --dry-run -- inputs/`（唯讀） | 僅輸出 `add 'features/power_moding/inputs/MANIFEST.sha256'` 一筆 |

**未改條文**，僅以等效寫法達成其**明載之目的**。提案：R-PMH11 以勘誤附註
承接（比照 R-PMH6／R-P36），原文不改字。**請追認。**

**canon 層之連帶**：`scripts/new_feature.py` 之 `GITIGNORE` 對每個 feature
都寫 `inputs/`；任何 feature 依 R-PMH11 之字面實施都會得到同樣之無效結果。

### 10.2 A-PMH07 —— R-PMH2 之前例在交付件上不成立（Phase 3 前須裁）

R-PMH2 之依據逐字為「Comfort R-C6 之同型處置（交付夾
`Climate Control Interface`，`test_group` 為 `Comfort`）」。
R-C6 原文（`features/comfort/RULINGS.md:128`）逐字為
「`workbook Test Group 欄一律填 "Comfort"。`」，並明言
「"Climate Control Interface" 為資料夾分類…不作為 Test Group 來源」。

**實測（唯讀）**：Comfort 之已交付件 `…_SWQT_Comfort_20260817.xlsx`，
`G` 欄 r10 起 **466 列，相異值只有一個：`Climate Control Interface`**。

即：**已交付之工作簿，其 Test Group 欄填的是交付夾名，不是 R-C6 裁定之
`Comfort`。** 執行層不判定成因（可能為條文未落實，亦可能為
「宣告值／寫回值本即分離」而 R-C6 之措辭與該分離不一致）。

**對本 feature 之影響**：若依 Comfort **交付件**之實況類推，
本 feature 之 G 欄應填 `Disclaimer screen` —— **與 R-PMH2 相反**。
R-PMH6 已將 G/H 延後至 Phase 3，故**不阻斷本輪**；
但**須在 Phase 3 開始前裁定**，否則 Layer 1 之定版會建立在未經核對之前例上。

---

## 11. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，六項。**

1. **母本 `P10:Q1411` DV 之列舉值未實測。** 本包只讀了三組標準 DV 之
   `sqref` 範圍，未讀其 `<formula1>` 之列舉內容。`QS Suggestion!B5` 明載
   建議 Priority 改為「高High，中Medium，低Low，不適用NA」，而
   `user_profiles/feature.yaml` 所記之前例為 `["P0","P1","P2","P3"]` ——
   **二者不同，且本包未判定母本現況為何者**。037 之 `Priority` 欄實測值
   為 `High` 形態。Phase 4 寫回 P 欄前必須先測，否則會寫出逸出 DV 之值。
   **本項為六項中最可能造成實際寫回失敗者。**

2. **`T10:Z1411`（七個車型欄）與 `AF10:AF1411`（Test Result）之列舉值同樣未讀。**
   本 feature 之車型欄依前例留白（Power Management R-P54 之同型處置），
   但「留白」是否合法仍取決於該 DV 是否允許空值 —— 未驗。

3. **母本之 `Cover 封面` / `ChangeHistory 修訂履歷` / `Product Document
   記錄封面頁` 三頁未讀。** 01 包 §9 第 4 項所記之「封面三個署名欄未複驗」
   在本包**仍未清償** —— 本包讀的是客戶那份之附屬三頁（步驟 3 所指定者），
   與封面頁不同。R-PMH10 只管 `D3/D4/D5`，未及封面。

4. **`data/outline_map.json` 之 `row_036_customer` 欄語意已隨 R-PMH7 改變。**
   該欄記的是 leaf 在**客戶那份**之列號（10–57）。母本為 BLANK，
   寫回時之目標列號將由 append 順序決定，與此欄無關。欄名雖已標明
   `_customer`，但仍有被誤用為寫回目標之風險。未加防呆。

5. **步驟 8 之可辨讀性判定為人工目視，未有機器可檢查之判準**（§9.1 通則 8）。
   「300 DPI 可辨讀」目前是一句人工結論。若日後要以此解除 A-PMH04，
   需要一個實跑之判準（例如對 render 圖跑 OCR 並比對已知字串命中率）。
   本包未做 —— 下放包步驟 8 明載「只驗能力」，但通則 8 對 **RESOLVED**
   之要求高於此。故 A-PMH04 維持 PENDING 是正確的。

6. **`Reference!C9` 與 `下拉選單!A6` 之字串不一致（`Pair-wise / N-wise`
   vs `Pairwise / t-wise`）未上報為異常。** 本包判其為表單自身之瑕疵、
   且 lint 權威明確取 `下拉選單`，故只記於 §6 未立 `A-PMH`。
   若分析層認為應立條登記，請指示 —— 執行層之判斷可能過輕。

---

## 12. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 —— 48/48 leaf 之 outline 與 pdf_page 全解 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 —— R-PMH8 已裁為 `BLANK`，母本資料區非空格 0，無歧義 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發（A-PMH06／A-PMH07 皆有既有條文可承接，屬追認與前例校正，非規則缺口） |
| 5 | 造值壓力 | 未觸發 —— 未實測者留 `TBD`；Q7 只報語料不提案 |
| 6 | done region 與規格矛盾 | 未觸發 —— 母本無 done region |
| 7 | 母本與三份已交付件之 r9 表頭有任一欄不相等 | **未觸發** —— 四方 34/34 逐欄相等 |
| 8 | `Test Case Framework` 與 037 `FROP` 或規格目次直接矛盾 | **未觸發** —— 該分頁**完全空白**（0 非空儲存格），無從矛盾 |
| 9 | 需以 `openpyxl` 對母本或工作副本 `save()` | **未觸發** —— 全程唯讀；DV 之實測改讀 `sheet6.xml` 原始 XML |

---

## 13. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 02 — baseline switch to forms master, BLANK state, outline map
```

```
git add -- features/power_moding/.gitignore \
           features/power_moding/ANOMALIES.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/data/outline_map.json \
           features/power_moding/inputs/MANIFEST.sha256 \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/02_baseline_switch.md \
           features/power_moding/docs/upstream/02_baseline_switch.md

git commit -- features/power_moding/.gitignore \
              features/power_moding/ANOMALIES.md \
              features/power_moding/RULINGS.md \
              features/power_moding/feature.yaml \
              features/power_moding/data/outline_map.json \
              features/power_moding/inputs/MANIFEST.sha256 \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/02_baseline_switch.md \
              features/power_moding/docs/upstream/02_baseline_switch.md
```

- **`inputs/MANIFEST.sha256` 首次入版控**（R-PMH11／A-PMH06）。
  素材五份（含新增之母本工作副本）仍不入版控。
- `sandbox/`（`spec.txt` ＋ 12 個 render PNG）已加入 `.gitignore`，不入版控。
- pathspec 逐項寫全名，未用 `features/power*` 形態之萬用字元（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 13.1 git 動作揭露（R-G6，唯讀與改狀態分列）

| 類別 | 本輪執行者 | 次數 |
|---|---|---|
| **唯讀 git** | `git check-ignore -v`（R-PMH11 所明許） | 5 |
| **唯讀 git** | `git add --dry-run`（不改 index，用於 A-PMH06 之實效驗證） | 1 |
| **改狀態 git** | **無** | 0 |

未執行 `git status` / `git log` / `git diff` / `git add`（實作）/ `git commit`。

---

## 14. 本輪之全部工作區動作（供 §13 之一致性核對）

| # | 動作 | 對象 |
|---|---|---|
| 1 | heredoc 追加 | `RULINGS.md` —— 02 包六條 ＋ 核對表 |
| 2 | 就地改寫 | `RULINGS.md` —— 核對表之 placeholder 換為實測 SHA256 |
| 3 | 就地改寫 ×2 | `.gitignore` —— 先依 R-PMH11 字面（無效），再改為 `inputs/*` ＋ 否定規則；另加 `sandbox/` 與 `data/outline_map.json` 之說明 |
| 4 | `cp -p` | 母本 → `inputs/`（工作副本） |
| 5 | `shasum -a 256 *.xlsx *.pdf > MANIFEST.sha256` | `inputs/MANIFEST.sha256` 重建（5 項；**排除自身**） |
| 6 | heredoc 寫檔 ＋ `sed` 修正 | `feature.yaml` 全面改寫 |
| 7 | `pdftoppm` ×4 | `sandbox/render/` 之 12 個 PNG（150／300 DPI × p3–p7、p11） |
| 8 | Python 寫檔 | `data/outline_map.json`（三次嘗試，前兩次因 fail-loud 未寫或被覆寫） |
| 9 | heredoc 寫檔 | `ANOMALIES.md` —— A-PMH01/05 改 RESOLVED，新增 A-PMH06/07/08，A-PMH03/04 補複核時點 |
| 10 | heredoc 寫檔 | `docs/upstream/02_baseline_switch.md`（本檔） |
| 11 | heredoc 寫檔 | `docs/INDEX.md` 補本輪次列 |

**對任何工作簿之儲存格寫入：無。**
**對唯讀來源（`forms/`、四個 ASW-R2 交付夾）之寫入：無。**
`forms/` 母本於複製後未再變動（工作副本與其 SHA256 相同即為證）。
