# 上繳包 12 —— pilot 修正與閘門補強

> 對應下放包：`features/power/docs/handoff/12_pilot_fixes.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；**未寫回 FW036**。

---

## 〇、G0 前置閘

7 / 7 素材 SHA256 與 `01_intake.md` §B 之台帳逐位元相符 —— **PASS**。

---

## 一、B1 —— `Test Case Framework` 分頁判讀（R-P92 / G68）

完整報告：`features/power/data/b1_tc_framework_sheet.md`。核心實測轉錄如下。

## 2. 實測

| 項目 | 實測值 |
|---|---|
| XML part | `xl/worksheets/sheet8.xml` |
| part 位元組 | **1,024** |
| 分頁狀態 | `visible`（**非隱藏**）|
| `<dimension ref>` | `A1` |
| `<sheetData/>` 為空元素 | **是** |
| **非空儲存格數** | **0** |
| `_rels` 檔存在 | **否** |
| `<drawing>` 節點 | 0 |
| `dataValidation` 節點 | 0 |

### part 全文（1,024 bytes 以內，逐字）

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="x14ac xr xr2 xr3" xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr2="http://schemas.microsoft.com/office/spreadsheetml/2015/revision2" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" xr:uid="{00000000-0001-0000-0700-000000000000}"><dimension ref="A1"/><sheetViews><sheetView showGridLines="0" zoomScaleNormal="100" workbookViewId="0"/></sheetViews><sheetFormatPr baseColWidth="10" defaultColWidth="8.83203125" defaultRowHeight="15"/><sheetData/><phoneticPr fontId="3" type="noConversion"/><pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/></worksheet>
```

## 3. 三本工作簿之分頁清單

| # | Power | Comfort | Privacy |
|---|---|---|---|
| 1 | `Cover_old`（隱藏） | `Cover_old`（隱藏） | `Cover_old`（隱藏） |
| 2 | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） |
| 3 | `Cover 封面` | `Cover 封面` | `Cover 封面` |
| 4 | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` |
| 5 | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` |
| 6 | `Test Case Specification&Result` | `Test Case Specification 測試用例規範` | `Test Case Specification 測試用例規範` |
| 7 | `Reference`（隱藏） | `Reference`（隱藏） | `Reference`（隱藏） |
| 8 | `Test Case Framework` | `QS Suggestion`（隱藏） | `QS Suggestion`（隱藏） |
| 9 | `QS Suggestion`（隱藏） | `下拉選單`（隱藏） | `下拉選單`（隱藏） |
| 10 | `下拉選單`（隱藏） | — | — |

Power **10** 分頁、Comfort **9**、Privacy **9**。
**`Test Case Framework` 為 Power 獨有**，Comfort / Privacy 皆無同名分頁。

## 4. G68 —— 與 §E 之衝突判定

判定式：該分頁若載有 Test Group / Test Set 之名稱或列數，即構成第二個
權威來源，與 §E 之 63 / 24 / 16 / 8 / 3 = 114（R-P35）併存而生衝突，
應觸發停止條件。

**實測非空儲存格 0**。分頁內無任何字元資料、無公式、無資料驗證、
無繪圖、無 `_rels`。故：

> **G68 = PASS（不衝突）。該分頁不構成權威來源。§E 未動、R-P35 未受影響。**

依 R-P92 之明令，**未因該分頁自行調整 §E**。

## 5. 附帶觀察（不改變上述結論）

該分頁為空、可見、且僅 Power 獨有。三種可能：範本演進殘留、
預留未填、或由他人自 Power 之上游範本帶入。**執行層無資料可判別，
不臆測**，登記為觀察。此點不影響 G68 之結論 —— 空即為空。


### 對 §E 之明確結論（必附一）

> **該分頁為空，非空儲存格 0，不載有任何 Test Group / Test Set 之名稱或列數。**
> **故不構成與 §E 併存之第二權威來源，不生衝突，未觸發停止條件。**
> **§E 之 63 / 24 / 16 / 8 / 3 = 114（R-P35）未動。**

---

## 二、B2 —— 十條逐條「修正前 / 修正後」對照（必附二）

依 R-P86（req_id 去後綴）、R-P87（proc↔ER 1:1）、R-P88（環境穩定性前提）、
R-P89（`input_test_data` 歸屬）修正。修正前之完整快照留於執行環境，
下列為逐欄實際字串差異，**未節錄**。

| TC | 變更欄數 | 涉及裁決 |
|---|---|---|
| `NR1L-PowerManagement-001` | 5 | R-P86 / 87 / 88 / 89 |
| `NR1L-PowerManagement-002` | 4 | R-P86 / 87 / 88 / 89 |
| `NR1L-PowerManagement-003` | 4 | R-P86 / 87 / 89 |
| `NR1L-PowerManagement-004` | 5 | R-P86 / 87 / 88 / 89 |
| `NR1L-PowerManagement-005` | 4 | R-P86 / 87 / 88 |
| `NR1L-PowerManagement-006` | 4 | R-P86 / 87 / 88 |
| `NR1L-PowerManagement-007` | 3 | R-P86 / 87 |
| `NR1L-PowerManagement-008` | 4 | R-P86 / 87 / 88 / 89 |
| `NR1L-PowerManagement-009` | 3 | R-P86 / 87 |
| `NR1L-PowerManagement-010` | 3 | R-P86 / 87 |

**修正前之違規率**：R-P86 後綴 **10 / 10**、R-P87 proc↔ER 不符 **10 / 10**、
R-P88 環境穩定性前提 **6 / 10**、R-P89 跨欄重複 **5 / 10**。
—— 此即 A-PW55 之量測依據：分析層 11 包僅讀 2 條，而四項發現皆為系統性。

### 逐條差異全文

#### NR1L-PowerManagement-001（5 欄變更）

**req_id**

修正前：
```
SWE-PM-071-01
```

修正後：
```
SWE-PM-071
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

修正後：
```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

修正前：
```
SplashScreen_Time as configured in the TLM node
```

修正後：
```
NA
```

**test_procedure**

修正前：
```
1. Start the suspend-resume boot sequence
2. Record the elapsed time from boot start until the TLM display changes
3. Compare the recorded time with SplashScreen_Time and check that the splash screen is loaded on the TLM display
```

修正後：
```
1. Start the suspend-resume boot sequence
2. Record the elapsed time from boot start until the TLM display changes
3. Compare the recorded time with SplashScreen_Time and check that the splash screen is loaded
```

**expected_result**

修正前：
```
1. The TLM display stays blank until SplashScreen_Time elapses
2. The splash screen is shown on the TLM display after SplashScreen_Time
```

修正後：
```
1. The boot sequence starts and the TLM display stays blank
2. The elapsed time is recorded from boot start
3. The recorded time equals SplashScreen_Time and the splash screen is shown
```

#### NR1L-PowerManagement-002（4 欄變更）

**req_id**

修正前：
```
SWE-PM-071-02
```

修正後：
```
SWE-PM-071
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

修正後：
```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

修正前：
```
Boot target status: Standby
```

修正後：
```
NA
```

**expected_result**

修正前：
```
1. No splash screen is shown on the TLM display
2. The boot sequence continues to the Standby status
```

修正後：
```
1. The boot target status is Standby
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

#### NR1L-PowerManagement-003（4 欄變更）

**req_id**

修正前：
```
SWE-PM-071-03
```

修正後：
```
SWE-PM-071
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

修正後：
```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

修正前：
```
Boot target status: Bench
```

修正後：
```
NA
```

**expected_result**

修正前：
```
1. No splash screen is shown on the TLM display
2. The boot sequence continues to the Bench status
```

修正後：
```
1. The boot target status is Bench
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

#### NR1L-PowerManagement-004（5 欄變更）

**req_id**

修正前：
```
SWE-PM-071-04
```

修正後：
```
SWE-PM-071
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

修正後：
```
1. A suspend-resume boot sequence is available on the bench
```

**input_test_data**

修正前：
```
StandardScreen_Time as configured in the TLM node
```

修正後：
```
NA
```

**test_procedure**

修正前：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Record the elapsed time until the TLM screen content changes again
3. Compare the recorded time with StandardScreen_Time and check that the standard screen is visualized on the TLM screen
```

修正後：
```
1. Start the suspend-resume boot sequence and let it progress normally
2. Record the elapsed time until the TLM screen content changes again
3. Compare the recorded time with StandardScreen_Time and check that the standard screen is visualized
```

**expected_result**

修正前：
```
1. The standard screen is visualized on the TLM screen after StandardScreen_Time
2. The boot sequence completes without an intermediate error screen
```

修正後：
```
1. The boot sequence progresses without an intermediate error screen
2. The elapsed time is recorded from boot start
3. The recorded time equals StandardScreen_Time and the standard screen is visualized
```

#### NR1L-PowerManagement-005（4 欄變更）

**req_id**

修正前：
```
SWE-PM-072-01
```

修正後：
```
SWE-PM-072
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. An event injection tool is connected to the bench
```

修正後：
```
1. An event injection tool is connected to the bench
```

**test_procedure**

修正前：
```
1. Start the TLM boot sequence
2. Inject the event burst while the boot is still completing
3. Read the TLM event log and compare the recorded event count with the injected count to check that no event is dropped
```

修正後：
```
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Read the TLM event log and compare the recorded count with the injected count
```

**expected_result**

修正前：
```
1. The TLM records every injected event in its buffer
2. The buffered event count equals the injected event count
```

修正後：
```
1. The TLM boot sequence starts
2. Every injected event reaches the TLM during boot
3. The buffered event count equals the injected event count with no event dropped
```

#### NR1L-PowerManagement-006（4 欄變更）

**req_id**

修正前：
```
SWE-PM-072-02
```

修正後：
```
SWE-PM-072
```

**pre_conditions**

修正前：
```
1. The TLM is powered from a stable supply
2. An event injection tool is connected to the bench
```

修正後：
```
1. An event injection tool is connected to the bench
```

**test_procedure**

修正前：
```
1. Start the TLM boot sequence
2. Inject the event burst while the boot is still completing
3. Wait for the boot sequence to complete
4. Read the TLM_Status transitions and check that every buffered event is processed after boot completion
```

修正後：
```
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Wait for the boot sequence to complete
4. Read the TLM_Status transitions and check that every buffered event is processed
```

**expected_result**

修正前：
```
1. The TLM processes the buffered events once the boot sequence completes
2. The TLM_Status transitions follow the order recorded for the injected events
```

修正後：
```
1. The TLM boot sequence starts
2. The injected events are buffered during boot
3. The boot sequence reaches completion
4. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

#### NR1L-PowerManagement-007（3 欄變更）

**req_id**

修正前：
```
SWE-PM-073-01
```

修正後：
```
SWE-PM-073
```

**test_procedure**

修正前：
```
1. Set the TLM volume level to 25
2. Send STATUS_LIN.PN14_LS_Actv = [1h] and STATUS_LIN.PN14_LS_Lvl7 = [1h]
3. Read the AUD_LVL signal and the audio output state to check that the volume is limited to 20 and the TLM is muted
```

修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read the AUD_LVL signal, the audio output state and the ICS module power state
```

**expected_result**

修正前：
```
1. The maximum volume level for Ecall, ACN, chimes, beeps and alerts is reduced to 20
2. The AUD_LVL signal is sent with the updated volume level of 20
3. The TLM is muted
4. The ICS module powers down
```

修正後：
```
1. The TLM volume level is at the starting value
2. The Load Shed condition is detected by the TLM
3. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

#### NR1L-PowerManagement-008（4 欄變更）

**req_id**

修正前：
```
SWE-PM-073-02
```

修正後：
```
SWE-PM-073
```

**input_test_data**

修正前：
```
Stop broadcasting STATUS_LIN.PN14_LS_Actv and PN14_LS_Lvl7 on the bus
```

修正後：
```
NA
```

**test_procedure**

修正前：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and check that the Load Shed action is maintained
```

修正後：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and read the audio output state again
```

**expected_result**

修正前：
```
1. The TLM uses the last valid Load Shed signal values
2. The Load Shed action is maintained for the rest of the current ignition key cycle
```

修正後：
```
1. The two Load Shed signals are absent from the bus
2. The TLM uses the last valid Load Shed signal values
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

#### NR1L-PowerManagement-009（3 欄變更）

**req_id**

修正前：
```
SWE-PM-073-03
```

修正後：
```
SWE-PM-073
```

**test_procedure**

修正前：
```
1. Set the TLM volume level to 25
2. Send STATUS_LIN.Batt_ST_Crit = [1h]
3. Read the display state, the HVAC controls and the AUD_LVL signal to check that current draw is minimized while the display stays on
```

修正後：
```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

**expected_result**

修正前：
```
1. The display remains on and the HVAC controls remain active
2. The phone stays active for ACN
3. The maximum volume level is reduced to 20 and AUD_LVL is sent with the updated level
4. The TLM is muted
```

修正後：
```
1. The TLM volume level is at the starting value
2. The Battery Critical condition is detected by the TLM
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

#### NR1L-PowerManagement-010（3 欄變更）

**req_id**

修正前：
```
SWE-PM-073-04
```

修正後：
```
SWE-PM-073
```

**test_procedure**

修正前：
```
1. Send STATUS_LIN.Batt_ST_Crit = [0h]
2. Start a timer at the moment the signal changes
3. Read the volume limit and the audio output state at 10 seconds and check that normal operation has resumed
```

修正後：
```
1. Send the recovery signal listed in Input Test Data
2. Start a timer at the moment the signal changes
3. Read the volume limit and the audio output state at the end of the measurement window
```

**expected_result**

修正前：
```
1. The TLM stays in the Battery Critical state until 10 seconds have elapsed
2. Normal operation resumes after 10 seconds
```

修正後：
```
1. The recovery signal is received by the TLM
2. The timer runs from the moment the signal changes
3. The TLM stays in the Battery Critical state until the measurement window elapses and then resumes normal operation
```


---

## 三、B3–B6 —— 閘門實作與 fixture 佐證（必附三）

### B3 四閘（R-P87 ~ R-P90）

| 閘 | 對應 canon | 實作函式 | fixture 正常 | fixture 違規 |
|---|---|---|---|---|
| **G63** | §6 Procedure ↔ ER 1:1 | `check_s6_proc_er_parity` | PASS | **實際 FAIL** |
| **G64** | §4.4 / §8.5 環境穩定性前提 | `check_s44_env_stability` | PASS | **實際 FAIL** |
| **G65** | §4.5 `input_test_data` 欄位歸屬 | `check_s45_data_ownership` | PASS | **實際 FAIL** |
| **G66** | R-P90 B 欄非空列數 = TC 列數 | `check_b_column_numbering` | 0 findings | 1 finding（B 欄全空）|

**G64 詞彙之經驗基礎（R-P88 明令不得憑印象）**：取自 canon 原文本身 ——
§4.4 Forbidden 之逐字範例 `HU is powered on.`（列於 "system defaults"），
與 §8.5 逐字「testers naturally ensure the environment is stable」。
由該二處導出兩類形態並寫入 `ENV_STABILITY_RE` 之註解：
（一）供電／開機（`powered on/up/from/by`、`is powered`）、
（二）穩定性與正常態（`stable`、`steady`、`normal operating`、`functioning normally`）。
**偽陽性數 0** —— 十條中六條之觸發皆為真違規，
hardware / peripheral 類前提（如「A suspend-resume boot sequence is available on the bench」）
依條文明令**未一併刪除**，亦未被誤觸發。

### B4 —— profile 條款閘門覆蓋率（R-P91 / G67）

`docs/runtime/profiles/FW036_R1L_Power_Profile.md` 共 **20 條**條款。

| 分類 | 數量 | 說明 |
|---|---|---|
| 可機械檢查 | **17** | 分母 |
| 不可機械檢查 | 3 | §3.3 first-match 走查與 §4 拆分準則含判斷成分；§6 為限制登記非規則 |
| **已有閘門** | **15** | G45 / G46 / G50 / G51 / G63–G66 / G71 / G72 等 |
| 未有閘門 | 2 | §3.6 `estimated_time` 留白、§3.8 車型欄留白 —— **須待寫回方能檢查**，非缺漏 |

> **G67 覆蓋率 = 15 / 17 = 88%。**

新增二閘：
- **G71** `check_workbook_columns` —— 以 `feature.yaml` 之 `workbook.columns`
  對 FW036 r9 實測標頭逐欄比對（17 組 欄→標頭關鍵字）。
  **使 A-PW40 之人工盤點升格為機械檢查。**
- **G72** `check_profile_clauses` —— §2 `test_group`、§3.3 design_method 九詞條下拉、
  §3.4 spec_reference 檔名（限 CFTS009 / CFTS010 二詞幹）、§3.7 functional_safety。

G71 / G72 依既有慣例（同 G46）**不併入 per-fixture 聚合**，
由其專屬 fixture 單獨驗證 —— 因 `make_tc` 之預設 spec_reference 詞幹非真實檔名。

### B5 —— §11 表格檢查併入 G50（R-P93）

`TABLE_RE` 偵測 `|` 分隔之 Markdown 表格與 HTML `<table>` / `<tr>` / `<td>` / `<th>`。
fixture 以 `| state | value | result |` **實際觸發**。
「blank line between fields」依 R-P93 之明令**未補**。

### B6 —— A-PW51 回報 Comfort（R-P94）

已於 `features/comfort/ANOMALIES.md` 追加 **A-CF-EXT-01**。
查核範圍**嚴格限於 Comfort `NEVER_WRITE` 之十八欄**（R-P94），未擴大為全欄位稽核，
**未修改 Comfort 之任何交付物**，未提出處置建議。

| 欄 | 非空列數 | 判讀 |
|---|---|---|
| B | 466 | **可解釋** —— 範本自帶之自動編號公式 |
| O（Test Case Reference ID）| 466（全為 `NEW`）| **矛盾** —— 列於 `NEVER_WRITE` 卻與 `feature.yaml` 之 `tc_ref_id_value: "NEW"` 相符 → 新登 **A-PW57** |
| T–Z（車型七欄）| 466（全為 `1`）| **未解釋** —— 即 A-PW51 |
| 其餘九欄 | 0 | 符合 `NEVER_WRITE` |

---

## 四、B7 —— 十條全文（必附四，不節錄）

三 leaf 之 `reasoning` 隨各條附列。

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
2. Record the elapsed time from boot start until the TLM display changes
3. Compare the recorded time with SplashScreen_Time and check that the splash screen is loaded
```

**expected_result**

```
1. The boot sequence starts and the TLM display stays blank
2. The elapsed time is recorded from boot start
3. The recorded time equals SplashScreen_Time and the splash screen is shown
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗正常開機分支：未轉往 Standby / Bench 時，SplashScreen_Time 到期後顯示 splash`

**reasoning**（該 leaf）

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
1. Set the boot target status to Standby
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

**expected_result**

```
1. The boot target status is Standby
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Standby 之抑制分支。依 §5.7「不同 trigger 即拆分」，轉入 Standby 與轉入 Bench 為兩個不同觸發，非同一觸發之兩個後果`

**reasoning**（該 leaf）

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
1. Set the boot target status to Bench
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

**expected_result**

```
1. The boot target status is Bench
2. The boot sequence starts
3. No splash screen is shown on the TLM display through SplashScreen_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Bench 之抑制分支，與轉入 Standby 為不同觸發（§5.7 / §8.3）`

**reasoning**（該 leaf）

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
2. Record the elapsed time until the TLM screen content changes again
3. Compare the recorded time with StandardScreen_Time and check that the standard screen is visualized
```

**expected_result**

```
1. The boot sequence progresses without an intermediate error screen
2. The elapsed time is recorded from boot start
3. The recorded time equals StandardScreen_Time and the standard screen is visualized
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗第二個時序點：StandardScreen_Time 之後顯示 standard screen，與 -01 之 SplashScreen_Time 為獨立部分失效`

**reasoning**（該 leaf）

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
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Read the TLM event log and compare the recorded count with the injected count
```

**expected_result**

```
1. The TLM boot sequence starts
2. Every injected event reaches the TLM during boot
3. The buffered event count equals the injected event count with no event dropped
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`功能測試 (Functional based ; no specific technique)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗緩衝面：開機期間到達之事件不得遺失。與 -02 之處理面為兩個獨立部分失效（§8.2.2）`

**reasoning**（該 leaf）

> 驗證目標：開機期間到達之事件須被緩衝且於開機完成後處理。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。

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
1. Start the TLM boot sequence
2. Inject the event burst listed in Input Test Data while the boot is still completing
3. Wait for the boot sequence to complete
4. Read the TLM_Status transitions and check that every buffered event is processed
```

**expected_result**

```
1. The TLM boot sequence starts
2. The injected events are buffered during boot
3. The boot sequence reaches completion
4. Every buffered event is processed and the TLM_Status transitions follow the injected order
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗處理面：緩衝之事件於開機完成後依 TLM_Status.Info setting 之轉換處理`

**reasoning**（該 leaf）

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
2. Send the two Load Shed signals listed in Input Test Data
3. Read the AUD_LVL signal, the audio output state and the ICS module power state
```

**expected_result**

```
1. The TLM volume level is at the starting value
2. The Load Shed condition is detected by the TLM
3. The maximum volume is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分`

**reasoning**（該 leaf）

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
1. The two Load Shed signals are absent from the bus
2. The TLM uses the last valid Load Shed signal values
3. The Load Shed action is maintained for the rest of the current ignition key cycle
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`基礎故障注入 (Fault Injection Lite)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗故障分支：Load Shed 訊號於匯流排上消失時之回退行為，與 -01 之正常偵測路徑為獨立部分失效`

**reasoning**（該 leaf）

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
3. Read the display state, the HVAC controls, the ACN phone state and the AUD_LVL signal
```

**expected_result**

```
1. The TLM volume level is at the starting value
2. The Battery Critical condition is detected by the TLM
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume is reduced to 20 and the TLM is muted
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER`

**reasoning**（該 leaf）

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
1. Send the recovery signal listed in Input Test Data
2. Start a timer at the moment the signal changes
3. Read the volume limit and the audio output state at the end of the measurement window
```

**expected_result**

```
1. The recovery signal is received by the TLM
2. The timer runs from the moment the signal changes
3. The TLM stays in the Battery Critical state until the measurement window elapses and then resumes normal operation
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗回復分支，與 -03 之進入分支為獨立部分失效。**10 秒之出處**：`4942354` 逐字為「shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]」—— 非造值（§8.4.1）`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。


---

## 五、§D 全表自驗（必附五）

| # | 項目 | 期望值 | **實測** | 判定 |
|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 SHA256 相符 | 7 / 7 | **PASS** |
| **G68** | `Test Case Framework` 判讀 | 是否載有 TG/TS；是否衝突 | 非空儲存格 **0**；**不載有**任何 TG/TS；**不衝突** | **PASS** |
| **G63** | Procedure ↔ ER 1:1 | fixture 正常 PASS、違規 FAIL；十條修正後全 PASS | fixture 兩案如期；十條 **10 / 10** 1:1 | **PASS** |
| **G64** | 環境穩定性偵測 | fixture 兩案如期；詞彙經驗基礎與偽陽性數 | fixture 如期；詞彙取自 canon §4.4 / §8.5 **逐字原文**；**偽陽性 0** | **PASS** |
| **G65** | `input_test_data` 重複偵測 | fixture 兩案如期 | fixture 如期；**真實 lint 另抓出該閘之盲點並已修**（A-PW58） | **PASS** |
| **G66** | B 欄非空列數 = TC 列數 | 本包僅驗閘門邏輯（合成） | 相等 → 0 findings；B 欄全空 → 1 finding | **PASS（合成）** |
| **G67** | profile 條款覆蓋率 | 可機械檢查數／已有閘門／覆蓋率 | 17 / 15 / **88%**；未覆蓋 2 項須待寫回 | **PASS** |
| **G69** | 十條 `req_id` 去後綴 | 10 / 10 無後綴 | **10 / 10**，值域 `SWE-PM-071` / `072` / `073` | **PASS** |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3；TC 數不變 | `exit=0`；阻斷類 **PASS**；R-P42(b) **無觸發**；leaf **3**；TC **10**；Test Set 單值 `Power Down` | **PASS** |
| **G71** | `workbook.columns` 對實測標頭 | （新增）17 組相符 | 17 / 17 | **PASS** |
| **G72** | profile §2/§3.3/§3.4/§3.7 | （新增）fixture 兩案如期 | 如期 | **PASS** |
| G1–G62 | 沿用（G17 已移除） | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期**；真實檔 `exit=0`、0.22s | **PASS** |

---

## 六、必附六 —— R-P92 是否已取得結論，寫回可否開放

**明確回答：R-P92 已取得結論；就 R-P92 本身而言，寫回之阻斷已解除。**

- R-P92 之停止條件為「`Test Case Framework` 分頁載有與 §E 衝突之權威內容」。
  實測該分頁**非空儲存格 0**，**條件不成立**。§E 未動。
- R-P90（B 欄）已明寫裁定，G66 已實作待實測。
- 惟**開放與否為分析層之裁決，非執行層可自行決定**。執行層僅回報：
  **本包未再發現任何新的寫回阻斷條件。**

執行層對寫回包之三點提醒（非阻斷，供 13 包設計參考）：
1. **G66 迄今僅合成驗證**，其真正的失敗證明須在首次寫回時取得。
2. **G67 之 2 項未覆蓋條款（§3.6、§3.8 留白）恰好只能在寫回時檢查** ——
   寫回包應同時補上該二閘，否則覆蓋率永遠停在 88%。
3. **A-PW57 之同型矛盾須先排除** —— Power 之 `NEVER_WRITE` 與 `feature.yaml`
   之寫入意圖須逐欄對讀，勿重蹈 Comfort 的 O 欄。

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

以下為執行層自行盤點，**非複述下放包所列**。

**（甲）確有該驗而未驗者 —— 五項**

1. **十條之技術正確性從未被任何人覆核。**
   本包所修的四項全是**形式規則**（欄位歸屬、行數對齊、ID 一致性、措詞）。
   「這 10 條是否真的測到了 `SWE-PM-071/072/073` 所要求的行為」——
   本包沒驗，11 包沒驗，任何閘門也驗不了。這是最大的缺口。

2. **G66 從未真正失敗過。** 依 G33 之標準（須確認在該階段確實可能失敗），
   G66 的合成 fixture 只證明了函式的算術，未證明它在真實寫回路徑上會攔下東西。
   本包已如實標為「PASS（合成）」而非「PASS」。

3. **G64 之詞彙雖有 canon 基礎，其「完備性」未驗。**
   我從 canon 兩處逐字原文導出兩類形態，這證明了**不是憑印象**，
   但沒有證明**沒有第三類**。Comfort / Privacy 之已交付 `pre_conditions`
   本可作為 A-PW35 式的經驗語料（如 B4 對 G51 所做），本包**未做**。

4. **`Test Case Framework` 為何存在、為何獨有於 Power，未查。**
   本包只證明它是空的。B1 §5 已誠實登記為「無資料可判別，不臆測」。

5. **colorScale `H10:H145` 之語義（A-PW52）本包未查。**
   R-P95 允許與寫回並行，故不阻斷，但仍是未驗。

**（乙）已驗而應標明其強度不足者 —— 二項**

6. **B6 之範圍限定是條文要求，但也因此看不見全貌。**
   我只查了 Comfort 的 18 個 `NEVER_WRITE` 欄。O 欄的矛盾是在這個窄範圍內
   偶然撞見的；其餘欄位若有同型問題，本包的方法**查不到**。
   這是遵守 R-P94 的代價，我認為值得，但應明說。

7. **A-PW58 是本包第四次「合成 fixture 過、真實資料抓到問題」**
   （前三：A-PW35、A-PW39、A-PW50），且**方向首次相反**（誤殺而非漏放）。
   四次之後應當承認：**合成 fixture 通過不足以佐證閘門正確**。
   本包新增的 G63 / G64 / G66 / G71 / G72 中，
   **只有 G63 / G65 見過真實資料**，其餘三閘仍只有合成證據。

**（丙）本包自身之作業瑕疵**

8. 無。本包未發生 05 包式的偏移錯誤 —— 每次編輯獨立進行、不共用位移，
   該規則自 06 包起持續生效。

---

## 八、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW3 / DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 九、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/data/b1_tc_framework_sheet.md` | B1 判讀報告（新增）|
| `features/power/generated/batch_001_power_down.json` | 十條修正後（改）|
| `features/power/scripts/lint_tcs.py` | G63–G66 / G71 / G72、G50 §11 表格（改）|
| `features/comfort/ANOMALIES.md` | A-CF-EXT-01（改，僅追加登記）|
| `features/power/RULINGS.md` | R-P86 ~ R-P95（改）|
| `features/power/ANOMALIES.md` | A-PW53 ~ A-PW58（改）|
| `features/power/docs/handoff/12_pilot_fixes.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/12_pilot_fixes.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 12 輪索引（改）|
