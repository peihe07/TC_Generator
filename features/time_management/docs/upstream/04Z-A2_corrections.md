# 上繳 04Z-A2 — backend 兩項唯讀評估、canon §10.3 獨立複驗、條文落檔

執行層 → 分析層。對應 `docs/handoff/04Z-A2_backend_review.md`。2026-08-21。

T1–T5 全數完成。**兩項須先講**：

1. **canon §10.3 之引用漏了最後一句，而那句是決定性的** ——
   原文含「the generator handles assignment, **the LLM does not emit
   `tc_id`**」。此句使執行層於 `04Z` 上繳所提之 G-TM2 項 3 補充由「建議」
   升為 **canon 明文要求**。見 §4.2。
2. **`patch_sheet_xml` 以 inline string 規避 `sharedStrings.xml`**，
   故 T3(2) 第 3 項所慮之「新增字串使該 member 變動而誤報」**在設計上
   已被規避**。見 §3.2.3。

---

## 1. T5 驗證（依 R-TM31，列明細）

```
R-TM36        RULINGS.md:1184        R-TM37        RULINGS.md:1209
G-TM2 項 2 訂正 RULINGS.md:1149（節）/ :1154（區塊內）
A-TM21(b) 降級  ANOMALIES.md:1212（節）/ :1215（區塊內）/ :1225（(a) 不降級）

R-TM 條數 40   期望 40   OK
G-TM 條數  2   期望 2    OK
A-TM 條數 21   期望 21   OK

scripts/ mtime（凍結證據）
  09:15:18  build_batch_context.py
  09:13:36  lint_tcs.py
  09:14:32  write_back.py

backend/ git status → 無輸出（未改）
```

三支 mtime 與 `04R` / `04Z` 兩次上繳所記完全相同。

## 2. T1 / T2 寫入確認

| T | 內容 | 位置 |
|---|---|---|
| T1 | R-TM36、R-TM37 | `:1184`、`:1209`；38 → **40** |
| T1 | G-TM2 項 2 訂正 | `:1149`。**原文加刪除線保留**（R-TM13），訂正置於條末並註明依據包 |
| T2 | A-TM21(b) 降級註記 | `:1212`。條數不變（21） |

### 2.1 R-TM37 之一項提請（執行層補記於該條回報段）

**回溯自查**：`34e2da6` 之 `rulings 35, anomalies 20` 與 `4b00d33` 之
`Rulings 29, anomalies 18` 皆為 commit 前以
`git show HEAD:...| grep -c` 對**已入庫內容**實測所得，非取自下放包期望值。
**符合 R-TM37。**

**提請**：R-TM37 只提「數字或狀態陳述」，未及**因果陳述**。
`34e2da6` 之 message 含「sxm was rejected on two counts」一類因果句，
本次其兩項理由皆有實測支持，但條文未涵蓋此類。是否納入？

## 3. T3 — `backend/` 兩項唯讀評估

### 3.1 `_dv_counts()`（`backend/xlsx_surgical.py:239-247`）

**(1) 如何區分 classic 與 x14**

```python
CLASSIC_DV_RE = re.compile(r"<dataValidation[ >]")     # :48
X14_DV_RE     = re.compile(r"<x14:dataValidation[ >]") # :49
```

以**namespace 前綴之字面**區分，非解析 XML 樹。掃描範圍限
`member.startswith("xl/worksheets/sheet")`（`:243`），逐 member 回傳
`(classic, x14)` 二元組。

**(2) 母本之 x14 下拉計為幾 —— 實測（唯讀）**

對 `inputs/` 之母本複本執行 `_dv_counts`：

| member | classic | x14 |
|---|---|---|
| `xl/worksheets/sheet5.xml` | 1 | 0 |
| **`xl/worksheets/sheet6.xml`** | **3** | **1** |
| 其餘七個 sheet | 0 | 0 |

**與 FORMS.md 所載逐項對應**：該檔記母本有四組 DV —— P（priority，
內嵌 list）、**R（design_method，x14 擴充）**、T–Z（車型）、
AF（test_result）。即 classic 3 + x14 1 = 4，**完全相符**。
sheet6.xml 即 `Test Case Specification 測試用例規範` 分頁。

**(3) openpyxl 丟棄 x14 時計數是否確由 1 變 0 —— 可由讀碼判定**

**可以。** `X14_DV_RE` 直接對該 member 之 XML 文字計數
`<x14:dataValidation` 之出現次數。節點若被丟棄即不存在於輸出 XML，
計數必為 0，`before[m] != after[m]`（`(3,1)` vs `(3,0)`）成立而 raise。

**此為讀碼可判定者，不需實跑** —— 因該判定只依賴「regex 對文字計數」
與「節點消失即文字消失」兩個事實，無隱藏狀態。

**且有 FORMS.md 之獨立實測佐證**：該檔記 openpyxl 存回後
`<x14:dataValidation>` 節點數 **1 → 0**、legacy DV **3 存活**、
zip members 48 → 47 —— 與本次讀碼推得之 `(3,1) → (3,0)` 一致。

**(4) 退化情形 —— 存在一個，但已由第一層互補**

`bad = {m: (before[m], after[m]) for m in before if before[m] != after[m]}`
（`:262`）**只遍歷 `before` 之 key**。若輸出新增一個來源所無之
`xl/worksheets/sheetN.xml`，該 member 不在 `before` 內，此層不檢查。

**但 `verify_structure` 第一層（`:252-259`）已檢查 member 集合之
`lost`/`added`**，新增 member 會先在該處 raise。**兩層互補，非漏洞。**

至於 classic 與 x14 皆為 0 之 member（七個），其比較為 `(0,0) != (0,0)`
即 False —— **不是恆真之漏洞**：若其 DV 由無變有，`(0,0)` vs `(1,0)`
仍會 raise。該層比較的是**前後差異**，非「是否非零」。

### 3.2 `patch_sheet_xml()`（`:184-221`）

**(1) 寫入粒度：逐 cell 節點，且只重寫受影響之 `<row>`**

`:197` `for row_num in sorted(set(by_row) & set(existing), reverse=True)`
—— **只有同時出現在「待改」與「既有」兩集合之列被重寫**，其餘列之 XML
完全不被觸及。自後向前重寫以保持先前 offset 有效（`:195` 註解）。

新增列僅得 append 於最後一列之後；要求插入既有列之前即 raise
（`:209-214`），理由為「插入會位移其下每一列，此路徑刻意不能做」。

**(2) 未指定之 cell 是否保證不動 —— 程式碼保證，非偶然**

`_patch_row`（`:162-175`）：

```python
for m in CELL_RE.finditer(row_xml):
    idx = col_to_idx(m.group(1))
    cells[idx] = m.group(0)          # ← 原始 XML 片段，逐字保留
    ...
for col, value in edits.items():
    cells[col] = _cell_xml(...)      # ← 只有 edits 內之 col 被取代
return "".join(cells[k] for k in sorted(cells))
```

`cells[idx] = m.group(0)` 存的是**正則匹配之全文**，未在 `edits` 內者
原樣輸出。**此為程式碼保證。**

**一項副作用（非缺陷，但應知）**：輸出以 `sorted(cells)` 依欄序重組。
若來源 XML 之 cell 順序非遞增（罕見但合法），重組會改變位元組而語意
不變。該 member 屬 `patched`，故 `verify_structure` 第三層不會 raise。

**另**：`_patch_row` 保留來源 cell 之 `s="…"` 樣式屬性（`:170-171`）
並在改寫時沿用（`:173`），故格式不隨值變動而遺失。

**(3) `sharedStrings.xml` —— 設計上規避，不會誤報**

**此為 T3(2) 第 3 項之答案，且與所慮相反。** `_cell_xml` 之 docstring
（`:145-148`）逐字：

> Strings go out as inline strings: the source `sharedStrings.xml` is copied
> verbatim, so appending to it would mean rewriting it — the one member the
> surgical path most wants to leave alone.

實作（`:158-159`）：

```python
return (f'<c r="{coord}"{style_attr} t="inlineStr">'
        f'<is><t xml:space="preserve">{text}</t></is></c>')
```

**新字串以 `t="inlineStr"` 內嵌於 cell，不寫入 `sharedStrings.xml`。**
故該 member 不變動、不出現在 `members_patched`、**`verify_structure`
第三層不會誤報**。所慮之情形在設計上已被規避。

**此為本次評估中設計最刻意的一處**：它以「每個字串多佔一點空間」換取
「最不想動的那個 member 完全不動」。

**(4) x14 `<extLst>` —— 完全不被觸及**

`patch_sheet_xml` 只改兩處：受影響之 `<row>` 區塊（`:197-219`）與
`<dimension>`（`:221` → `_fix_dimension`）。`<extLst>`（x14:dataValidation
之所在）位於 `<sheetData>` 之外，**程式碼中無任何一處引用 `extLst`**
（全檔 grep 僅命中檔頭註解）。

**即 x14 節點之存活不是靠保護邏輯，而是靠「根本沒去碰它」** ——
這比主動保護更可靠，因為沒有可失效的保護邏輯。

**附帶**：`_fix_dimension`（`:224-234`）會重寫 `<dimension ref>` 為
patch 後之實際範圍。此使目標 member 之內容必然變動 —— 但該 member 在
`patched` 內，符合預期。

## 4. T4 — canon §10.3 獨立複驗

### 4.1 原文（`docs/runtime/ASPICE_SWE6_AI_Instruction.md:521-525`）

```
### 10.3 TC ID format
Pattern: `{project}-{abbr}-{NNN}` — alphanumeric project + alphanumeric module
abbreviation + zero-padded 3-digit sequence (e.g. `PROJ-DM-001`). IDs MUST be
monotonically increasing within the same `{project}-{abbr}` group; the
generator handles assignment, the LLM does not emit `tc_id`.
```

### 4.2 **分析層之引用漏了最後一句**

`04Z` §4 所引之原文止於 `within the same {project}-{abbr} group.`，
**未含分號之後的**：

> the generator handles assignment, **the LLM does not emit `tc_id`**.

該句非補充說明，是**規範性要求**，且直接對應執行層於 `04Z` 上繳
G-TM2 回報段所提之補充：

> tc_id 應由 `tc_id_format` 依位置賦予，非由生成端提供。

**該補充自此由「執行層提請」升為「canon 明文」。** G-TM2 項 3 之修法
須據此收緊：**tc_id 不得自 TC JSON 之 `tc_id` 鍵讀取**，且生成階段
之 prompt／context 不得要求 LLM 產出 `tc_id`。

執行層之 `build_batch_context.py`（未被覆蓋者）之輸出結構**未含 `tc_id`
欄位**，與本句相符；現存 `write_back.py` 之 `write_rows()` 走
`tc.get(key)` 迴圈，若 `feature.yaml` 之 `columns` 含 `tc_id`（R-TM34
已補），**會嘗試自 TC 資料讀取** —— 即與 canon §10.3 末句相違。
**此使 A-TM21(d) 之嚴重性提高**：不只是「欄位不會被寫入」，而是修法
若照最直覺的方式做（讓 TC JSON 帶 tc_id）會**違反 canon**。

### 4.3 R-TM32 三項判定 —— **全部支持**

| # | 待判 | 判定 | 依據 |
|---|---|---|---|
| 1 | `NR1L-TimeAndDate-{n:03d}` 符合 `{project}-{abbr}-{NNN}` | **支持** | 三段以 `-` 分隔；`{n:03d}` 即 zero-padded 3-digit |
| 2 | `TimeAndDate` 符合 alphanumeric module abbreviation，條文未限長度 | **支持** | 原文為 `alphanumeric module abbreviation`，無長度限制；`PROJ-DM-001` 前有 `e.g.`，為示例非上限 |
| 3 | 序號跨批連續不重設符合 monotonically increasing within same group | **支持** | 原文 `IDs MUST be monotonically increasing within the same {project}-{abbr} group`。本 feature 全 22 leaf 同屬 `NR1L-TimeAndDate` 一組，跨批重設會使序號非單調 |

**三項全部支持，不觸發「任一項不支持即停」。** `feature.yaml:50` 之
`tc_id_format` 無須修改。

## 5. T6(3) — 該驗而未驗者（五全集）

### 5.1 依全集 1（指令逐項）

T1–T5 全數完成。T4 之三項判定全部支持，未觸發停止條件。

### 5.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + 四處位置 | 40；:1149 / :1184 / :1209 |
| `ANOMALIES.md` | 條數 + 降級註記三處位置 | 21；:1212 / :1215 / :1225 |
| `scripts/` | mtime | 09:13–09:15，未動 |
| `backend/` | `git status` | 無輸出，未改 |

兩處 `str.replace` 前置 `assert` + `count==1`。

### 5.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **`diff_cells()` 與 `sheet_members()`** | **未讀** —— `surgical_save` 之另兩個組成。前者決定「哪些 cell 算變動」，後者決定「sheet 名 → zip member」之對映。**後者若錯，patch 會寫進錯的 member**，而 `verify_structure` 只驗「不該變的沒變」，不驗「該變的變對了地方」 |
| 2 | A-TM21 (a)(f) 之實跑證實 | 凍結中不執行 |
| 3 | `build_batch_context.py` 全文複查 | 執行層自寫，`04R` 起未重讀 |
| 4 | A-TM05 / A-TM10 之實跑 | 續掛 |
| 5 | PU 陽性對照 | 待 Pei 裁 |
| 6 | A-TM12 / A-TM19 | 併後續批次 |

**第 1 項為本包新識別，且值得優先**：`verify_structure` 三層皆為
「**不該變的沒變**」之驗證，**無一層驗「該變的變對了地方**」。
若 `sheet_members()` 之對映錯誤，patch 會寫進另一個 sheet 之 member，
而該 member 恰在 `patched` 內 → 三層全綠。

此與 A-TM21(a) 同構（欄位對映錯 → 結構檢查全綠），只是發生在 member
層而非 column 層。**成本低（同檔案內），未獲指派故未讀。提請下一包指派。**

### 5.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| `_dv_counts` 對母本得 sheet6 `(3,1)` | 其餘七個 sheet 得 `(0,0)` → 非一律回報非零 | 有 |
| x14 存活靠「沒去碰」 | 全檔 grep `extLst` 僅命中註解，非命中保護邏輯 | 有 |
| canon §10.3 三項全支持 | 同一複驗發現分析層引用漏一句 → 該複驗非一律確認 | 有 |
| `scripts/` 未被本包寫入 | 同期 `RULINGS.md` / `ANOMALIES.md` 確有寫入 | 有 |

### 5.5 依全集 5（設計說明之可驗性）

`04Z-A2` §1.1 之「移除 `check_other_sheets()`」取捨，其理由
（「保留更弱且被完全涵蓋之檢查只會製造兩道獨立防護之假象」）——
**執行層同意且無保留**：該函式若留著，日後 `verify_structure` 若被改動
或誤用，讀者會以為仍有備援，而實際上沒有。

§3 之「兩者皆為交付件不可逆風險之所在」—— **本包評估後確認**：
`_dv_counts` 為 R-G3 之執行點（母本 x14 下拉）、`patch_sheet_xml` 為
唯一寫入者。兩者皆已讀。**但 §5.3 第 1 項指出還有第三個同級風險點
（`sheet_members`）未在該句涵蓋範圍內。**

## 6. 本包未動之事項

未動 git（**未 push**；分支 ahead 14）。
**未寫入、未覆蓋、未修改 `features/time_management/scripts/` 任一行**
（mtime 為證）。**未修 A-TM21 任何一項。**
**未改 `backend/` 任何檔**（T3 唯讀，`git status backend/` 無輸出）。
未執行任何腳本。未生成任何 TC。未碰 `features/vehicle_setting/`。
未 rm 任何檔案。未送出 RD-1。未填 `D5`、未組 Scope 值。
未以 openpyxl 存回任何工作簿。未自行修改 G-TM2 之其餘各項。
