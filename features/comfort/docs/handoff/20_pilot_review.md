# 20 — Comfort HMI / pilot review：不通過，退回修正

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/11_pilot.md`
- 判定：**pilot 不通過。** defect ×4、note ×1、待補證據 ×1。
  皆為就地可修，非重新設計。

依 canon §1.2 分層取樣，逐條讀 TC 內容，**不以 §9 自評為判定依據**。
所列 defect 皆為條文規則之違反，非樣式歧異，故不需通過 done-region check。

---

## 1. DEFECT-1（阻塞）—— TC-004 單步 procedure，且 lint 無此 gate

`NR1L-ComfortHMI-004` 之 `test_procedure` 僅一步：

> 1. Read the list of lumbar and bolster adjustment types offered on the Seats tab

**§10.5：至少兩個編號步驟（Setup → Verification 最少），單步 TC 一律駁回。**

修法：把 PC2 之 `[test-setup] The Seats tab is open…` 下放為第 1 步
（開啟 Seats tab），`Read the list…` 為第 2 步。此舉同時解決 PC2 之
`reachable` 措辭含糊與 §4.4「step-controlled state 不得入 Pre-Condition」。

### 1.1 連帶：lint gate 集合有洞

25 個 gate 中**無任何一個檢查 §10.5**。清單逐項核對：
`tc-id-*`、`req-id-unique`、`spec-ref-*`、`test-group`、`design-method`、
`priority`、`functional-safety`、`estimated-time`、`remarks`、
`trailing-period`、`ui-bracket`、`title-*`、`item-modal`、`er-modal`、
`source-class`、`proc-er-1to1`、`token-*`、`fabricated-qty`、`sibling-axis`
—— `proc-er-1to1` 只驗兩者列數相等，**單步對單步照樣 1:1**。

**「25/25 PASS」為真，但其涵蓋範圍不等於 §9／§10 之全集。**
與 A-CF05（intake 報 346 實為 403）同型：輸出正常，只是少驗了一項。

新增 gate **`proc-min-steps`**（`len(test_procedure) >= 2`），並反向驗證其
確實會失敗。同時逐條核對 §10.1 之十個必要 key、§10.4 `reasoning` 之
2–5 句、§10.5、§10.6 是否各有對應 gate；缺者補齊並回報補了哪幾個。

---

## 2. DEFECT-2（阻塞）—— TC-010／TC-012 之 `duplicate_of` 誤用

§10.6 之 `duplicate_of` 要求 **strict equivalence：same trigger + outcome
+ input + verification target**。

TC-009 之 trigger 為「長按門板硬鍵」，TC-010 為「長按觸控螢幕」——
**trigger 不同**，等價性即不成立。

且上繳包自身即記「**兩條 TC 仍各自寫出（操作面不同：門板硬鍵 vs 觸控螢幕）**」
—— 以操作面不同為由分寫兩條，復以等價為由標 `duplicate_of`，
**兩個判斷互相否定**。

`axis="none"` ⇔ `duplicate_of` 有值（§4.6）；此處 axis 不是 none，
是**操作面**。

修法：TC-010／TC-012 移除 `duplicate_of`，改填
`distinguishing_axis = {"axis": "mode", "delta": "操作面為觸控螢幕，
非門板硬鍵 (-, +)"}`（措辭自定，須含具體 token）。

### 2.1 待補證據（本項之前置）

上繳 §3.1 稱 `-080-02` 之內容為「logic as per Core N0」、`-081-02` 為
「equivalent to previous 4-way rocker」；但 §3 之表列 TC-010 主題為
「長按觸控螢幕 → 快速增減」。**兩處敘述不一致** —— 前者說 -02 是委派內容，
後者說 -02 是觸控面分支。

請回報 **037 之 `SWE1-HVAC-080-01`／`-080-02`／`-081-01`／`-081-02`
四個 leaf 之 Requirement Description 全文**（不截斷）。

- 若 -02 確為觸控面分支 → 依 §2 修法辦理
- 若 -02 確為委派內容 → `duplicate_of` 仍移除，但 TC 之驗證目標須改為
  該 leaf 之**扣除委派後餘留部分**，並於 `reasoning` 明列委派
  （§8.4.2）；若扣除後無餘留，回報停下，屆時才是 BLOCKED 之候選

**兩種情形下 `duplicate_of` 皆須移除**，故 §2 之修正不必等本項。

---

## 3. DEFECT-3 —— TC-001 之 PC4 為 step-controlled state 且三處重複

> PC4：`[spec-derived] A tab other than the Seats tab is shown on the lower
> screen (13.2)`

**§4.4 明列 step-controlled state 為禁用之 Pre-Condition 類型。**
13.2 之條文未以「當前顯示何 tab」為分支條件 —— 它只說「切到 Seats tab」；
該狀態是為使結果可觀察而設置者，非 spec trigger。§8.5 判定測試落在後者。

且同一事實出現於三處：PC4、procedure 第 1 步（`Note which tab is currently
shown`）、ER 第 1 步（`The tab shown … is not the Seats tab`）——
違反 §4.5「資料只屬於一個欄位」。

修法：刪 PC4。procedure 第 1 步與 ER 第 1 步保留（此為 §5.6 之 baseline
建立與其 ER，合法）。

**TC-002 之 PC4（`The user is not in the climate section`）與 TC-003 之
PC4（`already in the climate section`）不在此列** —— 兩者為 13.2 第二、
第三分支之區辨條件，確為 spec trigger，標註正確。

---

## 4. DEFECT-4 —— TC-005 之 ER1 非可觀察陳述

> ER1：`The lumbar/bolster level is readable`

**「可被讀取」是關於可觀察性之後設陳述，不是被觀察到的結果**（§6：
ER 須 observable、judgeable）。它斷言的是「這個量存在且看得到」，
而那正是本批尚未確立之事（上繳 §7.2 第 2 項自承）。

此措辭之成因是我在 19 §5 禁止假定 UI 元件存在 —— 執行層以模糊化規避假定，
方向對，但落點錯：**規避假定之正解是改用條文自己的動詞，不是改用後設語。**

修法：ER 之措辭錨定 13.3 條文自身之 `reflected`：

| 位置 | 改為 |
|---|---|
| TC-005 procedure 1 | 保留 baseline 步驟，但改記「調整前所顯示之腰靠／側靠狀態」 |
| TC-005 ER1 | 記錄步驟之 ER：陳述調整前之狀態已被記下（不寫 `readable`） |
| TC-005 ER2 | `The popup or the tab change is shown, and the adjustment is not reflected` |
| TC-006 ER | `The adjustment is reflected` |

`level` 一詞僅保留於 **13.6 使用它的地方**（min/max、greyed out、error
tone），不外推至 13.3／13.5 之 ER 主詞。

TC-011／TC-012／TC-014 之 ER 一併依同一原則複查：**凡以 `level` 為主詞而
該節條文未使用該詞者，改用該節自身之動詞。**

---

## 5. NOTE —— ch13 從未說明腰靠／側靠狀態顯示於何處

13.2 ~ 13.6 命名了 `Seat Control Popup`、`Seats tab`、`level`、
`greyed out`、`error tone`，但**未指明調整量顯示於何處**。

登 **A-CF15**（note）：ch13 之可觀察量僅間接可得；13.5 之級距量值由
CFTS044 擁有（19 §4.2），而其顯示位置無任何 spec 明載。
列 RD-1 候選。**不阻塞** —— §4 之修法已使 ER 不依賴該資訊。

若日後實機驗證顯示確無任何可讀之狀態呈現，13.5 方回到 BLOCKED 之候選
（R-C22 之界線）。

---

## 6. 通過、無須修改者

- 13.2 三分支 ↔ 三 leaf ↔ 三 TC，切法沿用 037（§8.2.1）
- 第九軸 source class 逐節判定，措辭取自 13.2 自身而未沿用 6.3 —— 正確，
  且 `spec-derived` 之理由（本節未以一句宣告該配置，係由分支句推得）成立
- stowed／retracted 入 `pre_conditions`：TC-001/002/003 之驗證目標確為
  「該狀態下之行為」，合 19 §2.2 判定測試
- `(-, +)` 之位置分割：`test_item` 照錄、procedure 用 `"-"` / `"+"` —— 正確
- 5 秒 timeout 為條文明載，照用；popup 樣式與 tab 內容不寫 —— 正確
- TC-014 未用「負向」設計方法（上限再按為邊界之合法輸入）—— 判斷正確
- lint 之反向驗證（注入缺陷、六 gate 翻 FAIL、還原回 25/25）
- 九軸複掃之「其餘 85 節未命中不得作為結論」—— R-C13 應用正確

---

## 7. 執行層作業指示

1. 依 §1 修 TC-004，並新增 `proc-min-steps` gate ＋ 反向驗證；
   逐條核對 §10.1／§10.4／§10.5／§10.6 之 gate 覆蓋，補齊並回報補了哪幾個。
2. 依 §2 移除 TC-010／TC-012 之 `duplicate_of`，改填 `distinguishing_axis`。
3. 回報 §2.1 之四個 leaf Requirement Description 全文。
4. 依 §3 刪 TC-001 之 PC4。
5. 依 §4 改寫 TC-005／006 之 ER，並複查 011／012／014。
6. 登 A-CF15，列 RD-1 候選。
7. 全批重跑 lint（含新 gate）與 §9 自評，**僅回報變動項**。
8. **仍不寫回 workbook。**
9. 上繳 `docs/upstream/12_pilot_rev2.md`。git 不執行。

---

## 8. 本包產生之新條文清單（自檢）

無新條文。§1.1 之 gate 覆蓋要求為既有 §10 之落實，非新規則。
