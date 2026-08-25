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
- **ch 9 已限縮解凍（R-PMH111）**: [OPEN] `Power Transitions` 組得開批，惟**任一斷言若倚賴 p9 能力矩陣之內容，該條停並登記**。判別法：該斷言之謂詞是否為「某受控對象（`ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`）於某電源狀態下是否可用」。**A-PMH18 維持 `PENDING`，其阻斷由整組改為條件式**
- **batch 3 未產出 —— 停止條件 10 觸發（29b 步驟 8）**: [BLOCKED] ch 9 × 矩陣之全對照查出**牴觸 2 列**（`r31`／`r32`：key-off 狀態下通話結束且 `Radio off Delay = 0` → `HU OFF`，與 PM1 之「為顯示 popup 而 stay awake」取相反值，條件互斥未證）。**下放包步驟 8 逐字令「發現牴觸即停並上呈」，故 batch 3（步驟 9）未產出。**⚠ **本包無 R-PMH87 型之解除授權**；若獲授權，其解法為於 batch 3 之相關 TC 加事件層限定（無通話進行中）
- **對上游陳述之更正已落檔（R-PMH112）**: [OPEN] `DR-PMH5` 所載「已暫停 section 9 之撰寫」因 R-PMH111 而不再成立，更正句已加於 `DR-PMH8` 首段（`DATA_REQUESTS.md` §八，新 SHA256 `162d551eb2861d59`）。**該更正之發出仍屬 Pei** —— `DR-PMH8` 狀態維持 `DRAFT`
- **A-PMH24（延遲參數名稱歧義）未開新 DR**: [OPEN] `Power Accessory Delay`（規格 9.1）與 `Radio Off Delay`（矩陣 `r15`／`r31`／`r32`）之關係未定義，二者從未同時出現於任一份文件。我判其與 `DR-PMH5` 之 (1)(2) 同源而未另開 DR，**該判斷未經裁定**

---

## PENDING-ON-DR 登記簿（R-PMH115，30 包步驟 3）

> **本簿不是檢查** —— 其不判定任何事、不產生 PASS／FAIL、不增加「檢查什麼種類的錯誤」，
> 故不在 R-PMH104 之凍結範圍內（R-PMH107 之判別法）。

> **DR 之狀態改為 `ANSWERED` 時，該 DR 所繫之各筆為必辦事項**，須於該輪之上繳逐筆回報其處置。

| # | (1) 該判定之所在 | (2) 所繫之 DR 與其第幾問 | (3) 答覆為何值時改為何 | (4) 登記日期 |
|---|---|---|---|---|
| 1 | `matrix_vs_chapter.VERDICT[(9, 1, 15)]` —— 矩陣 `r15`（`Key-off`）× `PM1)` 之記法，現為 `待定義` | `DR-PMH5` (1)(2)／`DR-PMH7` Q1（`VP`）／`DR-PMH8` Q4（二延遲名是否同指） | **逐值**：(甲) `VP` = head unit 顯示螢幕 **且** 二延遲名同指 → **改記 `牴觸`**（同謂詞相反值，條件完全重合）；(乙) `VP` = head unit 顯示螢幕 **而** 二延遲名為不同設定 → **仍記 `牴觸`惟其範圍縮小**，須重寫其依據並登記條件；(丙) `VP` **非** head unit 之顯示螢幕 → **改記 `未對照`**（無共同謂詞），與二延遲名之答覆無關；(丁) 任一問未獲答覆 → **維持 `待定義`** | 2026-08-25 |
| 2 | `gen_batch02.py` 之六條 TC 各二項事件層限定中，因 `r46`／`r47` 而納入者（R-PMH95 之涵蓋兩讀） | `DR-PMH7` Q2（`Else: Mute Active` 之記法） | **逐值**：(甲) 答為「**使之靜音**」（事件使 mute 變為 active）→ **限定正當，維持不動**，並將該二列由 `待定義` 改記 `牴觸`；(乙) 答為「**維持靜音**」（mute 狀態不變）→ **該二列改記 `未對照`**，而**六條之第二項限定即為過度限定** —— 其不致誤判，惟使 TC 較規格所需為窄；**須逐條評估是否移除**（移除須重跑 lint 之限定字串檢查，因 `limits` 宣告隨之改變）；(丙) 未獲答覆 → 維持現狀（限定保留，二列維持 `待定義`） | 2026-08-25 |
| 3 | `gen_batch02.py` 之 `-013`（`Once a Day`）之 procedure 與 `-011` 之 pre_condition | `DR-PMH8` Q1（「一日」之起算點）／Q2（設定之所在路徑） | **逐值**：(甲) Q1 答為具體起算點（午夜／點火週期／滾動 24 小時）→ **`-013` 之步驟須重寫**，以該起算點表述其「第二次觸發」之時點，並增一項 input_test_data；(乙) Q1 答為「未定義／由實作決定」→ **維持現狀**（現行措詞 `on the same day` 於三讀皆成立），並將此登記為永久限度；(丙) Q2 答為具體路徑 → **`-011` 之 pre_condition 改寫為該路徑**，其 `test_procedure` 之第 1 步隨之具體化；(丁) Q2 未答 → 維持 `the setting menu` 之措詞 | 2026-08-25 |
| 4 | `ANOMALIES.md` 之 **A-PMH23**（告別音之跨螢幕同步無 ER 斷言）與 `gen_batch02.py` 之 `-010` | `DR-PMH8` Q3（`Sounds will sync amongst all supported vehicle displays.` 是否涵蓋告別音） | **逐值**：(甲) 答為「涵蓋二者」→ **`-010` 之 ER 須增一條**（告別音於各支援螢幕間同步）**且其 procedure 須增一步**（維持 1:1），A-PMH23 改 `RESOLVED`；(乙) 答為「只涵蓋啟動音」→ **`-010` 不動**，A-PMH23 改 `ACCEPTED（經釐清不補）`；(丙) 答為「只涵蓋告別音」→ **`-009` 之 ER4 須移至 `-010`**（此讀法目前未被任何產出所採，其後果最大）；(丁) 未答 → 維持現狀，A-PMH23 續 `PENDING` | 2026-08-25 |
| 5 | `gen_batch03.py` 之 `Power Transitions` 各 TC 之 Pre-Condition `No phone call or projection call is active`（R-PMH113） | `DR-PMH8` Q5（IGN OFF 後通話結束且有 popup 待顯示時之行為） | **逐值**：(甲) 答為「**應 stay awake**」（`PM1)` 優先）→ **該 Pre-Condition 得移除**，且**應增一條 TC** 驗「通話結束後 popup 仍顯示」；`r31`／`r32` 之記法由 `牴觸` 改為 `未對照`（矩陣該格須更正）；(乙) 答為「**應關機**」（矩陣優先）→ **該 Pre-Condition 保留**，且 `PM1)` 之條件須加註例外；**應增一條 TC** 驗「通話結束即關機」；`r31`／`r32` 改記 `印證`（對該新 TC 而言）；(丙) 答為「由實作決定／無定論」→ **Pre-Condition 保留**，該行為永久登記為覆蓋缺口；(丁) 未答 → 維持現狀（Pre-Condition 保留，`r31`／`r32` 維持 `牴觸`） | 2026-08-25 |
| 6 | `matrix_vs_chapter.VERDICT[(9, 1, 6)]`／`[(9, 19, 24)]`／`[(9, 19, 25)]` —— 三列現為 `待定義` | `DR-PMH7` Q1（`VP` 之定義） | **逐值**：(甲) `VP` = head unit 之顯示螢幕 → **三列逐列重判**，其中 `r25`（`VP Turns Off` 於 key-off 狀態門開啟）**極可能改記 `牴觸`**（與 `PM1)` 之 stay awake 期間可同時成立而取相反值）；(乙) `VP` 為他物（如儀表板顯示）→ **三列改記 `未對照`**；(丙) 未答 → 維持 `待定義`。⚠ **本筆與第 1 筆之差別**：`r15` 另受 A-PMH24 所阻，即使本問獲答仍可能無法判定 | 2026-08-25 |
| 7 | `Power Transitions` 組（batch 3）之全部斷言 —— 其是否須依 R-PMH94 重掃 | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」並提供之 → **該文件為第七筆素材**，須補 `MANIFEST.sha256`，**batch 3 之全部斷言須依 R-PMH94 對其重掃一次**（R-PMH111 末段明令）；(乙) 答為「p9 自身即權威」→ **batch 3 之各 TC 須逐條複驗 R-PMH111 之判別法結果**（原判「不倚賴 p9」者仍成立，惟其依據由「來源不明」改為「主題不同」）；A-PMH18 改 `RESOLVED`；(丙) 未答 → 維持現狀，A-PMH18 續 `PENDING`，R-PMH111 之條件式續行 | 2026-08-25 |

| 8 | `spec_assertion_scan.IGNOFF_LINE_VERDICT[160]` —— 規格 p4 之 `Note: do not show popup again if popup was shown at Radio Off.`，現為 `待定義` | `DR-PMH7` Q3（該 `Note:` 之適用範圍） | **逐值**：(甲) 答為「**泛指所有 popup**」→ **改記 `牴觸`** —— 於 Radio Off 已顯示過之 popup 於 IGN OFF 不得再顯示，與 batch 3 之斷言取相反值；**`-016`～`-021` 須加 Pre-Condition「本次點火週期內該 popup 尚未於 Radio Off 顯示過」**；(乙) 答為「**僅適用於同段之 `Geolocation + SOS Popup`**」→ **改記 `未對照`**，batch 3 不動；(丙) 未答 → 維持 `待定義` | 2026-08-25 |
| 9 | `gen_batch03.py` 之 `-017` —— `60 秒無互動` 與 `總計 10 分鐘` 二上限**何者先到即何者生效**，本條以二個獨立步驟分別驗之而**不斷言其交互作用** | **無所繫之 DR** —— 規格未言，而**尚未有任何 DR 問及此事** | **逐值**：(甲) 若日後開問並答為「以先到者為準」→ **`-017` 須增一步驟與一 ER** 驗其交互（例如互動至第 9 分鐘後停手，驗其於 60 秒後關機而非等到第 10 分鐘）；(乙) 答為「10 分鐘為硬上限，互動中亦強制關機」→ **ER3 須改寫為斷言其強制性**；(丙) 未開問 → 維持現狀。⚠ **本筆為 `PENDING-ON-DR` 簿中唯一無所繫 DR 者** —— **其是否開問由下輪處置**（31 包步驟 5 明令本輪只登記） | 2026-08-25 |
| 10 | `ANOMALIES.md` 之 **A-PMH25**（9.1 權威文本於逾時處為破句）與 `-016` 之不斷言處置 | **無所繫之 DR** —— 30 包我判其「答覆不改變產出」而未併入 `DR-PMH8`，**該判斷未經裁定** | **逐值**：(甲) 若開問並答為具體秒數 → **`-016` 須增一步驟與一 ER** 驗該逾時；(乙) 答為「以 pop-up list 所定義者為準」→ **須取得該 pop-up list**（新素材），否則永久登記為缺口；(丙) 未開問 → 該行為**不會有任何一條 TC 驗到其秒數**，風險續存。⚠ **其與 R-PMH75 所承擔之風險（`the radio should shut Off` 不被驗到）為同一來源** | 2026-08-25 |
| 11 | `gen_batch04.py` 之 `-024` **撤除**（R-PMH129）—— `SU1.)` 之「動畫後呈現 splash，1.5 each」一句無 leaf，其行為**無任何 TC 覆蓋** | `DR-PMH8` Q6（該句是否應納入 037） | **逐值**：(甲) 答為「**應納入**」→ 其成為**新 leaf**，`Splash Screen` 組由 3 增為 **4**，`n_leaf` 46 → **47**，granularity 須全項重跑，**`-024` 依其保留於 `gen_batch04.py` 之定義重寫並解除 `dropped`**；(乙) 答為「**不納入**」→ 該行為**永久登記為覆蓋缺口**，`-024` 之定義維持 `dropped`；(丙) 未答 → 維持現狀（撤除，缺口續存） | 2026-08-25 |
| 12 | `ANOMALIES.md` 之 **A-PMH28**（p3–p7 流程圖之五類行為）—— 依 **R-PMH131** 不寫 TC | `DR-PMH8` Q7（流程圖是否為規範性；其散文所無之陳述是否應成為需求） | **逐值**：(甲) 答為「**流程圖為規範性且該五類應入 037**」→ 其成為**新 leaf**，`n_leaf` 增其數，**另批撰寫**；`-026`／`-033`／`-034` 之「不斷言輪替順序」隨之解除；(乙) 答為「**流程圖非規範性**」→ 五類永久登記為覆蓋缺口，**A-PMH04 之提案 (a)（render 入 `data/`）亦隨之失去理由**；(丙) 答為「規範性但不必入 037」→ **其為判讀背景而非需求**（同 State Matrix 之地位，R-PMH73），則各 TC 須依 R-PMH79 對其重掃一次牴觸；(丁) 未答 → 維持現狀 | 2026-08-25 |
| 13 | `generated/batch03.json` 之 `stopped` 中之 **`-023`**（`PITA8`）—— 停手待答，**非 out of scope** | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」→ 取得後 **`-023` 得撰寫 TC**，`Power Transitions` 組由 5 leaf 有 TC 增為 **6**；(乙) 答為「p9 自身即權威」→ **`-023` 得撰寫，惟其斷言須逐條套 R-PMH111 之判別法並具名**；(丙) 答為「p9 無權威來源」→ `-023` **改判 out of scope**，其狀態詞屆時方改為 `ACCEPTED`，`n_leaf` 46 → **45**；(丁) 未答 → 維持 `STOPPED-PENDING-DR`。⚠ **依 R-PMH130，其於「已知未決清單」之出現理由為「待答」而非「已接受」** | 2026-08-25 |
| 14 | `gen_batch01.py` 之 `-008`（leaf `-022-02`）—— 其 DESC 之例外 `unless certain phone call scenarios have occurred` **未被任何 pre_condition 排除** | `DR-PMH8` Q8（該 `certain` 指哪些情境） | **逐值**：(甲) 上游列舉該等情境 → **`-008` 之 pre_condition 須增其排除**，且**應評估是否另立 TC 驗該例外之行為**（其時該例外即成為可驗之行為）；(乙) 答為「無特定情境／該句為贅語」→ **`-008` 不動**，該例外自 DESC 之涵蓋要求中移除；(丙) 未答 → **`-008` 之射程持續不足**，其於「已知未決清單」中具名。⚠ **037 之 DESC 於同處亦未列舉** —— 非 SYS1 側之偏差，而是上游本身未定義 | 2026-08-25 |
**合計 14 筆。** 其分布：`DR-PMH5` 2 筆（#1／#7）、`DR-PMH7` 4 筆（#1／#2／#6／#8）、`DR-PMH8` **7** 筆（#1／#3／#4／#5／#11／#12／#14）、**無所繫之 DR 2 筆（#9／#10）**——一筆得繫於多個問。

> **34a（R-PMH132）之補入**：#11（`-024` 之撤除）、#12（A-PMH28 之五類）、#13（`-023` 之停手）。
> **R-PMH132(b) 生效後，本簿之各筆全數為交付揭露事項** —— 其第 (3) 欄即「已知未決清單」之內容。

> ⚠ **#9／#10 為本簿之新形態：「其判定繫於一個尚未存在之問」。**
> R-PMH115 之簿設計為「繫於某 DR 之答覆」，**未預期此形態**。
> 我以「所繫之 DR」欄記「無所繫之 DR」並具名其緣由，**該處置未經裁定**；
> 31 包步驟 5 明令「其是否須開 DR 由下輪處置，本輪只登記」，故本輪不開問。

> ⚠ **本簿之完整性無任何檢查所保證** —— 其為人工登記，**漏登之判定不會出現於此，亦不會有任何東西指出它漏了**。此一限度依 R-PMH52 於此具名。
- **batch 3 已產出，惟 7 leaf 中 2 leaf 停手（30 包步驟 4）**: [OPEN — 狀態詞依 R-PMH123 核對：`-023` 為 **`STOPPED-PENDING-DR`**，**非 `ACCEPTED` 亦非 `RESOLVED`**] `SWE1-HMI-PM-023`（10.5，`PITA8`）**經 R-PMH111 判別為倚賴 p9**（其謂詞正是「`Headunit` 於 `KEY OFF (No ACC)` × `HEADUNIT POWER ON` 下之可用程度」，且 PDF 中其前一行逐字為 `HEADUNIT POWER ON:`）→ **停並登記，不得產出**。`SWE1-HMI-PM-002`（7.1.1，`SU1.1`）**非因 p9 而停**（判別為「否」），其停手理由為**本句未載任何可驗之行為**（委於 `vehicle architecture` 與 `CFTS009`，後者非本 feature 所持有）—— **形態同 `-028`（R-PMH47(a)／R-PMH72），惟本筆未經任何裁定**
- **lint 之二項一般化（30 包，R-PMH107）**: [CLOSED] (a) `R-PMH50 source_clause 取自 PDF` → **`source_clause 逐字見於其所宣告之來源`** —— 原檢查會把「正確遵守 R-PMH75」判為 FAIL；新形態**更強**，實際回原文件比對。**其首次執行即查出 batch 1 之四條與 `sandbox/spec.txt` 之字形差異**（彎撇／刪節號），該差異只在字形不在字詞，已於 `_norm_src` 具名吸收。(b) §4.3.1 之比對於兩側同時去 `[CRnnnnn]`（A-PMH26）。**檢查項數維持 32**
- **`-002` 判 out of scope（R-PMH117）**: [CLOSED — Pei 於 2026-08-25 逐字裁定「核可」，連帶已全數執行] `SWE1-HMI-PM-002`（7.1.1，`SU1.1)`）依 canon §8.4.2 之三項判準與 `-028` 完全同型 → 判 out of scope、不寫入交付工作簿（比照 R-PMH72）。**其效力起於 Pei 之核可**（動到範圍：有 TC 之 leaf 47 → 46，R-PMH1 為範圍條文）。**已生效**：台帳二處標 `EXCLUDED-BY-R-PMH117`；`N_LEAF` 47 → **46** 並全項重跑（G1–G5 全 PASS，`--self-test` 五錨點如期 FAIL、`--check-doc-sync` PASS）；`framework.md` 之 `Power Transitions` 7 → **6**、合計 47 → **46**；**A6 錨點之組態由 `15×3+1×2` 改為 `14×3+2×2`** —— 沿用舊式會得 `min=1` 而使隔離失效，**已加 `assert` 攔之**。⚠ **`-023` 留在組內** —— 其為停手待 DR，非 out of scope，二者不得合併處置。登記於 A-PMH27
- **apparatus 首次解凍已用畢並恢復凍結（R-PMH116）**: [CLOSED — 31 包步驟 2] 解凍範圍嚴格限於 lint 之「§5.2B／§5.5 Final Step 含驗證意圖」一項。**病灶**：原判準含 `record`／`read`／裸 `compare` —— 三者為**蒐集資料**之動詞而非**驗證**之動詞。**強化後**須有明言判準之驗證子句。**must-hit 5/5 FAIL、範圍向 15/15 PASS、`Compare` 邊界二例皆符**。**新增檢查項 0**（同一 `chk(...)` 之判準強化，非新檢查）；**新增旗標 1**（`--final-step-must-hit`，其為該檢查之錨點）。**自本包結束起恢復凍結**
- **batch 3 由 6 條增為 8 條（31 包 §2.2）**: [CLOSED] `-019`（排程／取消）與 `-020`（設定完成／取消設定）各含兩個獨立分支 —— 依 canon §8.2.2 之壓力測試，**兩個獨立之部分失效落在同一個 pass/fail 判定上即為 bundling**，故各拆為二條。`-018`／`-019`／`-020`／`-021`／`-022` 之 `design_method` 依 **R-PMH118** 齊一為 EP；**`-023` 維持 FUNC**，其理由為**該輸入自始未被劃分為等價類**（權威文本只給 `dismisses` 一個分支）——**無劃分即無 EP，該界線於其 reasoning 具名**
- **停手三筆之狀態詞一致性核對（R-PMH123，33 包步驟 4）**: [CLOSED] **三者不同類，其狀態詞因而不同，此為刻意**：`-002`（A-PMH27）與 `-028`（A-PMH13）皆為 **`ACCEPTED`** —— 經裁定 out of scope、不寫入工作簿，**其缺口之事實未消失**；`-028` 原標 `RESOLVED（處置已定）`，**本包依 R-PMH123 更正為 `ACCEPTED`**。**`-023` 為 `STOPPED-PENDING-DR`** —— 其**仍在交付範圍內**（`Power Transitions` 組之 6 leaf 之一），只是暫不產出 TC，待 `DR-PMH5` `ANSWERED`。⚠ **R-PMH123 令三者「一致為 ACCEPTED」，而我判 `-023` 不同類故不改** —— **out of scope 與 stopped-pending 之差別正是 R-PMH119(b) 所分者**；一句話可反轉
- **`input_test_data` 四批一致化（33 包步驟 3）**: [CLOSED] 四批 **37 條全為 `NA`**。⚠ **下放包 §2.3 謂「batch 1／2／3 皆為 `NA`」而實測 batch 3 為 `N/A`** —— **兩批須改而非一批**，已一併更正。⚠ **下放包謂 43 條，實測 37 條**（8＋7＋8＋14）
