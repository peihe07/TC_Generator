# 18 — Comfort HMI / A-CF07 結案、Phase 4 起跑、pilot 批

- 產出層：分析層｜2026-08-15｜對象：執行層
- 確認：Pei，2026-08-15（「OK」）—— A-CF07 四項 Excel 確認全數通過
- 承接：`16_profile_signed.md` §3.2、`17_g1_baseline_exhaustiveness.md` §5

---

## 1. A-CF07 CLOSED

`output/…_SWQT_Comfort_20260815_prepared.xlsx`（SHA256 `b68117a211b08009…`）
經 Pei 於 Excel 開啟，四項確認全數通過：

1. 無修復提示
2. R 欄下拉可用且為九項
3. D5 Scope 正確
4. 第 10–11 列已清且無殘留列號

**A-CF07 結案。** `DELIVERY.sha256` ENTRY 001 之狀態欄由「未經 Excel 確認」
改為 **`Excel-confirmed by Pei 2026-08-15（四項）`** —— 該欄為狀態更新，
非改寫既有記載；ENTRY 001 之 hash 與內容不得變動（append-only）。

此為 Comfort 首次確認 zip-level surgical path 於本 feature 可行。
程式層檢查（48 members、DV counts、五格清空、B 欄公式完整）已於上繳 09b
記載，**但那些不能代替 Excel 自身之檔案完整性判定** —— 兩端俱備方為完整。

---

## 2. Phase 4 起跑條件 —— 三者齊備

| 條件 | 狀態 |
|---|---|
| G-1 PASS | ✅ 2026-08-15（下放包 17 §1） |
| profile 落檔 | ✅ `FW036_R1L_Comfort_Profile.md` |
| A-CF07 經 Pei 於 Excel 確認 | ✅ 2026-08-15（本包 §1） |

**Phase 4 開始。**

---

## 3. pilot 批 —— `Seat Control Tab`

| 項 | 值 |
|---|---|
| Test Set | `Seat Control Tab` |
| Layer 3 | 13.2、13.2.1、13.3、13.3.1、13.4、13.5、13.6 |
| leaves | **14**（3 / 1 / 2 / 2 / 2 / 2 / 2） |
| req_ids | `SWE1-HVAC-076` ~ `-082` |
| tc_id | `NR1L-ComfortHMI-001` 起，generator 指派 |
| 條文來源 | `data/section_fulltext.tsv`（**不得讀 `layer3_map.tsv` 之截斷標題**，R-C18） |

**13.1 不在本批** —— 其 categorization 為 `assumption`，未被 037 引用。
其內容（`lower comfort screen` 之有無影響座椅／腰靠控制之可及性）為背景，
**得於 `reasoning` 提及，不得作為 `specification_reference`，
不得據以產生 TC**（§8.4.2、R-C16）。

### 3.1 本批必須遵守之 profile 條款（逐項可查）

- **Test Item（I 欄）**：以 spec 語言濃縮之需求陳述，**modal 僅此欄允許**
  （G-1 PASS，profile §3.1）。JSON 仍須產出無 modal 之 `tc_title`
  （2–14 words）供 lint 與 sibling 判別
- **`pre_conditions`**：每一句標 source class
  （`spec-verbatim` / `spec-derived` / `test-setup`）；**未標者視為未追溯**。
  配置條件須具名其來源節次，不得以「某些車輛有此配置」概括（§8.4.1）
- **`specification_reference`**：
  `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)_{outline}`
  —— stem 固定，不得改寫為 SR25（R-C1）
- **`design_method`**：`下拉選單!A1:A9` 九字串之一，逐字元相符
- **`priority`**：P0 / P1 / P2 / P3
- **Q 欄留白**（`UNRULED_BLANK`）、**S 欄 `NA`**、**T–Z 欄留白**、
  **Remarks 空字串**
- **workbook 欄位英文、無 emoji、無行尾句點**；UI label 用 `"..."`，
  source token 照錄（profile §3.4）
- **Layer 3 不入 workbook**；N 欄承載 section 係 traceability，不得留白

### 3.2 sibling 注意

`13.2` / `13.2.1` 與 `13.3` / `13.3.1` 為母子節對。依 §4.6 作 sibling 判定；
`axis="none"` ⇔ `duplicate_of` 有值。`13.5` / `13.6`（短按增減 vs 到達
上下限）為同一控制之相鄰行為，須以 `distinguishing_axis` 明確區隔，
**兩者 tc_title 不得讀來相同**（§4.3 sibling-distinction）。

### 3.3 stop-and-report（不得自行決定，回報後停）

- 需要新的 marker（profile §5：目前無 marker，新增須先裁決）
- 遇到 profile §3.2 未列之配置軸
- 遇到 profile §3.4 未列之 source token
- 條文有歧義而任何補值都會構成 §8.4.1 之造值
- 條文所述行為之擁有者疑為其他 spec（§8.4.2、R-C17）

### 3.4 本批**不做**

- **不寫回 workbook。** pilot 為 generation ＋ lint，寫回於 pilot review
  通過後另行下放
- 不指派 pilot 以外之 tc_id
- 不動 `framework.md`、`profile`、`RULINGS.md` 之既有條文

---

## 4. 併同執行 —— 下放包 17 §5 之窮盡性掃描

17 §3.1 / §3.2 之兩項掃描（`data/source_tokens.tsv`、
`data/config_axis_candidates.tsv`，含隨機 15 節人工過目、seed 固定）
**與 pilot 併入同一次往返**，共用上繳包。

順序建議：**先掃描、後生成** —— 掃描若發現 profile §3.2／§3.4 有缺，
pilot 之 `pre_conditions` 與 token 處理即受影響，先掃可省一次重做。

---

## 5. 上繳與 pilot review

上繳 `docs/upstream/10_pilot_and_exhaustiveness.md`，須含：

1. 14 條 TC 之完整內容（JSON 與 workbook 欄位對照）
2. lint 結果（PASS/FAIL + 實測值）
3. §9 self-check 17 項之逐項自評
4. 兩份掃描 TSV 之全集與抽樣結果
5. 「本包是否仍有該驗而未驗者」之獨立判斷

分析層依 canon §1.2 作 pilot review：分層取樣；發現先分類為
**defect / style-divergence / note**，再決定是否阻塞。
**R-C19 之違反列 defect，非 style-divergence。**
reviewer 之發現須通過 done-region check 方成為 defect（done region 為
`home`，`cross-feature: style only`）。

git 不執行。

---

## 6. 本包產生之新條文清單（自檢）

無新條文。§1 為 anomaly 結案與狀態更新，§3 為作業指示。
