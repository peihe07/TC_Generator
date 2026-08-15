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
| 09 | 2026-08-15 | Part N 修正案 ＋ **profile 簽署** ＋ G-1 ＋ A-CF07 備妥 | [handoff/14_partN_amendment.md](handoff/14_partN_amendment.md)、[handoff/15_profile_draft.md](handoff/15_profile_draft.md)、[handoff/16_profile_signed.md](handoff/16_profile_signed.md) | [upstream/09_partN_amendment_and_profile.md](upstream/09_partN_amendment_and_profile.md)（含 [09_partN_amendment.md](upstream/09_partN_amendment.md)） | R-C19、G-1 gate | A-CF07 待結案 | PASS（2 項待裁示） |
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
| Phase | **3 完成** —— Part N ＋ **profile 皆已簽署**。`DECISIONS.md` 兩筆 Sign-off（Part N 08-14／profile 08-15）。**Phase 4 未開始** —— 僅差 Pei 之 Excel 確認 |
| workbook_state | `BLANK` |
| spec_mode | `A`（SYS1 export） |
| baseline | SR24 CR24879（R-C1；SR25 out of scope） |
| leaves | 403 |
| open PENDING | **無**（DR #8 已轉 DEFERRED，自阻塞清單移除）|
| open anomaly | A-CF02、A-CF04、A-CF07、A-CF08、A-CF09、A-CF13（A-CF06／A-CF10 CLOSED；A-CF11 升格 R-C13；A-CF12 DEFERRED）|
| 真正缺檔 | **2 件**：7" 螢幕配置來源（DR #6，擋 3 節）；HMI Pop Up List（DR #11 —— 入口問題已裁，urgency 降為影響 Phase 4 措辭）|
| 適用性判讀 | **4 `in_scope`／13 `undetermined`／0 `out_of_scope`**（17 節）；4 節依 R-C16 為 **RD-1 覆蓋缺口項，非 TC 工作項** |
| Layer 3 map | **129 節／403 leaves**，三個 assertion 全 PASS；section↔parent 為 1:1 雙射 |
| **Part N** | Test Group `Comfort`；**15 個 Test Set**；leaf 區間 **14–59**，最大者 14.6%。兩次修正：#15 更名（13 §2）、**四節改置**（14 §1）。七項 assertion 全 PASS |
| 全文基礎 | `data/section_fulltext.tsv` —— 129 節不截斷全文（R-C18）。長度 min 27／中位 245／max 1232 |
| Phase 4 開始條件 | ① profile 簽署 ✅ ② G-1 PASS ✅（附 provenance 但書）③ **A-CF07 經 Pei 於 Excel 確認四項 ⏳ —— 唯一未達成** |

---

## 3. 權威在哪裡

| 檔案 | 內容 |
|---|---|
| `RULINGS.md` | R-C1 ~ R-C19 + R-C4-1 + R-C5-1 逐字（21 條），加執行層落實回報 |
| `DECISIONS.md` | 決策表 —— **已簽署 2026-08-14**，受 R-C9 保護。§6 含兩次修正案，**Sign-off 未重簽** |
| `RECON.md` | Phase 1 survey + assertion 實測值 + uncited baseline sections |
| `ANOMALIES.md` | A-CF01 ~ A-CF13（A-CF13 含三項標籤衝突）|
| `DATA_REQUESTS.md` | #1 ~ #11 + standing rule |
| `feature.yaml` | pipeline 常數與裁決常數（`recon_assertions`） |
| `data/spec_id_to_outline.tsv` | 403 leaf → SR24 outline 之查表（追蹤入版控） |
| `data/sr24_uncited_sections.tsv` | SR24 基線內 51 節未被引用者之四值分類（A-CF08） |
| `data/sr24_substantive_applicability.tsv` | 17 節 substantive 之適用性判讀（含 `pending_on`／`disposition`）|
| `data/layer3_map.tsv` | **Layer 3 map** —— 129 節 × 六欄，Part N 之輸入 |
| `framework.md` | **Part N** —— Layer 1/2/3 之定義與對照（Layer 3 不入工作簿）|
| `data/test_set_map.tsv` | section → Test Set 查表（129 列），Phase 4 用；非工作簿內容 |
| `data/section_fulltext.tsv` | **129 節不截斷全文**（R-C18）—— 判讀一律以此為據，不用 `layer3_map` 之 60 字標題 |
| `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md` | **profile [OVERRIDE]**，已簽 2026-08-15（15 ＋ 16 §1） |
| `BASELINE.sha256` | 素材基準 **8 檔** —— inputs/ 5 ＋ spec-index/ SR24 三件（涵蓋範圍為執行層判斷，見上繳 09 §0 乙） |
| `DELIVERY.sha256` | 產出台帳 append-only —— ENTRY 001 = 範本清列（A-CF07） |
| `RUNBOOK.md` | feature 事實之權威 |
| `PLAYBOOK.md` | 狀態板 |

`docs/handoff/` 為分析層下放包，`docs/upstream/` 為執行層上繳包，
兩側皆不改對方之檔。
