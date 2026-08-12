# RECON — Projection (Phase 0)

Produced by `features/projection/scripts/recon_projection.py` (machine output
in `data/recon.json`). Every number below was measured against the copies in
`inputs/`, not carried over from the 下放包.

The shared `scripts/recon.py` was NOT used. It assumes an FM-WI-FSM-036 form
instance (header row 9, done-region-by-author). Projection's base workbook is
the NR1L_GEN1(HDCC) execution workbook — header row 2, data from row 4, seven
vehicle-model columns and five build-result columns. Forcing it through the
shared script would have produced a survey of the wrong shape.

**Reading the verdict column**: `符合` = reproduced the 下放包 §4 pre-verified
value exactly. `不符` = did not. Under 下放包 §0.5 no mismatch was reconciled;
each one is carried to ANOMALIES and to the 上繳包.

---

## 1. Base workbook — `NR1L_GEN1(HDCC)_Ver_20260813.xlsx`

sha256 `11579c9b3b8e56eb…` · sheet `TestResults` · 9 sheets in the file
(`TestProgress`, `Cover_old`, `ChangeHistory_old`, `QS Suggestion`, `下拉選單`,
`TestResults`, `Reference`, `BugList`, `Test Case Framework`)

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| data rows | 559 | **559** (rows 4–562) | 符合 |
| header row | 2 | **2** | 符合 |
| first data row | 4 | **4** | 符合 |
| column header match | — | **17 / 17** resolved by header text | — |

Column mapping (resolved by matching row-2 header text, not inherited):

```
B  seq                C  req_id (Polarion)     D  req_id           E  tc_id
F  test_group         G  test_set              H  test_item        I  pre_conditions
J  input_test_data    K  test_procedure        L  expected_result  M  spec_reference
N  tc_ref_id          O  priority              P  estimated_test_time
Q  design_method      R  functional_safety     S–Y vehicle model
Z  author             AA test vehicle          AB test period      AC tester
AD–AH build results   AI defect id             AJ remarks
```

Note the layout is one column LEFT of every FM-WI-FSM-036 instance in this
repo from `F` onward, because this workbook has no `Test Case ID (TestRail)`
column. Do not inherit letters from another feature.yaml.

## 2. Coverage vs 037 (`…SWRA-CPAA_0521.xlsx`, sheet `Basic Report`)

sha256 `ad7d0abc148e170a…`

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| leaves | 171 | **171** (+1 Heading row) | 符合 |
| covered by workbook | 164 | **164** | 符合 |
| 反向溢出（簿內非 037 的 reqid） | 0 | **0** | 符合 |
| uncovered | 7 | **7** | 符合 |

Uncovered, verbatim:

```
SWE1-PROJ-133   SWE1-PROJ-146   SWE1-PROJ-167-001   SWE1-PROJ-167-002
SWE1-PROJ-184   SWE1-PROJ-190   SWE1-PROJ-195
```

**133 的下架問題已查清，答案是否定的。** The MD-version 037 records at
`ChangeHistory 修訂履歷` V1.1 (2026-01-21): *"Change SYS-RA-PROJ-133 to
unavailable"*. But `SWE1-PROJ-133` is **still present as a live leaf in
CPAA_0521** — it is one of the 171. The two 037 sets therefore disagree on
this requirement's status, and the ruled source (R-P2 = CPAA) says it is
live. **實質缺口維持 7 條，不是 6 條。** Registered as A-PJ11.

Source-requirement families behind the 171 leaves:

| family | count | leaf id range |
|---|---|---|
| `SYS-RA-PROJ` | 145 | SWE1-PROJ-071-001 … SWE1-PROJ-198 |
| `SYS-RA-HUIG4.5` | 16 | SWE1-PROJ-208 … SWE1-PROJ-225 |
| `SYS-RA-CP_R10` | 9 | SWE1-PROJ-201 … SWE1-PROJ-227 |
| `CP-R10-3.2.7.2` | 1 | SWE1-PROJ-203 |

預驗值為 `SYS-RA-PROJ 145 / AA-V4.5 16 / CP-R10 6 / CP-R46 4`。**145 符合；其餘
不符。** The strings `AA-V4.5` and `CP-R46` occur **zero times** anywhere in the
037 — not in the source column, not in any of columns D–U, and zero times in
all 36 columns of all 559 workbook rows. The 16 leaves the 下放包 attributes to
`AA-V4.5` are the `SYS-RA-HUIG4.5` block (count matches exactly); the 10 it
splits as `CP-R10 6 / CP-R46 4` are one `SYS-RA-CP_R10` block of 9 plus the
single odd-format `CP-R10-3.2.7.2`. Registered as A-PJ09 — this removes the
stated basis for A-PJ05 and for DATA_REQUESTS #4/#5.

Also contradicted: the 下放包 states that uncovered leaves 184 / 190 / 195 "正落
此區間". They do not. All three carry `SYS-RA-PROJ` source ids
(`SYS-RA-PROJ-184` / `-190` / `-195`) and sit in the main block.

`SWE1 HMI Source ID` (column D): **0 / 171 filled** — 符合 A-PJ02.

## 3. 欄位填充率

| 欄位 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| tc_id | 556 | **556** | 符合 |
| test_set | 558 | **558** | 符合 |
| pre_conditions | 558 | **558** | 符合 |
| input_test_data | 540 | **540** | 符合 |
| test_procedure | 558 | **558** | 符合 |
| expected_result | 558 | **558** | 符合 |
| spec_reference | 558 | **558** | 符合 |
| priority | 558 | **558** | 符合 |
| design_method | 558 | **558** | 符合 |
| Estimated Test Time | 0 / 559 | **0 / 559** | 符合 |
| Test Case Author | 518 / 559 | **518 / 559** | 符合 |
| 完全空白列 | 1 | **1** — row 562 | 符合（口徑須言明） |

Also measured, not in the 下放包: `seq` 559, `req_id (Polarion)` 559, `req_id`
559, `test_group` 559, `test_item` 559, `tc_ref_id` 558, `functional_safety`
558, `remarks` 184.

**「完全空白列」的口徑**: no row in this sheet is blank in every column. Row 562
(seq 559, `SWE1-PROJ-227`, Test Group `Carplay Wired and Wireless`) is blank
across all nine TC-content columns — Test Set, Pre-Conditions, Procedure,
Expected Result, Specification Reference, Priority, Design Method, Functional
Safety — while still carrying seq, both req ids, Test Group, Test Item and a
`tc_ref_id`. It is a traceability stub with no test case in it. Under that
definition the count is exactly 1, matching the pre-verified value. The
definition is recorded in the script (`CONTENT_FIELDS`) so the number stays
reproducible.

The three rows missing `tc_id` are 48, 53 and 562. The one row missing
`tc_ref_id` is 152.

## 4. `$token$` 盤點

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| distinct tokens | 10 | **10** | 符合 |
| 出現列數 | 59 | **59** | 符合 |
| 可解析 | 8 | **9** | 不符 — 見下 |
| 未解析 | 2 | **1** | 不符 — 見下 |

| token | 出現列數 |
|---|---|
| `$Day_Night_Mode$` | 22 |
| `$VC_Veh_Line$` | 14 |
| `$VC_Veh_Brand$` | 12 |
| `$HUModeStatus$` | 4 |
| `$Screen_Size$` | 3 |
| `$VC_VEH_LINE$` | 3 |
| `$VC_VEH_BRAND$` | 3 |
| `$HCP_DISP2.Est_Range_BEV$` | 2 |
| `$VC_VEH_Line$` | 2 |
| `$FuelLvlLow$` | 2 |

`$Screen_Size$` **does** resolve through the mapping table: the Logical
Identifier is spelled `Head_Unit_Screen_Size`, and its Atlantis High entry on
`Proxi & Configuration` gives `Radio_Display_Type` — exactly the target R-P7
rules by hand. The mapping table corroborates R-P7 instead of being silent on
it, so only `$HCP_DISP2.Est_Range_BEV$` is genuinely unresolved. Registered as
A-PJ13. No decision changes; R-P7 stands and gains a second source.

## 5. 訊號解析驗證（§5 對照表逐列實查）

Both DBCs parse as ISO-8859 with CRLF; reading them as UTF-8 silently yields
nothing.

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| FDCAN8 messages | 244 | **244** | 符合 |
| FDCAN8 signals | 1,264 | **1,503** | 不符 |
| BHCAN messages | 123 | **123** | 符合 |
| BHCAN signals | 672 | **692** | 不符 |
| message overlap | 24 | **24** | 符合 |
| PROXI configuration words | 948 | **1,052** distinct (1,058 rows) | 不符 |

The signal- and parameter-count differences are counting-rule differences
(this script counts every `SG_` line and every distinct `Parameter Name`), not
missing content. They change no decision — every signal the feature needs
resolved. Recorded for the record only.

Per-signal lookup — all nine claims checked:

| claim | bus | found | VAL_ table |
|---|---|---|---|
| `BCM_FD_27.DAY_LGT_MD_DISP` | FD | ✅ | `0 Night / 1 Day` |
| `BCM_FD_27.DAY_LGT_MODE_DISP` | — | ❌ **absent from both DBCs** | — |
| `TELEMATIC_FD_4.CurrentSource` | FD | ✅ | `0 AM_Selected / 1 FM_Selected / 2 MW_Selected / 3 LW_Selected …` |
| `STATUS_TELEMATIC.CurrentSource` | CAN-B | ✅ | identical table |
| `STATUS_BH_BCM1.LowFuelWarningSts` | CAN-B | ✅ | `0 OFF / 1 ON` |
| `BCM_FD_14.Command_02Sts` | FD | ✅ | `0 Not_Pressed / 1 Pressed / 3 SNA` |
| `HYBRID_DISPLAY.EstimatedRange` | FD | ✅ | `255 SNA` |
| `IPC_FD_5.Est_Range_Disp` | FD | ✅ | `255 SNA` |
| `HCP_CHARGING_STAT.Est_Range_FullCharge` | FD | ✅ | `2047 SNA` |

The `DAY_LGT_MODE_DISP` trap is confirmed exactly as the 下放包 describes: the
mapping table carries both spellings in one cell and only `DAY_LGT_MD_DISP`
exists.

**§5 CAN 範式與 DBC 不一致。** The pattern writes
`BCM_FD_14.Command_02Sts = 1 (PSD)` and `= 0 (NOT_PSD)`. The DBC's own VAL_
table for that signal is `0 "Not_Pressed" / 1 "Pressed" / 3 "SNA"`; the strings
`PSD` and `NOT_PSD` appear in neither DBC. Written as given, the exemplar
pattern would ABORT under its own gate L-PJ1. Registered as A-PJ12; the
corrected pattern is in `data/signal_map.json → can_step_pattern`.

Mapping-table lookups (Atlantis High: `CAN Mapping` cols 26–30, `Proxi &
Configuration` cols 16–20 — both column blocks confirmed by their row-2/3
headers, matching the 下放包):

| LID | Atlantis High signal |
|---|---|
| `Day_Night_Mode` | `BCM_FD_27.DAY_LGT_MODE_DISP  BCM_FD_27.DAY_LGT_MD_DISP` (two in one cell) |
| `VC_VEH_BRAND` | `Proxi: Brand_Configuration_2` |
| `VC_VEH_LINE` | `Car_Configuration_15.Vehicle_Line_Configuration` |
| `HUModeStatus` | `STATUS_TELEMATIC.CurrentSource  TELEMATIC_FD_4.CurrentSource` |
| `FuelLvlLow` | `STATUS_BH_BCM1.LowFuelWarningSts` |
| `Head_Unit_Screen_Size` | `Radio_Display_Type` |
| `Est_Range_BEV` | **absent** (9 other `Est_Range*` LIDs exist; none is a BEV variant) |

Mapping LIDs are stored UPPER CASE (`VC_VEH_LINE`, `VC_VEH_BRAND`) while the
workbook uses three casings. Lookups must be case-insensitive.

**PROXI `Vehicle_Line_Configuration` 的 332 問題與 A-PJ04 所述不同。** The
enumeration read verbatim from `PROXI_HDCC27_R3_20250424.xlsx` includes
`105 = 332 (69 Hex)`. So 332 is not outside the enumeration — it is the
**label** of code 105, and the workbook is naming the vehicle line where the
configuration word takes 105. A-PJ04's evidence line ("332 不在列舉值內") does
not reproduce. Registered as A-PJ10. **R-P8 is unaffected**: the ruling is to
leave the literal untouched and note it in Remarks, which remains correct.

`Radio_Display_Type` verbatim: `0 = Absent / 1 = 7" 1280x768 / 2 = 8.4"
1024x768 / 3 = 10.1" 1920x1200 / 4 = 10.1" 1200x1920 / 5 = 10.25" 1920x720 /
6 = 12" 1920x1200 / 7 = 12" 1200x1920 / 8 = 12.3" 1920x720 / 9 = 14.5"
1024x1920`. R-P7's `= 2` for the `only 8.4"` rows is confirmed correct.

`Projection Mode Selection` sheet confirmed as a bitfield —
`00 = CarPlay + Android Auto`, `01 = CarPlay Only`, `02 = Android Auto Only`,
`04 = CarLife Only`, b3–b7 reserved. The sheet's own note adds a trap worth
carrying into every pre-condition: **value 0 does not disable projection** —
it activates both CarPlay and Android Auto for backward compatibility; to
disable projection the separate `Projection_Mode` parameter must be `Absent`.
All of `Projection_Mode`, `Projection_Mode_Selection`, `GPS_Presence`,
`NAV_Presence`, `Nav_Repetition` and
`WiFi_2_BT_BLE_External_Antenna_Presence` exist in the PROXI Format sheet.

## 6. 工具依賴

| 工具 | 預驗 | Procedure 欄 | Procedure + Pre-Conditions | 判定 |
|---|---|---|---|---|
| CAN tool | 39 | **39** | 40 | 符合（Procedure 欄口徑） |
| PCTS | 23 | **23** | 23 | 符合 |
| ATS | 10 | **10** | 10 | 符合 |
| testapp | 6 | **6** | 6 | 符合 |
| logcat | 10 | **10** | 10 | 符合 |
| adb | 2 | **0** | 2 | 不符（口徑差異） |

No single column scope reproduces all six. On the Procedure column alone CAN
is 39 (matching) but adb is 0; adding Pre-Conditions makes adb 2 (matching)
but CAN 40. The two adb rows are 431 and 433, where the instruction sits in
Pre-Conditions, not in Procedure. Both scopes are reported rather than one
being picked silently. `CAN` is matched **case-sensitively** — a
case-insensitive `\bCAN\b` also matches the English modal "can" and inflates
39 to 86.

The 23 PCTS rows (R-P6 凍結區, listed in `feature.yaml → done_region.frozen_rows`):

```
255 256 257 258 259 260 261 262 263 264 265 266 267 271
371 376 377 378 379 441 443 521 522
```

## 7. 環境阻塞（Remarks 欄）

| Remarks | 預驗 | 實測 | 判定 |
|---|---|---|---|
| `Need to test in real car env` | 85 | **85** | 符合 |
| `Not in ASW-R1 Release Scope` | 77 | **77** | 符合 |
| `*Section 35 應該修改為Section 15` | 6 | **6** — rows 219–224 | 符合 |
| `only 8.4"` | 6 | **6** — rows 425, 426, 428, 429, 430, 431 | 符合 |

Remarks is populated on 184 of 559 rows. Other values present but not in the
下放包: `Vehicle not in Scope` 4, `Need to test in real car` 3 (a second
spelling of the 85-row string), `No cluster env` 3.

## 8. 品質缺陷

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| §5.1 禁用動詞 | 7 (check whether 3 / inspect 3 / observe 1) | **7** — identical split | 符合 |
| 模糊語 | 11 (correctly 7 / a while 2 / normally 2) | **11** — identical split | 符合 |

Counting rules, recorded so the numbers stay reproducible: banned verbs are
counted on the **Procedure column only** (the same word in an Expected Result
states an outcome, it is not an unexecutable instruction); vague language is
counted **per row over Procedure + Expected Result together**, so a row
carrying `correctly` in both columns is one defective row, not two. Widening
either scope to Test Item inflates the totals (`correctly` gains 5,
`normally` gains 8).

`properly` and `successfully`: **0 occurrences**. They stay in the L-PJ6
vocabulary as a guard on newly written text.

## 9. Test Group 欄（10 值）

| Test Group | 預驗 | 實測 |
|---|---|---|
| Device Manager | 192 | **192** |
| Carplay Wired and Wireless | 60 | **60** |
| Android Auto Wired and Wireless | 58 | **58** |
| Touch | 57 | **57** |
| Bluetooth | 53 | **53** |
| WiFi | 51 | **51** |
| Audio Management | 31 | **31** |
| GPS | 30 | **30** |
| Media Player | 23 | **23** |
| SSE / ECNR | 4 | **4** |

全部符合（總計 559）。

## 10. Test Set 欄（18 值 + 1 空）

HMI Display 76 · Projection Launch 65 · Connection 61 · Device Manager 54 ·
Disconnection 49 · Projection Detection 49 · Knob 42 · Projection Audio 37 ·
Voice Recognition 22 · Vehicle Signal Forwarding 22 · Day/Night Mode 22 ·
Pairing 12 · Cluster Navigation 12 · Projection Apps 12 · Performance 10 ·
Projection Display 5 · Wireless Coexistence 4 · USB Device 4 · (空) 1

全部符合（總計 559）。

## 11. 執行狀態（00.01.01.04 = 欄 AG）

| 狀態 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| Pass | 67 | **67** | 符合 |
| Fail | 34 | **34** | 符合 |
| Block | 3 | **3** | 符合 |
| NA | 90 | **90** | 符合 |
| 未執行 | 365 | **365** | 符合 |

The workbook carries five build columns in all: AD `00.01.01.02`,
AE `00.01.01.03`, AF `Daily Build 20260805`, AG `00.01.01.04`,
AH `00.01.01.05`.

## 12. 兩份 037 比對（A-PJ01 驗證）

| 項目 | 預驗 | 實測 | 判定 |
|---|---|---|---|
| ID 交集 | 171/171 | **171/171** — neither side has an id the other lacks | 符合 |
| Verification Criteria 相異 | 171/171 | **171/171** | 符合 |
| description 相異 | 127/171 | **105/171** | 不符 |

Compared on CPAA `Basic Report` col F (Description) / col T (Verification
Criteria) against MD `Analysis Report` col E (Requirement Description) / col
AI (Verification Criteria), MD header row 8, data from row 9. Also measured:
CPAA leaves 4 Verification Criteria cells empty, MD leaves 0.

The description count is a measurement difference, not a content difference —
the two sets do disagree pervasively, which is what A-PJ01 turns on. R-P2's
choice of CPAA stands. Recorded in the mismatch table only, not raised as its
own anomaly.

**MD 版的兩項用途已確認到位**:
- `QA` sheet — **44 rows: 26 Closed, 15 Opening, 3 blank**. The 下放包 said
  "12+ 條已 Closed"; the real figure is more than twice that, so the RD-1
  question count can be cut further than planned. The 15 `Opening` rows are
  live questions and are RD-1 input, not answers.
- Quality-attribute columns CPAA lacks are present: Feasibility,
  Verifiability, Unambiguous, Completeness, Correctness, Consistency,
  Traceability, Readability, Impact, Risk Factor, Complexity, Reusable —
  each with a paired `Description/Action for …` column.

## 13. 其他既測項目（非 §4 要求）

- **Design method vocabulary** — the `下拉選單` sheet lists 9 strings; the
  workbook uses all 9 and nothing outside them (558 rows):
  功能測試 266 · 狀態轉換 188 · 決策表 34 · 負向測試 25 · 基礎故障注入 24 ·
  邊界值分析 8 · 情境/用例 7 · 等價劃分 4 · 組合測試 2.
  The vocabulary is clean — no lint findings.
- **Priority** — P0 376 · P1 96 · P2 85 · P3 1 (558 rows).
- **`spec_reference` citation sources** — `CFTS085` on 473 rows,
  `Projection_Device_HMI_Logic_and_Flow_…` on 120, `Accessory_Interface_
  Specification_CarPlay_Addendum_R1` on 80, `Device_Manager_HMI_Logic_and_
  Flow_…` on 52, `HUIG_4_5` on 51, `CFTS025` on 30, `CFTS019` on 16. This is
  what fixes `spec_mode` at `[A, B, D]`: the spec line runs through both SYS1
  HMI documents (A/B) and CFTS085 (D) simultaneously.
  `Accessory_Interface_Specification_CarPlay_Addendum_R1` is cited on 80 rows
  and is **not in `inputs/`** — see DATA_REQUESTS #6.
- **`332` in row text** — 16 contiguous rows, 151–166.

---

## 14. 預驗值不符彙總（全部未自行調和，依 §0.5 上報）

| # | 項目 | 預驗 | 實測 | 性質 | 去處 |
|---|---|---|---|---|---|
| 1 | 037 source families | `AA-V4.5 16 / CP-R10 6 / CP-R46 4` | `SYS-RA-HUIG4.5 16 / SYS-RA-CP_R10 9 / CP-R10-3.2.7.2 1`；`AA-V4.5` 與 `CP-R46` 全檔零次 | **實質** — 抽掉 A-PJ05 與 DR#4/#5 的立論 | A-PJ09 |
| 2 | 184/190/195 落在 AA/CP 區間 | 是 | 否 — 三條皆 `SYS-RA-PROJ` | **實質** | A-PJ09 |
| 3 | `Vehicle_Line_Configuration` 無 332 | 不在列舉值內 | 在 — `105 = 332 (69 Hex)`，332 是標籤不是值 | **實質** — 改寫 A-PJ04 證據；R-P8 不受影響 | A-PJ10 |
| 4 | leaf 133 可能已下架 | 若已下架則缺口 6 | CPAA 仍列為 live leaf；僅 MD 版標 unavailable → 缺口維持 **7** | **實質** | A-PJ11 |
| 5 | CAN 範式列舉標籤 `PSD` / `NOT_PSD` | — | DBC 為 `Not_Pressed` / `Pressed` / `SNA`；`PSD` 兩份 DBC 皆無 | **實質** — 範式照抄會觸發自身 L-PJ1 | A-PJ12 |
| 6 | `$Screen_Size$` 未解析 | 未解析 | 經 LID `Head_Unit_Screen_Size` 解析為 `Radio_Display_Type` | **佐證** — 與 R-P7 同向 | A-PJ13 |
| 7 | FDCAN8 signals | 1,264 | 1,503 | 計數口徑 | 本文件 |
| 8 | BHCAN signals | 672 | 692 | 計數口徑 | 本文件 |
| 9 | PROXI configuration words | 948 | 1,052 distinct / 1,058 rows | 計數口徑 | 本文件 |
| 10 | 037 description 相異 | 127/171 | 105/171 | 計數口徑 | 本文件 |
| 11 | adb 依賴列數 | 2 | Procedure 欄 0；含 Pre-Conditions 2 | 計數口徑 | 本文件 |
| 12 | MD 版 QA 已 Closed | 12+ | 26 Closed / 15 Opening / 3 空 | 低估（方向有利） | 本文件 |

其餘 §4 全部項目逐項相符。
