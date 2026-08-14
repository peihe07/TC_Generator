# 上繳包 04 — framework Part VI、DECISIONS 簽核、profile 草案

執行層 → 分析層。2026-08-13。回應 `docs/handoff/04_framework.md` §5 之六項要求。

**四項停手條件全部未觸發**：framework 無既存 Part VI、`DECISIONS.md` Sign-off
區塊為空、R25 編號未占用、SXM profile 各 `[OVERRIDE]` 條款在 Privacy 情境下
皆有對應通則可取代（逐條處置見 §4 之 profile §7 對照表）。

---

## 1. §5.1 —— §3 六項完成狀態

| # | 作業 | 狀態 | 備註 |
|---|---|---|---|
| 1 | R25 貼入 `RULINGS.md` | ✅ | 編號未占用；附 R25-3 之取代說明 |
| 2 | Part VI append + 首句加列 | ✅ | 見 §2 |
| 3 | `DECISIONS.md` Sign-off 填入 | ✅ | Pei / 2026-08-13 / R25-2；§8 一字未改 |
| 4 | 建 `inputs/BASELINE.sha256` | ⏭ **跳過** | 已由 **R26-2** 取代，見 §1.1 |
| 5 | `PLAYBOOK.md` §6 勾 P2、P3 標註 | ✅ | 見 §5 |
| 6 | 起草 Privacy profile | ✅ | 草案全文見 §4，**待 chat 核可** |

### 1.1 第 4 項之處置（依 Pei 指示跳過）

R25-3 原文要求建立 **`features/privacy/inputs/BASELINE.sha256`**（於 `inputs/`
之下）。Pei 於本包下放後另行裁示落點改為 **feature 根**
（`features/privacy/BASELINE.sha256`），並增設 append-only 的
`DELIVERY.sha256`。兩檔已於同日建立並納入版控。

R25-3 要求之四項內容（檔名 / SHA256 / 命中之客戶樹路徑 / 稽核日期）
在新落點皆有著落：前二項逐行記於檔內，後二項記於檔頭。
**落點差異為 Pei 明示，非執行層自裁**；已於 `RULINGS.md` R25 條後註明。

順帶一提：若照原路徑建於 `inputs/` 之下，會踩到停手條件 2 ——
`features/privacy/.gitignore:2` 的 `inputs/` 會把它整個排除掉，檔案根本進不了
版控。新落點無此問題（已以 `git check-ignore` 確認）。

---

## 2. §5.2 —— framework.md 行數與 Part VI 起訖

| 項目 | 值 |
|---|---|
| append 前行數 | 1,051 |
| append 後行數 | **1,204** |
| Part VI 標題行 | **1055** |
| Part VI 內文起訖 | **1055 – 1204**（檔末）|

首句更新（**修正過一次**，見 §6.2）：

```
Covers Test Groups **Media** (Part I, below), **Home** (Part II), **AMFM**
(Part III), **SXM** (Part IV), and **Privacy** (Part VI, end of file). The
cross-cutting rulings in Part I (...) apply to ALL Test Groups.
```

**一項既有缺漏，未自行修正**：該首句原本就沒有列 **Part V（Projection）**，
現在也沒有。本包只授權「加列 Privacy」，故未順手補 Projection ——
但 `## Part V — Projection` 確實存在於行 553。回報待裁。

---

## 3. §5.3 —— `BASELINE.sha256` 全文

```
# BASELINE — features/privacy/inputs/ 客戶素材基準
#
# 為什麼存在：inputs/ 是 gitignored（.gitignore:2），素材本身永遠不進版控。
# 2026-08-13 實測，amfm / home / media / projection 四個 feature 的 inputs/
# 已全部清空、sxm 只剩 2 檔（原 15）、repo 根 output/ 整個不見 —— 而
# git 無從還原，因為那些檔從未被追蹤。tag 還在，指向的產物卻已不存在。
#
# 這份清單是那件事之後留下的防線：素材可以消失，雜湊留在版控裡。
# 任何一個檔被換掉、被覆寫、被「重新下載一份新版」，都會在 git diff 現形。
#
# 驗證（自 features/privacy/ 執行）：
#     shasum -a 256 -c BASELINE.sha256
# macOS 的 shasum 會對本註解區塊印 "WARNING: N lines are improperly
# formatted"，那是 perl 版的行為，exit code 仍為 0，逐檔仍印 OK。
# GNU coreutils 的 sha256sum 會靜默略過 # 開頭的行。
#
# 更新時機：素材有增減或經裁決換版時，連同裁決編號一併更新本檔。
# 未經裁決而此檔需要更新 —— 那本身就是要回報的事。
#
# 基準確認：下放包 01 §2（2026-08-13）。8 檔全數 MATCH
# /Users/peihe/Work/02_Project_R1LR/ 樹內同名候選。
# R22-1 時態限縮：MATCH 是現在式陳述，不蘊含「從未被覆寫」。
#
# 已知未決：V6_R2 之副本對齊 DT28 樹而非 HDCC28（A-PV14）。本檔記錄的是
# inputs/ 現有的那一份，不預判它是否為正確平台版本。
c54f700f81c4c70e52b9ccf460a143b341471163c7b6d5e1d5f0b9f00637aa0f  inputs/Audio_Output_Management_-_ETM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V3_R3.docx
49dd3c31405fb0c34d4cf11048d325d6f047c0d333c10248310e72c57e194fbb  inputs/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx
d5813bb7ccd6f721949c166c60727448193cbbff920d539b79639ebb31461cae  inputs/Audio_Output_Management_-_LTM_Non-Amplified_Audio_System_(Base_Audio)_VF651_V2_R2.docx
f46d15ca29b6a75d689a1e331a92d2e1286ebe549668936dfe2eec31839c2854  inputs/CFTS022_Privacy_mode-FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA.xlsx
cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d  inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx
5eb0dd739f002fe04e4891ceb9fd7d233b4e128a8b35eadce8ad6a631854dd78  inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx
190e6f3ebaee5fe7ccc5a79014278777a179730409c9a215e77926f200c8a7fe  inputs/SWE1_CFTS_022-Privacy_Features.xlsx
e534afa55710547f6fc53de21de3c1830073bf17f162e835668b153c3a93158c  inputs/SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx
```

驗證：`shasum -a 256 -c BASELINE.sha256` → **8 OK，exit 0，零警告**。

---

## 4. §5.4 —— profile 草案全文（供 chat 核可）

落點：`docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`
（檔頭已標 **DRAFT，awaiting chat approval**，核可前不生效、B1 不啟動）

起草方式與一項刻意的取捨：以 SXM profile 為體例來源（同為 BLANK + rev C
範本），但**結構條款繼承、內容條款不繼承**。SXM 的七個 delta 全部逐條重新
判斷，未逐條再導的一律標明「not inherited」及其理由 —— profile §7 有完整
對照表。這是為了避免 A-026 型的錯誤：跨 feature 範例借形式，literal 一律回溯
本 feature 的 spec。

停手條件 4 之逐條確認：SXM 各 `[OVERRIDE]` 條款在 Privacy 情境下**皆有**
對應通則可取代（§2 取代 free-form labels、§3.1 取代 §4.3、§3.3 取代 §12、
§3.5 取代 §10.7），**無任何一條落空**，故該停手條件未觸發。

```markdown
# Project Profile — FW036 / R1L SWE1 Privacy (CFTS022 Privacy Mode, Stellantis newR1L)

> **DRAFT — 2026-08-13, awaiting chat approval (下放包 04 §3.6).**
> Not in force until approved. B1 generation does not start before that.

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.
>
> Instantiated from `FW036_R1L_SXM_Profile.md` — the nearest sibling, because
> both are BLANK workbooks on the same FM-WI-FSM-036-A01 revision C template.
> **Structural clauses are inherited; content clauses are not.** SXM and
> Privacy share no spec document and no 037 family, so every SXM delta was
> re-derived rather than carried over. Where a clause below has no SXM
> counterpart, §7 says so explicitly.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope 037-A03 Privacy, **10 leaves**
  `SWE1-HMI-PRIVACY_FEATURES-001…010` (version C, approved 2026-02-09)
- Deliverable workbook: FM-WI-FSM-036-A01 **generic blank template**
  `SWQT_20260121`, SHA256 `cd876c202c71e74b…`. There is no Privacy-specific
  workbook and none will be requested — **A-PV01 / R23-1** ruled that producing
  the deliverable from the generic template *is* the final form.
- **Workbook is BLANK** — no legacy region, no done region, no frozen rows.
  Style authority is the fallback chain (canon §2), not a local precedent.
- **Form revision C**, same layout as SXM (A-SX05 precedent): `Estimated Test
  Time` at **Q** shifts design_method → **R**, functional_safety → **S**,
  author → **AA**, remarks → **AH**. Data sheet is `Test Case Specification
  測試用例規範` (no `&Result` suffix).
- `Test Case Framework` sheet: **absent** — the template ships 9 sheets
  (`Cover_old`, `ChangeHistory_old`, `Cover 封面`, `ChangeHistory 修訂履歷`,
  `Product Document 記錄封面頁`, `Test Case Specification 測試用例規範`,
  `Reference`, `QS Suggestion`, `下拉選單`). Verified 2026-08-13. The three Set
  names therefore live in the per-row columns only (framework Part VI,
  Workbook sync) — same outcome as SXM, reached by measuring this instance.
- Author on new rows: `PeiPYHsu`. TC id series: **`NR1L-Privacy-{NNN}`**
  from 001 (R-PV02 — full feature name, mixed case, per the template's own
  sample row `NR1L-AntiTheft-001`; **not** the three-letter form SXM uses).

### 0.1 Template preparation state [ADD]

The template shipped with two residual sample rows. Cleared 2026-08-13 under
**R23-4**, via `backend/xlsx_surgical.py`:

- five cells cleared — D10 / F10 / G10 / S10 / D11 — with their `s=` style
  attributes preserved in place
- **column B untouched**: B10 is the formula `=IF(ISBLANK($D10),"",ROW()-9)`,
  so the row number follows column D automatically. Clearing B would have
  deleted the template's numbering mechanism
- whole-row deletion was rejected: it shifts the DV `sqref` ranges and R10's
  x14 dropdown

First generated TC lands on **row 10**. Prepared workbook and its provenance
are recorded in `features/privacy/DELIVERY.sha256` (ENTRY 001) — **not yet
opened in Excel**, which gates P4 (R17-9-equivalent).

## 1. Requirements authority chain [ADD]

- Chain: CFTS022 artifact (`4915xxx`) → 037-A03 leaf (`SWE1-HMI-PRIVACY_
  FEATURES-nnn`) → FW036 TC.
- **spec_mode D** — clause authority is the CFTS022 docx
  (`R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708`,
  SHA256 `5eb0dd739f00…`).
- **PROF → artifact mapping, offset = −1** (framework Part VI): the 037's
  `Source Requirement ID` is `SYS-RA-PROF-nnn`; the CFTS022 artifact is
  `4915(nnn−1)`. Verified on 8 consecutive leaves (-003…-010).
  **-001 and -002 are NOT yet verified** — confirm at P2 before citing.
- **SYS3 SYSAD is context-only** (A-PV05 / R23-3): background understanding
  only, **never** a `specification_reference` (canon §10.7 bars analysis and
  design documents). Declared as `context_only` in `feature.yaml`.
- SYS2/SYSRA safety layer does **not** enter the trace chain: the ruled 037
  carries no ASIL/FTTI column (recon 2026-08-13; AMFM R6 / SXM precedent).
- **Need list is not derivable from this 037**: its source column holds
  component/Polarion ids, not document citations. Trace runs through the
  architecture and export files instead (intake 2026-08-13).

## 2. Test Set vocabulary [OVERRIDE — replaces the generic free-form labels]

- Test Group = `Privacy` (column G) and the capability Test Set (column H) from
  framework **Part VI**, on every generated row. `fill_test_group_set: true` —
  ruled under BLANK per canon §2.
- The three Sets are the Part VI table: `Input Monitoring`,
  `Personalization Display`, `Speed-Controlled Volume`.
- **Layer 3 = CFTS022 artifact id**, framework-internal, **never written to the
  workbook**.
- `Speed-Controlled Volume` (8 leaves) is deliberately unsplit. Splitting it by
  restore / signal / adjustment would give 5 Sets over 10 leaves — canon
  §4.1.3's "Test Set column becomes a near-copy of the TC ID column"
  anti-pattern. Workload is handled at BATCH level, never by splitting a Set.
- The two single-leaf Sets are **genuine outliers under §4.2**, not accidents:
  -001 and -002 are the only non-SCV requirements in the feature and share
  neither setup nor UI entry point with SCV. Precedent: AMFM
  `Tuner Availability` (2), SXM `Source Availability` (1).

## 3. FW036 Privacy house style (field rules)

### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]

Test Item = condensed requirement statement in spec language (modals permitted
**here only**, quoting requirement text). The generic §4.3 tc_title (no modals)
is still produced in output JSON for lint and sibling distinction. Multiple TCs
per leaf append the distinguishing scenario tag.
§6 unchanged for Expected Result: **no modal verbs, ever**.

*Inherited from SXM §3.1 — structural, applies to any FW036 deliverable.*

### 3.2 Pre-Conditions [ADD — Privacy applicability triggers]

Valid spec-trigger Pre-Conditions (§8.5 exception):

- **Amplifier presence**: `An external amplifier is present on the vehicle` /
  `…is not present…`. This is the feature's central configuration axis — six of
  ten leaves turn on it (see §4) — and it is stated in the clause text, so it
  qualifies as a spec trigger rather than a fabricated setup step.
- **Wake-up source**: `The HU wakes up on Interior CAN` / `The AMP wakes up on
  Interior CAN`, where the clause names it (-003, -008).
- **Sleep-mode exit**: `The HU has exited Sleep Mode` (-001 only).
- `HU is powered on` remains **banned** (generic rule) — it is implied by every
  other trigger and carries no verification value.

### 3.3 Design Method [OVERRIDE — restricts §12 output strings]

Return exactly one of the **9** dropdown strings from the workbook `下拉選單`
sheet, character-for-character.

- **Authority is `下拉選單!A1:A9`** — nine entries. Two template defects are
  recorded and deliberately not worked around:
  - the DV on R11:R59 points at `$A$1:$A$11`, i.e. two blank options, while R10
    points at `$A$1:$A$9` (A-PV10 / R23-6)
  - `Reference!C9` reads `Pair-wise / N-wise` where `下拉選單!A6` reads
    `Pairwise / t-wise` (A-PV11 / R23-7)
  `Reference` is a descriptive appendix and **does not enter lint**. Both
  defects go upstream with RD-1.
- **Boundary/validity rule**: -005 (valid vs invalid `$VolumeSCV$` values) is
  Equivalence Partitioning on both sides of the partition, not Functional.

### 3.4 Signal citations [ADD]

CFTS022 `$SIGNAL$` notation is quoted verbatim in Pre-Condition / Input Test
Data — `$VolumeSCV$`, `<Tsend>`. The profile-scoped §11 exception for
source-quoted tokens applies: square brackets are retained inside quoted signal
values only; author prose still uses `"..."` for UI labels.

*Inherited from SXM §3.4; the token set is Privacy's own.*

### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]

Format: **`CFTS022-{artifact_id}`**, where `{artifact_id}` is the 7-digit
CFTS022 artifact id resolved through the PROF → artifact mapping (§1).

- The id is **looked up, never constructed** — spec_mode D's defining rule.
  The −1 offset is a verified regularity, not a licence to compute an id for a
  leaf whose mapping has not been checked (**-001 / -002 pending**).
- **VF651 external references** carry the platform constraint of §4 below.

**No cite-form mechanism.** SXM needed one (its §3.5 Delta 2) because four of
its leaves cite short-form ids that resolve in no released artefact. Privacy has
no such case: all ten leaves resolve to CFTS022 artifacts directly. If one
appears at P2, it returns to chat — it is **not** inherited by analogy (§7).

### 3.6 Remarks [ADD]

Empty string unless: BLOCKED row, anomaly flag, or documented workaround.

Remarks is **external-facing** (AMFM R10-4): no internal ruling ids, no anomaly
ids (`A-PV…`, `R23-…`). Those belong in `reasoning` / `assumptions`.

No twin-mirror mechanism — SXM's §3.6 Delta 3 exists because eleven of its
leaves are text twins of AMFM clauses. Privacy has no sibling deliverable
sharing a spec document.

### 3.7 Estimated Test Time (column Q) [ADD]

**UNRULED_BLANK**, same as SXM (A-SX05). Revision C's new column has no ruled
fill policy for Privacy either. Left **blank at generation** and reported as a
named blank-by-decision column in the write-back dry-run summary.

Estimating without a source is §8.4-adjacent fabrication; `NA` reads as refusal.
Write-back can fill the column corpus-wide later if an RD-1 answer defines a
rubric.

## 4. Split policy [ADD]

Generic §8.3 applies. Privacy-specific:

**AMP present / not present is a positive/negative pair, never a merge.**
Two pairs exist:

| axis | not present | present |
|---|---|---|
| automatic adjustment | -006 (PROF-172) | -007 (PROF-173) |
| user-initiated change | -009 (PROF-175) | -010 (PROF-176) |

Canon §7 ("an enumerated supported case takes at least one negative TC")
makes each side its own TC. **Merging a pair into one TC with a branching
procedure is forbidden** (§5.2 bars in-procedure branching).

**`Service` / `HMI` is an axis, not a Set boundary** (§8.3). The 037's Sub
Categorization marks -001/-004/-005/-010 as `Service` (signal side) and the
other six as `HMI` (display side). The axis cuts across
`Speed-Controlled Volume` and the labels are classification terms rather than
capability names (§4.2 bars those as Set names). Use it to distinguish siblings
within a Set; never to draw a Set boundary. Precedent: AMFM note 2 (band),
Projection §N.4 (transport axis).

**No absorption mechanism is adopted.** SXM's §4 Delta 5 (R10-2 absorption with
marker `[A-SX08]`) is **not** inherited. Three CFTS022 clauses have no leaf in
this 037 — `4915167` (PROF-168, personalization entry for SCV volume) and
`4915176` / `4915177` (AMP-side compare and store). CFTS022 holds 253
functional requirements while this 037 was allocated 10 leaves, so "no leaf"
most likely means "allocated to another feature's 037". Per canon §8.4.2 and
the asymmetric-error-cost principle, these are **observations, not coverage
gaps**, and **must not be recorded as gaps before P2 verifies allocation**.

## 5. Marker vocabulary [ADD]

Inline in generated JSON `reasoning` / `assumptions`. Prefix is **`A-PV`**, not
the `A-PR` that `new_feature.py` generated from `feature[:2].upper()`
(R-PV02 — the script was deliberately left unchanged).

| marker | meaning | leaves |
|---|---|---|
| `[A-PV14]` | the leaf cites VF651_V6_R2, whose `inputs/` copy comes from the DT28 platform tree rather than HDCC28 — platform version unresolved | -007, -008, -010 (B2 only) |

**One marker only, and it gates a batch rather than annotating a row.** Markers
live in reasoning/assumptions, **never in Remarks** (external-facing, R10-4).

## 6. External references — VF651 platform constraint [ADD]

`specification_reference` entries pointing at VF651 documents take the
**HDCC28** platform version, without exception. This is where Privacy's
substantive risk sits, so the state of each variant is spelled out:

| variant | state |
|---|---|
| `VF651_V2_R2` (LTM Non-Amplified) | `inputs/` copy `d5813bb7…` **confirmed HDCC28 baseline** (A-PV04 / R23-2) — citable |
| `VF651_V6_R2` (LTM/ETM Amplified) | `inputs/` copy `49dd3c31…` measured to come from the **DT28** tree; the HDCC28 copy is `e20ba7a4…`. **Must not be cited until A-PV14 closes** |
| `VF651_V3_R3` (ETM Non-Amplified) | in `inputs/`, **not cited**. Absence from citations must **not** be read as exclusion — A-PV03 / R-PV01(a) is DEFERRED to P2 re-verification |
| `VF651_V9_R3` / `V11_R3` (ANC) | Not requested (A-PV02). If any leaf turns out to touch an ANC configuration, **stop and report** — do not extend scope |

**Same-name files are identified by hash, never by filename** (R15-5). This is
not a precaution here, it is a necessity: seven of the eight `inputs/` files
have same-name candidates with more than one content in the customer tree, and
V6_R2 has **7 candidates across 6 distinct contents**.

## 7. Escalation — what does NOT carry over [ADD]

The SXM profile's seven deltas were derived from SXM's evidence. Only the
structural ones are inherited here; the content ones are explicitly **not**:

| SXM delta | Privacy |
|---|---|
| 1 — `{doc}-{stla_id}` + HYBRID map | **not inherited** — Privacy has no ReqIF; the mapping is the PROF −1 offset (§1) |
| 2 — R11 cite-form for unresolvable short ids | **not inherited** — no such leaf exists here |
| 3 — twin mirror Remarks | **not inherited** — no sibling deliverable shares a spec |
| 4 — `UNRULED_BLANK` column Q | **inherited** (§3.7) — template-level, not feature-level |
| 5 — R10-2 absorption + `[A-SX08]` | **not inherited** (§4) |
| 6 — three stackable markers | **not inherited** — Privacy has one marker (§5) |
| 7 — R8 not auto-inherited | **inherited as a principle** — see below |

**Nothing from another feature's rulings applies here by analogy.** If a
situation arises that an AMFM or SXM ruling would have covered, it returns to
chat for a Privacy ruling. The clauses above are the complete adopted set.

**Additionally binding, from the cross-feature register**
(`features/amfm/RULINGS.md`):

- **R18-3** — `backend/xlsx_surgical.py` is the only write path; the zip-member
  and DV-count invariant aborts (never warns); a violation is canon §0 item 3
  and escalates to Tier 2
- **R20-5** — Privacy's write_back is built on `xlsx_surgical` from the start.
  **The four existing feature `write_back.py` scripts are quarantined and must
  not be used as a starting point.**
- **R15-2** — a ruling whose outcome is postponement is `DEFERRED`, not
  `PENDING`
- **R22-1** — a hash audit is a present-tense statement; "matches" does not
  imply "was never overwritten"

## 8. Known anomalies register [ADD]

`features/privacy/ANOMALIES.md`, A-PV01 … A-PV14.

At Phase 3 draft: **RESOLVED** A-PV01/02(Amplified)/04/05/06/07/08/10/11/12/13,
**CLOSED** A-PV09, **DEFERRED** A-PV02(ANC)/A-PV03,
**PENDING** — **A-PV14 only**.

**A-PV14 blocks B2, not B1.** The batch plan (framework Part VI) puts the five
AMP-dependent leaves in B2 precisely so the pilot is not blocked by an open
item while still covering all three Test Sets.

New findings are registered at the moment they are found, with the citing
leaves named — never after the batch that needs them stalls.

## 9. Baseline and delivery integrity [ADD]

Privacy-specific, and the reason it exists is worth stating: on 2026-08-13 four
features' `inputs/` directories and the repo-root `output/` were found empty,
and git had nothing to restore because both paths are gitignored.

- `features/privacy/BASELINE.sha256` — the 8 source files, **tracked**
- `features/privacy/DELIVERY.sha256` — **append-only** ledger of produced
  workbooks, **tracked**; entries are added, never rewritten
- Verify at every session opener and every batch gate, from
  `features/privacy/`:

  ```bash
  shasum -a 256 -c BASELINE.sha256
  shasum -a 256 -c --ignore-missing DELIVERY.sha256
  ```

  Any `FAILED` stops work. `--ignore-missing` is required on the second: the
  ledger accumulates cleaned-up artefacts, and without it they report
  `FAILED open or read`. Tampering still fails and exits 1.
```

---

## 5. §5.5 —— `PLAYBOOK.md` §6 更新後全文

```markdown
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
- [ ] P3 framework Part N + profile approved —— **framework 已核可**
      （R25-1：Part VI 已 append 至 `docs/fw036/framework.md`，行 1055 起；
      Test Group `Privacy`、三個 Test Set、Layer 3 為 CFTS022 artifact id）；
      **profile 草案已起草待 chat 核可**
      （`docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`）。
      兩者皆核可後方可勾
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
```

**P3 仍不勾**：framework 部分已核可（R25-1），profile 尚待 chat 核可。
兩者皆核可後方可勾 —— 這與 R25-2 所立之體例同型（「部分已成立」不等於
「整項已成立」）。

---

## 6. §5.6 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，六項。**

1. **framework Part VI 之 PROF → artifact 對映，我沒有獨立重驗。**
   §2 草案給的 8 筆對映（-003…-010，offset −1）與「-001/-002 未逐條驗證」
   之註記，都是分析層的實測結果，我照抄進 framework。**執行層未開
   CFTS022 docx 核對任何一筆。** 這與上繳包 00 §7.6 第 1 項是同一件事，
   當時列為「P2 進場前必辦」，至今仍未辦。
   **profile §1 已把「-001/-002 未驗」寫成硬性條件**（引用前須確認），
   但那 8 筆「已驗」的，我也只能轉述。

2. **首句缺 Part V（Projection）未修**（§2）。授權範圍只有 Privacy。

3. **profile 之 §3.2 Pre-Conditions 三組觸發語句是我起草的，無先例可據。**
   `An external amplifier is present on the vehicle` 等措辭取自 037 leaf
   標題與 framework 草案的條文要旨欄，**未回到 CFTS022 docx 核對其原始
   措辭**。§8.5 允許 spec-trigger 作為 Pre-Condition，但前提是那確實是
   spec 說的話。P2 起草 B1 時必須逐句回溯。

4. **`Test Case Framework` 分頁「absent」是實測，但三個 Set 名稱寫哪裡
   之結論是類推。** 我驗了範本 9 個分頁確實沒有該頁（framework 草案 §Workbook
   sync 要求「接線時查證」，已辦）。但「therefore 三個 Set 名稱只存在於逐列
   欄位」是沿用 SXM 的處置，**未驗證 Privacy 是否有別的需求**。

5. **profile 草案本身沒有被任何機制檢查過。** lint 不讀 profile，測試不讀
   profile。它是一份純文字約定，其內部一致性（例如 §5 標記表說 A-PV14 只
   影響 -007/-008/-010，而 §6 說 V6_R2 不得引用）目前只靠人讀。
   若 chat 核可後發現條款互相矛盾，沒有東西會先報錯。

6. **`DELIVERY.sha256` ENTRY 001 所記的工作簿仍未經 Excel 開啟。**
   profile §0.1 與 DELIVERY 檔內都寫了「此項未完成前不得升格為交付件」，
   但它同時也是 **P4 的前置條件** —— 而 B1 生成（下一包）就會開始往那份
   工作簿寫入。**建議在 B1 下放包之前先完成這次開啟確認**，否則會出現
   「往一份未驗證可開啟的檔案寫入 5 筆 TC」的順序問題。
