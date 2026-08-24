# DECISIONS — Power Moding (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] A+B
- spec 基線分工: [RULED §9.1 通則 3] 判讀基準 = `spec_pdf`（內文面）；追溯用 = `sys1_export`（結構面，`{outline}` 之唯一來源）。已知例外四項見 `feature.yaml` `spec_baseline.known_exceptions`
- 指名複核項: [RULED A-PMH03] outline `7.1` 之 5 個 leaf（`pdf_page` 皆 p8）於 Phase 4 逐一以 PDF 原文複核語句順序 —— export 該節相對 PDF 為重排，被移位改寫者為動畫／splash 之時序
- spec text layer: [AUTO] text-layer: 15618 chars (via pymupdf)
- source files: [AUTO] 5 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 1 checked, 1 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 29 cited sections, all found in a 52-entry ruled export; map at data/recon_leaf_to_section.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields + estimated_test_time = 16，與 `feature.yaml` 零衝突（R-PMH9 之四方交叉佐證另證 34/34 逐欄相等）
- 前言三欄: [RULED R-PMH27，Pei 2026-08-24 裁「（甲）」] `D3 審查者`／`D4 目的`／`D5 範圍 Scope` **一律留空**。結論同 R-PMH10，**其依據段由 R-PMH27 更換** —— 原「語料 5/5 無一填寫」作廢（母體未定義）。改依 R-PMH24 之母體實測：`D3` 全空、`D4` 全空、`D5` 空者略多（分析層 9/16；執行層實測 9/17，差異見上繳 05 §2）。**本裁定非多數決**，須連同三項一併記載：(a) 非空者中有數者填錯（`HomeHMI` 填他 feature 之 037 報告名、`Notifications HMI` 填表單編號本身、`App Team Effort` 填一份文件編號）；(b) 案（乙）之代價為版號過期無通知機制（本 feature 037 為 `V0.1`，Popup 已至 `V0.2`）；(c) 部分 feature 無單一份 037（VF230 對應 11 份、CFTS044 對應 4 份），案（乙）在全案非良定義。**日後若客戶要求填寫，字串由 Pei 給定並另立新條，不得以「補上」之名逕行填寫。**
- DV 全量: [AUTO 03 包步驟 2] legacy 3 組（`P10:Q1411` = `"P0,P1,P2,P3"`／`T10:Z1411` = `"0,1"`／`AF10:AF1411` = `"Pass, Fail, Pending,Block,NA"`）＋ x14 1 組（`R10:R1411` → `下拉選單!$A$1:$A$9`）。四份已交付件之逸出 **0**
- 寫回機制: [RULED R-G3／R-G1 註] x14 DV 存在 —— **不得 `openpyxl` + `save()`**，一律走 `xlsx_surgical` splice
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 48
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 48 (list in recon.json)
- covered nowhere: [AUTO] 48 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- Test Group（G）欄: [RULED R-PMH13，Pei 2026-08-23 核可] 一律填 `Disclaimer screen`（交付夾名，**小寫 s**，R-PMH18）。依據為四份已交付件 4/4 皆填交付夾名；R-PMH2 之後半已撤回
- Test Set（H）欄: [RULED R-PMH36，Pei 2026-08-24 裁「甲」] **Layer 2 定版 8 組**：`Splash Screen`(3)／**`Disclaimer Screen`**(7)／`Startup Animation`(9)／`Startup Sounds`(6)／`Power Transitions`(7)／`Power Off Behavior`(8)／`Voice Assistant Key`(5)／`Off Road Plus`(3)，合計 48、餘數 0。⚠ 第 2 組與 Test Group `Disclaimer screen` **字面重複，為 canon §4.2 之明示例外**，限本 feature、本組、此一情形，**不得外推**。⚠ **三字串刻意不同**：G 欄 `Disclaimer screen`（小寫 s）／H 欄 `Disclaimer Screen`（大寫 S）／`tc_id` `DisclaimerScreen`（大寫 S 無空白）—— 比對須大小寫敏感。granularity 對三案無鑑別力，**不得引為理由**；本條依據為**可過濾性**與**不造詞**。
- tc_id_format: [RULED R-PMH16，Pei 2026-08-23 裁（乙）] `NR1L-DisclaimerScreen-{NNN}`（**大寫 S**，R-PMH18）。已知反例 Comfort `ComfortHMI` 隨條保留；本條為本 feature 之裁定，**不主張為全案慣例**
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [AUTO 已驗] `Power Moding HMI Logic and Flow R1 SR24 2A_{outline}` —— 與 037 `HMI Source ID`、SYS1 `SYSRE_HMI_Source ID` 三方同構，非構造而是複現
- 字面常數保真: [RULED R-PMH18] `Disclaimer screen`（G 欄）與 `DisclaimerScreen`（tc_id abbr）**刻意不同，不得統一**；一切比對與 lint 須大小寫敏感

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: 依 spec 章節分組，pilot 取最小之完整章節] leaf 之章分布 7(19)／8(6)／9(5)／10(10)／11(5)／12(3)；PDF 頁分布 p8(25)／p9(5)／p10(15)／p11(3)
- **`DR-PMH3` 之連帶（預先登記，14 包步驟 6）**: [PENDING] 若上游回覆 `SU9.)`／`SU9.1)` **應在 037**，則 `Disclaimer Screen` 組將自 **7 leaf 增為 9**，連帶須重驗：(a) Layer 2 之八組計數與 48 總數（R-PMH36 之定版數字）；(b) granularity G1–G5（`min` 由 3 變 3、`max` 由 9 變 9，惟分母由 48 變 50 —— `check_granularity.py` 之 `n_leaf` 須改）；(c) `layer3_sections.tsv` 與 `outline_map.json` 之 48 列；(d) batch 1 須增 2 條 TC。**本包不預改任何數字** —— 待 DR 回覆。
- **交付前阻斷項（DR-PMH1）**: [RULED R-PMH47] `SWE1-HMI-PM-028` 依 (ii)＋(iii) 判 out of scope 並**寫入工作簿揭露**，其 `Test Procedure`／`Expected Result` 為 `PENDING: DR-PMH1 …`。**含 PENDING 之工作簿不得出貨**（§8.4.3）—— 交付前須 DR-PMH1 結案，或由 Pei 裁定降轉。未結 DR 清單見 `DATA_REQUESTS.md`
- **Phase 6／7 之前置阻斷項**: [RULED A-PMH12] 首次填 `Q`（Estimated Test Time）或 `AF`（Test Result）之前**必須處理**兩項母本 DV 瑕疵 —— (1) priority DV 之 sqref 為 `P10:Q1411` **跨兩欄**，使 `Q` 套用 `"P0,P1,P2,P3"` 下拉，任何分鐘數都會被擋下；(2) `AF` 之列舉逐字為 `"Pass, Fail, Pending,Block,NA"`，` Fail` 與 ` Pending` **含前導空白**，寫入 `Fail`（無空格）會被擋下。二者因四份交付件該二欄全空而從未被檢驗過
- **寫回前必跑之機器檢查**: [RULED R-PMH22] `scripts/check_write_back.py` 三項（blank 前提／起始列來源／列數差），三項故意失敗測試已實跑並全部攔下，範圍向亦通過
- **⚠ 上列檢查之接線狀態**: [KNOWN-INCOMPLETE — 05 包步驟 5] 三項檢查**已實作並經故意失敗驗證**，但**尚未被任何寫回路徑呼叫** —— `feature.yaml` 之 `write_back_checks` 節目前只是宣告。R-PMH22 所要求之「於每次寫回前**自動**驗證」之**接線為 Phase 6 之交付項**。**本項為已知未完成，非疏漏、亦非 RESOLVED**（通則 8：文字修補不構成 RESOLVED，而一段未被呼叫的正確程式碼，其效力與文字修補相同）
- **規格 PDF 之文字萃取來源**: [RULED R-PMH60 — 16 包步驟 4] `sandbox/spec.txt` 由 `pdftotext -layout` 產出（`sandbox/` 於 `.gitignore` 內，不入版控；PDF 本體與其 SHA256 在 `inputs/MANIFEST.sha256`）。第二份獨立萃取 `sandbox/spec_pymupdf.txt` 由 PyMuPDF 1.28.0 產出（11 頁）。**二者之等同性以 marker 集合驗，不以字元數**：全集皆 31、逐章 13／6／1／7／1／3 全同、缺漏皆 `SU9.)`／`SU9.1)` —— **等同性成立**。指令：`python scripts/marker_coverage.py --verify-extraction sandbox/spec_pymupdf.txt`
- **⚠ 字元數不得作為等同性之依據**: [RULED R-PMH21／R-PMH60] 兩份萃取正規化後之字元數為 15,171／15,420（差 249），另分析層之 `pm.txt` 為 15,751。**該等差額不予採認為疑點** —— 抽取字元數已由 R-PMH21 明文排除於完整性／正確性／版本一致性之判準之外。03 包上繳 §6.2 早已記載同一工具差異（pymupdf 15,618 vs pdftotext 15,167），**15 包 §10 第 3 項將其重提為未解疑點，係判準之誤用**
- BLOCKED batches at start: [AUTO] **0** —— 29/29 章節於 SYS1 命中、48/48 leaf 之 `pdf_page` 已解、無 DR-PMH 待答

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:

---

## 附註 —— 本檔之產生方式

recon.py 於 2026-08-23 產出 `DECISIONS.new.md`（A-TM15 之防護：不覆寫既有檔）。
原 `DECISIONS.md` 為 scaffold 模板，**全部欄位皆為未填之 placeholder，
無任何人工內容**，故本次合併為「以 recon 產出為底，逐項補上 recon 不讀之
`RULINGS.md` 既裁條文」，未丟棄任何既有內容。`DECISIONS.new.md` 已刪除。

標為 `[RULED …]` 者為已裁條文之落地，**不是 recon 之提案**，簽核時不得
視為可逕改之 `[PROPOSED]`。
