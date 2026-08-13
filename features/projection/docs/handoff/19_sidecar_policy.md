# 下放包 — Projection：R-P93 政策衝突裁定

> 交付對象：Claude Code
> 觸發：R-P93（旁檔入庫）與 `.gitignore:20` 及 `FEATURE_ONBOARDING §6` 明文衝突
> 授權層級：Tier 1
> 日期：2026-08-12

---

## 0. 裁定：採 (b)，現行政策優先

> **R-P94｜R-P93 修正為「產出旁檔但不入庫」**
>
> R-P93 之「旁檔須入庫」**撤銷**。修正為：
> - 交付物仍成對產出 `<檔名>.sha256` 旁檔，置於 `output/`
> - **旁檔不入庫**，隨 `output/` 一併受 `.gitignore:20` 排除
> - 旁檔之用途為**本機驗證**（送達前後之四處一致性比對、日後重驗交付版本），非版控追溯
> - **可追溯性由 tag annotation 單獨承擔**
>
> `.gitignore` 與 `FEATURE_ONBOARDING §6` **不修改**。
>
> **依據**：
> 1. 現行政策為既有、刻意、且**已寫明理由**之設計——`.gitignore:20` 上方三行註解逐字載明「the write-back sidecar carries the delivery digest, which per FEATURE_ONBOARDING §6 lives in the tag annotation and must never be committed to a tracked file」。R-P93 係在未查證該政策之情況下提出。
> 2. **單一真實來源**：digest 若同時存在於 tag annotation 與被追蹤之檔案，兩者可能分歧——被追蹤之檔案可於日後被修改而 tag 不動，屆時無從判斷何者為交付當時之值。tag annotation 綁定於特定 commit 且不隨後續變更而改變，是較強之錨點。
> 3. 我援引之 AMFM 前例（`output/…_Radio_20260129.sha256`）**實為 untracked**——我以其存在推論「旁檔入庫是慣例」，而未查其追蹤狀態。**檔案存在 ≠ 檔案被追蹤。**

---

## 1. A-PJ75｜立新規則前未查既有政策

> **R-P93 之提出係在未查證既有政策之情況下進行**，致與 `.gitignore:20` 及 `FEATURE_ONBOARDING §6` 直接衝突。
>
> 加重情節有二：
> 1. 我在同一份下放包中援引 AMFM 前例作為依據，**卻未查該前例之追蹤狀態**——實測為 untracked，該前例恰恰支持相反結論
> 2. 我在同一份包之 §3 明文要求執行層「OPEN DR 清單須自 repo 現行記載取得，不得沿用本包之列舉（canon §5a 第十五條）」，**而我自己列的那份清單即為錯誤**（列了已撤銷之 #9 #10、漏列 OPEN 之 #14）
>
> 責任歸屬：分析層。與 A-PJ73（未查證即陳述狀態）、A-PJ74(b)（未查證即接受更正）同族。

> **canon §5a 第十七條（新增）｜立新規則前須查既有政策**
> 提出任何新規則、新慣例或新檔案配置前，須先查證該領域是否已有明文政策。
> **既有政策優先於新提案**，除非新提案能指出既有政策之明文理由已不成立。
> 政策之存在往往記於註解、`.gitignore`、或 canon 之非顯著段落——**未看見不等於不存在**。
>
> 實例（A-PJ75）：R-P93 提出「旁檔須入庫」，而 `.gitignore:20` 上方三行註解已明文禁止，且 canon `FEATURE_ONBOARDING §6` 已指定 tag annotation 為 digest 之唯一位置。

---

## 2. tag annotation 定稿（依 R-P94 修正）

執行層產出之版本正確，僅倒數第 3 行須依 (b) 改寫。**定稿如下**：

```
Projection FULL_REFINE delivery

交付檔    NR1L_GEN1(HDCC)_Ver_20260813.xlsx
SHA256    b16debb7bc609e39044803760171cf1d2b583fd1ed8a4cd2602e82029c8c6b67
size      574,700 bytes
基準檔    11579c9b3b8e56eb9f25a06acd2ce9281409286248a37b327be4732cc0bdede9（Phase 0 落地版本）

交付位置
  output/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/NR1L_GEN1(HDCC)_Ver_20260813.xlsx

交付檔不在版本歷史中（inputs/ 與 output/ 依客戶原始檔政策排除）。
本 tag 之樹不含交付檔；交付版本以上列 SHA256 綁定，
本 annotation 為該 digest 之唯一版控位置（FEATURE_ONBOARDING §6）。
output/ 之 .sha256 旁檔為本機驗證用，不入庫。

內容
  資料列   559 → 565（刪 r562、補 7 條）
  覆蓋     165/171 leaf
  變更     既有 63 列 + 授權例外 76 列（ER 6 / Author 40 / Remarks 30）
  裁決     R-P1 ~ R-P94
  異常     A-PJ01 ~ A-PJ75
  OPEN DR  #1 #2 #8 #11 #12 #13 #14 #15 #16 #17 #18 #19
```

裁決與異常之上界依本包更新為 R-P94 / A-PJ75，**執行層須再次對 repo 核對後方寫入**。

---

## 3. DR#14 之狀態須複查（不阻塞 tag）

執行層自 repo 取得之 OPEN 清單含 **#14**。依 R-P76，DR#14 之 Atl-Mid 部分（30 列）已處置完畢，Atl-Hi 部分（12 列）已轉 DR#18。

**若其全部範圍已轉出，DR#14 應可 CLOSED**；若 repo 記載之 DR#14 尚有未轉出之範圍（例如 R-P47 改寫後之「B5 跨車型前置條件」涵蓋面大於原問題），則維持 OPEN 正確。

**處置**：以 repo 現行記載為準寫入 annotation（即維持 #14 為 OPEN），**另於 RD-1 彙整時複查其剩餘範圍**，若確已全數轉出則結案並註記。**不因此延後 tag。**

---

## 4. 上繳要求

1. `output/` 旁檔產出確認（不入庫，`git check-ignore` 命中即為正確）
2. R-P94 落檔；R-P93 標 SUPERSEDED 並保留原文
3. A-PJ75 登記；canon §5a 第十七條落檔
4. tag annotation 定稿，裁決／異常上界對 repo 核對後之最終值
5. 送達步驟 1、2 之執行結果（若尚未執行）
6. 四處 SHA256 一致性驗證

---

## 5. 本包產生之新條文清單（A-PJ53 要求）

| 編號 | 形式 | 位置 |
|---|---|---|
| R-P94 | 可貼區塊 | §0 |
| A-PJ75 | 可貼區塊 | §1 |
| canon §5a 第十七條 | 可貼區塊 | §1 |

落檔：R-P94 → `DECISIONS.md §0.26`（R-P93 標 SUPERSEDED，保留原文）；A-PJ75 → `ANOMALIES.md`；canon §5a 第十七條 → `FEATURE_ONBOARDING.md`。

**不 commit。**
