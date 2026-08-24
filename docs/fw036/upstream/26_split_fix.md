# 上繳 26 包：拆分缺陷修正

基底 `features/power/sandbox/b19/pm_19.xlsx`（sha256 `b4dd5ca0…`）。
輸出 `features/power/sandbox/b26/pm_26.xlsx`（sha256 `0181f6de…`），
390 資料列，止於工作副本，交付本未動。

## 摘要

| 項 | §四 要求 | 實測 | 狀態 |
|---|---|---|---|
| 全本資料列 | 390 | **390** | 達成 |
| B 型面向列 | 127（144 − 17） | **127** | 達成 |
| 縮併列數 | 17 | **17**，清單與 25 包 §九-1 逐項相符 | 達成 |
| Test Case ID | 001–389 + 存根列 | **001–389**，存根列 row 334 略過 | 達成 |
| 無觀察步之列 | 0（v2 全表重掃） | **0** | 達成 |
| `proc↔er` 編號數 | E=0 | E=0 | 達成 |
| lint A–N | 全零 | 全零（含 I-sibling=0） | 達成 |
| 括號消歧殘餘碰撞 | 0 | **0**（消歧 40 列） | 達成 |
| x14 讀回 | 前後相等 | 1 → 1（`R10:R221` → `R10:R325`） | 達成 |
| 止於工作副本 | 是 | 是 | 達成 |
| 與 25 包逐格等價 | —（本包自加） | **達成**，硬閘門 | 達成 |

`verify.py` 共 18 項逐項覆核，全項達成；任一項不達成即 exit 1。

### lint 前後（`--profile power`）

| | A–N（含 I-sibling） | P | Q | R | T | U |
|---|---|---|---|---|---|---|
| 25 包 `pm_25`（本包之前態） | 全 0 | 10 | 0 | 0 | 0 | 10 |
| 26 包 `pm_26` | 全 0 | 10 | 0 | 0 | 0 | 10 |

P=10／U=10 為 21 包起之未校準既有值，本包未動。
報告：`docs/fw036/lint_reports/pm_26__power_20260824.md`。

## 一、覆核判定與分析層錯誤清單：全部接受

§「分析層錯誤清單」三筆（面向數表與規則 2 不可調和、表合計 186 實為 184、
283 為有 TC ID 之列數而資料列實為 284）與規則 1 末步邊界修補之追認，
與 25 包上繳所載一致，無補充。

§一 之「須 Pei 追認」：Pei 交付本下放包並指示執行，視為追認，據以執行。

## 二、基底：實取 b19 而非 §四 所寫之 `pm_25.xlsx`（逾越，已設硬閘門）

§四 定基底為 `sandbox/b25/pm_25.xlsx`。縮併 17 列須**刪列**，而
`backend/xlsx_surgical.py` 只有 25 包新增之插列段（`surgical_insert_rows`），
**無刪列段**。兩條路：

1. 為此包新造一個刪列工具 —— 只此一用，且刪列同樣要搬移列位參照，
   風險與插列同級而無第二個使用者。
2. 以修正後之規則 2 v2 自 b19 重出（插 106 列而非 25 包之 123 列），
   再逐格證明結果等於「pm_25 縮併 17 列 + 4 列 PRE 修正 + ID／No.# 重排」。

取 2。等價性不是口頭聲明，是 `verify.py` 的硬閘門，逐格比對四類：

- **未縮併列之 `test_item` 與各承載欄**（`A C D E G H K N O P Q R S`）
  與 pm_25 逐字相同 —— 括號取該面向之**觀察步**（= 面向末步），
  故未縮併之面向其括號與 25 包相同，這是等價性得以成立之所繫
- **PRE** 逐字相同，僅 179b／180b 四列得異動（§三）
- **縮併列之 PROC／ER** = 被刪列與存留列之 setup 後步驟序列**串接**
  （不得有任何新增或改寫文字）
- **被刪列恰 17 列**，且每一列之末步皆為驅動步（無觀察）

四項全數達成，例外 0。被刪之 25 包 row：
`34, 145, 162, 232, 234, 237, 239, 242, 244, 249, 260, 285, 288, 302, 311, 405, 407`
—— 與 25 包上繳 §九-1 之 17 列表逐項相符。

因此本包寫出仍為既有二段一路（`surgical_insert_rows` → `surgical_save`），
未新造工具，`openpyxl.save` 全程未用，zip 成員 42 未變、差異僅
`xl/worksheets/sheet6.xml`。

## 三、§二 179b／180b PRE 修正

依 §二 逐字執行：PRE 第 1 行換為
`The HU is in FULL OPERATION mode due to an active incoming phone call`，
並**不再**增 `An incoming phone call is active on the HU` 一行
（狀態行已含通話前提）。顯示前提行與工具行不動。

| 26 包 row | TC ID | PRE |
|---|---|---|
| 260 | -251 | `1. The HU is in IDLE mode` / `2. The display is on the phone main screen` / `3. LIN and CAN tool…` |
| 261 | -252 | `1. The HU is in FULL OPERATION mode due to an active incoming phone call` / `2. The display is on the phone main screen` / `3. LIN and CAN tool…` |
| 262 | -253 | `1. The HU is in IDLE mode` / `2. The display is on the phone projection call UI` / `3. LIN and CAN tool…` |
| 263 | -254 | `1. The HU is in FULL OPERATION mode due to an active incoming phone call` / `2. The display is on the phone projection call UI` / `3. LIN and CAN tool…` |

a 列（IDLE 起、來電 → FULL OPERATION）與 b 列（FULL OPERATION 起、
掛斷 → IDLE）之狀態前提現已互不矛盾。

## 四、規則 2 v2 之觀察判準：切分用句首錨定，重掃用放寬判準

§一 定觀察步為「`Read`／`Check that` **起首**」。以此對 30 列切分，
實測**無**任何後設步既非驅動亦非觀察（`build.py` 對此中止，未觸發），
30 列亦無「非 `Read` 起首但含 `check that`」之步 —— 切分不受影響。

但 §四 之「全表重掃」若沿用句首錨定，會誤報兩列**既有未拆列**：

| 26 包 row | TC ID | PROC 首步 |
|---|---|---|
| 24 | -015 | `Attempt a user setting on the TLM and check that it is rejected` |
| 29 | -020 | `Attempt an HMI interaction that does not change the TLM status and check that it is rejected` |

此二列之觀察在句中而非句首，是**有效驗證列**，非本包造成。故重掃判準
放寬為「`Read` 起首**或**句中含 `check that`」。以放寬判準重掃：
b19 全本 284 列 0 例外、pm_26 全本 390 列 0 例外。兩套判準之分工與
理由已寫入 `verify.py` 註解。

## 五、逐列對照表

## §一 17 列縮併對照

| b19 原 row | 被刪之 25 包 row | 該列驅動步 | 併入之 26 包 row | 併入後之觀察步 |
|---|---|---|---|---|
| 21 | 34 | Wait until Timeout1 has elapsed | 34 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is no longer 2 (Timed) |
| 97 | 145 | Set Rear_Camera_Enable.Info to True | 144 | Read the TLM screen and check that the rear view camera images are shown |
| 109 | 162 | Place a further bluetooth call while Timeout1 is still running | 160 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is still 2 (Timed) |
| 157 | 232 | Select SwitchOff_Timeout_Setting.Req = 00 min | 229 | Read Timeout1 and check that it is 00 min |
| 157 | 234 | Select SwitchOff_Timeout_Setting.Req = 20 min | 230 | Read Timeout1 and check that it is 20 minutes |
| 158 | 237 | Select SwitchOff_Timeout_Setting.Req = 00 min | 232 | Read Timeout1 and check that it is 00 min |
| 158 | 239 | Select SwitchOff_Timeout_Setting.Req = 60 min | 233 | Read Timeout1 and check that it is 60 minutes |
| 159 | 242 | Select SwitchOff_Timeout_Setting.Req = 00 min | 235 | Read Timeout1 and check that it is 00 min |
| 159 | 244 | Select SwitchOff_Timeout_Setting.Req = 180 min | 236 | Read Timeout1 and check that it is 180 minutes |
| 162 | 249 | Let the boot of the TLM end | 240 | Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep) |
| 170 | 260 | End that call and receive an incoming bluetooth call | 250 | Read the call audio routing and check that the incoming call is presented and can be answered |
| 188 | 285 | Keep the broadcast stopped to the end of the ignition key cycle | 274 | Read AUD_LVL and check that the maximum volume is still reduced to 20 at the end of the ignition key cycle |
| 189 | 288 | Send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) | 276 | Read the TLM display and check that it stays on |
| 194 | 302 | Send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) | 289 | Read the TLM display and check that it stays on |
| 197 | 311 | Send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) | 297 | Read the CAN trace and check that no AUD_LVL signal carrying a new volume level appears |
| 285 | 405 | Run the head unit through the following 29 ignition cycles | 390 | Read the HU screen on each of those cycles and check that the core disclaimer screen is not shown |
| 285 | 407 | Run the head unit through the thirty-first ignition cycle | 391 | Read the HU screen and check that the core disclaimer screen is shown again |

合計 **17** 列，與 25 包上繳 §九-1 之清單逐項相符。

## 面向數 v1 → v2（B 型 30 列）

| row | PROC 步數 | setup | v1 面向 | v2 面向 | 縮併 |
|---|---|---|---|---|---|
| 10 | 5 | 1 | 4 | 4 | 0 |
| 17 | 5 | 2 | 3 | 3 | 0 |
| 21 | 6 | 1 | 5 | 4 | **1** |
| 24 | 7 | 1 | 6 | 6 | 0 |
| 26 | 7 | 1 | 6 | 6 | 0 |
| 28 | 5 | 2 | 3 | 3 | 0 |
| 29 | 6 | 1 | 5 | 5 | 0 |
| 30 | 7 | 2 | 5 | 5 | 0 |
| 32 | 5 | 1 | 4 | 4 | 0 |
| 39 | 5 | 1 | 4 | 4 | 0 |
| 45 | 7 | 1 | 6 | 6 | 0 |
| 97 | 5 | 1 | 4 | 3 | **1** |
| 102 | 5 | 1 | 4 | 4 | 0 |
| 109 | 5 | 3 | 2 | 1 | **1** |
| 124 | 8 | 2 | 6 | 6 | 0 |
| 125 | 8 | 2 | 6 | 6 | 0 |
| 126 | 8 | 2 | 6 | 6 | 0 |
| 127 | 8 | 2 | 6 | 6 | 0 |
| 157 | 6 | 1 | 5 | 3 | **2** |
| 158 | 6 | 1 | 5 | 3 | **2** |
| 159 | 6 | 1 | 5 | 3 | **2** |
| 162 | 6 | 2 | 4 | 3 | **1** |
| 170 | 5 | 1 | 4 | 3 | **1** |
| 188 | 6 | 1 | 5 | 4 | **1** |
| 189 | 8 | 1 | 7 | 6 | **1** |
| 190 | 5 | 1 | 4 | 4 | 0 |
| 194 | 8 | 1 | 7 | 6 | **1** |
| 197 | 5 | 1 | 4 | 3 | **1** |
| 204 | 5 | 1 | 4 | 4 | 0 |
| 285 | 6 | 1 | 5 | 3 | **2** |

合計：v1 144 → v2 **127**，縮併 17。

## 插列對照表（26 包）

| 型 | b19 原 row | 面向數 | 26 包 rows | 新 TC ID 起訖 |
|---|---|---|---|---|
| B | 10 | 4 | 10–13 | 001–004 |
| A | 11 | 4 | 14–17 | 005–008 |
| A | 12 | 3 | 18–20 | 009–011 |
| B | 17 | 3 | 25–27 | 016–018 |
| B | 21 | 4 | 31–34 | 022–025 |
| A | 23 | 3 | 36–38 | 027–029 |
| B | 24 | 6 | 39–44 | 030–035 |
| B | 26 | 6 | 46–51 | 037–042 |
| B | 28 | 3 | 53–55 | 044–046 |
| B | 29 | 5 | 56–60 | 047–051 |
| B | 30 | 5 | 61–65 | 052–056 |
| B | 32 | 4 | 67–70 | 058–061 |
| B | 39 | 4 | 77–80 | 068–071 |
| B | 45 | 6 | 86–91 | 077–082 |
| B | 97 | 3 | 143–145 | 134–136 |
| B | 102 | 4 | 150–153 | 141–144 |
| B | 109 | 1 | 160–160 | 151–151 |
| B | 124 | 6 | 175–180 | 166–171 |
| B | 125 | 6 | 181–186 | 172–177 |
| B | 126 | 6 | 187–192 | 178–183 |
| B | 127 | 6 | 193–198 | 184–189 |
| B | 157 | 3 | 228–230 | 219–221 |
| B | 158 | 3 | 231–233 | 222–224 |
| B | 159 | 3 | 234–236 | 225–227 |
| B | 162 | 3 | 239–241 | 230–232 |
| B | 170 | 3 | 249–251 | 240–242 |
| A | 179 | 2 | 260–261 | 251–252 |
| A | 180 | 2 | 262–263 | 253–254 |
| B | 188 | 4 | 271–274 | 262–265 |
| B | 189 | 6 | 275–280 | 266–271 |
| B | 190 | 4 | 281–284 | 272–275 |
| B | 194 | 6 | 288–293 | 279–284 |
| B | 197 | 3 | 296–298 | 287–289 |
| B | 204 | 4 | 305–308 | 296–299 |
| B | 285 | 3 | 389–391 | 379–381 |

## ID 重排前後對照（首尾樣本，含 25 包對照）

| 26 包 row | No.# | 26 包 TC ID | 25 包 TC ID | b19 原 TC ID |
|---|---|---|---|---|
| 10 | 1 | NR1L-PowerManagement-001 | NR1L-PowerManagement-001 | NR1L-PowerManagement-001 |
| 11 | 2 | NR1L-PowerManagement-002 | NR1L-PowerManagement-002 | NR1L-PowerManagement-001 |
| 12 | 3 | NR1L-PowerManagement-003 | NR1L-PowerManagement-003 | NR1L-PowerManagement-001 |
| 13 | 4 | NR1L-PowerManagement-004 | NR1L-PowerManagement-004 | NR1L-PowerManagement-001 |
| 14 | 5 | NR1L-PowerManagement-005 | NR1L-PowerManagement-005 | NR1L-PowerManagement-002 |
| 334 | 325 | （存根列） | None | None |
| 386 | 377 | NR1L-PowerManagement-376 | NR1L-PowerManagement-391 | NR1L-PowerManagement-272 |
| 387 | 378 | NR1L-PowerManagement-377 | NR1L-PowerManagement-392 | NR1L-PowerManagement-273 |
| 388 | 379 | NR1L-PowerManagement-378 | NR1L-PowerManagement-393 | NR1L-PowerManagement-274 |
| 389 | 380 | NR1L-PowerManagement-379 | NR1L-PowerManagement-394 | NR1L-PowerManagement-275 |
| 390 | 381 | NR1L-PowerManagement-380 | NR1L-PowerManagement-396 | NR1L-PowerManagement-275 |

## 六、括號消歧

沿用 25 包之兩段候選（setup 首步 → 具區分性之 PRE 行），未動規則。
碰撞列由 25 包之 46 列降為 **40 列**（6 列落在被刪之 17 列內），
殘餘碰撞 **0 組**，未拆原列括號零變動。

## 七、逾越下放包字面之處

本包新增二項：

1. **基底取 b19 而非 §四 所寫之 `pm_25.xlsx`** —— 理由與硬閘門見 §二。
2. **§四 全表重掃之觀察判準放寬** —— 理由與實測見 §四。
   切分判準未動，仍為 §一 之句首錨定。

沿用 25 包已上繳之三項（`No.#` 一併重編、面向列除四欄外其餘各欄自錨列
逐字複製、A 型 179／180 括號保留原列之區分前綴），未擴大。

## 八、本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。前二項為本包新發現。**

### 1. row 109 實為「未拆」，但其括號仍被面向規則改寫（資訊淨損）

v2 下 row 109 之面向數為 **1**（setup=3 已含兩個觀察步，其後僅一個觀察步），
插 0 列，PROC／ER 與 b19 原列**逐字相同** —— 等於沒拆。但 `test_item`
之括號下半仍照面向規則重寫：

| | 括號下半 |
|---|---|
| b19 原列 | `(read the active source and the TLM state -> The TLM stayed in Timed state throughout and no transition to Standby occurred)` |
| 26 包 row 160 | `(The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received)` |

原括號描述該列**整體**之驗證目的，新括號只是末條 ER 行，範圍更窄。
該列既未拆，改寫是純粹的資訊淨損。

**建議**：面向數為 1 之列不套用面向括號規則，`test_item` 逐字保留原列。
影響 1 列。**未擅改** —— 括號內容屬分析層，且此舉會動到 §二 之等價閘門
（須將該列列為白名單），須裁定後執行。

### 2. 17 列縮併後，括號只述觀察步、不述併入之驅動步

縮併列之 PROC 現為「setup + 驅動步 + 觀察步」，但括號取該面向之觀察步，
**未提及該列的 trigger**。例：

| 26 包 row | PROC 之驅動步 | 括號下半 |
|---|---|---|
| 230 | `Select SwitchOff_Timeout_Setting.Req = 20 min` | `(read Timeout1 and check that it is 20 minutes -> Timeout1 is 20 minutes)` |

本包實測殘餘碰撞 0，故目前無 lint 後果。但這是規則 2 v2 之殘餘弱點：
**若兩面向之觀察步同文而僅驅動步不同，括號必然逐字相同**，屆時只能靠
消歧前綴補救，而括號本身仍未描述該列所驗之情境。17 列全數如此。

**建議**：括號改為 `(<驅動步> — <觀察步> -> <ER>)`，逾 20 詞時退回現行式。
影響 17 列。**未擅改**，同屬分析層。

### 3. §九-2（語意複核）—— 仍未做，且對象已變

26 包 §三 排於內容三項完成後之全本覆核。須注意覆核對象已由 25 包之
407 列變為 **390 列**，且 127 列 B 型面向之 PROC 形態由「setup + 一步」
變為「setup + 驅動步 + 觀察步」—— 面向獨立性之判斷基礎隨之改變，
不可沿用對 407 列的任何既有印象。

### 4. §九-3（Excel 實開）—— 仍未做

插入列數由 123 降為 106，樣式承接路徑（`surgical_insert_rows` 逐列複製
錨列列高與逐格 `s=`）未變，仍未在 Excel 中實開確認 390 列版面。屬 Pei。

### 5. §九-4（TestRail 舊 ID → 新 ID 對照表）—— 仍 **[待 Pei 裁]**，且已更迫切

本包未執行（§四 之四項任務不含此項）。但須指出：**ID 已重排兩次** ——
25 包 001–406、26 包 001–389。兩者皆未寫回，故對外尚無曝露；
但若日後要對照表，**基準必須是 pm_26**，25 包上繳 §六 之對照表已作廢，
不可據以延伸。裁定愈晚，可用的中間態愈少。

## 九、後續

依 26 包 §五：本包通過 → 內容三項包（TLM→HU、行為化、Front_Panel）→
全本人讀覆核（§八-3）→ Pei 實開抽驗 + 授權 → 寫回 `(Revise2)`。

建議內容三項包之前先裁定 §八-1（row 109 括號）與 §八-2（縮併列括號），
兩項皆屬 `test_item`，與內容三項同一欄位，合併一次改動比分兩次省一輪覆核。

## 十、產物

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b26/pm_26.xlsx` | 輸出工作副本，390 資料列，sha256 `0181f6de…` |
| `features/power/scripts/b26/build.py` | 分析層：規則 2 v2 切分 + §二 PRE 修正 → `plan.json` |
| `features/power/scripts/b26/plan.json` | 35 原列 × 141 面向列之四欄內容、v1→v2 面向稽核 |
| `features/power/scripts/b26/apply.py` | 執行層：插 106 列 → 四欄寫入 → 全本重排 |
| `features/power/scripts/b26/verify.py` | §四 驗收 18 項（含與 25 包等價性硬閘門） |
| `docs/fw036/lint_reports/pm_26__power_20260824.md` | lint 後報告 |
