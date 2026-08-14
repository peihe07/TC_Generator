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

**編號說明**：下放包 02 為 01 之補遺（補其 open PENDING P-C1／P-C2），
兩者於同一次往返內處理，故上繳只有一份，02 不另編往返序。下放包 03（覆核
＋ Phase 2 指示）與 04（D-C8/D-C9 裁決）同屬第二次往返，合併上繳為 02；
05／06 合併為上繳 03；07／08 合併為上繳 04。

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
| Phase | 2 覆核完成，**待 Pei 簽署 `DECISIONS.md`**；Phase 3 是否開始待 Pei 裁（07 §5） |
| workbook_state | `BLANK` |
| spec_mode | `A`（SYS1 export） |
| baseline | SR24 CR24879（R-C1；SR25 out of scope） |
| leaves | 403 |
| open PENDING | **無**（D-C10 待裁，宜待 A-CF12 釐清） |
| open anomaly | A-CF02、A-CF04、A-CF07、A-CF08、A-CF09、A-CF12（A-CF10 CLOSED；A-CF11 升格 R-C13；A-CF06 半結案）|
| 真正缺檔 | **1 件**：7" 螢幕配置來源（DR #6，擋 3 節）。DR #7 已解 |
| 適用性判讀 | **4 `in_scope`／13 `undetermined`／0 `out_of_scope`**（17 節） |

---

## 3. 權威在哪裡

| 檔案 | 內容 |
|---|---|
| `RULINGS.md` | R-C1 ~ R-C14 + R-C4-1 + R-C5-1 逐字（16 條），加執行層落實回報 |
| `DECISIONS.md` | Phase 1 決策表（recon 預填，**待 Pei 簽署**） |
| `RECON.md` | Phase 1 survey + assertion 實測值 + uncited baseline sections |
| `ANOMALIES.md` | A-CF01 ~ A-CF12 |
| `DATA_REQUESTS.md` | #1 ~ #10 + standing rule |
| `feature.yaml` | pipeline 常數與裁決常數（`recon_assertions`） |
| `data/spec_id_to_outline.tsv` | 403 leaf → SR24 outline 之查表（追蹤入版控） |
| `data/sr24_uncited_sections.tsv` | SR24 基線內 51 節未被引用者之四值分類（A-CF08） |
| `data/sr24_substantive_applicability.tsv` | 17 節 substantive 之適用性判讀（含 `pending_on`，D-C10 前置） |
| `RUNBOOK.md` | feature 事實之權威 |
| `PLAYBOOK.md` | 狀態板 |

`docs/handoff/` 為分析層下放包，`docs/upstream/` 為執行層上繳包，
兩側皆不改對方之檔。
