# 11 — 範本全屬性比對與首批全文覆核（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 11
結果：**十步全部完成。R-P79 已取得結論 —— Power 之 DV 座標正確，未沿用 Comfort 座標。**
惟本包另查出一項與寫回直接相關之範本差異（B 欄無公式）。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| 建立 `handoff/11_template_verify.md` | DONE（§A 7 區塊 / §J 7 列 / §H 10 步，自檢一致） |
| 1 G0 前置閘 | **PASS 7 / 7** |
| 2 B1 範本全屬性比對，驗 G56 / G57 | DONE —— **DV 座標正確**；查出三項 Power 獨有差異 |
| 3 B2 A-PW46 查證，驗 G58 | DONE —— **本條前提有誤**，Comfort 政策實與 Privacy 一致 |
| 4 Power profile 建立，G50 改引用條款，驗 G59 | DONE —— 雙向實測 |
| 5 G51 動詞判準重導，驗 G60 | DONE —— 人工清單漏列 12 個 |
| 6 F3 補查，驗 G61 | DONE —— **Load Shed 非 status**，走查成立 |
| 7 首批 10 條 TC 全文，驗 G62 | DONE —— 13 欄 × 10 條無空值 |
| 8 §D 全表自驗 | DONE |
| 9 §A 七條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE（R-P1–R-P85；A-PW01–A-PW52 連續無缺） |
| 10 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

---

## 一、B1 —— 範本全屬性比對（R-P79 / G56 / G57，**上繳項一**）

全文見 `features/power/data/b1_template_diff.md`。
**全程以 `zipfile` 直讀 `xl/*.xml`，未經 openpyxl 寫入路徑、未呼叫 `save()`**（11 §I；R-G3）。

### 1.1 G56 —— 資料驗證（DV）

| feature | DV | 明細（sqref → 語義） |
|---|---|---|
| **Power** | 4 | `Q10:Q221 R10:R11 P10:P11` → priority ＋ estimated_time；`U10:AA221` → **車型欄**；x14 `S10:S221` → **design_method**；`AG10:AG13` → Test Result |
| Comfort | 4 | `P10:Q601` → priority ＋ estimated_time；`T10:Z601` → 車型欄；x14 `R10:R601` → design_method；`AF10:AF601` → Test Result |
| Privacy | 5 | `P10:Q11`；`T10:Z11`；`AF10:AF11`；x14 `R10` ＋ `R11:R20`（同一 DV 拆為兩條） |

**四條 DV 之語義三者相同；座標各依其自身版本。**

- Power 之 priority DV 落在 **Q**（Power 之 priority 欄）— 正確
- Power 之車型欄 DV 落在 **U–AA**（Power 之七個車型欄）— 正確
- Power 之 design_method x14 DV 落在 **S**（Power 之 design_method 欄）— 正確
- Power 之 Test Result DV 落在 **AG**（Power 之 Test Result 欄）— 正確

### **G56 之明確結論**

> **Power 之 DV 範圍與其自身欄位對應完全相符，未沿用 Comfort 座標。**
> R-P79 所憂之情形（DV 以 Comfort 欄字母設定而落在錯誤欄位）**未發生**。

### 1.2 G57 —— 其餘五項

| 屬性 | Power | Comfort | Privacy | 判定 |
|---|---|---|---|---|
| **分頁** | 10 個，`Test Case Specification&Result` | 9 個，`…測試用例規範` | 同 Comfort | **Power 獨有**（多 `Test Case Framework`） |
| **合併儲存格** | 5：`U8:AA8` `AC7:AI7` `A1:AF1` `B7:AB7` **`D5:F5`** | 4：`T8:Z8` `AB7:AH7` `A1:AE1` `B7:AA7` | 同 Comfort | 前四項為**右移一格之同一組**；**`D5:F5` 為 Power 獨有** |
| **條件式格式** | 1：`H10:H145` colorScale | 0 | 0 | **Power 獨有** |
| **凍結窗格** | 無 pane 元素 | 無 | `topLeftCell="A2"` | Comfort ≠ Privacy（依 R-P80 不取多數） |
| **公式** | **0** | 592（`B10: IF(ISBLANK($D10),"",ROW()-9)` 起） | 11（同式） | **Power 獨有 —— 見下** |
| 欄寬定義 | 已比對，無異常 | — | — | — |

### 1.3 **一項具寫回影響之差異：Power 之 B 欄無自動編號公式**

Comfort / Privacy 之範本於 `B10` 起帶 `IF(ISBLANK($D10),"",ROW()-9)`，
**No.# 序號隨 D 欄自動產生**。Comfort 之 `write_back.py` 因此把 B 列入
`NEVER_WRITE` 並註明「B carries the template's own numbering formula;
clearing or overwriting it removes the mechanism」。

**Power 之 `B10` / `B11` / `B12` 實測為純空儲存格 —— 無公式、無值。**

> **寫回時 Power 之 No.# 欄不會自動填入。** 若比照 Comfort 把 B 列入
> `NEVER_WRITE`，交付件之序號欄將全空。此項須裁定（見 §九 Q1）。

### 1.4 A-PW52 —— Power 之 DV 覆蓋範圍不齊

`Q10:Q221`（priority）與 `U10:AA221`（車型欄）涵蓋全資料範圍；
但 `P10:P11` / `R10:R11`（estimated_time）僅 2 列、`AG10:AG13`（Test Result）僅 4 列。
Comfort 對應者皆涵蓋全範圍（`P10:Q601` / `AF10:AF601`）。
該三欄依 profile §3.6 / §0.2 皆留空，故現階段不影響寫回。

---

## 二、B2 —— A-PW46 之查證（R-P81 / G58，**上繳項二**）

### 結果：**(a) 之變體 —— Comfort 有明文裁決，且其裁決與 Privacy 相同（留白）**

逐字引用三項證據：

1. **Comfort profile draft §3**（`features/comfort/docs/handoff/15_profile_draft.md`）：

   > **T–Z 欄 Vehicle Model**：一律留白（Privacy R30-4）。
   > **A-PV15 同樣適用於 Comfort**：範本七欄止於 27 世代，本專案平台為
   > HDCC28，**不得將 27 世代欄位對映至 28 平台**。

2. **Comfort `write_back.py`**：

   ```python
   NEVER_WRITE = ["B", "C", "E", "O", "Q", "T", "U", "V", "W", "X", "Y", "Z",
                  "AB", "AC", "AD", "AE", "AF", "AG"]
   ```
   T–Z 即 Comfort 之七個車型欄，全在禁寫清單內。

3. **Comfort baseline 工作簿**（`features/comfort/inputs/*036*.xlsx`）：
   T 欄非空數 **0**（D 欄非空 2，為範本樣本列）。

另：**全 Comfort 腳本無一呼叫 `.save()`**（`grep -rln '\.save('` 結果為空），
僅 `write_back.py` 提及 `T` 且在禁寫清單內。

### **A-PW46 之前提有誤**

> Comfort **並未「決定填 `1`」**。其政策與 Privacy 相同 —— 皆為留白。
> 已交付件中之 466 個 `1` **非由 Comfort 管線產生**，來源不明
> （可能為客戶端或人工於管線外填入）。→ **A-PW51**

**故不存在「兩份已知 good 政策相反」之情形**；存在的是
「一份已交付件之內容與其自身政策不符」。這比原本的描述更嚴重，
也更強地支持 **R-P80** —— 已交付件之內容**不但不具權威，甚至不必然反映該 feature 之裁決**。

**Power 之處置維持留白，未因查證改變**（本即二種情形之共同結果，R-P81）。

---

## 三、B3 —— Power profile（R-P82 / G59）

`docs/runtime/profiles/FW036_R1L_Power_Profile.md` 已建立。
涵蓋 R-P82 所列四項，另補：§0.1 欄位對應、§0.2 範本自身限制、
§3.3 §12 first-match 之 status 清單、§4 拆分準則、§6 已知限制、§7 不繼承自 Privacy 者。

### G59 —— 雙向實測

G50 之兩項方括號豁免**已改為引用 profile §3.1 / §3.2**，
並以 `PROFILE_PATH.exists()` 為條件 —— **profile 不存在即無豁免依據**。

| 情形 | 訊號值 `[1h]` ＋ source-class `[spec-derived]` | 不當 UI 方括號 `[Power]` |
|---|---|---|
| profile **存在** | **0 findings**（正確豁免） | **實際觸發**（正確攔下） |
| profile **缺席** | **2 findings**（豁免失效） | **實際觸發** |

二者皆經 fixture 實測，符 G59 之驗證條件。

---

## 四、B4 —— G51 動詞判準重導（R-P83 / G60）

全文見 `features/power/data/b4_precond_verbs.md`。
語料：Comfort 466 ＋ Privacy 11 列之 `test_procedure`；
偽陽性量測母體為其 `pre_conditions` **1823 行**。
依 R-P80，僅用其結構性事實，不引用任何內容裁決。

| 指標 | 結果 |
|---|---|
| 經驗動詞（procedure 行首，≥ 3 次） | **20 個** |
| **人工清單漏列** | **12 個** —— `adjust` `change` `count` `do` `move` `note` `operate` `put` `toggle` `touch` `turn` `wait`（皆實際出現於已交付 procedure） |
| 人工列舉而未見於該語料 | 13 個 —— **非誤列，僅未經佐證**（如 `send` / `connect` 於 Power 自身 TC 中即有使用） |
| **偽陽性（人工清單）** | **0 / 1823 行** |
| **偽陽性（經驗清單）** | **0 / 1823 行** |

**因二者偽陽性同為零，G51 改採聯集（32 個動詞）** —— 最大化涵蓋而無已量測之代價。
更新後 fixture 全數如期，首批 10 條 TC 之 `pre_conditions` 亦未觸發。

---

## 五、B5 —— F3 補查（R-P84 / G61）

**搜尋條件**（依 R-P84 要求載明）：

- 語料：CFTS010 依 R-P3′ 自原始檔抽出之文字層，**78,976 字元**
- 正則：`\bload\s*shed\b`，**大小寫不敏感**，**含詞界**
- 掃描範圍：**全文，不限章節**

**結果**：

| 指標 | 實測 |
|---|---|
| `Load Shed` 出現次數 | **29** |
| 與 `status` / `state` / `mode` 於 60 字元內之共現 | **0 處** |
| 作為章節標題者 | 2 處 —— §1.4.1.6 `Load Shed`、§1.7.2 `Load Shed` |

二處皆為**條件／功能名**，非 TLM status。
CFTS010 中 `TLM_Status` 出現 9 次，皆指向 CFTS009 之
「TLM_Status.Info setting」章節，未於 CFTS010 另立 status 清單。

> **F3 之走查確認成立。** `007` / `009` 之決策表判定維持，未重判、未重跑 lint。

該結論已寫入 profile §3.3，使 §12 之 first-match 走查有成文依據。

---

## 六、B6 —— 首批 10 條 TC 全文（R-P85，**上繳項三**）

十三欄 × 10 條，逐條含該 leaf 之 `reasoning`。**未節錄、未省略換行、未以摘要代替。**
G62：**無任何空值欄**。

### NR1L-PowerManagement-001 — SWE-PM-071-01

**tc_id**：`NR1L-PowerManagement-001`

**req_id**：`SWE-PM-071-01`

**tc_title**：`Splash screen shown after SplashScreen_Time on normal boot`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

**input_test_data**：`SplashScreen_Time as configured in the TLM node`

**test_procedure**

```
1. Start the suspend-resume boot sequence
2. Record the elapsed time from boot start until the TLM display changes
3. Compare the recorded time with SplashScreen_Time and check that the splash screen is loaded on the TLM display
```

**expected_result**

```
1. The TLM display stays blank until SplashScreen_Time elapses
2. The splash screen is shown on the TLM display after SplashScreen_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗正常開機分支：未轉往 Standby / Bench 時，SplashScreen_Time 到期後顯示 splash`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-002 — SWE-PM-071-02

**tc_id**：`NR1L-PowerManagement-002`

**req_id**：`SWE-PM-071-02`

**tc_title**：`No splash screen when TLM passes to Standby`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

**input_test_data**：`Boot target status: Standby`

**test_procedure**

```
1. Set the boot target status to Standby
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

**expected_result**

```
1. No splash screen is shown on the TLM display
2. The boot sequence continues to the Standby status
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Standby 之抑制分支。依 §5.7「不同 trigger 即拆分」，轉入 Standby 與轉入 Bench 為兩個不同觸發，非同一觸發之兩個後果`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-003 — SWE-PM-071-03

**tc_id**：`NR1L-PowerManagement-003`

**req_id**：`SWE-PM-071-03`

**tc_title**：`No splash screen when TLM passes to Bench`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

**input_test_data**：`Boot target status: Bench`

**test_procedure**

```
1. Set the boot target status to Bench
2. Start the suspend-resume boot sequence
3. Read the TLM display through SplashScreen_Time and check that no splash screen is loaded
```

**expected_result**

```
1. No splash screen is shown on the TLM display
2. The boot sequence continues to the Bench status
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗轉入 Bench 之抑制分支，與轉入 Standby 為不同觸發（§5.7 / §8.3）`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-004 — SWE-PM-071-04

**tc_id**：`NR1L-PowerManagement-004`

**req_id**：`SWE-PM-071-04`

**tc_title**：`Standard screen shown after StandardScreen_Time`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. A suspend-resume boot sequence is available on the bench
```

**input_test_data**：`StandardScreen_Time as configured in the TLM node`

**test_procedure**

```
1. Start the suspend-resume boot sequence and let it progress normally
2. Record the elapsed time until the TLM screen content changes again
3. Compare the recorded time with StandardScreen_Time and check that the standard screen is visualized on the TLM screen
```

**expected_result**

```
1. The standard screen is visualized on the TLM screen after StandardScreen_Time
2. The boot sequence completes without an intermediate error screen
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗第二個時序點：StandardScreen_Time 之後顯示 standard screen，與 -01 之 SplashScreen_Time 為獨立部分失效`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.1.1.1 之 `4942337` 所定之兩個開機時序點與兩個抑制條件。關鍵情境條件：suspend-resume 開機序列，並以目標狀態為 Standby 或 Bench 分支。為什麼這樣切：依 §8.2.2 之壓力測試拆為四條 —— splash 顯示、Standby 抑制、Bench 抑制、standard screen。**Standby 與 Bench 於 10 包 pilot review（F1）後再拆** ——依 §5.7「不同 trigger 即拆分」，二者為不同觸發而非同一觸發之兩個後果；§8.3 壓力測試亦成立：Standby 抑制正確而 Bench 誤顯示時，原合併之一條無法給出明確判讀。刻意略過：`4942337` 未述 SplashScreen_Time 與 StandardScreen_Time 之數值，依 §8.4 不造值，procedure 以「與設定值比對」表述。

### NR1L-PowerManagement-005 — SWE-PM-072-01

**tc_id**：`NR1L-PowerManagement-005`

**req_id**：`SWE-PM-072-01`

**tc_title**：`Events during boot are buffered without loss`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. An event injection tool is connected to the bench
```

**input_test_data**：`Event burst: 20 events injected at 100 ms intervals during boot`

**test_procedure**

```
1. Start the TLM boot sequence
2. Inject the event burst while the boot is still completing
3. Read the TLM event log and compare the recorded event count with the injected count to check that no event is dropped
```

**expected_result**

```
1. The TLM records every injected event in its buffer
2. The buffered event count equals the injected event count
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`功能測試 (Functional based ; no specific technique)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗緩衝面：開機期間到達之事件不得遺失。與 -02 之處理面為兩個獨立部分失效（§8.2.2）`

**reasoning**（該 leaf）

> 驗證目標：開機期間到達之事件須被緩衝且於開機完成後處理。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。

### NR1L-PowerManagement-006 — SWE-PM-072-02

**tc_id**：`NR1L-PowerManagement-006`

**req_id**：`SWE-PM-072-02`

**tc_title**：`Buffered events processed after boot completes`

**test_set**：`Power Down`

**pre_conditions**

```
1. The TLM is powered from a stable supply
2. An event injection tool is connected to the bench
```

**input_test_data**：`Event burst: 20 events injected at 100 ms intervals during boot`

**test_procedure**

```
1. Start the TLM boot sequence
2. Inject the event burst while the boot is still completing
3. Wait for the boot sequence to complete
4. Read the TLM_Status transitions and check that every buffered event is processed after boot completion
```

**expected_result**

```
1. The TLM processes the buffered events once the boot sequence completes
2. The TLM_Status transitions follow the order recorded for the injected events
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗處理面：緩衝之事件於開機完成後依 TLM_Status.Info setting 之轉換處理`

**reasoning**（該 leaf）

> 驗證目標：開機期間到達之事件須被緩衝且於開機完成後處理。關鍵情境條件：開機序列進行中注入事件叢發。為什麼這樣切：緩衝面（不遺失）與處理面（開機後依 TLM_Status 轉換處理）為兩個獨立部分失效 —— 緩衝成功而處理未發生仍屬失敗，反之亦然，依 §8.2.2 拆為兩條。刻意略過：`4942338` 引用之 “TLM_Status.Info setting” 章節屬 CFTS009 §1.6.2.1.15，非本 leaf 所引用之錨點，依 **R-P42** 不納入測試範圍，僅於 ER 引其轉換順序之存在。

### NR1L-PowerManagement-007 — SWE-PM-073-01

**tc_id**：`NR1L-PowerManagement-007`

**req_id**：`SWE-PM-073-01`

**tc_title**：`Load Shed limits volume and mutes TLM`

**test_set**：`Power Down`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**：`STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 25`

**test_procedure**

```
1. Set the TLM volume level to 25
2. Send STATUS_LIN.PN14_LS_Actv = [1h] and STATUS_LIN.PN14_LS_Lvl7 = [1h]
3. Read the AUD_LVL signal and the audio output state to check that the volume is limited to 20 and the TLM is muted
```

**expected_result**

```
1. The maximum volume level for Ecall, ACN, chimes, beeps and alerts is reduced to 20
2. The AUD_LVL signal is sent with the updated volume level of 20
3. The TLM is muted
4. The ICS module powers down
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-008 — SWE-PM-073-02

**tc_id**：`NR1L-PowerManagement-008`

**req_id**：`SWE-PM-073-02`

**tc_title**：`Load Shed signals lost: last values retained`

**test_set**：`Power Down`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
```

**input_test_data**：`Stop broadcasting STATUS_LIN.PN14_LS_Actv and PN14_LS_Lvl7 on the bus`

**test_procedure**

```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Read the AUD_LVL signal and the audio output state
3. Keep the broadcast stopped for the remainder of the ignition cycle and check that the Load Shed action is maintained
```

**expected_result**

```
1. The TLM uses the last valid Load Shed signal values
2. The Load Shed action is maintained for the rest of the current ignition key cycle
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`基礎故障注入 (Fault Injection Lite)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗故障分支：Load Shed 訊號於匯流排上消失時之回退行為，與 -01 之正常偵測路徑為獨立部分失效`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-009 — SWE-PM-073-03

**tc_id**：`NR1L-PowerManagement-009`

**req_id**：`SWE-PM-073-03`

**tc_title**：`Battery Critical minimizes draw and keeps ACN active`

**test_set**：`Power Down`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**：`STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25`

**test_procedure**

```
1. Set the TLM volume level to 25
2. Send STATUS_LIN.Batt_ST_Crit = [1h]
3. Read the display state, the HVAC controls and the AUD_LVL signal to check that current draw is minimized while the display stays on
```

**expected_result**

```
1. The display remains on and the HVAC controls remain active
2. The phone stays active for ACN
3. The maximum volume level is reduced to 20 and AUD_LVL is sent with the updated level
4. The TLM is muted
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。

### NR1L-PowerManagement-010 — SWE-PM-073-04

**tc_id**：`NR1L-PowerManagement-010`

**req_id**：`SWE-PM-073-04`

**tc_title**：`Normal operation resumes 10 seconds after recovery`

**test_set**：`Power Down`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The Battery Critical condition is already active
```

**input_test_data**：`STATUS_LIN.Batt_ST_Crit = [0h]
Measurement window: 10 seconds`

**test_procedure**

```
1. Send STATUS_LIN.Batt_ST_Crit = [0h]
2. Start a timer at the moment the signal changes
3. Read the volume limit and the audio output state at 10 seconds and check that normal operation has resumed
```

**expected_result**

```
1. The TLM stays in the Battery Critical state until 10 seconds have elapsed
2. Normal operation resumes after 10 seconds
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗回復分支，與 -03 之進入分支為獨立部分失效。**10 秒之出處**：`4942354` 逐字為「shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]」—— 非造值（§8.4.1）`

**reasoning**（該 leaf）

> 驗證目標：CFTS010 §1.7.2 之 `4942354` 所定之 Load Shed 與 Battery Critical 兩組條件及其動作與回復。關鍵情境條件：以 LIN 訊號注入分別觸發二者。為什麼這樣切：二者為**不同控制實體**（PN14_LS 訊號組 vs Batt_ST_Crit），依 §8.2.2 之「不同控制實體則拆分」拆為獨立 TC；各自之故障分支（訊號消失之回退）與回復分支（10 秒後恢復）亦為獨立部分失效，再各拆一條，共四條。刻意略過：037 描述所載之「Load Shed 適用 Atlantis High」為 037 之範圍註記，已置於 pre_condition；`4942354` 之 EE Architecture 欄為 Atlantis Mid, Atlantis High，二者不衝突。車型欄依 R30-3 / R30-4 留白，未依 A-PW29 填寫（R-P54）。


---

## 七、§D 全表實測值對照（**上繳項四**）

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | 7 / 7 | PASS |
| **G56** | 範本 DV 比對 | 【實測填入】 | Power 四條 DV **全部落在自身正確欄位**（Q / U–AA / S / AG）；**未沿用 Comfort 座標** | 已填空 |
| **G57** | 其餘屬性 | 【實測填入】 | 分頁 Power 獨有 ＋1；合併 4 項右移一致 ＋ `D5:F5` Power 獨有；條件式格式 Power 獨有 1；**公式 Power 0 / Comfort 592 / Privacy 11**；凍結窗格 Comfort ≠ Privacy | 已填空 |
| **G58** | A-PW46 查證 | 【實測填入】 | **(a) 之變體** —— Comfort 有明文裁決且與 Privacy 相同（留白）；已交付件之 `1` 非管線產生 | 已填空 |
| **G59** | profile 存在且 G50 引用之 | profile 存在；豁免改為引用條款 | profile 已建；豁免以 `PROFILE_PATH.exists()` 為條件；**雙向實測**（有 0 findings / 無 2 findings），不當方括號兩情形皆攔下 | **PASS** |
| **G60** | G51 動詞判準 | 【實測填入】 | 經驗動詞 **20**；人工漏列 **12**；**偽陽性二者皆 0 / 1823 行**；改採聯集 32 個 | 已填空 |
| **G61** | F3 補查 | 【實測填入】 | `Load Shed` 29 次、與 status/state/mode 共現 **0 處**、僅為章節標題 → **非 status** | 已填空 |
| **G62** | 首批 TC 全文完整性 | 13 欄 × 10 條皆有內容 | **無任何空值** | **PASS** |
| G50 / G51 / G54 等 | 沿用 | — | `--self-test` **28 個 fixture ＋ G46 三案全數如期**；真實 lint 阻斷類 PASS、R-P42(b) 0 觸發 | PASS |

**無 MISMATCH。**

---

## 八、**明確回答：R-P79 是否已取得結論，寫回可否開放**（**上繳項五**）

### R-P79 —— **已取得結論**

DV、分頁、合併儲存格、條件式格式、欄寬凍結、公式六項皆已比對。
**條文所憂之核心風險（Power 之 DV 以 Comfort 座標設定）確認未發生** ——
Power 之四條 DV 逐條落在其自身之正確欄位。

### 寫回可否開放 —— **執行層之建議：一項須先裁，其餘不阻斷**

**須先裁者：B 欄之處置（§1.3）。**
Comfort / Privacy 之範本以公式自動編號，故其 pipeline 把 B 列入 `NEVER_WRITE`；
**Power 之 B 欄無公式**。若直接沿用 Comfort 之 `NEVER_WRITE`，
交付件之 No.# 欄將全空。這是一個「照抄他人設定就會出錯」之處，
與 A-PW40 同型 —— 只是這次錯的會是行為而非座標。

**不阻斷者**：
- A-PW52（DV 覆蓋不齊）—— 涉及之三欄依 profile 皆留空
- 條件式格式與 `D5:F5` 之 Power 獨有差異 —— 皆為顯示層，不影響寫入
- 凍結窗格之 Comfort ≠ Privacy —— 依 R-P80 不取多數，且不影響寫入

---

## 九、獨立判斷：本包是否仍有該驗而未驗者（**上繳項六**）

10 上繳包 §7.2 之五項，本包處置：第 1 項→R-P79（六項屬性已比對）；
第 2 項→R-P80（且 B2 再添一例佐證）；第 3 項→R-P82（profile 已建）；
第 4 項→R-P83（動詞已重導）；第 5 項→R-P84（Load Shed 非 status）。

### 9.1 就第 3 項之殘留（下放包指定由執行層自行判斷）

§11 之「no HTML / Markdown tables」與「blank line between fields」二項**仍未實作**。

**執行層判斷：前者應補，後者不應。**

- **「no HTML / Markdown tables」應補** —— 純字串規則，零判斷成分，
  且 TC 內容若含 `|` 分隔之表格會直接破壞工作簿之儲存格內容。實作成本極低。
- **「blank line between fields」不應補** —— 該規則描述的是**工作簿呈現**，
  而本管線之 TC 以 JSON 之獨立鍵儲存，欄位間不存在「空行」之概念；
  在 JSON 層強制之等於發明一個規格未要求之約束。

### 9.2 新增未驗項（五項）

**1.（最重）B 欄無公式一事，是靠「比對公式」偶然查出的。**
   R-P79 列了六項屬性，公式是最後一項。若下放包只列了 DV，
   這個會讓交付件序號全空的差異就不會被發現。
   **而它與 A-PW40 同型：照抄他人設定即出錯。**
   目前沒有任何閘門會在寫回前檢查「B 欄是否有值或公式」。

**2. `Test Case Framework` 分頁 —— Power 獨有，內容完全未讀。**
   B1 只比對了分頁**清單**，未讀該分頁之內容。
   其名稱暗示它可能載有本 feature 之 Test Group / Test Set 期望值 ——
   若如此，它就是一個**未被檢視的權威來源**，且可能與 §E 之定版衝突。

**3. 條件式格式 `H10:H145` colorScale 之語義未查。**
   H 欄為 Test Set。colorScale 施於 r10–r145 而非 r10–r221 ——
   **145 這個上界不明**（037 之資料列末為 r145，疑似關聯）。
   若該格式係為標示某種狀態，寫入 Test Set 值可能觸發非預期之著色。

**4. B2 查出 Comfort 已交付件有管線外之修改，但未查其範圍。**
   我只查了車型欄。**其餘欄位是否亦有管線外之修改，未查。**
   若有，則 10 包 B1 以 Comfort 為第二來源之交叉驗證，其語料本身即不純。
   （r9 標頭為範本層，受影響機率低，但這是推論而非量測。）

**5. profile 已建，但其條款未被任何閘門逐條驗證。**
   G59 只驗了 §3.1 / §3.2 兩項方括號豁免是否隨 profile 存廢而生效。
   profile 之其餘條款（§2 Test Set 清單、§3.3 status 清單、§3.4 檔名、
   §3.5 priority、§3.6–3.8 欄位留白）**皆無閘門對應**——
   它們現在是「寫下來的紀律」，與 08 包所批評之情形同型。

---

## 十、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| **不得寫回 FW036 workbook** | **未寫回任何 workbook** |
| **不得對任何 workbook 呼叫 `save()`** | **未呼叫**。B1 全程 `zipfile` 直讀 XML；B4 以 `read_only=True` 讀 Comfort / Privacy |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補 |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改 |
| 不得修改任何已落檔裁決條文之內文（R-P36） | 未動任何 `[R-Pnn]` 區塊內文 |
| 不得測試未被引用之錨點（R-P42） | 10 條 TC 未變；R-P42(b) 0 觸發 |
| 不得解析任何 RTF 或 OLE stream 之內容 | 未讀任何 RTF 或 OLE stream |
| 不得續行章節層反向缺口調查（R-P37） | 未做任何章節層量測。B5 之搜尋為**錨點內文之字串搜尋**，非章節層缺口調查 |
| 不得變更 §E 之分布數字（R-P35） | 63/24/16/8/3 未動 |
| **不得因 A-PW46 之查證結果改變 Power 車型欄之留白處置** | **未改**；profile §3.8 明訂留白 |
| **不得以「兩份已交付件中一份如此」為由推導任何裁決** | **未推導**。B2 之結論係基於 Comfort **自身之 profile 與腳本**，非基於其交付件內容 |
| 不得調整 `MIN_FINGERPRINT`（R-P62） | 維持 40 |
| 不得擴大批次範圍超出 `Power Down` 3 leaf | **leaf 仍為 3、TC 仍為 10**，未變動 |
| 不得以 repo 現況作為任何 fixture 之測試對照 | 28 個 fixture 與 G46 之違規 yaml 全為合成；G59 之 profile 缺席情境以變數注入，未刪除實檔 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

---

## 十一、待裁

- **Q1（寫回前唯一須先裁者）B 欄之處置。**
  Power 之 B 欄無自動編號公式，而 Comfort / Privacy 有並因此將 B 列入 `NEVER_WRITE`。
  Power 若照抄，交付件序號欄將全空。應明寫序號，或另有處置？
- **Q2 §9.2 第 2 項：`Test Case Framework` 分頁為 Power 獨有，內容完全未讀。**
  其名稱暗示可能載有 Test Group / Test Set 之期望值 —— 是否為未被檢視之權威來源？
- **Q3 §9.2 第 3 項：條件式格式 `H10:H145` colorScale 之語義未查**，
  且其列上界 145 不明。寫入 Test Set 值是否會觸發非預期著色？
- **Q4 A-PW51：Comfort 已交付件之車型欄 `1` 非由其管線產生。**
  是否向 Comfort 回報？併請裁示 §9.2 第 4 項 —— 其餘欄位是否亦有管線外修改。
- **Q5 §9.1：§11 之「no HTML / Markdown tables」是否補入 G50**
  （執行層建議補；「blank line between fields」建議不補，理由見 §9.1）。
- **Q6 §9.2 第 5 項：profile 之其餘條款無閘門對應**，現為「寫下來的紀律」。
- **Q7 A-PW52：Power 範本之 DV 覆蓋範圍不齊**（三欄僅涵蓋 2–4 列）。
- **Q8 首批 10 條 TC 之全文覆核**（§六已附）。
