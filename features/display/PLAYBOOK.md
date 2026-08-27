# PLAYBOOK — Display (FW036 TC Generation)

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
- Profile: `docs/runtime/profiles/FW036_R1L_Display_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-DInn]` marker +
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

> 讀 `DisplayHMI/PLAYBOOK.md`、`DisplayHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`DisplayHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 5a. 寫作慣例（**建議，非條文**）

> 本節之項為**慣例**，不是裁決條文；違反不觸發任何停止條件。
> 立於下放包 32 §1.4 末，其來由為執行層連續兩輪之同型失誤。

### 5a.1 全稱句之上方緊接其所據之輸出

凡寫「**全在／皆為／不含／無一／全部**」之句，其**正上方**應緊接
該句所據之腳本輸出。

**來由**（兩例，皆為執行層自陳）：

| 輪 | 寫下之句 | 實情 |
|---|---|---|
| 29 §2.2 | 「CFTS_020 之 `EE Architecture` 值域**不含** `All`」 | 30 輪實測 `All` 出現 **83** 次，舊判準漏網 **71** 條。該句是那一輪回溯結論之**整個依據**，而它沒被量過 |
| 31 §5.2 初稿 | 「其主題**為**通訊中斷／DTC 之診斷行為」 | 該句上方之輸出正寫著 **59/63 零命中** —— 句子是從**章節標題**推的，計數的卻是**本體** |

**兩次皆為 R-G22 所規制**（斷言須由腳本產出），**而 R-G22 已經在了。**
第二次之更正來自「輸出恰好擺在旁邊」——**該幸運不可依賴，
但它指出這個可設計之習慣。**

**其最易失守之處**：「回溯檢查」類文件 —— 該類文件之語氣已在宣告
自己在查證，讀者（含作者）遂不再問「這一句本身量過沒有」。
（同 ledger 之 R-G22 條下指標。）

## 5b. 交付慣例（**建議，非條文** —— 立於下放包 34b §三）

> R-DM57 收尾凍結期內不立新條文。本節與 §5a 同為慣例。

### 5b.1 交付版面之列序 = Requirement ID 升冪

`write_back_036.py` 之列序自下放包 34b 起以 **Requirement ID 升冪**為預設；
**批次序僅為生成時之內部順序，不得出現在交付版面。**

**來由**：34／34a 之交付本按 `pilot-01` → `rvc-01` → `ops-01` 之生成序寫回，
於工作簿上呈現為 `004 004 005 007 007 007 008 … 001 001 …` ——
讀者（客戶）看到的是我們的作業史，不是需求結構。

**同一裁定之另一半**：無 TC 之需求**補一空列，僅填 D 欄**。
未覆蓋一事因而由「讀者須自行比對 037」變為「打開工作簿即見」。

### 5b.2 母本之公式欄與樣式，寫回時一律不得代償

B 欄為公式欄（R-DM15，條文早已在），母本 `B11` 更是
`ref="B11:B74"` 之**共用公式宿主**；賦值不只毀該格，是毀掉 64 列的公式。
同理，改寫儲存格時須保留其 `s=` 樣式索引與 `<row>` 之屬性。

**來由**：34b 執行時比對母本才抓到 —— **條文在、`feature.yaml` 之註記也在，
腳本仍寫了 B 欄，且連續兩份交付本帶著它出門。**
註記寫在被讀的地方，不等於寫在被執行的地方。

## 6. Status board — Display

- [ ] P0 intake complete; INTAKE.md reviewed; missing files: ____
- [ ] P1 recon complete; workbook_state: ____; leaves: ____; targets: ____
- [ ] P2 DECISIONS signed (date: ____)
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [x] **P5 pilot batch `pilot-01` reviewed**（rev1 → rev5）; verdict: 核可;
      corrections: #2 deferred（DR-DM10）、欄位歸屬、邊界負向條、#1 收斂為訊號側
- [x] **P6 all batches generated; lint green**
      `pilot-01` 3 ＋ `rvc-01` 6 ＋ `ops-01` 14 = **23 TC**;
      `lint036 --profile display` 二十項行計皆 0（合併母體 23）;
      `check_disclosure.py` 雙向 0／0;
      placeholders: **無 `PENDING:` 佔位**；未涵蓋面向以 deferred 四鍵 ＋
      R-G33 括號下半指名承載（8 項 token）
- [~] **P7 交付件已產出並複製至交付路徑（2026-08-26）**；
      **tag 未打、Excel 實開未確認、RD-1 未發**
      - **2026-08-27（34b）**：`output/` 已重出**版面修正版**
        （sha `06972455…`，24 列 = 23 TC ＋ `SWE1-DM-006` 空列，
        列序改為 Requirement ID 升冪）。**TC 內容一字不動。**
        `DELIVERY.sha256` **ENTRY 002** 已建。
      - **交付路徑之副本尚未更新，且已與台帳不符** ——
        客戶樹之檔實測 sha `b12bd378…`（非 ENTRY 001 所記之 `4528b937…`），
        內容仍為 34a 之 23 條但**已經 Excel 開啟並重存**。
        **複製與處置屬 Pei**；本層未動。
      - 交付路徑 `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/
        00_TestCase/ASW-R2/Display/`
      - 交付檔名 `…_SWQT_Display_20260826.xlsx`（與 Privacy 之
        `…_SWQT_Privacy_20260813.xlsx` 命名一致）
      - 交付副本 SHA256 `4528b937…` 與 repo `output/` 副本
        **逐位元相同**（`cmp` 實測）；台帳兩行皆 `OK`
      - `DELIVERY.sha256` **ENTRY 001** 已建；其第二行指向交付副本本身
      - **來源母本 sha `6372fb6be02f48dc…` 未變** —— 未就地覆寫，
        `reference:` 綁定維持 13/13
      - **未完成者**：Excel 實開確認（無「修復」提示、R／P／AE 下拉可用、
        分頁數 9）；`fw036-display-v1` tag；RD-1
      - **交付包必附未結 DR 11 筆**（見 `docs/upstream/34_closeout.md` §五）
      - **覆蓋為 7/8 leaf 且全部部分覆蓋** —— `SWE1-DM-006` 未覆蓋。
        交付時不得表述為「八條全覆蓋」
- Open PENDING rulings: ____
