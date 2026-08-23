# 上繳 61 —— VF230 進場：裁決落檔、素材補入、leaf 母體、Layer 2 候選

執行層寫入。依據：`docs/handoff/61_vf230_intake.md`（P0/P1 指示）。canon §8.2 六節。

**本輪未生成任何 TC，未寫回任何工作簿，未執行任何 git 寫入性操作。**
Part 1（CFTS044）之交付內容、`framework.md`、既有批次產物**一律未觸及**
（W-106 之回歸證明見 §5）。

> **編號說明**：61 包指名本檔為 `docs/upstream/61_vf230_intake.md`，
> 而 `docs/upstream/` 之既有序為**往返輪次**（現至 34）。本檔依指名落檔，
> 其 `61` 為**下放包號**，非往返輪次 —— 此為 `docs/upstream/` 內唯一之例外。
> 該不一致與 A-VS124 同源，一併待裁。

---

## 1. 本輪之交付

| # | 61 包工單 | 狀態 | 產物 |
|---|---|---|---|
| 1 | W-102 素材驗核 | **完成** | `inputs/`（+13 檔）、`inputs/INPUTS.sha256`（16→29 列） |
| 2 | W-103 leaf 母體 | **完成** | `data/vf230_leaves.tsv`（619 leaf）、`data/_vf230_w103.json`、`scripts/vf230_leaves.py` |
| 3 | W-104 Test Group | **停下（如令）** | 三源實測見 §6；`profiles.vf230.test_group = null` |
| 4 | W-105 Layer 2 候選 | **完成（待裁）** | `docs/reports/vf230_layer2_candidates.md`、`scripts/vf230_layer2.py` |
| 5 | W-106 `feature.yaml` | **完成（含回歸證明）** | `feature.yaml`、`docs/reports/w106_regression.md` |
| 6 | W-107 DR 波及判定 | **未執行** | 見 §7 |
| 7 | 裁決落檔 | **完成** | `RULINGS.md` +R-VS59–63、`DATA_REQUESTS.md` +DR-28、`ANOMALIES.md` +A-VS124–128 |
| 8 | `INDEX.md` 補齊 | **部分完成** | 見 §8 |

**Pei 於 2026-08-23 之兩項現場裁定**：(a) R-VS61 之搬檔限制**單次免除**，
授權執行層代為補入素材；(b) 61 包 §6 第 3–5 項之 REF 素材**得由 CFTS044 代用**
（落為 R-VS63）。二者已逐字落檔。

---

## 2. W-102 —— 素材驗核

**量測條件**：`cp -n` 自 `…/Vehicle Settings/VF230_V1_R5/` 一層複製
`FM-WI-FSM-03*.xlsx` 與 `C-VF230*.doc` 入 `inputs/`；逐檔以
`shasum -a 256` 對來源與副本各取一次比對。

```
複製            13 檔（11 份 037 ＋ 036 ＋ spec）
與來源位元相同   13 / 13     mismatch 0
INPUTS.sha256   16 → 29 列（CFTS044 區塊 16 逐字未動；VF230 區塊 13 另立）
shasum -a 256 -c   29 / 29 OK（exit 0）
```

`#` 起首之區塊註解不影響 `shasum -c` 之驗核。

**SYSAD（61 包 §6 第 6 項，「未比對 hash」）**：已比對，**兩份逐位元相同**
（`469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200`），
故未重複複製。該待辦關閉。

**`output/` 三檔（R-VS62）**：**未複製入 `inputs/`**，本輪未取用、未對帳。

---

## 3. W-103 —— leaf 母體

**量測條件**：11 份 037 逐份獨立解析，**不先合併**；leaf 判準沿用
`recon.py` 之既有實作（Categorization 正規化後以 `functional` 起首者為 leaf），
**未引入 ID 後綴啟發式**（R-C3 明禁）。總數自各份重算（canon §5a），
並以 `assert` 驗合併後筆數與逐份加總相符。

| 037 分報告族群 | 分頁 | 列 | leaf | heading | other |
|---|---|---:|---:|---:|---:|
| Trailer_Name - Max_Power_Level_Report | Analysis Report | 143 | 131 | 12 | 0 |
| Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense | Analysis Report | 118 | 99 | 19 | 0 |
| Time_Date_Autodoor_Camera_features | Analysis Report | 94 | 79 | 15 | 0 |
| 6 Aux Switches, SWITCH 1 Power Mode and E-Save | Analysis Report | 94 | 64 | 30 | 0 |
| Illuminated_Approach - Trailer_Number_Report | Analysis Report | 66 | 57 | 9 | 0 |
| Suspension_Service_Mode - Headlights_with_Wipers | Analysis Report | 62 | 52 | 10 | 0 |
| Cornering Lights_lane_features | Analysis Report | 58 | 49 | 9 | 0 |
| Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode | Analysis Report | 44 | 35 | 9 | 0 |
| SWITCH_1_Type - SWITCH 4 Hold_Last_State | Analysis Report | 32 | 24 | 8 | 0 |
| Pressure_Unit , Power_Unit And Torque_Unit | **Sheet1** | 20 | 17 | 3 | 0 |
| Daytime_Running_Light And Headlights_Off_Delay | **Sheet1** | 14 | 12 | 2 | 0 |
| **TOTAL（自各份重算）** | | **745** | **619** | **126** | **0** |

```
相異 swe_id        619（跨份重複 0）
Categorization     Functional Requirement 619 ／ Heading 126 ／ 其他 0
src_ref 前綴       SYS-RA-VF230_V1-  745 / 745（無雜前綴）
src_ref 數值域     524 – 2665，745 個相異值，區間內缺號 1397
```

**兩份分頁名為 `Sheet1`**（其版面與其餘 9 份逐欄相同）—— 見 A-VS126。
以分頁名定位會靜默漏收該 2 份之 29 leaf；本輪已改為**以版面定位**。

**未經跨源驗核**：VF230 缺 SYS2（DR-28），故 619 之 Functional/Heading
判定**單源自 037**。「Categorization 僅二值、0 other」只證 037 內部一致，
**不證其與上游相符**，不以之冒充驗核。

**R-VS59 第 3 項之末值**：VF230 尚無 TC 產出，**本輪無值可報**。

---

## 4. W-105 —— Layer 2 候選（待裁，`framework.md` 未動）

**量測條件**：spec 之 Heading 段落（`python-docx`，`Heading N` 樣式）
∩ 037 之 Requirement Title 簇；交集判準為正規化後**全等**，不做子字串容錯。

```
spec Heading      192（層級分布 L1:1 L2:17 L3:34 L4:11 L5:99 L6:30）
037 Title 簇      106，涵蓋 619 leaf
交集              exact 103 ／ 無對應 3
```

**交集本身極強（103/106），但不產生可用之 Layer 2 粒度** —— 99 個 L5 中
**95 掛於同一 L4 章**，致粒度塌成 603 leaf（97.4%）對 16 leaf（2.6%）之二分。
canon §4.1.2 步驟 2 之假定（spec 目次可作切分軸）於 VF230 不成立。見 A-VS127。

**另備之切分源（037 之 11 份分報告族群）**：12–131 leaf，中位 52，
較上者均勻、較 106 簇為粗。**本層建議以此為起點，惟不決。**

**未決之殘項**：無對應之 3 簇（`E-Save` 6 leaf、`Rear Guidance Lights with
Cargo Lights` 5、`CHMSL CAMERA DYNAMIC CENTERLINE` 5）之 Layer 2 歸屬無 spec 依據；
另有 2 簇（`Speed Unit`／`Charge Power Level`）於 spec 目次各有兩處同名章而分屬
不同 L4 分支，歸屬歧義。

**未自創 Layer 2 標籤**（canon §4.1.2 步驟 3 明令用 spec 自身之 section ID）。

---

## 5. W-106 —— `feature.yaml` 多 workbook（含回歸證明）

61 包 §4.1 之「擇一」取**前者**：保留 `workbook` 鍵指向 CFTS044，新增具名鍵。

新增 `paths` 鍵 5：`workbook_cfts044`／`workbook_vf230`／`a03_report_vf230`／
`spec_pdf_vf230`／`sys1_export_vf230`（後者為 `null`，DR-28 覆後方填）。
新增 `profiles` 區塊 2：`cfts044`／`vf230`。

**R-VS59 之 `seq: "B"` 落於 `profiles.vf230.columns`，不在共用之
`workbook.columns`** —— 後者為兩本共用，寫入其中會使 CFTS044 之凍結 B 欄
進入寫回範圍，違反 R-VS59 第 2 項。`profiles.cfts044` 刻意不設 `seq`。

**回歸證明**（`docs/reports/w106_regression.md`）：以暫存副本各跑一次
`scripts/recon.py`，`feature.yaml` 分別為 git HEAD 版與改後版，其餘一致。

```
RECON.md           差異僅 `7a8,11` 之純新增四列（新宣告 input 之 sha256）
                   無修改、無刪除
DECISIONS.new.md   差異僅 `4 present` → `8 present`
data/ 產物         逐檔相同
recon 摘要         state=BLANK, leaves=46, sections=0, targets=46（前後相同）
```

→ **Part 1 之每一行 recon 輸出位元未變**；改造為純加性。

**波及面較 §4.1 所設想小**：`features/vehicle_setting/scripts/` 之 27 支腳本
**無一讀 `feature.yaml`**（皆為硬路徑一次性腳本）；消費者集中於 repo 根之
`scripts/feature_config.py`／`recon.py`／`intake.py`。

---

## 6. W-104 —— Test Group（停下項，不決）

61 包 §4.3 只問「是否等同 `Vehicle Setting`」，即預設二選一。**實測有三個
互異之候選**（A-VS128）：

```
(a) spec 之 L1 Heading（逐字）   Vehicle Setup Management [VF230_V1_]
(b) 037 之 Sub Categorization    Vehicle Setting Management (VSM)     388  62.7%
                                 Vehicle Setup Management(PSVF230)     76
                                 Vehicle Controls Management by VP (VC) 70
                                 Vehicle Control                        51
                                 Camera                                 25
                                 CAN (including VHAL)                    5
                                 Time_and_Date (PSCFTS015)               4
(c) feature.yaml 現行 test_group  Vehicle Setting
```

依 **R-C6**（feature 身分取自 spec 模組名）應取 (a)，惟其逐字含 `[VF230_V1_]`
尾綴，**截去與否本身即一項裁定**。`profiles.vf230.test_group` 落為 `null`
並附三源之註 —— **不以 Part 1 之值預填**，預填會使「未裁定」與「已裁定為同值」
不可分辨。

**請裁**：Test Group 之值，及 (a) 之尾綴處置。

---

## 7. W-107 —— DR 波及判定（未執行）

61 包 §4.6 令「VF230 之 recon 完成後，逐 DR 判定其提問是否落在 VF230 之 leaf 上」。

**本輪未執行，理由具名**：其前提為「VF230 之 recon 完成」，而 recon 之
`survey_workbook` 對 VF230 無對應輸入（036 為 BLANK，§4.5 已令不得以之推得
覆蓋率），`build_outline_map` 亦需 SYS2（DR-28 未覆）。本輪只到 leaf 母體，
**未跑 VF230 之 recon**。

在無 recon 之下逐 DR 判定，其依據只剩 leaf 之 token 掃描 —— 該做法可行，
但屬**本輪未獲指示之方法選擇**，故不逕行。**待下輪指示**：是否以
`data/vf230_leaves.tsv` 之 token 掃描替代 recon 作為 W-107 之輸入。

**未以 DR-15 為由阻塞 VF230 之 P1**（§4.6 之禁令已遵守）。

---

## 8. `INDEX.md` 補齊 —— 部分完成，未補之範圍具名

回填 **33 列**（往返 NN 02–34），由 `scripts/index_backfill.py` 機械產生。

**首版有一項錯誤，已更正並記錄**：INDEX 之 NN 為**往返輪次**
（`docs/upstream/` 之序，至 34），而 handoff 之**包號**已至 61 ——
**兩套獨立計數**。首版以 NN 相等配對，造出 **27 組假對應**；
改以各上繳前段之**逐字引用**（`docs/handoff/…md`）解出真對應。
標 ⟨依自述往返 NN⟩ 者為僅自述「往返 NN = NN」而未逐字引用者，其對應為推得。

**未回填之範圍（具名）**：

- **「日期」欄**：全 33 列未填。各上繳未一律於固定位置載日期，機械抽取
  會誤取內文之量測日。
- **「結果」欄**：全 33 列未填。其需逐輪之判斷（哪些 W 完成、哪些未執行），
  非機械可得；實質以各列所連之上繳文件為準。
- **「新條文」／「新 anomaly」欄之語意**：判準為「該輪之下放或上繳為
  `docs/` 內**首次提及**該編號之文件」，**非「該輪裁定成立」** —— 一條文
  可先於某輪被提及而於後輪方裁定。
- **25 件下放包無對應上繳**（補篇、指令書，或其輪次尚未上繳），已另表列出。

---

## 9. 本輪新開之 anomaly（5）

| # | 一句話 |
|---|---|
| A-VS124 | 61 包所開之 W-102–W-107 與 DR-27 與 Part 1 既有編號全面撞號 |
| A-VS125 | `C-VF230_V1_R5_PDT27.doc` 實為 OOXML，§6 第 2 項「需轉檔」之前提不成立 |
| A-VS126 | 11 份 037 之分頁名不一致，2 份為 `Sheet1` —— 以分頁名定位會靜默漏 2 份 |
| A-VS127 | canon §4.1.2 之交集法於 VF230 不產生可用之 Layer 2 粒度 |
| A-VS128 | VF230 之 Test Group 之三個來源互不相同 —— W-104 有三個候選而非二個 |

---

## 10. 撞號 —— 本輪最需裁定者（A-VS124）

**DR 已逕行改號**：61 包 §7 之草稿編為 DR-27，而 **DR-27 已為 37 輪 W-105
之唯一性提問所用**（成對 A-VS119）。DR 為對外提問，同號兩義會使覆文無從對應，
其代價高於改號 —— 故本件落為 **DR-28**。61 包 §7、§8 之「DR-27」一律指本件。

**W 號未改，待裁**。Part 1 已用至 **W-109**，其中 W-104–W-107 於 60、61 輪
各有所指；W-102／W-103 為空號。**建議改編為 W-110–W-115**：

```
W-102 素材驗核        → W-110
W-103 leaf 母體       → W-111
W-104 Test Group      → W-112
W-105 Layer 2 候選    → W-113
W-106 feature.yaml    → W-114
W-107 DR 波及判定     → W-115
```

本輪產物一律以中性檔名落檔（`scripts/vf230_leaves.py`／`vf230_layer2.py`／
`index_backfill.py`），不寫入撞號之 W 號。

**另**：61 包 §4.2 標「處置（W-103）」而 §5.4 之 Layer 2 為 W-105；
§4.5 標「處置（W-105）」而 §5.2 之 leaf 母體為 W-103 ——
**61 包 §4 與 §5 之 W 號互不一致**，本層以 §5／§8 之清單為準。

---

## 11. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，三項。**

1. ~~**VF230 之 619 leaf 未經任何跨源驗核**（§3）。~~
   **已於同輪稍後解決，見 §12** —— 該判斷本身即為錯的：可用之跨源
   （035 SYSRA）當時已在 `inputs/` 內，本層未察。此為 A-VS131。

2. **`output/` 三檔未對帳**（R-VS62 允其用於交叉比對）。其
   `fw036_vf230_from_fw037_functional_requirements.xlsx` 之列數與本輪之 619
   是否相符**未測** —— 該比對不需新素材，本輪未做是**範圍選擇**，非受阻。
   若相符，可作為 619 之弱佐證；若不符，須登記 anomaly。**建議下輪納入。**

3. **037 之 `Verification Criteria`／`Verification Method` 兩欄未取用**。
   實測 **619 / 619 leaf 之 `Verification Criteria` 皆非空（100%）**。其與 TC 之
   `expected_result` 之關係**本輪未查**。Part 1 之既有作業是否曾取用該二欄，
   本層未回查 —— 若 Part 1 未取用而 VF230 之上游填得較完整，
   **可能存在一個未被使用之權威來源**。

**另有一項非「未驗」而是「不可驗」**：spec 之 `.doc` 雖可直讀，其
**目次與 037 之 leaf 之逐條對應（Layer 3）本輪未建**，因 Layer 2 未鎖。
Layer 3 依 canon §4.1.2 步驟 3 須待 Layer 2 核可後方能作。

---

## 12. 補篇（同輪稍後）—— 跨源驗核完成，DR-28 之前提作廢

Pei 於 2026-08-23 另補入兩檔（61 包 §6 之清單外），本層據以複驗，
結果**推翻本上繳 §11 第 1 項之自我判斷**。

### 12.1 兩個補入檔之處置

| 檔 | 處置 |
|---|---|
| `C-VF230_V1_R5_PDT27.docx` | 與 `.doc` **內容逐字相同**（段落 3954／表 6／Heading 192／全文 sha1 `5096965efbec`），轉檔未帶新資訊。`paths.spec_pdf_vf230` **維持指向 `.doc`**（原始交付檔名）；`.docx` 另記為 `spec_docx_vf230` 留痕。**建議刪除，未刪**（刪檔屬 Pei 之權） |
| `FM-WI-FSM-035-A02_…_SYSRA_VF230_V4_Released.xlsx` | **即 DR-28 所缺之跨源**。落為 `paths.sysra_vf230` 與 `profiles.vf230.crosscheck` |

`inputs/INPUTS.sha256` 29 → **32 列**（另補一列：`HMI Settings List R1 SR25
Post R1L-R` 自 Part 1 時期即在 `inputs/` 而從未入清單）。
**實體檔 32 = 清單 32 列 = `shasum -c` 32 OK，0 非 OK** —— 至此 `inputs/`
之雜湊覆蓋為全量，無漏列。

### 12.2 跨源驗核結果（`docs/reports/vf230_crosscheck.md`）

035 之 `Basic Report` 與 CFTS044 之 SYS2 export **逐欄同型**
（`SYS2 Sys-RA-Feature-ID`／`SYS2 分類 Category`／`SYS2 VF章節`／
`SYS2 EE Architecture`／`SYS2 限定地區`），2655 列。

```
037 之 745 列          全數命中 035（未命中 0）
leaf   619 / 619       035 皆判 Functional Requirement    零錯配
                       反向錯配（037 Functional × 035 非 Functional）= 0
head   126             035 判 Heading 118 ／ Functional Requirement 8   ← 錯配
ASIL   命中 leaf 之 ASIL 全為 NA 或空 → VF230 無安全相關 leaf
```

**§3 之「619 單源自 037、未經跨源驗核」因而更正**：已驗，且**leaf 側零錯配**。

### 12.3 兩項新開之待裁（A-VS129／A-VS130）

**A-VS129 —— 8 列錯配，leaf 母體可能為 627**。037 判 `Heading` 而 035 判
`Functional Requirement` 者 8 列，其 037 條文逐字為 `The HMI layer shall
capture the customer selection for …`（5）與 `HW supplier shall notify the
IPC_VEHICLE_SETUP2.* signal via VHAL interface …`（3）—— **皆為需求形態**。
八者集中於 SWITCH 族（Power Mode／Type／Hold Last State），非隨機散布。
**本層未改母體**，`vf230_leaves.tsv` 維持 619。**請裁**。

**A-VS130 —— 037 只涵蓋 035 之 Functional 之 57.7%**。

```
035 之 Functional Requirement       1087
  為 037 之 745 列所收              627   （619 leaf ＋ A-VS129 之 8）
  未收                              460   42.3%
```

未收者全數 `ATL-Hi`、全數落於 `01.10.…`，**與已收者同一分支**；
同一章節內既有收錄亦有未收（`01.10.01.01.74` 收 14、未收 33），
故非「整章委派他 feature」之乾淨切分。

**非本層漏收** —— 全樹搜尋確認 VF230 之 037 分報告**僅此 11 份**，
未收之 460 條在上游尚無 SWE.1 分析。

**其後果須具名**：若 VF230 之交付範圍為「該 VF 之全部功能需求」，
現行 619（或 627）**只是 1087 之 57.7%**。交付時「覆蓋率」一詞將有
**兩個分母，答案相差 42.3 個百分點**。**請裁交付範圍之界**。

### 12.4 原生 SYS2 已尋得，未取用

`SYS2_VF230.xlsx` 位於 `9_ASPICE/SYS.2 System Requirements Analysis/
Z.QS YuShen 260423/08.[SYS2]Vehicle Settings/`（2626 列，schema 同型）。

**未複製入 `inputs/`** —— 其為 repo 既定根目錄之外之素材，補入須依
**R-VS61**（2026-08-23 之免除已明記為單次個案）。

且該檔**缺 037 之 6 個 `E-Save` leaf**（`SYS-RA-VF230_V1-2660`～`-2665`），
而 035 有、spec 目次無。**三源不一致**，DR-28 因而不撤回，僅降 Urgency 為 Low
並作廢其「影響」段。

### 12.5 本補篇之獨立判斷 —— 仍有該驗而未驗者

**有。** §11 之第 2 項（`output/` 三檔未對帳）與第 3 項（`Verification
Criteria` 未取用）**仍未做**。

**且本補篇本身揭示一個方法層之教訓**：§11 第 1 項之所以判錯，
是因為本層以**檔名族群**推得「素材有無」（找 `SYS2*`），而未問
「有無其他檔承載同一欄位」。同一失效在本輪已出現三次 ——
A-VS125（以檔名推得格式）、A-VS126（以分頁名推得版面）、
A-VS131（以檔名推得素材有無）。**三者皆為「以標籤代替內容」**。
