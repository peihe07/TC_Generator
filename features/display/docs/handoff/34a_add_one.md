# 下放包 34a —— 附件：補一條（Pei 已問，此為裁定），其餘照收

- 日期：2026-08-26
- 性質：34 包之附件。併入 `docs/upstream/34_closeout.md` 補記，不另出上繳。

## 一、裁定

1. **補**：`{4819710}`（＝`{4819820}` 架構副本擇一引用，兩號並列於
   `specification_reference`）之 DCSD Power Button 喚醒軸，**新增 1 條 TC**
   入 `ops-01`（13 → 14），leaf `SWE1-DM-001`。
   理由：E3 誤殺屬**內容缺口**（R-DM57(a) 之例外）；本 feature 罕見之
   具體值（`250 ms`）；001 需求文逐字含 `timeout conditions`。
   `$DCSD_Power$ = [Pressed]` 之 raw 依 R-DM48 條款層級判定，
   解不得則 ER 驗行為（radio turn on → Timed Mode）＋ 250 ms 之保持。
2. **重跑寫回**：22 → 23 條，§3.2／§3.3／§3.4 全套重做（完整性計數、
   回讀、來源 sha 不變之確認）。輸出檔名日期不變。
3. **寫回標的之偏離（output/）：追認**。三項理由全對 ——
   尤其 (b)：為交付而毀掉唯一的素材完整性保證，本末倒置。
   34 包 §3.1 之文字由本件更正。
4. **`output/` 之 xlsx：入 git**（分析層建議，依 `user_profiles`／
   `time_management` 先例；`inputs/` 被 ignore，git 是寫回史唯一留存處）。
   pathspec 補入該檔。**執行仍屬 Pei。**
5. **B31 之 H4**：不開新 DR（凍結）。於 DR-DM2 補充函末追加一行：
   `Also, {4819575} defers pop-up handling to "HMI core specification
   requirement H4" — please provide that document or its popup list.`
6. 33 包重號（`_resume`）：平行會話碰撞（既知 NN 風險），執行層
   擇 `_scoped` 併驗相容，處置正確。已在 BACKLOG，不另動作。

## 二、上繳補記要求

補跑後之：#新 TC 十欄全文、合併 lint（母體 23）、寫回三表、
覆蓋總表更新（001 之 TC 數 8 → 9）、pathspec 終版。
