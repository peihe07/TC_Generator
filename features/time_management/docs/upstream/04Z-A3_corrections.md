# 上繳 04Z-A3 — sheet_members / diff_cells 唯讀評估，A-TM22 定級為理論風險

執行層 → 分析層。對應 `docs/handoff/04Z-A3_positive_verification.md`。2026-08-21。

T1–T4 全數完成。

**定級結論先講：A-TM22 為理論風險，非實質盲區。** `sheet_members()`
走 OOXML 標準之權威對映路徑（`workbook.xml` `r:id` → `workbook.xml.rels`
`Target`），非索引推算亦非檔名慣例；解析失敗由下游 `surgical_save` raise
攔截；母本實測經 DV 計數交叉驗證通過。**依據見 §3.3。**

**但 G-TM3 仍應實作** —— 其主要防護對象應改為 **A-TM21(a) 之 column 層**，
該層無任何對映保證機制。見 §3.4。

---

## 1. T4 驗證（依 R-TM31，列明細）

```
R-TM38        RULINGS.md:1276        R-TM39        RULINGS.md:1307
G-TM3         RULINGS.md:1334        G-TM2 項 3 訂正 RULINGS.md:1240 / :1245
A-TM22 索引    ANOMALIES.md:34       A-TM21(d)      ANOMALIES.md:1231 / :1234

R-TM 條數 42   期望 42   OK
G-TM 條數  3   期望 3    OK
A-TM 條數 22   期望 22   OK

scripts/ mtime  09:15:18 / 09:13:36 / 09:14:32   （三度上繳所記相同）
backend/ git status → 無輸出（未改）
```

## 2. T1 / T2 寫入確認

| T | 內容 | 位置 |
|---|---|---|
| T1 | R-TM38、R-TM39、G-TM3 | `:1276`、`:1307`、`:1334`；40 → **42**，G-TM 2 → **3** |
| T1 | G-TM2 項 3 訂正 | `:1240`。**原文加刪除線保留**（R-TM13） |
| T2 | A-TM22 + 索引列 | `ANOMALIES.md:34`；21 → **22** |
| T2 | A-TM21(d) 嚴重性提高 | `:1231`。A-TM21 條數不變 |

## 3. T3 — `backend/` 兩項唯讀評估

### 3.1 `sheet_members()`（`backend/xlsx_surgical.py:75-103`）

**(1) 如何解析 —— 走 rels，非推算**

```python
book = z.read("xl/workbook.xml").decode("utf-8")          # :83
rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")  # :84
# rels: Id -> Target
for rel in re.finditer(r"<Relationship\b([^>]*)/>", rels):     # :86-91
    target[rid.group(1)] = tgt.group(1)
# workbook.xml: <sheet name= r:id=> -> target[r:id]
for m in re.finditer(r"<sheet\b([^>]*?)/?>", book):            # :93-102
    out[_unescape(name.group(1))] = tgt
```

**此即 OOXML 標準所定之權威對映路徑**：分頁名 → `r:id` → rels 之
`Target`。**不憑索引推算、不憑檔名慣例。**

docstring（`:78-80`）明言其理由：

> Resolved rather than assumed: sheet order in `workbook.xml` is display
> order, which is not the `sheetN.xml` numbering. The AMFM workbook happens
> to agree; relying on that would be luck.

**(2) 是否有自身之正確性保證 —— 有，且錯誤不會靜默取到別的**

| 情形 | 行為 |
|---|---|
| `r:id` 解析不到對應 rel | `:97-98` `continue` —— **該分頁不進 `out`** |
| 下游查不到該分頁 | `surgical_save:295-296` `raise StructureError(f"no zip member resolved for sheet {name!r}")` |

**關鍵**：解析失敗之後果是「**該 key 不存在**」而非「**取到錯的 member**」，
且下游有明確之 raise。**這與 A-TM21(a) 之情形根本不同** —— 後者是
「字母宣告錯了就寫進錯欄」，錯誤會被**執行**而非被攔。

`sheet_members()` 內之 `continue` 為靜默，但**其靜默不產生錯誤結果，
只產生缺漏**，而缺漏必被下游 raise。**兩者互補。**

**(3) 母本實測 + DV 交叉驗證 —— 通過**

`sheet_members()` 對母本複本之完整解析（九分頁）：

```
Cover_old                          -> xl/worksheets/sheet1.xml
ChangeHistory_old                  -> xl/worksheets/sheet2.xml
Cover 封面                          -> xl/worksheets/sheet3.xml
ChangeHistory 修訂履歷                -> xl/worksheets/sheet4.xml
Product Document 記錄封面頁            -> xl/worksheets/sheet5.xml
Test Case Specification 測試用例規範    -> xl/worksheets/sheet6.xml   ← 目標分頁
Reference                          -> xl/worksheets/sheet7.xml
QS Suggestion                      -> xl/worksheets/sheet8.xml
下拉選單                             -> xl/worksheets/sheet9.xml
```

**交叉驗證（`04Z-A3` T3(1) 所指定者）**：

| 路徑 | 結果 |
|---|---|
| `feature.yaml` `workbook.sheet` | `Test Case Specification 測試用例規範` |
| `sheet_members()` 解析 | `xl/worksheets/sheet6.xml` |
| 該 member 之 `_dv_counts` | **`(3, 1)`** |
| `04Z-A2` §3.1 所測之 x14 所在 | **`sheet6.xml (3, 1)`** |

**兩條獨立路徑指向同一 member** —— 一條走 rels 解析（結構），一條走
DV 計數特徵（內容）。**相符。**

**(4) 附帶：母本之顯示序與檔名序恰好全部一致**

九分頁之顯示序 1–9 與 `sheetN.xml` 之 N 逐項相同。**即憑索引推算在本
母本上會碰巧正確** —— 正是 docstring 所稱之「happens to agree; relying
on that would be luck」。`sheet_members()` 未依賴它，故該巧合不影響
其正確性，但**它使「憑索引推算」之錯誤在本母本上無法被發現** ——
若日後有人以索引推算替換此函式，母本測試會全綠。此點值得記錄。

### 3.2 `diff_cells()`（`:113-137`）

**(1) 座標從何而來**

```python
for name in mutated.sheetnames:                    # :121
    if name not in original.sheetnames:
        raise StructureError(f"sheet {name!r} is new; ...")   # :123-124
    old, new = original[name], mutated[name]
    max_row = max(old.max_row, new.max_row)        # :126
    max_col = max(old.max_column, new.max_column)  # :127
    for r in ... for c in ...:
        if a != b: sheet_changes[(r, c)] = b       # :133-134
```

**逐 cell 全掃比對**，座標即 openpyxl 之 `(row, col)` 索引，非解析而來。
新增分頁即 raise（`:123`）。

**(2) 是否以分頁名或 member 名為 key —— 以分頁名，且與 `sheet_members()`
同源**

`changes[name]`（`:136`）之 key 為 **openpyxl 之 `sheetnames`**。
`surgical_save:293-296` 以該 key 查 `sheet_members()` 之結果：

```python
for name, edits in changes.items():
    member = members.get(name)
    if member is None:
        raise StructureError(f"no zip member resolved for sheet {name!r}")
```

**兩個 key 之來源**：

| 來源 | 取得方式 |
|---|---|
| `diff_cells` | openpyxl `wb.sheetnames`（openpyxl 自 `workbook.xml` 讀出）|
| `sheet_members` | 直接正則解析 `workbook.xml` 之 `name="…"` ＋ `_unescape` |

**二者最終皆源自 `workbook.xml` 之同一組 `name` 屬性**，故正常情形一致。
理論上之分歧點在 **XML escape 之處理差異**：`sheet_members` 之
`_unescape` 處理 `&amp;` / `&lt;` / `&gt;` 等；若 openpyxl 之處理範圍不同
（如數值字元參照 `&#x…;`），分頁名含該類字元時兩者可能不一致。

**本 feature 之九個分頁名皆不含須 escape 之字元**（實測見 §3.1(3)），
故此路徑上無風險。**但這是「當前資料恰好安全」而非「機制保證安全」**
—— 若日後分頁名含 `&`，須重驗。

### 3.3 **A-TM22 定級：理論風險**（非實質盲區）

依 `04Z-A3` §3 之定級判準（「若 `sheet_members()` 之對映有自身之正確性
保證，本條降為理論風險；若無，則為實質盲區」）：

**對映有自身之正確性保證，三項依據：**

1. **走權威來源** —— OOXML 標準之 `r:id` → rels `Target`，非推算（§3.1(1)）
2. **錯誤形態為缺漏而非誤指** —— 解析失敗使 key 不存在，下游
   `surgical_save` 必 raise；**不會靜默取到別的 member**（§3.1(2)）
3. **母本實測經獨立路徑交叉驗證** —— rels 解析與 DV 內容特徵同指
   `sheet6.xml`（§3.1(3)）

**故 A-TM22 降為理論風險。**

**但降級附兩項條件，須明記：**

- **(i) 本定級針對當前母本結構。** 若工作簿之分頁組成、rels 編號或分頁名
  變動（含含有 XML escape 字元之分頁名，§3.2(2)），須重驗。
- **(ii) 母本之顯示序與檔名序恰好全部一致**（§3.1(4)），故「憑索引推算」
  之替代實作在本母本上會全綠。**本定級之依據是現行實作走 rels，
  不是母本測試通過** —— 兩者不可混用。

### 3.4 **G-TM3 仍應實作，但其主要防護對象應改**

`04Z-A3` §3 將 G-TM3 定位為 A-TM22 之對策。**經 §3.3 定級後，該定位
應調整：**

| 盲區 | 對映之保證 | G-TM3 之防護力 |
|---|---|---|
| member 層（A-TM22） | **有**（rels 權威 + 下游 raise） | 錦上添花 |
| **column 層（A-TM21(a)）** | **無** —— `feature.yaml` 字母純宣告，`resolve_columns()` 之複驗不存在 | **主要防護對象** |

**column 層才是無保證的那一層。** `resolve_columns()` 之 docstring 承諾
表頭複驗而實作只讀字母（A-TM21(a)），且 `verify_structure` 三層皆不驗
欄位對映 —— 寫進錯欄時錯欄仍在目標分頁內、屬 `patched`，全綠。

**提請**：G-TM3 之條文理由段宜補述此點，使實作者知道取樣欄之選擇
應以偵測 column 層位移為首要（執行層已於 G-TM3 之回報段補記取樣建議：
以 `tc_id` 為最佳取樣欄，因其依序號必互異，可排除「兩欄值恰同」之偽陰性）。

**執行層未自行修改 G-TM3 條文**（條文修改屬分析層）。

## 4. T5(4) — 該驗而未驗者（五全集）

### 4.1 依全集 1（指令逐項）

T1–T4 全數完成。T3 兩項皆讀畢並附位置與片段，A-TM22 已定級。

### 4.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + 四處位置 | 42 / G-TM 3；:1240 / :1276 / :1307 / :1334 |
| `ANOMALIES.md` | 條數 + 兩處位置 | 22；:34 / :1231 |
| `scripts/` | mtime | 09:13–09:15，未動 |
| `backend/` | `git status` | 無輸出，未改 |

兩處 `str.replace` 前置 `assert` + `count==1`。

### 4.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | `_patch_row` / `_new_row_xml` / `_fix_dimension` 之**實跑** | 全部評估皆讀碼推得。`surgical_save` 之完整路徑**從未在本 feature 實跑過**（無 TC 可寫）。**B1 生成後首次寫回即為首次實跑** —— G-TM3 之正向驗證因此更重要 |
| 2 | openpyxl 之 sheetname escape 處理範圍 | §3.2(2) 之理論分歧點。本 feature 分頁名安全，故未追 |
| 3 | A-TM21 (a)(f) 之實跑證實 | 凍結中不執行 |
| 4 | `build_batch_context.py` 全文複查 | 執行層自寫，`04R` 起未重讀 |
| 5 | A-TM05 / A-TM10 之實跑 | 續掛 |
| 6 | PU 陽性對照 | 待 Pei 裁 |
| 7 | A-TM12 / A-TM19 | 併後續批次 |
| 8 | R-TM38 之回溯自查 | **見 R-TM38 回報段之提請** —— 本 feature 迄今上繳中之條文引用是否有同型截斷，未逐一回查 |

**第 1 項須特別說明**：`backend/xlsx_surgical.py` 之全部評估
（`verify_structure` 三層、`_dv_counts`、`patch_sheet_xml`、
`sheet_members`、`diff_cells`）皆為**讀碼**與**對母本之唯讀探測**。
**寫入路徑本身從未執行過** —— 因本 feature 尚無任何 TC。

故所有「此保護有效」之結論，其強度為「程式碼看起來會這樣做」，
非「實測確認它這樣做」。**B1 之首次寫回將是該路徑在本 feature 之首次
實跑**，屆時 G-TM3 之正向驗證是唯一能發現「讀碼推論與實際行為不符」
之機制。

### 4.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| `sheet_members` 解析目標分頁為 sheet6 | 其餘八分頁各指向不同 member，非全部指向同一個 | 有 |
| DV 交叉驗證相符 | `_dv_counts` 對其餘七分頁得 `(0,0)`，非一律回報 `(3,1)` | 有 |
| A-TM22 降為理論風險 | 同一分析對 A-TM21(a) **維持**實質盲區 → 該分析非一律降級 | 有 |
| `backend/` 未被本包改動 | 同期 `RULINGS.md` / `ANOMALIES.md` 確有寫入 | 有 |

### 4.5 依全集 5（設計說明之可驗性）

`04Z-A3` §1 之自我定性（「引用的人切斷」與 docstring 承諾／讀者切斷
同構）—— 執行層同意，並補一項：**三者之共同點是「保留了容易保留的那半，
丟掉了需要動手的那半」**。docstring 保留承諾丟掉實作、讀者保留「找到了」
丟掉「驗過了」、引用保留形式丟掉操作。**三者皆非疏忽，而是每一步都在
「已經夠了」的地方停下。**

`04Z-A3` §2.1 之 R-TM39 —— 執行層已於其回報段補記一項界線：
「零命中」之舉證有效期限於**寫回路徑之組成不變**，路徑若引入其他模組
須重做搜尋。

## 5. 本包未動之事項

未動 git（**未 push**；分支 ahead 14）。
**未寫入、未覆蓋、未修改 `features/time_management/scripts/` 任一行**。
**未修 A-TM21 / A-TM22 任何一項。** **未改 `backend/` 任何檔**
（T3 唯讀，`git status backend/` 無輸出）。未執行任何腳本。
未生成任何 TC。未碰 `features/vehicle_setting/`。未 rm 任何檔案。
未送出 RD-1。未填 `D5`、未組 Scope 值。未以 openpyxl 存回任何工作簿。
**未自行修改 G-TM3 之條文**（§3.4 之提請留待分析層處理）。
