# 16 — Comfort HMI / 寫回執行：三段逐驗，止於 Excel 確認前

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 24（R-C28）＋ 25（列高裁定、pilot 定案、寫回授權）
- 結果：**§3.1 前置 gate 5 項全 PASS，§3.2 splice 完成，§3.3 assertion 9 項全 PASS。**
  產出 `…_Comfort_20260815_pilot.xlsx`，SHA256 `b4ad82c2487a38c0…`。
  **已停下，等 Pei 於 Excel 執行四項確認。**

---

## 1. 條文與文件（24 §4.1／§4.2／§4.3、25 §1）

### 1.1 R-C28 貼入，R-C25 旁註

`RULINGS.md` 現有 30 個逐字條文區塊（R-C1…R-C28 ＋ R-C4-1、R-C5-1）。
R-C28 原文貼入。**R-C25 原文一字未改**，於其區塊上方加一段 `>` 旁註：

> **旁註（24 §1，2026-08-15）**：本條之兩問即 **R-C28** 之第二、三問。
> R-C28 於其前補「第一問：出處」——「該事實在其標註來源節之 full_text
> 有無明文對應」。**本條原文不改寫**；兩者並存，R-C28 為完整判準。

### 1.2 RUNBOOK 之兩類違反對照表

| | 前四次（TC-001 PC4、TC-004 PC2、TC-005、TC-014 PC3） | 第五次（TC-007 PC2） |
|---|---|---|
| 失敗於 R-C28 之 | 第三問（落點） | **第一問（出處）** |
| 違反 | §4.5／§4.4 | **§7 FF／§8.4.1** |
| 性質 | 事實為真，欄位放錯 | **事實無來源** |

置於既有之「判準 vs 用詞禁令」一節旁 —— 兩者同一主題：**以表徵為判準者，
其失敗形態是靜默的。**

### 1.3 profile §3.2 指向 R-C28

新增一段，含「**此為 Phase 4 展開之前置，非預防性建議 —— pilot 之 TC-007
即栽在此處**」與「第一問之回答須具名條文之相關句」兩句。

---

## 2. 列高「需行數」欄之加註（24 §4.4）

上繳 14 §4 與 15 §4 之列高表格上方各加一段：

> 算法：`ceil(len(該欄文字) / 欄寬)` 逐行加總，取 I/J/L/M/AH 之最大。
> **未計字型、比例字寬、CJK 全形**，故為粗估。
> **跨檔不可比**：home 之 row 135 估 77 行，其實際列高 78pt（約 5–6 行文字）
> —— 該檔 I 欄寬 51.2 且內容為英文比例字，等寬假設嚴重高估。
> 本欄**只能用於同一檔內之相對比較**，不得跨檔比較絕對值。

**該欄當初支撐的是「同一檔內哪幾列最受影響」，那個用途成立；
它不支撐「home 比 Comfort 更受影響」，而我上一包的表格擺法容易被那樣讀。**

---

## 3. A-CF16 —— 由 PENDING 轉 RESOLVED

**須先報一項不符**：A-CF16 **在本輪之前並未登記於 `ANOMALIES.md`**。
上繳 14／15 以 A-CF16 稱呼列高事項，實際登記從未發生 —— 我當時只在上繳包
內用了編號，未落地。本輪一併補登並直接記為 RESOLVED。

條目內容：現象與成因（範本 `SWQT_20260121` 原本即如此，A-CF07 之清列
只動五格值）、23 §2 判定規則之兩半（前半可證：Privacy 之受限檔即其
`DELIVERY.sha256` ENTRY 003 所記之已交付件；後半 repo 外：Pei 2026-08-15
答「沒有」）、方向 3 之依據（不對稱錯誤成本）、R-C27 已消除最嚴重一段。

**重審條件已載明**：

> 本裁定成立於一個當下為真的事實，非永久性質。若評閱方日後就列高、
> 或就「內容需點選儲存格方能閱讀」提出意見，本裁定即需重審 —— 屆時
> 方向 1／2 之取捨須重新衡量，且其影響及於所有以空白範本 `SWQT_20260121`
> 產出之 feature（現含 Privacy 與 Comfort）。
> 重審之觸發者為外部意見，**不由本 feature 自行判斷**；執行層於察覺該類
> 意見時登記並回報，不逕行改動。

---

## 4. §3.1 前置 gate —— 5 項全 PASS

| gate | 期望 | 實測 | 結果 |
|---|---|---|---|
| BASELINE.sha256 8 檔 | OK=8, FAILED=0 | OK=8, FAILED=0 | PASS |
| DELIVERY.sha256 且仍 2 筆無 ENTRY 002 | OK=2, ENTRY002 absent | OK=2, absent | PASS |
| 來源 hash | `b68117a211b08009…` | `b68117a211b08009…` | PASS |
| lint | 32/32 | 32 / 32 gates PASS; 0 finding(s) across 14 TCs | PASS |
| 生成 TC 數 | 14 | 14 | PASS |

第三項之意義非「檔案存在」而是「**來源為 Pei 已於 Excel 確認之同一份
位元組**」—— 若 prepared 檔在確認後被任何操作動過，該確認即不再涵蓋它。

---

## 5. §3.2 splice

- 腳本：`features/comfort/scripts/write_back.py`（**新寫**，非改自四個既有
  feature 之 `write_back.py`；R20-5 之隔離品不作為起點）
- 寫入路徑：`backend/xlsx_surgical.py` 之 `surgical_save`，唯一路徑（R18-3）
- 目標列 **row 10–23**，append from first data row（BLANK 型）
- 寫入欄 **D F G H I J K L M N P R S AH**（14 欄）
- **不寫入欄**：`B C E O Q T U V W X Y Z AB AC AD AE AF AG`
  —— B 之公式 `=IF(ISBLANK($D10),"",ROW()-9)` 自算編號 1–14，寫入即毀機制
- 產出新檔，**不覆寫** prepared 檔
- surgical report：`sheets_patched {Test Case Specification: 180 cells}`，
  `members_patched ['xl/worksheets/sheet6.xml']`

---

## 6. §3.3 寫回後 assertion —— 9 項全 PASS（自產出檔讀回）

| # | assertion | 期望 | 實測 |
|---|---|---|---|
| 1 | zip member 數與來源相同 | 48 | **48**，對稱差集 none |
| 2 | 差異僅限目標 sheet 之 xml | `['xl/worksheets/sheet6.xml']` | 相同 |
| 3 | DV counts 與來源相同 | equal | sheet5 `(1,0)`／sheet6 `(3,2)`，其餘 7 sheet 皆 `(0,0)` |
| 4 | row 10–23 逐列 14 欄之值與 JSON 一致 | `[]` | `[]`（14 列 × 14 欄 = 196 格比對） |
| 5 | Q 與 T–Z 留白 | `[]` | `[]` |
| 6 | S 欄一律 `NA` | `[]` | `[]` |
| 7 | B 欄 row 10–35 公式逐列原樣存在 | `[]` | `[]` |
| 8 | BLOCKED row 之 L／M 為空且 Remarks 首 60 字含 `Owner:` | `[]` | `[]`（-010／-012） |
| 9 | row 24 起無殘留內容 | `[]` | `[]`（掃 24–35） |

**產出 SHA256**：`b4ad82c2487a38c0206b032ea540ab130c56943b8726e660312fa26be1cc7856`

### 6.1 三處與下放包所寫不同，逐項說明

**（a）assertion 3 之 sheet 編號不寫死。** 下放包舉 `sheet6.xml` 為例。
腳本改以 `sheet_members(SRC)[SHEET]` 解出 —— 寫死者若範本改版即無聲通過。

**（b）assertion 4 由 12 欄擴為 14 欄。** 下放包列 D F G H I J K L M N P R。
我加 **S** 與 **AH**。理由：AH 原本只受 assertion 8 覆蓋，而該項只檢
BLOCKED 兩列之首 60 字元 —— **其餘 12 列之 Remarks 全文從未與 JSON 比對過**。
這是我第一次跑完 §3.3 後自己發現的缺口，補上後重驗，**產出檔 hash 不變**
（`b4ad82c2…`，證明補的是檢查而非內容）。

**（c）assertion 7 之範圍由 row 10–23 擴為 10–35。** B 欄之公式在範本中
延伸至遠超目標列處；只驗 10–23 會漏掉「splice 破壞了 row 24 之後的公式」
這一形態。同一理由使 assertion 9 之殘留掃描**排除 B 欄** —— B24 有公式是
範本原狀，把它算成殘留即為誤報。

---

## 7. §3.4 台帳 —— ENTRY 002

`DELIVERY.sha256` 追加 ENTRY 002，**ENTRY 001 一字未改**。內容含：操作
（`write_back.py --write`）、路徑（`xlsx_surgical.py`）、來源（ENTRY 001
之輸出，即 Pei 已確認之位元組）、目標列 row 10–23、TC 數 14（含 2 條
`[BLOCKED-SPEC]`）、寫入欄與留白欄、結構量測、驗證結果、未做事項。

**狀態欄記「未經 Excel 確認」**，並附一句：**程式層檢查不能代替 Excel
自身之檔案完整性判定。**

複驗：`shasum -a 256 -c --ignore-missing DELIVERY.sha256` → **4 行全 OK**。

**「4 行」須說明，以免下次被讀成錯誤**：prepared 檔出現兩次 —— 一次為
ENTRY 001 之輸出，一次為 ENTRY 002 之輸入基準。append-only 台帳記的是
**每次操作之輸入與輸出**，同一檔在鏈上前後相接時必然重複列出，且該重複
正是「ENTRY 002 確實接在 ENTRY 001 的產物上」之機械證據。

---

## 8. §3.6 不做者 —— 逐項實測確認

| 不做 | 確認方式 | 結果 |
|---|---|---|
| 不複製至客戶交付路徑 | `find` 掃 `*10_Reviewing*ComfortHMI*` | 零命中 |
| 不動 prepared 檔 | 重測 hash | `b68117a211b080…`，與 ENTRY 001 相符 |
| 不改 ENTRY 001 | 純 append，`>>` | ENTRY 001 區塊逐字未動 |
| 不執行 git | 未呼叫 | 無 |

`output/` 現有 2 檔：prepared 與 pilot。

---

## 9. 前置 gate 之一次性 —— 一個副作用，據實報

ENTRY 002 追加後，我為補 assertion 4 而重跑 `--write`，**gate 2 立即 FAIL**：

```
- **FAIL** — DELIVERY.sha256 OK 且仍 2 筆、無 ENTRY 002 — OK=4, ENTRY002=present
```

**這是機制正確運作，不是缺陷** —— 台帳 append-only，故該 gate 天然是
一次性的：一旦記帳完成，同一次 splice 不得再跑一遍。

處置：加 `--verify-only`，只對**已產出之檔**重跑 §3.3，不 splice、不寫檔、
不動台帳。補驗後產出 hash 仍為 `b4ad82c2…`，逐位元組未變。

**未採之作法**：放寬 gate 2 使其「容許 ENTRY 002 已存在」。那會讓「重跑
一次寫回」變成無聲可行，而重跑之風險正是台帳要防的。

---

## 10. §3.5 停下 —— 待 Pei 於 Excel 確認四項

1. 開檔**無修復提示**
2. **R 欄下拉九項可用**（design method）
3. **D5 Scope 正確**
4. **row 10–23 內容與編號正確**（B 欄應自動顯示 1–14）

第 4 項尤請留意 **row 19 與 row 21**（`NR1L-ComfortHMI-010`／`-012`），
其 L／M 為空、Remarks 以 `[BLOCKED-SPEC] Owner: …` 起首 —— 那是
`[BLOCKED-SPEC]` row 之預期外觀，不是漏填。

---

## 11. 「本包是否仍有該驗而未驗者」—— 獨立判斷

不重述 §6 之覆蓋，逐項列我認為仍未被任何機制驗到者：

1. **Excel 之實際開檔行為，我驗不到。** §6 全部 9 項皆為 zip／XML／openpyxl
   層之量測。openpyxl 讀得開不等於 Excel 開得開 —— A-CF07 之所以需要
   Pei 的四項確認，正是這個理由。**這是設計上的停點，不是遺漏。**
2. **`estimated_test_time` 與 `tc_title` 兩個 JSON 欄位未寫入任何儲存格。**
   profile 未指派其落點（`tc_title` 依 canon §4.3 為推導用，不入表；
   `estimated_test_time` 無對應欄）。**但沒有任何 gate 檢查「JSON 有而
   workbook 無」的欄位是刻意還是漏掉的**。現行 `COLS` 是一份人工清單，
   它漏一欄不會有人喊。建議下輪加一個 gate：JSON key 集合減去 `COLS`
   之值域，須完全落在一份具名之「不入表」白名單內。
3. ~~row 24 之後只掃了 12 列。~~ **已補測**：`max_row` 為 59，故另掃
   row 36–59 之 D／F／I／J／L／M／AH，**零殘留**。腳本內之 assertion 9
   仍只掃 24–35（固定窗），此為已知窄於實際列數之處，列此備考。
4. **AH 欄之換行呈現**（15 §4 之 dry-run 曾列）未於產出檔複測 —— 依 §3
   之方向 3 裁定，列高維持現狀，故此項現為**已知且已接受**，非未驗。
5. **A-CF16 之補登暴露一件事**：上繳包內使用 anomaly 編號，與該編號實際
   登記於 `ANOMALIES.md`，是兩件事，而目前沒有機制連結兩者。建議下輪加
   一項檢查：掃 `docs/upstream/*.md` 中出現之 `A-CF\d+`，凡未見於
   `ANOMALIES.md` 者即報。這與 R-C13（零命中須換路徑）同源 —— 引用了
   一個不存在的編號，是靜默失敗。

第 2 與第 5 項我判為**應補之 gate**，但依 25 §3 之授權範圍未逕行加入
（本包授權為寫回，非 lint 擴充）；列此待裁。

---

## 12. 建議 commit message（git 未執行）

```
feat(comfort): write pilot batch into workbook via surgical path

- add R-C28 (pre_conditions three questions, provenance first) to RULINGS;
  annotate R-C25's relationship without rewriting its text
- record the two violation classes in RUNBOOK; point profile 3.2 at R-C28
- annotate the row-height estimate with its measurement conditions and
  cross-file incomparability
- register A-CF16 as RESOLVED with the re-review condition
- add write_back.py: three stages, 5 pre-gates + 9 post-write assertions,
  all read back from the emitted file
- append DELIVERY ENTRY 002, status "not yet Excel-confirmed"
```

---

## 13. 待 Pei

**在 Excel 開啟 `…_Comfort_20260815_pilot.xlsx`，確認 §10 之四項。**
確認後另裁交付形式、位置與送達（Tier 3）。
