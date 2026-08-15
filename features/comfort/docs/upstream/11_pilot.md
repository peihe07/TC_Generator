# 上繳包 11 — pilot 14 條 ＋ lint ＋ §9 自評 ＋ 九軸複掃

執行層 → 分析層。2026-08-15。回應下放包 `19_pilot_rulings.md` §7。

**結論：九項作業全部完成。pilot 14 條已生成，lint 25 gate 全 PASS，
§9 self-check 17 項逐條自評完成。未寫回 workbook。**

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **13.5 之可觀察量確實存在，未觸發停下** —— 條文自身命名之量為 **`level`**（13.6：`Once the minimum or maximum **level** has been reach`；037 之 `-080-01` 亦用同詞）。ER 以「level 移動一個 step」表述，**無任何級距量值**。R-C22 落實 |
| **乙** | **`080-02` 與 `081-02` 判為 `duplicate_of`** —— 兩者之區別內容**恰好就是**被 19 §4 判為委派之部分（Core N0 之長按參數、CFTS044 之等效性）。扣除委派後無獨立可觀察差異，依 §4.6 標 `axis=none` ＋ `duplicate_of`。**這是忠實反映收窄，不是省略 leaf** —— 14 個 leaf 皆有 TC |
| **丙** | **九軸複掃：129 節中 44 節命中至少一軸**；另有 **9 節含條件句式而九軸皆未命中**，清單見 §5，供第二輪裁 |

---

## 1. 19 §7 —— 九項逐項

| # | 項目 | 狀態 |
|---|---|---|
| 1 | R-C21、R-C22 貼入 `RULINGS.md` | ✅ 現 **24 條** |
| 2 | profile §3.2 增第九軸、§3.4 增第五列 | ✅ |
| 3 | A-CF14 依 R-C21 列入 **Comfort** 之 `DATA_REQUESTS.md` | ✅ #12，**home 檔案零變更**（實測 `git status` 0） |
| 4 | HMI Core L&F、CFTS044 列 `DATA_REQUESTS`，Low | ✅ #13／#14，註明 out of scope、僅供查考 |
| 5 | 生成 pilot 14 條 | ✅ §3 |
| 6 | lint ＋ §9 自評 | ✅ §4 |
| 7 | 全 129 節九軸複掃 | ✅ §5 |
| 8 | 不寫回 workbook | ✅ 未動 `output/`，`DELIVERY.sha256` 仍 2 筆 |
| 9 | 上繳 | 本檔 |

### 1.1 profile 兩處增補之措辭

**§3.2 第九軸**寫入時同時落實 19 §2.1 之禁令與 §2.2 之判定測試：

> **第九軸之 source class 逐節判定，不得跨節套用措辭**：讀該節 `full_text`，
> 條文有字面表述者標 `spec-verbatim` 並照錄；由條文推得者標 `spec-derived`。
> **不得將 6.3 之 `non-foldable secondary lower screen` 措辭套用於 13.x。**
>
> **lower screen 之 stowed／retracted 為執行期狀態，非配置軸。** 判定測試：
> 該 TC 之驗證目標是否就是「螢幕處於該狀態時之行為」？是 → `pre_conditions`；
> 否 → `test_procedure`。

**§3.4 第五列**依 19 §3 之位置分割，**未新增例外**。

---

## 2. 13.5 可觀察量之取得過程（19 §5 之前置）

19 §5 要求：13.5 之可觀察量**自 13.2 ~ 13.6 之 `full_text` 取得**，
不得由下放包指定，確無則回報停下。通讀五節，逐節列出條文自身命名之
可觀察量：

| 節 | 條文命名之可觀察量 |
|---|---|
| `13.2` | `Seats tab`、`Seat Control Popup`、5 秒 timeout |
| `13.2.1` | 四種調整類型之名稱 |
| `13.3` | （無新增；指涉 popup／tab change） |
| `13.3.1` | `the selected option` |
| `13.4` | （無新增） |
| `13.5` | **無** —— 僅 `a small set amount` |
| `13.6` | **`level`**（`the minimum or maximum level`）、`grey out`、`error tone` |

**13.5 自身確無**，但 **13.6 命名了 `level`**，且 037 之 `SWE1-HVAC-080-01`
描述亦作 `fast increase/decrease of lumbar/bolster **level**`。
故 13.5 之 ER 以 **level 移動一個 step** 表述 —— 該量由**同批條文**命名，
非本層指定，符合 19 §5 之要求。**不需停下，不標 BLOCKED**（R-C22）。

---

## 3. pilot 14 條

Test Group `Comfort` ／ Test Set `Seat Control Tab` ／
tc_id **`NR1L-ComfortHMI-001` ~ `-014`**（generator 依位置指派，R-C7）。
條文一律讀 `data/section_fulltext.tsv`（**未讀 `layer3_map.tsv` 之截斷標題**，
R-C18）。生成器 `scripts/gen_pilot.py`，可重跑。

| tc_id | req_id | outline | 主題 | P | duplicate_of |
|---|---|---|---|---|---|
| 001 | -076-01 | 13.2 | 螢幕未收合 → 下螢幕切 Seats tab | P1 | |
| 002 | -076-02 | 13.2 | 螢幕收合 → HU 顯示 Seat Control Popup（5s timeout） | P1 | |
| 003 | -076-03 | 13.2 | 螢幕收合且已在 climate section → 切 Seats tab | P1 | |
| 004 | -077 | 13.2.1 | 四種腰靠／側靠調整類型 | P1 | |
| 005 | -078-01 | 13.3 | 第一次按壓只觸發 popup／tab，不套用調整 | P1 | |
| 006 | -078-02 | 13.3 | 第二次按壓才反映調整 | P1 | |
| 007 | -079-01 | 13.3.1 | keycycle 後選項仍 latching | P1 | |
| 008 | -079-02 | 13.3.1 | 收合後 Back Bolster 仍為選定項 | P2 | |
| 009 | -080-01 | 13.4 | 長按門板硬鍵 → 快速增減 | P1 | |
| 010 | -080-02 | 13.4 | 長按觸控螢幕 → 快速增減 | P2 | **-080-01** |
| 011 | -081-01 | 13.5 | 短按 → level 移動一個 step | P1 | |
| 012 | -081-02 | 13.5 | 觸控短按 → level 移動一個 step | P2 | **-081-01** |
| 013 | -082-01 | 13.6 | 到達上下限 → 控制 greyed out | P1 | |
| 014 | -082-02 | 13.6 | 上限後再按 → error tone，level 不變 | P2 | |

### 3.1 乙 —— 兩個 `duplicate_of` 之理由

19 §4 把 13.4／13.5 判為 **in scope 但收窄**：

| 節 | 在範圍 | **不在範圍（委派）** |
|---|---|---|
| 13.4 | 長按 → 快速增減之啟動 | 長按門檻、重複速率、加速曲線 → **HMI Core L&F N0** |
| 13.5 | 短按 → 一次級距變化 | 級距量值、與 4-way rocker 之等效性 → **CFTS044** |

037 對兩節各拆兩個 leaf，而**第二個 leaf 之內容恰好就是委派部分**
（`-080-02` = 「logic as per Core N0」；`-081-02` = 「equivalent to previous
4-way rocker」）。扣除委派後，其可觀察行為與第一個 leaf 相同 ——
依 §4.6，`axis="none"` ⇔ `duplicate_of` 有值。

**兩條 TC 仍各自寫出**（操作面不同：門板硬鍵 vs 觸控螢幕），
14 個 leaf 全部有 TC，coverage 分母不變。`reasoning` 逐條明列委派之外部
擁有者（19 §7.5）。

**若分析層認為此判定過寬**（即認為 -02 應有獨立 axis），改動範圍僅為兩份
JSON 之 `distinguishing_axis`，不影響其餘 12 條。

---

### 3.2 逐條內容（JSON ↔ workbook 欄位對照）

### `13.2` — SWE1-HVAC-076 — 3 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS1.) When the (-, +) seat control buttons are pressed from the door control for lumbar & bolster, if the lower screen is not in the stowed position, switch the tab on the lower screen to the Seats tab. If the lower screen is in the stowed position, display the Seat Control Popup on the head unit (popup times out after 5 seconds of not interaction). If the lower screen is in the stowed position, and the user is already in the climate section on the main head unit, switch the user to the Seats tab.

</details>

**reasoning**：驗證目標：13.2（LS1.）以「lower screen 是否處於 stowed 位置」與「使用者是否已在主 HU 之 climate section」兩個條件分出三個分支，三個 037 leaf 恰對應三個分支，故一葉一 TC，切法沿用 037 之分解（§8.2.1）。
配置軸：依 19 §2.1 之第九軸（secondary lower screen 之有無）。其措辭取自 **本節自身**「the lower screen」，**未沿用 6.3 之 non-foldable secondary lower screen**—— 那是另一節的文字（R-C18 同型風險）。故標 spec-derived 而非 spec-verbatim：本節未以一句話宣告該配置，是由分支句推得。
stowed／retracted 之歸屬：依 19 §2.2 之判定測試 —— 三條 TC 之驗證目標**就是**「螢幕處於該狀態時之行為」，故該狀態為 spec 定義之 trigger condition，入 pre_conditions 並標 source class，不下放為 procedure 步驟。
刻意不寫：popup 之視覺樣式、Seats tab 之內容 —— 本節未定義，寫入即造值（§8.4.1）。5 秒 timeout 為條文明載之具體值，照用。

#### NR1L-ComfortHMI-001 — SWE1-HVAC-076-01

| 欄 | 值 |
|---|---|
| tc_title | Seats tab opens on the lower screen when it is not stowed |
| I test_item | When the (-, +) seat control buttons are pressed from the door control for lumbar & bolster, if the lower screen is not in the stowed position, the system shall switch the tab on the lower screen to the Seats tab |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-verbatim] The lower screen is not in the stowed position (13.2)<br>4. [spec-derived] A tab other than the Seats tab is shown on the lower screen (13.2) |
| K input_test_data | NA |
| L test_procedure | 1. Note which tab is currently shown on the lower screen<br>2. Press "-" on the door seat control |
| M expected_result | 1. The tab shown on the lower screen is not the Seats tab<br>2. The lower screen switches to the Seats tab |
| N spec_reference | `…CR24879_(September_25_2023)_13.2` |
| P priority | P1 |
| R design_method | 決策表 (Decision Table Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-002 — SWE1-HVAC-076-02

| 欄 | 值 |
|---|---|
| tc_title | Seat Control Popup appears on the head unit when the lower screen is stowed |
| I test_item | When the (-, +) seat control buttons are pressed from the door control for lumbar & bolster, if the lower screen is in the stowed position, the system shall display the Seat Control Popup on the head unit, and the popup shall time out after 5 seconds of not interaction |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-verbatim] The lower screen is in the stowed position (13.2)<br>4. [spec-derived] The user is not in the climate section on the main head unit (13.2) |
| K input_test_data | NA |
| L test_procedure | 1. Press "-" on the door seat control<br>2. Do not interact with the head unit for 5 seconds |
| M expected_result | 1. The Seat Control Popup is displayed on the head unit<br>2. The Seat Control Popup is no longer displayed |
| N spec_reference | `…CR24879_(September_25_2023)_13.2` |
| P priority | P1 |
| R design_method | 決策表 (Decision Table Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-003 — SWE1-HVAC-076-03

| 欄 | 值 |
|---|---|
| tc_title | Seats tab is opened when the user is already in the climate section |
| I test_item | When the (-, +) seat control buttons are pressed from the door control for lumbar & bolster, if the lower screen is in the stowed position and the user is already in the climate section on the main head unit, the system shall switch the user to the Seats tab |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-verbatim] The lower screen is in the stowed position (13.2)<br>4. [spec-verbatim] The user is already in the climate section on the main head unit (13.2) |
| K input_test_data | NA |
| L test_procedure | 1. Note which tab is currently shown in the climate section on the head unit<br>2. Press "-" on the door seat control |
| M expected_result | 1. The tab shown in the climate section is not the Seats tab<br>2. The head unit switches to the Seats tab |
| N spec_reference | `…CR24879_(September_25_2023)_13.2` |
| P priority | P1 |
| R design_method | 決策表 (Decision Table Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.2.1` — SWE1-HVAC-077 — 1 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS1.1) The 4 types of adjustments the user will be able to alter for lumbar/bolster will be: Lumbar In/Out, Lumbar Up/Down, Back Bolster, Thigh Bolster.

</details>

**reasoning**：驗證目標：13.2.1（LS1.1）列舉腰靠／側靠可調之四種類型。037 對本節只產出一個 leaf（parent 形態即需求，R-C3 之 34 列之一），故一條 TC 覆蓋四項列舉，不再細分 —— 細分為四條會使 Test Set 欄淪為 TC ID 之副本，且條文本身即以一句列舉四者（§8.2.1）。
四個名稱逐字照錄條文（Lumbar In/Out、Lumbar Up/Down、Back Bolster、Thigh Bolster），不改寫、不補充順序以外之語意。
刻意不寫：各類型之調整範圍與級距 —— 本節未定義（級距屬 13.5，且其量值由 CFTS044 擁有，見 19 §4.2）。

#### NR1L-ComfortHMI-004 — SWE1-HVAC-077

| 欄 | 值 |
|---|---|
| tc_title | Four lumbar and bolster adjustment types are available |
| I test_item | The 4 types of adjustments the user will be able to alter for lumbar/bolster will be: Lumbar In/Out, Lumbar Up/Down, Back Bolster, Thigh Bolster |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [test-setup] The Seats tab is open and its lumbar and bolster controls are reachable |
| K input_test_data | NA |
| L test_procedure | 1. Read the list of lumbar and bolster adjustment types offered on the Seats tab |
| M expected_result | 1. The offered adjustment types are "Lumbar In/Out", "Lumbar Up/Down", "Back Bolster" and "Thigh Bolster" |
| N spec_reference | `…CR24879_(September_25_2023)_13.2.1` |
| P priority | P1 |
| R design_method | 功能測試 (Functional based ; no specific technique) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.3` — SWE1-HVAC-078 — 2 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS2.) When the (-, +) seat control buttons are pressed, it will trigger the popup or tab change within climate, and only on the second press will be reflected.

</details>

**reasoning**：驗證目標：13.3（LS2.）規定第一次按壓只觸發 popup 或 tab 切換，調整要到第二次按壓才反映。兩個 037 leaf 對應兩個階段，故以按壓序數為 distinguishing axis 分兩條（§4.6）。
「反映」之可觀察量取條文自身之 level（13.6 命名「the minimum or maximum level」，037 之 -080-01 亦用同詞）—— 依 **R-C22**，不補任何級距量值。
刻意不寫：popup 與 tab 切換何者發生 —— 條文以 or 並列且由 13.2 之分支決定，本節不再重複驗證該分支（§8.2.1 不擴張至 sibling）。

#### NR1L-ComfortHMI-005 — SWE1-HVAC-078-01

| 欄 | 值 |
|---|---|
| tc_title | First press triggers the popup or tab change only |
| I test_item | When the (-, +) seat control buttons are pressed, the system shall trigger the popup or tab change within climate, and only on the second press will the adjustment be reflected |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is not currently shown, and the lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Press "+" once on the door seat control |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The popup or the tab change is shown, and the lumbar/bolster level is unchanged |
| N spec_reference | `…CR24879_(September_25_2023)_13.3` |
| P priority | P1 |
| R design_method | 狀態轉換 (State Transition Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-006 — SWE1-HVAC-078-02

| 欄 | 值 |
|---|---|
| tc_title | Second press applies the lumbar adjustment |
| I test_item | When the (-, +) seat control buttons are pressed, only on the second press will the adjustment be reflected |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The first press has already triggered the popup or the tab change (13.3)<br>4. [test-setup] The lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Press "+" a second time on the door seat control |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The lumbar/bolster level moves one step towards its maximum |
| N spec_reference | `…CR24879_(September_25_2023)_13.3` |
| P priority | P1 |
| R design_method | 狀態轉換 (State Transition Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.3.1` — SWE1-HVAC-079 — 2 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS2.1) The user last selected lumbar/bolster selection will be latching during a keycycle, after a keycycle, and after the lower screen has been stowed/retracted. If the lower screen displayed the last selected option as Back Bolster , then the user retracts the lower screen, the next time they press the door (-, +) buttons or enter the seat tab on the HU, Back Bolster will still be the selected option.

</details>

**reasoning**：驗證目標：13.3.1（LS2.1）之 latching。條文先給通則（during a keycycle、after a keycycle、after the lower screen has been stowed/retracted），再給一個具名例子（Back Bolster + 收合 + door 按鍵或 HU seat tab）。兩個 037 leaf 恰對應通則與例子。
distinguishing axis = **lifecycle event**：-01 驗 keycycle 邊界，-02 驗螢幕收合後之重入路徑。兩者不是 duplicate —— 觸發事件不同，且 -02 另含「door 按鍵或 HU seat tab 兩條重入路徑」之具名內容。
例子中之 Back Bolster 為條文具名，照錄；不替換為其他類型。

#### NR1L-ComfortHMI-007 — SWE1-HVAC-079-01

| 欄 | 值 |
|---|---|
| tc_title | Last selected adjustment latches across a keycycle |
| I test_item | The user last selected lumbar/bolster selection will be latching during a keycycle, after a keycycle, and after the lower screen has been stowed/retracted |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] A lumbar/bolster adjustment type is currently the selected option (13.3.1) |
| K input_test_data | NA |
| L test_procedure | 1. Note which lumbar/bolster adjustment type is the selected option<br>2. Run a keycycle<br>3. Open the Seats tab and read the selected option |
| M expected_result | 1. The selected option is readable<br>2. The head unit completes the keycycle<br>3. The selected option is the same one noted in step 1 |
| N spec_reference | `…CR24879_(September_25_2023)_13.3.1` |
| P priority | P1 |
| R design_method | 狀態轉換 (State Transition Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-008 — SWE1-HVAC-079-02

| 欄 | 值 |
|---|---|
| tc_title | Back Bolster stays selected after the lower screen is retracted |
| I test_item | If the lower screen displayed the last selected option as Back Bolster , then the user retracts the lower screen, the next time they press the door (-, +) buttons or enter the seat tab on the HU, Back Bolster will still be the selected option |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-verbatim] The lower screen displayed the last selected option as Back Bolster (13.3.1) |
| K input_test_data | NA |
| L test_procedure | 1. Retract the lower screen<br>2. Press "+" on the door seat control<br>3. Read the selected option |
| M expected_result | 1. The lower screen is retracted<br>2. The Seat Control Popup or the Seats tab is shown<br>3. The selected option is "Back Bolster" |
| N spec_reference | `…CR24879_(September_25_2023)_13.3.1` |
| P priority | P2 |
| R design_method | 狀態轉換 (State Transition Testing) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.4` — SWE1-HVAC-080 — 2 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS3.) The user will be able to long press on the hard button (-, +) or on the touch screen itself to initiate fast increases/decreases. (See HMI Core Logic and Flow, requirement N0.)

</details>

**reasoning**：驗證目標：13.4（LS3.）長按 (-, +) 或觸控螢幕 → 啟動快速增減。
**範圍收窄（19 §4.1）**：本節自身定義之行為為「長按啟動快速增減」，**在範圍**；`(See HMI Core Logic and Flow, requirement N0)` 係交叉參照其通用長按機制 —— **長按之判定門檻、重複速率、加速曲線由 HMI Core Logic and Flow requirement N0 擁有，不在本 feature 範圍，不測、不補值**（§8.2.1 委派）。故 procedure 不指定按壓時長，ER 不述速率。
-01 與 -02 之關係：037 將本節拆為「快速增減被啟動」與「邏輯依 Core N0」。後者之全部內容即上述委派部分，於本 feature 範圍內**不具獨立之可觀察差異**，故依 §4.6 標 axis=none 並填 `duplicate_of`。此為忠實反映委派，非省略 leaf。
可觀察量取條文自身之 level（R-C22），不補級距量值。

**sibling**：`duplicate_of` = `SWE1-HVAC-080-01`，axis = `none`

> delta：本 leaf 之唯一區別內容為 long-press 邏輯依 HMI Core Logic and Flow requirement N0，而該邏輯已判由 Core 擁有、不在本 feature 範圍（19 §4.1）。扣除委派部分後，其可觀察行為與 -01 相同，僅操作面（觸控螢幕 vs 門板硬鍵）不同

#### NR1L-ComfortHMI-009 — SWE1-HVAC-080-01

| 欄 | 值 |
|---|---|
| tc_title | Long press initiates fast lumbar level change |
| I test_item | The user will be able to long press on the hard button (-, +) or on the touch screen itself to initiate fast increases/decreases |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Long press "+" on the door seat control until the level has moved several steps<br>3. Release "+" |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The lumbar/bolster level moves towards its maximum faster than one step per press<br>3. The lumbar/bolster level stops changing |
| N spec_reference | `…CR24879_(September_25_2023)_13.4` |
| P priority | P1 |
| R design_method | 功能測試 (Functional based ; no specific technique) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-010 — SWE1-HVAC-080-02

| 欄 | 值 |
|---|---|
| tc_title | Long press on the touch screen initiates the same fast change |
| I test_item | The user will be able to long press on the touch screen itself to initiate fast increases/decreases, with the long-press logic as per HMI Core Logic and Flow (requirement N0) |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Long press the on-screen "+" control until the level has moved several steps<br>3. Release the on-screen "+" control |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The lumbar/bolster level moves towards its maximum faster than one step per press<br>3. The lumbar/bolster level stops changing |
| N spec_reference | `…CR24879_(September_25_2023)_13.4` |
| P priority | P2 |
| R design_method | 功能測試 (Functional based ; no specific technique) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.5` — SWE1-HVAC-081 — 2 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS4.) A short press of the (-, +) button will increase the lumbar/bolster by a small set amount, that would be equivalent to a short press of the previous 4-way rocker hard control (See CFTS044).

</details>

**reasoning**：驗證目標：13.5（LS4.）短按 (-, +) → 腰靠／側靠增加一個級距。
**範圍收窄（19 §4.2）**：本節自身定義之行為為「短按產生一次級距變化」，**在範圍**；`(See CFTS044)` 所定者為該級距之**量值**及其與舊款 4-way rocker 之等效性 —— **由 CFTS044 擁有，不在本 feature 範圍，不測、不補值**（§8.2.1 委派）。
**R-C22 之落實**：條文之 a small set amount 無數值，ER **不補任何量值**，改以條文自身命名之可觀察量 **level** 表述（13.6 之 the minimum or maximum level；037 之 -080-01 亦用同詞）。「移動一個 step」為可觀察、可判定，合於 §6，故**不標 BLOCKED**。
-01 與 -02 之關係：-02 之全部內容（與 rocker 之等效性）即上述委派部分，扣除後無獨立可觀察差異，依 §4.6 標 axis=none 並填 `duplicate_of`。

**sibling**：`duplicate_of` = `SWE1-HVAC-081-01`，axis = `none`

> delta：本 leaf 之唯一區別內容為「與舊款 4-way rocker 之等效性」，而該等效性之基準由 CFTS044 擁有、不在本 feature 範圍（19 §4.2）。扣除委派部分後，其可觀察行為與 -01 相同，僅操作面（觸控螢幕 vs 門板硬鍵）不同

#### NR1L-ComfortHMI-011 — SWE1-HVAC-081-01

| 欄 | 值 |
|---|---|
| tc_title | Short press moves the lumbar level by one step |
| I test_item | A short press of the (-, +) button will increase the lumbar/bolster by a small set amount |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The popup or tab change has already been triggered, so the next press is applied (13.3)<br>4. [test-setup] The lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Short press "+" on the door seat control<br>3. Short press "-" on the door seat control |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The lumbar/bolster level moves one step towards its maximum<br>3. The lumbar/bolster level returns to the level noted in step 1 |
| N spec_reference | `…CR24879_(September_25_2023)_13.5` |
| P priority | P1 |
| R design_method | 功能測試 (Functional based ; no specific technique) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-012 — SWE1-HVAC-081-02

| 欄 | 值 |
|---|---|
| tc_title | Short press on the touch screen moves the level by one step |
| I test_item | A short press will increase the lumbar/bolster by a small set amount, that would be equivalent to a short press of the previous 4-way rocker hard control |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Short press the on-screen "+" control<br>3. Short press the on-screen "-" control |
| M expected_result | 1. The lumbar/bolster level is readable<br>2. The lumbar/bolster level moves one step towards its maximum<br>3. The lumbar/bolster level returns to the level noted in step 1 |
| N spec_reference | `…CR24879_(September_25_2023)_13.5` |
| P priority | P2 |
| R design_method | 功能測試 (Functional based ; no specific technique) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


### `13.6` — SWE1-HVAC-082 — 2 TC

<details><summary>條文全文（來源：section_fulltext.tsv）</summary>

> LS5.) Once the minimum or maximum level has been reach, the system will grey out the (-, +) control. So if the user is increasing their lumbar, once the maximum has been reached, pressing the (+) button again will result in error tone being triggered.

</details>

**reasoning**：驗證目標：13.6（LS5.）到達上下限後之兩個行為 —— 控制被 grey out，以及再按會觸發 error tone。兩個 037 leaf 對應兩者。
distinguishing axis = **observable channel**：-01 驗視覺（控制呈現 greyed out），-02 驗聽覺（error tone）加上級距不再變化。兩者 tc_title 不得讀來相同（§4.3 sibling-distinction），已分開措辭。
**R-C22 之落實**：error tone **照錄**條文措辭，ER 寫「an error tone is played」—— 有無可判定，合於 §6；其頻率、時長、視覺回饋一律不寫（條文未給）。**不標 BLOCKED** —— 值不知道但事件看得見。
另併列可觀察之 UI 事實：達上限後級距不再變化。
設計方法取 BVA：兩條皆為上下限邊界行為。**未取負向測試** —— 於上限再按 (+) 是合法輸入落在邊界，非注入非法值。

#### NR1L-ComfortHMI-013 — SWE1-HVAC-082-01

| 欄 | 值 |
|---|---|
| tc_title | Control is greyed out at the minimum and maximum level |
| I test_item | Once the minimum or maximum level has been reach, the system shall grey out the (-, +) control |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [test-setup] The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum |
| K input_test_data | NA |
| L test_procedure | 1. Press "+" repeatedly until the lumbar/bolster level stops increasing<br>2. Read how the "+" control is presented<br>3. Press "-" repeatedly until the lumbar/bolster level stops decreasing<br>4. Read how the "-" control is presented |
| M expected_result | 1. The lumbar/bolster level reaches its maximum and stops changing<br>2. The "+" control is greyed out<br>3. The lumbar/bolster level reaches its minimum and stops changing<br>4. The "-" control is greyed out |
| N spec_reference | `…CR24879_(September_25_2023)_13.6` |
| P priority | P1 |
| R design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |

#### NR1L-ComfortHMI-014 — SWE1-HVAC-082-02

| 欄 | 值 |
|---|---|
| tc_title | Error tone is played when pressing beyond the maximum level |
| I test_item | So if the user is increasing their lumbar, once the maximum has been reached, pressing the (+) button again will result in error tone being triggered |
| J pre_conditions | 1. [spec-derived] The vehicle is equipped with a lower screen that provides seat controls (13.2)<br>2. [spec-derived] The door control carries the seat control (-, +) buttons for lumbar and bolster (13.2)<br>3. [spec-derived] The lumbar/bolster level is already at its maximum (13.6)<br>4. [test-setup] The cabin is quiet enough for a tone to be heard |
| K input_test_data | NA |
| L test_procedure | 1. Note the current lumbar/bolster level<br>2. Press "+" on the door seat control |
| M expected_result | 1. The lumbar/bolster level is at its maximum<br>2. An error tone is played and the lumbar/bolster level stays at its maximum |
| N spec_reference | `…CR24879_(September_25_2023)_13.6` |
| P priority | P2 |
| R design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| G / H | `Comfort` / `Seat Control Tab` |
| Q / S / T–Z / AH | 留白 / `NA` / 留白 / 空字串 |


---

## 4. lint ＋ §9 self-check

### 4.1 lint —— `scripts/lint_tcs.py`，**25 gate 全 PASS**

為 Comfort 新寫，未沿用 Privacy 之 gate（其 `spec-reference` 綁 CFTS022
artifact id，Comfort 無此物）。權威一律**讀取**不硬編：design method 讀
workbook 之 `下拉選單`（9 字串）、Test Group 與 tc_id 格式讀 `feature.yaml`、
有效 outline 讀 `layer3_map.tsv`（129）、條文讀 `section_fulltext.tsv`。

```
files: 7   TCs: 14   vocabulary: 9 strings   valid outlines: 129

PASS — tc-id-format / tc-id-unique / tc-id-sequence / req-id-unique
PASS — spec-ref-stem / spec-ref-outline / spec-ref-sr25
PASS — test-group / design-method / priority / functional-safety
PASS — estimated-time / remarks
PASS — trailing-period / ui-bracket
PASS — title-length / title-modal / item-modal / er-modal
PASS — source-class / proc-er-1to1
PASS — token-placement / token-source
PASS — fabricated-qty / sibling-axis

25 / 25 gates PASS; 0 finding(s) across 14 TCs
```

**反向驗證（§5a：檢查項須確認其在該階段確實可能失敗）**：於一份 JSON 注入
五種缺陷後重跑，**六個 gate 轉 FAIL**（`spec-ref-stem`、`spec-ref-sr25`、
`priority`、`trailing-period`、`source-class`、`token-placement`），
還原後回到 25/25。gate 是真閘，非裝飾。

### 4.2 §9 self-check —— 17 項逐條自評

| # | §9 項目 | 自評 | 依據 |
|---|---|---|---|
| 1 | Test Set 合 framework、無 Test Group 前綴、無 Misc | **PASS** | 全 14 條 `Seat Control Tab`，為 Part N #9；lint `test-group` gate |
| 2 | tc_title 3 種形態之一、2–14 words、sibling token 可見、無 modal | **PASS** | lint `title-length`／`title-modal`；實測 7–11 words。sibling token：001/002/003 以 `not stowed`／`stowed`／`already in the climate section` 區隔；013/014 以 `greyed out`／`error tone` 區隔 |
| 3 | Pre-Condition 為 state/env、為 spec trigger 非隱含環境前提 | **PASS** | 每行標 source class（lint `source-class`）。stowed／retracted 依 19 §2.2 判定測試入 PC —— 三條 TC 之驗證目標即該狀態下之行為。**未寫** `HU is powered on`／`Climate is available`（profile §3.2 禁用） |
| 4 | Input Test Data 歸屬正確、重複資料移走或 `NA` | **PASS** | 14 條皆 `NA` —— 本批無需注入之資料，按壓動作屬 procedure |
| 5 | 步驟可執行、無禁用動詞、Final Step 擁有驗證 | **PASS** | 每條末步為可觀察之讀取或按壓，其 ER 為判定點 |
| 6 | 步驟長度與意圖層級 | **PASS** | 2–4 步；無「執行完整情境」型巨步 |
| 7 | 標準 setup 片段逐字重用 | **PASS** | `PC_SCREEN`／`PC_DOOR` 兩片段於各條逐字重用（生成器常數，非逐條改寫） |
| 8 | CLI 步驟用 description + `$` 格式 | **N/A** | 本批無 CLI 步驟 |
| 9 | 需要 before/after 時給 baseline | **PASS** | 005/006/011/012/014 皆以第 1 步 `Note the current lumbar/bolster level` 建立 baseline |
| 10 | Procedure ↔ ER 1:1、ER 可觀察、無 modal、結果完整 | **PASS** | lint `proc-er-1to1`／`er-modal`。ER 之可觀察量取條文自身命名者（`level`／`greyed out`／`error tone`／`selected option`） |
| 11 | 無 FP／FF；supported 配 negative | **PASS** | 014 為上限後之負向行為，與 011/013 配對；**未用「負向測試」設計方法** —— 於上限再按 `"+"` 是合法輸入落在邊界，非注入非法值（避開 Privacy R33-1(d) 之陷阱） |
| 12 | 追溯 Req/SWRA、尊重 RD 分解不擴張、無造值、無造範圍 | **PASS** | 14 leaf ↔ 14 TC，切法沿用 037（§8.2.1）。委派部分明列於 `reasoning` 且**不測**（§8.4.2）。lint `fabricated-qty` |
| 13 | Design Method 於 procedure 定案後指派 | **PASS** | 決策表用於 13.2 之三分支；狀態轉換用於 13.3／13.3.1 之序列與 latching；BVA 用於 13.6 之上下限；其餘功能測試 |
| 14 | 四欄無行尾句點 | **PASS** | lint `trailing-period` |
| 15 | UI label 用 `"..."` 不用 `[...]` | **PASS** | lint `ui-bracket`；`(-, +)` 依 19 §3 分割（lint `token-placement`／`token-source`） |
| 16 | `specification_reference` 列全每個直接驗證之節 | **PASS** | 每條一節，與其 leaf 之 outline 一致；lint `spec-ref-outline` |
| 17 | 原始 spec 勝過 index export；閾值為 spec 來源之具體值 | **PASS** | 條文一律讀 `section_fulltext.tsv`（R-C18）。唯一寫入之具體值為 13.2 之 **5 秒**（條文明載）；13.5 之級距**不寫**（CFTS044 擁有） |

**17 項中 16 項 PASS、1 項 N/A（第 8）、0 項 FAIL。**

---

## 5. 丙 —— 九軸機械複掃（19 §6）

判準改為**九軸之字面表述**，而非 17 §3.2 之泛用條件句式 ——
後者實測會漏掉 profile 自己已列的軸（Standard 座椅、MTC、單區），
上繳 10 §3.4 已記。**兩表並用**，皆保留於腳本。

| 軸 | 命中節數 | 節次 |
|---|---|---|
| 軸1 ATC/MTC | 9 | 2.2, 2.3, 2.6, 2.14, 7.4, 16.2, 16.3, 16.6, 16.14 |
| 軸2 zone | 6 | 2.3.1, 2.11, 7.10, 14.14, 16.11, 17.5 |
| 軸3 tri-mode | 2 | 2.12.1, 3.1 |
| 軸4 MAX A/C | 7 | 2.13, 3.2, 16.3, 16.4, 16.8, 16.13, 17.2 |
| 軸5 MAX DEF | 9 | 2.10, 3.2, 3.3, 15.1, 16.3, 16.4, 16.8, 16.10, 16.13 |
| 軸6 獨立座椅分區 | 5 | 11.6, 11.6.1, 11.7, 11.10, 14.16.1 |
| 軸7 加熱方向盤等級 | 2 | 11.8, 11.9 |
| 軸8 座椅等級 | 6 | 11.1, 11.2, 12.1, 12.2, 12.8, 12.9 |
| **軸9 lower screen** | **4** | **6.3, 13.2, 13.3.1, 14.13** |

**命中至少一軸：44 / 129 節。**

### 5.1 含條件句式但九軸皆未命中者 —— 9 節，供第二輪裁

`2.1`、`2.5`、`2.5.1`、`2.7.1`、`2.9`、`7.6`、`9.1`、`11.11`、`14.19`

其條件句式已列於 `data/config_axis_candidates.tsv`。抽樣過目時已見其中數例
（如 `2.5` 之 `RECIRC is not available in certain modes`、`9.1` 之
`On some vehicles (See CFTS043 for details)`）。

**R-C13 重申**：本複掃之「其餘 85 節未命中」**不得作為「無其他軸」之結論**，
只得作為「已盡機械之力」之記錄。上繳 10 §3.3 之抽樣即在 15 節中找到三個
未列軸，其中之一（lower screen）已成為第九軸。

---

## 6. 未做者

- **未寫回 workbook**（18 §3.4 / 19 §7.8）—— `output/` 未動，
  `DELIVERY.sha256` 仍 2 筆 OK，無 ENTRY 002。
- 未指派 pilot 以外之任何 tc_id（`-015` 起未使用）。
- 未動 `framework.md`、`RULINGS.md` 之既有條文（R-C21／R-C22 為新增，
  profile 兩處為 19 §7.2 指定之增補）。
- **未動 home 之任何檔案**（R-C21；實測 `git status -- features/home` 為 0）。
- 未補入 HMI Core L&F 或 CFTS044（19 §4.3：取得反而誘使越界）。
- 未重跑任何既有 feature 之 recon（R-C8）。
- 未執行 git。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 13.5 可觀察量之取得（通讀五節，逐節列出條文自身命名者）。
2. lint 25 gate 全 PASS，**且以注入缺陷確認六個 gate 會失敗**。
3. 九軸複掃全 129 節；含條件句式而未命中者 9 節已列。
4. §9 17 項逐條自評，每項具名其依據（lint gate 或條文位置）。
5. `home` 檔案零變更；`DELIVERY.sha256` 未新增 ENTRY。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **`Seat Control Popup` 之內容與外觀** | 13.x 未定義 | 低 —— ER 只驗其「顯示／不再顯示」，未述樣式 |
| 2 | **`level` 之呈現位置** | 條文命名了量但未說在哪裡讀 | **中** —— ER 寫「The lumbar/bolster level is readable」，實測時需先確認可讀之處。若實機無任何 level 指示，該量即不可觀察，屆時才是 BLOCKED 之候選（R-C22 之界線） |
| 3 | **其餘 9 節之候選軸** | 屬分析層判定（17 §3.2） | 中 —— 已列於 §5.1 |
| 4 | **`(-, +)` 於其餘 5 節之處理** | 本批只用到 13.2~13.6 | 低 —— §3.4 第五列已通則化 |
| 5 | **pilot 之 workbook 呈現** | 未寫回（本包禁止） | 低 —— 寫回於 pilot review 通過後另行下放 |

**第 2 項是本批最實質的未驗項**：R-C22 說「值不知道但變化看得見」不算
BLOCKED —— 前提是**變化確實看得見**。條文命名了 `level`，但未指明其 UI
呈現。若 pilot review 或實機驗證顯示無任何 level 指示可讀，011／012／013／
014 四條之 ER 需重寫，且 13.5 會回到 BLOCKED 之候選。
**我未假定任何 UI 元件存在**（19 §5 明禁），ER 措辭停在「readable」而不指
其位置，正是為此。

### 7.3 執行層對「本包可否結案」之判斷

**可結案，送 pilot review。** 14 條齊備、lint 全綠且經反向驗證、
§9 逐條自評有據、九軸複掃已盡機械之力。

**review 時建議優先看三處**：
1. §3.1 之兩個 `duplicate_of` 判定是否過寬（改動範圍小，僅兩份 JSON）
2. §7.2 第 2 項之 `level` 可讀性（牽動四條 TC 之 ER）
3. 001/002/003 之 stowed 狀態入 `pre_conditions` 是否合 19 §2.2 之判定測試
   —— 我判「三條之驗證目標即該狀態下之行為」，故入 PC 而非 procedure
