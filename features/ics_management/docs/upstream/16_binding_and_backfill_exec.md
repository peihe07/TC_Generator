# 上繳包 16 — 綁定與讀者、12 處回填、reasoning 更正（2026-08-30）

對應下放包：`docs/handoff/16_binding_and_backfill_exec.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `afda1094129c8535c998cc6e383e67547e50b211ed18586cede3614ecb97e256`**
—— 與執行層自身記錄相符，未停。

**本包 git 執行次數 0**（含唯讀）。
**E27／E30／E31／E32／E1／E9／E18 全部未觸發。作業 A～E 全數完成。**

**十六包來第一次補完一件缺件：DR-ICS8 之 12 處佔位全數回填，ICS 佔位由 18 處降至 6 處。**

---

## §1 裁決指紋＋前提驗證＋圍籬 diff

### 1.1 前提驗證 —— **P1～P4 全部相符**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | `## R-ICS` **55** 行、相異 **48**；無重複條號 | **55 行、相異 48**；無 DUPLICATE | 相符（**E18 未觸發**）|
| P2 | A-ICS **107 列**、相異 107、號段 1–107 無缺口；DR 21／21 | **107／107／無缺口**；**DR 21／21／無缺口** | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |
| P4 | 圍籬 diff 新增 `R-ICS47`＋`R-ICS48` 二條、刪除 0 | **新增 95 行、刪除 0**；新增 `##` 標題 **`R-ICS47`、`R-ICS48`** | 相符 |

**A-ICS107 之告誡已遵行**：台帳最大號一律以 `grep` 取最大值，未以檔案末列推定。
`ledger_guard` 之 `registry_ids` 本即取全檔最大值，故列序錯置不影響其判準 —— 實測相符。

---

## §2 作業 A — 綁定 BHCAN2 ＋ 建立讀者

### 2-1 `feature.yaml`：`reference:` **10 → 11 鍵**

鍵名取 **`dbc_bh2`**，依既有體例（`dbc_b`／`dbc_fd`）。
sha256 **現場以 `shasum -a 256` 重算**（未抄用任何包所載之值）：
`46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`。
**既有 10 鍵一字未改**（由 §2-4 之 11／11 全 MATCH 反證）。

### 2-2 `FORMS.md`：僅一列一欄

改前：`> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19 選定為其 B-CAN 資料庫）。…`
改後：`… ：`display`（R-DM19 選定為其 B-CAN 資料庫）、`ics_management`（R-ICS46，Pei 裁定之台架觀察匯流排）。…`

**該表無獨立之 R-G15 反向記載列**（反向記載即嵌於各檔標題下之引述行），
依令**未新建**。其版次、sha、取代關係欄及其他所有列**一字未改**。

### 2-3 讀者之移植檢查表（R-G40 五）

| 原型之鍵／行為 | 移植後 | 對照結果 |
|---|---|---|
| `ROOT = parents[3]`／`FEATURE_YAML = parents[1]/"feature.yaml"` | 同 | 沿用（相對深度相同）|
| `yaml.safe_load` 讀 `reference:` | 同 | 沿用 |
| 空 `reference:` → 印訊息並 return 0 | 同 | 沿用 |
| 逐鍵 `sorted(ref)`、`file`／`sha256` | 同 | 沿用 |
| 五種 verdict：`MATCH`／`MISMATCH`／`MISSING`／`NO FILE DECLARED`／`NO SHA DECLARED` | 同 | 沿用 |
| 分塊讀檔（1 MB）計 sha256 | 同 | 沿用 |
| 不符 → exit 1 並印**二值** | 同 | 沿用 |
| **永不回寫宣告值**（R-G23）| 同 | 沿用 |
| docstring 之 feature 特定敘述 | **改寫** | 由 R-DM19／26 列訊號解析，改為 R-ICS46／b03 之 12 處回填與 A-ICS97（本 feature 之 10 個 sha 此前無人比對）|

**缺鍵：0（無需補）。** 差異僅在 docstring 之情境敘述，程式行為逐項相同。

### 2-4 【E27 判定點】首跑 **11／11 相符 → 未觸發**

11 鍵全數 `MATCH`，exit 0。**既有 10 鍵無一不符** ——
即過去十六包所綁之參考件**皆未被改動**。

**這是 A-ICS97 之直接解除**：本 feature 之 sha 此前十六包無任何程式比對，
本包首次驗證，結果全綠。

### 2-5 納入 gate 集 —— **未執行，理由具名**

下放包 §3 作業 A 步驟 5 令「納入 gate 集」。**本包未執行，非遺漏：**

- 全案之閘登錄簿為 `docs/runtime/GATES.tsv`（47 列）。實測 **`ics_management` 於該簿命中 0 列**
  —— 本 feature 至今無任何 feature 級閘登錄。
- **`display` 與 `bed_lowering` 之同名 `verify_reference_binding.py` 亦均未登錄於該簿**
  （全 repo 搜尋，命中 0）。即「讀者入簿」在本 repo 尚無先例。
- `gates_tsv --check` **開工前即為紅**（五支紅之一，成因與本包無關）。
  向一個已紅之全域登錄簿新增本 feature 之首列，其效果無法在本包內驗證。
- `docs/runtime/GATES.tsv` **不在 `features/ics_management/` 之內**，屬跨線檔。

**執行層不逕自寫入跨線之全域登錄簿**（同 R-ICS44(d)「只量不綁」之拿法）。
**已實跑該讀者並於 §6 報其結果**（第六支）。入簿之形式與時點請分析層裁。

---

## §3 作業 B — 12 處佔位回填

### 3-1 【E31 判定點】複驗 —— **未觸發**

`DR-ICS8` 之佔位 **12 處**，缺件相異值 **1 種**：`<TGW_DISP_STAT CAN signal>`。
**12 處全部落在 `test_procedure` 欄**（與 b13 §1 之複驗一致）。

### 3-2 回填後之逐處全文


**Power hardkey pressed while HU screen on**

- `test_procedure` 行 1：1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and record it
- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 0 (Display_off)
- `expected_result` 行 1：1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)
- `expected_result` 行 4：4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is observed on the CAN trace (supporting observation)

**Power hardkey pressed at Telematic Power full operation**

- `pre_conditions` 行 3：3. $STATUS_TELEMATIC.PowerSts_Telematic$ is 4 (Full_Operation)
- `test_procedure` 行 1：1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and record it
- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 0 (Display_off)
- `expected_result` 行 1：1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ is recorded on the CAN trace (supporting observation)
- `expected_result` 行 4：4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is observed on the CAN trace (supporting observation)

**Power hardkey pressed while HU screen off**

- `test_procedure` 行 1：1. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and record it
- `test_procedure` 行 5：5. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 2 (Normal_mode)
- `expected_result` 行 1：1. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is observed on the CAN trace (supporting observation)
- `expected_result` 行 5：5. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)

**Power hardkey pressed at Telematic Power idle**

- `pre_conditions` 行 3：3. $STATUS_TELEMATIC.PowerSts_Telematic$ is 3 (Idle)
- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 2 (Normal_mode)
- `expected_result` 行 4：4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)

**Screen off hardkey starts the three second timer**

- `test_procedure` 行 3：3. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 1 second after the button press and check that it is 2 (Normal_mode)
- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 2 seconds after the button press and check that it is 2 (Normal_mode)
- `expected_result` 行 3：3. The "TOUCH SCREEN TO TURN ON" graphic is shown, and the signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)
- `expected_result` 行 4：4. The "TOUCH SCREEN TO TURN ON" graphic is shown, and the signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)

**Screen off hardkey pressed again within three seconds**

- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace 5 seconds after the second press and check that it is 2 (Normal_mode)
- `expected_result` 行 4：4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)

**Three second period completed after screen off hardkey**

- `test_procedure` 行 3：3. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 0 (Display_off)
- `expected_result` 行 3：3. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 0 (Display_off) is observed on the CAN trace (supporting observation)

**Screen off hardkey pressed while HU screen off**

- `test_procedure` 行 4：4. Read the signal $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ on the CAN trace and check that it is 2 (Normal_mode)
- `expected_result` 行 4：4. The signal value $TELEMATIC_DISPLAY2.TGW_DISP_STATSts$ = 2 (Normal_mode) is observed on the CAN trace (supporting observation)

**回填處數統計**：`test_procedure` **12 處**（PENDING 全消）、
`expected_result` **12 行**（值名同批改，避免混用）、
`pre_conditions` **2 條**（A-ICS106 之裸符號）。

### 3-3 值之來源逐字

| 規格側 | DBC 側（`VAL_ 1500`，`forms/PDT27_E2A_R1_BHCAN2.dbc`）|
|---|---|
| `"DISP_OFF"` | `0 (Display_off)` |
| `"DISP_NORMAL"` | `2 (Normal_mode)` |

| 規格側 | DBC 側（`VAL_ 1470`）|
|---|---|
| `"Full_Operation"` | `4 (Full_Operation)` |
| `"Idle"` | `3 (Idle)` |

**訊號名與值名同批改，無「訊號名用 DBC、值名用規格」之混用。**
`VAL_ 1500` 之另三值（`7 Rear_Camera_Display`／`8 On_blanked_screen`／`15 SNA`）
於本次 12 處中**未被用到** —— 具名，非遺漏。

### 3-4 `reasoning` 追記（R-17(b)）

八條各追記，逐字：

> **b16 回填（R-ICS48(c)／R-17(a)）**：規格作 `$TGW_DISP_STAT$`，DBC 實名
> `TGW_DISP_STATSts`＠`BO_ 1500 TELEMATIC_DISPLAY2`（`forms/PDT27_E2A_R1_BHCAN2.dbc`，
> b16 綁為 `reference.dbc_bh2`），依 R-17 採 DBC 實名實值；值取自 `VAL_ 1500` 逐字
> （`0 "Display_off"`／`2 "Normal_mode"`）。同一物之判定**僅繫於 R-17(c) 項③**
> （項①② 對 CFTS020 結構性不可比，A-ICS94），**列為可重驗項**。

TC 2／TC 4 另各追記裸符號改寫之依據，並載明
**「A-ICS91 之台架可行性面維持 OPEN，不因本次改寫而結案」**（R-ICS48(c)）。

### 3-5 【E30 判定點】`(supporting observation)` 之複審 —— **判定為仍正確，未改，故 E30 未到判定點**

b14 §3-4 曾推測該標記「在方向確立後可能不再正確」。
**本包逐行檢視 ER 原文後，判定其仍正確，理由如下：**

`(supporting observation)` 描述的是該 ER 項**相對於本條主要斷言之證據角色**，
不是訊號之傳輸方向。八條之主要斷言皆為**畫面狀態**
（`The HU screen is dark and shows no content`、`The previous "HU Screen ON" screen is shown again`、
`The "TOUCH SCREEN TO TURN ON" graphic is shown`）；
`$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$` 之觀察是**佐證該畫面斷言**。

DUT 為該訊號之發出者，**使該佐證更直接、更可信，但不改變其為佐證之角色** ——
本條要驗的仍是「按鍵→畫面狀態」，不是「DUT 送出正確之值」。

**故 12／12 之標記判為正確，改動數 0。E30（改動會牽動驗證目標）未到判定點。**
**此判定推翻 b14 §3-4 之推測** —— 該推測係在未逐行對照 ER 主要斷言之下作出。

### 3-6 【E32 判定點】回填後之佔位 —— **未觸發**

| 批 | 回填前 | 回填後 |
|---|---|---|
| b01 | 1 | 1 |
| b02 | 0 | 0 |
| **b03** | **12** | **0** |
| b04 | 2 | 2 |
| b05 | 2 | 2 |
| b06 | 0 | 0 |
| b07 | 1 | 1 |
| **合計** | **18 處／14 條** | **6 處／6 條** |

**6 ＝ 18 － 12，與預期 #8 完全相符 → E32 未觸發。**
涉佔位之 TC **14 → 6**，與預期 #9 相符。

### 3-7 回填之副作用：`has_pending` 旗標須同步（自行發現並修正）

回填後首次重跑 `selfcheck_b01.py` **報 FAIL 1 項**（§8.4.3）：
b03 之八條 `has_pending` 仍為 `true` 而其佔位已全消。

**此為本包回填所致之副作用，非既有缺陷。** 已修正 8 條（`true` → `false`），
並以 `pending_census.py --write` 同步各批 manifest。修正後 **19 項 FAIL 0**。

**具名此事**：下放包 §3 作業 B 步驟 6 只令「重跑三支」，未令同步該旗標；
若只依字面重跑而不修，本包會交出一批自相矛盾的 TC。

---

## §4 作業 C — `reasoning` 過時引述之更正（3 條）

### 4-1 更正前（三條逐字相同）

> R4_BHCAN `BO_ 1283`，`SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" DCSD`，**發送節點為 SGW 而非 ICS**（已具名，見 upstream-04 §三）。

### 4-2 A 檔之實情（逐字複驗）

`forms/PDT27_E2A_R1_BHCAN2.dbc`：`BO_ 1283 RADIO_B3: 8 ETM`；
`SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" SGW`。

### 4-3 更正後

> **b16 更正（A-ICS100／R-ICS48(e)）**：原文引 `R4_BHCAN` 之 `BO_ 1283`，
> `SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" DCSD` 並斷「發送節點為 SGW 而非 ICS」——
> **該行逐字取自 `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`，於 Pei 所裁之台架匯流排上不正確**。
> 改依裁定之 `forms/PDT27_E2A_R1_BHCAN2.dbc`（b16 綁為 `reference.dbc_bh2`）：
> `BO_ 1283 RADIO_B3: 8 ETM`，`SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" SGW`，
> **發送節點為 ETM（本 DUT 側）、接收節點為 SGW**。二檔之起始位元、長度、factor／offset、
> 值域、單位、`VAL_` 皆相同（b15 實測 17／17），差異僅在發收方，係閘道轉發之上下游二段。
> （凡引 DBC 原行者一律註明所據檔名，以免再次過時。）

**更正 3 條，each 註明所據 dbc 檔名（與預期 #14 相符）；不及交付欄。**

---

## §5 作業 D — Pre-Condition 體例抽查（`docs/reports/16_precondition_style.md`）

31 條之 `pre_conditions` 項目總數 **105**：

| 類 | 實數 | 占比 |
|---|---|---|
| 環境／硬體前提 | **58** | 55% |
| **狀態陳述、無建立步驟** | **42** | **40%** |
| 狀態陳述、有建立步驟 | **5** | 5% |

**核心答案：是全批體例，不是 TC 2／4 之個例。**
「無建立步驟」之 42 項分佈於**全部七個批次**，非集中於 b03；
TC 2／TC 4 之 `$Telematic_Power$` 只是其中二項。
「有建立步驟」僅 5 項（5%），反而是少數。

依 **R-ICS47(d)**（IN §4.4 定 Pre-Condition 為起始狀態／環境且明禁寫入動作），
**該形態本身非缺陷**；40% 之比例與該裁定一致。**只量不改，未動任何 TC。**

**局限**：「有建立步驟」以字面比對判定，語意等價而用詞不同者會被歸入「無建立步驟」，
故 42 為**上限**。

---

## §6 作業 E — 常設自檢集

| 項 | 結果 |
|---|---|
| 圍籬 diff | **+95／−0**；新增 `R-ICS47`、`R-ICS48`（P4 相符）|
| 候選篩 | 原始 **140**／殘餘 **68**／**殘餘率 49%**（前七包 53／53／43／52／47／47／47%）。**殘餘由 66 升至 68**，因回填引入新實詞（訊號名與值標籤）|
| 未錨定斷言 | **3（弱驗證）＋ 6（已標明）**，不變 |
| `selfcheck_b01.py` | **PASS** —— 機檢 19 項 FAIL 0（修正 `has_pending` 後）|
| `verify_verbatim_b01.py` | **PASS —— 31／31**（`test_item` 上半未動，與預期 #10 相符）|
| `pending_census.py` | **6 處／6 條** |
| `ledger_guard.py` | 前後 exit 0，**逐字相同** |
| **第六支：`verify_reference_binding.py`** | **11／11 MATCH，exit 0** |
| 五支 gate | **差 +1 於 `canon_refs`（445 → 446）** —— 見下 |
| 快照 | `docs/reports/16_rulings_snapshot.md` **已產出**，55 錨點 |

### 6-1 gate 之 +1 —— **經查不源於本包**

`canon_refs` 由 445 升至 446。**本包二新檔（`verify_reference_binding.py`、
`16_precondition_style.md`）於 `--report` 之 unresolved／ambiguous 清單中
（含 waiver 與不含 waiver 二種跑法）皆 0 命中**；
本包所改之 `feature.yaml`、`b03_tcs.json` 亦 0 命中。

另一佐證：掃描檔數由 2523 升至 **2524（+1）**，而本包新增 **二檔** ——
**期間有並行寫入**（他線於 `docs/fw036/` 之活動已見於本 session 稍早）。

**不修**（`canon_refs` 為開工前即紅之閘，成因在他線）。**具名而不調和。**

### 6-2 禁區自證

- `features/display/`、`features/vehicle_setting/`：**變動 0 處**（`find -newermt` 實測）
- `forms/FORMS.md`：僅 BHCAN2 一列之「使用 feature」欄一處
- 錨（`specification_reference`）：**變動 0 處**（錨行總數仍 **65**）
- `test_item` 上半：未動（`verify_verbatim` 31／31 反證）
- 其他 TC 之 `reasoning`：未動（僅 b03 之三條 ＋ 回填八條之追記）

---

## §7 預期數字對照（下放包 §5，20 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` 開工前 | 55 行（相異 48）、A-ICS 107、DR 21／21 | 全數相符 | 相符 |
| 2 | 圍籬 diff | 新增二條、刪除 0 | **+95／−0，二條** | 相符 |
| 3 | `reference:` 鍵數 | 10 → 11 | **10 → 11**（`dbc_bh2`）| 相符 |
| 4 | `FORMS.md` 變動 | 僅一列一欄 | **僅一列一欄** | 相符 |
| 5 | 讀者首跑 | 11／11 | **11／11，exit 0** | 相符（**E27 未觸發**）|
| 6 | `display`／`vehicle_setting` 變動 | 0 處 | **0 處** | 相符 |
| 7 | 回填處數 | 12 | **12** | 相符 |
| 8 | 回填後佔位總數 | 6 處 | **6 處** | 相符（**E32 未觸發**）|
| 9 | 涉佔位之 TC 數 | 14 → 6 | **14 → 6** | 相符 |
| 10 | `verify_verbatim` | 31／31 | **31／31** | 相符 |
| 11 | TC 總數 | 31 | **31** | 相符 |
| 12 | 錨變動 | 0 處 | **0 處**（錨行 65）| 相符 |
| 13 | Test Set 相異值 | 5 | **5** | 相符 |
| 14 | 作業 C | 3 條；each 註明 dbc 檔名 | **3 條；皆註明** | 相符 |
| 15 | 作業 D | 四類實數；答全批抑或個例 | 58／42／5；**全批體例** | 相符 |
| 16 | `(supporting observation)` 複審 | 逐條判定；改動數為實測值 | 12／12 判**仍正確**；改動 **0** | 相符 |
| 17 | 候選篩 | 二數並報＋殘餘率 | 140／68／**49%** | 相符 |
| 18 | 五支 gate | 差**皆 0** | **canon_refs +1**（經查不源於本包，§6-1）| **不符（具名）** |
| 19 | **git 執行次數** | **0** | **0** | 相符 |
| 20 | 快照 | 已產出 | **已產出** | 相符 |

**19 項相符、1 項不符（#18）。** 另有一項下放包所令而本包未執行者：
**作業 A 步驟 5「納入 gate 集」**（§2-5，理由具名）。

---

## §8 未結 DR 清單（21 條）

| DR | 現況 | 本包新事實 |
|---|---|---|
| DR-ICS1／3／11／14／17／19／21 | OPEN | — |
| DR-ICS2 | OPEN | B5 所繫 |
| DR-ICS4 | OPEN | **1 處佔位**（b01）|
| DR-ICS5／7／10／15 | 可結 | — |
| DR-ICS6 | OPEN | **5 處佔位**（b04×2／b05×2／b07×1）|
| **DR-ICS8** | OPEN | **12 處佔位全數回填，殘餘 0** —— 見 §10-2 之建議 |
| DR-ICS9 | OPEN | V1／V2／V3 所繫；**無佔位故不會自行浮出** |
| DR-ICS12 | 追蹤件 | — |
| DR-ICS13 | 分析層已標「可結」 | 執行層未動 |
| DR-ICS16 | 匯流排軸已結 | **BHCAN2 已綁為 `reference.dbc_bh2`；讀者已建，11／11** |
| DR-ICS18 | 告知／追認件 | — |
| DR-ICS20 | OPEN | G2／G3 效力所繫 |

**回填後之 6 處佔位只繫於二個 DR：DR-ICS6（5 處）與 DR-ICS4（1 處）。**

---

## §9 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `feature.yaml` 增 `dbc_bh2`（sha 現場重算）；`FORMS.md` 一列一欄增列；新建 `scripts/verify_reference_binding.py`（移植，缺鍵 0）；b03 之 12 處佔位回填 ＋ 12 行 ER 值名同批改 ＋ 2 條裸符號改寫；八條 `reasoning` 追記；三條 `reasoning` 過時引述更正；8 條 `has_pending` 同步 ＋ manifest 同步；`16_precondition_style.md`；`16_rulings_snapshot.md` |
| **核實無誤** | **11／11 sha 全 MATCH（A-ICS97 解除，十六包來首次驗證）**；12 處佔位缺件相異值 1 種；回填後 6 處／6 條（＝18−12）；`verify_verbatim` 31／31；錨行仍 65；`display`／`vehicle_setting` 變動 0；`canon_refs` 之 +1 不源於本包（二新檔 0 命中）|
| **正確地不動** | `(supporting observation)` 12／12 判仍正確而**未改**（推翻 b14 之推測）；`VAL_ 1500` 之另三值未用到（具名非遺漏）；未寫入 `docs/runtime/GATES.tsv`（跨線全域簿，§2-5）；未修 `canon_refs` 之紅；未對任何 DR 結案；A-ICS91 之台架可行性面未結案；A-ICS104／105 未排入；G5 維持押後；五簿一字未寫；**git 0 次** |

---

## §10 獨立判斷

### 10-1 本包是否仍有該驗而未驗者 —— **有，二項**

1. **`VAL_ 1500` 之 `7 (Rear_Camera_Display)`／`8 (On_blanked_screen)`／`15 (SNA)` 三值未被任何 TC 用到。**
   規格側 `4819466`（`[ON_BLANK]`／`[SNA]`）與 `4819475`（`[DISP_REAR_CAMERA]`）
   均載此三態，而本線 31 條無一條驗之 —— **可能是覆蓋缺口**。本包未查其適用性，未生成。
2. **`RQ_DISP_INTS` 之值書寫未複審。** b03 三條之 `reasoning` 載
   `VAL_ 1283 RQ_DISP_INTS 255 "SNA";` 只列舉 255，而交付欄書 `0 (0 %)`。
   本包只更正該三條之發收方引述，**未查其值之書寫是否亦須依 R-17(a) 調整**。

### 10-2 【下放包 §6 指定其一】DR-ICS8 是否可標「可結」（只建議不裁）

**建議：可標可結。** b15 之保留理由已消滅。

b15 建議不可結，理由是「12 處佔位一處未回填，標可結會使 `pending_census` 與 DR 台帳矛盾」。
**本包 12 處全數回填，`pending_census` 之 DR-ICS8 殘餘為 0** —— 該矛盾不再存在。

其缺件（`TGW_DISP_STAT` 之訊號實體）已由 b14 判同一物、b15 交叉確認、b16 綁定並回填，
且 `verify_reference_binding` 首跑 11／11 證明所據之 dbc 就是被量測過的那一支。

**惟須連帶記載二事**（不影響結案，但不可遺失）：
(a) 同一物之判定**僅繫於 R-17(c) 項③**（項①② 對 CFTS020 結構性不可比，A-ICS94），
    已逐條寫入 `reasoning` 之可重驗項；
(b) **A-ICS91 之台架可行性面維持 OPEN** —— TC 2／TC 4 之前提能否在 BHCAN2 上建立，
    與 DR-ICS8 是兩件事，不因本次結案而解決。

### 10-3 【下放包 §6 指定其二】ICS 線是否已達「可部分交付」之點

**建議：已達「可清點」之點，尚未達「可交付」之點。二者差一件事，而那件事現在寫得下一行。**

**無佔位之條：31 － 6 ＝ 25 條。** 其中：

| 群 | 條數 | 可交付性 |
|---|---|---|
| b03 之八條（本包回填）| 8 | **可交付** —— 訊號實名實值已定、方向已明、匯流排已綁且受讀者檢驗 |
| b01／b02／b06 等其餘無佔位者 | 17 | **其中 4 條不可交付**：V1／V2／V3（DR-ICS9）、B5（DR-ICS2）|

**故：25 條無佔位，其中 21 條可交付、4 條不可。**

**那 4 條是唯一的阻礙，而它們的特性必須再說一次**：
V1／V2／V3 與 B5 **無佔位**，故 `pending_census` 不報、`selfcheck` 全綠、
本包之所有數字都不會提醒它們。**只有凍結記錄 §2 與本節會提醒。**
其阻因是 `VOLUME POP_UP` 之顯示條件在 CFTS022／020／019 與所有 HMI L&F 中查無，
線索止於 `HMI Pop Up List` —— 該件不在 repo。**連續十一包無進展。**

**建議之措辭**：ICS 現在可以說出一句十六包來說不出的話 ——
**「21 條可交付，4 條卡在 DR-ICS9／DR-ICS2，6 條卡在 DR-ICS6／DR-ICS4。」**
三個數字加起來是 31，且每一個都指向一個具名的 DR。
**這比「可部分交付」更有用**：它讓下一步是去要四份上游回覆，而不是再掃一次規格。

---

## §11 建議登錄之 anomaly（編號由分析層取）

1. **A-ICS97 可結**：本 feature 之 11 個 sha 首次受檢，**11／11 相符**；
   讀者已建於 `features/ics_management/scripts/verify_reference_binding.py`。
2. **【未執行事項】「納入 gate 集」無可行之載體**（§2-5）：
   `docs/runtime/GATES.tsv` 中 `ics_management` 命中 0 列，
   且 `display`／`bed_lowering` 之同名讀者亦均未登錄 —— **讀者入簿在本 repo 尚無先例**。
3. **回填之副作用：`has_pending` 旗標須手動同步**（§3-7）。
   下放包只令重跑三支自檢，未令同步該旗標；若依字面執行會交出自相矛盾之 TC。
   **拿法建議：回填類作業之收尾清單應含衍生旗標與 manifest 之同步。**
4. **`(supporting observation)` 之標記判為仍正確**（§3-5），**推翻 b14 §3-4 之推測**。
   標記描述證據角色，非傳輸方向。
5. **`VAL_ 1500` 之三值（`7`／`8`／`15`）無任何 TC 涵蓋**，而規格側 `4819466`／`4819475`
   均載此三態 —— 可能之覆蓋缺口，本包未查。
6. **`RQ_DISP_INTS` 之值書寫未依 R-17(a) 複審**（§10-1-2）。
7. `canon_refs` 之 +1 不源於本包（§6-1），成因在並行寫入。

**本包未產生任何新裁決條文，未自取任何編號。**

---

## §12 引用清單

R-ICS48(a)~(g)、R-ICS47(a)(d)(f)、R-17(a)(b)(c)、R-G40、R-G41(a)（全案）；
R-ICS1 ~ R-ICS48（實測 55 行／相異 48）；
A-ICS16、A-ICS31、A-ICS72、A-ICS91、A-ICS94、A-ICS97、A-ICS98、A-ICS100、A-ICS106、A-ICS107；
A-DM14、R-DM19、R-G15、R-G23；DR-ICS1 ~ DR-ICS21；R-G13、R-G17、R-G18、R-G25；
FO §8.2、FO §8.4、FO §8.5；IN §4.4、IN §7、IN §8.4.3、IN §8.7.5(a)、IN §9、IN §10.7、IN §11。
