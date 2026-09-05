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
- **CFTS 嵌入物件之檢查（R-G67，Pei 2026-08-30，全域）**：intake 時須查
  `…/Reference Documents/CFTS Embedded Objects/CFTS<nnn>/` 有無該 feature
  之母 CFTS 目錄；有者逐張轉圖並出「由圖找列」二欄表，**查無者亦記明已查**。
  圖中可能載有未見於 docx 之數值與流程（sw_update 實測：四個門檻、
  一段 UDS 序列），而其 ObjectID **不在錨定語料內**，錨定三機制對其無效。
  條文與其成因見 FO §9.2 R-G67。
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
5. Fabrication pressure: any value the source does not state (IN §8.4)
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
| Style authority | fallback chain (FO §2.1) | done region | done region | done region |
| Write-back | append from first data row | positional freeze + rewrite tail | in-place segment rewrite + **content-hash** invariant | none |
| Done invariant | n/a | positional hash | ordered content hash | full hash |
| Draft rows | n/a | discard & regenerate (default) | discard & regenerate (default) | n/a |

### 2.1 BLANK fallback chain (style decisions when no done region exists)

`done region → nearest FW036 sibling feature done region (STYLE ONLY) →
docs.md generic rules`

Bindings under BLANK:

- Test Item = standard IN §4.3 tc_title (no precedent to defer to)
- Test Group / Test Set columns = **FILL** per framework Part N
  (TEST_SET_POLICY is itself the default when no precedent overrides it)
- spec_reference = constructed from spec_mode template (IN §10.7)
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
FO §7 RD-1 packaging), because per-sentence patches leave the next omission
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
> 而全案有數十處以「canon」加裸節號指向它們之引用（依 R-G57，今應書
> `FO §5a 第 N 條`；歷史檔之既有寫法不追改）。此索引不改寫原文，只把既有
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
    **雙向查證是三層檢驗（FO §8.3）在事實陳述上的對應物。**
    自查提示：若某個結論在物理上高度不可能（如大幅增刪內容後檔案大小不變），
    該結論本身即應觸發自我懷疑，而不是等對方指出。

17. **立新規則前須查既有政策。** 提出任何新規則、新慣例或新檔案配置前，須先查證
    該領域是否已有明文政策。**既有政策優先於新提案**，除非新提案能指出既有政策之
    明文理由已不成立。政策之存在往往記於註解、`.gitignore`、或 canon 之非顯著
    段落——**未看見不等於不存在**。
    實例（A-PJ75）：R-P93 提出「旁檔須入庫」，而 `.gitignore:20` 上方三行註解已
    明文禁止，且 FO §6 已指定 tag annotation 為 digest 之唯一位置。該包並援引
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
2. **量測條件未言明** —— 雙方數字不符卻無法歸因於誰對誰錯（FO §5a）
3. **檢查器自身故障無人察覺** —— gate 檢查簿子，但沒有東西檢查 gate（A-PJ48）

契約要解決的是這三件。

### 8.1 下放包的必要成分

下放包必須自帶完整脈絡。**假設讀者對本專案一無所知，且無法提問。**

| 成分 | 內容 | 缺了會怎樣 |
|---|---|---|
| 禁區 | 明列不得執行之操作，git 一律列入 | 執行層越權而不自知 |
| 背景 | 本 feature 與本批之定位，一段即可 | 執行層無法判斷邊界情形 |
| 裁決引用 | 依 **R-G52** 之引用制：`R-XX@<sha8>`，執行層自 repo 讀原文並回報所讀 sha8。得另附原文（附了不算錯）| 執行層依編號猜內容 |
| 作業清單 | 逐項或逐列指示，含依據之裁決編號 | 執行層自行決定範圍 |
| 預期數字 | 本批各項指標之預估值 | 見 FO §8.3 |
| 掃描條件 | 欄位範圍、是否區分大小寫、是否用詞界 | 數字不符無法歸因 |
| 上繳要求 | 明列上繳包須含哪幾項 | 覆核時缺料 |
| 升級條件 | 何種情形須停下升級至 chat 覆核 | 該停的沒停，或不該停的停了 |

**逐字照錄之原理由**：編號在執行層眼中只是字串。`R-P8′` 三個字元不帶任何資訊，
執行層只能照字面猜，猜錯就是無授權變更。

**[SUPERSEDED by R-G52 — 逐字照錄之要求部分]**（2026-08-24，23 包 §D）：
上述理由所要防之事仍在，但其手段由「全文照錄」改為「引用 + 指紋」——
`R-XX@<sha8>` 帶的是**可驗之身分**，不是待猜之字串；執行層讀 repo 原文，
sha 不符即停下（FO §8.4）。**原文段保留不刪**（R-TM13 之精神）。
逐字照錄之成本隨條文數線性膨脹，且抄寫本身即漂移源（23 包 §B-2）。

### 8.2 上繳包的必要成分

| 成分 | 內容 |
|---|---|
| 預期數字對照 | 逐項列出預期 vs 實測，**相符者亦須列出** |
| 不符項目 | 逐項說明，**不自行調和** |
| 結果分類 | 依 FO §8.4 三分法 |
| 逐列 diff | 有變更者，可編輯欄分開呈現 |
| lint 全跑 + 基線重現 | 見 FO §8.3 |
| 新開 anomaly 與 DR | 成對，缺一不可 |
| 未預期之發現 | 下放包未涵蓋而執行時撞到者 |
| 掃描條件揭露 | 本批實際使用之欄位範圍與比對方式 |
| 獨立判斷 | 「本包是否仍有該驗而未驗者」 |
| 四支 gate 之實跑輸出 | `scripts/gate_all.py` 之輸出，exit 0；非 0 者須附升級說明（26 包 §C 裁定 2，S3 啟用）|

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
3. **不沿用前輪數字** —— 累計量每輪自總量重算（FO §5a）
4. **不先改共用檔再說它該怎麼提交**（2026-08-30 增，sw_update 上繳 56 §7(丁)）——
   凡分析層直接編輯 canon 或任何共用檔者，**其下放包須與該編輯同時落檔**，
   且下放包首節須先寫「**本包已改了什麼**」。**「改了什麼」與「怎麼提交」
   要在同一個包裡，且早於任何 git 動作。**

> **第 4 項之來源**：`13a465f` 把 canon 變更與下放包落檔包成同一 commit，
> 而「canon 須單獨提交」之令寫在**那個尚未被讀的下放包裡** ——
> **改在前，令在後**，執行層當時無從得知。
> **其責在分析層，不在執行層之未讀**（判準見下）。
>
> **配套之限定**（同輪所裁）：「**無可依之指示**」指指示**不存在或不可得**，
> **不含「指示已在工作區而執行層未讀」** —— 後者仍為執行層之疏漏。
> 若寫成「未讀者即無責」，**它會獎勵不讀**。

### 8.7 落檔與封存

- 下放包 `features/<feature>/docs/handoff/NN_<slug>.md`（分析層寫）
- 上繳包 `features/<feature>/docs/upstream/NN_<slug>.md`（執行層寫）
- 一次往返共用同一 `NN`
- 索引 `features/<feature>/docs/INDEX.md`（執行層於每次上繳時更新）
- 報告 `features/<feature>/docs/reports/`

**分析層產出之任何供落檔文件，一律 `write_file` 寫入 repo**，聊天附件僅為
副本（A-PJ62、A-PJ78）。

### 8.8 節奏

- **一批一上繳**，前批未覆核不得開下批 —— **除 R-G53 綠色通道生效期間**（FO §9.2）
- 升級 chat 覆核之條件由下放包明列
- **git 一律不在執行層** —— 所有下放包禁區之首條

### 8.9 包規模與裁決引用（S5）

每包需 Pei 裁定之新規上限 3 條，超過即拆包。
包尾自檢表增列「本包引用之既有裁決編號清單」；引用未落檔編號
= 包退回。Tier 1 事項（純格式、可逆、單 feature）分析層以保守
預設先行，標 [DEFAULT] 記入 RULINGS_LEDGER 供 Pei 事後追認或
推翻；僅 Tier 2+ 阻塞等裁。

---

## 9. 全域條文與通則（整併落點）

**本節為兩個原 `## 9.` 之整併**（W-P1′，2026-08-24）。整併前 canon 有兩個
`## 9.`：「通則 —— 自 feature 條文升格者」（2026-08-17，User Profiles 01–09 輪）
與「全域慣例」（53 輪 close-out），且 §9.1／§9.2／§9.3 各有兩個落點 ——
以「canon」加裸 §9.1 之引用因而歧義。整併後**每一節號唯一**（R-G57）。
**被移動之內容一律逐字保存，其原節號之去向見 FO §9.8 之 [MOVED] 對映。**

**升格之單位為「原則」，不是「條文」。** 來源條文多半同時含通則與該 feature
之事實（檔名、列數、異常編號）；升上來的只有前者。**來源條文於其 feature 之
`RULINGS.md` 全部保留**，各加註其升格去向 —— 刪掉就看不出它從哪裡來。

**feature 側之 `RULINGS.md` 與 profile 保留原文**（其量測條件與成因記在那裡）；
**本節為引用之權威來源**，新 feature 讀本節即可，不必回頭翻 feature 檔。
下列條文與常規產於 User Profiles（FW036），**其判準已於該 feature 之
189 條語料與 18 支閘上實跑驗證**，現升為全域。

### 章節導覽

| 節 | 內容 | 整併前之落點 |
|---|---|---|
| 9.1 | 十一項通則 | 原第一個 §9 之 §9.1（不變）|
| 9.2 | 全域裁決條文 R-G1～R-G11、R-G51～R-G68、R-G42（2026-09-05 R-G43 改號前為「R-G1 ～ R-G27」）| 原第一個 §9 之 §9.2 **併** 第二個 §9 之 §9.1 |
| 9.3 | 一條裁決只管一件事 —— 收斂所揭之代價 | 原第一個 §9 之 §9.3（不變）|
| 9.4 | 缺口 —— 具名留給下一個 feature | 原第二個 §9 之 §9.4（不變）|
| 9.5 | 欄位接合矩陣 | 原第二個 §9 之 §9.5（不變，含 9.5.1～9.5.3）|
| 9.6 | 全域常規 G-A ～ G-N | **[MOVED]** 自原第二個 §9 之 §9.2 |
| 9.7 | 兩項素材與資料之判準 G-L／G-M | **[MOVED]** 自原第二個 §9 之 §9.3 |
| 9.8 | [MOVED] 對映表 | 新增 |

> **節序之取捨**：9.4／9.5 保留原號（其外部引用最多，含 §9.5.2／§9.5.3
> 之子節引用），故 G-A～G-N 與 G-L／G-M 順序後移至 9.6／9.7 而非插在中間。
> **保住既有引用優先於保住閱讀順序** —— 讀者有導覽表，引用沒有。

---
### 9.1 十一項通則

| # | 通則 | 來源 |
|---|---|---|
| 1 | **引用集合與生成集合是兩個分母**，須分立並各自具名；引用任一數時載明是哪一個，**不得互推** | R-U19（user_profiles）|
| 2 | **037 之 `Sub Categorization` 欄不作阻斷判準。** 阻斷之判準為「於本 feature 全部 spec 內**無任何介面可觀察端**」—— 需來回一趟才看得到，不等於看不到 | R-U21 |
| 3 | **spec 基線得有兩面**（結構面／內文面）。採雙面者須**指定何者為判讀基準**，另一面標「追溯用」；且**須載明該分工之已知例外** | R-U25 ＋ R-U35(a) ＋ R-U38 |
| 4 | **BLANK 之 style authority 不得取本管線自身之產出**（FO §5a 之延伸：不以自身先前輸出為來源）| R-U6（其原則部分）|
| 5 | **聊天附件之副本不等於 repo 檔。** 數字須在**有雜湊之物件**上重測；「大小相同」不是「內容相同」。以附件量得之數字為「被取代」而非「被複驗」 | R-U16 ＋ R-U18 |
| 6 | **判「不可讀」前須先驗抽取能力，且須跨素材形式試過**（xlsx／PDF／內嵌圖／向量文字層）。「抽不出來」與「沒去抽那一份」是兩件事 | R-U23 |
| 7 | **已知會誤切之來源，不得整份取代已知會少句之來源 —— 增欄，不取代。** 以一種錯法換另一種錯法不是修好 | R-U31 |
| 8 | **缺陷之解除條件須為機器檢查且實跑。** 文字修補（警示、註解、範例改寫）不構成 RESOLVED | R-U14 |
| 9 | **保住檔案與保住雜湊是兩件事。** 歸檔之檔案須有可執行之 `shasum -c`，且該雜湊檔本身須入版控 | R-U12 |
| 10 | **裁決條文須以可測判準表述，不以具名個案代替。** 以個案之名字寫成的條文，其適用範圍會被讀成該個案 | **R-U39(2)** |
| 11 | **一條裁決只管一件事。** 包了數件者，日後只能整條取代或整條保留 —— 兩者皆失真（見 FO §9.3）| 執行層 09 輪回報 |

> **第 10 項為本次收斂中最貴的一條。** `R-U22` 原文寫「`PROF-001-01`（PLP 表）
> 之處置」，於是「哪些 leaf 得引 `3.x`」被讀成「只有那一個 leaf」；
> R-U39(2) 改為可測判準（掃 180 leaf 之 `pdf_text` 找 `PLP` 字樣）後，
> 答案可能不只一條。**代價是一整輪的往返。**

### 9.2 全域裁決條文 R-G1～R-G11、R-G51～R-G68（含 R-G62′）、R-G42

> **2026-09-05 R-G43 改號**：原 R-G12～R-G29 十八條改為 R-G51～R-G68，`R-G23′`→`R-G62′`；
> R-G1～R-G11 與 R-G42 不動。**本節之號自此與 `RULINGS_LEDGER.md` 不再重疊。**
> 原節名為「全域裁決條文 R-G1 ～ R-G27」（該名自 R-G30 起即已與實況不符）。
> 對照表：`docs/fw036/SHA_MIGRATION_rg43.tsv`。

**本節為 R-G 系列之單一落點。** 整併前 R-G1～R-G51 有兩個表（原第一個 §9 之
§9.2 與第二個 §9 之 §9.1），兩表之「一句話」摘要有出入。整併規則：

1. **一句話以較完整之一版為準**，逐條與兩版原文比對，出入處列於 FO §9.8.2
2. **來源欄取自第二版**（第一版無此欄）
3. 兩版皆有而互補者（R-G1、R-G8）**併記**，不擇一
4. 兩版皆有而一版之命題實為他條所管者（R-G6），**取原命題**，另一版之陳述
   於 FO §9.8.2 註明其正確歸屬

**每條具穩定錨點**（`#### R-Gn`），其條文本體之 sha256 入
`docs/fw036/RULINGS.sha.tsv`，供 R-G52 之 `R-Gn@<sha8>` 引用。

| 條 | 題 | 來源 |
|---|---|---|
| R-G1 | 036 母本之固定與其身分 | user_profiles 02 輪 |
| R-G2 | `forms/` 舊檔以 `mv` 歸檔 | 02 輪 |
| R-G3 | `framework.md` 範例禁用 `openpyxl` + `wb.save()` | 02 輪，A-UP09 |
| R-G4 | 衍生檔之檔名歸屬與其讀者（現行版本 R-G4-1）| 05 輪（部分取代）|
| R-G5 | 全部 git 操作屬 Pei | 全輪次 |
| R-G6 | 上繳包之記載一致性 | —— |
| R-G7 | 反向驗證之對照向（現行版本 R-G7-1）| 多輪 |
| R-G8 | 比率須載明其分子與分母 | —— |
| R-G9 | lint 規則之驗證須含範圍向 | —— |
| R-G10 | 清單式分類須以餘數驗證 | —— |
| R-G11 | 可測判準須同時聲明其盲區 | 多輪 |
| R-G51 | `git commit` 一律帶 pathspec | 37 輪 |
| R-G52 | 裁決引用制（取代逐字照錄）| 23 包 §D，Pei 2026-08-24 |
| R-G53 | 綠色通道（一批一上繳之例外）| 同上 |
| R-G54 | Pilot 退出準則 | 同上 |
| R-G55 | 預期數字自動生成 | 同上 |
| R-G56 | 閘登錄簿與除役 | 同上 |
| R-G57 | canon 引用唯一可解析 | 同上，措辭依 24 包 §C 裁定 2 |
| R-G58 | prompt 指紋 | 同上 |
| R-G59 | 規則副本同步指紋 | 同上 |
| R-G60 | 自查表機檢對映 | 同上 |
| R-G61 | 條文之任何字元變動皆變更其 sha | 25 包 §C 裁定 C，Pei 2026-08-24 |
| R-G62 | 同一工單同時只得有一份有效下放包 | 26 包 §C [DEFAULT]，待 Pei 追認 |
| R-G62′ | 單一來源擴至每條線；取號一律 live | 27 包 §二，Pei 裁定 2026-08-24（出處 V33 裁定記錄 4）|
| R-G63 | 下放指示之路徑實在性 | bed_lowering 01 包，Pei 裁定 2026-08-26 |
| R-G64 | 產出物目錄政策 | 27 包 §C，Pei 裁定 2026-08-24（換號 08-27）|
| R-G65 | 工作區清理制 | 同上 |
| R-G66 | 來源集中制（`sources/`）| 同上 |
| R-G67 | CFTS 嵌入物件之逐 feature 檢查 | sw_update 53／54 包，Pei 裁定 2026-08-30 |
| R-G68 | 條文須加框（`body_kind` 不變式） | sw_update 59 包，**分析層 [DEFAULT] 2026-08-30，Pei 得推翻** |

#### R-G1 — 036 母本之固定與其身分

```
036 母本自 2026-08-17 起固定，不再逐 feature 詢問（見 FO §0 Tier 0）；
**其身分以 SHA 認定，非檔名**。
```

#### R-G2 — `forms/` 舊檔以 `mv` 歸檔

```
`forms/` 舊檔以 `mv` 歸檔，**不刪除**；移動前後各記 `shasum`。
```

#### R-G3 — `framework.md` 範例禁用 `openpyxl` + `wb.save()`

```
`framework.md` §Workbook sync 之範例禁用 `openpyxl` + `wb.save()`，
改 `xlsx_surgical` splice。
```

#### R-G4 — 衍生檔之檔名歸屬與其讀者

```
**現行版本為 R-G4-1。** `recon.py` 之 leaf→section 產物寫
`recon_leaf_to_section.tsv`；不得無聲覆寫既存 tracked 檔。
**其讀者為三個**（`lint_tcs.py`／`make_batch_context.py`／`extract_exemplars.py`）。
```

#### R-G5 — 全部 git 操作屬 Pei

```
**全部 git 操作屬 Pei**，含還原、回退、`checkout`／`restore`／`stash`／`clean`。
遇覆寫事故：**兩版並存、上報、停手**，不自行還原。
```

#### R-G6 — 上繳包之記載一致性

```
上繳包之記載一致性：「未執行 git」須與全文動作清單逐項對得起來；
**唯讀與改狀態之 git 分列**。
```

#### R-G7 — 反向驗證之對照向

```
**現行版本為 R-G7-1。** 反向驗證須含「什麼都沒做」之對照向；對照向**亦用於
驗證定位／抽取機制本身**，未全綠者須逐項追因，不得以「多數命中」通過。
```

#### R-G8 — 比率須載明其分子與分母

```
**任何比率須同時載明其分子與分母之定義。** 缺判準之比率不予採認，等同未量測。
```

#### R-G9 — lint 規則之驗證須含範圍向

```
**lint 規則之驗證須含範圍向** —— 對不該轉紅之近似案例證明其不轉紅。
只證明會 FAIL 之規則，可能是對所有東西都 FAIL 之規則。
```

#### R-G10 — 清單式分類須以餘數驗證

```
**清單式分類須以餘數驗證** —— 另以「全集減已分類」求餘數並驗其為空；
不得以逐項檢視代替。逐號列舉之缺漏，其形狀正是「相鄰兩號皆在清單內而它不在」。
```

#### R-G11 — 可測判準須同時聲明其盲區

```
**可測判準須同時聲明其盲區**，並指定盲區之處置路徑（人工判讀／另立判準／
接受漏失）。**未聲明盲區之判準，其「命中數」不得被當作「全集」**。
```

#### R-G51 — `git commit` 一律帶 pathspec

> **原編號 R-G12，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
**`git commit` 一律帶 pathspec**：`git commit -- <pathspec>`，不得使用不帶
pathspec 之 `git commit`（它提交整個 index，而 index 可能已含另一 session
置入之檔案）。`git add` 亦同：一律帶明確路徑，不用 `git add .`／`-A`。
**執行層仍只準備不執行（R-G5）**。
```

#### R-G52 — 裁決引用制（取代 FO §8.1「裁決逐字照錄」）

> **原編號 R-G13，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G13：裁決條文集中於各 feature 之 RULINGS.md 與 canon §9，每條具穩定
錨點（`### R-XX <slug>`）。`scripts/rulings_hash.py` 產生
`RULINGS.sha.tsv`（ruling_id → 條文本體 sha256），該 tsv 入版控。
下放包引用格式為 `R-XX@<sha8>`；執行層自 repo 讀取條文原文，
上繳包逐條回報所讀 sha8。sha 不符 = 停下回報，不自行調和（§8.4）。
未落檔之條文不得引用（§8.5-1 不變）。逐字照錄自本條生效起不再要求，
但下放包得於必要時仍附原文（附了不算錯）。
```

> 本條條文中以「canon」加裸節號 9 所指者為 **FO §9**（本節）。
> **條文逐字不改**，其實指以本註記錄（同 R-G60 之處置）；
> 該逐字行入 `CANON_REFS_WAIVER.tsv`，理由 `verbatim-ruling-text`。

**[DEFAULT] 上繳回報格式**（24 包 §C，分析層先裁，待 Pei 追認）：

```
R-G13 之上繳回報：逐條表列 `ruling_id | 下放引用 sha8 | 實讀 sha8 | 判`，
相符者亦列（FO §8.2 精神）。不符者依 R-G13 停下回報。
```

#### R-G53 — 綠色通道（FO §8.8 之例外）

> **原編號 R-G14，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G14：post-pilot Phase 6 批次，連續 3 批同時滿足
（lint 全綠、預期數字全符、全簿基線重現、獨立判斷無新發現）者，
自第 4 批起執行層自動續批，每 5 批彙總一份上繳；Pei 抽樣覆核
（每彙總至少 1 批全查 + 其餘批各抽 1 parent）。三分法、掃描條件揭露、
獨立判斷每批照附於彙總。任一批任一條件不符即退出通道，回到一批一上繳，
重新累計。§8.8「一批一上繳」加註「除 R-G14 生效期間」。
```

#### R-G54 — Pilot 退出準則

> **原編號 R-G15，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G15：pilot 判定以 done-region check 後之分類計：
- PASS：defect = 0 且 style-divergence ≤ 2（note 不計）
- PASS-with-corrections：defect ≤ 2 且皆為局部修正（非 corpus-wide
  規則錯誤），修正清單隨批落地
- REGENERATE：任一 defect 屬規則層（影響全 corpus 之 prompt / lint /
  profile 規則錯誤）
同一 pilot 重跑上限 2 次；第 3 次觸發 Tier 2 檢討，檢討對象為規則與
prompt 本身而非語料。
```

> 本條之操作性文字另載於 FO §1.2（Pilot review protocol）之 verdict 段。

#### R-G55 — 預期數字自動生成

> **原編號 R-G16，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G16：下放包之預期數字表由 `scripts/expected_numbers.py` 自
feature.yaml + 批次清單 + lint_defs 推導產生；分析層覆核後簽入包內。
手算僅限工具未覆蓋之新指標，逐項標 `[MANUAL]`。工具產出與上繳實測
不符時，工具與語料兩側皆查（§5a-16），不得預設任一側為準。
```

#### R-G56 — 閘登錄簿與除役

> **原編號 R-G17，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G17：`docs/runtime/GATES.tsv` 登錄每支 lint 閘：id、判準一句話、
來源裁決、生效日、近 10 輪命中數。上繳包附本批各閘命中統計。
連續 10 輪命中 0 之閘自動列入除役候選；Pei 於該 feature close-out
一次裁定。除役 = 移入 GATES.tsv `retired` 區段並於 lint_defs 停用，
不刪紀錄。G-A（三輪待判除役）併入本條管理，原文標
[SUPERSEDED by R-G17 — 管理機制部分]。
```

#### R-G57 — canon 引用唯一可解析

> **原編號 R-G18，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

**本條採 24 包 §C 裁定 2 之修訂版**（原 23 包 §D 版之「unresolved 一律 FAIL」
改為「waiver 清單外之 unresolved … FAIL」；理由見 24 包 §D-1）。

```
R-G18：canon 節號引用一律帶文件前綴（`FO §X` / `IN §X`）；此為書寫
規則，適用於兩份 canon 自身、模板、與所有新寫文件。歷史 handoff /
upstream 檔不追改（歷史記錄不改寫）；其既有 unresolved 與 ambiguous
引用逐檔逐行列舉於 `docs/fw036/CANON_REFS_WAIVER.tsv`（入版控）。
閘判準：waiver 清單外之 unresolved 或 ambiguous > 0 即 FAIL；
waiver 只減不增，新增即紅。裸「canon §X」於兩 canon 共用節號時計
ambiguous。本閘為每 feature close-out 必跑項。
```

> **兩份 canon 之代號**（R-G57 首跑所揭，23a §四-2）：
> `FO` = `docs/fw036/FEATURE_ONBOARDING.md`（流程、契約、全域裁決）；
> `IN` = `docs/runtime/ASPICE_SWE6_AI_Instruction.md`（TC 撰寫規則、欄位、自查表）。
> 兩者共用 17 個節號（0～8、8.1～8.7、9 —— 此處為節號之列舉，非引用），
> 故不帶前綴之引用於該 17 個
> 節號上**必然歧義** —— 這是 §9.1 第 10 項通則之同一形態：
> **以不帶判準之名字寫成的引用，其適用範圍會被讀成讀者手邊那一份。**
> 閘為 `scripts/canon_refs.py`。

#### R-G58 — prompt 指紋（TC 規則抗漂移之一）

> **原編號 R-G19，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G19：每批之批次 manifest 記錄本批實際使用之 prompt 模板 sha256 與
exemplar 集 sha256；上繳包照抄。與前批不符而下放包未宣告變更者，
該批退回。prompt 模板與 exemplar 集之任何變更為 Tier 2。
```

#### R-G59 — 規則副本同步指紋（TC 規則抗漂移之二）

> **原編號 R-G20，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G20：每次 pilot review 與 feature close-out，執行層回報
`docs/runtime/ASPICE_SWE6_AI_Instruction.md` 現行 sha256；分析層與
Project 指令副本所載 sha 比對。不符 = 先 re-sync Project 副本再進行
審查；審查不得在已知不同步之規則副本上進行。
```

#### R-G60 — 自查表機檢對映（TC 規則抗漂移之三）

> **原編號 R-G21，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G21：§9 自查表逐項標註其保證來源：有對應 lint 閘者記閘 id
（入 GATES.tsv），無者標「人工項」。pilot review 逐 TC 勾檢人工項。
使「機器保證」與「人力承擔」在紙上分得開（G-D、G-E 之精神）；
人工項清單之增減為 Tier 2。
```

> **本條所稱之自查表指 `IN §9`（Self-Check）**，非本節。
> 條文原文寫「§9」，依 R-G57 於此註明其實指，**原文不改**。

#### R-G61 — 條文之任何字元變動皆變更其 sha

> **原編號 R-G22，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G22：條文之任何字元變動（含加註、沿革、SUPERSEDED 標記）皆改變其
sha，不設「加註不算改動」之例外。下放包引用之 sha8 與執行層實讀不符時，
執行層停下回報（R-G13），分析層核對變動性質後於下一包換發新 sha8 引用；
變動屬實質修訂者，依通則另出 ′ 版條文。
```

> **本條之來源**（24 上繳 §十三-7）：R-VF45 於 24 包被加註
> `[本句之目標編號經裁定 3 取代]` 後其 sha 即變，而該加註**不是實質修訂**。
> 「加註是否算改動」若不裁，R-G52 之 sha 比對會在每次留痕加註後產生
> 一次假性不符，而假性不符多了就會被當成噪音忽略 —— **那正是 R-G52
> 之效力所繫**。故本條選擇「一律算改動」，把成本放在換發引用（分析層一次）
> 而非放在判斷變動性質（執行層每次）。
> **其代價**：留痕加註亦須換發 sha8，下放包之引用表因而每包可能有數列更新。

#### R-G62 — 同一工單同時只得有一份有效下放包

> **原編號 R-G23，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

**[DEFAULT]**（26 包 §C，分析層先裁，待 Pei 追認；Pei 得推翻）

```
R-G23 [DEFAULT]：同一工單同時只得有一份有效下放包；發現同輪重複下放
（如 23b 與 25 之分歧）時，以分析層指定之單一來源為準，另一份標
[SUPERSEDED] 不刪。全域線（docs/fw036）之下放包由單一分析 session
產出。（分析層 2026-08-24，依 R-VF66 之精神；Pei 得推翻）
```

> **本條之來源為其自身之違反實例。** 25 包（W-P2）撞上 `23b_wp2_supplement.md`
> 與 `25_wp2.md` 兩份同輪下放包，二者對裁定 D 之落點分歧（上繳 25 §五-1）。
> 26 包（W-P3）**在宣告本條的同一輪再度發生** —— `docs/fw036/handoff/` 下
> 同時有 `26_wp3.md`、`26_wp3_final.md`、`26_wp3_closeout.md` 三份，
> 落檔時間相隔六分鐘，各指定不同之上繳檔名，且
> **同一新條號 `R-G62` 被指派給兩件不同的事**
> （`26_wp3.md` 指「上繳前必跑閘」，本包指「單一下放包來源」）。
> Pei 於 chat 裁定以 `26_wp3_closeout.md` 為準，另二份依本條標 [SUPERSEDED]。
>
> **這正是 R-VS59～R-VS66 撞號之同一形態**（A-VF10）：
> **兩條線各自編號而無人持有全域之號碼簿。** 差別只在這次於當輪即被攔下，
> 而非活了六輪。

#### R-G62′ — 單一來源擴至每條線；取號一律 live

> **原編號 R-G23′，2026-09-05 隨其母條（R-G23→R-G62）改號，見 R-G43**。R-G43 之改號表未列 ′ 條；不隨改則 `R-G23′` 將指向台帳側之 R-G23（綁定須被檢查），即 R-G43 所欲消除之歧義本身。**此一推論為執行層所為，請分析層覆核**。

```
R-G23′（擴充，Pei 裁定 2026-08-24，出處 V33 裁定記錄 4）
單一來源之範圍由全域線擴至每條線：同一 feature／同一線同一時刻
僅一個分析 session 發包。R-VF／R-VS 取號一律「落檔當下 live 取號」
（grep "^### R-{前綴}" 取現行最大 +1），不得預先配號。
```

> **R-G62 本體一字不動**（R-G61：動了 sha 就換發）—— 本條為其 ′ 版擴充，
> 另立錨點另計 sha。
>
> **擴充之來源**：R-G62 只管全域線（`docs/fw036`），而**撞號實際發生在
> feature 線** —— `R-VS59`～`R-VS66` 八組（A-VF10）、V31 包之
> `R-VF83`／`R-VF84`／`R-VF85` 與既有同號者（V32 §1）。
> **兩次皆為兩個 session 各自對同一條線取號。**
>
> **「live 取號」之必要性亦為實測所得**：V31 包於成文時預配
> `R-VF83`–`R-VF85`，而該三號在其落檔前已被 24 包之改編佔用 ——
> **預配之號在落檔時已經不是空號。** 落檔當下取號使該窗口消失。

#### R-G63 —— 下放指示之路徑實在性

> **原編號 R-G24，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G24（Pei 裁定 2026-08-26）：凡下放包或下放指示要求對某路徑放檔、
搬移、讀取，分析層須於發出指示前建妥該路徑並以 list_directory 實測
驗證其存在；包內所載路徑一律為已驗證之實然路徑，不得為推定之應然
路徑。新 feature 接手時，_intake/{Feature_Name}/（TitleCase）之建立屬
intake recon 包之交付內容，缺此項該包不得視為完整。
```

> **本條之來源為其自身之違反實例。** bed_lowering 下放包 01 §六-1 指示
> Pei 放檔至 `_intake/bed_lowering/`，而該路徑當時**不存在**，
> 且 `_intake/` 之既有慣例為 TitleCase（AMFM、Comfort、Display、Privacy、
> SXM、Time_Management、Vehicle_Category）。**大小寫與存在性兩項皆為
> 三十秒可驗而未驗** —— 與 G-H 同型（答案在鄰近 feature 之交付現況裡，
> 查的成本三十秒）。
>
> **前六個 feature 未觸發，是因為其 `_intake/` 目錄早已存在，
> 不是因為指示對。** 新 feature 為該缺陷之首例。
>
> **與 G-L 之分工**：G-L 管上繳方向之素材宣告（「到齊」須附路徑與 SHA）；
> 本條管下放方向之動作指示（要人動的路徑須先驗存在）。
> **同一形態之兩個方向，先前只覆蓋了一半。**
>
> **附記（實測所揭，2026-08-26，同日更正）**：`_intake/` 為**暫存投遞區**，
> intake 完成後檔案移至 `features/{slug}/inputs/`。故本條所要求之「建妥」
> 是建投遞區，不是建最終落點；檔案之最終落點仍為 `inputs/`。
>
> **但「清空」並非 intake 完成之通例** —— 本條初版曾寫「八個子目錄現時皆為
> 0 files」，**該敘述不實，同日更正**：實測只有 `Bed_Lowering` 為 0；
> `AMFM`／`Comfort`／`Privacy`／`Time_Management` 檔案本體雖已移走，
> `INTAKE.md` + `intake.json` 仍留原地；`Display`／`SXM`／`Vehicle_Category`
> 連來源檔本體都還在。**故不得以「`_intake/<Feature>/` 是否為空」
> 推定該 feature 之 intake 狀態。**
>
> 初版那句是分析層以一次 `list_directory_with_sizes` 之總計列
> （`Total: 0 files, 8 directories`）推出來的 —— **而那一列只數頂層，
> 不遞迴。** 同一形態亦見於 G-D：一個永遠空的清單與一個壞掉的清單，
> 輸出相同。

#### R-G64 — 產出物目錄政策

> **原編號 R-G25，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G25：產出物目錄政策如下表。政策自生效日管新檔；既有檔案不搬移。
| 位置 | 內容 | 版控 |
|---|---|---|
| features/<f>/generated/ | LLM 產出 json | 入 |
| features/<f>/data/ | 量測中間物（tsv、manifest） | 入 |
| features/<f>/sandbox/<tag>/ | 工作簿作業副本（xlsx 只准在此修改） | 入 |
| features/<f>/delivered/ | 交付定稿唯一位置；定稿以複製入內，附 sha 對照表 | 入 |
| features/<f>/reports/ | 該 feature 之 lint 報告 | 入 |
| docs/reports/ | 跨 feature／全域報告 | 入 |
| output/ | 拋棄式暫存 | 不入 |
新產出落點不符者由 lint 路徑檢查判紅。delivered/ 內 xlsx 之 sha 須與
其對照表（delivered/MANIFEST.tsv）一致。
```

> **`sandbox/<tag>/` 為 xlsx 唯一可改之處**，與 R-G3（不得以 openpyxl
> 開啟寫入）分工：R-G3 管**手段**，本條管**位置**。
> **`delivered/` 只進不改** —— 定稿以複製入內，其 sha 由 MANIFEST.tsv 釘住；
> 改動定稿之唯一合法路徑是在 sandbox 產新版後再複製一份進來。

#### R-G65 — 工作區清理制

> **原編號 R-G26，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G26：superseded 產出（被新版取代之 json、舊 lint 報告）得自工作區
移除，git 歷史為其歸檔。移除前必跑引用懸空檢查 —— 被現行條文、異常、
waiver、對照表指名之檔不得移除。移除以專門 commit 為之，訊息列明
清單，不混入其他變更。現行有效版、delivered/、被引用檔一律留。
output/ 不入版控，隨時可清。
```

> **「git 歷史為其歸檔」是本條之全部前提** —— 未入版控之檔一經移除即無歸檔，
> 故 `output/` 以外之未追蹤檔不在本條射程內，其移除不受本條授權。
> **專門 commit** 之要求同 R-G51（一律帶 pathspec）：清理與內容變更混在
> 同一 commit 時，事後無從以單一 revert 還原被誤刪之檔。

#### R-G66 — 來源集中制（`sources/`）

> **原編號 R-G27，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G27：共用來源文件集中於頂層 sources/：raw/<doc_id>/ 放原檔
（xlsx／pdf／dbc，全 repo 一份）；extracted/<doc_id>/ 放 intake 抽取之
文字形（逐 sheet tsv／md，逐檔帶來源 sha 對照）；MANIFEST.tsv 記
doc_id、檔名、sha256、版本、使用 feature。feature 端不再存原檔副本，
feature.yaml 以 doc_id 引用。內容爭議以 raw 為準（FO §8.6 同精神）。
既有 feature 之舊副本不搬，新 feature 一律走 sources/。
```

> **`extracted/` 是衍生物，不是來源** —— 其與 `raw/` 不符時一律以 `raw/`
> 為準（FO §8.6）；抽取工具改版後 `extracted/` 得重產，`raw/` 不得。
> **與 R-G63 之銜接**：新 feature 之 `_intake/{Feature_Name}/` 仍為投遞區，
> 投遞後之原檔落點為 `sources/raw/<doc_id>/`，非 `features/<f>/inputs/`。

#### R-G67 — CFTS 嵌入物件之逐 feature 檢查

> **原編號 R-G28，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G28（Pei 裁定 2026-08-30）：intake 時須檢查該 feature 之母 CFTS 是否於
`…/Reference Documents/CFTS Embedded Objects/CFTS<nnn>/` 下有嵌入物件；
有者逐張轉為可讀影像並出「由圖找列」二欄表：**其所載之值／流程**、
**其對應之 037 列**，併記其與文字來源**一致或不一致**。不一致者為 DR 之材料。
查無者亦須記明「已查、無此目錄」，不得以未提及代替。
嵌入物件之 ObjectID 落於錨點池號段內而**不在錨定語料內** ——
其內容不進路徑 A，故錨定之三機制對其一律無效；
該事實須記入該 feature 之 `ANCHOR_POOL.md` 附記（R-G8）。
```

> **本條之來源**（sw_update，2026-08-30）：`CFTS057` 下六個 `.rtf`
> 皆為 Visio 圖，其中 `4908702`（Wi-Fi 下載 session 流程）載有四個門檻
> ——重試上限 7、`T = 30 minutes after timed mode has expired`、
> `T = 5 minutes since last data received`、中斷時終止 session 並
> `I += 1` 或 `I = 0`。**六個 ObjectID 於母 docx 之內文出現次數皆為 0** ——
> 號段落在池之範圍內，**而號段內不等於語料內**。
>
> **其後果不在錨錯，在覆蓋**：一列若其正解係某張圖所載，
> **路徑 A 在原理上找不到它，低分偵測器也不會攔它** ——
> 它不是「分數低」，是**不在候選集合中**。三機制（自證錨／區塊錨／低分）
> 皆假設正解在候選集合內，**對「不在集合內」者全部無效**。
>
> **「由圖找列」而非「由列找圖」之理由**：由列找圖不可窮舉
> （311 列 × 未知圖數），**由圖找列可以** —— 圖數有限，逐張問
> 「它所載之事對應到哪些列」。sw_update 對 `4908702` 實作之，
> 對應到 9 列，其中 1 列（`057`）與其**不一致**（同一個 30 分鐘，
> 037 起算於 ignition cycle，圖起算於 timed mode expired）——
> **該不一致即為 DR 之材料，而它只有做了這一步才看得到。**
>
> **與 G-M 之分工**：G-M 管「先查他 feature 之 `inputs/`」，
> 本條管「查本 feature 之母 CFTS 有無嵌入物件」。
> **同一形態之兩個方向** —— 素材不只在別人的目錄裡，也在自己那份文件裡面。
>
> **與 R-SU26（素材欄位全覽，sw_update 側）之分工**：
> 該條管「一份已知素材裡有哪些欄」，本條管「有哪些素材」。
> **欄位全覽做過不蘊含素材已盤點。**
>
> **追溯適用之拘束（Pei 裁定 2026-08-30，下放包 56 §二 #3）**：
> 本條立於既有七個 feature 之 intake 之後，其「未記明」已不可區辨為
> 「查過沒寫」抑或「沒查」。追溯適用拆兩段 —— **查**（全部 feature 立即，
> `ls` 一次即知）／**出表**（僅查得有物件者，隨其下一批）。
> **事後補查之記錄一律標明其為事後補查與其日期。**
> 其產物為**今天之事實**，**不得表述為「當時已查」** ——
> 二者在紙上長得一樣，而它們回答的不是同一個問題。
> **既有 feature 之「未記明」不追改為「已查」**，其洞具名留著。

#### R-G68 — 條文須加框（`body_kind` 之不變式）

> **原編號 R-G29，2026-09-05 改號，見 R-G43**（依 R-G43 §一：條文本體一字不改，故下框之首行仍書原號）。

```
R-G29 [DEFAULT]（分析層 2026-08-30，依上繳包 58 §6(丁)；Pei 得推翻）

凡 `RULINGS.sha.tsv` 中 `kind == ruling` 之錨點，其節內須有至少一個
fenced block；`body_kind == section` 者為缺陷，非一個類別。
判準由 `lint_docs036` 守之，其閘登錄 `GATES.tsv`（R-G17）。

理由：無框之條文，「哪裡是條文」由讀者認定，而 sha 只能量它看得見的
東西 —— 整節。故 R-G13 之引用比對對其失去鑑別力：條文被改與成因被補，
在 sha 上長得一樣（上繳包 58 §6(丙)）。

過渡：現有 74 條（(a) 26／(b) 48）為存量，其修補依下放包 59 §三 #1 之
次序分兩段。**閘於存量清完前以警示計數呈現，不判紅**；清完後轉紅。
```

> **[DEFAULT] 之理由**：R-G52／R-G61 皆為 Pei 所裁，
> **本條加諸其上一個新的形式要求** —— 分析層先裁以免阻斷，**Pei 得推翻**。
>
> **存量之數已更正**：下放包 59 §三 #2 之條文原載 `(a) 27／(b) 47`，
> **實測為 `(a) 26／(b) 48`** —— 其差為 `R-TM11`，
> 成因為執行層 T70b 之分類視窗偏移一行（上繳包 59 §1.1）。
> **本條之文字依實測記為 26／48。**
>
> **第一段已執行**（T71a，2026-08-30）：**(a) 26 條機械加框，
> 全部 26 條之框內文字與加框前之節文字逐字相同**（四檔合計 **+52 行、−0 行**，
> 即每條 2 行框標記，**無一字被改**）。

#### R-G42 — 交付規格表（全域）

```
R-G42（Pei 2026-08-30 裁「NR1L、全名」「不要再回歸，請寫下規則」）

適用本條生效後之每一次交付；既有已交付簿不回歸。
一、列序：D 欄依 req_id 數值升冪；037 有列而無 TC 之需求補一列僅填 D 欄；
    讀者改為全域 lint（量 delivered/ 內 xlsx 之 D 欄），不再依賴 WB-ORDER。
二、TC ID：NR1L-{ABBR}-{nnn}；ABBR 取 037 req_id 之縮寫 token，歧義由 Pei 裁一次登 feature.yaml。
三、Test Group：037 report 之 feature 全名，不縮寫。
四、固定欄：Author = PeiPYHsu；Priority 必填 P0–P3；Est. Time 留空 [DEFAULT]。
五、檔名：delivered/ 只放客戶檔名定稿 `…_SWQT_{FeatureName}_{YYYYMMDD}.xlsx`，
    無其他尾綴；sandbox 名之檔不進；每檔須有 MANIFEST 列（R-G25）。
六、內容物：xlsx ＋ MANIFEST ＋ DELIVERY_NOTE ＋ 未結 DR 清單 ＋（PARTIAL）tc_id 對照表。
七、PENDING：delivered/ 內須為 0；例外須有 R- 號記入 MANIFEST note。
八、讀者：lint_docs036 新閘 DELIVERY-SPEC，登 GATES.tsv；只掃 delivered/。
    features/<f>/output/ 自本條起廢用。
全文以 docs/fw036/RULINGS_LEDGER.md 之 R-G42 節為準。
```

#### R-G4／R-G7 之原文與 R-G51 之來源

`R-G4`／`R-G7` 之原文保留於 feature 側並標 `[SUPERSEDED by …]`，
**升上來的是修訂後之版本**（R-G4-1／R-G7-1）。

**R-G51 之來源**（2026-08-18，Pei 裁定升格）：`052f67d` 與
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
| `input_test_data` 之欄位歸屬（IN §4.5）| IT-2 | 57 輪 |
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

### 9.6 全域常規 G-A ～ G-K ＋ G-N

> **[MOVED]** 本節原為第二個 `## 9.` 之 §9.2；整併後移此，內容逐字未改。
> 原標題「G-A ～ G-K ＋ G-N（全域常規；G-L／G-M 見 §9.3）」中之
> 「§9.3」現為 **FO §9.7**（見 §9.8.1）。


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

### 9.7 兩項素材與資料之判準（53 輪 close-out）

> **[MOVED]** 本節原為第二個 `## 9.` 之 §9.3；整併後移此，內容逐字未改。


| # | 判準 | 成因 |
|---|---|---|
| **G-L** | **沒有路徑的「到齊」不算到齊。** 素材清單每項須附其**檔案系統路徑與 SHA**；「到齊」定義為 `shasum -c` 對得上 | 52 輪：Pop Up List 記「待驗」而它在 repo 裡三份；Tutorials 記「到齊」而它不在 |
| **G-M** | 「先查他 feature」之範圍**含其 `inputs/`**，不只交付件 | `TC-169` 寫「逐步對映不在我方輸入內」，**而那份輸入在 `features/comfort/inputs/`，卡了五十輪** |

### 9.8 [MOVED] 對映與兩版摘要之出入

#### 9.8.1 [MOVED] 對映表

整併前之節號 → 整併後之落點。**內容一律逐字保存，無一段被刪。**

| 整併前 | 標題 | 整併後 |
|---|---|---|
| 第一個 `## 9.` | 通則 —— 自 feature 條文升格者 | **併入本節之前言** |
| 第一個 §9.1 | 十一項通則 | §9.1（**不變**）|
| 第一個 §9.2 | 全域條文 R-G1～R-G51（集中）| §9.2（**併**，見 §9.8.2）|
| 第一個 §9.3 | 一條裁決只管一件事 | §9.3（**不變**）|
| 第二個 `## 9.` | 全域慣例（53 輪 close-out）| **併入本節之前言** |
| 第二個 §9.1 | R-G1 ～ R-G51（全域裁決條文）| §9.2（**併**，其來源欄升為主表之來源欄）|
| 第二個 §9.2 | G-A ～ G-K ＋ G-N（全域常規）| **[MOVED] → §9.6** |
| 第二個 §9.3 | 兩項素材與資料之判準 | **[MOVED] → §9.7** |
| 第二個 §9.4 | 缺口 —— 具名留給下一個 feature | §9.4（**不變**）|
| 第二個 §9.5 | 欄位接合矩陣（含 9.5.1～9.5.3）| §9.5（**不變**）|

**歧義引用之消解**：整併前裸 §9.1 有兩個落點（十一項通則／R-G 表），
裸 §9.2 有兩個（R-G 表／G-A～G-N），裸 §9.3 有兩個
（一條裁決只管一件事／G-L 與 G-M）。整併後各為唯一。
**歷史 handoff／upstream 檔中之既有引用不追改**（R-G57），其逐處列於
`docs/fw036/CANON_REFS_WAIVER.tsv`；**讀歷史檔遇 §9.1～§9.3 者，以本表判其實指**。

#### 9.8.2 R-G1～R-G51 兩版摘要之出入（逐條比對結果）

兩版逐條比對。**無實質矛盾**（FO §F-1 之升級條件未觸發）；出入為五類：
一版較完整（七條）、互補須併記（兩條）、命題歸屬須釐清（兩條）。

| 條 | 出入 | 處置 |
|---|---|---|
| R-G1 | **互補**。第一版「自 2026-08-17 起固定，不再逐 feature 詢問」；第二版「單一來源與其身分（SHA，非檔名）」。兩者非同一命題，第二版之「以 SHA 而非檔名認定身分」為第一版所無 | **併記**，兩句皆入 |
| R-G2 | 第一版多「移動前後各記 `shasum`」 | 取第一版 |
| R-G3 | 第一版多指名替代方案 `xlsx_surgical` splice | 取第一版 |
| R-G4 | 第一版載檔名與**三個讀者**；第二版僅「衍生檔之檔名歸屬」 | 取第一版 |
| R-G5 | **命題歸屬**。第一版「**全部** git 操作屬 Pei」並列舉 `checkout`／`restore`／`stash`／`clean`；第二版「執行層不執行**寫入性** git」。第二版較寬 | **取第一版**（較嚴者為現行操作依據：23 包 §A、23a §一皆依「全部」書寫）。第二版之「寫入性」為不精確之摘要 |
| R-G6 | **命題歸屬**。第一版「『未執行 git』須與全文動作清單逐項對得起來；唯讀與改狀態之 git 分列」；第二版「同一份文件內之數字須自洽」 | **取第一版**。第二版所述之「數字自洽」由 FO §5a 管，非 R-G6 之內容 |
| R-G7 | 第一版載「什麼都沒做」之對照向、對照向亦驗機制本身、不得以「多數命中」通過；第二版「閘須證明它會轉紅」 | 取第一版。第二版所述者為 G-K 之命題（相關而非同一）|
| R-G8 | **互補**。第一版只言「分子」；第二版「分子分母各是什麼」 | **併記**為「分子與分母」 |
| R-G9 | 第一版多「只證明會 FAIL 之規則，可能是對所有東西都 FAIL 之規則」 | 取第一版 |
| R-G10 | 第一版多餘數之算法與缺漏之形狀 | 取第一版 |
| R-G11 | 第一版多盲區之處置路徑與「命中數不得當作全集」 | 取第一版 |
| R-G51 | 第一版載完整判準與 `git add` 之同規 | 取第一版 |

> **本表本身即第 11 項通則之實例**：兩版之所以能出現出入而六輪無人察覺，
> 是因為「一句話摘要」不是可測判準 —— **兩個摘要都對，而它們說的不是同一件事。**
