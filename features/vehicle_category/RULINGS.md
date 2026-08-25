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

