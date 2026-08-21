# A-PM09 撤銷 + 分析層第五次過早結論（2026-08-21）

## 撤銷

~~A-PM09：rows 49／50／52／53／54 各缺 `Ignition_Pre_Off` 分支之對應 TC，
覆蓋不足，須拆列。~~

> **撤銷（2026-08-21，分析層自查）**
> 該結論僅檢視 rows 47–54 即下「缺分支」之全稱判斷，未掃全表。
> 實測全 283 列：`Ignition Pre Off` 出現於 **8 列**
> （55、63、99、118、119、125、127、171）；`Ignition Off` 出現於
> **12 列**（21、28、29、47、62、73、74、100、115、119、124、126）。
> **兩分支皆有 TC，覆蓋無缺口。**
> 成對關係明確：row 62／63 =（Ignition Off／Ignition Pre Off）同一
> 驗證之兩分支；row 99／100 同；row 115／118 同；row 55 與 row 47
> 為 Full-Operation 下之兩分支。
> 依 R-TM13 保留原條文並加註，不刪除。

**此為分析層第五次以局部樣本下全稱結論**（前四次：ER 極性、
連接詞計數、括號下半解析、DBC VAL_ 僅列 0–8）。
共同模式：**未以已知全集驗證即宣稱「無／缺／全部」**。
後續凡涉「缺」「無」「全部」之判斷，一律先跑全表掃描再書寫。

## 連帶更正

### 1. 附件 D rows 49／50 之自註修訂

原自註「原文為 Ignition_Pre_Off OR Ignition_Off 二選一，本列取
Ignition_Off；另一分支缺 TC，見 A-PM09」→ 改為：

> 原文（CFTS009-4941466）之條件為 `Ignition Pre Off` OR
> `Ignition Off`；本列取 `2 (Ignition_Off)`。另一分支由 row 63
> （`Ignition Pre Off`）承載，覆蓋完整。

### 2. Input Test Data 已承載轉態值之列（內聯時直接取用）

以下各列之 Input 欄已明載目標值，內聯時**逐字取用，無須查原文**：

| row | Input 內容 | 內聯後之 PROC 值 |
|---|---|---|
| 62 | `LTM_OperationalModeSts: "Ignition Off"` | `$STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)` |
| 63 | `LTM_OperationalModeSts: "Ignition Pre Off"` | `= 10 (Ignition_Pre_Off)` |
| 99 | `transition to "Ignition Pre Off"` | `= 10 (Ignition_Pre_Off)` |
| 100 | `transition to "Ignition Off"` | `= 2 (Ignition_Off)` |
| 115 | `Ignition working condition: "Ignition Off"` | `= 2 (Ignition_Off)` |
| 118 | `Ignition working condition: "Ignition Pre Off"` | `= 10 (Ignition_Pre_Off)` |
| 171 | `Ignition working condition: "Ignition Pre Off"` | `= 10 (Ignition_Pre_Off)` |
| 11 | 四個 ignition working condition | `= 5／6／7／8`（見附件 A） |
| 246–249 | 日期型（Dec 21／Mar 20／Jun 21／Sep 23） | 非訊號，屬情境條件，入 PRE |

**此表使 46 列「未指明目標值」中之 9 列有明確來源**，
無須逐列回查原文。

### 3. `Ignition_Pre_Off` = VAL_ 10（非 0–8 範圍內）

先前附件 A–D 僅列 VAL_ 0–8，遺漏 9–15。完整列舉見
`transition_values_from_source.md` §一。凡涉 `Ignition Pre Off`
之列一律用 **10**。

## 尚待查原文之列（46 − 9 = 37 列）

`Bring the HU to …` 15／`Bring the TLM to the status …` 9／
`Attempt an/a …` 6／`Let the TLM enter/exit/settle/evaluate` 6／
`Let LTM_OperationalModeSts.Info transition occur` 5（其中 49／50／
52／53／54 已依 §1 定案，實餘 0）。

依路線 (c) 逐列以 test_item verbatim 關鍵詞定位 CFTS009／010 原文，
每列註明所據 object id。
