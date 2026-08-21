# 04Z — `04` 往返結案：六項缺陷登記、tc_id 欄位補、來源標記條文

分析層 → 執行層。覆核對象：`docs/upstream/04R_corrections.md`。**受理。**

T4 之全文評估是本輪最有產出的一步：**兩項 docstring 承諾了而實作沒有的
保護**，正是本 feature 一路在防的形態，而它們藏在一份「看起來已經寫好」
的檔案裡。

`scripts/` 仍凍結（A-TM20 未獲答覆），本包**不下放任何修改腳本之指令**。

---

## 1. §2.1 R-TM31 之自身盲區 —— 立為條文

執行層指出：列出明細只在**我方知道自己產出長什麼樣**時才足以歸屬；
本次能判定，靠的是 `Structure ported from` 這個**偶然存在**的字串。

**這比 R-TM31 本身更根本。** R-TM31 管「輸出要夠細」，但細到什麼程度
才夠，取決於產出物本身可不可辨識 —— 那是產出時就要決定的事，不是驗證時。

```
R-TM33（分析層自裁，2026-08-21）—— 產出物須帶可 grep 之來源標記

本 feature 產出之每一支腳本，其 docstring 首段須含一句可 grep 之來源
標記，形如：

    ported from <path> under R-TM29; authored by TC_Generator analysis
    round <NN>

使歸屬判定不依賴偶然字串。R-TM31 要求驗證輸出可歸屬，本條使該歸屬
成為可能 —— 兩條合用方完整。

適用範圍：腳本、資料檔（data/*.tsv、data/*.txt）之檔頭註解。
不適用於 TC 工作簿欄位（§1 語言規則，且交付件不帶內部標記）。

依據：04R 上繳 §2.1。本次之歸屬判定依賴 `Structure ported from`，
該字串為執行層偶然寫入而非刻意設計。
```

## 2. 六項缺陷 —— 登記，並確定哪些是 B1 前必修

執行層之六項全部成立。分析層之補充判讀：

**(a) 與 (b) 是同一形態，且是最嚴重的兩項** ——
`resolve_columns()` 之 docstring 逐字承諾「兩者不符即 raise」而實作只讀
字母、`ws` 與 `header_row` 兩參數完全未用；`check_other_sheets()` 宣稱
「逐位元相同」而只比對 member 名稱集合。

**讀 docstring 的人會以為保護存在。** 這比「沒有保護」更危險 ——
沒有保護時，下一個人會去加；假裝有保護時，沒有人會去加。

(a) 尤其要緊：它保護的正是 rev A/B → rev C 之欄位漂移
（`design_method` Q→R、`author` Z→AA），而那次漂移是本 feature 最早
抓到的實質錯誤之一。

**(c)+(d) 合起來是一個完整的斷鏈**：`TC_ID_FORMAT` 為模組常數不讀 yaml，
而 `write_rows()` 根本不寫 `tc_id`，且 `feature.yaml` 之 `columns` 無
`tc_id` 鍵。**三處各自看都像小問題，合起來是「Test Case ID 欄永遠不會
被寫入」。** §3 補其中之 yaml 一環。

```
A-TM21（PENDING，Tier 2 —— 凍結中不修，登記待歸屬裁定）

features/time_management/scripts/ 現存之 write_back.py（214 行）與
lint_tcs.py（301 行）經唯讀全文評估，六項實質缺陷：

(a) resolve_columns() docstring 承諾表頭複驗與不符即 raise，
    實作只讀 feature.yaml 之字母，ws / header_row 兩參數未使用。
    —— docstring 承諾而實作沒有，靜默失效第六例
(b) check_other_sheets() docstring 稱「逐位元相同」，實作只比對 zip
    member 名稱集合，內容被改寫而名稱不變則全綠。
    —— 同上，第七例
(c) TC_ID_FORMAT 為模組常數（None）且不讀 feature.yaml。R-TM32 已裁定
    且值已入 feature.yaml:49，write-back 仍會被 unresolved 檢查攔死
(d) write_rows() 不寫 tc_id；feature.yaml 之 columns 亦無 tc_id 鍵。
    合 (c) 即「Test Case ID 欄永遠不會被寫入」
(e) CONST_FUNCTIONAL_SAFETY 為死碼 —— 僅出現於定義與 unresolved 檢查，
    write_rows() 內未使用，填值亦不會進工作簿
(f) lint_required_fields() 只檢查鍵存在不檢查是否為空；base_tc() 為
    全空字串，故一條所有欄位皆空之 TC 會全綠通過

另一項強度差異（非缺陷，§3.6）：read_design_methods() 遍歷整個
`下拉選單` 分頁收詞彙，僅檢查非空。FORMS.md 實測 DV 來源為 $A$1:$A$9
恰九條；現實作讀到 8 條或 10 條皆不報錯。

(a)(b)(f) 為讀碼推得，凍結期間未實跑證實（04R §4.3 項 2）。
```

```
G-TM2（閘門，2026-08-21）—— B1 生成前之必修項與不得回退項

無論最終由哪一方持有 scripts/，下列須在 B1 生成前成立：

【必修】
1. A-TM21 (a) —— resolve_columns() 實作 docstring 所述之表頭複驗，
   或改寫 docstring 使其與實作相符。**不得留下承諾與實作不符之狀態。**
2. A-TM21 (b) —— check_other_sheets() 同上處置
3. A-TM21 (c)+(d) —— tc_id 自 feature.yaml 讀取並實際寫入 F 欄
4. A-TM21 (f) —— 必填欄位檢查須及於空值
5. read_design_methods() 加數量驗證（期望 9，取自 $A$1:$A$9）

【不得回退 —— 現存版優於被覆蓋版，須保留】
6. lint_spec_reference 驗物件 id 實際存在於 CFTS015 docx
   —— 被覆蓋之執行層版本無此閘門。Privacy R30-1 曾因偏移量推算 id
   而產生兩個錯誤 id，此閘門正為該形態而設
7. self-test 之紅綠雙向（綠向證明不誤報，紅向證明抓得到）
8. load_authorities 之「任何一項讀不到即 raise，不以預設值頂替」

【TODO 標記訂正】
9. TC_ID_FORMAT 之 TODO 撤除 —— R-TM32 已裁定
10. C 欄（Polarion ID）之 TODO 撤除 —— 非未定；SYS2 export 經 intake
    分類為 polarion_export，Part VII 明載其角色為錨鏈中介而非逐列 id 來源
11. Test Set 值域閘門之 TODO 撤除 —— framework Part VII 七組已由
    R-TM17 簽核（2026-08-20），可立即實作
12. priority 閘門之 TODO 拆分 —— **值域** P0–P3 為母本 P 欄 DV 內嵌，
    可自母本讀，非 TC 內容裁決；**分佈**才是內容裁決。兩者不得混為一談

G-TM1 之四項閘門仍全數有效，本條為其外加。
```

## 3. tc_id 欄位對映 —— 補 `feature.yaml`

`feature.yaml` 不在凍結範圍（凍結限於 `scripts/`），本包補其一環。

```
R-TM34（分析層裁定，2026-08-21）—— columns 補 tc_id

feature.yaml 之 workbook.columns 補：

    tc_id: "F"        # Test Case ID；R-TM34

依據：FORMS.md 之 rev C 母本實測欄位對映，F 欄為 Test Case ID
（Home 複本之 provenance warning 亦載「F 欄 216 列全填 tc_id」，
為同一欄之獨立佐證）。

本條只補欄位對映；實際寫入須待 A-TM21 (c)(d) 修畢（G-TM2 項 3）。
```

## 4. §4.5 之未驗項 —— 分析層即刻補驗，關閉

執行層記 R-TM32 之依據 1「canon §10.3」未驗。分析層複驗 canon 原文：

> §10.3 TC ID format —— Pattern: `{project}-{abbr}-{NNN}` — alphanumeric
> project + alphanumeric module abbreviation + zero-padded 3-digit
> sequence (e.g. `PROJ-DM-001`). IDs MUST be monotonically increasing
> within the same `{project}-{abbr}` group.

三項確認：

1. `NR1L-TimeAndDate-{n:03d}` 符合 `{project}-{abbr}-{NNN}` 之形
2. `TimeAndDate` 為 alphanumeric，符合「alphanumeric module abbreviation」
   —— 條文未限長度，範例之 `DM` 為示例非上限；privacy 之 `Privacy`
   為同一形態之既有實例
3. R-TM32 之「序號跨批連續不重設」符合「monotonically increasing within
   the same `{project}-{abbr}` group」

**依據 1 成立，R-TM32 三項依據全部經驗證。**

## 5. §4.3 項 1 —— `verify_structure()` 之保證範圍，本包指派

執行層未讀且**不代為聲稱**，正確。該函式在 `backend/`，唯讀無風險，
且它是否涵蓋 A-TM21(b) 之缺口，直接決定 (b) 之嚴重性等級 —— 本包指派。

---

## 6. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM33 / R-TM34 / G-TM2

標題行：

```
## R-TM33 — 產出物須帶可 grep 之來源標記
## R-TM34 — columns 補 tc_id
## G-TM2 — B1 生成前之必修項與不得回退項
```

內文為 §1 / §3 / §2 之區塊全文。
追加後 `## R-TM` 條數應為 **37**；`## G-TM` 條數應為 **2**。

### T2 — `ANOMALIES.md`：新增 A-TM21

內容為 §2 之區塊全文。索引追加：

```markdown
| A-TM21 | 現存 write_back.py / lint_tcs.py 六項實質缺陷 | PENDING | Tier 2（凍結中不修）|
```

索引條數 20 → **21**。

### T3 — `feature.yaml`：補 `tc_id`（R-TM34）

**改前先記 mtime 與 SHA256，改後再記** —— 併行者亦可能寫此檔（A-TM20），
兩次快照使覆蓋可被發現（R-TM31）。

```bash
shasum -a 256 features/time_management/feature.yaml
stat -f '%m %N' features/time_management/feature.yaml
```

於 `workbook.columns` 段內加：

```yaml
    tc_id: "F"        # Test Case ID；R-TM34
```

`assert old in text` + `count==1` + `replace(...,1)`，改後複查該行，
並再記一次 mtime 與 SHA256。

**不動 `scripts/` 任一檔。**

### T4 — `backend/` 之 `verify_structure()` 唯讀評估

讀 `backend/xlsx_surgical.py` 之 `verify_structure(src, out, members_patched)`
全文，回報：

1. 其**實際比對之範圍** —— 是否含未列於 `members_patched` 之 member
   之**內容**比對（非僅名稱）
2. 據此判定 A-TM21(b) 之缺口是否被涵蓋：**完全涵蓋 / 部分 / 未涵蓋**
3. 若涵蓋，A-TM21(b) 之嚴重性降為「docstring 與實作不符」而非
   「保護缺失」—— 兩者之處置不同（前者改 docstring 即可，
   後者須補實作）。**依 R-TM31 附程式碼位置與片段，不只結論。**

**只讀 `backend/`，不改。**

### T5 — 驗證（依 R-TM31，列明細）

```bash
grep -n '^## R-TM3[34]' features/time_management/RULINGS.md
grep -n '^## G-TM2'     features/time_management/RULINGS.md
grep -n '^| A-TM21'     features/time_management/ANOMALIES.md
grep -n 'tc_id'         features/time_management/feature.yaml
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 37
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 21
ls -l --time-style=+%H:%M features/time_management/scripts/ 2>/dev/null \
  || stat -f '%Sm %N' -t '%H:%M' features/time_management/scripts/*
```

末項期望：三支之 mtime 仍為 **09:13 / 09:14 / 09:15**（凍結未破）。
**改用 mtime 而非 `git status`** —— 後者對 untracked 目錄恆列一行，
無法區分「未寫入」與「未追蹤」（04R §1.1 已證）。

### T6 — 上繳

`docs/upstream/04Z_corrections.md`。須含 T5 全部輸出、T3 之兩組
mtime/SHA256、T4 之三項評估、**本包是否仍有該驗而未驗者之獨立判斷**
（明列全集）。

### 不得執行者

- 不動 git
- **不寫入、不覆蓋、不修改 `features/time_management/scripts/` 任一行**（A-TM20）
- 不修 A-TM21 之任何一項（凍結中）
- 不改 `backend/` 任何檔（T4 只讀）
- 不執行任何腳本（含 `--self-test`）
- 不生成任何 TC
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 7. 呈報 Pei —— 同一個問題，第二次

**`features/time_management/` 由哪一個 session 負責？**

本輪又多了具體代價：現存兩支腳本有六項實質缺陷，其中兩項是
**docstring 承諾了而實作沒有的保護**。這些要修，但**凍結中我不下放
修改指令** —— 歸屬未定時修了同樣會被覆蓋，而且這次會覆蓋掉修正。

我需要的仍是一句：**本 session 繼續，還是交給另一個 session。**

- 本 session 繼續 → 請停用另一邊對此 feature 之作業，我下放 G-TM1 + G-TM2
  共十二項之修改指令
- 交給另一邊 → 我把 G-TM1、G-TM2、R-TM32/34、五條界線、A-TM13 缺口
  整理成交接單，本 session 轉唯讀覆核

`05`（B1 生成）在此之前不下放。

其餘待你之項（不阻塞）：R-TM10-A1 替代樣式來源（仍無候選）、
RD-1 Q-TM1–3 送出、A-TM18 Comfort 之 (a)/(b) 判定。

## 8. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM33 | 分析層自裁，來源標記 | §1 | ✅ T1 |
| R-TM34 | 分析層裁定，columns 補 tc_id | §3 | ✅ T1 + T3 |
| G-TM2 | 閘門，十二項 | §2 | ✅ T1 |
| A-TM21 | anomaly，PENDING，Tier 2 | §2 | ✅ T2 |
| R-TM32 依據 1 補驗 | 已驗，關閉未驗項 | §4 | 無需指派（分析層已完成）|

分析層本包未動 git、未改任何腳本、未觸 `scripts/`、未觸 `vehicle_setting/`。
