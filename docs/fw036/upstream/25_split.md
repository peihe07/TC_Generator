# 上繳 25 包：拆分套用（A 型逐字 + B 型規則化）

基底 `features/power/sandbox/b19/pm_19.xlsx`
（sha256 `b4dd5ca0c0f02394117e52d4c8b342743d1ccef236d5b2ca392f8ba16f9871ca`，
下放包所指之 b4dd5ca0… 相符）。
輸出 `features/power/sandbox/b25/pm_25.xlsx`，止於工作副本，交付本未動。

## 摘要

| 項 | 下放包 §四 預期 | 實測 | 狀態 |
|---|---|---|---|
| A 型面向列 | 14 | 14 | 達成 |
| B 型面向列 | 186 | **144** | **不符**，見 §二 |
| 插入列數 | 165 | **123** | 隨面向數 |
| 全本資料列 | 448 | **407** | **不符**，見 §二／§三 |
| Test Case ID | 連續無跳號無重複 | 001–406，406 列 | 達成 |
| `proc↔er` 編號數逐列相等 | E=0 | E=0 | 達成 |
| lint A–N | 全零 | 全零（含 I-sibling=0） | 達成 |
| x14 讀回 | 前後相等 | 1 → 1（`R10:R221` → `R10:R340`） | 達成 |
| zip 成員 | 未變 | 42 → 42，差異僅 `sheet6.xml` | 達成 |
| `surgical_save` 唯一路徑 | 是 | 是（另見 §五 插列工具） | 達成 |

### lint 前後（`--profile power`）

| | A | B | C | D | E | F | G | H | I | I-sibling | J | K | L | M | N | P | Q | R | T | U |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 前 `pm_19` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 10 |
| 後 `pm_25` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 10 |

A–N 全零（含 I-sibling）。P=10／U=10 為 21 包起之未校準既有值，本包未動。
報告：`docs/fw036/lint_reports/pm_25__power_20260824.md`。

## 一、Pei 本包裁定（執行前提問所得）

1. **面向數以 §二 規則 2 為準 + 修補規則 1** —— 不採 30 列面向數表。
2. **row 230 存根列略過不給 Test Case ID；`No.#`（B 欄）一併重編。**

## 二、面向數：下放包 §二 之演算法與 30 列表不可能同時成立

實測（30/30 列）：**表列面向數 = 該列 ER 行數 = 該列 PROC 步數**，三者逐列相同。
下放包 §二 之 30 列表合計 **184**，非文中所寫之 186（加總誤算，淨增亦非 156）。

但 §二 規則 2 定義「setup 段**之後**每一步為一面向」—— setup 步不計面向，
故面向數必為 `PROC 步數 − setup 步數`，恆小於 ER 行數。要湊到 184 只能讓
setup 步也各自成列，其列之 PROC 即 setup 段本身，會產生逐字相同或互為前綴之
退化列，**直接違反 §四「任兩同源面向列不得逐字相同」**。兩者不可調和。

⚠ 附註「不一致時以實測為準並於上繳列出差異」據此執行：以規則 2 為準，
30/30 列皆與預核表不一致，逐列差異見 §六。

### 規則 1 之修補（4 列非修補不可）

規則 1 首分支「PROC 自首步至第一個 `Read the signal
$STATUS_TELEMATIC.PowerSts_Telematic$…` 止（含該步）為 setup 段」，
在該讀取步位於 **PROC 末步**時會吞掉全部步驟：

| row | PROC 步數 | 原判 setup | 原判面向數 |
|---|---|---|---|
| 32 | 5 | 5 | **0** |
| 97 | 5 | 5 | **0** |
| 102 | 5 | 5 | **0** |
| 170 | 5 | 5 | **0** |

面向數 0 時規則 3「原列改寫為第一面向列」無法成立。修補為一句限制：
**該讀取步為 PROC 末步時屬觀察步，不併入 setup**，隨即落到規則 1 之後兩分支。
四列皆得 setup=1、面向數 4。修補僅此一句，未新增動詞清單、未改其他分支。

## 三、全本列數 407（非 448）

- 基底資料列實為 **284**（rows 10–293），非下放包所寫 283。差額為 **row 230**：
  僅 `No.#`=221、`Requirement ID`=`SWE-PM-089`，無 Test Case ID、無四欄內容之
  存根列。283 為「有 TC ID 之列數」。
- 407 = 284 + 123（A 型 +9、B 型 +114）。
- Test Case ID 001–406 連續（406 = 407 − 存根列 1）。存根列依裁定不給 ID。
- `No.#` 依裁定重編 1–407。此舉逾越 §三 字面之「僅重寫 ID 欄，他欄不動」，
  係 Pei 本包裁定所許；不重編則 B 欄自新 row 11 起與實際列序全面錯位。

## 四、A 型 14 列：與下放包 §一 之逐字差異二處

1. **row 11 之 ER** 依 §一 所給文字寫入
   （`The signal $STATUS_BH_BCM1.OperationalModeSts$ = <V> (<L>) is registered
   without a bus error`），而原列該行為
   `The signal value $…$ = 5 (Ignition_Pre_Start) is received without a bus error`。
   §一 明示逐字，故以 §一 為準；此為對原列的**措辭改動**，非逐字複製，列此備查。
2. **rows 179b／180b 之 PRE** 依 §一「增一行
   `An incoming phone call is active on the HU`」寫入（置於工具可用行之前，
   該行依慣例恆為末行）。結果 PRE 同時聲明「The HU is in IDLE mode」與
   「An incoming phone call is active on the HU」—— 通話進行中 HU 應已在
   FULL OPERATION，兩行互斥。未擅改，列此待裁。

`test_item` 括號下半：§一 對 179／180 之 a／b 只給共同尾段
（`(incoming call -> FULL OPERATION)` 等），四列會兩兩逐字相同而觸發
lint I-sibling（179／180 同屬 `SWE-PM-069`）。故保留原列括號既有之區分前綴
（`The display is on the phone main screen — ` ／
`The display is on the phone projection call UI — `），文字全取自原列。

## 五、工具：`surgical_save` 無插列能力，另補結構插列段

`backend/xlsx_surgical.py` 之 `patch_sheet_xml` 對中段插列**明文中止**
（"surgical emit can only append rows past the last source row … Inserting
mid-sheet would shift every row below it, which this path deliberately cannot
do"）。§三 要求「新列原位插入」，故新增 `surgical_insert_rows`：純結構插列，
不寫任何值，逐列複製錨列之列高、`customFormat` 與逐格 `s=` 樣式
（否則插入列無框線、無自動換行、列高錯誤），並搬移 `<sheetData>` 外之列位參照：

| 元素 | 前 | 後 |
|---|---|---|
| `dimension` | `A1:AH293` | `A1:AH416` |
| `autoFilter` | `A9:AH221` | `A9:AH340` |
| `conditionalFormatting` | `H10:H145` | `H10:H264` |
| `dataValidation` | `P10:P221 Q10:Q11` | `P10:P340 Q10:Q11` |
| `dataValidation` | `T10:Z221 S10:S12` | `T10:Z340 S10:S12` |
| x14 `xm:sqref` | `R10:R221` | `R10:R340` |
| `mergeCells` | 5 個（皆在 rows 1–8） | 未動 |

`xl/drawings/*` 之錨點實測皆為 row 0、`vmlDrawing1.vml` 為 row 8，
全在插列區之上，故無須改動 zip 其他成員。兩段皆過 `verify_structure`，
`openpyxl.save` 全程未用。

本包寫出仍為兩段一路：`surgical_insert_rows`（結構）→ `surgical_save`（值）。

新增測試 `tests/test_xlsx_surgical_insert.py`（9 項，全綠）：位移代數、
值隨列下移、插入列樣式承錨列、列位參照隨列搬移、交付不變式、與後續
`surgical_save` 串接、錨列不存在中止、列序非升序中止。

`tests/test_single_write_path.py` 二項失敗為**既有狀態**（已以 stash 對照確認
與本包無關：`time_management`／`user_profiles`／`vehicle_setting` 之既有
call site 未登錄於 `KNOWN_VIOLATIONS`）。

## 六、逐列對照表

## 插列對照表

| 型 | 原 row | 原 TC ID | 面向數 | 新 rows | 新 TC ID 起訖 |
|---|---|---|---|---|---|
| B | 10 | NR1L-PowerManagement-001 | 4 | 10–13 | 001–004 |
| A | 11 | NR1L-PowerManagement-002 | 4 | 14–17 | 005–008 |
| A | 12 | NR1L-PowerManagement-003 | 3 | 18–20 | 009–011 |
| B | 17 | NR1L-PowerManagement-008 | 3 | 25–27 | 016–018 |
| B | 21 | NR1L-PowerManagement-012 | 5 | 31–35 | 022–026 |
| A | 23 | NR1L-PowerManagement-014 | 3 | 37–39 | 028–030 |
| B | 24 | NR1L-PowerManagement-015 | 6 | 40–45 | 031–036 |
| B | 26 | NR1L-PowerManagement-017 | 6 | 47–52 | 038–043 |
| B | 28 | NR1L-PowerManagement-019 | 3 | 54–56 | 045–047 |
| B | 29 | NR1L-PowerManagement-020 | 5 | 57–61 | 048–052 |
| B | 30 | NR1L-PowerManagement-021 | 5 | 62–66 | 053–057 |
| B | 32 | NR1L-PowerManagement-023 | 4 | 68–71 | 059–062 |
| B | 39 | NR1L-PowerManagement-030 | 4 | 78–81 | 069–072 |
| B | 45 | NR1L-PowerManagement-036 | 6 | 87–92 | 078–083 |
| B | 97 | NR1L-PowerManagement-088 | 4 | 144–147 | 135–138 |
| B | 102 | NR1L-PowerManagement-093 | 4 | 152–155 | 143–146 |
| B | 109 | NR1L-PowerManagement-100 | 2 | 162–163 | 153–154 |
| B | 124 | NR1L-PowerManagement-115 | 6 | 178–183 | 169–174 |
| B | 125 | NR1L-PowerManagement-116 | 6 | 184–189 | 175–180 |
| B | 126 | NR1L-PowerManagement-117 | 6 | 190–195 | 181–186 |
| B | 127 | NR1L-PowerManagement-118 | 6 | 196–201 | 187–192 |
| B | 157 | NR1L-PowerManagement-148 | 5 | 231–235 | 222–226 |
| B | 158 | NR1L-PowerManagement-149 | 5 | 236–240 | 227–231 |
| B | 159 | NR1L-PowerManagement-150 | 5 | 241–245 | 232–236 |
| B | 162 | NR1L-PowerManagement-153 | 4 | 248–251 | 239–242 |
| B | 170 | NR1L-PowerManagement-161 | 4 | 259–262 | 250–253 |
| A | 179 | NR1L-PowerManagement-170 | 2 | 271–272 | 262–263 |
| A | 180 | NR1L-PowerManagement-171 | 2 | 273–274 | 264–265 |
| B | 188 | NR1L-PowerManagement-179 | 5 | 282–286 | 273–277 |
| B | 189 | NR1L-PowerManagement-180 | 7 | 287–293 | 278–284 |
| B | 190 | NR1L-PowerManagement-181 | 4 | 294–297 | 285–288 |
| B | 194 | NR1L-PowerManagement-185 | 7 | 301–307 | 292–298 |
| B | 197 | NR1L-PowerManagement-188 | 4 | 310–313 | 301–304 |
| B | 204 | NR1L-PowerManagement-195 | 4 | 320–323 | 311–314 |
| B | 285 | NR1L-PowerManagement-275 | 5 | 404–408 | 394–398 |

## 面向數差異清單（B 型 30 列）

| row | PROC 步數 | ER 行數 | setup | setup 判定依據 | 實測面向數 | 預核表 | 差 |
|---|---|---|---|---|---|---|---|
| 10 | 5 | 5 | 1 | `powersts` | 4 | 5 | -1 |
| 17 | 5 | 5 | 2 | `powersts` | 3 | 5 | -2 |
| 21 | 6 | 6 | 1 | `powersts` | 5 | 6 | -1 |
| 24 | 7 | 7 | 1 | `powersts` | 6 | 7 | -1 |
| 26 | 7 | 7 | 1 | `powersts` | 6 | 7 | -1 |
| 28 | 5 | 5 | 2 | `powersts` | 3 | 5 | -2 |
| 29 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |
| 30 | 7 | 7 | 2 | `powersts` | 5 | 7 | -2 |
| 32 | 5 | 5 | 1 | `lead-verb+repair` | 4 | 5 | -1 |
| 39 | 5 | 5 | 1 | `lead-verb` | 4 | 5 | -1 |
| 45 | 7 | 7 | 1 | `powersts` | 6 | 7 | -1 |
| 97 | 5 | 5 | 1 | `first-step+repair` | 4 | 5 | -1 |
| 102 | 5 | 5 | 1 | `first-step+repair` | 4 | 5 | -1 |
| 109 | 5 | 5 | 3 | `powersts` | 2 | 5 | -3 |
| 124 | 8 | 8 | 2 | `powersts` | 6 | 8 | -2 |
| 125 | 8 | 8 | 2 | `powersts` | 6 | 8 | -2 |
| 126 | 8 | 8 | 2 | `powersts` | 6 | 8 | -2 |
| 127 | 8 | 8 | 2 | `powersts` | 6 | 8 | -2 |
| 157 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |
| 158 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |
| 159 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |
| 162 | 6 | 6 | 2 | `powersts` | 4 | 6 | -2 |
| 170 | 5 | 5 | 1 | `first-step+repair` | 4 | 5 | -1 |
| 188 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |
| 189 | 8 | 8 | 1 | `first-step` | 7 | 8 | -1 |
| 190 | 5 | 5 | 1 | `lead-verb` | 4 | 5 | -1 |
| 194 | 8 | 8 | 1 | `first-step` | 7 | 8 | -1 |
| 197 | 5 | 5 | 1 | `first-step` | 4 | 5 | -1 |
| 204 | 5 | 5 | 1 | `first-step` | 4 | 5 | -1 |
| 285 | 6 | 6 | 1 | `first-step` | 5 | 6 | -1 |

合計：實測 **144**／預核表 184（下放包 §二 寫 186，實為 184，加總誤算）

## ID 重排前後對照（首尾樣本）

| 新 row | 新 No.# | 新 TC ID | 來源原 row | 原 No.# | 原 TC ID |
|---|---|---|---|---|---|
| 10 | 1 | NR1L-PowerManagement-001 | 10 | 1 | NR1L-PowerManagement-001 |
| 11 | 2 | NR1L-PowerManagement-002 | 10 | 1 | NR1L-PowerManagement-001 |
| 12 | 3 | NR1L-PowerManagement-003 | 10 | 1 | NR1L-PowerManagement-001 |
| 13 | 4 | NR1L-PowerManagement-004 | 10 | 1 | NR1L-PowerManagement-001 |
| 14 | 5 | NR1L-PowerManagement-005 | 11 | 2 | NR1L-PowerManagement-002 |
| 15 | 6 | NR1L-PowerManagement-006 | 11 | 2 | NR1L-PowerManagement-002 |
| 349 | 340 | （存根列，不給 ID） | 230 | 221 | None |
| 411 | 402 | NR1L-PowerManagement-401 | 288 | 279 | NR1L-PowerManagement-278 |
| 412 | 403 | NR1L-PowerManagement-402 | 289 | 280 | NR1L-PowerManagement-279 |
| 413 | 404 | NR1L-PowerManagement-403 | 290 | 281 | NR1L-PowerManagement-280 |
| 414 | 405 | NR1L-PowerManagement-404 | 291 | 282 | NR1L-PowerManagement-281 |
| 415 | 406 | NR1L-PowerManagement-405 | 292 | 283 | NR1L-PowerManagement-282 |
| 416 | 407 | NR1L-PowerManagement-406 | 293 | 284 | NR1L-PowerManagement-283 |

## 七、括號下半消歧（46 列）

§四 要求「任兩同源面向列不得逐字相同」，lint I-sibling 之同源判準為
**同一 Requirement ID**。依 §二 規則 2 組出之括號，46 列在同 Requirement ID
內逐字相同（rows 124–127 同屬 `SWE-PM-041`／`SWE-PM-042`；157–159 同屬
`SWE-PM-057`；188／189／190／194／197 同屬 `SWE-PM-073`）。

消歧候選依序試，取第一個能解開該組者，文字全取自原列、以原列既有之 `—`
分隔形態接前綴：

1. 該列 setup 首步（= PROC 第 1 步）—— 解開 124–127
2. 該列 PRE 中未被同組全體共有之首行 —— 解開 157–159
   （`PROXI Switch_Off_Time = 20／60／180 minutes`）與 189／194
   （`the TLM is in BODY ON mode` ／ `the TLM is in BODY OFF-TIMED mode`）

殘餘碰撞 0 組；未拆之原列括號零變動（0 列被動改寫）。
消歧僅施於碰撞列，故同一原列之面向列中，部分帶前綴、部分不帶
（如新 rows 231–235）；形態不齊但合 §四，未擴大施作。

`超過 20 詞時取 ER 行之核心子句`依 §二 規則 2 實作為：整句逾 20 詞時
括號僅留該面向之 ER 行（去編號）。

## 八、逾越下放包字面之處（三項，皆已於上文標明）

1. `No.#`（B 欄）一併重編 —— 逾越 §三「僅重寫 ID 欄，他欄不動」。**Pei 本包裁定。**
2. 面向列除四欄外，其餘各欄（含 `Test Group`／`Input Test Data`／
   `Test Case Reference ID`／`Functional Safety`／`Test Case Author`）自錨列
   逐字複製。§二 規則 4 只列了五欄（Requirement ID／Test Set／
   spec_reference／Priority／Design Method）；只寫五欄會令插入列其餘各欄留空。
   已驗：未拆原列非 ID 欄零變動。
3. A 型 179／180 括號保留原列之區分前綴（§四 之要求，見 §四 末段）。

## 九、本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

### 1. 17 列面向列無觀察步（規則 2 之殘餘缺陷，最重）

規則 2 把 setup 段之後**每一步**當面向，不分驅動步與觀察步。中段之驅動步
自成一列時，該列 PROC 為「setup + 一個驅動步」、無任何讀取／檢查，
**該列驗不到任何東西**。實測 17／144 列：

| 原 row → 新 row | 該面向之步驟 |
|---|---|
| 21 → 34 | Wait until Timeout1 has elapsed |
| 97 → 145 | Set Rear_Camera_Enable.Info to True |
| 109 → 162 | Place a further bluetooth call while Timeout1 is still running |
| 157 → 232／234 | Select SwitchOff_Timeout_Setting.Req = 00 min／20 min |
| 158 → 237／239 | Select SwitchOff_Timeout_Setting.Req = 00 min／60 min |
| 159 → 242／244 | Select SwitchOff_Timeout_Setting.Req = 00 min／180 min |
| 162 → 249 | Let the boot of the TLM end |
| 170 → 260 | End that call and receive an incoming bluetooth call |
| 188 → 285 | Keep the broadcast stopped to the end of the ignition key cycle |
| 189 → 288 | Send the signal `$STATUS_LIN.Batt_ST_Crit$` = 1 (True) |
| 194 → 302 | 同上 |
| 197 → 311 | 同上 |
| 285 → 405／407 | Run the head unit through the following 29／thirty-first ignition cycles |

lint 抓不到（ER 行數相符、E=0），故不會自己浮出來。正解應為「驅動步併入其
後之觀察步」，但這會再改一次面向數（17 列面向數各減，全本再少 17 列至 390）。
**未擅改**：面向數已由 Pei 本包裁定為規則 2，再動一次須另裁。

### 2. 144 列之語意正確性未經人讀複核

本包只驗了規則層（逐字複製、編號相等、括號可分、lint）。「該面向是否確為一個
獨立觀察點」屬語意判斷，144 列未逐列人讀。24 包 §「B 型（30 列）」原本要求
「面向定義須**逐列設計**」，本包實際以單一演算法統一產出 —— 這正是 §九-1
那類缺陷得以成批進入的路徑。

### 3. 全本 407 列未經 Excel 實開目視

x14 讀回、zip 成員、DV 計數、插入列樣式（列高／框線／自動換行）皆以程式驗過，
但 407 列之版面（含列高 112／126／168 混用之錨列所複製出的插入列）未在
Excel 中實開確認。R9／R10（版面與空白）之報告基線在本包未重跑。

### 4. `Test Case Reference ID`（O 欄）全為 `NEW`，未區分新舊

123 列新插入列之 O 欄自錨列複製為 `NEW`，與原列同值。若 TestRail 側以此欄
判別新增／既有，406 個重排後之 ID 與 TestRail 既有映射之對應關係本包未處理，
亦非本包範圍 —— 但 §三 之全本 ID 重排已使舊 ID 全數失效，
**下游映射修復尚無任何一包承擔**。

## 十、後續

下放包 §「本包後續」之內容三項（TLM→HU 統一、內部變數行為化、
Front_Panel_OnOff）依約於本包覆核通過後另包執行。建議該包之前先裁定
§九-1（17 列無觀察步）與 §四-2（179b／180b PRE 互斥）。

## 十一、產物

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b25/pm_25.xlsx` | 輸出工作副本，407 資料列 |
| `features/power/scripts/b25/build.py` | 分析層：A／B 型拆分內容 → `plan.json` |
| `features/power/scripts/b25/plan.json` | 35 原列 × 158 面向列之四欄內容、面向數稽核 |
| `features/power/scripts/b25/apply.py` | 執行層：插列 → 四欄寫入 → 全本重排 |
| `features/power/scripts/b25/verify.py` | §四 驗收，13 項逐項覆核，不達成即 exit 1 |
| `backend/xlsx_surgical.py` | 新增 `surgical_insert_rows` 等 |
| `tests/test_xlsx_surgical_insert.py` | 插列路徑 9 項測試 |
