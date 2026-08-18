# 32 下放包 — 第三批覆核（第三段）：4.4 覆寫分支之序列

**本包無裁決條文。** 31 輪上繳**核可**。

## 覆核進度

- **本輪新讀**：`TC-087`～`TC-092`（6 條）
- **累計讀畢**：**27 / 30**；**未讀**：`TC-093`／`094`／`095`
- 第四批取樣清單仍未讀 —— 不在核可範圍

## 發現

### V-1（defect）`TC-091` 之操作序列測不到 4.4 之覆寫

4.4（PRACC4）逐字：

> `**At the start of a new key cycle**, Head Unit will load last known Profile
> **unless a different Profile is detected or initiated** (through the key fob
> or memory seat buttons).`

覆寫之發生點是 **key cycle 之起始** —— 上次之 profile **不應被載入**。

`TC-091`（`006-03`，記憶座椅鍵覆寫）之序列為：

| 步驟 | 內容 |
|---|---|
| 1 | `Switch the ignition off and then on again` → ER1：**`with Driver Profile B active`** |
| 2 | `Select memory seat button 1` |
| 3 | 檢查現用者為 A |

**B 已經被載入了。** 覆寫在 ER1 那一刻就已經沒有發生；
步驟 2 之後所測到的，是「按記憶座椅鍵可切換 profile」——
**那是 4.3 之 `004-03`（`TC-086`）已經覆蓋的行為**。

**同節之另一分支做對了**：`TC-090`（key fob）步驟 1 熄火、
步驟 2 **`Present the key fob … and switch on`** —— 覆寫與 key-on 同時發生，
ER2 為「點火開啟且 key fob 被偵測」，B 從未被載入。

**兩個覆寫分支，一個序列對、一個序列錯。**

**改**：`TC-091` 之座椅鍵操作須落在 key-on 之時（或其前），
ER 須斷言 **A 為該 key cycle 之起始 profile**，
而非「B 載入後被切走」。若實車上座椅鍵僅能於 ignition on 後按，
則該限制須寫入 remarks 並具名其對「起始載入」之可觀察性影響 ——
**不得以「先開機再按」充當覆寫之驗證**。

**連帶自檢**：全批凡條文含「於某時點之前／同時」之時序語
（`at the start of`／`before`／`upon`／`prior to`）者，
逐條確認其 procedure 之動作順序與該時序一致。命中 0 亦回報。

## 已讀 6 條中值得記下的兩處

1. **`TC-089` 之 pre-condition 明列排除兩個覆寫條件** ——
   不排除則失敗時分不出是預設路徑壞了，還是覆寫誤觸發。
2. **`TC-087` 對 key fob 關聯之建立流程不推定** ——
   spec 於本節未述，故以 pre-condition 承接、具名其不在範圍（§8.4.1）。

## 作業

1. V-1：`TC-091` 序列修正 ＋ 時序語之全批自檢
2. 重跑全閘，貼輸出
3. **不生成第四批**

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- **寄出 RD 查詢單** —— Tier 3，屬 Pei
- 寫回工作簿（R-U14）
- 第四批之生成

## 上繳

`docs/upstream/32_review_fixes3.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 分析層之記錄

`TC-093`～`095`（3 條）與第四批取樣清單，下一輪讀畢後第四批方得開批。
