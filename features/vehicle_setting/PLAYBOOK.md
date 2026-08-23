# PLAYBOOK — Vehicle Setting (FW036 TC Generation)

Copied into every feature directory by `new_feature.py`. This is the
OPERATIONAL view: who does what, in which tool, with which handoff
artifacts, and the core TC-production loop. Rule authority stays with
`docs/fw036/FEATURE_ONBOARDING.md` (phases, tiers, workbook_state,
spec_mode) and the generic instruction + feature profile — on any conflict,
those win. Check off and annotate this file as the feature progresses; it
doubles as the feature's status board.

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
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_Vehicle Setting_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-VEnn]` marker +
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
  (touches no tracked file) → annotated tag `fw036-{feature}-regen-vN`
  carrying xlsx SHA256 + done-region hash + row summary + lint result.
- The workbook Scope field is the workbook's identity claim — verify it
  matches the ruled requirement source at intake AND before submission
  (two independent features had it wrong in one week).
- RD-1 at delivery: systemic classes first with class-level remedies;
  every item = anomaly id + evidence + local disposition + requested
  action; the feature never waits on answers.
- What VARIES lives only in `feature.yaml` (paths, columns, done-region
  rule, spec_mode, reference template, lint vocab) and the profile
  ([OVERRIDE]/[ADD] clauses citing what they displace). Scripts are
  copy+yaml, no shared library (canon §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `Vehicle SettingHMI/PLAYBOOK.md`、`Vehicle SettingHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`Vehicle SettingHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Vehicle Setting

- [x] P0 intake complete; INTAKE.md reviewed; missing files: none (INPUTS.sha256 recorded)
- [x] P1 recon complete; workbook_state: BLANK; leaves: 271 (237 Functional); targets: 237
- [x] P2 DECISIONS signed (date: 2026-08-20)
- [x] P3 framework Part N + profile approved — framework **locked 2026-08-22** (P19, signed 2026-08-20); profile `FW036_R1L_VehicleSetting_Profile.md` created round 18
- [x] P4 data artifacts built — `leaves.tsv` / `leaf_to_reqid.tsv` / `lid_pairs.tsv` / `spec_variables.tsv` (+ `normalized_key`, `suspect_prefix`) / `can_signal_map.tsv` / `delegation_lookup.tsv`
- [x] P5 pilot batch **01** reviewed; verdict: **PASS (Pei, 2026-08-22)**; corrections: 3 defects (D-1 baseline comparison, D-2 final-step action, D-3 executable steps < 2) → `batch01_v3.json`, batch **10 → 8**
- [ ] P6 all batches generated; lint green; placeholders: **4 PENDING lines across 2 TCs held out of batch** (`Stop-StartSystem-006` DR-19, `SwitchLHD/RHD-010` DR-20)
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: **2026-08-22, items 1–5 of the 8-item dispatch letter (37 §2)**

### Open DRs — 待送 vs 待覆 (D-9)

| DR | 送件文項次 | 阻塞 | 影響 leaf | 狀態 |
|---|---|---|---:|---|
| DR-15 | 1 | yes | 160 | **待覆**（送出 2026-08-22） |
| DR-17 | 2 | yes | 14 | **待覆**（送出 2026-08-22） |
| DR-14′ | 3 | yes | 16 | **待覆**（送出 2026-08-22） |
| DR-19 | 4 | yes | 3 | **待覆**（送出 2026-08-22） |
| DR-20 | 5 | yes | 1 | **待覆**（送出 2026-08-22） |
| DR-18 | 6 | no (確認型) | 160 | **待送** |
| DR-8 | — | no | — | **待送** |
| DR-11 | — | no | 1 | **待送** |
| DR-12 | — | no | — | **待送** |

送件文第 7 項（`$VC_VEH_LINE$` 車型碼）與第 8 項（`$PowerMode$` 之 `IGN_OFF_ACC`）
**於 `DATA_REQUESTS.md` 無對應之 DR 編號**，且本次未送。

- Open PENDING rulings: none — R-VS19″ / R-VS41 / P19 皆已裁；`A-VS02` 為缺號，不補不重編

---

## 判準之錨點檢查表（R-VF19，2026-08-23）

**凡書寫判準者 —— 正規化規則、掃描定義、比對條件、篩選式 ——
落筆時即附兩個錨點。分析層書寫下放包中之判準時同受拘束。**

| # | 步驟 | 不做會怎樣 |
|---|---|---|
| 1 | 寫下**必命中錨點**：一個已知應命中之實例 | 判準過窄而命中 0，與「標的不存在」不可分辨 |
| 2 | 寫下**必不命中錨點**：一個已知不應命中之實例 | 判準過寬而大量偽陽性，與「標的很多」不可分辨 |
| 3 | **先驗錨點存在於被掃描之集合內**（R-VF19 執行層註，A-VF4） | 錨點值恆為 `None`，「前後不變」與「集合內無此列」不可分辨 |
| 4 | 實作後**先對錨點實測**，錨點不符者回報並停 | 錯誤之判準套用於全集，其輸出與正確結果不可分辨 |
| 5 | 錨點與其實測值**寫入上繳** | 後人無從複驗該判準當時是否成立 |

**本檢查表之立法史（不刪 —— 其為「條文已立不等於已進入慣性」之證據）**：

- **A-VS135(a)** R-VF8 之逐字正規化不足以達成其目的（`\n` 之序列化）
- **A-VS135(b)(c)** R-VF7 之 token 定義三度修正（泛用詞／訊息名／`$X$` 誤濾）
- **A-VF2** R-VF11 立法**當輪**，執行層寫 W-VF14 判準 (c) 時仍未附錨點
- **A-VF4** 錨點本身選錯：選了不在被掃描檔內之 leaf（W-VF18、R-VF17 首版）
- 分析層側：V06 §5.3(2) 之「簇分布必變」為未經錨點檢驗之斷言，實測為錯
