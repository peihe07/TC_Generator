# DECISIONS — Projection (FW036)

Marker semantics per FEATURE_ONBOARDING §4:

- `[AUTO]` — machine-determined, recorded for audit, no action needed
- `[PROPOSED: value — rationale]` — Pei edits if disagreeing; untouched at
  sign-off = binding as proposed
- `[PEI]` — cannot be proposed; must be filled before sign-off
- `[SIGNED]` — ruled by Pei before scaffold; reproduced verbatim, not editable
  by this pipeline

---

## 0. Signed rulings (Pei, 2026-08-11) — 逐字

Reproduced word for word from the Phase 0 下放包 §2. Nothing here was
paraphrased, reordered, or completed.

### Feature 界定

| ID | 裁決 |
|---|---|
| **R-P1** | feature 名稱 = `Projection`，單一 feature，不拆分 ProjectionDeviceMedia-HMI |
| **R-P2** | 037 主線 = `FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA-CPAA_0521.xlsx` |
| **R-P3** | workbook 主體 = `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` |
| **R-P5** | 素材根目錄 = `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection` |

### 修訂總則

| ID | 裁決 |
|---|---|
| **R-P4** | 所有測試 data 不可更動；只修正字詞使其明確、準確、可落地執行。步驟必須查明實際怎麼操作；需 testapp／工具的也必須確認操作步驟。**SWE1 是分析，數值一律以 CPAA 原始 spec、CFTS、HMI 為準，不可編造。** |

### 個別處置

| ID | 裁決 |
|---|---|
| ~~**R-P6**~~ | ~~PCTS 相關 23 列**凍結不動** —— 不改寫、不留白、不開步驟；僅在 DATA_REQUESTS 掛一列待補手冊~~ **`SUPERSEDED` by R-P11 (2026-08-12)** —— 原文保留供審計軌跡 |
| **R-P7** | `$Screen_Size$` → PROXI `Radio_Display_Type`；Remarks 註明 `only 8.4"` 的 6 列寫為 `Radio_Display_Type = 2` **（2026-08-12 升格為雙來源，見 §0.1）** |
| ~~**R-P8**~~ | ~~`$VC_VEH_Line$ = 332` **原文保留不動**，Remarks 註記待確認~~ **`SUPERSEDED` by R-P8′ (2026-08-12)** —— 原文保留供審計軌跡 |
| **R-P9** | `$HCP_DISP2.Est_Range_BEV$` 開 RD-1；步驟依 O-4 寫成可觀察形式，**不填訊號** |
| **R-P10** | `$HUModeStatus$` 取 FD 的 `TELEMATIC_FD_4.CurrentSource`；BH 的 `STATUS_TELEMATIC.CurrentSource` 於 Remarks 註記為等價來源 |

### Profile 條文（O-1 ~ O-4）

**O-1**　把不明確的步驟寫踏實，不牴觸基本 spec。**Expected Result 不得更改。**

**O-2**　PROXI 配置寫在 **Pre-Conditions**；送 CAN、開工具、讀值、比對等**所有操作一律寫在 Procedure 步驟**。不使用 Input Test Data 承載 PROXI。

**O-3**　工具步驟依 `CarPlay TestApp` / `ATS 8.10.0` 手冊撰寫；無手冊者不得推測。

**O-4**　不得編造測項。**沒有數值就寫成可觀察的結果。**

These four are reproduced verbatim in
`docs/runtime/profiles/FW036_R1L_Projection_Profile.md`.

### Phase 0 recon 對這些裁決的影響

None of the rulings above is weakened by recon. Two gain a second source and
one has its stated *evidence* revised:

- **R-P7 — corroborated, and promoted to dual-source on 2026-08-12.**
  `$Screen_Size$` resolves through the mapping table under the Logical
  Identifier `Head_Unit_Screen_Size` → `Radio_Display_Type`, the same target
  R-P7 rules by hand. PROXI confirms `2 = 8.4" 1024x768`. The token is no
  longer "ruled without a mapping"; it carries two independent sources —
  mapping (name) + PROXI (enumeration). (A-PJ13)
- **R-P8 — evidence revised at Phase 0, ruling then reversed at Phase 2.**
  `Vehicle_Line_Configuration` *does* enumerate 332, at `105 = 332 (69 Hex)`.
  332 is the vehicle-line **label**, not a configuration value. Phase 0 kept
  the literal untouched; **R-P8′ (2026-08-12) reverses that** and corrects it
  to `= 105 (332)`. (A-PJ10)
- **R-P10 — confirmed on both buses.** `TELEMATIC_FD_4.CurrentSource` (FD) and
  `STATUS_TELEMATIC.CurrentSource` (CAN-B) both exist and carry identical
  value tables. Note the DBC labels carry a `_Selected` suffix
  (`AM_Selected`, not `AM`); L-PJ1 compares against the DBC, so steps must be
  written with the suffix.

---

## 0.1 Signed rulings (Pei, 2026-08-12) — Phase 2, 逐字

Reproduced word for word from the Phase 2 下放包 §2.2. Nothing here was
paraphrased, reordered, or completed. R-P6 and R-P8 above are marked
`SUPERSEDED` and their原文 retained for the audit trail.

**R-P8′**（取代 R-P8）
> `$VC_VEH_Line$ = 332` 解除保留，更正為 `Car_Configuration_15.Vehicle_Line_Configuration = 105 (332)`。依據為 PROXI `Format` 分頁 row 466 col9 之列舉 `105 = 332 (69 Hex)`。DR#3 關閉。

**R-P11**（取代 R-P6）
> R-P6 的凍結解除，改為證據綁定：PCTS 相關 23 列的步驟修訂，僅在該測項的操作路徑已由實機取證確認後方得進行。取證方式為 adb 實測（方式 B），佐以人工確認補足 adb 無法取得之項目。未取得證據之測項，其相關列維持不動。
> 取證範圍為 5 個測項：`C2`、`NavigationStatusTests`、`MT1`、`D5`、`WP43`。
> `NR1L-PROJ-374~377` 因 Remarks 標記 `Not in ASW-R1 Release Scope`，環境阻塞優先於工具阻塞，即使取證完成仍維持不動。

**R-P12**
> L-PJ4 窄口開啟，限定為「純刪除」：diff 必須是純刪除操作，且刪除的詞須在白名單內（`correctly` / `normally` / `properly` / `successfully`）。不得新增或改寫任何字。適用 row 424–429 六列。row 433 / 434 / 520 因無可觀察判準，不適用窄口，轉 RD-1。

**R-P13**（A-PJ09）
> 037 的來源家族更正為 `SYS-RA-PROJ` 145 / `SYS-RA-HUIG4.5` 16 / `SYS-RA-CP_R10` 9 / `CP-R10` 1。原判之 `AA-V4.5` 與 `CP-R46` 於 CPAA_0521 全檔 0 次，係分析端誤判。A-PJ05 撤銷，DR#4、DR#5 關閉——對應之 SYS2 報告（`SYS2_HUIG_4_5`、`SYS2_CP.R10`）已在 `inputs/`，缺件不存在。

**R-P14**（A-PJ11）
> leaf `SWE1-PROJ-133` 於 MD 版 037 標記 unavailable 不拘束主線。R-P2 已定 CPAA_0521 為權威，副線之下架不得撤銷主線之 live leaf。未覆蓋缺口維持 **7 條**。

**R-P15**（A-PJ12）
> CAN 送值標籤一律以 DBC `VAL_` 表為準。`Command_02Sts` 之合法標籤為 `Not_Pressed` / `Pressed` / `SNA`；`PSD` / `NOT_PSD` 於兩份 DBC 皆不存在，不得使用。
> SWC 跨 feature 範式之引用原則更正為：**取其結構（PROXI 前置 → `message.signal = 值 (標籤)` → 明確持續時間 → 讀值比對），不取其字面標籤**。

**R-P16**（A-PJ14）
> CarPlay Addendum R10 納入 `inputs/`（82 列引用，帶 §3.2.6、§3.3.5 等錨點）。授權跨出 R-P5 根目錄取檔。

**R-P17**（A-PJ15）
> Projection Device HMI Logic and Flow 兩版併存。**核對基準為 `(May 3 2023)` 版**——workbook 116 列引用該版，且對照組（Device Manager `(March 13 2023)`、Pop Up List）版本皆相符，僅此一份對不上。`(February 5 2026)` 版保留於 `inputs/` 作版本演進參照。O-1 之「不牴觸基本 spec」以 May 3 2023 版為核對對象。

**R-P18**（A-PJ16）
> CFTS025 開 DR#8，**不阻塞** Phase 3 / Phase 4。leaf `SWE1-PROJ-146` 全文轉指 `CFTS025-4660`，需求本文未確認存在，維持未覆蓋。

**R-P19**（A-PJ08）
> `Estimated Test Time` 全 559 列空白為既有慣例，**維持空白**，不補。
> `Test Case Author` 空白 41 列補為 `PeiPYHsu`。
> 第 562 列殘樁刪除。

**R-P20**（A-PJ17，新登記）
> PROXI 之列舉值為權威來源；`Logical Identifiers and CAN Mapping` 僅供 Logical Identifier → 訊號／配置字名稱之對映，其列舉值不具權威性。
> 依據：mapping v1_76 之 `VC_VEH_LINE` 列舉截斷於 `101 = WL`，缺 `102/103/104/105/106/124/130`；PROXI `Format` row 466 完整列至 `130 = HDCC`。
> L-PJ2 之值域檢查一律對 PROXI 執行，不得對 mapping 執行。

### Phase 2 執行時發現、與裁決文字不符之處

依 §0.5「不自行調和」，以下各項照實登記，未依任一種讀法逕行套用：

- **R-P12 的 RD-1 列號**。窄口清單 `row 424–429` 與實測完全相符（六列皆為
  ER 內的 `correctly`）。RD-1 清單 `433 / 434 / 520` 則無論用哪種讀法都對
  不齊：以**實體列**讀，row 433 在詞界修正後已無任何違規（其原本的
  `a while` 正是 A-PJ18 的假陽性），而真正帶 `normally` 的是 row 434 與
  **row 435**；以 **tc_id** 讀，`NR1L-PROJ-433` / `-434` 恰好就是 row 434 /
  435（吻合），但 `NR1L-PROJ-520` 是 row 521，一列 PCTS/MT1 測項，不含任何
  模糊語。兩種讀法各對一半。→ **A-PJ19，待 Pei 指定讀法**。
- **R-P20 的依據數字**。mapping v1_76 的 `VC_VEH_LINE` 列舉截斷處經實測為
  `101 = WL`，缺 `102/103/104/105/106/124/130` —— 與裁決文字完全相符，已據
  此改寫 L-PJ2。
- **§5.2 的預期真陽性 10 處**（ER 9 / PROC 1）—— 實測完全相符。詳見
  `ANOMALIES.md` A-PJ18。

---

## 0.2 追加裁決 (Pei, 2026-08-12) — Phase 2 補裁, 逐字

原文逐字：

> 434/435/520 採實體列號｜A-PJ20 不指定 V59/V8｜A-PJ21 不指定 V45｜MT1/D5/WP43 併入首次實跑回填｜SYS1 匯出留用（登 A-PJ23）｜A-PJ06 下一輪獨立分析。

逐項展開與落檔位置：

| # | 裁決 | 解決 | 落檔 |
|---|---|---|---|
| 1 | **434/435/520 採實體列號** | A-PJ19 | R-P12 的 RD-1 清單定為實體列 434 / 435 / 520。窄口清單 424–429 不變。profile §5 的 L-PJ4 窄口段已補上確定清單 |
| 2 | **A-PJ20 不指定 V59/V8** | A-PJ20 | row 441 的 refresh rate 步驟不得指派 `V59` 或 `V8`。該列維持不動，入 RD-1。DR#9 撤銷 |
| 3 | **A-PJ21 不指定 V45** | A-PJ21 | row 443 的無名測項不得認定為 `V45`。該列維持不動，入 RD-1。DR#10 撤銷 |
| 4 | **MT1/D5/WP43 併入首次實跑回填** | DR#11 | 三項 partial 缺的操作細節不另辦人工確認，改為在該測項首次實際執行時一併回填 `pcts_evidence.json`。四列（267 / 441 / 521 / 522）在回填前維持 ABORT |
| 5 | **SYS1 匯出留用（登 A-PJ23）** | — | 自行判斷補入的 `SYS1_HMI_Projection_Device_HMI _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx`（`530274f8…`）獲追認留用，並登記為 A-PJ23 |
| 6 | **A-PJ06 下一輪獨立分析** | A-PJ06 | Test Group 10 值之議題自 Phase 3 一般流程中抽出，改列獨立分析輪次 |

### 這六項共同的取向

前三項（434/435/520、不指定 V59/V8、不指定 V45）方向一致：**凡需在來源之外
指認對象者，一律不指認**。A-PJ20 / A-PJ21 都是「步驟指向一個測項，而該測項
在工具內不存在或不涵蓋所需項目」，候選都不只一個且互不等價 —— 與 R-P9 對
`$HCP_DISP2.Est_Range_BEV$` 的處置、R-P18 對 leaf 146 的處置同型。三者現在
構成一條穩定的先例線：**候選不唯一即不選，該列維持不動並入 RD-1。**

第 4 項把「取證」與「實跑」合流：adb 唯讀取不到的東西，本來就要在真正跑那
個測項時才看得到，另辦一次人工確認是重複勞動。代價是這 4 列解鎖時點後移到
首次實跑。

### 尚未收到條文的編號

`R-P21`、`R-P22`、`A-PJ22`、`A-PJ24` 於補裁當時僅有編號到達、條文未送達，
故未落檔。**條文已於同日補齊** —— R-P21 / R-P22 見 §0.3，A-PJ22 / A-PJ24 見
`ANOMALIES.md`。此處保留記錄，說明該批編號曾有一段時間只有號碼沒有內容。

---

## 0.3 Signed rulings (Pei, 2026-08-12) — R-P21 / R-P22, 逐字

**R-P21**（部分撤銷 R-P13）
> R-P13 之 DR#4 關閉部分撤銷。DR#4 重新開啟並更名為「HUIG 4.5 規格本文」，服務 workbook 79 列 + 037 之 16 條 SYS-RA-HUIG4.5 leaf。
> 撤銷理由：79 列全數引用 HUIG 規格本文（`HUIG_4_5 §6 R06-010`、`HUIG_4.5_R12-460` 等 §/R-ID 形式），其中 43 列僅引規格本文、36 列同時引規格本文與 SYSRA，零列僅引 SYSRA。`inputs/` 內之 `SYS2_HUIG_4_5_…SYSRA…xlsx` 為技術安全需求分析報告，不能替代規格本文。原判係將分析報告誤認為規格本身。
> R-P13 之其餘部分（AA-V4.5 / CP-R46 命名撤銷、A-PJ05 RETRACTED、DR#5 關閉）維持有效。

**R-P22**
> 授權補入 `HUIG 4.5.pdf` 與 `SYS1_HUIG4.5.xlsx` 至 `inputs/`，授權範圍跨出 R-P5 根目錄。已定位四處副本：`1_Customer_Requirement/CPAA_spec/`、`9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/`（PDF + xlsx）、`10_Reviewing/00_TestCase/Bluetooth/REF/`。
> 依 Phase 2 下放包 §4.1 之 hash 規則處理：hash 全同則取 `1_Customer_Requirement/` 下者；hash 有異則停下不自選版，列出各副本路徑、hash、檔案時間待裁。
> 補入後 DR#4 關閉、A-PJ24 關閉。spec_mode 需重評——HUIG 為 SYS.1 層產物，引用量 79 列僅次於 CFTS085(473)、Projection HMI(126)，與 CarPlay Addendum(82) 同級。

### R-P21 引用統計 — 逐項複驗（2026-08-12）

裁決所述之四個數字全部重現：

| 項目 | 裁決 | 實測 | 判定 |
|---|---|---|---|
| HUIG 引用列數 | 79 | **79** | 符合 |
| 僅引規格本文 | 43 | **43** | 符合 |
| 兼引規格本文與 SYSRA | 36 | **36** | 符合 |
| **僅引 SYSRA** | **0** | **0** | 符合 |

`僅引規格本文 43` 由兩種書寫形式合計而成，逐行判定：**25 列**帶 §/R-ID
（`HUIG_4_5 §7.15 R07-326`、`HUIG_4.5_R12-460`、`HUIG_4_5 R07-360` 等）、
**18 列**寫成裸引用（`HUIG_4_5` 單獨一行，或 `HUIG R06-023, R06-200` 省略
版號）。兩者都是規格本文引用，皆非 SYSRA。

**「零列僅引 SYSRA」是本裁決的關鍵**，也確實成立：SYSRA 從未單獨出現，永遠
與規格本文並列。分析報告在這份 workbook 裡從來不是引用終點，只是補充 ——
這正是 R-P21 所指「將分析報告誤認為規格本身」的反證。

### R-P22 取檔 — hash 全同，未觸發停下分支

| 檔案 | SHA256 | 副本數 | 處置 |
|---|---|---|---|
| `HUIG 4.5.pdf` | `4cad660843e3ca98144ec6a5a6a850ec8e6a07523f825e63ca4e9f938616a508` | **3 處，位元全同**（8,213,730 B，皆 2026-05-12） | 依規則取 `1_Customer_Requirement/CPAA_spec/` |
| `SYS1_HUIG4.5.xlsx` | `5df67a2a4565e9cc68ea8588976601e46d24995237cba89d8f90c9c14cd36278` | 1 處（74,976 B，2026-07-16） | 取 `9_ASPICE/01_SYS.1…/CPAA/`，無可比對象 |

PDF 三處副本（`1_Customer_Requirement/CPAA_spec/`、
`9_ASPICE/01_SYS.1 Requirement Elicitation/CPAA/`、
`10_Reviewing/00_TestCase/Bluetooth/REF/`）hash 位元相同，加上 SYS1 xlsx 一件，
恰為裁決所述之「四處副本」。**異 hash 分支未觸發。**

`inputs/` 現有 **34 件**。

### 取檔時另發現的版本歧異（登記，未處置）

`SYS2_HUIG_4_5` 這份 SYSRA 報告在專案樹內有**兩種內容**：

| SHA256 | 大小 | 檔名 | 位置 |
|---|---|---|---|
| `659202c1…` | 247,224 B | `SYS2_HUIG_4_5_FM-WI-FSM-035-A02 …_SYSRA_HUIG_4_5_V01.xlsx` | 4 處（含 `inputs/` 內現用者） |
| `4a049e0c…` | 231,157 B | `SYS2_HUIG_4_5.xlsx` | `9_ASPICE/02_SYS.2 System Requirements Analysis/Projection/` |

檔名不同故非「同名異 hash」，但同指一份 SYSRA 產物。`inputs/` 內用的是
`659202c1…`（4 處一致的那一份）。因 R-P21 已裁定 SYSRA 不作為規格來源，此
歧異不影響任何引用解析，**僅記錄**。

### spec_mode 重評（R-P22 要求）

`spec_mode` 目前為 `[A, B, D]`。HUIG 4.5 補入後的引用量排序：

| 來源 | 列數 | 層級 | 已在 `inputs/` |
|---|---|---|---|
| CFTS085 | 473 | CFTS（mode D） | ✅ |
| Projection Device HMI | 126 | SYS.1 HMI（mode A/B） | ✅ 兩版 |
| CarPlay Addendum R10 | 82 | 供應商規格 | ✅ 三格式 |
| **HUIG 4.5** | **79** | **SYS.1** | ✅ **本次補入** |
| Device Manager HMI | 75 | SYS.1 HMI（mode A/B） | ✅ |
| Pop Up List | 34 | SYS.1 附表 | ✅ |
| CFTS025 | 24 | CFTS | ❌ DR#8 |
| CFTS019 | 16 | CFTS | ✅ |

HUIG 與 CarPlay Addendum 同為 SYS.1 層的**外部供應商／整合規格**，兩者合計
161 列，且都不是「SYS1 匯出 + PDF 成對」的 HMI Logic and Flow 型態。現行
`[A, B, D]` 三碼無法表達這一類來源。**[PROPOSED]**：不擅改 `spec_mode`
字面，改在 `feature.yaml → spec_sources` 記錄完整來源分層，並於 Phase 3
framework Part N 一併裁定是否需要新的 mode 代碼。此項待 Pei。

---

## 0.4 Signed rulings (Pei, 2026-08-12) — R-P23 / R-P24, 逐字

**R-P23**（Layer 3 定義修正）
> Layer 3 之推導以 CFTS085 五碼章節為粒度，四碼僅作為相鄰性判斷之父層。
> 版本沿革章節 `1.3.2.14` ~ `1.3.2.18`（115 列，佔 CFTS085 引用 24%）排除於 Layer 2 同構檢驗之外。該五章按 release 切分，必然橫跨功能，計入將使乾淨叢集被誤判為綑綁。
> 排除僅適用於同構檢驗；該 115 列仍屬正常 TC，其 Layer 3 歸屬另記為 version-track，並於 `framework.md` 標明此分支不參與 §4.1.3 粒度判定。
> **補充**：version-track 這 115 列在 Phase 4 修訂時的 spec 核對對象**仍是那些版本章節**——排除只在框架推導階段生效，不能讓後人以為這批列沒有 spec 依據。

**R-P24**（相鄰性判準）
> Layer 2 之 Layer 3 同構度，以**共同父章節**計算，非以單一章節之主導佔比計算。
> 依據：`Connection` 主導章 `.11.3` 65%，餘 19 列全在 `.11.2`，兩章同屬 `.11 Wireless Projection`，收至四碼即 100%。`Vehicle Signal Forwarding` 同型（`.10.2`／`.10.3` 同屬 Location Data 樹）。
> 單一章節佔比僅在**跨父章**時才構成綑綁證據。

### R-P23 補充條款的落檔位置

「version-track 的 spec 核對對象仍是版本章節」這一句已寫入
`docs/runtime/profiles/FW036_R1L_Projection_Profile.md` §3d 與
`data/layer2_isomorphism.json` 的 `_meta`。**這是最容易被後人誤讀的一點**：
「排除於同構檢驗」與「沒有 spec 依據」是兩件完全不同的事，前者是框架推導的
方法選擇，後者會讓 115 列的修訂失去核對基準。兩處都以明文標示。

### Device Manager 判定（R-P24 交辦之切法）

Pei 交辦：確認落在 `1.3.2.11.3` 的 18 列，其 Test Item 是否為「從 Device
Manager 頁面發起連線」；若是，屬同一 UI 入口的能力，不算綑綁。

**結論：不算綑綁，判定 ✅。** 兩條各自獨立成立的證據：

**證據一 —— 共享 UI 入口，§4.1.3 健康判準滿足。** 那 18 列全部是 Device
Manager 主畫面上的操作，逐列可列舉：device list 顯示、function icon 的
Available／Active 狀態、按 icon 連線／斷線、`Add Device` 鈕、favorite 鈕、
Back 鈕、INFO (i) 鈕。全 54 列對「Device Manager／device list／App drawer／
phone settings」的命中率：

| 章節 | 列數 | 命中共享 UI 入口 |
|---|---|---|
| `1.3.2.11.3` | 18 | **18/18 = 100%** |
| `1.3.2.14`（version-track） | 12 | 12/12 = 100% |
| `1.3.2.8` | 24 | 22/24 = 92% |
| **合計** | **54** | **52/54 = 96%** |

**證據二 —— 那 18 列是協定軸的鏡像對，不是兩種能力。** rows 89–97 為
CarPlay 側 9 列、rows 98–106 為 Android Auto 側 9 列，兩側逐項一一對應
（device list / icon 狀態 / 連線 / 斷線 / 排序 / Add Device / favorite /
Back / INFO）。全 54 列協定分布 CarPlay 23、AA 23、兩者 8 —— 對稱。

**它們落在 `.11.3 Connecting to Wireless Projection` 的原因也清楚了**：按下
function icon 這個動作**確實會發起連線**，所以 CFTS085 把該條需求歸在連線
章節。但 TC 側驗的是「在 Device Manager 畫面上按 icon 會發生什麼」——能力是
畫面操作，連線是它的後果。章節歸屬跟隨需求的**作用**，Layer 2 跟隨測試的
**入口**，兩者在此處分岔屬正常，不是邊界切錯。

18 列的 037 需求原文全部相同：
`For user selection requirements, see the HMI Logic and Flow. 按照客户提供的UI，实现设备列表`
—— 同一條需求，這也再次確認它們是一個單元。

---

## 0.5 Signed rulings (Pei, 2026-08-12) — R-P25 ~ R-P28, 逐字

**R-P25**（補發；Part V §N.2 於落檔時已引用本條，正文延後送達 —— A-PJ28）
> Layer 3 的章節歸屬跟隨需求的「作用」，Layer 2 跟隨測試的「入口」。兩者分岔不必然代表 Layer 2 邊界切錯。
> 判定分岔屬正確或綑綁，以 §4.1.3 之共享 UI 入口為準：入口一致者為同一能力，章節分岔僅反映 spec 依作用歸章。
> 案例：`Device Manager` 之 18 列落在 `1.3.2.11.3 Connecting to Wireless`（按 function icon 會發起連線，spec 依作用歸章），但 TC 驗的是 Device Manager 畫面上的操作，入口一致（54 列中 52 列命中 Device Manager／device list／App drawer／phone settings，96%），故不綑綁。
> 本條與 R-P24 互補：R-P24 處理同父章之分岔，R-P25 處理跨父章但同入口之分岔。

**R-P26**（`HMI Display` 定案）
> `HMI Display` 由暫定綑綁轉為確定綑綁。
> 兩份獨立樣本同向：CFTS085 側 26 列主導 38%、跨 3 章節；HUIG 側 30 列散在 8 子章、跨 4 個頂層章（7 Video / 9 Input devices / 13 Application status / 15 Multi-Display）。合併涵蓋 49/76 = 64%，已過半且雙來源一致。§N.2 的 ⚠️ 收為 ❌，子叢集拆解維持三分。

**R-P27**（`Projection Audio` 方向反轉，判定維持暫定）
> `Projection Audio` 由暫定乾淨轉為存疑（⚠️ 維持，方向反轉）。
> CFTS085 側 50%/3 章節、HUIG 側 11 列散在 3 個頂層章（6 Bluetooth / 8.2.2 Media stream / 10.x ASR），兩份樣本皆不支持乾淨。但涵蓋率僅 62%，未達可判定綑綁的門檻——`HMI Display` 是 64% 且雙來源同向才敢收，這裡證據方向雖同但量不足。維持 ⚠️，待 SYSAD 補完再裁。

**R-P28**（待辦順序）
> 待辦順序改為 SYSAD 優先。
> `SYS3_PROJ` 覆蓋未解 85 列中的 71 列（84%），且在兩個爭議 Set 中佔比最高（`HMI Display` 41/50、`Projection Audio` 25/25 全覆蓋）。`Projection Audio` 剩餘 14 列的 Layer 3 只可能來自 SYSAD——它是唯一能結案的來源。順序：SYSAD 71 → CarPlay Addendum 44 → Projection HMI 11 → CFTS019 10。

### R-P26 / R-P27 的門檻對比（記錄下來，因為它是往後的判準）

兩條裁決的差別**不在證據方向，在證據量**。`HMI Display` 64% / 雙來源同向 →
定案；`Projection Audio` 62% / 雙來源同向 → 維持暫定。兩者只差 2 個百分點，
但差別的實質是絕對列數：`HMI Display` 合併涵蓋 49/76 列，`Projection Audio`
僅 23/37 列。小樣本上的「同向」不足以支撐定案。

### R-P28 的執行結果 —— SYSAD 已推導，但**未能結案 `Projection Audio`**

R-P28 的前提是「`Projection Audio` 剩餘 14 列的 Layer 3 只可能來自 SYSAD ——
它是唯一能結案的來源」。SYSAD 推導已於同日完成，機械上成功（500 列引用中解出
**498 列**），但**對兩個爭議 Set 給不出鑑別證據**。

原因是 SYSAD 的結構與 CFTS085／HUIG 不同類：**它的 `NRL-xxxxxx` 是章節 id，
一節一個，不是需求 id**。500 列引用只落在 **99 個** distinct 章節 id 上，且
高度集中 —— 單一個 `NRL-154702`（`4.6.1 設計目標與需求對映`）就服務
**190 列、橫跨 10 個 Test Set**，其中包含 `HMI Display` 全部 67 列與
`Projection Audio` 全部 37 列。

一個橫跨 10 個 Set 的章節不能用來區分 Set。詳見 A-PJ29。

**因此 `Projection Audio` 仍為 ⚠️**，且 R-P28 所設想的結案路徑不成立 ——
待 Pei 重新指定。CarPlay Addendum（44 列）是下一個候選來源。

---

## 0.6 Signed rulings (Pei, 2026-08-12) — R-P29 / R-P30, 逐字

**R-P29**（Layer 3 鑑別力閘門，取代逐案排除）
> A-PJ26 與 A-PJ29 是同一個缺陷的兩種表現，不該逐案列黑名單。定通則：
> **Layer 3 的推導單位必須具備鑑別力。一個 spec id 若橫跨過多 Layer 2 叢集，即不承載分組資訊，排除於同構檢驗之外。**
> 量化門檻：單一 id 橫跨 Test Set 數 **≥ 6**（18 個之三分之一）者排除。
> 依據 canon §4.1.4 之 Layer 3 四項用途——TC 排序、sibling 辨識、覆蓋度分析、範圍漂移防制——四者皆以「章節劃出的界線小於 Layer 2」為前提。橫跨 10/18 個 Test Set 的 `NRL-154702` 對四者皆無作用。
> 排除僅在框架推導階段生效。該等列之 spec 核對對象仍是原章節；「排除於同構檢驗」不等於「沒有 spec 依據」（同 R-P23 補充條款）。
> 執行方式：對每份來源**逐 id 計算跨 Test Set 數，產出排除清單，不預設哪些章節該排除**。SYSAD 的 `x.y.1 設計目標與需求對映` 預期會落入，但是否還有其他 id 落入須實測——這正是通則優於黑名單之處。
>
> **假集中比假分散危險。** 假分散使乾淨叢集被誤判為綑綁，成本是多切一刀、可回收；假集中使綑綁通過檢驗，缺陷永久留在框架裡。因此鑑別力閘門寧可過度排除。

**R-P30**（`Projection Audio` 結案來源改指）
> R-P28 之「SYSAD 為唯一結案來源」撤銷。實測排除 SYSAD 後，`Projection Audio` 37 列與 `HMI Display` 76 列之非 SYSAD 來源涵蓋率皆為 100%，僅靠 SYSAD 者 0 列。
> `Projection Audio` 結案來源改為四份併用：CFTS019 16 列 / CarPlay Addendum 14 列 / HUIG 13 列（已有）/ CFTS085 12 列（已有）。
> 待辦順序改為：CFTS019 → CarPlay Addendum（CFTS019 覆蓋率最高且列數少，先跑）。

### R-P29 閘門實測結果（門檻 6，五份來源逐 id 計算）

**通則的價值當場證實：實測只排除一個 id，且比執行端原先提的黑名單更精準。**

| 來源 | 推導單位數 | 排除 | 觸及列數 |
|---|---|---|---|
| CFTS085（五碼章節） | 25 | **0** | 0 |
| HUIG（章節） | 26 | **0** | 0 |
| CarPlay Addendum（章節） | 18 | **0** | 0 |
| CFTS019（章節） | 1 | **0** | 0 |
| **SYSAD（章節）** | 34 | **2** | 277 |

SYSAD 落入者：`4.6.1 設計目標與需求對映`（197 列 / 跨 **10** Set）、
`4.2.1 設計目標與需求對映`（80 列 / 跨 **6** Set）。

執行端先前提議「三個 `設計目標與需求對映` 型章節全數排除」是**過度排除**：
第三個 `4.5.1`（11 列）只跨 3 個 Set，通過閘門且確實有鑑別力。通則比黑名單
精準，R-P29 的立論成立。

### ⚠️ 但閘門**不涵蓋** A-PJ26 的 version-track

R-P29 的前提之一是「A-PJ26 與 A-PJ29 是同一個缺陷的兩種表現」。**實測不支持
這一句。** 在 R-P23 裁定的五碼粒度下，version-track 五章全部**通過**閘門：

| 章節 | 列數 | 跨 Set 數 | 閘門判定 |
|---|---|---|---|
| `1.3.2.14 SR20+ Apple Certification Changes` | 85 | **4** | **通過** |
| `1.3.2.15` | 3 | 1 | 通過 |
| `1.3.2.16` | 10 | 1 | 通過 |
| `1.3.2.17` | 15 | 2 | 通過 |
| `1.3.2.18` | 2 | 1 | 通過 |

兩者是**不同機制**，不是同一缺陷的兩種表現：

| | A-PJ26 version-track | A-PJ29 需求對映表 |
|---|---|---|
| 排除理由 | **語意**——按 release 切分，不按功能 | **結構**——無鑑別力 |
| 偵測方式 | 讀章節標題（`SR20+ …Changes`） | 計算跨 Set 數 |
| 造成 | 假分散 | 假集中 |
| R-P29 閘門 | **抓不到**（最高 4 Set） | 抓得到（6 / 10 Set） |

**因此 R-P23 的 version-track 排除條款仍須獨立存在**，不能由 R-P29 取代。
兩條併行：R-P29 是結構性閘門（機械可算），R-P23 是語意性排除（須讀標題）。
未自行合併或改寫任一條，待 Pei 裁定是否要為語意性排除也定一條通則。

### R-P30 執行結果 —— `Projection Audio` 已可結案

CFTS019 與 CarPlay Addendum 均已推導（方法各自探測後決定，見 framework
§N.9）。排除 SYSAD 後 `Projection Audio` 的 Layer 3 涵蓋率為 **36/37 = 97%**
（唯一無證據者為 row 521，屬 PCTS/MT1 列）。章節分布：

| 章節 | 列數 |
|---|---|
| **CFTS019 `1.3.3.1 Source Priorities`** | **16** |
| Addendum `3.2.7.2 Audio`（含 Mixing / Ducking / Main Audio 四支） | 12 |
| Addendum `3.3.3 Resource Management` | 8 |
| HUIG `6 Bluetooth` | 5 |
| HUIG `8.2.2 Media stream` | 3 |
| HUIG `10.x ASR` | 3 |

R-P30 的語意判斷得到證實 —— **CFTS019 確實是 `Projection Audio` 的主要 Layer 3
來源**，且其 16 列全數落在單一章節 `1.3.3.1 Source Priorities`（跨 1 個 Set）。
加上 Addendum 的 `3.2.7.2 Audio` 樹 12 列（依 R-P24 同父章），兩者合計 28 列
集中在兩個語意明確的音訊章節。判定建議見 framework §N.9，**未自行改寫
§N.2 的 ⚠️**，待 Pei 裁。

---

## 0.7 Signed rulings (Pei, 2026-08-12) — R-P31 ~ R-P33, 逐字

**R-P31**（兩道閘門並存，互不涵蓋）
> R-P29 之立論「A-PJ26 與 A-PJ29 為同一缺陷之兩種表現」撤銷。實測：version-track 五章在五碼粒度下跨 Test Set 數為 4/1/1/2/1，全數通過 R-P29 門檻。兩者機制不同：
>
> | 閘門 | 量什麼 | 判定方式 | 對應裁決 |
> |---|---|---|---|
> | 結構閘門 | 界線夠不夠細（跨 Set 數 ≥ 6 排除） | 機械可算 | R-P29 |
> | 語意閘門 | 界線切的方向是否為功能 | 須讀章節標題，人工判定 | R-P23 |
>
> **兩道閘門並存，不得合併、不得以其一涵蓋其二。** R-P29 之排除條款與 R-P23 之 version-track 排除各自獨立生效。
> R-P29 之其餘部分（門檻值、通則優於黑名單、假集中比假分散危險、排除僅在推導階段生效）維持有效。

**R-P32**（語意閘門定為通則，但不自動化）
> Layer 3 之推導單位，其章節界線須沿功能切分。界線依其他維度切分者——時間／release、文件管理、跨領域對映表——縱有鑑別力，仍排除於同構檢驗之外。
> **判定方式為人工閱讀章節標題與內容，逐案登記理由，不得以字串規則自動化。**「標題含 release 標記者排除」之類的啟發式會誤傷真正的功能章節（功能章節標題亦可能含版本標記），且無法涵蓋未預期的非功能切分維度。
> 已登記之語意性排除：CFTS085 `1.3.2.14` ~ `1.3.2.18`（version-track，R-P23）。
> 新增語意性排除時，須同時記載：**章節 id、列數、切分維度、以及為何該維度非功能**。

**R-P33**（`Projection Audio` 收為 ✅）
> 涵蓋率由 32% 提升至 97%（36/37），唯一無證據之 row 521 為 PCTS／MT1 列，屬 R-P11 凍結區，非證據缺口。
> 依 R-P24 收斂後，28 列集中於兩個語意明確之音訊章節（CFTS019 `1.3.3.1 Source Priorities` 16 列跨 1 Set、Addendum `3.2.7.2 Audio` 樹 12 列跨 1 Set），另 Addendum `3.3.3 Resource Management` 8 列、HUIG 3 章 11 列，全部跨 1–2 Set。
> 依 A-PJ30 之絕對列數門檻：36 列遠高於暫定時之 23 列。
> 判定：**✅ 乾淨叢集**。
>
> **A-PJ06 關閉。** Layer 2 定案：**16 乾淨 + 1 橫切（`Performance`）+ 1 綑綁（`HMI Display`）**。

### 兩道閘門的分工，及其不可自動化的一半

R-P31 / R-P32 合起來確立了 Layer 3 推導的雙閘門結構：

```
推導單位 → [結構閘門 R-P29：跨 Set 數 ≥ 6 ?] → [語意閘門 R-P23/R-P32：界線沿功能切 ?] → 進入同構檢驗
                機械可算，每輪自動執行              人工讀標題，逐案登記理由
```

**R-P32 明文禁止把語意閘門自動化，理由在裁決文字裡**：字串啟發式會誤傷標題
含版本標記的真功能章節，且無法涵蓋未預期的非功能切分維度。這一點須寫進
framework Part V，否則後人會試圖補上「自動化」這塊看似缺失的拼圖。

本專案至今的鑑別力對比，說明兩個閘門各自的必要性：

| 推導單位 | 服務列數 | 跨 Set | 結構閘門 | 語意閘門 |
|---|---|---|---|---|
| CFTS019 `1.3.3.1 Source Priorities` | 16 | **1** | 通過 | 通過 |
| CFTS085 `1.3.2.14 SR20+ …Changes` | 85 | 4 | **通過** | **排除**（按 release 切） |
| SYSAD `NRL-154702 4.6.1 需求對映` | 190 | **10** | **排除** | （已排除） |

第一列與第三列的鑑別力相差三個數量級 —— 前者一個 clause 服務一個 Set 的
全部相關列，這是 Layer 3 應有的形狀；後者一個章節服務 190 列橫跨 10 個 Set。
第二列則是只有語意閘門攔得住的那一類。

---

## 0.8 Signed rulings (Pei, 2026-08-12) — R-P34 / R-P35, 逐字

**R-P34**（pilot 選定）
> Phase 4 pilot 批次選定 `Vehicle Signal Forwarding`（22 列，r151–r236）。
> 選定依據為機制覆蓋度而非列數：該批同時觸及 L-PJ1 解析成功（CAN-B）、L-PJ1 應拒收（R-P9 未解訊號）、L-PJ2 PROXI 值域（R-P8′）、O-3 有手冊工具（CarPlay Tests / ATS）、O-3 無手冊工具（mobile GAL log）、L-PJ5 禁用動詞，且 **PCTS 命中 0 列**——不觸及 R-P11 凍結區，pilot 之失敗皆為真失敗。
> 對照組 `Day/Night Mode` 22 列為單一訊號重複、全部範圍外、零缺陷，資訊量不足，不採。

**R-P35**（範圍外列仍須修訂）
> Remarks 標記 `Not in ASW-R1 Release Scope` 之列**仍在修訂範圍內**。該標記為執行阻塞，非修訂阻塞——FW036 為規範與結果並存之交付物，TC 文字之正確性不因該版不執行而豁免。
> 唯一無條件不修訂者為 `feature.yaml → done_region.frozen_rows`（r376–379）與未取證之 PCTS 列（R-P11）。
> 本 pilot 中受此條影響者 5 列：r151, r152, r167, r168, r235。

### R-P34 的選定理由當場兌現

pilot 的價值在於**兩個方向都被證明**：gate 會放行有依據的寫法，也會擋住無依據的。
本批 22 列中 **13 列修訂、9 列維持不動**，而那 9 列裡有 8 列是「依規則不得動」
而非「沒做完」：

| 未動原因 | 列 | 依據 |
|---|---|---|
| 工具無手冊 | r231–r234（mobile GAL）、r222–r224（logcat） | O-3 |
| 查無 spec 依據 | r230 | O-4 / §2.4 |
| 手冊核實後確認無誤 | r219 | —— 正向結果 |

**r151/r152 的拒收是本 pilot 最重要的一項結果。** L-PJ1 的檢驗方式是
「Procedure 內不得出現任何 `message.signal`」，實測 2/2 通過拒收檢查 ——
若當時寫入三候選之一，gate 會 ABORT。這證明 R-P9 不是一句宣示，是可執行的
約束。

---

## 0.9 Signed rulings (Pei, 2026-08-12) — R-P36 ~ R-P38，pilot review, 逐字

**R-P36**（步數對齊為硬性約束）
> Procedure 之步數必須等於凍結之 ER 行數。ER 依 O-1 凍結，1:1 對齊（canon §6）因此成為**硬性約束而非慣例**。
> 改寫得重寫步驟文字、合併敘述、加長單一步驟（canon §5.2 B/C 允許 ≤18 字），**不得增刪步驟**。
> 若某列之可執行性確實需要更多步驟，該列轉 RD-1，不得逕改。
> 基線：555/558 列（99%）現為嚴格 1:1。

**R-P37**（ER 分歧不予修正，逐列登記）
> ER 凍結導致之 Procedure↔ER 術語／機制分歧，**不予修正，逐列登記**。
> 分歧不視為缺陷，係 O-1 之必然後果。**RD-1 提問須同時涵蓋 ER，不得只問 Procedure**——r151/152 之 ER 本身即含無依據之機制斷言。
> 登記於 `data/er_divergence.json`，供 RD-1 與後續版本一次性處置。

**R-P38**（平台標準工具之界線）
> 平台標準工具（`logcat`、`adb` 等）之**啟動與讀取方式屬公知，不需手冊即可撰寫**；但其**產品專屬參數**（過濾 tag、訊息格式、欄位名稱）仍受 O-3 拘束，無依據不得填寫。
> 因此 r222–224 維持現況為正確處置：步驟已寫到公知介面所能支持的層級，缺的是產品專屬過濾條件。DR#12 保留該項。

### D-1 修復與複驗（2026-08-12）

**基線複驗**：全簿 558 個可比列中 **555 列（99.5%）**Procedure 步數等於 ER
行數，不等者僅 3 列（r184 5/4、r355 5/4、r517 5/9）。**1:1 是這個簿子的實際
結構，不是慣例。** R-P36 的立論成立。

r167/168 依 D-1 折回 2 步，並移除 `until step 3 has been read` 之前向引用：

```
1. Send CAN on CAN-B: STATUS_BH_BCM1.LowFuelWarningSts = 1 (ON) and keep it at 1 (ON) for the remainder of the test
2. Read the CarPlay projection UI and check that the low fuel indicator is displayed
```

持續時間仍為可觀察形式、未自訂數值。**複驗結果**：22/22 列 L-PJ8 對齊通過、
L-PJ1 通過（`STATUS_BH_BCM1.LowFuelWarningSts=1` → CAN-B，`VAL_ 0 OFF / 1 ON`）、
R-P9 拒收 2/2 通過、無任何前向或回頭指涉。

### R-P37 登記結果 —— 分歧範圍比預估的窄，但嚴重度分佈更清楚

`data/er_divergence.json` 逐列掃描全簿，**登記 35 列**，分兩類：

| 類型 | 列數 | 內容 |
|---|---|---|
| `mechanism_assertion` | **2**（r151, r152） | ER 斷言一個依 R-P9 判定無依據的機制 —— 「HU receives signal `$HCP_DISP2.Est_Range_BEV$` on the CAN bus」 |
| `terminology` | **28** | ER 使用 SWE1 邏輯名或匯流排上不存在的標籤（如 `$FuelLvlLow$ = Active`），Procedure 已改為 DBC 原文 |
| （僅提及 CAN、無 token） | 5 | 不構成分歧，一併記錄供比對 |

**兩類的 RD-1 提問方式不同**：`terminology` 是同一件事的兩種寫法，問的是
「ER 是否隨版本更新為匯流排實名」；`mechanism_assertion` 是 ER 主張了一個
我們判定無依據的機制，問的是「這個訊號到底是什麼」—— 後者若不問 ER，
RD-1 會漏掉問題的一半。這正是 R-P37 那句「不得只問 Procedure」所指。

### R-P38 的界線，可推廣形式

R-P38 與 ATS 那 5 列的處理方式是同一條界線的兩面：

| | 有依據（可寫） | 無依據（不可寫） |
|---|---|---|
| ATS | **怎麼過濾** —— traffic view + 工具列 Filter 欄（手冊 §6.1.2 / p27） | **過濾什麼** —— 但 `GPRMC` 等字串本就是簿內既有 test data，非新增 |
| logcat | **怎麼啟動與讀取** —— 平台公知 | **產品專屬過濾 tag** —— 無依據 |

**界線落在「介面」與「內容」之間**：工具怎麼操作可由手冊或公知支持；要找的
東西是什麼，必須來自 spec 或簿內既有 test data。此條已寫入 profile。

---

## 0.10 Signed rulings (Pei, 2026-08-12) — R-P39 / R-P40，B2 review, 逐字

**R-P39**（步驟交叉指涉不構成缺陷 —— 更正分析層之過寬表述）
> 步驟交叉指涉**不構成缺陷**。canon §5.2 未禁止之。
> 構成缺陷者為**前向指涉造成之循環順序**——步驟 N 之完成條件依賴步驟 N+k，而 N+k 為驗證步。此為**可執行性缺陷**，非引用形式缺陷。
> 全簿 30 列具 `Repeat steps N and M` 形式之回頭指涉，**一律不動**。
> 本條更正 Phase 4 pilot review 中分析層對 §5.2 之過寬表述。

**R-P40**（工具計數定義）
> `工具` 欄**不含 PCTS**，PCTS 另立一欄。理由為 PCTS 受 L-PJ7 證據綁定管制，與其他工具之管制機制不同，混計會**遮蔽 L-PJ7 的暴露面**。

### R-P39 的實測支持 —— 30 列全為回頭指涉，零前向

| Test Set | 列數 |
|---|---|
| Disconnection | 11 |
| Connection | 5 |
| Device Manager | 5 |
| Projection Audio | 3 |
| Projection Launch | 2 |
| Day/Night Mode | 2 |
| Cluster Navigation | 2 |
| **合計** | **30** |

分布逐項與裁決所述相符。更重要的是**方向分析**：逐行比對「引用的步號 vs 該行
自身步號」，**30 列全部是回頭指涉（N 指向 < N），前向指涉 0 列**。

這反過來確證 D-1 的缺陷是一個**特例**而非通例：`until step 3 has been read`
是全簿唯一的前向指涉，而且它指向的正是驗證步 —— 步驟 2 要等步驟 3 完成，
步驟 3 又是最終判定，形成循環。**D-1 的修復本身仍然正確，被更正的是它的
理由。**

常見形式也說明為何不能動：`as recorded in step N`（15 列）、
`the same as recorded in step N`（5 列）—— 這些是比對型步驟的必要成分，
移除會使步驟失去比對對象。

### r177/r188 已還原，但分類維持 22/0/0

`Repeat steps 3 and 4` 原文已還原。**惟該兩列仍屬「改對了」而非「核實無誤」**
—— 它們的步驟 3/4 另有 token 需解析：

```
前：3. Trigger $Day_Night_Mode$ = Night via CAN tool, record T1 …
後：3. Send CAN: BCM_FD_27.DAY_LGT_MD_DISP = 0 (Night), record T1 …
```

B2 分類維持 **改對了 22 / 核實無誤 0 / 正確地不動 0**。

另記一項：`per direction` **是原文既有的**（`before` 內即含此詞），非改寫時
新增，故無 O-4 疑慮。

---

## 0.11 Signed rulings (Pei, 2026-08-12) — R-P42 ~ R-P44，B3 review, 逐字

**R-P42**（L-PJ9 採用）
> **L-PJ9 採用（flag，非 ABORT）。**
> 條件：PRE 含 `Test equipment for` / `test setup for` / `analyzer for` / `equipment for measuring` **且** Procedure 無具名工具路徑 → flag。
> 全簿命中 7 列（PRE 泛稱 8 列，扣除 r112 有具名路徑者）。全部落在 `Performance`。
> flag 之處置為**維持不動 + 開 DR**，不得自行指定設備。

**R-P43**（L-PJ10 採用，兩類須先分開）
> **L-PJ10 採用（flag），兩類須先分開。**
> **缺陷類**：`<TBD>`、`<configured …>` —— 值應由 spec 提供而未提供。5 列（r36 / r111 / r124 / r149 / r225），flag 並轉 RD-1。
> **參數類**：`<Device Name>`、`<Apple CarPlay OR Android Auto>` —— 值由執行者於執行時代入，非缺陷。8 列（r60 / r61 / r317–r322），白名單排除。
> 白名單以**列舉**維護，不以樣式推斷；新增參數形式須逐案登記。

**R-P44**（L-PJ11 暫緩）
> **L-PJ11 暫緩，改為 B5 的人工檢核項。**
> 全簿 `Tap/Select 清單項` 命中 16 列，其中 **14 列在 `Knob`（B5）**，B3 僅 4 列。以 4 列樣本寫規則將嚴重過擬合；B5 執行時樣本增為 18 列，且 `Knob` 為單一能力叢集，可判斷該寫法是慣例或疏漏。
> B5 執行時**逐列人工檢核** PRE 是否保證清單內容存在，並記錄判定與理由；B5 上繳後再裁 L-PJ11 是否成立、以及規則形式。
> 在此之前，A-PJ41 的 4 列維持不動（spec 未載明，依 §3.1 不自補）。

### R-P44 的實測支持 —— 命中數完全取決於規則怎麼寫

同一個概念，三種寫法給三個數字：

| 規則形式 | 命中 | PRE 無保證 | 分布 |
|---|---|---|---|
| A. 名詞列舉（6 個名詞，執行層上輪所用） | 20 | **5** | Device Manager 2 / Projection Apps 2 / Disconnection 1 |
| B. A + 加入 `song` | 34 | **19** | **Knob 14** / Device Manager 2 / Projection Apps 2 / Disconnection 1 |
| C. 以 `in the list` 錨定（分析層所用） | 16 | **16** | **Knob 14** / Projection Apps 2 |

**裁決所述之 16 列在寫法 C 下完全重現**（Knob 14 + Projection Apps 2）。
執行層上輪報 4 列，是因為名詞清單漏了 `song` —— `Tap a song in the list to
highlight it` 在 `Knob` 出現 14 次。

**這正是 R-P44 該緩的理由，而且比預期更強**：不是「樣本太小所以規則不準」，
而是**規則的寫法本身就決定了樣本大小**。5／19／16 三個數字都不是錯的，它們
量的是三個不同的東西。在樣本到齊前先定規則，等於先射箭再畫靶。

### r60/r61 的漏掉原因 —— 掃描範圍（canon §5a 第四條）

執行層掃 `PRE + Procedure`（**可編輯欄**），分析層掃含 ER。r60/r61 的
`<Device Name>` 出現在 **ER 欄**：

```
r60 ER: 2. The popup displays "<Device Name> detected. Do you want to…
```

兩邊都對。**但此處的差異有實務意義**：ER 凍結，該佔位符即使判為缺陷也改不
掉，故列入參數類白名單（8 列）不影響處置。分類不變 —— 缺陷類仍為 5 列。

### r112 證明 L-PJ9 的雙條件設計是必要的

r112 的 PRE 有泛稱（`An audio analyzer for measuring sampling rate
deviation`），但 Procedure 有具名路徑（`Utilities > Audio Utilities >
Sample Rate`，手冊 p32）。**單看 PRE 會多抓這一列**；兩條件並用才得到正確的
7 列。

---

## 0.12 Signed rulings (Pei, 2026-08-12) — R-P45 / R-P46，B4 review, 逐字

**R-P45**（PRE 矛盾之更正門檻）
> PRE 與 Procedure／ER 矛盾時，**僅在 ER 逐字陳述該狀態時方得更正 PRE**；僅有邏輯蘊含者維持不動。
> 依據：ER 依 O-1 凍結且為權威；逐字陳述構成 spec 級證據，邏輯蘊含則是推論。
> **兄弟列不構成證據。** r140 之對照列 r145 的 PRE 有 `An Android Auto VR session is active` 而 CarPlay 列沒有，高度像疏漏——但兄弟列不是 spec，依 O-4 不採（canon §8.4.1）。

**R-P46**（L-PJ9 改為可增補清單）
> **詞彙型 gate 之樣式清單不追求一次寫全。** 每批發現新樣式即登記並重跑全簿，重新記錄基線列數。
> L-PJ9 樣式擴充：新增 `trace tool` / `capture tool` / `simulator`，雙條件命中由 7 列增為 **10 列**（新增 r141 / r142 / r147）。其餘 9 列因 Procedure 具名 ATS／CAN tool 而正確排除——雙條件設計再次證明必要。
> 每次擴充須記錄：**新增樣式、擴充前後命中數、新增命中列**。

### L-PJ9 樣式擴充記錄（R-P46 要求之格式）

| 日期 | 新增樣式 | 擴充前 | 擴充後 | 新增命中列 |
|---|---|---|---|---|
| 2026-08-12（B4） | `trace tool` / `capture tool` / `simulator` | 7 | **10** | r141, r142, r147 |

---

## 0.13 Signed rulings (Pei, 2026-08-12) — R-P47 / R-P48，B5 停下處置, 逐字

**R-P47**（PROXI 為單車型文件）
> `PROXI_HDCC27_R3_20250424.xlsx` 為 **HDCC27 單一車型之配置檔**（Header: `HDCC27 - Draft`），非全車系配置字典。
> 因此 R-P20（PROXI 為值域權威）之適用範圍**限於 HDCC27**。跨車型之前置條件無法以本檔驗證，**L-PJ2 對非 HDCC27 車型不適用，不得據以判違規，亦不得據以放行**。
> 本條更正 R-P20 之隱含前提——當時未察 PROXI 為單車型文件。

**R-P48**（L-PJ11 不採用）
> `Knob` 14 列 `Tap a song in the list to highlight it` 逐字相同、PRE 保證清單內容者 0/14——**完全一致即為慣例，非疏漏**。L-PJ11 不採用為 gate。
> 跨叢集不一致（`USB Device` r458 明寫資料狀態，`Knob` 14 + `Projection Apps` 2 未寫）改列 **RD-1 風格問題**，不作缺陷。同簿內兩種慣例並存屬既有書寫差異，非本 phase 可裁。
> **A-PJ41 CLOSED。**

### R-P47 的證據複驗

PROXI `Header` 分頁第 4 列逐字為 **`HDCC27 - Draft`** ✅ —— 單車型文件確認。

workbook 第 3 列的 7 個車型欄與 B5 的 7 個值**逐一對應**，且**架構分層完全
吻合**：

| 車型欄 | 值 | 架構 | PROXI 可解 |
|---|---|---|---|
| S `HDCC27 Atl-Hi` | `HDCC27` | **Atl-Hi** | 輪廓對得上（標籤 `HDCC` = 130） |
| T `DT27 Atl-Hi` | `DT27` | **Atl-Hi** | 輪廓對得上（標籤 `DT` = 124） |
| U `VF(ProMaster)637 Atl-Mi` | `637` | Atl-Mid | ❌ |
| V `Commander (598) Atl-Mi` | `598` | Atl-Mid | ❌ |
| W `Regengade (5210) Atl-Mi` | `5210` | Atl-Mid | ❌ |
| X `Toro(2261) Atl-Mi` | `2261` | Atl-Mid | ❌ |
| Y `Fastack (376) Atl-Mi` | `376` | Atl-Mid | ❌ |

**5 個對不上的全是 Atl-Mid，2 個對得上輪廓的全是 Atl-Hi** —— 這不是巧合。
profile §4 明訂訊號解析取 mapping 表的 **Atlantis High** 欄
（`CAN Mapping` 26–30 / `Proxi & Configuration` 16–20），**Atlantis Mid
車型從一開始就在本專案的解析基礎之外**。

**這是 R-P20 的第二次修正**：第一次是 R-P8′ 揭露 mapping 列舉截斷，這次是
PROXI 為單車型。**兩次同一個盲點 —— 把手上唯一的那份檔案當成該類文件的全部。**

### A-PJ45 影響範圍複驗 —— 止於 Knob 42 列，B6/B7 不受牽連

全簿掃描 `PROXI VC_Veh_Line = <值>`：**命中 42 列，全部在 `Knob`**，7 個值
各 6 列。**Atl-Mid 30 列、Atl-Hi 12 列**，與裁決所估相符。

B6／B7 的 PROXI 命中經查為**不同型**，全部可在 HDCC27 檔內解析：

| Test Set | PROXI 用法 | 列 | 參數存在 | 值域 |
|---|---|---|---|---|
| Projection Detection | `Projection_Mode = 1 (Present)` | 4 | ✅ | ✅ |
| | `Projection_Mode_Selection = 0` | 2 | ✅ | ✅ |
| Disconnection | `Wi-Fi_Cfg = 1 (Present)` | **13** | ✅ | ✅ `0 = Absent 1 = Present` |
| | `USB_Presence = 2 (2 USB)` | 1 | ✅ | ✅ `2 = 2 USB` |

**B6／B7 無連帶阻塞，可照常開批。**

---

## 0.14 Signed ruling (Pei, 2026-08-12) — R-P49，B8 review, 逐字

**R-P49**（比對式共用，不重寫）
> 詞彙型 gate 之比對式須**單一實作、跨批共用**，批次腳本一律引用**不得重寫**。
> 任何比對條件（詞界、大小寫、掃描範圍）之變更**只在該單一實作處進行**，變更後重跑全簿並更新基線。
> 依據：A-PJ38 於 L-PJ5 修正詞界時加入 `re.I`，B6/B7/B8 之批次腳本重寫該式時漏失，造成假陰性（A-PJ48）。**條件正確但實作分散，等同未修正。**

### R-P49 落實 —— `features/projection/scripts/lint_defs.py`

單一實作已建立，B9 起所有批次腳本 `import lint_defs`，不再自行撰寫比對式。
模組內含：

- `RE_BANNED`（L-PJ5，詞界 + `re.I`）、`RE_VAGUE`（L-PJ6，詞界 + `re.I`）
- `RE_CAN`（**刻意大小寫敏感** —— A-PJ37：`re.I` 會命中英文助動詞 `can`）
- `RE_GENERIC_TOOL` + `RE_NAMED_TOOL`（L-PJ9 雙條件，樣式為 R-P46 之可增補清單）
- `RE_PLACEHOLDER` + `PLACEHOLDER_WHITELIST`（L-PJ10，白名單為列舉非樣式推斷）
- `RE_STEP_XREF` + `forward_xrefs()`（R-P39：回頭指涉合法，只有前向循環是缺陷）
- `SCAN_RISK` / `SCAN_EDITABLE`（canon §5a 第四條：掃描範圍須言明）
- `BASELINE`：七項全簿基線值

**基線複驗（2026-08-12，全簿 r4–r561）—— 八項全數重現**：

| 項目 | 基線 | 實測 |
|---|---|---|
| L-PJ5 禁用動詞 | 5 | **5** ✅ |
| L-PJ6 模糊語 | 10 | **10** ✅ |
| L-PJ9 泛稱工具 | 10 | **10** ✅ |
| L-PJ10 缺陷類佔位符 | 5 | **5** ✅ |
| L-PJ10 參數類佔位符 | 8 | **8** ✅ |
| 步驟交叉指涉 | 30 | **30** ✅ |
| 步數 != ER 既有例外 | 3 | **3** ✅ |
| 前向循環指涉 | 0 | **0** ✅ |

模組的 docstring 逐字記載了 R-P49 的理由 ——「條件正確但實作分散，等同未修正」
—— 讓下一個改動它的人先讀到為什麼不能複製貼上。

---

## 0.15 Signed ruling (Pei, 2026-08-12) — R-P50，批次結構變更, 逐字

**R-P50**
> 原 Phase 5 批次計畫之 B10–B14 合併為兩批：**B10′（機制批）**與 **B11′（清查批）**。
> 依據：B3–B9 六批 216 列僅變更 6 列（2.8%），且變更全部集中在 CAN／PROXI／token／工具路徑四種機制。以 Test Set 分批之邊界在 Phase 5 未發揮作用——B6／B7／B9 之批次結論皆為「乾淨叢集、無範圍歸屬疑義」，Layer 3 未攔下任何修訂決定。
> 批次排序實際採用之依據自始為風險矩陣（機制命中數），非三層框架。framework 之產出對交付物（ASPICE SWE.6 追溯）仍屬必要，但不應決定 Phase 5 之批次結構。
> **本變更不放寬任何 gate、不降低逐列嚴謹度**，僅改變分批邊界。

### §5 預期數字對照 —— 實測等於**原 Phase 5 §1 風險矩陣的逐欄加總**

| 欄 | 原表加總 | B10′ §5 | 實測 | |
|---|---|---|---|---|
| PCTS | 21 | 19 | **21** | 實測 = 原表 ✅ |
| CAN | 13 | 13 | **13** | ✅ |
| PROXI | 12 | 12 | **12** | ✅ |
| token | 16 | 12 | **16** | 實測 = 原表 ✅ |
| 模糊語 | 9 | 9 | **9** | ✅ |
| 禁詞 | 2 | 1 | **2** | 實測 = 原表 ✅ |
| 凍結 | 4 | 4 | **4** | ✅ |
| **剩餘列數** | **195** | **173** | **195** | 實測 = 原表 ✅ |

七項機制與列數**全部等於原表加總**；B10′ §5 於 PCTS／token／禁詞三項與列數
一項與之不符，屬轉錄與算術落差，非量測分歧。B10′ 實際列數 44（非 50–60）
—— 因多數列同時命中多個機制。B11′ 因此為 151 列（非約 115）。

---

## 0.16 Signed ruling (Pei, 2026-08-12) — R-P51，L-PJ1 權威來源擴充, 逐字

**R-P51**
> L-PJ1 之權威來源擴充為 **DBC ∪ VF176 逐訊號登記表**。
> VF176 為文件而非 DBC，**不建自動萃取管線**（受影響僅 5 列，建管線不成比例）。改採**逐訊號人工登記**：每個 VF176 訊號於 `signal_map.json` 新增條目，標 `authority: "VF176"`、`vf176_section`、`verified_manually: true`，並登記其值定義（VF176 有列舉則登記，無則 `enum: null`）。
> L-PJ1 對已登記者放行，**未登記者一律 ABORT** —— gate 不被繞過，只是承認第二個權威來源。
> 適用：Cluster Navigation 5 列（frozen r376–379 不受影響，仍無條件 ABORT）。

### 執行結果

**來源檔 hash 比對** —— `c92cc3ddda2cd87a75f1a0882d011b0b7e36876f6dd99044e1ba7683fa686c3d`，
與 Phase 0 `[AUTO]` 區塊記錄**完全相符** ✅，未觸發停下分支。

**萃取方法（先探測後決定）** —— docx 為表格型：11 個表、以 pStyle 分層
（`1`/`21`/`31`/`41`/`51`）、**無數字編號標題**。故不套用 CFTS085／SYSAD 的
「數字編號標題追蹤」，改以「表格內容 + pStyle 上文」定位。這是第六種方法。

**登記 7 個訊號**（`signal_map.json → vf176_signals`）：

| 訊號 | enum | 可寫程度 |
|---|---|---|
| `TELEMATIC_NAV_INFO.Direction` | **38 項**（ID → Navigation Name） | 值 (標籤) |
| `TELEMATIC_NAV_INFO.ResolutionDistToTurn` | **3 項**（`One` / `ZeroPointOne` / `ZeroPointZeroOne`） | 值 (標籤) |
| `TELEMATIC_NAV_INFO.DistToTurn` | ❌ 連續量 | **僅名稱** |
| `TELEMATIC_NAV_INFO.Unit` | ❌ 未列舉 | **僅名稱** |
| `TELEMATIC_DISPLAY_INFO.UTF_Text_1/2/3` | ❌ 文字 | **僅名稱** |

下放包 §2.4 之預期（`DistToTurn`／`ResolutionDistToTurn`／`Unit` 為連續量）
**部分成立**：`DistToTurn`／`Unit` 確為連續量／未列舉，但
**`ResolutionDistToTurn` 有列舉**（VF176 逐字 `set to "One"` / `"ZeroPointOne"`
/ `"ZeroPointZeroOne"`，以標籤陳述而無數值代碼）。

**gate 擴充驗證**（`lint_defs.resolve_signal()`，單一實作 R-P49）：

- 5 列之訊號全部解析為 `authority=VF176` ✅
- **負向驗證**：`TELEMATIC_NAV_INFO.LastAnnouncement`（VF176 有定義但**未登記**）
  → **ABORT** ✅；`FAKE_MSG.FakeSig` → **ABORT** ✅
  —— **gate 未被繞過**

**5 列最終判定為「核實無誤」，零變更。** 原因是它們全部是 **READ 操作**
（讀值比對），不是 SEND —— 訊號名稱本就正確，無值可填亦不需填。R-P51 解決的
是 gate 會誤 ABORT 它們，不是簿子有錯。

### L-PJ9 樣式擴充記錄（R-P46，第二次）

| 日期 | 新增樣式 | 擴充前 | 擴充後 | 新增命中列 |
|---|---|---|---|---|
| 2026-08-12（B4） | `trace tool` / `capture tool` / `simulator` | 7 | 10 | r141, r142, r147 |
| **2026-08-12（B10′）** | **`A method to`** | **10** | **15** | **r541, r542, r543, r544, r545** |

`lint_defs.BASELINE["L-PJ9 generic tool"]` 已由 10 更新為 **15**。
r541／r543／r544／r545 因此由 B11′ **重分類**併入 B10′ —— 屬 **gate 擴充導致**
之重分類，非分類條件錯誤（原分類時 gate 尚未涵蓋該樣式）。

## 1. Intake

- spec_mode: `[AUTO: A, B, D]` — fixed by the `spec_reference` column's own
  citations: `CFTS085` on 473 of 559 rows (mode D), the two SYS1 HMI Logic and
  Flow documents on 172 rows combined (modes A/B). The spec line runs through
  all three at once; no single mode describes it.
- workbook_state: `[AUTO: FULL_REFINE]` — a state canon §2 does not define.
  See §2 below and profile §1.
- Spec release/version pinned: `[AUTO]` — Projection Device HMI Logic and Flow
  (February 5 2026); Device Manager HMI Logic and Flow R1 SR24 Post 2A
  (March 13 2023); CFTS085 25PI3.5 export 20250910_1704; PROXI HDCC27 R3
  20250424; CAN mapping v1_76.
- Missing referenced specs: `[AUTO]` — PCTS Verifier manual (DR#1),
  `Est_Range_BEV` LID mapping (DR#2), `Vehicle_Line_Configuration` 332
  definition (DR#3), `Accessory_Interface_Specification_CarPlay_Addendum_R1`
  (DR#6, cited by 80 rows). Each has a DATA_REQUESTS row and an anomaly.

### [AUTO] Source files present — SHA256

All 25 files copied from the R-P5 root on 2026-08-11 into
`features/projection/inputs/`. Sources are read-only and were not modified;
`cp -p` preserved timestamps. Hashes are of the copies, which is what the
pipeline reads.

| SHA256 | file |
|---|---|
| `11579c9b3b8e56eb9f25a06acd2ce9281409286248a37b327be4732cc0bdede9` | `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` |
| `ad7d0abc148e170a810afbc8b61f048ddcb2106ec21a7869cb7426e64c8a08c6` | `FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA-CPAA_0521.xlsx` |
| `2f836a27029a17dcc7b75d504d36537cc02c3fa038640f9f7eb4d0c6c45cf23d` | `SWE1_PROJ_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_MD20260324.xlsx` |
| `82e3f3b4aae1f11886abc6dd53a6d8811b15005be44cb88bec08afb9b48d599b` | `Logical Identifiers and CAN Mapping v1_76.xlsx` |
| `706982bcccb860364f6445b72ea1cdc6977d91c6726a2a373d216283f7587a40` | `PHDCC27_E2A_R1_FDCAN8.dbc` |
| `70aaa730604f4d0a9b640bf10a51b1ea20582b3a9a997ac27586d7a55a02b98b` | `PHDCC27_E2A_R1_BHCAN.dbc` |
| `e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2` | `PROXI_HDCC27_R3_20250424.xlsx` |
| `d88b1072f18f2c9d847e2c95dade0dc6d1fd2f145cac19b21469a38833ccf7c5` | `SYS1_HMI_Projection_Device_R1L-R_HMI_Logic_and_Flow_(February_5_2026).xlsx` |
| `4b351960a55eae92dc521830bccd0c91f6c5a8429399067ed568e86025ff4fa8` | `SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023).xlsx` |
| `edc1e4d6764711306fe9552d1acf175e55e51cc52c0b8b5cd00eb55be1a75ae9` | `Projection Device R1L-R HMI Logic and Flow (February 5 2026).pdf` |
| `cd5bbfbd378ad91e3855c571aa1c3efb22c5687cc105aa1318b4016fa4aef77e` | `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf` |
| `4b20abf4860d394e332a3576265eb050bf3569822c3b75ff944e224944a76999` | `R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.docx` |
| `9417aa715c7a5b2e13f341296b235a4a14c7f406fcb2147686b98e0c921c228a` | `R1LR_Atl-H_25PI3.5_Phone and Mirroring_CFTS_85 Brought In Device Mirroring_20250910_1704.doc` |
| `8fef8da9809f77f6cb3e50bca51eba8fbaf5d0595a5b46a062ae353301a1e803` | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.doc` |
| `ea7f4953e7bfe2b6b9f448392fef88e79a5424daf2d03efe9277adf47217bad7` | `SYS2_CFTS085_…_SYSRA_CFTS085_V01.xlsx` |
| `60a71a7a0d05c1250d8e04390633400afa727934b668e4605a5655d4dd1edeea` | `SYS2_CP.R10_…_SYSRA_CP.R10_V01.xlsx` |
| `659202c10947c800c9ca38df3d54a775ec606ece68abb2beb4da0d2413d4b21e` | `SYS2_HUIG_4_5_…_SYSRA_HUIG_4_5_V01.xlsx` |
| `29ffc7c818aa09f7ef99d8287d95f4c0e941d946e5240e40107b5107e56bc4ce` | `SYS3_PROJ_FM-WI-FSM-011-A01 Xi Tong Jia Gou She Ji  System Architectural Design_SYSAD.docx` |
| `c144e926fc19df63b1b47a2b1d0290f5670d5233317695f4e7de0dc9d84a15aa` | `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` |
| `c92cc3ddda2cd87a75f1a0882d011b0b7e36876f6dd99044e1ba7683fa686c3d` | `Navigation_Repetition_on_IPC-LTM_(R1L)_VF176_V42_R5.docx` |
| `0f5797211ba74d1dc0d28387a21b86351f47f75acd6af71592f32db295d252d0` | `ATS User Guide.pdf` |
| `03ca0f9eb0e47e696336cdbbc4a71d26f9ea7eaf5064b429e3ac5a80d41d794e` | `ATS 8.10 README.rtf` |
| `b0d64ccd78d30a6503f0036441db1cf0bf3a2f4fc65b3e7a0ac0fa3bf7ab7b2a` | `CarPlay Tests User Manual R2.19.4.pdf` |
| `302ddb72f6bc85a104aeb8819967a2cc1243b2343090220bcce1a4b45d4da1c8` | `CarPlay Tests 2.19.4 README.rtf` |
| `134552e815fb71b959fa077b82a04609b2c1f48c364e6527d652e822e01fb3fa` | `FM-WI-FSM-036-A01 …_SWQT_SWC_20260708.xlsx` — cross-feature, **style only** |

The CarPlay manual sits at `CarPlay TestApp/CarPlay Tests User Manual
R2.19.4.pdf`, one level above the path the 下放包 §3.2 gives
(`…/CarPlay Tests App Test Files and README/`). The README rtf is in the
subdirectory as stated. Both are present.

### [AUTO] Phase 2 補入素材 — SHA256（2026-08-12）

Seven files added under R-P16 / R-P17 / §6.4. R-P5 was extended by explicit
authorisation for the first six; the apk comes from the R-P5 root.

| SHA256 | file | 裁決 |
|---|---|---|
| `b8d4d6e1b8add3dbffdca8f28e39129231f613a7d41811bda6bd07eb40cb8bff` | `Accessory Interface Specification CarPlay Addendum R10.pdf` | R-P16 |
| `6fc6d1fcb6b174e00875fa354422a36fc285596a2ce1f67ee4e0e9b5fe2ded6a` | `Accessory Interface Specification CarPlay Addendum R10.docx` | R-P16 |
| `5665820f1889cf44e82fc0f8e69e65d14ce141dff73d1baa6df0a23997d3eef7` | `SYS1_Accessory Interface Specification CarPlay Addendum R10.xlsx` | R-P16 |
| `36e585c300517d377f8827a9e062b1824ebbc509ea1ba0601ae04951fd0f52cb` | `Projection Device HMI Logic and Flow R1 SR24 Post 2A (May 3 2023).pdf` | R-P17 — **核對基準** |
| `61338e3be17a2760f6896f8682a7d97f7f5775bb5e684e99de8c46d3487e95b1` | `Projection Device HMI Change Log R1 SR24 Post 2A (May 3 2023).xlsx` | R-P17 |
| `530274f8c0afed9a12e2b1445b7fc6c06e3e09d6096fcb53720e325683de4f7c` | `SYS1_HMI_Projection_Device_HMI _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx` | R-P17 |
| `dd7b26a6a4cd14ceff72eb9424d6ef5ed5eea2175f3c09b77dde3e773dbe2b24` | `pcts_verifier_release_signed - 922397802.apk` | §6.4 |

**§4.1 / §4.2 之異 hash 分支未觸發。** 全部副本逐一計算：

- **CarPlay Addendum R10** — 四處「副本」實為三件不同產物，不是三個版本。
  兩份 PDF（`1_Customer_Requirement/CPAA_spec/` 與
  `10_Reviewing/00_TestCase/Bluetooth/REF/`）**hash 位元相同**
  （`b8d4d6e1…`），依 §4.1 規則 2 取前者；後者僅記錄路徑。另兩件是同一文件
  的不同格式 —— `.docx`（`6fc6d1fc…`，全文，便於條款查找）與 SYS.1 匯出
  `.xlsx`（`5665820f…`，outline）。三種格式全部落地：82 列的引用帶
  `§3.2.6` / `§3.3.5` 章節錨點，PDF 供引用比對、docx 供全文檢索、SYS1 xlsx
  與本 repo 既有的「SYS1 匯出 + PDF 成對」慣例一致（mode A/B）。
- **Projection Device HMI (May 3 2023)** — PDF 與 Change Log 各只有一處副本，
  無可比之對象。額外落地一件下放包 §4.2 未點名者：
  `9_ASPICE/01_SYS.1…/SYS1_HMI/Archive/SYS1_HMI_Projection_Device_HMI
  _Logic_and_Flow_R1_SR24_Post_2A_(May_3_2023).xlsx` —— 與已在 `inputs/` 的
  Feb 2026 SYS1 匯出完全平行，使核對基準版也具備 outline。**此件屬自行判斷
  補入，列此供 Pei 覆核**；若不採，刪檔即可，不影響其他裁決。
- **PCTS apk** — 裝置上實際安裝的 `com.google.android.projection.gearhead.
  pctsverifier` 版本為 `5.1-prod.922397802`，與 apk 檔名建號 `922397802`
  一致（§6 取證確認）。

### [AUTO] 不落地 — confirmed excluded

PCTS apk · CarPlay 資產目錄與教學影片 · 所有 `.zip` (including `ATS 8.10.0.zip`,
`CarPlay Tests App Test Files and README.zip`) · `ATS.app` ·
`FM-WI-FSM-036-A01 …_SWQT_Projection_20260623.xlsx` (定位未裁) ·
`ProjectionDeviceMedia-HMI/` (R-P1) · Office lock files (`~$…`).

## 2. Workbook survey

- workbook_state: `[AUTO: FULL_REFINE]` — 559 rows, every one populated, 164
  of 171 leaves covered, results recorded across five builds. canon §2 binds
  `FULL` to audit-only-no-generation, which this case is not: the step text
  has to be made executable, and 6–7 leaves need new rows. The new state is
  defined in profile §1.
- Sheet: `[AUTO: TestResults]` (9 sheets in the file)
- Header row: `[AUTO: 2]` · first data row `[AUTO: 4]` · last `[AUTO: 562]`
- Column mapping: `[AUTO — 17/17 matched by header text]`, listed in
  `feature.yaml → workbook.columns` and RECON §1. This is NOT an
  FM-WI-FSM-036 form; from column F onward it sits one letter left of every
  other feature in this repo.
- Done-region: `[AUTO — the entire sheet]`. Under FULL_REFINE there is no
  author-based selector; all 559 rows are protected and exactly two columns
  are unfrozen (Pre-Conditions, Test procedure).
- Frozen sub-region: `[AUTO per R-P6 — 23 PCTS rows]`, enumerated in
  `feature.yaml → done_region.frozen_rows`.
- Design-method vocabulary: `[AUTO — 9 strings from 下拉選單, all 9 in use,
  nothing outside them]`. No lint findings.
- 完全空白列: `[AUTO: 1 — row 562]`, a traceability stub for `SWE1-PROJ-227`
  carrying ids and Test Item but no TC content.
  → `[PEI]` disposition: is row 562 a row to fill, or a stub to leave alone?
- `Estimated Test Time` 0/559 and `Test Case Author` blank on 41 rows:
  `[PEI]` — blank-by-convention, or a gap to close? (A-PJ08)

## 3. Coverage

- 037 leaf count: `[AUTO: 171]` (+1 Heading row)
- Covered by the workbook: `[AUTO: 164]`
- Uncovered: `[AUTO: 7]` — `SWE1-PROJ-133 / 146 / 167-001 / 167-002 / 184 /
  190 / 195`. **7, not 6**: `SWE1-PROJ-133` is still a live leaf in the ruled
  037 (R-P2 = CPAA), even though the MD version's change log marks
  `SYS-RA-PROJ-133` unavailable at V1.1 (2026-01-21). (A-PJ11)
  → `[PEI]` — does the MD down-listing bind, or does the ruled source?
- Reverse overflow (workbook req_ids absent from the 037): `[AUTO: 0]`
- Parent/child both-leaf duplications: `[AUTO: none detected]`

## 4. Style bindings

- Style authority: `[AUTO — the base workbook's own done region]`, per profile
  §1. It is the only feature in this repo whose style authority is the file
  being rewritten.
- Expected Result / Test Item / Input Test Data / Specification Reference /
  results / BugList: `[AUTO — frozen, content-hash invariant]` (O-1, L-PJ4)
- Author value on new rows: `[PROPOSED: PeiPYHsu]` — matches the existing 518
  authored rows.
- Exemplar source for CAN steps: `[AUTO — SWC workbook, style only]`. Its
  column layout is a defect (A-PJ07) and is not copied. The corrected pattern
  lives in `data/signal_map.json → can_step_pattern`; the 下放包's version
  used enumeration labels that do not exist in either DBC (A-PJ12).

## 5. Split & scope

- split_mode: `[PROPOSED: none for the 559 existing rows]` — FULL_REFINE
  rewrites in place; row count and row order do not change, so no split
  decision arises. Splitting applies only to the 7 appended leaves.
- Granularity precedent for the appended rows: `[PROPOSED — the existing
  rows serving neighbouring leaves in the same Test Set]`

## 6. Framework & profile

- Profile: `docs/runtime/profiles/FW036_R1L_Projection_Profile.md` — written,
  carrying O-1 … O-4 verbatim and L-PJ1 … L-PJ7.
- Test Group column carries 10 module names, not one: `[PEI]` — canon §4.1.1
  says Test Group = a single module name. Registered as A-PJ06; the 下放包
  defers it to Phase 3. The column is not written by this pipeline either way.

## 7. Execution

- Batch plan: `[PROPOSED]` — 見 PLAYBOOK §6. Phase 0 does not fix it; the
  natural unit is the Test Set (18 values), with the 23 frozen PCTS rows
  excluded from every batch.
- BLOCKED at start: `[AUTO]` — 23 PCTS rows (R-P6, DR#1); 2 rows carrying
  `$HCP_DISP2.Est_Range_BEV$` (R-P9, DR#2); 80 rows citing the CarPlay
  Addendum spec that is not in `inputs/` (DR#6) are citation-blocked only,
  not step-blocked.

---

## 8. Open `[PEI]` items — Phase 2 待裁

1. **A-PJ09** — `AA-V4.5` and `CP-R46` appear nowhere in the 037; the real
   families are `SYS-RA-HUIG4.5` (16), `SYS-RA-CP_R10` (9) and one
   `CP-R10-3.2.7.2`. A-PJ05 and DATA_REQUESTS #4/#5 rest on the stated
   labels. Do they stand, get re-aimed at HUIG 4.5 / CP_R10, or get withdrawn?
2. **A-PJ11** — leaf 133: does the MD change log's `unavailable` bind, or does
   the ruled CPAA source? Decides whether the gap is 7 or 6.
3. **A-PJ12** — confirm the corrected CAN exemplar (`Pressed` / `Not_Pressed`
   from the DBC) replaces the 下放包's `PSD` / `NOT_PSD`.
4. **A-PJ08** — `Estimated Test Time` 0/559 and 41 blank `Test Case Author`:
   blank-by-convention, or fill?
5. **Row 562** — fill the `SWE1-PROJ-227` stub, or leave it?
6. **A-PJ06** — Test Group as 10 module names vs canon §4.1.1.
7. **DR#6** — `Accessory_Interface_Specification_CarPlay_Addendum_R1`, cited
   by 80 rows and not supplied. Request it, or scope those citations out?

---

## Sign-off

- Reviewed by: ____________  Date: ____________
- Overridden items (list numbers): ____________
- Ruling notes:
