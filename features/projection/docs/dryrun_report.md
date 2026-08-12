# Dry-run report — Projection (`FULL_REFINE`)

> 執行：2026-08-12 · 依 Phase 6 下放包之五項檢查表（R-P53）
> 基準：`inputs/NR1L_GEN1(HDCC)_Ver_20260813.xlsx` SHA256 `11579c9b3b8e56eb…`
> **未寫回 xlsx、未修改任何 TC、未執行 git 操作**
>
> **判定：FAIL — 四項不通過，須先處置後重跑**

掃描條件（R-P41）：比對範圍為 `TestResults` 全 36 欄；正規化採
`lint_defs.norm()`（collapse whitespace runs），與 L-PJ4 雜湊實作同一實作
（R-P49）。修訂後狀態由 11 份批次 JSON 疊加產生，涵蓋 558/558 列。

---

## 摘要

| 項 | 結果 | 說明 |
|---|---|---|
| D-1 | ⚠️ **條件不符** | 6 列 ER 變更為 R-P12 授權之 L-PJ4 窄口，但 D-1 之通過條件未涵蓋 |
| D-2 | ⚠️ **同上 + 41→40** | 凍結欄除窄口 6 列外全數不變；`Test Case Author` 待補為 **40 列非 41** |
| D-3 | ✅ PASS | 559 → 558，僅刪 r562，無任何列移動 |
| D-4 | ❌ **FAIL** | 刪除 r562 使 `SWE1-PROJ-227` 失去唯一追溯列 → 未覆蓋 leaf 7→**8**，補列 6→**7** |
| D-5 | ✅ PASS | 73 列「正確地不動」，**無編號可指者 0** |
| §3 附帶 | ❌ **2 項不符** | L-PJ9 基線 15→**17**；L-PJ1 **2 列未解析** |

---

## D-1｜diff 只落在兩個可編輯欄

**變更列 63，變更欄位分布：**

| 欄 | 變更列數 |
|---|---|
| `Pre-Conditions (I)` | 23 |
| `Test procedure (K)` | 42 |
| **`Expected Result (L)`** | **6** |

超出 `{I, K}` 者 **0 列**（不計 ER）。

### ⚠️ D-1 的通過條件與 R-P12 衝突

D-1 寫「有變更之欄位 ⊆ `{I, K}`」「**任何其他欄出現變更即 FAIL**」。但
**r424–r429 這 6 列的 ER 變更是 R-P12 明文授權的 L-PJ4 窄口**（純刪除
`correctly`，白名單詞，記於 `data/er_narrow_gate.log.json`）。

依 D-1 字面即 FAIL；依 R-P12 則為合規。**未自行調和** —— 建議 D-1 之通過
條件修訂為：

```
有變更之欄位 ⊆ { Pre-Conditions (I), Test procedure (K) }
              ∪ { Expected Result (L) 之 L-PJ4 窄口列，且該列須見於 er_narrow_gate.log }
```

---

## D-2｜34 個凍結欄逐列雜湊

凍結欄數 **34**（36 − I − K）✅

| 檢查 | 結果 |
|---|---|
| 五個 build 執行結果欄（30–34）變更 | **0** ✅ |
| `Test Item` / `Input Test Data` / `Specification Reference` | **0** ✅ |
| ER 欄以外之全部凍結欄 | **0** ✅ |
| ER 欄（12） | 6 列（同 D-1，窄口） |

### ⚠️ R-P19 的兩條款互相作用：41 → 40

R-P19 定「`Test Case Author` 空白 41 列補為 `PeiPYHsu`」與「第 562 列殘樁
刪除」。**r562 本身就是那 41 列的第 41 列**（其 `Test Case Author` 為空）。

```
含 r562 之空白作者列  41  ← Phase 0 recon 記錄值
刪除 r562 後          40  ← 實際待補
```

**實際待補為 40 列**：r272–r294（23）、r360–r367（8）、r370–r375（6）、
r436、r560、r561。未自行調和，待裁。

---

## D-3｜列數與列序 ✅ PASS

```
資料列   559（r4–r562） → 558（r4–r561）
刪除     r562 唯一
```

**r562 刪除證據**：九個 TC 內容欄（Test Set / Pre-Conditions / Procedure /
Expected Result / Specification Reference / Priority / Design Method /
Functional Safety）**全空**，僅餘 7 個非空欄（seq 559、Polarion id、req id
`SWE1-PROJ-227`、Test Group、Test Item、Input Test Data `NA`、tc_ref_id）。

**無任何列被移動**：本 pipeline 之寫回策略為逐欄原地改寫，63 個變更列全部
in-place，列索引不變。

---

## D-4｜未覆蓋 leaf 補列 ❌ FAIL

**刪除 r562 使 `SWE1-PROJ-227` 成為未覆蓋 leaf。**

`SWE1-PROJ-227` 在全簿只出現於 **r562 一列**，而該列正是 R-P19 要刪除的殘樁。
刪除後：

```
未覆蓋 leaf   7 → 8
  原 7：133 / 146 / 167-001 / 167-002 / 184 / 190 / 195
  新增：227
補列          6 → 7   （R-P18 仍排除 146）
```

**這牴觸完整性不變式** —— canon §5：「Every leaf gets a row: TC rows, or
BLOCKED placeholder rows（completeness invariant, **both directions**）」。
r562 雖無 TC 內容，卻是 `SWE1-PROJ-227` 唯一的追溯列；刪掉它等於讓一條 leaf
在簿中完全消失。

**兩種可能處置（未自行選擇）**：

| 選項 | 內容 | 代價 |
|---|---|---|
| (a) | 保留 r562，改以 `BLOCKED` 佔位列處理 | R-P19 之刪除條款須撤回；列數維持 559 |
| (b) | 照刪，並將 `SWE1-PROJ-227` 併入表尾補列（6 → 7 條） | 需為 227 撰寫可通過 gate 的 TC，其 Test Item 為 External Accessory (EA) framework，來源充足性未評估 |

**補列內容尚未產出** —— 本階段依 §0.2／§0.3 不寫回、不修改 TC，故 D-4 現況
為「規格已確認、內容未產出」。6（或 7）條補列之撰寫需另行下放。

---

## D-5｜阻塞列 ↔ 依據編號 ✅ PASS

掃描 558 列，「正確地不動」**73 列**，**無編號可指之列數 = 0** ✅

引用之依據編號 19 種，主要分布：

| 編號 | 列數 | | 編號 | 列數 |
|---|---|---|---|---|
| `A-PJ45` | 42 | | `A-PJ50` | 4 |
| `L-PJ7` / `R-P11` | 9 / 9 | | `DR#13` / `R-P42` / `R-P46` | 4 / 4 / 4 |
| `A-PJ39` / `L-PJ9` | 7 / 7 | | `A-PJ44` / `O-3` / `A-PJ40` / `R-P43` / `L-PJ4` | 3 各 |

完整之「列號 → 依據編號」對照表：`/tmp/d5.json`（可依需要落檔至
`features/projection/data/`）。

**群組加總 86 vs 不重複列數 73** —— 差額 13 為重疊列（同列同時屬多群組，例如
r376–379 同時屬 `frozen` 與 `PCTS`）。下放包 §2 已預告此情形，上繳表以列為
單位，未以群組加總代替。

---

## §3 附帶驗證

### 八項基線 —— 6 項符合、1 項不符

| Gate | 預期 | 實測 | |
|---|---|---|---|
| L-PJ5 禁詞 | 1 | **1** | ✅ |
| L-PJ6 模糊語 | 4 | **4** | ✅ |
| **L-PJ9 泛稱工具** | **15** | **17** | ❌ |
| L-PJ10 缺陷類 / 參數類 | 5 / 8 | **5 / 8** | ✅ |
| 交叉指涉 | 30 | **30** | ✅ |
| 步數 != ER 例外 | 3 | **3** | ✅ |
| 前向循環指涉 | 0 | **0** | ✅ |

### ❌ 發現一：L-PJ9 由 15 增為 17 —— **改善造成的迴歸**

新增命中 **r177 / r188**（Day/Night Mode）。成因是 **B2 的修訂本身**：

```
修訂前 PROC：3. Trigger $Day_Night_Mode$ = Night via CAN tool, record T1 …
修訂後 PROC：3. Send CAN: BCM_FD_27.DAY_LGT_MD_DISP = 0 (Night), record T1 …
```

`CAN tool` 這個字串在 `RE_NAMED_TOOL` 內。B2 把步驟寫得更精確時**消掉了
「CAN tool」四個字**，於是 L-PJ9 的第二條件（Procedure 有具名工具）由 True
翻為 False，兩列因 PRE 的 `A screen capture tool (60 fps or higher)` 而被
flag。

**這兩列的 PRE 泛稱是真的**（`screen capture tool` 未指明何種工具），
修訂前被 `CAN tool` 遮住而未浮現。所以嚴格說 L-PJ9 現在的 17 才是正確值，
15 是被遮蔽的結果 —— 但基線變動須經裁決，未自行更新。

### ❌ 發現二：L-PJ1 誤判 PROXI 配置字為 CAN 訊號 —— **B9 修訂引入**

r270 / r271 的 Procedure 經 B9 修訂後含
`Model matching Car_Configuration_15.Vehicle_Line_Configuration`。該字串含
點號，**L-PJ1 的 `{MESSAGE}.{Signal}` 正則將其當作 CAN 訊號**，於 DBC ∪
VF176 皆解析失敗 → 2 列 ABORT。

r272 未命中，因其 PROC 無該字串（僅 PRE 有）。

**這是 B9 修訂引入的缺陷**：把 PROXI 配置字的完整點號形式寫進 Procedure，
與 CAN 訊號的書寫形式撞型。**兩種可能處置（未自行選擇）**：

| 選項 | 內容 |
|---|---|
| (a) | L-PJ1 正則排除已知之 PROXI 配置字（`Car_Configuration_15.*` 等 group.name 形式） |
| (b) | Procedure 內改寫為不含點號之形式（如 `the Vehicle_Line_Configuration PROXI value`），PRE 保留完整名 |

### 其餘附帶項

| 項 | 結果 |
|---|---|
| lint L-PJ1 全簿 | ❌ 2 列（見上） |
| `er_divergence.json` | **35 列，增量 0** ✅ |
| 進度校驗 | `558 = 516 已處理 + 42 阻塞` ✅ |
| 變更列總數 | **63** |

---

## §5 第 6 項｜本表與 canon §6 之差異是否有遺漏之驗證面向

執行層之獨立判斷，逐條列出。**本表五項未涵蓋，而本 feature 確實需要驗的**：

### M-1｜新列（D-4 補列）不受 D-1／D-2 保護

D-1／D-2 驗的是「既有列的凍結欄未變」。**補列是全新的列，34 個凍結欄的值
都是新寫的**，不在任何雜湊比對範圍內。目前唯一的約束是 D-4 的「須通過
L-PJ1~L-PJ10」與「Test Group / Test Set 值域一致性」。

建議增列：補列之 `Priority` / `Design Method` / `Functional Safety` 須取自
既有值域（`下拉選單` 9 個設計方法字串、Priority P0–P3），且
`Specification Reference` 須指向 `inputs/` 內存在的文件與可解析的章節錨點。

### M-2｜`er_divergence.json` 只驗總數，未驗內容仍成立

§3 驗「35 列、增量 0」。但 B2／B9／B10′ 修訂後，**部分列的 Procedure 已改為
匯流排實名，其與 ER 的分歧內容因此改變**（例如 r167/r168 由
`$FuelLvlLow$ = Active` 改為 `STATUS_BH_BCM1.LowFuelWarningSts = 1 (ON)`，
ER 仍寫舊寫法）。列數不變不代表分歧描述仍正確。

建議增列：`er_divergence.json` 之每列 `proc_excerpt` 須與修訂後的 Procedure
一致，否則 RD-1 會拿著過期的描述去問。

### M-3｜`data/` 產物與修訂後狀態的一致性未驗

`signal_map.json`、`pcts_evidence.json`、`layer3_gate.json` 等 13 份 artifact
是 Phase 0–5 的中間產物。dry-run 未驗證它們是否仍與修訂後的簿子一致 ——
例如 `signal_map.json` 的 `workbook_rows` 計數是修訂前的 token 出現列數，
修訂後多數 token 已解析消失。

建議增列：交付前標明哪些 artifact 是「修訂前快照」（不需更新，作為歷史證據）
與哪些須同步（供 Phase 7 使用者）。

### M-4｜Test Case Framework 分頁未驗

`feature.yaml → write_back.fill_test_group_set: false`，故 G/H 欄不寫。
但該簿有 `Test Case Framework` 分頁（Phase 0 recon 記錄 9 個分頁之一），
本表未要求驗證該分頁是否需同步或維持不變。

建議增列：`Test Case Framework` 分頁納入 D-2 之凍結範圍（或明文排除並說明）。

### M-5｜D-2 未涵蓋 `BugList` 以外的其他分頁

D-2 明列「`BugList` 分頁全表」，但該簿共 **9 個分頁**：`TestProgress`、
`Cover_old`、`ChangeHistory_old`、`QS Suggestion`、`下拉選單`、`TestResults`、
`Reference`、`BugList`、`Test Case Framework`。

建議增列：**除 `TestResults` 外之 8 個分頁全部雜湊不變**，而非只點名
`BugList`。

---

## 判定與後續

**FAIL** —— D-4 為實質不通過（完整性不變式），另有 D-1／D-2 之條件衝突與
§3 之 2 項不符。依 §0.4 停下回報，**未自行修復**。

待處置清單：

| # | 項目 | 需要的裁決 |
|---|---|---|
| 1 | D-4：`SWE1-PROJ-227` 因 r562 刪除而失去追溯 | 選 (a) 保留 r562 或 (b) 補列 7 條 |
| 2 | D-1／D-2：L-PJ4 窄口 6 列之 ER 變更 | 修訂 D-1 通過條件 |
| 3 | D-2：`Test Case Author` 待補 40 非 41 | 確認 R-P19 之列數 |
| 4 | §3：L-PJ9 基線 15 → 17 | 確認新基線 |
| 5 | §3：L-PJ1 誤判 PROXI 點號形式（r270/r271） | 選 (a) 改 gate 或 (b) 改寫法 |
| 6 | M-1 ~ M-5 五項建議增列 | 是否納入檢查表 |

**DR#14 (b) 仍未答覆** —— 42 列在 D-5 中以 `A-PJ45 / DR#14` 為依據，形式上
合格，但依 §4 dry-run 不得在其答覆前判為 PASS。本次因 D-4 已 FAIL，
CONDITIONAL PASS 的前提不成立。
