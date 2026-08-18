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
| 4 | **Pop Up List 中 `PU1087`／`PU1088` 兩列之 popup 內文**（非整份版本 —— **索取標的已於 06 輪依 R-U27 收窄**）| MISSING | `PROF-002-03`（`4.1.1`）| **不再擋章節**：spec PDF p6 已載該二 popup 之**觸發條件**，故觸發、顯示與否、流程分支皆可驗；**僅其 popup 內文之逐字 ER 不寫**（§8.4.1 不推定內容）| A-UP06 | **MEDIUM**（原 高；R-U27 降級）|
| 3 | spec `3.1`–`3.5`（PLP1–PLP5）等 8 條之上游釐清 —— **性質已改為「上游覆蓋缺口」**（R-U28），非索取缺件 | 未送出 | 0（現況無 leaf 對應）| 不阻擋生成。`3.1`–`3.5` 有內容且可讀 → 依 R-U22 作 `PROF-001-01` 之 in-scope 依據；`10.1`／`11.1`／`11.2` 為變體覆寫條款且無 SWE 需求 → 列 RD-1 | A-UP02 | 中（RD-1，Tier 3 由 Pei 送出）|

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


## 第 3／4 列之性質變更（06 輪，R-U27／R-U28）

**DR #4 之索取標的收窄**：原列「載有 PU1087／PU1088 之 Pop Up List 版本」，
**現改為「該二列之 popup 內文」**。依據：spec PDF p6 逐字載

> `PU1087` is displayed when users confirm Setting restore to default by
> pressing Yes in pop-up `PU_0118`. `PU1088` is displayed when settings have
> been successfully restored to default.

**即觸發條件 spec 自己給了，缺的只是那兩個 popup 上寫什麼。**
故 `4.1.1` 之 TC 得以生成，`PROF-002-03` 解除阻斷，本列由 HIGH 降 **MEDIUM**。

**DR #3 之性質改變**：由「索取缺件」改為「**上游覆蓋缺口**」——
`3.1`–`3.5` 之內容**存在且可讀**（05 輪自 PDF p5 抽出逐項清單），
037 只是沒有為它們產出 leaf。形態同 Comfort **R-C16**。

---

## RD #5 —— R1 High 之 label 覆寫，其範圍是否及於全章（19 輪，J-7）

**問題**：`****R1 High Only: "Stellantis Account" to be replaced with
"Connected Account"` 之覆寫，**在版面上為列級** —— 其 `****` 標記與
PDF p14 之 Table EDPR1 中 `****“ Stellantis Account”` 那一列對應
（座標複位：註記於 x=101.4／y=275.9–286.7，該列於 y=289.8；表中其餘列無 `****`）。

**其是否推及全章之同名 label，版面無從判定。** 具體受影響者：

| 節 | 該節自己的字 | 若覆寫及於本節則應為 |
|---|---|---|
| 9.2（EDPR2）| `Stellantis Connected Account button` | `Connected Account button` |
| 9.1（EDPR1）| `Stellantis Connected Account will link to Connected Profile app` | `Connected Account will link to…` |

**現行處置（J-7）**：ER 維持各節之逐字；`PROF-088`（TC-020）之 remarks
註明兩形式指同一按鈕，且該 TC 驗的是**缺席**而非 label 內容，故不影響判定。

**索取標的**：該覆寫之適用範圍 —— 僅 Table EDPR1 之該列，或及於 ch9 全章之同名 label。

**若答案為「及於全章」**，須連帶處理：`lint_variant_labels` 之
`VARIANT_LABEL_OVERRIDES` 適用範圍、`PROF-085`（TC-017）之列項字面值
（現已用 Connected Account，屆時無須改）、以及 9.1／9.2 之 ER 逐字。

**性質**：spec 之歧義，非我方判準問題（§8.4.1「ambiguous source → preserve
ambiguity」）。**併 DR #3 之上游問題群送出。**
