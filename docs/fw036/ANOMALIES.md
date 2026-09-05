# ANOMALIES —— 全域線（GC 系列）

> 新建 2026-09-05（GC-01 審閱 §五-5，Pei 准）。收全域清理／來源集中線之分析層自報。
> feature 線之 A 條仍記各該 feature 之 `ANOMALIES.md`。編號 `A-GC{n}`。

| id | 內容 | 證據 | 形態 | 狀態 |
|---|---|---|---|---|
| A-GC1 | 下放包 GC-01 記 HMI Settings List 3 份 3 體，實為 **5 份 4 體** | `up/20260905_GC-01.md` 2-1 節 | 樣本代母體 | 已承認（`down/20260905_GC-01_review.md` §一）|
| A-GC2 | LID 異體只記 vehicle_setting，漏 time_management | 同上 | 樣本代母體 | 已承認 |
| A-GC3 | `_intake/SW_Update` 記 9 檔，實為 8 | 同上 2-2 節 | 未區分 meta | 已承認 |
| A-GC4 | `lint_reports/` 記 110，實為 106 | 同上 §5 | 估值未標估 | 已承認 |
| A-GC5 | 記 R-G40／41 兩側同題，實為台帳單邊；僅 R-G42 同題 | 同上 §3 | 一號推及三號 | 已承認 |
| A-GC6 | 模板誤值記三處，實為四處（`functional_safety` R→S） | 同上 §6 | 抄人寫之數（R-G20(LEDGER)）| 已承認 |
| A-GC7 | R-G44 條文以「大小相異」為判準，逆不成立 | 同上 2-1 節（295,635 三份二體）| 判準不對稱 | 條文已修（review §三）|
| A-GC8 | 「任何引用皆歧義」措辭過強；人讀 47.3% 可判 | 同上 §4 | 判準未載 | 已承認 |
| A-GC9 | R-G45 所附「待記者」為樣本值：記 1，實為 **5 feature／13 檔次** | 同上 11-3 節 | 樣本代母體 | 已承認（`down/20260905_GC-01_review2.md` §二）|

| A-GC10 | 「`Test Case Specification&Result` 該名不存在」為偽：它不在 R-G1 母本，但為另一真實變體，145 本中 24 本帶該名（含 `features/power` 在效輸入）；`backend/parser.py:77`、`writer.py:10`、`review_engine.py:1338` 硬編該名 | `up/20260905_GC-02.md` 6-2 節；`docs/reports/tc_sheetname_census_20260905.tsv` | 樣本代母體；**執行層（GC-01 §6 寫入）與分析層（審閱 §三據以下裁）同犯** | 已承認；審閱 §三「R-G48 之補充」之夾具改名裁決**撤回**（`down/20260905_GC-02_review.md`）；模板括號已改 |
| A-GC11 | 審閱 `down/20260905_GC-01_review.md` §三 內有裸節號（`§5`、`§0`～`§4`），違 PROTOCOL「文面引用」；已經 R-G36 機器抽取進台帳，`canon_refs` section ambiguous +1 | `up/20260905_GC-02.md` 9-1 節 | 審閱檔不受自己所定之規拘束 | 已承認；台帳逐字不改，下一輪 `rulings_hash` 後以註記指明其所指為 `up/20260905_GC-01.md` 5 節、`down/20260901_VS-SL-01.md` 各節 |

| A-GC12 | R-G43 之理由「台帳為 `rulings_hash.py` 之指紋源」未量測即斷言，**為偽** | `up/20260905_GC-03.md` 9-3 節：掃描面為 FO ＋ `features/*/RULINGS.md`（`scripts/rulings_hash.py:255-258`）；`RULINGS.sha.tsv` 698 列來源為台帳者 0；R-G12～R-G29 之指紋列全部來自 FO | 人寫之理由代量測 | 已承認（`down/20260905_GC-03_review.md` §一）。裁定 (A) 維持，理由以刪除線更正；掃描面缺口由 R-G43(b) 補。**同一事實解釋 R-G30–R-G41 之「缺列」——該十二條只在台帳，本就不在掃描面，非 Pei 漏跑** |

| A-GC13 | GC-03 審閱 §四 之判準（key 級 grep）未先量其分母，對 comfort／time_management 兩線為**盲測** | `up/20260905_GC-04.md` 4-1 節：comfort 之工作簿引用 PU id **0/1340**、time_management 引用設定名 9/316、LID signal 1/2548；分母由執行層附上方顯 | 判準未量其覆蓋 | 已承認（`down/20260905_GC-04_review.md` §三）。13 判依分母修正五列 |
十三筆之共同形態：以樣本代母體、以人寫之數代機器之數、以人寫之理由代量測、以判準代其覆蓋。
防再犯條文：R-G50（全稱斷言須附查詢式與命中數）、R-G50(b)（對照向須回報被移出／還原之檔數）、
R-G50(c)（列為「不跑」之工具只准 `--check`／`--out <工作區>`）、
R-G16 補充（`docs/reports/*_YYYYMMDD.tsv` 常設排除於一切母體）。
**A-GC10 與 A-GC12 為兩層同時犯**：分析層據執行層之未量測敘述下裁，兩層皆未先跑母體查詢。
