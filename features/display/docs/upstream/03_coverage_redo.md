# 上繳包 03 —— 覆蓋對照重做，02 之三處報告缺陷更正

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/03_coverage_redo.md`
- 結果：**步驟 1–10 全數執行；下放包 01 §五九條 + 03 §七第 10 條，
  十條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §9 只備妥訊息與 pathspec，未執行

---

## 0. 覆核之採認

分析層對 §9 之退回**成立，且我接受其對我 §11 第 3 項之評語**。

我當時寫的是「此數字可用於揭露落差之量級，不可用於任何涵蓋率之主張」——
這句話預設了「量級是對的，只是精度不足」。實際上該啟發式把 r31–r34
指向錯誤的 leaf，於是 004／005 顯示 0；**方向錯了，不是精度不足**。
自陳為啟發式並不等於察覺其會產生相反的結論，這兩件事我當時混為一談。

R-DM12 之判準（「欄名會活得比正文久」）對應到我的具體錯誤：我在
`coverage_map.py` 的 docstring、TSV 欄名、`ANOMALIES.md` 表頭三處分別
寫了「搜尋輔助」「對應 SWE-DM」「依據」—— 免責寫在最不會被引用的地方，
結論語氣寫在最會被引用的地方。

---

## 1. §五四條之抄錄核對表（步驟 1）

抄錄方式同前輪：以 `re` 自下放包 03 之 fenced 區塊機器抽取後原樣寫入
`RULINGS.md`，未經人工轉錄；抄畢反向抽取並與原檔逐字元 `==` 比對。

| # | 條號 | 來源包 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 14 | R-DM12 | 03 | 235 | `78599eabe092b8a1` | 是 |
| 15 | R-DM13 | 03 | 355 | `2b5a77ed7b7a1a52` | 是 |
| 16 | R-DM14 | 03 | 269 | `ea998f51f74c9a41` | 是 |
| 17 | R-DM15 | 03 | 171 | `135cf28886d1a0a5` | 是 |

**累計 17/17 逐字元相符**（01 包 8 條、02 包 5 條、03 包 4 條）。
下放包 03 之另三個 fenced 區塊（B 欄公式、兩組輸出欄位規格）為規格而非
條文，未計入。

R-DM7 依 R-TM13 原文保留於 `RULINGS.md`，未刪除、未改寫；R-DM13 對其
「Description 文字」一項之廢止以核對表下方之註記載明。

---

## 2. `probe_036.py` 兩基準並列之輸出（步驟 2）

依 §2.1 更正：`declared` 欄之來源必須具名。`template-declared` 取自
`docs/fw036/templates/feature.yaml`（scaffold 寫入新 feature 之內容），
`effective-declared` 取自 `features/display/feature.yaml`（本 feature 已
更正之對應）。腳本為 `features/display/scripts/` 下之自有腳本，不受
§五第 9 條拘束。

```
matching method: the expected label, whitespace-normalised and lower-cased, as a substring of the whitespace-normalised header cell at the declared column
template-declared source: /Users/peihe/Work_Projects/TC_Generator/docs/fw036/templates/feature.yaml
effective-declared source: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml

## column mapping — template-declared vs header-derived
| key | declared | header text at declared col | expected label | verdict |
|---|---|---|---|---|
| req_id | D | Requirement or Design ID 需求/設計 ID | requirement or design id | MATCH |
| test_group | G | Test Group 測試組 | test group | MATCH |
| test_set | H | Test Set 測試集 | test set | MATCH |
| test_item | I | Test Item 測試項目 | test item | MATCH |
| pre_conditions | J | Pre-Conditions 先前條件 | pre-condition | MATCH |
| input_test_data | K | Input Test Data 輸入條件 | input | MATCH |
| test_procedure | L | Test procedure 測試程序 | procedure | MATCH |
| expected_result | M | Expected Result 預期結果 | expected result | MATCH |
| spec_reference | N | Specification Reference 規格參考 | spec | MATCH |
| tc_ref_id | O | Test Case Reference ID 測項參考ID | test case reference id | MATCH |
| priority | P | Test Case Priority 測試用例優先級別 | test case priority | MATCH |
| design_method | Q | Estimated Test Time (mins) 預估測試時間 （分鐘） | design methods | MISMATCH |
| functional_safety | R | Test Case Design Methods 測試用例設計方法 | functional safety | MISMATCH |
| author | Z | Fastack (376) Atl-Mi | test case author | MISMATCH |
| remarks | AH | Remarks 備註 | remark | MATCH |

match count (template-declared): 12/15
  MISMATCH design_method @ Q: header='Estimated Test Time (mins) 預估測試時間 （分鐘）'; columns whose header contains 'design methods': ['R']
  MISMATCH functional_safety @ R: header='Test Case Design Methods 測試用例設計方法'; columns whose header contains 'functional safety': ['S']
  MISMATCH author @ Z: header='Fastack (376) Atl-Mi'; columns whose header contains 'test case author': ['AA']

## column mapping — effective-declared vs header-derived
| key | declared | header text at declared col | expected label | verdict |
|---|---|---|---|---|
| req_id | D | Requirement or Design ID 需求/設計 ID | requirement or design id | MATCH |
| test_group | G | Test Group 測試組 | test group | MATCH |
| test_set | H | Test Set 測試集 | test set | MATCH |
| test_item | I | Test Item 測試項目 | test item | MATCH |
| pre_conditions | J | Pre-Conditions 先前條件 | pre-condition | MATCH |
| input_test_data | K | Input Test Data 輸入條件 | input | MATCH |
| test_procedure | L | Test procedure 測試程序 | procedure | MATCH |
| expected_result | M | Expected Result 預期結果 | expected result | MATCH |
| spec_reference | N | Specification Reference 規格參考 | spec | MATCH |
| tc_ref_id | O | Test Case Reference ID 測項參考ID | test case reference id | MATCH |
| priority | P | Test Case Priority 測試用例優先級別 | test case priority | MATCH |
| design_method | R | Test Case Design Methods 測試用例設計方法 | design methods | MATCH |
| functional_safety | S | Functional Safety 功能安全 | functional safety | MATCH |
| author | AA | Test Case Author 測試案例作者 | test case author | MATCH |
| remarks | AH | Remarks 備註 | remark | MATCH |

match count (effective-declared): 15/15

## 兩基準之並列結論
  template-declared : 12/15 — 不符 3 鍵 ['design_method', 'functional_safety', 'author']
  effective-declared: 15/15 — 不符 0 鍵 無
  template 之分頁名 'Test Case Specification&Result' 於本母本 不存在
  -> effective 之全綠是「更正已生效」之複驗，不得讀為「模板無誤」。模板之不符即 A-DM7 之內容。

## header-derived column map (candidates per key)
| key | expected label | candidate columns | template | effective |
|---|---|---|---|---|
| req_id | requirement or design id | C,D | D | D |
| test_group | test group | G | G | G |
| test_set | test set | H | H | H |
| test_item | test item | I | I | I |
| pre_conditions | pre-condition | J | J | J |
| input_test_data | input | K | K | K |
| test_procedure | procedure | L | L | L |
| expected_result | expected result | M | M | M |
| spec_reference | spec | N | N | N |
| tc_ref_id | test case reference id | O | O | O |
| priority | test case priority | P | P | P |
| design_method | design methods | R | Q | R |
| functional_safety | functional safety | S | R | S |
| author | test case author | AA | Z | AA |
| remarks | remark | AH | AH | AH |

```

**兩基準之結論並列**：`template-declared` **12/15**（不符
`design_method`／`functional_safety`／`author`，且其分頁名
`Test Case Specification&Result` 於本母本不存在）；`effective-declared`
**15/15**。

上繳包 02 §6.4 之機器輸出印的是 `15/15`（那次的 `declared` 已是更正後之
`feature.yaml`），而正文寫 12/15 —— 兩者皆為真但基準不同，且輸出未具名，
讀者見 15/15 會得出「模板無誤」之相反結論。**已更正：兩基準一律並列，
各自具名，並在輸出末尾明寫「effective 之全綠是更正已生效之複驗，
不得讀為模板無誤」。**

---

## 3. 036 母本表頭之 `repr` 全欄（步驟 3）

```
## header row content — repr() of the RAW cell value
   (newlines are the master's own; nothing is normalised here)
  B: 'No.#\n序號'
  C: 'Requirement or Design\nID (Polarion)\n設計/需求 ID (Polarion)'
  D: 'Requirement or Design ID\n需求/設計 ID'
  E: 'Test Case ID (TestRail)\n測試用例 ID (TestRail)'
  F: 'Test Case ID\n測試用例ID'
  G: 'Test Group\n測試組'
  H: 'Test Set\n測試集'
  I: 'Test Item\n測試項目'
  J: 'Pre-Conditions\n先前條件'
  K: 'Input Test Data\n輸入條件'
  L: 'Test procedure\n測試程序'
  M: 'Expected Result\n預期結果'
  N: 'Specification Reference \n規格參考'
  O: 'Test Case Reference ID\n測項參考ID'
  P: 'Test Case Priority\n測試用例優先級別'
  Q: 'Estimated Test Time (mins)\n預估測試時間\n（分鐘）'
  R: 'Test Case Design \nMethods\n測試用例設計方法'
  S: 'Functional Safety\n功能安全'
  T: 'HDCC27\nAtl-Hi\n'
  U: 'DT27\nAtl-Hi\n'
  V: 'VF(ProMaster)637\nAtl-Mi'
  W: 'Commander (598)\nAtl-Mi'
  X: 'Regengade (5210)\nAtl-Mi'
  Y: 'Toro(2261)\nAtl-Mi'
  Z: 'Fastack (376)\nAtl-Mi'
  AA: 'Test Case Author\n測試案例作者'
  AB: 'Test Version\n測試版號'
  AC: 'Test Vehicle\n(Bench)\n測試車型(Bench)'
  AD: 'Test Period\n測試期間'
  AE: 'Tester\n測試者'
  AF: 'Test Result\n測試結果'
  AG: 'Defect ID\n缺陷ID'
  AH: 'Remarks\n備註'

```

分隔符為**換行**，33 欄皆然。上繳包 02 §6.4 標 `(raw)` 卻印正規化值，
確為誤植；該節恰是登記 A-DM5（037 表頭不規則空白）之處，印出乾淨的
036 表頭等於暗示「036 沒這個問題」。

一併記兩處前輪未報之細節：`'HDCC27\nAtl-Hi\n'`、`'DT27\nAtl-Hi\n'`
帶**尾隨換行**；`'Specification Reference \n規格參考'` 為**尾空格 + 換行**。

`ANOMALIES.md` 之 A-DM5 已補述其適用範圍及於 036 母本，並記三份素材
（037／SYS2／036）之表頭皆不可逐字取欄，此為本 feature 之通則。

---

## 4. 新 `coverage_sys2_vs_swe_dm.tsv`（步驟 5）

舊檔依 R-TM13 改名 `data/coverage_sys2_vs_swe_dm.RETRACTED.tsv`，
檔頭加註一行廢止理由，**未刪除**。

欄位（依 §3.3 之規格，另於其後追加三欄 —— 見本節末）：

```
sys2_row | sys_ra_id | category | swhw | heading_ancestor | signals |
values | melco | anchor_kind | candidate_leaf | note |
func_l1 | func_l2 | func_l3
```

```
## anchor_kind 分布（最高優先之現存錨）
  signal: 43
  heading: 36
  value: 1

## 各錨之存在數（非互斥，逐列獨立計）
  含 $signal$        : 43
  含 [value]         : 34
  有 heading 祖先    : 80
  Melco 命中 Excluded: 1
  相異訊號名 15: ['Back_Button', 'CCDMF_RQ_DISP_INTS', 'CM_TCH_STAT', 'DCSD_DISP_STAT', 'Enter_Button', 'ICSMuteButton', 'ICSPowerButton', 'ICSScreenOffButton', 'ICS_KNOB1_DIR', 'ICS_KNOB1_VAL', 'ICS_KNOB2_DIR', 'ICS_KNOB2_VAL', 'RQ_DISP_INTS', 'TGW_DISP_STAT', 'Telematic_Power']
  相異值 token 13: ['0% Intensity', 'DCSD_and_HU_LVDS_Backchannel_Protocol', 'DISP_HOT', 'DISP_NORMAL', 'DISP_OFF', 'DISP_ON', 'DISP_REAR_CAMERA', 'Idle', 'OFF', 'ON_BLANK', 'RR_CMRA', 'SNA', 'pressed']

## candidate_leaf 分布（候選，非裁定）
  SWE-DM-001 (State Management): 0
  SWE-DM-002 (Wake-up Management): 0
  SWE-DM-003 (Startup & Wake-up Handling): 0
  SWE-DM-004 (Thermal Management): 4
  SWE-DM-005 (Thermal Protection Management): 4
  SWE-DM-006 (HMI Popup Management): 0
  SWE-DM-007 (RVC Management): 0
  SWE-DM-008 (Dynamic Display Arbitration): 0
  有候選之列: 4
  無候選之列: 76

```

### 4.1 依錨種類分列之列數

| anchor_kind（最高優先之現存錨） | 列數 |
|---|---|
| signal | 43 |
| heading | 36 |
| value | 1 |
| melco | 0 |
| none | 0 |

各錨之存在數（非互斥，逐列獨立計）：`$signal$` 43、`[value]` 34、
heading 祖先 80、Melco 命中 037 Excluded 1（r54，`PSCFTS020-1-56-9`／
`-10`）。

`candidate_leaf`：`SWE-DM-004` 4 列、`SWE-DM-005` 4 列（皆為 r31–r34），
其餘六個 leaf 各 0；**有候選 4 列 / 無候選 76 列**。

### 4.2 與下放包 §3.3 對照之一處差異：`[VALUE]` token 數

下放包 §3.3 記「相異 9 個」並列出其分布。本輪之 regex 為
`\[([A-Za-z0-9_%\s]+)\]`，得 **13 個**。以 `\[([A-Z0-9_]+)\]`（僅大寫、
底線、數字）重算，得 **9 個且分布與 §3.3 逐項相符**
（`DISP_OFF` 15／`DISP_NORMAL` 12／`DISP_REAR_CAMERA` 5／`DISP_HOT` 4／
`DISP_ON` 1／`RR_CMRA` 1／`OFF` 1／`ON_BLANK` 1／`SNA` 1）。

差異之四個 token 為 `'0% Intensity'`、`'pressed'`、`'Idle'`、
`'DCSD_and_HU_LVDS_Backchannel_Protocol'`。

> **其中 `[0% Intensity]` 出現 20 次，是 FR 母體中出現最頻繁的值
> token，超過 `[DISP_OFF]` 的 15 次。** 它是 `$RQ_DISP_INTS$` 的值，
> 屬 R-DM14 所定之值域來源，卻被「僅大寫」之定義整個丟掉。
> 提請分析層確認 R-DM14 之「相異值 token 9」應否改採寬式定義 —— 本輪
> 兩種定義之數字皆已列出，未擇一。

`$Signal$` 側無此問題：相異 15 個，出現次數前三
`TGW_DISP_STAT` 33／`RQ_DISP_INTS` 28／`DCSD_DISP_STAT` 9，與 §3.3
逐項相符。

### 4.3 `candidate_leaf` 之產生方式（逐字，無相似度）

只有 heading 錨會產生候選，因為它是唯一在 037 側有對應物的錨：037 不含
訊號層資訊（R-DM14），Melco 命中標示的是 037 的 HW 排除項而非 leaf。

判準為 **leaf 片語逐字出現於 heading 文字中**。leaf 片語之取法：
`Requirement Title` 以 `' - '` 與 `' & '` 切分，加上
`Sub Categorization`，正規化空白、小寫，**長度 < 8 字元者捨去**。

```
SWE-DM-001: ['Display Operative State Management [ON/OFF/Wakeup]', 'ON/OFF states', 'State Management']
SWE-DM-002: ['Display Operative State Management [ON/OFF/Wakeup]', 'Touch Based WakeUp', 'Wake-up Management']
SWE-DM-003: ['Display Operative State Management [ON/OFF/Wakeup]', 'Sleep and Splash', 'Startup & Wake-up Handling']
SWE-DM-004: ['Display Operative State Management', 'Warning Pop Ups', 'Hot Algorithm', 'Warning Expectations', 'Thermal Management']
SWE-DM-005: ['Display Operative State Management', 'Warning Pop Ups', 'Hot Algorithm', 'Decisions of OFF/ON', 'Thermal Protection Management']
SWE-DM-006: ['Display Operative State Management', 'Warning Pop Ups', 'Pop Up handling', 'HMI Popup Management']
SWE-DM-007: ['Display RVC Handling', 'RVC Management']
SWE-DM-008: ['Display RVC Handling', 'Dynamic Display Arbitration']
```

`MIN_PHRASE = 8` 是本檔唯一可調參數。**它不使比對變成模糊** —— 片語
要嘛逐字出現要嘛不出現 —— 它只擋掉過於泛用之片段。每一筆候選都在
`note` 欄載明命中之片語原文（如 `SWE-DM-004←'Hot Algorithm'`），可逐筆
目視覆核。§七第 10 條未觸發：全流程無任何「相似」「近似」「模糊」步驟。

`'Hot Algorithm'` 同時是 004 與 005 之片語，故 r31–r34 之候選為兩者並列，
**不擇一**。

### 4.4 錨定法自身之兩項限制（**須與結果併同引用**）

1. **heading 錨在 r72 退化。** FR 母體之 heading 祖先分布：

   | 列數 | heading 祖先 |
   |---|---|
   | **48** | r72 `2.2 Serializer Touch Interrupt PIN Definition` |
   | 6 | r62 `2.3 LVDS Interface` |
   | 5 | r55 `Screen Touch Events` |
   | 4 | r30 `Multi-stage' DCSD Display Hot Algorithm` |
   | 3 | r51 `Rear Camera Events` |
   | 其餘 | 各 1–2 列 |

   **80 列中 48 列（60%）掛在同一個節點底下**，而該 heading 之文字講的是
   序列器觸控中斷之接腳定義，與顯示行為無關。對這 48 列而言 heading 錨
   「存在但無鑑別力」。另：r62 為 `2.3`、r72 為 `2.2`，**編號逆序**，
   該匯出之 Heading 層級疑似已被壓平。

2. **`RVC` 之縮寫不逐字。** 037 用 `Display RVC Handling`／`RVC Management`
   （SWE-DM-007／008），SYS2 之 heading 用 `Rear Camera Events`／
   `Rear Camera Interrupts`。`RVC` → `Rear View Camera` 之展開不是逐字
   比對，依 §七第 10 條不得作為錨，故二 leaf 之候選為 0。

   **這是方法之界線，不是「SYS2 無 RVC 需求」之發現。** 兩者若混同，
   就是把上一輪的錯誤換個方向再犯一次。是否開放一份逐字的縮寫對照表
   （`RVC` = `Rear View Camera`）作為錨，請分析層裁示 —— 執行層不自行
   採用。

### 4.5 追加之三欄

`func_l1`／`func_l2`／`func_l3` 取自 SYS2 之
`SYS2 功能(一階/二階/三階) Function (Level n)` 三欄，為匯出檔自身之逐字
欄位。**未列為錨**（§3.3 未指定），僅作為隨列可讀之脈絡。其分布顯示
其鑑別力有限且有前綴變體：

- Level 1：73/80 非空、7 相異，最大群 `B. 顯示與互動管理(Display and
  Interaction Management)` 37 列；另有無 `B.` 前綴之
  `顯示與互動管理(Display and Interaction Management)` 5 列
- Level 3：66/80 非空、8 相異，最大群
  `B.1.3. DCSD 顯示狀態發送 (DCSD Display State Sending)` 37 列；同樣有
  無前綴變體 4 列

> 有前綴與無前綴之同名值並存，形態同 A-DM4（Category 大小寫變體）。
> 若日後要把 Function Level 當錨，須先處理此變體。本輪只記，不用。

---

## 5. `sys2_heading_tree.tsv` 全文（步驟 6）

節點 = `Category` 正規化為 `heading` 之列；子 = 其後之非 Heading 資料列，
至下一個 Heading 列為止。**位置性，取自匯出檔自身之列序，無任何相似度。**

```
# SYS2 Basic Report — section tree
node = Category normalises to 'heading'; children = following non-Heading data rows until the next Heading row (positional, from the export's own order)
data rows 333 | heading nodes 45 | rows before the first heading (orphans) 0
accounting: 333 == 333 : True

| heading_row | sys_ra_id | heading_text | child_rows | child_FR_count |
|---|---|---|---|---|
| r2 | SYS-RA-DM-001 | ICS and DCSD [CFTSMV020_CIP_R3] | （無） | 0 |
| r3 | SYS-RA-DM-002 | Revision Notes | r4–r4 (1) | 0 |
| r5 | SYS-RA-DM-004 | Introduction | r6–r11 (6) | 0 |
| r12 | SYS-RA-DM-011 | HU Behavior when receiving Implausible Signal Values | r13–r13 (1) | 1 |
| r14 | SYS-RA-DM-013 | DCSD and HU HMI Communication | r15–r19 (5) | 2 |
| r20 | SYS-RA-DM-019 | DTC Maturation Criteria | （無） | 0 |
| r21 | SYS-RA-DM-020 | Networking DTC's | （無） | 0 |
| r22 | SYS-RA-DM-021 | BH-CAN Loss of Communication | r23–r28 (6) | 2 |
| r29 | SYS-RA-DM-028 | The DTCs are defined in Diagnosis specification. | （無） | 0 |
| r30 | SYS-RA-DM-029 | Multi-stage' DCSD Display Hot Algorithm | r31–r34 (4) | 4 |
| r35 | SYS-RA-DM-034 | DCSD Display Status Behavior | （無） | 0 |
| r36 | SYS-RA-DM-035 | Rear Camera Interrupts | r37–r37 (1) | 1 |
| r38 | SYS-RA-DM-037 | HU and DCSD Screen ON behavior | r39–r39 (1) | 1 |
| r40 | SYS-RA-DM-039 | Rear Camera Events | r41–r42 (2) | 2 |
| r43 | SYS-RA-DM-042 | Rear Camera Interrupts | r44–r45 (2) | 2 |
| r46 | SYS-RA-DM-045 | Screen Touch Event Interrupts for DCSD | r47–r47 (1) | 1 |
| r48 | SYS-RA-DM-047 | HU 3-second Timer Times Out | r49–r49 (1) | 1 |
| r50 | SYS-RA-DM-049 | HU and DCSD Screen OFF state Behavior | （無） | 0 |
| r51 | SYS-RA-DM-050 | Rear Camera Events | r52–r54 (3) | 3 |
| r55 | SYS-RA-DM-054 | Screen Touch Events | r56–r61 (6) | 5 |
| r62 | SYS-RA-DM-061 | 2.3 LVDS Interface | r63–r71 (9) | 6 |
| r72 | SYS-RA-DM-071 | 2.2 Serializer Touch Interrupt PIN Definition | r73–r303 (231) | 48 |
| r304 | SYS2-RA-303 | ICS HMI Communication | r305–r305 (1) | 0 |
| r306 | SYS2-RA-305 | HU behavior in response to ICS POWER hardkey pressed events | （無） | 0 |
| r307 | SYS2-RA-306 | HU behavior in response to ICS SCREEN OFF hardkey press events | （無） | 0 |
| r308 | SYS2-RA-307 | Rotary Knob Data Transfer {4819577} | r309–r310 (2) | 0 |
| r311 | SYS2-RA-310 | Short Press Event | （無） | 0 |
| r312 | SYS2-RA-311 | Press and Move Event | （無） | 0 |
| r313 | SYS2-RA-312 | Stuck Button Behavior | r314–r316 (3) | 1 |
| r317 | SYS2-RA-316 | DCSD Display Status Behavior | （無） | 0 |
| r318 | SYS2-RA-317 | Rear Camera Interrupts | （無） | 0 |
| r319 | SYS2-RA-318 | HU and DCSD Screen ON behavior | （無） | 0 |
| r320 | SYS2-RA-319 | Rear Camera Events | （無） | 0 |
| r321 | SYS2-RA-320 | HU and DCSD Transitioning to Screen OFF behavior | （無） | 0 |
| r322 | SYS2-RA-321 | Rear Camera Interrupts | （無） | 0 |
| r323 | SYS2-RA-322 | Screen Touch Event Interrupts for DCSD | （無） | 0 |
| r324 | SYS2-RA-323 | HU and DCSD Screen OFF state Behavior | （無） | 0 |
| r325 | SYS2-RA-324 | Rear Camera Events | （無） | 0 |
| r326 | SYS2-RA-325 | Screen Touch Events | （無） | 0 |
| r327 | SYS2-RA-326 | DCSD Display Hot Behavior | r328–r328 (1) | 0 |
| r329 | SYS2-RA-328 | Multi-stage' DCSD Display Hot Algorithm | （無） | 0 |
| r330 | SYS2-RA-329 | Touch Screen Event Communication and X-Y Coord System | r331–r331 (1) | 0 |
| r332 | SYS2-RA-331 | (Press,) Drag and Drop Event | （無） | 0 |
| r333 | SYS2-RA-332 | [Artifact Type:Description] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1M, R1L-R, R1H, VP484, R1L, VP384, VP4R84, VP5R120] [EE Architecture:Atlantis Mid, PowerNet, Atlantis High]_x000D_ A Press, Drag and Drop event will be used by the HU for all touch screen HMI controls (ex. 'Reconfigurable Menu Bar') that allow the customer to press and drag a screen object to some other location on the screen and then to assign (drop) the object onto some other screen control._x000D_ | （無） | 0 |
| r334 | SYS2-RA-333 | Capacitive Multi-touch Screen Gesture support | （無） | 0 |

wrote /Users/peihe/Work_Projects/TC_Generator/features/display/data/sys2_heading_tree.tsv
FR rows under a heading: 80
headings with 0 FR children: 30
```

計數自洽：45 個節點 + 288 個子列 = 333 資料列，首個 Heading 之前無孤兒列。
80 個 FR 全數落在某個節點之下。**45 個節點中 30 個之 FR 子列數為 0。**

### 5.1 此樹對 Q2 之意義（描述，非裁定）

- 有 FR 子列之節點僅 15 個，其中 r72 一個節點就吃掉 48 個 FR
- r304 起（`SYS2-RA-*` 區段）之 20 個節點裡，只有 r313
  `Stuck Button Behavior` 有 1 個 FR 子列，其餘 19 個節點 FR 子列數為 0；
  且該區段之節點名與 r30–r55 區段**大量重複**（`Rear Camera Events`、
  `Rear Camera Interrupts`、`DCSD Display Status Behavior`、
  `Screen Touch Events`、`Multi-stage' DCSD Display Hot Algorithm`
  各出現兩次）
- 即：SYS2 之後半段像是同一組章節標題的第二份副本，但其下幾乎沒有 FR

> 這件事本身可能是 Q2 的關鍵（母體 80 是否已含重複計數），但**本輪不
> 裁定，也不做任何去重** —— 去重需要判斷兩個同名節點是否為同一物，
> 那是跨命名之對應，屬 R-DM3 明文禁止執行層自行推定之事項。
> 以 `A-DM{n}` 登記之必要性請分析層裁示。

---

## 6. R-DM8 之 004／005 缺值判定與證據位置（步驟 9）

依 §4.1：上繳 02 §14b 之查證只回 CFTS 與 SYS3，**未查 SYS2**。本輪補查
並將兩側併讀（`scripts/hot_behaviour_join.py`）。

| SWE-DM | 缺值 | 判定 | 證據位置 |
|---|---|---|---|
| 004 | thermal warning threshold 之門檻值與單位 | **不缺**（單級門檻） | CFTS `{4820289}`／`{4820290}`，二者之 `[Radio:R1H] [EE Architecture:Atlantis High]` 與本專案 R1LR Atl-H 相符 |
| 005 | critical 判準 | **仍缺** | `1.15.1.5 {4820660}`／`1.15.4.5 {4821298}` 明載 multi-stage 版本「有較低之溫度門檻」並轉指 `{CFTS013-952}`；`{4820282}` 轉指 `{CFTS013-629}` → **DR-DM4** |
| 005 | 回復條件 | **不缺** | CFTS `{4820287}`／`{4820288}`／`{4820290}`；SYS2 r34 為 `{4820288}` 之逐字同語句 |

### 6.1 兩側之逐字對照（非相似度）

- **訊號**：`$DCSD_DISP_STAT$`、`$TGW_DISP_STAT$`、`$RQ_DISP_INTS$`
  三者兩側皆有，**單側者 0 個**
- **值**：`[DISP_HOT]`／`[DISP_OFF]`／`[DISP_ON]`／`[0% Intensity]`
  兩側皆有，**單側者 0 個**
- **溫度數值+單位**：SYS2 r30–r34 **0 段**；CFTS 全文 **2 段**，皆在
  `1.11.2.2 {4820281}` 之下

即 **SYS2 之 hot 四列是 CFTS `1.11.2.2` 的 HU 側子集，不是另一組需求**。
分析層 §4.1 所稱「SYS2 這四列正是該行為之狀態機定義」成立，惟須補一句：
它們**不含**溫度門檻，門檻只在 CFTS。故 R-DM14「SYS2 為訊號值域之第一
來源」與「門檻值來自 CFTS」兩者並行不悖，各管一段。

### 6.2 由此新開之 DR-DM4 與 A-DM13

`1.11.2.2` 之首段即寫 `See {CFTS013-629} for the DCSD Display Hot
Algorithm` —— **演算法本體不在 CFTS_020**。全文清點 CFTS_020 之外部
條號引用，相異外部文件 **8 份**：`CFTS004`／`009`／`010`／`013`／`019`／
`022`／`033`／`044`。引用次數較高者 `CFTS019-723`×12、`CFTS009-722`×9、
`CFTS033-2111`×7、`CFTS013-629`×6、`CFTS013-633`×5、`CFTS013-967`×5、
`CFTS044-656`×5、`CFTS013-952`×4。

- **DR-DM4**（新開）：CFTS_013，載 Display Hot 演算法本體與分級門檻，
  urgency HIGH，服務 SWE-DM-005
- **A-DM13**（新開）：判讀基準本身是一份會外指的文件；BLOCKED 之預估
  不能只看手上四份。其餘六份之影響本輪未逐一評估

**本節未回填任何值。** 上表引 `{4820289}` 等條號係指出「值在何處」，
讀出與採用屬 Phase 2（R-DM8、canon §8.4.1）。

---

## 7. `A-DM11` 更正後全文、`A-DM12`／`A-DM13` 新增全文

```markdown
## A-DM11 — R-DM7 覆蓋落差（**2026-08-24 更正；原結論撤回**）  [PENDING]

### 撤回之內容

本條原載「以 bag-of-words token 重疊為依據，80 列母體中 58 列無對應，
`SWE-DM-004`／`005`／`007` 命中 0 列」。**該結論撤回。**

撤回理由（下放包 03 §3.1，分析層以關鍵字直查 SYS2 `Description` 發現）：
SYS2 r30 之 Heading 為 `Multi-stage' DCSD Display Hot Algorithm`，其子列
r31–r34 為 Display Hot 之狀態機需求，與 `SWE-DM-004`／`005` 之
Requirement Title 所稱之 `Hot Algorithm` **逐字同名**。而原啟發式將
r31／r32 判給 `SWE-DM-001`、r34 判給 `SWE-DM-003`、r33 判為「無」——
**同時產生偽陽性與偽陰性，且兩者互為因果**：列被錯配到相鄰 leaf，
被搶走的 leaf 於是顯示 0。

原方法之產物依 R-TM13 保留於
`data/coverage_sys2_vs_swe_dm.RETRACTED.tsv`（檔頭已加註廢止），不刪除、
不再引用。方法本身由 **R-DM13 廢止**。

> 致誤之方法為下放包 01 R-DM7 所指定（「Description 文字」列為三種依據
> 之一），分析層已於下放包 03 §4.2 自陳「方法是我指定的」。執行層之
> 責任在於：上繳 02 §11 第 3 項雖自陳其為啟發式，**低估了嚴重性** ——
> 只說了精度不足，未察覺它會把結論指向相反方向。

### 更正後之陳述（錨定法，R-DM13）

母體不變：SYS2 `Category` 正規化為 `functional requirement` 之 **80 列**。
錨一律逐字，無錨即記無錨（`scripts/coverage_map.py`，全表見
`data/coverage_sys2_vs_swe_dm.tsv`）：

| anchor_kind（最高優先之現存錨） | 列數 |
|---|---|
| signal（`$NAME$`） | 43 |
| value（`[VALUE]`） | 1 |
| heading | 36 |
| melco | 0 |
| none | 0 |

各錨之存在數（非互斥）：含 `$signal$` 43 列、含 `[value]` 34 列、
有 heading 祖先 80 列、Melco 命中 037 Excluded 1 列（r54）。

`candidate_leaf`（**候選，非裁定**；依 R-DM12 引用時須連同 `anchor_kind`）：

| leaf | 候選列數 |
|---|---|
| SWE-DM-004（Thermal Management） | 4（r31–r34） |
| SWE-DM-005（Thermal Protection Management） | 4（r31–r34） |
| 其餘六個 leaf | 0 |
| 有候選之列 / 無候選之列 | 4 / 76 |

r31–r34 之候選依據為 heading 錨逐字含 leaf 片語 `'Hot Algorithm'`；該片語
同時出現於 004 與 005 之 Requirement Title，故兩者並列為候選，不擇一。

### 仍站得住之覆蓋陳述

**只有一句**：以 id 為據之對應為 **0 列**（A-DM2，逐字比對）。
「58 列無對應」已撤回；「76 列無候選」為錨定法之輸出，其意義是
**「無逐字錨可連到 leaf」**，不等於「不屬於本 feature 範圍」。

### 錨定法本身之兩項限制（本輪實測，須併同引用）

1. **heading 錨在 r72 退化。** SYS2 之 45 個 Heading 中，`r72
   2.2 Serializer Touch Interrupt PIN Definition` 一個節點底下掛了 231 列，
   其中 **48 列為 FR —— 佔母體 80 列之 60%**。該 heading 之文字與顯示行為
   無關，故對這 48 列而言 heading 錨存在但無鑑別力。
   （另：r62 為 `2.3 LVDS Interface`、r72 為 `2.2 …`，編號逆序，該匯出之
   Heading 層級疑似已被壓平。）
2. **RVC 之縮寫不逐字。** 037 用 `Display RVC Handling`／`RVC Management`
   （`SWE-DM-007`／`008`），SYS2 之 heading 用 `Rear Camera Events`／
   `Rear Camera Interrupts`。`RVC` → `Rear View Camera` 之展開**不是逐字
   比對**，依下放包 03 §七第 10 條不得作為錨，故二 leaf 之候選為 0。
   **這是方法之界線，不是「SYS2 無 RVC 需求」之發現** —— 兩者不可混同。

- 提案處置：本表為 R-DM7 所要求之揭露。範圍之裁定屬 Tier 2（Q2），
  依下放包 03 §4.2 **於本條之限制 1、2 有處置前不提交裁定**

## A-DM12 — 036 母本 B 欄為公式欄，前輪完全未報告  [PENDING]

036 母本 `Test Case Specification 測試用例規範` 分頁之 B 欄（`No.#\n序號`）
為公式欄。本輪以 `data_only=False` 實測 B10–B1411：

- **1402/1402 逐列符合 `=IF(ISBLANK($D{row}),"",ROW()-9)`**，$D 之列號逐列
  遞增且與所在列一致，不符 0 列
- B 欄為該分頁資料列中**唯一**含公式之欄（全 34 欄逐格掃描）
- `data_only=True` 讀 B10 得快取值 `1`，B11 起為 `None` —— 即快取為
  **陳舊值**：D10 目前為空，公式應回傳 `""`，快取卻仍存 `1`

上繳包 02 全文未提及 B 欄之存在與其公式。`workbook_state` 判 `BLANK`
不受影響（canon §2 step 1 之判準為 Test Item／TC ID，非 B 欄），但寫回時
若對 B 欄賦值，將摧毀 1402 列之公式，序號改為死值。

- 證據：本輪之 `data_only=False` 全欄掃描
- 提案處置：依 **R-DM15**，寫回一律不觸碰 B 欄；`feature.yaml` 已補註。
  另註：因快取陳舊，任何以 `data_only=True` 讀 B 欄判斷「該列是否已填」
  之實作會誤判 r10

## A-DM13 — CFTS_020 引用 8 份外部 CFTS 文件，一份未在手上  [PENDING]

判讀基準 CFTS_020 之本文以 `{CFTSnnn-mmm}` 形式引用外部條號。本輪全文
清點：相異外部文件 **8 份**（`CFTS004`／`009`／`010`／`013`／`019`／
`022`／`033`／`044`；另有指向自身之 `CFTS020-*`）。引用次數較高者：
`CFTS019-723`×12、`CFTS009-722`×9、`CFTS033-2111`×7、`CFTS013-629`×6、
`CFTS013-633`×5、`CFTS013-967`×5、`CFTS044-656`×5、`CFTS013-952`×4。

其中兩份已知直接擋住 R-DM8 之缺值：`CFTS009-722`（Splash/Disclaimer
時段，DR-DM1）與 `CFTS013-629`／`-633`／`-952`（Display Hot 演算法本體，
DR-DM4）。其餘六份之影響本輪**未逐一評估**。

- 證據：`scripts/hot_behaviour_join.py` 之併讀輸出；CFTS_020 本文全文
  regex 清點
- 影響：spec_mode D 之判讀基準本身是一份會外指的文件；BLOCKED 之預估
  不能只看手上四份
- 提案處置：登記；DR-DM4 開立。其餘六份之影響待 Phase 2 逐一評估
```

A-DM5 之補述（適用範圍擴及 036 母本）見 §3；全文在 `ANOMALIES.md`
A-DM5 條之末段。

---

## 8. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 7 項。**

1. **錨定法對 48 列（60% 母體）實質無效。** heading 錨在 r72 底下不具
   鑑別力，而這 48 列同時也是 `SYS2-RA-*` 區段之主體。**現行方法對母體
   的多數列給不出任何有意義的判讀**，這不是「這些列無關」，是「方法看
   不到」。§4.4 已載明，但我要在此重申：若拿 76/80 無候選去談範圍，
   會重蹈 58 的覆轍。
2. **SYS2 後半段之疑似重複章節未處理。** §5.1 所述之同名節點成對出現，
   若其為同一物之兩份副本，則母體 80 這個數字本身要重算。本輪未去重、
   未登記為 anomaly（去重需跨命名推定，R-DM3 禁止），但**這個疑點目前
   沒有任何條文在追它**。
3. **`[VALUE]` token 之定義未定。** 兩種定義給 9 與 13，且差異包含出現
   20 次的 `[0% Intensity]`。R-DM14 引用的是 9。在定義敲定前，任何以
   「相異值 token 數」為據的檢查都不穩。
4. **037 之 `Requirement Description` 全文仍未逐條精讀。** 前輪第 4 項
   未清，本輪亦未做。leaf 片語只取自 Title 與 Sub Categorization。
5. **SYS2 之 `Polarion`／`_polarion` 兩分頁仍未看。** 前輪第 5 項未清。
6. **CFTS_020 之其餘六份外部引用未評估。** 只查了 `CFTS009`（DR-DM1）
   與 `CFTS013`（DR-DM4）。`CFTS019-723` 被引 12 次，比這兩者都多，
   完全未查其主題。
7. **`recon.py` 仍未跑通**（A-DM8，Q5 未裁）。本輪之量測全部出自我自寫
   的六支腳本，**沒有任何一項經 repo 既有管線複核**。腳本愈多，這一點
   愈重要 —— 我自己寫的檢查驗不出我自己方法上的盲點，上一輪的 58 就是
   這樣過關的。

另記本輪**已驗而下放包未要求**者：B 欄公式之 1402 列逐列複驗與「B 為
唯一公式欄」之全欄掃描；B10 快取陳舊值之發現；CFTS_020 外部引用之全文
清點；`[VALUE]` 兩種定義之對照。

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
fix(display): retract heuristic coverage map, redo with verbatim anchors

- R-DM13: bag-of-words coverage retracted; it mislabelled SYS2 r31-r34
  and reported SWE-DM-004/005 as zero-hit. Old TSV kept as .RETRACTED.tsv
- new coverage_map.py anchors on $signal$/[value]/heading/melco only,
  verbatim throughout; candidate_leaf per R-DM12 naming
- candidates: SWE-DM-004/005 x4 rows each (r31-r34), 76 rows none
- sys2_heading_tree.tsv: 45 nodes, 48 of 80 FR rows hang off one node
- probe_036.py prints both baselines named; headers now repr()
- R-DM8 re-adjudicated with SYS2 in scope: 004 threshold and 005 recovery
  present in CFTS, 005 multi-stage criterion still missing -> DR-DM4
- A-DM12 (036 column B is a formula), A-DM13 (CFTS_020 cites 8 externals)
- RULINGS.md: R-DM12..R-DM15 verbatim (17/17 cumulative)
```

pathspec（**併行 session 會 stage 他檔，務必帶路徑**）：

```
git add features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/DECISIONS.md \
        features/display/feature.yaml \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

`data/` 下含新增之 `sys2_heading_tree.tsv`、改名後之
`coverage_sys2_vs_swe_dm.RETRACTED.tsv`，以及重出之
`coverage_sys2_vs_swe_dm.tsv`；舊路徑之刪除需一併 stage
（`git add` 帶目錄即可，或加 `-A`）。
