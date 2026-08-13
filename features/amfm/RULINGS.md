# RULINGS — AMFM intake (pre-scaffold)

## R1 — Requirement source (Pei, 2026-08-09)

**Ruling: 以 037-A03 最新版為主** — the SWE1_AMFM FM-WI-FSM-037-A03 report
(102 leaves, `SWE-RA-RAD-*`, dated 20260323, sources = SYSAD architecture
components) is the authoritative requirement basis for TC generation.

Interpretation on record (to be confirmed at Phase 2 sign-off): "A03" refers
to the 037-A03 STLA 報告 file, not to a newer revision of the SWRA-A02
document lineage (no such file is present).

## Consequences — three collisions this ruling creates

### C1 — Workbook Scope field contradicts the ruling
The workbook Scope reads `FM-WI-SW-RAD-SWRA-A02`. Under R1 that is stale and
must be updated to name the 037-A03 (same defect class as Home A-H26, caught
in the same week — the field is evidently copy-managed by hand).
- Action: Scope correction is part of write-back, exactly as Home A-H26.

### C2 — The done region traces the WRONG requirement family
All 158 existing rows (author Wilson) trace `SWE-RAD-*` — the SWRA-A02
family, not the ruled source. Under R1, for traceability purposes the
workbook is effectively **BLANK against the 037-A03's 102 leaves**: zero
rows trace `SWE-RA-RAD-*`.
- Sub-decision C2a (PENDING, Pei): what happens to Wilson's 158 rows?
  (i) keep as-is (legacy region, frozen, excluded from invariants — the
      Home A-H06 scoping trick at 158-row scale), or
  (ii) remove/replace in the regenerated workbook, or
  (iii) re-map: if SWE-RAD reqs correspond to SWE-RA-RAD reqs, re-trace
      them — but the two sets describe DIFFERENT content (user functions
      vs system behaviors), so a clean mapping is unlikely; any partial
      mapping is RD work, not TC-author work (§8.2).
- Style-authority note: whichever way C2a goes, Wilson's rows remain the
  workbook's only style precedent (Test Group/Set filled, TC IDs assigned,
  req-ref embedded in procedure). Style can be borrowed even if
  traceability is not.

### C3 — The SWRA-A02's 57 leaves lose their coverage claim
If the 037-A03 is the source, the 57 `SWE-RAD-*` leaves (with ASIL/FTTI
columns) are no longer the coverage target of THIS workbook.
- Sub-decision C3a (PENDING, Pei): confirm the 57 leaves need no coverage
  here (superseded / covered elsewhere / retired). If any survive as
  requirements, they need a home — otherwise this ruling silently drops
  safety-annotated requirements, which an assessor will ask about.

## Practical next steps under R1

1. feature.yaml `a03_report` → the 037-A03 file (Scope-arbitration in
   intake.py currently picks SWRA-A02 per the stale Scope; override
   manually until the Scope cell is fixed)
2. Trace chain: SWE-RA-RAD → SYSAD components → SYS3 docx (architecture) +
   CFTS024 doc (upstream). spec_reference format is an open Phase 3 item —
   candidates: SYSAD component id, SYS3 section, or CFTS clause (mode D
   lookup). BT profile §3.6 precedent applies.
3. SYS2 export (Sys-RA ids, CFTS024) is the safety-analysis layer; check at
   recon whether any 037-A03 leaf carries a safety attribute requiring it.
4. Recon needs the AM/FM template adaptation (header/columns by text, the
   intake.py v2 approach) before it can survey this 037.

C2a and C3a block nothing at intake/recon time but MUST be ruled before
write-back strategy is designed — they define what "done region" and
"completeness" even mean for this workbook.

## R2 — Workbook base (Pei, 2026-08-09)

**Ruling: 選項 (a)** — the delivered pre-filled instance
`FM-WI-FSM-036-A01 ..._SWQT_CFTS024_Radio_20260129.xlsx` is the working
base for recon and write-back, now placed in `inputs/`. The blank form
(`..._SWQT_20260121.xlsx`, in `forms/`) was considered as an alternative
bootstrap base and rejected for now; it remains available as the layout
reference. C2a (disposition of Wilson's 158 rows within this instance)
stays PENDING and is unaffected by R2.

## R3 — Authorship principle (Pei, 2026-08-09)

**Ruling (verbatim): 「只要是我產的要打PeiPYHsu，完全引用他人的就留著他人的名字」**
— rows Pei generates carry `PeiPYHsu`; rows fully quoted from another
author keep that author's name. Applied to feature.yaml
(`write_back.author_value`, done_region comment). Under R4(i) the frozen
Wilson rows therefore keep `Wilson`.

A-AM05's two prior corrections signed in the same pass:
`done_region.author_value: Arif → Wilson` (selector semantics per R4),
`columns.remarks: AH → AG` (header text is authority).

## R4 — C2a: Wilson 158 rows (Pei, 2026-08-09)

**Ruling: 選項 (i) — 凍結為 legacy region**，並綁一條 RD-1。

- The 158 `SWE-RAD-*` rows stay in the workbook, frozen, excluded from
  coverage/traceability invariants (Home A-H06 scoping at 158-row scale)
- Style authority survives: borrow style, not traceability (A-AM02 note)
- Re-map (iii) rejected: RD work, not TC-author work (§8.2); would resolve
  at most ~1/3 (A-AM03) with per-pair human confirmation
- Replace (ii) rejected for now: organizational cost not assessable inside
  the pipeline; if RD-1 confirms SWRA-A02 formally superseded, downgrade
  to (ii) later is a pure deletion operation — (i) preserves that option
- RD-1 question (the A-AM04 sharpened form): was the 037-A03 authored
  against an earlier SWRA-A02 revision? Is the contiguous tail
  `SWE-RAD-040`…`-045` deferred or deleted? Is SWRA-A02 formally
  superseded? — recorded in `docs/fw036/RD1_questions_amfm.md`

## R5 — C3a: 18 unrepresented SWRA-A02 rows (Pei, 2026-08-09)

**Ruling: 確認本 workbook 不承擔其覆蓋。**

- Safety exposure measured and bounded: all 57 SWRA-A02 rows are ASIL `QM`
  / FTTI `NA`; R1 drops no ASIL-rated requirement (A-AM04)
- Disposition question merges into the R4 RD-1 (same question, two faces)
- A-AM04 resolution condition: RD-1 reply arrives or delivery deadline,
  whichever first

## R6 — DECISIONS remaining [PROPOSED] (Pei, 2026-08-09)

**Ruling: 照案簽。** Includes: SYS2/SYSRA layer not in trace chain (no
ASIL/FTTI attachment point on ruled leaves); style authority = Wilson rows
(style only); spec_reference `<Spec Filename>_{outline}` pending Phase 3
mode-D refinement; batch plan by spec chapter, pilot = smallest coherent
batch; done-region compliance notes (5) frozen, not fixed.

## R7 — Phase 3 framework rulings (Pei, 2026-08-09)

Verbatim: 「Q1-AMFM Q2 能力制 Q3本來就會有多份，如果需要補上我會補上該份spec
重複就是重複 但要標注起來我會自行判斷」

- **Q1 — Test Group = `AMFM`** (overrides the Wilson `Radio` precedent for
  new rows; legacy rows keep `Radio`, frozen). feature.yaml `test_group`
  already reads `AMFM`.
- **Q2 — Test Set = capability scheme** (framework Part III table), not the
  legacy band scheme (`FM`/`AM`/`USB`). Divergence from legacy recorded in
  the profile.
- **Q3 — multi-spec references are expected.** Cite `CFTS024-{stla_id}` /
  `CFTS011-{stla_id}` / `CFTS004-{stla_id}` per the leaf's source; missing
  spec files (CFTS011, CFTS004) will be supplied by Pei when needed —
  registered A-AM06/A-AM07, no leaf blocked, no RD-1 for the files.
  CFTS004 attribution carries `[ASSUMPTION A-AM07]` until the file confirms.
- **Q4 — duplicates stay duplicates, marked.** 037-internal duplicate STLA
  ids and numbering gaps registered as A-AM08; each leaf still gets its own
  TC (§8.2, no consolidation); disposition of each duplicate pair is Pei's
  per-case call at review.

The R6 spec_reference placeholder (`<Spec Filename>_{outline}`) is hereby
refined by R7-Q3 to the per-source `{doc}-{stla_id}` format.

## R8 — VR trigger path out of scope (Pei, 2026-08-10)

**Ruling (verbatim): 「不進去了」** — the VR Command trigger path is NOT
covered by this workbook. Leaves 003 / 009 / 025 / 027 test the HU HMI
main path only; the CFTS clauses' "or a VR Command" alternative belongs
to the CFTS028 (Voice Recognition) delivery. Each affected TC's
`reasoning` notes the delegation (§8.2.1 pattern). Closes the A-AM09 VR
class. Consistent with the 037's own systematic omission of VR wording
(A-AM09 evidence).

## R9 — Leaf 029 spec_reference correction (Pei, 2026-08-10)

**Ruling: 029 → `CFTS024-4872457`.** Evidence: 029's title is the
verbatim body of clause 4872457 (Direct Number Input; similarity 0.909,
vs 0.036 against its declared 4872451), minus exactly the VR wording the
037 systematically omits. The declared id `(4872451)` is a copy error
(4872451 = ICS tune-down, correctly owned by 028). Consequences:
- spec_reference for 029 = `CFTS024-4872457` (overrides the declared id)
- the 028/029 entry in A-AM08 is NOT a duplicate pair — reclassified as
  an upstream id-tail typo; goes to RD-1 (Q-AM2)
- pipeline: `build_stla_map.py` needs a declared-id override entry for
  029 (Claude Code side) so the map and batch context resolve to 4872457

## R10 — Pilot gate rulings (Pei, 2026-08-10)

**Ruling (verbatim): 「都走你建議的」** — all four pilot-gate points adopt
the recommended dispositions:

1. **Config-gate design method = EP** (001/002 and generalized): leaves
   that pairwise/groupwise cover a configuration parameter's value classes
   are Equivalence Partitioning, not Functional. Applies corpus-wide
   (e.g. 064 dual-tuner, 066 `$ANT_TYP$`, 081–085 market config).
   Profile §3.3 amended.
2. **A-AM10 absorption kept, two hard conditions**: (a) every absorbed
   clause id enters `specification_reference` (dual/multi cite per §10.7)
   — 025-02, 027-02, 029 to be fixed; (b) RD-1 Q-AM3 notifies upstream of
   the full unallocated-clause set. Decision test added to Profile §4:
   unallocated + same spec section + elaborates the leaf's cited clause →
   absorb with `[A-AM10]` marker + multi-cite; otherwise → coverage hole
   in reasoning + RD-1.
3. **Suppression branch = independent TC** (026-02/028-02 confirmed, and
   generalized): an "only if X" clause with reachable ¬X yields its own
   suppression TC (different trigger state; §5.2 forbids in-procedure
   branching; §7/§8.3 independent partial failures). Profile §4 amended.
4. **Remarks: external language only**: signed upstream-correction notes
   are allowed in Remarks, phrased for external readers, never internal
   ruling ids. 029's remark rewritten; 025-02/027-02 remarks superseded by
   the (2a) multi-cite; 026-02/028-02 A-AM09 remarks dropped (the cited
   clause itself carries the wording — nothing to explain externally).
   Profile §3.6 amended.

Review notes (classification: note, not defect): 001 step 5 ER softened to
"the seek executes" (seek stop-on-station detail owned by Seek leaves);
A-AM11 formally registered.

## R11 — Cross-document citations are cite-form, not absorption (Pei, 2026-08-10)

**Ruling (verbatim): 「引用式,不吸收。」** Where a leaf's clause borrows an
outcome from another CFTS (`{See CFTS019-718}` in §1.3.3, reached by
`SWE-RA-RAD-014`), the outcome IS asserted — anchored to the citation, never
adopted as this leaf's own verified behaviour. Three parts:

1. **ER anchored to the reference.** 014's ER states the tone in cite-form:
   `the key press rejection tone is played, as defined by CFTS019-718`.
2. **Multi-cite.** `specification_reference` = `CFTS024-{citing clause}` +
   `CFTS019-718`, own clause first (§10.7 already permits cross-file
   multi-citation; Profile §3.5 `{doc}` set extended to the cited-only
   documents).
3. **Scope boundary.** The cited document's own rule surface is NOT tested —
   which conditions count as "not allowed", the tone's specification — that is
   the Audio Management delivery. 014 verifies only that the outcome occurs in
   the citing clause's scenario.

Distinguished from R10-2 absorption, which takes an unallocated **same-document**
clause into the leaf's coverage and cites its 7-digit anchor. Cite-form claims
no coverage of the cited requirement, so it needs no `[A-AM10]` marker and does
not enter the absorption gate.

Pipeline consequences (Claude Code side, done):
- `lint_tcs.py`: cross-doc tokens are accepted in `specification_reference`
  only for the leaf whose clause writes them (`cross-reference` gate); a cited
  token with no anchoring ER line fails (`cross-reference-anchor`); cite-form
  citations are excluded from the R10-2a absorption count.
- `make_batch_context.py`: each affected leaf carries the R11 instruction.
- A-AM15 closes as RESOLVED-BY-RULE; `clause_citation_overrides` stays
  available but is not needed under cite-form.

## R12 — Browse batch review dispositions (chat tier, 2026-08-10)

Four generator-flagged points, all covered by existing canon; ruled at
chat tier with Pei visibility (override open):

1. **014/015 boundary — keep the carve, no `duplicate_of`.** §8.2.2
   forbids TC-side consolidation of RD-separated leaves; after the carve
   (015 = classification options themselves, 014 = list content &
   ordering) the verification targets no longer overlap, so the
   duplicate_of threshold (same trigger + outcome + verification target)
   is not met. Upstream near-subset overlap added to RD-1 Q-AM2 awareness.
2. **019 sourced from a Description-type artifact — generate.** The
   leaf's own cited clause is the requirement basis (R1); the artifact-
   type hygiene issue is upstream's, noted in Q-AM2.
3. **023 narrow scope confirmed.** Overwrite semantics (confirmation /
   prompt) are spec-silent; not fabricated per §8.4.1/§8.4.2; exclusion
   stays a reasoning note, not an RD-1 item.
4. **021 joins A-AM11.** Monotonic-relation ER per the 026/028 precedent;
   no step-count fabrication.

## R13 — Write-back column conventions (Pei, 2026-08-10)

Two columns the generated rows share with the frozen legacy region, ruled at
the dry-run gate.

**F (Test Case ID) — `newR1L-AMFM-001` upward.** The TC ID is an *author-side*
number, not the customer-side Test Case Reference ID, and canon §10.3 puts its
assignment with the generator; Wilson's 158 ids were author-assigned the same
way. So numbering is legitimate and only the scheme was open. The new rows form
their own `{project}-{abbr}` series because:
- §10.3 asks for monotonicity **within** a series — Radio and AMFM are two
  series, each monotonic, both compliant;
- it aligns with R7-Q1 (Test Group = `AMFM`);
- it stays uncoupled from the R4-frozen region, so if RD-1 later confirms the
  SWRA-A02 family is obsolete and the legacy rows are removed, the AMFM series
  has no hole.
Rejected: continuing `newR1L-Radio-*` (binds new rows to the naming R7-Q1 set
aside, and couples the sequence to the frozen region); leaving F blank (breaks
form completeness, and no downstream party has a better basis to number).

**O (Test Case Reference ID) — `New`, matching the legacy rows.** Case is
style, and style authority is the Wilson region (R6). Condition checked before
applying: the `下拉選單` sheet defines only column Q's nine design methods, and
column O carries no data validation (the sheet's validations are AE10:AE14,
P10:P167, S10:Y229) — so no form vocabulary outranks the legacy value.
`feature.yaml` `tc_ref_id_value` changed `NEW` -> `New`.

Implemented in `write_back.py` (`assign_tc_ids`, collision-guarded against ids
already in the sheet) and `feature.yaml`; both re-verified against the canon §6
checklist in the second dry run.

## R14 — AMFM close-out (Pei, 2026-08-13)

Signed 2026-08-13, Pei replying 「照建議」 to C1–C6 including the revised
C4 per-pair recommendations. Verbatim block below; the heading follows this
file's convention, the block's text is unaltered.

**R-PV02 (bootstrap 下放包 landing point before scaffold) is NOT covered by
this signature** — it carried no recommended option and remains PENDING.

```text
[RULING] R14 — AMFM close-out（Pei 簽署 2026-08-13，回覆「照建議」）

R14-C1  P7 追認
  實態：tag fw036-amfm-regen-v1 存在；output/ 產出檔 171,631 bytes；
        sidecar / tag annotation / shasum -a 256 實測三方逐字元相同：
        da18b5b0ca9ee5794b67a31ddd317b4a23decf9e0e88380a3717f823e45f3f22
        legacy done-region hash（ordered content, columns D..AG,
        158 rows）= 30d9e4c0719a2929；rows 158 preserved / 143 regen
        (0 placeholder) / 301 total；lint PASS - 143 TCs, 102 leaf
        files, 0 findings。
  裁：P7 已執行，追認之。補登 PLAYBOOK §6，數量一律以 bytes 表示。

R14-C2  R8 追認
  裁：R8 stands —— VR 觸發路徑不進本 workbook，003/009/025/027 四葉
      維持現狀。DATA_REQUESTS #4 關列。

R14-C3  DATA_REQUESTS #2b 拆列
  裁：主檔 4874050-…CFTSMV024_CIP_R3_O1965_Excel_Document.xls 標
      「已入 inputs/」關列；其餘 12 件 O 附件（9 件天線 DTC 表 +
      2 件交通圖示表 + 1 件內嵌註記）另立一列，Urgency Low，
      用途註明「audit 舉證用，不阻塞任何批次」。

R14-C4  duplicate_of 三對（依讀取 generated/ 原文後之修訂建議）
  C4-a  087/094 —— 維持雙 TC。
        理由：CFTS011-4942534 列舉 connected / not connected 兩個值類；
        087 驗正常狀態四項資訊完整顯示（Functional），094 驗
        not-connected 值類與換台後頻率欄位跟隨（EP）。屬 §8.3
        negative / value-class 軸，非人造差異。
  C4-b  089/095 —— 維持現況，不動 v1。
        理由：拆分本身合於 §8.2.2（4942540 綁取樣側與更新側兩件事，
        兩者為獨立部分失效），但與 090/096 依 §5.7 併為一條之處理
        不一致；不一致之根因在上游（037 對 MW 配置兩片葉子、對 AM
        與 FM 各一片）。任一側改動皆使已 tag 之 v1 需 re-issue，而
        正確切法取決於上游答覆。改以 RD-1 提問（見 R14-C4-d），
        待答覆後再決定 v2 是否統一三波段深度。
  C4-c  090/096 —— 改分類，非 duplicate_of 議題。
        理由：兩者 duplicate_of 皆為空字串，條款 id 相異
        （AM 4942536 / FM 4942545），分屬不同波段之不同 leaf，
        依 §8.2.1 本不得跨 leaf 合併。TC 側無可裁之事。
        自 PLAYBOOK §6「duplicate_of 逐對裁決」移出，改列 RD-1
        Q-AM2 item 3 之 FYI。A-AM08 residual 收斂為 087/094、
        089/095 兩對。
  C4-d  新增 RD-1 提問，併入 Q-AM2 item 3（條文見 §2.6）。

R14-C5  A-AM11 / A-AM12 / A-AM13 / A-AM14 狀態轉換
  裁：RD-1 送出當日，四條由 PENDING 轉 AWAITING_UPSTREAM；
      resolution condition = 上游回覆到達或交付期限，孰先。
      轉換由 Pei 通知送出後執行，執行層不得自行提前。

R14-C6  RD-1 送出
  裁：docs/fw036/RD1_amfm_submission.md 照現稿送出（加入 C4-d 之
      新增提問後）。送出屬 Tier 3，僅 Pei 執行。
      送前檢查已完成：四項附件齊備
        unallocated_clauses.json  features/amfm/data/（48,963 B）
        stla_id_suspects.json     features/amfm/data/（148 B，內容已驗：
                                  單筆 SWE-RA-RAD-029，declared 4872451
                                  agreement 0.036 → better 4872457
                                  agreement 0.909，即 Q-AM2 item 1 之 extract）
        family-overlap 表          features/amfm/docs/family_overlap.md
        version/hash 表            內嵌於 S2

R14-C7  量測口徑
  裁：檔案大小之陳述一律以 bytes 為單位。KB 之進位基底歧義
      （171,631 bytes = 167.61 KiB 四捨五入 / 167.60 KiB 捨去）
      為本次已發生之口徑差，記入 §5a 量測條件紀律。
```
