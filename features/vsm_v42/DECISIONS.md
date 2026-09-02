# DECISIONS — Vehicle Setup Management R1 Low (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: **[AUTO] D** —— 母 spec 為 OOXML docx（R-VL5；magic bytes `50 4B 03 04` 實測，上繳 02 E22）
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 11 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: **[AUTO] BLANK** —— R-VL1 自 R-G1 母本起建；`sandbox/base` 副本 cmp 全等、
  zip members 48、x14 DV 1（未經 openpyxl 存回），上繳 02 E19
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 68 —— **此為 recon 代表檔（Park Sense）之數，非母體**
- **母體（本線據以生成之 leaf 全集）：128**（R-VL4；68 ＋ 60，Source ID 去重 128、兩檔無交集；
  跨源對帳 128／128 命中，上繳 02 E3／E6／E16）。全集見 `data/leaves.tsv`（152 列 ＝
  128 leaf ＋ 23 Heading ＋ 1 UNCATEGORIZED），該檔已帶 `test_set` 欄（下放包 04 W-11）
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 68 (list in recon.json)
- covered nowhere: [AUTO] 68 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: None]
- tc_id scheme: [RULED] NR1L-VSM42-{n:03d} — frozen per this feature's RULINGS.md, not open at sign-off

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): **[RULED] R-VL17（Pei 2026-09-02「准」）—— 十組鎖定，leaf 合計 128**
  Park Sense 18／Camera Gridlines 10／Lighting 11／Speed Assist 21／Driver Warning 13／
  Wiper and Sensor 5／Units 15／EPB Maintenance Mode 17／Personal Data and Defaults 14／
  Time and Navigation 4。全表見 `framework.md`；十組逐組對測相符（下放包 04 E34）。
  Layer 3 之規格章節號已由執行層實測回填（21／24 家族對映，3 家族未對映，見上繳 04）
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: 依 `framework.md` 之十個 Test Set 分批（母體 128，非 68）；
  pilot = `EPB Maintenance Mode`（17，R-VL17 之分析層提案，開跑前 Pei 可改指）]

---

## Sign-off

- Reviewed by: ____  Date: ____　　**（狀態：待 Pei 簽 —— 執行層不代簽）**
- Overridden items: ____
- Ruling notes:

---

## 執行層附註（下放包 02 W-3，2026-09-01）

- 本檔為 `recon.py` 之預填本，取代原 `new_feature.py` 空白模板（該模板無任何人為編輯，
  故取代不損失簽核痕跡）。**未簽**。
- `037 leaves: [AUTO] 68` 為 recon 代表檔（`a03_report` = Park Sense）之數，
  **非本線母體**。母體依 R-VL4 為兩份 037 之 Functional leaf 合計 **128**
  （68 ＋ 60，Source ID 去重 128，兩檔無交集），全集見 `data/leaves.tsv`（152 列 =
  128 leaf ＋ 23 Heading ＋ 1 UNCATEGORIZED）。簽核前請以 128 為準。
- `column mapping: [AUTO] 15 fields` 係 recon 依表頭文字解析所得；本包依 R-VL8(b)
  自 `sandbox/base` 副本 r9 **逐欄實測**後回填 `feature.yaml`，計 columns 21 鍵
  ＋ variant_columns 7 ＋ execution_columns 5。

## 執行層附註（下放包 04 W-10，2026-09-02）

依 W-10 補齊四欄實值：`spec_mode`（§1）、`workbook_state`（§2）、**母體 128**（§3）、
**框架 R-VL17**（§6）；另更新 §7 batch plan 之母體數（68 → 128）。
**未代簽**；`Sign-off` 段之 `Reviewed by`／`Date` 留空，狀態標「待 Pei 簽」。

其餘 `[PROPOSED]` 項未動 —— 依本檔開頭之契約，簽核時未經更動者即以所提為準。
`[PEI]` 項尚餘一項未決：**`profile [OVERRIDE] clauses`** ——
`docs/runtime/profiles/FW036_R1L_VSM_V42_Profile.md` 已由分析層落檔（2026-09-02），
惟該目錄為執行層禁區（讀可寫不可），故本包**不代填該欄**。
