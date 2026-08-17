# DATA REQUESTS — User Profiles (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/user_profiles/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx` | **MISSING** | 全部（180 母體之唯一來源）| **Phase 1 recon 完全停擺**；作業項 3 不可跑、作業項 4 之 135-id 命中不可驗、作業項 5 之 Layer 2 交集不可取 | A-UP04 | **BLOCKING（最高）** |
| 2 | `HMI Pop Up List`（pattern：`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` 或其 R1L-R 對應版）| **部分到齊 18/20**，見第 4 列 | spec 8.3 明文「Specific popups can be found in the HMI Pop Up List」；spec 全文另有 PU0585／PU0626／PU1573 等 PU id | Phase 3 profile 之 popup 詞彙表與 lint `popup_ids` 無來源；引用 PU 字面值之 TC 無法回溯 | A-UP06 | 高（Phase 3 前）|
| 4 | **載有 `PU1087`／`PU1088` 之 Pop Up List 版本**（pattern：Personal Account 之 R1L-R 對應版，或較 `SR24 Post 2A (Dec 15, 2023)` 為新之 SR24／SR25 版）| **MISSING（本輪新開）** | `PROF` 之 `4.1.1`（Profile Setup 之兩個 popup）| 該二 popup 之字面值無來源；其餘 18 個 id 已可回溯 | A-UP06 | 高（Phase 3 前）|
| 3 | spec 3.1–3.5（PLP1–PLP5）等 8 條無覆蓋條文之上游釐清 | 未送出 | 0（現況無 leaf 對應）| 不阻擋生成；PROF-001-01 之 Verification Criteria 引用 PLP 表，該表本身無 SWE 覆蓋 | A-UP02 | 中（RD-1，Tier 3 由 Pei 送出）|

## 第 1 列之實測依據（2026-08-17）

搜尋範圍：repo 全樹，加上 `~`（深度 6，排除 `Library/`、`.Trash/`）。
比對式：`-iname "*037*Personal*"`、`-iname "*Personal Account*"`、
`-iname "*PROF*.xlsx"`（大小寫不敏感，檔名比對，非內容比對）。
命中：**0 個 037 檔**。repo 內既有之 037 僅 `features/power/inputs/`、
`features/comfort/inputs/`、`features/sxm/inputs/` 三個他 feature 的。
`features/user_profiles/inputs/` 於 scaffold 後僅有 036 母本複本 1 檔。

## 第 2 列之實測依據

`data/outline_map.json` 全文（169 條 Description 欄）以 `PU[\s_]?(\d{3,4})`
掃描，得**唯一 PU id 20 個／逐引用 22 次**，與下放包 01_intake.md 之
「spec 全文唯一 PU id 20 個」**相符**。逐 id 與逐 section 對映見
`data/spec_popup_ids.tsv`，已填入 `feature.yaml` `lint.popup_ids`。

**首次量測曾得 18，係本執行層之抽取缺陷**：初版比對式 `PU\s?\d{3,4}` 漏掉
`PU_0118`（4.1.1）與 `PU_0129`（5.13.2）兩個底線分隔形態。此為 canon §5a
第 7 條（假陰性源自詞彙不全）與第 12 條（抽取式之缺陷不會報錯 —— 18 與 20
都不觸發例外）之實例，記於此以備後續同類 gate 檢查。


## 第 4 列之實測依據（R-U9 之涵蓋驗證，2026-08-17）

**量測對象**：`features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A
(Dec 15, 2023).xlsx`，工作表 `Main`，資料列 row 3–1343（**1341 列**，
A 欄非空 1341）。

**量測條件（自陳，§4.3 之漏抽同型風險）**：

| 抽取式 | 範圍 | 唯一 id |
|---|---|---|
| `\bPU\d{4}\b`（含詞界）| A 欄 | 1330 |
| `PU\d{4}`（**不含**詞界）| A 欄 | 1330 |
| `PU\d{4}` | **全表 17 欄** | 1331 |
| `PU\s*_?\s*\d{3,5}`（涵蓋底線／空白分隔）| 全表 17 欄 | 1340 |

**四式在本 feature 之 20 個 id 上結論相同**，故本次之涵蓋數與抽取式無關 ——
此點須明講：DR #2 之首次量測曾因漏抽底線形態而得 18（該次之 18 是缺陷），
**本次之 18 不是缺陷**，兩者同數而不同因。

**結果：18 / 20 命中，缺 `PU1087`、`PU1088`。**

- 兩者**落在該表之編號區間內**（`PU0001`–`PU1578`），非超出範圍；
  該區間內共 **248 個空號**，`PU1080`–`PU1088` 與 `PU1092`–`PU1095` 全為空號，
  而 `PU1089`／`PU1090`／`PU1091`（本 feature 亦引用）**在表內**
- 該表**確為正確之文件家族**：`Module` 欄 181 個相異值中含
  `Profiles`、`Profile Setup Assistant`、`Personal Account/Driver Profiles`、
  `Connected Personal Account` 等
- 兩個缺者皆出自 spec **`4.1.1`**（Profile Setup），與 `PU1088` 之 2 次引用

**處置**：依 02b 作業項 2 之明文「不足 → 具名列出缺哪幾個 id，轉 DR，
**不以近似版本替代**」——

- **未**移入 `spec-index/`
- **未**更新 `BASELINE.sha256`
- **A-UP06 不結案**

> **不以 18/20 充當到齊**：缺的那兩個正是 Profile Setup 之 popup，
> 而 spec 8.3 明文「The Profile Setup processes is a series of popups」——
> **缺口不在邊陲，在該功能的正中央。**
