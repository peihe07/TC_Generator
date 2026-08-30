# 59 — 58 回報覆核；B3/B7 解凍；二項交 Pei

下放包 | 分析層 → 執行層 | 往返 NN = 59

前置：`data/58_b4_b2_report.md` 已覆核，判定 **ACCEPT**。
G0 9/9 ＋ 3/3、G253 PASS、G254 B-1 衝突 0（片段內）。
三段鏈重做方法正確、三筆語意跳接拒收正確、「未查而僥倖」自陳正確。
58 包 §E「寫回移至 59 包」由本包取代，寫回移至 60 包，**仍受 §K-2 阻斷**。

## 0. 覆核所見

- 「105 → 102」證實 R-P368 解決的是**方法正確性**，不是 PENDING 之量。
  十一名中九名為 HU 內部變數，**本質上不進 LID** —— 執行層之診斷成立。
  其結論：S6 衝突不可能由查表解消，只能由 Pei 裁處置。
- `LTM_OperationalModeSts.Info` → BCM 側 `OperationalModeSts` 之等同性屬上游職權，
  維持 DR-PW26(1)，**不因「解得」而視為已確認**。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P370] R-P365(d) 撤回；B3、B7 解凍先行；B5 續凍。
         （a）R-P365(d)「R4 BHCAN 是否複製入 features/power/inputs/」撤回 ——
              台帳三檔皆在 forms/，為全案共用，跨 feature 依賴之前提已消解；
              R-P365 依 R-P36 原文不改，加註
         （b）B3 可及性報告（R-P367）與 B7 家族 K 三分法（R-P366）
              **不依賴 §K 二項**，即時施作；B7 先於 B3
         （c）B5 機器改寫續凍，待 §K-2 裁後
         （d）DR-PW23 附表以 58 版為準；十一名「未解得（止於段 1）」之九名
              於附表加註「HU 內部變數，LID 不收錄」，其解消途徑僅餘上游回覆或 Pei 裁
         裁決者：分析層（Tier 2）。
```

## H. 作業指示

1. 抄 R-P370；R-P365 加註
2. B7 依 R-P366 施作，出 `data/family_k_disposition_55.tsv`，驗 G251
3. B3 可及性報告 `data/proxy_reachability_55.md`，驗 G252 → **停，待覆核**
4. 上繳 `features/power/docs/upstream/59_unfreeze.md`

## I. 禁區

沿用 58 包 §I。B5 不得施作。

## J. 自檢

一條，一個頂層 block。對既有 canon：R-P370 對 R-P366 / R-P367 — 為其解凍，無改文；對 R-P365 — (a) 撤回其 (d)，加註處理。無違反。

## K. 待 Pei 裁（二項）

### K-1　B-1 型衝突：`$PwrAccDelayAct$`
規格 CFTS009-4941055 → LID r1458 逐字 → `BODY_CNTRL3.Comfort_Enable_Time`（B-CAN）
→ **BHCAN2 無、R4 有、FDCAN8 訊息名為 `BCM_FD_27`**。影響 `ENTER_STANDBY` 之 `Timeout1` 值。
- 甲：`Timeout1` 值改 `PENDING: DR-PW26 <值>`，片段常數名不動，等上游
- 乙：採 FDCAN8 之 `BCM_FD_27.<同名 SG_>`（須執行層先實查該訊息下是否有同名 SG_；有則採，無則回甲）
- 丙：例外准用 R4 名（對 R-P368(e) 開例外，須你明文）

### K-2　PENDING 102 / 283（36.0%）對 S6（57 包 §K-1 重述，前提改 102）
- 甲：等 DR-PW23，寫回無期限順延
- 乙：分段寫回 —— 181 條先交，102 條留 `PENDING: DR-PW23 <名>` 附清單（對 S6 開例外）
- 丙：你逐名審 13 名，可裁「測試台可觀察」者降轉具體步驟，餘者依甲
- 丁（新）：內部變數視為中介 —— Procedure 改驅動 CFTS 所載**使該變數變化之上游 CAN 事件**、
  觀察 CFTS 所載之**下游效果**，內部變數自 Procedure/ER 移除，僅留 `test_item` 上半 verbatim。
  等於以「因→果」取代「設內部值」。**改變驗證對象之結構（R-13 之慮），且每名須逐條讀 CFTS 找上下游**；
  可行性未估，若採，先以 `RemStartFail` 一名試作交你看，再決定推廣。
