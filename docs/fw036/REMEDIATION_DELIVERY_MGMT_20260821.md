# 回修交付版本管理（2026-08-21）— REMEDIATION_PLAN v3 附錄

回修不只是改內容，交付物本身的版本合規同樣要成立。

## 版次命名（待 Pei 裁定一制）

提案：回修版檔名沿用原名，日期改回修完成日，尾綴 `(Revise)`；
同本二修 `(Revise2)`。例：
`..._SWQT_BT_20260901(Revise).xlsx`
（沿用語料既有慣例：DealerMode 已有 `(Review)`/`(Revise)`/`(done)`
尾綴先例。）☐照提案 ☐其他制___

原始交付檔不覆寫、不刪除，回修版並存於同目錄；
舊版是否移 REF/ 由 Pei 逐本裁定。

## ChangeHistory 修訂履歷（036 內建 sheet）

每回修本必須增列一筆：日期／作者（Pei）／描述引用本計畫
M 項編號與列數（例：`M1: removed powered-on pre-conditions,
275 rows; M2b: rebuilt rows 159-184`）。無履歷列 = 驗收退回。

## 寫回與帳務（全屬 Pei）

1. 分析層出批次指示 → 執行層在 repo 工作副本上以
   xlsx_surgical.py 修改 → lint A–P 全跑
2. 上繳包附：lint 報告（前後對照）＋ 修改列清單 ＋
   「該驗未驗」獨立判斷
3. Pei 覆核通過 → Pei 親自複製至 10_Reviewing 交付位置
   → DELIVERY.sha256 追加（append-only）
4. 涉及已 tag 之本（AMFM v1）：回修版屬新交付版次，
   不動已 tag 歷史；tag 策略屬 Pei

## 驗收判準（每批）

- lint 目標項清零（該批對應之檢查項）
- 非目標欄位 sha 前後一致（surgical 不外溢）：以逐欄 diff 證明
  僅目標欄變動
- 抽樣：每批 ≥10% 或 ≥5 列人工比對原文，確認未破壞
  verbatim 上半、未觸凍結欄
- x14 下拉驗證：交付本含 extended dropdown 者，寫回後實測
  下拉仍在（openpyxl 破壞風險為已知，surgical 路徑須驗證）
