# G185 —— §12 全九列之條件欄與謂詞核對（R-P266）

> 權威原文：`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §12。
> **本檔只核對，不改謂詞。**

## 一、條件欄逐字之佐證

九列之條件欄逐字**皆見於權威原文**：9 / 9。
tie-break 句逐字可見：是（僅三句，對應第 3、8、9 列）。

## 二、核對結果 —— **不一致 4 / 9**

| 列 | 條件欄逐字 | tie-break | 現行謂詞所依 | 一致 |
|---|---|---|---|---|
| 1 | `Invalid input / illegal op` | — | `ROW1_RE` = `attempt to|invalid|illegal|not allowed` | 是 |
| 2 | `Simulated fault (disconnect, timeout)` | — | `ROW2_RE` = `disconnect|inject(ed|ion)? (a )?fault|fault injection` | **否** |
| 3 | `State A → State B transition` | `State Transition = state-change focus` | `POSITIVE_RE` = `passes to|transitions? to|goes to|switches to|returns to … state|enters? …|leaves? …` | 是 |
| 4 | `Multiple conditions → outcome` | — | `substantive_conditions(pre) >= 2` —— **只數 `pre_conditions`** | **否** |
| 5 | `Input partitioned valid / invalid` | — | `ROW5_RE` = `a value other than|other than "|out of range` | 是 |
| 6 | `Boundary (=limit, limit±1)` | — | `ROW6_RE` = `after the date passes|boundary|the day before|limit(\b|±)|greater than` | **否** |
| 7 | `Multi-parameter combination` | — | **無謂詞** | 是 |
| 8 | `End-to-end flow, ≥3 features` | `Scenario = ≥3 steps crossing features` | `features_of(proc)` 之相異功能族數 ≥ 3 | 是 |
| 9 | `Single feature check` | `Functional = 1–2 steps single feature` | catch-all（第 1–8 列皆未命中） | **否** |

## 三、逐列說明

### 第 1 列 —— 一致

- **條件欄逐字**：`Invalid input / illegal op`
- **tie-break**：**無**
- **現行謂詞所依**：`ROW1_RE` = `attempt to|invalid|illegal|not allowed`
- `invalid` / `illegal` 直取條件欄之二詞；`attempt to` / `not allowed` 為 `illegal op`（不被允許之操作）之語料措詞。**依條件欄，未引 tie-break。**

### 第 2 列 —— **不一致**

- **條件欄逐字**：`Simulated fault (disconnect, timeout)`
- **tie-break**：**無**
- **現行謂詞所依**：`ROW2_RE` = `disconnect|inject(ed|ion)? (a )?fault|fault injection`
- **條件欄之括號明列二例：`disconnect`、`timeout`；現行謂詞只取 `disconnect`，`timeout` 未納入。** 另 `inject…fault` 為條件欄 `Simulated fault` 之語料措詞。A-PW178 已知其漏 `Stop the broadcast`；**本次另查出漏 `timeout`。**

### 第 3 列 —— 一致

- **條件欄逐字**：`State A → State B transition`
- **tie-break**：`State Transition = state-change focus`
- **現行謂詞所依**：`POSITIVE_RE` = `passes to|transitions? to|goes to|switches to|returns to … state|enters? …|leaves? …`
- 皆為「A → B 之轉換」之正向措詞，依條件欄。tie-break（`state-change focus`）與條件欄同義，未造成分歧。

### 第 4 列 —— **不一致**

- **條件欄逐字**：`Multiple conditions → outcome`
- **tie-break**：**無**
- **現行謂詞所依**：`substantive_conditions(pre) >= 2` —— **只數 `pre_conditions`**
- **條件欄未限定條件之所在欄位；現行代理判準只數 `pre_conditions`。** R-P267 已裁其系統性低估（`…-026` 之第二條件在 `test_procedure`）。

### 第 5 列 —— 一致

- **條件欄逐字**：`Input partitioned valid / invalid`
- **tie-break**：**無**
- **現行謂詞所依**：`ROW5_RE` = `a value other than|other than "|out of range`
- 條件欄之 `valid` / `invalid` 二詞於語料實測皆為 **0**（36 包）；現行取語料中之等價切分措詞。**依條件欄之語義，未引 tie-break。**

### 第 6 列 —— **不一致**

- **條件欄逐字**：`Boundary (=limit, limit±1)`
- **tie-break**：**無**
- **現行謂詞所依**：`ROW6_RE` = `after the date passes|boundary|the day before|limit(\b|±)|greater than`
- **條件欄之 `limit±1` 為「界線值加減一」；現行之 `limit(\b|±)` 會命中裸詞 `limit`（如 `the volume limit`）。** 37 包於 `rejudge_axis` 已因同一問題另立 `BOUNDARY_RE`，**而 `rejudge_design_method` 之 `ROW6_RE` 未同步訂正。**

### 第 7 列 —— 一致

- **條件欄逐字**：`Multi-parameter combination`
- **tie-break**：**無**
- **現行謂詞所依**：**無謂詞**
- R-P249 已裁其為死列（first-match 序之結果）。無謂詞即無引用錯誤。

### 第 8 列 —— 一致

- **條件欄逐字**：`End-to-end flow, ≥3 features`
- **tie-break**：`Scenario = ≥3 steps crossing features`
- **現行謂詞所依**：`features_of(proc)` 之相異功能族數 ≥ 3
- **R-P259 已訂正** —— 舊謂詞取 tie-break 之 `≥3 steps`，現依條件欄之 `≥3 features`。

### 第 9 列 —— **不一致**

- **條件欄逐字**：`Single feature check`
- **tie-break**：`Functional = 1–2 steps single feature`
- **現行謂詞所依**：catch-all（第 1–8 列皆未命中）
- **條件欄為 `Single feature check`（實質判準）；現行為 catch-all（無判準）。** 二者不同：catch-all 會收納「非單一功能而僅因前列謂詞不足而落底」者。**惟 R-P231(c) 明訂第 9 列為 catch-all** —— 此為既有裁決與條件欄之分歧，非謂詞取錯措詞，列出供分析層裁定。
