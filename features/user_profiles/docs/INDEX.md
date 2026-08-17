# User Profiles — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案）：scaffold／R-G1 R-G2 R-U7 form 處置／recon／outline map／framework 草案 | [handoff/01_intake.md](handoff/01_intake.md)＋[01a_rulings.md](handoff/01a_rulings.md)＋[01b_tasks.md](handoff/01b_tasks.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-G1、R-G2（全域，本包首次落檔）；R-U1 ~ R-U7（本 feature） | A-UP01 ~ A-UP03（下放包播種，A-UP03 本輪 RESOLVED）；**A-UP04 ~ A-UP09 新開** | **作業項 1／2／4(spec 側)／5(草案)／6 完成；作業項 3 停下 —— 037 不在 repo（A-UP04）＋ 預期值單位不一致（A-UP07）。相符 18／不符 4／未實測 12（4 項待裁）** |

---

## 2. 現況

### 已完成

- **Scaffold**：`features/user_profiles/` 全套就位；下放包三檔未被覆寫。
  `RULINGS.md` 含 R-G1／R-G2／R-U1 ~ R-U7 **逐字**；
  `ANOMALIES.md` 含 A-UP01 ~ A-UP09。
- **036 母本處置（R-G1／R-G2／R-U7）**：三份舊檔以 `mv` 移入
  `archive/forms_superseded/`（**未刪除**），移前移後 SHA256 一致；
  `forms/` 僅餘 `…_SWQT_20260817_ext.xlsx`。母本結構探測六項全完成並寫入
  `forms/FORMS.md`；R-G1 亦寫入 `docs/fw036/FEATURE_ONBOARDING.md` §0。
  母本未被覆寫（**openpyxl save 全 repo 未執行**）。
- **BASELINE.sha256**：4 筆（inputs/ 1 ＋ spec-index Personal Account 3），
  `shasum -c` **4/4 OK**。
- **spec 側 outline map**：169 條，單一 stem、0 unparsed、0 重複、
  `Outline Number` 169/169 一致。候選被引集合 135 條已落檔。
  spec 全文唯一 PU id **20 個**（與下放包相符）。
- **workbook_state = BLANK**：獨立實測佐證 R-U6（A–AH 全欄非空格 0）。

### 停下待裁（4 項 Tier 2）

| 項 | 內容 | 阻擋什麼 |
|---|---|---|
| **A-UP07** | 作業項 3 預期值單位不一致：182（ID 前綴形態）vs 180（Categorization）。01b 之判準下 182 不可能成立 | **Phase 1 recon 之 assertion 無合法期望值。037 到齊亦不解除** |
| A-UP05 | `20260816_ext` 之 manifest 記載與磁碟檔非同源（601 列 vs 1411 列），量測對象已不存在 | 不阻擋；FORMS.md 記載之正式處置 |
| A-UP08 | 母本無 `Test Case Framework` 分頁，而 framework.md §Workbook sync 依賴它 | 不阻擋 Phase 0；交付慣例待確認 |
| Layer 2 | Test Set 邊界三草案（7／11／6 個 Set），**037 分群不可得，草案為 spec 單邊** | Phase 3 framework Part N |

### 阻擋中（素材，Tier 3 由 Pei 送出／取得）

| DR | 檔 | Urgency |
|---|---|---|
| #1 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`（A-UP04）| **BLOCKING** —— recon 全停 |
| #2 | HMI Pop Up List（A-UP06）| 高（Phase 3 前）|
| #3 | A-UP02 之 8 條無覆蓋條文 RD-1 | 中 |

### 實作約束（已實測，非待裁）

- **A-UP09**：openpyxl 存回摧毀母本 R 欄 x14 下拉
  （`<x14:dataValidation>` 1 → 0、zip members 48 → 47，三條 legacy DV 存活）。
  Phase 6 寫回**不得**以 openpyxl 存回。`feature.yaml`
  `write_back.forbid_openpyxl_save: true`。

### 下一包之前置

1. **先裁 A-UP07**，再跑 recon —— 順序反了就會變成用實測值改期望值（§8.5）。
2. 037 到齊後：跑 `scripts/recon.py`、更新 `BASELINE.sha256`、
   以 `data/expected_cited_sections.tsv` 做 135 條**集合對集合**命中驗證。
3. Layer 2 定版後方可附 `docs/fw036/framework.md` Part（本輪刻意未附）。

---

## 3. 資料產物

| 檔 | 列數 | 說明 |
|---|---|---|
| `data/spec_id_to_outline.tsv` | 169 | section id → outline／polarion id／實體列號／字元數（tracked）|
| `data/outline_map.json` | 169 | 含 Description 全文 |
| `data/expected_cited_sections.tsv` | 135 | 候選被引 section（037 到齊後之比對基準）|
| `data/spec_popup_ids.tsv` | 20 | PU id → 引用次數／section |

腳本：`scripts/build_outline_map.py`
