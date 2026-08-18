# 34 — 第 4–8 列判定、`priority` 全批重判、腳本自改方式改正

上繳包 | 執行層 → 分析層 | 往返 NN = 34

下放包 §J 自檢 **二次**（R-P200(c)）：
初讀為 5 / 5 /「五條」；**執行中經 R-P200(b)(ii) 就地修訂增 R-P241**，
重驗為 **§A 區塊數 6、§J 列數 6、§H 步驟 9「六條」**，三處一致 —— 續行。

**本包未改任何 TC 值**：`git diff --stat -- features/power/generated/` 為空。

---

## 一、B3 —— 腳本自改方式改正（R-P238 / G165）**先行**

### 1.1 ⚠ 對 33 包上繳之訂正：同型損壞為兩處，非一處

33 包上繳稱「六個寫入者已加 `guard_write`」。實測：
`dryrun_write_back.py` 之 `from protect_products import guard_write`
亦被誤置於**第 90 行之函式體內**（`sys.path.insert` 之後），
致 `SyntaxError: unexpected indent (line 91)`。

**自 33 包起即損壞而未被發現**，原因二項：

1. **G108 之基線僅 7 檔**（`assign_final_tc_id` / `lint_tcs` / `or_branch_coverage` /
   `reverse_coverage` / `verify_anchor_set` / `verify_layer3` / `verify_source_clause`），
   涵蓋率 **7 / 59 = 11.9%**，不含該檔；
2. 該檔於本包之前未被執行。

**故 33 包之該項陳述部分為偽**，A-PW175 所述之事故實為兩處。
依 R-P149 未以 git 修復；以本包新建之工具修復（丟棄第 90 行、插入於第 32 行）。
修復前已依 R-P234 備份（`sandbox/backup/20260818T093836Z`，133 檔）。

**推論（明載）**：「G108 未報錯」不得作為「腳本無損壞」之證據。

### 1.2 `edit_script.py`（R-P238(a)）

| 函式 | 邊界之來源（AST） | 用途 |
|---|---|---|
| `insert_module_import()` | 頂層 import 節點之 `end_lineno` 最大值 | 插入 import |
| `replace_node()` | 頂層 `def` / `class` 之 `lineno`–`end_lineno`（含裝飾器） | 整體替換 |
| `append_module_code()` | `if __name__ == "__main__":` 守衛之 `lineno`（無守衛則模組末端） | 追加頂層定義 |
| `drop_line()` | 指定行號 | 移除誤置行 |

四者皆於寫回後重新 `ast.parse`，**失敗即自動回復原檔**。fixture 4 項全數如期。

**`append_module_code()` 於本包內即被實作修正**（並陳，R-P182）：
初版追加於**模組末端**，即守衛之後，致 `main()` 執行時
`substantive_conditions` 尚未定義（`NameError`）。改為插入於守衛之前；
守衛之位置由 AST 判定，非文字定位。

### 1.3 驗證

- `features/power/scripts/` **59 檔，語法錯誤 0**
- 寫入保護仍生效：`build_b5_material.py` 如期 `ProtectedWrite: **拒寫** b5_material.md`
- 本包全部 `.py` 變更皆經 AST 邊界完成，**無任何區域性正則插入**

---

## 二、B1 —— 第 4、5、7、8 列判定（R-P236 / G163）

### 2.1 謂詞與其依據

| 列 | 判準 | 謂詞 | 依據 |
|---|---|---|---|
| 4 Decision Table | 多條件 → 結果 | `pre_conditions` 之**實質**條件項數 ≥ 2（扣除 bench 環境列） | **代理判準；僅為提案，須人工確認**（R-P236(b) / §5a） |
| 5 Equivalence Partitioning | 輸入切為 valid / invalid | `a value other than` / `other than "…"` / `out of range` | 語料實測：`valid` 0、`invalid` 0、`partition` 0；`other than` 27、`a value other` 22、`out of range` 1 |
| 7 Combinatorial | 多參數組合 | **無** | 語料實測：`combination` 0、`both` 0、`each of` 0；`and` 306 次過泛不可用 |
| 8 Scenario / Use Case | ≥ 3 步跨功能 | `test_procedure` 步數 ≥ 3 | tie-break 逐字「≥3 steps crossing features」；語料實測 3 步 16 條、2 步 248 條。**「跨功能」未機械化，須人工確認** |

**第 7 列須明載**：其命中數 0 係**「無從判定」**，**非「已判為不適用」**。

### 2.2 first-match 全批分布（1→2→3→4→5→6→7→8→9）

| 列 | method | 條數 |
|---|---|---|
| — | **矛盾（正向與明示不轉換同時命中）** | 2 |
| 1 | Negative / Invalid | 1 |
| 2 | Fault Injection | **0**（**謂詞偽陰性，見 §四**） |
| 3 | State Transition | 81 |
| 4 | Decision Table（代理判準之提案） | **80** |
| 5 | Equivalence Partitioning | 2 |
| 6 | Boundary Value Analysis | 6 |
| 7 | Combinatorial | 0（無從判定） |
| 8 | Scenario / Use Case（≥3 步） | 7 |
| 9 | Functional Based（落底） | **85** |

**（d）落底 173 → 85**（減 88：第 4 列 80、第 8 列 7、第 5 列 2）。

**第 4 列之 80 條提案尚未經人工確認** —— §D 之 G163 期望值載「第 4 列之提案皆經
人工確認」，該確認屬人工，執行層不代行。

---

## 三、B2 —— `priority` 全批重判提案（R-P237 / G164）

受檢範圍：全部 P0 **193** ＋ Branding and Theme 全 **34**，去重後 **201 / 264**。
輸出 `data/g164_priority_rejudge.md`（逐條列命中字串為證）。

### 3.1 ⚠ 並陳兩版並載明偏誤方向（R-P187 / R-P182）

| 版 | P0 成立 | 命中裝飾性 → 提案 P3 | 無類別亦非裝飾性 |
|---|---|---|---|
| **v1** | **198** | 0 | 3 |
| **v2** | **108** | **40** | **53** |

**v1 之缺陷**：（甲）`\bCAN\b` 誤加 `re.I`，吃到英文常用字 “can”；
（乙）connection 類含 `connect(?:ion|ed|ivity)` / `network`，吃到 bench 樣板句
「a CAN simulation tool **is connected** to the **network**」——
**該句存在於每一條 TC**，故該二類於 Branding and Theme 各命中 34 / 34。

**偏誤方向：偏向「P0 成立」**，即偏向確認現值、免除重判作業之方向 ——
對執行層有利，依 R-P187 明載。
**結構性理由**：謂詞讀入了 `pre_conditions` 之 bench 樣板列，該列與受測行為無關。
v2 於 `evidence()` 濾除 bench 列，並令 `CAN` 區分大小寫。

### 3.2 Branding and Theme 全 34 條（v2）

| 判定 | 條數 |
|---|---|
| 無 P0 類別命中；命中裝飾性／個人化 → **提案 P3** | **19** |
| P0 成立 | 11 |
| 無 P0 類別命中，亦非裝飾性 → 提案人工裁決 | 4 |

**與 33 §5.3 之「抽樣 5 / 5 全數無法歸類」不一致**：全量下為 23 / 34（**67.6%**）。
11 條成立者多經 boot / recovery（開機畫面確屬開機流程）。
**抽樣結論不可推及全體，此為實例**（A-PW180）。

### 3.3 本包未改任何 `priority` 值（R-P237(c)）

---

## 四、B4 —— `SWE-PM-073` 實測查證（R-P239 / G166）

### 4.1 ⚠ 裁決條文之事實前提須訂正

條文令「判 `Batt_ST_Crit` 之注入是否為該 TC 所觀察之對象」，惟
`SWE-PM-073` 標為故障注入者為 **`…-008`**，其故障為 **load shed 訊號之缺失**；
`Batt_ST_Crit` 屬 `…-009` / `…-013` 等（皆標決策表）。
**依原文逐字查證，不代換**（A-PW181）。

### 4.2 四欄逐字

`source_clause`（相關句）：
> Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle.

`pre_conditions`：
> 1. The bench is an Atlantis High configuration
> 2. A LIN and CAN simulation tool is connected
> 3. The Load Shed condition is already active

`test_procedure`：
> 1. Stop the broadcast of the two Load Shed signals on the bus
> 2. Read the AUD_LVL signal and the audio output state
> 3. Keep the broadcast stopped to the end of the ignition cycle to check that Load Shed is maintained

`expected_result`：
> 1. The two Load Shed signals are absent from the bus trace
> 2. AUD_LVL still carries the reduced level and the TLM stays muted
> 3. The Load Shed action is maintained for the rest of the current ignition key cycle

### 4.3 依 R-P232 之判定：**成立，維持**

（甲）故障**注入於 `test_procedure` 第 1 步**，非僅列為前提 ——
與 `…-050` 之 `The battery is disconnected`（情境建構之前提）形態不同；
（乙）ER 第 1 行**直接觀察故障本身**（訊號自 bus trace 消失），第 2、3 行觀察故障下之行為；
（丙）`source_clause` 以 `Under fault condition of` 明示其為故障情境。

### 4.4 ⚠ 第 2 列謂詞之偽陰性

`ROW2_RE` 為 `disconnect|inject…|fault injection`，而 `…-008` 之注入措詞為
**`Stop the broadcast`**，無上列任一詞。
故 §二之「第 2 列 0 條」**係謂詞漏判，非語料中無故障注入**。
依 17 §I（判準不因結果調整）**本包不擴充該謂詞**，標為已知偽陰性（A-PW178）。

---

## 五、B5 —— §10.2 rubric 缺口登記（R-P240）

### 5.1 ⚠ 編號歧義先訂正

33 §5.2 之 `110` / `138` / `139` 為 **tc_id 末三碼**，非 leaf ID
（leaf 全集為 `SWE-PM-001`–`115`，**無 138 / 139**）。執行層初以 leaf ID 查核而查無，
改查 tc_id 後三條皆定位（A-PW182）。

| tc_id | leaf | 現值 | §10.2 命中之類別（證據） |
|---|---|---|---|
| `…-110` | `SWE-PM-031` | P0 | `safety` → `Rear view camera`；`boot / recovery` → `Standby` |
| `…-138` | `SWE-PM-046` | P0 | `safety` → `Rear view camera`；`audio output` → `audio` |
| `…-139` | `SWE-PM-046` | P0 | `safety` → `Rear view camera`；`audio output` → `audio` |

**三條皆經第一類 `safety` 成立，與裁決一致。**
`…-138` / `…-139` 另命中 `audio output`，惟其命中字串出自 ER 之 `audio and video` ——
**`audio` 為偶然共現，不足以支撐影像輸出之歸類**，實質依據仍為 `safety`。

### 5.2 缺口之量測

全批 P0 中，**§10.2 七類皆未命中而其標的為影像／畫面輸出者共 19 條**
（如 `…-075` / `…-077`「press is ignored while the rear camera is displayed」、
`…-076` / `…-078` / `…-108` / `…-109` Splash Screen 呈現）。
後視攝影機相關者可經 `safety` 涵蓋，**Splash Screen 等非安全性畫面輸出則無類可歸** ——
**缺口於本 feature 內即已顯現**，非僅其他 feature（DTV、投影顯示）之風險（A-PW179）。
本包不改 §10.2。

---

## 六、B6 —— 目標式深挖之落實（R-P241）

### 6.1 （a）可列舉欄位之值分布，依最集中值佔比排序（264 條）

| # | 欄位 | 相異值 | 最集中值 | 佔比 | 深挖之不符率 |
|---|---|---|---|---|---|
| ① | `estimated_test_time` | 1 | （空） | **100.0%** | 定義上單值 → 0% |
| ② | `functional_safety` | 1 | `NA` | **100.0%** | 定義上單值 → 0% |
| ③ | `test_group` | 1 | `Power Management` | **100.0%** | 定義上單值 → 0% |
| ④ | `remarks` | 3 | （空） | 98.5% | **3.4%**（9 / 264） |
| ⑤ | `design_method` | 4 | 狀態轉換 | 95.8% | **60.5%**（31 包已深挖） |
| ⑥ | `split_flag` | 2 | `True` | 88.3% | **4.9%**（13 / 264） |
| ⑦ | `reasoning_note` | 27 | （空） | 82.2% | **無可機械化之判準** |
| ⑧ | `priority` | 3 | `P0` | 73.1% | **46.3%**（本包 G164：93 / 201） |
| ⑨ | `test_set` | 5 | Power State | 48.5% | 已定版（§E），不深挖 |
| ⑩ | `input_test_data` | 97 | `NA` | 39.4% | 未深挖 |
| ⑪ | `split_index` | 12 | `1` | 39.0% | 併入 ⑥ |
| ⑫ | `specification_reference` | 33 | — | 32.2% | 未深挖 |

### 6.2 ⚠ （a）之停止規則實測失效

規則為「連續二欄之不符率 < 10% 即停」。依集中度排序居前之三欄（①②③）
**皆為常數欄，不符率必為 0%** —— 規則於**第 ③ 欄即觸發停止**，
在抵達任何具資訊之欄位（④ 起）之前。

**執行層未依該規則停止**，續深挖至 ⑧。此為對本層**不利**之方向（作業量增加），
依 R-P187 明載並說明：常數欄之「0% 不符」非量測結果，而是
「該欄不承載任何資訊」之同義反覆；若計入停止規則，
該規則將永遠在最無資訊之處終止深挖（A-PW184）。

### 6.3 ⚠ （c）之前提實測為偽

R-P241(c) 稱可列舉欄位「已近用盡」並列六欄。**實測為 12 欄**，
**未列入**者六欄：`remarks`（98.5%）、`split_flag`（88.3%）、`reasoning_note`（82.2%）、
`input_test_data`（39.4%）、`split_index`（39.0%）、`specification_reference`（32.2%）。
其中 `remarks` 與 `split_flag` 於本包首次深挖即各得缺陷。
**故「已近用盡」不成立，其所推得之「自由文字欄位無人目視為必然代價」隨之減弱**（A-PW183）。

### 6.4 首次深挖之二欄

**④ `remarks`（不符 3.4%）**：判準為「對帳表載有 blocking / advisory DR 之 leaf，
其 TC 應於 `remarks` 註記」。應註記而未註記 **8 條**
（`…-033` / `034` / `035` / `036` / `038` / `040` / `041` / `043`），無 DR 而註記 1 條（A-PW185）。

**⑥ `split_flag`（不符 4.9%）**：判準依 **R-P115**（`split_index` = 同一 leaf 內依
規格原文子句出現序）。`True` 但該 leaf 僅產出 1 條 TC **9 條**；
`split_index = 0` **4 條**（`…-053` / `054` / `055` / `097`）（A-PW186）。

**⚠ 本欄判準於本包內二次訂正，三版並陳（R-P182）**：

| 版 | 分組與假設 | 不符率 |
|---|---|---|
| v1 | 以含後綴之 `req_id` 分組（**分組錯誤**） | 13 / 264 = 4.9% |
| v2 | base parent 分組；假設「split = 多個 `req_id` 分支」 | **233 / 264 = 88.3%** |
| v3 | 依 R-P115 定義：「split = 同一 leaf 產出多條 TC」 | **13 / 264 = 4.9%** |

v2 之 88.3% **恰等於 `split_flag=True` 之比率**，該巧合即為判準假設錯誤之徵候。
**偏誤方向：v2 偏向「大量不符」，即誇大深挖成效** —— 對執行層有利，
依 R-P187 明載；訂正之依據為 R-P115 之定義原文，非結果好看與否（A-PW187）。

### 6.5 （d）現有任何機制皆未涵蓋之實質性質

| # | 未涵蓋之性質 | 現有機制為何不涵蓋 |
|---|---|---|
| 1 | ER 是否為 `source_clause` 之**語義蘊含** | 反向涵蓋三透鏡皆為**詞彙層**；門檻 0.45 為人工設定。詞彙重疊高而語義相反者無機制可攔 |
| 2 | `test_procedure` 各步之**可執行性** | 無任何閘門檢查；G142 僅驗前提之**形態** |
| 3 | 同一 leaf 內多條 TC 是否**真正互斥** | `distinguishing_axis` **僅出現於 `gen_batch04/05/06.py` 三個產生器，不見於任何閘門或驗證腳本** |
| 4 | `tc_title` 是否忠實描述該 TC | 無機制 |
| 5 | TC 內**數值門檻**是否等於規格所載 | G94 只驗 `source_clause` 對 CFTS 原文之保真；TC 內之 `20` / `10 seconds` 與 clause 之對應無機制 |
| 6 | 前提條件是否**充分** | G142 / G147 驗型態與狀態描述，不驗其足以使 procedure 決定性可執行 |
| 7 | **測項之遺漏** | 反向涵蓋為詞彙層透鏡，門檻與拆句規則皆人工設定；G113 只看 OR 分支 |

**本包未新增任何涵蓋之機制**，據實列出使缺口可見（A-PW188）。

### 6.6 （d）R-P159 加註

依 R-P36 原文不改，加註指向 R-P241。
原文 SHA256 `43fbfd07141987782a0af0a18608cfec`，**加註前後同一（UNCHANGED）**。

---

## 七、§D 自驗

| # | 項目 | 期望值 | 實測 |
|---|---|---|---|
| G163 | 第 4、5、7、8 列判定 | 各列命中數；落底 173 → ?；第 4 列提案皆經人工確認 | 分布見 §二；落底 **173 → 85**；**第 4 列 80 條提案尚待人工確認**（執行層不代行） |
| G164 | `priority` 重判提案 | 逐條依據；建議 P3 數 | 201 條逐條依據見 `data/g164_priority_rejudge.md`；**建議 P3 40 條**（Branding and Theme 19） |
| G165 | 腳本自改方式 | 無任何 `.py` 之區域性正則插入；曾以正則插入者已列出 | **PASS**；59 檔語法錯誤 0；曾以正則插入者已列出，並修復第二處既存損壞 |
| G166 | `SWE-PM-073` 查證 | 四欄逐字；第 2 列成立與否 | 四欄逐字見 §四；**第 2 列成立，維持**；另發現謂詞偽陰性 |
| G167 | （**§D 未列期望值**） | — | B6 實測見 §六；**執行層不自行擬定期望值**（A-PW189） |
| G70 | lint 全閘 | 全 PASS | **阻斷類 PASS，exit = 0**；待人工裁決 275 項（R-P42(b) / R-P67，不判 FAIL） |

**不改值之佐證**：`git diff --stat -- features/power/generated/` 為空。

---

## 八、帳冊異動

- **RULINGS.md**：R-P236 – **R-P241** 六條逐字抄入 ＋ 執行層回報；
  R-P159 依 R-P36 加註。
  **R-P1 – R-P241 連續、無重複、無缺號**；既有條文前綴 SHA256
  `2aaca22fe0bbae549831a0a1b6007591`（**UNCHANGED**）。
- **ANOMALIES.md**：新增 **A-PW176 – A-PW189**（14 條）。**A-PW1 – A-PW189 無缺號**。
- **DATA_REQUESTS.md**：無新增（DR-PW1 – DR-PW15 沿用）。

---

## 九、執行層自判：本包仍有該驗而未驗者

**有，五項。**

1. **第 4 列之 80 條提案未經人工確認。** R-P236(b) 明訂代理判準不得凌駕實質判準，
   §D 之 G163 期望值亦載「皆經人工確認」——**該確認未做**，
   故第 4 列之 80 條與落底之 85 條**皆為暫定值**。
2. **第 8 列之「跨功能」未機械化。** 現行謂詞只驗「≥ 3 步」，
   7 條命中者是否真為跨功能未確認。
3. **第 7 列無謂詞，其 0 為「無從判定」。** 若語料中確有組合測試而措詞不同
   （如第 2 列之 `Stop the broadcast` 之於故障注入），現行方法看不見它。
   **第 2 列已證實發生此事，第 7 列同型風險未排除。**
4. **G164 之 v2 謂詞未經 fixture 驗證。** 其 v1 之缺陷係由 Branding 之
   34 / 34 異常比率反推而得，非由 fixture 攔下 ——
   **依 R-P214，一個自設、自實作、自回報之判準，其首次適用不足以證其正確**。
   v2 是否另有同型偽陽／偽陰，無機制可知。
5. **本包新增之 `remarks` / `split_flag` 兩項缺陷（9 + 13 條）未改值。**
   依 R-P237(c) 之同一原則留待 35 包，惟本包未取得明文裁定其一併處理，
   **有遺漏之風險，於此標明**。
