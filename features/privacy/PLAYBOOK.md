# PLAYBOOK — Privacy (FW036 TC Generation)

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
> **本 feature**：尚未寫回。P7 依規則 1 走 `xlsx_surgical`，規則 2 之 invariant 為交付前 gate —— A-PV09。
>
> **寫回路徑（R20-5, 2026-08-13）**：Privacy 尚未寫回。其 write_back
> **不得複製任一既有 feature 之腳本作為起點**（四支皆已封存），
> 自始建於 `backend/xlsx_surgical.py`，並受 R18-3 之 ABORT 級
> invariant 拘束。此為 R18-3 規則 1 之首次正向適用。

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
- Profile: `docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-PRnn]` marker +
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

> 讀 `PrivacyHMI/PLAYBOOK.md`、`PrivacyHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`PrivacyHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Privacy

> 值之來源：`RECON.md` / `_intake/Privacy/INTAKE.md` / `data/recon.json`
> 之實測，非記憶或下放包轉述（R17-3）。更新於 2026-08-13。

- [x] P0 intake complete; INTAKE.md reviewed; 7 檔全數分類（零
      unclassified／unreadable）; spec_mode **D**;
      missing files: **無缺件**，但需求報告之 source 欄為 component/
      Polarion id，**need list 不可自該範本導出**（trace 走
      architecture／export 檔）
- [x] P1 recon complete; workbook_state: **BLANK**; leaves: **10**;
      targets: **10**（`SWE1-HMI-PRIVACY_FEATURES-001` … `-010`，
      covered nowhere = 10）
- [ ] P2 DECISIONS signed (date: ____) —— `DECISIONS.md` §8 已有三條簽署
      裁決（R-PV01(c)、R-PV01(a)(b)(d) 延後、R-PV02），
      但 sign-off 欄仍空，故不勾
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING rulings: **1 條** —— **A-PV14**（V6_R2 之 `inputs/` 副本
  對齊 DT28 而非 HDCC28；P2 引用該檔前須先裁定平台版本）。
  2026-08-13 下放包 02：R23 八條簽署，A-PV01 / 04 / 05 / 07 / 08 / 10 /
  11 / 12 全數轉 RESOLVED。
  另 DEFERRED 2 條（A-PV02 之 ANC 部分、A-PV03）、CLOSED 1 條（A-PV09）
- 素材／產出雜湊（2026-08-13 建立）：`BASELINE.sha256`（8 個素材）與
  `DELIVERY.sha256`（產出摘要）**已納入版控**，`inputs/` 與 `output/`
  維持 gitignored。**每次 session opener 與每個 batch gate 執行**
  （自 `features/privacy/` 起）：

  ```bash
  shasum -a 256 -c BASELINE.sha256                    # 8 OK，exit 0
  shasum -a 256 -c --ignore-missing DELIVERY.sha256   # exit 0
  ```

  `DELIVERY.sha256` 為 **append-only 台帳**，逐次追加不覆蓋；舊條目即使
  其檔案已從 `output/` 清掉仍留著。`--ignore-missing` 因此是必要的 ——
  不加會讓已清理的舊產出報 `FAILED open or read`。加了之後，
  內容遭竄改仍 `FAILED` 且 exit 1（已實測），檔案不存在則靜默略過。
  亦即該指令驗的是「還在磁碟上的產出有沒有被動過」，不是「產出還在不在」。

  任一 `FAILED` 即停手回報 —— 素材或產出在無裁決的情況下變動了。
  雜湊需要更新時必須連同裁決編號一併更新；**無裁決而需更新，
  那件事本身就是要回報的**。`BASELINE.sha256` 之更新為就地修正
  （素材是同一批），`DELIVERY.sha256` 之更新一律為**新增 ENTRY**。
- 範本準備（R23-4 / R23-5, 2026-08-13）：殘留樣本列五格已清、
  D5 Scope 已填 `SWE1_CFTS_022-Privacy_Features`。
  產物 `output/…_SWQT_Privacy_20260813.xlsx`（SHA256 `ed741d8d23f7…`）；
  **客戶原件 `inputs/` 逐 byte 未動**（`cd876c202c71e74b…`）
- 基準確認（R22 §2, 2026-08-13）：`inputs/` 8 檔全數 **MATCH**
  `/Users/peihe/Work/02_Project_R1LR/` 樹內同名候選。
  **現在式陳述**（R22-1）：此刻相符，不蘊含「從未被覆寫」
