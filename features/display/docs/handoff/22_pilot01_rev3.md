# 下放包 22 —— #1 亦受 A-DM33 波及：popup 側須分離 deferred

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/22_pilot01_rev3.md`
- **本包對交付物之推進：pilot-01 rev3（收斂為可交付之三條）**（R-G31）
- **前置（已查證）**：上繳包 21 已回；`generated/pilot-01.json` 三筆
  （#1／#4／#3）；lint 二十項行計 0；停止條件 53–55 皆 0；
  A-DM33／DR-DM10 已登記

---

## 一、上繳包 21 之覆核

**核可，處置正確。** 三項具名，一項退回（§二）。

### 1.1 A-DM33 是本 feature 至今最重要的一項發現

`1.11.2.2` 之逐字全文顯示**兩組互斥之關閉流程，兩組皆宣告適用於
`R1H` / `Atlantis High`**：

| | 組 A `{4820282}`–`{4820288}` | 組 B `{4820289}`–`{4820292}` |
|---|---|---|
| 誰關背光 | HU 判定後送 `[DISP_OFF]`＋`[0% Intensity]`，DCSD 收到才關 | DCSD 越過門檻**即**關 |
| 警示階段 | **有**（`has finished displaying the Display Hot warning screen`） | **無** |
| 關背光後之 `$DCSD_DISP_STAT$` | `continue to send … [DISP_HOT]` | `Send … [DISP_OFF]` |

**這不是措辭差異，是兩個不同的狀態機。** 執行層不代為裁定而開
DR-DM10(a)，正確 —— 上游文件之內部矛盾屬 Tier 2。

### 1.2 自我推翻第一版理由

A-DM33 初稿寫「三組條款皆適用且互不一致」，逐條讀屬性行後改為
「兩組適用且互相排斥，第三組之 DCSD 側為 `Radio:noSys`」。
**結論不變（#2 仍 deferred），理由改變**，並依 R-G19 於四處分別更正留註。

R-G19 立條之後第三次生效，且這次是在**同一份文件之撰寫過程中**攔下。

### 1.3 §八三項自陳 —— 逐項處置

| # | 自陳 | 分析層之判定 |
|---|---|---|
| 1 | `framework.md` 與 037 之一致性未經複驗；本輪只驗了「TC 與 framework 一致」 | **成立且重要**。前者為真不蘊涵後者。列為寫回前之閘（§四步驟 5） |
| 2 | `4 (DISP_HOT)` 未於本輪重跑解析鏈；「綁定未變則結果應同」是推論 | **成立**。腳本為確定性且綁定 11/11 MATCH，故本輪不重跑；**但列入寫回前之閘**（§四步驟 5），屆時與 #1 之值逐字比對 |
| 3 | #4 之「No popup is shown」無正面出處，係自「觸發條件未成立」推得 | **判定可寫**，見 §三 R-DM49 |

第 3 項之自陳最值得記：

> 本層判其可寫（否則一切負向條皆不可寫），但記明它與 ER 1／ER 2 之
> 證據強度不同。兩者不可兼得時，選擇留下並揭露。

**這是正確的處置，而它需要一條條文把它變成規則而非個案。**

---

## 二、退回：#1 之 popup 側亦受 A-DM33 波及

### 2.1 執行層之 deferred 範圍界定漏了 #1

上繳 21 §2.3 判「#3 不受影響」（正確 —— 兩組對回復側無分歧），
但**未檢 #1**。分析層檢之，結論：**#1 之 ER 3 受組 A／組 B 之矛盾直接波及。**

#1 之 ER 3 為：

```
3. The popup "Screen is Hot. Display brightness has been reduced." is displayed for 10 seconds
```

該 ER 成立之前提是：**越過門檻後，顯示仍亮著，使 popup 看得見。**

而組 B 之 `{4820289}` 逐字為：

> `When the DCSD Display transitions to a Hot state (> 85 degrees C) from a
> non-Hot state (<= 85 degrees C), and if there is no high priority screen
> (RVC), then DCSD shall: … Turn off the backlight (both top and bottom
> portion) and disable touch.`

**若組 B 為準，越過門檻之同時背光即關 —— 一個看不見的 popup 顯示
十秒，其 ER 不可觀測。** #1 會在組 B 之實作上恆為 fail（False Fail），
而在組 A 之實作上通過。

**這與 #2 被 deferred 是同一個原因，只是我在 21 包只指出了 #2。**

### 2.2 #1 之哪一部分仍可寫

逐項檢 #1 之三行 ER 對兩組之相容性：

| ER | 內容 | 組 A | 組 B | 判定 |
|---|---|---|---|---|
| 1 | 進入 Hot state | 一致 | 一致 | **可寫** |
| 2 | `$DCSD_DISP_STAT$ = 4 (DISP_HOT)` 收到 | `{4820282}` 明載 | `{4820289}` 明載 | **可寫**（兩組皆同） |
| 3 | PU0517 顯示十秒 | 蘊含（有警示階段） | **矛盾**（背光已關） | **deferred** |

即 **#1 之訊號側可交付，popup 側須分離。**

### 2.3 處置：#1 收斂，popup 側另立 deferred 項

1. **#1 之 ER 3 與 procedure step 3 移除**，收斂為兩步兩 ER
   （進入 Hot state ＋ 送出 `4 (DISP_HOT)`）。
   `specification_reference` 維持 `{4820282}`＋`{4820289}`
   （兩者皆為其直接驗證之節）。
2. **`tc_title` 隨之改寫** —— 現行 `Hot threshold exceeded → thermal
   warning popup displayed` 已不符其 ER。改為指向訊號通知之標題
   （由執行層擬，須合 §4.3 三形之一、2–14 字、與 #4 之 sibling token 相異）。
3. **`test_item` 括號下半隨之改寫**，且**不得與 #4 之括號下半逐字相同**
   （lint I-sibling）。
4. **新增 deferred 項**入 `batch_context.md` 之 `deferred` 陣列：

   ```
   SWE1-DM-004 之 warning popup（PU0517）—— DR-DM10(a) 未結。
   組 B {4820289} 於越過門檻時即關背光，使 popup 之顯示不可觀測；
   組 A {4820283} 則蘊含警示階段。兩組皆宣告適用於 R1H / Atlantis High。
   ```

5. **`DATA_REQUESTS.md` 之 DR-DM10 其「阻斷範圍」欄增列
   `SWE1-DM-004 之 popup 側`** —— 現僅列 005。

### 2.4 收斂後之覆蓋揭露

leaf `SWE1-DM-004` 之需求文逐字含
`shall trigger warning popup requests` —— **該面向於本批不再被驗證**。
須於 `batch_context.md` 明記為**已知覆蓋缺口**，不得以「#1 已涵蓋 004」
帶過。

pilot-01 rev3 之三條為：#1（004 訊號側）、#4（004 邊界負向）、
#3（005 回復側）。**004 之 popup 側與 005 之關閉側皆 deferred。**

---

## 三、裁決條文

```
R-DM49（負向條之 ER：「不發生」得自觸發條件未成立推得）
負向／邊界條之 ER 若為「某事不發生」（無 popup、訊號不為某值、
狀態不轉換），其證據形態與正向條不同：規格通常只寫「條件成立時
做什麼」，不寫「條件不成立時不做什麼」。

**判定：可寫。** 但須滿足三項：
(a) 其所否定之行為，其**正向出處逐字存在**（即「條件成立則發生」
    有明確出處），否定係自「條件未成立」推得；
(b) 該否定**不得引入任何新的值**——只能否定正向所載之值
    （✓ `is not 4 (DISP_HOT)`；✗ `should be 0 (OFF)`，後者需 DR-DM9）；
(c) 於 `reasoning` 或 `split_reason` 記明其證據強度與正向 ER 不同。

理由：若不許此形態，則一切負向條皆不可寫，而 canon §9 第 11 項
與 §7 明文要求 supported 配負向。兩項要求不可兼得時，
**選擇留下並揭露**，不選擇沉默移除。

實例（上繳 21 §八第 3 項，執行層自陳）：#4 之
`No popup is shown on the display`——`{4820289}` 只說越過門檻時
做四件事，未說未越過時不做。執行層判其可寫並記明證據強度差異，
本條將該處置定為規則。
```

---

## 四、作業步驟

1. 抄錄 §三 R-DM49 入 `features/display/RULINGS.md`（獨立核對表）。
2. **依 §2.3 收斂 #1**：移除 ER 3 與 step 3、改寫 `tc_title` 與
   `test_item` 括號下半、更新 `batch_context.md` 之 `deferred`
   與已知覆蓋缺口、更新 `DATA_REQUESTS.md` 之 DR-DM10 阻斷範圍。
3. 重跑逐條 §9 自檢十七項（三條）與 `lint036.py`（整批，附母體）。
   **特別複驗 lint I-sibling**：#1 與 #4 同為 `SWE1-DM-004`，
   其括號下半改寫後仍須非逐字重複。
4. 依 R-DM49(c) 於 #4 之 `split_reason` 補記其證據強度差異。
5. **寫回前之閘（本輪執行，結果附上繳；仍不寫回）**：
   (a) `framework.md` 之 Layer 2 四組對 037 之 8 leaf 逐字複驗
       —— 涵蓋 8／相異 8／無重複無遺漏，且各組名稱與 `DECISIONS.md`
       簽核第 2 項逐字相符
   (b) 重跑 `signal_resolution.py`，`$DCSD_DISP_STAT$` 之
       `4 (DISP_HOT)` 與 #1 之 ER 逐字比對
6. 更新 `docs/INDEX.md`。

**仍不寫回 036 母本。**

---

## 五、停止條件

沿用 1–55，另加：

56. 步驟 5(a) 之複驗若 framework 與 037 之對應非 8／8 → 停並回報。
57. 步驟 5(b) 之重跑若得出與 `4 (DISP_HOT)` 不同之值 → 停並回報，
    **不得逕以任一方為準**。
58. 收斂後之 #1 若其 ER 仍含任何依賴「顯示為亮」之觀測 → 停
    （組 B 下不可觀測）。

**全部 git 操作屬 Pei。**

---

## 六、上繳包要求（`docs/upstream/22_pilot01_rev3.md`）

1. R-DM49 之抄錄核對表
2. 收斂後之 #1 全文，及 `tc_title`／括號下半之改寫理由
3. `batch_context.md` 之 `deferred` 與已知覆蓋缺口全文
4. 三條之 §9 自檢十七項
5. `lint036.py` 全文輸出（整批，附母體；I-sibling 具名）
6. 步驟 5 兩項閘之輸出
7. 未驗項分流（A／B，R-G29）
8. 建議之 commit 訊息與 pathspec（不執行）
