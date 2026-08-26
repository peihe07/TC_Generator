# Audio Management — 下放包 01：Intake 勘察與立案裁定

- Feature slug：`audio_mgmt`（R-AM4 併准）
- 日期：2026-08-26
- 裁定人：Pei（Q1–Q6 已裁，本包為裁定落檔）
- 程序位置：Phase 0（Intake）＋ Phase 1（Recon）合併完成

---

## 一、來源檔案分類表（R-AM1：取代 sniffer 輸出）

sniffer（`scripts/intake.py`）對本 feature 之輸出**作廢**，以下表為 Phase 0 正式分類。
作廢理由：三件來源為偽裝格式（見「格式異常」欄），另兩件 CFTS 匯出無
`Analysis Report` 分頁，sniffer 之分頁名嗅探必然誤判（同 Display R-DM5 型）。

| # | 檔案 | 實際格式 | 分類 | 格式異常 |
|---|---|---|---|---|
| 1 | `SWE_1_Audio_Management_Pending_For_Review.xlsx` | xlsx，4 分頁（Part 01–04） | **SWE.1 分析報告（驗證範圍主驅動）** | 分頁名非標準（無 Analysis Report） |
| 2 | `R1LR_Atl-H_25PI3_5_Multimedia_-_Radio_and_Audio_CFTS_019_Audio_Management_20250910_1235.pdf` | **純文字**（Requirement Specification Report 匯出，非 PDF） | 母 spec 原文（Part1+Part2 全文），章節 ObjectID `{48xxxxx}` 共 234 個，範圍 4865821–4867749 | 副檔名 .pdf 與內容不符 |
| 3 | `CFTS019AudioManagementPart1_released_20260415.xlsx` | xlsx，Polarion Basic Report | **錨源（Q2 裁定）**：245 物件（101 FR / 109 Info / 33 Heading / 2 OOS），OID 4865821–4866154 | 無 Analysis Report 分頁 |
| 4 | `CFTS_019_Part2_All_AcceptedExceptDTCrework.xlsx` | xlsx，Polarion Basic Report | **錨源（Q2 裁定）**：566 物件（347 FR / 3 NFR / 142 Info / 105 Heading / 4 OOS），OID 4866155–4867787 | 無 Analysis Report 分頁 |
| 5 | `SYS2CFTS019PF_R1LR_v1__RadioPerformanceStandard_Part1_Released.xlsx` | 標準 035 Analysis Report | 範圍外參考（Q3）：29 需求，SYS-RA-AMM-1119 起 | 無 |
| 6 | `SYS2CFTS019R1_Series_Radio_EQ_Document_Version_1_8_AcceptedoneRAR.xlsx` | 標準 035 Analysis Report | 範圍外參考（Q3）：40 需求，SYS-RA-AMM-1155 起 | 無 |
| 7 | `SYS2CFTS019CIP_Radio_DSPPP_Accepted5reqsRARs.xlsx` | 標準 035 Analysis Report | 範圍外參考（Q3）：108 需求，SYS-RA-AMM-1191 起 | 無 |
| 8 | `FMWIFSM036A01_..._SWQT_AudioAACP_20260624.xlsx` | 標準 036 模板（表頭第 9 列，34 欄） | 舊 TC 簿，**僅參考不續寫**（Q1 裁定）：既存 50 條 TC（`NR1L_AudioMgnt_001`+），錨定 `SWE1-PROJ-203` | 內容非 canon（中文 AC 式 test_item） |
| 9 | `SYS3_CFTS019-Audio_FM-WI-FSM-011-A01_..._SYSAD.docx` | **純文字/markdown**（非 docx） | 輔助參考：37 頁架構設計，引 66 個 SYS-RA-AMM | 副檔名 .docx 與內容不符 |

---

## 二、勘察發現（F1–F6，全數實測，非概估）

**F1 — 錨定橋斷裂（最嚴重）。** SWE.1 全部 318 葉追溯至 SYS-RA-AMM-082..1111。
附案三本 SYS2 分析報告自 SYS-RA-AMM-1119 起跳，覆蓋 082..1111 之
SYS2 CFTS019 主體分析報告未在案。兩本 CFTS Basic Report 之
`SYS2 Sys-RA-Feature-ID` 橋接欄實測 0/811 填寫。
SWE1_AMM ↔ CFTS ObjectID 之間無任何正式欄位可走。→ Q2 裁定、DR-AM1。

**F2 — SWE1_AMM_076 ID 碰撞。** Part 01 尾（來源 SYS-RA-AMM-242，
Steering Wheel Information Volume Control）與 Part 02 首（來源
SYS-RA-AMM-246，Information Source Mute Routing Configuration）
各有一條 076，為上游真實編號缺陷。318 葉實為 **317 個唯一 SWE ID**。
來源 ID（SYS-RA-AMM）318 個全數唯一，無其他碰撞。→ Q4 裁定、DR-AM2。

**F3 — 覆蓋方向缺口。** PF（29）＋EQ（40）＋DSPPP（108）共 177 條
SYS-RA-AMM-1119+ 需求，SWE.1 報告零覆蓋。→ Q3 裁定為範圍外，
強制揭露表見 §六。

**F4 — sniffer 誤判。** 見 §一，R-AM1 處置。

**F5 — 036 舊簿內容。** 50 條舊 TC 錨定 Projection 需求命名空間
（SWE1-PROJ-203），與本案 SWE1_AMM 無交集；格式非 canon。→ Q1 裁定。

**F6 — SWE.1 Sub Categorization 不堪為 Layer 2。** 70 群、同義漂移嚴重
（Volume Control / Volume Management / Volume Control Interface 並存；
Mute Control / Mute Management 並存）。降為 Layer 2 歸位之次要訊號。

---

## 三、裁定紀錄（Q1–Q6，Pei 2026-08-26 裁）

### R-AM3（Q1）：工作簿基底 = BLANK + R-G1 模板
新 TC 簿自 R-G1 模板空白起建。既存 `SWQT_AudioAACP` 簿之 50 條舊 TC
原封不動、不續寫、不回修，僅作參考。理由：舊 TC 錨定 SWE1-PROJ-203
（Projection 需求命名空間），與本案 SWE1_AMM 命名空間無交集，混簿將
污染追溯；且舊內容為中文 AC 式 test_item，非 canon 格式，續寫將迫使
單簿雙制。

### R-AM2（Q2）：錨源 = 兩本 CFTS Basic Report
specification_reference 之錨定物件池 = 檔 3、檔 4 兩本 Basic Report 之
Source Requirement ID 欄（Polarion 7 位 ObjectID），格式依 IN §10.7(a)
`CFTS019-{ObjectID}`。因正式橋接欄全空（F1），對位方法為：
SWE.1 需求內容（Title + Description）↔ Basic Report Description 內容對位，
**能唯一對位者**取該列 ObjectID 為錨；**對位不到或一對多者**填
`PENDING: DR-AM1 SWE1-to-CFTS ObjectID mapping unresolved for this leaf`
並逐條登記，不硬配、不取語意相近他列代入（IN §8.4.1 / R-13 同理）。
內容對位屬 Pei 本裁定明文授權之例外，僅限本 feature、僅限此橋；
DR-AM1 之上游正式對照表到位後，全簿回填校正。

### R-AM5（Q3）：驗證範圍 = SWE.1 之 318 葉
範圍 = SWE.1 報告全部 318 列（317 唯一 SWE ID，含 F2 碰撞之兩列均入範圍）。
PF / EQ / DSPPP 之 177 條需求範圍外，不擅自擴編，以 §六 揭露表列為
coverage gap，交付時隨簿揭露。

### R-AM6（Q4）：SWE1_AMM_076 碰撞之交付欄處置
兩條 076 各自出 TC。交付簿 `Requirement or Design ID` 欄**均照抄
`SWE1_AMM_076`**（上游僅存在此字串；自造 `076a/b` 寫入交付欄 = 造 ID，
追溯反斷）。兩組 TC 之區分由各自 test_item 內容與 specification_reference
（錨至不同 CFTS 物件）承載。「076a（=SYS-RA-AMM-242）／076b（=SYS-RA-AMM-246）」
代號僅限分析層文件內部追蹤使用，禁入交付欄。DR-AM2 上呈請上游改號，
改號後交付欄隨改。（Pei 於 Q4 提問後說明，無異議即照此辦。）

### R-AM7（Q5）：req_id 欄格式
`Requirement or Design ID` 欄照抄 SWE.1 原文底線式 `SWE1_AMM_{NNN}`，
不改寫為連字號、不增删前綴。

### R-AM1（Q6）：Phase 0 人工分類
sniffer 輸出作廢，§一分類表為正式 Phase 0 產出。slug = `audio_mgmt` 併准。

---

## 四、Framework 草案（IN §4.1；鎖定前置條件見 §七）

**Layer 1（Test Group）**：`Audio Management`

**Layer 2 / Layer 3**（CFTS 1.3.x 章節 ∩ SWE.1 子類收斂；葉數為映射概估，
鎖定須經 317 葉逐條歸位全表掃描，不憑概估出貨）：

| Test Set（Layer 2） | Layer 3（CFTS 章節，不入簿） | 概估葉數 |
|---|---|---|
| Audio Sources | 1.3.1.1–1.3.1.3 | ~40 |
| Tones and Alerts | 1.3.1.4–1.3.1.6, 1.3.2.6 | ~45 |
| Audio Processing | 1.3.2.7–1.3.2.9, 1.3.2.15, 1.3.2.17–1.3.2.22 | ~50 |
| Volume Control | 1.3.2.10–1.3.2.12 | ~40 |
| Surround and Fade | 1.3.2.13, 1.3.2.16 | ~20 |
| Source Arbitration | 1.3.3.1–1.3.3.4, 1.3.3.15–1.3.3.19 | ~55 |
| Mute Requests | 1.3.3.5–1.3.3.7, 1.3.3.12 | ~30 |
| Projection Audio | 1.3.3.11, 1.3.3.14 | ~10 |
| Power and Persistence | 1.3.2.2–1.3.2.4＋Volume Restoration 群 | ~20 |
| Logistic Mode | 1.3.5.1–1.3.5.2 | ~8 |

註 1：1.3.4（Arbitration Conditions Tables）為條件表素材，隨 Source
Arbitration 引用，不獨立成集。
註 2：1.4（Diagnostic）、1.5（Configuration）章之葉需求歸位於逐條歸位時
判定；SWE.1 子類含 Diagnostics（1）、Persistent Storage（10）等，
預期多數落入 Power and Persistence 或既有集，如需增集於歸位時提裁。
註 3：`Projection Audio` 與舊簿同名 Test Set，但本簿自 SWE1_AMM 命名空間
錨定，與舊簿無追溯交集，不構成衝突。

---

## 五、未結 DR 清單（IN §8.4.3；隨每包上繳）

| DR | 內容 | 狀態 | 送出日 |
|---|---|---|---|
| DR-AM1 | SYS-RA-AMM-082..1111 ↔ CFTS019 ObjectID 正式對照表缺失（SYS2 CFTS019 主體分析報告未在案；Basic Report 橋接欄全空）。請上游提供對照或補件 | 待 Pei 送出 | — |
| DR-AM2 | SWE1_AMM_076 編號碰撞（SYS-RA-AMM-242 與 -246 同號）。請上游改號 | 待 Pei 送出 | — |

DR 送出屬 Pei；分析層僅代擬。

---

## 六、Coverage Gap 揭露表（R-AM5 附件，交付隨簿）

| 來源文件 | 需求數 | SYS-RA 範圍 | SWE.1 覆蓋 | 處置 |
|---|---|---|---|---|
| PF-R1L-R（Radio Performance Standard Part1） | 29 | AMM-1119+ | 0 | 範圍外，揭露 |
| Radio EQ Document v1.8 | 40 | AMM-1155+ | 0 | 範圍外，揭露 |
| CIP Radio DSPPP v3.9 | 108 | AMM-1191+ | 0 | 範圍外，揭露 |

---

## 七、產能計畫

- 量體：317 唯一葉 × sibling 拆分係數估 1.3–1.6 ≈ **410–500 TC** ≈ 9–10 批
  （50 列/批，3 批一繳，IN 慣例）。
- 加速：
  1. SWE.1 之 Verification Criteria / Verification Method 欄品質良好
     （已含步驟雛形），prompt builder 直接注入，省首輪行為化往返。
  2. 三批乾淨後啟 R-G14 綠色通道自動續批。
  3. 批次按 Layer 2 排（sibling 同批、setup 共用），首發 **Source
     Arbitration**（P0 密度最高，早暴露 DR）。
  4. 錨定不卡批：R-AM2 內容對位＋PENDING 並行，DR-AM1 回件後末站統一回填。
- 阻塞面已清：Q1–Q6 全裁。唯一前置 = **02 包：317 葉逐條歸位表**
  （framework 鎖定），完成即開 Batch 1。

## 八、下一步

1. 分析層產出 `02_framework_assignment.md`（317 葉逐條歸位 + framework
   鎖定版 `framework.md`）→ Pei 過目。
2. 執行層依 R-G1 模板建新簿 scaffold（`scripts/new_feature.py`）。
3. Batch 1（Source Arbitration 首 50 葉）下放。
