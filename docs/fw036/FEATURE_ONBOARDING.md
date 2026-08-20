# FEATURE_ONBOARDING — FW036 TC Generation Process Canon

How a new feature (with or without an HMI spec, with or without existing
workbook content) enters the pipeline. Distilled from the Media and Home
runs. This file is the process authority; feature RUNBOOKs instantiate it.

---

## 0. Decision authority matrix — THE core of this canon

Every decision in the pipeline belongs to exactly one tier. When in doubt,
escalate one tier up — never down.

### Tier 0 — AUTO (recon script decides; humans only see the result)

- Intake classification: file kinds sniffed by CONTENT (sheet signatures,
  PU-column detection, text-layer probe), spec_mode proposal, and the
  **missing-document list derived from the 037 HMI Source ID column** — the
  requirements themselves name their sources, so "what do I still need" is
  machine-derivable on day one (Home lesson: the Last Mode citation sat in
  037 from the start and was only noticed mid-pipeline). Label-variant
  matches are flagged for confirmation (A-H03 pattern). Obtaining the files
  stays Tier 3.
- **036 母本選擇（R-G1，Pei 2026-08-17，全域）**：自 2026-08-17 起所有新
  feature 一律以 `forms/…_SWQT_20260817_ext.xlsx` 為 036 母本，不再逐
  feature 詢問。既有 feature 之已交付件不因本條改變。結構事實見
  `forms/FORMS.md` §`…_SWQT_20260817_ext.xlsx`。配套之 R-G2 已將其餘三份
  036 檔以`mv` 移入 `archive/forms_superseded/`（不刪除）。
  註：該母本 R 欄 design_method 之 DV 為 x14 擴充，openpyxl 讀取即丟棄 ——
  **任何以 openpyxl 存回母本之操作都會摧毀該下拉**（R16/R18-3 之外的獨立理由）。
  已實測（2026-08-17，repo 外複本）：`<x14:dataValidation>` 1 → 0、
  zip members 48 → 47，而三條 legacy DV（P／T–Z／AF）存活、工作表數與 B 欄
  公式範圍不變 —— **損壞是選擇性的，只比對列數／公式／工作表數的檢查會全綠**。
  §`Workbook sync`（framework.md Part I）之 `wb.save()` 範例跑在 rev A/B 版面
  （無 x14 DV），照抄到本母本即為此缺陷。見 user_profiles A-UP09。
- `workbook_state` detection when segmentation is unambiguous
- Column mapping via header-text match (report match count, e.g. 32/32)
- Design-method vocabulary extraction from the 下拉選單 sheet
- Leaf inventory, coverage-gap counts, done-region req_id sets
- Spec text-layer availability (`pdftotext` yield test)
- spec_id → section/outline mapping build (fail-loud on miss)

**明列之三項（2026-08-17，User Profiles 09 輪 §4）—— 目的為減少逐項請裁，
不是擴大自裁權**：

- **工作簿欄位字串與 framework 表之逐字一致** —— 例如 H 欄之 Test Set 值須與
  framework §2 之表逐字相同（含大小寫）。**照抄不是判斷**；表本身之內容仍為
  Tier 2（R-U39(3) 之核可即此形態：問的是「照抄對不對」，而那不必問）
- **既有條文之機械套用** —— 條文已明定判準且該判準不需解釋時，逕行套用。
  **判準需要解釋、或同一條文可作兩種讀法時，不屬本項**（R-U39(2) 即反例：
  R-U22 之「PROF-001-01 之處置」可讀成限縮亦可讀成舉例，**那不是機械套用**）
- **量測條件之技術選擇** —— 用 `zipfile` 或 `openpyxl`、以正則或詞庫、
  窗口取多長。**惟其判準與偽陽性風險須於上繳包揭露**（R-G8），
  且**選擇改變了結論時，該改變本身是 Tier 2**（08 輪之等長窗口即此形態：
  技術選擇之修正改了兩個注入向之結果，故其修正經回報而非逕行採用）

> **三項之共同界線**：AUTO 管的是「怎麼做」，不是「做什麼」與「做出來對不對」。
> 一旦選擇會改變結論，它就不再是技術選擇。

Output convention: `[AUTO]` entries in DECISIONS.md. No sign-off needed,
but they are recorded so an audit can see what was machine-determined.

### Tier 1 — Claude Code, cleared to proceed (canon-bound, gate-checked)

No discussion needed. Claude Code executes per this canon + feature RUNBOOK
+ profile, and the gates (lint, write-back invariants) catch drift:

- Porting/adapting pipeline scripts; `feature.yaml` wiring
- Building data artifacts (outline map, spec split, exemplars, sibling map)
- Batch context assembly
- **Generation of all post-pilot batches** (pilot itself is Tier 2)
- Lint runs; write-back runs (invariants ABORT on violation — an aborted
  run escalates to Tier 2, it is never "fixed" by weakening the invariant)
- ANOMALIES.md **registration** (recording a finding with evidence and a
  proposed disposition — NOT ruling on it)
- DECISIONS.md `[AUTO]` entries; git commits per repo convention
- Regenerating any derived artifact

### Tier 2 — discuss with Claude (chat), Pei signs

Judgment calls that shape scope, traceability, or audit posture. Claude
prepares a recommendation with evidence; Pei rules. The ruling is written
into DECISIONS.md or ANOMALIES.md verbatim:

- All `[PROPOSED]` entries in DECISIONS.md (batch sign-off, one pass)
- framework.md Part N Test Set derivation and granularity
- Profile `[OVERRIDE]` clauses — anything that displaces a docs.md generic
  rule needs an explicit, cited override
- Anomaly dispositions (PENDING → RESOLVED)
- **Pilot batch review** (the one mandatory human quality gate)
- Boundary cases: blocked-parent proportion, scope carve-out vs assumption
  marker, negative-pair sufficiency, cross-feature exemplar admissibility
- Any write-back invariant violation
- Splitting or merging a Test Set after generation has started

### Tier 3 — Pei only (not delegable)

- Final xlsx submission through controlled document management
- Release tag creation (SHA256 ↔ commit binding)
- Sending RD-1 questions / spec-file requests upstream
- Anything that signs the controlled document

### Escalation triggers — Claude Code MUST stop and file, never improvise

1. Spec lookup unresolved (missing section, missing PU id, missing file)
2. `workbook_state` segmentation ambiguous (mixed qualifying/placeholder
   rows inside one segment)
3. Write-back invariant violation
4. A needed rule has no profile/canon coverage (candidate new [OVERRIDE])
5. Fabrication pressure: any value the source does not state (§8.4)
6. Done-region content that contradicts the spec (A-026 pattern)

Filing = a DECISIONS.md or ANOMALIES.md entry with evidence + proposed
disposition, then continue with unaffected work.

---

## 1. Phase map

```
Phase 0  Intake     — dump files into _intake/<Feature>/; run intake.py
Phase 1  Recon      — automated survey → RECON.md + DECISIONS.md (pre-filled)
Phase 2  Rulings    — Pei reviews DECISIONS.md [PROPOSED] items, signs   (Tier 2)
Phase 3  Framework  — framework.md Part N + profile file                 (Tier 2)
Phase 4  Data build — scripts + feature.yaml → data artifacts            (Tier 1)
Phase 5  Pilot      — one batch → Pei review → prompt adjustments        (Tier 2)
Phase 6  Batch      — generate → lint → write-back                       (Tier 1)
Phase 7  Delivery   — tag + submission + RD-1                            (Tier 3)
```

Phases 0–1 and 4 are fully delegable start-to-finish. The human time cost
of a new feature is: one DECISIONS.md pass (Phase 2), one framework/profile
review (Phase 3), one pilot review (Phase 5), one dry-run approval and
delivery (Phase 7). Validated end-to-end by the Home run (2026-08-09).

### 1.1 Three-layer quality structure (validated: Home A-H10)

A green lint is necessary, never sufficient. The layers catch different
defect classes and none substitutes for another:

1. **Lint** catches mechanical drift — vocabulary, format, resolution,
   traceability. It cannot catch a wrong rule: Home's corpus was lint-green
   while carrying a notation error, because the lint rule itself encoded
   the wrong scope.
2. **The human pilot gate** catches judgment drift — style-authority
   misreads, scope calls, rule-scope errors. This is why Phase 5 is the one
   mandatory human quality gate and generation of post-pilot batches must
   not be treated as license to skip it retroactively.
3. **The done region arbitrates disputes with evidence.** When reviewer
   intuition and generated output disagree, check what the done region
   actually does before ruling — in the Home pilot it overturned two
   reviewer suspicions (an "invented" constant and a blank-field choice were
   both done-region precedent) and settled one real defect (quote notation).
   Corollary: a reviewer finding is not a defect until it survives the
   done-region check.

### 1.2 Pilot review protocol (Phase 5)

- Sample: the pilot batch in full, plus at least one parent from every other
  batch (stratified). Cover every placeholder and every anomaly-bearing TC.
- Review order per TC: reasoning → split vs 037 sub-ids → Pre-Condition
  scope → procedure/ER wording vs done region → priority argument.
- Every finding is classified before it blocks anything: defect (fix
  corpus-wide), style divergence (check done region first — see 1.1.3),
  or note (record, don't fix).
- Output: a digest in chat with verdict PASS / PASS-with-corrections /
  REGENERATE, the correction list, and any lint-rule amendments. The verdict
  and ratifications are recorded in ANOMALIES.md as the pilot gate entry.
- If generation ran ahead of an unsigned ruling (schedule pressure), the
  review scope EXPANDS to verify the assumed rulings — retroactive
  ratification is recorded explicitly, never implied.

---

## 2. workbook_state — automated classification (Phase 1)

For every data row after the header:

1. **Filled row**: Test Item or TC ID non-empty.
2. **Qualifying done row**: author non-empty AND Procedure has ≥2 numbered
   steps AND content is non-placeholder. (Media lesson: draft rows with
   `Procedure = "Test"` are filled but NOT done.)
3. Segment qualifying rows → classify:

| State | Definition | Precedent |
|---|---|---|
| `BLANK` | zero filled rows | — |
| `PARTIAL_CLEAN` | contiguous done region + trailing blank/draft | Media (10–332 done, 333+ draft) |
| `PARTIAL_INTERLEAVED` | done and regen segments alternate | Home (3 Arif segments, 2+1 gaps) |
| `FULL` | all rows qualify | audit-only mode, no generation |

Ambiguous segmentation → Tier 2 with suspect row numbers listed.

### Per-state strategy binding

| Decision | BLANK | PARTIAL_CLEAN | PARTIAL_INTERLEAVED | FULL |
|---|---|---|---|---|
| Style authority | fallback chain (§3) | done region | done region | done region |
| Write-back | append from first data row | positional freeze + rewrite tail | in-place segment rewrite + **content-hash** invariant | none |
| Done invariant | n/a | positional hash | ordered content hash | full hash |
| Draft rows | n/a | discard & regenerate (default) | discard & regenerate (default) | n/a |

### BLANK fallback chain (style decisions when no done region exists)

`done region → nearest FW036 sibling feature done region (STYLE ONLY) →
docs.md generic rules`

Bindings under BLANK:

- Test Item = standard §4.3 tc_title (no precedent to defer to)
- Test Group / Test Set columns = **FILL** per framework Part N
  (TEST_SET_POLICY is itself the default when no precedent overrides it)
- spec_reference = constructed from spec_mode template (§10.7)
- Cross-feature exemplars carry marker `cross-feature: style only`; every
  literal (label, number, popup text, state name) MUST be re-traced to the
  current feature's spec — enforced as a lint rule, not by discipline
  (A-026 lesson)

---

## 3. spec_mode — source taxonomy (Phase 0)

| Mode | Source shape | Text pipeline | spec_reference | Precedent |
|---|---|---|---|---|
| A | Polarion/SYS1 export | outline map from export | `{filename}_{outline}` | Media, Home |
| B | PDF with text layer | pdftotext + section regex | `{filename}_{section}` | Home (hybrid A+B) |
| C | Scanned PDF | OCR pipeline + PNG render | via SYS1 if available, else OCR-anchored | Media images |
| D | CFTS / Word | doc extraction; reference is **looked up, never constructed** | CFTS clause id / SYS3 long form | BT profile §3.6 |
| E | No spec (037/SWRA only) | none | Verification Criteria column; expect heavy BLOCKED + RD-1 | — |

A feature may combine modes (Home = A for text + C for figure pages).
Images are always rendered for figure/table pages regardless of mode —
anatomy layouts and tables often exist only in images.

**Mode A blind spot (Home A-H12/16/18)**: a Polarion export can silently
drop SENTENCES inside sections it otherwise carries. Item-code diffing
(`spec_diff`-style) sees only missing sections, never missing sentences —
Home's export dropped three chapter-9 sentences with zero code-level signal.
Mitigations, in order of strength: sentence-level diff of export text vs PDF
text layer where one exists; where it doesn't, treat every "the export reads
shorter than the figure" reviewer impression as an anomaly to check, and
package such findings as ONE chapter-level re-export request upstream (see
§7 RD-1 packaging), because per-sentence patches leave the next omission
undetected. Export omissions of struck-through source text are correct
behaviour, not defects — verify strikethrough before filing.

---

## 4. DECISIONS.md contract (Phase 1 output, Phase 2 gate)

- Template: `docs/fw036/templates/DECISIONS.md`
- Every entry is `[AUTO]`, `[PROPOSED: value — rationale]`, or `[PEI]`
- Phase 2 = Pei edits disagreements in place, fills `[PEI]` items, signs
  the sign-off block. **An unsigned DECISIONS.md blocks Phase 4+.**
- A `[PROPOSED]` left untouched at sign-off becomes binding as proposed —
  this is the mechanism that reduces questions without removing control.

---

## 5. Standing gates (all features, all states)

- Lint is a hard gate; the vocabulary/whitelist parts read from
  `feature.yaml` + profile
- Write-back invariants (traceability / completeness / done-region hash)
  abort rather than warn; weakening an invariant is a Tier 2 decision
- Every leaf gets a row: TC rows, or BLOCKED placeholder rows with Remarks
  (completeness invariant, both directions)
- One project = one `docs/fw036/framework.md`; features are Parts
- Profiles live in `docs/runtime/profiles/FW036_R1L_<Feature>_Profile.md`
- Feature directories live under `features/`, one per feature, named
  lowercase without an HMI suffix (`features/amfm`, `features/home`,
  `features/sxm`, `features/media`; reorganised 2026-08-11 — they used to
  sit at repo root as `AMFM/`, `HomeHMI/`, …). Self-contained, mirroring
  `features/media/` layout; scaffold via `scripts/new_feature.py`
- Entry point per feature: `features/<name>/PLAYBOOK.md` §6 status board
- **Script sharing model (ruled at Home close-out, 2026-08-09): copy + yaml,
  no shared library extraction.** feature.yaml + the loader already absorb
  the constant-level differences; the residual per-feature differences
  (segmentation strategy, external-table extraction, lint rulings like
  Home's A-H10) are genuinely divergent and would become conditional-branch
  sprawl inside a shared package. Revisit only if three features accumulate
  identical UNRULED logic — constants don't count.

---

## 5a. 數字紀律 (all features, all phases)

> **條號索引**（2026-08-12 補）：第 1~10 條原以散文與 bullet 形式書寫、未編號，
> 而全案有數十處「canon §5a 第 N 條」之引用指向它們。此索引不改寫原文，只把既有
> 的對應關係寫明，使引用可解析。第 11~14 條本即為編號條列。
>
> | 條 | 內容 | 形式 |
> |---|---|---|
> | 1 | 列號須標明實體列號或 tc_id 尾碼 | 下方 bullet 1 |
> | 2 | **計數須標明逐列或逐引用** | 下方 bullet 2 |
> | 3 | 門檻須標明絕對量或比例 | 下方 bullet 3 |
> | 4 | **掃描範圍須標明涵蓋哪些欄位** | 下方 bullet 4 |
> | 5 | **文字比對須標明大小寫與詞界** | 下方 bullet 5 |
> | 6 | 字串比對缺陷具傳染性 | 粗體段 |
> | 7 | 詞彙型 gate 具兩種必然缺陷 | 粗體段 |
> | 8 | 樣本大小依賴規則措辭時不得自我校準 | 粗體段 |
> | 9 | **單一來源之涵蓋範圍不等同其類別** | 粗體段 |
> | 10 | 累計數字每輪須自總量重算 | 粗體段 |
> | 11 | 檢查項須確認其在該階段確實可能失敗 | 編號條列 |
> | 12 | 抽取式之缺陷不會報錯 | 編號條列 |
> | 13 | 量出來的數字不一定能當規則 | 編號條列 |
> | 14 | 檢查條件要自我完備 | 編號條列 |
> | 15 | **不以自身輸出為來源** | 編號條列 |
> | 16 | **接受更正亦須查證** | 編號條列 |
> | 17 | **立新規則前須查既有政策** | 編號條列 |
>
> 引用最密集者為第 9 條（五次：mapping 列舉截斷、PROXI 單車型、DBC 不含 VF176、
> 同名分頁非值域權威、自產索引僅收曾被引用者）。

**凡涉及數字的裁決或判準，須同時寫明「量什麼」與「以什麼為單位」。**

- **列號**須標明係**實體列號**或 **tc_id 尾碼**
- **計數**須標明係**逐列**或**逐引用**
- **門檻**須標明係**絕對量**或**比例**
- **掃描範圍**須標明涵蓋哪些欄位
- **文字比對**須標明**是否區分大小寫**與**是否使用詞界**

**字串比對缺陷具傳染性。** 修正任一以字串比對實作之 gate 時，須同時檢查
所有同類 gate 是否具相同缺陷。

> 實例：L-PJ6 之 `a while` 誤判 `content area while`（A-PJ18）與 L-PJ5 之
> `inspect` 誤判 `Car Inspector`（A-PJ38），為**同一缺陷、相隔三輪各自
> 發現**。

**詞彙型 gate 具兩種必然缺陷。** 假陽性源自**詞界不足**，假陰性源自
**詞彙不全**。兩者皆不可能一次寫全，須以**增補機制**而非一次性設計處理。

> 實例：A-PJ18（`a while` 誤判 `content area while`）、A-PJ38（`inspect`
> 誤判 `Car Inspector`）為假陽性；A-PJ44（L-PJ9 漏 `trace tool` /
> `capture tool` / `simulator`）為假陰性。

**樣本大小依賴規則措辭時，不得以該樣本校準該規則。** 須以獨立錨點界定樣本，
或延後至樣本由其他來源到齊。用規則自身的措辭圈出樣本、再拿那個樣本校準規則，
是循環論證。

> 實例：L-PJ11 之三種錨定寫法給出 **5／19／16** 三種樣本量
> （A-PJ41／R-P44）——三個數字都不是錯的，它們量的是三件不同的事。

**跨輪次傳遞之累計數字，每輪須自總量重算，不得沿用前輪差值。**
**累計錯誤不會自行暴露，只會持續傳遞。**

> 實例（A-PJ51）：`剩餘列數 173` 於 B9→B10′ 連續三輪傳遞，實際 195，
> 差額為單一批次被重複扣除。分析層與執行層雙方均未察，因雙方皆沿用前輪
> 結論而非自總數重算。

**引用任何單一來源作為「權威」之前，先確認它的涵蓋範圍是否等同於它的類別。**

> 實例（同一裁決 R-P20 的兩次修正）：
> `Logical Identifiers and CAN Mapping` 的列舉截斷於 `101 = WL`，被誤當作
> 完整值域（R-P8′）；`PROXI_HDCC27_R3` 的 Header 為 `HDCC27 - Draft`，
> 是單車型配置檔，被誤當作全車系配置字典（R-P47）。
>
> 兩次的共同形態：**手上唯一的那份 ≠ 該類文件的全部。**
> 同風險形態亦見於 AMFM 的 `CIP_Radio_Tables`、SXM 的 `CFTS024`。

**單位未言明時，數字自洽不構成正確的證據。** 兩個不同單位的數字可能恰好
相同，使誤用在表面上完全自洽而不露破綻。

### 三個實例（Projection，2026-08-12）

| 案例 | 未言明的單位 | 後果 |
|---|---|---|
| A-PJ19 | 列號慣例：實體列號 vs tc_id 尾碼 | 一份三列清單，兩種讀法各對一半，無法執行 |
| A-PJ27 | 計數單位：逐列 vs 逐引用行 | 「HUIG 75」被當成列數；巧合在於 HUIG 的行計數 75 恰等於兩個 Test Set 的列數和 50+25，誤用完全自洽 |
| A-PJ30 | 門檻單位：絕對列數 vs 百分比 | 裁決理由寫百分比、實際依據是列數；後人照理由套用會在小樣本上誤判定案 |
| A-PJ37 | 大小寫：`\bCAN\b` 加 `re.I` 命中英文助動詞 `can`；於 `TI+PRE+PROC+ER` 範圍下 `HMI Display` 之 CAN 計數由 0 虛增為 17、`Knob` 由 0 虛增為 20 |
| A-PJ38 | 詞界：`inspect` 子字串命中專有名詞 `Car Inspector`，使 L-PJ5 全簿計數由 5 虛增為 7 |
| A-PJ18 | 詞界：子字串比對將 `content area while` 誤判為 `a while` |
| A-PJ36 | 掃描範圍：涵蓋哪些欄位 | 同一指標在不同欄位範圍下數值不同，兩者皆為真而互不相符。L-PJ6 裁定範圍為 Procedure + Expected Result，實測 0；若含 Test Item 則為 2 |

A-PJ27 是本紀律存在的理由最清楚的一例：**沒有任何跡象顯示數字被誤用**，
兩種單位下 75 都成立，錯誤直到重新逐列實測才浮現。

---

11. **檢查項須確認其在該階段確實可能失敗。** 不可能失敗的檢查項應標「未實測」，
    不得標 PASS —— 那是同義反覆而非證據。dry-run 未開寫入時，「寫回後雜湊不變」
    必然成立；它驗證的是「我沒寫」，不是「我寫對了」。判斷方式：問這一項在
    本階段**有沒有一條路徑會讓它 FAIL**，答不出來就是同義反覆（A-PJ56）。
    推論：靜態讀取驗不到只在寫入時才成立的性質 —— 公式是否保全、資料驗證
    範圍是否涵蓋新列、值域由誰強制，**都必須以複本實測**（A-PJ57 ~ A-PJ60，
    四條全部只在複本寫入後才浮現）。

12. **抽取式之缺陷不會報錯。** 自來源文件抽取錨點、id 或結構時，少抽表現為
    「該項不存在」，多抽表現為「多出無意義的項」，兩者皆不觸發例外。因此：
    (1) 抽取式須以**已知全集**驗證（如 docx 全文 id 數 vs 索引數）；
    (2) **自由文字中的數字預設不是錨點**，寧可標「未解析」也不猜；
    (3) 抽取結果之總數須與來源之獨立計數比對，不得僅檢查抽取過程無例外。
    實例（A-PJ65）：Addendum 抽取式改三次——`R10` 被當章節號、`Table 18-11` /
    `line 845` / `800 x 480` 被當章節號、`Addendum` 子字串命中 MFi 另一份文件。
    **三次皆未報錯。** 對照第十一條：那條說的是檢查項可能不會失敗，這條說的是
    抽取式失敗了也不會說。

13. **量出來的數字不一定能當規則。** 自既有資料推導之統計範圍（長度分布、值域
    分布、比例門檻）其地位為**代理判準**，用以近似實質判準而非取代之。
    **實質判準通過而代理判準不通過時，以實質判準為準**，並依實測擴充代理判準之
    範圍；**不得為滿足代理判準而更動內容**——那是讓觀測值反過來改寫被觀測物。
    辨識方式：問這個判準是「規則說的」還是「我量出來的」。母體導出之區間，其
    下限就是現有最短者，任何更短的新樣本都會 FAIL，即使它完全正確（A-PJ68：
    `Test Item` 長度 11–143 字，兩列 BLOCKED 佔位因來源敘述本身即短而越界，
    加長即編造）。對照第十二條：那條說抽取式會安靜地錯，這條說量測值會安靜地
    變成規則。

14. **檢查條件要自我完備。** 通過條件應寫成「**與參照對象在所有可讀屬性上一致**」，
    而非「**已知的幾項正確**」。前者涵蓋尚未想到的屬性，後者只涵蓋已想到的；
    後者每發現一項遺漏就要修訂一次條件文字，前者不用。
    **判別法：若某檢查項在發現新遺漏時需要修訂其條件文字，該條件即非自我完備。**
    實例（W-9）：「補列與參照列 r561 在所有可讀屬性上一致，除內容欄與 `No.#`
    公式外」——涵蓋 font 7 項、fill 2 項、border 5 項、alignment 6 項、
    protection 2 項、number_format、quotePrefix、列高／隱藏／outline、篩選 ref，
    共 252 格逐屬性。
    反例（W-6）：「資料驗證範圍延伸至 r568」只涵蓋當時已發現的那一項；框線、
    對齊、篩選範圍三項因無人發現而無人寫，成為 A-PJ69。

15. **不以自身輸出為來源。** 陳述任何事實、數字或狀態時，來源須為 repo 之現行
    記載或當下之實測，**不得為自己先前輪次之輸出**。自身輸出可能已被更正，而
    更正不會回頭改寫先前的輸出——引用它等同引用一個已知錯誤的副本。
    實例：A-PJ51（剩餘列數 173 沿用三輪）、A-PJ73（repo 狀態描述過期）、
    037 description 127/171 已於 Phase 0 更正為 105/171 而 close-out 又寫回 127。

16. **接受更正亦須查證。** 收到對自身陳述之更正時，**查證義務與提出陳述時相同**。
    未查證即接受更正，與未查證即主張，同為本節之違反——**認錯不是免除查證的理由，
    而讓步比主張更容易被誤認為謹慎。**
    實例（A-PJ74）：一方以錯誤之實測值更正另一方之正確數字，對方未查證即接受，
    致正確記載被改為錯誤記載。
    **推論**：若一方之更正被無條件接受，則該方之錯誤將直接寫入記錄且無人攔截。
    **雙向查證是雙層檢驗（canon §7.3）在事實陳述上的對應物。**
    自查提示：若某個結論在物理上高度不可能（如大幅增刪內容後檔案大小不變），
    該結論本身即應觸發自我懷疑，而不是等對方指出。

17. **立新規則前須查既有政策。** 提出任何新規則、新慣例或新檔案配置前，須先查證
    該領域是否已有明文政策。**既有政策優先於新提案**，除非新提案能指出既有政策之
    明文理由已不成立。政策之存在往往記於註解、`.gitignore`、或 canon 之非顯著
    段落——**未看見不等於不存在**。
    實例（A-PJ75）：R-P93 提出「旁檔須入庫」，而 `.gitignore:20` 上方三行註解已
    明文禁止，且 canon §6 已指定 tag annotation 為 digest 之唯一位置。該包並援引
    AMFM 前例為據，卻未查該前例之追蹤狀態——實測為 untracked，恰恰支持相反結論。
    **檔案存在 ≠ 檔案被追蹤。**

## 6. Write-back → tag sequence (Phase 6→7 boundary, validated: Home)

Order: **dry-run reviewed → commit → --write → tag**, under two guards:

1. The working tree is CLEAN when `--write` runs — the output workbook is
   then derived from exactly one commit, and anyone can re-derive it by
   checking out that commit and re-running.
2. `--write` touches NO tracked file. Output workbook + `.sha256` sidecar go
   to a gitignored `output/`; the digest goes into the **tag annotation**,
   never a tracked file (a tracked digest would force a second commit and
   detach the tag from the producing state).

Tag: `fw036-<feature>-regen-v<N>`, annotation carrying the output filename,
its SHA256, the done-region content hash, the row summary
(`<done> preserved / <regen> regen (<n> placeholder) / <total> rows`), and
the lint result. The workbook is normalized (zip timestamps, dcterms dates)
before hashing so the digest is reproducible.

**Dry-run review checklist** (the reviewer verifies, the summary must
therefore state): per-segment before→after row counts with the arithmetic
reconciling to the total sheet delta; done-region hash unchanged and row
count unchanged; segment ORDER unchanged; regen req_id set == the target
leaf set exactly; placeholder rows listed; downstream segment shifts
consistent with insertions; blank-by-convention columns named. A summary
missing any of these is returned, not approved.

---

## 7. RD-1 packaging (Phase 7)

One document per feature delivery, ordered by leverage:

1. **Systemic defects first**, stated as a class with a class-level remedy
   (e.g. "re-export chapter 9 and diff against the PDF" — not three
   sentence patches). One omission found by accident implies undetected
   siblings; the request must close the class.
2. Requirement-set corrections (missing rows, misfiled ids, wrong
   descriptions), each citing its anomaly id and the evidence.
3. Wording/label confirmations and residual-risk items (version-label
   equivalences, which-string-ships questions). State explicitly what
   changes if the answer goes the other way — most are spec_reference-only.
4. FYI notes (numbering gaps, inherited constants) — explicitly marked as
   requiring no action.

Every item carries: anomaly id, one-line evidence, the disposition already
taken locally, and the requested upstream action. The feature does not wait
on answers — dispositions are designed so a contrary answer changes strings,
not content.

---

## 8. 下放包與上繳包契約

### 8.0 為什麼需要契約

分析層（Claude Desktop）與執行層（Claude Code）不共享對話。執行層是每次重新
開始的實例，**看不到任何聊天脈絡**。下放包是唯一的輸入，上繳包是唯一的輸出。

兩者若無固定形式，會出現三種失效：

1. **裁決未落檔即被引用** —— 條文停留在對話裡，執行層無正文可依（A-PJ28）
2. **量測條件未言明** —— 雙方數字不符卻無法歸因於誰對誰錯（§5a）
3. **檢查器自身故障無人察覺** —— gate 檢查簿子，但沒有東西檢查 gate（A-PJ48）

契約要解決的是這三件。

### 8.1 下放包的必要成分

下放包必須自帶完整脈絡。**假設讀者對本專案一無所知，且無法提問。**

| 成分 | 內容 | 缺了會怎樣 |
|---|---|---|
| 禁區 | 明列不得執行之操作，git 一律列入 | 執行層越權而不自知 |
| 背景 | 本 feature 與本批之定位，一段即可 | 執行層無法判斷邊界情形 |
| 裁決逐字 | 適用之裁決全文照錄，**不得摘要、不得以編號代替** | 執行層依編號猜內容 |
| 作業清單 | 逐項或逐列指示，含依據之裁決編號 | 執行層自行決定範圍 |
| 預期數字 | 本批各項指標之預估值 | 見 §8.3 |
| 掃描條件 | 欄位範圍、是否區分大小寫、是否用詞界 | 數字不符無法歸因 |
| 上繳要求 | 明列上繳包須含哪幾項 | 覆核時缺料 |
| 升級條件 | 何種情形須停下升級至 chat 覆核 | 該停的沒停，或不該停的停了 |

**裁決逐字的理由**：編號在執行層眼中只是字串。`R-P8′` 三個字元不帶任何資訊，
執行層只能照字面猜，猜錯就是無授權變更。

### 8.2 上繳包的必要成分

| 成分 | 內容 |
|---|---|
| 預期數字對照 | 逐項列出預期 vs 實測，**相符者亦須列出** |
| 不符項目 | 逐項說明，**不自行調和** |
| 結果分類 | 依 §8.4 三分法 |
| 逐列 diff | 有變更者，可編輯欄分開呈現 |
| lint 全跑 + 基線重現 | 見 §8.3 |
| 新開 anomaly 與 DR | 成對，缺一不可 |
| 未預期之發現 | 下放包未涵蓋而執行時撞到者 |
| 掃描條件揭露 | 本批實際使用之欄位範圍與比對方式 |
| 獨立判斷 | 「本包是否仍有該驗而未驗者」 |

**不自行調和**是上繳包最重要的一條。數字不符時，執行層的職責是**回報並停下**，
不是把數字改成一致。

### 8.3 三層檢驗

契約的核心結構，缺任一層即失效：

```
第一層  gate            檢查簿子          lint
第二層  預期數字         檢查檢查器        下放包 §預期數字 ↔ 上繳包對照
第三層  全簿基線         檢查預期數字      lint_defs.BASELINE
```

**第二層的存在理由**：若 gate 自身故障，第一層會全綠而毫無異狀。A-PJ48 即為
此例——批次腳本重寫比對式時漏失 `re.I`，禁用動詞因出現在句首必為大寫而全數
落空，lint 全綠。攔下它的不是任何 gate，是下放包預期「禁詞 2」而實測 0。

**第三層的存在理由**：若有人修改 gate 的比對式，全簿基線會立即有一項對不上。
這是第二層在單批範圍內看不見的。

### 8.4 結果三分法

執行層對每一列的結論只有三種，**三者價值相同**：

| 分類 | 意義 |
|---|---|
| 改對了 | 依裁決修正 |
| 核實無誤 | 對照來源確認現況正確，不需改 |
| 正確地不動 | 依規則（無依據、凍結、缺件）維持不動 |

「核實無誤」不是「沒看」，須附理由；**不得以「無 gate 命中」作為理由**。
「正確地不動」不是失敗，須指得出裁決或 DR 編號。

此三分法在 `FULL_REFINE` 型 feature 尤其關鍵：**「依規則正確地不動」與「漏做」
在 diff 上長得一樣**，只能靠分類清單區分。

### 8.5 執行層的三不

1. **不代擬條文** —— 發現引用之裁決無正文時，回報而不自行補寫
2. **不自行調和** —— 數字或事實不符時停下回報
3. **不越權補件** —— 素材補入須經授權；縱使結果良性，超出點名範圍仍須先問

### 8.6 分析層的三不

1. **不散文化裁決** —— 條文須以可直接貼入之區塊產出，不得夾在敘述中
2. **不憑記憶給事實** —— 文件名、章節、節號、數值一律先查再寫
3. **不沿用前輪數字** —— 累計量每輪自總量重算（§5a）

### 8.7 落檔與封存

- 下放包 `features/<feature>/docs/handoff/NN_<slug>.md`（分析層寫）
- 上繳包 `features/<feature>/docs/upstream/NN_<slug>.md`（執行層寫）
- 一次往返共用同一 `NN`
- 索引 `features/<feature>/docs/INDEX.md`（執行層於每次上繳時更新）
- 報告 `features/<feature>/docs/reports/`

**分析層產出之任何供落檔文件，一律 `write_file` 寫入 repo**，聊天附件僅為
副本（A-PJ62、A-PJ78）。

### 8.8 節奏

- **一批一上繳**，前批未覆核不得開下批
- 升級 chat 覆核之條件由下放包明列
- **git 一律不在執行層** —— 所有下放包禁區之首條

---

## 9. 通則 —— 自 feature 條文升格者（2026-08-17，User Profiles 01–09 輪）

**升格之單位為「原則」，不是「條文」。** 來源條文多半同時含通則與該 feature
之事實（檔名、列數、異常編號）；升上來的只有前者。**來源條文於其 feature 之
`RULINGS.md` 全部保留**，各加註其升格去向 —— 刪掉就看不出它從哪裡來。

### 9.1 十一項通則

| # | 通則 | 來源 |
|---|---|---|
| 1 | **引用集合與生成集合是兩個分母**，須分立並各自具名；引用任一數時載明是哪一個，**不得互推** | R-U19（user_profiles）|
| 2 | **037 之 `Sub Categorization` 欄不作阻斷判準。** 阻斷之判準為「於本 feature 全部 spec 內**無任何介面可觀察端**」—— 需來回一趟才看得到，不等於看不到 | R-U21 |
| 3 | **spec 基線得有兩面**（結構面／內文面）。採雙面者須**指定何者為判讀基準**，另一面標「追溯用」；且**須載明該分工之已知例外** | R-U25 ＋ R-U35(a) ＋ R-U38 |
| 4 | **BLANK 之 style authority 不得取本管線自身之產出**（§5a 之延伸：不以自身先前輸出為來源）| R-U6（其原則部分）|
| 5 | **聊天附件之副本不等於 repo 檔。** 數字須在**有雜湊之物件**上重測；「大小相同」不是「內容相同」。以附件量得之數字為「被取代」而非「被複驗」 | R-U16 ＋ R-U18 |
| 6 | **判「不可讀」前須先驗抽取能力，且須跨素材形式試過**（xlsx／PDF／內嵌圖／向量文字層）。「抽不出來」與「沒去抽那一份」是兩件事 | R-U23 |
| 7 | **已知會誤切之來源，不得整份取代已知會少句之來源 —— 增欄，不取代。** 以一種錯法換另一種錯法不是修好 | R-U31 |
| 8 | **缺陷之解除條件須為機器檢查且實跑。** 文字修補（警示、註解、範例改寫）不構成 RESOLVED | R-U14 |
| 9 | **保住檔案與保住雜湊是兩件事。** 歸檔之檔案須有可執行之 `shasum -c`，且該雜湊檔本身須入版控 | R-U12 |
| 10 | **裁決條文須以可測判準表述，不以具名個案代替。** 以個案之名字寫成的條文，其適用範圍會被讀成該個案 | **R-U39(2)** |
| 11 | **一條裁決只管一件事。** 包了數件者，日後只能整條取代或整條保留 —— 兩者皆失真（見 §9.3）| 執行層 09 輪回報 |

> **第 10 項為本次收斂中最貴的一條。** `R-U22` 原文寫「`PROF-001-01`（PLP 表）
> 之處置」，於是「哪些 leaf 得引 `3.x`」被讀成「只有那一個 leaf」；
> R-U39(2) 改為可測判準（掃 180 leaf 之 `pdf_text` 找 `PLP` 字樣）後，
> 答案可能不只一條。**代價是一整輪的往返。**

### 9.2 全域條文 R-G1～R-G12（集中，feature 側改為引用）

| 條 | 一句話 |
|---|---|
| R-G1 | 036 母本自 2026-08-17 起固定，不再逐 feature 詢問（見 §0 Tier 0）|
| R-G2 | `forms/` 舊檔以 `mv` 歸檔，**不刪除**；移動前後各記 `shasum` |
| R-G3 | `framework.md` §Workbook sync 之範例禁用 `openpyxl` + `wb.save()`，改 `xlsx_surgical` splice |
| **R-G4-1** | `recon.py` 之 leaf→section 產物寫 `recon_leaf_to_section.tsv`；不得無聲覆寫既存 tracked 檔。**其讀者為三個**（`lint_tcs.py`／`make_batch_context.py`／`extract_exemplars.py`）|
| R-G5 | **全部 git 操作屬 Pei**，含還原、回退、`checkout`／`restore`／`stash`／`clean`。遇覆寫事故：**兩版並存、上報、停手**，不自行還原 |
| R-G6 | 上繳包之記載一致性：「未執行 git」須與全文動作清單逐項對得起來；**唯讀與改狀態之 git 分列** |
| **R-G7-1** | 反向驗證須含「什麼都沒做」之對照向；對照向**亦用於驗證定位／抽取機制本身**，未全綠者須逐項追因，不得以「多數命中」通過 |
| R-G8 | **任何比率須同時載明其分子定義。** 缺判準之比率不予採認，等同未量測 |
| R-G9 | **lint 規則之驗證須含範圍向** —— 對不該轉紅之近似案例證明其不轉紅。只證明會 FAIL 之規則，可能是對所有東西都 FAIL 之規則 |
| R-G10 | **清單式分類須以餘數驗證** —— 另以「全集減已分類」求餘數並驗其為空；不得以逐項檢視代替。逐號列舉之缺漏，其形狀正是「相鄰兩號皆在清單內而它不在」|
| R-G11 | **可測判準須同時聲明其盲區**，並指定盲區之處置路徑（人工判讀／另立判準／接受漏失）。**未聲明盲區之判準，其「命中數」不得被當作「全集」** |
| **R-G12** | **`git commit` 一律帶 pathspec**：`git commit -- <pathspec>`，不得使用不帶 pathspec 之 `git commit`（它提交整個 index，而 index 可能已含另一 session 置入之檔案）。`git add` 亦同：一律帶明確路徑，不用 `git add .`／`-A`。**執行層仍只準備不執行（R-G5）** |

`R-G4`／`R-G7` 之原文保留於 feature 側並標 `[SUPERSEDED by …]`，
**升上來的是修訂後之版本**（R-G4-1／R-G7-1）。

**R-G12 之來源**（2026-08-18，Pei 裁定升格）：`052f67d` 與
`645e55f → cc04aa1` 為**同一成因之兩次發生** —— 一個 session 的
`git commit` 不帶 pathspec，把另一個 session 已放進 index 的檔案一併提交。
**兩次皆非疏忽，是該作法本身會產生此結果。**
`052f67d` 已依 R-U55 採「留著不動歷史」，其代價（log 歸屬不準）
記於 User Profiles 之 `ANOMALIES.md` A-UP10，狀態為 **ACCEPTED 而非 RESOLVED**。
**各 feature 之 `RULINGS.md` 不因本條被寫入** —— 本段即其唯一落點，
他 feature 於下次開輪次時依 R-U44 自檢即可。

### 9.3 一條裁決只管一件事 —— 本次收斂所揭之代價

收斂時發現三條**只有一部分被取代**，而條文之粒度使它無法只取代那一部分：

| 條 | 被取代之部分 | **仍生效之部分** |
|---|---|---|
| R-U3 | 「證據＝內文完整」之解讀 | spec 基線之檔名、`spec_mode` |
| R-U15 | 阻斷範圍 | 「不得以鄰近 id 推定內容」等三項判讀 |
| R-U22 | 引用範圍之限縮 | 「先驗可讀性」「037 沒引用不等於 spec 沒寫」 |

**故第 11 項通則**：立條時一條只管一件事；已成之條文若須部分取代，
以 `[SUPERSEDED by X — <哪一項>]` 標明範圍，不以整條標記代替。

---

## 9. 全域慣例（FW036 User Profiles 之升格，53 輪 close-out）

**本節為 canon 同步之結果**（Operating Charter 之義務）。
下列條文與常規產於 User Profiles（FW036），**其判準已於該 feature 之
189 條語料與 18 支閘上實跑驗證**，現升為全域。

**feature 側之 `RULINGS.md` 與 profile 保留原文**（其量測條件與成因記在那裡）；
**本節為引用之權威來源**，新 feature 讀本節即可，不必回頭翻 feature 檔。

### 9.1 R-G1 ～ R-G12（全域裁決條文）

| 條 | 一句話 | 來源 |
|---|---|---|
| R-G1 | 036 母本之單一來源與其身分（SHA，非檔名）| user_profiles 02 輪 |
| R-G2 | `forms/` 舊檔以 `mv` 歸檔，**不刪除** | 02 輪 |
| R-G3 | `framework.md` §Workbook sync 之範例不得用 `openpyxl.save()` | 02 輪，A-UP09 |
| R-G4／R-G4-1 | 衍生檔之檔名歸屬；**不得無聲覆寫** | 05 輪（部分取代）|
| R-G5 | **執行層不執行寫入性 git** | 全輪次 |
| R-G6 | 上繳包之記載一致性（同一份文件內之數字須自洽）| —— |
| R-G7／R-G7-1 | **反向驗證之對照組**：閘須證明它會轉紅 | 多輪 |
| R-G8 | 比率之判準揭示（分子分母各是什麼）| —— |
| R-G9 | lint 規則之驗證須含**範圍向**（不得對正當輸入轉紅）| —— |
| R-G10 | 清單式分類須以**餘數**驗證 | —— |
| R-G11 | **可測判準須同時聲明其盲區** | 多輪 |
| R-G12 | **git commit 一律帶 pathspec** | 37 輪 |

### 9.2 G-A ～ G-K ＋ G-N（全域常規；G-L／G-M 見 §9.3）

| # | 常規 | 成因（其代價之實例）|
|---|---|---|
| **G-A** | 同一條待判連續三輪判為「不成立」者，須改判準或除役 | PU0588 之兩處誤報活了六輪 —— **紅的會被修，綠的沒人看，待判的每輪被抄一次** |
| **G-B** | 枚舉型判準一律接對照（清單須與其母體重算比對）| `STATE_VALUES`／`UI_LOCATORS` 為寫死清單而無人驗 |
| **G-C** | `feature.yaml` 之「宣告」與「生效」須分得開（`{value, applied, why}`）| yaml 宣告了交付件並不帶的值，**兩個 feature 皆然** |
| **G-D** | 掃描報表須列**被抑制之條數** | **一個永遠空的清單與一個壞掉的清單，輸出相同** |
| **G-E** | 可測範圍到底之後，品質由**人讀**承擔，不得因閘全綠而縮減 | 30–41 輪每輪有缺陷；42 輪三支新程式一條 TC 都沒動 |
| **G-F** | **任何靜態轉錄**（review pack、查詢單、出處對照、交付說明）一律加指紋 | 時效性不是「檢查」之性質，是任何靜態轉錄之性質 |
| **G-G** | `--verify` 之結果由**產出方**於上繳時附上 | 不依賴另一層記得做一件事；**建立當輪即抓到真陽性** |
| **G-H** | 遇「無先例」之判斷，先查他 feature 之**交付件**（不是其 yaml），**且須先確認母本同一** | T:Z 被送成裁示題，而答案在 Comfort 已交付的檔案裡，查的成本三十秒 |
| **G-I** | 凡判準含 `\b` 而其詞表有非 ASCII 者，改以 `(?<![\u4e00-\u9fff])`／字串包含，**並附中文命中之方向性案例** | `\b` 是 ASCII 詞界，`待判`／`未決` 永遠比不到 |
| **G-J** | 修正**成批落地**，不逐條處理 | 「重寫回 0.04 秒」只涵蓋機器；一次淨化連帶三份 pack 重出與三次重判 |
| **G-K** | 凡「全面查核」之回報，須附「**本查核對已知案例會轉紅**」之實測 | 48 輪之 grep 抓不到它自己要找的 bug；結論對而證據無效 |
| **G-N** | **自我測試不得以當前語料為案例。** 缺陷之原文須**以字面釘入測試**，另加一組「**修正後不得再命中**」之回歸 | 56 輪：`audit_second_segment` 之 G-K 段讀語料取三條，31 條一改寫即由 `10/10` 掉到 `7/10` —— **不是判準退化，是證明消失**，而兩者在分數上長得一樣 |

### 9.3 兩項素材與資料之判準（53 輪 close-out）

| # | 判準 | 成因 |
|---|---|---|
| **G-L** | **沒有路徑的「到齊」不算到齊。** 素材清單每項須附其**檔案系統路徑與 SHA**；「到齊」定義為 `shasum -c` 對得上 | 52 輪：Pop Up List 記「待驗」而它在 repo 裡三份；Tutorials 記「到齊」而它不在 |
| **G-M** | 「先查他 feature」之範圍**含其 `inputs/`**，不只交付件 | `TC-169` 寫「逐步對映不在我方輸入內」，**而那份輸入在 `features/comfort/inputs/`，卡了五十輪** |

### 9.4 缺口 —— **本次未做，具名留給下一個 feature**

`data/*.tsv` 與 `outline_map.json` 目前只有 `BASELINE.sha256` 保護其**位元組**，
**沒有東西保護「它與 PDF 現況一致」**。
而 `TC-017`／`074` 之正確性正來自 07 輪之補句表（`xlsx_missing_clauses.tsv`）。

**應有而未有**：一支「以 PDF 現況重算補句表並與檔案比對」之閘。
其困難在於補句表是**人工判讀之產物**（07 輪之逐節稽核），不是可重算之衍生物 ——
**故它不是「加一支閘」，是「為人工判讀之產物設計一種可驗形式」。**

### 9.5 欄位接合矩陣（58 輪，User Profiles 之升格）

**這一節是流程資產，不是 User Profiles 之事實** —— 故置於 canon 而非 profile。

> **欄位之間的接合要一組一組地查。查過兩組不代表查過全部，
> 而缺陷偏好長在沒有人看的那幾組。**

TC 有九個內容欄，兩兩之接合關係數十組。
**User Profiles 五十八輪中，缺陷有一半以上出在接合，而非單欄內容。**
單欄之閘查得到**形態**（欄位存在、合法、措辭合規），查不到**用途**；
用途只在欄位之間看得出來。

#### 9.5.1 已查 14 組（附其閘與首次發現輪次）

| 組 | 閘／發現 | 首次發現於 |
|---|---|---|
| `procedure` → `ER`（ER 引用之基準線是否存在）| T-1 | 30 輪 |
| `procedure` → `ER`（反向：步驟記錄而 ER 未用）| U-2 | 31 輪 |
| `pre_conditions` → `ER`（前提是否蘊含被測結果）| W-1 | 33 輪 |
| `procedure` → 條文時序（動作是否落在條文之時點）| V-1 | 32 輪 |
| `ER` → 條文分支（斷言是否綁得住所要之分支）| U-1 | 31 輪 |
| `input_test_data` → `procedure`／`pre`（值是否被使用）| IT-1 | 57 輪 |
| `input_test_data` 之欄位歸屬（§4.5）| IT-2 | 57 輪 |
| `remarks` → `specification_reference` | G20／K-4 | 25 輪 |
| `specification_reference` ↔ 字面值（雙向：多引／少引）| G17／G18 | 18／29 輪 |
| `test_item` 首段 ↔ 第二段（資訊量）| TI-2／AD-1 | 56 輪 |
| `design_method` ↔ `input_test_data`／`procedure` | K-4a | 21 輪 |
| `priority` ↔ 其理由文字 | K-4b | 21 輪 |
| 變體 `pre` ↔ 禁用字面值 | `lint_variant_labels` | 15 輪 |
| 委派句 ↔ 被指名之 leaf | D-1／Y-1 | 23／36 輪 |

**輪次欄要讀的是它的分布**：14 組裡有 3 組是**最後三輪**才發現的
（`input_test_data` 兩組、`test_item` 兩段一組）。
到第 55 輪為止，那三組上的缺陷一直存在且一直全綠 ——
**不是因為它們難，是因為沒有人問過那兩欄之間有沒有接上。**

#### 9.5.2 未查 9 組（附「若壞了會怎樣」與可測性）

| 組 | 若壞了會怎樣 | 可測性 |
|---|---|---|
| **`test_item` ↔ `ER`** | 標題說「X 顯示」而 ER 從未斷言 X —— **交付欄自相矛盾** | 高（實詞比對）|
| **`test_item` ↔ `procedure`** | 標題所述之觸發，步驟從未執行 | 高 |
| **`pre_conditions` → `procedure`**（孤兒前提）| 前提建立了一個沒有人用的狀態 | 高（同 IT-1 之形）|
| **`procedure` → `pre_conditions`**（反向：步驟需要而前提未建立）| 步驟第一句即無法執行 | 中（需語意）|
| **`design_method` ↔ `ER`** | 標「狀態轉換」而 ER 無 A→B 之斷言 | 中 |
| **`priority` ↔ `ER`** | 標 P0 而其 ER 不含核心斷言 | 低（語意）|
| **`remarks` ↔ `ER`** | remarks 稱「ER 某行不可省」而該行已被改掉 | 高（行號比對）|
| **`ER` ↔ `ER`** | 多行 ER 互相矛盾 | 低（語意）|
| **`specification_reference` ↔ `pre_conditions`** | 前提之字面值無出處（G18 已部分覆蓋引號值）| 中 |

**前三組可測性高且與已立之閘同型**（`pre_conditions` → `procedure` 之孤兒前提
與 IT-1 幾乎是同一支程式換一組欄位），成本各約一支閘。

#### 9.5.3 此表之身分：**已知未查，不是已查為綠**

User Profiles **不補做這九組**：語料已定稿、交付件已產出（ENTRY 005），
於該時點新增九支閘會觸發九輪重出，其代價高於其收益。

**但「不做」與「沒發現」必須在紙上分得開**（G-D 之精神）——
本表即該區分之載體。**新 feature 讀本表，不必重新發現「有這回事」；
而讀到「未查」時，讀到的是一個具名的空缺，不是一片沉默。**
