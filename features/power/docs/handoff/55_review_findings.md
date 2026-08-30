# PM 站③ 分析層審閱 — 可驗證性缺陷盤點（55 包附件）

- 對象：`FM-WI-FSM-036-A01_…_PowerManagement_20260824.xlsx`，`Test Case Specification&Result` 分頁，390 資料列
- 基線：與 `delivered/pm_29.xlsx`（SHA `35305835…`）五欄逐字一致，390 資料列（tc_id 至 `-389`）；本檔 = pm_29
- 方法：全 390 列逐欄機器掃描 + 人工抽讀 25 列；下列列號 = 工作簿 `No.#`
- 性質：分析層盤點；裁定見 §4 與 `55_verifiability.md` §A。**列號須依 55 包 §0 / B1 於現行 corpus 重量後方可施作。**

---

## 0. 總判

Pei 的直覺成立，且不是零星問題，是**結構性**的：390 列中 290 列（74%）的驗證步驟目標不是可觀察量。
根因單一：`Read the <X> and check that it is <Y>` 被當萬用模板，把規格名詞（functionality、state、reaction、behavior）直接填進 `<X>`，形式上像步驟，實際上把判斷推回給測試員（IN §5.1 禁止之 defer judgement，只是換了動詞）。

不逐列手修。先立配方（§3），再機器改寫，估計觸及 300+ 列。

---

## 1. 缺陷家族（依嚴重度）

### A. 假可觀察目標 — 290 列 ★最嚴重
`Read the <非訊號名詞> and check that …`，`<X>` 不是 `$Signal$`、不是具名 UI 元件、不是可量測之音訊/log。

代表：
- #2 `Read the AMP functionality and check that it is available` → ER `The AMP functionality is available`
- #31/#38/#167… `Read the HU functionality and check that it is not available`（38 列同型，A1）
- #83 `Read the HU functionality state and check that the functionalities run in background`
- #247–249 `Read the HU reaction and check that it is the reaction defined for a phone call becoming active`
- #296/#300 `Read the HU behavior and check that a radio reset is performed / no reset occurs`
- #298/#299 `Read the main CPU / CAN micro and check that it resets`
- #30/#37/#166… `Read the network state and check that the network is on/off`
- #339 `Read the screen sequence and check that …`

為何不可驗證：`functionality`、`reaction`、`behavior`、`network state` 無定義之觀察點；兩位測試員可得相反判定。ER 與步驟互為同義反覆，未增加任何判準。

修正：R-P353 白名單四類；「functionality available」拆為該功能之具體可觀察代理量（須引錨點）。

### B. 前置狀態無建立配方 — 226 列
`The HU is in <State> state` 作為 Pre-Condition，但全案無任何一處定義「如何把 HU 帶到該狀態」。PM 的狀態本身就是受測對象，進入路徑非自明。

並有 15 種拼法：`Full-Operation` / `FULL OPERATION`、`Idle` / `IDLE`、`Partial_Operation` / `Partial Operation`、`an operative state`（25 列，未指明哪一態）、`a … state`（3 列）、`BODY ON` / `BODY OFF-TIMED`（車輛模式，非 HU 態）。

修正：R-P354 `ENTER_<STATE>` 標準片段表。

### C. 不可執行之動作 — 三型

**C1. 抽象動詞（69 列）**：`Bring the HU to Timed mode`、`Let the HU enter Standby`、`Attempt an HMI interaction that does not change the HU status`、`Issue a Network Sleep request`、`Let the bench place an incoming phone call`、`Apply a manual time adjustment`。
- #15/#20/#83 `Attempt an HMI interaction … and check that it is rejected`：哪個互動？rejected 如何呈現？
- #44–46 `Bring the HU to the Bench state`：#45 前置寫 `Engineering Line is activated`，同樣無方法
- #365–390 整段 Startup Display 以 `Bring the HU to Timed/Full-Operation mode` 開頭（26 列）

**C2. 內部訊號直接 Set（40 列）**：`Set Antitheft_Result.Info to Not_Successfully`、`Set Phone_Call.Info to Not_Active`。`.Info` 為 HU 內部變數，測試台無法直接寫入。

**C3. 內部訊號作前置（66 列）**：`Phone_Call.Info is Active`、`Antitheft_Activation.Req is True`、`RemStartFail is True`。

修正：C1 → R-P354(f)；C2/C3 → R-P355（DR-PW23 擴大）。

### D. 規格語言洩漏 — 25 列
`a proper Splash Screen`（#132–146、#192–195）、`the proper HMI Antitheft screens`（#196–210）、`as defined per HMI`（#330–332）、`as defined`（#335）、`normal maximum` / `normal Brand based animation` / `normal power down sequence`（#165、#274–285、#346）。
「proper」「as defined」是 CFTS 原文措辭，ER 直接沿用即無判準。修正：R-P353 末段。

### E. 步驟控制狀態誤入 Pre-Condition — 16 列
`The previous internal state was Full-Operation`（#120–123）、`held a known value before the disconnection`（#58–61）、`The boot of the HU is not ended`（#230–232）、`The disclaimer screen has not yet been shown`（#250、#389）、`The HU has already played the startup sound that day`（#350–352）。
修正：R-P358(b)。

### F. 重複 TC — 12 對
(126,129) (212,354) (213,355) (214,356) (215,357) (216,358) (217,359) (218,347) (250,389) (255,390) (305,320) (306,321)
四欄（Test Item / Pre / Procedure / ER）逐字相同。修正：R-P357 —— 同 Req ID 刪後者；SWRA ID 不同者二列皆留，不得合併。

### G. HU mode 以非訊號方式讀取 — 15 列
#21、#57、#68、#125、#250–254、#290–292、#294–295、#389 用 `Read the HU mode and check that it is FULL OPERATION`，全案其他列均用 `$STATUS_TELEMATIC.PowerSts_Telematic$ = n`。修正：R-P353。

### H. Specification Reference 過寬 — 100 列
#1–43、#52–67 每列引 6–11 個 ObjectID，整段共用同組（#1–14 全引 4941354/4941355/4941357/4941358/4941360/4941453）。追溯性被稀釋。修正：R-P356。

### I. PENDING 未結 — 15 列
#56、#84、#85、#92、#110、#111、#148–150、#154、#156、#159、#161、#340、#388。既知（DR-PW23 等），S6 規定含 PENDING 不得出貨。

### J. 零星
- #325：Test Item 缺括號下半，Procedure 僅 1 步
- #9–11：前置同時列 SDCARD / BT / 通話中，各列只測其一；#9 測 SDCARD 時通話中會搶音源，FF 風險
- #80：前置 `equipped with AMP/ICS/DTV`，Test Item 說 AMP/ICS/DTV shall be OFF，Procedure 只讀 ANC，OFF 從未驗證
- #10：`Select BT Music streaming as the audio active source` 未給 UI 路徑
- `LIN and CAN tool is available on HU`（380+ 列）→ Pei 裁保留（R-P358(a)）

---

## 2. 家族 × 列號（附錄，量自 pm_29）

| 家族 | 列數 | 列號 |
|---|---|---|
| A | 290 | 1–4, 9–14, 16–19, 21–24, 27–35, 37–42, 44–51, 57–59, 63–65, 68–70, 77–83, 89, 91, 97–98, 101–104, 108, 112, 115–116, 119–120, 124–125, 132–135, 140, 142, 146, 150–152, 157, 160, 164–201, 207, 210–219, 222, 225, 229–230, 232–236, 240–241, 243–305, 307–320, 322–324, 326–390 |
| A1 | 38 | 2–4, 13, 22–24, 31–35, 38–42, 167–171, 173–177, 179–183, 185–189, 364 |
| B | 226 | 1–15, 19–35, 37–42, 47–51, 58–67, 77–84, 92–123, 125, 134–140, 148–160, 164, 166–197, 200–201, 207, 210, 219–227, 229–255, 266–271, 278–284, 287–289, 293–295, 328–333, 337, 339, 360–369, 389–390 |
| C1 | 69 | 15, 20, 36, 43–46, 63–66, 72, 83, 85, 132–133, 165, 208, 229–232, 250–255, 290–292, 304, 338–339, 341–346, 348–353, 365–379, 383–390 |
| C2 | 40 | 87, 124–131, 134–136, 141–147, 149–151, 153, 158, 162–163, 196–205, 207, 209–210, 245 |
| C3 | 66 | 36, 43, 58–61, 85–88, 90, 92–96, 101–104, 112–121, 123–126, 129, 141–147, 150, 152–160, 196–203, 207, 209–210, 243–245 |
| D | 25 | 132–133, 140, 142, 146, 165, 192–197, 200–201, 207, 210, 259, 274, 276, 285, 330–332, 335, 346 |
| E | 16 | 58–61, 120, 122–123, 230–232, 246, 250, 350–352, 389 |
| G | 15 | 21, 57, 68, 125, 250–254, 290–292, 294–295, 389 |
| H | 100 | 1–43, 52–67, 84–92, 101–104, 112–119, 150–160, 219–227 |
| I | 15 | 56, 84–85, 92, 110–111, 148–150, 154, 156, 159, 161, 340, 388 |

---

## 3. 處置（已入 55 包 §A / §B）

1. 可觀察目標白名單 + 代理量表（R-P353）— 治 A/A1/D/G
2. `ENTER_<STATE>` 片段表（R-P354）— 治 B/C1
3. DR-PW23 擴大為內部訊號總表（R-P355）— 治 C2/C3/I
4. Spec ref 收斂（R-P356）— 治 H
5. 重複對去留（R-P357）— 治 F
6. 步驟控制狀態移出、零星項（R-P358）— 治 E/J

執行順序：基底確認 → 2 → 1 → 3 → 4 → 5/6 → 機器改寫 → 站④。

---

## 4. Pei 裁定（2026-08-30，逐字「都裁 1. 是 2. 可 3.但只要SWRA ID不同就不可以合併 4.不用 5.允許」）

1. 配方先行 → 採（R-P352）
2. `ENTER_<STATE>` 得併用 SYS1 → 採（R-P354(b)）
3. 重複對：同 Req ID 刪後者；**SWRA ID 不同者不得合併** → R-P357
4. `LIN and CAN tool …` **保留** → R-P358(a)
5. 代理量由分析／執行層指定 → 採，須引錨點（R-P353）
