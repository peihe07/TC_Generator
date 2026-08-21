# 批次 Playbook A：通用流程 + 批 0–4（2026-08-21）

每批固定五段：**規則**（引用條文）→ **Pei 前置**（你做什麼）→
**下放**（你貼給誰的指令，逐字）→ **覆核判準** → **完成動作**。
鐵律：前批未覆核不得開下批；下放包由分析層（本 Project）產出，
你只負責觸發、裁定、覆核、寫回。

註：DELIVERY.sha256 未見於 repo root，寫回步驟中之 ledger 路徑
以你現行檔案實際位置代入 `<LEDGER>`（勿新建第二本帳）。

---
## 批 0：lint 建置（已下放，可立即執行）
規則：R-TM7、R-VS18、唯讀約束（見包內）。
Pei 前置：無。
下放（貼 Opus5）：
```
讀 docs/fw036/handoff/00_lint_bootstrap.md 與 00_lint_spec.md，執行
```
覆核判準：upstream/00 存在；Media 校準 11 項全符基準；pytest 綠；
8 本報告齊。
完成動作：回本 Project 貼一句 `批0覆核通過` → 我開批 R。

---
## 批 R：裁定回寫（canon/機制條文入庫）
規則：你在 REMEDIATION_PLAN v3 勾定之 R-1~R-5、S1/S2/S4/S5/S6、
版次命名制。
Pei 前置：**打開 REMEDIATION_PLAN_20260821.md 逐項勾**（直接改
檔內 ☐ 為 ✅/❌，存檔即為裁決紀錄）。
下放：勾完回本 Project 貼 `裁定完成，出批R包` → 我產出
`handoff/01_canon_writeback.md`（含逐字貼入區塊與插入位置）→
你貼 Opus5：`讀 docs/fw036/handoff/01_canon_writeback.md，執行`
覆核判準：canon diff 僅含已勾條文；RULINGS_LEDGER.md 建立；
v2 檔首出現 superseded 標記。
完成動作：**git commit（你本人）**；建議
`docs: adopt remediation rulings R-1..R-5, S1..S6`。

---
## 批 1：M1 BT powered-on（275 列）
規則：canon §4.4、§8.5（FULL OPERATION 逐列判定表隨包附）。
Pei 前置：批 R 完成；無其他。
下放：貼我 `出批1包` → 我產 `02_m1_bt_pc.md` → 貼 Opus5：
`讀 docs/fw036/handoff/02_m1_bt_pc.md，執行`
覆核判準：lint D 對 BT 工作副本 = 0；逐欄 diff 僅 pre 欄變動；
x14 下拉存活實測附截圖或讀回驗證；抽 5 列人工比對。
完成動作（寫回，你本人）：
```bash
cp "features/…工作副本" "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Bluetooth/FM-WI-FSM-036-A01 …_SWQT_BT_20260901(Revise).xlsx"   # 日期=完成日
shasum -a 256 "<寫回檔>" >> <LEDGER>
```
＋確認 ChangeHistory 已含 `M1: removed powered-on pre-conditions, 275 rows`。

---
## 批 2：M2b 殘缺列重建（46 列）
規則：§4.2 詞彙表、R-5 裁定結果（BT159–184 中文 proc 處置）、
author 補值=原區段作者或 Pei（包內逐列標明依據）。
Pei 前置：批 1 寫回完成。
下放：`出批2包` → `03_m2b_broken_rows.md` → 貼 Opus5 同型指令。
覆核判準：lint G=0（三本）；46 列 Test Set 值皆屬各本既有詞彙；
author 欄無空。
完成動作：同批 1 寫回三本（BT/HFP/Projection）＋ ledger ＋履歷。

---
## 批 3：M4+M5+M8+M11+M12 機械合批（~190 列）
規則：§11 引號、§6 情態詞（引號豁免）、R-4 首字轉大寫、
工作備註→Remarks。
Pei 前置：批 2 寫回完成。
下放：`出批3包` → `04_mech_smallfix.md` → Opus5。
覆核判準：lint B/F/H/J 目標本清零；E 對齊修復列逐列人工看；
HFP row75 型備註出現在 Remarks 欄且交付欄無 CJK 殘留。
完成動作：寫回 DealerMode/HFP/AMFM(F 項部分)/Media(1 列) ＋
ledger ＋各本履歷。

---
## 批 4：M7 spec_reference 正規化（52 列）
規則：R-2；短號改 7 位須附 CFTS 原文對照證據（§8.4.1）。
Pei 前置：批 3 寫回完成。
下放：`出批4包` → `05_m7_specref.md` → Opus5。
覆核判準：lint O 目標本清零；12 個短號之新 ObjectID 逐一附
原文出處行；PU 檔名全語料單一拼法。
完成動作：寫回 AMFM/Media/Projection ＋ ledger ＋履歷。
