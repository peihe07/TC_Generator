# 上繳包 13 —— ER 品質修正與首批覆核完成

> 對應下放包：`features/power/docs/handoff/13_er_quality.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；**未寫回 FW036**。

---

## 〇、G0 前置閘

7 / 7 素材 SHA256 與 `01_intake.md` §B 之台帳逐位元相符 —— **PASS**。

---

## 一、B1 —— R-P87 之加註與雜湊佐證（必附一）

依 R-P36，**原文一字未改**，加註置於該裁決區塊**之外**（緊接其下之執行層回報段）。

### 加註後之 R-P87 原文（逐字）

```
[R-P87] **Procedure ↔ ER 須 1:1（G63）。**
        `001` 之 procedure 為 3 步而 ER 為 2 行；`002` 同。
        §6 要求「1:1 aligned with steps」，§9 第 10 項列為自查項。
        十條全數檢查並修正。
        補設閘門 G63：`test_procedure` 之編號步驟數
        須等於 `expected_result` 之編號行數。
        裁決者 Pei，逐字依據：「是」（回應 11 Q8 之 F5）。
```

### 加註內容（置於區塊外）

> **註記（R-P96，13 包）：本條僅規定 procedure 步數 = ER 行數，
> 未規定補出之 ER 行須為可觀察結果，致 12 包之修正引入新缺陷 ——
> 五條已讀 TC 中五條將 procedure 動作複述為 ER。
> 判讀價值之要求已由 R-P96 補足。原文保留。**

### G76 —— 原文位元組佐證

| 項目 | 值 |
|---|---|
| 加註前 SHA256 | `c96b642a71cb2bf1036c54829718eb1801aab3a5604ea2716f1e9bb51d23de9b` |
| 加註後 SHA256 | `c96b642a71cb2bf1036c54829718eb1801aab3a5604ea2716f1e9bb51d23de9b` |
| 位元組長度 | 434（前後相同） |
| **G76** | **UNCHANGED** |

---

## 二、B2 —— 十條之「12 包修正後 / 本包再修正後」對照（必附二）

依 §B2 之明令，**每條皆列出十三欄之現值**，未以「未變更」帶過。

| TC | 變更欄位 | 12 包 proc 步數 → 本包 | 涉及裁決 |
|---|---|---|---|
| `001` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 / R-P97 |
| `002` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |
| `003` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |
| `004` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 / R-P97 |
| `005` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |
| `006` | `test_procedure`、`expected_result` | 4 → **3** | R-P96 |
| `007` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |
| `008` | `expected_result` | 3 → 3 | R-P96（僅 ER2 之可觀察性）|
| `009` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |
| `010` | `test_procedure`、`expected_result` | 3 → **2** | R-P96 |

**合併步驟之後果已驗**：G63 之 1:1 **10 / 10 仍成立**；
最少步數為 **2**，§10.5「至少 2 個編號步驟」**未違反**。

### 逐條對照全文

#### NR1L-PowerManagement-001

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Start the suspend-resume boot sequence
2. Record the elapsed time from boot start until the TLM display changes
3. Compare the recorded time with SplashScreen_Time and check that the splash screen is loaded
```

本包再修正後：
```
1. Start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time and again after SplashScreen_Time has elapsed
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The boot sequence starts and the TLM display stays blank
2. The elapsed time is recorded from boot start
3. The recorded time equals SplashScreen_Time and the splash screen is shown
```

本包再修正後：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown through SplashScreen_Time and the splash screen is loaded once SplashScreen_Time has elapsed
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-001`
- `req_id`：`SWE-PM-071`
- `tc_title`：`Splash screen shown after SplashScreen_Time on normal boot`
- `test_set`：`Power Down`
- `pre_conditions`：`1. A suspend-resume boot sequence is available on the bench`
- `input_test_data`：`NA`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P1`
- `split_flag`：`True`
- `split_reason`：`本條驗正常開機分支：未轉往 Standby / Bench 時，SplashScreen_Time 到期後顯示 splash`

#### NR1L-PowerManagement-002

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Set the boot target status to Standby
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

本包再修正後：
```
1. Set the boot target status to Standby and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The boot target status is Standby
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

本包再修正後：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-002`
- `req_id`：`SWE-PM-071`
- `tc_title`：`No splash screen when TLM passes to Standby`
- `test_set`：`Power Down`
- `pre_conditions`：`1. A suspend-resume boot sequence is available on the bench`
- `input_test_data`：`NA`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P2`
- `split_flag`：`True`
- `split_reason`：`本條驗轉入 Standby 之抑制分支。依 §5.7「不同 trigger 即拆分」，轉入 Standby 與轉入 Bench 為兩個不同觸發，非同一觸發之兩個後果`

#### NR1L-PowerManagement-003

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Set the boot target status to Bench
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

本包再修正後：
```
1. Set the boot target status to Bench and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The boot target status is Bench
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

本包再修正後：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-003`
- `req_id`：`SWE-PM-071`
- `tc_title`：`No splash screen when TLM passes to Bench`
- `test_set`：`Power Down`
- `pre_conditions`：`1. A suspend-resume boot sequence is available on the bench`
- `input_test_data`：`NA`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P2`
- `split_flag`：`True`
- `split_reason`：`本條驗轉入 Bench 之抑制分支，與轉入 Standby 為不同觸發（§5.7 / §8.3）`

#### NR1L-PowerManagement-004

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Record the elapsed time until the TLM screen content changes again
3. Compare the recorded time with StandardScreen_Time and check that the standard screen is visualized
```

本包再修正後：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content through StandardScreen_Time and again after StandardScreen_Time has elapsed
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The boot sequence progresses without an intermediate error screen
2. The elapsed time is recorded from boot start
3. The recorded time equals StandardScreen_Time and the standard screen is visualized
```

本包再修正後：
```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized through StandardScreen_Time and is visualized once StandardScreen_Time has elapsed
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-004`
- `req_id`：`SWE-PM-071`
- `tc_title`：`Standard screen shown after StandardScreen_Time`
- `test_set`：`Power Down`
- `pre_conditions`：`1. A suspend-resume boot sequence is available on the bench`
- `input_test_data`：`NA`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P1`
- `split_flag`：`True`
- `split_reason`：`本條驗第二個時序點：StandardScreen_Time 之後顯示 standard screen，與 -01 之 SplashScreen_Time 為獨立部分失效`

#### NR1L-PowerManagement-005

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Read the TLM event log and compare the recorded count with the injected count
```

本包再修正後：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log and compare the recorded count with the injected count
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The TLM boot sequence starts
2. Every injected event reaches the TLM during boot
3. The buffered event count equals the injected event count with no event dropped
```

本包再修正後：
```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The buffered event count equals the injected event count with no event dropped
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-005`
- `req_id`：`SWE-PM-072`
- `tc_title`：`Events during boot are buffered without loss`
- `test_set`：`Power Down`
- `pre_conditions`：`1. An event injection tool is connected to the bench`
- `input_test_data`：`Event burst: 20 events injected at 100 ms intervals during boot`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`功能測試 (Functional based ; no specific technique)`
- `priority`：`P0`
- `split_flag`：`True`
- `split_reason`：`本條驗緩衝面：開機期間到達之事件不得遺失。與 -02 之處理面為兩個獨立部分失效（§8.2.2）`

#### NR1L-PowerManagement-006

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Wait for the boot sequence to complete
4. Read the TLM_Status transitions and check that every buffered event is processed
```

本包再修正後：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Wait for the boot sequence to complete
3. Read the TLM_Status transitions and check that every buffered event is processed
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The TLM boot sequence starts
2. The injected events are buffered during boot
3. The boot sequence reaches completion
4. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

本包再修正後：
```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The boot sequence reaches completion
3. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-006`
- `req_id`：`SWE-PM-072`
- `tc_title`：`Buffered events processed after boot completes`
- `test_set`：`Power Down`
- `pre_conditions`：`1. An event injection tool is connected to the bench`
- `input_test_data`：`Event burst: 20 events injected at 100 ms intervals during boot`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P1`
- `split_flag`：`True`
- `split_reason`：`本條驗處理面：緩衝之事件於開機完成後依 TLM_Status.Info setting 之轉換處理`

#### NR1L-PowerManagement-007

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read the AUD_LVL signal, the audio output state and the ICS module power state
```

本包再修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data and read the AUD_LVL signal, the audio output state and the ICS module power state
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The TLM volume level is at the starting value
2. The Load Shed condition is detected by the TLM
3. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

本包再修正後：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-007`
- `req_id`：`SWE-PM-073`
- `tc_title`：`Load Shed limits volume and mutes TLM`
- `test_set`：`Power Down`
- `pre_conditions`：

  ```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
  ```
- `input_test_data`：

  ```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 25
  ```
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`
- `design_method`：`決策表 (Decision Table Testing)`
- `priority`：`P0`
- `split_flag`：`True`
- `split_reason`：`本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分`

#### NR1L-PowerManagement-008

變更欄位：`expected_result`

**test_procedure** —— **未變更**

12 包修正後：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and read the audio output state again
```

本包再修正後：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and read the audio output state again
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The two Load Shed signals are absent from the bus
2. The TLM uses the last valid Load Shed signal values
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

本包再修正後：
```
1. The two Load Shed signals are absent from the bus trace
2. AUD_LVL still carries the reduced level and the TLM stays muted
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-008`
- `req_id`：`SWE-PM-073`
- `tc_title`：`Load Shed signals lost: last values retained`
- `test_set`：`Power Down`
- `pre_conditions`：

  ```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
  ```
- `input_test_data`：`NA`
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`
- `design_method`：`基礎故障注入 (Fault Injection Lite)`
- `priority`：`P1`
- `split_flag`：`True`
- `split_reason`：`本條驗故障分支：Load Shed 訊號於匯流排上消失時之回退行為，與 -01 之正常偵測路徑為獨立部分失效`

#### NR1L-PowerManagement-009

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

本包再修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data and read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The TLM volume level is at the starting value
2. The Battery Critical condition is detected by the TLM
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

本包再修正後：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-009`
- `req_id`：`SWE-PM-073`
- `tc_title`：`Battery Critical minimizes draw and keeps ACN active`
- `test_set`：`Power Down`
- `pre_conditions`：

  ```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
  ```
- `input_test_data`：

  ```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25
  ```
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`
- `design_method`：`決策表 (Decision Table Testing)`
- `priority`：`P0`
- `split_flag`：`True`
- `split_reason`：`本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER`

#### NR1L-PowerManagement-010

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

12 包修正後：
```
1. Send the recovery signal listed in Input Test Data
2. Start a timer at the moment the signal changes
3. Read the volume limit and the audio output state at the end of the measurement window
```

本包再修正後：
```
1. Send the recovery signal listed in Input Test Data and start a timer at the moment the signal changes
2. Read the volume limit and the audio output state before the measurement window elapses and again at the end of the measurement window
```

**expected_result** —— **已變更**

12 包修正後：
```
1. The recovery signal is received by the TLM
2. The timer runs from the moment the signal changes
3. The TLM stays in the Battery Critical state until the measurement window elapses and then resumes normal operation
```

本包再修正後：
```
1. The volume limit stays reduced to 20 and the TLM stays muted before the measurement window elapses
2. The volume limit returns to its normal maximum and the audio output is unmuted once the measurement window has elapsed
```

其餘十一欄之現值（皆未變更，依 §B2 明令列出現值而非以「未變更」帶過）：

- `tc_id`：`NR1L-PowerManagement-010`
- `req_id`：`SWE-PM-073`
- `tc_title`：`Normal operation resumes 10 seconds after recovery`
- `test_set`：`Power Down`
- `pre_conditions`：

  ```
1. A LIN and CAN simulation tool is connected
2. The Battery Critical condition is already active
  ```
- `input_test_data`：

  ```
STATUS_LIN.Batt_ST_Crit = [0h]
Measurement window: 10 seconds
  ```
- `specification_reference`：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`
- `design_method`：`狀態轉換 (State Transition Testing)`
- `priority`：`P1`
- `split_flag`：`True`
- `split_reason`：`本條驗回復分支，與 -03 之進入分支為獨立部分失效。**10 秒之出處**：`4942354` 逐字為「shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]」—— 非造值（§8.4.1）`

---

## 三、B3 —— G73 之合成 fixture 與真實實測（必附三）

### 3.1 判準之經驗來源（R-P96 禁憑印象列舉）

取 Comfort + Privacy 已交付件中 proc 與 ER **1:1 對齊**者，
得 **1076 組 (procedure 步驟, ER 行)** 語料，量測實詞重疊率。
完整報告：`features/power/data/b3_er_restatement.md`，核心轉錄於下。

## 1. 語料

| 來源 | proc 與 ER 皆非空之 TC | 其中 1:1 對齊者 | `pre_conditions` 行數 |
|---|---|---|---|
| Comfort | 461 | **461** | 1798 |
| Privacy | 11 | **11** | 25 |
| **合計** | 472 | **472** | 1823 |

對齊語料共 **1076** 組 (procedure 步驟, ER 行)。

## 2. 重疊率之經驗分佈

`overlap = |ER 實詞 ∩ proc 實詞| / |ER 實詞|`（實詞 = 去停用詞）

| 分位 | overlap |
|---|---|
| P50 | 0.500 |
| P75 | 0.750 |
| P90 | 1.000 |
| P95 | 1.000 |
| P99 | 1.000 |
| 最大 | 1.000 |

- overlap ≥ 0.60 者 **477** 組（44.3%）
- overlap ≥ 0.70 者 **276** 組（25.7%）
- overlap ≥ 0.80 者 **157** 組（14.6%）
- overlap ≥ 0.90 者 **120** 組（11.2%）
- overlap ≥ 1.00 者 **120** 組（11.2%）

### overlap 最高之 12 組（已交付件中最接近複述者）

| 來源 | overlap | procedure 步驟 | ER 行 |
|---|---|---|---|
| Comfort | 1.00 | Turn Sync on | Sync is on |
| Comfort | 1.00 | Set the temperature unit to Celsius | The temperature unit is Celsius |
| Comfort | 1.00 | Set the temperature unit to Fahrenheit | The temperature unit is Fahrenheit |
| Comfort | 1.00 | Turn the driver side AUTO on | The driver side AUTO is on |
| Comfort | 1.00 | Press the RECIRC button until RECIRC is in the Open stat | RECIRC is in the Open state |
| Comfort | 1.00 | Set the temperature to the highest possible position | The temperature is at its highest possible position |
| Comfort | 1.00 | Set the temperature to the lowest position | The temperature is at its lowest position |
| Comfort | 1.00 | Turn SYNC on | SYNC is on |
| Comfort | 1.00 | Turn SYNC on | SYNC is on |
| Comfort | 1.00 | Turn "REAR DEFROST" off from the climate screen and read | The exterior rear-view mirror defrost is off |
| Comfort | 1.00 | Turn "REAR DEFROST" on and read the exterior rear-view m | The exterior rear-view mirror defrost is on |
| Comfort | 1.00 | Read the power button | The power button reads ON |

## 3. 可觀察標的之經驗詞庫

ER 行有而其對應 procedure 步驟無之實詞，共 **288** 個相異詞。

出現 ≥ 5 次者：

| 詞 | 次數 |
|---|---|
| `highlight` | 191 |
| `display` | 159 |
| `show` | 144 |
| `button` | 138 |
| `shown` | 109 |
| `active` | 77 |
| `longer` | 68 |
| `climate` | 51 |
| `pop-up` | 50 |
| `fan` | 43 |
| `off` | 41 |
| `current` | 37 |
| `chang` | 36 |
| `state` | 35 |
| `spe` | 32 |
| `screen` | 32 |
| `set` | 28 |
| `face` | 26 |
| `auto` | 25 |
| `step` | 25 |
| `mode` | 24 |
| `feet` | 23 |
| `one` | 22 |
| `passenger` | 22 |
| `system` | 22 |
| `popup` | 22 |
| `new` | 21 |
| `degree` | 21 |
| `airflow` | 21 |
| `led` | 21 |
| `arrow` | 20 |
| `grey` | 20 |
| `widget` | 20 |
| `temperature` | 19 |
| `hi` | 18 |
| `mod` | 18 |
| `rear` | 17 |
| `front` | 17 |
| `mov` | 17 |
| `remain` | 17 |
| `comfort` | 17 |
| `seat` | 16 |
| `bar` | 16 |
| `only` | 16 |
| `increment` | 15 |
| `unchang` | 15 |
| `doe` | 15 |
| `windshield` | 15 |
| `lo` | 14 |
| `increas` | 14 |
| `half` | 13 |
| `value` | 13 |
| `level` | 13 |
| `sett` | 12 |
| `control` | 11 |
| `statu` | 11 |
| `follow` | 11 |
| `available` | 11 |
| `back` | 11 |
| `down` | 10 |
| `instead` | 10 |
| `def` | 10 |
| `open` | 10 |
| `heat` | 10 |
| `category` | 9 |
| `driver` | 9 |
| `manual` | 9 |
| `select` | 9 |
| `small` | 9 |
| `next` | 9 |
| `eco` | 9 |
| `vent` | 9 |
| `sync` | 8 |
| `change` | 8 |
| `held` | 8 |
| `pop` | 8 |
| `max` | 8 |
| `cushion` | 8 |
| `previou` | 7 |
| `reflect` | 7 |
| `feature` | 7 |
| `awake` | 7 |
| `mtc` | 6 |
| `vehicle` | 6 |
| `move` | 6 |
| `unit` | 6 |
| `above` | 6 |
| `loop` | 6 |
| `hvac` | 6 |
| `toggl` | 6 |
| `tab` | 6 |
| `red` | 6 |
| `lumbar` | 6 |
| `bolster` | 6 |
| `carri` | 6 |
| `side` | 5 |
| `being` | 5 |
| `indicator` | 5 |
| `match` | 5 |
| `switch` | 5 |
| `jump` | 5 |
| `place` | 5 |
| `size` | 5 |
| `press` | 5 |
| `c` | 5 |
| `blank` | 5 |
| `med` | 5 |
| `blue` | 5 |
| `clos` | 5 |

## 4. G64 之經驗量測（R-P99(a)）

| 項目 | 實測 |
|---|---|
| 語料行數（已交付 `pre_conditions`） | **1823** |
| `ENV_STABILITY_RE` 觸發行數 | **0** |
| 偽陽性率 | 0.00% |

### 觸發明細（全列，供判別真偽陽性）

（無觸發）

## 5. 閘門邏輯對已交付語料之實測（R-P99）

| 分支 | 判準 | 觸發 / 1076 | 比率 |
|---|---|---|---|
| tier 1 | 動作述語 ＋ overlap ≥ 0.50 | **69** | 6.4% |
| tier 2 | overlap = 1.00 | **120** | 11.2% |

**該等觸發於已交付件中屬合法之狀態回讀**（§6「prove condition established」），形如
「Select the rear Feet mode → The rear Feet mode is selected」。
**故 G73 全部列為待人工裁決類，不阻斷** —— 比照 R-P76 之 R-P42(b)。

### tier 1 觸發之前 15 例（已交付件）

| 來源 | overlap | procedure 步驟 | ER 行 |
|---|---|---|---|
| Comfort | 0.67 | Turn AUTO on and read the fan speed and the airflow  | The fan speed and the airflow mode are set by the sy |
| Comfort | 0.50 | Change the driver temperature | The passenger temperature changes with the driver te |
| Comfort | 0.50 | Press the temperature down arrow once | The temperature moves down by 1 increment |
| Comfort | 0.50 | Press the temperature slider handle and move it | The temperature slider position moves |
| Comfort | 0.50 | Turn "FRONT DEF" on and read the fan speed | The fan speed is changed by the system |
| Comfort | 1.00 | Read the power button | The power button reads ON |
| Comfort | 0.50 | Read the RECIRC state and its LED | RECIRC is open and its LED is off |
| Comfort | 0.75 | Change the climate setting using a front hard contro | The front climate setting changes |
| Comfort | 0.50 | Change the driver temperature using the driver tempe | The front driver temperature changes |
| Comfort | 0.60 | Set a rear temperature different from the current ca | The rear temperature is set to the requested value |
| Comfort | 0.71 | Read the three rear airflow mode buttons | The three rear airflow mode buttons are turned off |
| Comfort | 0.67 | Change the rear temperature | The rear temperature changes |
| Comfort | 0.75 | Read the button text while the rear climate is unloc | The button reads "LOCK REAR" |
| Comfort | 0.50 | Read the button text | The button reads "UNLOCK REAR" |
| Comfort | 1.00 | Set the rear temperature to a value inside the range | The rear temperature is set to a value inside the ra |

## 6. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）

| 版本 | G73 tier 1 | G73 tier 2 | G74 |
|---|---|---|---|
| 12 包修正後（本包修正前） | **7** | **4** | **2** |
| 13 包再修正後 | **0** | **0** | **0** |


### 3.2 合成 fixture

| fixture | 期望 | 實測 |
|---|---|---|
| ER 皆為可觀察結果 | 0 項 | **0 項** |
| ER 複述 procedure 動作 | ≥ 2 項 | **2 項**（`starts`、`is recorded`）|

依 G46 / G71 / G72 之既有慣例，G73 / G74 **不併入 per-fixture 聚合** ——
多數既有 fixture 之 ER 即為「The boot sequence starts」形態，
本閘依設計即應標記之，併入會使無關 fixture 全數變動。

### 3.3 真實實測（本批十條）

| 版本 | G73 tier 1 | G73 tier 2 | G74 |
|---|---|---|---|
| 12 包修正後（本包修正前）| **7** | **4** | **2** |
| **13 包再修正後** | **0** | **0** | **0** |

修正前之 tier 1 命中 `001` `002` `003` `004` `005` `006` `010` 七條，
**涵蓋 R-P96 所舉之全部五例**，且另發現 `006` / `010` 亦命中 ——
即分析層之推測正確，且範圍比已讀之五條更廣。

**依 R-P99(c)，G73 / G74 之證據型別為「合成＋真實」。**

### 3.4 執行層須回報之一項實測結論

> **G73 無法機械化為阻斷閘。**
> tier 1 於已交付語料觸發 **69 / 1076（6.4%）**、tier 2 觸發 **120 / 1076（11.2%）**。
> 其形態為「Select the rear Feet mode → The rear Feet mode is selected」，
> 即 §6 所稱之「prove condition established」狀態回讀 —— 可失敗、具判讀價值。
> **更甚者，已交付 Privacy 之 ER 含
> 「The output volume is read」、「The state of the speed controlled volume is recorded」，
> 與 R-P96 所舉之 `001` ER2「The elapsed time is recorded」同形。**
>
> 故 G73 全部列為**待人工裁決類**（比照 R-P76 之 R-P42(b)），不使 exit=1。
> **若分析層認為該 6.4% / 11.2% 亦屬缺陷，則結論相反，且其影響及於
> Comfort / Privacy 之已交付件** —— 已列入 RULINGS 待裁與 A-PW62。

---

## 四、B4 —— G64 經驗語料量測（必附四）

| 項目 | 實測 |
|---|---|
| 語料（Comfort + Privacy 已交付 `pre_conditions`）| **1823 行** |
| `ENV_STABILITY_RE` 觸發行數 | **0** |
| **偽陽性率** | **0.00%** |
| 新發現之第三類形態 | **無 —— 但見下方限制** |

依 **R-P80**，僅用其「`pre_conditions` 欄不含環境穩定性前提」之結構性事實。

> **執行層之限制聲明（G75）**：偽陽性已測得 0 / 1823，此結論成立。
> **完備性則在原理上無法以該語料檢驗** —— 該語料之所以可用，
> 正因其結構性事實為「不含環境穩定性前提」。
> **語料中本就沒有的東西，無法用來檢驗偵測器是否會漏掉它。**
> 「0 觸發」只說明無誤殺，不說明不存在第三類形態。
> 若須驗完備性，正確語料應為**未通過覆核之草稿**，而非已交付件。
> 已登記為 A-PW63，未以「偽陽性 0」偽稱完備性已驗。

---

## 五、B5 —— 十條 TC 全文（必附五，`006`–`010` 在前）

十三欄 × 10 條，逐條含所屬 leaf 之 `reasoning`。未節錄、未省略換行。

### NR1L-PowerManagement-006 — SWE-PM-072

**tc_id**：`NR1L-PowerManagement-006`

**req_id**：`SWE-PM-072`

**tc_title**：`Buffered events processed after boot completes`

**test_set**：`Power Down`

**pre_conditions**

```
1. An event injection tool is connected to the bench
```

**input_test_data**

```
Event burst: 20 events injected at 100 ms intervals during boot
```

**test_procedure**

```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Wait for the boot sequence to complete
3. Read the TLM_Status transitions and check that every buffered event is processed
```

**expected_result**

```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The boot sequence reaches completion
3. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗處理面：緩衝之事件於開機完成後依 TLM_Status.Info setting 之轉換處理`

**reasoning**（leaf `SWE-PM-072`）

> 驗證目標：開機期間到達之事件須被緩衝且於開機完成後處理。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。

### NR1L-PowerManagement-007 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-007`

**req_id**：`SWE-PM-073`

**tc_title**：`Load Shed limits volume and mutes TLM`

**test_set**：`Power Down`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**

```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 25
```

**test_procedure**

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data and read the AUD_LVL signal, the audio output state and the ICS module power state
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分`

**reasoning**（leaf `SWE-PM-073`）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-008 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-008`

**req_id**：`SWE-PM-073`

**tc_title**：`Load Shed signals lost: last values retained`

**test_set**：`Power Down`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and read the audio output state again
```

**expected_result**

```
1. The two Load Shed signals are absent from the bus trace
2. AUD_LVL still carries the reduced level and the TLM stays muted
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`基礎故障注入 (Fault Injection Lite)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗故障分支：Load Shed 訊號於匯流排上消失時之回退行為，與 -01 之正常偵測路徑為獨立部分失效`

**reasoning**（leaf `SWE-PM-073`）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-009 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-009`

**req_id**：`SWE-PM-073`

**tc_title**：`Battery Critical minimizes draw and keeps ACN active`

**test_set**：`Power Down`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**

```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25
```

**test_procedure**

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data and read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER`

**reasoning**（leaf `SWE-PM-073`）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-010 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-010`

**req_id**：`SWE-PM-073`

**tc_title**：`Normal operation resumes 10 seconds after recovery`

**test_set**：`Power Down`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The Battery Critical condition is already active
```

**input_test_data**

```
STATUS_LIN.Batt_ST_Crit = [0h]
Measurement window: 10 seconds
```

**test_procedure**

```
1. Send the recovery signal listed in Input Test Data and start a timer at the moment the signal changes
2. Read the volume limit and the audio output state before the measurement window elapses and again at the end of the measurement window
```

**expected_result**

```
1. The volume limit stays reduced to 20 and the TLM stays muted before the measurement window elapses
2. The volume limit returns to its normal maximum and the audio output is unmuted once the measurement window has elapsed
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗回復分支，與 -03 之進入分支為獨立部分失效。**10 秒之出處**：`4942354` 逐字為「shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]」—— 非造值（§8.4.1）`

**reasoning**（leaf `SWE-PM-073`）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-001 — SWE-PM-071

**tc_id**：`NR1L-PowerManagement-001`

**req_id**：`SWE-PM-071`

**tc_title**：`Splash screen shown after SplashScreen_Time on normal boot`

**test_set**：`Power Down`

**pre_conditions**

```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time and again after SplashScreen_Time has elapsed
```

**expected_result**

```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown through SplashScreen_Time and the splash screen is loaded once SplashScreen_Time has elapsed
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗正常開機分支：未轉往 Standby / Bench 時，SplashScreen_Time 到期後顯示 splash`

**reasoning**（leaf `SWE-PM-071`）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-002 — SWE-PM-071

**tc_id**：`NR1L-PowerManagement-002`

**req_id**：`SWE-PM-071`

**tc_title**：`No splash screen when TLM passes to Standby`

**test_set**：`Power Down`

**pre_conditions**

```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set the boot target status to Standby and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

**expected_result**

```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Standby 之抑制分支。依 §5.7「不同 trigger 即拆分」，轉入 Standby 與轉入 Bench 為兩個不同觸發，非同一觸發之兩個後果`

**reasoning**（leaf `SWE-PM-071`）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-003 — SWE-PM-071

**tc_id**：`NR1L-PowerManagement-003`

**req_id**：`SWE-PM-071`

**tc_title**：`No splash screen when TLM passes to Bench`

**test_set**：`Power Down`

**pre_conditions**

```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set the boot target status to Bench and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

**expected_result**

```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Bench 之抑制分支，與轉入 Standby 為不同觸發（§5.7 / §8.3）`

**reasoning**（leaf `SWE-PM-071`）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-004 — SWE-PM-071

**tc_id**：`NR1L-PowerManagement-004`

**req_id**：`SWE-PM-071`

**tc_title**：`Standard screen shown after StandardScreen_Time`

**test_set**：`Power Down`

**pre_conditions**

```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content through StandardScreen_Time and again after StandardScreen_Time has elapsed
```

**expected_result**

```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized through StandardScreen_Time and is visualized once StandardScreen_Time has elapsed
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗第二個時序點：StandardScreen_Time 之後顯示 standard screen，與 -01 之 SplashScreen_Time 為獨立部分失效`

**reasoning**（leaf `SWE-PM-071`）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-005 — SWE-PM-072

**tc_id**：`NR1L-PowerManagement-005`

**req_id**：`SWE-PM-072`

**tc_title**：`Events during boot are buffered without loss`

**test_set**：`Power Down`

**pre_conditions**

```
1. An event injection tool is connected to the bench
```

**input_test_data**

```
Event burst: 20 events injected at 100 ms intervals during boot
```

**test_procedure**

```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log and compare the recorded count with the injected count
```

**expected_result**

```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The buffered event count equals the injected event count with no event dropped
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`功能測試 (Functional based ; no specific technique)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗緩衝面：開機期間到達之事件不得遺失。與 -02 之處理面為兩個獨立部分失效（§8.2.2）`

**reasoning**（leaf `SWE-PM-072`）

> 驗證目標：開機期間到達之事件須被緩衝且於開機完成後處理。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。

---

## 六、§D 全表自驗（必附六）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G73** | ER 複述偵測 | fixture 兩案如期；真實實測須回報；再修正後 0 findings | fixture 0 / 2 如期；真實：修正前 tier1 **7** ＋ tier2 **4**，**再修正後 0 / 0** | **PASS** | **合成＋真實** |
| **G74** | 時間量測 ER 無 `equals` | 涉時間量測者皆改行為描述；受影響條數 | 受影響 **2 條**（`001` / `004`）；十條實測 2 → **0** | **PASS** | **合成＋真實** |
| **G75** | G64 經驗語料 | 語料行數、偽陽性數、是否存在第三類形態 | **1823 行**、偽陽性 **0**（0.00%）、**第三類形態未發現，惟完備性在原理上不可驗**（A-PW63）| **PASS（偽陽性）／ 不可驗（完備性）** | 真實 |
| **G76** | R-P87 原文位元組未變 | UNCHANGED | SHA256 前後同為 `c96b642a…de9b`，434 bytes | **UNCHANGED** | 真實 |
| **G63** | Procedure ↔ ER 1:1 | 再修正後仍 10 / 10 | **10 / 10**（步數 3–4 降為 2–3 後仍成立）| **PASS** | 合成＋真實 |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3；TC 仍 10 | `exit=0`；阻斷類 **PASS**；待裁類 **無觸發**；leaf **3**；TC **10**；Test Set 單值 `Power Down` | **PASS** | 真實 |
| G1–G72 | 沿用（G17 已移除）| 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期**；G66 / G71 / G72 合成如期 | **PASS** | 混合（見 A-PW61）|

§10.5「至少 2 個編號步驟」**未違反**（最少步數 2）。

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

12 §七之八項處置已由 R-P98 / R-P99 / R-P100 分派，本節**不覆述**，
僅列執行層自行判斷之項目。

**（甲）本包新產生之該驗而未驗者 —— 四項**

1. **十條之技術正確性仍未被任何人覆核 —— 且本包使其風險上升。**
   這是 12 包 §七第 1 項，未解，且本包**主動改動了 procedure 之步驟結構**
   （3–4 步合併為 2–3 步）。合併步驟是 R-P96 明令的作法，我照做了；
   但合併之後「這條 TC 是否仍完整測到該 leaf 所要求的行為」
   **只有我一個人判斷過**。R-P98 要求分析層覆核十條 ——
   **本包之改動使該覆核比 12 包時更必要，而非更不必要。**

2. **`008` 是十條中唯一 procedure 未變更者，而它未經 G73 之任何觸發。**
   我對它只改了 ER2 的措詞（「uses the last valid values」→
   「AUD_LVL still carries the reduced level」）。
   G73 對 `008` 修正前後皆 0 觸發 —— 即**本閘沒有替 `008` 做過任何事**，
   它的品質完全靠我的人工判斷。同理適用於 tier2 未觸發的其他欄位。

3. **G73 之 tier 2 判準（overlap = 1.00）在本批修正後 0 觸發，
   但這可能是我為了讓它歸零而改的措詞所致，而非品質確實提升。**
   `007` / `009` 之 ER1 我改了兩次 —— 第一次改完 tier1 仍觸發（`reads back`），
   第二次才歸零。**這正是「對著閘門改，而非對著規則改」的風險。**
   我認為第二版（「The TLM volume indicator shows the starting level
   and the audio output is unmuted」）確實更可觀察，
   但**這個判斷出自我自己，與閘門歸零是同一次改動，無法互相佐證。**

4. **R-P96 之判準與已交付件衝突一事，本包只做到「回報」。**
   我沒有、也不應該去判定 Comfort / Privacy 之已交付件是否有缺陷（R-P94）。
   但這代表：**G73 現在是一個判準與現行交付實務不一致的閘門**。
   在分析層裁定之前，它每次觸發都需要人工判斷，
   而人工判斷正是這套流程要減少的東西。

**（乙）已驗而應標明其強度不足者 —— 二項**

5. **G75 之「完備性」實質未驗（A-PW63）。**
   §D 要求「是否存在第三類形態」，我回報「未發現」——
   但該語料**在原理上不可能發現**。我把它標為「不可驗」而非「PASS」。

6. **G74 之形態基礎只有兩個實例。**
   R-P97 引了 `001` / `004` 兩處，我據此寫了
   `equals / is equal to / matches / is exactly` 四種形態。
   四取二是我的擴充，**不是經驗導出** —— 語料中沒有反例可供量測
   （已交付 ER 無此形態）。強度低於 G73 / G64 / G51。
   我在此明說，而非讓它以「PASS」混過去。

**（丙）本包自身之作業瑕疵 —— 一項**

7. **G73 之門檻我調整過三次**（0.833 → 0.75 → 0.50），
   每次都是為了讓它涵蓋 R-P96 所舉之例。最終取 P50 是有依據的
   （本閘非阻斷，recall 重於 precision），
   但**過程確實是「先看答案再定門檻」**。
   我把三次的實測數字都留在 B3 報告與程式碼註解中，
   讓後續可以檢驗這個選擇，而不是只呈現最終值。

**（丁）R-P36 之遵守**

本包對 RULINGS.md 之加註置於裁決區塊**之外**，
R-P87 原文 434 bytes、SHA256 前後相同（G76 UNCHANGED）。
未發生 05 包式之偏移錯誤 —— 每次編輯獨立進行、不共用位移。

---

## 八、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW3 / DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 九、寫回狀態

**R-P92 已結案。現行阻斷條件為 R-P98** —— 分析層須完成十條覆核。
R-P96 / R-P97 之修正已完成。**執行層無其他新增阻斷條件。**

---

## 十、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/data/b3_er_restatement.md` | B3 / B4 經驗導出報告（新增）|
| `features/power/data/b2_before13.json` | 12 包修正後之快照，供前後對照（新增）|
| `features/power/scripts/build_er_restatement.py` | 語料量測腳本（新增，`read_only=True`）|
| `features/power/generated/batch_001_power_down.json` | 十條再修正後（改）|
| `features/power/scripts/lint_tcs.py` | G73 / G74 與其 fixture（改）|
| `features/power/RULINGS.md` | R-P96 ~ R-P100、R-P87 加註（改）|
| `features/power/ANOMALIES.md` | A-PW59 ~ A-PW63、A-PW56 更新（改）|
| `features/power/docs/handoff/13_er_quality.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/13_er_quality.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 13 輪索引（改）|
