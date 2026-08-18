# G192 —— 同型缺陷之全域搜尋（R-P273）

> 起點：第 6 列之 `limit(\b|±)` 命中裸詞 `limit` ——
> 37 包已於 `rejudge_axis` 修過同一缺陷而 `rejudge_design_method` 未同步。
> **本檔只查與呈**；修正與否逐項於上繳說明。

## 一、彙總（掃描 80 個謂詞定義）

| 項 | 數 |
|---|---|
| **甲** 同名謂詞於 ≥ 2 模組各自定義 | **8** |
| 　其中內容**已分岔**（副本不一致） | **6** |
| **乙** 含裸英文常用詞之謂詞 | **28** |

## 二、甲 —— 同名謂詞之多處定義（8）

| 謂詞名 | 模組 | 內容一致 |
|---|---|---|
| `BENCH_RE` | `audit_precond_state`、`rejudge_design_method`、`rejudge_priority` | **否 —— 已分岔** |
| `COND_RE` | `confirm_row4`、`rejudge_design_method` | **否 —— 已分岔** |
| `MODE_RE` | `audit_precond_state`、`rejudge_axis` | **否 —— 已分岔** |
| `PD_RE` | `build_b1`、`build_b2`、`build_layer3`、`verify_gates`、`verify_gates_03`、`verify_layer3` | 是 |
| `PM_RE` | `build_b1`、`build_b2`、`build_layer3`、`verify_gates`、`verify_gates_03`、`verify_layer3` | 是 |
| `TOKEN_RE` | `build_b4_signals`、`rejudge_axis` | **否 —— 已分岔** |
| `TRIGGER_RE` | `build_swepm025_triggers`、`rejudge_axis` | **否 —— 已分岔** |
| `WORD_RE` | `build_er_restatement`、`build_precond_verbs` | **否 —— 已分岔** |

### 已分岔者之逐一比對

**`BENCH_RE`**

- `audit_precond_state`：`simulation tool|bench|injection tool|is connected|is available|is paired|equipped|present in the bench|clock is set|network is awake|tool is connected`
- `rejudge_design_method`：`simulation tool|bench|injection tool|is connected|is available|is paired|equipped|clock is set|carries the ex-factory`
- `rejudge_priority`：`simulation tool|test bench|is connected to|is available|is paired with|equipped with|clock is set|carries the ex-factory`

**`COND_RE`**

- `confirm_row4`：`\b(?:When|While|If|Under|Unless|In case|Once|As long as|in the following .{0,12}conditions?)\b`
- `rejudge_design_method`：`^\s*\d+\.`

**`MODE_RE`**

- `audit_precond_state`：`\bis in (?:the )?([A-Z][A-Za-z_\- ]{2,30}?)(?: mode| state| status)?\b|\b([A-Z]{3,}(?:[ _][A-Z]{2,})*)\b`
- `rejudge_axis`：`\bBODY (?:ON|OFF-TIMED|OFF)\b|\bFull-Operation\b|\bPartial Operation\b|\bTimed\b|\bStandby\b|\bSleep\b|\bIdle\b|\bBench\b|\bOff\b`

**`TOKEN_RE`**

- `build_b4_signals`：`\$[A-Za-z_]+\$|[A-Za-z][A-Za-z0-9_.$]*\d*`
- `rejudge_axis`：`\$?[A-Za-z][\w.\-]*\$?|\[\d+h\]|\d+`

**`TRIGGER_RE`**

- `build_swepm025_triggers`：`(Front_Panel_OnOff\.Req|CLIMATIC_PANEL\.Radio_Btn0)(.*?)(?=THEN|$)`
- `rejudge_axis`：`\b[A-Za-z]\w*\.(?:Req|Info|Sts)\b|\bSTATUS_[A-Z]+\.\w+|\$[A-Za-z_]\w*\$|\b\w+_Enable\b|\bFront_Panel_OnOff\b`

**`WORD_RE`**

- `build_er_restatement`：`[A-Za-z][A-Za-z0-9_.$'-]*`
- `build_precond_verbs`：`[A-Za-z][A-Za-z'-]*`

## 三、乙 —— 含裸英文常用詞之謂詞（28）

> **裸詞非必為缺陷** —— 其風險為「該詞於語料中另有無關之用法」，
> 須逐一實測其命中組成方能判定。第 6 列之 `limit` 即經此法查出。

| 模組 | 謂詞 | 裸詞 |
|---|---|---|
| `audit_precond_state` | `MODE_RE` | `mode`、`state`、`status` |
| `audit_precond_state` | `BENCH_RE` | `available`、`awake`、`bench`、`clock`、`connected`、`equipped`、`injection`、`network`、`paired`、`present`、`simulation`、`tool` |
| `build_dangling` | `WRAPPER_RE` | `docx`、`xlsx` |
| `build_dangling_rulecheck` | `RESOURCE_RE` | `docx`、`xlsx` |
| `confirm_row4` | `COND_RE` | `case`、`conditions`、`following`、`long` |
| `g113_buckets` | `ILLUSTRATIVE_RE` | `example`、`like`、`rather`、`refer`、`specification`、`than` |
| `lint_tcs` | `ENV_STABILITY_RE` | `configured`、`connected`、`from`、`functioning`、`normal`、`normally`、`operating`、`power`、`powered`、`properly`、`stable`、`steady` |
| `lint_tcs` | `TABLE_RE` | `table` |
| `lint_tcs` | `PRECOND_BEHAVIOUR_RE` | `been`、`begins`、`changes`、`completed`、`completes`、`elapses`、`expires`、`finishes`、`hour`、`minute`、`occurred`、`occurs` |
| `lint_tcs` | `TEST_QUANTITY_RE` | `burst`、`cycles`、`events`、`injection`、`interval`、`intervals`、`iterations`、`level`、`measurement`、`starting`、`volume`、`window` |
| `lint_tcs` | `FINAL_STEP_INTENT_RE` | `check`、`confirm`、`that`、`verif`、`verify`、`whether` |
| `lint_tcs` | `TIME_TOKEN_RE` | `duration`、`elapsed`、`measured`、`milliseconds`、`minutes`、`recorded`、`seconds`、`time`、`timer` |
| `lint_tcs` | `TIME_EQUALITY_RE` | `equal`、`equals`、`exactly`、`matches` |
| `rejudge_axis` | `TIMING_RE` | `minutes`、`seconds`、`time` |
| `rejudge_axis` | `BOUNDARY_RE` | `least`、`most`、`than` |
| `rejudge_design_method` | `NO_TRANSITION_RE` | `change`、`does`、`pass`、`reads`、`remains`、`reset`、`stays`、`still`、`unchanged` |
| `rejudge_design_method` | `ROW1_RE` | `allowed`、`attempt`、`illegal`、`invalid` |
| `rejudge_design_method` | `ROW2_RE` | `disconnect`、`fault`、`inject`、`injection` |
| `rejudge_design_method` | `POSITIVE_RE` | `back`、`enters`、`from`、`full`、`goes`、`idle`、`leaves`、`mode`、`passes`、`power`、`reaches`、`returns` |
| `rejudge_design_method` | `ROW6_RE` | `after`、`before`、`boundary`、`date`、`greater`、`less`、`limit`、`passes`、`than` |
| `rejudge_design_method` | `BENCH_RE` | `available`、`bench`、`carries`、`clock`、`connected`、`equipped`、`factory`、`injection`、`paired`、`simulation`、`tool` |
| `rejudge_design_method` | `ROW5_RE` | `other`、`range`、`than`、`value` |
| `rejudge_priority` | `COSMETIC_RE` | `animation`、`brand`、`colou`、`customi`、`font`、`icon`、`image`、`screen`、`season`、`skin`、`splash`、`theme` |
| `rejudge_priority` | `BENCH_RE` | `available`、`bench`、`carries`、`clock`、`connected`、`equipped`、`factory`、`paired`、`simulation`、`test`、`tool`、`with` |
| `reverse_coverage` | `SPLIT_RE` | `until` |
| `reverse_probe_rows` | `PARAM_RE` | `carries`、`equal`、`greater`、`reads`、`than` |
| `reverse_probe_rows` | `REMOVE_RE` | `broadcast`、`cease`、`ceases`、`cuts`、`disable`、`disables`、`disconnect`、`disconnects`、`interrupt`、`interrupts`、`message`、`messages` |
| `scan_clause_patterns` | `ENUM_RE` | `following` |
