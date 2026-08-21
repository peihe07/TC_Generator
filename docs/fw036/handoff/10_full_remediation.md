# 下放包 10：全案整批回修（Pei 指示一次做完，2026-08-21）

前置：`09_r1v2_swc_baseline.md`（R-1 v2）須先回寫 canon 並重寫 lint P。
基準：**SWC 0708 為全案風格權威**。八本分別作業、分別產出工作副本、
分別驗收；**不合併工作簿**。每完成一本即上繳該本區段，不待全部完成。
新規 0 條（R-1 v2、R-7 已於 09 包成文）。

## 作業總表

### A. Power Management（283 列）— 最優先，一次修足
| 項 | 內容 | 列數 |
|---|---|---|
| A1 | **回改** 批 1 三件組 → R-1 v2 (a)/(b) 式 | 42 格 |
| A2 | Input Test Data 內聯至 Procedure／PC，一律改 `NA` | 158 |
| A3 | 步驟含 `listed in Input Test Data` 之指涉全數消除 | 同上 |
| A4 | PROXI 改 `PROXI $X$ = "值"`（現 129 行無前綴） | 129 |
| A5 | M16 spec_reference → `CFTS009/010-{ObjectID}` 在前、HMI 式在後 | 283 |
| A6 | 賦值值加 DBC `VAL_` 括號標籤（對照見 08 包 §四） | 18 |
寫回版次 `(Revise2)`；`(Revise)` 不覆寫。

### B. BT 0729（436 列）
| B1 | M1 PC `HU is powered on…` 移除；`adb shell is accessible` 保留；`FULL OPERATION MODE` 依 §8.5 逐列判（觸發態改寫、環境前提刪） | 275 |
| B2 | M2b 殘缺列：rows 159/160/171/172/179/180/183/184 補 `test_set`（詞彙表 9 種）＋`author` | 8 |
| B3 | M11 首字大寫（真違規，行計） | 14 |
| B4 | M10 test_item >50 token 摘句（R-3） | 375 |
K（雙語）依 R-5 `[DEFAULT]` 豁免，不動。

### C. HFP 0316（159 列）
| C1 | M2b 29 列補 `test_set`／`author`／`spec`／`pre`；`spec`/`pre` 走 §8.4.3 三態，不得自撰內容 | 29 |
| C2 | **A-HF01** Test Set 欄之 `12-01需求重點不是只是看電話號碼格式` 清除並歸類 | 1 |
| C3 | M5 ER 情態詞（引號內原文豁免） | ~18 |
| C4 | M12 工作備註中文移至 Remarks | ~15 |
| C5 | M8 步驟/ER 不對齊 | 5 |

### D. DealerMode 0417（125 列）
| D1 | M4 方括號 `[X]` → `"X"` | 120 |
| D2 | M5 ER 情態詞 | 16 |
| D3 | M8 對齊 | 6 |

### E. AMFM 0810（298 列）— **須 Pei 先知會 Wilson**
| E1 | M6 Wilson 區 `check whether` → `check that`（依 ER 極性，不得機械替換） | 30 |
| E2 | M9 test_item 缺括號下半（含 rows 87–90 sibling 同文） | 154 |
| E3 | M7 spec_ref `;` → 換行；短號 → 7 位 ObjectID（須附 CFTS 原文出處） | 32+ |
| E4 | M10 摘句 | 29 |

### F. Projection 0623（653 列）
| F1 | M2b row 571 六欄全空：先判是否誤留空列，**不得自行刪列** | 1 |
| F2 | M11 首字大寫（rows 429–432 等，依 R-4 轉大寫） | 4 |
| F3 | M10 摘句 | 91 |
| F4 | M7 短號 `CFTS025-4660` ×7 → 7 位 ObjectID | 7 |
K 依 R-5 豁免。

### G. Media 0625（602 列）
| G1 | M7 Pop Up List 檔名三拼統一為 `(Dec_15_2023)` | 8 |
| G2 | M8 對齊 1 列、C hedge 1 列（R-6b 後若仍計） | 2 |
Media 其餘全清，勿改。

### H. Home 0809（216 列）— **須 Pei 先簽 Layer 2 框架**
| H1 | M2a Test Set 整欄補值 | 216 |
| H2 | M10 摘句（含 row 135 之 415 字表格傾倒） | 17 |
框架未簽前，H 段不得開工；其餘七本不受影響。

## 共通規則

1. 一律工作副本；`xlsx_surgical.py`／`surgical_save` 唯一寫入路徑；
   交付本唯讀，不得覆寫。
2. **不得自行撰寫缺失內容**：走 §8.4.3 三態（`NA`／`PENDING: DR-{n}`／
   標記待覆核）。
3. **不得刪列、不得新增列**（Projection row 571、AMFM 重複列皆同）。
4. 摘句一律 R-3 + R-4；verbatim 上半不套 R-1/R-6b 之檢查。
5. 每本驗收：目標項歸零；**非目標項不得增加**（減少且可歸因於已授權
   改動者視為達成，見 06 包 §二）；逐格 diff 僅目標欄；x14 讀回。
6. 每本上繳附：改動列清單、待覆核列、新增 DR、lint 前後、
   **「本包是否仍有該驗而未驗者」獨立判斷**、引用裁決編號清單。

## 順序

A → B → D → G → C → F → E（知會後）→ H（簽署後）。
A 完成即上繳，不待其餘。
