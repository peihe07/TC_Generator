# PLAYBOOK — SW Update (FW036 TC Generation)

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
- Profile: `docs/runtime/profiles/FW036_R1L_SWUpdate_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-SUnn]` marker +
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

> 讀 `SW UpdateHMI/PLAYBOOK.md`、`SW UpdateHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`SW UpdateHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — SW Update

- [x] P0 intake complete; INTAKE.md reviewed; missing files: **無**（六份素材 + 036 母本 + Pop Up List 全在場）
- [x] P1 recon complete; workbook_state: **BLANK**; leaves: **307**; targets: **307**
- [ ] P2 DECISIONS signed (date: ____)
- [ ] P3 framework Part N + profile approved
- [ ] P4 data artifacts built
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING rulings: **無**（A-SU1／A-SU2／A-SU3 皆 RESOLVED）
- 驗證母體（R-SU3）: **311** = FR 307 + NFR 4；錨點池（R-SU7 v2）: **574**

## 7. 操作慣例（建議，非條文）

> 本節為實際發生過之錯所留下的教訓，逐則記其出處。
> **違反不構成停止條件**，但照做可省一輪。

**(1) 分類型產出，每一類都要有一路獨立計數 —— 不能只驗最好驗的那類。**

出處：上繳包 02 §六（自評 #1），T10／T12 案例。

T10 對 CFTS_57 之 7 位 id 做四分類（章節／需求／Description／不可歸類），
交付時只做了一路交叉驗證：「章節物件 87 = TOC PAGEREF 87」。
該路只守章節物件 —— 對「需求物件」與「不可歸類」之邊界完全無獨立覆核。

缺陷因此存活：分類採「首見為準」，而 11 個帶 `[Artifact Type:…]` 宣告之
id 在文件中**先以內文 `Requirement ID {id}` 形態出現**，宣告排在後方，
遂被誤歸「不可歸類」。錨點池因而少了 9 個（565 而非 574）。

錯數之所以被抓到，是因為下一包（T12）從 **Description 側**重數一次而對不上
（137 ≠ 135）—— 屬僥倖，不屬設計。若 R-SU7 未恰好要求 Description 對照，
565 會一路帶進 Phase 2/3 之錨定。

**作法**：分類產出交付前，對每一類各找一路與分類邏輯**不同源**的計數
（如：宣告數 vs 文序走訪數、正向分類 vs 反向對照），並令各類之和
閉合到母體總數。本例修正後之閉合式為 `87 + 487 + 137 + 10 = 721`
= 裸命中 unique 總數。

**(2) 閉合檢查閉合的是它量的那個東西 —— 檢查通過不代表量對了東西。**

出處：上繳包 06 §3.1（T20a 之 487 空字串案）；本輪 A-SU4 為同族之再現。

T20a 抽取 487 個 CFTS 需求物件之全文，閉合檢查為 `487 = 487` ——
**通過了**。但該式閉合的是 **id 數**，不是**文字**：初版之切法取錯段落，
487 個全文**皆為空字串**，閉合照樣通過。若當時續跑，每列得分 0，
而 0 分不會讓任何檢查 FAIL —— 一份全零的錨表會看起來像一份錨表。

同族之再現（A-SU4）：修好空字串後，`487 = 487` 仍通過，
而 14 個物件之文字吞併了 43 個不屬於它們的 Description（佔全部文字 19.5%）。
**兩次都是閉合檢查通過、量錯了東西**；兩次都由**分布**（長度中位數、極值）
而非由閉合式察覺。

**作法**：對「抽出內容」之產出，閉合檢查至少要有一式**針對內容本身**
—— 長度分布（中位數／極值／零值計數）、抽樣目視、或內容之結構不變量
（如「不得含下一個物件之宣告」）。只數個數的閉合式必須明白寫出
「本式閉合的是個數，不是內容」。

**(3) 發現更強之探針時，增設而不取代 —— 探針之效力由裁定者定。**

出處：上繳包 06 §3、§2.3。

R-SU13 之自我檢定指定了三個「已知標的探針」，全部 FAIL。執行層另找到
證據更強之探針（037 自己寫出的對應，2/2 PASS）。換掉指定探針即可全過、
跑完全母體、交出一份漂亮的完成品 —— **而指定探針的 0/3 仍然是真的，
只是不會出現在報告裡**。

執行層增設而未取代，並自陳「沒發生是因為下放包指定了探針，不是因為我謹慎」。

**作法**：自我檢定之探針由裁定者指定；執行層發現更強者一律**增設並回報**，
不得替換。當強弱探針結論相反時，**停下來讓裁定者裁**，不由執行層決定
哪個探針算數 —— 那正是這條規則要防的事。

**(4) 候選產生器與裁決器是兩件事 —— 召回 100% 與首選正確 82% 可以同時為真。**

出處：下放包 09 §3.1（17 列人裁地面真值）；上繳包 08 §4（四規則回測）。

同一個 TF-IDF 管線，在 17 列地面真值上：**正解落於前 5 候選 17/17（100%）**，
但**首選即完整正解僅 12/17（71%）**、首選之章正確 14/17（82%）。
**它是個近乎無漏的候選產生器，同時是個會錯兩成的裁決器。**

若只看首選正確率，會結論「這條路不通」而換工具；若只看召回，
會結論「這條路很好」而直接取首選定錨。**兩個結論都錯。**
正確的用法是兩階段：管線產候選（用其高召回），裁決另設（不用其低精度）。

**作法**：評估一條檢索／比對管線時，**召回與精度必須分開報**，
且要明說它將被當成產生器還是裁決器。只報一個數字的評估，
無論那個數字多好看，都不足以決定該管線怎麼用。

**(5) 閉合式必須拆到被裁定的那個維度上。**

出處：上繳包 08 §2.1（A-SU5）。

T12 產出 137 個 Description 之**歸屬**（誰屬於誰），其閉合檢查為
`137 = 137`。**該式對「歸屬給了誰」完全不敏感** —— 把兩個 Description
歸錯宿主，總數仍然是 137，檢查照樣通過。錯誤存活了兩包，
直到 T22a 把「歸需求 43 / 歸章節 94」拆開單列才顯形。

這是 §7(2) 的第三次再現，而三次量錯的東西各不相同：
**文字**（487 個空字串）→ **邊界**（吞併 43 個 Description）→ **歸屬**（誤歸 2 個）。
每次的閉合式都通過了，每次通過的都是別的維度。

**作法**：問「這份產出被裁定的是哪個維度？」——是分類就拆到每一類，
是歸屬就拆到每個宿主群，是文字就驗長度分布。**總數閉合永遠是最弱的一式**，
它只能證明沒漏沒重，不能證明分對了。

**(6) 指標之選擇本身即可掩蓋問題。**

出處：上繳包 08 §9.3（`313` 之召回 vs 涵蓋率）。

同一列 `SWE1-FOTA-313`（正解 6 個物件）：
- 以**召回**（至少一個正解在候選內）衡量 → **PASS**（命中 1/6）
- 以**涵蓋率**（全部正解都在候選內）衡量 → **FAIL**

若報告只列召回 17/17（100%），那個「6 個正解只找到 1 個」的結構性盲區
**不會出現在報告裡** —— 不是被隱瞞，是被指標本身濾掉了。

**作法**：選指標前先問「這個指標對哪種失敗不敏感？」。
一對多的任務至少要同時報**召回**與**涵蓋率**；有層級的任務要同時報
細粒度與粗粒度的準確率。**只報一個指標時，須明寫它看不見什麼。**

**(7) 證明「零是真的零」與報「零」是兩件事。**

出處：上繳包 09 §2.4（統攝語形之式B／式C／式D 皆 0 命中）。

六式語形掃描中三式得 0。報「0 命中」是誠實的，但**讀者無從分辨那是
「語料真的沒有」還是「regex 寫得太嚴」** —— 而這兩件事對後續的意義完全相反：
前者是有效的否定結果，後者是掃描失效。

作法是**反向探測**：用更寬鬆的裸字串再掃一次（`listed`、`as follows`、
`section`、`table`、`refer to`、`see`），全部 0 —— 於是那三式的零被證明是真的零。
同一次探測也揭出了六式**確實會漏**的兩條路徑（語序倒置、計數門檻），
那才是該報的缺陷。

**關鍵是探測時不改原式** —— 改式即為看著結果轉旋鈕；漏網另列，
讓裁定者決定要不要補式。

**作法**：任何「未發現」「無命中」「無異常」之結論，都要附一路
**比原方法更寬鬆**的探測，證明該否定不是方法失效造成的。
只報零，等於把「沒有」與「沒看見」混為一談。
