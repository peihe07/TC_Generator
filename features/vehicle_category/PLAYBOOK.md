# PLAYBOOK — Vehicle Category (FW036 TC Generation)

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
Claude Code without asking — bounded by the six stop conditions (FO §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (FO §6) — a summary missing a field is returned, not approved

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
7. On anything the sources don't state: `[ASSUMPTION A-VCnn]` marker +
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
  copy+yaml, no shared library (FO §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `Vehicle CategoryHMI/PLAYBOOK.md`、`Vehicle CategoryHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`Vehicle CategoryHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 7. 操作慣例（建議，非條文）

> 下放包 13 T76。**二則皆為操作慣例，不是裁決條文** ——
> 其違反不構成停止條件，但照做可省一輪。
> 二則之由來皆為實際發生過的錯，逐則記其出處。

### 7.1 新寫掃描器／檢查器時，先跑兩組已知輸入 —— **雙向**

```
(a) 反向輸入 —— 確認其會 FAIL（防判準太鬆）
(b) 已知標的 —— 確認其會命中（防判準太窄）
下放包已點名之標的、既往異常所載之實例，皆為現成之 (b)。
二者缺一，判準之邊界只被逼出一邊。

(b) 之已知標的，**優先取單筆或極小之探針**，而非既有批次。
    既有批次能驗判準，驗不到隨批次大小而變之實作假設
    （硬編位置索引、`[0]`／`[-1]`、min/max 之空集合處理）。
```

### 7.1.1 「先」須為程式結構，不是紀律（下放包 20 §1.1）

三次同型（T52／T79／T105c），**其中第三次發生於 §7.1(b) 已存在之後** ——
問題不再是規則缺口，是「**先**」字沒有被結構化：
寫完掃描器、跑了全批、看到結果，然後才想起該驗已知標的。

**處置 —— 已知標的驗證改為掃描器之自帶前置斷言（self-test）**：

```
掃描器之 main 流程：
  1. 斷言已知標的命中（assert probe in results-of-probe-run）
  2. 斷言反向輸入 FAIL
  3. 二者通過，始跑正式母體
  1／2 失敗即以非零碼退出，不輸出任何正式結果。
```

**「先」由紀律變為程式結構 —— 不先跑就跑不了。**

適用：**新寫者一律適用，既有掃描器不回溯。**
首個適用者為 CONT 表之二層防護（下放包 20a §2.4）。

> 末段之由來（下放包 18 §七）：第九件（`TCS[10]` 硬編位置索引）
> 之所以被抓到，是因為 (b) 用了**單筆探針**。若 (b) 只用既有批次驗，
> 它會潛伏到某個 10 筆以下之批次 —— 而**第 6 批（`Brake Service`，2 leaf）
> 與第 7 批（`Cabrio Widget`，1 leaf）正是那樣的批次**。

**原則僅有 (a)。** 擴為雙向之由來（下放包 15 §四）：
T52 與 T79 之初版**皆漏抓它被造出來要抓的那一筆**，二次同型非巧合。
(a) 驗的是「該 FAIL 的會 FAIL」，**驗不到「該命中的會不會命中」**。

T79 尤為典型：分析層 §2.3(a) **已點名 `VC-007-01`**，那就是一個現成的
已知標的 —— 掃描器寫完先跑它，初版之漏抓當場現形。

**不只載明反例。** 把反例真的塞進待驗檔跑一次，確認檢查器抓得到，
再還原。已知標的同理。

由來：上繳包 11 §5.3 之自我限定 —— 「寫檢查器的人和寫被檢查物的人
是同一個，判準就帶著我的盲點」。**光寫反例仍是自己說了算；
跑一次才知道判準接得住。** 下放包 13 §一採此法為往後之標準作法。

實例：第 11／12 項（上繳包 12 §4.2）、第 13／14 項（上繳包 13 §2.2）——
四項皆先注入反例確認 FAIL、再還原確認 PASS。
第 14 項之反例僅差一個字母大小寫（`tab` → `Tab`），仍被抓到。

### 7.2 任何判讀之輸入不得為顯示用之截斷字串

> **⚠ 範圍已擴充（下放包 18 §一）。** 原措辭為「**複核腳本之掃描標的**
> 不得為顯示用之截斷字串」，**原措辭不刪**（R-TM13），修訂文如下。
> 第一次修法只寫了「掃描標的」，範圍限在腳本，**故第二次仍然發生**。

```
§7.2（修訂）

任何判讀之輸入不得為顯示用之截斷字串 —— 不論該判讀由腳本或由人為之。

適用範圍含但不限於：正則掃描、集合比對、統計、以及**據以下裁**。
凡以 `[:n]`、`head`、`textwrap` 或任何顯示層裁切取得之字串，
一律不得作為判斷之依據；需要判斷時重取完整值。

由來：二次同源 —— 第六件（74 字元截斷之正則誤報）、
下放包 17 §4.1(1)（230 字元截斷後誤判 037 為異常）。
第一次修法只寫了「掃描標的」，範圍限在腳本，故第二次仍然發生。
```

**原措辭（保留）**：複核腳本之掃描標的不得為顯示用之截斷字串。

由來：下放包 13 §二 —— 分析層複核 Final Step 時對 `VC-028-02`
誤報「無檢查動詞」，因其**對一個截斷至 74 字元的顯示字串跑正則**，
而 `record` 落在截斷之後。**判準本身沒錯，套在錯的輸入上。**

第二次（下放包 17 §4.1(1)）：分析層之粗查腳本寫 `d[:230]`，
對截斷後之字串下裁，並把二筆完整之 037 Description 寫成「疑似異常須登記」。
**這次不是腳本判準錯，是讀完之後用眼睛下的裁定** —— 原措辭涵蓋不到。

該件之意義：上繳包 11 §9 之自我限定**不限於執行層** ——
複核者的錯更難被發現，因為複核之後沒有下一道。

---

## 6. Status board — Vehicle Category

- [ ] P0 intake complete; INTAKE.md reviewed; missing files: ____
- [ ] P1 recon complete; workbook_state: ____; leaves: ____; targets: ____
- [ ] P2 DECISIONS signed (date: ____)
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING rulings: ____
