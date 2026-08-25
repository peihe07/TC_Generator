# 上繳包 30 —— batch 3（`Power Transitions`）、`PENDING-ON-DR` 登記簿、`DR-PMH8` 四五問

- 日期：2026-08-25
- 下放包：[handoff/30_batch3.md](../handoff/30_batch3.md)
- **零寫回工作簿**；`workbook_state = BLANK` 未變

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH113～115 **3/3 逐字相符**，命中數各 1 |
| 2 `DR-PMH8` 增問 | **Q4 ＋ Q5**（Q5 另立而不併入 Q4，理由見 §2），新 SHA256 `cbcd34eb07cc5352` |
| 3 `PENDING-ON-DR` 登記簿 | **8 筆**（下放包要求至少 3），四欄齊備，第 (3) 欄逐值列出 |
| 4 **batch 3 之產出** | **6 條 TC 自 5 leaf**，lint **32/32 PASS**；**7 leaf 中 2 leaf 停手並登記** |
| 5 章 9 之規格側全枚舉 | **已做完** —— 章 9 之 30 行全數逐行判定（非只 12 行關鍵詞命中） |
| 停止條件 7／8／9 | **全未觸發** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH113 | batch 3 之限定授權 | 609 | `b64fcc9f090e5e62` | `b64fcc9f090e5e62` | 1 | ✅ |
| R-PMH114 | A-PMH24 併入 `DR-PMH8` | 357 | `4c809f779bd6a6bc` | `4c809f779bd6a6bc` | 1 | ✅ |
| R-PMH115 | `PENDING-ON-DR` 登記簿 | 623 | `b97321495dec10ba` | `b97321495dec10ba` | 1 | ✅ |

---

## 2. `DR-PMH8` 之 Q4 與 Q5

**Q4**（R-PMH114 之逐字）已抄入，未改一字。

**Q5（覆蓋缺口）另立而不併入 Q4 之後段** —— 下放包步驟 2 令「由執行層擇一並載理由」。
**理由**：二者之**型別不同** —— Q4 問**兩個術語是否同指**（`DR-PMH7` 之類），
Q5 問**一個無需求之行為該如何**（`DR-PMH6` Q2 之類）。
**併問會使二者之答覆難以分辨**：上游若只回一句「是同一個」，Q5 仍未答而我方可能誤以為已答。

`DR-PMH8` 現有 **5 問 ＋ 首段之更正句**，新 SHA256 `cbcd34eb07cc5352`，
**狀態維持 `DRAFT`，`SENT` 欄留空**。

---

## 3. `PENDING-ON-DR` 登記簿（R-PMH115）—— **8 筆**

| # | 判定之所在 | 所繫之 DR |
|---|---|---|
| 1 | 矩陣 `r15` × `PM1)` 之記法（`待定義`） | `DR-PMH5`(1)(2)／`DR-PMH7` Q1／`DR-PMH8` Q4 |
| 2 | batch 2 六條因 `r46`／`r47` 而納入之限定 | `DR-PMH7` Q2 |
| 3 | `-013` 之「一日」與 `-011` 之設定路徑 | `DR-PMH8` Q1／Q2 |
| 4 | A-PMH23（告別音跨螢幕同步）與 `-010` | `DR-PMH8` Q3 |
| 5 | batch 3 之 Pre-Condition（R-PMH113） | `DR-PMH8` Q5 |
| 6 | 矩陣 `r6`／`r24`／`r25` 之 `待定義` | `DR-PMH7` Q1 |
| 7 | batch 3 全部斷言是否須依 R-PMH94 重掃 | `DR-PMH5`(1)(2) |
| 8 | 規格 p4 之 `Note:` × batch 3 之斷言（`待定義`） | `DR-PMH7` Q3 |

**第 (3) 欄逐值列出**（甲／乙／丙／丁），不寫「須重看」。全文見 `DECISIONS.md`。

> ⚠ **本簿之完整性無任何檢查所保證** —— 其為人工登記，
> **漏登之判定不會出現於此，亦不會有任何東西指出它漏了**。已於簿末具名。

---

## 4. batch 3 —— **6 條 TC 自 5 leaf**，lint 32/32

### 4.1 R-PMH111 之判別法 —— **逐條套用並具名（含「否」者）**

判別法承載於 JSON 之 `p9_dependency` 欄（**不只在 reasoning 之散文裡**）。

| leaf | TC | 判別 | 依據 |
|---|---|---|---|
| `-018-01` | `-016`／`-017` | **否** | 斷言為「head unit 是否維持喚醒／popup 是否顯示」 |
| `-018-02` | `-018` | **否** | 斷言為「更新是否開始、後續 popup 是否被 dismiss」 |
| `-018-03` | `-019` | **否** | 斷言為「後續 popup 是否顯示」 |
| `-018-04` | `-020` | **否** | 斷言為「Charge Now 是否顯示」 |
| `-018-05` | `-021` | **否** | 斷言為「XEV popup 是否顯示、radio 是否關機」 |
| **`-023`（10.5）** | **未產出** | **是** | 見 §4.2 |
| **`-002`（7.1.1）** | **未產出** | 否 | 見 §4.3 |

**產出之 6 條中判為「是」者 = 0 → 停止條件 8 未觸發。**

### 4.2 ⚠ `SWE1-HMI-PM-023`（`PITA8`）**經判別為倚賴 p9，停並登記**

`PITA8` 逐字：`During Key OFF (with no ACC position available), HU power ON, all headunit
functionality is expected to have the same functionality as key on, except for controls that
communicate with modules external to the headunit which are not functional during Key OFF.`

**其謂詞正是 R-PMH111 判別法之標的**：`Headunit` 於
`KEY OFF (No ACC position)` × `HEADUNIT POWER ON` 下之可用程度 ——
**而 p9 同格之逐字為 `Headunit: Full on, some limited functionality`。**

**更直接之證據**：PDF 中本句之**前一行逐字為 `HEADUNIT POWER ON:`** ——
**其為 p9 矩陣之欄標題。** 本句在版面上即掛在該欄之下。

→ **依 R-PMH111 停並登記，不得產出。** 其登記於 `generated/batch03.json` 之 `stopped` 欄。

### 4.3 ⚠ `SWE1-HMI-PM-002`（`SU1.1`）**非因 p9 而停 —— 而它也停了**

R-PMH111 判別為 **否**（其謂詞為「點火關閉時電源鍵所引發之畫面轉換」，非受控對象之可用性）。

**其停手之理由是另一件事**：`SU1.1)` 逐字將行為委於
`based on vehicle architecture. See CFTS009 for clarification.` ——
**CFTS009 非本 feature 所持有之素材**。任何 TC 皆須自行指定
「哪一種架構對應哪一種轉換」，**即造值**（canon §8.4.1）。

**形態同 `SWE1-HMI-PM-028`**（12.2，`Please refer to CFTS009 for complete behavior.`），
該筆經 R-PMH47(a) 判為 out of scope、R-PMH72 裁定不寫入工作簿。

> ⚠ **本筆未經任何裁定。** 我依同一形態停手並具名，**其處置待裁** ——
> 若判其應產出，則須先取得 CFTS009 或裁定一個架構為準。

### 4.4 六條之全文

#### `NR1L-DisclaimerScreen-016` — Head unit stays awake at ignition off to display the pending pop-up

- **leaf**：`SWE1-HMI-PM-018-01`（FROP: Power Management）　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. Power Accessory Delay is set to 0 seconds
3. At least one pop-up from the ignition off list is pending
```

**test_procedure**

```
1. Turn the ignition off and record the head unit power state
2. Read the display and record the pop-up shown
3. Do not interact with the pop-up and record the awake duration
4. Compare the recorded duration with the stated maximum
```

**expected_result**

```
1. The head unit stays awake when the ignition is turned off
2. The pending pop-up is displayed
3. The head unit does not power off while the pop-up is being displayed
4. The head unit stays awake for no longer than 2.5 minutes
```

#### `NR1L-DisclaimerScreen-017` — FOTA pop-up interaction extends the stay awake time up to ten minutes

- **leaf**：`SWE1-HMI-PM-018-01`（FROP: Power Management）　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. A FOTA pop-up is displayed after the ignition has been turned off
```

**test_procedure**

```
1. Interact with the FOTA pop-up and record the interaction time
2. Stop interacting with the pop-up and record when the radio powers off
3. Interact with the pop-up repeatedly beyond ten minutes and record when the radio powers off
```

**expected_result**

```
1. The radio stays awake while the user is interacting with the FOTA pop-up
2. The radio stays awake until the user has not interacted with the pop-up for 60 seconds
3. The radio does not stay awake for more than 10 minutes because of these pop-ups
```

#### `NR1L-DisclaimerScreen-018` — Accepting the FOTA pop-up starts the update and dismisses the later pop-ups

- **leaf**：`SWE1-HMI-PM-018-02`（FROP: FOTA Via Wi-fi）　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA update available pop-up is displayed after the ignition has been turned off
3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle
```

**test_procedure**

```
1. Accept the FOTA pop-up
2. Read the update state and record it
3. Read the display for the FOTA via Wi-Fi and Charge Now pop-ups
```

**expected_result**

```
1. The FOTA update available pop-up is accepted
2. The update starts
3. The FOTA via Wi-Fi and Charge Now pop-ups are dismissed
```

#### `NR1L-DisclaimerScreen-019` — Scheduling or dismissing the update displays the later pop-ups

- **leaf**：`SWE1-HMI-PM-018-03`（FROP: FOTA Via Wi-fi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA update available pop-up is displayed after the ignition has been turned off
3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle
```

**test_procedure**

```
1. Schedule an update time on the FOTA pop-up and read the display
2. Repeat the test, dismiss the update on the FOTA pop-up instead, and read the display
```

**expected_result**

```
1. The FOTA via Wi-Fi and Charge Now pop-ups are displayed after an update time is scheduled
2. The FOTA via Wi-Fi and Charge Now pop-ups are displayed after the update is dismissed
```

#### `NR1L-DisclaimerScreen-020` — Charge Now is displayed after the Wi-Fi configuration pop-up is handled

- **leaf**：`SWE1-HMI-PM-018-04`（FROP: WiFi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA via Wi-Fi configuration pop-up is displayed after the ignition has been turned off
3. Charge Now is applicable on this vehicle
```

**test_procedure**

```
1. Choose to configure Wi-Fi, complete the Wi-Fi configuration and read the display
2. Repeat the test, dismiss the Wi-Fi configuration pop-up instead, and read the display
```

**expected_result**

```
1. The Charge Now pop-up is displayed when the Wi-Fi configuration is complete
2. The Charge Now pop-up is displayed after the Wi-Fi configuration pop-up is dismissed
```

#### `NR1L-DisclaimerScreen-021` — Dismissing the XEV key off pop-ups shuts the radio down

- **leaf**：`SWE1-HMI-PM-018-05`（FROP: EV/PHEV Pages）　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1
- **`source_clause_origin`**：`sys1_export 9.1`　**R-PMH111 判別**：否

**pre_conditions**

```
1. No phone call or projection call is active
2. The vehicle is an XEV on which the Charge Now, Summary and Preconditioning pages are applicable
3. The ignition has been turned off
```

**test_procedure**

```
1. Read the pop-ups shown after ignition off and record them
2. Dismiss the XEV key off pop-ups
3. Read the radio power state
```

**expected_result**

```
1. The Charge Now, Summary and Preconditioning pop-ups are shown
2. The XEV key off pop-ups are dismissed
3. The radio shuts down
```


### 4.5 R-PMH113 之 Pre-Condition —— **位置為 Pre-Condition，非 procedure**

六條之 PC1 皆為 `No phone call or projection call is active`。
**未寫成 `Do not…`** —— 「無通話進行中」是一個**狀態**（canon §4.4），
非測試員之動作（canon §4.5）。**限定之位置由其型別決定，非由前例決定。**

其於 JSON 中以 `pre_condition_limits` 欄承載，**與 procedure 之 `limits` 分開**
（後者為 R-PMH99(c) 之字串檢查所讀，二者之檢查不同處）。

### 4.6 §8.4.1 不造值之三處

| 條 | 未斷言者 | 理由 |
|---|---|---|
| `-016` | **任何逾時秒數** | 權威文本於該處為破句（**A-PMH25**） |
| `-020` | `configuration is complete` 之任何延遲 | 規格未給秒數 |
| `-021` | `Charge Now/Summary; Preconditioning` 為一個或三個畫面 | 規格以 `/` 與 `;` 並列而未言 |

---

## 5. 章 9 之規格側全枚舉（步驟 5）—— **做完了**

下放包令「若其規模允許則做，否則量其行數並具名其未做」。**量之後發現規模允許。**

| 項 | 數 |
|---|---|
| 章 9 之敘述行區間 | **L407–L437** |
| 其非空行（母體） | **30** |
| 關鍵詞（`pop-?ups?`）命中 | **12** |
| **未命中而逐行判定者** | **18** |
| **未判定者** | **0** |

**「落選」類別於規格側亦告消滅**（R-PMH100 之同一原則首次施於規格側）。

`IGNOFF_LINE_VERDICT` 現有 **43** 項（25 關鍵詞命中 ＋ 18 全枚舉），
記法分布 **{'未對照': 18, '待定義': 1, '印證': 24}** —— **牴觸 0**。

> ⚠ **母體為章 9 之 30 行，非 p8–p11 之 235 行。** 其餘章之規格側全枚舉**仍未做**
> （KNOWN-INCOMPLETE 三）。**本次只完成了本批所需之那一章。**

### 5.1 `SU3.)` × batch 3 之斷言 —— **不是新牴觸**

`SU3.)`（`No pop-ups will appear until the disclaimer screen has been removed.`）
與本批之「IGN OFF 之 popup 會顯示」表面上取相反值。**判為 `未對照`，其依據為條件互斥可證**：
`SU3.)` 之相位為**開機序列**，本批之相位為 **IGN OFF**，依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。

**該依據非本包所立** —— 既有之 `popup` 斷言掃描已於 L407 立同一依據（方向相反而依據同一）。
**故其非停止條件 7 所稱之「新的」牴觸。**

### 5.2 一處 `待定義`

L160（`Note: do not show popup again if popup was shown at Radio Off.`）——
其適用範圍未定義（`DR-PMH7` Q3）。依 R-PMH95 記 `待定義`，**已入 `PENDING-ON-DR` 第 8 筆**。

---

## 6. lint 之二項一般化（R-PMH107）—— **檢查項數維持 32**

### 6.1 `source_clause` 之來源檢查

| | 原 | 現 |
|---|---|---|
| 判準 | `source_clause_origin` 之字串**必以 `spec_pdf` 起首** | **`source_clause` 須逐字見於其所宣告之來源** |
| 對 9.1 之效果 | **會把「正確遵守 R-PMH75」判為 FAIL** | 通過 |
| 強度 | 只看欄位字串 | **實際回原文件比對** |

**其首次執行即查出一件事**：batch 1 之四條 `source_clause` 與 `sandbox/spec.txt`
**在字形上不同** —— `vehicle’s` vs `vehicle's`、`Loading…` vs `Loading...`。
**二者為同一份 PDF 之兩種萃取**；差異只在字形，不在字詞。
`_norm_src` 因而於兩側正規化引號與刪節號，**其代價已具名**：
若某處之引號本身有意義，本檢查看不出來。

### 6.2 §4.3.1 之比對

兩側同時去 `[CRnnnnn]`（**A-PMH26**）。

### 6.3 檢查項數之證明

```
batch01 → 32/32 PASS    batch02 → 32/32 PASS    batch03 → 32/32 PASS
--limit-must-hit → 刪去 19/19 皆 FAIL；重複 FAIL；一步三項 FAIL
```

`chk(...)` 之呼叫數未變。**新增檢查程式 0、新增檢查項 0。**

---

## 7. 停止條件之逐條檢查

| # | 條件 | 結果 |
|---|---|---|
| 7 | batch 3 之任一斷言掃描發現**新的**牴觸 | **未觸發** —— `popup_ignoff` 掃描 43 項判定，**牴觸 0**；`SU3.)` 之表面相反已有既有依據（§5.1） |
| 8 | 任一斷言經 R-PMH111 判別為倚賴 p9 **而仍被產出** | **未觸發** —— 判為「是」者 1 筆（`-023`），**未產出** |
| 9 | 9.1 之五 leaf 有任一 `source_clause_origin` 非 `sys1_export` | **未觸發** —— 6 條全為 `sys1_export 9.1`（實測，唯一值） |
| 常設 | ch 9 不得開批 | **已解除**（R-PMH111 之限縮解凍） |
| 常設 | 零寫回工作簿 | **遵守** |
| 常設 | 不動 `new_feature.py`／`docs/runtime/`／他 feature | **遵守** |

---

## 8. 檢查總表（程式產生，R-PMH92）

新納入三列（**既有檢查對新資料之適用，R-PMH107**）：
`lint_batch.py generated/batch03.json`、
`spec_assertion_scan.py --assertion popup_ignoff`、
`spec_assertion_scan.py --assertion animation`。

**未註冊 must-hit 而標「未實測」者 = 4**（不變）。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | 其 (1)(2) 未答 → `-023` 停手；R-PMH111 之條件式續行 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 之判定 |
| `DR-PMH8` | **`DRAFT`（5 問）** | 否 —— **惟其載有 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **batch 3 之六條未經任何人讀覆核。** lint 32/32 只證明其合於已編碼之規則（R-PMH52）。
   **batch 1 曾在 12 包、batch 2 曾在 29 包各被判「產出面須改」** —— 二者皆是 lint 全綠之後。
2. **`-002` 之停手未經裁定。** 我依 `-028` 之形態停手，**而 `-028` 之處置是 Pei 裁的，不是我推的**。
   若判其應產出，須先取得 CFTS009 或裁定一個架構為準。**這是本包最需要一句話的地方。**
3. **A-PMH26 之處置（`test_item` 上半不再嚴格逐字）為我之判斷。**
   另一解是向 profile 申請 §11 之例外。**我選了不動 profile 的那條路，該選擇未經裁定。**
4. **`-018` 標 FUNC 而 `-019`／`-020` 標 EP，其依據我已具名而其一致性可議** ——
   三者同為「使用者於同一 popup 上之選擇」，只因 `-018` 只有一個類而落 FUNC。
   **若判其應同技術，三條之 `design_method` 須齊一。**
5. **`-017` 之二個上限（60 秒無互動／總計 10 分鐘）何者先到即何者生效，規格未言。**
   本條以二個獨立步驟分別驗之而**不斷言其交互作用** —— 該情形未開 DR。
6. **A-PMH25 未併入 `DR-PMH8`** —— 我判其答覆不改變 batch 3 之產出（不造值於任一答覆下皆成立）。
   **該判斷未經裁定**，且與 30 包 §四之教訓（我上次也判「同源」而被推翻）為同一形態。
7. **其餘章之規格側全枚舉仍未做**（KNOWN-INCOMPLETE 三）—— 本次只做了章 9 之 30 行。

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): packages 29b-30 — ch9 unfreeze + comparison, batch 3 (Power Transitions), PENDING-ON-DR registry
```

pathspec（**14 路徑** —— **含 29b**，該包經覆核通過但未授權提交，其異動仍在工作區）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/29b_ch9_unfreeze.md
features/power_moding/docs/handoff/30_batch3.md
features/power_moding/docs/upstream/29b_ch9_unfreeze.md
features/power_moding/docs/upstream/30_batch3.md
features/power_moding/generated/batch03.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/lint_batch.py
features/power_moding/scripts/matrix_vs_chapter.py
features/power_moding/scripts/spec_assertion_scan.py
```

（實為 15 行 —— `generated/batch01.json` 已自清單移除，其內容於本包未變更。）

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| 停手之 leaf | **2**（`-023` 依 R-PMH111；`-002` 依 §8.4.1，**未經裁定**） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT` |
| 新增檢查程式／檢查項 | **0／0** |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
