# 上繳包 10 —— T19a／T19b／T19c（DR triage、R-DD18、PARK_BRK 查證）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`13_dr_triage.md` §七（T19a–c）；與包 12 之 T18 系列**併行**
- 本輪**未生成 `-017`~`-028`、未寫回、未執行 git**
- 共用路徑：**未寫入一字**；profile §3 之 PARK_BRK 列**未動**（由分析層回填）
- **T17b 維持停止**

> **三句話**：
> **R-DD18 落檔，錨點 19**（18 現行 ＋ 1 留存），既有 18 條 `sha8` 全未變。
> **T19c 查得** —— `LID CAN Mapping r1310` A 欄回核為 `PARK_BRK_EDG` 且唯一；
> **Atlantis 與 Atlantis High 二欄不同字**，依 R-DD6 v2(b) 取 Atlantis High
> 之 `BCM_FD_9.ParkBrakeSts`，於 `R5_FDCAN8` 查得（1 bit，`VAL_ 0 "OFF"／1 "ON"`）。
> **SYSAD 引文四項要點獨立重定位全數相符**，含母體字元數之 2,074 差可完全歸因（§4）。

---

## 1. T19b —— R-DD18 之 T-抄

### 1.1 逐字元核對

| 條號 | 來源 | 字元數 | 落檔 | 逐字元差異 |
|---|---|---|---|---|
| R-DD18 | 包 13 §三 | 683 | 1 次 | **0** |

**與錨點一併落檔**（R-DD14 之體例），出處註在圍籬內。

### 1.2 條數與停止值之同步（依 §七 T19b 所命「隨實況同步並回報」）

| | 上輪（包 12 後）| **本輪** |
|---|---|---|
| 索引現行 | 17 | **18** |
| 索引留存 | 1 | **1** |
| 檔內 `## R-DD` 錨點 | 18 | **19** |
| **停止條件 2 之值** | 18 | **19** |

工具試跑：

```
$ python3 scripts/rulings_hash.py --target features/driver_distraction/RULINGS.md --out <scratch>
寫入 …：19 錨點（ruling 19），來源 1 檔
重複 ruling_id 1 組（其中本體不同 1 組）：R-DD6（v1 L128／v2 L208）
```

### 1.3 既有 18 條 `sha8` —— 全未變

```
R-DD1  a9b76e4b   R-DD6 v1 f28ee265   R-DD10 6f601dd1   R-DD15 b344ee36
R-DD2  da3cd8ec   R-DD7    f33ed793   R-DD11 872344f4   R-DD16 85588cb1
R-DD3  cc7aea6c   R-DD8    5dca74aa   R-DD12 42ddd946   R-DD17 a9ecb4c1
R-DD4  8d4f36bf   R-DD6 v2 a5cbaf9c   R-DD13 d46f4c85   ─────────────────
R-DD5  75513f31   R-DD9    965b6d4c   R-DD14 590f1cdc   **R-DD18 a79ceb6c（新）**
```

`diff` 上輪與本輪之 `(ruling_id, sha8)`：**唯一差異為新增之 R-DD18 一列**。
行號再度全部位移，`sha8` 一個未動。

---

## 2. T19a —— 台帳六項更新

`RULINGS.md` +28／`ANOMALIES.md` +45−?／`DATA_REQUESTS.md` +152−20
（合計 +205 −20 行）。

| # | 項 | 落點 | 結果 |
|---|---|---|---|
| 1 | **DR-DD3 → RESOLVED** | `DATA_REQUESTS.md` | 新增「結案（下放包 13 §二）」節；**結案依據逐字**入圍籬；摘要列改 `RESOLVED`、Anomaly 欄劃除 A-DD5 |
| 2 | **A-DD5 → RESOLVED（撤銷）** | `ANOMALIES.md` | 新增「撤銷」節；**條目不刪**（R-TM13 精神），保留其成立期間之軌跡 |
| 3 | **DR-DD2 降轉格式更正件** | `DATA_REQUESTS.md` | 標題改；狀態改 `DRAFTED（格式更正件，緩發）`；新增「降轉之依據 —— R-DD18」與「R-DD18(b) 之採認界線（逐條落實）」二節；Urgency 高→低 |
| 4 | **DR-DD1 文稿插 SYSAD 引文段** | `DATA_REQUESTS.md` | §四 之 8 行（555 字元）**逐字**插於末段前；**其餘一字未動**（見 §2.1）|
| 5 | **DR-DD4 縮問 ＋ PARTIALLY ANSWERED** | `DATA_REQUESTS.md` | 狀態改 `PARTIALLY ANSWERED (unit: km/h, per SYSAD)`／縮為一問、緩發；新增改稿全文與 B1 拘束補 |
| 6 | **A-DD2 連結 R-DD18** | `ANOMALIES.md` | 新增「處分（下放包 13 §三）」節；狀態改 `PENDING（待規範欄更正；**施加路徑已解**）` |

### 2.1 DR-DD1 之插段 —— 逐字，且只插不改

§四 之引文段以程式自下放包切出（自 `> Additionally,` 起至空行前止，
**8 行／555 字元**），插於 `> Until clarified, the four rows are on hold …` **之前**，
中間補一行 `>`（引用區塊之空行）。**原文稿其餘部分未動一字。**

### 2.2 ⚠ DR-DD2 降轉之處置 —— 舊理由不刪、不推翻

原「執行層未自行採用 `EDG`」之三項理由**保留為軌跡**，並逐項對照 R-DD18 之處置：

| 原理由 | R-DD18 之處置 |
|---|---|
| 1. `Description` 為規範欄，位階不同 | 採認**僅及施加路徑**；`test_item` 上半仍照原文 `EGD`（R-DD18(b)）|
| 2. `-129` 未被更正，「已定案」之推定不成立 | 未更正前標 `[ASSUMPTION A-DD2]`，上游正式更正後撤 |
| 3. R-DD5／R-13 禁代以語意相近之他訊號 | 所禁者為**自行推定**；本案有書面回覆，不屬之（R-DD18(a)）|

> **當時不採是對的**（R-DD18 尚未存在，界線未定）；
> **現在採也是對的**（界線已劃出，且限於施加路徑）。**二者不衝突。**
> 台帳寫成可對讀之形，而非把舊理由刪掉重寫。

### 2.3 DR-DD3 結案之一項連帶效果

`DR-DD3` 與 `DR-DD1` 之「二個獨立阻斷，不可互抵」註記，
其防範對象為「**以 DD3 之值到位推論 DD1 得解**」。

**DD3 已結案 → 該註記之效力隨之終止。**
`-025`~`-028` 之凍結**現僅餘 A-DD1／DR-DD1 一個成因**。台帳已載明。

---

## 3. T19c —— `LID CAN Mapping r1310` 全列傾印與 DBC 驗證

**程式**：`scripts/t19c_parkbrk.py`（新增，唯讀）

```
==============================================================================
T19c —— `LID CAN Mapping r1310`
==============================================================================
架構帶（自 r2 讀取）：A=LID Information／F=Powernet／K=CUSW／P=Atlantis／U=Compact／Z=Atlantis High／AE=Comments

[回核] A 欄 `Logical Identifier` = 'PARK_BRK_EDG'　期待 'PARK_BRK_EDG'　→ 相符 ✓
[回核] `PARK_BRK_EDG` 完全相等之列：[1310] → 唯一 ✓
[回核] 含 `PARK_BRK` 而不等於 `PARK_BRK_EDG` 之 A 欄值：無

-- r1310 全欄逐字
     A [LID Information 帶 · Logical Identifier] = 'PARK_BRK_EDG'
     P [Atlantis 帶 · Signal Name] = 'STATUS_BH_BCM1.ParkBrakeSts'
     Q [Atlantis 帶 · CAN] = 'CAN-B'
     Z [Atlantis High 帶 · Signal Name] = 'BCM_FD_9.ParkBrakeSts'
    AA [Atlantis High 帶 · CAN] = 'CAN-FD'

[取欄] Atlantis 欄（P）= 'STATUS_BH_BCM1.ParkBrakeSts'
[取欄] Atlantis High 欄（Z）= 'BCM_FD_9.ParkBrakeSts'
       二欄不同字 → 取 Atlantis High
[取欄] Atlantis High 欄所載之名：['BCM_FD_9.ParkBrakeSts']

------------------------------------------------------------------------------
DBC 驗證（存在性 ＋ VAL_ 逐字）
------------------------------------------------------------------------------

候選 `BCM_FD_9.ParkBrakeSts`
   [PDT27_E2A_R4_BHCAN.dbc] BO_ `BCM_FD_9` **不在** ✗
   [PDT27_E2A_R5_FDCAN8.dbc] BO_ id=1066 ✓
        SG_ : SG_ ParkBrakeSts : 180|1@0+ (1,0) [0|1] "-" ETM,LTM,TBM
        VAL_: [('0', 'OFF'), ('1', 'ON')]
              0 = 'OFF'
              1 = 'ON'

==============================================================================
T19c 判定：A 欄回核 ✓／Atlantis High 名於綁定 DBC 查得 ✓
**profile §3 之 PARK_BRK 列由分析層回填；本檔不寫 profile。**
```

### 3.1 逐項答 §七 T19c 所問

| 問 | 答 |
|---|---|
| A 欄回核 = `PARK_BRK_EDG` | **相符 ✓**，且**全分頁唯一**（僅 r1310）；含 `PARK_BRK` 而不等於該名者**無** |
| 全列傾印（R-DD10 形制）| 見上：僅 **A／P／Q／Z／AA** 五欄非空 |
| Atlantis High 欄之訊號名 | **`BCM_FD_9.ParkBrakeSts`**（AA 欄 `CAN-FD`）|
| 二 DBC 存在性 | `R5_FDCAN8` **BO_ 1066 ✓**；`R4_BHCAN` **不在** |
| `VAL_` 逐字 | **`0 = 'OFF'` ／ `1 = 'ON'`** |
| 訊號定義 | `SG_ ParkBrakeSts : 180\|1@0+ (1,0) [0\|1] "-"　ETM,LTM,TBM` —— **1 bit** |

### 3.2 ⚠ 二欄不同字 —— R-DD6 v2(b) 在此列有實際分辨力

```
P  [Atlantis 帶 · Signal Name]      = 'STATUS_BH_BCM1.ParkBrakeSts'   Q  = 'CAN-B'
Z  [Atlantis High 帶 · Signal Name] = 'BCM_FD_9.ParkBrakeSts'         AA = 'CAN-FD'
```

**與 `$Speedometer$`（r1738，二欄同字）不同：此列二欄不同字。**
依 **R-DD6 v2(b)**「不同字時取 **Atlantis High**」→ 取 `BCM_FD_9.ParkBrakeSts`。

**備援名之查證**（R-DD13(d)：未取之名記為備援並註其匯流排）：

| 名 | 架構欄 | 匯流排 | `R4_BHCAN` | `R5_FDCAN8` | `VAL_` |
|---|---|---|---|---|---|
| **`BCM_FD_9.ParkBrakeSts`**（**取**）| Atlantis High | CAN-FD | 不在 | **BO_ 1066 ✓**（180\|1@0+）| `0 OFF`／`1 ON` |
| `STATUS_BH_BCM1.ParkBrakeSts`（備援）| Atlantis | CAN-B | **BO_ 854 ✓**（24\|1@0+）| 不在 | `0 OFF`／`1 ON` |

**二者皆在綁定庫中查得，且 `VAL_` 逐字相同**（`0 OFF`／`1 ON`）——
故 R-DD13(a) 之「以存在於綁定 DBC 為篩」在此**篩不掉任何一個**，
取捨完全由 **R-DD6 v2(b)** 決定。

> **台架若無 CAN-FD**，依 R-DD13(d)「須先報再換」——
> 備援路徑為 `STATUS_BH_BCM1.ParkBrakeSts`（CAN-B），其值域與主路徑相同。
> **本輪不自行決定用哪一條**，二者並列回報。

### 3.3 下放包所述之覆核

§七 云「候選 …之 0 OFF／1 ON **前輪已測**，本輪確認其確為該列所載」。

**確認**：r1310 之 P／Z 二欄即載該二名（前輪 A-DD2 所記之 `c15`／`c25` 為
0-based 索引，對應 Excel 之 **P**／**Z**，相符）。**`0 OFF`／`1 ON` 為本輪重測所得**，
非引前輪之值。

### 3.4 R-DD18(b) 之一條界線已落實

> 「施加名之 CAN 對應**仍須自 LID 該列實測查得**，不得因勘誤成立而略過查證。」

**本節即該查證。** 勘誤（`EGD`→`EDG`）之成立只給出「查哪一列」，
**不給出該列載何訊號** —— 後者仍是實測。

---

## 4. SYSAD 引文之獨立重定位（自評第 4 項）

**目的**：證分析層 §一 之引文為**原文**而非轉述。
執行層自 `features/driver_distraction/inputs/SYS3_…SYSAD_V1 (1).docx` 獨立抽取
（`python-docx`，段落 ＋ 表格列），**未參照分析層之切法**。

### 4.1 母體覆核 —— 差 2,074 可完全歸因

| | 分析層（§一）| 本輪實測 |
|---|---|---|
| 單元（段落＋表列）| **2,075** | **2,075** ✓ |
| 字元 | 281,916 | **279,842** |

```
281,916 − 279,842 = 2,074 ＝ 2,075 個單元之間的接合字元數（2,075 − 1）
```

**即分析層以 `"\n".join(units)` 計長，本輪以 `sum(len(u))` 計。
單元數相符，字元數之差可完全歸因於接合字元。**

> 若不算這一步，2,074 之差會被讀成「母體不同」。

### 4.2 要點 2 —— 二句引文逐字重定位（**選此項**）

**引文一**（分析層書 `ProcessorType4to6 … for LATAM`）→ **單元 492**：

```
JudgmentConfigProviderFactory reads the vehicle CAN architecture key to select
the correct variant: JudgmentProcessorType1 (parking-brake logic) for HK, and
JudgmentProcessorType4to6 (speed hysteresis with separate restriction and
cancellation thresholds) for LATAM.
```

> 實際 token 為 **`JudgmentProcessorType4to6`**；分析層之 `ProcessorType4to6` 為省略式。
> **語義完全相符**，且該句同時載明 **HK 走 parking-brake logic** —— 與 §一 要點 2 之後半相符。

**引文二**（分析層以雙引號書之）→ **單元 1242，逐字命中**：

```
Market-specific types (such as LATAM) evaluate restriction using speed hysteresis thresholds
```

**「三處」之覆核**：`hysteresis` 全文 **9 命中**（單元 492／528／902／908／1242／1243／1249／1738／1744），
其中**同時含 `LATAM` 者恰 3 處**（**492／1242／1738**）。**與分析層所稱「三處」相符 ✓**

### 4.3 順帶覆核之另二項要點

| 要點 | 分析層 | 本輪實測 |
|---|---|---|
| 3 `Gear_Box_Type` 架構本體 0 命中 | 0 | **0 ✓** |
| 3 `VC_Trans` 4 命中全為文末轉貼之 CFTS 需求表 | 4 | **4 ✓**，皆為表列（單元 718–721），內容為 `SYS-RA-…-126`~`-129` 之需求原文 |
| 4 訂閱 `VehicleSpeed`／`ParkingBrakeState`／`ShiftLeverPosition` | — | **3 命中**（單元 50／116／444）✓ |

### 4.4 ⚠ 要點 1 之一項措辭精度（R-G19：理由與數字須分別驗證）

`VEHICLE_SPEED_THREE_MPH_TO_KMPH` **全文 1 命中**，單元 301：

```
3. Receives notifyStatus() callbacks for DD restriction states (Judgment Type 3/4),
   vehicle speed relative to VEHICLE_SPEED_THREE_MPH_TO_KMPH, and Teen Key presence
```

**該句本身未書「判定單位為 km/h」** —— 該結論由**常數之名**所編碼
（`THREE_MPH_TO_KMPH` ＝ 3 MPH 換為 km/h）。

**分析層之結論成立**，但其依據是**命名**而非敘述句。差別在於：

- 命名支持「存在一個由 MPH 換算之 km/h 門檻常數」 —— **強**
- 命名不支持「DUT 之比較運算一律以 km/h 為之」 —— 該句未言

**這正是縮問後 DR-DD4 仍須問「該常數之實值與取整規則」的理由** ——
單位已定，**值未定**，而值決定 raw 128 落在哪一側。**縮問之判斷正確。**

---

## 5. B1 拘束補之落實（包 13 §五）

```
ER 不得斷言 128（不應鎖）／78（不應解）之邊界格 —— 除非 037 該列明書。
跨越側（129／77）之斷言不受限。A-DD6 marker 維持至 DR-DD4 回覆。
```

已加為自檢之追加項（**判準含「037 該列明書者不在此限」之 carve-out**）：

```python
for v in ("128", "78"):
    if re.search(rf"(?<![\d.]){v}(?![\d.])", tc["expected_result"]):
        if not re.search(rf"(?<![\d.]){v}(?![\d.])", src_txt):   # 037 該列
            edge.append((tc["tc_id"], v))
```

**二產物皆 0 命中**：

| 產物 | 檢數 | 結果 | 用及跨越側者 |
|---|---|---|---|
| pilot（4 TC）| **24** | **22 PASS ／ 2 N/A ／ 0 FAIL** | `-009`／`-011` |
| B1（10 TC）| **24** | **22 PASS ／ 2 N/A ／ 0 FAIL** | `-003`／`-005`／`-007`／`-013`／`-015` |

**A-DD6 marker 維持**（DR-DD4 未回覆）。

---

## 6. 未結 DR 清單（依 §六 級別）

| 級 | DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|---|
| **必發** | **DR-DD1** | DRAFTED（**改稿含 SYSAD 引文**）| `-025`~`-028`（4）| **凍結** |
| **必發** | **DR-DD5** | DRAFTED | `-017`~`-024`（8）| 不入批次 |
| **必發** | **DR-DD6** | DRAFTED | `-017`~`-024`（8）| 不入批次 |
| 緩發 | DR-DD2 | DRAFTED（**格式更正件**）| `-021`~`-024`（4）| **不阻斷** —— 施加名已由 R-DD18 解 |
| 緩發 | DR-DD4 | **PARTIALLY ANSWERED**（單位 km/h）／縮為一問 | 9 列書 MPH 者 | **不阻斷** |
| 緩發 | DR-DD7 | DRAFTED（品質旗標）| 文稿問 2；**實測涉 11** | **不阻斷** |
| **結案** | ~~DR-DD3~~ | **RESOLVED** | `-017`~`-028`（12）| **解除** |

**必發 3 筆卡 12 leaf；緩發 3 筆皆非阻斷；DD3 已結。**

另：**`-001`／`-002` 之處置仍無 DR 承載**（上繳 09 §3.3，三案未裁）。

### 6.1 阻斷疊圖（本輪後）

```
-001 ~ -002  (2)   Body OFF 電源域，無具名識別碼；**無 DR 承載**（待裁）
-003 ~ -008  (6)   **B1 已生成**；-003/-005/-007 帶 A-DD6
-009 ~ -012  (4)   pilot 已修訂；-009/-011 帶 A-DD6
-013 ~ -016  (4)   **B1 已生成**；-013/-015 帶 A-DD6
-017 ~ -020  (4)   DR-DD5 ＋ DR-DD6（**A-DD5 已撤**）
-021 ~ -024  (4)   DR-DD5 ＋ DR-DD6；施加名已解，用及者標 [ASSUMPTION A-DD2]
-025 ~ -028  (4)   **僅餘** A-DD1／DR-DD1（**A-DD5 已撤**）
```

**已生成 14 TC ／ 28 leaf。** 本輪之解除使 `-017`~`-028` 少一個成因（A-DD5）。

---

## 7. 獨立自評

### 7.1 我做對的

- **SYSAD 的 2,074 差算了。** 單元數 2,075 相符、字元數差 2,074 ——
  **恰為 2,075 個單元之間的接合數**。不算這一步就只能寫「母體略有出入」，
  那等於沒複核。
- **「三處」是數出來的。** `hysteresis` 全文 9 命中，同時含 LATAM 者恰 3 處。
  分析層的數字精確，而**精確這件事需要被驗證，不是被相信**。
- **T19c 把備援名也查了。** §七只要求驗 Atlantis High 欄之名；
  但 R-DD13(d) 要求未取之名記為備援並註其匯流排 —— 查了才發現
  **二者皆在庫中、`VAL_` 逐字相同**，即 R-DD13(a) 之篩在此篩不掉任何一個，
  取捨**完全**由 R-DD6 v2(b) 承擔。這件事影響「台架無 FD 時怎麼辦」。
- **DR-DD2 降轉沒有把舊理由刪掉。** 三項理由逐項對照 R-DD18 之處置，
  寫成「當時不採是對的，現在採也是對的」。**刪掉會讓日後看不出界線是怎麼劃出來的。**

### 7.2 我做糙的

- **T19a 我先寫了六項編輯才想到摘要表要同步**，於是分兩次改同一個檔。
  台帳有「明細節 ＋ 摘要表」兩層，改一層就該同時改另一層。

### 7.3 我拒絕做的

- **不改 DR-DD1 文稿之其餘部分。** 只插 §四 那 8 行。
- **不寫 profile §3 之 PARK_BRK 列**（§七明文由分析層回填）。
  T19c 查得了值，寫下去很順手 —— 但那是分析層的欄位。
- **不自行決定主路徑或備援路徑。** 二者並列回報（§3.2）。
- **不把要點 1 之「命名支持」寫成「敘述句支持」**（§4.4）。

### 7.4 一件我原本會漏的

`-025`~`-028` 的凍結，我原本要照抄「A-DD1 ＋ A-DD5」兩個成因。

**A-DD5 已撤** —— 而且撤的連帶效果不只是少一個標記：
DD3 與 DD1 之間那條「不可互抵」的註記，其**防範對象**（以 DD3 的值推論 DD1 得解）
**隨 DD3 結案而消失**。註記本身不是錯的，是**沒有東西可防了**。

台帳若只把 A-DD5 改成 RESOLVED 而留著那條註記，
下一個人會以為那裡還有一個活的約束。

---

## 8. 量測條件揭露（R-G8）

### 8.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| 19 錨點 | 工具解析出之 `ruling` 列數 | 本檔圍籬條文 19（18 現行 ＋ 1 留存）|
| 既有 18 條 sha8 未變 | 與上輪 tsv `sha8` 相同者 | 上輪之 18 條 |
| SYSAD 單元 2,075 | 非空段落 ＋ 非空表格列 | 同一份 docx（`python-docx`）|
| 字元差 2,074 | 分析層 281,916 − 本輪 279,842 | 接合字元數 2,075 − 1 |
| `hysteresis` 含 LATAM 者 3／9 | 同時含 `latam`（不分大小寫）之單元數 | `hysteresis` 命中之 9 單元 |
| `PARK_BRK_EDG` 唯一 | A 欄完全相等之列數 = 1 | `CAN Mapping` r4–r2629 之非空 LID 列 2,626 |
| 自檢 22 PASS／2 N/A／0 FAIL | 各判別之檢項數 | **24 檢**（IN §9 十七項 ＋ 追加 7）|

### 8.2 界線

- **SYSAD 之單元切法**為「非空段落 ＋ 非空表格列（以 ` | ` 接合各儲存格）」。
  **分析層之切法未載明**，本輪之相符（2,075）**是結果相符，非方法已知相同**。
  若其切法不同而恰得同數，本覆核不會發現。
- **`hysteresis`／`LATAM` 之比對為 substring、不分大小寫**，未做詞界。
- **T19c 之 DBC 驗證以 `BO_ <id> <MESSAGE>` ＋ 其區塊內之 `SG_ <Signal>` 雙鍵**；
  裸 `SG_` 名全表比對**未做** —— 故「不在」之判斷嚴格範圍為
  「該 MESSAGE 不在該 DBC」或「該 MESSAGE 內無該 SG_」。
- **`VAL_` 之擷取以該 BO_ id ＋ 訊號名為鍵**，未涵蓋 `VAL_TABLE_` 之間接定義。
- **B1 拘束補之 `128`／`78` 掃描**以「前後非數字或小數點」為界，
  故 `1128`／`8.0625` 不會誤命中；但**若 ER 以文字書「一百二十八」則掃不到**。

### 8.3 檔與開啟方式

| 標的 | 開啟 |
|---|---|
| `RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md` | **本輪寫入**（私有路徑）|
| SYSAD docx | **唯讀**（`python-docx`）|
| LID v1_76／二 DBC | **唯讀** |
| profile | **未開**（§七：PARK_BRK 列由分析層回填）|
| `docs/fw036/RULINGS.sha.tsv` | **未開**（T17b 停止）|
| 工作簿 | **未開** |

### 8.4 本輪未量測者

- **`-001`／`-002` 之激勵** —— 仍無具名識別碼（上繳 09 §3.3）。
- **`-017`~`-028` 之生成** —— 非本輪範圍。
- **profile §3 之 PARK_BRK 列是否已由分析層回填** —— 未讀該檔。
- **SYSAD 要點 4 之 VHAL 屬性是否入 TC** —— 依 R-DD4（SYSAD 為 SWE.2 側，
  人讀參考）**不入**，本輪未以其為任何 TC 之來源。

---

## 9. 待分析層／Pei

| # | 事項 | 現況 |
|---|---|---|
| 1 | **profile §3 之 PARK_BRK 列回填** | T19c 已查得：`BCM_FD_9.ParkBrakeSts`（`R5_FDCAN8` BO_ 1066、1 bit、`0 OFF`／`1 ON`）；備援 `STATUS_BH_BCM1.ParkBrakeSts`（CAN-B、`R4_BHCAN` BO_ 854、同值域）|
| 2 | **profile §3 之 `Country_Code` 列** | A-DD5 已撤，`[ASSUMPTION A-DD5]` 標記要求待分析層移除 |
| 3 | **`-001`／`-002` 之處置** | 仍無 DR 承載；三案見上繳 09 §3.3 |
| 4 | **DR-DD7 之範圍** | 文稿問 2 leaf，實測涉 11 |
| 5 | tsv 重生之解除 | **T17b 維持停止**；本線現為 **19 列**（非 14），續行時允許項須以 19 計 |
| 6 | 其餘 4 feature 之 `RULINGS.md` 體例 | 未代改 |
| 7 | `-017`~`-028` 之生成 | 待 DD5／DD6 回覆 |
