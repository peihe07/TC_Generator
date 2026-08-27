# 下放包 02 —— A-SU1 重裁（R-SU6 v2／R-SU4 v2）與續行指示

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`01_intake_recon.md`（其 §三 3.1 格式判定由本包更正；其餘不動）
- 對應上繳：仍為 `features/sw_update/docs/upstream/01_intake_recon.md`
  （同一輪，T0–T10 一包收）
- 裁定狀態：R-SU6 v2、R-SU4 v2 —— 分析層依 Pei 2026-08-27 授權即裁；
  A-SU1 → RESOLVED

---

## 一、A-SU1 之處分

A-SU1 成立，成因採認：**衍生本／圖檔身分為 Claude Project 附件傳遞
所致，非素材本身性質**（A-VC7 同源同型）。處分四項：

1. R-SU6 全條撤銷，以 v2 取代（§二）
2. R-SU4(a) 揭露段撤銷更正，並增 (a2) 錨點池條款（§二）
3. 下放包 01 §三 3.1 之「已裁認事實」標記**撤回**；#3–#6 之格式與
   大小以 A-SU1 §一之 repo 實測表為準（真 OOXML ×3；真 PDF 1.6、
   68 頁全文字層、83,286 字元、4,955,682 B）
4. 不發 DR（素材在本機）；T7 之 0 筆不變

A-SU1 於 `ANOMALIES.md` 改記 RESOLVED，處分文引用本包（R-G13
citation-by-reference，不重抄全文）。

---

## 二、裁決條文 v2（全文，取代 01 §二 之同號條文）

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

## 三、RULINGS.md 抄錄指示（解除暫停）

抄入 `features/sw_update/RULINGS.md`，逐字（R-G23）：

- R-SU1、R-SU2、R-SU3、R-SU5：依下放包 01 §二 原文
- R-SU4、R-SU6：**依本包 §二 v2 全文**（含沿革行）；
  v1 不入 RULINGS.md 正本 —— v1 從未生效於該檔，沿革行之
  citation-by-reference（指向下放包 01 §二 + A-SU1）即為履歷，
  不重抄已撤文字

上繳包附六條之逐條核對結果。

---

## 四、任務（T1 起解除暫停，含修訂）

| # | 任務 | 修訂 |
|---|---|---|
| T1' | **素材搬入 `inputs/` 由 Pei 執行**（A-SU1 處置）。執行層只做：搬入前（源資料夾）／後（inputs/）各記一次 SHA256 + mtime 入素材台帳，六份逐一；源資料夾唯讀 | 分工修訂 |
| T2 | 照跑 intake.py，如實回報。01 §三 3.2 之「預期不命中」判斷基於 037 分頁名，與 A-SU1 無涉，維持；其餘素材之分類以實測為準 | 不變 |
| T3 | 照 01 | 不變 |
| T4' | 照 01 之數字重測比對；惟 §三 3.1 之 #3–#6 格式／大小改對 **A-SU1 §一之 repo 實測表**比對（01 該四格已撤）。A-SU1 §一已交叉確認之 037／SYS1 結構量仍全項重跑，不因已確認而略 | 基準修訂 |
| T5' | `PU\d+` 掃描擴為**兩源**：(i) 037 全欄（含列號）；(ii) PDF 文字層逐頁（含頁碼；A-SU1 已見 p.10 `POP UP REQUIREMENTS` 表與 `PU0152`）。兩源分列回報，對 `forms/Pop Up List HMI R1 (26PI).xlsx` 查存在性，查得與否皆如實 | 擴源 |
| T6–T9 | 照 01（T8：A-SU1 改記 RESOLVED；T9：feature.yaml 之 spec_pdf 註解改「真 PDF 1.6，68 頁全文字層」） | 微修 |
| T10 | **錨點池結構驗證**（R-SU4 v2 (a2)）：自 CFTS_57 原件 document.xml 抽全部 7 位數命中，逐一附結構脈絡三分類（章節物件／需求物件／不可歸類），產出 `features/sw_update/ANCHOR_POOL.md`：id、所屬章節、類型、驗證脈絡摘句；末附三類計數與不可歸類全清單。**只分類不對應** —— 037 對應屬 Phase 2/3 | 新增 |

---

## 五、上繳包要求（併入 01 §七，仍一包收）

1. 01 §七 之 1–7 全項（T 編號依本包修訂版）
2. A-SU1 之 RESOLVED 記錄（處分引用本包）
3. T10 之三類計數與 `ANCHOR_POOL.md` 路徑
4. 六條裁決（R-SU1/2/3/5 = 01 原文；R-SU4/R-SU6 = 本包 v2）逐條核對結果
