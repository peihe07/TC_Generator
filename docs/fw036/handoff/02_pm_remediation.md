# 下放包 02：Power Management 全項回修（批 1，Pei 指定優先）

前置：01a／01b 條文須已回寫（R-1、R-3、R-4、S4、S6 生效）。
附件：`02_pm_signal_map.md`（DBC 實查對照表，本包唯一訊號依據）。
對象：`ASW-R2/Power Management/…SWQT_PowerManagement_20260820.xlsx`
（283 列，作者全為 PeiPYHsu，無跨人問題）。新規 0 條。

## 作業原則

1. 工作副本作業：先複製至 repo 工作區，**絕不直接改交付檔**。
2. `xlsx_surgical.py` 為唯一寫回路徑；x14 下拉須於寫回後讀回驗證。
3. 每欄改動前後留 diff；非目標欄不得變動。
4. 訊號一律照附件對照表，**不得自行查表外推**；表外訊號標
   `PENDING: DR-{n}`（§8.4.3），不得杜撰網段。

## M3：訊號記法（R-1）

- CAN 層 7 種 → 改三件組，逐字照附件第一節（含 `Radio_btn0`
  大小寫更正 12 列，A-PM01）
- 內部訊號層 13 種 → 維持記法；`PhoneCall.Info` 5 列統一為
  `Phone_Call.Info`（A-PM02）
- PROXI 層 22 種 → 全數維持；`$Radio_Theme$` 不得套三件組（A-PM03）
- 43 列同行混用雙制者：分層改寫，每 token 自我識別，同行並列允許

## M15：I-sibling 括號重複（S4，104 列）

同 Requirement ID 下括號下半逐字相同者，依各列
**Pre-Condition／Procedure 之實際差異**改寫括號內容為區分 token。
差異無法辨識者→標記待覆核，**不得臆造區分詞**。

## M10-PM：test_item 過長（R-3，71 列）

上半 >50 token 者摘句，保留與括號目的直接相關之句；
全文以 `specification_reference` 指回（PM 屬 CFTS 家族，
格式 `CFTS009-{ObjectID}`／`CFTS010-{ObjectID}`，R-2）。
不得改動括號下半。

## M11-PM：首字大寫（R-4，2 列）

rows 20、204 之 test_item verbatim 中段起抄，首字母轉大寫。

## 驗收（lint036 對工作副本，全項同時成立）

- P（三件組）= 0；J = 0；L = 0；I-sibling = 0
- **不得變動**：D=0 G=0 K=0 M=0 N=0 A=0 B=0（PM 原即清零）
- E 值須維持 **0**（PM 錨值；變動即改動外溢）
- C、F、H 維持原報告值
- 抽驗：CAN 7 種各抽 1 列比對 DBC；M15 抽 10 列確認區分 token
  來自實際差異；M10 抽 8 列確認摘句可回指原文

## 上繳

`docs/fw036/upstream/02_pm_remediation.md`：逐項改動列清單、
lint 前後對照、x14 下拉驗證結果、非目標欄零變動之證明、
A-PM01~03 處置結果、未結 DR 清單、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

## 完成後 Pei 動作（勿代執行）

```bash
cp "<工作副本>" "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_<完成日>(Revise).xlsx"
shasum -a 256 "<寫回檔>" >> <LEDGER>
```
＋ ChangeHistory 增列：`M3/M15/M10/M11: signal notation, sibling
tokens, test_item length, capitalization — PowerManagement`
