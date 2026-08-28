# 上繳包 12 —— R-DD19 乙案落地、A-DD8／A-DD9、DR 三處修訂、T21a／T21b（批次 B2）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`15_case_b_unfreeze.md` §五（T-抄／T-登／T21a／T21b）
- 次序：包 14 之 T20 系列**已於前輪完成**（`framework.md` 已落、自檢第 1 項已為實際比對版）
- 本輪**未生成 `-025`~`-028`、未寫回、未執行 git**；共用路徑**未寫入一字**；**T17b 維持停止**

> **三件事**：
> **T-抄 20 錨點**（19 現行 ＋ 1 留存），既有 19 條 `sha8` 全未變。
> **B2 八則生成，26 檢全綠** —— 其中二項自檢本輪**由白名單改為溯源檢**，
> 並附**六種注入之反向對照，全數被攔**（§5.3）。
> **DD5／DD6 之 `on hold` 已替換** —— 乙案生效後該句失實，不得向上游陳述失實狀態。

---

## 1. T-抄 —— R-DD19

| 條號 | 來源 | 字元數 | 落檔 | 逐字元差異 |
|---|---|---|---|---|
| R-DD19 | 包 15 §一 | 883 | 1 次 | **0** |

**條數與停止值同步**：

| | 上輪 | **本輪** |
|---|---|---|
| 索引現行 | 18 | **19** |
| 索引留存 | 1 | 1 |
| 錨點 | 19 | **20** |
| **停止條件 2 之值** | 19 | **20** |

工具試跑：`寫入 …：20 錨點（ruling 20），來源 1 檔`
**既有 19 條 `sha8` 逐一比對全未變**，唯一差異為新增之 `R-DD19 e293c320`。

---

## 2. T-登

### 2.1 A-DD8／A-DD9 建條

二條之**條目逐字**入 `ANOMALIES.md`（各 149／172 字元，落檔 1 次），
並附採認基礎（R-DD19(a)(b) 逐字）與其與 DR 之關係。

**A-DD9 之條目另載 R-DD19(c) 硬邊界**，且明記其與上繳包 05 §3.5(甲) 之關係：

> 上繳 05 當時指出「PROXI `Annotation` 把 manual 與 MTA **並列為不同項**，
> 恰是反證；但 Annotation 為舉例、非歸屬定義，**故亦不得反過來據以排除**」。
> **乙案未推翻該判斷** —— 它只在**兩極**上採認，邊界仍懸，故立為硬邊界。

### 2.2 DR 文稿三處修訂（逐字替換）

| # | 標的 | 動作 | 字元／行 | 落檔 |
|---|---|---|---|---|
| 2.1 | **DR-DD1** | 末段之前**插入**一問（LATAM 之市場條件如何表述）| 338／5 | 1 次 |
| 2.2 | **DR-DD6** | 問句段**之後**插入判準句（P 檔之有無為決策關鍵）| 398／6 | 1 次 |
| 2.3 | **DR-DD5／DD6** | 末行 `…on hold…` **替換** | 275／4 | **2 處** |

**`on hold in SWQT` 之殘留 = 1** —— 即 **DR-DD1** 之該句，**刻意保留**：
`-025`~`-028` 之凍結未解（乙案不及於 DD1），該句對 DD1 仍屬實。

> **§2.3 之理由值得記**：乙案生效後 DD5／DD6 之「on hold」不再屬實。
> **DR 不得向上游陳述已失實之狀態** —— 若不改，上游會以為那 8 列還沒開始做，
> 而實際上八則 TC 已在假設下產出並掛了 marker。
> **一個過期的狀態陳述，比沒有狀態陳述更糟。**

---

## 3. T21a —— 非 P 代表值

```
==========================================================================
T21a —— `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT` 之 VAL_ 全列舉
==========================================================================
DBC : PDT27_E2A_R5_FDCAN8.dbc
BO_ : id=263 (0x107)
SG_ : SG_ GearEngagedForDisplay_PT : 12|5@0+ (1,0) [0|31] "" ETM,LTM,TBM

VAL_ 全列舉（**逐字**，共 18 項）：
    0 = 'Initialize'
    1 = 'Gear_1st'
    2 = 'Gear_2nd'
    3 = 'Gear_3rd'
    4 = 'Gear_4th'
    5 = 'Gear_5th'
    6 = 'Gear_6th'
    7 = 'Gear_7th'
    8 = 'Gear_8th'
    9 = 'Gear_9th'
   12 = 'Park'
   13 = 'Neutral'
   14 = 'Reverse'
   15 = 'Drive'
   16 = 'Low'
   17 = 'Manual'
   18 = 'Sport_Mode'
   31 = 'SNA'

值域 [0|31] 中**未列舉**之 raw： [10, 11, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

P 檔（037 之 `[P]`）： [(12, 'Park')] → 前輪所確認者

非 P 之全部成員（17 項）：
  行車檔位類（13）： [(1, 'Gear_1st'), (2, 'Gear_2nd'), (3, 'Gear_3rd'), (4, 'Gear_4th'), (5, 'Gear_5th'), (6, 'Gear_6th'), (7, 'Gear_7th'), (8, 'Gear_8th'), (9, 'Gear_9th'), (15, 'Drive'), (16, 'Low'), (17, 'Manual'), (18, 'Sport_Mode')]
  其他（4）： [(0, 'Initialize'), (13, 'Neutral'), (14, 'Reverse'), (31, 'SNA')]

--------------------------------------------------------------------------
取定
--------------------------------------------------------------------------
  取 **15 = 'Drive'** 為非 P 之代表。

  取法（reasoning 將逐字載明）：
  (1) 037 `-127`／`-129` 書 `$PresentGear$ <> [P]`，其為一**類**而非特定值；
      類內任一成員皆滿足該條件（同取樣 feature 之理）。
  (2) 於非 P 之成員中取**行車常態檔位**：`15 = 'Drive'` 為 DBC `VAL_` 逐字，
      且為自排車行進之常態選擇 —— 較 `Gear_1st`~`Gear_9th`（特定檔位）
      與 `Low`／`Manual`／`Sport_Mode`（特殊模式）更接近常態。
  (3) `0 = 'Initialize'` 與 `31 = 'SNA'` **不取** —— 前者為初始化態、
      後者為訊號不可用，二者皆非「已選定之非 P 檔位」，
      取之會把「檔位非 P」與「檔位未知」混為一談。
  (4) `13 = 'Neutral'`／`14 = 'Reverse'` 雖亦非 P 且為真實檔位，
      **未取但併記** —— 類內取樣，非唯一解。

  **不掛 marker**（下放包 §3.3 明文：類內取樣非假設）。
```

### 3.1 取定與其載明

**取 `15 = 'Drive'`。** `VAL_` 共 **18 項**，非 P 之成員 **17 項**。

reasoning 逐字載明四點取法（見 §6 之 `newR1L-DD-C003`）：
類為一而非特定值／取行車常態檔位／`0 (Initialize)` 與 `31 (SNA)` **不取**
（取之會把「檔位非 P」與「檔位未知」混為一談）／`13 (Neutral)`、`14 (Reverse)`
亦合法而未取。**不掛 marker**（下放包 §3.3 明文：類內取樣非假設）。

### 3.2 順帶量到之一項

值域 `[0|31]` 中**未列舉之 raw 有 14 個**（`10, 11, 19–30`）。
**本輪未取用任一未列舉值** —— 其無 `VAL_` 逐字可書，寫入即違 R-DD9(a)。

---

## 4. T21b —— 批次 B2（8 則）

**產物**：`generated/batch_b2.json`　**生成器**：`scripts/gen_batch_b2.py`

### 4.1 骨架對照（§3.1）

| leaf | source | 內容 | Test Set | priority | design_method |
|---|---|---|---|---|---|
| `-017` | `-125`+`-126` | 自排＋P → 解除 | `Hong Kong Market` | P1 | 決策表 |
| `-018` | `-125`+`-126` | fail-safe | 同 | P1 | 基礎故障注入 |
| `-019` | `-125`+`-127` | 自排＋非P → 受限 | 同 | **P0** | 決策表 |
| `-020` | `-125`+`-127` | fail-safe | 同 | P1 | 基礎故障注入 |
| `-021` | `-125`+`-128` | 手排＋手煞ON → 解除 | 同 | P1 | 決策表 |
| `-022` | `-125`+`-128` | fail-safe | 同 | P1 | 基礎故障注入 |
| `-023` | `-125`+`-129` | 手排＋手煞OFF → 受限 | 同 | **P0** | 決策表 |
| `-024` | `-125`+`-129` | fail-safe | 同 | P1 | 基礎故障注入 |

`Test Set` = `Hong Kong Market` —— **framework.md Part II 組 5**（leaf 017–024）。
八則之上半皆 `full`（38–44 token，未逾 50）。

### 4.2 施加路徑與 marker（§3.2）

| 條件 | 寫法 | marker |
|---|---|---|
| 市場 | `PROXI Country_Code = 91` | **無** —— A-DD5 已撤（包 13 §二），為確定值 |
| 自排 | `PROXI Gear_Box_Type = 4 (ATX)` | **A-DD8 ＋ A-DD9** |
| 手排 | `PROXI Gear_Box_Type = 1 (MTX)` | **A-DD8 ＋ A-DD9** |
| P 檔 | `$PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)` | 無 |
| 非 P | `… = 15 (Drive)` | 無（T21a，類內取樣）|
| 手煞 | `$BCM_FD_9.ParkBrakeSts$ = 1 (ON)` ／ `= 0 (OFF)` | **A-DD2**（R-DD18(b)）|
| 速度 | PC 訊號源行 at `0 (0.0000 km/h)` | **無** —— 0 非門檻值 |

**速度壓 0 之理由已入八則之 reasoning**：排除基準速度規則之干擾，
使觀察可歸因於檔位／手煞。**不掛 A-DD6**（A-DD6 所涵者為 §3.1 之門檻 raw，0 不在其列）。

### 4.3 fail-safe 之所停訊號（§3.4）

037 之 AC2 於四列**逐字全等**，其 Method 給二選項：
`Stop or suppress <gear|park-brake> updates`，**或** `make VC_Trans_Equipped unavailable`。

**取前者**，依 §3.4「取該 source AC1 所條件之訊號」：

| leaf | source AC1 所條件之訊號 | **所停之訊息** |
|---|---|---|
| `-018`／`-020` | `$PresentGear$` | `"PT_SYSTEM_FD_1"` |
| `-022`／`-024` | `$PARK_BRK_EGD$` | `"BCM_FD_9"` |

**`PROXI` 參數不作失效標的** —— 其為組態非訊號，停送無從施加；
故 037 所列之另一選項不取。**該取法之依據已逐則載於 reasoning。**

### 4.4 ⚠ 一項須明說的佈置選擇 —— `-020` 之基準態

`-020` 之 source 為 `-127`（自排＋**非 P** → 受限）。
若其基準態取「非 P」，則故障注入前後**皆為受限**，
**fail-safe 生效與否不可觀察**。

故基準態取 `12 (Park)`（該 source 家族之「可解除」側）。

**這是否擴入 `-126` 之領域？** 不是，理由已入 reasoning：

> AC2 之原文**未條件於檔位或手煞之值**（其僅書 `required … input is unavailable`，
> 四列逐字全等），故基準之選定為**測試佈置**，非對需求之主張，
> 不構成擴入 sibling（IN §8.2.1）。

**`-024` 同理**（其 source `-129` 為手煞 OFF → 受限，基準取手煞 ON）。

### 4.5 A-DD7 組 3／組 4 之載明

`-018`／`-020` 為 A-DD7 **組 3**、`-022`／`-024` 為**組 4**（037 原文各組內逐字全等）。
四則之 reasoning 皆載明其與同組 sibling **驗證目標實質相同**，
**不得以取樣之不同偽稱為不同之驗證目標**（承包 10 §四之處置）。

### 4.6 R-DD19(c) 硬邊界之落實

**四交付欄中之 `Gear_Box_Type` 值只有 `1 (MTX)` 與 `4 (ATX)`。**
`MTA`／`DDCT`／`= 2`／`= 3` 於四欄**零命中**（自檢逐則掃描）。

`reasoning` 中**得**提及該二值（載明其被排除）—— 其為紀錄，非 Pre-Condition 或輸入。
**生成器亦於落檔前 assert 該邊界**（掃四交付欄，命中即中止）。

> 第一版生成器把 `reasoning` 也納入掃描，於是自己攔下自己 ——
> **R-DD19(c) 禁的是「作 Pre-Condition 或輸入」，不是「不得提及」。**
> 若照第一版辦，就會為了通過自檢而把「為何排除 MTA／DDCT」從 reasoning 刪掉，
> **那正好刪掉了讀者最需要知道的那一句。**

---

## 5. 自檢

### 5.1 結果（三產物同一骨幹，`SC_ARTIFACT` 指定）

| 產物 | 檢數 | 結果 |
|---|---|---|
| pilot（4 TC）| **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |
| B1（10 TC）| **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |
| **B2（8 TC）** | **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |

### 5.2 本輪對自檢之三處改動 —— **二處是因為舊檢會誤判 B2**

| # | 項 | 改動 | 何以必須改 |
|---|---|---|---|
| 1 | **第 13 項（§12）** | 期待值由「AC 別」改為**自 procedure 形態機械推導**，且**把 PC 之訊號源行計為該訊號之一個值** | B2 之 AC1 為條件組合（決策表）而非轉換；舊版硬掛 State Transition。加計 PC 值後，pilot 之 `-009`（PC 0 → 送 129）仍正確判為狀態轉換 |
| 2 | **第 12 項（§8.4.1）** | 手建之**數值白名單**改為**溯源檢** | 白名單是為速度 raw 手建的，B2 之 `12 (Park)`／`15 (Drive)` 一來就紅。**換一批 leaf 就失效的檢，不是檢** |
| 3 | 第 16 項（§10.7）| 支援**雙引**：逐行對應該 leaf 之每一 source，升冪 | `-017`~`-024` 為雙引 leaf（HK 章閘 ＋ 條文）|

**第 2 項之新判準**：四交付欄中每一個 `= <raw> (<label>)` 之 `(raw, label)`
須可溯至 **(i)** 該訊號之 DBC `VAL_`（自二綁定 DBC 實讀）、
**(ii)** profile §3.1 之 raw 表、或 **(iii)** PROXI `Format` 之 Table 列舉；
且**裸 raw（無括號標籤）一律判為不可溯**（R-DD9 要求帶標籤）。

B2 之溯源分布：`{'DBC VAL_': …, 'PROXI Format r443': …, 'profile §3.1': …}`（見 §5.4 輸出）。

> **白名單與溯源檢的差別**不在嚴格程度，在**是否隨產物自動延展**。
> 白名單每加一批 leaf 就要人手維護，而漏加的下場是**紅**（還好）；
> 但若有人為了讓它變綠而把新值加進白名單，就**沒有任何東西再檢查那個值的出處**。

### 5.3 ⚠ 反向對照 —— 六種注入，全數被攔

新檢是綠的，但綠不代表它在工作。注入六種壞值（暫存檔，跑完即刪，正式產物未動）：

| 注入 | 被攔於 |
|---|---|
| PC 用 `Gear_Box_Type = 2 (MTA)` | **第 12 項 ＋ R-DD19(c)** |
| PC 用 `Gear_Box_Type = 3 (DDCT)` | **R-DD19(c)** |
| 檔位改 `= 20 (Park)`（DBC 無此 raw）| **第 12 項** |
| 檔位改 `= 12 (Parking)`（標籤與 `VAL_` 不符）| **第 12 項** |
| 檔位改 `= 12`（裸 raw 無標籤）| **第 12 項** |
| 拿掉 `[ASSUMPTION A-DD9]` | **marker 義務項** |

> 第 4 種（`12 (Parking)`）是白名單**永遠抓不到**的 —— 12 在白名單裡。
> **溯源檢比的是 `(raw, label)` 對，不是 raw 本身。**

### 5.4 B2 自檢輸出（機器逐字）

```
====================================================================================
TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）
====================================================================================
[PASS]   1 §4.1/§4.2 + framework.md Test Set ∈ framework.md Layer 2，且與其 leaf 之分組相符；無 Test Group 前綴、無 Misc／Unclassified
         framework Layer 2 共 6 組 ['Body Off Init', 'Hong Kong Market', 'Lockout Enforcement', 'Lockout Tables', 'Market Speed Gating', 'Speed Monitoring']；本產物用 ['Hong Kong Market']；不符 無；前綴 無；泛稱組 無
[PASS]   2 §4.3.1           test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal
         017: 上半子串 ✓/38tok、下半 有、中文 無、modal 無；018: 上半子串 ✓/44tok、下半 有、中文 無、modal 無；019: 上半子串 ✓/39tok、下半 有、中文 無、modal 無；020: 上半子串 ✓/44tok、下半 有、中文 無、modal 無；021: 上半子串 ✓/38tok、下半 有、中文 無、modal 無；022: 上半子串 ✓/43tok、下半 有、中文 無、modal 無；023: 上半子串 ✓/38tok、下半 有、中文 無、modal 無；024: 上半子串 ✓/43tok、下半 有、中文 無、modal 無
[PASS]  2b §4.3.1           同一 Requirement ID 衍生之列，括號下半不逐字相同
         無重複
[PASS]   3 §4.4/§8.5 + R-DD17 Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）
         0 命中；4 則各 1 項且皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 §4.5             Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA
         4 則皆 NA=True；回指 無；跨欄重複 無
[PASS]   5 §5.1/§5.5        步驟無禁用動詞；Final Step 含 ACTION ＋ check target（preferred verb）
         禁用動詞 0 命中；末步缺 `check that` 無
[PASS]   6 §5.2             步驟長度：一般 ≤12 字、Final ≤18 字（含 action+check target）
         字數 {'newR1L-DD-C001': [7, 9], 'newR1L-DD-C002': [7, 7, 11, 12], 'newR1L-DD-C003': [7, 11], 'newR1L-DD-C004': [7, 7, 11, 12], 'newR1L-DD-C005': [9, 11], 'newR1L-DD-C006': [9, 9, 11, 14], 'newR1L-DD-C007': [9, 13], 'newR1L-DD-C008': [9, 9, 11, 14]}
[N/A ]   7 §5.3             標準 setup 片語逐字重用
         本 feature 未定義 project-level setup 常數（feature.yaml 無該鍵）—— 無適用對象
[N/A ]   8 §5.4             CLI／tooling 步驟採 description + `$` 指令格式
         4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟
[PASS]   9 §5.6             before／after 需要時建立 baseline
         017: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；018: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；019: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；020: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；021: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；022: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；023: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；024: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟
[PASS]  10 §6               Procedure↔ER 1:1；ER 可觀察；ER 無 modal
         步驟 {'newR1L-DD-C001': 2, 'newR1L-DD-C002': 4, 'newR1L-DD-C003': 2, 'newR1L-DD-C004': 4, 'newR1L-DD-C005': 2, 'newR1L-DD-C006': 4, 'newR1L-DD-C007': 2, 'newR1L-DD-C008': 4}／ER {'newR1L-DD-C001': 2, 'newR1L-DD-C002': 4, 'newR1L-DD-C003': 2, 'newR1L-DD-C004': 4, 'newR1L-DD-C005': 2, 'newR1L-DD-C006': 4, 'newR1L-DD-C007': 2, 'newR1L-DD-C008': 4}；modal 無；非觀察語句 無
[PASS]  11 §7               無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向
         FF：010／012 之 fail-safe 皆先建立正常態再注入故障，未假設隱藏狀態；FP：本 4 leaf 無列舉式支援項（無 format／device／protocol 之列舉），無配對義務
[PASS]  12 §8.1/§8.2/§8.4   追溯 Req/SWRA；不擴入 sibling；**每一 raw 值可溯至 DBC VAL_／profile §3.1／PROXI Format**；無範圍捏造
         req_id 形制 True；§8.4.2 禁詞 0 命中；溯源 {'profile §3.1': 8, 'PROXI Format r443': 8, 'DBC VAL_': 16}；不可溯 無
[PASS]  13 §12              Design Method 於 procedure 定稿後指派，且合 first-match 序
         009/011 觸發為 A→B 狀態轉換，於 Scenario 前命中；010/012 為 simulated fault（停送＋逾時），於 State Transition 前命中；皆為下拉選單實值 True
[PASS]  14 §11 + R-DD11     四欄 numbered item 無作者所書之行尾句號（引號內字串之終端標點保留）
         0 違規
[PASS]  15 §11 + R-DD12(c)  UI 標籤用 `"..."`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker
         0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）；單引號／角括號 無
[PASS]  16 §10.7 + profile §1 spec_reference 逐行對應該 leaf 之每一 source；一行一 ObjectID、升冪、無串接
         017: source ['125', '126'] → ['CFTS022-4915120', 'CFTS022-4915121']；018: source ['125', '126'] → ['CFTS022-4915120', 'CFTS022-4915121']；019: source ['125', '127'] → ['CFTS022-4915120', 'CFTS022-4915122']；020: source ['125', '127'] → ['CFTS022-4915120', 'CFTS022-4915122']；021: source ['125', '128'] → ['CFTS022-4915120', 'CFTS022-4915123']；022: source ['125', '128'] → ['CFTS022-4915120', 'CFTS022-4915123']；023: source ['125', '129'] → ['CFTS022-4915120', 'CFTS022-4915124']；024: source ['125', '129'] → ['CFTS022-4915120', 'CFTS022-4915124']
[PASS]  17 §8.6/§8.7        門檻為 spec 溯源之具體值；相似操作於 ER 具名區辨；來源規格勝於索引匯出
         門檻具名 raw True（profile §3.1 依 R-DD7(c)）；A-DD6 marker True；ER 取樣具名 True
[PASS]   + §11              多行欄位無行首／行尾空白，空行為真空行
         0 違規
[PASS]   + profile §2.3     ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked
         0 命中
[PASS]   + §10.2            priority 為 P0–P3 且合 profile §4
         017=P1／018=P1／019=P0／020=P1／021=P1／022=P1／023=P0／024=P1
[PASS]   + §10.5            test_procedure 至少 2 個編號步驟
         {'newR1L-DD-C001': 2, 'newR1L-DD-C002': 4, 'newR1L-DD-C003': 2, 'newR1L-DD-C004': 4, 'newR1L-DD-C005': 2, 'newR1L-DD-C006': 4, 'newR1L-DD-C007': 2, 'newR1L-DD-C008': 4}
[PASS]   + R-DD16(b)        輸出 split_flag／split_reason；未拆者 false／"NA"
         缺鍵 無；值不合 無；鍵名依 R-DD16(a) 用 test_item／spec_reference（既有寫回形制）
[PASS]   + 包 13 §五          ER 不得斷言 128（不應鎖）／78（不應解）之邊界格（037 該列明書者不在此限）；跨越側 129／77 不受限
         0 命中；用及跨越側者 []
[PASS]   + R-DD19(c)        硬邊界：MTA(2)／DDCT(3) 不得出現於四交付欄之任一處
         0 命中；四欄所用之 Gear_Box_Type 值 ['Gear_Box_Type = 1 (MTX)', 'Gear_Box_Type = 4 (ATX)']
[PASS]   + R-DD19/R-DD18    用及 PROXI Gear_Box_Type 者標 A-DD8＋A-DD9；用及 $BCM_FD_9.ParkBrakeSts$ 者標 A-DD2
         缺標 無；本產物所用之 marker ['A-DD2', 'A-DD8', 'A-DD9']
====================================================================================
RESULT: PASS 24 ／ N/A 2 ／ FAIL 0　（共 26 檢）
```

---

## 6. B2 八則全文

### newR1L-DD-C001 —— `SWE1-RA-Driver_Distraction-017`（P1／Hong Kong Market）

> 上半：037 Analysis Report r25 c3 (Requirement Description)；`full`；38/50 token

```json
{
  "tc_id": "newR1L-DD-C001",
  "req_id": "SWE1-RA-Driver_Distraction-017",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains valid VC_Trans_Equipped and PresentGear inputs\nCase [Normal]VC_Trans_Equipped is Automatic and PresentGear is P\nThen DD Service sets the Lock Out State to NOT_RESTRICTED and notifies the subscribed Listener\n(Automatic transmission with the gear selector in Park)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 4 (ATX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)\n2. Open \"Pairing (1st time)\" and check that it opens",
  "expected_result": "1. The signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ is carried on the bus at 12 (Park)\n2. \"Pairing (1st time)\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915121",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "決策表 (Decision Table Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，自排車之解除判定 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Pairing (1st time)\"（p7 top=304（Phone 列），非黃標、非 NAV 系）。037 VC 之 `Listener receives a … notification` 依 profile §2.3 不入 ER，改以該 feature 之可及性承載。關鍵情境條件：市場 `PROXI Country_Code = 91`（確定值，A-DD5 已撤，不掛 marker）；變速箱型式依 **R-DD19** 之乙案，施加路徑掛 [ASSUMPTION A-DD8]、代表值掛 [ASSUMPTION A-DD9]（`4 (ATX)`）；檔位取 `12 (Park)`（DBC `VAL_` 逐字）。速度訊號源壓於 `0 (0.0000 km/h)` —— **排除基準速度規則之干擾**，使觀察可歸因於檔位；0 非門檻值，**不掛 A-DD6**。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位** —— 其歸屬為 DR-DD6 之未決問題，R-DD19(c) 定為硬邊界；fail-safe 面由同 source 之 AC2 列承載。"
}
```

### newR1L-DD-C002 —— `SWE1-RA-Driver_Distraction-018`（P1／Hong Kong Market）

> 上半：037 Analysis Report r26 c3 (Requirement Description)；`full`；44/50 token

```json
{
  "tc_id": "newR1L-DD-C002",
  "req_id": "SWE1-RA-Driver_Distraction-018",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot obtain valid VC_Trans_Equipped or PresentGear input\nCase [Exception]the transmission configuration or dynamic gear input required for judgment is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Fail-safe: the gear message is stopped and pairing is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 4 (ATX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)\n2. Open \"Pairing (1st time)\", then leave it\n3. Stop transmitting the message \"PT_SYSTEM_FD_1\" and let the input timeout elapse\n4. Open \"Pairing (1st time)\" again and check that it does not open",
  "expected_result": "1. The signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ is carried on the bus at 12 (Park)\n2. \"Pairing (1st time)\" opens and its view is displayed, and the previous screen is shown again after leaving it\n3. The message \"PT_SYSTEM_FD_1\" is no longer present on the bus and the input timeout window has elapsed\n4. \"Pairing (1st time)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915121",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，判定所需之車輛訊號消失時，fail-safe 使受限 feature 不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Pairing (1st time)\"（p7 top=304（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**（停送承載訊息），依 profile §3.2「逐 leaf 依 037 AC2 原文定」——本列 AC2 逐字書 `cannot obtain valid … input`，其 Method 逐字書 `Stop or suppress … updates` 與 `After the agreed input timeout`。**所停之訊號取該 source AC1 所條件之訊號**（下放包 15 §3.4）—— 判定所需之訊號即 AC1 之條件訊號。**PROXI 參數不作失效標的**（其為組態非訊號，停送無從施加）——故 037 Method 所列之另一選項（`make VC_Trans_Equipped unavailable`）不取。步驟 2 先確認訊號正常時該 feature 可用，否則末步之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**基準態取該 source 家族之「可解除」側** —— AC2 之原文**未條件於檔位或手煞之值**（其僅書 `required … input is unavailable`），故基準之選定為測試佈置，非對需求之主張，不構成擴入 sibling（IN §8.2.1）。本列所停者為檔位訊息 \"PT_SYSTEM_FD_1\"。市場 `PROXI Country_Code = 91`（確定值）；變速箱型式依 R-DD19 掛 [ASSUMPTION A-DD8]／[ASSUMPTION A-DD9]。速度訊號源壓於 `0`，排除基準速度規則之干擾，不掛 A-DD6。**本列之 037 原文與 `newR1L-DD-C004`（`-020`） 逐字全等**（A-DD7 組 3（`-018`／`-020`））——其區別僅在取樣 feature 與追溯 ID，**不得以取樣之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA 路徑 037 本列未書，寫入即造值；**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位**（R-DD19(c) 硬邊界）。"
}
```

### newR1L-DD-C003 —— `SWE1-RA-Driver_Distraction-019`（P0／Hong Kong Market）

> 上半：037 Analysis Report r27 c3 (Requirement Description)；`full`；39/50 token

```json
{
  "tc_id": "newR1L-DD-C003",
  "req_id": "SWE1-RA-Driver_Distraction-019",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains valid VC_Trans_Equipped and PresentGear inputs\nCase [Normal]VC_Trans_Equipped is Automatic and PresentGear is not P\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Automatic transmission with the gear selector away from Park)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 4 (ATX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 15 (Drive)\n2. Open \"Reconfigurable menu bar\" and check that it does not open",
  "expected_result": "1. The signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ is carried on the bus at 15 (Drive)\n2. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915122",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "決策表 (Decision Table Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，自排車之受限判定 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列），非黃標、非 NAV 系）。037 VC 之 `Listener receives a … notification` 依 profile §2.3 不入 ER，改以該 feature 之可及性承載。關鍵情境條件：市場 `PROXI Country_Code = 91`（確定值，A-DD5 已撤，不掛 marker）；變速箱型式依 **R-DD19** 之乙案，施加路徑掛 [ASSUMPTION A-DD8]、代表值掛 [ASSUMPTION A-DD9]（`4 (ATX)`）；檔位取 **`15 (Drive)`** —— 037 書 `<> [P]` 為一**類**，類內任一成員皆合法；於非 P 之 17 個成員中取行車常態檔位，`0 (Initialize)` 與 `31 (SNA)` 不取（前者為初始化態、後者為訊號不可用，取之會把「檔位非 P」與「檔位未知」混為一談），`13 (Neutral)`／`14 (Reverse)` 亦合法而未取。**類內取樣非假設，不掛 marker**（T21a）。速度訊號源壓於 `0 (0.0000 km/h)` —— **排除基準速度規則之干擾**，使觀察可歸因於檔位；0 非門檻值，**不掛 A-DD6**。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位** —— 其歸屬為 DR-DD6 之未決問題，R-DD19(c) 定為硬邊界；fail-safe 面由同 source 之 AC2 列承載。"
}
```

### newR1L-DD-C004 —— `SWE1-RA-Driver_Distraction-020`（P1／Hong Kong Market）

> 上半：037 Analysis Report r28 c3 (Requirement Description)；`full`；44/50 token

```json
{
  "tc_id": "newR1L-DD-C004",
  "req_id": "SWE1-RA-Driver_Distraction-020",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot obtain valid VC_Trans_Equipped or PresentGear input\nCase [Exception]the transmission configuration or dynamic gear input required for judgment is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Fail-safe: the gear message is stopped and the menu-bar view is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 4 (ATX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)\n2. Open \"Reconfigurable menu bar\", then leave it\n3. Stop transmitting the message \"PT_SYSTEM_FD_1\" and let the input timeout elapse\n4. Open \"Reconfigurable menu bar\" again and check that it does not open",
  "expected_result": "1. The signal $PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ is carried on the bus at 12 (Park)\n2. \"Reconfigurable menu bar\" opens and its view is displayed, and the previous screen is shown again after leaving it\n3. The message \"PT_SYSTEM_FD_1\" is no longer present on the bus and the input timeout window has elapsed\n4. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915122",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，判定所需之車輛訊號消失時，fail-safe 使受限 feature 不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列））。關鍵情境條件：失效形態取**匯流排逾時**（停送承載訊息），依 profile §3.2「逐 leaf 依 037 AC2 原文定」——本列 AC2 逐字書 `cannot obtain valid … input`，其 Method 逐字書 `Stop or suppress … updates` 與 `After the agreed input timeout`。**所停之訊號取該 source AC1 所條件之訊號**（下放包 15 §3.4）—— 判定所需之訊號即 AC1 之條件訊號。**PROXI 參數不作失效標的**（其為組態非訊號，停送無從施加）——故 037 Method 所列之另一選項（`make VC_Trans_Equipped unavailable`）不取。步驟 2 先確認訊號正常時該 feature 可用，否則末步之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**基準態取該 source 家族之「可解除」側** —— AC2 之原文**未條件於檔位或手煞之值**（其僅書 `required … input is unavailable`），故基準之選定為測試佈置，非對需求之主張，不構成擴入 sibling（IN §8.2.1）。本列所停者為檔位訊息 \"PT_SYSTEM_FD_1\"。市場 `PROXI Country_Code = 91`（確定值）；變速箱型式依 R-DD19 掛 [ASSUMPTION A-DD8]／[ASSUMPTION A-DD9]。速度訊號源壓於 `0`，排除基準速度規則之干擾，不掛 A-DD6。**本列之 037 原文與 `newR1L-DD-C002`（`-018`） 逐字全等**（A-DD7 組 3（`-018`／`-020`））——其區別僅在取樣 feature 與追溯 ID，**不得以取樣之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA 路徑 037 本列未書，寫入即造值；**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位**（R-DD19(c) 硬邊界）。"
}
```

### newR1L-DD-C005 —— `SWE1-RA-Driver_Distraction-021`（P1／Hong Kong Market）

> 上半：037 Analysis Report r29 c3 (Requirement Description)；`full`；38/50 token

```json
{
  "tc_id": "newR1L-DD-C005",
  "req_id": "SWE1-RA-Driver_Distraction-021",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains valid VC_Trans_Equipped and PARK_BRK_EGD inputs\nCase [Normal]VC_Trans_Equipped is Manual and PARK_BRK_EGD is ON\nThen DD Service sets the Lock Out State to NOT_RESTRICTED and notifies the subscribed Listener\n(Manual transmission with the parking brake applied)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 1 (MTX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $BCM_FD_9.ParkBrakeSts$ = 1 (ON) [ASSUMPTION A-DD2]\n2. Open \"Edit phone book (speller input)\" and check that it opens",
  "expected_result": "1. The signal $BCM_FD_9.ParkBrakeSts$ is carried on the bus at 1 (ON) [ASSUMPTION A-DD2]\n2. \"Edit phone book (speller input)\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915123",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "決策表 (Decision Table Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，手排車之解除判定 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Edit phone book (speller input)\"（p7 top=291（Phone 列），非黃標、非 NAV 系）。037 VC 之 `Listener receives a … notification` 依 profile §2.3 不入 ER，改以該 feature 之可及性承載。關鍵情境條件：市場 `PROXI Country_Code = 91`（確定值，A-DD5 已撤，不掛 marker）；變速箱型式依 **R-DD19** 之乙案，施加路徑掛 [ASSUMPTION A-DD8]、代表值掛 [ASSUMPTION A-DD9]（`1 (MTX)`）；手煞訊號名依 **R-DD18** 採認上游書面回覆之 `PARK_BRK_EDG`，其 CAN 對應為 T19c 實測所得，規範欄未更正故掛 [ASSUMPTION A-DD2]。速度訊號源壓於 `0 (0.0000 km/h)` —— **排除基準速度規則之干擾**，使觀察可歸因於手煞；0 非門檻值，**不掛 A-DD6**。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位** —— 其歸屬為 DR-DD6 之未決問題，R-DD19(c) 定為硬邊界；fail-safe 面由同 source 之 AC2 列承載。"
}
```

### newR1L-DD-C006 —— `SWE1-RA-Driver_Distraction-022`（P1／Hong Kong Market）

> 上半：037 Analysis Report r30 c3 (Requirement Description)；`full`；43/50 token

```json
{
  "tc_id": "newR1L-DD-C006",
  "req_id": "SWE1-RA-Driver_Distraction-022",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot obtain valid VC_Trans_Equipped or PARK_BRK_EGD input\nCase [Exception]the transmission configuration or parking-brake input required for judgment is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Fail-safe: the parking-brake message is stopped and the phone book is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 1 (MTX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $BCM_FD_9.ParkBrakeSts$ = 1 (ON) [ASSUMPTION A-DD2]\n2. Open \"Edit phone book (speller input)\", then leave it\n3. Stop transmitting the message \"BCM_FD_9\" and let the input timeout elapse\n4. Open \"Edit phone book (speller input)\" again and check that it does not open",
  "expected_result": "1. The signal $BCM_FD_9.ParkBrakeSts$ is carried on the bus at 1 (ON) [ASSUMPTION A-DD2]\n2. \"Edit phone book (speller input)\" opens and its view is displayed, and the previous screen is shown again after leaving it\n3. The message \"BCM_FD_9\" is no longer present on the bus and the input timeout window has elapsed\n4. \"Edit phone book (speller input)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915123",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，判定所需之車輛訊號消失時，fail-safe 使受限 feature 不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Edit phone book (speller input)\"（p7 top=291（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**（停送承載訊息），依 profile §3.2「逐 leaf 依 037 AC2 原文定」——本列 AC2 逐字書 `cannot obtain valid … input`，其 Method 逐字書 `Stop or suppress … updates` 與 `After the agreed input timeout`。**所停之訊號取該 source AC1 所條件之訊號**（下放包 15 §3.4）—— 判定所需之訊號即 AC1 之條件訊號。**PROXI 參數不作失效標的**（其為組態非訊號，停送無從施加）——故 037 Method 所列之另一選項（`make VC_Trans_Equipped unavailable`）不取。步驟 2 先確認訊號正常時該 feature 可用，否則末步之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**基準態取該 source 家族之「可解除」側** —— AC2 之原文**未條件於檔位或手煞之值**（其僅書 `required … input is unavailable`），故基準之選定為測試佈置，非對需求之主張，不構成擴入 sibling（IN §8.2.1）。本列所停者為手煞訊息 \"BCM_FD_9\"。市場 `PROXI Country_Code = 91`（確定值）；變速箱型式依 R-DD19 掛 [ASSUMPTION A-DD8]／[ASSUMPTION A-DD9]；手煞訊號名依 R-DD18 掛 [ASSUMPTION A-DD2]。速度訊號源壓於 `0`，排除基準速度規則之干擾，不掛 A-DD6。**本列之 037 原文與 `newR1L-DD-C008`（`-024`） 逐字全等**（A-DD7 組 4（`-022`／`-024`））——其區別僅在取樣 feature 與追溯 ID，**不得以取樣之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA 路徑 037 本列未書，寫入即造值；**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位**（R-DD19(c) 硬邊界）。"
}
```

### newR1L-DD-C007 —— `SWE1-RA-Driver_Distraction-023`（P0／Hong Kong Market）

> 上半：037 Analysis Report r31 c3 (Requirement Description)；`full`；38/50 token

```json
{
  "tc_id": "newR1L-DD-C007",
  "req_id": "SWE1-RA-Driver_Distraction-023",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains valid VC_Trans_Equipped and PARK_BRK_EGD inputs\nCase [Normal]VC_Trans_Equipped is Manual and PARK_BRK_EGD is OFF\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Manual transmission with the parking brake released)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 1 (MTX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $BCM_FD_9.ParkBrakeSts$ = 0 (OFF) [ASSUMPTION A-DD2]\n2. Open \"DND Customize auto reply message\" and check that it does not open",
  "expected_result": "1. The signal $BCM_FD_9.ParkBrakeSts$ is carried on the bus at 0 (OFF) [ASSUMPTION A-DD2]\n2. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915124",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "決策表 (Decision Table Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，手排車之受限判定 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"DND Customize auto reply message\"（p7 top=317（DND 列），非黃標、非 NAV 系）。037 VC 之 `Listener receives a … notification` 依 profile §2.3 不入 ER，改以該 feature 之可及性承載。關鍵情境條件：市場 `PROXI Country_Code = 91`（確定值，A-DD5 已撤，不掛 marker）；變速箱型式依 **R-DD19** 之乙案，施加路徑掛 [ASSUMPTION A-DD8]、代表值掛 [ASSUMPTION A-DD9]（`1 (MTX)`）；手煞訊號名依 **R-DD18** 採認上游書面回覆之 `PARK_BRK_EDG`，其 CAN 對應為 T19c 實測所得，規範欄未更正故掛 [ASSUMPTION A-DD2]。速度訊號源壓於 `0 (0.0000 km/h)` —— **排除基準速度規則之干擾**，使觀察可歸因於手煞；0 非門檻值，**不掛 A-DD6**。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位** —— 其歸屬為 DR-DD6 之未決問題，R-DD19(c) 定為硬邊界；fail-safe 面由同 source 之 AC2 列承載。"
}
```

### newR1L-DD-C008 —— `SWE1-RA-Driver_Distraction-024`（P1／Hong Kong Market）

> 上半：037 Analysis Report r32 c3 (Requirement Description)；`full`；43/50 token

```json
{
  "tc_id": "newR1L-DD-C008",
  "req_id": "SWE1-RA-Driver_Distraction-024",
  "test_group": "Driver Distraction",
  "test_set": "Hong Kong Market",
  "test_item": "AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot obtain valid VC_Trans_Equipped or PARK_BRK_EGD input\nCase [Exception]the transmission configuration or parking-brake input required for judgment is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED and notifies the subscribed Listener\n(Fail-safe: the parking-brake message is stopped and the auto reply editor is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)\n2. PROXI Country_Code = 91\n3. PROXI Gear_Box_Type = 1 (MTX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $BCM_FD_9.ParkBrakeSts$ = 1 (ON) [ASSUMPTION A-DD2]\n2. Open \"DND Customize auto reply message\", then leave it\n3. Stop transmitting the message \"BCM_FD_9\" and let the input timeout elapse\n4. Open \"DND Customize auto reply message\" again and check that it does not open",
  "expected_result": "1. The signal $BCM_FD_9.ParkBrakeSts$ is carried on the bus at 1 (ON) [ASSUMPTION A-DD2]\n2. \"DND Customize auto reply message\" opens and its view is displayed, and the previous screen is shown again after leaving it\n3. The message \"BCM_FD_9\" is no longer present on the bus and the input timeout window has elapsed\n4. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915120\nCFTS022-4915124",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：香港市場條件下，判定所需之車輛訊號消失時，fail-safe 使受限 feature 不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"DND Customize auto reply message\"（p7 top=317（DND 列））。關鍵情境條件：失效形態取**匯流排逾時**（停送承載訊息），依 profile §3.2「逐 leaf 依 037 AC2 原文定」——本列 AC2 逐字書 `cannot obtain valid … input`，其 Method 逐字書 `Stop or suppress … updates` 與 `After the agreed input timeout`。**所停之訊號取該 source AC1 所條件之訊號**（下放包 15 §3.4）—— 判定所需之訊號即 AC1 之條件訊號。**PROXI 參數不作失效標的**（其為組態非訊號，停送無從施加）——故 037 Method 所列之另一選項（`make VC_Trans_Equipped unavailable`）不取。步驟 2 先確認訊號正常時該 feature 可用，否則末步之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**基準態取該 source 家族之「可解除」側** —— AC2 之原文**未條件於檔位或手煞之值**（其僅書 `required … input is unavailable`），故基準之選定為測試佈置，非對需求之主張，不構成擴入 sibling（IN §8.2.1）。本列所停者為手煞訊息 \"BCM_FD_9\"。市場 `PROXI Country_Code = 91`（確定值）；變速箱型式依 R-DD19 掛 [ASSUMPTION A-DD8]／[ASSUMPTION A-DD9]；手煞訊號名依 R-DD18 掛 [ASSUMPTION A-DD2]。速度訊號源壓於 `0`，排除基準速度規則之干擾，不掛 A-DD6。**本列之 037 原文與 `newR1L-DD-C006`（`-022`） 逐字全等**（A-DD7 組 4（`-022`／`-024`））——其區別僅在取樣 feature 與追溯 ID，**不得以取樣之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA 路徑 037 本列未書，寫入即造值；**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位**（R-DD19(c) 硬邊界）。"
}
```

---

## 7. 未結 DR 清單（狀態依 §二 修訂後）

| 級 | DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|---|
| **必發** | **DR-DD1** | DRAFTED（含 SYSAD 引文 ＋ **本輪新增 LATAM 表述之問**）| `-025`~`-028`（4）| **凍結維持** |
| **必發** | **DR-DD5** | DRAFTED（**末行已改**：陳述假設生成而非 on hold）| `-017`~`-024`（8）| **不阻斷** —— 乙案已解凍 |
| **必發** | **DR-DD6** | DRAFTED（**末行已改** ＋ **本輪新增判準句**）| `-017`~`-024`（8）| **不阻斷** —— 乙案已解凍 |
| 緩發 | DR-DD2 | DRAFTED（格式更正件）| `-021`~`-024`（4）| 不阻斷；施加名已由 R-DD18 解 |
| 緩發 | DR-DD4 | PARTIALLY ANSWERED／縮為一問 | 9 列書 MPH 者 | 不阻斷 |
| 緩發 | DR-DD7 | DRAFTED（4 組 11 leaf）| — | 不阻斷 |
| **結案** | ~~DR-DD3~~ | RESOLVED | `-017`~`-028`（12）| 解除 |

**DD5／DD6 之必發等級不變**（R-DD19(e)）—— 乙案是「未回覆期間怎麼做」，
不是「不必問」。

**待登（未代登）**：`-001`／`-002` 之激勵 DR（上繳 11 §5.4）；
[CG-DD1] 甲案之素材索取（上繳 11 §4.4）。

### 7.1 阻斷疊圖（本輪後）

```
-001 ~ -002  (2)   內部窮盡未得識別碼；應登 DR（乙式），**維持不入批次**
-003 ~ -008  (6)   B1（`Speed Monitoring`）
-009 ~ -012  (4)   pilot（`Lockout Enforcement`）
-013 ~ -016  (4)   B1（`Lockout Tables`）；[CG-DD1] 負向面未涵蓋
-017 ~ -024  (8)   **B2 已生成**（`Hong Kong Market`）；八則掛 A-DD8／A-DD9，
                   其中 021–024 另掛 A-DD2
-025 ~ -028  (4)   **凍結維持** —— 僅餘 A-DD1／DR-DD1
```

**已生成 22 TC ／ 28 leaf。** framework 六組中，組 2／3／4／5 已有產出；
組 1 待 DR，組 6 待 DD1。

---

## 8. 獨立自評

### 8.1 我做對的

- **溯源檢取代白名單。** 第 12 項一開始只是「B2 紅了」的技術問題，
  最省事的修法是把 `12`／`15` 加進白名單 —— 加完全綠，而且看起來合理。
  但那樣**沒有任何東西再檢查那兩個值的出處**。改成比對 `(raw, label)` 對
  之後，`12 (Parking)` 這種**白名單永遠抓不到**的錯才會紅。
- **反向對照做了六種。** 特別是第 4 種（標籤與 `VAL_` 不符）——
  那正是新檢相對於舊檢**唯一多出來的能力**，不驗它就等於沒證明改對了。
- **`-020`／`-024` 之基準態選擇寫進 reasoning 而非默默決定。**
  基準取「可解除側」看起來像擴入 sibling，**必須說明 AC2 原文未條件於該值**。
- **DD5／DD6 之 `on hold` 改了，DD1 之沒改。** 三處替換裡最容易錯的是
  「全部一起改」—— 而 DD1 之凍結未解，那句對它仍屬實。

### 8.2 我做糙的

- **生成器第一版把 `reasoning` 也納入 R-DD19(c) 之掃描**，於是自己攔下自己。
  照那版辦，就得把「為何排除 MTA／DDCT」從 reasoning 刪掉 ——
  **那正好刪掉讀者最需要的那一句。** 邊界是「不得作輸入」，不是「不得提及」。
- **第 13 項改完先漏了 PC 之訊號源行**，於是 pilot 與 B1 一起紅。
  是回頭看 `-009` 之 procedure 只有一次 `Send` 才想到 —— **轉換之「before」在 PC 裡**。

### 8.3 我拒絕做的

- **不把 `12`／`15` 加進白名單**（§5.2-2）。
- **不用 `MTA`／`DDCT` 作任何 TC 之 PC 或輸入**（R-DD19(c)），
  即使 `-017`~`-024` 之 037 原文只書 `[Automatic]`／`[Manual]` 二值、
  而 MTA／DDCT 落在哪一側「看起來」可推 —— 上繳 05 §3.5(甲) 已量測其不可推。
- **不取值域中 14 個未列舉之 raw**（§3.2）—— 無 `VAL_` 逐字可書。
- **不撤 DD5／DD6 之必發等級**（R-DD19(e)）。

### 8.4 一件我原本會漏的

`-020` 我原本要照 `-018` 複製，而 `-018` 之基準態是 P（其 source `-126` 即 P 側）。
複製到 `-020` 就變成「source 是非 P，而基準用 P」——**看起來是抄錯**。

回頭讀 037 才確定：**四列 AC2 逐字全等，且皆未條件於檔位之值**。
所以基準取 P 不是抄錯，是**唯一能讓 fail-safe 可觀察的佈置** ——
但這件事**必須寫在 reasoning 裡**，否則審查者只會看到「source 非 P、TC 用 P」。

---

## 9. 量測條件揭露（R-G8）

### 9.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| 20 錨點 | 工具解析出之 `ruling` 列數 | 本檔圍籬條文 20（19 現行 ＋ 1 留存）|
| 既有 19 條 sha8 未變 | 與上輪 tsv `sha8` 相同者 | 上輪之 19 條 |
| `VAL_` 18 項／非 P 17 項 | `VAL_ 263 GearEngagedForDisplay_PT` 之列舉數 | 值域 `[0\|31]` 共 32 個 raw（未列舉 14 個）|
| DR 修訂 3 處（落檔 4 次）| 2.1×1 ＋ 2.2×1 ＋ 2.3×2 | 三段修訂 |
| `on hold in SWQT` 殘留 1 | 替換後仍存之出現次數 | 替換前 3 次（DD1／DD5／DD6）|
| B2 八則之 `Gear_Box_Type` 值 | 四交付欄中之相異值 = `1 (MTX)`／`4 (ATX)` | PROXI Table 六值（`0,1,2,3,4,5`）|
| 反向對照 6/6 被攔 | 注入後有對應項 FAIL 者 | 6 種注入 |
| 自檢 24 PASS／2 N/A／0 FAIL | 各判別之檢項數 | **26 檢**（IN §9 十七項 ＋ 追加 9）|

### 9.2 界線

- **溯源檢之 DBC 查表**以 `BO_ <id> <MSG>` ＋ 其後之 `VAL_ <id> <SIG>` 為鍵，
  **只查二綁定 DBC**。若某訊號之列舉定義於 `VAL_TABLE_`（間接），**查不到而判為不可溯**
  —— 偏嚴，不會放過。
- **溯源檢之正則為 `(\$sig\$)[^\n]*?(?:=|at) (\d+) \((label)\)`**，
  即 raw 與其標籤須**同行**且訊號名在其前。**若寫法換行或倒裝，會判為裸 raw（紅）**
  —— 同樣偏嚴。
- **`91`（`PROXI Country_Code`）於裸 raw 檢中列為例外** —— 其為十進位值而
  PROXI `Format` r468 之 Table 未列 Hong Kong（上繳 06 §DR-DD3 已載），
  故無括號標籤可書。**此為明列之例外，非漏檢。**
- **第 13 項之機械推導**只認三種形態（停送／同訊號多值／條件 ≥2），
  其餘落入 `功能測試`。**若日後出現需 BVA／等價劃分／組合測試之 TC，該項會誤判**
  —— 屆時須擴充，非現況之缺陷。
- **A-DD7 之組別於 B2 為人工標註**（`-018`/`-020` 組 3、`-022`/`-024` 組 4），
  未於本輪重跑 18 欄分組驗證（上繳 09 §5 已測）。

### 9.3 檔與開啟方式

| 標的 | 開啟 |
|---|---|
| `RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`generated/batch_b2.json`／`scripts/*` | **本輪寫入**（私有路徑）|
| 037／二綁定 DBC／`framework.md` | **唯讀** |
| profile | **未開** —— §四 之 profile 更新為分析層自辦 |
| `docs/fw036/RULINGS.sha.tsv` | **未開**（T17b 停止）|
| 工作簿 | **未開** |

### 9.4 本輪未量測者

- **profile §3 之 `$VC_Trans_Equipped$` 列是否已由分析層改為 CONDITIONAL** —— 未讀該檔。
- **`-025`~`-028`** —— 凍結維持，非本輪範圍。
- **`-001`／`-002`** —— 待 DR。
- **B2 八則未經工作簿寫回驗證** —— 拘束「不寫回」。
- **PROXI `Gear_Box_Type` 之 byte 101／bit 0–2 於本輪未重測** —— 引上繳 05 §3.1 之實測值。

---

## 10. 待分析層／Pei

| # | 事項 | 現況 |
|---|---|---|
| 1 | profile §3 `$VC_Trans_Equipped$` 改 CONDITIONAL ＋ 補非 P 代表值 | §四 自辦；T21a 已回報 `15 (Drive)` |
| 2 | profile §3 PARK_BRK 列回填 | 上繳 10 §9-1，**三輪未獲回覆** |
| 3 | profile §3 `Country_Code` 之 A-DD5 標記移除 | 上繳 10 §9-2，**三輪未獲回覆**（B2 已按「確定值、不掛 marker」辦）|
| 4 | `-001`／`-002` 之 DR（乙式）| 內部已窮盡；文稿待擬 |
| 5 | Body OFF 與 power 線 TLM status 之同一性 | 執行層不判 |
| 6 | [CG-DD1] 之解除 | 三案 |
| 7 | tsv 重生之解除 | T17b 停止；本線 **20 列** |
| 8 | `-025`~`-028` | DD1 未回覆，凍結維持 |
