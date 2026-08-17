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
| 2 | `HMI Pop Up List`（pattern：`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` 或其 R1L-R 對應版）| 未到齊 | spec 8.3 明文「Specific popups can be found in the HMI Pop Up List」；spec 全文另有 PU0585／PU0626／PU1573 等 PU id | Phase 3 profile 之 popup 詞彙表與 lint `popup_ids` 無來源；引用 PU 字面值之 TC 無法回溯 | A-UP06 | 高（Phase 3 前）|
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
