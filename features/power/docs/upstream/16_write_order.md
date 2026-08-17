# 上繳包 16 —— 寫回排序規則與 dry-run

> 對應下放包：`features/power/docs/handoff/16_write_order.md`（含追加條文 R-P117 / §B6）
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/` 之原始檔**；**未指派最終 tc_id**；
> **未實作亦未建議 R-P116 之任一處置**；**未依 Arif 素材改動 G77 或任何 TC**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

---

## 一、B3 dry-run 之完整實測（必附一）

### 1.1 沙箱與來源之同一性

| 項目 | 值 |
|---|---|
| 來源 | `inputs/…_SWQT_PowerManagement_20260816.xlsx` |
| 來源 SHA256（dry-run 後重算）| `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| 沙箱副本 `sandbox/base.xlsx` SHA256 | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` |
| **來源未被觸碰** | **True**（二者相同）|
| 輸出 `sandbox/dryrun.xlsx` SHA256 | `99c1ad9373aa5f384016bf253f234a05d24ecc7780561d847f0ad67b38c4d3a0` |
| 沙箱版控 | `features/power/sandbox/.gitignore` = `*`（**不入版控**，R-P114(a)）|
| 寫回路徑 | `backend/xlsx_surgical.py` 之 `surgical_save()` —— **全程無 `Workbook.save()`** |
| 寫入條數 | **10**（僅臨時 tc_id 001–010，R-P114(e)；011–015 未納入）|

### 1.2 G66 —— B 欄非空列數（**真實**）

| 項目 | 實測 |
|---|---|
| B 欄非空列數 | **10** |
| TC 列數 | 10 |
| **判定** | **PASS** |

Power 之範本無 `IF(ISBLANK($D10),"",ROW()-9)` 編號公式（11 包 B1），
故 B 欄由寫回程式明寫序號 —— 此即 R-P90 之處置，本次為其首度真實驗證。

**失敗證明**：以刻意留空 B 欄之副本 `sandbox/fail_b.xlsx` 重跑 ——
`b_filled = 0 / 10`，
**判定 FAIL**。該閘確實可能失敗。

### 1.3 G71 —— 17 組欄位對應之實際落點（**真實**）

| 欄位鍵 | 儲存格 | r9 標頭（實測）| 寫入之值 | 判定 |
|---|---|---|---|---|
| `req_id` | `D10` | Requirement or Design ID / 需求/設計 ID | `SWE-PM-071` | **PASS** |
| `tc_id` | `F10` | Test Case ID / 測試用例ID | `NR1L-PowerManagement-001` | **PASS** |
| `test_group` | `G10` | Test Group / 測試組 | `Power Management` | **PASS** |
| `test_set` | `H10` | Test Set / 測試集 | `Power Down` | **PASS** |
| `test_item` | `I10` | Test Item / 測試項目 | `Splash screen shown after SplashSc` | **PASS** |
| `pre_conditions` | `J10` | Pre-Conditions / 先前條件 | `1. A suspend-resume boot sequence ` | **PASS** |
| `input_test_data` | `K10` | Input Test Data / 輸入條件 | `NA` | **PASS** |
| `test_procedure` | `L10` | Test procedure / 測試程序 | `1. Start the suspend-resume boot s` | **PASS** |
| `expected_result` | `M10` | Expected Result / 預期結果 | `1. The TLM display stays blank whi` | **PASS** |
| `spec_reference` | `N10` | Specification Reference  / 規格參考 | `R1LR_Atl-H_25PI3.5_Activation and ` | **PASS** |
| `tc_ref_id` | `O10` | Test Case Reference ID / 測項參考ID | `NEW` | **PASS** |
| `estimated_time` | `P10` | Estimated Test Time (mins) / 預估測試時間 / （分 | （留白） | **PASS** |
| `priority` | `Q10` | Test Case Priority / 測試用例優先級別 | `P1` | **PASS** |
| `design_method` | `S10` | Test Case Design  / Methods / 測試用例設計方法 | `狀態轉換 (State Transition Testing)` | **PASS** |
| `functional_safety` | `T10` | Functional Safety / 功能安全 | `NA` | **PASS** |
| `author` | `AB10` | Test Case Author / 測試案例作者 | `PeiPYHsu` | **PASS** |
| `remarks` | `AI10` | Remarks / 備註 | （留白） | **PASS** |

**17 / 17 PASS。** A-PW40 之人工盤點於此獲得寫回層之真實佐證 ——
`priority` 落於 `Q`（非 scaffold 所記之 `P`）、`design_method` 落於 `S`、
`author` 落於 `AB`、`remarks` 落於 `AI`（非 `AH`，`AH` 實為 Defect ID）。

> **一項作業瑕疵（本節首次執行時）**：`remarks` 之期望值我原設為「須非空」，
> 而本批十條皆無備註，致 `AI10` 被誤報 FAIL。
> **該 FAIL 是我的量測規則錯，不是欄位錯位** —— 標頭實測確為 `Remarks / 備註`。
> 已改為「選填欄，空白即為預期」並於程式碼註記該次誤報。

**失敗證明**：以欄位整體右移一格之副本 `sandbox/fail_shift.xlsx` 重跑 ——
**G71 六欄 FAIL**；G72 首列變為
`test_group = 'NR1L-PowerManagement-001'`、
`design_method = None`、
`functional_safety = '狀態轉換 (State Transition Testing)'`
—— 即 design method 被寫進 functional safety 欄。二閘皆確實可能失敗。

### 1.4 G72 —— profile 條款之工作簿層檢查（**真實**）

十列逐列相符：
`test_group` 全為 `Power Management`（profile §2）；
`design_method` 全為下拉選單九詞條之一（§3.3）；
`spec_reference` 全為 CFTS 檔名 ＋ 章節號形態（§3.4）；
`functional_safety` 全為 `NA`（§3.7）；
`estimated_time`（P 與 R 兩欄）與車型欄 U–AA **全部留白**（§3.6 / §3.8，R-P54 / R-P81）。

**§3.6 / §3.8 之留白檢查即 14 包 G67 所稱「須待寫回方能檢查」之二項 ——
本包一併完成。**

### 1.5 G87 —— XML 層 diff

| 項目 | 實測 |
|---|---|
| `surgical_save` 所修補之 member | `['xl/worksheets/sheet6.xml']` |
| 前後**實際相異**之 member | `['xl/worksheets/sheet6.xml']` |
| zip member 集合相同 | **True** |
| 分頁清單（含 state）相同 | **True** |
| 合併儲存格相同 | **True** |
| 條件式格式相同 | **True** |

> **僅 `xl/worksheets/sheet6.xml` 一個 part 相異，即目標分頁本身。無非預期變動。**

`surgical_save` 之 `verify_structure()` 亦獨立通過（zip member 集合相等、
逐分頁 DV 計數相等、僅已修補之 part 相異）—— 未拋 `StructureError`。

---

## 二、G86 —— DV 存活之逐條前後對照（必附二，R-G3 首度實測）

| ns（前）| sqref（前）| type（前）| ns（後）| sqref（後）| type（後）| 判定 |
|---|---|---|---|---|---|---|
| `main` | `B7:C7` | `list` | `main` | `B7:C7` | `list` | **同** |
| `main` | `AG10:AG13` | `list` | `main` | `AG10:AG13` | `list` | **同** |
| `main` | `Q10:Q221 R10:R11 P10:P11` | `list` | `main` | `Q10:Q221 R10:R11 P10:P11` | `list` | **同** |
| `main` | `U10:AA221` | `list` | `main` | `U10:AA221` | `list` | **同** |
| `x14` | `S10:S221` | `list` | `x14` | `S10:S221` | `list` | **同** |

> **五條 DV 全數存活，含 x14 之 `S10:S221`（design method 下拉），逐字相同。**

### 執行層之區辨（不得混稱）

**此結果不表示「R-G3 之缺陷不存在」。**
`surgical_save` 之設計正是為繞開該缺陷 —— 它**不呼叫 `Workbook.save()`**，
而是將 openpyxl 算出之儲存格差異**貼回原始 sheet XML 之文字**，
其餘每一個 zip member **位元組照抄**。

**本次實測所證明者**：該繞道對本 workbook **確實有效**。
**本次實測未證明者**：openpyxl `save()` 已可安全使用 —— 該路徑本包未執行，
亦依 16 §I 不得執行。已登記 A-PW77。

---

## 三、B2 排序腳本與 G85（必附三）

`features/power/scripts/assign_final_tc_id.py`
排序鍵 `(int(SWE-PM 數字部分), split_index)` —— 二者皆整數，全序且可重現。

### G85 —— 回歸斷言（R-P55），以**合成亂序資料**驗證

| 斷言 | 期望 | 實測 |
|---|---|---|
| 排序後 req_id 序 | 071×4 → 072×2 → 073×9 | **相符** |
| 各 leaf 內 split_index 自 1 連號 | `1,2,3,4 / 1,2 / 1..9` | **相符** |
| final_tc_id 自 001 起連號 | `001, 002, 003, …, 015` | **相符** |
| 缺 `split_index` | 須報錯，不得預設 0 | **ValueError** |
| 帶後綴之 `req_id`（R-P86）| 須報錯 | **ValueError** |

**G85 五案全數如期。**

### 首批之最終 tc_id 對照（**預覽，未指派**）

`data/final_tc_id_map.tsv`。R-P113(c) 明訂最終指派於全部 114 leaf 完成後為之，
**本腳本不改寫任何批次 JSON**。

| 列 | final（預覽）| provisional | req_id | split_index |
|---|---|---|---|---|
| 1–4 | 001–004 | 001–004 | SWE-PM-071 | 1–4 |
| 5–6 | 005–006 | 005–006 | SWE-PM-072 | 1–2 |
| 7 | 007 | 007 | SWE-PM-073 | 1 |
| 8 | 008 | 008 | SWE-PM-073 | 2 |
| **9** | **009** | **011** | SWE-PM-073 | 3 |
| **10** | **010** | **012** | SWE-PM-073 | 4 |
| **11** | **011** | **009** | SWE-PM-073 | 5 |
| **12** | **012** | **014** | SWE-PM-073 | 6 |
| 13 | 013 | 013 | SWE-PM-073 | 7 |
| **14** | **014** | **015** | SWE-PM-073 | 8 |
| **15** | **015** | **010** | SWE-PM-073 | 9 |

### 一項實測衝突（A-PW78）

**若逕以排序鍵重排 JSON 陣列，G38 / §10.3 會判「tc_id 未單調遞增」——
實測 3 項 FAIL**（`009` / `013` / `010`）。
處置：**JSON 陣列序維持臨時 tc_id 遞增序；寫回列序另由排序鍵決定。二者刻意分離。**
已載於 profile §4.5 與批次檔頭之 `tc_id_note`。**未放寬 G38。**

---

## 四、B4 —— R-P116 之裁定素材（必附四，**不含建議**）
## 1. Comfort 已交付件中是否存在「僅填 `req_id` 而其餘欄留空」之列

依 **R-P80**，僅取其結構性事實。

| 量測項 | 值 |
|---|---|
| `D` 欄（Requirement or Design ID）非空之列 | **466** |
| 其中「僅 `D` 欄（＋`B` 序號）有值、其餘 33 欄全空」者 | **0** |

即：**Comfort 之已交付件無此形態之先例。**
（此為事實陳述，不蘊含任何一種處置為正確。）

## 2. 037 之 `SWE-PM-088` / `089` / `090` 三筆

取自 `Power_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
之 `SWE1 Requirements` 分頁（G0 台帳內之素材）。

| 欄 | SWE-PM-088 | **SWE-PM-089** | SWE-PM-090 |
|---|---|---|---|
| Source Requirement ID | `Sys-RA-PM-0331` | **`SWE1-PM-ANT-008`** | `Sys-RA-PM-0343` |
| Requirement Title | Vehicle Line-Based Performance Gauge Selection | **Seasonal Startup Animation Selection** | Auto Theme Mode Selection |
| Categorization | Functional Requirement | **Functional Requirement** | Functional Requirement |
| Sub Categorization | HMI Service | **HMI Service** | HMI Service |

**與 R-P1 / DR-PW1 直接相關之事實**：`089` 之 `Source Requirement ID` 為
`SWE1-PM-ANT-008` —— **非 `Sys-RA-*` 形態**，故 §C rule 1 之錨點鏈於此斷開，
此即該 leaf 依 R-P1 留空之原因。088 / 090 皆為正常之 `Sys-RA-PM-*`。

其 `Categorization` 與 `Sub Categorization` 與前後兩筆**完全相同**，
即：**從 037 之分類欄看不出 089 有任何特殊性**，其特殊性全在來源 ID 之形態。

## 3. 二種處置對列數與 B 欄序號之影響

前提：R-P113(e) —— 工作簿列序即 SWE-PM ID 序，故 `089` 之位置介於
`088` 之末條與 `090` 之首條之間。設全案 TC 總數為 `N`（尚未定，
首批 3 leaf 已產出 15 條）。

| | （甲）保留一列空白 | （乙）整列跳過 |
|---|---|---|
| 工作簿資料列數 | **N + 1** | **N** |
| `B` 欄序號最大值 | N + 1 | N |
| `089` 之後所有列之 `B` 值 | 較（乙）**各 +1** | —— |
| 最終 `tc_id` 之連號 | 若該空列**不配 tc_id**，則 tc_id 仍為 1..N 而**列號與 tc_id 自 089 之後全面錯開**；若配 tc_id，則有一個 tc_id 對應不到任何 TC | tc_id 與列號自始至終一致 |
| 客戶以 037 比對時 | 037 之 115 筆與工作簿逐筆對得上（含 089 之空列）| 工作簿無 089 之痕跡，需另行說明其缺席 |
| 涵蓋率之呈現 | 空列會被計入列數，若有人以「列數 / 037 筆數」計算覆蓋率將失真 | 不受影響 |

**114 / 115 之關係**：037 有 **115** 筆 SWE-PM ID（G1 實測，連續），
其中 `089` 依 R-P1 不產 TC，故可測者 **114**。
§E 之 `63 / 24 / 16 / 8 / 3 = 114` 為 **leaf 數**，非 TC 數 ——
TC 數因 §8.2.2 拆分而大於 114（首批 3 leaf 已產 15 條）。
**二種處置皆不影響 §E。**

---

**執行層未提出建議，未實作任何一種（16 §I）。**

---

## 五、`008` / `009` 全文 —— 15 包已附，本包僅報異動（必附五）

依 16 §B5，15 包上繳 §一已附 `008` / `009` 全文，**本包不重附**。

**本包對該二條之唯一異動**：新增 `split_index` 欄
（`008` → 2、`009` → 5，R-P115）。其餘十六欄一字未改。

---

## 六、B6 —— `SWE-PM-073` 涵蓋缺口補測（R-P117）

### 6.1 `4942354` 完整原文之 13 項行為與覆蓋對照

| # | 行為（規格逐字要旨）| 覆蓋 |
|---|---|---|
| 1 | `PN14_LS_Actv=[1h]` 與 `PN14_LS_Lvl7=[1h]` → 立即將最大音量降為 20 | `007` |
| 2 | 若原音量較大，送出帶更新值之 `AUD_LVL` | `007` |
| 3 | 若 Ecall/ACN/chimes 未啟用 → TLM 靜音 | `007` |
| 4 | ICS 模組斷電 | `007` |
| 5 | 訊號遺失時沿用最後值 **until broadcast resumes** | `008`（僅不恢復側）→ **`011` 補回復側** |
| 6 | 若不恢復 → 維持整個 ignition key cycle | `008` |
| 7 | **通話轉移至 head set（Load Shed 段）** | **無 → `012`** |
| 8 | BODY ON **或 BODY OFF-TIMED** 下收到 `Batt_ST_Crit=[1h]` → 最小化耗流 | `009`（僅 BODY ON）→ **`014` 補 BODY OFF-TIMED** |
| 9 | 立即將最大音量降為 20 | `009` |
| 10 | 若原音量較大，送出 `AUD_LVL` | `009` |
| 11 | 若 Ecall/ACN/chimes 未啟用 → 靜音 | `009` |
| 12 | **通話轉移至 head set（Battery Critical 段）** | **無 → `013`** |
| 13 | 停留至 **voltage out of range** 條件滿足 **或** `Batt_ST_Crit=[0h]` 後 10 秒回正常 | `010`（僅後者）→ **`015` 補前者** |

**三項缺口與分析層之判定完全一致。** `SWE-PM-073` 之 TC 由 4 增為 **9**；
**leaf 數仍為 3**，未構成 R-P72 所禁之範圍擴大。

### 6.2 `SWE-PM-071` / `072` 之同型對照 —— **無缺口**

| leaf | 行為項 | 覆蓋 |
|---|---|---|
| `071` | (1) SplashScreen_Time 後載入 splash | `001` |
| | (2) 轉往 Standby 時不顯示 | `002` |
| | (3) 轉往 Bench 時不顯示 | `003` |
| | (4) StandardScreen_Time 後顯示 standard screen | `004` |
| `072` | (1) 開機期間之事件須被辨識 | `005` |
| | (2) 依 TLM_Status 轉換處理（**該轉換定義於 CFTS009 §1.6.2.1.15，依 R-P42 不在範圍**）| `006`（範圍內部分）|
| | (3) 須緩衝、不遺失 | `005` |
| | (4) 儘快處理，depending on boot timings | `006` |

**`071` 4 / 4、`072` 4 / 4（其中一項受 R-P42 限縮）—— 皆無同型缺口。**

### 6.3 補測之五條全文


### NR1L-PowerManagement-011 — SWE-PM-073（split_index 3）

**tc_id**：`NR1L-PowerManagement-011`

**req_id**：`SWE-PM-073`

**split_index**：`3`

**tc_title**：`Load Shed recovers: normal volume and audio restored`

**test_set**：`Power Down`

**test_item**：`Load Shed recovers: normal volume and audio restored`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
```

**input_test_data**

```
STATUS_LIN.PN14_LS_Actv = [0h]
STATUS_LIN.PN14_LS_Lvl7 = [0h]
```

**test_procedure**

```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Resume the broadcast with the recovery values listed in Input Test Data
3. Read the volume limit and the audio output state to check that Load Shed ends
```

**expected_result**

```
1. The two Load Shed signals are absent from the bus trace
2. The TLM accepts the resumed broadcast without a bus error
3. The volume limit returns to its normal maximum and the audio output is unmuted
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 Load Shed 之回復分支：訊號廣播恢復後 Load Shed 動作結束`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P117(a)（16 包）**：`4942354` 載「the last values ... shall be used **until load shed signal broadcast resumes**」。`008` 僅測「不恢復 → 維持整個 ignition key cycle」，**未測 `until ... resumes` 之回復側**。對照 Battery Critical 有 `009`（進入）與 `010`（回復），Load Shed 原有進入（`007`）、故障（`008`）而**無回復**。本條補之。

### NR1L-PowerManagement-012 — SWE-PM-073（split_index 4）

**tc_id**：`NR1L-PowerManagement-012`

**req_id**：`SWE-PM-073`

**split_index**：`4`

**tc_title**：`Continuing call transferred to head set under Load Shed`

**test_set**：`Power Down`

**test_item**：`Continuing call transferred to head set under Load Shed`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. A non-Ecall non-ACN call is active and continuing
```

**input_test_data**

```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
```

**test_procedure**

```
1. Send the two Load Shed signals listed in Input Test Data
2. Read the call audio routing to check that the call moved to the head set
```

**expected_result**

```
1. The TLM accepts both Load Shed signals without a bus error
2. The continuing call is routed to the head set and is not dropped
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗通話轉移分支（Load Shed 側）：進行中之非 Ecall/ACN 通話轉至 head set`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P117(b)（16 包）**：`4942354` 於 Load Shed 段載「The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active」，13 / 14 / 15 包之四條 TC **皆未測**。本條補之。

### NR1L-PowerManagement-013 — SWE-PM-073（split_index 7）

**tc_id**：`NR1L-PowerManagement-013`

**req_id**：`SWE-PM-073`

**split_index**：`7`

**tc_title**：`Continuing call transferred to head set under Battery Critical`

**test_set**：`Power Down`

**test_item**：`Continuing call transferred to head set under Battery Critical`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. A non-Ecall non-ACN call is active and continuing
```

**input_test_data**

```
STATUS_LIN.Batt_ST_Crit = [1h]
```

**test_procedure**

```
1. Send the Battery Critical signal listed in Input Test Data
2. Read the call audio routing to check that the call moved to the head set
```

**expected_result**

```
1. The TLM accepts the Battery Critical signal without a bus error
2. The continuing call is routed to the head set and is not dropped
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗通話轉移分支（Battery Critical 側）：進行中之非 Ecall/ACN 通話轉至 head set`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P117(b)（16 包）**：`4942354` 於 Battery Critical 段另載同一句通話轉移要求。**兩處各為獨立觸發**（Load Shed 訊號組 vs `Batt_ST_Crit`），依 §5.7「不同觸發即拆分」與 profile §4 拆為 `012` / `013` 兩條，非重複。

### NR1L-PowerManagement-014 — SWE-PM-073（split_index 6）

**tc_id**：`NR1L-PowerManagement-014`

**req_id**：`SWE-PM-073`

**split_index**：`6`

**tc_title**：`Battery Critical minimizes draw in BODY OFF-TIMED mode`

**test_set**：`Power Down`

**test_item**：`Battery Critical minimizes draw in BODY OFF-TIMED mode`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY OFF-TIMED mode
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

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 mode 分支：Battery Critical 於 BODY OFF-TIMED 模式下之行為（`009` 為 BODY ON）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P117(c)（16 包）**：`4942354` 載「While in BODY ON **or BODY OFF-TIMED** mode」，而 `009` 之 pre-condition 僅 `BODY ON`。依 §8.3「mode 為拆分軸」補 BODY OFF-TIMED 一條。

### NR1L-PowerManagement-015 — SWE-PM-073（split_index 8）

**tc_id**：`NR1L-PowerManagement-015`

**req_id**：`SWE-PM-073`

**split_index**：`8`

**tc_title**：`Battery Critical exits on voltage out of range condition`

**test_set**：`Power Down`

**test_item**：`Battery Critical exits on voltage out of range condition`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The Battery Critical condition is already active
3. The vehicle voltage out of range condition can be applied on the bench
```

**input_test_data**

```
STATUS_LIN.Batt_ST_Crit = [1h] (held)
```

**test_procedure**

```
1. Keep the Battery Critical signal at the value listed in Input Test Data
2. Apply the voltage out of range condition on the bench
3. Read the volume limit and the audio output state to check that the state is left
```

**expected_result**

```
1. The TLM stays in the Battery Critical state while the signal is held
2. The TLM registers the voltage out of range condition
3. The TLM leaves the Battery Critical state without waiting for the signal to clear
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗回復條件之第一分支：voltage out of range（`010` 驗第二分支之 10 秒逾時）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P117(c)（16 包）**：`4942354` 之回復條件為「until **either voltage out of range conditions are satisfied** or shall go back to normal behavior 10 seconds after ...」，`010` 僅測後者。本條補前者。
**執行層須明報之限制**：該錨點**未載 voltage out of range 之電壓門檻值**，依 §8.4.1 不造值、依 R-P42 不得赴其他未被引用之錨點取值，故 procedure 以「套用該條件」表述而非給定電壓。**此條在取得門檻值前不可實際執行** —— 已於上繳包 §七提請分析層裁定是否開 DR。

### 6.4 補測後之 lint

`exit=0`；阻斷類 **PASS**；待人工裁決類無觸發。
15 條全數通過 G45 / G63 / G73 / G77 / G79 / G81 / G82。

---

## 七、§D 全表自驗（必附六）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G85** | 排序腳本邏輯 | 071×4 → 072×2 → 073×N；split_index 各 leaf 內自 1 連號 | 071×4 → 072×2 → **073×9**；連號相符；另二案（缺鍵、帶後綴）皆報錯 | **PASS** | 合成 |
| **G86** | dry-run DV 存活 | 四條 DV（含 x14）前後是否逐字相同 | **實測為五條**（四 main ＋ 一 x14）；**全部逐字相同** | **PASS** | **真實** |
| **G66** | B 欄非空列數 = TC 列數 | 10 / 10（真實）＋ 失敗證明 | **10 / 10**；B 欄留空 → **0 / 10 FAIL** | **PASS** | **合成＋真實** |
| **G71** | `workbook.columns` 對實測標頭 | 17 / 17（真實）＋ 失敗證明 | **17 / 17**；右移一格 → **6 欄 FAIL** | **PASS** | **合成＋真實** |
| **G72** | profile 條款之工作簿層檢查 | 真實 ＋ 失敗證明 | 十列逐列相符；右移一格 → `design_method` 變 `None` | **PASS** | **合成＋真實** |
| **G87** | XML 層 diff | 變動之 part 清單 | **僅 `xl/worksheets/sheet6.xml`**；members / sheets / merges / cf 皆相同 | **PASS** | 真實 |
| G63 / G73 / G77 / G79 / G81 / G82 | 沿用 | 15 條全 PASS | 全 **0 findings** | **PASS** | 合成＋真實 |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3 | `exit=0`；leaf **3**；TC **4 → 15**（R-P117 補測）| **PASS** | 真實 |
| G1–G84 | 沿用（G17 已移除）| 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

**§D 之期望值「四條 DV」與實測「五條」不符** —— 實測為
`B7:C7`、`AG10:AG13`、`Q10:Q221 R10:R11 P10:P11`、`U10:AA221` 四條 main
**加上** x14 `S10:S221` 一條，共五條。11 包 B1 之表列亦為四條 main ＋ 一條 x14。
**判為下放包之計數口徑（僅計 main）與本包（含 x14）不同，非實測異常。**

**G67 覆蓋率更新**：profile 增訂 §4.5 後共 **25 條**，
可機械檢查 **21**，已有閘門 **21**（新增 G85；§3.6 / §3.8 之留白檢查由本包 dry-run 補齊）
—— **21 / 21 = 100%**。
—— 惟仍須提醒：**覆蓋率 100% 與品質無關**。15 包所查出之三項在覆蓋率 89% 時全都零觸發，
而本包 R-P117 之三項缺口，**在覆蓋率 100% 之今日依然沒有任何閘門會發現**。

---

## 八、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

**（甲）本包新產生或新暴露之該驗而未驗者 —— 六項**

1. **`015` 在取得 `voltage out of range` 門檻值前不可實際執行（A-PW79）。**
   我依 R-P117(c) 補了這條，但該錨點只寫了條件的**名字**，沒有電壓值。
   §8.4.1 不許我造值，R-P42 不許我去別的錨點找。
   **結果是一條寫得出來、卻執行不了的 TC。** 我沒有自行開 DR（那是分析層的），
   但這件事必須有人處理，否則它會以「已覆蓋」的姿態留在交付物裡。

2. **R-P117 之三項缺口，在閘門覆蓋率 100% 的今天依然無人能發現。**
   查出它們的是「人讀規格原文逐句對照 TC」。
   G82 只驗 ER 的具名標的在不在 `source_clause` 裡 ——
   **它不會問「`source_clause` 裡有而 ER 裡沒有的，是什麼」**。
   這個方向的檢查（規格 → TC 的反向涵蓋）**本包沒有做成閘門**，
   我也不確定它能不能機械化。這是目前最大的結構性缺口。

3. **`071` / `072` 無缺口這個結論，是我自己比對的。**
   與 15 包 §七第 2 項同型：**判「無缺口」的人，就是當初寫出 `073` 三項缺口的人。**
   `072` 我還額外做了一次 R-P42 的範圍限縮判斷（TLM_Status 轉換定義不在範圍），
   那個判斷若錯，`072` 就有第五項行為未測而我報了「無缺口」。

4. **dry-run 只寫了 10 條、只用了一個 workbook、只跑了一次。**
   G66 / G71 / G72 現在有「真實」證據了，但那是**一次**寫回、**十列**、
   **BLANK 工作簿**（無既有列需保護）。真正的寫回是 N 列、單次、
   且屆時工作簿裡可能已有他人的列。**append 之邊界保護本包完全沒測。**

5. **`surgical_save` 的 `verify_structure` 我是「它沒拋例外」就當它通過。**
   我沒有獨立驗證它的三個檢查本身是對的（zip member 集合、DV 計數、
   相異 part 集合）。它是 backend 的共用元件，不在本 feature 的閘門體系內 ——
   **本專案至今沒有任何一道閘門在驗這個唯一授權之寫回路徑。**

6. **B4 的「Comfort 無此形態之先例」只證明了 Comfort 沒有。**
   我沒查 Privacy、Home、或其他 20 個 feature。
   15 包才因為加入 Home 而讓 G77 的結論翻轉，**這裡我又只用了一個母體。**
   若分析層要以「有無先例」作為 R-P116 的裁定依據，這個素材的母體太小。

**（乙）已驗而應標明其強度不足者 —— 二項**

7. **G86 之「DV 全數存活」證明的是繞道有效，不是缺陷消失。**
   已於 §二與 A-PW77 逐字區辨，未讓它以「R-G3 已解決」的形式流出。

8. **G85 全部以合成資料驗證，未見真實批次。**
   `assign_final_tc_id.py` 對真實 15 條也跑過並產了對照表，
   但那次沒有斷言 —— **有斷言的是合成資料，有真實資料的沒有斷言。**
   要等 114 leaf 全部產出後才有真正的回歸對象。

**（丙）本包自身之作業瑕疵 —— 一項**

9. **G71 的第一次量測我把 `remarks` 的期望值寫成「須非空」，誤報了一個 FAIL。**
   已修正並在程式碼裡註記該次誤報，未把錯誤的 FAIL 或修正後的 PASS 其中任一
   單獨呈現。

**（丁）下放包本身之三項記載事項**（陳述，非指摘）

- §J 自檢寫「**四條**」，而追加條文使本包實為 **五條**（R-P113 ~ R-P117）。
  已按五條抄入 RULINGS.md。
- §F 所擬之 A-PW73 / 74 / 75 **與 15 包既有之 A-PW73 / A-PW74 衝突**，
  依「撤回列不刪、不重編號」順延為 **A-PW75 / A-PW76 / A-PW77**。
- §D 之「四條 DV」與實測「五條」為計數口徑差異（是否含 x14），非實測異常。

---

## 九、DATA_REQUESTS

DR-PW1（High，併 R-P116 之待裁）、DR-PW5（High）、
DR-PW3 / DR-PW6（Medium）、DR-PW7（Low）維持 live；DR-PW2、DR-PW4 維持撤回。
**本包無新增** —— `015` 之門檻值缺口已列入待裁，由分析層決定是否開 DR。

---

## 十、寫回狀態

R-P113(d) 已裁定為**全部 114 leaf 完成後單次寫回**，
故現階段不存在「開放與否」之問題。
R-P98 / R-P105 / R-P112 之覆核義務不受影響（`008` / `009` 待覆核）。
**dry-run 僅對沙箱副本為之，客戶樹與 `inputs/` 未被觸碰（SHA256 佐證見 §1.1）。**

---

## 十一、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/scripts/dryrun_write_back.py` | dry-run 寫回（新增；`surgical_save`，無 `save()`）|
| `features/power/scripts/assign_final_tc_id.py` | 最終 tc_id 排序（新增，含 G85 自測）|
| `features/power/data/b3_dryrun.json` | dry-run 之完整實測資料（新增）|
| `features/power/data/b4_089_row_material.md` | R-P116 裁定素材（新增）|
| `features/power/data/final_tc_id_map.tsv` | 最終 tc_id 對照表預覽（新增）|
| `features/power/data/b1_before16.json` | 15 包版快照（新增）|
| `features/power/sandbox/` | 沙箱（**`.gitignore` = `*`，不入版控**）|
| `features/power/generated/batch_001_power_down.json` | `tc_id_status`、`split_index`、補測五條（改）|
| `docs/runtime/profiles/FW036_R1L_Power_Profile.md` | §4.5 tc_id 兩階段指派（改）|
| `features/power/RULINGS.md` | R-P113 ~ R-P117（改）|
| `features/power/ANOMALIES.md` | A-PW75 ~ A-PW79（改）|
| `features/power/docs/handoff/16_write_order.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/16_write_order.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 16 輪索引（改）|
