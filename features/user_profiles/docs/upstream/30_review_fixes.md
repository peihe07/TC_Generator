# 上繳 30 — T-1 修正與「step N 引用」之全批自檢

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`30_review_batch03.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第四批未生成**
- 語料：**108 條，未變動**（本輪修改其中 1 條之 procedure 與 ER）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 108 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 108 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／**T-1 0**／K-4b 0／Q-1 9 處待判 |
| `audit_consistency.py --self-test` | **29 / 29**（＋4：T-1）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 13 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

---

## 1. T-1 —— `TC-101` 之修正

### 1.1 修正內容

| 欄 | 前 | 後 |
|---|---|---|
| procedure 1 | `Read the status bar and **check that a Profile button is present**` | `Read the status bar and **record the Profile button icon**` |
| ER 1 | `A Profile button is present in the status bar` | `A Profile button is present in the status bar **and its icon is recorded**` |
| ER 3 | `… differs from the icon **read in step 1**` | `… differs from the icon **recorded in step 1**` |

ER1 保留「按鈕存在」之斷言（那是 4.6 之第一個要求），**另加記錄** ——
**兩者不可互換**：只寫「圖示已記錄」會失去「按鈕預設存在」這個斷言。

判準依據為下放包所引之 §5.6：**記錄步驟與比較步驟須成對**，
作法比照同批之 `TC-103`。

---

## 2. 連帶自檢 —— **命中 18 處，紅 1**（即 `TC-101`，已修）

### 2.1 **v1 判準抓不到本案 —— 這一點要先講**

我第一版的自檢寫成「該步驟有無 `record`／`read` 之動詞」。
**`TC-101` 之步驟 1 正好有 `Read`**（`Read the status bar and check that…`），
於是 **v1 判它綠** —— **而它正是本包點名要抓的那一條**。

> **動詞在，不代表讀的是同一個東西。**

**若我照 v1 的結果回報，會寫成「命中 18 處、紅 0」，
並且那份回報會通過所有閘。** 這是本輪最該記住的地方。

### 2.2 v2 判準：抓**被比較之物**

`the <X> recorded/read in step N` 之 X：

| X 之形態 | 檢查 |
|---|---|
| **具體物**（`icon`／`order`／`page`）| 該步驟須提及 X |
| **泛稱或功能詞**（`value`／`values`／`those`／`as`）| 退回查 `record`／`read` 動詞 |

**泛稱之退回是必要的，不是放水**：`the values recorded in step 1` 之步驟 1
寫的是 `record the two **preferences**` —— **泛稱與具名本就不會字面相同**，
對它們要求字面相符會製造一批假紅。

**v2 首跑之中間結果亦值得記**：加了「具體物」判準後首跑得 **紅 4**，
其中三處（`038` 之 `as`、`045` ×2 之 `those`）是**抽取誤判** ——
`as`／`those` 被當成被比較之物。補入功能詞表後為 **紅 1**。
**兩次都是判準錯，語料只有一處真缺陷。**

### 2.3 全批 18 處之分布（**命中不等於錯**）

| 引用形態 | 處 | 判 |
|---|---|---|
| 泛稱（`the value(s) recorded in step N`）| 9 | 綠 —— 該步驟皆有 `record` |
| 具體物且該步驟提及之 | 8 | 綠 |
| **具體物而該步驟未提及** | **1** | **紅 —— `TC-101`，已修** |

修正後複跑：**T-1 0 處**。

### 2.4 方向性案例（＋4，共 **29 / 29**）

| 案例 | 期望 |
|---|---|
| **`TC-101` 之原形**（步驟 1 只查按鈕在否，ER3 比對其 icon）| **紅** |
| 其修正後之形（步驟 1 記錄 icon）| 綠 |
| **護欄**：泛稱 `values` 而步驟記的是 `preferences` | **綠** |
| 引用之步驟根本不存在（`step 5` 而只有 2 步）| **紅** |

第三條是護欄 —— **它守住「泛稱不得要求字面相符」這條退路沒有被收掉**；
第四條補了一個下放包未提、但同屬「基準線不存在」之形態。

---

## 3. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **T-1 只掃 ER → procedure 之引用** | 判準盲區 | **反向不掃**：procedure 說「與步驟 N 所記者比較」而 ER 未斷言其結果者，本掃描看不見 |
| 2 | **具體物之比對為字面比對** | 判準盲區 | 步驟寫 `the button graphic`、ER 寫 `the icon` —— **同一物換個詞就會假紅**；現行語料無此形態，故未再加同義詞表（加了就要維護，而維護不動的詞表會過期）|
| 3 | **`TC-079`～`TC-095` 之 17 條未經覆核** | **分析層待辦** | 下放包已聲明；本輪未改變該數 |
| 4 | **第四批取樣清單未經覆核** | **分析層待辦** | 29 輪提出，本層尚未讀 —— **第四批因此未生成** |
| 5 | **`044`（5.15.1）之基線外文件依賴** | 承 29 輪 | 是否轉 DR 屬分析層 |
| 6 | **Q-1 之 9 處待判、D-3 之 13 處黃** | 承前 | 判讀未變 |
| 7 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 8 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

### 3.1 一項關於本輪方法之自陳

**`TC-101` 這個缺陷，現行十支閘沒有一支抓得到，是人工覆核抓到的。**
本輪把它落為 T-1 之後，同型由閘承擔 —— 但**閘是照著已知的那一條長出來的**：
它抓的是「ER 引用步驟而該步驟未建立基準線」，
**抓不到「步驟建立了基準線而 ER 從未用它」**（多餘的記錄步驟）。
現行語料是否有該反向形態，**本輪未查**。

---

## 4. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch03.py`（`TC-101` 之 procedure 1 與 ER1／ER3）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（**T-1 掃描** ＋4 方向性案例）| 否 |
| 3 | 檔案重生成 ×30 | `generated/`（batch03；**內容變動者 1 條**：`101`）| 否 |
| 4 | **檔案新建** | `docs/upstream/30_review_fixes.md`（本檔）| 否 |
| 5 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 6 | 程式執行 | T-1 自檢（v1／v2 各一次 ＋ 修正後複跑）、生成 ×1、全部閘、九支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第四批未生成** —— 待其取樣清單經覆核，且 17 條讀畢。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
