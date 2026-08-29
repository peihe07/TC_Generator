# SOURCE_COLUMNS — SW Update 素材欄位全覽（R-SU26）

**R-SU26(a)**：任一來源檔於首次使用前，須產出欄位全覽 ——
欄序、標頭原文、非空列數、值之型態摘要。
**R-SU26(b)**：逐欄標記 `已用`／`不用（理由）`／`未定`；
**`未定` 不得留存跨輪**，下一輪須裁為前二者之一。
**R-SU26(d)**：**掃描寫得再全，掃的範圍是自己選的。**
「掃了但沒命中」與「根本沒掃到那一欄」須可分辨 —— 本表即其分辨之依據。

> ⚠ **本檔為人手維護之台帳，非 `recon.py` 之產物。**
> `RECON.md` 檔首載明其由 `recon.py` 生成，**故不於該檔手改**
> （手改將於下次重生時失去，且違其生成物之語意）。
> `framework.md` 之射程為三層框架，非素材欄位，故亦不載本表。

---

## 用途統計（2026-08-29，**下放包 30 §五裁定後**）

| 素材 | 欄數 | 已用 | 不用 | **未定** |
|---|---:|---:|---:|---:|
| 037 `AnalysisReport_FULL` | 18 | **8** | **10** | **0** |
| SYS1 `Basic Report` | 7 | **3** | **4** | **0** |
| 036 母本 TC 分頁（非空標頭） | 33 | **17** | **16** | **0** |
| **`Error_Code_List.xlsx`**（分頁，非欄） | **9** | **1** | **8** | **0** |
| **合計** | **67** | **29** | **38** | **0** |

> ### ✅ **未定仍為 0** —— `Error_Code_List.xlsx` 九分頁**一輪內裁畢**
>
> 其於下放包 29 入案（陳報）、下放包 30 §五裁定，**未跨輪**，
> R-SU26(b) 全程未被觸犯。欄位全覽見上繳包 27 §T42b。

### `Error_Code_List.xlsx` 九分頁之裁定（下放包 30 §五）

| 分頁 | 裁定 | 理由 |
|---|---|---|
| `Error Code List`（80 碼） | **已用** | **R-SU35** —— 負向路徑之觀測面來源；台帳為 `ERROR_CODES.md` |
| `Model Code`（44 列） | **不用** | 車型代碼↔車型名之對照，與 TC 之驗證內容無供給關係 |
| `Issue Mapping Version`（2 列） | **不用** | 內容為 SharePoint 連結字串，**素材不在本地、不可及**；**不得據以推定其內容** |
| `ProvideSW_final`／`Flash Status`／`Flash Record`／`MD_IMAGE`／`R1L_Need_Machine`／`PROD_Parameter_Compare` | **不用**（6 頁） | 台架作業與版本發佈之記錄（欄為 `Machine Label`／`FTP Image Path`／`Done Date` 等作業欄），非需求或驗證面之定義 |

> ### ⚠ 一項可用之**附帶事實**（不改上表）
>
> `Flash Status` 之 `Error Code` 欄**實填** `262147`／`336643`／`393219`
> （執行層實測，三值皆為 `Error Code List` 之在案碼）——
> **證明該錯誤碼確於實機作業中被觀測到並被記錄**。
>
> 此為 **DR-SU2 v2(a)（顯示途徑）之一條線索**，
> **但該分頁未載「在哪裡讀到」** —— 它記的是結果，不是觀測手段。
> **故不解該 DR。線索與答案不得混同。**

> ### ✅ **未定欄自此為 0** —— R-SU26(b) 之要求全案履行完畢
>
> 沿革：21 §三立 R-SU26(b)（`未定` 不得跨輪留存）→ 9 欄 → 5 欄（R-SU28 v2）
> → 1 欄（R-SU28 v3，037 歸零）→ **0 欄（下放包 26 §2.3）**。

### 下放包 26 §2.3 之清帳（**五欄逐欄裁定**）

| 欄 | 裁定 | 依據 |
|---|---|---|
| 036 `C` | **不用（留空）** | §2.1 —— **留空為裁定，不是遺漏**（理由逐字見下） |
| 036 `E` | **不用** | §2.2 —— 測試管理端 |
| SYS1 欄 4 `SYSRE_HMI_Source ID` | **改標「已用」** | §2.3 —— 其為 R-SU4(b) 之錨 token 來源，**一直在用**，前輪標「未定」為分析層之誤 |
| SYS1 欄 0 `ID`、欄 6 `_polarion` | **不用** | §2.3 —— 其唯一用途為 036 `C` 欄之鏈路，而該鏈路於本 feature 不成立 |

#### 036 `C` 欄「留空」之理由（**R-SU28(c) 令逐字記入台帳**）

本 feature 之 037 為 **18 欄舊版面、無 `HMI Source ID` 欄**，
鏈路之**第一環不存在**；替代鍵三欄交集皆 **0** 且形態不同族。

**`vehicle_category` 之作法不可移植** —— 其可行係因其 037 版面較新
（20 欄 rev D），**非因其方法較好**。

**留空為裁定，不是遺漏。**

> ### ✅ **Pei 確認不需填（2026-08-28，下放包 29 §1.1）**
>
> 本欄之依據**由「無取值路徑」升級為「不需填」** ——
> 前者是我方取不到，後者是它本來就不必有值。
>
> **「日後要填須新開 DR」之但書撤銷** —— 不需填即無日後之填。
> 原但書之內容（須向上游索 037 ↔ Polarion 對照）**保留為歷史**，
> 不再是本欄之待辦。

**分析層不得以任何推定值填入**（037 之 `Source Requirement ID` 形態與
Polarion `NRL-` 不同族，強行對應即造值）—— 本句**維持有效**，
其射程為「若有人日後想填」，與是否需填無關。

#### 036 `E` 欄「不用」之理由

**15 本簿 2167 列全空**、**`E` 欄於母本無標準 DV 亦無 x14 DV**／無條件式格式；
其語意為 TestRail 之測試管理端 id，**填寫者非 TC 產出端**
（同 `AB`–`AG` 之判準，且有 2167 列之實測佐證）。

### 〔歷史〕未定 5 欄之角色陳報（T37c；**陳報事實，不裁定** —— 已由上表裁畢）

| 來源 | 欄 | 值之形態（實測） | 由誰填／何時填 | 本 feature 是否需要 |
|---|---|---|---|---|
| **036** | `C` `Requirement or Design ID (Polarion)` | 母本 BLANK。**他 feature 實測：35 本中僅 `vehicle_category` 一本有填**（126 列全填，unique 66），值形如 `NRL-171043` | 產出端（TC 撰寫時）；其值須有來源 | **未定** —— 其值之來源見下 |
| **036** | `E` `Test Case ID (TestRail)` | 母本 BLANK。**35 本實測全空** | TestRail 匯入後回填，屬**測試管理端** | 疑不需（產出階段） |
| **SYS1** | 0 `ID` | `NRL-168414` … （unique 120） | 上游 Polarion 匯出 | —— |
| **SYS1** | 4 `SYSRE_HMI_Source ID` | `SYS1_HMI_..._1`／`_1.1`（unique 120） | 上游 Polarion 匯出 | —— |
| **SYS1** | 6 `_polarion` | `NR1L/NRL-168414`（unique 120） | 上游 Polarion 匯出 | —— |

**⚠ 五欄中有三欄是同一件事**（T37c 之發現）：

036 之 `C` 欄標頭為 **`Requirement or Design ID (Polarion)`**，
而 `vehicle_category` 於該欄填 **`NRL-171043`** ——
其形態與 **SYS1 欄 0 `ID`（`NRL-168414`）**、
**欄 6 `_polarion`（`NR1L/NRL-168414`）** 同源。

即：**SYS1 之三個識別碼欄，正是 036 `C` 欄所要之值的來源。**
五個未定欄實為**一組**（一個消費端 + 三個供給端 + 一個獨立的 `E`）。

**本 feature 之特殊處（陳報，不裁）**：R-SU11 已裁
「framework Layer 3 主軸為 CFTS_57；SYS1 不作章對章橋接，其接點為 HMI 87 列」。
故 sw_update 之 037 列是否有對應之 Polarion id、
以及該對應是否經 SYS1 之 120 列可得，**未查**。
**`C` 欄能否填、該不該填，取決於該對應之存在與否，屬分析層之裁定。**

> ### ⚠ **「無 DV」一語之射程**（T49d，下放包 36 §四）
>
> 本檔各處之「無 DV」**皆為欄範圍內之陳述**（`C`／`E`／`S` 三欄確實不在
> 母本任一 DV 範圍內），**逐項覆核為真，非誤**。
>
> **惟其易被讀成全簿之陳述，而全簿之事實是**：
> **標準 `<dataValidation>` 有 4 處；x14 DV 有 1 處 —— `R10:R1411`。**
> 只掃 `<dataValidation>` 元素**掃不到後者**，而 `R` 正是下放包 33
> 填入清單外之值的那一欄。
>
> **全簿之 DV 盤點與各欄值域全文見 `CONTROLLED_VOCAB.md`。**
> 本檔管「有哪些欄」，該檔管「該欄能填什麼」（R-SU40(e)）。

## 已查・不用之來源（**查過而無內容者，須留跡**）

**R-SU26(d)**：「掃了但沒命中」與「根本沒掃到」須可分辨。
下列三源經 Pei 指示查證，**其命中為 0** —— 該 0 是結論，不是遺漏。

| 來源 | 規模 | FOTA／OTA／SW-update 觀測定義 | 裁定 |
|---|---:|---:|---|
| `forms/DTCs Matrix Core List Rev. 1.6.xlsx` | 7 分頁／254 筆 DTC | **0**（Lead CFTS 無 CFTS057） | **已查・不用** |
| `CFTS_004 General Diagnostic Requirements`（Jun 2026）+ SYSAD | 554 物件／168 DID／112 routine | **0**（`FOTA` 僅見於 SYSAD 縮寫表；`OTA` 僅 SXM 換包 NRC） | **已查・不用** |
| `SWE1_Diagnostics_V1.xlsx`（037 A03） | 395 需求列 | **0**（唯一命中為 buzzer 列之偽陽性） | **已查・不用** |

**診斷側之窮舉至此完畢**（PLAYBOOK (26)：否定式裁定之依據一律是窮舉）。

**執行層之覆核範圍（T42d，須明記）**：第一源在 `forms/` 內，
已以 `FOTA|OTA|CFTS057|software update|SW update` 正則掃全簿全頁，**0 命中**，主張成立。
**後二源不在 repo 內**（素材由 Pei 上傳至分析層側），**此側無法覆核** ——
其為分析層親測之陳報，非執行層實測。

---

---

## 037 `AnalysisReport_FULL`（18 欄）

來源：`AnalysisReport_FULL`，表頭列 7、資料列 8 起，全 **383** 資料列；驗證母體 **311** 列。

| 欄 | 標頭原文 | 非空（383） | 非空（311 母體） | 值型態摘要 | 用途 |
|---:|---|---:|---:|---|---|
| 0 | `SWE-Requirement ID` | 383 | 311 | 自由文字，unique 383，長度中位 13 | **已用** —— `req_id`／全案之列 id（R-SU3） |
| 1 | `Source Requirement ID` | 383 | 311 | 自由文字，unique 374，長度中位 15 | **不用** —— R-SU5 v2：三形態並存，該欄不取為 spec_reference |
| 2 | `Requirement Title` | 382 | 311 | 自由文字，unique 372，長度中位 47 | **已用** —— Layer 2 切分之材料（T28a／T28b）；TC 不 verbatim 抄 |
| 3 | `Requirement Description` | 382 | 311 | 自由文字，unique 376，長度中位 286 | **已用** —— 路徑 A 之查詢側（R-SU12）、TC `test_item` 上半之 verbatim 來源 |
| 4 | `Release Version` | 319 | 311 | 枚舉 `1.0.0`／`1.00.0` | **不用** —— **R-SU28(a)**：值域為二（`1.0.0`／`1.00.0`）且其差為寫法之別，無鑑別力 |
| 5 | `Categorization` | 382 | 311 | 枚舉 `Functional Requirement`／`Heading`／`Information`／`Non Functional Re | **已用** —— in-scope 判定（FR／NFR／Heading，R-SU3） |
| 6 | `Sub Categorization` | 310 | 310 | 枚舉 `HMI`／`Service` | **已用** —— HMI／Service 之分面（T28c、原則 3） |
| 7 | `Feasibility` | 311 | 311 | 枚舉 `Yes` | **不用** —— **R-SU28(a)**：常數欄（全 `Yes`），無鑑別力 |
| 8 | `Description/Action for Feasibility` | 311 | 311 | 自由文字，unique 138，長度中位 66 | **不用** —— **R-SU28 v2**：**讀其內容後裁**（非依母欄）。171/311 為同一樣板句；其餘為**實作可行性之理由**（「可用既有 HMI event handling」「可經定義之介面整合安全模組」）。其對象為實作之可行性，非需求之驗證面或可觀測後果，與 TC 之任一欄位無供給關係 |
| 9 | `Impact` | 311 | 311 | 枚舉 `Yes` | **不用** —— **R-SU28(a)**：常數欄（全 `Yes`），無鑑別力 |
| 10 | `Description/Action for Impact` | 311 | 311 | 自由文字，unique 191，長度中位 129 | **不用** —— **R-SU28 v2**：**讀其內容後裁**。118/311 為同一樣板句；其餘為實作面之影響（事件源整合、訊號解碼、UI 渲染同步、排程與逾時監督）。偶提及畫面者係**複述需求本文既有之外部面**，**不提供需求本文以外之觀測資訊** —— 對 R-SU25(c) 之供給為零 |
| 11 | `Risk Factor` | 311 | 311 | 枚舉 `Medium` | **不用** —— **R-SU28(a)**：常數欄（全 `Medium`），無鑑別力 |
| 12 | `Description/Action for Risk Factor` | 311 | 311 | 枚舉 `The requirement is abl` | **不用** —— **R-SU28 v2**：實測 unique = **1**（全 311 列同句），為**常數欄**，依 v1(a) 判準成立。另記：其內容 `The requirement is able to reuse upto 50%` 之語意屬 `Reusable`，填在 `Risk Factor` 之說明欄 —— **037 之欄內容錯置，記錄即止，不立案** |
| 13 | `Reusable` | 311 | 311 | 枚舉 `Fully (100%)`／`High (>= 50%)` | **不用** —— **R-SU28(a)**：SWE.1 之再用性評估，與 TC 之驗證內容無關 |
| 14 | `Description/Action for Reusable` | 311 | 311 | 自由文字，unique 115，長度中位 85 | **不用** —— **R-SU28 v3 一**：**讀其內容後裁**（非依母欄）。191/311 為同一樣板句；其餘為實作面之再用性陳述。其對象為**既有實作之可再用程度**，與需求之驗證面、可觀測後果、TC 之任一欄位皆無供給關係 |
| 15 | `Priority` | 311 | 311 | 枚舉 `High`／`Low`／`Medium` | **已用** —— R-SU22：僅作參考訊號，不作 P 值之唯一依據 |
| 16 | `Verification Criteria` | 310 | 310 | 自由文字，unique 309，長度中位 365 | **已用** —— **R-SU27(a)：R-SU25(c) 外部可觀測後果之候選來源**（本輪起） |
| 17 | `Verification Method` | 311 | 311 | 自由文字，unique 26，長度中位 42 | **已用** —— **R-SU27(b)：測試層級之參考訊號**（本輪起） |


### 〔已結〕`未定` 清單（037）—— R-SU28 v2 之延展，**已到期並裁畢**

| 欄 | 標頭原文 | 非空（311 母體） | unique | 狀態 |
|---:|---|---:|---:|---|
| 14 | `Description/Action for Reusable` | 311 | 115 | **不用**（**R-SU28 v3 一**，延展到期定案；037 未定歸 0） |

抽樣材料見 `docs/upstream/21a_desc_columns_material.md` §欄 14
與 `docs/upstream/22_dr2_batch.md` §2（重列）。

> **延展之記明（R-SU28 v2）**：本次為**一次性延展**，理由為分析層之閱讀順序，
> **非默許跨輪**。**延展須逐次記明，不得累積。**

**欄 8／10／12 已於本輪裁「不用」**（其理由逐欄載於上表，
且皆**讀其內容後**方裁 —— 依 R-SU28(c)：欄之「不用」不得因其母欄之值型態成立）。

### SYS1 export（`Basic Report`，120 資料列，7 欄）

| 欄 | 標頭原文 | 非空 | 值型態摘要 | 用途 |
|---:|---|---:|---|---|
| 0 | `ID` | 120 | 自由文字，unique 120 | **不用** —— **下放包 26 §2.3**：其唯一用途為 036 `C` 欄之鏈路，而該鏈路於本 feature 不成立（第一環 `HMI Source ID` 不存在） |
| 1 | `Space / Document` | 120 | 枚舉 `Requirements / SYS` | **不用** —— **R-SU28 v3 二**：常數欄，依 v1(a) 判準成立，不需讀其內容 |
| 2 | `Outline Number` | 120 | 自由文字，unique 120 | **已用** —— R-SU11：SYS1 之接點為 HMI 87 列；T18b 分群 |
| 3 | `Description` | 120 | 自由文字，unique 118 | **已用** —— T18b／T18d 之比對側 |
| 4 | `SYSRE_HMI_Source ID` | 120 | 自由文字，unique 120 | **已用** —— **下放包 26 §2.3**：R-SU4(b) 之**錨 token 來源，一直在用**；前輪標「未定」為分析層之誤 |
| 5 | `Type` | 120 | 枚舉 `SYSRE_HMI` | **不用** —— **R-SU28 v3 二**：常數欄，依 v1(a) 判準成立，不需讀其內容 |
| 6 | `_polarion` | 120 | 自由文字，unique 120 | **不用** —— **下放包 26 §2.3**：同欄 0，其唯一用途為 036 `C` 欄之鏈路 |

### 036 母本（`Test Case Specification 測試用例規範`，表頭列 9，34 欄）

| 欄 | 標頭原文 | 用途 |
|---|---|---|
| `B` | No.# ／ 序號 | **不用** —— 共用公式之宿主（`t="shared"` 1401 處），賦值即毀 |
| `C` | Requirement or Design ／ ID (Polarion) ／ 設計/需求 ID (Po | **不用（留空）** —— **下放包 26 §2.1**：037 為 18 欄舊版面無 `HMI Source ID`，鏈路第一環不存在；替代鍵三欄交集皆 0。**留空為裁定，不是遺漏**；日後要填須新開 DR，不得以推定值填入 |
| `D` | Requirement or Design ID ／ 需求/設計 ID | **已用** —— `req_id`（`feature.yaml` §workbook.columns） |
| `E` | Test Case ID (TestRail) ／ 測試用例 ID (TestRail) | **不用** —— **下放包 26 §2.2**：15 本簿 2167 列全空、**該欄無標準 DV 亦無 x14 DV**；其語意為 TestRail 之測試管理端 id，填寫者非 TC 產出端 |
| `F` | Test Case ID ／ 測試用例ID | **已用** —— TC ID（R-SU24；`feature.yaml` 未列，實測 `F9`） |
| `G` | Test Group ／ 測試組 | **已用** —— `test_group`（`feature.yaml` §workbook.columns） |
| `H` | Test Set ／ 測試集 | **已用** —— `test_set`（`feature.yaml` §workbook.columns） |
| `I` | Test Item ／ 測試項目 | **已用** —— `test_item`（`feature.yaml` §workbook.columns） |
| `J` | Pre-Conditions ／ 先前條件 | **已用** —— `pre_conditions`（`feature.yaml` §workbook.columns） |
| `K` | Input Test Data ／ 輸入條件 | **已用** —— `input_test_data`（`feature.yaml` §workbook.columns） |
| `L` | Test procedure ／ 測試程序 | **已用** —— `test_procedure`（`feature.yaml` §workbook.columns） |
| `M` | Expected Result ／ 預期結果 | **已用** —— `expected_result`（`feature.yaml` §workbook.columns） |
| `N` | Specification Reference  ／ 規格參考 | **已用** —— `spec_reference`（`feature.yaml` §workbook.columns） |
| `O` | Test Case Reference ID ／ 測項參考ID | **已用** —— `tc_ref_id`（`feature.yaml` §workbook.columns） |
| `P` | Test Case Priority ／ 測試用例優先級別 | **已用** —— `priority`（`feature.yaml` §workbook.columns） |
| `Q` | Estimated Test Time (mins) ／ 預估測試時間 ／ （分鐘） | **已用（工具側）** —— `RECON.md` §Workbook 已解析 `estimated_test_time = Q`；**`feature.yaml` 未列**，寫回是否填未裁 |
| `R` | Test Case Design  ／ Methods ／ 測試用例設計方法 | **已用** —— `design_method`（`feature.yaml` §workbook.columns） |
| `S` | Functional Safety ／ 功能安全 | **已用（欄已映射）** —— `functional_safety`；**該欄不在母本任一 DV 範圍內**（T35c 實測；DV 之全簿盤點見 `CONTROLLED_VOCAB.md`）；他 feature 之交付本 5/6 填 `NA`。本 feature pilot 未填，值域未裁 |
| `T` | HDCC27 ／ Atl-Hi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `U` | DT27 ／ Atl-Hi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `V` | VF(ProMaster)637 ／ Atl-Mi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `W` | Commander (598) ／ Atl-Mi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `X` | Regengade (5210) ／ Atl-Mi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `Y` | Toro(2261) ／ Atl-Mi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `Z` | Fastack (376) ／ Atl-Mi | **不用（留空）** —— **下放包 23 §四**：車型適用旗標，DV `T10:Z1411` = `"0,1"`；他 feature 6/6 一律留空，**沿既有實務**。⚠ 若 Pei 要求填，本裁定失效並須重裁（其值須有來源，不得推定） |
| `AA` | Test Case Author ／ 測試案例作者 | **已用** —— `author`（`feature.yaml` §workbook.columns） |
| `AB` | Test Version ／ 測試版號 | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AC` | Test Vehicle ／ (Bench) ／ 測試車型(Bench) | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AD` | Test Period ／ 測試期間 | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AE` | Tester ／ 測試者 | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AF` | Test Result ／ 測試結果 | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AG` | Defect ID ／ 缺陷ID | **不用（產出階段）** —— **R-SU28 v3 三**：測試結果面，填寫者為**測試執行端**非產出端。**實測佐證**：35 本已掃之簿於本欄**皆空**（T37a） |
| `AH` | Remarks ／ 備註 | **已用** —— `remarks`（`feature.yaml` §workbook.columns） |

### 文字型素材之結構元素（CFTS_57／SYSAD／VF747／HMI PDF）

| 素材 | 已用之結構元素 | 未用之結構元素 |
|---|---|---|
| **CFTS_57**（docx） | heading style 1–4 之 `{7位}` 章節（87）；`[Artifact Type:Subsystem Functional Requirement]` 宣告之需求物件（487）；其後至下一宣告之全文（語料 v2） | **表格**（`<w:tbl>`）、**圖**（drawing）、註腳、`[Artifact Type:…]` 之**其他型別**（Description 137 已用其歸屬，其餘型別未列）、修訂標記 |
| **SYSAD**（docx） | 迄今**僅作 T33c 之全文語形掃描** | 章節結構、介面節、架構圖、**全部表格** |
| **VF747**（docx） | 已綁 `reference.vf747`；**內容未讀** | 全部 |
| **HMI 規格 PDF** | R-SU6 v2：真 PDF、68 頁全文字層；T5' 之 popup id 抽取（52 個） | 頁面版面、圖、**全文之語意內容** |
