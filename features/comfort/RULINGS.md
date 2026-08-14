# RULINGS — Comfort (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Comfort 之裁決權威；
跨 feature 條文承接時註明來源包。

**檔案建立於 2026-08-14**（下放包 01 §5.1）。R-C1～R-C5 原文取自
`docs/handoff/01_phase0_intake.md` §3，R-C6～R-C7 取自
`docs/handoff/02_rulings_addendum.md`，皆 2026-08-14 已簽。
Comfort 現**無 open PENDING**（01 §4 之 P-C1／P-C2 已由 R-C6／R-C7 關列）。

---

## R-C1 ~ R-C5 —— 下放包 01 §3（Pei 裁定，2026-08-14）

```
R-C1  spec baseline
Comfort feature 之 spec baseline 採 SWE.1（037）所引用者，即
SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)。

spec_reference stem 一律使用上列 SR24 檔名，與 037 之 HMI Source ID 完全一致，
不得改寫為 SR25。

SR25 CR29359 (Feb 24 2025) 於本 feature 為 out-of-scope 參考資料，不得作為
spec 來源、不得用以推翻 SR24 之字面內容、不得據以擴張驗證範圍。

依據：037 之 HMI Source ID 129/129 全數指向 SR24 CR24879；trace chain 完整性
優先於文件新舊。
```

```
R-C2  UI label 拼寫
TC 之 UI label 與狀態文字依 SR24 之拼寫與大小寫（例：AUTO、RECIRC、grayed、
A/C），不採 SR25 之 Auto／recirc／greyed／AC。

背景：SR25 對同一批 section 做過大小寫與拼寫調整；因 R-C1 定 SR24 為基線，
SR25 之拼寫不進 TC。pilot review 時若見 TC 使用 SR24 拼寫而與 SR25 不同，
不構成 defect。
```

```
R-C3  leaf 判準
leaf（驗證單位）集合 = Categorization == "Functional Requirement"，共 403 列。

禁止以 tc id 後綴形態（是否具 -NN）判定 leaf。該判準只得 369 列，會漏掉 34 列
「ID 為 parent 形態、但自身即為 Functional Requirement 且無子項」者
（例：037 row 66 SWE1-HVAC-011 Fan Speed Control、row 137 SWE1-HVAC-026
Rear Defrost Control、row 183 SWE1-HVAC-037 On/ State）。

此判準須以 recon 腳本之 assertion 機械強制（403 == Functional Requirement
計數），不得僅寫在文件裡。
```

```
R-C4  HMI Source ID 解析
HMI Source ID 儲存格取第一行為 spec section id。其後各行為 Polarion item id
（例 ..._7.3\n4803284\n4803285），共 92 列具此形態，不參與 section 解析，
保留為 audit 佐證欄位。

解析後之 section id 相異數必須為 129；不符即 fail-loud，不得靜默略過。
```

```
R-C5  SR25 新增內容之處置
SR25 outline 共 187 節，其中 58 節未被 037 引用；扣除章級容器標題、1.x
Assumptions 與影像頁後，屬實質需求而 037 未分析者為：
  18.2 / 18.3 / 18.4          （BCW1、BCW2，10.25" Comfort Widget）
  19.1 / 19.2 / 19.3          （W0、LCW1、LCW2，7" Home screen Comfort Widget）
  20.1 ~ 20.4.3（10 項）       （CRB1–CRB4.3，LATAM Alternative Rear Blower）
  21.1 ~ 21.5 + 21.3.1（6 項） （L3H1–L3H5，L3 HVAC management）

因 R-C1 定基線為 SR24，上列全部 out of scope，不產 TC、不入 coverage 分母、
不列 BLOCKED。僅以單一 note 型 anomaly 記錄其存在，供日後 037 升版時查考。

不得以「求完整」為由自行補成 RD 項目或 TC（§8.2、§8.4.2）。
```

---

## R-C6 ~ R-C7 —— 下放包 02 補遺（Pei 裁定，2026-08-14）

```
R-C6  Test Group
workbook Test Group 欄一律填 "Comfort"。

依 §4.1.1：Layer 1 Test Group 等同 spec 文件標題之模組名；spec 標題為
"Comfort HMI Logic and Flow"，故模組名為 Comfort。客戶交付路徑中之
"Climate Control Interface" 為資料夾分類，非 spec 標題，不作為 Test Group
來源。

Test Set（Layer 2）不得重複 "Comfort" 前綴（§4.2）。
```

```
R-C7  tc_id scheme
tc_id 格式為 NR1L-ComfortHMI-{NNN}，NNN 為三位零填補序號，於同一
NR1L-ComfortHMI 群組內單調遞增。

序號由 generator 指派，LLM 不得自行產生 tc_id（§10.3）。
本 scheme 自本包起凍結，生成開始後不得變更。
```

---

## 執行層回報（2026-08-14，Phase 0 → Phase 1）

以下為執行層對上列條文之落實紀錄與實測值，**非條文本身**。

### R-C1 —— 落實於三處，非僅文件

1. `feature.yaml` `spec_reference_template` 寫死 SR24 全名 stem。
2. `paths.sys1_export` / `paths.spec_pdf` 指名 SR24 全名 —— **不使用萬用字元**。
   `spec-index/cache/` 同時存有 SR25 CR29359，一個 `SYS1_HMI_Comfort_*`
   會同時命中兩份基線並讓 `resolve_glob()` 以「ambiguous」中止；寫全名是
   為了讓「取到 SR25」在結構上不可能發生，而非靠命名運氣。
3. `recon.py` assertion `spec_reference_stem`：037 全 403 leaves 之 citation
   stem 必須是且僅是 SR24 全名。實測 **PASS** —— 相異 stem 數 = 1。

### R-C3 —— 機械強制已就位（條文明文要求）

`recon.py` assertion `functional_requirement_count`，期望值置於
`feature.yaml` `recon_assertions`（Comfort 之裁決常數，非 pipeline 常數）。

- 實測：Categorization 分布 `{'Functional Requirement': 403, 'Heading': 95}`
  → leaf 計數 **403**，**PASS**。
- 同時輸出被禁判準之實測值：`-NN` 後綴形態只得 **369**，漏 **34** 列
  （`SWE1-HVAC-011`、`-026`、`-027`、`-037`、`-039`、`-041` … 全列於
  `data/recon.json` `parent_shape_functional`）。條文舉之三例
  （011 / 026 / 037）全在該 34 列內。差額 34/403 = 8.4%，與 A-CF03 相符。
- 反向驗證：將期望值改為 402 重跑，腳本輸出 `FAIL`、**不寫 DECISIONS.md**、
  以非零碼離開。assertion 為真正之閘，非裝飾。

### R-C4 —— 129 已查得，且逐節對 SR24 export 查核

- 解析規則：取儲存格第一行，其後各行為 Polarion item id，保留不解析。
- 實測相異 section 數 **129**，**PASS**。
- 具多行形態之 citation 儲存格：**57 列**（限 Functional Requirement 範圍內計）。
  條文所載之 92 列係對全部 498 資料列（含 Heading）計；兩數不衝突，統計母體不同。
- outline map 對 SR24 export（`Basic Report`，180 個 outline number，無重複）
  建立；129 節**逐一查得，miss = 0**。map 落於
  `data/spec_id_to_outline.tsv`（403 列 + 表頭，追蹤入版控）。
- fail-loud 已實作於兩處：export 缺 outline 欄或 `sys1_export` 為 null 時，
  「無基線可查」本身即記為 FAIL；查得不到之節列入 `outline_misses`。
  **不曾、也不會以「SR25 有」代替**——`sys1_export` 只指向 SR24。

### R-C6 / R-C7 —— 已寫入 `feature.yaml`

`test_group: "Comfort"`；`write_back.tc_id_format: "NR1L-ComfortHMI-{n:03d}"`。
序號由 generator 指派之約束於 Phase 4 落實，此處僅凍結格式。
