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
- [x] P2 DECISIONS signed (date: **2026-08-13**) —— Pei 整份簽核，依據
      **R25-2**。Sign-off 區塊為獨立動作，不因 §8 個別裁決簽署而自動成立
- [x] P3 framework Part N + profile approved —— framework Part VI 已 append
      並經 **B1-GATE-1 更正**（R30-1：-001 → 4914955、-002 → 4915158；
      「offset 恆為 −1」改記為 SCV 區塊之局部規律）；
      profile **已核可**（R28-1，含 07 包 §2 三項修訂；P-4/P-5 由
      R30-3/R30-4 定案並寫入 §3.8/§3.9）
- [x] P4 data artifacts built —— `data/recon.json`（P1 產物）、
      `data/spec_ref_reviewed.json`（R35-7 之語意覆核凍結紀錄，10 葉）；
      `features/privacy/scripts/` 之 `lint_tcs.py` 與 `write_back.py`
- [x] P5 pilot batch **B1**（-001…-005）reviewed;
      verdict: **不整批退回** —— -001…-004 通過，-005 待 ECU 讀法裁定
      （下放包 10）; corrections: **D1** -005 TC2 設計方法與程序不相稱
      （R33-1 改寫）、**D2** 單一步驟綁多動作（-002/-003）、
      **D3** -004 PC 與步驟重複 —— 三項皆已修
- [x] P6 all batches generated; lint **green**;
      placeholders: **1** —— `SWE1-HMI-PRIVACY_FEATURES-008` 之
      BLOCKED 列（`[BLOCKED-ECU]`，R34-3）。
      B1 五葉 6 TC + B2 四葉 4 TC + BLOCKED 1 列 = **11 TC / 10 葉**。
      -008 依 R34-1 之 ECU 歸屬判準排除於驗證範圍，但仍產出一列
- [x] **P7 完成（Pei Excel 實開確認，2026-08-13，七點全過 —— R38-1）**
      tag: ____（建議 `fw036-privacy-v1`，Tier 3 未執行）;
      submitted: ____（Tier 3）; RD-1 sent: ____（#6–#13 八項，Tier 3）
      - 產出 `output/…_Privacy_20260813_regen-v1.xlsx`
      - SHA256（**全長**，R15-4 不截斷）
        `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f`
      - 輸入基準 SHA256
        `ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4`
      - **11 TC / 10 葉**，第 10–20 列；`NR1L-Privacy-001…011` 照序不跳號
        （第 18 列為 -008 之 BLOCKED 列，`NR1L-Privacy-009`）
      - zip 成員 **48 → 48**（零增零減）；classic DV **3+1**；x14 DV **2**；
        差異成員僅 `xl/worksheets/sheet6.xml`
      - 表頭區第 1–9 列逐格未變；其餘 9 分頁逐格相同
      - lint **PASS**（19 gate 全具雙對照）
      - **量測條件（R15-3）**：本次結構驗證以 **zip 成員集合與 DV 計數**
        為據，**非以位元組數**（R37-2 —— 壓縮容器之體積變化不指示內容
        變化方向）。
        bytes 之三段鏈（**R42 歸屬更正**）：
        空白範本 **65,823** → 準備階段（清五格＋填 D5）→ ENTRY 001
        **59,992**（寫回之真正輸入）→ 寫回 append 11 列 → ENTRY 002
        **63,001**。
        主實例為**準備階段**那一對：清五格文字、填一格文字，
        淨內容變化極小而體積少 **5,831** bytes ——
        體積變化與內容變化不成比例。
        跨兩步之 65,823 → 63,001 亦成立（內容增加而體積減少），
        但**不是寫回那一步**；寫回實為 59,992 → 63,001，變大。
      輸出位置 **`features/privacy/output/`**（R26-1，維持 gitignored，
      `.gitignore` 不修改）；身分摘要落於 feature 根之
      `BASELINE.sha256` / `DELIVERY.sha256`（R26-2，兩者皆進版控）。
      每次 `--write` 後於 `DELIVERY.sha256` **追加一個 ENTRY**（R26-3）：
      產出檔名 / SHA256 / bytes / 產製日期 / 對應 tag / lint 結果 /
      zip 成員數。**`feature.yaml` 目前無寫回輸出路徑欄位**
      （R26 執行時停手條件 3 觸發，未自行新增）
- Open PENDING rulings: **0 條**（R38 close-out，2026-08-14）。
  A-PV02（ANC）轉 RESOLVED —— 十葉全數完成且未觸及 ANC 配置，
  條件式停手自始未觸發。
  DEFERRED **6 條**：A-PV03（待 P2 重驗）、A-PV13（記載與實作不一致）、
  A-PV15 / A-PV17 / A-PV18（待 RD-1 回覆）、A-PV16（待測試團隊確認）。
  CLOSED 1 條（A-PV09）。其餘 12 條 RESOLVED。
- **B1 三道前置全部通過**（歷史紀錄）：GATE-1 對映獨立重驗
  （10/10，兩筆經 R30-1 更正）／GATE-2 Excel 實開確認（R29-1，四點全過）／
  GATE-3 欄 S 與車型欄政策（R30-3 填 `NA`、R30-4 留白）
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

  **台帳綠燈不等於產出俱在（R27-1）**：`--ignore-missing` 讓被清掉的舊條目
  靜默略過，所以 `DELIVERY` 驗的是「還在磁碟上的產出有沒有被動過」，
  不是「產出還在不在」。`BASELINE` 不加旗標，故它兩者都驗。

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
