# 上繳包 15 —— 首批覆核收尾與誤讀清除

> 對應下放包：`features/power/docs/handoff/15_batch1_closeout.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；**未寫回 FW036**。
> **未依 B5 之素材改動 G77 或任何 TC（15 §I）。**

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

---

## 一、B1 —— `008` / `009` 全文（必附一，置於最前）

十六欄逐條（十三欄 ＋ `req_id` / `test_set` / `reasoning_note`），
含 leaf `source_clause`（**已依 R-P109 補為 `4942354` 完整原文**）。
未節錄、未省略換行。

### NR1L-PowerManagement-008 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-008`

**req_id**：`SWE-PM-073`

**tc_title**：`Load Shed signals lost: last values retained`

**test_set**：`Power Down`

**test_item**：`Load Shed signals lost: last values retained`

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

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**：（無）

**leaf `SWE-PM-073` 之 `source_clause`（`4942354` 完整原文，R-P109 補齊後）**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**leaf `SWE-PM-073` 之 `reasoning`**

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。　**R-P109 補齊（15 包）**：原 `source_clause` 之 `...` 恰好蓋住 「If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down.」與故障／回復兩款 —— 即 `007` / `008` / `010` 之 ER 所斷言者。已改為 `4942354` **完整原文，不截斷**。

### NR1L-PowerManagement-009 — SWE-PM-073

**tc_id**：`NR1L-PowerManagement-009`

**req_id**：`SWE-PM-073`

**tc_title**：`Battery Critical minimizes draw and keeps ACN active`

**test_set**：`Power Down`

**test_item**：`Battery Critical minimizes draw and keeps ACN active`

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

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**：（無）

**leaf `SWE-PM-073` 之 `source_clause`（`4942354` 完整原文，R-P109 補齊後）**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

**leaf `SWE-PM-073` 之 `reasoning`**

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。　**R-P109 補齊（15 包）**：原 `source_clause` 之 `...` 恰好蓋住 「If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down.」與故障／回復兩款 —— 即 `007` / `008` / `010` 之 ER 所斷言者。已改為 `4942354` **完整原文，不截斷**。

---

## 二、B2 —— 十條之全欄掃描（必附二）

**判定規則**：`已修正` = 本包實際改動；`已檢查` = 含誤讀關鍵詞但經判定為合法引述；
`無涉` = 掃描後確認不含任何誤讀關鍵詞。

| TC | `tc_title` | `test_item` | `pre_conditions` | `input_test_data` | `test_procedure` | `expected_result` | `specification_reference` | `design_method` | `priority` | `split_flag` | `split_reason` | `functional_safety` | `remarks` | leaf `reasoning` | `reasoning_note` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `001` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 |
| `002` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 |
| `003` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 |
| `004` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 |
| `005` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 |
| `006` | **已修正** | **已修正** | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 | 無涉 | **已修正** | **已修正** |
| `007` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 |
| `008` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 |
| `009` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 |
| `010` | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | 無涉 | **已修正** | 無涉 |

### `006` 之殘留實測 —— **四處，非一處**

| # | 欄位 | 殘留內容 | 發現者 |
|---|---|---|---|
| 1 | `split_reason` | `緩衝之事件於**開機完成後**依 TLM_Status.Info setting 之轉換處理` | **分析層** |
| 2 | `test_item` | `Buffered events processed **after boot completes**` | **執行層全欄掃描** |
| 3 | `expected_result` | `the TLM_Status transitions **follow the injected order**`（R-P108）| **執行層全欄掃描** |
| 4 | **`distinguishing_axis.delta`** | 同 `split_reason`（複製自該欄）| **執行層全欄掃描** |

**其餘九條全欄掃描：無同型殘留。**
`005`–`010` 之 leaf `reasoning` 顯示「已修正」，係因本包依 R-P107 / R-P108 / R-P109
於 leaf 層追加查證記錄，非誤讀殘留。

### G81 之實作決定與一項須回報者

**R-P107 所列之十三欄清單，不足以涵蓋本 JSON 之實際欄位。**
`distinguishing_axis` 不在該清單內，而它確實帶有誤讀
（其 `delta` 欄複製自 `split_reason`）且會影響 sibling 判別。

故 **G81 實作為掃全部欄位**（`for field in tc.items()`）而非掃指定十三欄 ——
**清單式列舉之閘門會隨資料結構演進而失效**（A-PW73）。

G81 另設「引號內之出現視為引述，不判違」之豁免 ——
查證記錄本身必須引述被否定之措詞，否則無法記錄「規格未載 X」。
該豁免有專屬 fixture。

### G81 實測（R-P107 之驗證條件：須以修正前實證其會觸發）

| 版本 | G81 findings |
|---|---|
| 14 包版（修正前）| **4**（`test_item` / `split_reason` / `expected_result` / `distinguishing_axis`）|
| **15 包版（修正後）** | **0** |

---

## 三、B3 —— `4942338` 完整原文與順序斷言之處置（必附三）

### 完整原文（`anchor_bodies()` 直取，**未截斷**）

```
Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. “TLM_Status.Info setting” while the boot is still completing. TLM must buffer the events and process them as soon as possible, depending on boot timings.
```

**全文僅此二句，無第三句、無其他段落。**

### 判定

| 斷言 | 規格逐字依據 | 判定 |
|---|---|---|
| 事件須被辨識並依 TLM_Status 轉換處理 | `must be recognized by TLM and then TLM has to behave and process it according to the transitions` | **有據** |
| 處理發生於開機期間 | `while the boot is still completing` | **有據** |
| 須緩衝、儘快處理 | `must buffer the events and process them as soon as possible` | **有據** |
| **按注入順序處理** | **無** | **無據 —— FIFO 為推論** |

> **G83 = 依 (a) 刪除順序斷言。**

ER2 現為「Every buffered event is processed before the boot sequence completes
and none remains pending at boot completion」——
以「無事件於開機完成時仍未處理」之可觀察判準取代 FIFO 推論。
刪除依據已逐字記入 `006` 之 `reasoning_note`。

另依 R-P42：`TLM_Status.Info setting` 之轉換定義位於 CFTS009 §1.6.2.1.15，
不在本 leaf 之錨點範圍，**本包未擴大測試至該章**。

---

## 四、B4 —— `source_clause` 補齊與 R-P104 加註佐證（必附四）

### G84 —— R-P104 原文位元組佐證

| 項目 | 值 |
|---|---|
| 加註前 SHA256 | `1bf16987a0ec742f67d050bae75039ef87219944288179a78a5188558d9f4c74` |
| 加註後 SHA256 | `1bf16987a0ec742f67d050bae75039ef87219944288179a78a5188558d9f4c74` |
| 位元組長度 | 672（前後相同） |
| **G84** | **UNCHANGED** |

加註內容（置於裁決區塊**之外**）：

> **註記（R-P109，15 包）：本條令 `source_clause` 得截斷，
> 未規定截斷不得落在待查證處，致 `007` 之 `source_clause` 之 `...`
> 恰好蓋住 mute 與 ICS 兩款 —— 即其 ER 所斷言者，
> 使本條之立意落空。截斷之界線已由 R-P109 補足。原文保留。**

### `SWE-PM-073` 之 `source_clause`（補齊後，`4942354` 完整原文 1,568 字元）

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

被 `...` 遮蔽而現已補回者：
`If Ecall/ACN/chimes mode is not active, TLM shall be muted.`、
`ICS module shall power down.`、
故障條款（`the last values of load shed signals shall be used`）、
維持條款（`maintained for the rest of current ignition key cycle`）、
回復條款（`10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]`）。
—— 即 `007` / `008` / `010` 之 ER 所斷言者，**全部曾被截斷遮蔽**。

### G82 實測與可機械化程度

| 版本 | G82 findings |
|---|---|
| 補齊前 | **2**（`007` / `008` 之 `AUD_LVL`）|
| **補齊後** | **0** |

**可機械化程度（必報項）**：

- **可機械檢查**：ER 之**專有標的** —— 訊號名（`AUD_LVL`、`STATUS_LIN.*`）、
  `_Time` 類參數、全大寫識別子、數值。判準為「該 token 是否出現於 `source_clause`」。
- **不可機械檢查**：ER 之**一般英文措詞**與規格之對應。
  措詞本就不會逐字相同（ER 寫 `The TLM is muted`，規格寫 `TLM shall be muted`
  尚可比對；但 ER 寫 `the audio output is unmuted`，規格無對應詞），
  強行比對只產生雜訊。
- **故 G82 攔得住「截斷蓋掉具名標的」，攔不住「截斷蓋掉某項以一般措詞表述之行為」。**
  此限制已逐字寫入 profile §4.4，未以「G82 已就位」掩蓋。

---

## 五、B5 —— Arif 144 列末步素材（必附五，供 Pei 裁定 Q3）

> **本節僅為裁定素材。執行層依 15 §I 未據此改動 G77 或任何 TC。**

完整報告（含 144 條末步全文）：`features/power/data/b5_arif_final_step.md`。

母體檔：`FM-WI-FSM-036-A01 …_SWQT_Home_20260809.xlsx`
SHA256 `42d9544eed7127f9fe912588715b144d9f2f3412d9e961efe450cc03da15551f`
選取器：Z 欄（Test Case Author）== `ArifChen`；
**母體列數 assertion 144 == 144 PASS**（A-CF14 之教訓：以 `Arif` 選取得 0 列，
而 0 列會產出「全數不含驗證措詞」之空集合結論）。
`read_only=True`，未呼叫 `save()`。
## 1. 母體

 done region **144** 列，其中 `test_procedure` 非空且可拆出末步者 **144** 條。

## 2. 驗證意圖措詞之命中

| 詞 | Arif 末步命中 | 佔比 |
|---|---|---|
| `check` | **77** | 53.5% |
| `verify` | **0** | 0.0% |
| `confirm` | **0** | 0.0% |
| `ensure` | **0** | 0.0% |
| `validate` | **0** | 0.0% |
| `observe` | **0** | 0.0% |
| `read` | **0** | 0.0% |
| `count` | **0** | 0.0% |
| `wait` | **0** | 0.0% |
| `compare` | **0** | 0.0% |
| `measure` | **0** | 0.0% |

**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）命中 18 / 144（12.5%）。**

## 3. 三個母體之並列比較

| 母體 | 末步條數 | §5.2B 措詞命中 | 佔比 |
|---|---|---|---|
| **Arif done region（Home）** | 144 | **18** | 12.5% |
| Comfort + Privacy 已交付（14 包 B4） | 472 | **0** | 0.0% |

## 4. Arif 末步之行首動詞（前 10）

| 動詞 | 次數 | 佔比 |
|---|---|---|
| `check` | 77 | 53.5% |
| `pres` | 35 | 24.3% |
| `select` | 28 | 19.4% |
| `drag` | 3 | 2.1% |
| `swipe` | 1 | 0.7% |

## 4.1 典型措詞形態（前 10 種，取前三字）

| 形態 | 次數 |
|---|---|
| `Select "Add Page"` | 8 |
| `Check the Home` | 8 |
| `Press the greyed` | 7 |
| `Check the default` | 6 |
| `Check the popup` | 6 |
| `Check the order` | 6 |
| `Press "X" button` | 5 |
| `Check the state` | 5 |
| `Check the pagination` | 4 |
| `Check that the` | 3 |

**關鍵區別（供裁定）**：`check` 出現於 **77 / 144（53.5%）**，其中 **77** 條以 `Check` 起首 —— 即驗證意圖確為 Arif 之慣例。
惟 §5.2B 所列之**完整措詞**（`check that` / `to check` / `and check`）僅命中 **18（12.5%）** —— 多數為祈使句 `Check the ...`，非 `check that ...`。
**現行 G77 之正則要求完整措詞，故對 Arif 之 59 條祈使式末步亦會判 FAIL。**
此點為素材，**執行層未據以改動 G77**（15 §I）。


### 執行層之素材說明（不含裁定）

三個母體之實測指向**兩個不同的事實**，須分開看：

1. **驗證意圖是否為慣例** —— Arif 之末步 **77 / 144（53.5%）以 `Check` 起首**，
   Comfort + Privacy **0 / 472**。二者相反。
2. **§5.2B 之完整措詞是否為慣例** —— Arif **18 / 144（12.5%）**，
   Comfort + Privacy **0 / 472**。二者皆低。

即：**Arif 確實在末步寫驗證意圖，但寫的是祈使句 `Check the ...`，
而非 canon §5.2B 所列之 `check that ...`。**
**現行 G77 之正則要求完整措詞，對 Arif 之 59 條祈使式末步亦會判 FAIL。**

執行層**不就此提出處置建議**（Q3 屬 Pei）。

---

## 六、§D 全表自驗（必附六）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G81** | 誤讀關鍵詞全欄掃描 | 修正前 `006` 之 `split_reason` 應觸發；修正後十條 0 | 修正前 **4 項**（含 `split_reason`）；修正後 **0**；fixture 3 案如期（含引述豁免）| **PASS** | **合成＋真實** |
| **G82** | ER 斷言之規格依據完整性 | 可機械化程度；不足數與補齊後結果 | 可機械化者限**專有標的**；不足 **2** → 補齊後 **0**；fixture 2 案如期 | **PASS（部分可機械化）** | **合成＋真實** |
| **G83** | `006` ER 順序斷言 | 完整原文是否載順序；處置 (a) 或 (b) | **完整原文僅二句，未載順序** → 依 **(a) 刪除** | **PASS** | 真實 |
| **G84** | R-P104 原文位元組未變 | UNCHANGED | SHA256 前後同為 `1bf16987…4c74`，672 bytes | **UNCHANGED** | 真實 |
| **G63** | Procedure ↔ ER 1:1 | 修正後全 PASS | **0 findings**（10 / 10 1:1）| **PASS** | 合成＋真實 |
| **G73** | ER 複述偵測 | 修正後全 PASS | **0 findings** | **PASS** | 合成＋真實 |
| **G77** | Final Step 驗證意圖 | 修正後全 PASS | **0 findings**；末步 14–18 字 | **PASS** | 合成＋真實 |
| **G79** | `source_clause` 必附 | 修正後全 PASS | **3 / 3 非空** | **PASS** | 合成＋真實 |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3；TC 仍 10 | `exit=0`；阻斷類 **PASS**；待裁類無觸發；leaf **3**；TC **10** | **PASS** | 真實 |
| G1–G80 | 沿用（G17 已移除）| 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合（A-PW61）|

**G67 覆蓋率更新**：profile 增訂 §4.3 / §4.4 後共 **24 條**，
可機械檢查 **20**（§4.3 `reasoning_note` 之**用途**不可機械檢查，僅其存在可檢查；
§4.4 之一般措詞對應不可機械檢查），已有閘門 **19**（新增 G81 / G82）——
**19 / 20 = 95%**。未覆蓋者為 §3.6 / §3.8 之留白檢查（須待寫回）。
—— 惟須提醒：**覆蓋率上升與品質上升不是同一件事**，本包所查出之三項
（順序斷言、截斷遮蔽、四處殘留）在覆蓋率 89% 時全都存在且全都零觸發。

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

14 §七之八項已由 R-P107 ~ R-P112 分派，本節**不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **`Test Case Framework` 分頁並非 Power 獨有 —— Home 工作簿亦有（A-PW74）。**
   12 包 B1 判定其為「Power 獨有（Comfort / Privacy 皆無）」，
   而該判定之母體只有兩個 feature。本包因 B5 讀 Home 工作簿而順帶實測到。
   **R-P92 之結論不受影響**（該結論建立於「實測 0 非空儲存格」，與是否獨有無關），
   但 A-PW56 之敘述本身是錯的。
   **這暴露一個一般性問題：本專案多次以 Comfort + Privacy 兩個母體推論「全案慣例」**
   —— G51 動詞、G64 詞彙、G73 判準、G77 語料皆然。
   B5 一加入 Home，G77 之結論就從「0 / 472」變成「53.5% 有驗證意圖」。
   **其餘各閘之語料是否也會因加入第三個母體而翻轉，本包未驗。**

2. **`005` 是否也有 R-P108 型之無據斷言，本包未獨立驗證。**
   `005` 與 `006` 同出 `4942338`。我逐句比對了完整原文與 `005` 之 ER，
   判定其「buffered event count equals the injected event count with no event
   dropped」有據（`must buffer the events`）——
   **但「count equals」這個等量斷言，原文同樣未逐字載明**。
   我認為它是 `buffer` 的必然蘊含（緩衝而遺失即非緩衝），
   與 FIFO 之於「as soon as possible」不同。
   **這個區分是我做的，強度與當初判 `006` 無誤時相同。**

3. **G81 是個案型閘門，其黑名單只涵蓋已知的兩次誤讀。**
   R-P107 本身已明訂「不宣稱可攔下未來之其他誤讀」，我照做並照實標示。
   但須明說其後果：**下一次語義誤讀，G81 依然是零觸發。**
   本包新增之 G81 / G82 對「查出下一個誤讀」的貢獻接近零。

4. **十條中僅 `SWE-PM-073` 之 `source_clause` 被補為完整原文。**
   `SWE-PM-071` / `072` 之 `source_clause` 本就是完整原文（無 `...`），
   我核對過。但 G82 僅檢查**專有標的**，
   若 071 / 072 之原文抄寫時漏了某個以一般措詞表述之句子，
   **本包的方法查不到**。

5. **`distinguishing_axis` 之 `delta` 欄與 `split_reason` 內容重複。**
   本包修正時兩處各寫一次，**它們是同一句話存兩份**。
   這正是 A-PW69 得以發生的結構原因 —— 重複的資料必然會漂移。
   本包未做去重（超出下放包範圍），但應登記。

**（乙）已驗而應標明其強度不足者 —— 二項**

6. **G82 之「補齊後 0」不等於「規格依據完整」。**
   0 findings 只說明 ER 中的**具名 token** 都出現在 `source_clause` 裡。
   `008` 之 ER2「AUD_LVL still carries the reduced level and the TLM stays muted」——
   `AUD_LVL` 有據，而「still carries」「stays muted」這兩個**持續性**斷言
   是否有規格依據，G82 不驗。（我判定有據：`the last values ... shall be used`。）

7. **B5 之母體選擇是分析層指定的，我沒有驗證「Arif 144 列為全案格式權威」這個前提。**
   下放包寫「記憶中 Arif 之 144 列為全案格式權威」——
   我確認了該區確為 144 列、作者確為 `ArifChen`、SHA256 已記錄，
   **但「它是格式權威」這件事我沒有、也無法從資料驗證。**
   若該前提不成立，B5 的整份素材對 Q3 的證據力就要重估。

**（丙）本包自身之作業瑕疵 —— 一項**

8. **G82 之第一版 fixture 我寫錯了，`make_tc` 產生的 `req_id` 是 `SWE-PM-073-01`
   （帶 R-P86 所禁之後綴），與 leaf 之 `parent` 對不上，導致「應 PASS」的 fixture 判 FAIL。**
   我以 `req_id` 明寫修正了 fixture。
   **但這也順帶暴露：`make_tc` 至今仍產生後綴式 `req_id`** ——
   對合成 fixture 無害（R-P86 規範交付物），
   惟任何以 `req_id` 對 leaf 之新閘門，其 fixture 都會踩到同一個坑。已登記於本節。

---

## 八、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW3 / DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 九、寫回狀態

**阻斷條件為 R-P98 / R-P105 / R-P112** —— 分析層須完成 `008` / `009` 之覆核。
R-P107 ~ R-P111 之處置已完成。**執行層無其他新增阻斷條件。**
**Q3 待 Pei 裁定；素材已備妥，實作未動。**

---

## 十、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/data/b5_arif_final_step.md` | Arif 144 列末步素材（新增）|
| `features/power/data/b2_before15.json` | 14 包版快照（新增）|
| `features/power/scripts/build_arif_final_step.py` | B5 量測腳本（新增，`read_only=True`）|
| `features/power/generated/batch_001_power_down.json` | `006` 四處殘留清除、順序斷言刪除、`073` `source_clause` 補齊（改）|
| `features/power/scripts/lint_tcs.py` | G81 / G82 與其 fixture、批次層閘門入口（改）|
| `docs/runtime/profiles/FW036_R1L_Power_Profile.md` | §4.3 `reasoning_note`、§4.4 截斷界線（改）|
| `features/power/RULINGS.md` | R-P107 ~ R-P112、R-P104 加註（改）|
| `features/power/ANOMALIES.md` | A-PW69 ~ A-PW74、A-PW68 更新（改）|
| `features/power/docs/handoff/15_batch1_closeout.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/15_batch1_closeout.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 15 輪索引（改）|
