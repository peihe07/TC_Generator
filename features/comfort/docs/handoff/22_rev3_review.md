# 22 — Comfort HMI / rev3 覆核：第六項發現、marker 白名單、R-C25

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/13_pilot_rev3.md`
- 判定：BLOCKED row 處置**通過**；ER 主詞修正**通過**。
  **defect ×1（TC-014），須 rev4。** 另採納 marker 白名單。

---

## 1. DEFECT-6 —— TC-014 之 PC3：同一形態第四次出現

> PC3：`[spec-derived] The lumbar/bolster level is already at its maximum (13.6)`
> procedure 1：`Press "+" repeatedly until the lumbar/bolster stops increasing`
> ER1：`The lumbar/bolster is at its maximum level`

**同一事實出現於三個欄位。** 與 rev1 之 TC-001 PC4、TC-004 PC2、
TC-005 setup 為同一形態，本輪為第四次。

### 1.1 本例比前三例難判，故須寫成條文

前三例之狀態非 spec 分支條件，直接落入 §4.4 之禁用類型。**本例不同**：
13.6 之行為就是「到達上下限後再按 → error tone」，**該狀態確為 spec 定義之
trigger condition**，合 §8.5 之例外，PC3 之標註本身沒有錯。

問題不在資格，在重複。

```
R-C25  §8.5 例外賦予資格，§4.5 決定落點

某狀態為 spec 定義之 trigger condition 者，依 §8.5 例外**取得**進入
pre_conditions 之資格。該資格不等於落點 —— §4.5 仍要求同一事實只出現於
一個欄位。

當該 TC 自身之步驟無論如何都必須建立該狀態時（§7 FF：include setup,
don't assume hidden state），落點為 test_procedure，pre_conditions 不再
重複陳述。

判定順序：先問「這是不是 spec trigger」（§8.5，資格），
再問「誰建立它」（§7／§4.5，落點）。兩問答案可以是「是」與「procedure」，
兩者不衝突。
```

**修法**：刪 TC-014 之 PC3。procedure 步驟 1 與 ER1 保留 —— 它們是
§7 FF 所要求之 setup 及其可觀察確認。

### 1.2 這回答了 §9.2 第 2 項

執行層問「其餘 12 條是否另有未察之 defect」。**有，即本項。**

且它與執行層自陳之「**改動點不等於審視點**」互為佐證：TC-014 之 PC 區塊
rev2、rev3 皆未被改動，故三輪皆未被重讀。前者是「改過所以以為看過」，
後者是「沒改過所以沒看」—— 兩者都不是「看過而判斷錯」。

---

## 2. marker 白名單 gate —— 採納（§9.2 第 3 項）

執行層問是否需要。**需要，且理由比它所述更強。**

`[BLOCKED-SPEC]` 現為 **lint 豁免之觸發器**：掛上它，`proc-min-steps` 與
`proc-er-1to1` 即不適用。**任何可自行取得之豁免，等於沒有豁免條件。**

```
R-C26  觸發 lint 豁免之標記須經白名單

凡標記之出現會使某列免受一個或多個 lint gate 檢查者，其得使用之 tc_id
須列於 profile 之具名白名單。

gate 檢查：列帶該標記而 tc_id 不在白名單 → FAIL。
白名單之增列須經裁定（profile §5「新增 marker 須先裁決」之延伸：
不只新增 marker 須裁，既有 marker 之新增使用者亦須裁）。

理由：豁免若可自我授予，其條件即不成立。此與「豁免須為具名回報行、
不得為條件式中之靜默跳過」（R-C24）互補 —— 後者使豁免可見，
本條使豁免不可自取。
```

白名單初值：`NR1L-ComfortHMI-010`、`NR1L-ComfortHMI-012`（profile §5.1
已具名，直接引用）。gate 名 `marker-whitelist`，須反向驗證。

---

## 3. 通過、無須修改者

- **BLOCKED row 六欄**：procedure/ER 空、`spec_ref` 照填、Remarks marker
  為開頭 token 且無 ruling id、`split_flag` 復位、`distinguishing_axis`
  移除 —— 全數正確
- **`blocked-row-empty`（空非短）與 `blocked-remarks` 兩個自加 gate** ——
  採納。「只做豁免會讓 BLOCKED row 變成不被任何檢查覆蓋的洞」之診斷正確；
  豁免一個 gate 的同時補兩個，方向對
- **三種反向驗證**，含「非 BLOCKED 單步仍 FAIL」（豁免未擴散）—— 正確
- **profile §5 三者對照表**（`[BLOCKED-ECU]`／`[BLOCKED-SPEC]`／R-C16 缺口
  項）：三者外觀相近而成因不同，寫成可查的表是必要的。「見到空 procedure
  時須讀 Remarks 之 marker 方知類別」一句尤其該留
- **ER 主詞**：獨立複核 12 條，現全為系統可觀察之物
  （`is shown`／`is reflected`／`is increased`／`is greyed out`／`is played`）。
  被動語態不構成問題 —— 主詞是狀態，不是觀察者
- **§9 自評依 R-C23 重做後兩項轉部分 N/A** —— 這是 R-C23 之正確用法：
  它改變的不是判定對錯，是**判定的粒度**。「14 條一律 PASS」掩蓋了
  「其中 2 條根本沒有 procedure 可判」
- **DATA_REQUESTS #16 與 #13／#14 之區別**（要不要取得 vs 有沒有人驗）——
  區分正確。「範圍界定只說明不由 Comfort 驗，不保證有人驗」一句成立

---

## 4. 一句給日後 —— 用詞禁令 vs 判準

執行層 §3.3 之自我分析值得保留於 `RUNBOOK.md`：

> rev1 是 `is readable`，rev2 是 `is recorded`，兩者都把主詞放在觀察者身上。
> 我 rev2 改的時候，以為問題是「readable 這個字」，實際問題是「ER 的主詞是
> 誰」—— 換字沒有換主詞，所以錯誤原樣搬了家。
> **用詞禁令我可以繞過而不自知，判準不行。**

此與 R-C13（零命中須換路徑而非下結論）、R-C18（截斷欄位不得用於判讀）同源：
**以表徵為判準者，其失敗形態是靜默的。**

---

## 5. 執行層作業指示（rev4）

1. R-C25、R-C26 原文貼入 `RULINGS.md`。
2. 刪 TC-014 之 PC3（§1.1）；procedure 與 ER 不動。
3. **全批複查 §4.5 之三處重複形態**：凡同一事實同時出現於
   `pre_conditions` 與 `test_procedure`（或其 ER）者，依 R-C25 判定落點，
   回報檢出幾條、哪幾條、如何處置。**此為 R-C25 之首次全批適用。**
4. 加 `marker-whitelist` gate（§2），白名單取 profile §5.1 之二列，
   反向驗證：未列白名單之 tc_id 掛 marker → FAIL。
5. §4 之「用詞禁令 vs 判準」寫入 `RUNBOOK.md`。
6. 全批重跑 lint 與 §9 自評（依 R-C23），僅回報變動項。
7. **寫回之準備，但不執行 splice**：
   - 產出 write-back **dry-run** 報告（依 canon §6／profile [OVERRIDE]
     檢查表；BLANK 型為 append from first data row，首列 row 10）
   - 報告須含：目標列範圍、每欄之填入值與留白欄之具名清單、
     BLOCKED row 兩列於 xlsx 內之呈現（空欄與 Remarks 長字串之換行行為，
     §9.2 第 1 項）
   - **不呼叫 `xlsx_surgical` 之寫入路徑**，不產生新檔，
     `DELIVERY.sha256` 不增列
8. 上繳 `docs/upstream/14_pilot_rev4_and_dryrun.md`。git 不執行。

**寫回之實際執行須 Pei 裁定**（交付形式、位置、送達屬 Tier 3），
於 dry-run 覆核通過後另行下放。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C25 §8.5 例外賦予資格，§4.5 決定落點 | ✅ §1.1 | 已簽 2026-08-15 |
| R-C26 觸發 lint 豁免之標記須經白名單 | ✅ §2 | 已簽 2026-08-15 |

兩條適用全 feature，安置位置待 canon re-sync。
