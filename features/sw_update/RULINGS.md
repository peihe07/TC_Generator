# RULINGS — SW Update (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 SW Update 之裁決權威；
跨 feature 條文承接時註明來源包。

## 現行版索引（R-SU8(b)）

> 判準（R-SU8(a)）：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-SU1 | v1 | feature 身分與 test_group（`SW Update`／`sw_update`；前綴 R-SU／A-SU／DR-SU） | 01 §二 |
| R-SU2 | v1 | 036 母本與 workbook_state = BLANK；寫回採 XML 外科式修改 | 01 §二 |
| R-SU3 | v1 | 驗證母體 311 = FR 307 + NFR 4；範圍以 037 實際納入為準 | 01 §二 |
| R-SU4 | **v2** | spec_reference 雙家族錨點（CFTS057-{ObjectID}／SYS1 章節 token）+ 錨點池範圍 (a2) | 02 §二 |
| R-SU5 | **v2** | 037 Source Requirement ID 欄之三形態；該欄不取為 spec_reference | 03 §2.1 |
| R-SU6 | **v2** | HMI 規格本文為真 PDF，全文字層；一律機器抽取，p.{n} 為覆核義務 | 02 §二 |
| R-SU7 | **v2** | Description 物件不入池；錨點池 574 = 章節 87 + 需求 487，Description 137 | 04 §1.2 |
| R-SU8 | v1 | 本表之判準：v 字尾最大者為現行；檔首須維持索引表 | 05 §二 |
| R-SU9 | v1 | recon 產物之重生條件（未簽佔位得刪檔重生並揭露；已簽或含人手內容不得刪） | 05 §二 |
| R-SU10 | v1 | Layer 2 分群鍵為 Heading id（非標題字串）；Test Set 名稱另命名 | 06 §二 |
| R-SU11 | v1 | framework Layer 3 主軸為 CFTS_57；SYS1 不作章對章橋接，其接點為 HMI 87 列 | 06 §二 |
| R-SU12 | v1 | 逐列對照之軸改為 037 `Requirement Description` × CFTS_57 需求物件全文；標題比對降為輔助 | 07 §二 |
| R-SU13 | **v2** | 錨定之驗證三支柱（文本路／序位一致性／自證錨）、探針來源限制、自檢四項 | 08 §二 |
| R-SU14 | v1 | 兩階段錨定：不取首選為錨，取前 5 候選 + 裁決；一列多錨為正常 | 09 §四 |

**留存之被取代條文（依 R-TM13 不刪不改，不得引用）**：

| 條號版本 | 已被取代於 | 其所載之失效值 |
|---|---|---|
| `R-SU5`（v1） | R-SU5 v2 | 「欄形態為 `SYS-RA-FOTA-{n}`」單一形態陳述；非空 373／unique 364 |
| `R-SU7`（v1） | R-SU7 v2 | 池 565、需求 478、Description 135 |
| `R-SU13`（v1） | R-SU13 v2 | 「A 用文字、B 用序號，**無共用輸入**」之獨立性表述；未限制探針來源；H 級分差判準未定 |

---

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
R-SU5 v2（037 之 Source Requirement ID 欄 —— 依 A-SU2 更正形態陳述）

037 之 `Source Requirement ID` 欄 383 列**全部非空**，實測三形態：

(i)   `SYS-RA-FOTA-{n}` 純形態 —— 370 格
(ii)  `SYS-RA-FOTA-{a}/SYS-RA-FOTA-{b}` 併記 —— 3 格：
      SWE1-FOTA-171（336/334）、175（360/361）、216（506/507）
(iii) `SYS-RA-VF747_V2-{n}`（7 格：225, 226, 227, 228, 230, 239, 240）
      與 `SYS-RA-VF747_V6-{n}`（3 格：241, 242, 243）—— 計 10 格

v1 之「非空 373／unique 364」為 first-id-only 抽取條件下之正確值
（上繳包 01 §三 3.3 已閉合重現）；全集之 FOTA id unique 數由
執行層量測入台帳（T11），後續引用以台帳為準。

拘束照舊：
(a) `spec_reference` 不得取本欄。FOTA 族（i)(ii)：其 SYS-RA 母體
    無對應規格檔可查，理由不變。VF747 族（iii)：v1 之理由**不成立**
    —— 手上有 `Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx`；
    惟引用版本為 V2／V6、在手文件為 V1_R3（版本落差），且其
    物件結構未經 repo 原件實測（A-SU1 之教訓：不得以附件複本
    斷原件）。故 (a) 對 (iii) **暫行維持**，是否為該 10 列另立
    第三錨點家族，待 T11 量測後提 Pei 裁。
(b) 本欄僅作 037 內部追溯保留，不進入任何 TC 欄位（不變）。
(c) SYSAD 分配表三項錯位觀察不立案不再提（不變，Q5）。

沿革：v1 見下放包 01 §二；形態更正依據 A-SU2（2026-08-27）。
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

---

```
R-SU7（CFTS_57 之 Description 物件 —— 不入錨點池）

上繳包 01 T10 實測：CFTS_57 原件含 `[Artifact Type:Description]`
物件 135 個，為結構可驗證之 Polarion 物件，但既非章節亦非需求。

裁定：**不入錨點池**（池維持 565 = 章節 87 + 需求 478）。

理由：TC 之錨指向其驗證之需求單元（IN §10.7(a)、§8.2 需求單元
由上游定義）；Description 為需求之從屬說明內容，以之為錨會使
追溯碎裂於單元之下。

配套：Description 內容於 TC 撰寫中被取用時，**錨落其所屬之
需求／章節物件**。為此 `ANCHOR_POOL.md` 須補「Description →
所屬物件」對照（T12）；對照不可解者列表回報，其內容在對照
落地前不得作為 TC 之依據（IN §8.4.1）。
```

---

```
R-SU7 v2（CFTS_57 之 Description 物件 —— 統計數依 T12 分類法修正）

（Pei 2026-08-27 准統計數更正。）

上繳包 02 T12 實測：T10 之「首見為準」分類法將 11 個帶
`[Artifact Type:…]` 宣告之 id 誤歸「不可歸類」；改採
**宣告優先於文序**後：

  錨點池 = **574**（章節物件 87 + 需求物件 **487**）
  Description 物件 = **137**（歸需求 45、歸章節 92、不可解 **0**）
  不可歸類 = 10

v1 之 565／478／135 為分類法缺陷下之值，撤銷；成因為量測法
修正，非素材變動（素材 sha 不變）。兩路獨立計數閉合：
87 + 487 + 137 + 10 = 721 = 裸命中 unique 總數。

其餘不變：Description 不入池；其內容被取用時錨落所屬需求／
章節物件，對照表見 `ANCHOR_POOL.md` §六（137/137 可歸，
空表確認）。

沿革：v1 見下放包 03 §二 2.2；更正依據上繳包 02 §一 T12。
```

---

```
R-SU8（RULINGS.md 之現行版判準與索引）

`RULINGS.md` 依 R-TM13 保留被取代之條文（不刪除、不改寫）。
為免自動化或人工讀取誤用已撤銷之值，定判準二項：

(a) 同一條號有多個版本區塊時，**v 字尾最大者為現行**；
    無 v 字尾者視為 v1。被取代之版本僅供沿革查考，
    其所載之任何數值、形態陳述、拘束一律不得引用。

(b) `RULINGS.md` **檔首須維持現行版索引表**：條號、現行版、
    一句話主旨、來源下放包。每次 append 新版本時同步更新該表；
    索引表與條文區塊不一致時，**以條文區塊為準**，並即修索引。

本條之目的為讀取安全，不改變 R-TM13 之保留義務。
```

---

```
R-SU9（recon 產物之重生條件）

`scripts/recon.py` 於 `DECISIONS.md` 已存在時改寫 `DECISIONS.new.md`
（A-TM15 機制），其目的為保護**人手內容**。判準：

(a) 既有檔之簽核欄全為未簽佔位（`[PROPOSED]`／`[PEI]` 未填）
    且無任何人手編輯痕跡者，得刪檔令 recon 就地重生，
    **但須於上繳包揭露「刪檔重生」與其判定依據**。
(b) 任一項已簽、或含人手撰寫之內容者，**不得刪檔** ——
    保留 `.new` 並逐項人工合併，合併結果附 diff 上繳。
(c) 判定不確定時一律走 (b)。

本條同理適用於其他「已存在即改寫 .new」之腳本產物。
```

```
R-SU10（Layer 2 分群鍵）

037 之 `Categorization == Heading` 45 列，其標題僅 41 unique ——
`Critical Updates`、`OTA Architecture Requirements`、
`OTA Client Configuration options`、`User initiated sessions`
各出現兩次而轄不同區間（上繳包 04 §3.1 實測）。

裁定：
(a) framework 之分群鍵一律為 **Heading id**（`SWE1-FOTA-{n}`），
    不得以標題字串為鍵。
(b) Test Set 名稱由分析層另行命名（IN §4.2：能力叢集名詞，1–3 字），
    **不得逕取 Heading 標題**；Heading 標題僅為命名之素材。
(c) `framework.md` 之 Layer 3 欄須同時記 Heading id 與其標題原文，
    俾碰撞可見。
```

---

```
R-SU11（SYS1 之橋接軸）

037 Heading 與 SYS1 章之標題對照率僅 2/45（上繳包 04 §3.2 實測），
且 2 筆同對一章。成因：SYS1 之 28 章為 **HMI 畫面／流程視角**，
037 之 45 Heading 為**需求功能視角**，兩者非同一骨架之兩份副本。

裁定：
(a) framework 之 Layer 3 **主軸為 CFTS_57 章節**（對照率 42/45）。
(b) SYS1 **不作章對章之橋接**。SYS1 之接點為 037 之 **HMI 87 列**
    ——逐列（非逐 Heading）對 SYS1 之 120 個 outline entry 定位。
    此定位屬 Phase 2/3 之錨定協定，本條只定其軸，不定其方法。
(c) 純 Service 之 28 個 Heading 群（224 列）無 SYS1 接點，
    其 spec_reference 走 CFTS 家族單軌（R-SU4 v2(a)）；
    此為**預期狀態**，不因缺 HMI 錨而登記異常。
```

---

```
R-SU12（037 列與 CFTS_57 之對照軸）

實測（上繳包 05 §0、§6）：以 037 列之 `Requirement Title` 對
CFTS_57 之 **章節標題** 作詞集重疊比，311 列中 286 列（92%）
未達門檻，可比者僅 25 列。判別力不足以支撐 Layer 3 或錨定。

成因：比對兩端不對稱 —— 左端為需求句摘要，右端為目錄名詞。

裁定：
(a) 逐列對照之軸改為 **037 列之 `Requirement Description`（全文）
    × CFTS_57 之 487 個需求物件全文**。章節歸屬由需求物件之
    母章導出（`ANCHOR_POOL.md` 已載母子關係），不再逐列對章節標題。
(b) 標題對章節標題之比對（T18d／T19）**降為輔助訊號**，
    其結果不得單獨作為任何對應之依據；已產出之表列保留供交叉查考。
(c) 對照結果為**候選**，非結論。任何一列之最終錨點須經 R-SU13
    之雙路檢定並由分析層裁定；執行層不得逕定。
(d) 本條不改變 R-SU4 v2 之錨點形態，亦不改變 R-SU11(a)
    之 Layer 3 主軸（仍為 CFTS_57）—— 只改「怎麼對上」。
```

---

```
R-SU13（錨定之雙路驗證與信度分級）

單一相似度分數不足以定錨（R-AM15 之教訓）。錨定須兩條**互相獨立**
之路徑：

路徑 A —— **文本路**：037 列 `Requirement Description` 全文
  × CFTS_57 需求物件全文之相似度，取前 N 候選。
路徑 B —— **序號路**：037 列之 `Source Requirement ID`
  （`SYS-RA-FOTA-{n}`）之連續段落，對 CFTS_57 需求物件之
  文件序連續段落作區塊對位。037 列之 SYS-RA 號多呈連續遞增／
  遞減段（上繳包 05 §2 可見），該段之整體落點為區塊級證據。

兩路之獨立性：A 用文字、B 用序號，無共用輸入。

信度分級：
  **H**（高）—— A 之首選與 B 之區塊落點**同章**，且 A 首選分數
        與次選有明顯差距
  **M**（中）—— A、B 同章但 A 之首選與次選接近，或僅一路可判
  **L**（低）—— A、B **不同章**，或兩路皆不可判

處置：H 得逕列入錨表；M 列入並標記，撰寫該列 TC 時須人工複核；
**L 不得列入錨表** —— 集中列表由分析層裁，未裁定前該列之
`specification_reference` 依 IN §8.4.3 掛 `PENDING`。

自我檢定為**結構前提，非選配**（PLAYBOOK §7.1）：跑全母體前須先做
(i) 已知標的探針 —— 取已由分析層確認之對應（如 `SWE1-FOTA-351
Server-Initiated Session Flow` 對 CFTS `4.10.2`），檢查管線是否命中；
(ii) 反向輸入 —— 餵入與本 feature 無關之文字，確認其**不**產生高分
候選。兩項皆須於上繳包附原始輸出。
```

---

```
R-SU13 v2（錨定之驗證設計與自我檢定 —— v1 三處缺陷之更正）

v1 之三處缺陷（皆分析層之誤，上繳包 06 §1、§7 實測揭示）：
(1) 未限制「已知標的探針」之來源，致所指定之探針取自同包內
    剛被降為輔助訊號之比對路徑；
(2) 稱路徑 A、B「無共用輸入」，實作證明 B 之落點須用 A 之結果；
(3) 未定 H 級「明顯差距」之判準，迫使執行層自訂。

v2 條文：

**一、探針來源之限制（新增）**
「已知標的探針」之對應必須來自下列之一：
  (a) 分析層**逐案人工裁定**並記錄其依據者；
  (b) 來源文件**自身寫出**之對應（如 037 之 `Requirement Description`
      直接引用 CFTS ObjectID 或章節號）；
  (c) 上游交付物之既有欄位所載者。
**不得取自任何自動比對之產物**，尤其不得取自已被降級之路徑。
探針不足 3 例時，先建地面真值再自檢，不得以弱探針代之。

**二、驗證之三支柱（取代 v1 之「兩路獨立」）**
  支柱 1 —— **文本路（A）**：037 列 `Requirement Description` 全文
    × CFTS_57 需求物件全文之相似度，取前 N 候選。
  支柱 2 —— **序位一致性檢定（取代 v1 之路徑 B）**：037 列於文件序
    遞增時，其對應之 CFTS 需求物件於 CFTS 文件序**應大致單調不減**。
    以此為**約束**檢出違序列，非以此為第二來源。
    宣告：本支柱**不是獨立第二路**，是加諸於 A 之結構約束；
    其價值為壓制單列噪音與檢出跨章。段長為 1 者不適用。
  支柱 3 —— **自證錨（新增）**：來源文件自身寫出之對應（同上 (b)），
    為唯一之真地面真值。其數量少不減其效力。

**三、信度分級**
  **H** —— A 之首選符合序位一致性，且首選與次選之分差達判準
  **M** —— 符合其一
  **L** —— 皆不符，或兩者不可判
判準之數值**由分析層依地面真值樣本裁定**，執行層不得自訂；
未裁定前一律標記為「判準待定」，不得產出最終分級。

**四、自我檢定（結構前提，不得省略）**
  (i)   已知標的探針 —— 依「一」之來源限制，≥ 3 例
  (ii)  反向輸入 —— 與本 feature 無關之文字 ≥ 3 例，
        判準須以母體分布為基準並揭露其取樣方式
  (iii) 自證錨全數回測（支柱 3）
任一項不通過即停，不跑全母體。**執行層不得自換探針** ——
探針之效力由分析層裁；發現更強之探針應增設並回報，不取代。

沿革：v1 見下放包 07 §2.3；撤銷依據上繳包 06（2026-08-27）。
```

---

```
R-SU14（兩階段錨定）

地面真值實測（下放包 09 §三，17 列人裁）：路徑 A 之正解落於前 5 候選
之比率為 17/17（100%），A 首選即完整正解之比率為 12/17（71%），
首選之章正確為 14/17（82%）。

裁定：錨定分兩階段，**不取首選為錨**。

**階段一 —— 章級（供 framework Layer 3）**
以路徑 A 之前 5 候選之章分布為輸入，經回測選定之決策規則產出章級歸屬
與信度；規則之選定須以地面真值回測為據（不得自訂閾值）。
低信度者由分析層人裁。

**階段二 —— 物件級（供 spec_reference）**
於撰寫該列之 TC 時，自該列之前 5 候選中裁定其正解物件，
**得為多個**（IN §10.7 本即一列多行）。裁定依據記入該列之
`reasoning`。前 5 候選中無正解者，掛 `PENDING` 並登 DR
（IN §8.4.3），不得取次佳者充數。

**拘束**：
(a) 「前 5」之 5 為地面真值回測值，非任意數；若日後回測顯示
    召回不足，得由分析層調整並記其依據。
(b) 執行層產出候選與信度，**不裁定正解**。
(c) 一列多錨為正常結果，非異常（§三 #4、#18 之實證）。
```
