# PLAYBOOK — User_Profiles (FW036 TC Generation)

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
- Profile: `docs/runtime/profiles/FW036_R1L_User_Profiles_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-USnn]` marker +
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

> 讀 `User_ProfilesHMI/PLAYBOOK.md`、`User_ProfilesHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`User_ProfilesHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — User_Profiles

**最後更新：58 輪 close-out（2026-08-20）。本 feature 之分析層無未結項。**

- [x] **P0** intake complete；missing files：**3 項**（`PU1087`/`PU1088` 內文、
      RD #5、RD #6）—— 皆不擋執行，替代作法見 `DELIVERY_NOTE.md` §4.1
- [x] **P1** recon complete；workbook_state **BLANK**；leaves **180**；
      targets 180 / 180
- [x] **P2** DECISIONS signed（D-UP11-01 ～ D-UP41-01）
- [x] **P3** framework Part + profile approved（`docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md`）
- [x] **P4** data artifacts built（`outline_map.json` 169 節、`spec_popup_ids.tsv` 32、
      補句表、`verb_synonyms.tsv`、`enum_vocab.tsv`、`pending_judgements.tsv`）
- [x] **P5** pilot 16 條 reviewed；其後各批逐批覆核
- [x] **P6** all batches generated：**189 條，leaf 180 / 180**；
      lint green；placeholder **0**
- [x] **P7 寫回完成** → `DELIVERY.sha256` **ENTRY 001／002／003／005**
      （**004 未產出**：56 包曾指定，57 包指示與 AE-1 合併，台帳留「未產出」區塊說明號次跳空）；
      **未 tag、未送客戶目錄、RD 未寄 —— 三者皆屬 Pei**

### 6.1 覆核

| pack | 範圍 | 已讀 | 現行檔 |
|---|---|---|---|
| 24a | 135–145 | 11 / 11 | `57_review_pack_24a.md` |
| 24b | 146–156 | 11 / 11 | `57_review_pack_24b.md` |
| 33a | 157–173 | 17 / 17 | `57_review_pack_33a.md` |
| 33b | 174–189 | 16 / 16 | `57_review_pack_33b.md` |

**189 / 189 全部經第二人逐條讀畢**（56 包 §一：`TC-165` 本輪讀畢，缺陷 0）——
**分析層之覆核義務結清。**

**四份 pack 於 57 輪重出**（AD-1 之第二段改寫 31 條 ＋ AE-1 之搬移 6 條），
`--verify` 皆 0 不符。**其所轉錄之第二段英文措辭，是最後一批交付內容之變動。**

### 6.2 Open items

| 項 | 屬誰 |
|---|---|
| **交付**（送客戶目錄）| **Pei** |
| **git**（指令清單見 53 上繳 §7）| **Pei** |
| `R-U17`（刪 `inputs/` 之 spec 副本）| **Pei** |
| RD v2 ＋ #8 ＋ **A-UP14** 之寄出 | **Pei** |
| **Tutorials L&F 之 PDF 落 `inputs/`**（若欲補 `TC-167` 之引用欄）| **Pei** |
| **A-UP14** 之裁決（兩份上游對三個 popup id 之角色記載不一致）| **上游** |
| `A-UP09` | RESOLVED（41 輪）|
| `A-UP11`／`A-UP13` | 見 `ANOMALIES.md` |
| Open PENDING rulings | **無** |

### 6.3 收尾之數字

| 項 | 值 |
|---|---|
| TC | **189** ／ leaf **180 / 180** |
| 優先級 | P0×38 P1×66 P2×71 P3×14 |
| 閘 | **19 支**（新增 `audit_second_segment`；`audit_consistency` 內另增 IT-1／IT-2）|
| 方向性案例 | `audit_consistency` **65**、`lint_tcs` 64、`audit_delivery_fields` 16、`audit_second_segment` 13、其餘合計 100+ |
| 交付前自檢 | **十項**（57 輪新增第 j 項：IT）|
| 產出 | **ENTRY 001／002／003／005**，皆未交付 |
| 缺件 | **3 項**，皆不擋執行 |
| 已具名之留白 | **28 條** ＋ `INTR2.)` ＋ A-UP14 |
| **已知未查之欄位接合** | **9 組**，逐組具名於 canon §9.5 —— **「已知未查」，不是「已查為綠」** |
