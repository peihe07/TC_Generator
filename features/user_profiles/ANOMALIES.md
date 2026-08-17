# ANOMALIES — FW036 User Profiles HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-UPnn]`。PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
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

## A-UP02 — 8 條無 SWE 覆蓋之 spec 條文（PENDING）

spec 3.1–3.5（PLP1–PLP5）、10.1、11.1、11.2 共 8 條實質條文無任何 SWE
需求覆蓋，其中 PROF-001-01 之 Verification Criteria 本身即引用 PLP 表。
RD-1 候選；依 §8.4.2 不得自行吸收進 TC。

**處置**：RD-1，Tier 3 由 Pei 送出（下放包 01b §未決）。本輪不動。
Layer 3 骨架依 01b 作業項 5 取 spec 章 4–14，章 1–3 不入生成範圍。

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

## A-UP04 — 037 Analysis Report 不在 repo 內（PENDING，執行層新開）

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

**處置**：依 canon §0 升級條件第 1 條（missing file）停下並回報，
不改判準、不以 spec 側數字代替。已登記於 `DATA_REQUESTS.md` 第 1 列。
037 到齊後 recon 一次跑完即可解除。

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

## A-UP09 — openpyxl 存回會摧毀母本 R 欄 design_method 下拉（PENDING → **本輪修補完成，待覆核**）

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
  **02b 作業項 5 定本條「保持 PENDING 直至 R-G3 修補完成」** ——
  修補已完成，惟其**狀態變更屬 Tier 2**，本層不自行改判 RESOLVED，
  於此記明並請覆核。
- **檢查條件（依 canon §5a 第 14 條，寫成自我完備形式）**：
  寫回後之產出須「與寫回前之母本在所有可讀屬性上一致，除資料列之內容欄
  與 `No.#` 公式外」—— 涵蓋 x14 extLst、legacy DV、zip member 集合、
  工作表數與順序、公式範圍、樣式，而非只涵蓋目前已想到的那幾項。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-UPnn]`.
