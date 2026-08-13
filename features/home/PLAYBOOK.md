# PLAYBOOK — Home (FW036 TC Generation)

> ## 寫回常設規則 —— R18-3（2026-08-13，取代 R16-2 凍結令）
>
> R16-2 之全 repo 寫回凍結**已解除**。解除依據：探針對 AMFM 客戶原件與
> FW036 空白範本兩次驗證皆 LOSSLESS，且不再有任何重產動作。
> 代之以下列常設規則，即刻生效、適用全 feature：
>
> 1. `backend/xlsx_surgical.py` 為**唯一**寫回路徑；
>    openpyxl 存檔路徑不得用於任何交付件產出
> 2. 寫回後強制比對輸出與輸入之 zip 成員集合、各 sheet 之
>    classic / x14 DV 計數，不等即 **ABORT**（非 warn）；
>    允許差異者僅限被寫入之 sheet XML 本身
> 3. 該 invariant 之違反屬 canon §0 第三項，升 Tier 2，
>    不得以放寬 invariant 解決
>
> 反向測試（R18-4）：`tests/test_xlsx_surgical_invariant.py` —— 兩種
> 破壞模式皆驗證確實 ABORT。裁決全文：`features/amfm/RULINGS.md` R18。
>
> **本 feature**：已交付件缺 14 個 zip 成員，**不重產**（R18-1），
> DEFERRED 至下次內容變動 —— A-H27。修復前需先擴充寫回路徑（interleaved）。

Instantiated retroactively at feature close-out (the template postdates this
feature's run; Home is the run that produced it). This is the OPERATIONAL
view: who does what, in which tool, with which handoff artifacts, and the
core TC-production loop. Rule authority stays with
`docs/fw036/FEATURE_ONBOARDING.md` and the generic instruction + profile
(`docs/runtime/profiles/FW036_R1L_Home_Profile.md`) — on any conflict,
those win. The status board (§6) reflects the actual Home run.

---

## 0. The working model

**Analysis happens in the Claude Project (chat). Execution happens in
Claude Code.** The two never blur:

- Chat is where evidence is weighed, options are surfaced, and Pei rules.
  Nothing in chat writes the workbook.
- Claude Code is where scripts run, files change, and gates enforce.
  Nothing in Claude Code rules on scope, style authority, or anomaly
  dispositions — it registers and proposes, then continues unaffected work.
- Every handoff is a FILE, not a memory: chat's output is signed
  documents (DECISIONS, RULINGS, profile, digests recorded into
  ANOMALIES/RUNBOOK); Claude Code's output is generated artifacts plus
  reports (RECON, lint_report, dry-run summary) that come BACK to chat for
  the next ruling. If it wasn't written down, it didn't happen.

## 1. Flow at a glance

```
 CHAT (analysis)                      CLAUDE CODE (execution)
 ──────────────────                   ──────────────────────
 P0  dump files, read INTAKE.md   →   intake.py [--scaffold]
 P1                                   recon.py → RECON + DECISIONS(pre-filled)
 P2  rule on [PROPOSED]/[PEI],    →
     sign DECISIONS
 P3  draft framework Part N +     →   (commit docs)
     profile with Claude, approve
 P4                                   adapt scripts per feature.yaml,
                                      build data artifacts
 P5  review pilot digest in chat, →   generate PILOT batch only, report
     rule corrections
 P6                                   remaining batches → lint green
 P7  review dry-run summary,      →   commit → --write → tag
     approve --write;
     draft RD-1 with Claude;
     submit (Pei only)
```

Chat touchpoints are exactly five: DECISIONS sign-off, framework/profile
approval, pilot review, dry-run approval, delivery. Everything else runs in
Claude Code without asking — bounded by the six stop conditions (canon §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; rulings recorded in `ANOMALIES.md`
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_Home_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (canon §6) — a summary missing a field is returned, not approved

## 3. The TC production loop (P5/P6 core, one parent per turn)

For each requirement parent, in 037 document order within its batch:

1. **Read** the parent's literal text + its batch context (spec sections,
   sibling rows including the done region, exemplars, popup/table rows)
2. **Scope** — before writing anything: check sibling reqs (do not absorb
   what a sibling owns, §8.2.1); check external references (do not absorb
   other specs' rules, §8.4.2); check the RD sub-id structure (one sub-id
   may need several TCs, §8.2.2 — never the inverse)
3. **Split** along genuine axes only (trigger / input / boundary / mode /
   environment, §8.3); one verification objective per TC (§5.7): one
   trigger's consequential outcomes = one TC with multi-line ER
4. **Write** fields per the generic instruction + profile overrides;
   reuse standard snippets verbatim; every literal (label, number, popup
   text, state name) traces to THIS feature's spec — cross-feature
   exemplars lend shape, never facts
5. **Reason** (繁中, 2–5 sentences): objective, key conditions, why this
   split, what was deliberately delegated and to whom
6. **Self-check** against the §9 list; emit; the generator assigns TC ids
7. On anything the sources don't state: `[ASSUMPTION A-Hnn]` marker +
   ANOMALIES entry, or BLOCKED placeholder — never a fabricated value

Placeholders keep the leaf's row (completeness invariant, both
directions): requirement sentence as Test Item, `BLOCKED - see Remarks`,
Remarks = reason + anomaly id.

## 4. The rules that never change per feature

- Three-layer quality: lint (mechanical) → human pilot gate (judgment) →
  done region arbitrates disputes with evidence. Lint-green ≠ done; a
  reviewer finding isn't a defect until it survives the done-region check.
- Done region is style authority, never factual authority; frozen
  byte-for-byte under the state-appropriate hash invariant.
- Write-back invariants abort, never warn; weakening one is a chat ruling.
- Sequence at delivery: dry-run reviewed → clean-tree commit → `--write`
  (touches no tracked file) → annotated tag `fw036-home-regen-vN`
  carrying xlsx SHA256 + done-region hash + row summary + lint result.
- The workbook Scope field is the workbook's identity claim — verify it
  matches the ruled requirement source at intake AND before submission
  (Home itself had it wrong: A-H26).
- RD-1 at delivery: systemic classes first with class-level remedies;
  every item = anomaly id + evidence + local disposition + requested
  action; the feature never waits on answers.
- What VARIES lives only in `feature.yaml` (paths, columns, done-region
  rule, spec_mode, reference template, lint vocab) and the profile
  ([OVERRIDE]/[ADD] clauses citing what they displace). Scripts are
  copy+yaml, no shared library (canon §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `features/home/PLAYBOOK.md`、`features/home/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`features/home/feature.yaml`、
> `docs/runtime/profiles/FW036_R1L_Home_Profile.md`。目前狀態:{P?,一句話}。
> 本次執行:{任務}。遇到六條停下條款就登記並停,PENDING 的子決策
> ({列出})不得自行處置。完成後回報{對應上繳包}。

Current instance (the only remaining Claude Code task):

> 目前狀態:P7,v1 已 tag,A-H26 裁決要求 Scope 修正後重出 v2。
> 本次執行:A-H26 工單 — write_back 加 header 修正步(Scope →
> `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1`)、乾淨 tree commit、
> `--write`、tag `fw036-home-regen-v2`(annotation 含新 SHA256、
> done-region hash `b40e56826e7d7d84…`、144/72(4)/225、lint green、
> A-H26 註記)。v1 tag 保留。完成後回報 v2 SHA256。

## 6. Status board — Home

- [x] P0 intake complete (pre-dates intake.py; files assembled manually;
      Last Mode spec initially thought missing → found in inputs, A-H03)
- [x] P1 recon complete; workbook_state: PARTIAL_INTERLEAVED;
      leaves: 140; targets: 62 (done region: 144 rows / 3 segments, Arif)
- [x] P2 rulings signed (in-chat, recorded in ANOMALIES: A-H01…A-H05 et al.)
- [x] P3 framework Part II + Home profile approved
- [x] P4 data artifacts built (outline map, spec split OCR-anchored,
      exemplars by chapter)
- [x] P5 pilot reviewed 2026-08-09; verdict: PASS-with-corrections
      (A-H10 amendment, popup notation); retroactive ratifications A-H03/
      A-H09/A-H20 recorded
- [x] P6 all batches generated: 72 TCs / 62 leaves + 4 placeholders
      {055-03, 066, 070, 071}; lint green post-amendment;
      P0/P1/P2/P3 = 10/37/19/2
- [ ] P7 — v1 tagged (`fw036-home-regen-v1`); **pending: A-H26 v2 re-issue
      → controlled-document submission → RD-1 send**
      (`docs/fw036/RD1_questions_home.md`, recipient to fill; add A-H26 to
      Group 4 as self-corrected FYI)
- Open PENDING rulings: none (Home-side). Anomaly register: A-H01…A-H26,
  all RESOLVED/RECORDED except the RD-1 upstream answers.
