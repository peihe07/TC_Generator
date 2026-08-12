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

#### §3e — L-PJ1 的權威來源是兩個，不是一個（R-P51）

兩份 PHDCC27 DBC **不是本簿 CAN 訊號的全部權威**。`Cluster Navigation` 引用
`TELEMATIC_NAV_INFO.*` / `TELEMATIC_DISPLAY_INFO.*`，定義在 Phase 0 即已落地的
`Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx`（B/BH-CAN 訊號）。

**登記表以人工維護**（R-P51：5 列不值得建萃取管線），存於
`data/signal_map.json → vf176_signals`，每筆帶 `authority` / `enum` /
`verified_manually`。**未登記之 VF176 訊號仍 ABORT** —— gate 沒有被繞過，
只是承認第二個權威。負向驗證已通過（`LastAnnouncement` 有定義但未登記 → ABORT）。

可寫程度由 `enum` 決定：有列舉者可寫 `值 (標籤)`，無列舉者**只能寫名稱**
（O-4）。`Direction` 38 項、`ResolutionDistToTurn` 3 項有列舉；`DistToTurn`
（連續量）／`Unit`／`UTF_Text_*`（文字）無。

**這是 canon §5a 第九條的第三次命中，也是唯一一次方向為「擴充」**：

| | 誤當作全部的那份 | 修法 |
|---|---|---|
| R-P8′ | mapping 列舉（截斷於 `101 = WL`） | **限縮** |
| R-P47 | `PROXI_HDCC27_R3`（單車型） | **限縮** |
| **R-P51** | **兩份 PHDCC27 DBC** | **擴充** |

前兩次缺的是資料，這次缺的是 gate 的認識範圍 —— 同一條紀律，相反的修法。

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
| **L-PJ1** | Procedure 內每個 `{message}.{signal}` 必須在**權威來源**解析成功；送出的值必須存在於該 signal 的值表。**權威 = 兩份 DBC ∪ VF176 逐訊號登記表**（R-P51，2026-08-12）—— 見 §3e。未登記者一律 ABORT |
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

## 5a. `[OVERRIDE]` dry-run 檢查表（R-P53）

**Displaces**: canon §6 之 dry-run 欄位清單。canon §6 為 **regen 型**設計，
其 segment 算術、segment 順序、regen req-set 相等三項在 `FULL_REFINE` 無對應
概念（沒有 regen、沒有 segment、done region 是整張表）；done-region hash 一項
改以「34 個凍結欄逐列雜湊」實作。

### 檢查表 v2（R-P54 / R-P55 / R-P58，2026-08-12）

v1 之 D-1 ~ D-5 依 R-P55、R-P54 修訂，新增 D-6 ~ D-10（原執行層提報之 M-1 ~ M-5）。

| 項 | 通過條件 |
|---|---|
| **D-1** | 有變更之欄位 ⊆ `{Pre-Conditions (I), Test procedure (K)}` ∪ `{Expected Result (L) ∩ er_narrow_gate.log 之 6 列}` ∪ `{Remarks (AJ) ∩ remarks_scope_gate.log 之 30 列}`（R-P75）。窄口列（r424–r429）**須逐列附 diff**，並驗證為純刪除、被刪 token ∈ `{correctly, normally, properly, successfully}`。不得僅以「見 log」代替 |
| **D-2** | `TestResults` 34 個凍結欄逐列雜湊不變，**加上其餘 8 個分頁**。**雙軌（R-P60）**：公式軌（`data_only=False`）8 分頁全部必須不變，含全簿 **775** 個公式；值軌（`data_only=True`）`TestProgress` 之變動為預期行為，其餘 7 分頁不變。**dry-run 階段值軌標「未實測」，不得計為 PASS**（A-PJ56）。兩項授權例外須逐列列出：`Expected Result` 之 r424–r429（R-P12）、`Test Case Author` 之 **40** 列補值（R-P19／R-P54）、`Remarks` 之 **30** 列純附加（R-P75）＝ 共 **76** 列 |
| **D-3** | 分支 A（227 補列成功）：559 → 558 + 7 補列，末列 r568；分支 B：559 保留 + 6 補列。逐列 index-to-index 比對，**移動即 FAIL，不得視為 merge**。**列身分＝凍結欄逐列雜湊扣除全部『有授權例外之欄』**（`ROW_IDENTITY_COLS` = FROZEN_COLS − {`Expected Result`, `Remarks`, `Test Case Author`}，558 列 558 個相異值）。**凡新增凍結欄窄口必須同步擴充 `IDENTITY_EXCLUDED`**，否則該窄口之列會被誤判為被移動（A-PJ66，已發生兩次）。**不得用 `No.#`** —— 該欄內容為公式 `=ROW()-3`，值恆等於列位置，偵測不到重排（A-PJ57 推翻 R-P66 之指定欄，其意圖不變） |
| **D-4** | 未覆蓋 leaf 補列追加於表尾，`Test Case Author = PeiPYHsu`、`tc_ref_id = NEW`、不重新編號既有列、通過全部 gate。來源不足以寫出通過 gate 之 TC 者列為未補並開 DR（O-4） |
| **D-5** | 每一「正確地不動」列皆指得出至少一個裁決或 DR 編號。**以列為單位**上繳（群組間有重疊，加總會對不上） |
| **D-6** | 補列之獨立驗證。補列**不受 D-1／D-2 保護**——其 34 個凍結欄全為新寫。逐欄驗 `Priority` ∈ {P0–P3}、**`Design Method` ∈ `Reference!$C$4:$C$12`（資料驗證實際強制者，非 `下拉選單` 分頁 —— 兩份「組合測試」拼法不同，A-PJ58）**、`Test Group`／`Test Set` ∈ 既有值域（10／18）、**`Specification Reference` 真解析**（R-P73：逐條對 `data/*_sections.json` 查找，找不到即 FAIL；無 sections 檔之來源標「未解析」，不得計為通過）、`Requirement or Design ID` 存在於 037、**`Test Case ID` 符合 R-P64 續編規則且不與既有重複、**`Input Test Data` 依 canon §4.5 逐條判定（R-P72，不得以既有多數值為由）****、Procedure ↔ ER 行數 1:1、L-PJ1 ~ L-PJ10 全綠 |
| **D-7** | `er_divergence.json` 之 `proc_excerpt` 須更新為修訂後內容（`er_excerpt` 凍結）。**RD-1 會拿著過期描述去問** |
| **D-8** | `data/` artifact 逐份標記時效：修訂前快照標 `snapshot_phase` 且不更新，須同步者更新。**兩種語意不得混用於同一欄位**，必要時拆欄 |
| **D-9** | `Test Case Framework` 分頁實測為**完全空白**（`A1:A1`），原假設其有內容並與 framework Part V 比對之前提不成立。修正為：驗證維持空白且雜湊不變；**寫回後出現內容即 ABORT** |
| **D-10** | 八項全簿基線。補列納入後之值須一併回報——**補列可能改變基線，若改變須有裁決** |
| **D-11** | **全簿資料驗證合規**（R-P74）。範圍＝所有具資料驗證之欄；通過條件＝每一非空儲存格之值皆落在該欄 DV 來源之值域內（逐字比對）。**空白不視為違規**；**既有違規凍結欄不動入 RD-1，補列違規即 FAIL**。比對前須正規化數值儲存格 —— Excel 存數值 `1`、DV 寫 `"0,1"`，未正規化會把 Vehicle Model 21 格全部誤報 |

**D-5 是本表存在的主要理由。** regen 型的「未完成」就是缺漏；`FULL_REFINE`
的未完成多數是**依規則正確地不動**。兩者在 diff 上長得完全一樣 —— 都是
「這一列沒變」。**唯一的區分方式是清單。**

**D-6 是 v2 補上的最大缺口。** D-1／D-2 驗的是「既有列之凍結欄未變」，補列
沒有「既有」可比，34 個凍結欄全為新寫。此缺口在 R-P54 將補列由 6 增為 7
之後影響更大。

#### D-10 基線（修訂後全簿，rows 4–561）

| Gate | 值 | 計數單位 | 掃描範圍 |
|---|---|---|---|
| L-PJ5 禁詞 | 1 | 次 | I + K |
| L-PJ6 模糊語 | 4 | 次 | I + K + L |
| L-PJ9 泛稱工具 | **17** | 列 | PRE 命中泛稱且 PROC 無具名工具 |
| L-PJ10 缺陷類 | 5 | **列** | I + K + L |
| L-PJ10 參數類 | 8 | **列** | I + K + L |
| 步驟交叉指涉 | 30 | 列 | K |
| 步數 != ER 例外 | 3 | 列 | K vs L |
| 前向循環指涉 | 0 | 次 | K |

**單位不一致是刻意的，不是筆誤**：L-PJ6 以次計（r520 一列在 PROC 與 ER 各
命中一次，算兩次），L-PJ10 以列計（參數類 8 = 8 列，非 8 次）。canon §5a
第二條要求計數單位隨值一併載明，故此表列出單位欄。**L-PJ10 之掃描範圍必須
含 `Expected Result`** —— 參數類 8 列中 r60／r61 之 `<Device Name>` 只出現在
ER，只掃可編輯兩欄會得到 6。

#### 執行記錄

| 輪次 | 日期 | 結果 | 報告 |
|---|---|---|---|
| v1 首次 | 2026-08-12 | **FAIL**（D-4 FAIL、D-1／D-2 條件與 R-P12 衝突） | `docs/dryrun_report.md` |
| v2 | 2026-08-12 | **PASS**（D-1 ~ D-10 全綠，走分支 A） | `docs/dryrun_v2_report.md` |
| v3 | 2026-08-12 | **PASS**（檢查表 v3；含複本寫入實測） | `docs/dryrun_v3_report.md` |
| v4 | 2026-08-12 | **PASS**（檢查表 v4；D-1 ~ D-11 + W-1 ~ W-7 複本全過） | `docs/phase7_step1_5_report.md` |

### 凍結欄之例外一律為窄口（R-P12 / R-P75）

本 feature 有兩個凍結欄窄口，**設計形式相同**：白名單 + 固定形式 + 純變更方向
+ 逐列記錄。

| 窄口 | 欄 | 列 | 形式 | log |
|---|---|---|---|---|
| **R-P12**（L-PJ4） | `Expected Result` | 6（r424–r429） | **純刪除**，被刪 token ∈ `{correctly, normally, properly, successfully}` | `er_narrow_gate.log.json` |
| **R-P75** | `Remarks` | 30（Atl-Mid 車型） | **純附加**，固定字串 `Vehicle line out of R1LR SWQT scope (DR#14, 2026-08-12)` | `remarks_scope_gate.log.json` |

**凍結欄之例外一律為窄口，不得為一般授權。** 兩者共同確立此形式。

R-P75 的理由：本簿自身的範圍標記慣例即置於 `Remarks`（77 列先例）。只記於交付
文件而不入簿，執行者會遇到一個無法解析的 PROXI 前置條件而無任何說明 ——
**那正是本專案存在的理由所在之缺陷**。

**窄口僅適用既有列**（R-P80）：補列全欄新寫，不受凍結拘束，其 `Remarks` 自由
填寫不需授權。同一欄兩套規則，依據不同。

## 5b. `[ADD]` Phase 7 寫回動作清單 W-1 ~ W-7（R-P71）

| # | 動作 | 驗證 |
|---|---|---|
| W-0 | **備份交付檔**至 `backup/…<ISO8601>.bak.xlsx`，SHA256 須等於寫回前之值（R-P78） | 不符即中止 |
| W-1 | 保留公式模式載入（**禁 `data_only=True`**） | 公式總數 = 775 + 補列淨增 6 = **781**（R-P77 更正「775 不變」之算術錯誤） |
| W-2 | 寫入 63 列 71 格 + **Remarks 窄口 30 列純附加**（R-P75） | 變更欄 ⊆ 授權集合；30 列逐列純附加 |
| W-8 | **`Test Case Author` 40 個空白列補 `PeiPYHsu`**（R-P83，置於 W-4 後、W-7 前） | 寫回後該欄空白 = 0；變更列數 == 40 |
| W-3 | 刪除 r562（分支 A） | 559 → 558；刪前確認 227 補列已存在 |
| W-4 | 補列 7 條，ID `NR1L-PROJ-560~566` | D-4 / D-6 |
| W-5 | **`No.#` 寫公式 `=ROW()-3`** | c2 全欄 565 格皆為公式 |
| W-6 | **DV 範圍延伸至 r568** | r563–r568 各受控欄皆有下拉 |
| W-9 | **補列與參照列 r561 同構**（R-P86）：逐欄繼承全部樣式屬性 + 列層級設定 + 自動篩選 `ref` 延伸至 r568 | 7 列 × 36 欄逐屬性比對，不符 0；**逐欄繼承非整列套用** —— r561 之 36 欄實測有 **8 種**相異樣式簽章 |
| W-7 | 外部重算（`soffice --headless`） | 統計值與**預先算出**之預期一致 |

**W-5 / W-6 / W-9 是本清單存在的理由** —— 其餘各項現行檢查項皆能攔下，這三項
不能（D-2 比對內容不比對型別，D-6 比對值不比對有無下拉，**D-1 ~ D-11 全部不看
樣式**）。

三者是**同一缺口的三個表現**：「補列」原本被定義成「寫入儲存格的值」，而不是
「新增一列使其與既有列同構」（R-P86）。W-6 之所以早於另兩項存在，只因 A-PJ59
在複本實測時偶然發現了資料驗證那一項。

**W-9 之通過條件為「與參照列在所有可讀屬性上一致」，非「已知的幾項設定正確」** ——
前者會隨屬性增加自動涵蓋，後者只涵蓋已經想到的。

**驗證順序（R-P78）**：可在記憶體中驗證者（公式數量與內容、儲存格值、型別）
**一律置於 `save()` 之前**；僅能在落盤後驗者（W-7 外部重算）才置於其後，且其
失敗即觸發還原。**還原之定義＝以備份檔覆蓋並驗證 SHA256 回到寫回前之值。**

實作於 `features/projection/scripts/writeback.py`，每項自帶驗證，任一不過即
raise，不留半成品。**預設只在複本執行；對交付用檔案執行須明示放行。**

#### 檢查表 v3 之四項修訂（R-P59 ~ R-P66）

1. **D-2 雙軌**（R-P60）+ dry-run 值軌標「未實測」（A-PJ56 → canon §5a 第十一條）
2. **D-3 列身分**改為內容導出之雜湊（A-PJ57 推翻 R-P66 指定之 `No.#`）
3. **D-6 值域**改用資料驗證實際強制者（A-PJ58）+ 新增 `Test Case ID` 欄
4. **D-9** 由「比對一致性」改為「驗證維持空白」

**新增前置檢查（Phase 7 寫回，R-P59）**：寫回前後全簿 **775** 個公式逐一比對，
任一消失即 ABORT 並還原。禁止 `data_only=True` 載入後存檔 —— 複本反證實測
775 → 0，不可逆（A-PJ60）。

列號對照表見 `features/projection/data/d5_blocked_rows.json`，逐項明細見
`features/projection/data/dryrun_v2.json`。

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
