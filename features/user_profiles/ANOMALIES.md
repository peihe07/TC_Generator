# ANOMALIES — FW036 User Profiles HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-UPnn]`。PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
**ACCEPTED**（15 輪起）：狀態**未改變**，是被裁定接受 ——
與 RESOLVED 不同，後者指問題已消失。兩者不得互換使用。
Registration is Tier 1 (record + propose); disposition is Tier 2.

A-UP01～A-UP03 由下放包 `docs/handoff/01_intake.md` §Anomalies 播種
（分析層 2026-08-17 實測）。A-UP04 起為執行層 Phase 0 新開。

---

## A-UP01 — SYS1 誤件（RESOLVED）

初次附上之 SYS1 為 Personal Assistant（Siri）誤件；正確 spec 已補入並通過
覆蓋驗證。

**執行層複驗（2026-08-17）**：`spec-index/cache/` 內僅有
`SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_(February_10_2023).xlsx`
一份 Personal Account spec，`Basic Report` 資料列 169，與下放包一致。
Personal Assistant 誤件不在 repo 內。維持 RESOLVED。

## A-UP02 — 8 條無 SWE 覆蓋之 spec 條文（PENDING，**性質經 R-U28 重估**）

spec 3.1–3.5（PLP1–PLP5）、10.1、11.1、11.2 共 8 條實質條文無任何 SWE
需求覆蓋，其中 PROF-001-01 之 Verification Criteria 本身即引用 PLP 表。
RD-1 候選；依 §8.4.2 不得自行吸收進 TC。

**處置**：RD-1，Tier 3 由 Pei 送出（下放包 01b §未決）。
Layer 3 骨架依 01b 作業項 5 取 spec 章 4–14，章 1–3 不入生成範圍。

**性質重估（R-U28，Pei 2026-08-17）—— 非「內容不存在」**

05 輪查明 `3.1`–`3.5`（PLP 表）**有內容且可讀**（PDF p5 之文字層載其逐項清單）。
故本條之性質為 **「spec 有而 SWE 未涵蓋」**，**形態同 Comfort R-C16**
（037 未對已存在之條文產出需求），**不是**「索取缺件」。

**兩支處置，不得混為一談**：

| 條 | 性質 | 處置 |
|---|---|---|
| `3.1`–`3.5`（PLP 表）| spec 有內容，037 未產 leaf | 依 **R-U22** 作為 `PROF-001-01` 之 in-scope 依據；**不另生成獨立 TC**（我方不自造需求，§8.2）|
| `10.1`／`11.1`／`11.2` | **變體覆寫條款**且無任何 SWE 需求 | **不生成 TC**，列 RD-1 之上游覆蓋缺口 |

**06 輪之補充實測**：`10.1` 之 xlsx Description 全文即
`R1 High Only: for the "Connected Account" category title (if applicable) the
Description is the following: "Save your preferences to the cloud and access
them from vehicle to vehicle."` —— **確為變體覆寫條款**，R-U28 之歸類由資料證實。

**DR #3 仍送出**，性質改為「上游覆蓋缺口」。

## A-UP03 — FORMS.md `20260816_ext` 條目與磁碟脫鉤（RESOLVED，2026-08-17 執行層）

`FORMS.md` 之 `20260816_ext` 條目已與磁碟脫鉤：manifest 記 123,717 bytes／
SHA256 `6d53056e…`，實測 200,654 bytes、mtime 2026-08-17 09:45:54。

**執行層處置（作業項 2，R-U7）**：實測 SHA256 =
`4b3d447051f914eb41cc9754abaa5ed89bc0f06251baf01681a18bf884b6bcf7`、
200,654 bytes、mtime 2026-08-17 09:45:54。FORMS.md 之該條目已改記實測值，
並保留 manifest 原記載（123,717 bytes／`6d53056e…`）為歷史對照，
另註明磁碟現況與原記載不同源。檔案本身依 R-G2 已移入
`archive/forms_superseded/`，移動前後 SHA 一致。
**脫鉤之成因未查明**（原記載之 123,717-byte 檔在 repo 內已不存在，
git 亦未追蹤 xlsx），此點列為 A-UP05。

## A-UP04 — 037 Analysis Report 不在 repo 內（**RESOLVED**，R-U18）

下放包 `01_intake.md` §素材 指名 037：
`FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`。

**實測（2026-08-17）**：全 repo 與使用者家目錄（深度 6，排除 Library／
Trash）搜尋 `*037*Personal*`、`*Personal Account*`、`*PROF*.xlsx` 均無命中。
repo 內既有之 037 檔僅 power／comfort／sxm 三個 feature 的，非本 feature。
`features/user_profiles/inputs/` 於 scaffold 時為空。

**後果**：01b 作業項 3（recon，預期葉節點 182／母體 180／Heading 25）與
作業項 4 之「037 引用之 135 個 id 全數命中」無法執行；R-U1 之 FROP 欄
182 列、R-U4 之兩條 Out of scope、Sub Categorization、Priority 分布
亦無法複驗。

**處置（當時）**：依 canon §0 升級條件第 1 條（missing file）停下並回報，
不改判準、不以 spec 側數字代替。已登記於 `DATA_REQUESTS.md` 第 1 列。

**解除（R-U18，Pei 2026-08-17 裁定，逐字）**

> R-U18 A-UP04 → RESOLVED
>       037 已落 inputs/，SHA 9d176dde… 入 BASELINE，
>       三閘 180／25／2 相符，表頭列實得 row 7。
>       **記載限制（永久）**：Project 附件副本不在 repo，
>       其與 inputs/ 這份之同源性永不可證。
>       故 Phase 0 之 037 側數字非「被複驗」，是「被取代」；
>       日後不得以「Phase 0 已驗過」為由跳過重測。

**永久記載限制，照錄後另加一段其效力**：

> **Phase 0 之 037 側數字沒有被複驗過，也永遠不會被複驗。**
> 那些數字量的對象是一份 Project 附件副本，該副本不在 repo，
> 本層無從對它算雜湊 —— **「大小相同」不是「內容相同」**。
> 03 輪所做的是**在一個有雜湊的物件上重新量一次**，
> 其結果恰好與 Phase 0 相符，**而「恰好相符」不等於「同一份檔」**。
> 日後任何人不得以「Phase 0 已驗過」為由跳過重測。

**實測依據（03 輪）**：SHA `9d176ddef6d013539bd33e8a74e8b67d01fba232486aaac9eedad109a783eedb`
已入 `BASELINE.sha256`（6/6 OK）；三閘 180／25／2 相符；
表頭列以 `Requirement Description` 逐格定位，唯一命中 (row 7, col 5)。

## A-UP05 — `20260816_ext` 之 manifest 記載與磁碟檔非同源（**RESOLVED**，R-U11）

A-UP03 之殘留問題。FORMS.md 記 123,717 bytes／SHA256 `6d53056e…`、
B 欄公式 row 10–601、各 DV 範圍至 601；磁碟上該檔名之檔案實測為
200,654 bytes／`4b3d4470…`、**B 欄公式 row 10–1411**、
DV `P10:Q1411`／`T10:Z1411`／`AF10:AF1411`／`R10:R1411`（x14）。
**601 與 1411 是兩份不同的檔**，非同一檔之記載誤差。

進一步實測（`20260817_ext` vs 磁碟上之 `20260816_ext`，逐格比對
34 欄 × 1411 列 ＝ 47,974 格）：**逐格差異 0 格**，zip member 48 = 48，
差異僅 `xl/workbook.xml`（Excel documentId GUID）與 `docProps/core.xml`
（`dcterms:modified` 01:45:54Z → 01:46:09Z，相隔 15 秒），檔案大小差 4 bytes。
即 `20260817_ext` 是磁碟上 `20260816_ext` 之一次「另存新檔」，
內容、DV、公式範圍、結構完全相同。

原 123,717-byte 檔在 repo 內已不存在，xlsx 未被 git 追蹤，無從還原。
故 FORMS.md 之 `20260816_ext` 條目所描述之結構事實（B 欄 row 10–601、
各 DV 範圍、與原範本之 547 格差異）**其量測對象已不可得**，
該些數值不得再被引用為現行磁碟檔或現行母本之屬性。

**處置（R-U11，Pei 2026-08-17 裁定，逐字）**：

> R-U11 A-UP05 —— 結案為「歷史記載失效」
>       20260816_ext 之 mtime 2026-08-17 09:45:54，15 秒後另存為
>       20260817_ext；容量擴充（B 欄 601→1411）發生於 FORMS.md 記載之後，
>       故原記載之量測對象已不存在。FORMS.md 維持雙欄並列，原記載留為歷史。
>       **記載限制**：本條依 Pei 裁定結案，**非經成因查證確認**。
>       兩者不同，不得日後被引為「成因已查明」。

**記載限制，照錄並自陳其效力（02b 作業項 5 明文要求）**：

> **本條之結案依據為裁定，不是查證。** 「123,717-byte 之檔到哪裡去了」
> 這個問題**至今沒有答案** —— 該檔在 repo 內不存在、xlsx 未被 git 追蹤、
> 無從還原。**「已結案」與「成因已查明」是兩件事**，
> 日後任何人引用本條時不得把前者讀成後者。

FORMS.md 依裁定維持雙欄並列（manifest 原記載 ／ 本輪實測），
原記載留為歷史，不刪除。

## A-UP06 — HMI Pop Up List 未到齊（PENDING，執行層新開）

spec 8.3 明文：`The Profile Setup processes is a series of popups. Specific
popups can be found in the HMI Pop Up List`。spec 全文另含 **20 個唯一 PU id**
（逐引用 22 次），逐一列於 `data/spec_popup_ids.tsv`。該清單檔不在
`inputs/`，亦不在 repo 內。

**後果**：Phase 3 profile 之 popup 詞彙表與 lint `popup_ids` 之字面值
（popup 標題、按鈕文字）無來源可回溯。R-U6 明定「借用之任何字面值一律重新
回溯本 feature spec，以 lint 規則強制」—— 現況下 popup 內文之字面值既不在
spec 正文、又無 Pop Up List，**任何 popup 文字都只能引 PU id 而不得引內文**。

**處置**：已登記 `DATA_REQUESTS.md` 第 2 列。本輪不生成，無實際阻擋；
Phase 3 前須到齊或另裁。

**第二輪之進展（R-U9 之涵蓋驗證，2026-08-17）—— 仍 PENDING**

R-U9 裁定「素材未必缺，先驗再說」，並指定
`features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`
為候選。**實測 18 / 20 命中，缺 `PU1087`、`PU1088`**（四種抽取式結論相同，
量測條件見 `DATA_REQUESTS.md` 之第 4 列實測依據）。

依 02b 作業項 2 之明文「不足 → 具名列出缺哪幾個 id，轉 DR，
**不以近似版本替代**」：**未移入 `spec-index/`、未更新 BASELINE、本條不結案**，
已開 **DR #4**。

**該候選確為正確之文件家族**（`Module` 欄含 `Profiles`、
`Profile Setup Assistant`、`Personal Account/Driver Profiles`），
兩個缺者亦落在其編號區間內（區間共 248 個空號）—— **不是版本不對，
是這一版就沒有那兩列**。

> **缺口之位置須記**：`PU1087`／`PU1088` 皆出自 spec **`4.1.1`**
> （Profile Setup），而 spec 8.3 明文「The Profile Setup processes is a
> series of popups」—— **缺的不在邊陲，在該功能的正中央。**
> 故 18/20 不得充當到齊，18 個可回溯亦不使 Phase 3 之 popup 詞彙表成立。

## A-UP07 — 下放包 01b 作業項 3 之預期值單位不一致（**RESOLVED**，R-U8）

01b 明定判準為「leaf = Categorization 以 `Functional` 起始者」，
預期值為「葉節點 **182**、扣除 Out of scope 2 後母體 **180**、Heading 25」。

01_intake.md 同時記載：
- 「Categorization：Functional Requirement **180** / Heading 25 / Out of scope 2」
- 「葉節點（**ID 非任何其他 ID 之前綴**）**182**；生成母體 180（R-U4 排除 2）」

**兩個數字量的是兩件事**：182 以 **ID 前綴形態**量得，180 以 **Categorization
欄值**量得。在 01b 所裁定之判準下，`Out of scope` 不以 `Functional` 起始，
故該 2 列本就不落在葉節點集合內 —— 葉節點應為 **180**，且不需再扣除 2；
「182 再扣 2 得 180」在該判準下**不可能成立**。兩條路徑恰好都得到 180，
是 canon §5a A-PJ27 型之單位巧合（數字自洽而不露破綻）。

**另據**：Comfort R-C3 逐字「禁止以 tc id 後綴形態（是否具 -NN）判定 leaf」，
並要求以 recon assertion 機械強制 Categorization 計數。ID 形態判準在該
feature 已被明文禁用；本 feature 之 182 正出自同類判準。

**處置**：依 01b「與預期不符即停並回報，不得自行調整判準」與 canon §8.5
第 2 條（不自行調和）**停下**。`feature.yaml` `recon_assertions` 之
`functional_requirement_count` 與 `heading_count` 暫留 `TBD`，
不代擬期望值。需 Tier 2 釐清後方可跑 recon。

**處置（R-U8，Pei 2026-08-17 裁定）**：**依提議裁定。** 三閘一律以
Categorization 欄之逐列計數為單位 —— `functional_requirement_count == 180`、
`heading_count == 25`（欄值等於 `"Heading"` 者，**非** `len(headings)=27`）、
`out_of_scope_count == 2`；**182 之 ID 前綴形態值降為對照輸出，不作閘**。
生成母體維持 180，不變。

裁定並明記**本項之成因為下放包之誤**，且**執行層停下為正確** ——
01b 同時寫入兩個單位不同的判準，182 在其所裁之判準下不可能量得。

**執行層落地**：`feature.yaml` 之 `recon_assertions` 三閘已由 `TBD` 改填
180／25／2。**recon 本身仍未跑** —— 037 不在 repo（A-UP04／DR #1），
作業項 6 之前置未成立。

**注意**：本項為判準層之不一致，與 A-UP04（037 不在 repo）**互相獨立**。
037 到齊亦不會使 182 在該判準下成立。

## A-UP08 — 母本無 `Test Case Framework` 分頁，而 framework.md 之流程依賴它（**RESOLVED**，R-U10）

**實測**：036 母本 `20260817_ext`（rev C）共 **9 個工作表**，
**無 `Test Case Framework` 分頁**。rev A/B（Home 之 225 列版，
`archive/forms_superseded/…Home_20260809.xlsx`）為 10 個工作表，**有**該分頁。
此差異在 `FORMS.md` 既有記載中即已存在（rev C「absent (9 sheets total)」），
本輪確認之新事實是**它有下游依賴**：

`docs/fw036/framework.md` §`Workbook sync`（Part I，Media）明文要求該分頁
「single column A, values at rows 5–14」須新增 `A15: Preset Management`、
`A16: Media Widget`，即 **Test Set 清單確實會被寫進該分頁**。

**後果**：R-U6 裁定 Test Set 欄 = FILL（逐列寫入 H 欄），這一項不受影響；
但若交付慣例另要求該分頁列出本 feature 之 Test Set 清單，
**本 feature 之母本無該載體**。

**處置（R-U10，Pei 2026-08-17 裁定）**：**採 (b)。** rev C 起
`Test Case Framework` 分頁**不列為交付要求**；`framework.md` §Workbook sync
之該項改標「**rev A/B only**」。理由：rev C 為現行官方表單且無該分頁，
該分頁係 Media 時期之工作流產物，**非 STLA 表單要求**。
**不因此產生新 DR。**

**執行層落地**：`docs/fw036/framework.md` §Workbook sync 已加 rev A/B only
之限定段落，rev C 之 Test Set 詞彙以 H 欄逐列值為唯一載體
（與 R-U6 之 `Test Set = FILL` 一致）。

**附帶**：該節之範例程式碼為 `openpyxl` + `wb.save()`，與 A-UP09 直接衝突。

## A-UP09 — openpyxl 存回會摧毀母本 R 欄 design_method 下拉（**PENDING**，解除條件見 R-U14）

**實測（2026-08-17，scratchpad 複本，repo 外；母本與 `inputs/` 複本均未被寫入，
母本 SHA `6372fb6b…` 前後一致）**：對母本複本執行
`openpyxl.load_workbook()` → `save()`，比對 `xl/worksheets/sheet6.xml`：

| 項 | 存回前 | 存回後 |
|---|---|---|
| `<x14:dataValidation>` 節點數 | **1** | **0** |
| 其 `<xm:sqref>` | `R10:R1411` | （無）|
| legacy DV（`P10:Q1411`／`T10:Z1411`／`AF10:AF1411`）| 3 | **3，存活** |
| zip members | **48** | **47** |
| 工作表數 | 9 | 9 |
| B 欄公式末列 | 1411 | 1411 |

R 欄 design_method 之 DV 是 **x14 擴充**（來源 `下拉選單!$A$1:$A$9`），
openpyxl 讀取時即發出 `Data Validation extension is not supported and will be
removed` 並丟棄之，存回時不再寫出。

**缺陷形態值得記下**：損壞是**選擇性**的（只掉 x14 那一條，三條 legacy DV
完好），工作表數、公式範圍、其他 DV 範圍全部不變，zip member 只少 1 個 ——
**表面上像是一次無害的重新封裝**，任何只比對工作表數／列數／公式之檢查
都會全綠。這是 canon §5a 第 11 條之直接實例：靜態讀取驗不到只在寫入時
才成立的性質。

**處置**：
- `feature.yaml` 已設 `write_back.forbid_openpyxl_save: true`
- 已寫入 `forms/FORMS.md` 母本條目與 `docs/fw036/FEATURE_ONBOARDING.md` §0
- **Phase 6 寫回實作不得以 openpyxl 存回**；須以 zip member 級操作
  （只替換 `sheet*.xml` 之列資料，保留 extLst）或其他保全 x14 之途徑。
  此為實作約束，非裁決事項，但因其影響交付件正確性，登記待 Pei 知悉。
- **R-G3 之 canon 修補已完成（第二輪，2026-08-17）**：
  `docs/fw036/framework.md` §Workbook sync 已加禁用警示（含本條之實測表）
  並將範例改寫為 `xlsx_surgical` splice。
- **解除條件（R-U14，Pei 2026-08-17 裁定，逐字）—— 文字修補不算**：

  > R-U14 A-UP09 之解除條件
  >       文字修補不構成 RESOLVED。解除條件 = 機器檢查存在且實跑：
  >       對產出檔驗 x14:dataValidation 節點數與 zip member 集合，
  >       比對來源母本（可借 Comfort write_back §3.3 之同型 assertion）。
  >       **該 gate 立起並實跑前，本 feature 之寫回實作不得開工。**
  >       A-UP09 維持 PENDING。

  **本層 02 輪之獨立判斷於此得到裁定確認**：02 包 §6 第 1 項自陳
  「現行防線是一段散文，沒有一道機器檢查會在有人再次 `wb.save()` 時出聲」
  —— R-U14 把那句話變成了解除條件本身。
  **04 輪未立該 gate、未開工寫回**（04c §不在授權範圍）。
- **檢查條件（依 canon §5a 第 14 條，寫成自我完備形式）**：
  寫回後之產出須「與寫回前之母本在所有可讀屬性上一致，除資料列之內容欄
  與 `No.#` 公式外」—— 涵蓋 x14 extLst、legacy DV、zip member 集合、
  工作表數與順序、公式範圍、樣式，而非只涵蓋目前已想到的那幾項。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-UPnn]`.

---

## N-XF01 — comfort 之 `spec_id_to_outline.tsv` 孤兒檔（跨 feature note，R-U30）

**本項不是本 feature 之異常，是 R-G4 於他 feature 之連帶。**
登記於此**而不寫入 comfort**（R-U24／R-U30 明文）。

**實測（05 輪，唯讀）**：`features/comfort/data/spec_id_to_outline.tsv` 為
**recon 形態**（`req_id / outline / polarion_id / spec_reference / title`，403 資料列，
第一欄 403/403 命中 `^[A-Z]{2,4}` 之 `SWE`）。

**它不是被污染** —— comfort 從無 `build_outline_map.py`，其四份文件
（`RUNBOOK.md:27`、`docs/INDEX.md:111`、`RULINGS.md:1195`、`DECISIONS.md:18`）
**一致記載為「403 leaf → SR24 outline 之查表」**，記載與內容相符，且無任何讀者
（三個讀者皆在 `features/home/scripts/`，只讀 home 之 `data/`）。

**R-G4 之連帶**：R-G4 生效後，comfort 若重跑 recon，產物將落
`recon_leaf_to_section.tsv`，而舊檔留著不再更新、四份文件仍指舊名。

**處置（R-U30）**：**延後，登記不動手。** comfort 已交付，實務上不會重跑；
待 Comfort 下次開輪次一併清。**本 feature 不得寫入 comfort 任何檔** —— 已遵守。

---

## A-UP10 — `052f67d` 之 commit 歸屬不準（**ACCEPTED**，R-U55）

**狀態：ACCEPTED，不是 RESOLVED。**
問題未消失 —— 那個 commit 至今仍寫著 `feat(power)` 而承載 user_profiles
之 8 檔。**是它被裁定接受，不是它被修好。**

**事實**：`052f67d`（33 檔）之 message 為
`feat(power): round 09 — three new gates, feature.yaml corrected, batch 1 held`，
其中夾帶 user_profiles 之 8 檔（皆屬 03 輪）：
`BASELINE.sha256`、`DECISIONS.md`、`RECON.md`、
`data/recon_leaf_to_section.tsv`、`docs/INDEX.md`、
`docs/handoff/03_recon_start.md`、`docs/upstream/03_recon.md`、`feature.yaml`。
**內容完整無誤** —— 非「不該進版控之物進了版控」，是**歸屬不準**：
以 `git log -- features/user_profiles/` 追 03 輪，會落在一個 power 的 commit 上。

**成因**（power session 執行層自陳，逐字）：

> 我執行 `git add features/power/`，但另一個 session 在此之前已經把他們的檔案
> 放進 index 了，而 `git commit` 不帶 pathspec 就會提交整個 index。

**第二次發生**（照錄，R-U55 明文要求）：前有 `645e55f` → `cc04aa1`
之歷史重寫，該次把 power 之 round-07 檔案自樹上移除。
**兩次皆非疏忽，是該作法本身會產生此結果**（R-G12 之立條理由）。

**處置（R-U55）**：採案 1，不動歷史。裁定依據為本輪實測 ——
該 commit **已推送**、其後已有 **5 個提交**；案 2／3 之收益為一句 message
之歸屬，成本為 rebase 5 個提交 ＋ force push 一條已推送分支。

**再犯之防線**：**R-G12**（git commit 一律帶 pathspec），已升全域並寫入
`docs/fw036/FEATURE_ONBOARDING.md`。**本項不因該防線改記 RESOLVED** ——
防線防的是下一次，不是這一次。

---

## A-UP11 — 037 之 12.8／12.8.1 leaf **標題與描述錯位**（PENDING，執行層新開）

**發現於**：19 輪第二批生成時（ch12–14）。

**事實**：037 對 `12.8`（PVAL8）切四個 leaf、對 `12.8.1`（PVAL8.1）切三個，
其 **Requirement Title 與 Description 不對應**：

| req_id | 037 標題 | 037 描述之實際內容 | 相符 |
|---|---|---|---|
| `125-01` | Device Manager Disabled in Valet Mode | HVAC／Media 可用；Media 內 Device Manager 鎖住 | ✓ |
| `125-02` | Disable Projection, HFP, and VR | Projection／HFP 停用、VR 不啟動 | ✓ |
| `125-03` | **Glove Box Lock Prompt on Valet Mode Entry** | **狀態列互動限制**（僅 Valet Profile 與 HVAC 例外）| **✗** |
| `125-04` | **Glove Box Lock Button Greyed Out** | **所有不可互動項變灰** | **✗** |
| `126-01` | **Lock Out Specific Menu Areas** | **PU0832 手套箱鎖之進入提示** | **✗** |
| `126-02` | **Status Bar Restrictions and Grey Out** | **手套箱鎖按鈕變灰** | **✗** |
| `126-03` | Electronic Glove Box Lock Logic | 按下已變灰之手套箱鎖按鈕 → PU0833 | 部分 |

**形狀**：標題相對於描述**整體位移** —— `125-03`／`125-04` 之標題內容
落在 `126-01`／`126-02` 之描述上，反之亦然。

**判定依據**：以 spec `pdf_text` 複核，**Description 與條文對齊，Title 不對齊**。
`12.8`（PVAL8）之條文依序為：HVAC/Media 可用 → Projection/HFP/VR 停用 →
狀態列互動限制 → Media 內 Device Manager 鎖住 → 全部不可互動項變灰；
`12.8.1`（PVAL8.1）為：啟用手套箱鎖 → PU0832 提示 → 按鈕變灰 → PU0833。

**本輪之處置**：**依 Description 生成**（§8.2「037 為單位權威」，
而**單位之內容以其 Description 為準** —— 標題不是內容）。
七條 TC 之標題由執行層依描述另擬，037 標題僅留作索引。

**未做**：未改 037（**素材不得改**）；未推及其他章節之 leaf ——
**本輪只複核了 12.8／12.8.1 七條**，是否另有錯位者未全量掃描。

**建議**：(1) 全量掃描 037 之 title 與 description 是否對齊；
(2) 該落差是否須回報上游（同 DR #3 之形態）。**屬 Pei 之裁定。**

---

## A-UP12 — **互指之委派**：9.2 條件 2 與 11.3 第二句同時無覆蓋（**RESOLVED 於本輪**，L-2 / 22 包）

**狀態**：本輪補足並更正記載，故登記為 RESOLVED；**其成因之類別未關閉**（見末段）。

**形狀**：兩條 TC 之記載各自把同一側之覆蓋推給對方 ——

| 條 | 節 | 其記載 | 實際 |
|---|---|---|---|
| `TC-020` | 9.2（EDPR2）| reasoning：條件 2「由 **11.3** 之 leaf 承擔」| 11.3 沒有承擔 |
| `TC-040` | 11.3（CPA1）| remarks：第二句「由 **9.2** 之 leaf 承擔」| 9.2 沒有承擔 |

**兩者所指之條件並非同一件事**：

- 9.2 條件 2：`does not support **the connected profile feature**`（功能支援）
- 11.3 第二句：`does not support **connectivity**`（硬體配置）

**其不等價之證明不需外部資料**：9.2 自身把「區域無 <Brand> app」與條件 2
**並列為兩個獨立條件**。若「不支援該功能」只等於「無連網」，
則「區域無 app」這一條件無處安放 —— 一個有連網之車，在無 app 之區域仍無該功能。
反向亦成立：6.4.1（NOPR3.1）以 `not equipped with connectivity` 述另一個行為，
可見 spec 對「連網」有其一貫且較窄之用法。

**為什麼它比單向指錯更難發現**：單向指錯至少有一份記載是空的；
**互指之委派兩份記載都看起來已交代**，且兩份都通得過現行 G17／G18
（引用欄形態正確、字面值溯得到源）——
**覆蓋稽核之分子分母都不會動，缺口在文字裡而不在數字裡**。

**本輪之處置**：

| # | 動作 |
|---|---|
| 1 | 新增 `TC-077`（9.2 條件 2）與 `TC-078`（11.3 第二句）—— **兩個洞，非一個** |
| 2 | 更正 `TC-020` 之 reasoning 與 `TC-040` 之 remarks，具名原委派不成立及其理由 |

**成因之類別**：**現行無任何閘檢查「委派之對象是否真的承擔」。**
G17 驗引用欄有無登記、G18 驗字面值溯不溯得到源 —— **兩者都不讀 reasoning 裡
那句「由某某承擔」**。本輪之發現出自 22 包之人工覆核，不是掃出來的。

**本輪已補全量掃描**（78 條之 `reasoning` ＋ `remarks`，命中 21 處）。
委派之對象分三類，**三類之風險不同，不可混記**：

| 類 | 定義 | 現況 | 判 |
|---|---|---|---|
| (a) | 指向**語料內確實存在**之 TC | `011`→9.3.1(022)、`028`→9.5.2(029)、`065`→128-03、`075`→039、`076`→013／044 | **可驗，成立** |
| (b) | 指向**尚未取樣之 leaf** | `001`→`001-02`／`001-03`、`005`→6.2(`047`)、`007`→7.2(`058`)、`009`→8.7(`073-02`／`073-03`) | **是承諾，不是覆蓋** |
| (c) | 指向另一節而該節**不含該行為** | `020`↔`040`（本條）| **假委派 —— 已修** |

**(b) 之四處經查證，其 leaf 確實存在於 037 之 180 母體內**
（`data/recon_leaf_to_section.tsv` 逐條複驗），故非指錯 ——
**但在該批生成之前，那幾句話所描述的覆蓋並不存在**。
第三批開批時須逐條兌現；**未兌現者，其上游 TC 之 reasoning 須改述**。

**仍未關閉**：本掃描為人工分類（21 處逐條讀），**未落為閘**。
落閘之難處在 (b) 與 (c) 之分野需要判讀「該節之條文含不含該行為」——
不是字串比對。**在落閘之前，本類缺陷只能靠覆核發現。**
