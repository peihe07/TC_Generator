# W-106 回歸證明 —— feature.yaml 多 workbook 改造（61 包 §4.1）

量測條件：`scripts/recon.py --feature vehicle_setting --root <暫存副本>`，
暫存副本之 `inputs/` 以 symlink 指回 repo，`feature.yaml` 分別為
git HEAD 版（before）與改後版（after），其餘一致。

## RECON.md
```
7a8,11
> - workbook_cfts044: `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx` sha256=ebe5a65f30a0d4bc…
> - workbook_vf230: `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VF230_20260819.xlsx` sha256=5dd5431e6286a0af…
> - a03_report_vf230: `FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA_Trailer_Name - Max_Power_Level_Report.xlsx` sha256=effe232998a4f18c…
> - spec_pdf_vf230: `C-VF230_V1_R5_PDT27.doc` sha256=800c1fd2c34e14c9…
```
→ 僅 `7a8,11` 之**純新增**四列（新宣告 input 之 sha256）。無修改、無刪除。

## DECISIONS.new.md
```
10c10
< - source files: [AUTO] 4 present (SHA256 in RECON.md)
---
> - source files: [AUTO] 8 present (SHA256 in RECON.md)
```
→ 僅宣告 input 之計數。

## data/ 產物
```
(no differences)
```

## 結論

Part 1（CFTS044）之每一行 recon 輸出**位元未變**；改造為純加性。
`recon complete: state=BLANK, leaves=46, sections=0, targets=46` 前後相同。
