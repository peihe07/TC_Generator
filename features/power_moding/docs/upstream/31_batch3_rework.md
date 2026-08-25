# 上繳包 31 —— batch 3 之重做（8 條）、apparatus 首次解凍、`-002` 之登記

- 日期：2026-08-25
- 下放包：[handoff/31_batch3_rework.md](../handoff/31_batch3_rework.md)
- **零寫回工作簿**；`workbook_state = BLANK` 未變

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH116～118 **3/3 逐字相符**；**R-PMH117 標「待 Pei 核可」，核可前不生效** |
| 2 Final Step 檢查之強化 | **病灶已具名**；must-hit **5/5 FAIL**、範圍向 **15/15 PASS**、`Compare` 邊界二例皆符；**用畢已恢復凍結** |
| 3 batch 3 四項修正 | **6 條 → 8 條**，lint **32/32 PASS**（三批皆 32/32） |
| 4 `-002` 之登記 | **A-PMH27** 立；`DECISIONS.md` 記 `PENDING-APPROVAL`；JSON `stopped` 註 R-PMH117 |
| 5 `PENDING-ON-DR` 補登 | **8 筆 → 10 筆**；**新形態已具名**（見 §5） |
| 停止條件 7／8／9 | **全未觸發** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH116 | apparatus 首次解凍（限 Final Step 檢查） | 706 | `a1dca5d4759e0e2c` | `a1dca5d4759e0e2c` | 1 | ✅ |
| R-PMH117 | `-002` 判 out of scope，**待核可** | 626 | `896dc34b89c5597a` | `896dc34b89c5597a` | 1 | ✅ |
| R-PMH118 | 等價類之數量不決定技術 | 442 | `782875467a48ebf0` | `782875467a48ebf0` | 1 | ✅ |

> **抄錄不等於生效** —— R-PMH117 之效力起於 Pei 之核可，其於 `RULINGS.md` 之核對表下方已具名。

---

## 2. 步驟 2 —— Final Step 檢查之強化（R-PMH116）

### 2.1 (a) 病灶之具名

**現行判準逐字**：

```
VERIFY = r"\b(check that|confirm that|verify that|record|compare|read)\b|to verify"
```

**病灶**：`record`／`read`／裸 `compare` **是蒐集資料之動詞，不是驗證之動詞。**

`Read the radio power state` —— **讀了，而未言「讀到什麼才算通過」**；
其含 `read`，故原判準放行。batch 3 之五條全數以此通過。

**這正是分析層所預判之病灶**（31 包 §三之 ⚠ 一段），實測相符。

### 2.2 強化後之判準

```
VERIFY = (r"\b(check|checks|confirm|confirms|verify|verifies)\s+that\b"
          r"|\bto\s+(verify|check|confirm)\b"
          r"|\bcompare[sd]?\b[^.]*\b(with|against|to)\b")
```

**須有明言其判準之驗證子句。**

### 2.3 `Compare` 之處置（R-PMH116 明令具名）

**判通過。理由**：`Compare the recorded duration with the stated maximum`
**具名了兩造**（`the recorded duration` vs `the stated maximum`），
其 pass/fail 判準因而確定。

**裸 `Compare the values` 不具名兩造 → 不通過。**

**該理由一體適用於各批**，並以兩個邊界例入錨點（見下）。

### 2.4 (b)(c) 錨點之實跑

```
=== R-PMH116 —— Final Step 檢查之錨點（31 包步驟 2）===

(b) must-hit —— batch 3 五條**修正前**之 Final Step 須 FAIL：
  -017  FAIL 被攔下：True   3. Interact with the pop-up repeatedly beyond ten minutes and re
  -018  FAIL 被攔下：True   3. Read the display for the FOTA via Wi-Fi and Charge Now pop-up
  -019  FAIL 被攔下：True   2. Repeat the test, dismiss the update on the FOTA pop-up instea
  -020  FAIL 被攔下：True   2. Repeat the test, dismiss the Wi-Fi configuration pop-up inste
  -021  FAIL 被攔下：True   3. Read the radio power state

(c) 範圍向 —— batch 1／batch 2 之現行 Final Step 須 PASS：
  15 條全部 PASS：True

`Compare` 之邊界（R-PMH116 明令具名，其理由一體適用）：
  -016 之 `Compare … with …`（具名兩造） → 通過（期望 通過）：True
  裸 `Compare the values`（不具名兩造） → 不通過（期望 不通過）：True

============================================================
must-hit 5/5 FAIL: True；範圍向 15/15 PASS: True；`Compare` 邊界二例: True
```

**停止條件 7（must-hit 未 FAIL）未觸發；停止條件 8（範圍向有 FAIL）未觸發。**

### 2.5 解凍之範圍與恢復

| 項 | 數 |
|---|---|
| 新增檢查程式 | **0** |
| **新增檢查項** | **0** —— 同一 `chk(...)` 之判準強化，非新檢查（`chk` 呼叫數未變，三批皆 32/32） |
| 新增旗標 | **1**（`--final-step-must-hit`）—— 其為該檢查之錨點，R-PMH116(b)(c) 明令 |
| 及於其他 canon 節 | **無** |

> **本次解凍用畢，自本包結束起恢復凍結。**
> 其後之任何新增仍須 R-PMH104(a)(b) 之條件（實測之缺陷，或 Pei 裁定）。

---

## 3. batch 3 之四項修正 —— **6 條 → 8 條**

### 3.1 (a) 五條之 Final Step 加驗證子句

| tc | 修正前 | 修正後 |
|---|---|---|
| `-017` | `… and record when the radio powers off` | `… and check that the radio powers off` |
| `-018` | `Read the display for the FOTA via Wi-Fi and Charge Now pop-ups` | `Check that the FOTA via Wi-Fi and Charge Now pop-ups are dismissed` |
| `-019`／`-020` | `… and read the display` | `Check that the FOTA via Wi-Fi and Charge Now pop-ups are displayed` |
| `-021`／`-022` | `… and read the display` | `Check that the Charge Now pop-up is displayed` |
| `-023` | `Read the radio power state` | `Check that the radio shuts down` |
| `-016` | `Compare the recorded duration with the stated maximum` | **不動**（依 §2.3 之處置判通過） |

### 3.2 (b) 拆分 —— `-019`／`-020` 各拆為二條

**canon §8.2.2 之壓力測試**：排程成功而取消失效時該條落 fail、
取消成功而排程失效時亦落 fail —— **兩個獨立之部分失效落在同一個判定上，即 bundling。**

| 原 | 拆為 | 軸 |
|---|---|---|
| `-019`（排程／取消更新） | `-019` 排程／`-020` 取消 | 使用者選擇之等價類 |
| `-020`（完成／取消 Wi-Fi 設定） | `-021` 完成／`-022` 取消 | Wi-Fi 選擇之等價類 |

**TC 數 = 8 → 停止條件 9 未觸發（實測）。**

> ⚠ **`-019`／`-020` 共用同一 `source_clause`**（權威文本以 `or` 連接二類於同一句），
> 而 `-021`／`-022` **各有其句**。**該差異據實記載於二者之 reasoning。**

### 3.3 (c) §4.6 之表述已更正

30 包 §4.6 記 `-016` 之未斷言者為「**任何逾時秒數**」，
**與其 ER4 之 `The head unit stays awake for no longer than 2.5 minutes` 自相矛盾**
（R-PMH45 之同檔內互斥陳述）。

**更正後**：未斷言者為 **`stay awake` 之起算 60 秒**（該子句為 A-PMH16 所查出、SYS1 已刪者）。

**三值之複驗（執行層獨立量測，先算後比，R-G7-1）**：

| 探針 | SYS1 9.1 之命中 |
|---|---|
| `2.5 minutes` | **1** |
| `for 60 seconds` | **1** |
| `10 minutes` | **1** |
| `within 60 seconds` | **0** |
| `stay awake for 60 seconds` | **0** |

**與分析層 §2.3 之複驗相符。三值皆在權威文本內，非造值。**

### 3.4 (d) `design_method` 之齊一（R-PMH118）

`-018`／`-019`／`-020`／`-021`／`-022` **齊一為 EP**。

**`-023` 維持 FUNC，其理由須與 R-PMH118 並讀**：
R-PMH118 令「一條只含一類者其技術仍為 EP」，
**惟 `-023` 之輸入自始未被劃分為等價類** —— 權威文本只給一個分支（`dismisses` → 關機），
未給其對立分支之行為。**無劃分即無 EP。**
**該區別即 R-PMH118 之界線，已於其 reasoning 具名。**

### 3.5 八條之全文

#### `NR1L-DisclaimerScreen-016` — Head unit stays awake at ignition off to display the pending pop-up

- **leaf**：`SWE1-HMI-PM-018-01`（FROP: Power Management）　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：路徑：無互動之維持喚醒（對 -017 之 FOTA 互動延長）

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

- **leaf**：`SWE1-HMI-PM-018-01`（FROP: Power Management）　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：路徑：FOTA 互動延長（對 -016 之無互動）

**pre_conditions**

```
1. No phone call or projection call is active
2. A FOTA pop-up is displayed after the ignition has been turned off
```

**test_procedure**

```
1. Interact with the FOTA pop-up and record the interaction time
2. Stop interacting with the pop-up and record when the radio powers off
3. Interact with the pop-up repeatedly beyond ten minutes and check that the radio powers off
```

**expected_result**

```
1. The radio stays awake while the user is interacting with the FOTA pop-up
2. The radio stays awake until the user has not interacted with the pop-up for 60 seconds
3. The radio does not stay awake for more than 10 minutes because of these pop-ups
```

#### `NR1L-DisclaimerScreen-018` — Accepting the FOTA pop-up starts the update and dismisses the later pop-ups

- **leaf**：`SWE1-HMI-PM-018-02`（FROP: FOTA Via Wi-fi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：使用者選擇之等價類：接受（對 -019 之排程、-020 之取消）

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
3. Check that the FOTA via Wi-Fi and Charge Now pop-ups are dismissed
```

**expected_result**

```
1. The FOTA update available pop-up is accepted
2. The update starts
3. The FOTA via Wi-Fi and Charge Now pop-ups are dismissed
```

#### `NR1L-DisclaimerScreen-019` — Scheduling an update time displays the later pop-ups

- **leaf**：`SWE1-HMI-PM-018-03`（FROP: FOTA Via Wi-fi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：使用者選擇之等價類：排程（對 -018 之接受、-020 之取消）

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA update available pop-up is displayed after the ignition has been turned off
3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle
```

**test_procedure**

```
1. Schedule an update time on the FOTA pop-up
2. Check that the FOTA via Wi-Fi and Charge Now pop-ups are displayed
```

**expected_result**

```
1. The update time is scheduled
2. The FOTA via Wi-Fi and Charge Now pop-ups are displayed
```

#### `NR1L-DisclaimerScreen-020` — Dismissing the update displays the later pop-ups

- **leaf**：`SWE1-HMI-PM-018-03`（FROP: FOTA Via Wi-fi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：使用者選擇之等價類：取消更新（對 -018 之接受、-019 之排程）

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA update available pop-up is displayed after the ignition has been turned off
3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle
```

**test_procedure**

```
1. Dismiss the update on the FOTA pop-up
2. Check that the FOTA via Wi-Fi and Charge Now pop-ups are displayed
```

**expected_result**

```
1. The update is dismissed
2. The FOTA via Wi-Fi and Charge Now pop-ups are displayed
```

#### `NR1L-DisclaimerScreen-021` — Charge Now is displayed when the Wi-Fi configuration is complete

- **leaf**：`SWE1-HMI-PM-018-04`（FROP: WiFi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：Wi-Fi 選擇之等價類：完成設定（對 -022 之取消設定）

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA via Wi-Fi configuration pop-up is displayed after the ignition has been turned off
3. Charge Now is applicable on this vehicle
```

**test_procedure**

```
1. Choose to configure Wi-Fi and complete the Wi-Fi configuration
2. Check that the Charge Now pop-up is displayed
```

**expected_result**

```
1. The Wi-Fi configuration is completed
2. The Charge Now pop-up is displayed
```

#### `NR1L-DisclaimerScreen-022` — Charge Now is displayed after the Wi-Fi configuration pop-up is dismissed

- **leaf**：`SWE1-HMI-PM-018-04`（FROP: WiFi）　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：Wi-Fi 選擇之等價類：取消設定（對 -021 之完成設定）

**pre_conditions**

```
1. No phone call or projection call is active
2. The FOTA via Wi-Fi configuration pop-up is displayed after the ignition has been turned off
3. Charge Now is applicable on this vehicle
```

**test_procedure**

```
1. Dismiss the FOTA via Wi-Fi configuration pop-up
2. Check that the Charge Now pop-up is displayed
```

**expected_result**

```
1. The FOTA via Wi-Fi configuration pop-up is dismissed
2. The Charge Now pop-up is displayed
```

#### `NR1L-DisclaimerScreen-023` — Dismissing the XEV key off pop-ups shuts the radio down

- **leaf**：`SWE1-HMI-PM-018-05`（FROP: EV/PHEV Pages）　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1　**R-PMH111 判別**：否
- **軸**：事件：忽略 XEV key off popup 群（本批唯一之非等價類軸）

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
3. Check that the radio shuts down
```

**expected_result**

```
1. The Charge Now, Summary and Preconditioning pop-ups are shown
2. The XEV key off pop-ups are dismissed
3. The radio shuts down
```


### 3.6 lint 輸出

```
batch01 → 32/32 PASS    batch02 → 32/32 PASS    batch03 → 32/32 PASS
--limit-must-hit → 刪去 19/19 皆 FAIL；重複 FAIL；一步三項 FAIL
--final-step-must-hit → must-hit 5/5 FAIL；範圍向 15/15 PASS；`Compare` 邊界二例
```

---

## 4. 步驟 4 —— `-002` 之登記

- **`ANOMALIES.md`：A-PMH27**（形態同 A-PMH13），載 canon §8.4.2 三項判準之逐項結果；
- **`DECISIONS.md`**：`[PENDING-APPROVAL]`，明記「核可前維持停手、不產出、不寫入」；
- **`generated/batch03.json` 之 `stopped`**：該筆維持，並註 R-PMH117 與其待核可之性質。

> **上繳當時本包未改任何計數**（`n_leaf` 仍為 47）—— 47 → 46 之重算繫於核可。
>
> **追記（2026-08-25 同日）**：Pei 逐字裁定「**核可**」，**R-PMH117 已生效，連帶已全數執行** ——
> `N_LEAF` 47 → **46**、`Power Transitions` 7 → **6**、台帳二處標 `EXCLUDED-BY-R-PMH117`、
> granularity 全項重跑（G1–G5 全 PASS）、**A6 錨點之組態由 `15×3+1×2` 改為 `14×3+2×2`**
> （沿用舊式會使 `min=1` 而隔離失效，已加 `assert` 攔之）。
> `R-PMH117` 正文未改一字（SHA256 前後同值，實測）。詳見 `docs/INDEX.md` 之 31 包要點 §五。

---

## 5. 步驟 5 —— `PENDING-ON-DR` 之補登（8 → 10 筆）

| # | 判定之所在 | 所繫 |
|---|---|---|
| 9 | `-017` 之二上限（60 秒無互動／總計 10 分鐘）何者先到即何者生效 | **無所繫之 DR** |
| 10 | A-PMH25（9.1 權威文本破句）與 `-016` 之不斷言處置 | **無所繫之 DR** |

### 5.1 ⚠ 本簿之一個新形態，須具名

**R-PMH115 之簿設計為「繫於某 DR 之答覆」，而此二筆繫於一個**尚未存在**之問。**

我以「所繫之 DR」欄記 `無所繫之 DR` 並具名其緣由，**該處置未經裁定**。
31 包步驟 5 明令「其是否須開 DR 由下輪處置，本輪只登記」，故本輪不開問。

> **其風險**：一個「無所繫之 DR」之登記**沒有任何觸發點會叫醒它** ——
> R-PMH115 之必辦機制繫於 DR 之 `ANSWERED`，而此二筆永遠不會有那一刻。
> **本簿因而有兩筆是純粹的備忘，不是待辦。**

---

## 6. 檢查總表（程式產生，R-PMH92）＋ 解凍已恢復之聲明

新納入一列：`lint_batch.py --final-step-must-hit`（R-PMH116 之錨點）。
**未註冊 must-hit 而標「未實測」者 = 4**（不變）。

> **聲明**：R-PMH116 之解凍**用畢**，自本包結束起 **apparatus 恢復凍結**。
> 本包新增檢查程式 **0**、新增檢查項 **0**，強化只及於「§5.2B／§5.5 Final Step」一項，
> **未泛化至其他 canon 節**。

---

## 7. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | 其 (1)(2) 未答 → `-023` 停手；R-PMH111 之條件式續行 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 之判定 |
| `DR-PMH8` | **`DRAFT`（5 問）** | 否 —— **其載有 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 8. 本包是否仍有該驗而未驗者 —— **有**

1. **batch 3 之八條又是我寫的，又沒有人讀過。** 本包之修正出自分析層之覆核，
   **但修正後之文字（含兩條全新拆出之 TC）是我寫的**。
   **batch 1 在 12 包、batch 2 在 29 包、batch 3 在 31 包 —— 三批皆在 lint 全綠之後被判產出面須改。**
   **三次之後，「lint 全綠」對產出面之預測力應被視為接近零。**
2. **強化後之判準仍是列舉。** `check/confirm/verify that`／`to verify|check|confirm`／
   `compare … with|against|to` —— **其外之合法表述（如 `ensure that` 已被 §5.1 禁、
   `assert that`／`validate that`）不會通過**，而**其內之表述亦可能空洞**
   （`check that the state is correct` 會通過而未言何謂 correct）。
   **判準只攔動詞，不攔內容。**
3. **`-019`／`-020` 共用同一 `source_clause` 一事無任何檢查所攔。**
   lint 不驗「兩條之 `source_clause` 是否相同」，其區別全繫於 `distinguishing_axis` 之文字。
   **若日後有人誤刪其一，另一條看起來仍完整。**
4. **`-002` 之核可前，`n_leaf` 仍為 47 而 batch 3 只涵蓋 5 leaf** ——
   **granularity 之各項比值現在是以一個包含兩個停手 leaf 之分母算出的**。
   本包未重跑 `check_granularity.py`，**其現值之意義因而是模糊的**。
5. **`PENDING-ON-DR` 之 #9／#10 沒有觸發點**（§5.1）。
6. **A-PMH27 與 A-PMH13 之同型判斷是我做的比對**，
   **而 `-028` 之三項判準當時並非以 canon §8.4.2 逐項列出** —— 我是回頭套的。
   若該三項判準之適用有出入，兩筆之「完全同型」即不成立。

---

## 9. 建議之 commit（**未執行**）

```
feat(power_moding): package 31 — batch 3 rework (8 TCs), final-step check strengthened, -002 registered
```

pathspec（**16 路徑** —— **含 29b／30**，二包經覆核而未授權提交，其異動仍在工作區）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/29b_ch9_unfreeze.md
features/power_moding/docs/handoff/30_batch3.md
features/power_moding/docs/handoff/31_batch3_rework.md
features/power_moding/docs/upstream/29b_ch9_unfreeze.md
features/power_moding/docs/upstream/30_batch3.md
features/power_moding/docs/upstream/31_batch3_rework.md
features/power_moding/generated/batch03.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/lint_batch.py
features/power_moding/scripts/matrix_vs_chapter.py
features/power_moding/scripts/spec_assertion_scan.py
```

### 9.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| apparatus | **首次解凍，用畢已恢復凍結**；新增程式 0、新增檢查項 0、新增旗標 1 |
| 計數之變更 | **無** —— `n_leaf` 仍為 47，47 → 46 繫於 R-PMH117 之核可 |
| 停手之 leaf | **2**（`-023` 依 R-PMH111；`-002` 依 R-PMH117，**待核可**） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT` |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
