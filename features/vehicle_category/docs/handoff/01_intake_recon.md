# 下放包 01 —— Vehicle Category 開案（Phase 0 intake + Phase 1 recon）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/01_intake_recon.md`
- 前一包：無（本 feature 首包）
- 裁定狀態：Q1 甲、Q2 准、Q3 甲、Q4 准（Pei 2026-08-25）—— **全部已裁，無待裁項**

> **落檔說明（2026-08-25 補）**：本包原僅存在於分析層之對話輸出，未寫入 repo，
> 致執行層無全文可依。本次為原文落檔，§一–§九**逐字未改**。
> 落檔後之狀態更新見 **§十**（事後附記），該節為新增，非原文之一部分。

---

## 一、本包之目的與界線

建立 `features/vehicle_category/` 之骨架、驗明三份素材、實測工作簿欄位對應與
`workbook_state`，並完成 Phase 1 recon。

**本包不產出任何 TC，不寫回工作簿，不動 git。**

界線宣告（canon §5a）：本包 §三、§四之全部數字量自 Claude Project 附件複本，
**非** repo 內複本。執行層須對 repo 內複本重測並記 SHA256 入素材台帳；
台帳建立後，後續各輪一律引用台帳所記之實測值，
**不得回頭引用本包之任何數字**。本包之數字僅供 T4 之比對基準。

---

## 二、裁決條文（逐字抄入 `features/vehicle_category/RULINGS.md`）

> 抄錄時逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。抄畢於上繳包附逐條核對結果。

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

## 三、素材與需求母體實測（分析層量測值，供 T4 比對）

### 3.1 素材

| # | 檔名（Project 附件） | 角色 | 大小 |
|---|---|---|---|
| 1 | `FMWIFSM037A03N1LSWE1VehicleCategoryHMIV0.1 STLA 報告.xlsx` | 037 A03 SWRA | 100,475 B |
| 2 | `SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_December_27_2023.xlsx` | SYS1 Polarion export | 47,458 B |
| 3 | `Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_December_27_2023.pdf` | 規格本文 | 3,552,260 B |

> 檔名以 repo 內複本之實際檔名為準；本表之名可能因附件傳遞而經正規化
> （例如 `V0.1` ↔ `V0_1`、空格 ↔ 底線）。T1 須記實際檔名入台帳。

037 分頁：`封面` / `ChangeHistory 修訂履歷` / `Product Document 記錄封面頁` /
`Analysis Report` / `Instructions` / `下拉選單設定處`。

**`Analysis Report` 分頁存在** → `scripts/intake.py` 之 `SHEET_SIGNATURES`
（`"Analysis Report" in names`）可正常命中 `swra_report`。
**Display 之 R-DM5 偏差在本 feature 不成立**，`feature.yaml` 不需
`intake.kind_overrides`，`paths_meta.a03_sheet` 取預設 `Analysis Report`。

修訂履歷：Ver A（2025-12-26 初版）→ D（2026-04-27 增 `HMI Source ID`、
`FROP` 兩欄）。**本 037 為 A03 rev D 版面（20 欄）**。

### 3.2 需求母體

表頭列 = 7；資料列 = 8–152（145 列）；153 以後為空白格式列（至 198）。

| 項目 | 數 |
|---|---|
| 資料列 | **145** |
| 父需求 `SWE1-HMI-VC-NNN` | 66（001–066 連號，無跳號、無重號） |
| 子需求 `SWE1-HMI-VC-NNN-MM` | 79 |
| 有子之父（不入 leaf） | 28 |
| 無子之父（本身即 leaf） | 38 |
| **leaf 全集** | **117** |
| 形態外之 id | 0 |

### 3.3 欄位分布（145 列）

| 欄 | 值分布 |
|---|---|
| `Categorization` | `Functional Requirement` 145/145（無 Heading、無 Out of scope） |
| `Release Version` | `1.00.00` 145/145 |
| `FROP` | `Vehicle Settings` 128、`Power Management` 16、`Audio Management` 1 |
| `Sub Categorization` | `HMI` 103、`Service` 42 |
| `Source Requirement ID` | `SYS-HMI-RA-VC-###`，61 個相異值 |
| `HMI Source ID` | 66 個相異值 |
| `Verification Method`（117 leaf） | 單一字串起首 `Manual functional test on the target head unit: …`，117/117 |
| `Verification Criteria`（有子之父列） | `Please refer to the following IDs:` + 子 id 清單 |
| 第 10–18 欄（`Feasibility`…`Priority`） | 全 145 列皆為 `\xa0`（U+00A0），無內容 |

---

## 四、章節覆蓋落差

### 4.1 量測條件（逐字比對，非模糊）

- 母體：SYS1 `Basic Report` 資料列 2–110（109 列）之有效 `Outline Number`，**108 個**
- 引用集：037 之 66 個 `HMI Source ID`
- 方法：037 `HMI Source ID` 全值 ⟷ SYS1 `SYSRE_HMI_Source ID` 全值，逐字集合比對
- `SYS-HMI-RA` 之 0 命中：對 SYS1 三分頁全儲存格作子字串搜尋

```
SYS1 章節 108 ┃ 037 引用 66 ┃ 未引用 42 ┃ 引用但不在 SYS1 = 0
037 HMI Source ID → SYS1 SYSRE_HMI_Source ID：命中 66/66
```

### 4.2 未引用之 42 節

**(a) 非需求性質，24 節 —— 落差為正常，不入表 B**

| 類 | 章節 |
|---|---|
| 純標題列（章名，無內容） | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16 |
| Assumptions（免責／適用機種／參照文件清單） | 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 |
| 圖檔列 | 2.1 |

**(b) 有實質規格內容而 037 零涵蓋，18 節 —— 表 B 之內容**

| 群 | 章節 | 規格內容摘要 |
|---|---|---|
| Cabrio 車頂開闔 | 8.1, 8.2, 8.3, 8.4, 8.5 | A1/A2 長按開闔全程、放開即停、3D 動畫、車速 < 50 km/h 與最長 15 s 之前提、故障時控制灰化 |
| Cabrio 擋風板 | 9.1, 9.2 | B1/B2 長按升降、放開即停於任意位置 |
| Aux Switch | 10.1, 10.2 | 兩條進入路徑（Controls / Apps）、Type / Power Source / Last State 之四種組合、Last State 之可用條件（Latching + Ignition） |
| Settings 通則邏輯 | 11.9, 11.9.1, 11.9.2, 11.9.3 | 多選項列與單選項列之按壓語意、+/- 列之增減與端值灰化、駕駛分心情境下之整列行為 |
| EPB 彈窗 | 14.2, 15 | 彈窗優先序（E-Call → 來電／簡訊 → System Errors → EPB Service Mode → System Feedback）；PU0132 / 0133 / 0134 / 0136 / 0139 / 0141 / 0143 / 0144 / 0145 / 0202 / 0275 之訊息文字與逾時 |
| Cabrio Widget | 16.1, 16.2.1, 16.2.2 | Widget 內之車頂開闔與擋風板操作（16.2 已有 `SWE1-HMI-VC-066`，惟其僅涵蓋「widget 標題為 Cabrio」一句） |

> 章 8、9、10、15 之 037 列數為 **0** —— 非涵蓋不足，是整章缺席。

### 4.3 已涵蓋章節之 leaf 分布（Layer 3 素材，供 Phase 3 使用）

| 章 | 名稱 | 037 列 | leaf | 已引用章節數 |
|---|---|---|---|---|
| 2 | Vehicle Category Notes | 28 | 24 | 13 |
| 3 | Controls | 19 | 17 | 12 |
| 4 | Glove Box – Activation | 5 | 4 | 2 |
| 5 | Glove Box – Activation Error | 4 | 3 | 2 |
| 6 | Glove Box – Deactivation | 3 | 3 | 3 |
| 7 | Glove Box – Deactivation Error | 3 | 2 | 1 |
| 11 | Settings Templates / Notes | 26 | 20 | 10 |
| 12 | Settings | 31 | 25 | 13 |
| 13 | Settings Behavior and Ignition Status | 22 | 16 | 8 |
| 14 | Electronic Park Brake Service Mode | 3 | 2 | 1 |
| 16 | Cabrio Widget | 1 | 1 | 1 |
| | **合計** | **145** | **117** | **66** |

> 本表為 framework Part N 之**素材**，不是 Layer 2 之提案。
> Layer 2（Test Set）之切分屬 Phase 3，Tier 2，本包不提案。

### 4.4 FROP 跨域列（表 A 之母體）

| FROP | 列數 | 涉及章節 |
|---|---|---|
| `Power Management` | 16 | 13.1, 13.1.1, 13.2, 13.3, 13.4, 13.5 |
| `Audio Management` | 1 | 12.3.2（`SWE1-HMI-VC-048-02`，設定值變更確認音及其例外清單） |

`SWE1-HMI-VC-057` ~ `-064`（含子）之標的為「電源狀態下之 Settings 可及性」，
題材與既有 `power`、`power_moding` 兩 feature 相鄰。
**是否有實際重疊須以 req_id 與 spec_reference 逐列比對後始得斷言**；
本包未做該比對（母體在 repo 內，不在附件內）—— 見 T5。

---

## 五、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T0 | `python scripts/new_feature.py "Vehicle Category"` 建立 `features/vehicle_category/` 骨架。回報實際建出之目錄名 —— **若腳本將空格轉為其他形態而非 `vehicle_category`，停並回報，不得手動改名了事** | 1 |
| T1 | 三份素材置入 `_intake/Vehicle_Category/`，記實際檔名 + SHA256 + mtime 入素材台帳；複製入 `features/vehicle_category/inputs/`，**搬入前後各記一次 SHA256**。來源目錄唯讀 | 1 |
| T2 | 照跑 `scripts/intake.py`，如實回報分類結果。**預期 037 命中 `swra_report`**；若未命中，以 `A-VC{n}` 登記並附證據，**不得預先改腳本使其命中** | 1 |
| T3 | 跑 `scripts/recon.py` → `RECON.md` / `DECISIONS.md` / `recon.json`。工作簿欄位對應以**表頭字串實測**回報命中數（n/n），**不得沿用 `display` 或 `vehicle_setting` 之欄位字母** —— 036 母本雖同，版面 revision 仍須實測 | 1 |
| T4 | 對 repo 內複本**重測**本包 §三、§四之全部數字（145 / 66 / 79 / 28 / 38 / 117、四個欄位分布、108 / 66 / 42 / 66-命中、18 節清單），與本包逐項比對。**不符即停並回報**，不得以本包數字覆蓋實測值 | 1 |
| T5 | 取 `SWE1-HMI-VC-057` ~ `-064`（含子，16 列）之規格章節（13.1–13.5），與 `features/power/`、`features/power_moding/` 之既有 req_id 與 spec_reference 做**逐列比對**，回報有無實際重疊及其筆數。**只回報，不處置**（處置屬 Tier 2） | 1 |
| T6 | 以 `forms/Pop Up List HMI R1 (26PI).xlsx` 查：(a) `PU0091` 是否存在，存在則取其 timeout 與 category；(b) 規格 §15 之 11 個 EPB PU id（PU0132/0133/0134/0136/0139/0141/0143/0144/0145/0202/0275）是否存在。**查得與否皆如實回報**，查無不得代以語意相近者 | 1 |
| T7 | 建立 `DATA_REQUESTS.md`，登入 §六之五筆 DR，編定 `<n>` | 1 |
| T8 | 建立 `ANOMALIES.md`，登入 §七之三筆 A | 1 |
| T9 | 依 §八之草案填 `feature.yaml`。`reference:` 節須綁定：三份素材 + 036 母本 + `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` + `forms/Pop Up List HMI R1 (26PI).xlsx`，逐項記 SHA256（R-G15 / R-DM37 判準：其變動會使既有產出失效者一律綁定） | 1 |

**不在本輪範圍**：`framework.md`（Phase 3）、profile 檔、任何 TC、任何寫回、任何 git 操作。

**逸出即停**：遇 FO §0 之六項觸發任一者，停並填 `DECISIONS.md` 或
`ANOMALIES.md`（證據 + 提案處置），續作不受影響之項目。

---

## 六、資料請求（DR）—— 分析層草擬，**由 Pei 發出**（Tier 3）

| DR | 標的 | 內容 | 阻斷範圍 |
|---|---|---|---|
| DR-VC1 | 037 作者 | 規格 §3.6（CO13）之 Privacy Lock 彈窗 id 於**規格原文即為字面 `PUXXXX`**，非實 id；037 `SWE1-HMI-VC-021` 原樣沿用。請提供實際 PU 編號 | 僅 `SWE1-HMI-VC-021`。缺件期間該 TC 之對應欄填 `PENDING: DR-VC1 Privacy Lock popup ID`（IN §8.4.3），不得留空、不得填 NA |
| DR-VC2 | 037 作者 | `Source Requirement ID` 欄之 `SYS-HMI-RA-VC-###`（61 個相異值）在 SYS1 export 全簿命中 0。請說明該 id 之來源系統，及其對 SYS1 `NRL-######` 之對應關係 | 不阻斷生成（R-VC5(c)）。**交付前須有答覆**以完成雙向追溯 |
| DR-VC3 | 037 作者 | 規格 §8.1–8.5、§9.1–9.2、§10.1–10.2、§11.9–11.9.3、§14.2、§15、§16.1、§16.2.1、§16.2.2 共 **18 節**有實質需求內容而 037 無對應需求。請確認係「刻意排除」或「分析遺漏」；若為前者，請提供排除依據與承接單位 | 不阻斷本次交付（R-VC3）。惟表 B 之措辭取決於此答覆 |
| DR-VC4 | 規格作者 | 規格 §8.4 之 Cabrio 前提條件引 **VF507**、§14 之 EPB 逾時引 **VF352**，二文件未附 | **條件性** —— DR-VC3 回覆為「應補」時始為必要素材。DR-VC3 回覆前不催 |
| DR-VC5 | 037 作者 | `FROP` 欄之 `Power Management`（16 列）與 `Audio Management`（1 列）共 17 列：其 TC 應由本 feature 產出，或由 FROP 所指之 feature 承接？ | 不阻斷（R-VC3 已裁全取）。答覆到後若需縮限，以 `[OVERRIDE]` 處理，不得回頭默默扣列 |

---

## 七、異常登記（A）

| A | 內容 | 提案處置 |
|---|---|---|
| A-VC1 | 037 `Analysis Report` 第 10–18 欄（`Feasibility` … `Priority`）全 145 列皆為 `\xa0`（U+00A0），非空字串 | 執行層讀取時一律 strip 含 `\xa0`；不視為已填。**不回報上游**（表單樣板行為，非本案缺陷） |
| A-VC2 | 037 封面 `Reviewer：` 為空；`Date：` 為 `2020/09/05`，與修訂履歷（2025-12-26 ~ 2026-04-27）矛盾 | 判為表單樣板殘留。登記留痕；**不得引用該日期為版本依據**。是否回報上游由 Pei 定 |
| A-VC3 | 規格 §16.2 之對應需求 `SWE1-HMI-VC-066` 僅涵蓋「widget 標題為 Cabrio」一句，其下之 16.2.1 / 16.2.2（實際操作行為）無對應需求 | 併入 DR-VC3 一併查詢，**不單獨發 DR** |

---

## 八、`feature.yaml` 草案

> 路徑之 glob 以實際檔名為準（T1 記錄之名），本草案之檔名可能因附件
> 傳遞而經正規化。`paths:` 之基準為本 feature 目錄；`reference:` 之基準為 repo 根。
> 兩節之路徑寫法不同不是筆誤 —— `paths:` 記「檔在哪」（供腳本開檔），
> `reference:` 記「檔是哪一份」（供 `verify_reference_binding.py` 比對）。

```yaml
feature: "Vehicle Category"
test_group: "Vehicle Category"

# R-VC1：FROP 為功能推出計畫之歸屬，非 repo 之 feature 切分。
# 記於此保留該事實；不進入 test_group、不進入任何 TC 欄位。
frop: "Vehicle Settings"

paths:
  workbook: "inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx"   # R-G1 母本
  a03_report: "inputs/FMWIFSM037A03N1LSWE1VehicleCategoryHMIV0*STLA*報告.xlsx"
  sys1_export: "inputs/SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_December_27_2023.xlsx"
  spec_pdf: "inputs/Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_December_27_2023.pdf"
  popup_list: "inputs/Pop Up List HMI R1 (26PI).xlsx"       # PU0091 之值域來源；EPB 之 11 個 PU 見 T6
  settings_list: "inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx"   # 037 引用 24 次（VC-040/041/044 等）

# R-VC5：037 之 `Analysis Report` 分頁存在，intake sniffer 正常命中。
# 本 feature **不需** intake.kind_overrides，亦不需 paths_meta.a03_sheet
# （取預設 "Analysis Report"）。Display 之 R-DM5 偏差在此不成立。

spec_mode: "?"                    # 由執行層依 FO §3 實測後填入（R-VC4 不逕定）
spec_reference_template: null     # R-VC4：spec_reference 為查得（逐字抄 HMI Source ID 欄），非構造

workbook:
  sheet: "?"          # 實測自母本，不得沿用他 feature 之值
  header_row: 9       # 實測覆核
  columns: {}         # T3 之表頭實測結果填入；不得沿用 display / vehicle_setting 之欄位字母

done_region:
  detection: "author"
  author_value: null            # R-VC2：workbook_state = BLANK，本節不生效
  invariant: "content_hash"

write_back:
  author_value: "PeiPYHsu"
  tc_ref_id_value: "NEW"
  fill_test_group_set: true     # R-VC2(a)：BLANK -> FILL

lint:
  design_method_source: "dropdown_sheet"
  popup_ids: []                 # T6 查得後填入（PU0091 及查得之 EPB PU id）
  extra_rules: []

# R-VC3 之機器化：leaf 全集與覆蓋落差之數字宣告於此，使其於每次
# recon.py 執行時被機器比對，而非靠注意力維持。
# PASS 證明的是「該值仍未改變」，不是「該值是對的」——
# 其正確性來自 T4 之重測與上繳包之交叉檢查。
recon_assertions:
  leaf_count: 117
  functional_requirement_count: 145
  distinct_spec_sections: 66
  uncovered_content_sections: 18
```

---

## 九、上繳包要求

`features/vehicle_category/docs/upstream/01_intake_recon.md` 須含：

1. **T0–T9 逐項結果**，含實際指令與其原始輸出（不得只寫「已完成」）
2. **R-VC1 ~ R-VC5 之逐條抄錄核對結果**（抄入位置 + 逐條字面一致確認）
3. **T4 之比對表**：本包 §三、§四之每個數字 vs repo 內實測值，逐項標 `=` 或 `≠`
4. **素材台帳**：實際檔名 + 絕對路徑 + SHA256（搬入前 / 搬入後）+ mtime
5. **未結 DR 清單**（DR-VC1 ~ DR-VC5 全數未結）
6. **A-VC1 ~ A-VC3 之登記位置**
7. **量測條件揭露**（R-G8）：T4 / T5 / T6 各項所用之方法、工具與偽陽性風險

---

## 十、事後附記（2026-08-25 落檔時新增，非原文）

> 本節記錄 §一–§九 定稿之後、本包落檔之前已發生之事，使執行層不必
> 重跑已完成之項，亦不必猜測其狀態。**本節不修改上述任何條文。**

### 10.1 T0 已完成，走「甲」路

`new_feature.py` 拒絕含空格之 feature 名（A-TM04，狀態 PENDING）。
已裁走**甲**：傳 `"Vehicle_Category"`，產出 `features/vehicle_category/`。
`features/vehicle_category/` 骨架已存在，全目錄 untracked。

**T0 之「若非 `vehicle_category` 即停」條件已滿足**（目錄名正確），
不需重跑。

### 10.2 T0b 已完成 —— 字串更正

執行層已完成三組替換並附 diff：

| 組 | 內容 |
|---|---|
| (1) | `Vehicle_Category` → `Vehicle Category`：`RUNBOOK.md` 1,5／`PLAYBOOK.md` 1,128,129,135／`DECISIONS.md` 1；另及 `RULINGS.md` 1,4／`DATA_REQUESTS.md` 1／`ANOMALIES.md` 1（標題列，T7/T8/抄錄 覆寫時自然吸收） |
| (2) | `VE` → `VC`：`PLAYBOOK.md:97`／`ANOMALIES.md:4,14` |
| (3) | profile 名 CamelCase：`FW036_R1L_Vehicle_Category_Profile.md` → `FW036_R1L_VehicleCategory_Profile.md`，於 `RUNBOOK.md:22` 與 `PLAYBOOK.md:65` |

**驗證**：`grep -rn "Vehicle_Category" --include="*.md"` 與
`grep -rn "A-VE\|R-VE\|DR-VE"` 兩項命中數皆 **0**。

`feature.yaml:1,5,6` 之 `Vehicle_Category` 依裁定排除於 (1) 之外，未動 ——
**T9 填寫時須寫回 `feature: "Vehicle Category"` / `test_group: "Vehicle Category"`**
（R-VC1 之身分宣告值，含空格）。

### 10.3 執行層順帶回報之既有缺陷（只回報，本包不處置）

`features/vehicle_setting/PLAYBOOK.md:65` 寫
`FW036_R1L_Vehicle Setting_Profile.md`、
`features/power_moding/PLAYBOOK.md:65` 寫
`FW036_R1L_Power_Moding_Profile.md` —— **兩者於
`docs/runtime/profiles/` 皆不存在**（磁碟上為
`FW036_R1L_VehicleSetting_Profile.md`、
`FW036_R1L_PowerModing_Profile.md`）。

屬既有 feature 之殘留缺陷，**不在本包範圍，不代改**。是否處置由 Pei 定。

### 10.4 A-VC4 —— 於 T8 一併登入

```
A-VC4（new_feature.py 之 abbr 推導無法產生規定之前綴）

`scripts/new_feature.py` 以 `abbr = feature[:2].upper()` 推導標記前綴，
對 `Vehicle_Category` 產出 `VE`，而 R-VC1 規定之前綴為 `VC`。
骨架所生之 `RUNBOOK.md` / `DECISIONS.md` / `PLAYBOOK.md` / `ANOMALIES.md`
因此帶錯誤前綴，須以 T0b 之事後字串更正處理。

提案處置：與 A-TM04（`new_feature.py` 拒絕空格而非 slugify，狀態
PENDING / Tier 2）同批處理 —— 兩者同源，皆為 `new_feature.py` 之
命名推導不足。

**本輪不實作、不併案，僅登記。** 腳本之修改屬 Tier 2，
且本包 §五明文「不得預先改腳本」。
```

### 10.5 尚未啟動者

T1–T9 全部未啟動。`features/vehicle_category/docs/` 除本檔外為空；
`inputs/`、`data/`、`generated/`、`batches/` 皆空；
`DATA_REQUESTS.md`、`ANOMALIES.md` 為骨架樣板，未登入任何條目。

**T1 所需之三份素材尚未置入 `_intake/Vehicle_Category/`** ——
其來源為 Pei（檔案搬動屬 Pei）。素材若尚未落於本機，T1 起之全部
任務均無法啟動，須先向 Pei 取得三份檔案之實際路徑。
