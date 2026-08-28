# 下放包 13 —— DR-DD3 結案（Pei 確認識別）、R-DD18（勘誤採認之界線）、DR-DD1/DD4 改稿、T19

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`12_batch_b1.md`
- 裁定：**Pei 2026-08-28 —— DD3 識別確認（解掉）；本包範圍（DD2 界線條文、DD1 文稿補 SYSAD 引文、DD4 縮問、B1 邊界格拘束）准落**
- 落檔註記：首寫於 MCP 逾時中失敗（get_file_info 驗 ENOENT），本檔為重寫，同稿
- 本包與包 12 之 T18 系列**併行**；T19 各項不阻 T18

---

## 一、SYSAD 掃描（分析層實測，本包各節之量測基礎）

- 素材：`features/driver_distraction/inputs/SYS3_…SYSAD_V1 (1).docx`
  （Pei 原件，真 docx；經 Filesystem 複製至分析層後以 python-docx 讀）
- 母體：段落 ＋ 表格列共 **2,075** 單元、281,916 字元；
  關鍵詞逐一 `re.finditer` 全文掃描
- 要點四：
  1. `VEHICLE_SPEED_THREE_MPH_TO_KMPH` —— 具名常數，**判定單位為 km/h、
     門檻由 MPH 換算而來**（DD4 第一問之答）
  2. speed hysteresis（lock/unlock 雙門檻）**三處**明文為 LATAM 之
     market-specific type（`ProcessorType4to6 … for LATAM`）；
     HK 邏輯走 parking brake ＋ gear（DD1 之補強證據）
  3. `Gear_Box_Type`／`VC_Trans` 於架構本體 **0 命中**
     （4 個 `VC_Trans` 命中全為文末轉貼之 CFTS 需求表）——
     DD5／DD6 之內部來源（LID／PROXI／二 DBC／SYSAD）**已窮盡**
  4. DDC 判定訂閱 VHAL 屬性 `VehicleSpeed`／`ParkingBrakeState`／
     `ShiftLeverPosition`（參考事實，不入 TC —— SYSAD 為 SWE.2 側，R-DD4 位階）

---

## 二、DR-DD3 —— **RESOLVED**（Pei 2026-08-28 確認識別）

| 項 | 處置 |
|---|---|
| DR-DD3 | 狀態 `ANSWERED-PENDING-CONFIRM` → **`RESOLVED`**；結案依據一行：`Pei 2026-08-28 確認 SR24 R1 MCT v1.6 即 LID 所指之 CIP MCT（取檔出處為其發佈渠道）` |
| **A-DD5** | **撤銷**（識別已確認，assumption 不復存在）；條目不刪，狀態改 `RESOLVED`，載撤銷依據 |
| `Country_Code = 91` | 由 assumption 轉**確定值**；profile §3 該列之「凡用及者標 `[ASSUMPTION A-DD5]`」**移除**（分析層自辦）|
| 影響 leaf | `-017`~`-028` 之 A-DD5 標記義務解除；**pilot 四則未用及，無回修** |

阻斷疊圖之變化：`-017`~`-024` 剩 DR-DD5＋DR-DD6（＋DR-DD2 於 021–024）；
`-025`~`-028` 剩 A-DD1 凍結。

---

## 三、R-DD18（勘誤採認之界線；Pei 准落於本包範圍）

```
R-DD18（上游書面勘誤之採認 —— 與「代換」之界線）

R-DD5 禁「查無者代以語意相近之他訊號」；R-13 禁以推定代缺件。
二者所禁為**自行推定**。下列情形不屬之：

(a) 上游於其自身文件內對同一疑問留有**書面回覆**者
    （本案：CFTS022 r129 之 SYS2 MD Feedback 欄逐字
    `The LID which is referred here is $PARK_BRK_EDG$`，
    並有 HARMAN Comments 之原始提問與 System-HW/SW 欄同載 EDG），
    得採認該回覆所指之名為**施加名**。此為 lookup ＋ 上游書面確認，
    非語意代換。
(b) 採認之界線：
    - **僅及於施加路徑**（Procedure／ER 之訊號名）。
      `test_item` 上半 verbatim 照 037／CFTS 原文（含 EGD），不改字。
    - 施加名之 CAN 對應**仍須自 LID 該列實測查得**（T19c），
      不得因勘誤成立而略過查證。
    - 規範欄未更正前，用及該施加路徑之 TC 標 `[ASSUMPTION A-DD2]`；
      上游正式更正（DR-DD2 之回覆）後撤。
(c) 本條不得反向援引：無書面回覆之「看起來像筆誤」仍依 R-DD5／R-13
    登 DR，不得採認。書面回覆之有無是本條與代換之**全部**界線。
（Pei 2026-08-28 准落，下放包 13 §三）
```

**DR-DD2 隨之降轉**：由「請確認名稱」改為**格式更正件**
（請上游將規範欄與 `-129` 之 EGD 更正為 EDG），**非阻斷、緩發**。

---

## 四、DR-DD1 文稿改稿（補 SYSAD 引文）

原文稿（包 02 §三）末段前**插入**一段（其餘逐字不動）：

> Additionally, the System Architectural Design (FM-WI-FSM-015-A01)
> describes the speed-hysteresis judgment (separate lock and unlock
> thresholds) as a market-specific processor type **for LATAM**
> (`ProcessorType4to6 … for LATAM`; "Market-specific types (such as LATAM)
> evaluate restriction using speed hysteresis thresholds"), while the
> Hong Kong logic is described in terms of parking-brake state and gear
> selection. This is consistent with the CFTS022 section structure and
> inconsistent with the Hong Kong wording of SWE1 rows -025 ~ -028.

**凍結維持** —— 兩個獨立來源（CFTS 結構＋SYSAD 架構）與 SWE1 措辭相左，
但改市場條件仍屬上游之決定；證據補強使 DR 更好答，不使其可省。

## 五、DR-DD4 縮問改稿（三問 → 一問，降緩發）

- 原三問之第一問（判定單位）**已由 SYSAD 答**：km/h，門檻經
  `VEHICLE_SPEED_THREE_MPH_TO_KMPH` 換算 —— 於 DR 條目記為
  `PARTIALLY ANSWERED (unit: km/h, per SYSAD)`
- 改稿後僅餘一問：**該常數之實值與取整規則**
  （8.04672？8.05？8.0？—— 決定 raw 128 是否落鎖側）
- **降為非阻斷、緩發**，前提為以下拘束隨包生效：

```
B1 拘束補（併入包 12 §6.2）：
ER 不得斷言 128（不應鎖）／78（不應解）之邊界格 —— 除非 037 該列明書。
跨越側（129／77）之斷言不受限。A-DD6 marker 維持至 DR-DD4 回覆。
```

## 六、發送清單（供 Pei，收攏後）

| 級 | DR | 狀態 |
|---|---|---|
| **必發** | **DD1**（改稿含 SYSAD 引文）、**DD5**、**DD6** | 卡 12 leaf（-017~-028）|
| 緩發 | DD2（格式更正件）、DD4（縮為一問）、DD7（品質旗標）| 皆非阻斷 |
| 結案 | **DD3** | RESOLVED（本包 §二）|

## 七、任務（T19；與 T18 併行）

| # | 任務 |
|---|---|
| T19a | 台帳更新：DR-DD3 → RESOLVED（§二 依據逐字）；A-DD5 → RESOLVED；DR-DD2 降轉格式更正件；DR-DD1 文稿插段（§四 逐字）；DR-DD4 縮問改稿＋PARTIALLY ANSWERED 註記；A-DD2 條目連結 R-DD18 |
| T19b | T-抄：R-DD18 逐字入 `RULINGS.md`（加錨點；現行條數與停止值隨 T-抄 實況同步更新並回報）|
| T19c | `LID CAN Mapping r1310` 全列傾印（R-DD10 形制）：回核 A 欄 = `PARK_BRK_EDG`，取 Atlantis High 欄之訊號名，對二 DBC 驗存在性＋`VAL_` 逐字（候選 `STATUS_BH_BCM1.ParkBrakeSts`／`BCM_FD_9.ParkBrakeSts` 之 0 OFF／1 ON 前輪已測，本輪確認其確為該列所載）。查得後回報，**profile §3 之 PARK_BRK 列由分析層回填** |
| — | SYSAD 掃描之複核（§一）**併入 T19c 同包自評**：任選 §一要點 1／2 之一句原文獨立重定位，證分析層引文非轉述 |

**不在本輪**：`-017`~`-028` 之生成、寫回、git。

## 八、上繳包要求（併入 `docs/upstream/09_batch_b1.md` 或另立 10 號，依執行層時序）

T19a 台帳 diff、T19b 核對、T19c 全列傾印＋DBC 驗證、SYSAD 引文複核、
未結 DR 清單（依 §六 級別呈現）、獨立自評、R-G8 揭露。
