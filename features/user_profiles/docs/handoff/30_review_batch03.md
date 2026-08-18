# 30 下放包 — 第三批覆核（第一段：TC-096～108）

**本包無裁決條文。**

## 覆核範圍聲明

- **本包逐條讀畢**：`TC-096`～`TC-108`（**13 條**，含 spec 原文對讀）
- **未讀**：`TC-079`～`TC-095`（**17 條**）
- **29 輪之第四批取樣清單本層尚未讀** —— 不在本包核可範圍
- 未經第二人讀過者：**17 條**（非 0）

## 發現

### T-1（defect）`TC-101` 之 ER3 引用了 procedure 未記錄之物

| 欄 | 現況 |
|---|---|
| procedure 1 | `Read the status bar and **check that a Profile button is present**` |
| ER 1 | `A Profile button is present in the status bar` |
| ER 3 | `The Profile button icon **differs from the icon read in step 1**` |

**步驟 1 沒有讀圖示，也沒有記錄圖示** —— 它只確認按鈕在。
ER3 卻以「步驟 1 所讀之圖示」為比較基準，**該基準不存在**。

測試者依此執行會卡在步驟 3：手上沒有可比對的紀錄。

**同批之 `TC-103` 做對了**：步驟 1 為
`Read the status bar Profile button and **record its state**`，
ER1 為 `The Profile button state is **recorded**` —— 基準線是被建立的。

**改**：`TC-101` 步驟 1 改為
`Read the status bar and record the Profile button icon`，
ER1 相應改為記錄式。§5.6 之基準線要求：**記錄步驟與比較步驟須成對**。

**連帶自檢**：全批凡 ER 含 `recorded in step N`／`read in step N`／
`the value from step N` 者，逐條確認該步驟確有**記錄或讀取之動作**，
而非僅有「檢查存在」。命中 0 亦回報（R-G10）。

## 已讀 13 條中值得記下的四處

1. **`TC-105` 之 ER3 斷言「恰好一個」而非「B 沒連上」** ——
   後者容許實作把 A 踢掉再連 B，那同樣違反條文。
   **全稱限制之反向，其 ER 要斷言的是限制本身，不是這次操作失敗。**
2. **`TC-099` 之步驟 2 先讀出改派結果、步驟 3 再比對現用者** ——
   使本條**不依賴 `010-01` 之改派規則是否正確**。
   同一觸發之兩個 leaf，彼此不互為前提，切得乾淨。
3. **`TC-102` 只取純色 avatar 一側** —— 圖像 avatar 之呈現條文只寫
   `with avatar`，寫進 ER 即為推定（§8.4.1）。**取條文最具體之一側**，正確。
4. **`TC-104` 以「按鈕已被移除」為 pre-condition，並具名該操作屬 Home feature** ——
   §8.4.2 之正確處置：以他 feature 之結果為前提，不代測其流程。

## 作業

1. T-1：`TC-101` 修正 ＋ 全批 `step N` 引用之連帶自檢
2. 重跑全閘，貼輸出
3. **不生成第四批** —— 待其取樣清單經本層覆核，且 17 條讀畢

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- **寄出 RD 查詢單** —— Tier 3，屬 Pei
- 寫回工作簿（R-U14）
- 第四批之生成

## 上繳

`docs/upstream/30_review_fixes.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 分析層之記錄

`TC-079`～`TC-095`（17 條）與 29 輪之第四批取樣清單，下一輪讀畢。
**不以本包核可推定其已覆核。**
