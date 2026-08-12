# FW036 R1L Projection — Feature Profile

Feature: `Projection` (R-P1) · workbook_state: `FULL_REFINE` ·
spec_mode: `[A, B, D]`

Authority chain per `docs/runtime/profiles/PROFILE_INTEGRATION.md`: the
generic instruction governs unless a clause here carries `[OVERRIDE]` or
`[ADD]`. Every override below names the generic rule it displaces.

**What makes this feature different from every other one in the repo**: it is
not a regeneration. `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` already carries 559
test cases covering 164 of the 171 037 leaves, executed across five builds
with Pass/Fail/Block results recorded. The defect is not empty fields — it is
that the steps cannot be executed as written. CAN items say "send some signal"
without saying how; tool items name a tool without an operating path; some
signal names are SWE1 analysis-layer logical names rather than bus-real names.

---

## 1. `[OVERRIDE]` workbook_state = `FULL_REFINE`

**Displaces**: canon §2, which defines exactly four states —
`BLANK` / `PARTIAL_CLEAN` / `PARTIAL_INTERLEAVED` / `FULL` — and binds `FULL`
to *audit-only mode, no generation*.

This case is `FULL` by every measurable property and yet is not audit-only:
the step text must be rewritten to be executable, and 6–7 uncovered leaves
need new rows. canon has no cell for that combination, so this profile defines
one.

| 面向 | 綁定 |
|---|---|
| 風格權威 | base workbook 自身的 done region |
| 寫回策略 | 原地逐欄改寫，**列數與列序不變** |
| 不變式 | 除 `Pre-Conditions` 與 `Test procedure` 外，所有欄位（含 `Expected Result`、`Test Item`、`Input Test Data`、`Specification Reference`、全部執行結果欄與 BugList）的內容雜湊必須前後相同 |
| 生成範圍 | 僅對未覆蓋的 **7** 條 leaf 補列，**追加於表尾**（R-P14 定案為 7，非 6–7；R-P18 將 leaf 146 排除，實補 6 條） |
| 凍結區 | PCTS 相關列採**證據綁定**：測項未 confirmed 者不動（R-P11 取代 R-P6）；`Not in ASW-R1 Release Scope` 的 4 列無條件不動 |

Consequences that follow from the table and are binding:

1. **The done region is the entire sheet.** There is no author-based or
   row-range selector. All 559 rows are protected. **Three** columns are
   unfrozen: `Pre-Conditions`, `Test procedure`, and — added by R-P19 —
   `Test Case Author` on the 41 rows where it is blank. This is the only
   feature in the repo whose style authority is the file being rewritten —
   the workbook arbitrates its own style disputes.
2. **Row identity is positional.** The write-back invariant is checked
   row-index to row-index; a diff that moves a row is an abort, not a merge.
   **R-P19 opens the one sanctioned exception to "列數與列序不變"**: row 562
   (the `SWE1-PROJ-227` stub) is deleted. Data rows go 559 → 558 and the last
   row goes 562 → 561. Every other row keeps its index. No other deletion is
   authorised.
3. **Coverage is 7 leaves short** — `SWE1-PROJ-133 / 146 / 167-001 /
   167-002 / 184 / 190 / 195`. R-P14 settled the count at 7: the MD version's
   down-listing of 133 does not bind the ruled CPAA source. R-P18 then holds
   `146` back (its whole text delegates to CFTS025, which is not supplied), so
   **6 leaves are actually appended** and 146 stays uncovered.
4. **Appended rows go at the tail** and carry `author = PeiPYHsu`,
   `tc_ref_id = NEW`. They do not renumber anything. Note the tail moves to
   row 561 once R-P19's deletion is applied.
5. **`Estimated Test Time` stays empty on every row** (R-P19). Its 0/559 fill
   rate is convention, not a gap; filling it is a violation, not an
   improvement.

## 2. `[ADD]` O-1 … O-4 — 修訂總則

Reproduced verbatim from DECISIONS §0 (Pei, 2026-08-11). These four clauses
are the operating rules for every rewritten step.

**O-1**　把不明確的步驟寫踏實，不牴觸基本 spec。**Expected Result 不得更改。**

**O-2**　PROXI 配置寫在 **Pre-Conditions**；送 CAN、開工具、讀值、比對等**所有操作一律寫在 Procedure 步驟**。不使用 Input Test Data 承載 PROXI。

**O-3**　工具步驟依 `CarPlay TestApp` / `ATS 8.10.0` 手冊撰寫；無手冊者不得推測。

**O-4**　不得編造測項。**沒有數值就寫成可觀察的結果。**

The governing ruling behind all four, also verbatim (R-P4):

> 所有測試 data 不可更動；只修正字詞使其明確、準確、可落地執行。步驟必須查明實際怎麼操作；需 testapp／工具的也必須確認操作步驟。**SWE1 是分析，數值一律以 CPAA 原始 spec、CFTS、HMI 為準，不可編造。**

### Reading these together

O-1 and O-4 are the two halves of one constraint. O-1 says make the step
concrete; O-4 says do not invent the concreteness. Where a step is vague
because the *source* is vague, the resolution is an observable outcome, not a
guessed number. `$HCP_DISP2.Est_Range_BEV$` is the worked example: three
plausible signals exist, none is confirmed, and R-P9 rules that the step is
written observably with no signal filled.

O-2 places PROXI in Pre-Conditions and every action in Procedure. `Input Test
Data` is neither — it is frozen under §1 and must not be used to carry
configuration that O-2 assigns elsewhere.

O-3 makes tool coverage a function of **documented** coverage, and R-P11
widened what counts as documentation. ATS (10 rows) and CarPlay TestApp
(6 rows) have manuals in `inputs/`. PCTS still has no manual — but on-device
capture now satisfies O-3 for the tests it actually confirms, and only for
those. See §3a.

## 3. `[ADD]` 個別處置 — R-P7 … R-P11, R-P8′

Verbatim from DECISIONS §0 / §0.1, with the lookup result appended to each.
The rulings are binding; the appended findings are evidence, and where they
differ from what the ruling assumed, the ruling still governs.

| ID | 裁決 | 查證 |
|---|---|---|
| ~~**R-P6**~~ | ~~PCTS 相關 23 列**凍結不動**~~ **SUPERSEDED by R-P11 (2026-08-12)** | 23 列已列舉；改為證據綁定，見 §3a |
| **R-P11** | PCTS 相關 23 列的步驟修訂，僅在該測項的操作路徑已由實機取證確認後方得進行；未取得證據之測項，其相關列維持不動。`NR1L-PROJ-374~377` 因環境阻塞即使取證完成仍維持不動 | 取證已執行（2026-08-12）；14 列解鎖、9 列維持 ABORT，見 §3a |
| **R-P7** | `$Screen_Size$` → PROXI `Radio_Display_Type`；Remarks 註明 `only 8.4"` 的 6 列寫為 `Radio_Display_Type = 2` | 雙來源確認：mapping 表 LID `Head_Unit_Screen_Size` → `Radio_Display_Type`；PROXI 值表 `2 = 8.4" 1024x768`。6 列為 425, 426, 428, 429, 430, 431 |
| ~~**R-P8**~~ | ~~`$VC_VEH_Line$ = 332` **原文保留不動**~~ **SUPERSEDED by R-P8′ (2026-08-12)** | — |
| **R-P8′** | `$VC_VEH_Line$ = 332` 解除保留，更正為 `Car_Configuration_15.Vehicle_Line_Configuration = 105 (332)`。依據為 PROXI `Format` 分頁 row 466 col9 之列舉 `105 = 332 (69 Hex)` | PROXI Format **row 466** 經實測確認即該參數所在列，列舉文字逐字相符。**注意與 L-PJ2 的交互**：mapping v1_76 的列舉截斷於 `101 = WL`，`105` 正落在其缺漏區間 —— 若對 mapping 做值域檢查，本裁決的產出會被自己的 gate 判違規。R-P20 因此把值域權威釘在 PROXI（A-PJ17） |
| **R-P9** | `$HCP_DISP2.Est_Range_BEV$` 開 RD-1；步驟依 O-4 寫成可觀察形式，**不填訊號** | mapping 表 9 個 `Est_Range*` LID 無 BEV 變體；三候選互不等價，禁止三選一 |
| **R-P10** | `$HUModeStatus$` 取 FD 的 `TELEMATIC_FD_4.CurrentSource`；BH 的 `STATUS_TELEMATIC.CurrentSource` 於 Remarks 註記為等價來源 | 兩者皆存在且值表相同。**DBC 標籤帶 `_Selected` 後綴**（`AM_Selected`，非 `AM`）；L-PJ1 比對 DBC，故須照 DBC 寫 |

### §3a — PCTS 證據綁定（R-P11）

R-P6 的全區凍結解除。取而代之的規則只有一條：**一列能不能改，取決於它的
測項在 `data/pcts_evidence.json` 裡是不是 `confirmed`。**

取證於 2026-08-12 以 adb 唯讀方式執行（Pixel 10 / Android 16 / PCTS Verifier
`5.1-prod.922397802`，與 `inputs/` 的 apk 建號一致）。結果：

| 測項 | status | 服務列 | 解鎖 |
|---|---|---|---|
| `C2 - Confirm HU Vehicle Information` | **confirmed** | 255–266, 271（13 列） | ✅ |
| `NavigationStatusTests`（N1, N3, N5–N17） | **confirmed** | 371, 376–379（5 列） | ✅ 僅 371 |
| `MT1 - Microphone Sensitivity` | partial | 521, 522 | ❌ |
| `D5 - Confirm HU Displays 24-Bit Color` | partial | 441 | ❌ |
| `WP43 - Verify MD can start wireless projection` | partial | 267 | ❌ |
| （無編號）`PCTS video / display configuration test` | **not_found** | 443 | ❌ |

**23 列中解鎖 14 列。** 376–379 雖屬 confirmed 的測項，仍因
`Not in ASW-R1 Release Scope` 無條件凍結 —— 環境阻塞優先於工具阻塞。

三項 partial 缺的都是同一類東西：測項頁內才看得到的操作細節（MT1 的 OK 鈕與
量測值位置、WP43 的提示序列、D5 的色深顯示位置）。取得它們必須開啟測項頁，
而該動作會觸發 `TestRunnerService`，逾越唯讀授權。

**補裁 #4（2026-08-12）：三者併入首次實跑回填**，不另辦人工確認。這些細節本
來就要在真正執行該測項時才看得到，另辦一次是重複勞動。實跑時一併回填
`data/pcts_evidence.json` 並把 status 改為 `confirmed`，該測項的服務列即自動
解鎖 —— L-PJ7 讀的是那個檔案，不是靜態清單，所以解鎖不需要改 gate。

取證另外翻出兩件與現有步驟不符之處，**均已裁定不指認**：

- **row 441** —— `D5` 只涵蓋色深，DisplayTests 全 17 項無 refresh rate 測項；
  候選 `V59`（config 面）與 `V8`（rendering 面）不等價。補裁 #2 裁定
  **不指定**，該列維持不動並入 RD-1（A-PJ20）。
- **row 443** —— 引用的 `PCTS video / display configuration test` 在 431 個
  測項中不存在；候選 V45 / V46 / V47 / V50 不等價。補裁 #3 裁定**不指定**，
  比照 R-P18 對 leaf 146 的處置，維持不動並入 RD-1（A-PJ21）。

這兩條與 R-P9（`Est_Range_BEV` 三候選）、R-P18（leaf 146）構成同一條先例：
**候選不唯一即不選，該列維持不動並入 RD-1。** Phase 4 遇到同型情形可直接
援用，不必逐次上呈。

### §3b — R-P17 核對基準

O-1 的「不牴觸基本 spec」對 Projection Device HMI 的核對對象是
**`(May 3 2023)` 版**，不是 `inputs/` 裡較新的 `(February 5 2026)` 版。
workbook 126 條該文件引用中有 116 條帶 `(May_3_2023)` 版本戳記，而對照組
（Device Manager `(March_13_2023)` 75 列、Pop Up List `(Dec_15_2023)` 40 列）
版本皆與 `inputs/` 相符 —— 只有這一份對不上。路徑見
`feature.yaml → spec_baseline`；Change Log 同版併存，可量化兩版差距。同版的
SYS1 匯出（outline）亦已留用 —— 該件由執行端自行判斷補入、經補裁 #5 追認，
過程記於 A-PJ23，使核對基準版與參照版一樣具備「SYS1 匯出 + PDF 成對」的
mode A/B 結構。

### §3c — R-P20 列舉權威

**PROXI 是值域的唯一權威**；`Logical Identifiers and CAN Mapping` 只負責
Logical Identifier → 訊號／配置字**名稱**的對映，其列舉值不具權威性。實測：
mapping v1_76 的 `VC_VEH_LINE` 止於 `101 = WL (65 Hex) # = Not Used`，缺
`102 / 103 / 104 / 105 / 106 / 124 / 130`；PROXI `Format` row 466 完整列至
`130 = HDCC`。L-PJ2 的值域檢查一律對 PROXI 執行。


### §3d — 三層框架（A-PJ06 / R-P23 / R-P24，2026-08-12）

canon §4.1.1 要求 Test Group = 單一模組名；本簿的 Test Group 欄有 10 個值。
分析結論是 **A-PJ06 不是「值太多要合併」，而是一欄承載了三個維度** ——
功能域（Device Manager / Audio Management / Media Player / GPS / Touch）、
投屏協定（Carplay W&W / Android Auto W&W）、傳輸（Bluetooth / WiFi），外加
一個硬體特性標籤（`SSE / ECNR`，4 列）。10×18 的 180 格只有 46 格非零，
稀疏度正是維度混疊的必然結果。

**這條路不能靠改欄解決**：Test Group 與 Test Set 兩欄都在 §1 的凍結區內，
且 387/559 列（69%）已有執行紀錄，改欄即斷追溯。因此 framework 記錄真實
三層並附對映表回指凍結欄，**workbook 兩欄一字不動**。

| 層 | 內容 | 寫入 workbook？ |
|---|---|---|
| Layer 1 | `Projection`（單值） | ❌ 欄已凍結，維持既有 10 值 |
| Layer 2 | **16 個能力叢集 + 1 橫切 + 1 綑綁**（R-P33 定案） | ❌ 同上 |
| Layer 3 | CFTS085 **五碼**章節（R-P23） | ❌ canon 本來就不寫入 |
| 軸（非層） | 投屏協定、傳輸 —— §8.3 sibling 軸 | ❌ |

`SSE / ECNR`（4 列）登記為**硬體特性標籤**，非軸非層。

#### Layer 2 判準（合併版）

**RD 側集中（Sub Cat ≥67%）** 或 **跨 TG 完全由軸解釋** 或 **Layer 3 同父章**
—— 三者滿足其一即為乾淨。三個單一指標都會誤判：只用 RD 側會誤殺
`Connection`（57%），只用 TC 側會誤放 `HMI Display`，只用 Layer 3 單章佔比會
誤殺 `Vehicle Signal Forwarding`（29%，但五章全在 Location Data 樹下）。

`HMI Display`（76 列）是**唯一確定要拆的**：44 列由協定軸解釋、21 列是功能域
（Touch 13 + Media Player 8）、11 列是傳輸（Bluetooth × Wireless）。逸出率
**42%**，且 Layer 3 側跨父章（主導 `1.3.2.5` 僅 38%）。對照
`Projection Launch` 的逸出率 **4.6%** —— 42% vs 4.6% 就是綑綁與邊界個案的
分界。framework.md 以列號範圍記錄三個子叢集，Test Set 欄維持 `HMI Display`。
**這是 FULL_REFINE 的必然代價，後人看到欄值未清理不是遺漏。**

`Device Manager`（54 列）判定為**不綑綁**：全 54 列共享 Device Manager 主畫面
入口（命中率 96%；落在 `.11.3` 的 18 列為 100%），且該 18 列是協定軸的鏡像對
（CarPlay 9 / AA 9 逐項對應），037 需求原文完全相同。它們落在
`.11.3 Connecting to Wireless Projection` 是因為按 function icon 會發起連線
—— **章節歸屬跟隨需求的作用，Layer 2 跟隨測試的入口**，兩者在此分岔屬正常。

`Performance`（10 列）是**橫切狀態叢集** —— 它驗的是「投屏進行中」這個狀態
而非某個功能，Layer 3 側 100% 對到 `1.3.2.11.4 Active Wireless Projection`。
標註**不適用 §4.1.3 的「共享 setup 與 UI 入口」健康判準**。

#### ⚠️ Layer 3 的 version-track 分支（R-P23 補充條款）

CFTS085 的 `1.3.2.14` ~ `1.3.2.18` 按 release 切分（`SR20+ Apple
Certification Changes` 等），共 **115 列，佔 CFTS085 引用的 24%**。它們橫跨
功能是構造使然，計入同構檢驗會使乾淨叢集被誤判為綑綁 —— `Disconnection`
是最清楚的例子：計入時 49 列主導章佔比 41%（看似綑綁），排除後 23 列有 87%
落在 `1.3.2.11.5 Disconnecting`（乾淨）。

**排除僅在框架推導階段生效。這 115 列的 spec 核對對象仍是那些版本章節。**

這句話必須被完整讀到：「排除於同構檢驗」**不等於**「沒有 spec 依據」。
Phase 4 修訂這 115 列時，O-1 的「不牴觸基本 spec」照樣以 `1.3.2.14`~`.18`
為核對對象。把兩者混為一談會讓 24% 的 CFTS085 引用失去基準。

#### ⚠️ PROXI 是單車型文件（R-P47）

`PROXI_HDCC27_R3_20250424.xlsx` 的 `Header` 分頁第 4 列逐字為
**`HDCC27 - Draft`** —— 它是 **HDCC27 這一台車的配置檔**，不是全車系字典。

因此 R-P20（PROXI 為值域權威）的適用範圍**限於 HDCC27**。跨車型的前置條件
無法以本檔驗證，L-PJ2 對非 HDCC27 車型**不適用**。

**這是 R-P20 的第二次修正**。第一次是 R-P8′ 揭露 mapping 列舉截斷於
`101 = WL`；這次是 PROXI 只涵蓋一台車。**兩次同一個盲點 —— 把手上唯一的
那份檔案當成該類文件的全部。** 引用任何單一來源作為「權威」之前，先確認
它的涵蓋範圍是否等同於它的類別。

實例：`Knob` 42 列的 `PROXI VC_Veh_Line = <車型代號>` 跨 7 車型，5 個
Atl-Mid 車型在 HDCC27 的 PROXI 中無任何對應（A-PJ45 / DR#14）。

#### Layer 3 雙閘門（R-P29 結構 / R-P23·R-P32 語意）

推導單位須通過兩道**互不涵蓋**的閘門：**結構閘門**（跨 Test Set 數 ≥ 6 即
排除，機械可算）與**語意閘門**（界線須沿功能切分，人工判定）。實測證明互不
涵蓋 —— version-track 五章跨 Set 數 4/1/1/2/1 全數通過結構閘門，只有語意閘門
攔得住；SYSAD `4.6.1`（跨 10 Set）則只有結構閘門抓得到。

**語意閘門不得自動化**（R-P32）：字串啟發式會誤傷標題含版本標記的真功能
章節，且無法涵蓋未預期的切分維度。見 framework Part V §N.3。

#### Layer 3 粒度：五碼，四碼僅作父層（R-P23 / R-P24）

四碼會系統性壓扁兩個大章：

```
1.3.2.11 (120 列)  四碼看散在 7 個 Set，展開五碼後幾乎一一對應：
  .11.2 Pairing to Wireless          27 → Connection 19, Pairing 8
  .11.3 Connecting to Wireless       55 → Connection 35, Device Manager 18
  .11.4 Active Wireless              18 → Performance 10, Wireless Coexistence 4
  .11.5 Disconnecting from Wireless  20 → Disconnection 20 (100%)

1.3.2.10 (88 列)
  .10.1 Vehicle Sensor Data          71 → Knob 42, Day/Night Mode 22
  .10.2/.3 Location Data             17 → Vehicle Signal Forwarding 100%
```

同構度以**共同父章節**計算（R-P24）；單一章節佔比僅在跨父章時才構成綑綁
證據。

#### 分析 artifact

`features/projection/data/` 下六份，全部為 Tier 1 測量，不含分組提案：
`testgroup_matrix.json`（559 列逐列 + 10×18）、`cfts085_sections.json`
（clause→章節，486 clause / 0 未對映）、`sub_x_testset.json`（13×18）、
`protocol_axis.json`（協定／傳輸軸抽取）、`layer2_x_layer3.json`、
`layer2_isomorphism.json`（排除 version-track 後的同構度）。


## 4. `[ADD]` 訊號解析

Resolution order, and it is not negotiable: **workbook token → mapping table
Logical Identifier (Atlantis High column) → DBC signal or PROXI parameter**.
Querying a DBC with a workbook token directly resolves nothing — all 10
tokens miss on a direct lookup and 9 resolve after the mapping step.

The resolved table is `features/projection/data/signal_map.json`. Every entry
there was produced by lookup, not by assertion, and carries its `verified`
result. Three traps it encodes:

- `Day_Night_Mode` — the mapping cell lists **two** spellings;
  `DAY_LGT_MODE_DISP` exists in neither DBC. Take `DAY_LGT_MD_DISP`.
- Mapping LIDs are stored **UPPER CASE** (`VC_VEH_LINE`), the workbook uses
  three casings. Look up case-insensitively. Unifying the workbook's casings
  is a wording fix under O-1, not a semantic change.
- `$FuelLvlLow$` is **CAN-B only**. Both DBCs are required; they share only
  24 of their messages.

### CAN step pattern (four elements, none optional)

```
Pre-Conditions:
  1. PROXI Projection_Mode_Selection = 01 (CarPlay Only)

Procedure:
  1. Read the current HU volume and record it as Vol_initial
  2. Send CAN: BCM_FD_14.Command_02Sts = 1 (Pressed)
  3. Hold for 200 ms
  4. Send CAN: BCM_FD_14.Command_02Sts = 0 (Not_Pressed)
  5. Read the HU volume and check that it is lower than Vol_initial
```

PROXI 前置 → `message.signal = 值 (列舉標籤)` → 明確持續時間 → 釋放後讀值
比對. Shape taken from the SWC workbook (cross-feature, **style only** — its
column layout is a defect, A-PJ07; take the phrasing, not the layout).

The enumeration labels above are the DBC's own. The 下放包 §5 version of this
pattern wrote `(PSD)` / `(NOT_PSD)`, which appear in neither DBC and would
abort under L-PJ1 (A-PJ12). **R-P15 settles this as a general rule**: CAN
value labels always come from the DBC `VAL_` table, and the SWC cross-feature
exemplar lends its **structure**, never its literal labels.

A trap for every pre-condition that touches projection mode, taken verbatim
from the PROXI sheet's own note: **`Projection_Mode_Selection = 0` does not
disable projection** — it activates both CarPlay and Android Auto for
backward compatibility. Disabling requires the separate `Projection_Mode`
parameter to be `Absent`.

## 5. `[ADD]` Lint gate — L-PJ1 … L-PJ7

**硬性；違反 ABORT 不 warn。** These run in addition to the generic lint, not
instead of it.

| ID | 規則 |
|---|---|
| **L-PJ1** | Procedure 內每個 `{message}.{signal}` 必須在 `PHDCC27_E2A_R1_FDCAN8.dbc` 或 `PHDCC27_E2A_R1_BHCAN.dbc` **其一**解析成功；送出的值必須存在於該 signal 的 `VAL_` 表 |
| **L-PJ2** | Pre-Conditions 內每個 PROXI 配置字必須存在於 `PROXI_HDCC27_R3_20250424.xlsx`，其值必須落在 **PROXI 的**列舉範圍內。**值域檢查一律對 PROXI 執行，不得對 mapping 執行**（R-P20）。**適用範圍限於 HDCC27**（R-P47）—— 該檔為單車型配置檔（Header `HDCC27 - Draft`），對非 HDCC27 車型**不適用，不得據以判違規亦不得據以放行** |
| **L-PJ3** | Input Test Data 欄不得出現 `PROXI` 字樣（O-2） |
| **L-PJ4** | `Expected Result` 欄內容雜湊必須等於基準簿（O-1），違反即 ABORT。**窄口例外見下**（R-P12，2026-08-12） |
| **L-PJ5** | Procedure 禁用 canon §5.1 動詞（`observe` / `check whether` / `confirm whether` / `see if` / `verify` 作主動詞 / `watch` / `monitor` / `inspect`）。**以詞界比對**（A-PJ38，2026-08-12 修正）—— 子字串比對會把專有名詞 `Car Inspector` 誤判為 `inspect` |
| **L-PJ6** | 無來源之數值一律拒收（O-4）；模糊語須清除。**以詞界比對**（A-PJ18，2026-08-12 修正），詞彙表 `correctly` / `normally` / `properly` / `successfully` / `as expected` / `reasonable` / `a while` |
| **L-PJ9** | **flag，非 ABORT**（R-P42）。PRE 含 `Test equipment for` / `test setup for` / `analyzer for` / `equipment for measuring` **且** Procedure 無具名工具路徑 → flag。處置為維持不動 + 開 DR，不得自行指定設備。全簿命中 7 列，全在 `Performance` |
| **L-PJ10** | **flag，非 ABORT**（R-P43）。可編輯欄含 `<…>` 佔位符 → flag，但**兩類須先分開**：缺陷類（`<TBD>` / `<configured …>`，5 列）轉 RD-1；參數類（`<Device Name>` / `<Apple CarPlay OR Android Auto>`，8 列）以**列舉白名單**排除，不以樣式推斷 |
| ~~**L-PJ11**~~ | **暫緩**（R-P44）—— 「前置未保證清單內容存在」之檢出規則，樣本未到齊。B5（`Knob` 42 列，含 14 列此型）執行時改以人工逐列檢核，B5 上繳後再裁 |
| **L-PJ8** | Procedure 之步數必須等於凍結之 ER 行數（R-P36，2026-08-12）。改寫得重寫文字、合併敘述、加長單一步驟（canon §5.2 B/C，≤18 字），**不得增刪步驟**；確需增減者轉 RD-1 |
| **L-PJ7** | PCTS 相關列，其測項若未在 `data/pcts_evidence.json` 中 `status == "confirmed"`，該列任何欄位變動即 ABORT。`frozen_rows` 無論取證狀態一律 ABORT（R-P11，2026-08-12，取代 R-P6 的全區凍結） |

### L-PJ4 窄口（R-P12，2026-08-12）

L-PJ4 的預設仍是 ABORT。窄口**當且僅當**下列三條同時成立才放行：

1. diff 為**純刪除**（無新增、無改寫任何字）
2. 被刪除的 token ∈ `{correctly, normally, properly, successfully}`
3. 該列在窄口適用清單內

```
窄口適用（純刪除放行）：row 424, 425, 426, 427, 428, 429
                        —— 六列，皆為 Expected Result 內的 `correctly`
RD-1（不適用窄口，維持不動）：row 434, 435, 520   ← 實體列號（補裁 #1）
放行時記錄至 er_narrow_gate.log：列號、刪除詞、前後全文
```

兩份清單合起來恰好覆蓋 L-PJ6 的全部 9 個真陽性列，無重疊、無遺漏。補裁 #1
（2026-08-12）將 R-P12 原文的 `433 / 434 / 520` 定為**實體列號**讀法並更正為
`434 / 435 / 520` —— 原文的 433 在詞界修正後已無違規（A-PJ18 的假陽性），
真正帶 `normally` 的是 434 與 435。A-PJ19 據此關閉。

row 520 的 `correctly` 在 Procedure 與 Expected Result 各出現一次。Procedure
那一處不受 L-PJ4 拘束，仍須依 L-PJ6 清除；Expected Result 那一處凍結，入
RD-1。同一列兩種處置並存，不衝突。

### L-PJ6 詞界（A-PJ18，2026-08-12）

子字串比對會把 `content **a**re**a while** maintaining` 誤判為 `a while`。
必須以詞界比對：

```python
PATTERN = re.compile(
    r'\b(?:correctly|normally|properly|successfully|as expected|reasonable|a while)\b',
    re.I)
```

修正後對基準簿重跑，結果為真陽性 **10 處**（Expected Result 9 / Procedure 1，
落在 9 個實體列上），假陽性 **0**。此數即 Phase 4 起的基線；不符即停下開
anomaly。

### Implementation notes (Phase 0 measurements the gates have to survive)

- **L-PJ1** — DBC files are **ISO-8859 with CRLF**. Reading them as UTF-8
  raises or silently yields nothing, and a lint that finds nothing passes
  everything. Read as `latin-1`. Parse `BO_` for messages, indented `SG_` for
  signals, `VAL_` for value tables. Available inventory: FDCAN8 244 messages /
  1,503 signals / 1,052 value tables; BHCAN 123 / 692 / 514.
- **L-PJ2** — the PROXI parameter table is sheet `Format`, column F
  (`Parameter Name`), column I (the value table as free text); 1,052 distinct
  parameters. The R-P8 whitelist entry is the `$VC_VEH_Line$ = 332` literal.
- **L-PJ4** — the baseline is the `inputs/` copy, sha256
  `11579c9b3b8e56eb…`, sheet `TestResults`, column L, rows 4–562. Hash the
  normalised cell text (collapse whitespace runs) so that a re-save by Excel
  does not read as an edit.
- **L-PJ5** — **5 violations** in the base workbook after the 2026-08-12
  word-boundary fix (`check whether` 3, `inspect` **1**, `observe` 1). The
  previously reported 7 included two false positives on `Car Inspector`
  (r169/r170), a CarPlay Tests App view name — A-PJ38. Both L-PJ5 and L-PJ6
  carried the same substring defect and were found three rounds apart;
  **when fixing word boundaries on one string-matching gate, check them all.** They are the work, not a
  failure: the gate is what proves they were removed. Scanned on the Procedure
  column only — the same verb in an Expected Result states an outcome and is
  frozen under L-PJ4 anyway.
- **L-PJ6** — **10 true positives** after the 2026-08-12 word-boundary fix
  (`correctly` 8, `normally` 2), spread over 9 rows; `a while` drops to 0
  (both prior hits were the substring `content area while`). `properly`,
  `successfully`, `as expected` and `reasonable` have 0 occurrences and stay
  in the vocabulary as a guard on newly written text. **Interaction with
  L-PJ4**: 9 of the 10 sit in an Expected Result. Six of those (rows 424–429)
  are cleared by the R-P12 narrow gate as pure deletions; the rest are RD-1
  items, not edits.
- **L-PJ7** — the gate reads `data/pcts_evidence.json`, not a static row list.
  A PCTS row aborts unless its test is `confirmed`; `feature.yaml →
  done_region.frozen_rows` (376–379) aborts unconditionally. The gate compares
  all 36 columns, not just the editable ones.

### L-PJ8 步數對齊（R-P36）

ER 依 O-1 凍結，因此 canon §6 的 1:1 對齊在 FULL_REFINE 下由慣例升為**硬性
約束** —— 動 Procedure 的步數就等於單方面破壞對齊，而另一邊改不了。

**基線實測（2026-08-12）：558 個可比列中 555 列（99.5%）嚴格 1:1**，不等者
僅 3 列（r184 5/4、r355 5/4、r517 5/9）。pilot 曾一度把 r167/168 改成
3 步（ER 為 2 行），使破口由 3 增為 5，經 D-1 折回 2 步修復。

改寫時的可用手段：重寫步驟文字、把兩個動作併進一句、加長單一步驟。
**不可用**：新增步驟承載新動作。若某列的可執行性確實需要更多步驟，該列
轉 RD-1。

**步驟交叉指涉不是缺陷**（R-P39）。canon §5.2 未禁止之，全簿 30 列具
`as recorded in step N` / `Repeat steps N and M` 形式之回頭指涉，一律不動 ——
它們是比對型步驟的必要成分。

真正的缺陷是**前向循環**：步驟 N 的完成條件依賴步驟 N+k，而 N+k 是驗證步。
D-1 的 `until step 3 has been read` 即為全簿唯一一例。合併步驟以維持 L-PJ8
對齊時最容易寫出這種形式 —— **這是 L-PJ8 的副作用風險，改寫時要特別留意。**

### `[ADD]` 工具步驟的界線：介面 vs 內容（R-P38）

O-3 的「無手冊者不得推測」在實作上要分兩層。界線落在**介面**與**內容**
之間：

| | 有依據，可寫 | 無依據，不可寫 |
|---|---|---|
| 有手冊的工具（ATS / CarPlay Tests） | **怎麼操作** —— 手冊文件化的 traffic view、Filter 欄、選單路徑 | 手冊未載明的操作 |
| 平台標準工具（logcat / adb） | **怎麼啟動與讀取** —— 公知，不需手冊（R-P38） | **產品專屬參數** —— 過濾 tag、訊息格式、欄位名稱 |
| 無手冊的工具（mobile GAL log） | —— | 全部 |

**要找的東西是什麼**，必須來自 spec 或簿內既有 test data，不由工具手冊
提供。ATS 那 5 列是這條界線的範例：手冊零次提及 `NMEA` / `GPRMC`，但文件化
了 traffic view 與 Filter 欄，所以補的是「怎麼過濾」；`GPRMC` 這個字串本就
寫在簿內，屬既有 test data，非新增。

### `[ADD]` 檢視可執行性時須連同 ER 一併讀

**判準可能只存在於 ER。** 檢視 Procedure 是否可執行時，必須同時讀該列的
Expected Result —— canon 的分工是 Procedure 說「做什麼」、ER 說「應該發生
什麼」，因此一個看似缺判準的步驟，其判準往往就住在 ER。

實例（B3 r119–r122）：Procedure 寫 `Start music playback on Device A and
check the audio routing`，單看像是沒有判準；ER 第 6 行寫
`Device A's music audio cannot be routed through the HU during the active
2.4GHz CarPlay session` —— 判準完整。執行層一度將其列為缺陷，讀 ER 後撤回。

**這與 R-P37 同源**：ER 凍結使人容易忘記它仍是這一列的一部分。凍結的是
「不能改」，不是「不用讀」。

### `[ADD]` gate 的覆蓋面：查「錯」與查「缺」

L-PJ1 ~ L-PJ8 檢查的是**寫出來的東西對不對**；L-PJ9 / L-PJ10 是第一批檢查
**該寫的東西有沒有寫**的 gate。兩者性質不同，故後者為 **flag 而非 ABORT**
—— 它們指出的是「需要判斷」，不是「確定違規」。

B3（30 列）是這個區別的證據：L-PJ1 ~ L-PJ8 **0 命中**，但 12 列實際不可
執行 —— 缺設備 7（A-PJ39）、缺判準 1（A-PJ40）、缺前置 4（A-PJ41）。

### `[ADD]` ER 分歧不予修正（R-P37）

ER 凍結必然造成 Procedure 與 ER 的術語／機制分歧。**分歧不是缺陷，是 O-1 的
必然後果**，逐列登記於 `data/er_divergence.json`（35 列）而不修正：

- `terminology`（28 列）—— ER 用 SWE1 邏輯名或匯流排上不存在的標籤
  （`$FuelLvlLow$ = Active`），Procedure 已是 DBC 原文
- `mechanism_assertion`（**2 列**，r151/r152）—— ER 斷言一個依 R-P9 判定
  無依據的機制，Procedure 刻意拒絕指名

**RD-1 提問須同時涵蓋 ER**。只問 Procedure 會漏掉 `mechanism_assertion`
那一半 —— 該處是 ER 自己主張了無依據的機制。

### Gate interaction worth stating once

L-PJ4 (Expected Result frozen) and L-PJ6 (vague language must go) collide on
any row whose vagueness lives in the Expected Result. **L-PJ4 wins.** O-1 says
Expected Result 不得更改, and that is unconditional. The correct disposition
is an RD-1 item, never an edit that satisfies one gate by breaking the other.

## 6. `[ADD]` Column map

The base workbook is **not** an FM-WI-FSM-036 form instance. From column F
onward it sits one letter left of every other feature in this repo, because it
has no `Test Case ID (TestRail)` column. Header row 2, data rows 4–562.
Resolved by header-text match, 17/17. The full map lives in
`feature.yaml → workbook.columns`; do not inherit letters from another
feature's yaml.

Editable: `Pre-Conditions` (I), `Test procedure` (K). Everything else is
frozen under §1.

## 7. `[ADD]` spec_mode `[A, B, D]` — citation routing

The workbook's own `Specification Reference` column fixes this, and it names a
source on 558 of 559 rows:

| cited source | rows | in `inputs/`? |
|---|---|---|
| `CFTS085` | 473 | ✅ (mode D) |
| `Projection_Device_HMI_Logic_and_Flow` | 126 | ⚠️ version mismatch — A-PJ15 |
| `Accessory_Interface_Specification_CarPlay_Addendum_R10` | 82 | ❌ A-PJ14 |
| `HUIG_4_5` | 79 | ⚠️ safety-analysis report only — A-PJ09 |
| `Device_Manager_HMI_Logic_and_Flow` | 75 | ✅ (modes A/B) |
| `Pop_Up_List_HMI` | 34 | ✅ — 5 ids: PU0252, PU0254, PU0520, PU0523, PU0816 |
| `CFTS025` | 24 | ❌ A-PJ16 |
| `CFTS019` | 16 | ✅ |

No single mode describes this. CFTS085 carries the bulk (D); the two SYS1 HMI
Logic and Flow documents carry 201 rows between them (A/B). Hence `[A, B, D]`.

**116 of the 126 Projection Device citations carry the version stamp
`(May_3_2023)`, while `inputs/` holds the `(February 5 2026)` release.** O-1
requires rewritten steps not to contradict the base spec; checking 2023-era
steps against a 2026 document cannot distinguish a defective step from a
version change. Until A-PJ15 is ruled, those 116 rows are refined against the
CFTS085 text and the workbook's own done region, and any Projection-Device-
specific claim in them is left alone.
