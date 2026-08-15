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
  `scripts/verify_partn.py` 全部 assertion PASS（403 leaves／129 節每節恰
  屬一組／逐章回算相符／命名合規）。Layer 3 **不入工作簿**（§4.1.5）
  - **修正案 1（2026-08-15，下放包 13 §2）**：#15 更名
    `Comfort Widget` → `Home Screen Widget`（§4.2 之 Test Group 前綴）。
    Layer 3 與 leaves 不變
  - **修正案 2（2026-08-15，下放包 14 §1）**：依 R-C18 末句對 ch2／ch16
    逐節全文複核，**四節改置** —— `2.16`／`16.17` → Temperature and Fan 對
    （截斷誤讀，主詞為風量顯示）；`2.14`／`16.14` → Anatomy 對
    （MTC 為系統型別非模式開關，屬原始分類錯誤）。
    受影響組：#1 12→16、#2 41→35、#3 17→19、#11 14→17、#12 40→36、#13 16→17。
    **Test Set 之數量、名稱與邊界不變；ch2 = 92、ch16 = 99、總計 = 403 皆不變。**
    理由見 `framework.md` §3.5
  - **Sign-off 不重簽**（14 §5）：兩次修正皆未改變 Part N 之結構
    —— 組數、名稱邊界、母體與逐章數皆同，變更限於四節之組間歸屬與一處命名。
    執行層覆核此判斷後**同意**，未重簽
- profile [OVERRIDE] clauses: **[SIGNED 2026-08-15]** —— 依下放包
  `15_profile_draft.md` 全部條款 ＋ `16_profile_signed.md` §1 之三項裁定
  （Pei，2026-08-15）。落地於
  `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。
  三項裁定皆「照建議」：§3.1 Test Item 繼承（**附實測條件，轉為 G-1 gate**）、
  §3.4 source token 照錄（含 `12.1` 之 `LEDs (.`）、§0.1 之 Excel 實開確認
  由 Pei 執行。
  **A-CF07 之寫回處置已於 profile §0.1 明文**（03 §5 之要求已滿足）

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

## Sign-off 2 —— profile [OVERRIDE]

> **首筆 Sign-off（Part N，2026-08-14）不覆寫、不改寫。** 本筆為第二次簽署，
> 對象不同（R-C10：簽署標記須被實際填寫，且須可辨其涵蓋範圍）。

- Reviewed by: PeiPYHsu  Date: 2026-08-15
- 涵蓋範圍: `DECISIONS.md` §6 之 **profile `[OVERRIDE]` clauses** 一項。
  **不涵蓋**首筆已簽之 Part N（其狀態不因本筆改變），亦不涵蓋任何
  `[PROPOSED]` 項。
- Overridden items: 無 —— 15 §9 三項待裁皆「照建議」，未推翻草案任何條款
- Ruling notes:
  - 依據：`docs/handoff/15_profile_draft.md`（草案全部條款）＋
    `docs/handoff/16_profile_signed.md` §1（三項裁定，Pei「裁的都是是是是」）。
  - **G-1 為 §3.1 之生效條件，非本簽署之附款**（16 §2）：gate 已執行，
    **PASS**（143/144 含 modal），惟**附 provenance 但書** —— 量測對象為
    `forms/…_Home_20260809.xlsx`（SHA256 `1895fb2a…`），非 home RECON 所測檔
    亦非 Home v2，兩者皆不在 repo。詳 profile §3.1 與上繳 09。
    若分析層認為該替代不可接受，§3.1 回到 pending 並重裁。
  - **A-CF07 已依 profile §0.1 備妥，尚未結案**：prepared workbook 已產
    （`output/…_Comfort_20260815_prepared.xlsx`，SHA256 `b68117a2…`），
    `BASELINE.sha256`（8 檔）與 `DELIVERY.sha256`（ENTRY 001）已建並驗過。
    **四項 Excel 確認保留予 Pei**（裁定 3），確認前 A-CF07 不結案。
  - **Phase 4 起跑條件三者**（16 §3.2）：G-1 PASS ✅ ＋ profile 落檔 ✅ ＋
    **A-CF07 清列經 Pei 於 Excel 確認 ⏳**。第三項未達成，
    **Phase 4 未開始**。

---

## Amendment

- **Amendment 1（2026-08-15，下放包 13 §2）** —— Part N #15 更名
  `Comfort Widget` → `Home Screen Widget`。依 §4.2（Test Set 不得以 Test
  Group 為前綴）。Layer 3 與 leaves 不變；`verify_partn.py` 之前綴檢查由
  `measured ['Comfort Widget']` 轉為 `measured []`。

- **Amendment 2（2026-08-15，下放包 14 §1）** —— Part N 四節改置：
  `2.16`／`16.17` → Temperature and Fan 對；`2.14`／`16.14` → Anatomy 對。
  依 R-C18 末句之回溯複核。受影響組 #1／#2／#3／#11／#12／#13 之 leaf 數
  變動，**ch2 = 92、ch16 = 99、總計 = 403 皆不變**，組數與名稱邊界不變。
  `verify_partn.py` 七項檢查以修正後期望值重跑，全 PASS。

- **兩案皆未重簽 Sign-off**（14 §5）：Part N 之結構未變 —— 組數、名稱邊界、
  母體與逐章數皆同，變更限於四節之組間歸屬與一處命名。執行層覆核此判斷後
  同意。上方 §6 之條目已就地增記兩案（14 §5 明示「§6 之 Part N 條目增記」），
  本區為其索引。

> **記法之說明**：本檔表頭原則為「簽署後之異動一律追記於文末 Amendment，
> 不改寫既有條目」。本次兩案於 §6 條目下**新增子項**而未改寫既有文字 ——
> 既有之 `[SIGNED 2026-08-14]` 行逐字保留，修正案以子項附加。
> 就地增記與本區索引並存，是為了讓讀 §6 者不必先讀到文末才知道它已被修正。
