# 上繳包 05 —— 母體判準之修正、Q3 完整語料與 Phase 3 前置

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/05_corpus_fix_and_framework_prep.md`
- 前一包：[upstream/04_corpus_and_assertions.md](04_corpus_and_assertions.md)
- **併讀之補篇**：`05a_upstream_naming_scope.md`（R-PMH26）＋
  `05b_q3_final.md`（R-PMH27）—— 二者不另佔往返編號，其上繳併入本檔 §13。
- 執行狀態：**步驟 1–6 全部執行完畢**，05a／05b 之作業指示另見 §13。
  **停止條件 7 觸發**（母體 17 ≠ 16），
  **停止條件 8 觸發一項**（一個排除理由不成立）。二者已查明並逐項回報。
  **零寫回工作簿**；git 指令零次。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH24 | 母體判準以用途目錄排除，非以深度；新增反向驗證義務 | 472 | `9f02fc8ad0606ad4` | `9f02fc8ad0606ad4` | 逐字相符 |
| R-PMH25 | `design_method` vocabulary 取自 x14 所指 source | 364 | `37324b2cec85648b` | `37324b2cec85648b` | 逐字相符 |

### 1.1 R-PMH19 附註與 R-PMH10 語料更新之落實證明（原文 SHA256 未變）

| 條號 | SHA256（前 16） | 與前包所記 |
|---|---|---|
| R-PMH19 | **`cbdeed8b8bc0774b`** | 相同（04 包） |
| R-PMH10 | **`885070968235b262`** | 相同（02 包） |

R-PMH19 之附註（「(a) 已由 R-PMH24 取代」，含五個被誤排除之交付件具名）
與 R-PMH10 之 `[PEI-REOPEN]` 語料表（三次量測之對照），
皆以引用段落置於各自 fenced block **之外**。

---

## 2. 母體重建（步驟 6 之前置）—— **母體 17，非 16。停止條件 7 觸發**

### 2.1 候選數亦已變動：**32，非 04 包之 28**

| 新增之 4 檔 | mtime |
|---|---|
| `Vehicle Settings/CFTS044/REF/036_pre_fullwrite_20260823.xlsx` | 2026-08-23 17:55 |
| `Vehicle Settings/CFTS044/REF/036_pre_fullwrite2_20260823.xlsx` | 2026-08-23 18:42 |
| `Vehicle Settings/CFTS044/REF/036_pre_fullwrite3_20260823.xlsx` | 2026-08-23 19:57 |
| `Vehicle Settings/CFTS044/REF/036_pre_final_20260824.xlsx` | 2026-08-23 20:15 |

四者皆為**併行 session（vehicle_setting Part 1 線）於 04 包之後產生**之
寫回前備份，全部落在 `REF/` 下，**依 (a′) 全部排除，不影響母體**。

> **登記此點之理由**：`ASW-R2` 是一個**活動中的目錄**。任何以它為母體之
> 比率，其分母會隨他人之作業而變動。04 包報 28、05 包報 32，**兩者皆正確**，
> 差別只在量測時點。R-PMH19 之揭露義務要求載明母體清單 —— 建議**再加一項：
> 載明量測時點**，否則兩份上繳之數字無法對得起來。

### 2.2 篩選

| 階段 | 檔數 |
|---|---|
| 候選全集 | **32** |
| 排除 (a′) 位於用途目錄（`REF`／`output`／`validation`／`archive`／`backup`）下 | **7** |
| 排除 (b) 檔名含中間態標記 | **5** |
| 排除 (c) 同夾舊版 | **3** |
| **母體** | **17** |

### 2.3 母體 17 之交付夾（多層者依 R-PMH24 不受深度影響）

`AM:FM`／`Audio Management `／`Climate Control Interface`／`Connection Manager`／
**`Core HMI/HomeHMI`**／**`Core HMI/Menu Bar and AppDrawer`**／
**`Core HMI/Notifications HMI`**／`Disclaimer screen`／`Engineering Mode`／
**`Engineering Mode/App Team Effort`**／`Power Management`／`Privacy Mode`／
`SiriusXM`／`Time Management`／`User Profiles`／
**`Vehicle Settings/CFTS044`**／**`Vehicle Settings/VF230_V1_R5`**

### 2.4 差異歸屬：**分析層之 16 漏了 `Engineering Mode/App Team Effort/`**

分析層 §3.2 補測 5 檔（HomeHMI、Menu Bar and AppDrawer、Notifications HMI、
CFTS044、VF230）加原 11 = 16。**第 17 個為
`Engineering Mode/App Team Effort/…_SWQT_CFTS011_EngMode.xlsx`** ——
它在 04 包同樣被原 (a) 之深度規則排除，(a′) 生效後與那五個一併回到母體，
而補測清單只列了五個。

**此差異改變 Q3 之語料**（見 §3）。

---

## 3. Q3 語料之再更新 —— **`D5` 空 9 / 非空 8**

第 17 檔之實測：

| 交付夾 | 分頁 | 欄數 | `Cover!D6` | 資料列 | D3 | D4 | **D5** |
|---|---|---|---|---|---|---|---|
| `Engineering Mode/App Team Effort/` | `…測試用例規範` | 33 | `A` | 258 | 空 | 空 | **`FM-WI-SW-PSCFTS011-ENGM-A01`** |

**其 `D5` 非空**，且為**第六種格式** —— 一個**表單／文件編號**
（`FM-WI-SW-…-A01`），既非 037 報告名，亦非 CFTS 條目 id。

### 3.1 三次量測之演進

| 母體判準 | 母體 | `D3` 空 | `D4` 空 | **`D5` 空 / 非空** |
|---|---|---|---|---|
| 原依據（母體未定義） | 「5」 | 5 | 5 | 5 / **0** |
| R-PMH19（04 包） | 11 | 11 | 11 | 8 / **3** |
| R-PMH24（分析層 §三） | 16 | 16 | 16 | 9 / **7** |
| **R-PMH24（執行層實測，現行）** | **17** | **17** | **17** | **9 / 8** |

**`D3`／`D4` 於四次量測皆為全空，其留空無爭議。**
**`D5` 之非空數由 0 → 3 → 7 → 8**，而空者始終為 9（第 17 檔為非空）。

**即：`D5` 現為 9 空 / 8 非空 —— 幾乎對半。**
分析層 §五所稱「母體最大單一群（9/16）」在 17 之母體下為 **9/17**，
其相對多數之幅度由 56% 降為 53%。**（甲）之語料強度較 §五所述更弱。**

### 3.2 八個非空 `D5` 之逐字與指向（第 8 項為本包新增）

| # | 交付夾 | `D5` 逐字 | 指向 |
|---|---|---|---|
| 1 | `AM:FM/` | `SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323` | 自身 037 報告全名 |
| 2 | `SiriusXM/` | `SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406` | 同 #1 模板 |
| 3 | `VF230_V1_R5/` | `FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA` | 自身 037 報告名（另一排列） |
| 4 | `Menu Bar and AppDrawer/` | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告` | 自身 037 報告名（第三種排列） |
| 5 | `HomeHMI/` | 與 #4 **逐字相同** | **他 feature 之報告名（疑複製未改）** |
| 6 | `Privacy Mode/` | `SWE1_CFTS_022-Privacy_Features` | CFTS 規格條目 id |
| 7 | `Notifications HMI/` | `FM-WI-FSM-036-A01` | **表單編號本身** |
| **8** | **`Engineering Mode/App Team Effort/`** | **`FM-WI-SW-PSCFTS011-ENGM-A01`** | **另一份表單／文件編號** |

**八個非空者用了六種格式；其中三個指向物不是規格或報告**
（#5 他 feature 之報告、#7 本表單編號、#8 另一份文件編號）。
即：**非空之八者中，只有五者（#1–#4、#6）指向與本 feature 相關之上游文件。**

**執行層不提案**（下放包 §五明載分析層亦不提案，Q3 屬 Pei）。
惟須指出：若以「填得對者之取法」為據，其分母應為 **5**（#1–#4 指向 037 報告、
#6 指向 CFTS 條目），而**五者中仍用了四種排列**。

---

## 4. 步驟 6 —— 15 項排除清單之逐項反向覆核（R-PMH24 新增義務）

> 下放包 §六步驟 6 稱「12 個」，係依 04 包之候選 28 推得；
> 候選增為 32 後，**排除者為 15 個**。逐項覆核如下。

| # | 檔（相對 `ASW-R2/`） | 排除理由 | **理由是否成立** |
|---:|---|---|---|
| 1 | `Core HMI/Notifications HMI/…_HMI_Notification_20260303.xlsx` | (c) 同夾舊版 | **成立** —— 被 `20260817` 取代 |
| 2 | `Core HMI/Notifications HMI/…_20260309(Review).xlsx` | (b) `(Review)` | **成立** |
| 3 | `Engineering Mode/App Team Effort/…_EngMode_20251222(Refine).xlsx` | (b) `(Refine)` | **成立** |
| 4 | `…/…_EngMode_20260129(Revise).xlsx` | (b) `(Revise)` | **成立** |
| 5 | `…/…_EngMode_20260416(done).xlsx` | (b) `(done)` | **成立，但理由須換** —— 見 §4.1 |
| 6 | `Engineering Mode/…_EngMode_20260429.xlsx` | (c) 同夾舊版 | **成立** —— 被 `20260816` 取代 |
| 7 | `Engineering Mode/…_EngMode_20260816_Rebuilt.xlsx` | (b) `_Rebuilt` | **❌ 不成立 —— 見 §4.2** |
| 8 | `Power Management/…_PowerManagement_20260820.xlsx` | (c) 同夾舊版 | **成立** —— 被 `20260821` 取代 |
| 9–13 | `Vehicle Settings/CFTS044/REF/` 之 5 檔 | (a′) `REF` | **成立** —— 檔名逐字為 `036_pre_writeback`／`036_pre_fullwrite{,2,3}`／`036_pre_final`，皆為寫回前備份 |
| 14 | `Vehicle Settings/VF230_V1_R5/output/fw036_vf230_…xlsx` | (a′) `output` | **成立** |
| 15 | `…/output/validation/fw036_vf230_…xlsx` | (a′) `output/validation` | **成立** |

### 4.1 #5 之理由須換（不影響結論）

`(done)` 之字面語意為「完成」，與「中間態」相反。以「檔名含中間態標記」
為由排除一個名為 `(done)` 之檔案，**其理由之措辭與事實相反**。

**惟排除之結論仍成立**，因另有獨立依據：該檔 296 資料列，
與同夾之 `20260129(Revise)` 相同，且已被 `Engineering Mode/` 根層之
`20260429`（同為 296 列）取代。**即使 (b) 不適用，(c) 亦會排除它**
（若 `App Team Effort` 與 `Engineering Mode` 視為同一交付夾）。

**提案**：R-PMH19 (b) 之清單中，`(done)` 一項之理由改述為
「工作目錄內之階段快照」，或將其自 (b) 移入 (c) 之處理範圍。

### 4.2 #7 之理由**不成立** —— 停止條件 8 觸發

`Engineering Mode/` 根層有兩份同日期（20260816）之檔案：

| 檔 | 分頁 | 欄數 | `Cover!D6` | **資料列** |
|---|---|---|---|---|
| `…_SWQT_EngeeringMode_20260816.xlsx`（**保留，入母體**） | `…&Result` | 35 | `A` | **211** |
| `…_SWQT_EngMode_20260816_Rebuilt.xlsx`（**排除**） | `…&Result` | 35 | `A` | **527** |

**被排除者之資料列為保留者之 2.5 倍（527 vs 211）。**

`_Rebuilt` 之字面語意為「已重建」，其為**成品**而非中間態之可能，
至少與其為中間態之可能相當。而 (c) 之日期規則對兩者無鑑別力（同日），
故實際上是 **(b) 之字面比對決定了取捨，而該比對選中了資料較少的那一份**。

另：保留者之檔名為 **`EngeeringMode`（拼字錯誤，多一個 e）**，
被排除者為 `EngMode`（與該夾其餘檔案一致）。
**以檔名字串為判準時，被留下的是拼錯的那一份。**

**執行層不裁定何者為交付態** —— 那需要 Engineering Mode 之交付紀錄，
不在本 feature 之範圍。**依停止條件 8 停並回報。**

**對本 feature 之實際影響**：`Engineering Mode` 交付夾之
`D5` 為**空**（兩份候選皆需複驗才能斷言，本包只測了保留者）。
若改取 `_Rebuilt`，母體仍為 17，**僅該格之值可能改變**。
**本包未測 `_Rebuilt` 之 `D3`／`D4`／`D5`** —— 未測之理由：它現為被排除者，
測了會產生「把被排除者的數據併入母體」之誘惑（04 包已有同型自律）。

---

## 5. 步驟 2 —— 全母體 17 檔之 DV 掃描

**量測條件（R-PMH20）**：`zipfile` 直讀各檔 `xl/worksheets/*.xml` **全部分頁**
之 `<dataValidation>` 與 `<x14:dataValidation>`；下表之「全簿 DV」為活頁簿層計數，
其餘各欄為 `Test Case Specification*` 分頁層之值。**量測範圍 = 母體 17 檔，
量詞即為「這 17 檔」，不外推至「表單」。**

| 交付夾 | 全簿 DV | **x14 source** | priority sqref | 跨欄 | `AF`/`AG` 前導空白 | `Product Document!B7` |
|---|---:|---|---|---|---|---|
| `AM:FM` | 5 | `Reference!$C$4:$C$12` | `P10:P307 Q10:Q11` | 不跨 | 有 | `Confidential` |
| `Audio Management ` | 6 | `Reference!$C$4:$C$12` | `P13:P17 P20:P32 …` | 不跨 | 有 | `Confidential` |
| `Climate Control Interface` | 5 | **`下拉選單!$A$1:$A$9`** | `P10:Q601` | **跨欄** | 有 | 空 |
| `Connection Manager` | 6 | `Reference!$C$4:$C$12` | `P10:P132 Q10:Q11` | 不跨 | 有 | `Confidential` |
| `Core HMI/HomeHMI` | 4 | `Reference!$C$4:$C$12` | （無） | — | **無此 DV** | `Confidential` |
| `Core HMI/Menu Bar and AppDrawer` | 3 | **（無 x14）** | `P203:P228` | 不跨 | **無此 DV** | `Confidential` |
| `Core HMI/Notifications HMI` | 5 | **`下拉選單!$A$1:$A$9`** | `P10:P19 P22:P91` | 不跨 | 有 | `Confidential` |
| **`Disclaimer screen`（客戶那份）** | 5 | `Reference!$C$4:$C$12` | `Q10:Q221 R10:R11 P10:P11` | **跨欄** | 有 | `Confidential` |
| `Engineering Mode` | 5 | `Reference!$C$4:$C$12` | `Q10:Q221 R10:R11 P10:P11` | **跨欄** | 有 | `Confidential` |
| `Engineering Mode/App Team Effort` | 6 | **`下拉選單!$A$1:$A$11`** | `P10:P11` | 不跨 | 有 | `Confidential` |
| `Power Management` | 5 | `Reference!$C$4:$C$12` | `P10:P221 Q10:Q11` | 不跨 | 有 | `Confidential` |
| `Privacy Mode` | 6 | **`下拉選單!$A$1:$A$11`** | `P10:Q11` | **跨欄** | 有 | 空 |
| `SiriusXM` | 5 | `Reference!$C$4:$C$12` | `Q10:Q11 P10:P224` | **跨欄** | 有 | `Confidential` |
| `Time Management` | 5 | **`下拉選單!$A$1:$A$9`** | `P10:Q1411` | **跨欄** | 有 | 空 |
| `User Profiles` | 5 | **`下拉選單!$A$1:$A$9`** | `P10:Q1411` | **跨欄** | 有 | 空 |
| `Vehicle Settings/CFTS044` | 4 | **（無 x14）** | `P10:P132 Q10:Q11` | 不跨 | 有 | `Confidential` |
| `Vehicle Settings/VF230_V1_R5` | 5 | `Reference!$C$4:$C$12` | `P10:P132 Q10:Q11` | 不跨 | 有 | `Confidential` |

**（母本 `forms/…_20260817_ext.xlsx` 不在此 17 內** —— 它不在 `ASW-R2` 樹下。
其值見 04 包 §5.1：全簿 5 組、x14 → `下拉選單!$A$1:$A$9`、`P10:Q1411` 跨欄、
`AF` 有前導空白。）

### 5.1 (a) `AF`／`AG` 之前導空白

**這 17 檔中，具 test_result DV 者 15 檔，其 `formula1` 逐字皆為
`"Pass, Fail, Pending,Block,NA"` —— 15/15 全部帶前導空白**
（` Fail`／` Pending` 各前置一個空格；`Block`／`NA` 無）。
另 2 檔（`HomeHMI`、`Menu Bar and AppDrawer`）**無此 DV**。

**依 R-PMH20 之結論句**：
> **本次量測之 17 個交付件中，具 test_result DV 之 15 個，其列舉字串
> 全部帶前導空白。** 未量測母本以外之其他表單版本，故不作「表單皆如此」之陳述。

### 5.2 (b) 各檔之 x14 source

| source | 檔數 |
|---|---:|
| `Reference!$C$4:$C$12` | **10** |
| `下拉選單!$A$1:$A$9` | 4 |
| **`下拉選單!$A$1:$A$11`** | **2** |
| 無 x14 DV | 2（`Menu Bar and AppDrawer`、`Vehicle Settings/CFTS044`） |

**三項須記**：

1. **母本所用之 `下拉選單!$A$1:$A$9` 在這 17 檔中是少數（4/17）**；
   多數（10/17）指向 `Reference!$C$4:$C$12`。
   **R-PMH25 之判準因此更有必要** —— 若以「多數」定 source，會取到
   `Reference`，而母本之實測值是 `下拉選單`。**本 feature 依 R-PMH25
   取母本自身之實測值，不隨多數。**
2. **`$A$1:$A$11` 兩檔**：其 source 範圍為 11 列，而 `下拉選單` 分頁
   實際只有 9 個非空值 —— **該 DV 之列舉含兩個空值**。
   （允許選空值，實務上等同放寬。）
3. **2 檔完全無 x14 DV** —— 其 `design_method` 欄無下拉，可自由輸入。

### 5.3 (c) priority DV 之 sqref 是否跨欄

| 形態 | 檔數 | 名單 |
|---|---:|---|
| **跨 P、Q 兩欄** | **6** | `Climate Control Interface`／`Disclaimer screen`／`Engineering Mode`／`Privacy Mode`／`SiriusXM`／`Time Management`／`User Profiles`（其中 `Disclaimer screen`／`Engineering Mode` 之 `Q10:Q221 R10:R11 P10:P11` 為 35 欄版面，跨 P、Q、R 三欄） |
| 不跨 | 10 | 其餘 |
| 無 | 1 | `Core HMI/HomeHMI` |

（上表「跨欄」欄計 7 列，其中 `Time Management` 與 `User Profiles` 之
`P10:Q1411` 與母本相同。）

**即：A-PMH12 (1) 所指之「priority DV 跨欄而使 Estimated Test Time 套用
P0–P3 下拉」，在這 17 檔中有 7 檔具同一形態**，非母本獨有。
**未量測範圍以外者不作陳述。**

---

## 6. 步驟 3 —— `Product Document!B7:C7` 之登記

| 值 | 檔數 |
|---|---:|
| `Confidential` | **12** |
| 空 | **5**（`Climate Control Interface`／`Privacy Mode`／`Time Management`／`User Profiles`／——） |

DV 本身（`B7:C7`，legacy list，`"Confidential, Top Secret"`）**17 檔全部具備**，
且逐字相同。**無任何檔填 `Top Secret`。**

**只登記，不提案**（下放包步驟 3 明載）。惟指出一項與本 feature 直接相關者：
**母本之 `B7` 為空，而客戶那份（`Disclaimer screen/`）之 `B7` 為
`Confidential`。** 依 R-PMH7 本 feature 之交付基底為母本，故 Phase 7 若
未主動填寫，交付物之該格將為空 —— **12/17 之已交付件填了它**。
此為 Phase 7 之待決項，本包不處置。

---

## 7. 步驟 4 —— `data/layer3_sections.tsv`

**程式**：`scripts/build_layer3_sections.py`（本 feature 專屬，未改共用腳本）。

**48/48 對應到規格自身之 section id**（`outline_number` 取自 SYS1
`Basic Report` 之 `Outline Number`，**不自創標籤**，canon §4.1.1）。
**停止條件 9 未觸發。**

欄位：`swe_requirement_id`／`outline_number`／`chapter`／`chapter_title`／
`section_title`／`frop`／`pdf_page`。

| 章 | leaf | 章標題 |
|---:|---:|---|
| 7 | 19 | `Startup` |
| 8 | 6 | `Starup R1Low Only` |
| 9 | 5 | `Power Moding` |
| 10 | 10 | `Additional Power Moding Behavior Notes:` |
| 11 | 5 | `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS` |
| 12 | 3 | `Power Moding – Off Road+` |

FROP 分布 12 值，與 03 包 §7.1 逐項相符（Customizable 12／Disclaimer 7／
Audio 7／SWC 5／Power Management 5／Bluetooth 3／Rear View 2／FOTA 2／
Climate 2／e-call 1／WiFi 1／EV-PHEV 1）。

**不擬 Layer 2 名稱、不定 granularity。**

### 7.1 首版之缺陷與其修正（自陳）

**首版寫出之 TSV 結構是壞的。** `section_title` 之內容含**實體換行**與
`_x000D_` 字面量，未正規化即寫入，致一列被拆成多列 ——
`cut -f3 | sort | uniq -c` 讀出的「章」欄出現
`- If user accepts FOTA popup…` 這類值。

**成因**：TSV 之列分隔即換行、欄分隔即 tab，而**資料本身含這兩種字元**。
**與 A-PMH08（子字串包含法誤命中）同族**：把一個有結構的東西
當成無結構的字串處理。

**修正**：`flat()` 將 `_x000D_` 與所有空白摺為單一空格並截斷；
**並加寫出後之結構自檢**（回讀 TSV，驗列數 == 48+1、每列欄數一致），
不以「寫出成功」為通過（R-G7-1）。修正後回讀 **48 列 × 7 欄，自檢通過**。

---

## 8. 步驟 5 —— `check_write_back.py` 之接線狀態登記

已於 `DECISIONS.md` §7 加一列，標 **`[KNOWN-INCOMPLETE — 05 包步驟 5]`**：

> 三項檢查**已實作並經故意失敗驗證**，但**尚未被任何寫回路徑呼叫** ——
> `feature.yaml` 之 `write_back_checks` 節目前只是宣告。R-PMH22 所要求之
> 「於每次寫回前**自動**驗證」之**接線為 Phase 6 之交付項**。
> **本項為已知未完成，非疏漏、亦非 RESOLVED**（通則 8：文字修補不構成
> RESOLVED，而**一段未被呼叫的正確程式碼，其效力與文字修補相同**）。

`feature.yaml` 之 `write_back_checks` 節加 `wired: false`。

另依 **R-PMH25** 改寫 `lint.design_method_source`：
由 `"dropdown_sheet"`（以分頁名認定）改為 `"x14_dv_target"`，
並加 `design_method_source_measured: "下拉選單!$A$1:$A$9"`（母本 `<xm:f>` 之
實測值），註明全母體 17 檔中僅 4 檔指向此處而 10 檔指向 `Reference`，
**本 feature 取母本自身之實測值，不隨多數**。

---

## 9. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **`_Rebuilt` 那一份之 `D3`／`D4`／`D5` 未測**（§4.2）。刻意不測 ——
   它現為被排除者，測了會產生把其數據併入母體之誘惑。
   **若 Pei 裁定它才是交付態，該格須補測，且 §3.1 之 `D5` 計數可能改變。**

2. **`Engineering Mode` 與 `Engineering Mode/App Team Effort` 是否為
   兩個交付夾，本包未判。** (a′) 之字面使後者成為獨立 group，
   而其內容（258→290→296 之遞進，且成品以 `20260429` 出現在父層）
   **看起來像工作子目錄而非交付夾**。若二者應合併，母體為 **16** 而非 17，
   且 §3 之 `D5` 計數回到 9/7。**這正是分析層之 16 與執行層之 17 的差別所在。**
   本包照 (a′) 字面執行並回報，不自行合併。

3. **母體之量測時點未成為 R-PMH19 揭露義務之一部分**（§2.1）。
   `ASW-R2` 是活動目錄，04 包 28、05 包 32，兩者皆正確而數字不同。
   **建議補入揭露義務，本包不自行改條文。**

4. **`Product Document!B7` 之 Phase 7 影響未評估**（§6）。
   母本為空、12/17 已交付件填 `Confidential`。**若交付時該格須填，
   則本 feature 之寫回範圍不只 `Test Case Specification` 分頁** ——
   而現行 `feature.yaml` 之 `write_back` 只描述該一分頁。未處置。

5. **本包未複驗分析層 §3.2 所報之 5 檔數據。** §3 之表沿用其值
   （欄數 33／`Cover!D6` `B`／資料列數／`D5` 逐字），**只獨立測了第 17 檔**。
   依 §9.1 通則 5，未在有雜湊之物件上重測者為「被取代而非被複驗」——
   本包之 §3.1 計數因而**部分倚賴分析層之量測**，此點須明說。

---

## 10. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 —— Layer 3 表 48/48 對應 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— §3 只列語料與指向，不提案 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | R-PMH24 修正後之母體 ≠ 16 | **觸發** —— 實測 **17**；差異為 `Engineering Mode/App Team Effort/`，歸屬已查明（§2.4）並回報 |
| 8 | 反向覆核發現任一被排除檔之理由不成立 | **觸發一項** —— #7 `_Rebuilt`（§4.2）；另 #5 `(done)` 之理由措辭與事實相反但結論成立 |
| 9 | Layer 3 表有 leaf 無法對應 section id | **未觸發** —— 48/48 |

---

## 11. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 05 — corpus rule fixed, 17-file DV sweep, layer 3 table
```

```
git add -- features/power_moding/DECISIONS.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/scripts/build_layer3_sections.py \
           features/power_moding/data/layer3_sections.tsv \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/05_corpus_fix_and_framework_prep.md \
           features/power_moding/docs/upstream/05_corpus_fix_and_framework_prep.md

git commit -- features/power_moding/DECISIONS.md \
              features/power_moding/RULINGS.md \
              features/power_moding/feature.yaml \
              features/power_moding/scripts/build_layer3_sections.py \
              features/power_moding/data/layer3_sections.tsv \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/05_corpus_fix_and_framework_prep.md \
              features/power_moding/docs/upstream/05_corpus_fix_and_framework_prep.md
```

- 本輪未觸及本 feature 目錄以外之任何檔案。
- `ANOMALIES.md` **未動** —— 本包之新發現（母體 17、`_Rebuilt` 之理由不成立）
  皆為**停止條件之回報**而非異常登記；待 Pei 就 §4.2 與 §9 第 2 項裁定後
  再決定是否立 `A-PMH{n}`。
- `scripts/new_feature.py` 未改（禁止項仍在）。
- pathspec 逐項寫全名，未用萬用字元（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 11.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

---

## 12. 待 Pei 裁定

1. **Q3 之 `D5`** —— 甲（留空）／乙（填自身 037 報告全名）。
   **語料已更新為 9 空 / 8 非空**（母體 17），八個非空者用六種格式，
   其中三者指向物不是規格或報告。
2. **§4.2 之 `_Rebuilt`** —— `Engineering Mode` 之交付態為 211 列那份，
   還是 527 列那份？（R-PMH19 (b) 之字面比對選中了資料較少且檔名拼錯的那份。）
3. **§9 第 2 項** —— `Engineering Mode/App Team Effort/` 是交付夾還是工作
   子目錄？此決定母體為 **17** 或 **16**，並連動 §3 之 `D5` 計數。


---

# §13 —— 05a／05b 之併篇上繳（同一往返）

## 13.1 抄錄核對表（R-PMH26／R-PMH27）

| 來源 | 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|---|
| 05a | R-PMH26 | 上游 037 命名不在範圍（四項拘束） | 401 | `94a9c442a2f7f36e` | `94a9c442a2f7f36e` | 逐字相符 |
| 05b | R-PMH27 | Q3 重裁定案 | 701 | `e6e14fc0a96c1ccc` | `e6e14fc0a96c1ccc` | 逐字相符 |

Pei 之兩則裁定原文已逐字抄入 `RULINGS.md` 各該段首：
「037的報告命名不一致不關我的事 我不能要求他們改」／「（甲）」。

## 13.2 `[PEI-REOPEN]` 之撤除與 R-PMH10 原文複驗（05b §三）

| 檔 | 撤除後之殘留 |
|---|---|
| `DECISIONS.md` | **0** |
| `feature.yaml` | **0** |
| `PLAYBOOK.md` | **0**（Open rulings 表之 Q3 一列已移除，並加「已結清」一行） |
| `RULINGS.md` | 2 —— **皆為「標記已撤除」之敘述本身**，非生效中之標記 |

**R-PMH10 原文 SHA256 = `885070968235b262`**，與 02 包所記、05b §三所要求者
**相同**。撤除之標記與新附註皆置於其 fenced block **之外**。

R-PMH10 條後之附註改為「已於 2026-08-24 重裁定案，見 R-PMH27」，
並保留語料四次演進之對照表（供追溯），及其末句效力之重申
（日後客戶要求填寫時，字串由 Pei 給定並另立新條，不得以「補上」之名逕行填寫）。

## 13.3 ⚠ R-PMH27 所引之母體為 16，執行層實測為 17

R-PMH27 逐字載「`D5`：9/16 空、7/16 非空」，其 (a) 稱「七個非空者中有兩者填錯」。
**執行層依 R-PMH24 獨立重篩得 17**（本檔 §2，停止條件 7 之回報），
故對應數字應為：

| | R-PMH27 所載（16） | 執行層實測（17） |
|---|---|---|
| `D3` 空 | 16/16 | **17/17** |
| `D4` 空 | 16/16 | **17/17** |
| `D5` 空 / 非空 | 9 / 7 | **9 / 8** |
| (a) 指稱物非規格亦非報告者 | 2 | **3**（增 `App Team Effort` 之 `FM-WI-SW-PSCFTS011-ENGM-A01`） |

**結論不受影響**：兩種母體下 `D3`／`D4` 皆全空，`D5` 皆為「空者略多」，
且 **R-PMH27 明載本裁定「不是多數決」**。故三欄留空之結論成立，
僅其所引之數字待分析層依本檔 §2、§3 更新。

已於 `RULINGS.md` 之 R-PMH27 條後以勘誤附註記明（**原條文不改字**）。
母體究為 16 或 17，繫於 `Engineering Mode/App Team Effort/` 之身分（§9 第 2 項），
**待 Pei 裁定**。

## 13.4 05a §三之獨立複驗（先算後比）

**量測條件**：對 `ASW-R2` 全樹 `**/*037*.xlsx`（排除 `~$` 暫存）唯讀掃描，
**未讀 05a 之值再比對，係先算後比**。

| 項 | 05a 所載 | 執行層實測 | 結果 |
|---|---|---|---|
| `Vehicle Settings/VF230_V1_R5` | 11 | **11** | 相符 |
| `Vehicle Settings/CFTS044` | 4 | **4** | 相符 |
| `Vehicle Settings`（根層） | 4 | **4** | 相符 |
| 其餘各 feature | 各 1 | **各 1** | 相符 |
| 本 feature 之 037 版號 | `V0.1` | **`V0.1`** | 相符 |
| Popup 之 037 版號 | `V0.2` | **`V0.2`**（`…-SWE1-Popup-HMI-V0.2 STLA 報告.xlsx`） | 相符 |

037 檔總數 **36**，分布於 **20** 個目錄。

**一項口徑補述（R-PMH20）**：上列「其餘各 feature 1 份」之 17 個目錄中，
有 4 個是**用途目錄**而非 feature 交付夾 —— `AM:FM/REF`、`SiriusXM/REF`、
`Vehicle Settings/VF230_V1_R5/output`、`…/output/validation`。
**故「17 個目錄」不等於「17 個 feature」**；05a 之實質結論
（份數 >1 者僅 VF230／CFTS044／Vehicle Settings 三處）**不受影響**。

## 13.5 R-PMH26(d) 之適用點與其滿足（05a §四）

**適用點：`inputs/MANIFEST.sha256`。** 該台帳以「SHA256 + 檔名」兩欄記載，
其**指稱以 SHA256 為主、檔名為輔** —— `shasum -c` 之比對標的是雜湊，
檔名只作定位。**本項已滿足，未改動任何檔案。**

已於 `feature.yaml` 之 `paths:` 節前以註解記明其滿足之理由，
並加一句「下列 `paths.*` 之值為檔名，其正確性由 MANIFEST 之 SHA256 背書，
非由檔名自證」—— 以免日後有人把台帳改成只記檔名。

**R-PMH26 (a)(b)(c) 之遵守聲明**：本輪未就 037 檔名差異開立任何 DR、
未產生要求上游改名之建議、未將檔名差異登記為 anomaly。
本檔 §3.2 之「八個非空者用六種格式」係描述 **036 之 `D5` 欄現況**
（本 feature 側之欄位），非描述上游檔名，不在 (c) 之範圍。

## 13.6 本輪 open 項之結清狀態（複驗 05b §四）

| 項 | 05b 所載 | 執行層複驗 |
|---|---|---|
| Q3（D3／D4／D5） | 已結清（R-PMH27） | **已結清** —— 三處標記撤除、`DECISIONS.md` 改 `[RULED]` |
| Q7（`tc_id` abbr） | 已結清（R-PMH16） | **已結清** —— `feature.yaml` `tc_id_format` 已落地並經大小寫敏感複驗 |
| A-PMH06 canon 層 | PENDING-CANON | **相符** —— `new_feature.py` 未改 |
| A-PMH03／04 | PENDING，Phase 4 | **相符** |
| A-PMH10 | PENDING，不阻斷 | **相符** —— R-PMH25 已落地（`design_method_source: x14_dv_target`） |
| A-PMH12 | PENDING，Phase 6／7 前置阻斷項 | **相符** —— 已標於 `DECISIONS.md` §7 |
| H 欄（Test Set） | `[PEI]`，Phase 3 | **相符** |

**⚠ 執行層補一項 05b §四未列者**：**上繳 05 §10 之停止條件 7、8 仍未結清** ——
母體 16／17 之定案、與 `_Rebuilt` 何者為交付態（§4.2）。
二者皆不阻斷 Phase 3，但**不在 05b 之結清表內**，故在此具名，以免落單。

## 13.7 §13 之 git 與工作區動作

| # | 動作 | 對象 |
|---|---|---|
| 1 | heredoc 追加 ＋ 就地改寫 | `RULINGS.md` —— R-PMH26／R-PMH27 ＋ 核對表 ＋ R-PMH27 勘誤附註 ＋ R-PMH10 之 `[PEI-REOPEN]` 撤除 |
| 2 | Python 就地改寫 | `DECISIONS.md` 前言三欄改 `[RULED R-PMH27]` |
| 3 | Python 就地改寫 | `feature.yaml` —— 前言三欄註解改寫、R-PMH26(d) 之滿足理由 |
| 4 | Python 就地改寫 | `PLAYBOOK.md` §6 —— 移除 Q3 一列，加「已結清」一行 |
| 5 | 唯讀掃描 | `ASW-R2` 全樹 `**/*037*.xlsx`（36 檔）—— 未寫入 |
| 6 | heredoc 追加 | 本檔 §13 |

**改狀態 git：0。唯讀 git：0。對工作簿之寫入：0。**
