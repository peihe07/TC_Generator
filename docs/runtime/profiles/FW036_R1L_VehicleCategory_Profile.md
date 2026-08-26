# FW036 R1L Vehicle Category — Profile

- 設立依據：**R-VC19**（下放包 11 §2.2，Pei 2026-08-26）
- 命名依既有慣例（CamelCase 無分隔，同 `VehicleSetting`／`PowerModing`／
  `UserProfiles`）—— 該慣例非由 `feature` 字串機械推導，見 R-VC1 之註。
- 母體標註依 **R-VC15**：本檔凡引用計數必標母體，限
  `145 列` ／ `117 leaf` ／ `66 section` ／ `108 outline` 四者。
- **本檔只寫當前需要者，不預先設計未來條款**（R-VC19 §2.3）——
  避免 A-VC8 家族之「宣告一個不被讀的東西」。

---

## 0. 適用範圍

| 項 | 值 | 權威 |
|---|---|---|
| feature | `Vehicle Category` | R-VC1 |
| slug | `vehicle_category` | R-VC1 |
| `test_group`（工作簿 G 欄）| `Vehicle Category` | R-VC1 |
| Layer 2 Test Set（H 欄）| 8 組 | **R-VC16** |
| `spec_reference`（N 欄）| 逐字取 037 `HMI Source ID` 欄原值，不構造 | **R-VC4** |
| 驗證母體 | **117 leaf** | R-VC3 |
| `priority` | `data/priority_final.tsv`（P0 5／P1 32／P2 45／P3 35）| R-VC11／R-VC13／R-VC14 |

---

## 1. `[OVERRIDE]` —— IN §11 引號例外之啟動

IN §11 之例外其啟動條件為「**when the feature profile says so**」。
本節即該啟動，其範圍**嚴格限定於下列四項**，逐字採 R-VC19 (a)–(d)：

**(a)** **僅 `test_item` 上半之 verbatim 區段**得保留來源記法。
037 `Requirement Title` 之 `'...'` 與 `Requirement Description` 之
`«...»` 皆為來源記法，於該區段內逐字保留，不改寫。

**(b)** **作者之散文一律 `"..."`** —— procedure 之按壓標的、
非引用之 ER 行、括號下半、reasoning，**無例外**。

**(c)** 保留之記法**須對得上所引之來源列** —— 即該 token 確實逐字出現於
該 leaf 之 `Title` 或 `Description`。lint 之職責由「禁止」改為
「驗證其來源」。**⚠ 現行 lint 無法實作本項，見 §2。**

**(d)** 本例外**不及於**任何其他欄位、不及於 `«...»` 以外之新記法。
若日後出現第三種來源記法，須另裁後始得納入，**不得類推**。

### 1.1 本例外不改動之事

R-4 之範圍**不變**。引號記法**不屬**排版正規化 ——
其改寫會使讀者無法自 TC 反推規格原文之記法，損及 verbatim 之證據力
（R-VC19 末段）。本節為 feature-scoped 之例外啟動，非全域鬆綁。

---

## 2. lint 之 profile 分流 —— **現行機制無法實作 §1(c)**

R-VC19 §2.3 第 3 項要求「先查 `scripts/lint036.py` 對 `--profile` 之
現有支援程度，**如實回報其能否實作 (c) 之驗證來源**」。

### 2.1 實測結果

`scripts/lint036.py` **有** `--profile FEATURE` 參數（21 包引入），
但其能力與 §1(c) 所需相距三層：

| # | 實測 | 影響 |
|---|---|---|
| 1 | **`--profile` 不讀取任何 profile 檔案。** `grep 'profile\s*==\|profile.lower()\|profile in '` 零命中；該值僅作**真值**使用（`:185`／`:189`／`:195`／`:496`／`:740`），其字串內容從未被讀取 | 本檔之**內容無法影響 lint** —— 傳 `--profile vehicle_category` 與傳任意非空字串等效 |
| 2 | 其作用固定為：`P` 改採 R-1 v3 判準，另啟 `Q`／`R`／`T` 三項檢查 | 無「引號記法」相關之檢查可被 profile 開關 |
| 3 | **lint036 之輸入為 `.xlsx`**（`files` metavar 為「一個或多個 .xlsx 路徑」，`openpyxl.load_workbook`），非 `generated/*.json` | pilot 未寫回，本輪之 12 筆 TC **不在 lint036 之視野內** |

另查引號相關之既有能力：`quoted_spans()`（`:294`）只認 `" "` 與 `“ ”`，
且僅供檢查 B（ER 情態詞之引號內豁免）使用。
**無禁止 `'...'`／`«...»` 之檢查，亦無「驗證保留 token 之來源」之機制。**

### 2.2 已知限制之登記

§1(c) 之「驗證其來源」**現階段無承載者**。
依 R-VC19 §2.3 第 3 項「如實記為 profile 之已知限制並登記 A-VC{n}，
**不得改 lint**」（R-VC8 之授權邊界不涵蓋 lint）：

→ 登記為 **A-VC15**（`features/vehicle_category/ANOMALIES.md`）。

**在該限制解除前，§1(c) 由人工承擔** ——
本輪之 T62 即以腳本逐筆比對 6 筆之保留 token 是否逐字出現於其
`Title`／`Description`，結果見上繳包 11 §3。該比對**不在 lint 之內**，
故不隨 lint 執行，須逐輪明列於上繳包。

---

## 3. IN §8.7.5（訊號寫法）—— 本 feature 無適用對象

037 全文掃描之 CAN 訊號、PROXI 參數、VF 引用命中數**皆為 0**
（下放包 02 R-VC10 之明文排除依據；`feature.yaml` 之 `reference:`
據此排除 `dbc_b`／`dbc_fd`／`lid`／`proxi` 四項）。

故 §8.7.5 之訊號寫法條款於本 feature **無適用對象**，記明以免日後誤引。

**推論**：`lint036 --profile` 所啟之 `P`（R-1 v3 訊號寫法）與
`RE_P3_*` 系列檢查，於本 feature 之工作簿上**應恆為零違規** ——
非因合規，而因無訊號行。日後若見該項全綠，**不得讀為「訊號寫法已驗」**。

---

## 4. 本檔未涵蓋者

下列各項**刻意未寫入**，因其現無需要（R-VC19 §2.3）：

- `[OVERRIDE]` 之其他條款 —— 本 feature 目前只需 §1 一項
- `design_method` 之 feature 專屬分流 —— 採 canon §12 首匹配，無偏差
- `test_item` 上半之 token 上限 —— 採 R-3 之 50，無偏差
- 寫回相關之條款 —— Phase 6 未啟，另裁

**未寫入不等於已裁定為預設。** 需要時另立，不得由本節之沉默推論。
