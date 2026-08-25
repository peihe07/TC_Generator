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
- **outline `9.1` 之 `source_clause` 例外**: [RULED R-PMH75 — Pei 2026-08-24「以刪掉之後的為主」] `Power Transitions` 組之 5 leaf（`SWE1-HMI-PM-018-01`～`-05`，引 outline 9.1）其 `source_clause` **取自 SYS1 匯出，非 PDF** —— R-PMH50 於此反轉。`source_clause_origin` 須逐字記 `sys1_export 9.1` 並註 `R-PMH75`。**R-PMH50 於其餘 46 leaf 維持不變。** ⚠ **本輪未改 profile**（R-PMH46 之一次性授權已用畢，profile 之修改須經 Pei 核可）—— 開批前須確認撰寫者知悉本例外，否則會誤用 R-PMH50 之通則。**承擔之風險**：`the radio should shut Off`（逾時後收音機關機）不會有任何一條 TC 驗到
- **`SWE1-HMI-PM-028` 之排除**: [RULED R-PMH72 — Pei 2026-08-24「DR-PMH1 拿掉」] 不寫入交付工作簿、不產出 TC、不以 `PENDING` 佔位。`Off Road Plus` 3 → **2** leaf；有 TC 之 leaf 48 → **47**；granularity 之分母改 47 並全項重跑（8/47 = 0.1702 G1 ✅、min 2 ✅、9/47 = 0.1915 G4 ✅、[2,9] ⊂ [2,23] G5 ✅；A6 錨點重算為 47 分 16 組）。其列**保留**於 `layer3_sections.tsv`（48 列，增 `excluded_by` 欄）與 `outline_map.json`，標 `EXCLUDED-BY-R-PMH72`
- **⚠ State Matrix 之內容與 PDF p9 不對應**: [STOPPED — A-PMH18，19 包步驟 8] R-PMH73 定該 Excel 為 ch 9 之規範性判讀背景，**惟實測其軸與 p9 之軸逐字探針全 0**（13 個探針）。依 R-PMH73 明文「不一致者不得自行取捨，停並上呈」——**未將 A-PMH14 新漏 2 改為 `RESOLVED`**（其前提不成立），**ch 9 不得開批**。新漏 3 已改 `RESOLVED（來源已補）`，二者處置不同之理由見 `ANOMALIES.md`
- **ch 9（`Power Transitions`）不得開批**: [BLOCKED — A-PMH18／`DR-PMH5`] p9 之能力矩陣仍無來源。所提供之 `DCR21421` State Matrix 經**逐字**與**語意**兩層對照皆不涵蓋 p9（20 包 §2.1）。**R-PMH73 之「該矩陣為 ch 9 之判讀背景」已由 R-PMH76 更正** —— 其真正效力範圍為 ch 12 與 ch 10 之一部
- **`Off Road Plus` 開批之前置**: [RULED R-PMH76 — 20 包 §三] 該 Excel 列 16（`SRT or Off Road+ Hard Button press.`）對 ch 12 有直接效力。`-027` 之 Pre-Condition **須含「車輛已處於 Off Road state」**，否則其 ER「不喚醒」與矩陣之 `Radio Wakes Up and mutes` 直接衝突（二者為互補之兩支）。**本輪只回報依據，未撰寫 TC**
- **⚠ `RESIDUE_VERDICT` 之第二來源尚未建立**: [KNOWN-INCOMPLETE — 19 §14 第 2 項，20 包步驟 7 明令登記] `chapter_bidirectional.py` 之 20 條殘餘人讀結論，其中 13 條為執行層本人所寫，**既是判準之作者也是那個「人」**。其正解為分析層人讀，**已排入下一輪**。本項為已知未完成，非疏漏、亦非 RESOLVED（通則 8）
- **`10.3`（PITA6）之撰寫方式**: [RULED R-PMH80] `Power Off Behavior` 組（8 leaf）**得開批**。其 `10.3` 之 TC **Pre-Condition 須加「倒車影像未顯示（`Gear != Reverse`）」**（依 R-PMH55 之形態限縮，來源矩陣 `r48c10` 於 `reasoning` 具名）；RVC 情境之 `Popup not displayed over RVC` **只在矩陣有、規格未載**，依 R-PMH55(b) **不撰 TC**，登記為覆蓋缺口並開 `DR-PMH6`。**執行層所提之「PITA4 通則／例外」調和不採** —— `PITA4` 之對象為按鍵輸入，非 popup 之顯示
- **章 8／章 11 尚未與 State Matrix 對照**: [KNOWN-INCOMPLETE — 21 包 §3／A-PMH18 補記] ch 7 已全對照（30 事件列，牴觸 0），ch 10／12 於 20 包部分對照。**章 8（6 leaf）與章 11（5 leaf）完全未對照**，而矩陣之 `VR button long press without/at Projection`（`r11`／`r12`／`r28`／`r29`）與 ch 11 之 `VRLP1` 顯有共同主題。**該二章開批前應先完成其對照**
- **batch 1 之覆核線結束（R-PMH103）**: [CLOSED — 28 包步驟 4；**28a 經 Pei 核可生效（R-PMH105(a)）**] batch 1（8 條 TC，7 leaf）之覆核線依 R-PMH103 結束 —— 27 包之六項自評中**三項實質、三項精化**，為 Phase 4 開批十六輪以來首次多數不指向產出可能有錯。三項實質項已於 28 包處理（待判定不再計入已判定／PC 全枚舉 4,176 項／`test_procedure` 逐步驟二分 25 步）。**其殘餘為三項精化 ＋ `-007` 之 `L160` 待確認（`DR-PMH7`）。batch 1 仍不得寫回工作簿，其阻斷改為單一項：`tc_id` 為 provisional，待全 47 leaf 完成後單次指派**（12 包 §五）
- **KNOWN-INCOMPLETE（一）切分之連接詞仍是列舉**: [R-PMH103 之精化項] `SPLIT_CONNECTIVES` 為五個連接詞之列舉；**以無連接詞之並置表達之複合命題不會被切開**。**風險**：某 TC 之 ER 含兩個命題而只被判為一個，其中一個因而未經掃描 —— **27 包之 `-003` ER2 即此形態之實例（已修）**，惟該次是靠 `while` 被列入才抓到。**不再排程**
- **KNOWN-INCOMPLETE（二）`SPLIT_REVIEW` 無第二來源**: [R-PMH103 之精化項] R-PMH101(b) 令「人讀複核」，**而產生候選與複核為同一人**。**風險**：某候選被錯判為「非獨立命題」而併回，其斷言因而不入母體。**現行八項複核中兩項判為不接受（`-005`／`-006` PC2.2），其原句確為單一命題，可覆查。不再排程**
- **KNOWN-INCOMPLETE（三）規格側之全枚舉未做**: [R-PMH103 之精化項] R-PMH98 現只實施矩陣側（174 格 × 各斷言）。規格側之母體已界定並量為 **235 行**（p8–p11 之敘述行，27 包步驟 6），**惟未做逐行判定**。**風險**：規格自身之某行與某斷言取相反值而其用詞未被關鍵詞命中 —— **23 包之 `pop-up` 掃描曾以關鍵詞查出 p9 之兩行（A-PMH21），故該風險非理論**。**不再排程**
- **batch 2 之產出**: [28 包步驟 5] `Startup Sounds`（ch 8，6 leaf）→ **7 條 TC**（`SWE1-HMI-PM-012` 依 profile §4 拆為 2 條）。**選批理由三項皆可查**：章 8 雙向複驗新漏 0（17 包）／矩陣全對照牴觸 0（26 包）／marker 6/6 全在 SYS1（14 包）；**不受任何 DR 阻斷**。`tc_id` 續為 provisional，**零寫回**
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
- **R-PMH103／R-PMH104 已核可生效（R-PMH105）**: [CLOSED — 28a 包] Pei 於 2026-08-25 逐字裁定「寄 核可」。三項效力起算：(a) batch 1 覆核線**結束**，殘餘之三項精化＋`-007` 之 `L160` 待確認全數為 KNOWN-INCOMPLETE，**不阻斷開批**；(b) apparatus **凍結生效** —— 現有 32 項 lint 與 13 支程式全數保留並繼續執行，凍結者為其增長；(c) batch 2（`Startup Sounds`，ch 8，6 leaf）**開批**。**解凍條件不變**：某條已產出之 TC 經**實測**有誤且為現行檢查所不能攔者，或 Pei 裁定
- **三筆 DR 之發出已授權但尚未發出（R-PMH106）**: [OPEN] 最終全文落於 `DATA_REQUESTS.md` §七（三份逐字，SHA256 已記）。**執行層不得代為發出**（R-PMH83），`SENT` 欄留空至 Pei 告知**實際日期與對象**（R-PMH43）。**「已授權」不等於「已發出」——在該日期填入前，`DR-PMH5` 仍凍結 ch 9 之 5 leaf**
- **KNOWN-INCOMPLETE（四）`animation` 斷言之掃描未做**: [R-PMH104 凍結] batch 2 之 `-009`／`-010` 之 ER 含開機／關機動畫之斷言，依 R-PMH94 該有其自己的一次掃描，**而新增斷言即新增檢查項**（R-PMH104）。**風險**：矩陣或規格某處與動畫斷言取相反值而未被發現。**不再排程；解凍須依 R-PMH104(a)(b)**
