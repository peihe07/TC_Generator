# RULINGS — Vehicle Category (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Vehicle Category 之裁決權威；
跨 feature 條文承接時註明來源包。

來源：`docs/handoff/01_intake_recon.md` §二（下放包 01，Pei 2026-08-25 裁定
Q1 甲／Q2 准／Q3 甲／Q4 准）。抄錄逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。
逐條字面一致核對結果見 `docs/upstream/01_intake_recon.md` §2。

---

```
R-VC1（feature 身分與 test_group）

`feature` 為 `Vehicle Category`，slug 為 `vehicle_category`，
`test_group` 為 `Vehicle Category`。（Pei 2026-08-25 裁定 Q1 甲。）

本 feature 為**獨立 feature**，不併入 `vehicle_setting` 作為第三部。
裁定依據三項事實：

(a) 錨點家族不同。`vehicle_setting` 之兩部（CFTS044、VF230）皆以 CFTS
    母文件為 spec，`spec_reference` 走 IN §10.7(a) 之
    `CFTS{nnn}-{ObjectID}`；本 feature 之母 spec 為 HMI Logic and Flow，
    走 §10.7(b) 之 `{檔名}_{章節號}`。同一 feature 內並存兩種錨點形態，
    會使 `spec_reference_template` 與 lint 判準分歧。
(b) `test_group` 不同。工作簿 G 欄之值為交付面事實，不可共用。
(c) 編號衛生。`vehicle_setting/docs/handoff/` 現有 164 個檔，已因碰撞
    另立 `V` 前綴（見該 feature 之 V00、V04 兩包）。第三套前綴之邊際
    成本高於新開目錄。

037 之 `FROP = Vehicle Settings` 為**功能推出計畫之歸屬**，不等於 repo
之 feature 切分。該事實記於 `feature.yaml` 之 `frop:` 鍵保留，不進入
`test_group`、不進入任何 TC 欄位。

裁決前綴為 `R-VC`、異常前綴為 `A-VC`、資料請求前綴為 `DR-VC`，
不與任何既有 feature 共用序號。
```

---

```
R-VC2（036 母本與 workbook_state）

（Pei 2026-08-25 裁定 Q2 准。）

036 母本套用 R-G1 全域條文：
`forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
Specification & Result_SWQT_20260817_ext.xlsx`。

`workbook_state = BLANK`。無既有 done region，`done_region` 節不生效
（`detection: author`、`author_value: null` 為佔位，不得據以推論存在作者）。

配套三項：
(a) `write_back.fill_test_group_set = true`（canon §2.1，BLANK -> FILL）
(b) `write_back.author_value = "PeiPYHsu"`
(c) `write_back.tc_ref_id_value = "NEW"`

母本之 R 欄 design_method 下拉為 x14 擴充。**任何以 openpyxl 存回母本
之操作都會摧毀該下拉**（R-G1 註）。寫回一律採 XML 外科式修改：
以 zip 開檔、僅改 `xl/worksheets/sheet*.xml` 之目標儲存格、原樣重打包，
並於前後比對 `<dataValidation`、`x14:dataValidation`、
`<conditionalFormatting`、工作表數、drawing/chart rel 數之原始 XML 計數。

**本條之前提為「Pei 手上無既存之 Vehicle Category 036」。** 若日後出現
含他人已填 done region 之既存 036，本條即失效，須重裁，且 §三之 leaf
全集須先與該工作簿之既有 req_id 集合做差集。
```

---

```
R-VC3（驗證範圍與兩張強制揭露表）

（Pei 2026-08-25 裁定 Q3 甲。）

驗證母體為 037 `Analysis Report` 之 **leaf 全集 117 筆**，全取，
不因 `FROP` 欄之值而扣減。

依據：037 之交付單位是本份 037；`FROP` 是分類欄，不是範圍欄。
依 FROP 扣列等同分析層自行改寫上游之需求單元，違 IN §8.2
（TC 作者不得再分解、合併或發明 RD 單元）。

交付時**強制附兩張揭露表**，缺任一張不得出貨：

  表 A｜FROP 跨域揭露
    逐列列出 FROP ≠ `Vehicle Settings` 之 17 列（`Power Management` 16、
    `Audio Management` 1），含 SWE-Requirement ID、規格章節、FROP 值。

  表 B｜覆蓋落差揭露
    逐節列出 §4.2(b) 之 18 個「有實質規格內容而 037 無對應需求」之章節，
    註明「037 未涵蓋，本次不產出 TC」。本表為 IN §8.4.2 末段
    「真覆蓋洞須浮現、不得默默吸收」之落實。

日後若查出與 `power` / `power_moding` 有實際 req_id 重疊，處置為
**在該處立 `[OVERRIDE]` 縮限並記其依據**，不得回頭以本條為由默默扣列。
```

---

```
R-VC4（spec_reference 之錨點形態）

（Pei 2026-08-25 裁定 Q4 准。）

`spec_reference` **逐字取 037 `Analysis Report` 之 `HMI Source ID` 欄原值**，
不構造、不改寫、不去括號、不重新 token 化。

其形態為：
  SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_(December_27_2023)_{章節號}

依據三項：
(a) 該欄為上游交付件之正式欄位值，且與 SYS1 export 之
    `SYSRE_HMI_Source ID` 欄逐字相同 —— 037 之 66 個相異值對 SYS1 之
    108 個值命中 66/66，未命中 0（量測條件見 §四 4.1）。
    錨點之第一來源恆為上游正式欄，非本地推導之演算結果。
(b) 逐字抄欄則不需構造，IN §10.7(b) 之「全案逐字一致，禁止同檔名
    拼寫變體」自動成立。
(c) xlsx 檔名（`..._Post_2A_December_27_2023`，無括號）與 pdf 檔名
    （`Vehicle_Category_...`，無 `SYS1_HMI_` 前綴、無括號）皆為檔案
    系統之命名，會隨他人重新命名而變，不具追溯地位。

配套：`feature.yaml` 之 `spec_reference_template: null`
（模式為查得，非構造）。`spec_mode` 之字母由執行層依 FO §3 實測後填入，
本條不逕定。

排列一律依 IN §10.7 之「一個章節號一行、前綴逐行重述」，
禁用 `,`、`、`、`;` 串接；同文件內章節號升冪。
```

---

```
R-VC5（037 之 Source Requirement ID 不作為錨點）

037 `Analysis Report` 之 `Source Requirement ID` 欄，其值形態為
`SYS-HMI-RA-VC-###`（61 個相異值）。

分析層已實測：字串 `SYS-HMI-RA` 在 SYS1 export 之全工作簿
（`Basic Report` / `Polarion` / `_polarion` 三分頁、全儲存格）
之出現次數為 **0**（量測條件見 §四 4.1）。SYS1 之 ID 欄形態為
`NRL-171032` 系列，與該值無任何字面關係。

拘束三項：
(a) 本 feature 之 `spec_reference` 一律取 `HMI Source ID` 欄（R-VC4），
    不得取 `Source Requirement ID`。
(b) 任何跨命名之對應 —— 例如推定 `SYS-HMI-RA-VC-012` ↔ `NRL-171043` ——
    屬 FO §0 逸出觸發第 1 條「規格查找未解」，須停並回報，
    不得自行建立，亦不得以列序、章節序或任何相鄰性為據推導。
(c) 本項之未解**不阻斷** Phase 1 及後續生成 —— 另一條錨點鏈已 66/66 通。
    惟交付前須有 DR-VC2 之答覆以完成雙向追溯。
```

---

```
R-VC6（037 分析九欄為有效上游輸入；A-VC1 撤銷）

037 `Analysis Report` 第 10–18 欄 ——
Feasibility / Description-Action for Feasibility / Impact /
Description-Action for Impact / Risk Factor /
Description-Action for Risk Factor / Reusable /
Description-Action for Reusable / Priority ——
於 117 個 leaf 上皆有實質內容；於 28 個「有子之父」為 `\xa0`（U+00A0）。
欄 16 `Reusable` 與欄 17 `Description-Action for Reusable` 另有 3 列為
`None`（真空儲存格）：SWE1-HMI-VC-034、SWE1-HMI-VC-052、SWE1-HMI-VC-063。

下放包 01 §3.3 所記「第 10–18 欄全 145 列皆為 `\xa0`，無內容」為分析層
未經全表掃描之全稱斷言，**作廢**。據其所立之 A-VC1 一併**撤銷**，
其條文不得於任何場合沿用或引述為判準。

拘束四項：
(a) 欄 18 `Priority`（實測分布 Medium 88 / High 28 / Low 1）為上游對各
    leaf 之優先級判斷。TC 之 `priority` 欄（IN §10.2 之 P0–P3）
    **不得於忽略本欄之情況下本地推導**。P0–P3 與 High/Medium/Low 之
    映射規則另裁，在該裁定落地前，priority 欄不得產出。
(b) 欄 11 / 13 / 15 / 17 之描述文字為 `reasoning` 與 test_item 括號下半
    之素材來源，須納入 Phase 4 之資料建置範圍。
(c) 欄 14 `Risk Factor` 與欄 12 `Impact` 為 §10.2 映射之佐證，
    不單獨作為 priority 之依據。
(d) 「讀取時 strip 含 `\xa0`」之技術手段**保留**（A-VC1 之正確部分）。
    作廢者為「不視為已填」之推論 —— 這九欄在 117 個 leaf 上是已填的。
```

---

```
R-VC7（規格 PDF 之權威複本）

分析層 Claude Project 附件之規格 PDF 為
3,552,260 B，SHA256
`216cfa84dfb84c0b3c44e24881407521412e16d16728aaa49e90ff3b3275a455`。
repo 內複本及全機 7 份複本一律為 2,828,253 B，SHA256
`3a6752c83bed1582485ad5e1aa7052ae63e6f0bb94304839beaf0e0b12776a76`。

二者為不同之檔。**repo 內複本為權威**；附件之份判為 Project 上傳時
重新渲染之衍生物，不得作為任何判準之來源。
（`scripts/recon.py` 檔頭已預告此情形：re-rendered copy 之文字層探測
結果會與原件不同，一律以 repo `inputs/` 之複本為準。）

連帶拘束：下放包 01 §4.2(b) 之 18 節「規格內容摘要」欄係讀該衍生 PDF
所寫。其**章節號**已由 T4 驗明相符，**摘要文字未經權威複本確認**。
DR-VC3 發出前須以 repo `inputs/` 之 PDF 逐節重驗；重驗前該摘要不得
引為 DR 之措辭依據，亦不得寫入表 B。
```

---

```
R-VC8（recon.py 於 spec_reference_template 為 null 時之行為；Tier 2 修法授權）

`scripts/recon.py:894` 之 `tpl = cfg.get("spec_reference_template", "{outline}")`
在鍵存在而值為 `None` 時取得 `None`，於 `:900` 之 `tpl.replace()` 崩潰。
R-VC4 明文要求該鍵為 `null`，故本 feature 必然觸發。

採上繳包 A-VC6 之提案 (b)：**`spec_reference_template` 為 null 時，
`data/recon_leaf_to_section.tsv` 之 `spec_reference` 欄改逐字取 037
`HMI Source ID` 欄之原值**，使資料件與 R-VC4 一致。

提案 (a)（`... or "{outline}"`）**不採**：其產出為光禿之章節號，
與 R-VC4 所裁之全名不同，等於在資料件中埋一個與裁決相左的值。
崩潰會停，錯值不會 —— 後者為害更甚。

實作拘束三項：
(a) `survey_a03()` 現將 citation 拆為 stem 與 sec 後僅保留 sec
    （`sections[rid] = m.group("sec")`），原值已丟失。修法須**同時保留
    `first` 之原值**（例如新增 `citations[rid] = first`），
    **不得**以 `stem + "_" + sec` 還原 —— 該還原式在 stem 本身以底線
    接數字結尾時會取錯切點。
(b) 未宣告 `spec_reference_template` 之 feature 行為不變（`dict.get`
    之預設值路徑保留），使其他 12 個 feature 之既有產出基線不動。
(c) 修法後須對至少一個既有 feature（建議 `home` 或 `comfort`，
    其 recon 有回歸基線）重跑並確認產出逐字不變，再對本 feature 重跑。

本條為 Tier 2 工具修法之授權，範圍僅限上述。
`recon.py` 之其他行為一律不動。
```

---

```
R-VC9（recon_assertions 之宣告範圍與未機器化之揭露義務）

`scripts/recon.py` 之 `run_assertions()` 僅實作三個鍵：
`functional_requirement_count`、`distinct_spec_sections`、
`spec_reference_stem`。`leaf_count` 與 `uncovered_content_sections`
**無對應實作，宣告不生效**。

本 feature 之 `recon_assertions` 僅宣告：

    recon_assertions:
      functional_requirement_count: 145

下放包 01 §八 所草擬之 `leaf_count: 117`、`distinct_spec_sections: 66`、
`uncovered_content_sections: 18` 三鍵中，`leaf_count` 與
`uncovered_content_sections` **刪除**；`distinct_spec_sections: 66`
得保留（該鍵有實作），由執行層於重跑後確認其 PASS 再定去留。

依據：宣告一個不被讀取之鍵，比不宣告更糟 —— 不宣告至少誠實，
宣告則製造一個永不失敗之檢查，並使讀者誤認該值已受保護。
此與 display 之「宣告必然為 0 之 assertion 只會製造一個不可能失敗之
檢查（canon §5a）」同源，本案為其鏡像。

揭露義務：R-VC3 之 leaf 全集 117 與覆蓋落差 18，在對應 assertion
落地前**僅靠 T4 重測與上繳包交叉檢查守護，非機器保證**。
此事實須逐包揭露，**不得因 feature.yaml 有寫而視為已守**。

leaf 判準三者並存之事實一併記於 feature.yaml 註解：
  145 —— Categorization == Functional（recon.py 在用）
  117 —— 子需求 ∪ 無子之父（R-VC3 所裁之驗證母體）
   79 —— id-suffix（recon.py 明記不生效）
display 未暴露此分歧，因其 037 之三值恰皆為 8。
```

---

```
R-VC10（素材之 paths / reference 分工）

**`paths:` —— 素材一律複製入 `features/vehicle_category/inputs/`，
路徑以本 feature 目錄為基準。**

    paths:
      popup_list:    "inputs/Pop Up List HMI R1 (26PI).xlsx"
      settings_list: "inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx"

下放包 01 §五 T1 之「forms/ 兩份不複製，僅綁定」**作廢**。
依據：`features/display/feature.yaml` 已記載此坑 —— 將 forms/ 之 repo
相對路徑填入 `paths:`，`recon.py` 隨即以 `input not found … under
features/display` 中止。素材複製入 `inputs/` 為 home / display / comfort /
power_moding 之一致慣例。執行層留 `null` 為正確之保守處置。

**`reference:` —— 六項，路徑以 repo 根為基準。**

    a03_report / sys1_export / spec_pdf   → features/vehicle_category/inputs/…
    workbook_master / popup_list / settings_list → forms/…（或 inputs/ 之複本，
      擇一並於註解記明所綁者為何份）

下放包 01 §五 T9 所記之「七項」為分析層計數錯誤，**正解為六項**。
執行層推定第七項為下放包全文並依 R-G15 判準排除 —— 推定過程正確，
惟結論應為「本無第七項」。下放包全文不入 `reference:`。

**明文排除四項**：`dbc_b` / `dbc_fd` / `lid` / `proxi` 不綁定。
依據：037 全文掃描之 CAN 訊號、PROXI 參數、VF 引用命中數皆為 0；
規格本文之 VF507 / VF352 落在 037 未涵蓋之 18 節內。
本 feature 之產出不觸及該四檔，不符 R-G15「其變動會使既有產出失效」
之判準。**此排除須寫入 feature.yaml 註解** —— 否則日後必有人問
為何本 feature 較 display 少綁四項。
```

---

```
R-VC11（TC priority 之判定；R-VC6(a) 之落地）

037 `Analysis Report` 欄 18 `Priority` 之實測分布為
High 28 / Medium 88 / Low 1（117 leaf）。

**該欄係按規格章節整批賦值，非逐 leaf 判斷**（證據見 A-VC9）：
  章 4/5/6/7（Glove Box 全部）      → High  12，章內無例外
  章 13（Settings Behavior/Ignition）→ High  16，章內無例外
  章 2/3/11/12/14                   → Medium 88，章內無例外
  章 16（Cabrio Widget）             → Low    1
且欄 18 **無對應之 Description-Action 欄**，037 未載其判準。

故：**不得建立 High/Medium/Low → P0/P1/P2/P3 之機械映射表。**
機械映射會將一個判準不明、粒度為「章」的量，搬入一個判準明確、
粒度為「TC」的欄位 —— 其結果具有實測值之外觀而無實測值之內容，
即 IN §8.4.1 所禁之造值換一種形式。

TC 之 `priority` 依下列三層決定：

(a) **主判準** —— IN §10.2 之 P0–P3 rubric，逐 TC 判定。
    該 rubric 有明確定義（P0 安全／開機／連線／音訊輸出／eCall／
    車輛關鍵 CAN／資料遺失風險；P1 主要使用者功能或關鍵操作邏輯；
    P2 次要／支援功能；P3 次要 UI、低影響客製、罕用情境、外觀細節）。

(b) **上游約束** —— 037 Priority 為**邊界**而非映射來源：
      037 = High → 該 leaf 所衍生之 TC **不得低於 P1**
      037 = Low  → 該 leaf 所衍生之 TC **不得高於 P3**
      037 = Medium → 不設邊界（該格含 88 筆語意跨度極大之需求，
                     不具區辨力）
    此為 R-VC6(a)「不得於忽略本欄之情況下本地推導」之落地形式：
    本欄之資訊被用於設界，而非被抄寫。

(c) **分歧揭露** —— 依 (a) 所判與 037 之值語意相悖時
    （例如本地判 P0 而 037 為 Medium、本地判 P3 而 037 為 High），
    須於該 TC 之 `reasoning` 記明分歧與本地判定之依據，
    引 §10.2 之對應款。**不得為求一致而遷就任一方。**

R-VC6(a) 之「priority 欄不得產出」之凍結，於本條落地後**解除**。

DR-VC7 之回覆若載明 037 之 Priority 判準，本條 (b) 之邊界重審。
```

> **⚠ (b) 已作廢 —— 見 R-VC13（下放包 04，Pei 2026-08-25）。**
> 上方條文**原字不改**（R-TM13：不刪除，加註保留）。作廢者僅為 (b)：
> 「037 = High → 該 leaf 所衍生之 TC 不得低於 P1；037 = Low → 不得高於 P3」。
> 作廢理由：以**章級**之量對 **leaf** 設下界為粒度錯配 ——
> R-VC11 之立論本為「不採機械映射，因粒度不匹配」，原 (b) 自身重犯該錯，
> 僅由「等於」放寬為「不低於」。其必然輸出即上繳包 03 §6.2 之八筆抬升。
> **新 (b) 見 R-VC13：上游約束作用於章，不作用於 leaf。**
> 本條之 **(a) 主判準與 (c) 分歧揭露不變，繼續適用**。

---

```
R-VC12（§4.2 分類之修訂；圖內內容之處置）

**一、16.1 改列 (a)，表 B 母體由 18 節改為 17 節。**

上繳包 02 §7.4 之觀察成立：SYS1 `Description` 所載 16.1 之內容為
「Refer to the Vehicle Category - Cabrio Rooftop and Cabrio Wind
Draught Deflector HMI sections for complete logic.」——
其為**交叉引用**，非該節自身之實質需求內容，與 §4.2(a) 之
「非需求性質」同類。

下放包 01 §4.2 之計數修訂為：
    未引用 42 節 ＝ 非需求性質 **25** 節 ＋ 有實質內容 **17** 節
（原為 24 ＋ 18）

R-VC3 所稱「表 B｜覆蓋落差揭露」之母體隨之改為 **17 節**：
  8.1, 8.2, 8.3, 8.4, 8.5, 9.1, 9.2, 10.1, 10.2,
  11.9, 11.9.1, 11.9.2, 11.9.3, 14.2, 15, 16.2.1, 16.2.2

R-VC3 之其餘部分（117 leaf 全取、表 A、兩表為出貨門檻）**不變**。

**二、下放包 01 §4.2(b) 之摘要文字，就下列各節作廢。**

  §15         —— 「PU0132…PU0275 之訊息文字與逾時」
  §10.1／10.2 —— 「Type / Power Source / Last State 之四種組合、
                  Last State 之可用條件（Latching + Ignition）」

依 R-VC7，該等文字係讀 Project 附件之衍生 PDF 所得，
repo 權威素材（SYS1 `Description`、repo PDF 文字層）皆不載之，
其內容僅存於 `(image: imageNN.png)` 佔位之後。

拘束：
(a) 表 B 之該三節，「內容」欄一律書
    「該節內容僅存於圖，SYS1 匯出未帶文字」，**不得寫入任何摘要文字**。
(b) DR-VC3 對該三節之提問同此措辭（執行層已實作，予以追認）。
(c) §8.3 為**摘要漏列**而非錯誤（權威素材另載
    「A graphic representation of the vehicle status will be present
    on pop up」）。表 B 之該節內容補入此句，來源記為 SYS1 `Description`。
(d) 其餘 13 節之摘要經 T17 驗為「與 SYS1 所載相符」，予以保留，
    惟其效力僅及於「與 SYS1 相符」，**非「與規格原件相符」**
    （FO §3 Mode A 之盲點，執行層已於上繳包 02 §10 揭露）。

**三、通則。**
分析層日後對任何規格內容之摘要，其來源須為 repo `inputs/` 之權威複本；
以 Project 附件、衍生 PDF、OCR 或圖之視覺判讀所得者，
一律不得以實測值之格式寫入下放包。
如確需引用圖內內容，須標為「圖內內容，未經文字層確認」並登記 DR。
```

---

```
R-VC13（R-VC11(b) 之修訂：上游約束改為章級）

R-VC11(b) 原文「037 = High → 該 leaf 所衍生之 TC 不得低於 P1；
037 = Low → 該 leaf 所衍生之 TC 不得高於 P3」**作廢**。

作廢理由：A-VC9 已證 037 `Priority` 之粒度為**章**（十一章章內單一值，
零例外）。以章級之量對 leaf 設下界為粒度錯配，其必然輸出為
「章內善後步驟被主流程之優先級抬起」—— 上繳包 03 §6.2 之八筆
（VC-027／031／032／033-02／058-02／058-03／062-02／063-02，
全部為彈窗回饋與返回導覽）即為顯影。
R-VC11 之立論本為「不採機械映射，因粒度不匹配」，
原 (b) 自身重犯該錯，僅由「等於」放寬為「不低於」，錯配未解。

**新 (b) —— 上游約束作用於章，不作用於 leaf：**

  037 = High 之章 → 該章之 leaf 群中**至少須有一筆**定案為 P1 或 P0。
                    章內個別 leaf 不設下限。
  037 = Low  之章 → 該章之 leaf 群中**不得有**定案高於 P3 者。
  037 = Medium 之章 → 不設約束（該值含 88 筆語意跨度極大之需求，
                      不具區辨力）。

  某章不滿足其約束時，**不得逐筆抬升以求滿足** —— 應停並回報，
  該情形意味著本地判定與上游對該章之認知有系統性分歧，
  屬須裁事項而非可自動修補之偏差。

R-VC11 之 (a) 主判準與 (c) 分歧揭露**不變**，繼續適用。

依本條驗算：章 4／5／6／7／13 五個 High 章皆已滿足（各有 P1 或 P0），
章 16 之 Low 亦滿足。**八筆抬升全數撤銷，定案回歸本地判定。**
```

---

```
R-VC14（P0 之判準：攔阻失效與執行失效之區分）

IN §10.2 之 P0 類目含 `data-loss risk`。該款於「使用者資料之清除」
一類需求上，須區分二種失效方向 —— 二者不同級：

(a) **攔阻失效** —— TC 驗證「Cancel／否定路徑確實未變更資料」。
    其失敗意味著資料**被意外清除**。此為 data-loss，**P0**。
(b) **執行失效** —— TC 驗證「Yes／肯定路徑確實清除了資料」。
    其失敗意味著該清而未清。此**非** data-loss ——
    資料仍在，未發生遺失。**P1**。

(b) 之失效在轉售、租賃、還車等情境下構成**隱私外洩**風險，
其嚴重性不因本條而被否認；惟 §10.2 之 P0 類目
（安全／開機復原／連線／音訊輸出／eCall／車輛關鍵 CAN／資料遺失）
未列隱私，**不得以類推方式擴充 rubric 之類目**。
該風險依 R-VC11(c) 記於該 TC 之 `reasoning`。

本條之即時適用：
  SWE1-HMI-VC-036-01（選 Yes 清除個人資料並顯示確認彈窗）
    上繳包 03 §6.3 判 P0，依本條 (b) **改判 P1**。
  SWE1-HMI-VC-035-03（restore-defaults 之 Cancel）—— (a)，維持 **P0**
  SWE1-HMI-VC-036-02（clear-personal-data 之 Cancel）—— (a)，維持 **P0**

037 對此三筆皆為 Medium，依 R-VC13 之新 (b) 章級不設約束，
故 (a) 之二筆定案 P0 不受上游值影響（R-VC11(c) 之分歧揭露義務仍存）。
```

---

```
R-VC15（母體標註義務）

本 feature 之文件、條文、下放包、上繳包中，凡引用計數，
**必須標註其母體**。母體之命名限於下列四者，不得省略、不得混用：

  145 列    —— 037 `Analysis Report` 之全部資料列（列 8–152）
  117 leaf  —— R-VC3 所裁之驗證母體（子需求 ∪ 無子之父）
   66 section —— 037 `HMI Source ID` 之相異章節號
  108 outline —— SYS1 `Basic Report` 之有效 `Outline Number`

**不同母體之數字，不得互援為等同性、對應性或涵蓋性之依據。**
兩個數字相等而母體不同者，為巧合，不構成任何論證。
欲主張跨母體之對應關係，須逐項比對其**成員集合**，
不得以計數相等代替。

實例（本條之立條由來）：
  「章 13 全 16 筆（leaf 母體）恰等於 FROP = Power Management
    之 16 筆（列母體）」—— 兩個 16 落在不同母體，`恰等於` 不成立。
    正確之論證為：FROP = PM 之 16 列，其章別分布為 {'13': 16}，
    即全部落在章 13 —— 此為成員集合之比對，不倚賴計數相等。

適用範圍：本 feature 全部產出，含已交付之包。既交付者不改原文
（R-TM13），以 `docs/REVISIONS.md` 加註。

本條同時拘束分析層與執行層。分析層之下放包若違反本條，
執行層應據以停並回報，不得沿用。
```

---

```
R-VC16（Layer 2 定案：8 個 Test Set）

（Pei 2026-08-26 裁定：邊界准、#5 名稱采 `Settings List`。）

Layer 1 Test Group ＝ `Vehicle Category`（R-VC1）。
Layer 2 Test Set ＝ **8 組**，其邊界以**可執行之規則**定義如下，
規則為權威，節次清單為其展開結果：

    章 2                → `Category Structure`
    章 3                → `Controls`
    章 4 / 5 / 6 / 7    → `Glove Box`
    章 11，次級節號 ≤ 6 → `Settings Behavior`
    章 11，次級節號 ≥ 7 → `Settings List`
    章 12               → `Settings List`
    章 13               → `Ignition Availability`
    章 14               → `Brake Service`
    章 16               → `Cabrio Widget`

其中「章」取 037 `HMI Source ID` 尾段章節號之首段，
「次級節號」取其第二段（`11.7.1` 之次級節號為 7）。

驗算目標（**母體標註依 R-VC15**）：

  # 1 `Category Structure`   24 leaf ／ 13 section
  # 2 `Controls`             17 leaf ／ 12 section
  # 3 `Glove Box`            12 leaf ／  8 section
  # 4 `Settings Behavior`    15 leaf ／  6 section
  # 5 `Settings List`        30 leaf ／ 17 section
  # 6 `Ignition Availability` 16 leaf ／  8 section
  # 7 `Brake Service`         2 leaf ／  1 section
  # 8 `Cabrio Widget`         1 leaf ／  1 section
  ── 合計                   117 leaf ／ 66 section

拘束五項：

(a) **Layer 3（spec section）不入工作簿**（IN §4.1.5）。不得存為任何
    欄值，不得串接進 Test Set 名稱（不寫 `Settings List 12.3`）。
    section 與 TC 之關聯由 `specification_reference` 承載（R-VC4），
    那是 traceability 欄位，不是 Layer 3 欄位。

(b) **#4 / #5 之分界（11.6｜11.7）為本 framework 唯一有二來源交叉驗證
    之邊界** —— 規格目次 ＋ 037 `Sub Categorization`（章 11 為唯一混章，
    切換次數 = 1，Service 15 ／ HMI 5）。其餘 7 個邊界僅有規格目次
    單一來源支撐。此弱點須記於 `framework.md`，不得因已簽署而略去。

(c) **#7（2 leaf）與 #8（1 leaf）之保留，非 outlier 特許**，而係
    二者皆為「待補節會使其長大」之組（#7 待 14.2 與 §15；#8 待 16.2.1
    與 16.2.2）。DR-VC3 回覆為「應補」時，此二組之邊界**須重審**：
    屆時章 8／9 之 Cabrio 本體（7 節）應另立 `Cabrio Rooftop`，
    不得併入 #8。

(d) **11.9 群（11.9／11.9.1／11.9.2／11.9.3）歸 #5**（下放包 06 §二預裁，
    以權威複本實測為據）。上開規則之「章 11，次級節號 ≥ 7」已涵蓋之，
    不需另設例外。條件性生效，待 DR-VC3。

(e) **FROP 之對應**：FROP = `Power Management` 之 16 列（**145 列母體**）
    其章別分布為 `{'13': 16}`，即全部落在 #6 `Ignition Availability`；
    FROP = `Audio Management` 之 1 列（`VC-048-02`，§12.3.2）落在 #5。
    R-VC3 表 A 據此編製。**此為成員集合之比對結果，非計數相等之推論**
    （R-VC15）。
```

---

```
R-VC17（一對一之主張須以成員比對為據）

凡主張二集合為「一對一」、「恰等於」、「完全對應」、「全部落在」
或任何等同性關係者，**須以成員層之比對為據**，不得以計數相等代替。
本條**不論二集合是否同母體**皆適用 —— 同母體之計數相等更具說服力
之外觀，故更易誤用。

計數相等為等同性之**必要非充分條件**。兩集合大小相同而成員不同者，
其計數比對必然通過。

書寫要求：主張等同性時，須一併載明所用之成員比對方法及其結果
（例如「逐字集合比對，差集為空」、「一對多者 0 筆」）。
僅寫「n 恰等於 n」而無成員層證據者，視為論證不足，
須補驗或改寫為較弱之陳述。

本條與 R-VC15 之分工：
  R-VC15 —— 拘束**跨母體**之數字互援（不同母體之數字不可互援）
  R-VC17 —— 拘束**等同性主張之論證形式**（不論母體是否相同）
二者可同時適用，亦可各自單獨適用。

立條由來：執行層於 T45 自查所得（REV-12）。
分析層同期之 REV-11 為 R-VC15 之由來，二者為同一病灶之跨母體版與
同母體版。
```

---

```
R-VC18（Phase 4 pilot：Glove Box）

（Pei 2026-08-26 裁定。）

pilot Test Set ＝ **#3 `Glove Box`**（R-VC16）。

範圍：12 leaf（117 leaf 母體）／ 8 section（66 section 母體）——
  4.1  SWE1-HMI-VC-026-01 / -026-02 / -026-03
  4.2  SWE1-HMI-VC-027
  5.1  SWE1-HMI-VC-028-01 / -028-02
  5.2  SWE1-HMI-VC-029
  6.1  SWE1-HMI-VC-030
  6.2  SWE1-HMI-VC-031
  6.3  SWE1-HMI-VC-032
  7.1  SWE1-HMI-VC-033-01 / -033-02

**產出 12 筆 TC，一 leaf 一 TC。**

`SWE1-HMI-VC-033-01` 之 boundary 拆分（§8.3：門檻−1 / =門檻 /
鎖定期滿）**本輪不做** —— 其門檻因 A-VC14 而未定，拆分點無從定值。
本輪就該 leaf 產 1 筆 TC，其門檻欄填
`PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3）。
DR-VC8 回覆後另裁是否補拆為 2–3 筆。

**本輪不寫回工作簿。** 產出為 JSON，置於 `generated/`。
寫回屬 Phase 6，另裁。

pilot 之收斂條件見下放包 10 §四。收斂後始得議 Phase 4 之全量批次。
```

---

```
R-VC19（VC profile 之設立；§11 引號例外之啟動）

（Pei 授權範圍內之 Tier 2 裁定，2026-08-26。）

本 feature 設立 profile：
  `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md`
命名依既有慣例（CamelCase 無分隔，同 `VehicleSetting`／`PowerModing`／
`UserProfiles`）—— 該慣例非由 `feature` 字串機械推導，見 R-VC1 之註。

profile 之**首要條款**為啟動 IN §11 之引號例外，其範圍嚴格限定：

(a) **僅 `test_item` 上半之 verbatim 區段**得保留來源記法。
    037 `Requirement Title` 之 `'...'` 與 `Requirement Description` 之
    `«...»` 皆為來源記法，於該區段內逐字保留，不改寫。
(b) **作者之散文一律 `"..."`** —— procedure 之按壓標的、
    非引用之 ER 行、括號下半、reasoning，無例外。
    上繳包 10 §3 第 7 項已驗此層全數合規，該狀態須維持。
(c) 保留之記法**須對得上所引之來源列** —— 即該 token 確實逐字出現於
    該 leaf 之 `Title` 或 `Description`。lint 之職責由「禁止」
    改為「驗證其來源」（IN §11 例外末句之明文）。
(d) 本例外**不及於**任何其他欄位、不及於 `«...»` 以外之新記法。
    若日後出現第三種來源記法，須另裁後始得納入，**不得類推**。

依據：IN §11 之例外其啟動條件為「when the feature profile says so」。
在 profile 存在並載明之前，該例外未啟動 —— 執行層拒絕自行援用
（上繳包 10 §5.3 第 2 項）為正確處置。

本條不改任何既有全域條文。R-4 之範圍不變，引號記法**不屬**
排版正規化 —— 其改寫會使讀者無法自 TC 反推規格原文之記法，
損及 verbatim 之證據力。
```

> **⚠ (a) 已擴充、(d) 已作廢 —— 見 R-VC23（下放包 17 §3.2）。**
> 上方條文**原字不改**（R-TM13：不刪除，加註保留）。
> **(a)** 之「037 `Title` 之 `'...'` 與 `Description` 之 `«...»`」**列舉式範圍**
> 擴充為通則：凡逐字出現於所引來源列之記法一律逐字保留
> （含彎引號 `“…”`／`‘…’`、方括號 `[…]`、角括號 `<…>` 等）。
> **(d)** 之「新記法須另裁、不得類推」**作廢** —— 其保護已由 (c)
> （每一保留 token 須對得上所引之來源列）承擔，
> 而逐一列舉之往返成本高於其邊際保護。
> **(b)(c) 不變且更形吃重** —— (c) 為通則化後之**唯一實質保護**，
> 其驗證須逐 token 為之，不得抽樣。

---

```
R-VC20（verbatim 上半含爭議值之處置）

`test_item` 上半之 verbatim 若含一個正由 DR 爭議之值
（其值於 037 二欄不一致，或與規格／DBC 不一致），處置三項：

(a) **verbatim 照抄，不改寫、不迴避、不換欄取值。**
    上半為引用而非斷言；改寫損及 R-S4 所要之規格原句，
    換取另一欄之值則只是換一個爭議值（上繳包 10 §6(a) 已指出）。

(b) **該爭議須於 `reasoning` 明文揭露**，四項齊備：
    二欄各自之逐字內容、其分歧點、以何欄為 verbatim 上半及其理由
    （R-S4 要規格原句，非採信其值）、阻斷之 DR 編號。
    **括號下半之提示（如 `threshold value pending`）不構成揭露** ——
    其為 sibling 區分 token，欄位性質不同（上繳包 10 §6(b) 之自陳正確）。

(c) **該爭議值不得出現於 `expected_result` 之判準位置。**
    ER 是 pass/fail 之依據；一個未定之值不得成為判準。
    ER 應以行為表述（「the deactivation feature is blocked」），
    次數門檻由 procedure 之 `PENDING` 承載。

即時適用：`SWE1-HMI-VC-033-01` 依 (a) 保留 Title 之
`After three sequential wrong PINs` 為 verbatim 上半；
依 (b) 補 `reasoning` 之四項揭露；依 (c) **須複查其 ER 是否出現
`third`／`three`／`fourth` 等次數判準**，出現即改為行為表述。

DR-VC8 回覆後，本筆依其值 Revise，並依 R-VC18 另裁是否補拆
boundary 之 2–3 筆。
```

---

```
R-VC21（Phase 4 全量批次計畫）

（Pei 2026-08-26 裁定：順序准、規模准。）

pilot（`Glove Box`，12 TC）已收斂放行（下放包 13 §一）。
剩餘 105 leaf（117 leaf 母體）分 **7 批**，一 Test Set 一批，
**不跨組合批** —— Test Set 為 framework 所定之能力群，
跨組會使 `Test Set` 欄在同一批內分歧，批次即失去作為審閱單位之意義。

順序（排序判準依序為：DR 阻斷程度 → 格式形態新舊 → 規模）：

  1  `Category Structure`      24 leaf   無 DR 阻斷
  2  `Settings List`           30 leaf   無 DR 阻斷
  3  `Controls`                17 leaf   DR-VC1（僅 `VC-021` 一筆）
  4  `Settings Behavior`       15 leaf   無 DR 阻斷；含 2 個 P0 ＋ R-VC14 揭露
  5  `Ignition Availability`   16 leaf   DR-VC5（FROP 跨域全 16 筆）
  6  `Brake Service`            2 leaf   DR-VC3（邊界待重審）
  7  `Cabrio Widget`            1 leaf   DR-VC3（同上）

第 4 批不更前之理由：其含本 feature 5 個 P0 中之 2 個
（`035-03`／`036-02`）與 R-VC14 之分歧揭露義務（`036-01`）；
第 1、2 批將首次驗證非 Glove Box 形態之格式，待其穩定再做第 4 批風險最低。

第 6／7 批置末之理由：R-VC16(c) 明文其邊界待 DR-VC3 重審，
且屆時章 8／9 之 Cabrio 本體應另立 `Cabrio Rooftop`。重審前生成，
其結論可能被推翻。

每批之收斂條件：pilot 之十二項（實跑 15 項）＋ 二項：
  13. 該批之 `Test Set` 全筆一致，且與 `framework.md` §2 逐字相符
  14. 該批所用之 setup 片語皆取自 VC profile §5 之常數表

**每批之生成前須先勘查。** pilot 之 `Glove Box` 為純流程需求，
其素材全在文字層，故未設勘查步驟；其餘各組不得據此免除
（下放包 14 §二即為第 1 批之勘查所發現）。
```

---

```
R-VC22（批次之 DR 保留段）

批次內若有 leaf 之**地位**（是否為需求）待 DR 確認者，
該批分二段生成：

  **a 段** —— 地位確定之 leaf，本輪生成。帶 PENDING 者屬之
              （值或素材未到不影響其為需求）。
  **b 段** —— 地位待確認之 leaf，**保留不生成**，
              待 DR 回覆後另裁生成或剔除。

分段之判準為「該 leaf 是否可能整筆消失」，**不是「是否帶 PENDING」** ——
值不明者仍應生成並以 `PENDING: DR-{n}` 佔位（IN §8.4.3）；
地位不明者生成即可能全數作廢。

拘束四項：
(a) b 段之 leaf 須於該批之上繳包**逐筆列名**，載其阻斷之 DR 與保留理由。
(b) 該批之收斂條件以 **a 段之筆數**為母體，不以 Test Set 之 leaf 總數為母體。
    收斂不等於該 Test Set 完成。
(c) `framework.md` 之該 Test Set 不因分段而改動 —— 其 leaf 數仍為原數。
    分段是生成之安排，不是 Layer 2 之變更。
(d) b 段解除後之補生成，其收斂條件與 a 段同，且須複驗 a 段未因補入而失效
    （特別是 `test_item` 括號下半之兩兩不同須以 a＋b 全集重驗）。

第 1 批之適用：a 段 22 筆、b 段 2 筆（`VC-007-01`／`VC-013-04`，
阻斷於 DR-VC9(二)）。
```

---

```
R-VC23（R-VC19 之擴充：來源記法之通則化）

R-VC19(a) 之「037 `Title` 之 `'...'` 與 `Description` 之 `«...»`」
之列舉式範圍，**擴充為通則**：

  `test_item` 上半之 verbatim 區段內，**凡逐字出現於所引來源列
  （037 `Title`／`Description`，或 R-VC7 所定之 SYS1 權威複本）
  之記法，一律逐字保留**，不改寫、不正規化、不轉為 `"..."`。
  含但不限於：`'...'`、`«...»`、彎引號 `“...”`、方括號 `[...]`、
  角括號 `<...>`。

R-VC19(b)(c)(d) 之其餘拘束**不變且更形吃重**：

(b) **作者之散文一律 `"..."`**，無例外。本條擴充之範圍
    **僅及於 verbatim 上半**；procedure 之按壓標的、非引用之 ER 行、
    括號下半、reasoning，一律 `"..."`。
(c) **每一個保留 token 須對得上所引之來源列** ——
    即該 token 逐字出現於該 leaf 之 `Title`／`Description`／SYS1 對應句。
    **本條為通則化後之唯一實質保護，其驗證須逐 token 為之，
    不得抽樣。**
(d) 原「新記法須另裁」之要求**作廢** —— 其保護已由 (c) 承擔，
    且逐一列舉之往返成本高於其邊際保護。

**IN §11 之方括號禁令於本例外之範圍內讓位** ——
該禁令之立意為「禁止作者使用方括號」，非「禁止引用含方括號之原文」。
作者自書之方括號仍禁（(b) 所轄）。

即時適用：`VC-042-01`／`VC-043` 之彎引號與方括號，
於其 `test_item` 上半逐字保留。
```

---

