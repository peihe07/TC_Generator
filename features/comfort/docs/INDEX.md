# Comfort — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-14（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-14 | Phase 0 intake（開案） | [handoff/01_phase0_intake.md](handoff/01_phase0_intake.md) | [upstream/01_phase0_intake.md](upstream/01_phase0_intake.md) | R-C1 ~ R-C5 | A-CF01 ~ A-CF07 | PASS |
| — | 2026-08-14 | R-C6・R-C7 裁決補遺 | [handoff/02_rulings_addendum.md](handoff/02_rulings_addendum.md) | （併入上繳 01） | R-C6、R-C7 | — | PASS |
| 02 | 2026-08-14 | 上繳 01 覆核 ＋ Phase 2 ＋ 51 節分類 | [handoff/03_upstream01_review.md](handoff/03_upstream01_review.md)、[handoff/04_rulings_c8_c10.md](handoff/04_rulings_c8_c10.md) | [upstream/02_phase2_review.md](upstream/02_phase2_review.md) | R-C4-1、R-C8 ~ R-C10 | A-CF08、A-CF09 | PASS（2 項待裁） |
| 03 | 2026-08-14 | R-C5-1／R-C11 落實 ＋ 17 節適用性判讀 | [handoff/05_rc5_correction.md](handoff/05_rc5_correction.md)、[handoff/06_source_singularity.md](handoff/06_source_singularity.md) | [upstream/03_applicability.md](upstream/03_applicability.md) | R-C5-1、R-C11 | A-CF10 ~ A-CF12 | PASS（2 項待知悉） |
| 04 | 2026-08-14 | R-C12~14 落實 ＋ DR #6／#7 判讀 | [handoff/07_upstream03_review.md](handoff/07_upstream03_review.md)、[handoff/08_dr67_material.md](handoff/08_dr67_material.md) | [upstream/04_dr67_applicability.md](upstream/04_dr67_applicability.md) | R-C12 ~ R-C14 | A-CF11 升格／A-CF12 層級訂正 | PASS（2 項待知悉） |

| 05 | 2026-08-14 | R-C15~R-C17 落實 ＋ DR #8 DEFERRED ＋ Layer 3 map | [handoff/09_upstream04_review.md](handoff/09_upstream04_review.md)、[handoff/10_phase3_start.md](handoff/10_phase3_start.md) | [upstream/05_layer3_map.md](upstream/05_layer3_map.md) | R-C15 ~ R-C17 | A-CF13 | PASS |
| 06 | 2026-08-14 ~ 15 | Part N 定稿 → `framework.md` ＋ `DECISIONS.md` 簽署 | [handoff/11_partN_draft.md](handoff/11_partN_draft.md)、[handoff/12_partN_final.md](handoff/12_partN_final.md) | [upstream/06_framework.md](upstream/06_framework.md) | 無新條文 | A-CF13 第三項 | PASS |
| 07 | 2026-08-15 | R-C18 ＋ #15 更名 ＋ 129 節全文抽出 | [handoff/13_upstream06_review.md](handoff/13_upstream06_review.md) | [upstream/07_fulltext.md](upstream/07_fulltext.md) | R-C18 | （無新登；A-CF13 相關事實補充） | PASS |
| 08 | 2026-08-15 | ch11／ch12 合併依據落地 ＋ ch2／ch16 全文 | （Pei 直接指示，無下放包） | [upstream/08_ch2_ch16_fulltext.md](upstream/08_ch2_ch16_fulltext.md) | 無新條文 | A-CF13 第四項 | PASS |
| **09a** | 2026-08-15 | Part N 修正案（部分交付：14 §5 六項） | [handoff/14_partN_amendment.md](handoff/14_partN_amendment.md) | [upstream/09_partN_amendment.md](upstream/09_partN_amendment.md) | R-C19 | — | PASS |
| **09b** | 2026-08-15 | 完整交付：14 ＋ 15 ＋ 16（profile 簽署、G-1、A-CF07 備妥） | [handoff/14_partN_amendment.md](handoff/14_partN_amendment.md)、[handoff/15_profile_draft.md](handoff/15_profile_draft.md)、[handoff/16_profile_signed.md](handoff/16_profile_signed.md) | [upstream/09_partN_amendment_and_profile.md](upstream/09_partN_amendment_and_profile.md) | G-1 gate | A-CF07（後於 18 §1 CLOSED） | PASS |
| 10 | 2026-08-15 | 窮盡性掃描 ＋ pilot **stop-and-report** | [handoff/17_g1_baseline_exhaustiveness.md](handoff/17_g1_baseline_exhaustiveness.md)、[handoff/18_phase4_pilot.md](handoff/18_phase4_pilot.md) | [upstream/10_pilot_and_exhaustiveness.md](upstream/10_pilot_and_exhaustiveness.md) | R-C20 | A-CF14；A-CF07 CLOSED | **停於生成前（5 問待裁）** |
| 11 | 2026-08-15 | **pilot 14 條** ＋ lint ＋ §9 自評 ＋ 九軸複掃 | [handoff/19_pilot_rulings.md](handoff/19_pilot_rulings.md) | [upstream/11_pilot.md](upstream/11_pilot.md) | R-C21、R-C22 | — | PASS（送 pilot review） |
| 12 | 2026-08-15 | **pilot rev2** —— 4 defect 修正 ＋ gate 25→29 | [handoff/20_pilot_review.md](handoff/20_pilot_review.md) | [upstream/12_pilot_rev2.md](upstream/12_pilot_rev2.md) | 無新條文 | A-CF15 | **12 條可 review／2 條待裁** |
| 13 | 2026-08-15 | **pilot rev3** —— `[BLOCKED-SPEC]` ＋ 系統性 ER 修正 | [handoff/21_blocked_spec_ruling.md](handoff/21_blocked_spec_ruling.md) | [upstream/13_pilot_rev3.md](upstream/13_pilot_rev3.md) | R-C23、R-C24 | — | PASS（31 gate 全綠） |
| 14 | 2026-08-15 | **pilot rev4** ＋ 寫回 **dry-run**（未執行） | [handoff/22_rev3_review.md](handoff/22_rev3_review.md) | [upstream/14_pilot_rev4_and_dryrun.md](upstream/14_pilot_rev4_and_dryrun.md) | R-C25、R-C26 | — | PASS（列高待裁） |
| 15 | 2026-08-15 | **pilot rev5** —— TC-007 判定、Owner 前置、列高前例量測 | [handoff/23_rev4_review.md](handoff/23_rev4_review.md) | [upstream/15_pilot_rev5.md](upstream/15_pilot_rev5.md) | R-C27 | — | PASS（列高待裁） |
| 16 | 2026-08-15 | **寫回執行** —— 三段逐驗，止於 Excel 確認前 | [handoff/24_rc28_three_questions.md](handoff/24_rc28_three_questions.md)＋[handoff/25_writeback.md](handoff/25_writeback.md) | [upstream/16_writeback.md](upstream/16_writeback.md) | R-C28 | DELIVERY ENTRY 002 | PASS（gate 5/5、assertion 9/9；**未經 Excel 確認**） |
| 17 | 2026-08-15 | **A-CF02 交付夾一致化** ＋ 三項待補檢查 | [handoff/26_writeback_review.md](handoff/26_writeback_review.md)＋[handoff/27_acf02_baseline_alignment.md](handoff/27_acf02_baseline_alignment.md) | [upstream/17_acf02_and_gates.md](upstream/17_acf02_and_gates.md) | — | A-CF02 RESOLVED | PASS（lint 32→35，三項皆反向驗證） |
| 18 | 2026-08-15 | **批次 2 Tri-Mode Climate** —— 11 生成 / 3 停下 | [handoff/28_no_delivery_batch2.md](handoff/28_no_delivery_batch2.md) | [upstream/18_batch2.md](upstream/18_batch2.md) | — | — | PASS（35/35，25 TC；**3.3／3.4 待軸裁定**） |
| 19 | 2026-08-15 | **批次 2 補齊** —— 第十・十一軸，Tri-Mode Climate 14/14 | [handoff/29_axes_rc29_rc30.md](handoff/29_axes_rc29_rc30.md) | [upstream/19_batch2_complete.md](upstream/19_batch2_complete.md) | R-C29、R-C30 | DELIVERY ENTRY 003 | PASS（35/35，28 TC；spec-ref 改判多節，四項反向驗證） |
| 20 | 2026-08-15 | **批次 2 定案** —— -024 拆四、forbidden-verb／er-subject-net | [handoff/30_batch2_content_review.md](handoff/30_batch2_content_review.md)＋[handoff/31_gates_anomalies.md](handoff/31_gates_anomalies.md) | [upstream/20_batch2_final.md](upstream/20_batch2_final.md) | R-C31 | A-CF17／18／19 | PASS（37/37，28 leaf / **31 TC**）|
| 21 | 2026-08-15 | **批次 3 Front Climate Anatomy** —— 9 生成 / 7 停下 | [handoff/32_rc32_batch3.md](handoff/32_rc32_batch3.md) | [upstream/21_batch3.md](upstream/21_batch3.md) | R-C32 | A-CF20／21 | PASS（37/37，37 leaf / **40 TC**；2.1／2.14 待軸與條文衝突裁定）|
| 22 | 2026-08-15 | **批次 3 補齊** —— 第十二・十三軸、§4.1 實質複查 | [handoff/33_rc33_axes.md](handoff/33_rc33_axes.md) | [upstream/22_batch3_complete.md](upstream/22_batch3_complete.md) | R-C33 | A-CF21 RESOLVED-BY-RULING｜DR #17／18／19 | PASS（37/37，42 leaf / **45 TC**；2.1-01／-02 阻塞於 DR #17）|
| 23 | 2026-08-15 | **回溯複查** —— 既有 31 條補 18 行 PC；-045 拆二 | [handoff/34_retro_review.md](handoff/34_retro_review.md) | [upstream/23_retro_review.md](upstream/23_retro_review.md) | — | — | PASS（37/37，42 leaf / **46 TC**）|
| 24 | 2026-08-15 | **批次 4 Temperature and Fan** ＋ 介面型軸補掃 | [handoff/35_rc34_batch4.md](handoff/35_rc34_batch4.md) | [upstream/24_batch4.md](upstream/24_batch4.md) | R-C34 | A-CF22 | PASS（38/38，60 leaf / **64 TC**；2.7.1 待第十四軸裁定）|
| 25 | 2026-08-15 | **ch16 鏡射表** ＋ interface-axis-answered／pending-sibling | [handoff/36_rc35_mirror_gates.md](handoff/36_rc35_mirror_gates.md) | [upstream/25_mirror_and_gates.md](upstream/25_mirror_and_gates.md) | R-C35 | DR #20 | PASS（40/40，60 leaf / 64 TC；**5 條 EMEA 排除過嚴待裁**）|
| 26 | 2026-08-15 | **移除 5 條過嚴 PC**、第十四軸、單一來源、sibling 候選 | [handoff/37_mirror_fixes.md](handoff/37_mirror_fixes.md) | [upstream/26_mirror_fixes.md](upstream/26_mirror_fixes.md) | R-C36、R-C37 | A-CF13 增記 | PASS（40/40，61 leaf / **65 TC**；Temperature and Fan 19/19）|
| 27 | 2026-08-15 | **R-C36-1 逐條補答** ＋ 批次 5 全停（ECO HVAC）| [handoff/38_rc36_1_batch5.md](handoff/38_rc36_1_batch5.md) | [upstream/27_batch5.md](upstream/27_batch5.md) | R-C36-1 | DR #21 | PASS（41/41，61 leaf / 65 TC；**5 條過嚴 ＋ 1 條判不出待裁；ch10 待第十五軸**）|
| 28 | 2026-08-15 | **第十五軸 ＋ 批次 5 ECO HVAC**；移除 6 條過嚴 PC | [handoff/39_emea_removals_axis15.md](handoff/39_emea_removals_axis15.md) | [upstream/28_batch5_axis15.md](upstream/28_batch5_axis15.md) | — | — | PASS（41/41，75 leaf / **80 TC**；044-02 待白名單裁定）|
| 29 | 2026-08-15 | **044-02 補證** ＋ 686 對候選分級判定 ＋ 等價組擴充 | [handoff/40_evidence_and_candidates.md](handoff/40_evidence_and_candidates.md) | [upstream/29_candidates_and_evidence.md](upstream/29_candidates_and_evidence.md) | — | A-CF23／DR #22／#23 | PASS（41/41，75 leaf / 80 TC；**AUTO 與 MODE 兩類判定失效，231 對待逐對**）|
**編號說明**：下放包 02 為 01 之補遺（補其 open PENDING P-C1／P-C2），
兩者於同一次往返內處理，故上繳只有一份，02 不另編往返序。下放包 03（覆核
＋ Phase 2 指示）與 04（D-C8/D-C9 裁決）同屬第二次往返，合併上繳為 02；
05／06 合併為上繳 03；07／08 合併為上繳 04；09／10 合併為上繳 05；11／12 合併為上繳 06；13 單獨上繳 07；上繳 08 對應 Pei 之直接指示，無下放包編號；14 單獨上繳 09。
**09 之六項作業於上繳 04 當輪未收到，於上繳 05 補做**（見該包 §0 甲）。

**上繳 04 待知悉 2 項**（詳見該包 §0）：
- **甲** DR #7 已解、DR #6 限縮至 7"，但**都不是靠 08 供入的素材解的** ——
  Market Config Table 對 `R1L-R` 與螢幕尺寸皆 0 命中；解答來自 037 自身
  之引用結構（R-C13 換路徑之直接應用）
- **乙** 判讀淨變動為「±」：20.x 十節依 R-C12 降級，16.1 與 18.2–18.4
  四節依結構證據升為 `in_scope`。另有一界線待分析層決定 —— **R-C12 是否
  應擴及「依據為間接證據」而不只是「來源有矛盾」**（該包 §6.2 第 3 項）

**上繳 03 待知悉 2 項**（詳見該包 §0）：
- **甲** CFTS043 作 "Altern**ate**"、SR24 作 "Altern**ative**"；以 SR24 用詞
  搜尋得 0 命中，差點誤判 10 節為 `out_of_scope`（A-CF11）
- **乙** CFTS043 4803259 之 NOTE 與其 `Radio`／`Scope` 欄矛盾；10 節之
  `in_scope` 繫於「採結構化欄位」之選擇（A-CF12）—— **D-C10 宜待其釐清**

**上繳 02 待裁 2 項**（詳見該包 §0；甲項已由 R-C5-1 處置）：
- **甲** R-C5 所列 22 節中之 16 節同時存在於 SR24 基線，out-of-scope 之推論
  對其失效 —— 牽動驗證範圍，宜於 Phase 3 前裁定
- **乙** 04 §2 稱全部 feature 未簽署之前提有誤（amfm／sxm 已簽）——
  結論不受影響，訂正理由

---

## 2. 現況

| 項目 | 值 |
|---|---|
| Phase | **4 進行中** —— pilot **rev5**：12 條 TC ＋ 2 條 `[BLOCKED-SPEC]` row，lint **32 gate** 全 PASS。**寫回仍未執行** |
| workbook_state | `BLANK` |
| spec_mode | `A`（SYS1 export） |
| baseline | SR24 CR24879（R-C1；SR25 out of scope） |
| leaves | 403 |
| open PENDING | **無**（DR #8 已轉 DEFERRED，自阻塞清單移除）|
| open anomaly | A-CF02、A-CF04、A-CF08、A-CF09、A-CF13、**A-CF14**（A-CF06／A-CF07／A-CF10 CLOSED；A-CF11 升格 R-C13；A-CF12 DEFERRED）|
| 真正缺檔 | **2 件**：7" 螢幕配置來源（DR #6，擋 3 節）；HMI Pop Up List（DR #11 —— 入口問題已裁，urgency 降為影響 Phase 4 措辭）|
| 適用性判讀 | **4 `in_scope`／13 `undetermined`／0 `out_of_scope`**（17 節）；4 節依 R-C16 為 **RD-1 覆蓋缺口項，非 TC 工作項** |
| Layer 3 map | **129 節／403 leaves**，三個 assertion 全 PASS；section↔parent 為 1:1 雙射 |
| **Part N** | Test Group `Comfort`；**15 個 Test Set**；leaf 區間 **14–59**，最大者 14.6%。兩次修正：#15 更名（13 §2）、**四節改置**（14 §1）。七項 assertion 全 PASS |
| 全文基礎 | `data/section_fulltext.tsv` —— 129 節不截斷全文（R-C18）。長度 min 27／中位 245／max 1232 |
| Phase 4 開始條件 | ① profile 簽署 ✅ ② G-1 PASS ✅ ③ A-CF07 經 Pei 於 Excel 確認 ✅ 2026-08-15 —— **三者齊備，Phase 4 已開始** |
| pilot | **14 條已生成**，lint 25/25 PASS（六 gate 經注入缺陷反向驗證）。19 之五問全裁：第九軸已入 profile、`(-, +)` 依位置分割、13.4/13.5 in scope 但收窄、R-C22 免除 BLOCKED、A-CF14 依 R-C21 登於 Comfort |
| rev3 之裁定 | TC-010／TC-012 依 **R-C24** 產 `[BLOCKED-SPEC]` row —— 併入 sibling 違反 §8.2.2、維持現狀則為 §7 之 False Pass，故三選一皆不採 |
| rev2 之 gate 補齊 | §10.1 `required-keys`、§10.4 `reasoning-sentences`、§10.5 `proc-min-steps`、§10.6 `duplicate-of-format` —— **四者當時皆為實際違反**，非預防性 |
| rev3 之 gate 補齊 | `blocked-row-empty`、`blocked-remarks` ＋ **具名豁免回報行**（R-C24：豁免不得為條件式中之靜默跳過）|
| rev4 之 gate 補齊 | `marker-whitelist`（R-C26：豁免不可自取）—— 與 R-C24 互補：前者使豁免**可見**，後者使豁免**不可自取** |
| **寫回待裁** | ⚠️ **列高**：14 列全部 `customHeight=True, height=14.0` 而 `wrapText=True` —— 折行但不長高。**前例已量**：Privacy 之實際交付件（同一空白範本、欄寬完全相同）**同樣受限**；home／SXM 起自已調版 instance，不構成反例。惟判定規則之第二半（客戶未見反映）**執行層無從驗證** |

---

## 3. 權威在哪裡

| 檔案 | 內容 |
|---|---|
| `RULINGS.md` | R-C1 ~ R-C27 + R-C4-1 + R-C5-1 逐字（29 條），加執行層落實回報 |
| `DECISIONS.md` | 決策表 —— **已簽署 2026-08-14**，受 R-C9 保護。§6 含兩次修正案，**Sign-off 未重簽** |
| `RECON.md` | Phase 1 survey + assertion 實測值 + uncited baseline sections |
| `ANOMALIES.md` | A-CF01 ~ A-CF26（A-CF13 含四項 spec 內部瑕疵；A-CF23 含 12 條 TC 之影響清單與 18 leaf 之待辦名單；**A-CF26 為跨 feature —— 範本 DV 涵蓋不足，具名對象 privacy，不代改其檔案**）|
| `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md` §5 | **四類 marker ＋ 判別次序** —— §5.1 `[BLOCKED-SPEC]`（R-C24）、§5.2 `[BLOCKED-NON-HMI]`（R-C38）、§5.2a `[COVERED-BY]`（R-C39，**非缺口**）、§5.3 對照與四出口次序、§5.4 R-C16 不產列者、§5.5 推導欄之重算風險 |
| `DATA_REQUESTS.md` | #1 ~ #40 + standing rule（**#32 對照關係未定義／#34 入口或操作方式未定義**為類項，同類合併不另開；類項標題須隨成員更新，見 `RUNBOOK.md`）（#12 跨 feature；#16 為 Core N0／CFTS044 之**涵蓋**問題，與 #13/#14 之「要不要取得」不同；#24 為 `044-02` 之 VM 分類，RD-1 候選）|
| `RUNBOOK.md` 末段 | **判準 vs 用詞禁令**（22 §4）—— 與 R-C13／R-C18 同源：以表徵為判準者，其失敗形態是靜默的 |
| `feature.yaml` | pipeline 常數與裁決常數（`recon_assertions`） |
| `data/spec_id_to_outline.tsv` | 403 leaf → SR24 outline 之查表（追蹤入版控） |
| `data/sr24_uncited_sections.tsv` | SR24 基線內 51 節未被引用者之四值分類（A-CF08） |
| `data/sr24_substantive_applicability.tsv` | 17 節 substantive 之適用性判讀（含 `pending_on`／`disposition`）|
| `data/layer3_map.tsv` | **Layer 3 map** —— 129 節 × 六欄，Part N 之輸入 |
| `framework.md` | **Part N** —— Layer 1/2/3 之定義與對照（Layer 3 不入工作簿）|
| `data/test_set_map.tsv` | section → Test Set 查表（129 列），Phase 4 用；非工作簿內容 |
| `data/section_fulltext.tsv` | **129 節不截斷全文**（R-C18）—— 判讀一律以此為據，不用 `layer3_map` 之 60 字標題 |
| `data/source_tokens.tsv` | §3.4 窮盡性 —— 189 個相異 token 之全集（17 §3.1） |
| `data/ch16_mirror_map.tsv` | ch16（EMEA ICS）↔ ch2／ch3 之鏡射表，31 列，含 `partial` 之行為分界（R-C36／R-C36-1）|
| `data/ch2_ch7_mirror_map.tsv` | **前後排鏡射表**，26 列 —— ch2 全 22 節與 ch7 全 11 節**雙向全列**（含 `no-counterpart`），`partial` 者必填行為分界。231 對之結構解，亦為 `Rear Climate`（46 leaf）生成時之依據 |
| `data/pending_sibling.tsv` | 跨 Test Set sibling 候選之判定台帳，**1668 列**（`vocab` 1588／`via-hierarchy` 80）。欄位含 `provisional`（42 §1／43 §1）、`source`（43 §2／44 §4）與 **`equivalent_tc_pairs`（52 §1 —— 條級嚴格等價，`duplicate_of` 之節級欄位表達不了者）**。verdict 四值：`sibling`／`not-sibling`／`not-broken-by-3-samples (class)`／`deferred`；另有 `provisional` 欄（42 §1）—— **機器維護，不得手工增修**，以 `sibling_candidates.py --rebuild` 全量重建＋鍵合併（R-C37：本表非完備性證明）|
| `data/image_leaves.json` | 037 之 25 個帶圖 leaf（52 張）之實測名單，含節次、Test Set、是否已生成（A-CF23 / 42 §4）|
| `scripts/verify_provisional_gate.py` | `provisional-sibling` gate 之**反向驗證** —— 六個方向性案例（含舊觸發會答錯的那一個），證其該響時響、不該響時不響（42 §1／43 §1）|
| `scripts/verify_axis_type_gate.py` | `axis-type-reverse-test` 之**反向驗證** —— 含「無區塊即失聲」與**目的版檢驗**（其措辭問軸所轄之功能，而其目的是別條 TC 失去觀察端；兩者發散，故兩版皆跑）（52 §3）|
| `scripts/verify_axis_gate.py` | `axis-value-count` gate 之**反向驗證** —— 五個軸區塊、模擬增值必 FAIL、未受保護之否定式 PC 必觸發（43 §4）；另驗每塊皆有 `scan:` 且載明窮盡之類別（44 §6）|
| `data/interface_axis_review.tsv` | 每節之四個介面型軸答案（R-C34，36 §6）|
| `data/emea_ics_per_tc.tsv` | 每條 TC 之 EMEA ICS 排除判定（R-C36-1，38 §1）|
| `data/config_axis_candidates.tsv` | §3.2 窮盡性 —— 18 筆軸候選（17 §3.2；**115 節無匹配 ≠ 無配置條件**，R-C13） |
| `generated/*.json` | **pilot 14 條**（7 個 parent），含 `source_clause`／`reasoning`／sibling 判定 |
| `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md` | **profile [OVERRIDE]**，已簽 2026-08-15（15 ＋ 16 §1） |
| `BASELINE.sha256` | 素材基準 **8 檔** —— inputs/ 5 ＋ spec-index/ SR24 三件（涵蓋範圍為執行層判斷，見上繳 09 §0 乙） |
| `DELIVERY.sha256` | 產出台帳 append-only —— 001 範本清列／002 pilot（superseded）／003 交付夾附件／**004–021 為十八次全量寫回（…／383 × 5／385／429）／**022 範本擴充驗證**／**023 首次自擴充後母本之寫回（429 列，14/14 PASS）**／**024–025 該檔被 Excel 重存之實測與歸檔**／**026 R-C45 解封後之寫回（434 列，14/14 PASS）**／**027 交付前複驗**／**028 `type: delivered`（2026-08-17，附 corpus-divergence 增註）**／**029 交付說明訂正版就位**／**030 J 欄去標籤 ＋ I 欄兩段式之寫回（434 列，assertion 15/15 PASS，未交付）** —— 004～021 皆**不可交付**（範本容量，DR #35 / A-CF26）；**023 之阻塞已解除，待 Excel 四項確認**|
| `output/STATUS.md` | 產出狀態之可讀摘要（不參與 `shasum -c`；標記寫在檔案旁邊而非檔案裡，改檔即改 hash）|
| `RUNBOOK.md` | feature 事實之權威 |
| `PLAYBOOK.md` | 狀態板 |

`docs/handoff/` 為分析層下放包，`docs/upstream/` 為執行層上繳包，
兩側皆不改對方之檔。

---

## 本 feature 已結案（Pei 裁定，2026-08-17）

**文件止於 `handoff/93_close.md` 與 `upstream/72_closed.md`。**
最後一份內容性上繳為 **`upstream/71_gap_context_recheck.md`**（20 個缺口之五層查證，
20/20 判定不變）；`72` 為結案確認，不含新的分析。

`handoff/92` 之 §6 四項作業**已撤銷**（見該包 §8 之增註）——
**撤銷的是後續作業，不是 71 之結論**。

狀態、交付物與其兩項未收束事項見 `../PLAYBOOK.md` §6。
