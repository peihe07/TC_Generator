# 上繳 27 包：`test_item` 括號兩案修正

基底 `features/power/sandbox/b26/pm_26.xlsx`（sha256 `0181f6de…`）。
輸出 `features/power/sandbox/b27/pm_27.xlsx`（sha256 `6e7023c7…`），
390 資料列，止於工作副本，客戶目錄未動。

## 摘要

| 項 | 裁定 | 實測 | 狀態 |
|---|---|---|---|
| §八-1 row 109 還原 | 逐字保留原列 | row 160 `test_item` 與 b19 row 109 **逐字同**，除 `No.#`／TC ID 外**全欄**與原列逐字同 | 達成 |
| §八-2 縮併列括號 | 形態 B（驅動步 -> ER） | **16 列**（扣掉 row 109），驅動步與 ER 皆逐字取自原列 | 達成 |
| 20 詞上限 | 縮併列免 | 4 列逾限（274=28、390=25、391=22、276／289／297=21）皆保留完整 trigger | 達成 |
| 相異範圍 | —（本包自加） | 逐格比對 pm_26：**相異僅 I 欄、恰 17 列** | 達成 |
| 列數／ID／No.# | 不變 | 390 列、001–389、1–390，與 pm_26 完全相同 | 達成 |
| lint A–N | 全零 | 全零（含 I-sibling=0） | 達成 |
| x14 讀回 | 前後相等 | `R10:R325` → `R10:R325`，zip 42 未變 | 達成 |

`verify.py` 共 13 項，全項達成；任一項不達成即 exit 1。

### lint 前後（`--profile power`）

| | A–N（含 I-sibling） | P | Q | R | T | U |
|---|---|---|---|---|---|---|
| 26 包 `pm_26` | 全 0 | 10 | 0 | 0 | 0 | 10 |
| 27 包 `pm_27` | 全 0 | 10 | 0 | 0 | 0 | 10 |

報告：`docs/fw036/lint_reports/pm_27__power_20260824.md`。

## 一、寫入路徑：本包不動列數，`surgical_save` 單段

面向切分（規則 1＋規則 2 v2）、setup 判定、消歧兩段候選一律沿 26 包未動，
插列數仍 106、全本仍 390 列、Test Case ID 仍 001–389。因此**無須插列段**，
基底即取下放所指之 `pm_26.xlsx`（26 包因需刪列而改取 b19，本包無此問題），
寫入範圍限 `test_item`（I）一欄。zip 成員 42 未變、差異成員僅
`xl/worksheets/sheet6.xml`、x14 下拉讀回相等。

## 二、消歧與形態 B 之交互

形態 B 之裸式在 5 列產生同 Requirement ID 碰撞
（`[229, 232, 235]` 為 157／158／159 之 `00 min` 分支；`[276, 289]` 為
189／194 之 BODY ON／BODY OFF-TIMED），皆由**既有**兩段消歧器第 2 段
（具區分性之 PRE 行）自動解開，未新增機制：

| row | 括號 |
|---|---|
| 229 | `(PROXI Switch_Off_Time = 20 minutes — select SwitchOff_Timeout_Setting.Req = 00 min -> Timeout1 is 00 min)` |
| 232 | `(PROXI Switch_Off_Time = 60 minutes — select …)` |
| 235 | `(PROXI Switch_Off_Time = 180 minutes — select …)` |
| 276 | `(the TLM is in BODY ON mode — send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> The TLM display stays on)` |
| 289 | `(the TLM is in BODY OFF-TIMED mode — send …)` |

其餘 11 列為裸形態 B。全本括號碰撞 0 組。
消歧列數與 26 包同為 40 列，**未拆原列與非縮併面向列括號零變動** ——
即本包沒有波及該動範圍以外的任何一格。

## 三、逐列對照

## 17 列括號前後對照

| b19 原 row | row | TC ID | 案 | 詞 |
|---|---|---|---|---|
| 21 | 34 | …-025 | §八-2 形態 B | 15 |
| 97 | 144 | …-135 | §八-2 形態 B | 16 |
| 109 | 160 | …-151 | §八-1 還原 | 22 |
| 157 | 229 | …-220 | §八-2 形態 B | 16 |
| 157 | 230 | …-221 | §八-2 形態 B | 10 |
| 158 | 232 | …-223 | §八-2 形態 B | 16 |
| 158 | 233 | …-224 | §八-2 形態 B | 10 |
| 159 | 235 | …-226 | §八-2 形態 B | 16 |
| 159 | 236 | …-227 | §八-2 形態 B | 10 |
| 162 | 240 | …-231 | §八-2 形態 B | 17 |
| 170 | 250 | …-241 | §八-2 形態 B | 19 |
| 188 | 274 | …-265 | §八-2 形態 B | 28 |
| 189 | 276 | …-267 | §八-2 形態 B | 21 |
| 194 | 289 | …-280 | §八-2 形態 B | 21 |
| 197 | 297 | …-288 | §八-2 形態 B | 21 |
| 285 | 390 | …-380 | §八-2 形態 B | 25 |
| 285 | 391 | …-381 | §八-2 形態 B | 22 |

逐列文字：

**row 34**（b19 21，`…-025`，§八-2）
- 26 包：`(The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ is no longer 2 (Timed))`
- 27 包：`(wait until Timeout1 has elapsed -> The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ is no longer 2 (Timed))`

**row 144**（b19 97，`…-135`，§八-2）
- 26 包：`(The rear view camera images are shown on the TLM screen)`
- 27 包：`(set Rear_Camera_Enable.Info to True -> The rear view camera images are shown on the TLM screen)`

**row 160**（b19 109，`…-151`，§八-1 還原）
- 26 包：`(The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received)`
- 27 包：`(read the active source and the TLM state -> The TLM stayed in Timed state throughout and no transition to Standby occurred)`

**row 229**（b19 157，`…-220`，§八-2）
- 26 包：`(PROXI Switch_Off_Time = 20 minutes — read Timeout1 and check that it is 00 min -> Timeout1 is 00 min)`
- 27 包：`(PROXI Switch_Off_Time = 20 minutes — select SwitchOff_Timeout_Setting.Req = 00 min -> Timeout1 is 00 min)`

**row 230**（b19 157，`…-221`，§八-2）
- 26 包：`(read Timeout1 and check that it is 20 minutes -> Timeout1 is 20 minutes)`
- 27 包：`(select SwitchOff_Timeout_Setting.Req = 20 min -> Timeout1 is 20 minutes)`

**row 232**（b19 158，`…-223`，§八-2）
- 26 包：`(PROXI Switch_Off_Time = 60 minutes — read Timeout1 and check that it is 00 min -> Timeout1 is 00 min)`
- 27 包：`(PROXI Switch_Off_Time = 60 minutes — select SwitchOff_Timeout_Setting.Req = 00 min -> Timeout1 is 00 min)`

**row 233**（b19 158，`…-224`，§八-2）
- 26 包：`(read Timeout1 and check that it is 60 minutes -> Timeout1 is 60 minutes)`
- 27 包：`(select SwitchOff_Timeout_Setting.Req = 60 min -> Timeout1 is 60 minutes)`

**row 235**（b19 159，`…-226`，§八-2）
- 26 包：`(PROXI Switch_Off_Time = 180 minutes — read Timeout1 and check that it is 00 min -> Timeout1 is 00 min)`
- 27 包：`(PROXI Switch_Off_Time = 180 minutes — select SwitchOff_Timeout_Setting.Req = 00 min -> Timeout1 is 00 min)`

**row 236**（b19 159，`…-227`，§八-2）
- 26 包：`(read Timeout1 and check that it is 180 minutes -> Timeout1 is 180 minutes)`
- 27 包：`(select SwitchOff_Timeout_Setting.Req = 180 min -> Timeout1 is 180 minutes)`

**row 240**（b19 162，`…-231`，§八-2）
- 26 包：`(The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received)`
- 27 包：`(let the boot of the TLM end -> The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received)`

**row 250**（b19 170，`…-241`，§八-2）
- 26 包：`(The incoming call is presented and can be answered)`
- 27 包：`(end that call and receive an incoming bluetooth call -> The incoming call is presented and can be answered)`

**row 274**（b19 188，`…-265`，§八-2）
- 26 包：`(The Load Shed action is maintained for the rest of the current ignition key cycle)`
- 27 包：`(keep the broadcast stopped to the end of the ignition key cycle -> The Load Shed action is maintained for the rest of the current ignition key cycle)`

**row 276**（b19 189，`…-267`，§八-2）
- 26 包：`(the TLM is in BODY ON mode — read the TLM display and check that it stays on -> The TLM display stays on)`
- 27 包：`(the TLM is in BODY ON mode — send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> The TLM display stays on)`

**row 289**（b19 194，`…-280`，§八-2）
- 26 包：`(the TLM is in BODY OFF-TIMED mode — read the TLM display and check that it stays on -> The TLM display stays on)`
- 27 包：`(the TLM is in BODY OFF-TIMED mode — send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> The TLM display stays on)`

**row 297**（b19 197，`…-288`，§八-2）
- 26 包：`(No AUD_LVL signal carrying a new volume level appears in the CAN trace)`
- 27 包：`(send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> No AUD_LVL signal carrying a new volume level appears in the CAN trace)`

**row 390**（b19 285，`…-380`，§八-2）
- 26 包：`(The core disclaimer screen is not shown on any of those 29 ignition cycles)`
- 27 包：`(run the head unit through the following 29 ignition cycles -> The core disclaimer screen is not shown on any of those 29 ignition cycles)`

**row 391**（b19 285，`…-381`，§八-2）
- 26 包：`(The core disclaimer screen is shown only once every 30 ignition cycles)`
- 27 包：`(run the head unit through the thirty-first ignition cycle -> The core disclaimer screen is shown only once every 30 ignition cycles)`


## 四、本包是否仍有該驗而未驗者 —— 獨立判斷

**有，三項。第 1 項為本包新發現，且比 §八-2 原案大得多。**

### 1. 另有 30 列括號是「純 ER 複述」，不含 trigger 也不含觀察步

§八-2 修的是 16 列縮併列。但 B 型 127 列面向列中，另有 **111 列**為
「觀察步 -> ER」形態，其中 **30 列**因逾 §二 之 20 詞上限而退回
**ER-only**（括號內連 `->` 都沒有，只剩一句 ER 複述）。

現況分布：

| 括號形態 | 列數 |
|---|---|
| §八-2 形態 B（`驅動步 -> ER`） | 16 |
| `觀察步 -> ER` | 81 |
| **ER-only（逾 20 詞退回）** | **30** |
| §八-1 還原（原列逐字） | 1 |

那 30 列的括號與 §八-2 所修的缺陷同類、甚至更重：**既不述 trigger，
也不述觀察動作**，只是把 ER 抄一遍。它們之所以沒在 §八-2 浮出來，
是因為它們不是縮併列 —— 而縮併只發生在 17 列，是抽樣偏差。

這 30 列的 trigger 位在 setup 段（非面向本體），故不能直接套形態 B；
可行的方向是 `(<setup 末步之驅動 或 setup 首步> -> <ER>)`，
或把 20 詞上限一併放寬。**未擅改** —— 這是 §二 括號規則的第三次修正，
且影響 30 列，屬分析層，須裁定。

### 2. 括號形態現為四軌並存

上表即是。§四「任兩同源面向列不得逐字相同」全數達成、lint 全零，
所以這不是缺陷，是**一致性問題**：同一本表的 B 型面向列有四種括號寫法。
若要收斂為單一形態，最省的時機是與第 1 項同包處理。

### 3. 沿舊仍未做者

- **② 內容三項**（TLM→HU、行為化、Front_Panel）—— 未開始
- **③ 390 列人讀覆核** —— 未跑。基準本已由 pm_26 換為 **pm_27**
- **④ Excel 實開抽驗** —— 屬 Pei，未做
- **TestRail 舊 ID → 新 ID 對照表** —— 依前議綁最終寫回同包產出。
  本包未動列數與 ID，故 pm_26 與 pm_27 之 ID 完全相同，
  對照表基準不因本包而變

## 五、產物

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b27/pm_27.xlsx` | 輸出工作副本，390 列，sha256 `6e7023c7…` |
| `features/power/scripts/b27/build.py` | 分析層：§八-1 還原 + §八-2 形態 B → `plan.json` |
| `features/power/scripts/b27/plan.json` | 35 原列 × 141 面向列之四欄內容 |
| `features/power/scripts/b27/apply.py` | 執行層：I 欄 17 列改寫，`surgical_save` 單段 |
| `features/power/scripts/b27/verify.py` | 驗收 13 項（含與 pm_26 之相異範圍逐格比對） |
| `docs/fw036/lint_reports/pm_27__power_20260824.md` | lint 後報告 |
