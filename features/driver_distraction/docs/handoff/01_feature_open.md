# 下放包 01 —— Driver Distraction 開線：recon 摘要、framework 草案、待裁清單

- 日期：2026-08-27
- 方向：分析層 → 執行層（Phase 0/1 任務）＋ Pei（待裁 Q1–Q6）
- Feature slug：`driver_distraction`（Q1 待准）
- 本包為本 feature 首包；`docs/handoff/` 於本包寫入前為空（已 list_directory 驗證）

---

## 一、來源盤點（分析層自 Project 附件實測，2026-08-27）

| # | 檔 | 角色（提案） | 實測 |
|---|---|---|---|
| S1 | `DD_SWE1_0807_EN.xlsx`（FM-WI-FSM-037-A03，2026-08-07） | **生成主驅動** | `Analysis Report` 分頁；header row 8、資料自 row 9；28 leaf（`SWE1-RA-Driver_Distraction-001`~`-028`）；Priority 28/28 High；附 Verification Criteria／Verification Method 欄 |
| S2 | `CFTS022_Driver_Distraction…SYSRA.xlsx`（FM-WI-FSM-035-A02） | **anchor pool** | `Basic Report` 264 列：FR 149／Heading 61／Info 47／Out-of-scope 7；ObjectID（7 位）欄齊備；SWE1 之 28 leaf 僅引其中 15 列 FR（-112~-133 區段） |
| S3 | `SYS1_HMI_Driver_Lockout_HMI_Logic_and_Flow_R1_SR24_1A_May_3_2021.xlsx` | HMI spec 索引（參考） | 19 outline 節點（1~4.1）；`SYSRE_HMI_Source ID` = `{檔名}_{章節號}` 形式 |
| S4 | `Driver_Lockout_HMI_Logic_and_Flow_R1_SR24_1A_May_3_2021.pdf` | HMI spec 原文（人讀參考） | 7 頁；p4 Standard Lockout Popup、p5/p6 Fullscreen Lockout 流程圖、p7 Driver Lockout Tables |
| S5 | `SYS3_…SYSAD_V1.docx`（FM-WI-FSM-015-A01） | 架構參考（不入語料） | DdControlService + JudgmentManager、VHAL、HMI 層等分解；含 Sequence Diagram 章 |

**檔型注意（既知偽型態家族）**：分析層手上之 Project 附件為轉換副本 ——
S5 實為 UTF-8 純文字（非 zip/docx）、S4 實為頁影像＋文字之封存檔（非真 PDF）。
**Pei 置入 `inputs/` 之原件型態以實物為準，執行層開檔前先驗型
（`file` / zip magic），不得沿用分析層之判型。**
分析層副本之 sha256 對原件**無比對意義**，本包不列，
`reference` 節之 sha 一律由執行層自 `inputs/` 實物重算。

### SWE1 → CFTS 追溯結構（實測全表）

28 leaf → 14 個 source 配對 → 15 個 CFTS SYS-RA 列。每 source 配對固定
AC1/AC2 兩 leaf。HK 章（-125 為 section 閘）之 leaf 採「閘＋條文」雙引格式
`SYS-RA-…-125\nSYS-RA-…-1nn`。

| SWE1 leaf | CFTS source | 題名 | CFTS ObjectID |
|---|---|---|---|
| 001–002 | 113 | Body OFF | 4915104 |
| 003–004 | 114 | Speedometer（monitor） | 4915105 |
| 005–006 | 115 | Speedometer（≤3MPH → Unlocked） | 4915106 |
| 007–008 | 116 | Speedometer（≥5MPH → Locked） | 4915107 |
| 009–010 | 117 | Locked Out State（access 阻擋） | 4915108 |
| 011–012 | 118 | Locked Out State（使用中轉 Locked） | 4915109 |
| 013–014 | 120 | Lockout Table（其一） | 4915112 |
| 015–016 | 121 | Lockout Table（其二） | 4915115 |
| 017–018 | 125+126 | HK Automatic + P → Unlocked | 4915120, 4915121 |
| 019–020 | 125+127 | HK Automatic + 非P → Locked | 4915120, 4915122 |
| 021–022 | 125+128 | HK Manual + 手煞ON → Unlocked | 4915120, 4915123 |
| 023–024 | 125+129 | HK Manual + 手煞OFF → Locked | 4915120, 4915124 |
| 025–026 | 125+132 | 速度 ≥5MPH → Locked（**見 A-DD1**） | 4915120, 4915128 |
| 027–028 | 125+133 | 速度 ≤3MPH → Unlocked（**見 A-DD1**） | 4915120, 4915129 |

---

## 二、異常登記（候選，待執行層 recon 覆核後入 ANOMALIES.md）

### A-DD1｜SWE1 -025~-028 之 HK/LATAM 歸屬矛盾（上游兩源互斥）

- CFTS 側：`-132`/`-133`（速度 5/3 MPH 門檻）位於 **LATAM Market Regulations**
  章（Heading `-130`，適用閘 `-131` Information「apply to the LATAM market only」）。
- SWE1 側：`-025`~`-028` 之 source 欄配 **`-125`（HK 閘）**＋`-132`/`-133`，
  且四列之 Requirement Description 與 Verification Criteria 原文自書
  「When Country_Code is Hong Kong」。
- 兩讀法互斥：同一對門檻條文，CFTS 結構歸 LATAM、SWE1 內文歸 HK。
- **暫行處置（R-13 家族，不代裁）**：037 為生成主驅動，TC 內容逐字沿 037；
  矛盾登 **DR-DD1** 向上游確認「-025~-028 之市場條件應為 HK 或 LATAM，
  或兩市場皆須（若皆須，LATAM 側缺獨立 leaf）」。
  DR 回覆前 framework 之該 4 leaf 歸組**暫掛**（見 §三 Layer 2 註）。

### A-DD2｜狀態命名兩制（事實登記，非錯誤）

CFTS 用 `"Locked"/"Unlocked"`（Lock Out State variable）；SWE1 之
Verification Criteria 用 `RESTRICTED/NOT_RESTRICTED`（DD Service 對
Listener 之 callback 值）。屬系統層變數名 vs 軟體層列舉之對映，
兩者各於其層自洽。TC 之 ER 用詞依裁定 Q4 定錨後統一，不得混用。

### A-DD3｜CFTS -120/-121 描述含 `_x000D_` 斷行殘留

verbatim 摘句（test_item 上半）時做 CR 殘留正規化（`_x000D_` → 換行），
屬排版正規化家族（R-4 同族），不改字。

---

## 三、framework 草案（Layer 1/2/3，待 Pei 裁後鎖 `framework.md`）

### Layer 1 — Test Group（Q2 待裁）

提案：`Driver Distraction`（取 SWE1 Project Name 欄實值）。
備選：`Driver Distraction Lockout`（CFTS 章名）。HMI spec 題名
`Driver Lockout` 不採 —— 037 為生成主驅動，Layer 1 從其命名。

### Layer 2 — Test Set 草案（六組，28 leaf 全分掛）

| # | Test Set | leaf | 範圍 |
|---|---|---|---|
| 1 | `Body Off Init` | 001–002 (2) | 出眠初始化：Lock Out State 復位、process 終止後冷啟 |
| 2 | `Speed Monitoring` | 003–008 (6) | $Speedometer$ 監看、≥5MPH 上鎖、≤3MPH 解鎖、訊號失效 |
| 3 | `Lockout Enforcement` | 009–012 (4) | Locked 態之存取阻擋、使用中之強制退出 |
| 4 | `Lockout Tables` | 013–016 (4) | Lockout Table 所列 feature 之逐項套用 |
| 5 | `Hong Kong Market` | 017–024 (8) | Country_Code=HK：自排 P 檔閘、手排手煞閘、輸入失效 |
| 6 | `Market Speed Gating` | 025–028 (4) | 5/3 MPH 門檻於市場條件下（**歸屬待 DR-DD1**） |

註：組 6 之名暫以市場中立措辭佔位。DR-DD1 若裁 HK → 併入組 5
（Hong Kong Market 成 12 leaf，六組併五組）；若裁 LATAM → 更名
`LATAM Market`。**組名於 DR 回覆前不寫入工作簿任何列。**

反模式自查（IN §4.1.3）：28 leaf 分 6 組，平均 4.7 leaf/組；最小組 2 leaf
（Body Off Init）為真 outlier（唯一之電源域行為），非逐 RD 立組；
無 Misc/Unclassified。

### Layer 3 —— 規格章節分組（僅入 framework.md，不入工作簿）

以 CFTS Heading 母號為座標（上游正式欄逐字值，可驗）：

| Layer 2 | CFTS Heading | 涵蓋 FR |
|---|---|---|
| Body Off Init / Speed Monitoring / Lockout Enforcement | -110 Driver Distraction Lockout (SR23+) | 113–118 |
| Lockout Tables | -119 Driver Distraction Lockout Tables | 120–121 |
| Hong Kong Market | -123 Hong Kong Market Regulations | 125–129 |
| Market Speed Gating | -130 LATAM Market Regulations（**依 CFTS 結構**；SWE1 內文歸 HK，見 A-DD1） | 132–133 |

範圍外之 CFTS 內容（Volume、Personalization 等 134 條 FR）**不屬本 feature**：
SWE1 未分解即不生成（bed_lowering R-BLM6 同型之先例；惟本案之未分解者
明顯屬他 feature 已有工作簿之範圍，非懸置項，不登 coverage gap）。
`-112`（適用性總則）與 `-136`（Out of scope，Embedded NAV）SWE1 未引，
recon 時列覆蓋台帳註記即可。

---

## 四、feature.yaml 關鍵值（草案，執行層落檔時逐鍵實測）

- `feature` / `test_group`：依 Q2 裁定
- `tc_id_format`：`newR1L-DD-{n:03d}`（Q3 待准；project 前綴權威 = 工作簿 D2，
  執行層自副本實測確認）
- `spec_mode`：`"D"`（looked up, never constructed）
- `spec_reference`：**IN §10.7(a) CFTS 家族** —— `CFTS022-{ObjectID}`，
  ObjectID 逐字查自 S2 `Basic Report` 之 7 位號欄（col F）。15 列全數有值，
  無 PENDING 需求。雙引列（HK 閘＋條文）之排列依 §10.7 一行一 ObjectID、
  升冪。**本 feature 不需 §10.7(b) override** —— 與 bed_lowering 之
  檔名級降轉不同型，勿沿用其 profile 條文
- `a03_report` 分頁名：`Analysis Report`（標準命名，intake sniffer 應命中；
  header row 8、資料 row 9 —— 與 bed_lowering 家族之 row 10 不同，
  執行層 intake 時以實測為準）
- 四庫（LID/DBC×2/PROXI）：**Q6 待裁**後補 `reference` 節

---

## 五、執行層任務（Phase 0/1）

- **T1**：`scripts/new_feature.py` 開 `driver_distraction` 標準骨架
  （templates 複製件不得覆蓋本包；`docs/handoff/01_feature_open.md` 已在場）
- **T2**：Pei 置入四原件（S1–S4；S5 是否入 `inputs/` 依 Q5）後，
  逐檔驗型（`file`＋magic）並重算 sha256，回填 `feature.yaml` `reference` 節
- **T3**：`scripts/intake.py` → `scripts/recon.py`；recon assertions 宣告
  `functional_requirement_count: 28`（本包實測值；其餘鍵未實測不宣告，
  R-VC9 家族）
- **T4**：SWE1 28 leaf 逐列抽 Requirement Description 全文入
  `data/leaf_inventory.tsv`（欄位形制沿 bed_lowering）；`_x000D_` 正規化
  於此步做並留原文欄
- **T5**：上繳包 01 附：T2 驗型結果、T3 assertion 輸出、
  T4 之 28 列清單、未結 DR 清單（DR-DD1）、獨立自評

---

## 六、待 Pei 裁（Q1–Q6）

| Q | 事項 | 提案 |
|---|---|---|
| Q1 | slug | `driver_distraction` |
| Q2 | Layer 1 / test_group | `Driver Distraction` |
| Q3 | tc_id_format | `newR1L-DD-{n:03d}` |
| Q4 | **ER 之斷言錨層級**：SWE1 之 VC 以「Listener receives RESTRICTED callback」表述（軟體層），SWQT 可觀察者為 HMI 現象（鎖定 feature 之 UI 態、popup）或 log。ER 錨定於何者 | 提案：HMI 現象為主錨；callback/log 表述之 leaf 依 R-BLM13 同族「reaction presence」降階處理，細則入 profile |
| Q5 | S5（SYSAD）是否入 `inputs/` 並綁 reference | 提案：入，僅人讀參考，不入語料指紋 |
| Q6 | 四庫綁定：`$Speedometer$`/`$VC_Trans_Equipped$`/`$PresentGear$`/`$PARK_BRK_EGD$`/`$Country_Code$` 之 DBC/PROXI 對應本包來源未附 | 提案：沿 R-BLM11 乙案，綁 `vehicle_setting/inputs/` 四原件；對照缺漏屆時逐項登 DR |
| — | DR-DD1（A-DD1 之上游查詢）文稿於裁定後由分析層擬出，Pei 發送 | — |

---

## 七、量測條件揭露（R-G8）

- 本包全部數字自分析層 Project 附件（轉換副本）以 openpyxl
  `read_only=True, data_only=True` 實測；S1 資料列判準 = A 欄非空
  （28/28 帶 `SWE1-RA-Driver_Distraction-` 前綴，無雜列）。
- S2 類別計數判準 = col K（`SYS2 分類 Category`）逐字值。
- 追溯表之 source 配對 = S1 col B 原值按 `\n` 切分，未做任何推定。
- 分析層副本與 Pei 原件之同一性**未驗**（副本為轉換型態，sha 不可比）；
  T2 之驗型與 sha 為此缺口之補位。
