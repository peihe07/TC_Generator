# B4 — G51 動詞判準之經驗導出（R-P83 / G60）

> 來源：Comfort 與 Privacy 之已交付件。依 **R-P80**，僅用其
> 「procedure 欄含動作、pre_conditions 欄不含動作」之**結構性事實**，
> 不引用其任何內容裁決。三份皆 `read_only=True`，未呼叫 `save()`。
> 產生指令：`python features/power/scripts/build_precond_verbs.py`

## 1. 語料

| 來源 | `test_procedure` 非空列 | `pre_conditions` 非空列 |
|---|---|---|
| Comfort | 461 | 465 |
| Privacy | 11 | 11 |
| **合計** | **472** | **476** |

`pre_conditions` 之行數合計 **1823**。

## 2. 經驗動詞（procedure 行首，出現 ≥ 3 次）

共 **20** 個。

| 動詞 | 出現次數 |
|---|---|
| `press` | 245 |
| `read` | 206 |
| `turn` | 157 |
| `open` | 111 |
| `change` | 85 |
| `set` | 73 |
| `select` | 43 |
| `note` | 25 |
| `trigger` | 22 |
| `adjust` | 13 |
| `move` | 11 |
| `start` | 9 |
| `wait` | 9 |
| `touch` | 8 |
| `record` | 7 |
| `toggle` | 6 |
| `operate` | 5 |
| `put` | 4 |
| `count` | 3 |
| `do` | 3 |

## 3. 與 09 包人工清單之對照

| | 數量 | 內容 |
|---|---|---|
| 人工清單 | 22 | — |
| 經驗清單 | 20 | — |
| **人工漏列**（經驗有而人工無） | **12** | `adjust`, `change`, `count`, `do`, `move`, `note`, `operate`, `put`, `toggle`, `touch`, `turn`, `wait` |
| **人工誤列**（人工有而 procedure 從未出現） | **13** | `check`, `click`, `compare`, `confirm`, `connect`, `disconnect`, `inject`, `insert`, `launch`, `navigate`, `send`, `tap`, `verify` |

## 4. G60 —— 對已交付 `pre_conditions` 之偽陽性

| 判準 | 誤觸發行數 | 佔 1823 行 |
|---|---|---|
| 09 包人工清單 | **0** | 0.0% |
| 本包經驗清單 | **0** | 0.0% |

### 人工清單之誤觸發明細（前 20）

（無）

### 經驗清單之誤觸發明細（前 20）

（無）
