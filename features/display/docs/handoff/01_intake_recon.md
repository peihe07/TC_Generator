# 下放包 01 —— Display 開案（Phase 0 intake + Phase 1 recon）

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`display`
- 對應上繳：`features/display/docs/upstream/01_intake_recon.md`
- 前一包：無（本 feature 首包）

---

## 一、本包之目的

建立 `features/display/` 之骨架、驗明四份素材、實測工作簿欄位對應與
`workbook_state`，並完成 Phase 1 recon。**本包不產出任何 TC，不寫回工作簿。**

本 feature 之素材形態與既有十二個 feature 皆不同（037 無 `Analysis Report`
分頁、leaf 僅 8 筆、追溯鏈在三份文件間有多套 id 命名），故 Phase 0 與
Phase 1 合為一包，使歧異一次浮現，不分兩輪各發現一半。

---

## 二、裁決條文（逐條抄入 `features/display/RULINGS.md`）

> 抄錄時逐字，不改寫、不合併。抄畢於上繳包附逐條核對結果。

```
R-DM1（feature 身分與 test_group）
`feature` 為 `Display`，slug 為 `display`，`test_group` 為 `Display`。
（Pei 2026-08-24 裁定「就用 Display」。）

037 之模組名 `Display Management` 與 CFTS_020 之文件名
`ICS and DCSD` 皆不進入 `test_group`、不進入任何 TC 欄位；二者僅得
記於 `feature.yaml` 之路徑註解與 `framework.md` 之說明文字。

裁決前綴為 `R-DM`、異常前綴為 `A-DM`、資料請求前綴為 `DR-DM`，
不與任何既有 feature 共用序號。
```

```
R-DM2（037 之來源授權）
037 A03 SWRA（`Display_Management_FMWIFSM037A03_STLA_Report_SWRA.xlsx`）
於 2026-08-24 在 Pei 之磁碟上未能定位；分析層已查
`9_ASPICE/`（無 SWE.1 目錄）、`10_Reviewing/00_TestCase/`、
`6_SW_Test/`、`7_Delivery/`、`0_Project_Management/`、
`Work_Projects/` 下各專案，皆無。

Pei 2026-08-24 授權：以 Claude Project 之附件為該檔之唯一來源，
由 Pei 手動置入 `_intake/Display/`。

執行層拘束二項：
(a) 不得自行向上游索取該檔，亦不得以任何其他檔案代替；
(b) 該檔一經置入即記其 SHA256 與 mtime 入素材台帳；台帳建立後，
    後續各輪之引用一律對台帳所記之 repo 內複本實測，不回頭引用
    本包之任何數字（canon §5a：不以自身先前輸出為來源）。
```

```
R-DM3（多套 id 命名之處置 —— 登記，不解）
本 feature 之追溯鏈在文件間出現多套互不相同之 id 命名：

  037 `SWE1 Requirements` 分頁   → `SWE-DM-001` … `SWE-DM-008`
  037 `SWE1 Requirements` 分頁   → `SYS-DISP-001` …（Source Requirement ID）
  037 `SYS2 Traceability` 分頁   → `SWE1-DM-001` …（同一物件，另一寫法）
  037 `SYS2 Traceability` 分頁   → `SYS-RA-DISP-001` …（指向 SYS2）
  SYS2 `Basic Report` 分頁       → `SYS-RA-DM-001` … `SYS-RA-DM-087`
                                    及 `SYS2-RA-088` 以後

`SYS-RA-DISP-*` 與 `SYS-DISP-*` 兩種寫法在 SYS2 released 版中之出現次數
為 **0**（量測條件見 §三 3.3）。

本輪之處置為**登記而非解決**：執行層以 `A-DM{n}` 逐項登記，附證據與
提案處置，不得自行推定其對應關係（例如推定
`SYS-RA-DISP-001` ↔ `SYS-RA-DM-001`）。任何跨命名之對應皆屬
canon §0 逸出觸發第 1 條「規格查找未解」，須停並回報。

`feature.yaml` 之 `req_id` 欄最終寫何種形態，屬 Tier 2，於 Phase 2 裁定；
本輪僅記現況。
```

```
R-DM4（037 之 Excluded 分頁其 id 語意已查明）
037 `Excluded NRLs (HW-only)` 分頁之 `NRL ID` 欄，其 8 個值
（`PSCFTS020-1-45-1` 等）**不是 SYS2 之 NRL ID**（SYS2 之 NRL ID
形態為 `NRL-52839`），而是 SYS2 `SYS2 Melco ID` 欄之值。

分析層已實測：該 8 值在 SYS2 Melco ID 欄之 99 個 token 中 8/8 命中
（量測條件見 §三 3.3）。

拘束：執行層引用該分頁時一律稱其為 Melco ID，不得以「NRL ID」之欄名
為據去 SYS2 之 NRL 欄查找 —— 那會 8/8 查無，並被誤讀為追溯斷鏈。
本條為已解之項，不再登記為 anomaly。
```

```
R-DM5（intake.py 之 sniffer 對本 037 之已知偏差）
`scripts/intake.py` 之 `SHEET_SIGNATURES` 以
`"Analysis Report" in names` 判定 `swra_report`。本 037 之分頁為
`SWE1 Requirements` / `SYS2 Traceability` / `Excluded NRLs (HW-only)`，
無 `Analysis Report`，故必然被分類為 `spec_xlsx`。

執行層拘束三項：
(a) 照跑 `intake.py`，如實回報其實際分類結果，不得預先改腳本使其命中；
(b) 分類偏差之修法（新增分頁簽章、或以 feature.yaml 人工指定
    `a03_report`）屬 Tier 2，本輪只提案不實作 —— 改判準會改結論，
    不屬 AUTO 之技術選擇；
(c) `intake.py` 之 need-list 推導對本檔亦不適用：其
    `Source Requirement ID` 欄之內容為 `SYS-DISP-nnn` 形態之
    Polarion id，非 `name_{section}` 形態之文件引用。腳本應如實
    報告「不可推導」而非產出空清單；若其產出空清單而未說明，
    以 `A-DM{n}` 登記。
```

```
R-DM6（素材台帳之到齊定義）
素材之「到齊」定義為：清單每項附其檔案系統絕對路徑與 SHA256，且
`shasum -c` 對得上。「檔名相符」「大小相同」皆不構成到齊。

搬入 `features/display/inputs/` 者為複本，來源目錄一律唯讀，
搬入前後各記 SHA256 與 mtime 並登入台帳。

四份以外之檔案不得搬入；`_intake/Display/` 若另有本包未列之檔，
登記後停手詢問。
```

```
R-DM7（覆蓋落差之量測義務 —— 8 vs 80）
037 之 leaf 全集為 8，而 SYS2 released 版之 `Functional Requirement`
列數為 80（`SYS-RA-DM-*` 區段 44 + `SYS2-RA-*` 區段 36；大小寫變體
1 列已計入，見 §三 3.3）。

本落差不得以「037 為權威、故 8 即全集」一句帶過。執行層須於本輪
產出可審之對照：以 SYS2 之 `Functional Requirement` 全集為母體，
逐列標記其是否可對應到 8 個 SWE-DM leaf 之一，對應依據逐列寫明
（Melco ID、Description 文字、或無）。無法對應者列出其列號與
`SYS2 Sys-RA-Feature-ID`。

該對照之用途為**揭露**，不是重新界定範圍。範圍之裁定屬 Tier 2，
於 Phase 2 依此對照為之。此處之判準為 canon §5a：引用任何單一來源
為「權威」前，先確認其涵蓋範圍是否等同其類別 —— 037 只有 8 筆，
不等於 Display 之軟體需求只有 8 筆。
```

```
R-DM8（缺值不得自填）
037 之 8 筆需求描述皆為 SWE 層抽象語句，其中至少四處之具體值
在 037 內不存在：

  SWE-DM-003  Splash / sleep 之時長門檻
  SWE-DM-004  thermal warning threshold 之門檻值與單位
  SWE-DM-005  thermal protection 之 critical 判準與回復條件
  SWE-DM-006  popup priority arbitration 之優先序規則與 timeout

上述各項一律先回 CFTS_020 本文與 SYS3 SYSAD 查；查得者記其章節，
查不得者以 `DR-DM{n}` 登記，不得以領域常識、其他 feature 之值、
或 037 之 `Verification Criteria` 欄文字回填（canon §8.4.1）。

`Verification Criteria` / `Verification Method` 二欄之地位為
**參考輸入而非權威**：其為上游之推導產物，以其為據等同以推導物
取代來源。（形態同 Vehicle Setting R-VF13，惟本 feature 尚未取得
該條之五項限制之對應裁定，故本輪一律不用。）
```

---

## 三、分析層已完成之實測（對照向，執行層須獨立重算）

> 下列數字為**對照向**，不是可引用之結論。執行層以 repo 內複本重算，
> 不符即停並回報。

### 3.1 共同量測條件

- 工具：`openpyxl`，`data_only=True`
- 037 因疑有殘留樣式列，採**非唯讀模式全表掃描**，逐列判「全欄皆空」
  以求真實資料列數（唯讀模式之 `max_row` 為 226，實際非空列為 14）
- SYS2 採唯讀模式，以 A 欄（`ID`）非空判資料列
- 字串比對：`str(v).strip()`，**區分大小寫**（大小寫變體因此可見，見 3.3）
- 標的為 Claude Project 之附件複本，**無雜湊保證**；執行層之重算為
  「取代」而非「複驗」

### 3.2 037（`Display_Management_FMWIFSM037A03_STLA_Report_SWRA.xlsx`）

| 分頁 | 表頭列 | 資料列 | 筆數 |
|---|---|---|---|
| `SWE1 Requirements` | r7 | r8–r15 | **8** |
| `SYS2 Traceability` | r1 | r2–r9 | 8 |
| `Excluded NRLs (HW-only)` | r1 | r2–r9 | 8 |

`SWE1 Requirements` 之欄（r7 表頭，A–R）：
SWE-Requirement ID / Source Requirement ID / Requirement Title /
Requirement Description / Release Version / Categorization /
Sub Categorization / Feasibility / Description-Action for Feasibility /
Impact / Description-Action for Impact / Risk Factor /
Description-Action for Risk Factor / Reusable /
Description-Action for Reusable / Priority / Verification Criteria /
Verification Method

| 項 | 實測值 |
|---|---|
| `SWE-Requirement ID` 符合 `SWE-DM-\d{3}` | 8/8 |
| `Source Requirement ID` 符合 `SYS-DISP-\d{3}` | 8/8 |
| `Categorization` | `Functional Requirement` 8/8（無 Heading、無 Information） |
| `Sub Categorization` | 8 個相異值 |
| `SYS2 Traceability` 之 `Source NRL ID(s)` 非空 | **0/8** |

八個 leaf 之標題與 Sub Categorization：

| ID | Sub Categorization | Requirement Title |
|---|---|---|
| SWE-DM-001 | State Management | Display Operative State Management [ON/OFF/Wakeup] - ON/OFF states |
| SWE-DM-002 | Wake-up Management | Display Operative State Management [ON/OFF/Wakeup] - Touch Based WakeUp |
| SWE-DM-003 | Startup & Wake-up Handling | Display Operative State Management [ON/OFF/Wakeup] - Sleep and Splash |
| SWE-DM-004 | Thermal Management | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Warning Expectations |
| SWE-DM-005 | Thermal Protection Management | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Decisions of OFF/ON |
| SWE-DM-006 | HMI Popup Management | Display Operative State Management & Warning Pop Ups - Pop Up handling |
| SWE-DM-007 | RVC Management | Display RVC Handling - Static |
| SWE-DM-008 | Dynamic Display Arbitration | Display RVC Handling - Dynamic |

### 3.3 SYS2（`SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`）

分頁：`Basic Report`（334 列 × 81 欄）／`Polarion`／`_polarion`

| 項 | 實測值 |
|---|---|
| `Basic Report` 資料列（A 欄非空，r2 起） | **333** |
| `SYS2 Sys-RA-Feature-ID` 符合 `SYS-RA-DM-\d+` | 87 |
| 其餘為 `SYS2-RA-\d+` 形態 | 246 |
| 含 `DISP` 之 id | **0** |
| `SYS2 Grouping` 欄 | `None` 333/333（全欄無值） |

`SYS2 分類 Category` × id 區段交叉（大小寫正規化後）：

| | `SYS-RA-DM-*` | `SYS2-RA-*` |
|---|---|---|
| functional requirement | 44 | 36 |
| heading | 22 | 23 |
| information | 14 | 71 |
| out of scope | 7 | 116 |

> **未正規化之原始分布**為：`Out of Scope` 116、`Information` 85、
> `Functional Requirement` 79、`Heading` 45、`Out of scope` 7、
> `Functional requirement` **1**（r314，`SYS2-RA-313`）。大小寫變體共 8 列。
> 任何以逐字比對實作之 gate 會在此處少算 8 列 —— 執行層之實作須明示
> 其是否正規化。

`SYS2 SW/HW/System` 欄分布：Out of Scope 116、Information 85、System 47、
Heading 45、HW 26、**SW 7**、Out of scope 7。

7 個 `SW` 列之列號與 id：r17 `SYS-RA-DM-016`、r18 `SYS-RA-DM-017`、
r245–r249 `SYS2-RA-244` … `SYS2-RA-248`。

> ⚠ **SW = 7 而 037 之 leaf = 8，且二者不是同一組東西。** r17/r18 之
> Description 為「DCSD supplier 與 HU supplier 應共同開發…」，形態為
> 供應商協作條款而非可測需求。不得以「7 ≈ 8」推定其對應。

Melco ID 交叉驗證：037 `Excluded NRLs` 分頁之 8 個值在 SYS2
`SYS2 Melco ID` 欄之 99 個 token 中 **8/8 命中**（支持 R-DM4）。

### 3.4 素材磁碟路徑（已實測存在）

| 角色 | 路徑 |
|---|---|
| CFTS 本文 | `/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI1.5/SubSystem/Cabin/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` |
| SYS2 | `/Users/peihe/Work/02_Project_R1LR/9_ASPICE/SYS.2 System Requirements Analysis/CFTS_020 ICS and DCSD/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` |
| SYS3 SYSAD | `/Users/peihe/Work/02_Project_R1LR/9_ASPICE/SYS.3 System Architectural Design/Display/SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` |
| 037 A03 SWRA | **磁碟上無**；依 R-DM2 由 Pei 置入 `_intake/Display/` |

> 同目錄另有 `SYS2_CFTS_020-ICS_and_Display_10WaitRAR_20260416.xlsx`
> （較舊、狀態為 WaitRAR）。**不搬入**；若執行層認為需要，登記為
> `DR-DM{n}` 後停手詢問，不自行納入。

---

## 四、作業步驟

> 逐步執行；任一步觸及 §五之停止條件即停並回報，不得跳過續做後續步驟。

1. **確認 `_intake/Display/` 四檔就位** —— 逐檔記 SHA256、大小、mtime。
   037 未就位則停（R-DM2）；其餘三檔可自 §3.4 之路徑複製。

2. **跑 `intake.py Display`** —— 不加 `--scaffold`，先看分類結果。
   如實回報每檔之 `kind` 與 `note`，包含 037 被分類為 `spec_xlsx` 之
   預期偏差（R-DM5(a)）。**不得改腳本。**

3. **建骨架** —— `scripts/new_feature.py`（或 `intake.py --scaffold`，
   擇一並說明理由）。`features/display/docs/handoff/01_intake_recon.md`
   已存在，**不得覆寫**；若 scaffold 會覆寫任何既有檔即停（§五第 7 條）。

4. **抄錄裁決條文** —— §二之八條逐字抄入 `RULINGS.md`，附逐條核對表
   （條號、字數或 SHA256、是否逐字相符）。

5. **素材搬入與台帳** —— 依 R-DM6。

6. **037 全表獨立重算** —— 先算後比，不得讀 §3.2 之值再對照。
   須含：三分頁之資料列數、id 形態命中率、`Source NRL ID(s)` 空值數。
   **量測條件須自行宣告**（唯讀 vs 非唯讀、判空之定義）。

7. **SYS2 全表獨立重算** —— 先算後比。須含 §3.3 之交叉表，且
   **明示是否正規化大小寫**，兩種算法之數字皆報。

8. **R-DM7 之覆蓋對照** —— 以 SYS2 之 `Functional Requirement` 全集
   （正規化後 80）為母體，逐列標記可否對應到 8 個 SWE-DM leaf。
   輸出為表：SYS2 列號 / `SYS2 Sys-RA-Feature-ID` / Melco ID /
   對應之 SWE-DM id 或 `無` / 對應依據。**不得裁定範圍。**

9. **036 母本與欄位對應實測** —— 依 R-G1，母本為
   `forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx`。
   複製一份入 `inputs/`，自其表頭列逐欄比對出 `feature.yaml` 之
   `workbook.columns` 全部鍵，報告匹配數與比對方法。
   **不得沿用任何既有 feature 之欄位表。**
   母本一律不以 `openpyxl` 存回（x14 DV 會被摧毀）。

10. **`workbook_state` 判定** —— 依 canon §2 三步逐列判定。
    預期為 `BLANK`（母本無內容），惟須以實測列出 filled / qualifying-done
    之列號集合，不得因「預期為 BLANK」而略過判定；不可能失敗之檢查項
    標「未實測」而非 PASS。

11. **spec_mode 分類** —— 依 canon §3。本 feature 具 CFTS docx、
    SYS2 Polarion 匯出 xlsx、SYS3 docx 三種形式，須各自測其抽取能力
    （docx 之全文 id 數 vs 索引數；SYS2 之 `Basic Report` 欄位結構），
    再指定何者為判讀基準、何者為追溯用。提案 `D`（CFTS/Word），
    但須以實測支持而非照抄本提案。

12. **跑 `recon.py --feature features/display`** —— 產出 RECON.md /
    DECISIONS.md / `data/recon.json`。若腳本因 037 分頁名不符而失敗，
    回報其失敗訊息與失敗點，**不修腳本**（R-DM5(b)）。

13. **`feature.yaml` 草案** —— 依實測值填寫；`test_group` 依 R-DM1 為
    `Display`。宣告值與生效值分開記。

14. **登記缺口與異常** —— `A-DM{n}` / `DR-DM{n}`，附證據與提案處置，
    **不裁定**。

---

## 五、停止條件

canon §0 六條逐條適用：

1. 規格查找未解（章節、id、檔案缺失）—— **本包已預期會觸發**：
   `SYS-RA-DISP-*` 在 SYS2 中 0 命中（R-DM3）
2. `workbook_state` 分段有歧義
3. 寫回不變量違反（本包無寫回；任何步驟需寫入工作簿即為越權，停）
4. 需要之規則無 canon／profile 涵蓋
5. 造值壓力：來源未載之任何值 —— **本包已預期會觸發**：
   R-DM8 之四處門檻值
6. done region 與規格矛盾（本 feature 預期無 done region）

另加本包專屬三條：

7. `new_feature.py` / `intake.py --scaffold` 會覆寫
   `docs/handoff/01_intake_recon.md` 或任何既有檔 → 停
8. `_intake/Display/` 之檔案清單與 §四步驟 1 所列不符 → 登記後停
9. 任何步驟需要修改 `scripts/` 下之既有腳本才能繼續 → 停並回報
   （R-DM5(b)）

**全部 git 操作屬 Pei**。執行層只準備 commit 訊息與 pathspec，不執行。

---

## 六、待裁清單

| # | 事項 | 層級 | 分析層提案 |
|---|---|---|---|
| Q1 | 036 母本與 `workbook_state` | **[PROPOSED]** | 依 R-G1 用 `_ext.xlsx` 母本，`workbook_state = BLANK`。Pei 若手上另有他人起頭之 Display 036，此條要改，style authority 會自回退鏈改走 done region。簽核時未經修改即生效 |
| Q2 | 驗證範圍：8 個 SWE-DM leaf，或含 SYS2 之 80 個 Functional Requirement | **[PEI]** | 提案：以 8 個 leaf 為 SWE.6 之驗證範圍（037 為 SWE.1 之交付物，SWE.6 對其負責），惟 §四步驟 8 之對照表須隨交付一併揭露，並將無對應之 SYS2 列整理為 RD-1 之提問。不得只交 8 條而不揭露落差 |
| Q3 | `req_id` 欄寫 `SWE-DM-001` 或 `SWE1-DM-001` | **[PEI]** | 提案：寫 `SWE-DM-001`（`SWE1 Requirements` 分頁為需求本體所在，`SYS2 Traceability` 為衍生索引）。另以 `A-DM{n}` 向上游反映二分頁不一致 |
| Q4 | `Verification Criteria` / `Verification Method` 二欄之地位 | **[PROPOSED]** | 提案：參考輸入，非權威（R-DM8 末段）。若 Pei 欲比照 Vehicle Setting R-VF13 開放為值域來源，須另立本 feature 之對應條文與其限制 |
| Q5 | `intake.py` sniffer 之修法 | **[PROPOSED]**，Phase 2 | 提案：於 `SHEET_SIGNATURES` 增以 `"SWE1 Requirements" in names` 判 `swra_report` 之簽章，並於 `feature.yaml` 允許人工覆寫 kind。本輪不實作 |
| Q6 | `D5`（範圍 Scope）欄之內容 | **[PROPOSED]**，Phase 3 | 延後至 framework 定版；候選為 `Display Management`（037 模組名）或 CFTS_020 文件全名 |

---

## 七、上繳包要求（`docs/upstream/01_intake_recon.md`）

須含下列各節，**缺節退回不予核可**：

1. 素材台帳：四份之來源路徑、目的路徑、搬入前後 SHA256、mtime、
   `shasum -c` 結果
2. §二八條之抄錄核對表
3. `intake.py` 之實際分類輸出全文（含 037 之偏差）
4. §四步驟 6–7 之獨立重算結果，**含量測條件之自行宣告**
   （唯讀與否、判空定義、是否正規化大小寫）
5. §四步驟 8 之覆蓋對照表全文
6. 036 欄位對應之匹配數與比對方法
7. `workbook_state` 判定之逐列依據
8. spec_mode 之實測依據（三種素材形式各自之抽取能力）
9. `feature.yaml` 草案全文
10. `A-DM{n}` 異常清單（含證據與提案處置）與 `DR-DM{n}` 開放清單
11. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
12. 建議之 commit 訊息與 pathspec（**不執行**）
13. `docs/INDEX.md` 之建立與本輪次列（執行層維護，分析層不寫）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 是否已以可貼區塊出現於 §二 |
|---|---|---|
| R-DM1 | feature 身分與 `test_group` = `Display`，前綴 `R-DM`/`A-DM`/`DR-DM` | 是 |
| R-DM2 | 037 之來源授權（Project 附件，Pei 手動置入） | 是 |
| R-DM3 | 多套 id 命名之處置 —— 登記不解 | 是 |
| R-DM4 | Excluded 分頁之 id 實為 Melco ID（已解，不登 anomaly） | 是 |
| R-DM5 | `intake.py` sniffer 之已知偏差與不得自行修改 | 是 |
| R-DM6 | 素材台帳之到齊定義 | 是 |
| R-DM7 | 覆蓋落差（8 vs 80）之量測義務 | 是 |
| R-DM8 | 缺值不得自填；`Verification Criteria` 非權威 | 是 |

八條皆為獨立單一事項，無包裹多件者。
