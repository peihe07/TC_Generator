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
- `workbook_state` detection when segmentation is unambiguous
- Column mapping via header-text match (report match count, e.g. 32/32)
- Design-method vocabulary extraction from the 下拉選單 sheet
- Leaf inventory, coverage-gap counts, done-region req_id sets
- Spec text-layer availability (`pdftotext` yield test)
- spec_id → section/outline mapping build (fail-loud on miss)

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
