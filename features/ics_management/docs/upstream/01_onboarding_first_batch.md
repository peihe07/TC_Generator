# 上繳包 01 — ICS Management 建檔與首批 TC（2026-08-29）

對應下放包：`features/ics_management/docs/handoff/01_onboarding_first_batch.md`
（sha256 `ba686c3546e4a451050a4c77ac10b29811b8aa6f2aecd26cccd482c8039d9268`）

執行層：Claude Code session。**本包未執行任何 git 操作**（FO §8.8：git 一律不在
執行層）。`git add` / `commit` / `push` 皆未跑；工作區狀態留給 Pei 處置。

---

## §0 本包之量測基礎（先揭露，後陳述）

| 項 | 條件 |
|---|---|
| repo 狀態 | 本包開工時 HEAD = `b4e8485`；工作區另有 `docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md` 之未提交修改（非本包所寫） |
| 素材讀法 | docx 一律自原檔 `word/document.xml` 抽取（`</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape`）；xlsx 一律 `openpyxl` `data_only=True` |
| 逐字比對正規化 | 彎引號→直引號、NBSP→空格、連續空白摺一、去頭尾空白、去句末單一句號。**除此四項外一字不動** |
| 字數計算 | `str.split()` 之 token 數（空白切分） |
| 掃描範圍 | TC 欄位掃描限 `pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`／`test_item`／`specification_reference` 六欄；禁詞掃描不分大小寫、帶詞界 |
| 工作簿掃描 | `Test Case Specification 測試用例規範` 分頁第 10–1411 列（1402 列），I 欄（Test Item）與 F 欄（Test Case ID）判 filled，AA 欄（Author）判 done |

---

## §1 讀取之裁決與其指紋（R-G13）

下放包 01 **未附 `R-XX@<sha8>` 形式之引用**（見 §六-4）。本包自 repo 讀原文，
並以 `scripts/rulings_hash.py --target features/ics_management/RULINGS.md` 回報所讀 sha8：

| 裁決 | sha8 | 本包用於 |
|---|---|---|
| R-ICS1 | `3e48552b` | slug／Test Group = `ICS` |
| R-ICS2 | `ad557b5d` | 適用域（暫定 {ICS, LTM}），V 組之採認 |
| R-ICS3 | `b10318e0` | `<Tstuck_button>` 首波取 120 s |
| R-ICS4 | `85de9871` | verbatim 來源分流：S 組取 CFTS022，V3 取 SWRA（002 未受位移）|

canon 之引用：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
（sha256 `0b0cea00…8e`）與其串接本 `docs/runtime/PROJECT_INSTRUCTION.md`
（sha256 `68b2c446…34`）。**本包實測二者於所引之 §8.4.3、§8.7.5 皆同步**
（各 1 處／2 處命中），故 §-節號之引用無歧義。

---

## §2 骨架補齊（下放包 §一-1）

| 項 | 實況 | 依據／量測 |
|---|---|---|
| `feature.yaml` | 已落 | 每一數值皆自實體檔實測，未實測者留 `null`／空 map |
| `.gitignore` | 已落 | `inputs/`、`sandbox/`、`data/recon.json`、`lint_report.json`、`output/` |
| `data/`、`output/`、`scripts/`、`docs/upstream/`、`generated/`、`sandbox/` | 已建 | — |
| 036 表單工作副本 | `sandbox/ics_management_00.xlsx` | 自 `forms/` 母本複製，`cmp` 全等，sha256 `6372fb6b…825b2` 與母本相同 |
| `inputs/` 三份來源 | **實際為四份，且非下放包所述之三份** | 見 §三-1 |

**兩處落點與下放包所令不同，理由為 R-G25，非自裁**：

1. 下放包令 `workbook/`，實落 `sandbox/`。R-G25 之落點政策令 `.xlsx` 之合法落點
   為 `delivered`／`inputs`／`sandbox`，`workbook/` 不在其列。
2. 下放包令 `batches/b01/`，實落 `generated/b01/`。同政策令 `.json` 之合法落點
   為 `data`／`generated`／`inputs`／`sandbox`。

**證據（實跑，非推論）**：先依下放包字面落於 `workbook/`＋`batches/b01/` 時，
`python3 scripts/lint_paths.py` 報「基線外 **4**」，四筆全為本 feature 之新件；
搬至 `sandbox/`＋`generated/` 後回到「基線外 **1**」，該 1 筆為
`features/driver_distraction/workbook/driver_distraction_00.xlsx`，**本包開工前即紅**。
`bed_lowering` 之 `workbook/`／`batches/` 之所以不紅，是因其列於
`docs/fw036/PATH_POLICY_BASELINE.tsv`（58 列）——
**基線是既存違規之凍結，不是新件之許可**。

若分析層認為應照下放包字面落點，請以裁決指示，並同時裁定基線是否加列
（改基線以消紅屬版控政策，Tier 3，本包不動）。

---

## §3 首批 6 條 TC（下放包 §二）

落點：`features/ics_management/generated/b01/b01_tcs.json`
（sha256 `fb60e728cad657cf5d03c32f4abd8f04ff55808a0ca9013235bb1b5a3cba9fe2`）
manifest：`features/ics_management/generated/b01/manifest.json`

| # | tc_title | req_id | Test Set | 錨 | design_method | priority |
|---|---|---|---|---|---|---|
| S1 | Stuck button held over 120 s | SWE-ICS-010 | Stuck Button | CFTS022-4914956 | Fault Injection | **P0**（下放包範式為 P1，見 §四-4）|
| S2 | Stuck fault held until de-bounced not-pressed | SWE-ICS-010 | Stuck Button | CFTS022-4914957 / -4914958 | Fault Injection | P1 |
| S3 | Button held exactly 120 s | SWE-ICS-010 | Stuck Button | CFTS022-4914956 | Boundary Value Analysis | P1 |
| V1 | VOLUME knob rotated clock-wise | SWE-ICS-001 | Volume Control | CFTS022-4914974 / -4914975 | Functional Based | P0 |
| V2 | VOLUME knob rotated counter clock-wise | SWE-ICS-001 | Volume Control | CFTS022-4914974 / -4914976 | Functional Based | P0 |
| V3 | Three detents rotated clock-wise | SWE-ICS-002 | Volume Control | CFTS022-4914975 | Functional Based | P1 |

### PENDING 佔位清單（IN §8.4.3；實跑輸出，非人工列舉）

| TC | 欄位 | DR | 缺件 |
|---|---|---|---|
| S1 | test_procedure | DR-ICS8 | `ICSMuteButton CAN signal` |
| S2 | test_procedure | DR-ICS8 | `ICSMuteButton CAN signal` |
| S3 | test_procedure | DR-ICS8 | `ICSMuteButton CAN signal` |
| V3 | pre_conditions | DR-ICS4 | `CFTS019 volume level range` |

共 4 處、涉 4 條。**無留空、無以 NA 代替缺件**。

### 逐條之來源逐字比對（`scripts/verify_verbatim_b01.py`，實跑）

```
Stuck button held over 120 s                   SWE-ICS-010   CFTS022  CFTS022-4914956
Stuck fault held until de-bounced not-pressed  SWE-ICS-010   CFTS022  CFTS022-4914957
Button held exactly 120 s                      SWE-ICS-010   CFTS022  CFTS022-4914956
VOLUME knob rotated clock-wise                 SWE-ICS-001   CFTS022  CFTS022-4914974
VOLUME knob rotated counter clock-wise         SWE-ICS-001   CFTS022  CFTS022-4914974
Three detents rotated clock-wise               SWE-ICS-002   SWRA     CFTS022-4914975

總判：PASS —— 6 條，逐字命中 6，未命中 0
```

5 條之上半逐字命中 CFTS022 原文，V3 之上半逐字命中 SWRA `SWE1 Requirements`
第 8 列 Requirement Description ——
**與 R-ICS4 之分流一致**（002 未受 A-ICS1 之 +1 位移）。

---

## §4 預期數字對照（FO §8.2，相符者亦列）

下放包未設「預期數字」節（§六-4），故下列預期取自下放包 §二 之文字承諾。

| 項 | 預期（下放包） | 實測 | 判 |
|---|---|---|---|
| 1 | TC 條數 6 | 6 | 相符 |
| 2 | Stuck Button 3 條 | 3 | 相符 |
| 3 | Volume Control 3 條 | 3 | 相符 |
| 4 | S1/S2 皆 trace SWE-ICS-010 | S1/S2/S3 皆 SWE-ICS-010 | 相符 |
| 5 | V1/V2 trace SWE-ICS-001、V3 trace SWE-ICS-002 | 同 | 相符 |
| 6 | 十鍵齊備 | 6/6 齊備 | 相符 |
| 7 | English only（不援引雙語例外）| 括號下半 6/6 無中文 | 相符 |
| 8 | Test Group = `ICS` | 6/6 = `ICS` | 相符 |
| 9 | TC ID `NR1L-ICS-{NNN}` | `feature.yaml` 落 `NR1L-ICS-{n:03d}`；**b01 之 JSON 不含 `tc_id`** | 相符（IN §10.3：生成器指派，LLM 不出 `tc_id`）|
| 10 | 訊號欄無 DBC → PENDING | 3 處 DR-ICS8 佔位 | 相符 |
| 11 | CFTS019 細節 → PENDING: DR-ICS4 | 1 處 | 相符 |

**不符 1 項，不自行調和，逐項如下：**

4. **S1 之 priority**：下放包 §三 之範式寫 `P1`；本包落 **`P0`**。
   理由：下放包 §二「通用格式規制」明令「Priority 依 `TEST_CASE_PRIORITY.md`
   自判 P0–P3」（A-ICS6），而該檔之「CAN 測試案例分級 P0」清單第 5 項為
   「系統異常時是否能正確回報錯誤碼（DTC）給診斷工具」—— S1 即該項。
   **兩條指示互斥**（範式之字面 vs 自判之指令），本包取後者並在此具名回報。
   若分析層裁定以範式為準，改回一字即可（`generated/b01/b01_tcs.json` 之 S1）。
   連帶：V1／V2 依同一 rubric 之「功能核心主流程預設 P0」落 P0，
   S2／S3／V3 為次要邏輯分支與邊界，落 P1。

---

## §5 自檢與閘之實跑輸出

### 5-1 IN §9 自檢（`scripts/selfcheck_b01.py`，實跑）

```
§9-1 Test Set              PASS      相異 Test Set = ['Stuck Button', 'Volume Control']；Test Group 前綴／禁用名 0
§9-2 tc_title              PASS      6 條字數 [6, 6, 5, 4, 5, 4]；違規 0
§4.3.1 test_item 兩段式    PASS      6 條皆有下半、皆英文；違規 0
§10.1 十鍵齊備             PASS      缺鍵 0
§10.2 priority             PASS      分佈 {'P0': 3, 'P1': 3}；越界 0
§10.5 procedure ≥2 步      PASS      步數 [4, 5, 5, 4, 4, 4]；違規 0
§9-10 Procedure↔ER 1:1     PASS      違規 0
§6 ER 無情態動詞           PASS      掃 ['shall','will','should','would']（不分大小寫、帶詞界）；命中 0
§5.1 禁用動詞（主動詞）    PASS      掃 item 首詞，不分大小寫；命中 0
§11 無尾句號               PASS      規制單位 = numbered item；違規 0
§11 無行首行尾空白         PASS      違規 0
§11 無方括號               PASS      違規 0
§11 UI 標籤雙引號          PASS      單引號 token 0
§10.7 spec_reference       PASS      逐行 CFTS{nnn}-{7 位}、升冪、無串接；違規 0
§12 design_method          PASS      用及 ['Boundary Value Analysis','Fault Injection','Functional Based']；越界 0
§8.4.3 PENDING 佔位        PASS      佔位 4 處，涉 4 條
§9-3  Pre-Condition 為狀態/環境   MANUAL
§9-5  Final Step 擁有驗證          MANUAL
§9-11 無 FP/FF                     MANUAL
§9-12 追溯 Req/SWRA                MANUAL
§9-17 來源 spec 勝過索引輸出       MANUAL

總判：PASS —— 機檢 16 項，FAIL 0；人工 5 項
```

**人工 5 項標 MANUAL 而非 PASS**：其判準無可機檢之形式，
標 PASS 等同宣告一個不可能失敗之檢查（charter §工作形態）。

**本 feature 無 `lint_tcs.py`**：其 F／K／T／U 閘之母體（outline map、
綁定 DBC、popup 清單）在本 feature 皆不存在，接一支無母體可查之 lint
即製造一支永遠綠的閘。俟 DR-ICS8 結案並有綁定庫後再議。

### 5-2 四支 gate（`scripts/gate_all.py`，實跑）

**開工前（基線）**與**本包完工後**兩次實跑，逐支列出：

| 閘 | 開工前 | 完工後 | 差 |
|---|---|---|---|
| `lint_docs036` | PASS exit 0 | PASS exit 0 | — |
| `canon_refs` | FAIL：unresolved + ambiguous = **474** | FAIL：**474** | 0 |
| `rulings_hash` | FAIL：`RULINGS.sha.tsv` 與現行條文不符 | FAIL：同 | 同 |
| `gates_tsv` | FAIL：`GATES.tsv` 與現行閘登錄不符 | FAIL：同 | 同 |
| `lint_paths` | FAIL：基線外 **1** | FAIL：基線外 **1** | 0 |

**總判 FAIL，四支未過 —— 四支皆為本包開工前即紅，本包未新增任何一筆。**
依 FO §8.2／26 包 §C 裁定 2 附升級說明：本包不觸及該四支之母體
（未改 canon、未改任何 RULINGS、未動 GATES.tsv、未改落點基線），
其成因與本 feature 無涉，處置屬全域收尾輪。
`lint_paths` 之中間態（基線外 4）與其消解過程已載於 §二。

---

## §6 未預期之發現（下放包未涵蓋，執行時撞到）

### 6-1 【重】CFTS022 不在本 feature 之 `inputs/`

下放包 §一-1 稱「三份來源檔（SWRA xlsx、SYSAD、CFTS022，皆偽 docx／UTF-8 文字）」。
**實測三處不符**：

1. `inputs/` 實有 **四**檔，且**無 CFTS022**：
   `ICS_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`、
   `SYS3_CFTS020_ICS_..._SYSAD_v1.0.docx`、
   `SYS2_CFTS_020_DISP_TCH_ICS_20260616_....xlsx`、
   `R1LR_Atl-H_26PI1.5 ..._CFTS_020 ICS and DCSD _20260310-1533.docx`
2. 四檔皆為**真** Office 檔（`file(1)` 判 `Microsoft Excel 2007+`／`Word 2007+`），
   非「偽 docx／UTF-8 文字」
3. b01 六條之錨所出之 CFTS022 實體位於
   **`features/privacy/inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx`**
   （sha256 `5eb0dd73…78`）。物件 4914953–58、4914970–91 皆在其中，逐一命中。

**處置**：`feature.yaml` 以 `reference.cfts022_fs` **綁 privacy 之原件而不複製**
（同 bed_lowering R-BLM11 綁 vehicle_setting 原件之理由：原件變動才是要偵測的
事件）。**未搬檔、未複製** —— 素材補入超出既定根目錄屬 Pei 裁定（charter §觸點）。

### 6-2 【重】DR-ICS5 之前提與實況不符 —— CFTS020 Functional Specification 就在 `inputs/`

DR-ICS5 記「CFTS020 Functional Specification 未提供（僅收到 SYSAD）」。
**實測**：`inputs/R1LR_Atl-H_26PI1.5 ..._CFTS_020 ICS and DCSD _20260310-1533.docx`
即該文件 —— 首頁題名 `Requirement Specification Report / CFTS_020 ICS and DCSD`，
917k 字元、5,196 非空行、`{7 位 ObjectID}` 相異 **407** 個。

其目次直接涵蓋 framework.md 現標為「不可動工」之面：

| framework 之面 | CFTS020 之對應章節（實測） |
|---|---|
| Display Control（006/007/011）| `1.8.1.1.1 HU behavior in response to ICS POWER hardkey pressed events {4819556}`、`1.5.1.1.2 HU behavior in response to ICS SCREEN OFF hardkey press events {4819389}` |
| Browse Control（003/004）、Menu Navigation（008/009）| `1.8.1.2 Rotary Knob Data Transfer {4819577}`、`1.8.1.3 Button Press Events {4819587}`、`1.8.1.1 Push Button Data Transfer {4819542}` |
| Stuck Button（010）| `1.4.1.3.1 Integrated Center Stack (ICS) - Audio and Telematics Button Stuck {4819296}`、`1.8.1.4 Stuck Button Behavior {4819615}` |

DUT 分支之判定（實測，非推定）：`1.8` 之標題為
`Functional Requirements - PNet & AtlHi & AtlMi- ICS, Silver Box HU, DCSD, FPDM, CCDMF, and CCDMR {4819537}`，
其下物件之 `[EE Architecture:Atlantis High, PowerNet]`、`[Radio:… R1L, R1L-R …]`
與本案 DUT 相符；`1.5` 分支為 `PowerNet` only，不適用。

**本包未據此擴充範圍**（範圍界定為 Pei 專屬，charter §觸點）。

### 6-3 【重】`<Tstuck_button>` 之「忽略按鍵動作」母條在 CFTS020，且 b01 未涵蓋

CFTS020 `1.8.1.4 Stuck Button Behavior {4819615}` 之物件 **4819617** 原句（逐字）：

> When the HU receives a physical button press signal with a continuous button
> pressed for more than \<Tstuck_button\>, the HU shall ignore the press request
> until a signal has been received that the button has been released.  Refer to
> {CFTS020-479} for the physical button press signals.

此句與 SWRA `SWE-ICS-009` 之 Requirement Description（A-ICS1 判其實屬 010）
語意逐項對應（`configured ICS button and knob signals`／`ignore corresponding
actions`／`<Tstuck_button> timeout duration`）。

**後果三項**：

1. SWE-ICS-010 之行為面有**兩件**：CFTS022 之「設 DTC ＋ 送 not-pressed」
   （b01 之 S1/S2/S3 已涵蓋）與 CFTS020 之「**忽略按鍵請求直至收到放開訊號**」
   （**b01 未涵蓋，且下放包 §二 未點名**）。
2. DR-ICS7 問 `<Tstuck_button>` 之值：CFTS020 亦寫符號 `<Tstuck_button>` 而非數值，
   故該 DR **仍需上游**；但其「哪一條的門檻」須先分清 —— CFTS022-4914956 之
   120 s 管 DTC，CFTS020-4819617 之 `<Tstuck_button>` 管忽略行為，
   **二者未必同值**。R-ICS3 現行條文只涵蓋前者。
3. `1.4.1.3.1 {4819296}` 另載 ICS 之 stuck DTC 成熟條件（monitor type
   `Continuous`、monitor rate `4 ms`、healing `40 ignition cycles`、
   Enable/Mature 條件轉引 `DTCs Matrix Core List`）——
   而 `forms/DTCs Matrix Core List Rev. 1.6.xlsx` **在 repo 內**。

### 6-4 【重】DR-ICS8 有可行之解，其材料全在 repo 內

CFTS020 物件 **4819547** 原句（逐字，`[EE Architecture:PowerNet, Atlantis High]`）：

> See the latest version of the [Logical Identifiers and CAN Mapping v\*.xlsx]
> file for the CAN signals related to the following Logical Identifiers (LIDs):
> $ICSMuteButton$$Enter_Button$$ICSScr…

即：ICS 之 LID→CAN 對照就走 LID 檔。**實測 `forms/Logical Identifiers and CAN
Mapping v1_78.xlsx` 之 `CAN Mapping` 分頁，9 個 LID 全數命中**：

| LID | 列 | Atlantis High 欄之 Signal Name（實測） | 格式（同欄，實測）|
|---|---|---|---|
| `Back_Button` | 131 | `CLIMATIC_PANEL.Radio_btn3` | 1 bit，`0 = Not_Pressed (Back button)` / `1 = Pressed` |
| `Enter_Button` | 666 | `CLIMATIC_PANEL.Radio_btn1` / `DIS_CENTERSTACK.DCSD_Enter` | 1 bit，`0 = Not_Pressed (List/Enter button)` / `1 = Pressed` |
| `ICS_KNOB1_DIR` | 1024 | `CLIMATIC_PANEL.Radio_Knob1_DIR` / `DIS_CENTERSTACK.DCSD_VOLKNOB_DIR` | 2 bit，`0 = Knob_no_change` / `1 = Knob_increment` / `2 = …` |
| `ICS_KNOB1_VAL` | 1025 | `CLIMATIC_PANEL.Radio_Knob1_VAL` / `DIS_CENTERSTACK.DCSD_VOLKNOB_VAL` | 6 bit，`0 - +63`，resolution = 1 |
| `ICS_KNOB2_DIR` | 1026 | `CLIMATIC_PANEL.Radio_Knob2_DIR` / `DIS_CENTERSTACK.DCSD_TUNEKNOB_DIR` | 2 bit，同 KNOB1_DIR 之列舉 |
| `ICS_KNOB2_VAL` | 1027 | `CLIMATIC_PANEL.Radio_Knob2_VAL` / `DIS_CENTERSTACK.DCSD_TUNEKNOB_VAL` | 6 bit，`0-63`，resolution = 1 |
| `ICSMuteButton` | 1038 | `CLIMATIC_PANEL.Radio_btn4` / `GW_B_5.Mute_Button` / `DIS_CENTERSTACK.DCSD_…` | 1 bit，`0 = Not_Pressed` / `1 = Pressed` |
| `ICSPowerButton` | 1039 | `CLIMATIC_PANEL.Radio_btn0` / `DIS_CENTERSTACK.DCSD_Power` | 1 bit，`0 = Button NOT pressed` / `1 = Button pressed` |
| `ICSScreenOffButton` | 1044 | `CLIMATIC_PANEL.Radio_btn2` / `DIS_CENTERSTACK.DCSD_Screen_Off` | 1 bit，`0 = Not_Pressed (Screen Off button)` / `1 = Pressed` |

掃描條件：`CAN Mapping` 分頁第 1–1045 列，全欄轉字串後之包含比對（區分大小寫、
不設詞界）；`Atlantis High` 為第 2 列表頭之欄群，其 `Signal Name`／`Format`
分別為第 26／28 欄（表頭列 = 第 3 列，實測）。9/9 命中，無漏。
**同欄多值者為原檔即以換行並列**（如 `ICSMuteButton` 之三值），
取捨須有條文，見下段。

**本包未據此改寫任何 PENDING 佔位**。理由：走這條路須先有一條裁定
「二架構欄不同字時取哪一欄」與「訊號寫法」的條文 ——
`driver_distraction` 為此開了 R-DD6 v2(b) 與 R-DD9。ICS 尚無對應條文，
執行層自選欄位即無授權變更（FO §8.5 之一）。**條文由分析層出，本包不代擬。**

### 6-5 CFTS022-4914958 之 `Artifact Type` 為 `Description` 而非 SFR

S2 之錨兼引 4914958，因「DTC 於收到 de-bounced not-pressed 後清除」之原句只在該物件。
但其屬性實測為 `[Artifact Type:Description]`（4914954／4914958／4914971／4914973 同）。
`privacy` 之既有交付只錨 SFR 型物件。**Description 得否充 `specification_reference` 之錨，
請分析層裁定**；裁「否」時 S2 改單錨 4914957，並將清除面另立或轉 DR。

### 6-6 與 `privacy` feature 之交界已查，無重疊

實測 `features/privacy/` 全目錄之 `CFTS022-\d{7}` 命中集合為
{4914955, 4915104, 4915158, 4915168–75}，**與 b01 之錨集合
{4914956, 4914957, 4914958, 4914974, 4914975, 4914976} 交集為空**。
4914955（退出 SLEEP MODE 後監測按鍵狀態）由 privacy 承擔，
故 S3 之「按鍵功能正常」不另錨 4914955（IN §8.2.1），只以按鍵狀態回報觀察之。

### 6-7 下放包 01 缺 FO §8.1 之四項必要成分

| 成分 | 下放包 01 |
|---|---|
| 禁區（git 一律列入）| **缺** |
| 裁決引用 `R-XX@<sha8>` | **缺**（只有裸編號）|
| 預期數字 | **缺**（§四之對照由本包自 §二 文字反推）|
| 掃描條件 | **缺** |
| 升級條件 | **缺** |
| 背景／作業清單／上繳要求 | 有 |

本包未因此停下（作業內容本身無歧義），但依 FO §8.0 之三種失效第 2 項具名回報。

---

## §7 結果三分法（FO §8.4）

| 分類 | 項 |
|---|---|
| **改對了** | 骨架六目錄、`feature.yaml`、`.gitignore`、036 副本、6 條 TC、2 支檢查腳本、manifest |
| **核實無誤** | R-ICS4 之分流（V3 之上半確為 SWRA 002 逐字，本包重抽比對）；A-ICS1 之 +1 位移（001/005/006/009/010 五列逐一覆核，與登記相符）；DR-ICS7 之 120 s／10 min 對照（4914956 = 120 seconds、4914954 = 10 minutes，皆逐字命中）|
| **正確地不動** | DR-ICS8 之三處佔位不改寫（§六-4：無授權條文）；CFTS020 之四個受阻面不動工（§六-2：範圍界定屬 Pei）；`ANOMALIES.md`／`DATA_REQUESTS.md`／`RULINGS.md`／`framework.md` 一字未動（分析層之簿）；`workbook_state` 之 write_back.author_value 留 `null`（交付形式未裁）；未跑 `recon.py`（本 feature 無 037 leaf 表為母體，三項 assertion 皆無對應）|

---

## §8 獨立判斷：本包是否仍有該驗而未驗者

**有，四項。**

1. **SWE-ICS-010 之「忽略按鍵請求」面完全未驗**（§六-3）。b01 之三條全在
   CFTS022 之 DTC 面；CFTS020-4819617 之 ignore 行為一條未寫，而它正是
   SWRA 010 之 Verification Criteria 原文（`Verify actions are ignored after
   configured stuck button timeout condition`）所指。**b01 之三條無一驗到該 VC。**
2. **V 組之 ECU 屬性與 DUT 之關係未驗到底**。實測 4914975／4914976 之
   `[ECU:RRM, ETM, LTM]`、4914972／4914974 之 `[ECU:LTM, ETM]` —— **皆無 `ICS`**。
   R-ICS2 以 {ICS, LTM} 聯集納入，DR-ICS9 問的正是這件；
   若上游裁定收窄為 `ICS`，**V1/V2/V3 三條全數回收**。
   本包依現行 R-ICS2 生成，但此為 b01 六條中風險最高之三條。
3. **`VOLUME POP_UP` 之顯示條件未驗**。4914974 只說「HU shall show 'VOLUME POP_UP'
   to indicate the current volume level」，未載其出現時機與停留時間（屬 CFTS019，
   DR-ICS4）。V1–V3 之 ER 第 1／3 行斷言 popup 顯示，
   **若 popup 只在特定條件出現，該三行即為潛在 FF（IN §7）**。
4. **DTC 之成熟／消除條件未驗**（§六-3 第 3 點）。S1 斷言「DTC is set」、
   S2 斷言「DTC is cleared」，但 4819296 明載成熟條件轉引 `DTCs Matrix Core List`
   （檔在 `forms/`），未查該表即無法確定「按滿 120 s 後多久 DTC 才成熟」。
   S1/S2 現行寫法未給等待時間，台架實跑可能因未成熟而誤判 FAIL。

---

## §9 未結 DR 清單（下放包 §一-3 要求）

| DR | 狀態 | 本包之新事實 |
|---|---|---|
| DR-ICS1 | OPEN | 覆核相符，無新事實 |
| DR-ICS2 | OPEN | 無新事實 |
| DR-ICS3 | OPEN | 無新事實 |
| DR-ICS4 | OPEN | b01 有 1 處佔位待其回覆 |
| DR-ICS5 | **OPEN，但其前提有誤** | CFTS020 FS 就在 `inputs/`（§六-2）。建議改為「請確認 `R1LR_Atl-H_26PI1.5 …CFTS_020 ICS and DCSD_20260310-1533` 是否即所需之 FS 版本」|
| DR-ICS6 | **OPEN，範圍可縮** | KNOB2／Enter／Back 之母條在 CFTS020 `1.8.1.1`／`1.8.1.2`／`1.8.1.3`（§六-2）；仍缺者為 HMI Logic and Flow 之畫面流 |
| DR-ICS7 | **OPEN，需拆為二** | 120 s（CFTS022-4914956，管 DTC）與 `<Tstuck_button>`（CFTS020-4819617，管忽略行為）未必同值（§六-3）|
| DR-ICS8 | **OPEN，有解可循** | 9 個 LID 全在 `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`（§六-4）；所缺者為「取哪一架構欄」與「訊號寫法」之裁決 |
| DR-ICS9 | OPEN | V 組三條之存續繫於此（§八-2）|

**9 條全開，無一結案。**

---

## §10 待分析層裁定之事項（本包不代擬條文，FO §8.5 之一）

1. `sandbox/`／`generated/` 之落點是否採納（§二），或改基線（Tier 3）
2. S1 之 priority 取 P0 或範式之 P1（§四-4）
3. CFTS022-4914958 之 `Description` 型物件得否充錨（§六-5）
4. CFTS020 是否納為本 feature 之第二來源，及其 spec_mode 之影響（§六-2）
5. `<Tstuck_button>` 之忽略行為面是否納入本 feature 之範圍（§六-3；範圍界定屬 Pei）
6. DR-ICS8 之解法：是否比照 `driver_distraction` 之 LID→DBC 路徑另立條文（§六-4）

## §11 本包引用之既有裁決／條文編號清單

R-ICS1、R-ICS2、R-ICS3、R-ICS4、A-ICS1、A-ICS6、R-G13、R-G15、R-G25、
R-BLM11、R-DD6 v2、R-DD9、FO §2、FO §3、FO §5a、FO §8.1、FO §8.2、FO §8.4、
FO §8.5、FO §8.8、IN §1、IN §4.3、IN §4.3.1、IN §4.4、IN §4.5、IN §5.1、
IN §5.2、IN §5.5、IN §5.6、IN §5.7、IN §6、IN §7、IN §8.2.1、IN §8.2.2、
IN §8.3、IN §8.4.1、IN §8.4.3、IN §8.6、IN §8.7.1、IN §9、IN §10.1、IN §10.2、
IN §10.3、IN §10.4、IN §10.5、IN §10.7、IN §11、IN §12。

**本包未產生任何新裁決條文**（執行層不代擬）。
建議登錄之 anomaly 四則（A-ICS8～A-ICS11 之候選，編號由分析層取）：
§六-1（素材位置與型態之陳述不符）、§六-2（DR-ICS5 前提有誤）、
§六-3（010 之第二行為面未涵蓋）、§六-7（下放包缺契約成分）。
