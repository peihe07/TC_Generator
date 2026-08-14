# 08 — Comfort HMI / DR #6・#7 素材落位與判讀指示

- 產出層：分析層｜2026-08-14｜對象：執行層
- 承接：`07_upstream03_review.md` §6.4

---

## 1. 素材落位實測（2026-08-14）

| 檔案 | bytes | 對來源 |
|---|---|---|
| `SR24 R1 Market Configuration Table v1.6.xlsx` | 279,779 | 一致 |

來源：`1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Reference Docs/
ECU Specific Reference Documents/`。

**大小與 AMFM 所記之 25PI3.5 release 相符**（A-AM09：273 KiB /
279,779 bytes，SHA256 `ae4cf0b9…`）。大小相符不等於內容相符（R-C14 同理），
故執行層取用前**須實測 SHA256 並與 `ae4cf0b9…` 前綴比對**；不符即停止使用
並回報，不得逕行判讀。

**版本陷阱（AMFM 前例）**：四個 release 之該檔全部標 `v1.6`，內容互不相同
—— 25PI3.5 `ae4cf0b9…`／25PI4.5 `9efae74f…`／26PI1.5 `2e66a6d9…`／
26PI2.5 `7e865d55…`。**版本標籤無法識別內容，必以 hash 對齊 release。**
Comfort 基線為 25PI3.5（與 CFTS043 一致）。

---

## 2. 判讀指示 —— DR #6／#7

以該檔續判 7 節 `undetermined`（16.1、18.2–18.4、19.1–19.3），更新
`data/sr24_substantive_applicability.tsv`。

| 節 | 待答問題 |
|---|---|
| 18.2 ~ 18.4 | 10.25" 是否屬 R1LR ATL-H 本次交付之螢幕配置 |
| 19.1 ~ 19.3 | 7" 是否屬本次交付之螢幕配置 |
| 16.1 | EMEA 是否屬本次交付之市場範圍 |

AMFM 曾以其 `Market Config - R1`、`R1 Tuner Layout` 工作表解同類問題，
可為起點，但**須先確認該工作表確實承載螢幕尺寸／市場之交付範圍資訊**，
不得以「AMFM 用過」即認定其適用於本題。

### 判讀紀律（重申，違反即退回）

- **R-C13**：零命中只能陳述索引層事實。以 `EMEA`／`10.25`／`7"` 等字串
  檢索得零命中，**不得**據以判 `out_of_scope`；應換路徑（結構化欄位篩選、
  工作表逐頁閱讀、相關詞全列舉），三路交叉仍無所獲方記 `undetermined`。
- **R-C12**：來源存在未解矛盾時記 `undetermined`，不得記 `in_scope`。
- `undetermined` 為合法結論。判不出來即標，並於 `basis` 具名缺何素材，
  同時開 `DATA_REQUESTS.md` 列。
- 本項為量測，非處置：不產 TC、不入 coverage 分母、不列 BLOCKED、
  不補 RD 項目、不改 R-C5／R-C5-1。

---

## 3. 次要候選（未經實測，暫不取用）

若 `Market Configuration Table` 不含螢幕尺寸配置，以下為**推測**候選，
取用前須先驗其確實承載該資訊，不得以「名稱像」即採：

- `VINtoArchitecture decoding v3.xlsx`（同目錄）
- `spec-index/sources/Vehicle Category HMI Logic and Flow R1 SR24 Post 2A
  (December 27 2023).pdf`

需要時於 `DATA_REQUESTS.md` 開列，由 Pei 補入（Tier 3）。

---

## 4. 作業與上繳

1. 先驗 hash，再判讀。
2. 更新 TSV（含 R-C12 之 `pending_on` 欄）與 `DATA_REQUESTS.md`。
3. 上繳 `docs/upstream/04_dr67_applicability.md`，附「本包是否仍有該驗而
   未驗者」之獨立判斷，更新 `docs/INDEX.md`。
4. `DECISIONS.md` 仍不簽署；Phase 3 仍不開始；git 不執行。

本包不產生新條文。
