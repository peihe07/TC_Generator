# 上繳包 14 —— Final Step 驗證意圖與首批覆核收尾

> 對應下放包：`features/power/docs/handoff/14_final_step_intent.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；**未寫回 FW036**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

---

## 一、B1 —— `006`–`009` 四條全文（必附一，置於最前）

十三欄逐條，含 `reasoning`、`reasoning_note`（如有）與該 leaf 之 `source_clause`。
未節錄、未省略換行。

> **請注意：`006` 已依 R-P103 實質改寫**（時序誤讀），
> 其內容與分析層先前所見者不同，覆核時應以本版本為準。

### NR1L-PowerManagement-006 — SWE-PM-072

**tc_id**：`NR1L-PowerManagement-006`

**req_id**：`SWE-PM-072`

**tc_title**：`Buffered events processed during boot in TLM_Status transition order`

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
2. Read the TLM_Status transitions during the remainder of the boot to check that every buffered event is processed
```

**expected_result**

```
1. No injected event is rejected and no error is reported while the boot is still completing
2. Every buffered event is processed before the boot sequence completes and the TLM_Status transitions follow the injected order
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗處理面：緩衝之事件於開機完成後依 TLM_Status.Info setting 之轉換處理`

**leaf `SWE-PM-072` 之 `source_clause`（規格原文，R-P104）**

```
Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. “TLM_Status.Info setting” while the boot is still completing. TLM must buffer the events and process them as soon as possible, depending on boot timings.
```

**leaf `SWE-PM-072` 之 `reasoning`**

> 驗證目標：開機期間到達之事件須被緩衝，且**於開機仍在進行時即依 TLM_Status 轉換儘快處理**。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機期間即依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。　**R-P103 查證（14 包）**：`4942338` 逐字為「process it according to the transitions ... **while the boot is still completing**」與「process them as soon as possible, depending on boot timings」。13 包之 `006` 標題與 ER 作「after boot completes」，**確為誤讀**，已改為「during boot」之表述。

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
2. Send the two Load Shed signals listed in Input Test Data
3. Read AUD_LVL, the audio output and the ICS power state to check the Load Shed action
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分`

**leaf `SWE-PM-073` 之 `source_clause`（規格原文，R-P104）**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7=[1h] signals are received by the TLM, the TLM shall immediately reduce the maximum volume level to 20 ... While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw ...
```

**leaf `SWE-PM-073` 之 `reasoning`**

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
3. Keep the broadcast stopped to the end of the ignition cycle to check that Load Shed is maintained
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

**leaf `SWE-PM-073` 之 `source_clause`（規格原文，R-P104）**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7=[1h] signals are received by the TLM, the TLM shall immediately reduce the maximum volume level to 20 ... While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw ...
```

**leaf `SWE-PM-073` 之 `reasoning`**

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
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display, HVAC controls, ACN phone state and AUD_LVL to check the current minimization
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER`

**leaf `SWE-PM-073` 之 `source_clause`（規格原文，R-P104）**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7=[1h] signals are received by the TLM, the TLM shall immediately reduce the maximum volume level to 20 ... While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw ...
```

**leaf `SWE-PM-073` 之 `reasoning`**

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

---

## 二、B2 —— R-P96 之加註與雜湊佐證（必附二）

依 R-P36，**原文一字未改**，加註置於該裁決區塊**之外**。

### R-P96 原文（逐字，加註後）

```
[R-P96] **ER 之每一行須為可觀察且可判讀之結果，
        不得為 procedure 動作之複述（G73）。**
        R-P87 僅規定「procedure 步數 = ER 行數」，
        未規定補出之行須具判讀價值，致修正引入新缺陷：

          `001` ER2「The elapsed time is recorded from boot start」
          `002` ER1「The boot target status is Standby」
          `003` ER1（同 002）
          `004` ER2（同 001）
          `005` ER1「The TLM boot sequence starts」

        該等行**永遠為真** —— 只要測試員執行了該步驟即成立，
        不構成任何判準，違反 §6「observable, judgeable」。

        §6 明訂 setup / transition 之 ER 係為
        「prove condition established」—— 證明條件已建立，
        **非複述執行者做了什麼**。

        判準：若某 ER 行在「該步驟被執行」之外不含任何額外資訊，
        即為複述，FAIL。
        若某步驟確無可觀察結果，**應合併該步驟**，
        不得為湊 1:1 而造 ER。

        十條全查。補設閘門 G73 —— 偵測 ER 行與其對應 procedure 步驟
        之複述關係（詞彙重疊率 ＋ 無新增可觀察標的）。
        判準之詞彙基礎須有經驗來源（比照 R-P83 / R-P88），
        不得憑印象列舉。

        **R-P87 依 R-P36 原文不改**，於其下加註指向本條。
        裁決者 Pei，逐字依據：「是」（回應 12 Q1）。
```

### 加註內容（置於區塊外）

> **註記（R-P101，14 包）：本條令『無可觀察結果之步驟應合併』，
> 未規定合併後之 Final Step 仍須符 §5.2B / §5.5，
> 致 12 包原有之 `and check that ...` 子句於 13 包合併時被剝除，
> 六條已讀 TC 中五條之 Final Step 無 check target。
> 驗證意圖之要求已由 R-P101 補足。原文保留。**

### G80 —— 原文位元組佐證

| 項目 | 值 |
|---|---|
| 加註前 SHA256 | `5bcbe45ead1b2edfea93b1b243a59af705fba12ca1371164463c5ba07a56cb54` |
| 加註後 SHA256 | `5bcbe45ead1b2edfea93b1b243a59af705fba12ca1371164463c5ba07a56cb54` |
| 位元組長度 | 1499（前後相同） |
| **G80** | **UNCHANGED** |

---

## 三、B3 —— 十條 Final Step 之「13 包版 / 本包版」對照（必附三）

| TC | Final Step 字數 13 → 14 | 步數 13 → 14 | G77 修正前 |
|---|---|---|---|
| `001` | 14 → **16** | 2 → 2 | FAIL |
| `002` | 7 → **14** | 2 → 2 | FAIL |
| `003` | 7 → **14** | 2 → 2 | FAIL |
| `004` | 16 → **17** | 2 → 2 | FAIL |
| `005` | 13 → **15** | 2 → 2 | FAIL |
| `006` | 14 → **18** | 3 → **2** | **PASS**（原已含 `and check that ...`）|
| `007` | 25 → **16** | 2 → **3** | FAIL |
| `008` | 17 → **18** | 3 → 3 | FAIL |
| `009` | 24 → **15** | 2 → **3** | FAIL |
| `010` | 20 → **18** | 2 → 2 | FAIL |

**修正前 G77 實測 = 9 / 10**，高於 §D 之停止門檻 5 ——
**分析層之判定與本閘之判準一致，未觸發停止條件。**
修正後 **0**。全部末步 14–18 字，皆在 §5.2B 之 18 字上限內。

**併發後果已驗**：G63 仍 **10 / 10**；G73 仍 **0**；§10.5 未違（最少 2 步）。
`007` / `009` 之步數由 2 回升為 3 —— 13 包為避免 G73 而合併之步驟，
本包因 Final Step 須承載 check target 而重新拆開，
其第 2 步之 ER 改為可觀察之「TLM accepts the signal without a bus error」。

### 逐條對照全文

#### NR1L-PowerManagement-001

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time and again after SplashScreen_Time has elapsed
```

本包版：
```
1. Start the suspend-resume boot sequence
2. Read the TLM display before and after SplashScreen_Time to check that the splash screen is loaded
```

**expected_result** —— **已變更**

13 包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown through SplashScreen_Time and the splash screen is loaded once SplashScreen_Time has elapsed
```

本包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears before SplashScreen_Time has elapsed, and the splash screen is loaded once it has
```

**tc_title** —— 未變更，現值：`Splash screen shown after SplashScreen_Time on normal boot`

Final Step 字數：13 包 12 → 本包 **16**（§5.2B 上限 18）

#### NR1L-PowerManagement-002

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Set the boot target status to Standby and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

本包版：
```
1. Set the boot target status to Standby and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time to check that no splash screen is shown
```

**expected_result** —— **已變更**

13 包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

本包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears at any time through SplashScreen_Time, and the TLM reaches the Standby boot target
```

**tc_title** —— 未變更，現值：`No splash screen when TLM passes to Standby`

Final Step 字數：13 包 6 → 本包 **14**（§5.2B 上限 18）

#### NR1L-PowerManagement-003

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Set the boot target status to Bench and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time
```

本包版：
```
1. Set the boot target status to Bench and start the suspend-resume boot sequence
2. Read the TLM display through SplashScreen_Time to check that no splash screen is shown
```

**expected_result** —— **已變更**

13 包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen is shown on the TLM display through SplashScreen_Time
```

本包版：
```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears at any time through SplashScreen_Time, and the TLM reaches the Bench boot target
```

**tc_title** —— 未變更，現值：`No splash screen when TLM passes to Bench`

Final Step 字數：13 包 6 → 本包 **14**（§5.2B 上限 18）

#### NR1L-PowerManagement-004

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content through StandardScreen_Time and again after StandardScreen_Time has elapsed
```

本包版：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Read the TLM screen content before and after StandardScreen_Time to check that the standard screen is visualized
```

**expected_result** —— **已變更**

13 包版：
```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized through StandardScreen_Time and is visualized once StandardScreen_Time has elapsed
```

本包版：
```
1. The boot sequence progresses without an intermediate error screen
2. The standard screen is not visualized before StandardScreen_Time has elapsed, and it is visualized once that time has passed
```

**tc_title** —— 未變更，現值：`Standard screen shown after StandardScreen_Time`

Final Step 字數：13 包 13 → 本包 **17**（§5.2B 上限 18）

#### NR1L-PowerManagement-005

變更欄位：`test_procedure`

**test_procedure** —— **已變更**

13 包版：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log and compare the recorded count with the injected count
```

本包版：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log to check that every injected event was buffered without loss
```

**expected_result** —— 未變更，現值：
```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The buffered event count equals the injected event count with no event dropped
```

**tc_title** —— 未變更，現值：`Events during boot are buffered without loss`

Final Step 字數：13 包 14 → 本包 **15**（§5.2B 上限 18）

#### NR1L-PowerManagement-006

變更欄位：`tc_title`、`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Wait for the boot sequence to complete
3. Read the TLM_Status transitions and check that every buffered event is processed
```

本包版：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM_Status transitions during the remainder of the boot to check that every buffered event is processed
```

**expected_result** —— **已變更**

13 包版：
```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The boot sequence reaches completion
3. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

本包版：
```
1. No injected event is rejected and no error is reported while the boot is still completing
2. Every buffered event is processed before the boot sequence completes and the TLM_Status transitions follow the injected order
```

**tc_title** —— **已變更**

13 包版：
```
Buffered events processed after boot completes
```

本包版：
```
Buffered events processed during boot in TLM_Status transition order
```

Final Step 字數：13 包 12 → 本包 **18**（§5.2B 上限 18）

#### NR1L-PowerManagement-007

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data and read the AUD_LVL signal, the audio output state and the ICS module power state
```

本包版：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read AUD_LVL, the audio output and the ICS power state to check the Load Shed action
```

**expected_result** —— **已變更**

13 包版：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

本包版：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

**tc_title** —— 未變更，現值：`Load Shed limits volume and mutes TLM`

Final Step 字數：13 包 26 → 本包 **16**（§5.2B 上限 18）

#### NR1L-PowerManagement-008

變更欄位：`test_procedure`

**test_procedure** —— **已變更**

13 包版：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and read the audio output state again
```

本包版：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped to the end of the ignition cycle to check that Load Shed is maintained
```

**expected_result** —— 未變更，現值：
```
1. The two Load Shed signals are absent from the bus trace
2. AUD_LVL still carries the reduced level and the TLM stays muted
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

**tc_title** —— 未變更，現值：`Load Shed signals lost: last values retained`

Final Step 字數：13 包 18 → 本包 **18**（§5.2B 上限 18）

#### NR1L-PowerManagement-009

變更欄位：`test_procedure`、`expected_result`

**test_procedure** —— **已變更**

13 包版：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data and read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

本包版：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display, HVAC controls, ACN phone state and AUD_LVL to check the current minimization
```

**expected_result** —— **已變更**

13 包版：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

本包版：
```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

**tc_title** —— 未變更，現值：`Battery Critical minimizes draw and keeps ACN active`

Final Step 字數：13 包 26 → 本包 **15**（§5.2B 上限 18）

#### NR1L-PowerManagement-010

變更欄位：`test_procedure`

**test_procedure** —— **已變更**

13 包版：
```
1. Send the recovery signal listed in Input Test Data and start a timer at the moment the signal changes
2. Read the volume limit and the audio output state before the measurement window elapses and again at the end of the measurement window
```

本包版：
```
1. Send the recovery signal listed in Input Test Data and start a timer at the moment the signal changes
2. Read the volume limit before and at the end of the window to check that normal operation resumes
```

**expected_result** —— 未變更，現值：
```
1. The volume limit stays reduced to 20 and the TLM stays muted before the measurement window elapses
2. The volume limit returns to its normal maximum and the audio output is unmuted once the measurement window has elapsed
```

**tc_title** —— 未變更，現值：`Normal operation resumes 10 seconds after recovery`

Final Step 字數：13 包 23 → 本包 **18**（§5.2B 上限 18）

---

## 四、B4 —— G77 之語料導出、合成 fixture、真實實測（必附四）

完整報告：`features/power/data/b4_final_step.md`。
## 1. 語料

末步共 **472** 條（Comfort 461、Privacy 11）。

末步字數：中位 7、P90 12、最長 19。

## 2. 驗證意圖措詞之出現次數

| 詞 | 末步命中 | 佔比 |
|---|---|---|
| `check` | **0** | 0.0% |
| `verify` | **0** | 0.0% |
| `confirm` | **0** | 0.0% |
| `ensure` | **0** | 0.0% |
| `validate` | **0** | 0.0% |
| `observe` | **0** | 0.0% |
| `look` | **0** | 0.0% |
| `note` | **0** | 0.0% |
| `measure` | **0** | 0.0% |
| `compare` | **0** | 0.0% |
| `read` | **243** | 51.5% |
| `count` | **3** | 0.6% |
| `wait` | **7** | 1.5% |

**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）於語料命中 0 / 472。**

## 3. 已交付末步之行首動詞

| 動詞 | 次數 |
|---|---|
| `read` | 160 |
| `pres` | 140 |
| `change` | 51 |
| `turn` | 35 |
| `select` | 13 |
| `adjust` | 9 |
| `touch` | 8 |
| `move` | 8 |
| `wait` | 7 |
| `open` | 6 |
| `set` | 5 |
| `trigger` | 5 |

## 4. 結論 —— 一項須回報之衝突

**§5.2B 之措詞在已交付實務中 0 / 472 attested。**
已交付件之末步慣例為「Read <具體可觀察標的>」——
以「所讀之標的」滿足 §5.5「Final Step 自身即揭示所檢查者」，不另加子句。
Privacy 之末步全數為此形態（例：`Read the state of the speed controlled volume on the HU`）。

**執行層之判別**：R-P101 所指之缺陷**成立** —— 13 包之末步
「Read the TLM display through SplashScreen_Time」所讀者為**載體**（display）
而非**標的**（splash screen），連已交付慣例之標準都未達到。
故本閘依 R-P101 之明令實作並列為阻斷類。

**惟須明載**：採 §5.2B 措詞後，Power 之末步慣例將與 Comfort / Privacy
**分歧**（A-PW67）。此與 G73 之情形不同 ——
G73 是判準無法與合法回讀區分（故不阻斷），
G77 是判準明確而**交付慣例與 canon 條文不一致**（故阻斷，但須登記）。

## 5. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）

| 版本 | G77 findings |
|---|---|
| 13 包版（修正前） | **9** |
| 14 包版（修正後） | **0** |


### 合成 fixture

| fixture | 期望 | 實測 |
|---|---|---|
| 末步含 `to check that ...` | 0 項 | **0 項** |
| 末步無 check target | ≥ 1 項 | **1 項** |
| 末步逾 18 字 | ≥ 1 項 | **1 項** |

**證據型別（R-P99(c)）：合成＋真實。**

---

## 五、B6 —— `006` 之查證結論與逐字依據（必附五）

### `4942338` 原文（`source_clause` 逐字）

```
Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. “TLM_Status.Info setting” while the boot is still completing. TLM must buffer the events and process them as soon as possible, depending on boot timings.
```

### 對照

| 欄 | 13 包版 | 規格原文所載 | 判定 |
|---|---|---|---|
| `tc_title` | `Buffered events processed **after boot completes**` | `while the boot is still completing`、`as soon as possible` | **誤讀** |
| `test_procedure` 步 3 | `Wait for the boot sequence to complete` | 同上 —— 規格未要求等待開機完成 | **誤讀（該步驟本身即誤讀之產物）** |
| `expected_result` 行 3 | `The boot sequence reaches completion` | 同上 | **誤讀** |
| leaf `SWE-PM-072` 之 `reasoning` | 「須被緩衝且於**開機完成後**處理」 | 同上 | **誤讀 —— 且此即源頭** |

### 判定與處置

> **G78 = 確係誤讀。**
> 規格所載為「開機**期間**即依 TLM_Status 轉換處理、**儘快**處理」，
> 非「開機完成後才處理」。

已修正：`tc_title` 改為 `Buffered events processed during boot in TLM_Status
transition order`；procedure 刪去等待步驟（3 步 → **2 步**）；
ER 改為「Every buffered event is processed **before the boot sequence completes**
and the TLM_Status transitions follow the injected order」。
**leaf `SWE-PM-072` 之 `reasoning` 一併更正並附查證記錄** ——
誤讀源頭在 reasoning，僅改 TC 不足。

**該誤讀自 09 包首批產出起即存在，歷經 12 / 13 兩輪修正與多次 lint 全綠而未被察覺**
—— 因其為語義錯誤，無任何閘門可及（A-PW68）。

---

## 六、§D 全表自驗（必附六）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G77** | Final Step 驗證意圖 | fixture 兩案如期；**修正前實測數須回報**；修正後 0 | fixture 3 案如期（含 18 字上限）；**修正前 9 / 10**；修正後 **0** | **PASS** | **合成＋真實** |
| **G78** | `006` 時序表述 | 誤讀與否；若誤讀則修正後相符 | **確係誤讀**；已改為 during-boot 表述，與 `4942338` 逐字相符 | **PASS（已修正）** | 真實 |
| **G79** | `source_clause` 必附 | 3 / 3 非空 | **3 / 3**；fixture 兩案如期 | **PASS** | 合成＋真實 |
| **G80** | R-P96 原文位元組未變 | UNCHANGED | SHA256 前後同為 `5bcbe45e…cb54`，1499 bytes | **UNCHANGED** | 真實 |
| **G63** | Procedure ↔ ER 1:1 | 修正後仍 10 / 10 | **10 / 10** | **PASS** | 合成＋真實 |
| **G73** | ER 複述偵測 | 修正後仍 0 findings | **0**（tier1 0、tier2 0）| **PASS** | 合成＋真實 |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3；TC 仍 10 | `exit=0`；阻斷類 **PASS**；待裁類無觸發；leaf **3**；TC **10**；Test Set 單值 `Power Down` | **PASS** | 真實 |
| G1–G76 | 沿用（G17 已移除）| 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期**；G66 / G71 / G72 合成如期 | **PASS** | 混合（A-PW61）|

**G67 覆蓋率更新**：profile 增訂 §4.1 / §4.2 後共 **22 條**條款，
可機械檢查 **19**（新增二條皆可機械檢查），已有閘門 **17**（新增 G77 / G79）——
**17 / 19 = 89%**。未覆蓋者仍為 §3.6 / §3.8 之留白檢查（須待寫回）。

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

13 §七之七項已由 R-P101 / R-P105 / R-P106 分派，本節**不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **`006` 之誤讀說明「五輪閘門全綠」不能作為任何品質證據。**
   該誤讀自 09 包首批產出即存在，歷經 12 / 13 兩輪修正、多次 lint `exit=0`
   而未被察覺。它不是閘門漏掉的邊角 —— 它是**整條 TC 在測錯的東西**。
   查出它的是 `source_clause` 原文比對，即人讀規格。
   **本包新增之 G77 / G79 都不會查到這一類問題**，往後也不會有閘門查到。

2. **同型誤讀是否只有 `006` 一處，本包未能證明。**
   我以三條 `source_clause` 逐字比對了十條 —— 但**比對者是我，
   而寫出該誤讀的也是我**。`005` 與 `006` 同出 `4942338`，
   我判定 `005` 無誤（其驗證面為緩衝不遺失，與時序無涉），
   但這個判定和當初寫出 `006` 誤讀是同一個判斷來源。
   **R-P105 之分析層覆核是唯一能獨立否證它的機制。**

3. **`007` / `009` 之步數在 13 / 14 兩包間來回一次（3→2→3）。**
   13 包為避免 G73 而合併，14 包為承載 check target 而拆回。
   **兩次都是為了讓閘門歸零，而非因為對測試設計有新的認識。**
   現行的 3 步版本我認為較好（第 2 步之「無 bus error」確為可觀察），
   但這個判斷同樣未經第二人檢視。

4. **G77 之 18 字上限我只驗了上界，未驗其合理性。**
   §5.2B 之 18 字是 canon 所定，我照做。
   但十條中有三條（`006` / `008` / `010`）**恰好落在 18 字**，
   即已頂到上限。若後續 leaf 之驗證標的更多，
   **18 字上限與「末步須揭示所檢查者」會直接衝突**。
   本包未遇到，但這是可預見的下一個結構性問題。

5. **`reasoning_note` 是本包新增之欄位，未經任何約定。**
   R-P102 要求「於各該 TC 之 `reasoning` 逐字記載」，
   而 TC 層原本沒有 `reasoning` 欄（只有 leaf 層有）。
   我自行新增了 `reasoning_note` 欄並同時寫入 leaf `reasoning`。
   **這是我的介面決定，不是裁決條文所定** ——
   若分析層要的是別的形式（例如寫入 `split_reason`），須明示。

**（乙）已驗而應標明其強度不足者 —— 二項**

6. **G77 之判準來自 canon 而非語料 —— 語料實測結果與之相反（0 / 472）。**
   R-P101 要求「判準詞彙以已交付末步為語料導出」，
   而語料導出之結果是**「不用 check that」**。
   我沒有照語料導出，我照 canon 實作了 —— 這是有意識的選擇，
   理由寫在 B4 §4 與 A-PW67，但它不是本條所要求的「經驗導出」。
   **我在此明說此點，而非讓「已依 R-P101 導出」混過去。**

7. **G79 只驗欄位存在，不驗內容真偽。**
   `source_clause` 的內容是我從規格抄的 —— **是否抄對、是否抄全，
   G79 一概不驗**。`006` 的誤讀恰好是在 `source_clause` **抄對**的
   前提下才被查出；若當初連 `source_clause` 都抄錯，
   本包的整個查證鏈會一起失效。此點已寫入 profile §4.1。

**（丙）本包自身之作業瑕疵**

8. 無。R-P96 原文 1499 bytes、SHA256 前後相同（G80 UNCHANGED），
   加註置於裁決區塊之外。每次編輯獨立進行、不共用位移。

---

## 八、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW3 / DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 九、寫回狀態

**阻斷條件為 R-P98 / R-P105** —— 分析層須完成 `006`–`009` 之覆核。
R-P101 / R-P102 / R-P103 / R-P104 之處置已完成。
**執行層無其他新增阻斷條件。**

---

## 十、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/data/b4_final_step.md` | G77 語料導出報告（新增）|
| `features/power/data/b3_before14.json` | 13 包版快照，供前後對照（新增）|
| `features/power/scripts/build_final_step.py` | 末步語料量測腳本（新增，`read_only=True`）|
| `features/power/generated/batch_001_power_down.json` | 十條 Final Step 修正、`006` 改寫、`reasoning` 補述（改）|
| `features/power/scripts/lint_tcs.py` | G77 / G79 與其 fixture（改）|
| `docs/runtime/profiles/FW036_R1L_Power_Profile.md` | §4.1 `source_clause`、§4.2 Final Step（改）|
| `features/power/RULINGS.md` | R-P101 ~ R-P106、R-P96 加註（改）|
| `features/power/ANOMALIES.md` | A-PW64 ~ A-PW68、A-PW59 更新（改）|
| `features/power/docs/handoff/14_final_step_intent.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/14_final_step_intent.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 14 輪索引（改）|
