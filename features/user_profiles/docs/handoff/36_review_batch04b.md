# 36 下放包 — 第四批覆核（第二段）：5.4 之全稱限制未被驗

**本包無裁決條文。** 35 輪上繳**核可**。

## 覆核進度

- **本輪讀畢**：`TC-112`～`TC-121`（10 條）
- **累計**：**21 / 26**；**未讀**：`109`／`110`／`111`／`122`／`123`（5 條）
- 拆檔有效：`26a` 一次讀完 13 條中之 10 條（`109`–`111` 在檔首，下輪補）

## 發現

### Y-1（defect）`TC-121` 之 `only` 未被任何一條驗到

5.4（PRACC10）首句：

> `Editing a Profile is **only** available for the active Profile, in the
> “Edit Profile” tab.`

`TC-121` 之 remarks 稱該全稱限制「其反向由 `SWE1-HMI-PROF-022` 承擔 ——
該 leaf 驗『選取另一個 profile 會 switch system to that Profile』，
即『不進入編輯』之另一面」。

**但 `TC-117`（即 022）之 ER3 為**：

> `Driver Profile B is the active Profile and is highlighted instead of the
> Profile recorded in step 1`

**它斷言「切換發生了」，未斷言「沒有進入編輯」。**
一個既切換、又順手開啟 B 之 Edit Profile 分頁之實作，
**`TC-117` 會過，`TC-121` 也會過** —— 該 `only` 無人驗。

**這與同批之處理不一致**：

| 節 | 全稱限制 | 反向 |
|---|---|---|
| 4.5.2 | `there will **always** be one Driver Profile per memory seat position` | **有**（`096` ／ `105`）|
| 5.7 | `can **only** be done through the Edit Profile screen` | **有**（`127` ／ `134`）|
| **5.4** | `Editing … is **only** available for the active Profile` | **無** |

**同一形狀，兩處配了、一處沒配，而沒配那處之理由不成立。**

**改（建議 (a)）**：於 `TC-117` 之 ER3 加一句
「Edit Profile 分頁未開啟」（或等效之可觀察形式）——
同一觸發之另一個必然結果，依 §5.7 併於同一條，**不必另造 TC**。
`TC-121` 之 remarks 隨之改述其委派對象與所依據之 ER 行號。

若採 (b)（另立負向 TC），須說明為何 §5.7 之併入不適用。

**連帶自檢**：全批凡 remarks／reasoning 稱「某全稱限制之反向由 X 承擔」者，
逐條開啟 X 確認其 ER **確實含該反向之斷言**，而非僅有正向。
**這是 A-UP12（互指之委派）之同型 —— 委派指得到，但被指者沒有那句話。**
命中 0 亦回報。

## 已讀 10 條中值得記下的三處

1. **`TC-115` 之螢幕尺寸 pre-condition** ——
   7 吋螢幕上該圖示本來就不顯示（5.1.2），
   **屆時「圖示不在」證不了任何事**。前提之作用是使斷言有意義，不是湊條件。
2. **`TC-119` 明言 5.3.2 與 latch（`018-02`）為互相衝突之兩條規則** ——
   並以 pre-condition 固定「B 之上次分頁為 Edit Profile」，
   **那是唯一能分辨「停留」與「latch 恰好相同」之情境**。
3. **`TC-118` 之 ER2／ER3 依序斷言** —— 條文寫 `loading **then** welcome`，
   併為一條會失去順序（同 `TC-088` 之理由）。

## 作業

1. Y-1：依 (a) 或 (b) 處置並具名所擇 ＋ 委派反向之全批自檢
2. **查 `docs/handoff/20_batch03.md` 之來歷** —— 分析層 20 輪所寫者為
   `20_batch01_review.md`，該檔非本層所出。回報其內容、產生輪次與寫入者；
   若為誤置或重複，具名處置建議（**不自行刪除**）
3. 重跑全閘，貼輸出
4. **第五批仍不開** —— 待第四批覆核完成（餘 5 條）

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- **寄出 RD 查詢單** —— Tier 3，屬 Pei
- 寫回工作簿（R-U14）
- 第五批之取樣與生成
- 刪除任何檔（含作業 2 之標的）

## 上繳

`docs/upstream/36_review_fixes5.md`，更新 `docs/INDEX.md`，附獨立判斷。
