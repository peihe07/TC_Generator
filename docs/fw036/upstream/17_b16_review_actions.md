# 上繳包 17：16 包覆核裁決之執行

下放：`docs/fw036/handoff/17_b16_review.md`
日期：2026-08-21　　**止於工作副本。**

| 項 | 值 |
|---|---|
| 基底 | `features/power/sandbox/b16/pm_16.xlsx`（`6c849fef…`） |
| 產出 | `features/power/sandbox/b17/pm_17.xlsx`（`c837096b…`） |
| 寫回 | `features/power/scripts/b17/apply.py` —— `surgical_save` 唯一路徑 |
| 改動 | **1 列 2 格**（row 72 之 `proc`／`er`） |

## 逐節處置

| 節 | 裁決 | 執行層處置 |
|---|---|---|
| §一 row 17 | 非偏離，追認；以註記為準 | 已知悉。原改寫維持不動 |
| §二 DR-PW20 | 確認 | 維持 rows 73／74／119／245 之 `PENDING: DR-PW20` |
| §三 R-1 v3(d) 修訂 | 從附件 A，保留內部訊號來源名 | 現況即此，無改動 |
| §四 lint | 確認不動，另立 feature-scoped 包 | 未改 `scripts/lint036.py` |
| §五 `PowerModeSts_Telematic` | 一律改 `$STATUS_TELEMATIC.PowerSts_Telematic$` | **已改，見下** |
| §六 row 186 | 須確認現行狀態 | 見下 |
| §七 軌 C | 附件 G 未寫入 | 已由 18 包補（附件 G／H） |

## §五 —— row 72 之改寫（四欄中唯一之出現）

全表四欄掃描：`PowerModeSts_Telematic` **僅見於 row 72** 之 `proc`／`er`
各一行（`test_item` 上半之出現屬 R-6 verbatim，不動）。改後：

```
PROC:
1. Drive the signal $STATUS_TELEMATIC.PowerSts_Telematic$ from 4 (Full_Operation) to 5 (Logistic_On)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)
3. Read the TLM state and check that it is the Logistic Idle state
```

改後四欄殘留 `PowerModeSts` 之列：**0**。

### ⚠ 該裁定於本列產生之二項後果（請分析層知悉）

1. **`Standard_Power` 於 `PowerSts_Telematic` 之 VAL_ 中不存在**
   （其列舉為 Sleep／Standby／Timed／Idle／Full_Operation／Logistic_On／
   Bench／Partial_Operation）。原文之起始值 `Standard_Power` 因而無對應標籤。
   執行層取該列**自身 PRE 與 test_item 上半所載之** `Full-Operation`
   → `4 (Full_Operation)`，**非自行推定**，惟仍屬「以他處所載代原處所載」，
   於此明列。
2. **觸發與觀察成為同一訊號。** 改寫後 PROC 1 所驅動者與 PROC 2 所觀察者
   皆為 `$STATUS_TELEMATIC.PowerSts_Telematic$`，該列因而不再驗證
   「BCM 側模式變化 → TLM 進入 Logistic Idle」之因果，而降為
   「該訊號可被置於 5 (Logistic_On) 且此時 TLM 為 Logistic Idle」之狀態檢查。
   **此為裁定之直接後果，非執行層之取捨** —— 若原意仍在驗證因果，
   須重新指定觸發訊號（BCM 側之 `STATUS_BH_BCM1.PowerModeSts` 已裁定不使用）。

## §六 —— row 186 之現行狀態：**既非留空亦非 PENDING，判準完整**

移除者為 Input 欄之 `Event burst: 20 events injected at 100 ms intervals`
（事件**數量**與**間隔**），二者原文未載。移除後之現況：

```
PROC:
1. Start the TLM boot sequence and inject events on the bench while the boot is still completing
2. Read the TLM event log and check that every injected event is buffered without loss
3. Read the TLM_Status transitions during the remainder of the boot and check that
   every buffered event is processed before the boot completes
ER:
1. The injected events are registered while the boot is still completing
2. The buffered event count equals the injected event count
3. Every buffered event is processed before the boot sequence completes and none remains pending
```

判準為 **`every injected event`／`buffered event count equals the injected event count`**
—— 相對於「實際注入者」而定義，**不依賴被移除的數量與間隔**。
故該步驟未失去判準，**不須標 `PENDING`**。`input` 欄為 `NA`（非留空）。

## 驗收

`verify.py`（253 列口徑）十二項全綠；lint A–N 全零、E=0、
P=10（全在 `test_item` 括號下半）；`test_item` 內容變動 0、
`spec_reference` 變動 0、軌 C 零變動；x14 三個 DV 讀回、壓縮成員 42 未變。

## 引用裁決

R-1 v3(a)(c)(d)（12 包＋17 包 §三修訂）、R-6、R-7、R-11(b)、
**17 包 §五（`PowerSts_Telematic` 全案裁定）**、路線 (c)、§8.4.1。
