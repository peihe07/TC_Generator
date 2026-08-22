# 下放包 01 —— Power Moding HMI 開案（Phase 0 intake）

- 日期：2026-08-22
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/01_intake.md`
- 前一包：無（本 feature 首包）

---

## 一、本包之目的

建立 `features/power_moding/` 之骨架、驗明四份素材、實測工作簿欄位對應與
`workbook_state`，並回報 Phase 1 recon 之輸入。**本包不產出任何 TC，不寫回工作簿。**

### 1.1 開案之背景 —— 命名落差已查明，不是兩件事

Pei 之 feature 指派名為 **`Disclaimer screen`**，而四份素材之檔名皆為
**Power Moding HMI**。二者不衝突，其關係為：

| 層級 | 值 | 依據（實測） |
|---|---|---|
| 客戶交付夾名 | `Disclaimer screen` | `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Disclaimer screen/` 實際存在，內含本次四份素材 |
| 規格文件／工作簿 | Power Moding HMI Logic and Flow R1 SR24 2A | 037 之 `HMI Source ID` 欄 48 列全為 `Power Moding HMI Logic and Flow R1 SR24 2A_{章節}` |
| repo slug / test_group | `power_moding` / `Power Moding` | **R-C6 前例**（見 §二 R-PMH2） |

**Comfort 為完全同型之前例**，其 `feature.yaml` 第 6 行逐字為：

```
test_group: "Comfort"          # R-C6 — spec 標題模組名，非交付夾之 "Climate Control Interface"
```

即：交付夾以 FROP 名命名（Comfort → `Climate Control Interface`；
Power Moding → `Disclaimer screen`），而 feature 身分取規格標題模組名。
本 feature 照此辦理，**不另立新慣例**。

---

## 二、裁決條文（逐條抄入 `features/power_moding/RULINGS.md`）

> 抄錄時逐字，不改寫、不合併。抄畢於上繳包附逐條核對結果。

```
R-PMH1（範圍）
本 feature 之驗證範圍為 037「Analysis Report」分頁中 `Categorization`
欄逐字為 `Functional Requirement` 之列全集，不以 `FROP /
(Feature Rollout Plan)` 欄之值作範圍過濾。

判準為可測：以 `Categorization == "Functional Requirement"` 掃描全表求
其全集，另以「全表列數 − Heading 列數 − 表頭與抬頭列數」求餘數驗證其
為空（R-G10）。分析層 2026-08-22 之實測值為 48（Heading 8），供對照，
不得以該數字代替重算。

交付夾名 `Disclaimer screen` 為 FROP 標籤，不縮減本範圍；FROP 欄之值
於本 feature 之用途僅為 framework Layer 2 之候選輸入（見 R-PMH5），
不作為 in/out of scope 之判準。
```

```
R-PMH2（feature 身分與 test_group）
`feature` 為 `Power Moding`，slug 為 `power_moding`，`test_group` 為
`Power Moding`（規格標題之模組名）。

交付夾名 `Disclaimer screen` 不進入 `test_group`、不進入任何 TC 欄位，
僅記於 `feature.yaml` 之交付路徑註解。

依據：Comfort R-C6 之同型處置（交付夾 `Climate Control Interface`，
`test_group` 為 `Comfort`）。
```

```
R-PMH3（與既有 `power` feature 之分離）
`features/power`（test_group `Power Management`，來源 CFTS009／CFTS010，
需求 id 形態 `SWE-PM-nnn`）與本 feature 為不同需求族、不同交付物、
不同客戶交付夾，**任何產物不得跨用**。

具體拘束三項：
(a) 欄位對應不得沿用 `features/power/feature.yaml` 之 `workbook.columns`，
    須自本工作簿 r9 表頭逐欄實測後書寫；
(b) 本 feature 之裁決前綴為 `R-PMH`、異常前綴為 `A-PMH`、
    資料請求前綴為 `DR-PMH`，不與 `R-P` / `A-PW` / `DR-PW` 共用序號；
(c) 任何以 `features/power*` 形態之 glob 自本日起會同時命中兩個目錄；
    腳本、備份、掃描與 `git add` 之 pathspec 一律寫全名，不用萬用字元。
```

```
R-PMH4（素材台帳之到齊定義）
素材之「到齊」定義為：清單每項附其檔案系統絕對路徑與 SHA256，且
`shasum -c` 對得上（G-L）。「檔名相符」「大小相同」皆不構成到齊。

本 feature 之素材來源目錄為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Disclaimer screen/`
（唯讀，不得寫入）。搬入 `features/power_moding/inputs/` 者為複本，
搬入前後各記 SHA256 並登入台帳（G0）。
```

```
R-PMH5（工作簿既有 48 列之處置）
本工作簿之資料列 10–57 共 48 列已填入 B/D/G/H/I/L/M/N 八欄，其內容為
037 對應欄位之機械搬運（D←SWE-Requirement ID、G←FROP、H←Requirement
Title、I←Requirement Description、L←Verification Method、
M←Verification Criteria、N←HMI Source ID）。

該 48 列**不是 done region**，不具 style authority：其 `Test Case Author`
欄（AB）48 列皆空、`Test Case ID`（F）48 列皆空、`Test procedure`（L）
48 列皆無編號步驟，不滿足 canon §2 之「qualifying done row」三項。

處置：視為**待改寫之草稿列**，其現況以 content-hash 立為基線，供改寫前後
比對；style authority 依 canon §3 之 BLANK 回退鏈決定，**不得取自該 48 列**
（§9.1 通則 4：BLANK 之 style authority 不得取本管線自身或未經核可之產出）。
```

```
R-PMH6（G/H 兩欄現值之處置延後）
現況 G 欄（Test Group）之值為 FROP 標籤、H 欄（Test Set）之值為 037 之
Requirement Title（完整句子，違反 canon §4.2「短名詞片語、非句子」）。

二欄之最終值屬 framework Layer 1／Layer 2 之產物，於 Phase 3 定版；
**Phase 0/1 不得改動該二欄**，僅登記現況。FROP 欄之 13 個相異值得作為
Layer 2 之候選輸入之一，與規格目次取交集後再判granularity（canon §4.1.2）。
```

---

## 三、分析層已完成之實測（供對照，執行層須獨立重算）

> 依 R-G7-1 之精神：下列數字為**對照向**，不是可引用之結論。
> 執行層以自身路徑重算，不符即停並回報。

**量測條件**：對 `/mnt` 沙箱之聊天附件複本以 `openpyxl`（`data_only=True`）讀取；
**該複本無雜湊保證，依 §9.1 通則 5，下列數字為「被取代」而非「被複驗」。**

### 3.1 037（`Analysis Report` 分頁，第 8 列起）

| 項 | 實測值 |
|---|---|
| `Categorization == Functional Requirement` | **48** |
| `Categorization == Heading` | 8 |
| `FROP` 相異值 | **13** |
| `HMI Source ID` 之文件 stem | 全 48 列同一份（`Power Moding HMI Logic and Flow R1 SR24 2A`） |

FROP 分布：Customizable Splash Screen / Animations 12、**Disclaimer screen 7**、
Audio Management 7、Power Management 5、Steering Wheel Controls 5、Bluetooth 3、
FOTA Via Wi-fi 2、Rear View Camera 2、Climate Control 2、WiFi 1、
EV/PHEV Pages 1、e-call (private) 1。（合計 48，餘數 0）

FROP `Disclaimer screen` 之 7 個 leaf 及其工作簿列號：

| 工作簿列 | SWE-Requirement ID | 章節 |
|---|---|---|
| 12 | `SWE1-HMI-PM-001-03` | §7.1 |
| 13 | `SWE1-HMI-PM-001-04` | §7.1 |
| 14 | `SWE1-HMI-PM-001-05` | §7.1 |
| 16 | `SWE1-HMI-PM-003` | §7.2 |
| 17 | `SWE1-HMI-PM-004` | §7.3 |
| 18 | `SWE1-HMI-PM-005` | §7.4 |
| 44 | `SWE1-HMI-PM-022-02` | §10.4 |

**此表僅為交付夾名之出處說明，非範圍界定**（R-PMH1）。

### 3.2 036 工作簿

| 項 | 實測值 |
|---|---|
| 分頁名 | `Test Case Specification 測試用例規範`（**與 `features/power` 之 `Test Case Specification&Result` 不同**） |
| 分頁清單 | `Cover_old` / `ChangeHistory_old` / `Cover 封面` / `ChangeHistory 修訂履歷` / `Product Document 記錄封面頁` / `Test Case Specification 測試用例規範` / `Reference` / `Test Case Framework` / `QS Suggestion` / `下拉選單`（10） |
| 表頭列 | r9（`B:No.#` … `AI:Remarks 備註`） |
| 資料列 | 10–57 連續，48 列，與 037 之 48 leaf 為 1:1 |
| 非空欄 | B(48) D(48) G(48) H(48) I(48) L(48) M(48) N(48)，其餘皆空 |
| `F`(tc_id) 非空 | 0 |
| `AB`(author) 非空 | 0 |
| `L` 具編號步驟（`^1.`） | 0 |
| 合併儲存格 | `A1:AF1` / `B7:AB7` / `U8:AA8` / `AC7:AI7` / **`D5:F5`** |
| `D5`（範圍 Scope） | **空白** |
| 封面 | 核准者 劉安哲 AllenACLiu、審查者 張愷霏 ErinKFChang、作者欄空白 |

> ⚠ **r9 表頭有兩個 `Estimated Test Time`（P 與 R）** —— 與 `features/power`
> 所遇之形態相同（A-PW38）。**這不表示欄序相同**，仍須逐欄實測（R-PMH3(a)）。

### 3.3 `workbook_state` —— 現有四類不足以描述，須裁

canon §2 之四類為 `BLANK` / `PARTIAL_CLEAN` / `PARTIAL_INTERLEAVED` / `FULL`。
本工作簿為 **48 列 filled、0 列 qualifying done**：

- 不是 `BLANK`（其定義為「zero filled rows」，而此處 filled = 48）
- 不是 `PARTIAL_CLEAN`（其定義需「contiguous **done** region」，而 done = 0）

依 canon §2 末句「Ambiguous segmentation → Tier 2」，**此為須裁項**，
列入 §六 [PEI]。分析層之提案見該節。

---

## 四、作業步驟

> 逐步執行；每步之產出寫入指定路徑。任一步觸及 §五之停止條件即停並回報，
> 不得跳過續做後續步驟。

1. **建骨架** —— 以 `scripts/new_feature.py` 建立 `features/power_moding/`
   之標準檔（`PLAYBOOK.md` / `RUNBOOK.md` / `RULINGS.md` / `ANOMALIES.md` /
   `DATA_REQUESTS.md` / `DECISIONS.md` / `feature.yaml` / `inputs/` / `data/` /
   `docs/` / `generated/` / `scripts/` / `sandbox/`）。
   `docs/handoff/` 已存在且含本檔，**不得覆寫**。
   若 `new_feature.py` 之參數與本 slug 不合，回報其實際介面，不自行改腳本。

2. **抄錄裁決條文** —— §二之六條逐字抄入 `RULINGS.md`，附逐條核對表
   （條號、字數或 SHA256、是否逐字相符）。

3. **素材搬入與台帳（G0）** —— 自
   `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Disclaimer screen/`
   複製四份至 `features/power_moding/inputs/`：
   - `FM-WI-FSM-036-A01 …_SWQT_PowerModingHMI_20260819.xlsx`
   - `FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1 STLA 報告.xlsx`
   - `SYS1_HMI_Power_Moding_HMI_Logic_and_Flow_R1_SR24_2A.xlsx`
   - `Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023).pdf`

   **來源目錄唯讀**，複製前後各記 SHA256 與 mtime，寫入
   `docs/upstream/01_intake.md` §素材台帳（R-PMH4）。
   四份以外之檔案不得搬入；來源目錄若另有本表未列之檔，登記後停手詢問。

4. **037 全表解析** —— 獨立重算 §3.1 之四個數字（不得讀本檔之值再比對，
   須先算後比）。`Categorization` 之餘數驗證須為 0（R-G10）。
   結果與 §3.1 不符者，逐項列出差異並停。

5. **036 欄位對應實測** —— 自 r9 表頭逐欄比對出 `feature.yaml` 之
   `workbook.columns` 全部 16 個鍵；報告匹配數（如 `16/16`）與其比對方法
   （逐字／正規化後）。**不得沿用任何既有 feature 之欄位表**（R-PMH3(a)）。

6. **`workbook_state` 判定** —— 依 canon §2 三步逐列判定，輸出
   filled / qualifying-done 之列號集合與其判定依據（三項條件各自之結果），
   並就 §3.3 之分類缺口提出處置提案，**不自行歸類**。

7. **spec_mode 分類** —— 依 canon §3。本 feature 同時具 SYS1 匯出（xlsx）
   與 PDF，須先驗兩者之抽取能力再判（§9.1 通則 6：判「不可讀」前須跨素材
   形式試過）。PDF 之文字層以 `pdftotext` 產出率測試，SYS1 匯出以其分頁
   （`Basic Report` / `Polarion` / `_polarion`）之欄位結構測試，兩者各自
   報告其涵蓋之章節數，並依 §9.1 通則 3 指定何者為判讀基準、何者為追溯用。

8. **`feature.yaml` 草案** —— 依實測值填寫；`test_group` 依 R-PMH2 為
   `Power Moding`；交付路徑以註解記交付夾名 `Disclaimer screen`。
   宣告值與生效值分開記（G-C）。

9. **登記缺口與異常** —— 本包所見之任何未涵蓋項以 `A-PMH{n}` 登記，
   附證據與提案處置，**不裁定**。

---

## 五、停止條件（canon §0 六條，逐條適用）

1. 規格查找未解（章節、PU id、檔案缺失）
2. `workbook_state` 分段有歧義 —— **本包已預期會觸發（§3.3），觸發即停並回報，
   不得自行歸入四類之一**
3. 寫回不變量違反（本包無寫回，若任何步驟需寫入工作簿即為越權，停）
4. 需要之規則無 canon／profile 涵蓋
5. 造值壓力：來源未載之任何值
6. done region 與規格矛盾（本 feature 無 done region，見 R-PMH5）

另加本包專屬二條：

7. `new_feature.py` 之 scaffold 會覆寫 `docs/handoff/01_intake.md` 或任何既有檔 → 停
8. 素材來源目錄之檔案清單與 §四步驟 3 所列不符 → 登記後停

**全部 git 操作屬 Pei**（R-G5）。執行層只準備 commit 訊息與 pathspec，不執行。

---

## 六、待裁清單

| # | 事項 | 層級 | 分析層提案 |
|---|---|---|---|
| Q1 | `workbook_state` 之分類（48 filled / 0 done，四類皆不合） | **[PEI]** | 提案：比照 `BLANK` 之**策略**（style authority 走回退鏈、write-back 自首資料列改寫、done invariant 不適用），但**另立狀態名** `PREFILLED_DRAFT` 並回饋 canon §2；不逕行併入 `BLANK`，因其列非空，寫回策略之「append」與此處之「改寫既有列」不同 |
| Q2 | 036 母本身分 —— R-G1 規定新 feature 一律以 `forms/…_20260817_ext.xlsx` 為母本，而本 feature 之交付夾已有一份帶 48 列內容之 036 | **[PEI]** | 提案：以客戶交付夾之現有檔為交付標的（其已含 48 列 req 對應且已在客戶手上），R-G1 之母本規定於「客戶已提供帶內容之 036」時不適用；惟須由執行層實測兩者之結構差異（分頁、DV 含 x14、B 欄公式、欄序）後再定案 |
| Q3 | 工作簿 `D5` 範圍 Scope 欄空白 | **[PEI]** | 提案：填 `Power Moding HMI Logic and Flow R1 SR24 2A`（規格文件全名），與 037 之 `HMI Source ID` 一致；不填交付夾名 |
| Q4 | 既有 48 列之 G/H 欄最終值 | [PROPOSED]，Phase 3 | 依 R-PMH6 延後至 framework 定版 |
| Q5 | 037 之 `Verification Criteria` / `Verification Method` 現已落在 M/L 欄 —— 其是否作為 TC 撰寫之輸入之一 | [PROPOSED] | 提案：作為**參考輸入**而非權威；權威為規格原文（PDF／SYS1 匯出）。理由：037 之該二欄本身即上游之推導產物，以其為據等同以推導物取代來源 |
| Q6 | slug `power_moding` 與既有 `power` 之相鄰性 | 已裁 | R-PMH3(c) |

---

## 七、上繳包要求（`docs/upstream/01_intake.md`）

須含下列各節，**缺節退回不予核可**：

1. 素材台帳：四份之來源路徑、目的路徑、搬入前後 SHA256、mtime、`shasum -c` 結果
2. §二六條之抄錄核對表
3. §四步驟 4–7 之實測結果（含量測條件與工具選擇之揭露，R-G8）
4. `feature.yaml` 草案全文
5. `workbook_state` 判定之逐列依據與 Q1 之處置提案
6. `A-PMH{n}` 異常清單（含證據與提案處置）
7. 待答之 `DR-PMH{n}`（若有）
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略；此節於
   Projection 連續六輪產出實質發現
9. 建議之 commit 訊息與 pathspec（**不執行**）
10. `docs/INDEX.md` 之建立與本輪次列（執行層維護，分析層不寫）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 是否已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH1 | 範圍 = 037 `Functional Requirement` 全集 | ✅ |
| R-PMH2 | feature 身分與 `test_group`，交付夾名不入欄位 | ✅ |
| R-PMH3 | 與 `features/power` 之分離（欄位／前綴／glob 三項） | ✅ |
| R-PMH4 | 素材台帳之到齊定義 | ✅ |
| R-PMH5 | 既有 48 列非 done region，視為草稿列 | ✅ |
| R-PMH6 | G/H 兩欄之處置延後至 Phase 3 | ✅ |

六條皆為獨立單一事項（§9.1 通則 11），無包裹多件者。
