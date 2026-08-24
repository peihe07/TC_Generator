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

**主線 CFTS044 已收尾（60 輪）。** 更新於 2026-08-24，W-175（90 包）。
VF230 線之狀態不在本節範圍 —— 見 `CROSSLINE.md`。

- [x] P0 intake complete; INTAKE.md reviewed; missing files: none (INPUTS.sha256 recorded)
- [x] P1 recon complete; workbook_state: BLANK; leaves: 271 (237 Functional); targets: 237
- [x] P2 DECISIONS signed (date: 2026-08-20)
- [x] P3 framework Part N + profile approved — framework **locked 2026-08-22** (P19, signed 2026-08-20); profile `FW036_R1L_VehicleSetting_Profile.md` created round 18
- [x] P4 data artifacts built — `leaves.tsv` / `leaf_to_reqid.tsv` / `lid_pairs.tsv` / `spec_variables.tsv` (+ `normalized_key`, `suspect_prefix`) / `can_signal_map.tsv` / `delegation_lookup.tsv`
- [x] **P5 pilot #1–#6 全數 PASS**：
  - pilot **#1** PASS（Pei 2026-08-22，**8** 條）—— 3 項 defect 修畢
  - pilot **#2** PASS（**15** 條）
  - pilot **#3＋#4** 不通過 → **七項 defect 修畢後 PASS**（**28** 條）
  - pilot **#5＋#6** 不通過 → **五項 defect 修畢後 PASS**（**18** 條）
  - **累計 69 條經人工關卡（225 之 31%）**
- [x] **P6 全批生成完畢；機械檢查全綠**：
  - **225 TC 涵蓋 219 leaf**
  - 母體 **237** 之三類：有 TC **219**／`held_out` **7**／`generatable = no` **11**（R-VS76 完整性 **PASS**）
  - §9 十七項 **0**／固定錨點 **20/20 必命中**／五項 defect **0**／R-VS77 八判準 **0**／**L3 全量 225/225 不符 0**
  - placeholders：無整條 PENDING 者（§B-1 = 0）；部分步驟 PENDING 者 25 條，見 `DELIVERY.md` §3
- [x] **P7 dry-run approved**（47 輪，四錨點皆可失敗）：
  - 母本 **`c72b9556…`**（**243 列**，資料列 **10–252**）
  - `DELIVERY.md` **11 節定稿**（**§0 交付物之實際狀態在首**）
  - 附件三份：`writability.tsv`／`REGEN_ORDER.md`／`DATA_REQUESTS.md`
  - RD-1 已送 **5 項**（2026-08-22）
  - **v__ tag: ____；submitted: ____ —— 二者仍空白，其屬 Pei**

### Open DRs — 待送 vs 待覆（D-9；2026-08-24 重列）

**待覆**（已送出 2026-08-22，5 項）

| DR | 送件文項次 | 阻塞 | 影響 | 狀態 |
|---|---|---|---:|---|
| DR-15 | 1 | yes | 11 TC | **待覆** |
| DR-17 | 2 | yes | 14 leaf | **待覆** |
| DR-14′ | 3 | yes | 16 leaf | **待覆** |
| DR-19 | 4 | yes | 5 TC | **待覆**（**併入 DR-21**，R-VS42；原編號保留 R-TM13） |
| DR-20 | 5 | yes | 1 leaf | **待覆**（**併入 DR-23**，R-VS42；搜尋已停止，44 包 §2） |

**待送**

| DR | Urgency | 阻塞 | 影響 | 備註 |
|---|---|---|---:|---|
| DR-15′ | High | yes | — | 取代 DR-15（63 包 §5）；**已送出者以本文補送** |
| DR-18 | Medium | no（確認型） | **20 TC** | 2 bit 狀態訊號無未用碼 —— 無效值之定義 |
| DR-21 | High | yes | **2 TC** | 類別式 B2（R-VS42 改制）；DR-12／DR-19 併入之 |
| DR-23 | Medium | yes | — | 類別式 B1（R-VS42 改制）；搜尋已停止 |
| DR-24′ | — | yes | **49 TC** | 時限（`<Tsend>` 等）之上限值；併入 `<Tdisplay>` |
| DR-25 | Medium | no（確認型） | **44 TC** | 依 R-VS57 由 High 降級 |
| DR-26 | Low | yes | 1 步驟 | 36 輪 W-101(3) 開立 |
| DR-27 | Medium | yes | 4 leaf | 37 輪 W-105 唯一性掃描開立 |
| DR-29 | Low | no | — | 19 個 `SWE-Requirement ID` 缺連字號 |
| DR-30 | Low | no | — | 037 與 035 於 8 列之 Categorization 相左 |

**已撤回**（原文保留 —— R-TM13）

| DR | 撤回之依據條文 |
|---|---|
| **DR-8′** | **R-VS62′**（65 包 §1，42 輪 D-3）—— `VC_VEH_LINE` 取自 PROXI 列 466，其素材缺件之前提消滅 |
| **DR-22′** | **R-VS49**（29 輪 D-4） |
| **DR-25′** | **R-VS66／R-VS67′(d)**（73 包 §1）—— 其標的（訊號不在基線 DBC）依 R-VS66 已非 DR 之事由，而是 issue-to-RD 之事由 |

**⚠ 一項於本次重列時查得**：**`DR-5-B` 無登記條目。**
其為 **39 條 TC** 之 AH 所載之阻塞標的（畫面層之樣式與內容待 TLM HMI Document），
出處為 **`docs/handoff/05_rulings.md`**，而 **`DATA_REQUESTS.md` 內僅一次提及、無 `## DR-5` 之條目**。
`DR-5`／`DR-7`／`DR-11` 同 —— 三者於該檔皆無條目。**具名，不補**（本輪禁區禁補素材）。

- Open PENDING rulings: none — R-VS19″ / R-VS41 / P19 皆已裁；`A-VS02` 為缺號，不補不重編

### 交付物之已知限制（自 `DELIVERY.md` §0 逐字取，四項）

1. **R 欄無選單；P 欄與 T–Z 欄自第 133 列起無選單**
   —— 修復範圍 **`R10:R252`／`P10:P252`／`T10:Z252`**（**A-VS153 未關閉**；
   驗收判準見 `docs/reports/x14_fix_prep.md` §4）
2. **11 批 80 條之首版不可重放**，其變更鏈**經實跑證實缺一層**
   （A-VS162／163／164；其可稽核範圍為「自凍結點起之變更」，非「自需求起之產出」）
3. **156 條（69%）未經人工覆核**
4. **就地改動實為 5 commit／26 檔次／24 檔，含實質欄位**
   （`test_procedure` 10／`pre_conditions` 10／`expected_result` 9）

> 上開四項**不因「八項回掃全數 0」而消失** ——
> 那八項驗的是條文一致性，不是這四件事。

### 未結之作業（供接手者判）

**⚠ 本節與 90 包 §2 所令之文字不同，其差具名如下。**

90 包令記「**60 輪之 W-172／W-173／W-174 未執行**；其中 W-172(2)
（`70b75d0` 之 15 檔次其下放包依據未查）有實質 —— 若無依據，即為
無授權之變更落在已交付之產物內」。

**實測：該三項已於 60 輪執行完畢並入庫**（commit `1670756`，
上繳 `docs/upstream/53_inplace_audit.md`）。**其結果為**：

| 項 | 結果 |
|---|---|
| **W-172** | **26 檔次逐一皆有下放包依據，無依據者 0**。`70b75d0` 之 15 檔次**並非值之改動而是欄位之新增**（前版無 `screen_pending` 欄），其依 **68 包 D-4** 逐字「`generated/` 各批次**增** `screen_pending` 欄」所令 —— **即 R-VS80「下放包之措辭亦受本條拘束」之實證**。**「無授權之變更落在已交付產物內」一事不成立。** |
| **W-173** | **R-VS81 已實作**（`scripts/versioned_out.py`），錨點兩側皆有標的（現行最大版號為目標 → raise；`_v{n+1}` → 成功；**內容相同者仍 raise**）。已接入 `earlyfix_w157.py`／`rvs6_restore_w160.py` |
| **W-174** | 鏈重建**新增 7 層**（門檻 10，未逾）。另查得 **A-VS165**：`REGEN_ORDER.md` 之「鏈長最長者」句與其表格**差恆為 1，自 58 輪起** —— 90 包所據之數即受其影響 |

**本層之處置**：狀態板為接手者之基準（90 包 §1 逐字：「不更新即收尾者，
下次接手會以錯誤之基準往下做」），**故不錄入一個實測為假之陳述**；
兩者並列於此，其取捨屬分析層。

**真正未結者，三項**：

| # | 事項 | 歸屬 |
|---|---|---|
| 1 | **下拉之修復**（`R10:R252`／`P10:P252`／`T10:Z252`）—— A-VS153 未關閉 | **Pei** |
| 2 | **`impl_gap` 56 條開 issue 予 RD**（R-VS66(a)） | **Pei** |
| 3 | `record_rewrite_w95.py`／`priority_and_style_w101.py`／`pilot_fix_w130.py` **三支歷史腳本未接 R-VS81** —— 其輸出為明列之對映表，改之須動 `generated/` | **分析層裁** |

**另二項待分析層更正**（上繳 53 §2.1／§5）：
A-VS163 之歸屬（那 18 檔次為照令執行，非本層之工程缺陷）與其數
（165 條中 133 為新增、26＋6 為重標）。

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

---

## driver 後置步驟（R-VF20 第 4 項，2026-08-23）

`writability.tsv`／`generatable.tsv` 由 `scripts/writability_driver.py --write`
產生，而 **R-VF17 之 4 leaf 之分級不在 driver 之判定內** ——
其值域來源為 037 之 `Verification Method` 欄，而 driver 之 `value_sourced()`
不認該欄（**刻意不改**：改之即對全部 leaf 重評，違反 R-VF14 第 4 項）。

**故 driver 每次 `--write` 後必跑 `python3 scripts/grade_overrides.py --apply`。**
詳見 `RUNBOOK.md` 之「分級覆寫層」。

驗證：`python3 scripts/grade_overrides.py --check`，不符即 `exit 1`。

---

## `接手` 之讀取清單（R-VF38 二，2026-08-23）

`<Feature>, 接手` 時之讀取順序：

1. **`CROSSLINE.md`** ← 跨線拘束項，**最先讀**
2. `PLAYBOOK.md` §6 狀態板
3. `docs/INDEX.md`

**兩線皆適用**（本條非 VF230 線專用）。

理由（A-VF8／A-VF9）：兩線共用 `features/vehicle_setting/` 之全部工具與資料檔，
而一線之裁定從無機制送達另一線 —— 已致 R-VF17 被一次例行 driver 重跑抹除
並進入 git 歷史。

