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

## R15 — AMFM close-out 覆核（分析層自裁，追認上繳包 01，2026-08-13）

```text
R15-1  §2.6 落點衝突 —— 執行層判斷正確，追認
  歸因：分析層撰寫缺陷。下放包 01 標題之「item 3 增補」係議題歸屬，
        被誤寫為插入位置；區塊自帶之 5. 才是能產生自洽文件之意圖。
  裁：追認置於 item 5，內文一字未改。附帶：新段縮排三格、item 1–4
      二格，統一為二格（純排版）。
  §5a：議題歸屬與插入位置是兩件事，下放包指定落點時必須分開陳述。

R15-2  已裁而結果為延後之狀態表示 —— 追認，並立為通則
  裁：Open PENDING 之語意為「待裁」，不收容「已裁而結果為延後」。
      已裁但需等外部條件者，一律標
      DEFERRED — <等待對象>（<裁決編號>），並移出 Open PENDING。
      適用全 feature。

R15-3  重測方法 —— 未逾界，但須標明證明範圍
  裁：import 純函式唯讀重算未逾「不重跑」之界；該禁令標的為會改動
      output/ 之寫回執行。無需改以獨立實作重寫。
  量測條件須明載：以相同雜湊定義重算，可證「產出未自產生時漂移」，
      不可證「該雜湊定義正確」。
  §5a：重測之獨立性有層級之分，陳述時必須指明是哪一種。

R15-4  legacy hash 之截斷表示
  裁：v1 已封存，不改 annotation。但 PLAYBOOK §6 P7 段須明載
      30d9e4c0719a2929 為前綴截斷、全長 30d9e4c0719a2929 2ff50123…。
      後續 feature 之 tag annotation 一律載全長。

R15-5  A-AM17（4874049 / 4874050 同名異容）—— 撤回裁決請求
  裁：維持 anomaly 登記即可，不另立 RD-1 條目、不重開 #2b。
      下次送 RD-1 時順帶提出。
  併入 §5a：**同名檔一律以 hash 認定**。分析層先前對本例與 V2_R2
      所留之「可能只是重存」餘地，已被 hash 證否（V2_R2 七路徑五內容），
      該類措辭不得再用。
```

## R16 — 交付件結構完整性（Pei, 2026-08-13）— 凍結令

```text
證據（分析層 zip 層實測，AMFM）：
  客戶原件  136,004 B / 59 zip members
  已交付檔  171,631 B / 48 zip members   （tag fw036-amfm-regen-v1）
  x14 dataValidation（sheet6）: 6 → 0

R16-1  AMFM v1 停止送出；以修正後之 writer 重產 v2 再交。
       tag fw036-amfm-regen-v1 保留為歷史，不刪不改；v2 另立新 tag。
       RD-1 送出不受此凍結影響，時點由 Pei 決定。
R16-2  全 repo 寫回凍結，至 writer 改為 zip 層外科手術並通過探針驗證。
       解除條件：§3.1 完成且 §3.2 之新 invariant 上線。
R16-3  Home 與 SXM 之已交付件比照 AMFM 做 zip 層比對。
R16-4  升為 canon 條文（FEATURE_ONBOARDING P7 交付段）。
R16-5  §5a：**lint green 與內容 hash 相符，證明不了交付件結構完整。**
       前者量列內容，後者量 zip 結構，兩者正交。
```

### 執行層回報之證據修正（2026-08-13，下放包 02 §3.1 實測）

R16 證據區塊之「x14 dataValidation（sheet6）: 6 → 0」**數字不符實測**。
以 `features/privacy/scripts/xlsx_roundtrip_probe.py` 對客戶原件量測：

| 量法 | 實測值 |
|---|---|
| `<x14:dataValidation>` 元素數（sheet6）| **2** |
| `<xm:sqref>` 群組數 | 2 |
| sqref 內之 range 總數 | 7（`Q156 Q147 Q10:Q95` 3 + `Q223:Q242 Q148:Q155 Q96:Q146 Q157:Q205` 4）|
| classic `<dataValidation>`（sheet6）| 3 |
| classic `<dataValidation>`（全簿）| 4 |

「6」對不上任一量法。最接近之組合為 2 (x14) + 4 (classic 全簿) = 6，
疑為兩類 DV 相加而標為 x14。**裁決結論（x14 → 0、交付件結構受損）不受影響**
——該結論由 21 lost / 10 added 之成員清單獨立成立，已逐項複現無誤。
依 R14-C7 量測口徑紀律與 §4.3 不得自行調和之原則，照實回報，未修改原文。

## R17 — R16 執行覆核（分析層自裁，2026-08-13；補登於同日，依 R19-2）

**補登說明**：本條文於 2026-08-13 簽署（下放包 03 §1），
但該包之作業清單未含「貼入 `RULINGS.md`」一項且未產生上繳包，
四條規則因此在生效卻未登記。依 **R19-2** 補登，**條文逐字照錄，未改一字**。
原簽署日同為 2026-08-13；依 charter「A ruling not written to the repo did
not happen —— 雙向適用」，補登前不具形式效力，補登後追溯自該日生效。

**執行層附註（不影響條文）**：下放包 03 之權限標示寫
「§1（R17-1 ~ R17-3）為分析層自裁」，但 §1 之區塊實際含 **R17-4**，
且 §5 自檢表將 R17-1 ~ R17-4 四條同列為已簽署。
本次依 R19-2 之指示「條文逐字取自 03 §1」補登整個 §1 區塊，即含 R17-4。
標示與內容之落差照實回報，未自行裁定何者為準。

```text
[RULING] R17 — R16 執行覆核（分析層自裁部分，2026-08-13）

R17-1  §4.4 停手範圍之解讀 —— 執行層正確，追認
  事實：R16 下放包 §4.4 寫「3.4 發現 Home 受損 → 回報後停手，
        重產與否由 Pei 裁」。執行層讀為「停 Home 之重產動作」，
        續行 §3.5 登記與 §3.6 草案，未動 Home 任何一列、未跑 --write。
  裁：追認。§3.5/§3.6 為回報之載體且不動交付件，續行正確。
  歸因：**分析層條文缺陷** —— 「停手」未標明標的。
  立為通則：**停手條件之條文必須明列停手標的**，格式為
        「停止 <具體動作>，續行 <具體動作>」。僅寫「停手」者，
        執行層得依最小停止範圍解讀，且該解讀優先。

R17-2  R16 證據數字更正 —— 執行層發現正確，根因已定位
  事實：R16 §2 寫「x14 dataValidation（sheet6）: 6 → 0」。
        執行層實測 x14 元素 2、sqref 群組 2、range 總數 7、
        classic(sheet6) 3、classic(全簿) 4，指出 6 對不上任一量法，
        推測為「兩類相加誤標」。
  根因（分析層複現，非執行層之推測）：
        分析層原始量法為 t.count("x14:dataValidation")，
        **無詞界之子字串計數**。實測拆解 A.xlsx sheet6：
          <x14:dataValidation 開始標籤      2
          </x14:dataValidation> 結束標籤    2
          <x14:dataValidations 容器開始     1
          </x14:dataValidations> 容器結束   1
                                    合計 = 6
        即開閉標籤各計一次，且複數容器元素亦被子字串命中。
        與「兩類相加」無關。
  裁：正確值為 **x14 dataValidation 元素 2 個、涵蓋 2 個 sqref 群組
        共 7 個 range，全數於 v1 消失**。RULINGS.md 之 R16 原文不改，
        於其後附本更正（執行層已如此處置，追認）。
  §5a 新增：**以子字串計數量測 XML 元素數量，必須加詞界與標籤形狀約束**
        （至少排除結束標籤與同前綴之複數容器）。此即 canon「詞彙型工具
        之缺陷不會報錯，須以已知全集驗證」之具體實例，記為第 11 例。
  裁決結論不受影響：21 lost / 10 added 之成員清單獨立成立且已複現。

R17-3  R16-2「SXM 尚未寫回」為錯誤前提 —— 歸因分析層
  事實：執行層實測 features/sxm/output/ 早有交付件與 .sha256，
        tag fw036-sxm-v1 存在，且已受損（lost 11 / added 10、
        x14 DV 2 → 0，失去者正是 R 欄設計方法下拉）。
  歸因：分析層撰寫 R16-2 時以**先前對話中之印象**為來源，未回到 repo
        實測 output/ 與 refs/tags。此違反 canon §5a
        「不以自身先前輸出為來源；回到 repo 現行記載或當下實測」。
  裁：R16-2 之「SXM 尚未寫回，攔得住」一句作廢，以本條取代。
        凍結令本身不受影響（其標的為未來之 --write）。
  §5a 強化：**任何關於「某 feature 目前處於何階段」之陳述，
        撰寫當下必須以 output/ 內容 + refs/tags + PLAYBOOK §6
        三者實測為據，三者不一致時停手回報。**
        本次為該類錯誤之第二次（前次為 AMFM P7 之 tag/§6 不一致）。

R17-4  Projection 對照組之證明力 —— 追認執行層之限縮
  事實：執行層指出 Projection output/ 與 inputs/ 位元完全相同，
        零差異證明的是「沒被寫過」，非 writer 安全。
  裁：追認。R16 §2 之 Projection 對照組敘述，其結論限縮為
        「該檔未經寫回路徑」，不得作為 writer 安全性之任何佐證。
```

## R18 — 交付件結構缺損之收束（Pei 簽署 2026-08-13）

```text
R18-1  已交付件一律不重產
  裁：SXM（fw036-sxm-v1）與 Home（fw036-home-regen-v2）維持現狀，
      不重產、不改 tag、不動任何一列。
      各自之結構缺損以 anomaly 形式登記，狀態 **DEFERRED —
      待下次內容變動時一併修復（R18-1）**，非 PENDING
      （依 R15-2：已裁而結果為延後者不得留在 Open PENDING）。
      登記內容須含實測數字：
        SXM   lost 11 / added 10，x14 DV 2 → 0（R 欄設計方法下拉）
        Home  lost 14 / added 10，含整組 SmartArt；x14 DV 0 → 0
              （該檔本無 DV，DV 判準看不見此缺損）
  R17-6 / R17-7 據此結案。whole-sheet splice 提案**不實作**，
      僅保留於 03 包內作為日後 interleaved 修復之已知路徑。

R18-2  AMFM v2 之處置
  裁：v2 已產出，保留於 output/，**不打 tag、不送出、不再加工**。
      v1 tag fw036-amfm-regen-v1 維持不動。
      v2 附掛未驗標籤：**尚未經 Excel 實開驗證（R17-9）**，
      交付前必須先由 Pei 完成該四點確認。時點由 Pei 決定。
      本包不觸發任何後續動作。

R18-3  凍結解除，代之以常設規則
  裁：R16-2 之全 repo 寫回凍結**即刻解除**。
      解除依據：探針對 AMFM 客戶原件與 FW036 空白範本兩次驗證
      皆 LOSSLESS（上繳包 02 §2 附原文），且不再有任何重產動作。
      代之以常設規則，即刻生效、適用全 feature：
        (1) backend/xlsx_surgical.py 為**唯一**寫回路徑；
            openpyxl 存檔路徑不得用於任何交付件產出
        (2) 寫回後強制比對輸出與輸入之 zip 成員集合、
            各 sheet 之 classic / x14 DV 計數，不等即 **ABORT**
            （非 warn）；允許差異者僅限被寫入之 sheet XML 本身
        (3) 該 invariant 之違反屬 canon §0 第三項，升 Tier 2，
            不得以放寬 invariant 解決
      五個 PLAYBOOK 之凍結橫幅一併移除，改記本規則。

R18-4  R17-5(b) 反向測試 —— 仍須執行，但不擋任何工作
  裁：invariant 之反向測試（以刻意破壞之輸出驗證確實 ABORT）
      仍須完成，因「不可能失敗之檢查項不得標 PASS」。
      但其完成與否**不作為任何 gate 之前提**，Privacy 照跑。

R18-5  AMFM 第 243–310 列無儲存格樣式
  裁：登記為 anomaly，**不修**。v1、v2 皆然，非結構缺損所致。
      狀態 DEFERRED — 待下次內容變動時一併處理。

R18-6  焦點
  裁：AMFM / Home / SXM / Projection 四 feature 之結構缺損議題
      至此**全部結案或 DEFERRED，無 Open PENDING**。
      分析層與執行層之工作焦點回到 Privacy。
```

### 執行層回報（下放包 04，2026-08-13）

R18-4 已執行，兩種破壞模式皆正確 ABORT，測試常駐於
`tests/test_xlsx_surgical_invariant.py`（3 passed）。輸出原文見
`docs/upstream/04_wrapup.md` §3。

**另須分析層知悉**：下放包 03 §1 之 **R17-1 ~ R17-4 為已簽署條文，
但從未寫入本檔** —— 03 包當時只有 R17-5(b) 一項可辦，該包未產生上繳包，
四條簽署條文因此留在 handoff 檔內未進登記。本包 §2 未列此項，
執行層**未自行補登**，回報待裁。

> **後續（R19-2，2026-08-13 同日）**：分析層認定為己方作業清單漏項，
> 裁定即刻補登，並立為通則：凡下放包自檢表標為已簽署之條文，該包之作業
> 清單必須含一項「貼入 `RULINGS.md`」；缺此項者執行層得逕行補登，
> 不須回報待裁。R17 全文已補於本檔（見上，位於 R16 與 R18 之間）。

## R19 — 04 包收束之覆核（分析層自裁，2026-08-13）

```text
[RULING] R19 — 04 包收束之覆核（分析層自裁，2026-08-13）

R19-1  §1.1 之作法選擇 —— 執行層正確，追認
  事實：04 包 §2.2 寫「features/{sxm,home}/ANOMALIES.md 各登一條」。
        A-SX28 / A-H27 於上繳包 02 時已建立且已含全部實測數字，
        執行層改寫其狀態與處置段而非另開新條。
  裁：追認。另開會產生兩條描述同一事件、數字相同而狀態不同的登記，
        正是 R15-2 要避免的狀態混亂。
  歸因：**分析層用語缺陷** —— 「各登一條」未區分「新建」與「登記」。
  立為通則：下放包指示登記時一律寫
        **「各登記一條；既有條目存在時更新之，不另開新條」**。
        僅寫「登一條」者，執行層得以「不重複登記」解讀，且該解讀優先。
        （同 R17-1 之精神：指示須明列標的與既有狀態之處置。）

R19-2  R17-1 ~ R17-4 未入 RULINGS.md —— 分析層過失，補登
  事實：下放包 03 §5 自檢表將 R17-1~R17-4 標為已簽署，但 03 包 §3
        僅指示執行 R17-5(b) 一項、未指示貼入 RULINGS.md，且該包
        未產生上繳包。04 包 §2.1 亦只指示貼入 R18。
        結果：四條規則正在被遵守，而 RULINGS.md 內 grep R17 零命中。
  歸因：**分析層作業清單漏項**，非執行層疏漏。執行層發現後未自行補登
        而回報待裁 —— 處置正確（補登他人之裁決條文不屬其權限）。
  裁：即刻補登。依 charter「A ruling not written to the repo did not
        happen —— 雙向適用」，R17-1~R17-4 在補登完成前不具形式效力，
        補登後追溯自 2026-08-13 生效。
  立為通則：**凡下放包自檢表標為已簽署之條文，該包之作業清單必須
        含一項「貼入 RULINGS.md」**；缺此項者，執行層得逕行補登
        並於上繳包載明 —— 不須回報待裁。

R19-3  R18-3 規則 1 尚無機制保證 —— 執行層發現成立，補作
  事實：「xlsx_surgical.py 為唯一寫回路徑」目前是紀律不是機制；
        backend/writer.py 與 scripts/translate_xlsx.py 內之 wb.save()
        未動，仍可被呼叫。
  裁：補一項常駐測試（非一次性腳本，同 R18-4 之體例）：
        掃描 repo 內所有 .py，凡出現 openpyxl 之存檔呼叫
        （wb.save / Workbook.save / save_workbook 等）而檔案不在
        白名單內者即 FAIL。白名單初值僅 backend/xlsx_surgical.py，
        及明確標註為非交付用途者（需於白名單旁註明理由）。
        測試須自帶陽性對照：白名單內之呼叫不得觸發 FAIL。
  §5a：**規則與機制之區別須在條文中標明**。R18-3 規則 1 之措辭
        「唯一」隱含機制保證而當時並無，此類措辭日後須附
        「（機制：<測試或檢查名稱>）」或明標「（紀律，無機制）」。

R19-4  §5.3 橫幅替換之驗證層級 —— 機械化驗證即足
  裁：04 包停手條件 2 之條件文字本身即為關鍵詞層級（「與 R16 所述
        不符」由分析層指定為三關鍵詞檢查），執行層之斷言實作與該
        條件等價。**不要求語意層人眼核對**，此項結案。

R19-5  A-AM19 之修復方向須標明未實測
  裁：A-AM19 所記之修復方向（自第 242 列繼承 <row> 屬性與各欄 s= 索引）
        為紙上推論，未寫過一行驗證程式。條目內須加註
        **「修復方向未實測，日後採用前須先驗證」**。
        依 canon「檢查項須確認其在該階段確實可能失敗；不可能失敗者
        標『未實測』而非 PASS」之同一精神，推論型處置建議亦適用。

R19-6  canon 草案 —— 檔名不改追認；「不重產」不得立為結果型通則
  (a) 檔名維持 CANON_DRAFT_r16_delivery_integrity.md：追認。
      理由「已提交的紀錄不因後續事件而失效」正確，且已於檔內標明
      同時承載 R16-4 與 R18-3。
  (b) 執行層建議將 R18-1（不重產）寫成通則 —— **部分採納，形式須改**。
      不得寫成結果型通則（「發現結構缺損預設不重產」），該形式會使
      「預設不修」成為交付缺陷之默認處置，風險不對稱。
      改寫為**判準型通則**，草案措辭如下：
        「已交付件發現結構缺損時，重產與否依下列判準逐案裁定，
         裁定屬 Tier 2：
           1. 缺損是否影響 TC 內容之正確性（影響 → 必須重產）
           2. 該交付件是否已送達客戶或已進管制文件流程
           3. 重產所需之 writer 能力是否已具備（如 interleaved
              形態需額外路徑）
           4. 是否存在交付時程壓力
         判準 1 為否決型：內容正確性受影響者，其餘三項不得推翻重產。
         個案先例：R18-1（AMFM/Home/SXM，判準 1 為否、3 對 Home 為
         否、故裁定不重產並登記 DEFERRED）。」

R19-7  Privacy A-PV03 → DEFERRED、A-PV09 → CLOSED —— 追認
  裁：兩項狀態變更皆正確套用 R15-2 與 R18-3。
      A-PV03 標題自載「明示延後」卻掛 PENDING，確為 R15-2 之標的；
      A-PV09 之建議已被 R16 採納並由 R18-3 落為常設規則，
      已成規則者不留追蹤清單。
```

### 執行層回報（下放包 05，2026-08-13）

**R19-2 已辦**：R17 全文補登於本檔（位於 R16 與 R18 之間），逐字未改。
補登時發現下放包 03 之權限標示（「§1 為 R17-1 ~ R17-3」）與其 §1 區塊
實含 R17-4、且 §5 自檢表列四條為已簽署 —— 落差照實回報，未自裁何者為準。

**R19-3 未辦，停手條件 3 觸發**：依 R19-3 撰寫之掃描在現況下即 FAIL ——
**11 個違規呼叫點**，散布於 4 個 feature 的 write_back 與 3 個共用模組。
依下放包 05 §3.3：不修改任何生產程式碼、該測試不入庫、續行第 4–5 項。
違規清單見下。掃描以 AST 實作（僅追蹤自 `load_workbook` / `Workbook()`
綁定之名稱），故 `pixmap.save()` 與 python-docx 之 `document.save()`
不會誤判 —— 已驗證：`features/*/scripts/split_spec.py` 與
`tests/test_amfm_cross_refs.py` 皆未被命中。

| # | 呼叫點 | 性質 |
|---|---|---|
| 1 | `features/home/scripts/write_back.py:469` | 交付件產出（Home）|
| 2 | `features/sxm/scripts/write_back.py:472` | 交付件產出（SXM）|
| 3 | `features/media/scripts/write_back.py:343` | 交付件產出（Media）|
| 4 | `features/projection/scripts/writeback.py:284` | 交付件產出（Projection）|
| 5 | `backend/writer.py:363` | `write_generated_results` —— app 寫回主路徑 |
| 6 | `backend/writer.py:404` | `write_framework_sheet` |
| 7 | `backend/writer.py:468` | `write_generated_tc_workbook`（含 template 分支）|
| 8 | `backend/writer.py:487` | 同上，無 template 分支 |
| 9 | `backend/api_server.py:2370` | 匯出下載用 xlsx（`BytesIO`）—— 交給使用者之檔案 |
| 10 | `backend/api_server.py:2410` | **就地覆寫 `source_path`** —— 破壞的是輸入檔本身 |
| 11 | `scripts/translate_xlsx.py:303` | 翻譯後之工作簿產出 |

**第 10 項須優先注意**：它不是「產生受損的副本」，是 `wb.save(source_path)`
覆蓋來源檔。在 R18-3 的框架下，這比其餘十項嚴重一級 —— 其餘產生的是
可丟棄的輸出，這一項損毀的是後續一切比對所依賴的基準。

**白名單設計（測試已寫好，待裁後入庫）**：初值僅
`backend/xlsx_surgical.py`（理由：受裁可之路徑本身）、
`features/privacy/scripts/xlsx_roundtrip_probe.py`（理由：非交付用途，
刻意產生 LOSSY 對照臂）、`tests/`（理由：非交付用途，fixture 建於
`tmp_path`）。測試自帶陽性對照，確認白名單內之呼叫不觸發 FAIL。

## R20 — 寫回路徑違規點之處置（分析層自裁，2026-08-13）

```text
[RULING] R20 — 寫回路徑違規點之處置（分析層自裁部分，2026-08-13）

R20-1  03 包權限標示落差 —— 歸因分析層，補登有效
  事實：03 包權限標示寫「§1（R17-1 ~ R17-3）為分析層自裁」，
        但 §1 區塊實際含 R17-4，§5 自檢表亦將四條同列為已簽署。
        執行層依 R19-2 之「逐字取自 03 §1」補了整個 §1 區塊（含
        R17-4），落差照實記載，未自裁何者為準 —— 處置正確。
  裁：**四條同為分析層自裁項**，權限標示之「R17-1 ~ R17-3」為
        分析層漏寫範圍上界，非有意排除 R17-4。補登有效，全數生效。
  §5a：條文區塊與其權限標示之範圍必須逐項對齊；標示以列舉而非
        區間表示時，須與區塊內實際條文數一致。

R20-2  R19-3 之測試以 ratchet 形式入庫 —— 不待違規點清零
  事實：停手條件 3 觸發（現況即 FAIL，11 個違規呼叫點），執行層
        未入庫、未動生產程式碼 —— 完全正確。
  裁：測試改以 **ratchet（棘輪）** 形式入庫，即刻執行：
        (1) 將現況 11 個呼叫點以「已知既存違規」清單寫入測試，
            逐點附檔名、行號、性質，作為 grandfathered baseline
        (2) 測試之通過條件為「掃描結果 ⊆ 白名單 ∪ 既存違規清單」
        (3) 新增任何不在兩份清單內之呼叫點 → **FAIL**
        (4) 既存違規清單為**只減不增**；移除一項時同步從清單刪除，
            清單本身即進度計量
        (5) 保留執行層已設計之白名單三項與陽性對照
  理由：規則之價值在於阻止新增，不在於一次清零。以「必須先清零才
        能入庫」為條件，等於讓最需要防護的期間完全無防護。
  §5a：**機制之導入不得以「現況已合規」為前提**；現況不合規時，
        正確作法是凍結現況並禁止惡化，而非延後機制。

R20-3  四支 feature write_back 腳本 —— 封存，不改寫、不得執行
  事實：features/{home,sxm,media,projection}/scripts/write_back.py
        （及 writeback.py）仍在 openpyxl 存檔路徑上。四者所屬
        feature 之交付件皆已產出，缺損已依 R18-1 裁為 DEFERRED。
  裁：依 R18「做過的都不重產」，**不改寫此四支腳本**。
        改以封存處置：
        (1) 四支腳本檔頭加入封存標頭（逐字）：
            「QUARANTINED (R20-3, 2026-08-13) — this script writes via
             openpyxl save and will destroy zip members and data
             validations. It must not be executed. The feature's
             delivered artefact is frozen; see ANOMALIES A-H27 /
             A-SX28 / A-AM18 and RULINGS R18-1.」
        (2) 各 feature PLAYBOOK 加註該腳本已封存
        (3) 四點自 R20-2 之既存違規清單中另標 `QUARANTINED`，
            與「仍可被呼叫之違規」區分
        (4) **不加程式層 guard**（加 guard 屬修改生產程式碼，
            且該腳本本就不應被執行；標頭與登記已足）
  Media 附註：features/media 未在 R16/R18 之檢測範圍內，其交付件
        是否受損**未量**。本包不擴大檢測範圍，僅封存腳本並登記
        「交付件狀態未量」。

R20-5  Privacy 之 write_back 自始建於 xlsx_surgical
  裁：Privacy 尚未寫回，**不得複製任一既有 feature 之 write_back
        腳本作為起點**（四支皆已封存）。其寫回路徑自始建於
        backend/xlsx_surgical.py，並受 R18-3 之 ABORT 級 invariant
        拘束。此為 R18-3 規則 1 之首次正向適用。

R20-6  canon 草案落點 —— 追認
  裁：判準型通則置於 §6a 之末，追認。執行層之理由（前文規範如何
        不製造缺損，本條規範缺損既成後怎麼辦）正確。

R20-7  A-AM19 之未實測標記內容 —— 追認並嘉許
  裁：執行層除照條文標註外，另寫明「未驗的具體是什麼」
        （s= 索引跨列沿用是否對所有欄成立；第 242 列為 template
        tail 最後一列，其樣式未必等同資料列常態；新增 <row> 屬性後
        spans 與 customFormat 是否需同步）。
        追認，並立為體例：**未實測標記須指名待驗之具體命題**，
        僅寫「未實測」者不合格 —— 無命題者日後無從驗起。
```

**R20-4（`api_server.py:2410` 就地覆寫）不在本區塊**：該項於下放包 06 §2
為待裁，隔日同日由 Pei 簽署選項 A，條文見 **R21**。

### 執行層回報（下放包 06，2026-08-13）

- R20-2 之 ratchet 測試已入庫：`tests/test_single_write_path.py`
- R20-3 之封存標頭已加於四支腳本；**Media 無 `PLAYBOOK.md`**，
  其加註改置於 `features/media/RUNBOOK.md`，照實回報，未自行建立 PLAYBOOK
- 作業順序調整：先辦 §3.3（加標頭）再辦 §3.2（入庫測試）。
  理由為標頭會使行號位移，先入庫則清單行號當場失準。
  兩項內容不受影響，僅順序對調。

## R21 — api_server.py:2410 就地覆寫之處置（Pei 簽署 2026-08-13）

```text
[RULING] R21 — api_server.py:2410 就地覆寫之處置（Pei 簽署 2026-08-13）

R21-1  基準稽核（先辦，唯讀）
  裁：對五個 feature 之 inputs/ 全部檔案計 SHA256，與客戶端來源
      目錄之對應檔比對，確認是否已有被覆寫者。
      **全程唯讀** —— 不得移動、改名、覆寫、刪除 inputs/ 或來源目錄
      之任何檔案。

R21-2  登記
  裁：R20-2 之既存違規清單中，api_server.py:2410 標為 `HAZARD`，
      與其餘十點區分。標註須寫明其與他點之性質差異：
      「overwrites the source file in place; destroys the baseline
       that all structural comparisons depend on, not merely the
       output」。

R21-3  程式碼變更 —— 解除覆寫，不解除受損
  裁：api_server.py:2410 之 wb.save(source_path) 改為寫入新檔並
      回傳新路徑，**永不覆寫來源**。
      **明確界定**：本項解除的是「基準被毀」之危害；該路徑仍以
      openpyxl 存檔，其輸出仍為受損檔，此缺陷**不在本項處置範圍**，
      續留 R20-2 之既存違規清單內，由該清單之只減不增機制追蹤。
      不得藉本項順手改為 xlsx_surgical —— 那是另一項變更，
      需另行裁定（api_server.py:2370 之匯出下載路徑同理，本包不動）。
```

### 執行層回報（下放包 07，2026-08-13）

**R21-1 已辦（唯讀）**：六個 feature、84 個 `inputs/` 檔全數計 SHA256，
與 `/Users/peihe/Work/` 客戶樹之全部同名候選逐一比對。
結果 **MATCH 81 / NO_MATCH 1 / NO_COUNTERPART 2**。

**R21-2 已辦**：`api_server.py:2410` 於 `tests/test_single_write_path.py`
之 `KNOWN_VIOLATIONS` 標為 `HAZARD`，性質說明逐字照錄。

**R21-3 未辦 —— 停手條件 1 觸發**：稽核出現 `NO_MATCH`
（`features/media/inputs/` 之 FW036 工作簿），依 07 包 §3.1
「停止 2.3 之程式碼變更，續行 2.2 之登記，立即回報」。
`api_server.py` 一字未改。詳見 `docs/upstream/07_baseline_audit.md`。
