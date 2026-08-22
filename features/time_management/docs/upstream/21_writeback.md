# 21 上繳 —— 兩條文、DR-6 狀態更正、017 拆分、寫回就緒

執行層，2026-08-22。對應下放包 `docs/handoff/21_writeback.md`。

---

## 0. 逐 T 項對照表（R-TM74）

| T 項 | 內容 | 狀態 | 備註 |
|---|---|---|---|
| **T0** | `cd` 專案根 | **完成** | — |
| **T1** | R-TM78 / R-TM79 入 `RULINGS.md`；R-TM52 加註 | **完成** | 見 §1 |
| **T2** | DR-6 狀態更正 | **完成** | 見 §2 |
| **T3** | A2：015 之顯示前提 | **完成** | 4 條（非 1 條，見 §3） |
| **T4** | A1：017 之跨架構拆分 | **完成** | **14 → 16 條，tc_id 區間變動，見 §4** |
| **T5** | 全批重驗 + dry-run 逐項核對 | **完成** | 見 §5 |
| **T6** | 上繳 | **完成** | 本檔 |

**未做者：無。不適用者：無。**

**增量（R-TM46 + R-TM79 —— 兩個數）**：
`## R-TM` **含撤回 80 → 82**；**不含撤回 78 → 80**。
差額 **2**（R-TM62 / R-TM63 之刪除線標題）。
`## A-TM` **0**（28）；`## G-TM` **0**（3）。

**本包三項須先看**：§4 之 **tc_id 區間變動**（57 → 59，寫回列 10–68）、
§3 之 **015 影響 4 條而非 1 條**、§5.2 之 **dry-run 五項逐項核對**。

---

## 1. T1 —— 兩條文與 R-TM52 之註記

R-TM78（dry-run 必跑）、R-TM79（條數兼計撤回條）已落檔。
R-TM52 之註記段記入 A-TM26 之「記錄完備而內容錯誤」實例。

### 1.1 R-TM78 之一項射程限制（執行層補記）

dry-run 能核對之項目，**限於 `run()` 所列印者**。
`rows` 之所以能被發現，是因為它恰好被印出來 ——
**若某項不在列印清單內，逐項核對也核不到它**。

現行列印涵蓋：來源檔 SHA、分頁、表頭列、欄位對映、列數、`skipped`、
`tc_id` 區間、`test_group`、`BLANK_BY_DECISION`、`unresolved`。

**未涵蓋者包括「每欄實際將寫入之值」** —— 即 dry-run 能確認「寫幾列、
寫哪些欄」，不能確認「每格寫什麼」。已寫入該條之回報段並列入未驗清單。

---

## 2. T2 —— DR-6 之狀態更正

主表列改為 **「Atlantis High 已解除；Atlantis Mid 未解除」**，
Urgency 標 `中（Atl-Mid 側）`。檔末追加狀態更正段，含三態實測數
（8 / 11 / 19）與「Atl-Mid 側僅 6 個 LID 有網段」之明細。

**併記分析層之來源訂正**：`18` §5 T4 之 `on CAN-B` 無來源，
其自陳為第四次同型推定，且發生在已立 R-TM49 之後。

---

## 3. T3 —— 015 之顯示前提

**影響 4 條，非 1 條**（下放包未指定條數）。B4 之 015 全部四條皆加：

```
The cluster does not have the data needed to reference the date
```

**置於架構限定行之後、其餘前置條件之前** —— 架構限定行依 R-TM76
須為首行，本行為次序上之顯示前提。（015 判為 `Both`，故實際無架構行。）

### 3.1 措辭之界線

reasoning 已明寫**不超出兩個來源**：

- HMI Settings List §7-6 註記：`Set Dateis only shown for vehicles in which
  the cluster does not have data needed to reference date`（typo 照錄於引用）
- CFTS015 4814000：`If the HU has No GPS, the HU … shall provide a manual
  method using HMI to enter date`

**只述 cluster 無資料，不推論其成因，亦不加 GPS 之條件** ——
4814000 之 `No GPS` 是 **HU 側**，§7-6 之 `cluster does not have data` 是
**cluster 側**，兩者非同一事。合併會寫出一個兩個來源都沒說的條件。

---

## 4. T4 —— 017 之跨架構拆分

### 4.1 拆法

017 之四物件：`4814019` 為 Atlantis High，`4814053` / `4814073` /
`4814091` 為 Atlantis Mid。原本兩條 TC 同時引用四者而 target 判為 `Both`，
致 TLM LID 取 Atl-Hi 欄而該欄無訊號 → 全部 `excluded`。

| 組 | 條數 | spec_reference | 架構限定行 | 訊號 |
|---|---|---|---|---|
| **Atl-Hi** | 2（現行兩條收斂） | `CFTS015-4814019` | Atlantis High | 無（以 IPC 顯示值為判準） |
| **Atl-Mid** | **2（新增）** | `CFTS015-4814053, 4814073, 4814091` | Atlantis Mid | **TLM LID 取欄 16–20** |

Atl-Mid 組之訊號三件組（取自 `lid_by_arch.tsv` 之 Atlantis 側）：

```
$TLM_MANAGED_TIME_DATE_Day$   in TLM_MANAGED_TIME_DATE.Day1_TLM_Master /
                                 …Day2_TLM_Master        on CAN-B  （列 2120）
$TLM_MANAGED_TIME_DATE_Month$ in …Month1/2_TLM_Master     on CAN-B  （列 2123）
$TLM_MANAGED_TIME_DATE_Year$  in …Year1–4_TLM_Master      on CAN-B  （列 2124）
```

**R-TM62 已撤回**，故本組得寫該等斷言；**其 reasoning 明記
`Atlantis (col 16-20)` 與來源列**，並寫明「本組為 Atlantis Mid，
故取欄 16-20 而非 26-30」——`lint_arch_column` 之新判準即驗此一致性。

### 4.2 **條數與 tc_id 區間變動**（下放包 T4 要求回報）

```
拆分前   57 條   rows 10-66   NR1L-TimeAndDate-001 … -057
拆分後   59 條   rows 10-68   NR1L-TimeAndDate-001 … -059
```

B3 由 14 條增為 16 條。**tc_id 依位置賦號（canon §10.3），
故 017 之後全部編號後移 2** —— 但因尚未寫回，無既有編號受影響。

---

## 5. T5 —— 全批重驗

```
lint_tcs --self-test               53 / 53
build_batch_context --self-test    13 / 13
lint（四檔，排除 .pre-arch）         檔 4；發現 0 項

B1 19 條 / 7 片     B3 16 條 / 5 片
B2 16 條 / 7 片     B4  8 條 / 3 片
                    ──────────────
                    **59 條 / 22 片**   22 片齊備: True
```

### 5.1 佔位 51 處與架構限定行之分佈

```
PENDING: DR-12b  25    設定頁名（+2，017 之 Atl-Mid 兩條亦含 Clock 設定）
PENDING: DR-10   10    PENDING: DR-5   4    PENDING: DR-9  1
PENDING: DR-20    9    PENDING: DR-8   1    PENDING: DR-6  1
                                            ──
                                            51

架構限定行：Atlantis High 21 條 | Atlantis Mid 6 條 | 不加（跨架構）32 條
```

Atl-Mid 由 4 條增為 6 條（017 之新增兩條）。

### 5.2 **dry-run 五項逐項核對**（R-TM78）

| 項 | 值 | 核對 |
|---|---|---|
| `rows` | **59 TCs at rows 10-68** | **符** —— 與四檔合計 59 一致 |
| `skipped` | 4 個軌跡備份（B1–B4.pre-arch.json） | **符** —— 恰四份，無遺漏無多列 |
| `tc_id` 區間 | `NR1L-TimeAndDate-001 … -059` | **符** —— 起點序號 0（母本 BLANK），末號 = 條數 |
| `columns` | 16 欄，`spec_reference=N`、`remarks=AH`、`functional_safety=S` | **符** —— 與 rev C 版面及 `08` §1.2 之逐欄複驗一致 |
| `unresolved` | **為空** | **符** —— 「全部已決（R-TM57 / R-TM59）」 |

**另兩項一併核對**：來源檔 SHA256 `6372fb6b…` 與 `inputs/` 之母本複本
相同（未被他處改動）；`T–Z` 之 `BLANK_BY_DECISION` 理由已為 R-TM77
（非舊之 `TODO(R-TM10-A1)`）。

**未寫入任何檔案** —— 輸出末行為 `DRY RUN —— 未寫出任何檔案`。

---

## 6. 未驗清單（R-TM54 三分）

### A. 可驗而未驗

| # | 項目 |
|---|---|
| A1 | **dry-run 不核對「每格寫什麼」**（§1.1）—— 其列印清單不含逐欄值 |
| A2 | 017 拆分後，**Atl-Hi 組之兩條是否仍完整覆蓋 4814019** 未獨立覆核（其 spec 由四物件收斂為一） |
| A3 | 59 條中 52 條未經獨立覆核；B1 之 pilot 覆核已因架構更正而部分作廢 |
| A4 | **DR-6 對 Atl-Mid 未解除**，現僅 1 處佔位 —— 但 017 之 Atl-Mid 組所用之 TLM LID 恰為有網段者（CAN-B），故未增加 |
| A5 | `10`–`20` 遺留：G1、G2、G4、PROXI 設定方式、89 筆 docx 無標籤物件、`section` 未交叉驗證 |
| A6 | 07/08/09 遺留六項 |

### B. 待 Pei

| # | 項目 |
|---|---|
| B1 | **寫回之放行** —— `surgical_save` 之寫入路徑至今從未執行 |
| B2 | **A-TM28（`Clock` / `Clock & Date`）現影響 25 條** |
| B3 | DR-5（4 處）與設備類（21 處）之上游查詢 |

### C. 已解決

| # | 項目 | 解決於 |
|---|---|---|
| C1 | dry-run 之地位（`20` §9.1） | R-TM78 |
| C2 | 條數計數失準（`20` §9.3） | R-TM79，本包起回報兩個數 |
| C3 | DR-6 對 Atl-Mid 之狀態（`20` §9.2） | 本包 T2 |
| C4 | 015 之顯示前提（`20` A2） | 本包 T3，4 條 |
| C5 | 017 之跨架構拆分（`20` A1） | 本包 T4，14 → 16 條 |

---

## 7. 未執行者（下放包所禁，逐項確認）

- **未動 git；未加 `--write`** —— 本包止於 dry-run
- 未刪除 `.pre-arch.json`（四份俱在）
- 未改 `Clock` 之頁名（A-TM28 未裁）
- 未建 `tm_constants.py`；未送 RD-1
- 未碰 `features/vehicle_setting/`

---

## 8. 寫回就緒狀態

| 項 | 值 |
|---|---|
| TC | **59 條** |
| leaf 覆蓋 | **22 / 22**，無遺漏無重複 |
| lint | **0 項發現** |
| 自驗 | 53 / 53、13 / 13 |
| dry-run | 五項逐項核對全符（§5.2） |
| 寫入範圍 | 列 **10–68**，`NR1L-TimeAndDate-001 … -059` |
| 佔位 | 51 處（DR-12b 25、其餘 26） |

**`--write` 待 Pei 放行。**

---

## 9. 提請裁定

1. **§1.1 —— dry-run 核不到「每格寫什麼」**。若要涵蓋，須在 `run()` 增印
   前 N 列之逐欄值（或另立一個 `--preview` 選項）。是否指派。
2. **§4.2 —— tc_id 區間已由 001–057 變為 001–059**。若 Pei 已據前一版
   數字對外溝通，此處須知。
3. **A2 —— 017 之 Atl-Hi 組 spec 由四物件收斂為一**，其覆蓋是否仍足，
   建議由分析層抽驗（該片為本次拆分之唯一樣本）。
