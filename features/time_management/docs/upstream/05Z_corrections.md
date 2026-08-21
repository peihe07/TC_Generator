# 上繳 05Z — canon 三節落實，self-test 21/21；**並更正一項我反覆引用三輪之錯誤**

執行層 → 分析層。對應 `docs/handoff/05Z_canon_adoption.md`。2026-08-21。

T1–T8 全數完成，self-test **21/21** 實跑通過。

**但本包最要緊的不是這些 —— 是 §1 之更正。**

---

## 1. **更正：`build_batch_context.py` 亦已被覆蓋，我三輪之陳述皆錯**

### 1.1 我說過什麼

`04Z-A2` 上繳 §5.2 之歸屬表，我寫：

| 腳本 | 執行層所寫 | 現存 | 特徵字串 |
|---|---|---|---|
| `build_batch_context.py` | 222 行，英文 | 222 行，英文 | **1（執行層）** |

並據此在 `04Z-A2` §3.2、`04Z-A3`、`05`、`05R` 四處反覆聲稱：

> 現存之 `build_batch_context.py`（執行層版）已含 `SPEC_GAP` 與
> `BOUNDARIES` 兩表，故 G-TM1 項 3、4 在 context 層有編碼，僅 lint 層缺。

### 1.2 實測 —— 三處版本全部相同，且皆非執行層之產出

| 位置 | SHA256（前 16） | 行數 |
|---|---|---|
| `data/scripts_snapshot_20260821/`（09:15:18 保全） | `7344b995d0b4faf2` | 171 |
| git HEAD（`3d3c126` 所收） | `7344b995d0b4faf2` | 171 |
| 工作樹（本包加來源標記後） | `4fea08592b1c7063` | 173（＝171＋2） |

```
grep -c 'Structure ported under' → 0      （執行層版之特徵字串）
grep -c 'SPEC_GAP'               → 0
grep -c 'BOUNDARIES'             → 0
docstring 第 2 行                 → """Step 4 (Time Management) — B1 之上下文產生器。
                                    （執行層版為 """Step 2 (Time and Date) — assemble …）
```

**結論：三支腳本全部被覆蓋，不是兩支。** `SPEC_GAP` 與 `BOUNDARIES`
兩表**從未存在於任何已保存之版本中** —— 快照保全的是覆蓋後之狀態。

### 1.3 我錯在哪裡

`04` 輪之判定依據為 `grep -c 'Structure ported under'` 得 1。
**該結果與現存快照（09:15:18）不符**，而快照之 mtime 早於我執行 grep 之時。
最可能之解釋：我 grep 之時該檔尚未被覆蓋，覆蓋於數秒後發生；
**但我此後未再複查，而快照與 commit 都在覆蓋之後。**

**這正是 A-TM15 之同型失誤，且我當時親自定性過**：

> 完成動作後未確認結果仍然成立。前二者是未驗證前提，本例是未驗證後果。

我在 `03Z-A1` 上繳如此描述自己在 01 包之失誤，然後在 `04` 輪犯了同一個。
**差別在於這次它被我引用了三輪，成為後續判斷之基礎。**

### 1.4 實質後果 —— 兩項

**(a) A-TM20 之歸屬記載須更正**：三支腳本皆非本 session 之產出，
非「兩支非、一支是」。

**(b) context 層之編碼不存在，而 G-TM1 曾以其為據**：

G-TM1 明訂「context 層之編碼不能取代 lint 層 —— 前者是給生成看的，
後者是驗生成的」。**反向亦然**：lint 層不能取代 context 層。

現況為 lint 層有 B3（spec gap）與 B4（界線）而 **context 層兩者皆無**。
即 **B1 生成時，模型不會收到 A-TM13 之缺口指示與五條界線之指示**，
只會在生成後被 lint 攔下。

**執行層未自行補回** —— context 層之內容設計屬 `06`（B1 生成包）之範圍，
且現存版之結構與執行層原版不同，補回需重新設計而非還原。
**提請於 `06` 指派。**

### 1.5 未被此錯誤影響者

- **階段 A（`write_back.py` 六項）**：其修改基於實讀全文，非基於歸屬判定
- **階段 B（`lint_tcs.py` 八項）**：同上
- **A-TM21 之六項缺陷**：基於 `04R` T4 之唯讀全文評估，該評估讀的是
  現存版本身，與歸屬無關

---

## 2. T8 驗證（R-TM31 列明細；R-TM46 增量 + 前後實測值）

```
R-TM48  RULINGS.md:1770      R-TM49  RULINGS.md:1802
R-TM9-A2 處置訂正 RULINGS.md:1707      R-TM41 處置訂正 RULINGS.md:1737
A-TM23  ANOMALIES.md:35   **RESOLVED**（canon §10.7(a)）
PENDING: DR- 錨對照 DATA_REQUESTS.md:102 / :109 / :110
N-TM1   RD1_questions_time_management.md:65
lint_d5_scope 呼叫 lint_tcs.py:687，early return 於 :689  → **在其之前**
三支腳本來源標記  build_batch_context.py:1  lint_tcs.py:1  write_back.py:1
候選表 v2 檔頭    含 R-TM33 來源標記與排列規則說明

條數（前 → 後，增量）
  ## R-TM   50 → 52   +2   期望 +2   OK
  ## G-TM    3 →  3   +0   期望 +0   OK
  ## A-TM   24 → 24   +0   期望 +0   OK
```

## 3. T2 — DR 號碼：**復用兩筆，新增一筆**

`05Z` T2 表列三筆，**其中兩筆已於既有 DATA_REQUESTS 登記**：

| 缺件 | DR 號 | 狀態 |
|---|---|---|
| 037 正式報告 | **DR-2**（既有，`01` 往返登記） | 復用 |
| CFTS015 缺件物件 6151328 / 6151331 | **DR-5**（既有，`01R` 往返登記） | 復用 |
| CAN 網段依據（DBC / 架構文件） | **DR-6** | **本次新增** |

**未另立新號之理由**：同一缺件若有兩個 DR，`PENDING: DR-{n}` 佔位之指向
即不唯一 —— 而該佔位之全部價值就在於「直接指向缺件之登記處」。

已於 `DATA_REQUESTS.md` 建「`PENDING: DR-{n}` 之錨對照」表，
並記 canon §8.4.3 之 `NA` 界線（`input_test_data` 之 `NA` 屬「確認不適用」
仍合法，與「缺件」不得混用）。

## 4. T6 — 三項調整與 red-green（21/21 全數實跑）

| # | 動作 | red-green |
|---|---|---|
| L1 | `lint_d5_scope` 移至 early return 之前 | 見下 |
| L2 | B1 判準改「未含 `PENDING: DR-`」；B3 同 | 紅 ×2、綠 ×1 |
| L3 | B2 加 test_item 兩項（缺括號、上半 > 50 token） | 紅 ×2 |

**新增之四個案例（實跑輸出）**

```
PASS 紅向 spec-gap        (L2：Remarks 有值但非 PENDING 佔位):
     SWE-RA-TIME&DATE-002 之 Remarks 未含 `PENDING: DR-` 佔位…
PASS 紅向 test-item-shape (L3：缺下半括號):
     test_item 缺下半之 `(...)` 測試目的。canon §4.3.1：缺括號下半 = FAIL
PASS 紅向 test-item-shape (L3：上半 51 token 未摘句):
     test_item 上半 51 token，超過 canon §4.3.1 之上限 50。須摘句…
PASS 綠向 2 (A-TM13 leaf 帶 PENDING 佔位): 未誤報 spec-gap
PASS B1 D5 守衛: D5（範圍 Scope）為**空**。canon §8.4.3…須寫 `PENDING: DR-{n}`

自驗：21 / 21
```

**綠向 2 為本次新增之刻意設計**：確認 B3 在「Remarks 已依 canon §8.4.3
帶合規佔位」時**不誤報**。若無此案例，B3 可能寫成「只要是 A-TM13 leaf
就報」而永遠無法通過 —— 與 `05R` 之 `remarks` 誤列必填同型。

**L1 之連帶行為改變**：`generated/` 為空時不再直接 `return 0`，改為印出
工作簿層之發現後，依「是否含 `spec-scope-pending` 以外之項」決定 exit code。
即 D5 為佔位時 exit 0（待決狀態不算失敗），D5 為空或有誤值時 exit 1。

## 5. T5 — 候選表 v2

`data/spec_reference_candidates_v2.txt`，依 canon §10.7 排列段：

```
SWE-RA-TIME&DATE-001
    CFTS015-4813919, 4813920, 4813984, 4814069
SWE-RA-TIME&DATE-002
    CFTS015-4813922, 4813939, 4814075, 4814085, 4814087
    PENDING: DR-5 CFTS015 缺件物件 6151331
SWE-RA-TIME&DATE-005
    CFTS015-4813936
    PENDING: DR-5 CFTS015 缺件物件 6151328
```

**前綴僅一次、升冪、無 `;`**。A-TM13 兩片之缺件依 R-TM41 處置訂正
改填 `PENDING: DR-5`，**不留空**。

**`-005` 之形態值得注意**：一個真值 + 一個佔位。佔位**不取代真值，
只補缺口**（已記入 R-TM41 之回報段）。

v1 原檔**未改**，保留為軌跡（R-TM13）。

## 6. T9(4) — 該驗而未驗者（五全集）

### 6.1 依全集 2（寫入後複查）—— **本包強化此項**

`04` 輪之失誤（§1）成因為「寫入後未複查」之延伸：**判定後未複查**。
本包起，凡涉及「某檔之歸屬或內容狀態」之判定，一律於**該包上繳前**
重新實測一次，不沿用同一 session 稍早之結果。

本包之複查：

| 檔案 | 複查方式 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + 四處位置 | 52；:1707 / :1737 / :1770 / :1802 |
| `ANOMALIES.md` | 條數 + A-TM23 狀態 | 24；RESOLVED |
| `DATA_REQUESTS.md` | DR-6 + 錨對照三列 | :20 / :109 / :110 |
| `lint_tcs.py` | `py_compile` + self-test 21/21 + L1 位置 | 通過 |
| **三支腳本之歸屬** | **SHA256 三方比對** | **§1 之更正即由此而來** |

### 6.2 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **context 層之 A-TM13 / 界線編碼** | §1.4(b)。**現不存在**，提請 `06` 指派 |
| 2 | A-TM24 `functional_safety` 之值 | 來源 1 已否定，待 Pei |
| 3 | R-TM49 例外條款之判準 | 「確認其為該訊號之網段而非上下文提及者」之可操作判準未定，已於 R-TM49 回報段提請 |
| 4 | R-TM47 之寫入（Part VII `Workbook sync`） | `05Z` 明令暫不動全域檔 |
| 5 | canon §8.7.5 對 B4 之影響 | `05Z` §2.3 已裁定 B4 用法不變（偵測用，非記法），**但 TC 內容之三件組寫法待 `06`** |
| 6 | 完整 lint 路徑（有 TC 時） | `generated/` 仍空 |
| 7 | `surgical_save` 寫入路徑 | 仍從未執行 |
| 8 | R-TM10-A1（步驟措辭、ER 樣板） | 仍無候選 |

### 6.3 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| 21 項 self-test 全過 | `05R` 首次為 16/17（綠向失敗）→ 該測試非一律全綠 | 有 |
| 三支腳本皆非執行層產出 | 同一 grep 對 `lint_tcs.py` / `write_back.py` 之來源標記命中 1 → 檢查有效 | 有 |
| 快照 = git = 工作樹（除來源標記） | 三者 SHA 前二者相同、第三者僅差 2 行 | 有 |
| S 欄無 DV（`05R` T3） | 同一解析對 P/R/T–Z/AF 命中 | 有 |

### 6.4 依全集 5（設計說明之可驗性）

`05Z` §2 之 R-TM48 三項生效依據，執行層逐項核對：

| 依據 | 判定 |
|---|---|
| 1. charter 明訂 repo 版為權威 | **未獨立複驗** —— 未讀 charter 原文，沿用分析層陳述 |
| 2. §4.3.1 / §8.4.3 與 Pei 既有直接指示一致 | **無法複驗** —— 執行層不掌握聊天層之歷史指示 |
| 3. 三節皆為收緊 | **已驗**：逐節確認為增加約束（見 R-TM48 回報段） |

**第 1 項可驗而未驗**（charter 在 `docs/runtime/OPERATING_CHARTER.md`，
唯讀無風險）。未獲指派故未讀。**若第 1 項不成立，R-TM48 之生效依據僅剩
第 3 項（不對稱論證），該論證雖成立但強度較弱。**

## 7. 本包未動之事項

未動 git。未生成任何 TC。未改 `backend/`、未改 canon、未改
`docs/fw036/framework.md`。**未修改 `data/spec_reference_candidates.txt`
原檔**。未將 `CFTS015-6151328` / `-6151331` 寫入任何欄位。
**未填 `functional_safety` 之值**。**未杜撰任何 CAN 網段**。
未碰 `features/vehicle_setting/`。未送出 RD-1。
**未自行補回 context 層之 SPEC_GAP / BOUNDARIES 編碼**（§1.4(b)）。
未動 `TODO(R-TM10-A1)` 之步驟措辭常數與 ER 樣板。
