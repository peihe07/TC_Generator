# RULINGS — SW Update (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 SW Update 之裁決權威；
跨 feature 條文承接時註明來源包。

來源：`docs/handoff/01_intake_recon.md` §二（下放包 01，Pei 2026-08-27
裁定 Q1–Q7）與 `docs/handoff/02_asu1_rulings.md` §二（下放包 02，
A-SU1 重裁之 R-SU4 v2／R-SU6 v2）。抄錄依下放包 02 §三 之指示：
R-SU1／R-SU2／R-SU3／R-SU5 取 01 原文，R-SU4／R-SU6 取 02 之 v2 全文
（含沿革行）；v1 不入本檔正本，其履歷由 v2 之沿革行 citation-by-reference
承載（R-G13）。抄錄逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。
逐條字面一致核對結果見 `docs/upstream/01_intake_recon.md`。

---

```
R-SU1（feature 身分與 test_group）

`feature` 為 `SW Update`，slug 為 `sw_update`，`test_group` 為
`SW Update`。（Pei 2026-08-27 裁定 Q1、Q6。）

命名依據：037 檔名作 `SoftwareUpdate`、SYSAD 作 `Software Update`、
CFTS 母件為 CFTS_57 Reflash —— 交付面統一取 `SW Update`，
由 Q6 裁定，不再援引來源檔名之拼寫。

裁決前綴為 `R-SU`、異常前綴為 `A-SU`、資料請求前綴為 `DR-SU`，
不與任何既有 feature 共用序號。

`scripts/new_feature.py` 之 abbr 推導（`feature[:2].upper()`）對
`SW_Update` 產出 `SW`，與規定前綴 `SU` 不符 —— 此為 A-VC4 / A-TM04
既已登記之同源缺陷，本 feature 不重複立案，以 T0b 字串更正處理。
```

---

```
R-SU2（036 母本與 workbook_state）

（Pei 2026-08-27 裁定 Q7 准。）

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

**本條之前提為「Pei 手上無既存之 SW Update 036」。** 若日後出現
含他人已填 done region 之既存 036，本條即失效，須重裁，且 §三之
母體全集須先與該工作簿之既有 req_id 集合做差集。
```

---

```
R-SU3（驗證母體 —— Q2 之落地）

（Pei 2026-08-27 裁定 Q2「按 037 有納入的範圍」；本條為其落地解讀，
Pei 2026-08-27 裁認。）

驗證母體為 037 `AnalysisReport_FULL` 之：

  `Functional Requirement`     307 列
+ `Non Functional Requirement`   4 列（SWE1-FOTA-281 ~ 284，
                                      皆 Service / High，內容可測）
= **311 列**

不入母體：
- `Heading` 45 列、`Information` 25 列
- `SWE1-FOTA-296`（`Categorization` 為空白；title `Regular Updates`，
  實為標題性質列）
- `SWE1-FOTA-335`（`Out of scope`；title 為空）

範圍以 037 實際納入為準 —— SYSAD 分解出之四線
（Software Update via USB / FOTA / ROV FOTA / TBM FOTA）中，
037 未納入之內容（見 §四 4.5 之觀察）**不補、不擴**，
不因 SYSAD 或 CFTS_57 有相應章節而外加需求單元（IN §8.2）。
```

---

```
R-SU4 v2（spec_reference 之雙家族錨點 —— (a) 依 A-SU1 更正，增 (a2)）

（Q3 准、Q4 之 Pei 裁定不受動搖；本 v2 更正 (a) 揭露段並新增 (a2)。）

本 feature 之 spec_reference 有兩個家族：

(a) CFTS 家族 —— IN §10.7(a)：`CFTS057-{ObjectID}`，ObjectID 為
    CFTS_57 Reflash 內之 7 位 Polarion 號碼。
    素材身分更正（A-SU1）：repo 原件為**真 OOXML docx**（133,530 B）；
    v1 之「UTF-8 純文字衍生本、非權威二進位原件」揭露段撤銷。
    Q3 裁定（ObjectID 可用作錨、不另發 DR）照舊。

(a2) 錨點池範圍（本輪新裁）：**不限 TOC brace 形 87 個**。
    池 = CFTS_57 原件中**可結構驗證**之 Polarion 物件 ID 全集，
    含「章節（heading）物件」與「正文需求物件」兩類。
    裸 7 位數之 regex 命中（A-SU1 實測 649 次／unique 633）
    **不逕入池** —— 須逐一以其在 document.xml 之結構脈絡驗證
    （所屬段落／表格、相鄰需求文句、與章節物件之從屬），
    三分類：章節物件／需求物件／不可歸類。
    不可歸類者排除並列表回報，不得入池（IN §8.4.1 同理：
    regex 命中非結構事實）。
    TC 錨定以**需求物件 ID 為先**；驗證對象為章節整體時
    方用章節物件 ID。
(b) HMI Logic and Flow 家族 —— IN §10.7(b)：
    `SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_(Aug_30_2023)_{章節號}`
    章節 token 逐字取 SYS1 export `Basic Report` 之
    `SYSRE_HMI_Source ID` 欄原值，不構造、不改寫、不去括號、
    不重新 token 化（R-VC4 同理）。

排列一律依 IN §10.7：一個 ObjectID／章節號一行，前綴逐行重述，
禁用 `,`、`、`、`;` 串接，同文件內升冪；同一 TC 兼引兩家族時
CFTS 行在前、HMI 行在後。

本 037 為 18 欄舊版面，無 `HMI Source ID` 欄 —— 037 列與錨點之
對應仍於 Phase 2/3 建立錨定協定（候選錨表 + 雙路驗證，R-AM15）。
本條定家族形態與池範圍，不定對應方法。

`spec_reference_template: null`（查得，非構造）。
`spec_mode` 由執行層依 FO §3 實測後填入。

沿革：v1 見下放包 01 §二；(a) 揭露段撤銷依據 A-SU1（2026-08-27）。
```

---

```
R-SU5（037 之 Source Requirement ID 欄）

037 之 `Source Requirement ID` 欄形態為 `SYS-RA-FOTA-{n}`，
分析層實測：非空 373 列、值域 1–526、unique 364，
**9 個 source id 被多列引用**（43, 68, 69, 112, 395, 411, 444, 475, 480）。

拘束三項：
(a) `spec_reference` 不得取本欄 —— 本欄指向之 SYS-RA 母體
    無對應規格檔可查，且與兩家族錨點（R-SU4）無字面關係。
(b) 本欄僅作 037 內部追溯保留，不進入任何 TC 欄位。
(c) §四 4.5 之三項 SYSAD 分配表錯位觀察，Pei 裁定（Q5）
    **不立 A 案、不發 DR** —— 記錄於下放包即止，
    不阻斷任何 Phase，後續不再重提。
```

---

```
R-SU6 v2（HMI Logic and Flow 規格本文之可及性 —— 依 A-SU1 重裁）

repo 原件實測（A-SU1）：真 PDF 1.6，68 頁，68/68 頁皆有文字層，
共 83,286 字元。v1 所稱「zip 容器、137 張 JPEG 頁圖、無文字層、
不可檢索」為附件傳遞產物之性質，非素材本身 —— v1 全條撤銷。

處置：
(a) SYS1 export 為本規格之參考索引（不變）：章節定位與描述文之
    第一查找來源；spec_reference 之章節 token 仍逐字取其
    `SYSRE_HMI_Source ID` 欄原值。
(b) 規格內文一律機器抽取 —— R-G36 正常適用，本件有文字層可抽。
    抽取以頁為單位（PyMuPDF page.get_text() 或等效）。
    **p.{n} 頁碼記錄保留為覆核義務**：凡自本 PDF 取用之值
    （不論文字抽取或目視），記其頁碼入 reasoning 或工作檔。
    理由：本家族之錨 token 為 SYS1 章節號，頁碼是內文細節
    （彈窗表、流程細節）之唯一重走定位；逐頁抽取下記頁碼成本趨零。
(c) 文字層未載之圖形內容（流程圖、畫面版面）仍以頁圖 render 目視，
    同記 p.{n}；判讀不確定時依 IN §8.4.1 保留模糊、登記待查，
    不得補值（v1(d) 併入本項）。

沿革：v1 見下放包 01 §二；撤銷依據 A-SU1（2026-08-27）。
```
