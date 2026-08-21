# 下放包 16 主檔：PM 全面改寫（分工版，2026-08-21）

Pei 裁定：走路線 (c)（值一律取自來源，不得依情境推定）；
改寫工作分兩軌並行。**其餘七本仍凍結。**

## 分工

| 軌 | 範圍 | 列數 | 負責 |
|---|---|---|---|
| A | rows 10–65 已逐列寫全 | 56 | 分析層（**已完成**，附件 A–E） |
| B | 同構列，照樣式改寫 | **197** | **執行層（本包）** |
| C | 需回查 CFTS 原文取值 | **30** | 分析層（進行中，完成後另包） |

軌 C 之 30 列（**執行層不得動**）：
124–127、149、181、233、234、265–282、289–291、293

## 執行層須讀之文件（依序）

1. `09_r1v2_swc_baseline.md` — R-1 v2 基礎（部分經 v3 取代）
2. `12_r1v3_signal_observability.md` — **R-1 v3 訊號寫法（現行）**
3. `13_r9r10_layout_whitespace.md` — R-9 版面／R-10 空白
4. `14_r11_samples.md` — R-11 一觀察點一步驟
5. `15_r12_precondition_specref.md` — R-12(a) PC 句式
6. `16a`–`16e` — 已完成 56 列（**逐列樣式範例**）
7. `16f_pm_pattern_samples.md` — 三型補範例與通則
8. `features/power/docs/transition_values_from_source.md` — DBC VAL_ 全集
9. `features/power/docs/A-PM09_withdrawn.md` — 9 列 Input 明載值對照
10. `features/power/docs/specref_anchor_chain_verified.md` — spec_ref
    錨鏈驗證結論（確認現況正確、不得改）

## 軌 B 作業規則

改寫 `pre`／`input`／`proc`／`er` 四欄。**`test_item` 與
`spec_reference` 不得動**：
- `test_item`：R-6 verbatim 上半不得改（括號下半本包亦不動）
- `spec_reference`：**已經 037＋SYS2 錨鏈逐列驗證為正確**
  （274/283 完全相符、9 列僅順序不同、1 列 037 側欄位空白），
  非「待查凍結」。詳見
  `features/power/docs/specref_anchor_chain_verified.md`。
  M16-PM 與 DR-PW19 均已撤銷。

同構群對照（26 群，取樣式最接近之已完成列為範本）：

| 群 shape (PC行,步數,含CAN,含內部訊號,Input有值) | 列數 | 範本 |
|---|---|---|
| (2,2,F,F,T) | 46 | **16f 型一**（row 150） |
| (3,2,F,T,F) | 32 | rows 10／15／21 |
| (2,2,F,T,F) | 21 | rows 13／14／24 |
| (3,2,F,F,T) | 20 | rows 34／35／36 |
| (2,2,F,F,F) | 9 | rows 19／20／31 |
| (3,2,F,F,F) | 8 | row 28 |
| (3,3,F,F,T) | 7 | **16f 型二**（row 187） |
| (4,2,F,T,F) | 6 | rows 52／53／54 |
| (1,2,F,F,F) | 6 | **16f 型三**（row 165） |
| (3,3,T,T,F) | 5 | rows 47／55／57 |
| 其餘 16 群 | 37 | 取 shape 最近之已完成列 |

**硬性**：
- 不得自行推定未明載之值 → `PENDING: DR-{n}`，並於上繳逐列列出
- 不得刪列、增列、拆列
- 不得改 `test_item`／`spec_reference`
- NBSP／全形空格／行尾空白全欄正規化（R-10(a)，含 test_item）
- 彎引號／方括號／行尾句號**僅在四欄與括號下半改**，
  test_item 上半不動（R-10(c)）

## 驗收

- Input 非 `NA` 列 = 0；`listed in Input Test Data` = 0
- 三件組 `in … on …` 殘留 = 0；`Send CAN:` 舊式 = 0
- PC 未編號行 = 0；PC 多條件並列行 = 0；PC 首項為狀態、末項為工具行
- 一步含 2+ 觀察點之行 = 0；`Read` 未寫應觀察值之行 = 0
- NBSP = 0
- PROC↔ER 編號數逐列相等（**E 必須為 0**）
- `test_item`／`spec_reference` 逐格零變動
- x14 下拉讀回；`surgical_save` 唯一路徑；交付本唯讀

## 上繳

`docs/fw036/upstream/16_pm_full_rewrite.md`：
軌 B 197 列改動清單、PENDING 列逐列理由、lint 前後、
diff 證明（僅四欄）、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

**止於工作副本。** 軌 C 完成後由分析層併入，再由 Pei 決定寫回版次。
