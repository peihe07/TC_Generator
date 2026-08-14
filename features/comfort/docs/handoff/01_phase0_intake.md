# 01 — Comfort HMI / Phase 0 Intake 下放包

- 產出層：分析層（Claude Desktop, Project「FW036 分析層」）
- 日期：2026-08-14
- 對象：執行層（Claude Code）
- 前置：無（Comfort 為新開案，`features/comfort/` 於本包建立）
- 依據：`docs/fw036/FEATURE_ONBOARDING.md` §0 決策層級、§1 Phase map、
  §2 workbook_state、§3 spec_mode；`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
  §4.1／§8.2／§8.4／§10.7／§11

---

## 1. 開案狀態

`features/` 於 2026-08-14 實測僅有 `amfm / home / media / privacy / projection /
sxm`，無 `comfort`；`_intake/` 僅有 `AMFM / Privacy / SXM`。故 Comfort 位於
Phase 0 之前，本包為開案第一份下放包。

| 項目 | 值 | 依據 |
|---|---|---|
| Feature | Comfort | 037 標題 |
| workbook_state | `BLANK` | 客戶交付夾無 036 workbook（實測） |
| spec_mode | `A`（Polarion/SYS1 export） | SR24 SYS1 export 已在 `spec-index/cache/` |
| scaffold 母本 | `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260121.xlsx` | 同 Privacy 前例 |

`BLANK` 之綁定依 FEATURE_ONBOARDING §2「BLANK fallback chain」：
style authority = 最近之 FW036 sibling feature done region（**STYLE ONLY**），
Test Group / Test Set 欄 FILL，spec_reference 由 spec_mode 模板構造，
cross-feature exemplar 一律帶 `cross-feature: style only` 標記，
其中每一個字面值（label、數字、popup 文字、狀態名）必須回溯至 Comfort 自身
spec，並以 lint rule 強制，不得倚賴紀律（A-026 教訓）。

---

## 2. 037 結構實測

量測條件：檔案 `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`，
sheet `Analysis Report`，header 位於 row 7（20 欄），資料列 row 8–505，
以 A 欄（`SWE-Requirement ID`）非空計數。工具：openpyxl `data_only=True`。

| 量測項 | 值 |
|---|---|
| 資料列總數 | 498 |
| Categorization = `Heading` | 95 |
| Categorization = `Functional Requirement` | 403 |
| ID 形態為 parent（`SWE1-HVAC-NNN`） | 129 |
| ID 形態為 leaf（`SWE1-HVAC-NNN-NN`） | 369 |
| parent 形態 ∩ `Heading` | 95 |
| parent 形態 ∩ `Functional Requirement` | **34** |
| leaf 形態 ∩ `Functional Requirement` | 369 |
| 模組 token | 全數 `HVAC`（單一） |
| HMI Source ID 缺漏 | 0 |
| 相異 spec section | 129（與 parent 數一對一） |

章節分布（依 HMI Source ID 第一行之 section 前綴）：
2(113)、16(115)、14(49)、7(48)、11(47)、12(29)、17(23)、13(20)、10(19)、
3(17)、9(10)、18(4)、15(3)、6(1)。

---

## 3. 已簽裁決條文

以下條文由 Pei 於 2026-08-14 chat 裁定，逐字記錄。執行層直接遵行，不再詢問。

```
R-C1  spec baseline
Comfort feature 之 spec baseline 採 SWE.1（037）所引用者，即
SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)。

spec_reference stem 一律使用上列 SR24 檔名，與 037 之 HMI Source ID 完全一致，
不得改寫為 SR25。

SR25 CR29359 (Feb 24 2025) 於本 feature 為 out-of-scope 參考資料，不得作為
spec 來源、不得用以推翻 SR24 之字面內容、不得據以擴張驗證範圍。

依據：037 之 HMI Source ID 129/129 全數指向 SR24 CR24879；trace chain 完整性
優先於文件新舊。
```

```
R-C2  UI label 拼寫
TC 之 UI label 與狀態文字依 SR24 之拼寫與大小寫（例：AUTO、RECIRC、grayed、
A/C），不採 SR25 之 Auto／recirc／greyed／AC。

背景：SR25 對同一批 section 做過大小寫與拼寫調整；因 R-C1 定 SR24 為基線，
SR25 之拼寫不進 TC。pilot review 時若見 TC 使用 SR24 拼寫而與 SR25 不同，
不構成 defect。
```

```
R-C3  leaf 判準
leaf（驗證單位）集合 = Categorization == "Functional Requirement"，共 403 列。

禁止以 tc id 後綴形態（是否具 -NN）判定 leaf。該判準只得 369 列，會漏掉 34 列
「ID 為 parent 形態、但自身即為 Functional Requirement 且無子項」者
（例：037 row 66 SWE1-HVAC-011 Fan Speed Control、row 137 SWE1-HVAC-026
Rear Defrost Control、row 183 SWE1-HVAC-037 On/ State）。

此判準須以 recon 腳本之 assertion 機械強制（403 == Functional Requirement
計數），不得僅寫在文件裡。
```

```
R-C4  HMI Source ID 解析
HMI Source ID 儲存格取第一行為 spec section id。其後各行為 Polarion item id
（例 ..._7.3\n4803284\n4803285），共 92 列具此形態，不參與 section 解析，
保留為 audit 佐證欄位。

解析後之 section id 相異數必須為 129；不符即 fail-loud，不得靜默略過。
```

```
R-C5  SR25 新增內容之處置
SR25 outline 共 187 節，其中 58 節未被 037 引用；扣除章級容器標題、1.x
Assumptions 與影像頁後，屬實質需求而 037 未分析者為：
  18.2 / 18.3 / 18.4          （BCW1、BCW2，10.25" Comfort Widget）
  19.1 / 19.2 / 19.3          （W0、LCW1、LCW2，7" Home screen Comfort Widget）
  20.1 ~ 20.4.3（10 項）       （CRB1–CRB4.3，LATAM Alternative Rear Blower）
  21.1 ~ 21.5 + 21.3.1（6 項） （L3H1–L3H5，L3 HVAC management）

因 R-C1 定基線為 SR24，上列全部 out of scope，不產 TC、不入 coverage 分母、
不列 BLOCKED。僅以單一 note 型 anomaly 記錄其存在，供日後 037 升版時查考。

不得以「求完整」為由自行補成 RD 項目或 TC（§8.2、§8.4.2）。
```

---

## 4. Open PENDING（須 Pei 裁定後方可進 Phase 3）

| # | 項目 | 選項 | 阻塞範圍 |
|---|---|---|---|
| P-C1 | Test Group 命名 | `Comfort`（spec 標題）／`Climate`（客戶交付夾為 `Climate Control Interface`） | framework Part N、workbook Test Group 欄 |
| P-C2 | tc_id scheme | `NR1L-HVAC-{NNN}`（037 模組 token）／`NR1L-Comfort-{NNN}`（Privacy 全稱前例） | 全部 TC ID，凍結後不可改 |

P-C1／P-C2 未裁定前，Phase 3 framework 不得鎖定。Phase 1 recon 不受此阻塞，
可先行。

---

## 5. 執行層作業指示（Phase 0 → Phase 1）

依 Tier 1 授權執行，逐項回報實測值，不以預期值代替。

1. **建立 feature 骨架**
   `scripts/new_feature.py` 產生 `features/comfort/` 之
   `RULINGS.md`、`ANOMALIES.md`、`DECISIONS.md`、`DATA_REQUESTS.md`、
   `PLAYBOOK.md`、`RUNBOOK.md`、`feature.yaml`。
   §3 之 R-C1～R-C5 以原文貼入 `RULINGS.md`。

2. **素材落位確認**
   `_intake/Comfort/` 應含 037（由 Pei 放入，屬 Tier 3）。
   spec 素材不需另行搬移：
   - `spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx`（68.40 KB，實測）
   - `spec-index/cache/…(September_25_2023).json`（10.57 MB，實測）
   - `spec-index/sources/Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf`（6.16 MB，實測）
   三者齊備，spec_mode A 可直接建 outline map。

3. **recon.py**
   - leaf inventory 依 R-C3；輸出必須報 `Functional Requirement == 403` 之
     assertion 結果，非僅印計數
   - HMI Source ID 依 R-C4 解析；輸出相異 section 數，assert == 129
   - outline map 對 SR24 export 建立；129 個 cited section 逐一查得，
     fail-loud on miss（不得以「SR25 有」代替）
   - 產出 `RECON.md` 與預填之 `DECISIONS.md`

4. **anomaly 登記（本包預先指定，執行層照登）**
   - `A-CF01`（note）：SR25 CR29359 存在且含 037 未分析之新章節 19–21 與
     18.2–18.4，依 R-C5 out of scope。記錄清單以備 037 升版時查考。
   - `A-CF02`（note）：客戶交付夾
     `10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/ComfortHMI/`
     於 2026-08-14 實測放置之 spec 為 SR25 PDF（13.86 MB）與 SR25 SYS1 xlsx
     （72.80 KB），與 R-C1 所定之 SR24 基線不一致。此為交付端素材，
     不影響 pipeline 取材（pipeline 取 `spec-index/`），但交付時之附件
     一致性須由 Pei 決定是否回填 SR24。
   - `A-CF03`（結構）：037 有 34 列 parent 形態卻為 Functional Requirement，
     naive leaf 判準會漏 8.4%。已由 R-C3 處置，登記供其他 feature 參照。

5. **DATA_REQUESTS.md 初始化**
   目前無已知缺檔。仍須建檔並寫入 standing rule：任何新發現之外部引用，
   於登記當下同時建 ANOMALIES 條目與 DATA_REQUESTS 列。

6. **上繳**
   寫入 `features/comfort/docs/upstream/01_phase0_intake.md`，並更新
   `features/comfort/docs/INDEX.md`（索引由執行層維護，分析層不寫）。
   上繳包須附「本包是否仍有該驗而未驗者」之獨立判斷。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 待簽 |
|---|---|---|
| R-C1 spec baseline = SR24 CR24879 | ✅ §3 | 已簽 2026-08-14 |
| R-C2 UI label 拼寫依 SR24 | ✅ §3 | 已簽 2026-08-14 |
| R-C3 leaf 判準 = Functional Requirement (403) | ✅ §3 | 已簽 2026-08-14 |
| R-C4 HMI Source ID 取第一行 | ✅ §3 | 已簽 2026-08-14 |
| R-C5 SR25 新增內容 out of scope | ✅ §3 | 已簽 2026-08-14 |
| P-C1 Test Group 命名 | ✅ §4（PENDING 表） | 未裁 |
| P-C2 tc_id scheme | ✅ §4（PENDING 表） | 未裁 |

R-C1～R-C5 均已以區塊形式出現於 §3，執行層須將該五條原文貼入
`features/comfort/RULINGS.md`（R19-2）。

---

## 7. 量測工具缺陷紀錄（§5a）

本包 §2 之數字全部以 openpyxl 對 037 實測，非引用先前輸出。

另記一則工具缺陷，供後續比對類作業引以為戒：本次曾以
`difflib.SequenceMatcher` 預設參數比對 SR24／SR25 文字，section 16.3 得
0.312、2.3 得 0.764，看似重大內容漂移。實為 `autojunk` 啟發式在長字串上
將空白判為 junk 所致之低估。關閉 autojunk 並改以 alnum 正規化後，兩節皆
落於 ≥0.98。**該缺陷不報錯**，若未逐字覆核將導出錯誤結論。凡以相似度為
判準之檢查，一律須以已知全集抽樣覆核（§5a 末條）。

此比對結果現已不影響裁決（R-C1 選 SR24，不需 SR25 比對支撐），但方法論教訓
保留。
