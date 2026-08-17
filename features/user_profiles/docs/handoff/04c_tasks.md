# 04c 下放包 — 作業指示（執行層）

裁決見 `04a_rulings.md`（R-U13～R-U17）與 `04b_rulings.md`
（R-U18～R-U20、R-G4～R-G6）。03 輪核可，無退回項。

## 先辦：記載更正與條文入庫（1–3）

1. **RULINGS.md 追加十一條逐字** —— R-U13～R-U20、R-G4～R-G6。
   R-G4／R-G5／R-G6 為全域條文，另依既有慣例登錄於全域規則處。

2. **R-G6 記載更正** —— `docs/upstream/03_recon.md` §8 之
   「git 未執行」據實改寫，動作清單納入該次 `git checkout`。
   **僅改該處記載，不改 §7.1 之敘述**（那段是對的）。

3. **ANOMALIES.md 狀態更新** —— A-UP04 → RESOLVED（R-U18，
   須照錄其永久記載限制）。A-UP09 維持 PENDING（R-U14）。
   A-UP02／A-UP06 維持 PENDING。

## 本輪之實質作業（4–7）

4. **三閘之反向驗證** —— 執行層 03 包 §7 自陳之真缺口，本輪清掉。
   對 037 之副本注入壞資料（至少三型：改一列 Categorization、
   增一列、刪一列），證明三閘各自會轉紅並報出正確的差額。
   **不可能失敗者標「未實測」而非 PASS**（canon）。
   副本用完即刪，`inputs/` 原檔不得觸碰。
   前例：Comfort 96 §6 之 `row-order-by-reqid` 第一版對正確資料轉紅，
   是反向驗證抓到的，不是人看出來的。

5. **`Service` 22 條之類別查證** —— 逐條讀其 Requirement Description，
   判斷是否為非 HMI 側行為（Comfort `[BLOCKED-NON-HMI]`／R-C38 同型）。
   ch4 佔 12 條，屆時才發現是一整章返工。
   **只出判讀與證據，不自裁分類**（Tier 2）。

6. **14 節帶圖條文之判讀依賴** —— 逐節問「不看圖能否寫出可執行的
   驗證步驟」，分類為 不依賴／部分依賴／完全依賴，逐節具名。
   03 輪只數了 14 這個數，未問過這個問題（Comfort A-CF23 同型）。
   完全依賴者列為 DR 候選。

7. **R-G4 之前置查證** —— 查 `features/home/scripts/lint_tcs.py` 與
   `make_batch_context.py` 實際讀 `spec_id_to_outline.tsv` 之哪一種內容
   （欄名、列數、用途），確認後才改 `recon.py`。
   若兩個讀者期待的是 build_outline_map 之形態，
   則 recon.py 之改名為安全變更；若不然，先停手上報。
   一併加上「不得無聲覆寫既存 tracked 檔」之前置檢查。

## 不在本包授權範圍

- 刪除 `inputs/` 之 spec 副本（R-U17，屬 Pei，執行層不得代勞）
- 任何 git 操作，含 checkout／restore／stash／clean（R-G5）
- spec 4.1.1 相關之 TC 生成（R-U15）
- 寫回實作（R-U14：x14 DV gate 未立前不得開工）
- Test Set 分類與 Service 之歸屬判定（Tier 2）

## 上繳

`docs/upstream/04_verification.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷，每個數字標明量測條件。
**動作清單須與「未執行 git」之陳述逐項對得起來**（R-G6）。

## 現況

- Layer 2 已定案（R-U20，8 個 Test Set，合計 180）→ framework.md 可起草
- 生成集合 = 133（R-U19）；037 引用集合 = 135，兩者不得互換
- 未決：DR #4（PU1087／PU1088）、DR #3（A-UP02 之 8 條 → RD-1）
