# DECISIONS — Comfort (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

> **已簽署 2026-08-14（見文末 Sign-off）。** 自此本檔受 **R-C9** 保護：
> `recon.py` 偵測到 Sign-off 已填即拒絕覆寫，改寫 `DECISIONS.new.md` 並以
> 非零碼離開。若日後需以新 survey 取代本檔，須人工 diff 後合併。
>
> 簽署後之異動一律追記於文末 **Amendment**，不改寫既有條目。

## 1. Intake
- spec_mode: [AUTO] A
- spec text layer: [AUTO] text-layer: 62782 chars (via pdftotext)
- source files: [AUTO] 4 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 4 checked, 4 PASS, 0 FAIL (measured values in RECON.md)
- spec outline map: [AUTO] 129 cited sections, all found in a 180-entry ruled export; map at data/spec_id_to_outline.tsv

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- draft disposition: [PROPOSED: discard & regenerate — lint consistency cheaper than row salvage]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 403
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 403 (list in recon.json)
- covered nowhere: [AUTO] 403 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap
- workbook req_ids absent from 037: [AUTO] done=0 (none) draft=1 ['xxx'] — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only. NOTE: under BLANK these are template sample rows before they are anything else — check the rows themselves before filing an RD-1

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [SIGNED 2026-08-14] **`home` 之 done region**（144 列，PARTIAL_INTERLEAVED），`cross-feature: style only`。**`amfm` 具名排除** —— 其 recon 自記 requirement-family mismatch，借樣式與借別的難以劃線，具名排除比註記警語可靠。依 05 §4；取代原 [PROPOSED: nearest sibling…]，該措辭解析不到對象（時序最近之 privacy／sxm 皆 BLANK 無 done region）
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)_{outline}]
- tc_id scheme: [RULED] NR1L-ComfortHMI-{n:03d} — frozen per this feature's RULINGS.md, not open at sign-off

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [SIGNED 2026-08-14] **已定** —— Test Group `Comfort`、
  **15 個 Test Set**，依下放包 `docs/handoff/12_partN_final.md` §2（Pei 簽署
  2026-08-14）。落地於 `features/comfort/framework.md`；驗算
  `scripts/verify_partn.py` 四個 assertion 全 PASS（403 leaves／129 節每節恰
  屬一組／逐章回算相符／命名合規）。Layer 3 **不入工作簿**（§4.1.5）
- profile [OVERRIDE] clauses: **[PEI — 仍為 Tier 2，維持未定]** ——
  本次簽署**不涵蓋**此項。Phase 4 之前須另行起草並簽署；
  至少須明文 A-CF07 之寫回處置（03 §5）

## 7. Execution
- batch plan: [SIGNED 2026-08-14] pilot = **第 13 章 `Seat Control Tab`**
  （14 leaves，13.2 ~ 13.6）。依 05 §4：pilot 之用途是在小樣本上暴露判斷
  漂移，第 13 章含 13.1 之 variant 條件（lower comfort screen 之有無），
  會逼出 §8.7.3 variant label 與 §4.4 Pre-Condition 兩類判斷。
  取代原 [PROPOSED: … pilot = smallest coherent batch]，該規則機械地選到
  第 6 章 1 個 leaf，樣本數 1 連批內一致性都測不到。
  **其餘批次之分組**：依 Part N 之 15 個 Test Set，不再沿用「依章分組」
  （章 2 與章 16 各 90+ 之問題已由 Part N 解決）

---

## Sign-off

- Reviewed by: PeiPYHsu  Date: 2026-08-14
- Overridden items: §4 exemplar source（原 [PROPOSED: nearest sibling…] →
  具名 `home`，`amfm` 具名排除）；§7 batch plan（原 pilot = smallest
  coherent batch → 第 13 章 `Seat Control Tab`）
- Ruling notes:
  - **Part N 依下放包 `docs/handoff/12_partN_final.md` 簽署**（Pei，
    2026-08-14，「是」）。該包取代 `11_partN_draft.md` §2 之草案表；
    11 之 §1／§3／§5／§6 仍有效。Test Group `Comfort`、15 個 Test Set、
    合計 403 leaves／129 節。落地於 `features/comfort/framework.md`。
  - **本次簽署不涵蓋 profile `[OVERRIDE]`** —— §6 第二項仍為 Tier 2、
    維持未定。Phase 4 之前須另行起草簽署。
  - **未於本次簽署處理者**（狀態不因簽署而改變）：17 節 in-baseline
    substantive 皆不入 Part N —— 4 節依 R-C16 為 RD-1 覆蓋缺口項、
    10 節 DEFERRED（A-CF12，Pei 直接向 RD）、3 節待 DR #6。
  - **凍結項不在簽署範圍內**：`test_group` = `Comfort`（R-C6）、
    `tc_id` = `NR1L-ComfortHMI-{NNN}`（R-C7）、baseline = SR24（R-C1）、
    UI label 拼寫依 SR24（R-C2）、leaf 判準（R-C3）。
  - **R-C9 自此生效**：本檔已簽，`recon.py` 重跑將拒絕覆寫並改寫
    `DECISIONS.new.md`。R-C10 之空簽署警告相應停止輸出。
  - **8 個 `[PROPOSED]` 未於簽署時更動，依本檔表頭語意即
    「binding as proposed」** —— 非遺漏，是生效。逐項列出以免日後誤讀為未定：
    §2 draft disposition、§3 safety attributes、§4 style authority／
    test item shape／test group–set columns／author on new rows／
    spec_reference、§5 split_mode。
  - 執行層依 12 §5.4 轉錄本簽署；**Reviewed by 與 Date 之值由 Pei 指定**，
    非執行層自填。本檔寫入日為 2026-08-15，記載之簽署日為 Pei 指定之
    2026-08-14（下放包 12 之簽署日）；兩者不同係轉錄時差，非追溯。

---

## Amendment

（尚無。簽署後之異動追記於此，不改寫上方既有條目。）
