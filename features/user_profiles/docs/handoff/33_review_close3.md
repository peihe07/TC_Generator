# 33 下放包 — 第三批覆核結案（30／30）

**本包無裁決條文。** 32 輪上繳**核可**。

## 覆核進度

**`TC-079`～`TC-108` 全部 30 條逐條讀畢。** 第三批之內容覆核結案。
未經第二人讀過者：**0**。

## 發現

### W-1（defect）`TC-094` 之 pre-condition 蘊含被測結果

| 欄 | 內容 |
|---|---|
| pre-condition 1 | `**Every Profile has been deleted** from the head unit` |
| procedure | 1. 開啟 “All Profiles” 分頁　2. 讀清單並確認 “Driver 1” 為唯一 |
| ER2 | `**“Driver 1” is present** and no other Driver Profile is listed` |

而 4.5（PRACC5）逐字：

> `If no custom Profile is set up, **or all profiles are deleted**, there will
> always be a default, non-connected profile in the vehicle.`

**「全部刪除」之後系統立即重建預設** —— 故測試開始那一刻，
pre-condition 所述之狀態**已經是假的**（Driver 1 早已存在）。
它描述了一個系統不允許存在之穩態，且其蘊含之結果
（車上只剩 Driver 1）**正是本 TC 要驗的東西**。

§4.4 明文禁止以「feature under test as premise」作 Pre-Condition。

**同 leaf 群之 `TC-093` 做對了**：刪除是 **procedure 步驟 1**，非前提。
`TC-094` 全程未執行刪除，它在驗一個自己假設出來的狀態。

**改**：刪除動作移入 procedure（比照 `093`），
pre-condition 改為刪除前之狀態（曾客製之 profile 存在、座椅鍵少於 2）。
ER 斷言「重建後只有一個」。
**兩條之分野不變** —— `093` 驗**重建發生**，`094` 驗**重建後只有一個**。

**連帶自檢**：全批凡 pre-condition 以完成式描述一個動作結果
（`has been deleted`／`has been removed`／`has been customized` …）者，
逐條判其所述之狀態是否即本 TC 之 ER 所要斷言者。
**是 → 循環，須把該動作移入 procedure；否 → 保留**。命中 0 亦回報。

## 30 條中值得記下的三處

1. **`TC-095` 以條文之例（2 個座椅鍵）為 pre-condition，並具名其取自條文而非自擬** ——
   ER 逐一指名兩個連結（Driver 1 ↔ 鍵 1、Driver 2 ↔ 鍵 2）；
   只驗「有兩個預設 profile」，一個把兩者都連到同一鍵之實作會通過。
2. **`TC-092` 之 ER2 併驗 `non-connected`** ——
   條文寫的是 `a default, **non-connected** profile`；
   只驗「有一個叫 Driver 1 的 profile」，一個把它建成連網 profile 之實作會通過。
3. **`TC-093` 之 ER3 併驗「偏好為預設值」** ——
   條文之 `default` 指重建出一個**預設** profile，
   不是把原客製 profile 改名留下。

## 作業

1. W-1：`TC-094` 修正 ＋ 完成式 pre-condition 之全批自檢
2. 重跑全閘，貼輸出
3. **第四批仍不開** —— 待其取樣清單經本層覆核（29 輪提出，已隔四輪）

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- **寄出 RD 查詢單** —— Tier 3，屬 Pei
- 寫回工作簿（R-U14）
- 第四批之生成

## 上繳

`docs/upstream/33_review_close3.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 現況

| 項 | 值 |
|---|---|
| 語料 | 108 條 ／ leaf 覆蓋 100 / 180 |
| 已覆核 | **108 / 108** |
| 分析層唯一未讀 | **第四批取樣清單**（29 輪）|
| 擋 Phase 6 | A-UP09 / R-U14（DV gate 未立）|
| 待 Pei | RD v2 寄出、R-U17、DR #4、N-XF01、A-UP10、A-UP11 是否回報上游 |
