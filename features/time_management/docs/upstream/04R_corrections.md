# 上繳 04R — R-TM31/32、G-TM1、A-TM20 落檔，現存兩支腳本唯讀全文評估

執行層 → 分析層。對應 `docs/handoff/04R_review.md`。2026-08-21。

T1–T5 全數完成。**T4 之全文評估發現六項現存版之實質缺陷，其中兩項是
docstring 承諾了而實作沒有的保護** —— 即本 feature 一路在防的靜默失效
形態。另發現 **TODO 標記兩處不恰當**（標為待決而其實已裁）。

同時如實記錄：現存版有三項**優於執行層被覆蓋之版本**者，見 §3.4。

---

## 1. T5 驗證（依 R-TM31，全部列明細）

```
1. R-TM31 / R-TM32   RULINGS.md:940 / RULINGS.md:969
2. G-TM1             RULINGS.md:997
3. A-TM20 索引        ANOMALIES.md:32  | A-TM20 | 併行者寫入本 feature… | PENDING | Tier 3（呈 Pei）|
4. tc_id_format      feature.yaml:49   tc_id_format: "NR1L-TimeAndDate-{n:03d}"   # R-TM32
5. R-TM 條數          35   期望 35   OK
6. A-TM 條數          20   期望 20   OK
```

### 1.1 判準 7 之輸出與期望不符 —— 但非凍結被破壞

`04R` T5 期望 `git status --short features/time_management/scripts/`
**無輸出**。實際輸出：

```
?? features/time_management/scripts/
```

**成因非寫入，而是該目錄從未進入 git**（整個 `scripts/` 為 untracked，
故 `git status` 恆列一行）。判準本身無法區分「未寫入」與「未追蹤」。

**改以 mtime 為凍結之獨立佐證**（依 R-TM31 之精神：輸出須足以判斷歸屬）：

```
Aug 21 09:13  lint_tcs.py
Aug 21 09:14  write_back.py
Aug 21 09:15  build_batch_context.py
```

三者之 mtime 皆停在覆蓋當時（09:13–09:15），**本包全程未動**。
本包對該目錄之全部動作為 `cat` / `grep` / `wc` / `ls`。

## 2. T1–T3 寫入確認

| T | 內容 | 位置 |
|---|---|---|
| T1 | R-TM31、R-TM32 逐字 | `RULINGS.md:940`、`:969`；33 → **35** |
| T2 | A-TM20 + 索引列 | `ANOMALIES.md:32`；19 → **20** |
| T2 | G-TM1（G-series 同檔） | `RULINGS.md:997` |
| T3 | `tc_id_format` | `feature.yaml:49`，置於 `tc_ref_id_value` 之後 |

### 2.1 R-TM31 之一項自身盲區（執行層補記於該條回報段）

本條要求「列出位置或片段」以便歸屬。但**列出明細只在我方知道自己產出
長什麼樣時才足以歸屬** —— 本次能判定，靠的是執行層版本帶有特徵字串
`Structure ported from`，而該字串是**偶然存在的，非刻意設計**。

執行層自訂之對應作法：凡本 feature 產出之腳本，docstring 首段須含一句
可 grep 之來源標記（形如 `ported from <path> under R-TM29`），使歸屬
判定不依賴偶然。**本次未及套用於已被覆蓋之兩支。**

## 3. T4 — 現存兩支腳本唯讀全文評估

**已讀完兩支全文**（`write_back.py` 214 行、`lint_tcs.py` 301 行）。
未改任一行、未執行。

### 3.1 六項實質缺陷

**(a) `write_back.py:resolve_columns()` —— docstring 承諾表頭複驗，實作沒有**

docstring 逐字：

> 欄位以 `feature.yaml` 之字母宣告解析，並以表頭文字複驗。
> **兩者不符即 raise** —— rev A/B/C 之欄位不同（remarks AG vs AH），
> 僅憑字母或僅憑表頭皆可能取到錯欄。

實作全文（`write_back.py:96-104`）：

```python
letters = cfg["workbook"]["columns"]
out: dict[str, int] = {}
for key, letter in letters.items():
    idx = openpyxl.utils.column_index_from_string(letter)
    out[key] = idx
return out
```

**只讀字母，無任何表頭比對，無 raise，`ws` 與 `header_row` 兩個參數
完全未使用。** docstring 所述之保護不存在。

嚴重性：這正是 rev A/B → rev C 漂移所需之保護（`design_method` Q→R、
`author` Z→AA）。`feature.yaml` 現值雖已由 recon 複驗過（`col_conflicts:
none`），但該保護是為「日後 yaml 與實例再度分歧」而設 —— 此刻它不存在，
且讀 docstring 者會以為它存在。**與 A-TM03 / A-TM06 / A-TM08 / A-TM10
同族之靜默失效，第六例。**

**(b) `write_back.py:check_other_sheets()` —— 名不符實**

docstring：「目標分頁以外之 zip member 須**逐位元相同**」。
實作（`:135-139`）：

```python
za, zb = zipfile.ZipFile(src), zipfile.ZipFile(out)
if set(za.namelist()) != set(zb.namelist()):
    raise StructureError("zip member 清單改變")
```

**只比對 member 名稱之集合，不比對任何內容。** 一個 member 之內容被
改寫而名稱不變，此檢查全綠。函式名與 docstring 皆宣稱做了內容比對。

（附帶：`verify_structure(src, out, members_patched)` 在其後被呼叫，
可能涵蓋部分保護；但該函式之保證範圍執行層未讀，不代為聲稱。）

**(c) `write_back.py:TC_ID_FORMAT` 為模組常數，不讀 `feature.yaml`**

```python
TC_ID_FORMAT = None       # TODO(R-TM10-A1)
```

`run()` 之 `unresolved` 檢查（`:171-178`）會因其為 `None` 而
**拒絕寫入**。R-TM32 已裁定且值已入 `feature.yaml:49`，但該支**不讀
該鍵**，故 R-TM32 落檔後 write-back **仍會被攔死**。

**此為 T4(3) 之答案**：顯式攔截**有**，但攔的對象是模組常數而非 yaml 鍵。

**(d) `write_back.py:write_rows()` 不寫 `tc_id`**

`cols` 來自 `cfg["workbook"]["columns"]`，而本 feature 之 `feature.yaml`
**無 `tc_id` 鍵**（僅 `req_id`…`remarks` 十五項）。故 F 欄（Test Case ID）
不會被寫入任何值，且 `TC_ID_FORMAT` 縱使有值亦無處使用。

**(e) `write_back.py:CONST_FUNCTIONAL_SAFETY` 為死碼**

該常數僅出現於定義處與 `unresolved` 檢查，`write_rows()` 內未使用 ——
`functional_safety` 之值走 `tc.get(key)` 自 TC 資料取。即使日後填入常數
亦不會被寫進工作簿。

**(f) `lint_tcs.py:lint_required_fields()` 只檢查鍵存在，不檢查是否為空**

```python
if key not in tc:
    out.append(("required-fields", f"{where}: 缺欄位 `{key}`"))
```

其 `base_tc()` 為 `{k: "" for k in auth["columns"]}` —— **全部欄位皆空
字串**，而 self-test 之綠向期望「無發現」。即**一條所有欄位皆為空字串
之 TC 會全綠通過**。

### 3.2 G-TM1 四項逐項判定（依 R-TM31 附位置證據）

| # | 閘門 | 現存版 | 證據 |
|---|---|---|---|
| 1 | D5 Scope 守衛 | **無** | `grep -n 'D5' write_back.py lint_tcs.py` → 零命中 |
| 2 | leaf 來源隔離 | **無** | `grep -n 'leaf_descriptions' *.py` → 零命中。`lint_required_fields` 僅檢查欄位鍵，未驗 `req_id` 屬 22 筆全集 |
| 3 | spec gap（A-TM13） | **無** | `grep -n 'A-TM13\|spec.gap\|6151328' *.py` → 零命中 |
| 4 | 界線（R-TM23/25） | **無** | `grep -n 'R-TM23\|R-TM25\|boundary\|DateTmFormat' write_back.py lint_tcs.py` → 零命中 |

**四項於 lint 層全缺。** 惟第 3、4 項於 `build_batch_context.py`
（執行層版，未被覆蓋）之 `SPEC_GAP` 與 `BOUNDARIES` 兩表有編碼 ——
但依 G-TM1 之明文，context 層不能取代 lint 層。

### 3.3 TODO 標記逐處判定（T4(1)）—— **兩處不恰當**

`write_back.py` 六處：

| 位置 | 標記 | 判定 |
|---|---|---|
| `CONST_FUNCTIONAL_SAFETY` | TODO | **恰當** —— 確為內容裁決；037 無 ASIL/FTTI 欄，亦不可自 RD 導出 |
| `PLACEHOLDER_BODY` | TODO | **恰當** —— 措辭屬 TC 內容 |
| `TC_ID_FORMAT` | TODO | **已不恰當** —— R-TM32 已裁定（2026-08-21），值已入 `feature.yaml:49`。應改為讀 yaml，非續標待決 |
| `C (Polarion ID)` | TODO「本 feature 有無 Polarion 匯出未定」 | **不恰當** —— SYS2 export 經 intake 分類為 `polarion_export`，且 Part VII 明載其為「錨鏈中介」。非未定，是已知其角色非逐列 id 來源 |
| `Q (Estimated Test Time)` | TODO | **恰當** —— rev C 新增欄，無任何條文賦值 |
| `T–Z (Vehicle Model)` | TODO | **恰當** —— 無條文 |

`lint_tcs.py` 四處：

| 標記 | 判定 |
|---|---|
| 步驟措辭閘門 | **恰當** —— 詞彙與門檻屬 TC 內容 |
| **Test Set 值域閘門「待本 feature 之 framework 定案」** | **不恰當** —— framework Part VII 之七組**已由 R-TM17 簽核**（2026-08-20），非待定。此閘門可立即實作 |
| **priority 分佈閘門「待本 feature 之條文決定」** | **部分不恰當** —— **值域** P0–P3 為母本 P 欄 DV 內嵌（非 TC 內容裁決），可自母本讀；**分佈**才是內容裁決。兩者被混為一談 |
| Input Test Data 填法 | **恰當** |

### 3.4 現存版優於執行層被覆蓋版本者（三項，如實記錄）

分析層 §5 指出「不能預設我方版本較好」。逐項核對後確認三項：

1. **`lint_spec_reference` 驗物件 id 實際存在於 CFTS015 docx** ——
   執行層版本**無此閘門**。其 `read_spec_objects()` 每次執行重讀 docx，
   docstring 並註明 Privacy R30-1 曾因偏移量推算 id 而產生兩個錯誤 id。
   **這是執行層版本缺少的一項實質保護。**
2. **self-test 為紅綠雙向**（綠向證明不誤報、紅向證明抓得到）。執行層
   版本之八案例以紅向為主，綠向僅一例。
3. **`load_authorities` 之「任何一項讀不到即 raise，不以預設值頂替」**
   有明文 docstring 並實作於五處讀取。

### 3.5 T4(4) — 他 feature 之 TC 內容常數：**未發現**

逐項檢查 R-TM29 界線所列四類：

| 類別 | 現存兩支 |
|---|---|
| 步驟措辭常數 | 無（`STEP_VERBS` 一類完全不存在）|
| ER 樣板字串 | 無 |
| Test Set 值 | 無（標 TODO，未寫入任何值）|
| priority 預設 | 無 |

三個內容常數（`CONST_FUNCTIONAL_SAFETY` / `PLACEHOLDER_BODY` /
`TC_ID_FORMAT`）皆為 `None`，未繼承 Privacy 之 `"NA"`、
`"BLOCKED - see Remarks"`、`"NR1L-Privacy-{n:03d}"`。

**R-TM29 界線遵守良好，無發現須回報之繼承。**

### 3.6 一項額外觀察 —— `read_design_methods` 無數量驗證

`lint_tcs.py:93-113` 遍歷 `下拉選單` **整個分頁之所有列所有欄**，
收「含 `(` 與 `)`」之字串為詞彙，僅檢查 `if not vals` 非空。

FORMS.md 實測該分頁 dimensions 為 `A1:A11`，A10/A11 為空，
DV 來源為 `$A$1:$A$9` —— **恰九條**。現實作若讀到 8 條或 10 條皆不報錯。

**與 R-TM21 之精神有落差**：閘門之權威來源本身無數量驗證，則權威缺一條
時閘門仍全綠。執行層版本讀 `A1:A9` 並對任一空值 raise。

**非缺陷，是強度差異**，故列於此而非 §3.1。

## 4. T6(3) — 該驗而未驗者（五全集）

### 4.1 依全集 1（指令逐項）

T1–T5 全數完成。T5 判準 7 之輸出與期望不符，成因已查明（§1.1），
非凍結被破壞。

### 4.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + R-TM31/32/G-TM1 位置 | 35；940 / 969 / 997 |
| `ANOMALIES.md` | 條數 + A-TM20 索引位置 | 20；:32 |
| `feature.yaml` | `tc_id_format` 位置與值 | :49，逐字相符 |
| `scripts/` | **mtime**（非 git status）| 09:13–09:15，未動 |

三處 `str.replace` 全部前置 `assert` + `count==1`。

### 4.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **`verify_structure()` 之保證範圍** | 未讀。§3.1(b) 之 `check_other_sheets` 缺口是否被其涵蓋，**執行層不代為聲稱**。屬 `backend/`，讀之無風險，未獲指派 |
| 2 | 兩支腳本之實際執行（含 `--self-test`） | 明令不執行。故 §3.1(f) 之「全空字串 TC 全綠」為**讀碼推得**，未經實跑證實 |
| 3 | `build_batch_context.py` 之全文複查 | **執行層自己所寫，本包未重讀**。其 `SPEC_GAP` / `BOUNDARIES` 兩表之內容正確性已於 T3 錨點複驗間接支持，但該支之其餘部分未再驗 |
| 4 | A-TM05 / A-TM10 之實跑 | 續掛（需 drop folder 素材）|
| 5 | PU 陽性對照 | 待 Pei 裁 |
| 6 | A-TM12 / A-TM19 | 併後續批次 |

**第 2 項須說明**：§3.1(f) 與 §3.2 之判定**全部由讀碼推得**。凍結期間
不執行是正確的，但這使本節之結論在強度上低於實跑驗證。若日後解凍，
`lint_tcs.py --self-test` 之綠向應會暴露 §3.1(f)。

### 4.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| G-TM1 四項於 lint 層全缺 | 同一 grep 對 `下拉選單`（8 處）、`self_test`（6 處）皆命中 → 掃描有效 | 有 |
| 未發現他 feature 內容常數 | 同一檢查於 Privacy 原檔命中 `"NA"` / `"BLOCKED - see Remarks"` | 有 |
| `scripts/` 未被本包寫入 | mtime 停在 09:13–09:15，而本包其餘產出之 mtime 為稍後 | 有 |

### 4.5 依全集 5（設計說明之可驗性）

`04R` §3 之 R-TM32 三項依據：

| 依據 | 本包 |
|---|---|
| canon §10.3 之 `{project}-{abbr}-{NNN}` | **未驗** —— 未讀 canon §10.3 原文 |
| privacy 為 `NR1L-Privacy-{n:03d}` | **已驗** —— `features/privacy/feature.yaml` 實測相符 |
| module 段取 `TimeAndDate` 而非 `TimeManagement` | **已驗**（推理層）—— 與 R-TM1 / R-TM8 之內部識別 vs 交付識別區分一致 |

第一項未驗不影響結論（後二項獨立支持），但如實記錄。

## 5. 本包未動之事項

未動 git。**未寫入、未覆蓋、未修改 `features/time_management/scripts/`
任一行**（A-TM20 凍結；mtime 為證）。**未執行任何腳本**（含 `--self-test`）。
未生成任何 TC。未碰 `features/vehicle_setting/`。未 rm 任何檔案。
未送出 RD-1。未填 `D5`、未組 Scope 值。未以 openpyxl 存回任何工作簿。
未自行移除現存版之任何標記或常數。
