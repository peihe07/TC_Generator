# DATA REQUESTS — driver_distraction (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/driver_distraction/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 標的 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| **DR-DD1** | 037 作者／上游 | **DRAFTED（下放包 20 §三 整段替換；確認件）**（待 Pei 發送）| `-025`~`-028`（4） | 該 4 leaf **範圍外**（R-DD25(b)），不生成 TC；**不阻斷交付** | A-DD1（**CLOSED-BY-SCOPE**）| **必發**（文件缺陷）—— 037 該四列把範圍外之 LATAM source 接上 Hong Kong 文字 |
| **DR-DD2** | 上游（CFTS022 作者）| **DRAFTED（格式更正件，緩發）** | `-021`~`-024`（4） | **不阻斷** —— 施加名依 **R-DD18** 採認為 `PARK_BRK_EDG`；所問改為規範欄之更正 | **A-DD2** | 低 |
| ~~**DR-DD3**~~ | 上游（素材提供）| **RESOLVED**（Pei 2026-08-28 確認識別）| `-017`~`-028`（12） | **解除** —— `Country_Code = 91` 為確定值，A-DD5 撤銷 | ~~A-DD5~~ | — |
| **DR-DD4** | 上游（CFTS022／037 作者）| **PARTIALLY ANSWERED**（單位 km/h）／縮為一問，**緩發** | **9 列書 MPH 門檻者**：`-003`／`-005`／`-007`／`-009`／`-011`／`-013`／`-015`（7，可生成）＋ `-025`／`-027`（2，**已判範圍外**，R-DD25(b)）| 不阻斷生成；ER 之 raw 數值標 A-DD6 | **A-DD6** | 中 |
| **DR-DD5** | 上游（LID 維護者）| **DRAFTED**（待 Pei 發送）| `-017`~`-024`（8）| **已由 R-DD19 乙案解凍**，B2 八則（`-017`~`-024`）已產出並掛 `[ASSUMPTION A-DD8]`；回覆不符時回修為機械換值 | — | **必發** —— 與 DR-DD6 並列 |
| **DR-DD6** | 上游（CFTS022 作者）| **DRAFTED**（待 Pei 發送）| `-017`~`-024`（8）| **已由 R-DD19 乙案解凍**，B2 八則已產出並掛 `[ASSUMPTION A-DD9]`；`MTA(2)`／`DDCT(3)` 仍為 R-DD19(c) 硬邊界 | — | **必發** —— 組 1／2 待此 |
| **DR-DD7** | 上游（037 作者）| **DRAFTED**（待 Pei 發送）| 文稿問 `-010`／`-012`；**實測涉 11 leaf** | **不阻斷** —— 品質旗標；**緩發** | **A-DD7** | 低 |
| **DR-DD8** | 上游（CFTS022 作者／素材提供）| **DRAFTED**（待 Pei 發送）| **`-013`／`-015`** 之負向側（表外功能；範圍依下放包 17 §四 10-5）| **不阻斷生成** —— 負向側記為 `[CG-DD1]` 涵蓋缺口；亦為取樣只有 5 列可用之根因 | **[CG-DD1]** | **必發** —— 驗證方法步驟 4 待此 |
| **DR-DD9** | 上游（CFTS022／037 作者）| **DRAFTED**（待 Pei 發送；**文稿不動**）| `-001`／`-002`（2，**已產出**）| **不阻斷** —— `-002` 依 **R-DD20 v3(c)** 已可出貨（`$` 行撤，非規格缺件）；process 之具名為**品質改善項**，回覆到位後得補入步驟 | **A-DD10** | **緩發**（下放包 19 §二 R-DD20 v3(d) 降級）|

**發送清單（下放包 13 §六）**：

| 級 | DR | 狀態 |
|---|---|---|
| **必發** | **DD1**（確認件）、**DD5**、**DD6**、**DD8** | **DD1 已不卡 leaf** —— `-025`~`-028` 判範圍外（R-DD25(b)），該 DR 改為文件缺陷之確認件；DD5／DD6 已由 R-DD19 乙案解凍生成（**必發等級不減**，R-DD19(e)）；DD8 為 `-013`／`-015` 之負向側（範圍依下放包 17 §四 10-5），亦為取樣只有 5 列可用之根因。**四筆皆不阻斷出貨。** |
| 緩發 | DD2（格式更正件）、DD4（縮為一問）、DD7（品質旗標）、**DD9**（下放包 19 §二 降級）| 皆非阻斷 |
| **結案** | **DD3** | **RESOLVED**（下放包 13 §二）|

**八筆未發送；DD3 已結案。**

> **自下放包 19 §二 R-DD20 v3(c)(d) 起，未結 DR 中已無阻斷出貨者** ——
> DD9 為最後一筆（`-002` 之 `PENDING`），該包撤其佔位並降為緩發。

> **DD5／DD6 之「阻斷」欄已於本輪改寫**（下放包 16 §七 之拘束：
> 不得向上游或台帳陳述已失實之狀態）。上繳 12 §2.3 改的是 **DR 文稿末行**，
> 本表之 `Batch impact` 欄當時未同步 —— 仍書「該 8 leaf 不入批次」，
> 而 B2 八則已於上輪產出。**同一過期陳述之第二處，本輪補正。**

> **DR-DD5 已於下放包 09 §二 裁定建檔**（保留號轉正式條目）。
> 裁定所據者為 T13a 之「**不合慣例**」量測，非「哪一列看起來對」。
>
> **DR-DD5 與 DR-DD6 為獨立阻斷**：DD5 定「**有無施加路徑**」，
> DD6 定「**值如何對應**」。任一單獨回覆仍不解另一 —— 即使 DD5 裁定
> r421 為準（有路徑），`[Manual]` 對 `Gear_Box_Type` 六值制之歸屬仍懸；
> 即使 DD6 給出歸屬，r420 為準時該歸屬無處施加。**二者須分別追**
> （同 DR-DD1／DR-DD3 之理）。

---

## DR-DD1 —— 市場條件衝突（`-025`~`-028`）

- **標的**：037 作者／上游
- **狀態**：DRAFTED（**文稿於下放包 20 §三 整段替換**；待 Pei 發送）
- **性質**：**釐清件 → 確認件**（範圍裁定後，「香港還是拉美」已由 Tier 3 答；
  餘下者為**文件缺陷** —— 037 該四列把範圍外之 LATAM source 接上 Hong Kong 文字）
- **等級**：**必發**（文件缺陷）　**阻斷：無** —— 交付不再等其回覆
- **範圍**：`-025`~`-028` 四 leaf **範圍外**（R-DD25(b)），非凍結；A-DD1 已 `CLOSED-BY-SCOPE`
- **⚠ 與 DR-DD3 為二個獨立阻斷，不可互抵**（下放包 05 §四 採認執行層所指）：
  **DR-DD1 裁 HK 只定「市場為何」，仍不給出 `Country_Code` 之值。**
  即使 DR-DD1 先回，HK 段（`-017`~`-028`）仍卡於 DR-DD3。**二者須分別追。**

### 舊稿（**SUPERSEDED 2026-08-28，下放包 20 §三**）

**失實處（三項）**：

1. 末行 `Until clarified, the four rows are on hold in SWQT test case generation.`
   —— 範圍裁定後該四列**不是 on hold，是範圍外**（R-DD25(b)）
2. 主問「(a) Hong Kong、(b) LATAM、(c) both」—— **已由 Tier 3 答**（R-DD25(a)）
3. 末段「If the answer is (b) LATAM: please also specify how the market condition
   is expressed…」—— 其前提（可能裁 LATAM 而仍須生成）**不再成立**

> **一個過期的狀態陳述，比沒有狀態陳述更糟**（上繳包 12 §2.3 之同一形態）。

**留副本之依據（下放包 21 §四 10-4）**：前版只留指向
`docs/handoff/02_rulings_q1q6.md` §三 之位置，**而該處所存者為最初稿，非本次所替換之稿**
（本稿已含 SYSAD 引文段，為包 13 §五 縮問改稿後之版本，2020 字元）——
即**當時所指之位置根本取不到被替換的那一份**。
**台帳之自足性不應繫於他檔之位置**，故全文留存於此。

<details>
<summary>舊稿全文（2020 字元，SUPERSEDED；<b>不得引用</b>）</summary>

> **DR-DD1 — Market condition conflict for SWE1-RA-Driver_Distraction-025 ~ -028**
>
> In FM-WI-FSM-037-A03 (DD_SWE1, 2026-08-07), rows
> SWE1-RA-Driver_Distraction-025 through -028 cite source requirements
> `SYS-RA-Driver_Distraction-125` (section gate: "The requirements in the
> section shall be implemented if $Country_Code$ = [Hong Kong]") together
> with `SYS-RA-Driver_Distraction-132` / `-133` (5 MPH lock / 3 MPH unlock
> thresholds). Their Requirement Descriptions and Verification Criteria
> also state "When Country_Code is Hong Kong".
>
> However, in CFTS022 SYSRA (FM-WI-FSM-035-A02), `-132` and `-133` are
> located under the **LATAM Market Regulations** heading (`-130`), whose
> applicability note (`-131`) states the section applies to the LATAM
> market only. The two sources are mutually exclusive on the market
> condition.
>
> Question: for SWE1 rows -025 ~ -028, should the market condition be
> (a) Hong Kong, (b) LATAM, or (c) both markets? If (c), please confirm
> whether separate SWE1 rows for the LATAM side will be added, since the
> current four rows carry Hong Kong wording only.
>
> Additionally, the System Architectural Design (FM-WI-FSM-015-A01)
> describes the speed-hysteresis judgment (separate lock and unlock
> thresholds) as a market-specific processor type **for LATAM**
> (`ProcessorType4to6 … for LATAM`; "Market-specific types (such as LATAM)
> evaluate restriction using speed hysteresis thresholds"), while the
> Hong Kong logic is described in terms of parking-brake state and gear
> selection. This is consistent with the CFTS022 section structure and
> inconsistent with the Hong Kong wording of SWE1 rows -025 ~ -028.
>
> If the answer is (b) LATAM: please also specify how the market condition
> is expressed for these rows — as a list of `$Country_Code$` values, or
> via the `Regulation_type` property referenced in the System Architectural
> Design. "LATAM" is a region, not a single country code, and the test
> cases need a concrete precondition value.
>
> Until clarified, the four rows are on hold in SWQT test case generation.

</details>

### 文稿（下放包 20 §三，逐字；**整段替換**）

> **DR-DD1 — Rows `-025` ~ `-028` derive from out-of-scope LATAM requirements
> while their text specifies Hong Kong**
>
> `SWE1-RA-Driver_Distraction-025` ~ `-028` in FM-WI-FSM-037-A03 cite
> `SYS-RA-Driver_Distraction-125` together with `-132` / `-133`. In CFTS022,
> `-132` / `-133` belong to the LATAM chapter, and the System Architectural
> Design describes the speed-hysteresis judgment they specify as a
> market-specific processor type for LATAM
> (`ProcessorType4to6 … for LATAM`), whereas the Hong Kong logic is
> described in terms of parking-brake state and gear selection.
>
> This programme covers NAFTA and does not cover LATAM; Hong Kong is in
> scope as a right-hand-drive market (`Market Config - R1`, row 97: RHD,
> Region APAC), not as a LATAM market. The behaviour specified by
> `-132` / `-133` is therefore not implemented in this programme.
>
> However, the Requirement Description, Verification Criteria and
> Verification Method of all four rows read `Country_Code is Hong Kong` /
> `Preset Country_Code to Hong Kong`.
>
> Question: please confirm that rows `-025` ~ `-028` should be removed or
> revised, since they combine an out-of-scope LATAM source requirement with
> Hong Kong wording. SWQT has recorded them as out of scope and has not
> generated test cases for them; the remaining 24 leaves are covered.

---

### ⚠ 執行層之複測補充（上繳包 01 §3）

**A-DD1 之主張已逐項複測成立**，且另得一項下放包文稿未載之證據：

| 037 列 | 所引之 source | CFTS022 之章歸屬 | 內部一致？ |
|---|---|---|---|
| `-017`~`-024`（8 列）| `-125` ＋ `-126`~`-129` | `-125`~`-129` **全在 `-123 Hong Kong Market Regulations` 下** | ✅ 一致 |
| **`-025`~`-028`（4 列）** | `-125` ＋ `-132`／`-133` | `-125` 在 HK 章、**`-132`／`-133` 在 `-130 LATAM Market Regulations` 下** | ❌ **不一致** |

**即：同一份 037 之作者，在 12 列上一致地以 `-125` 為 HK 之章閘；
唯獨最後 4 列把它接到 LATAM 章之需求上。**

此為**量測，非結論** —— 它使「配錯」之可能高於「有意雙市場」，
但**該判斷屬上游**。建議發送時附此表。

---

## DR-DD2 —— `$PARK_BRK_EGD$` 之拼法（`-021`~`-024`）—— **降轉為格式更正件**

- **標的**：上游（CFTS022 作者）
- **狀態**：**DRAFTED（格式更正件，緩發）**（下放包 13 §三；原為「請確認名稱」）
- **由來**：A-DD2；R-DD5 之 T6 逐訊號查對，五訊號中**唯一四庫皆查無者**
- **阻斷範圍**：**不阻斷**

### 降轉之依據 —— R-DD18

**R-DD18 已裁**：上游於其自身文件內留有**書面回覆**者，得採認該回覆所指之名
為**施加名**（此為 lookup ＋ 上游書面確認，非 R-DD5／R-13 所禁之語意代換）。

本案之書面回覆（CFTS022 `Basic Report` r129，逐字）：

```
SYS2 HARMAN Comments : …looks incorret. Does the expected LID name is "PARK_BRK_EDG".
SYS2 MD Feedback     : The LID which is referred here is $PARK_BRK_EDG$
```

**故本 DR 所問已非「名稱為何」（R-DD18 已答），而是「規範欄何時更正」** ——

| | 降轉前 | 降轉後 |
|---|---|---|
| 所問 | 請確認正確識別碼為何 | **請將規範欄與 `-129` 之 `EGD` 更正為 `EDG`** |
| 性質 | 名稱未定，施加路徑待決 | **格式更正件** |
| 級別 | 待發送 | **緩發**（§六 發送清單）|

### R-DD18(b) 之採認界線（逐條落實）

| 界線 | 落實 |
|---|---|
| 僅及於**施加路徑**（Procedure／ER 之訊號名）| `-021`~`-024` 之 Procedure／ER 用 `PARK_BRK_EDG` |
| `test_item` 上半 verbatim 照原文（含 `EGD`），不改字 | 上半不動 |
| 施加名之 CAN 對應**仍須自 LID 該列實測查得** | **T19c 已查**（**上繳包 10 §3**「T19c —— `LID CAN Mapping r1310` 全列傾印與 DBC 驗證」；不因勘誤成立而略過查證）|
| 規範欄未更正前，用及該施加路徑之 TC 標 `[ASSUMPTION A-DD2]` | 待 `-021`~`-024` 生成時施行 |
| 上游正式更正後撤該 marker | 待本 DR 之回覆 |

> **R-DD18(c) 不得反向援引**：本案之採認**全部**繫於「有書面回覆」這一件事。
> 無書面回覆之「看起來像筆誤」仍依 R-DD5／R-13 登 DR。

### 問

> In CFTS022 SYSRA (FM-WI-FSM-035-A02), rows `-128` and `-129` state the
> condition using `$PARK_BRK_EGD$`. This identifier is **not present** in
> `Logical Identifiers and CAN Mapping v1_76.xlsx`, in either DBC
> (`PDT27_E2A_R4_BHCAN` / `PDT27_E2A_R5_FDCAN8`), or in
> `PROXI_HDCC27_R3_20250424.xlsx`.
>
> The LID sheet `CAN Mapping` row 1310 carries **`PARK_BRK_EDG`**
> (mapped to `STATUS_BH_BCM1.ParkBrakeSts` on CAN-B and
> `BCM_FD_9.ParkBrakeSts` on CAN-FD) — the same letters with **`DG`
> transposed to `GD`**.
>
> CFTS022 itself already records this: on row `-128`, the
> `SYS2 HARMAN Comments` column reads *"…looks incorret. Does the expected
> LID name is \"PARK_BRK_EDG\"."* and the `SYS2 MD Feedback` column replies
> *"The LID which is referred here is $PARK_BRK_EDG$"*. The
> `SYS2 System-HW` and `SYS2 System-SW` columns on that row use
> `$PARK_BRK_EDG$`, while the normative `Description` column still uses
> `$PARK_BRK_EGD$`. **Row `-129` was not corrected at all** — its
> `System-SW` column still carries `$PARK_BRK_EGD$`.
>
> Question: is the correct identifier `PARK_BRK_EDG`? If so, should the
> `Description` columns of `-128` and `-129` (and the SWE1 rows derived from
> them, `-021`~`-024`) be corrected?

### ⚠ 執行層當時未自行採用 `EDG` —— 其理由與 R-DD18 之關係

當時之三項理由（保留為軌跡，**不刪**）：
- `Description` 為**規範欄**，其餘為註記／回饋欄 —— **二者位階不同**；
- `-129` **未被更正**，故「已定案」之推定不成立；
- R-DD5 明文「查無者逐項登 DR，**不得代以語意相近之他訊號**」（R-13）。

**R-DD18 未推翻上述任何一項**，而是把「採認」與「代換」分開：

- 第 1、2 項所指者為**規範欄之效力** —— R-DD18(b) 因此把採認**限於施加路徑**，
  `test_item` 上半仍照原文之 `EGD`，且未更正前須標 `[ASSUMPTION A-DD2]`。
  **三項理由在其各自的範圍內仍然成立。**
- 第 3 項所禁者為**自行推定**；本案有上游之書面回覆，**不屬自行推定**（R-DD18(a)）。

> 即：**當時不採是對的**（R-DD18 尚未存在，且採認之界線未定）；
> **現在採也是對的**（界線已由 R-DD18 劃出，且限於施加路徑）。
> 二者不衝突。

---

## DR-DD3 —— `CIP Market Configuration Table v*.xlsx`（標的為具名檔）

- **標的**：上游（素材提供）
- **狀態**：DRAFTED（下放包 05 §四；待 Pei 發送）
- **由來**：T9b／T10d
- **阻斷範圍**：`-017`~`-028`（HK 全段 12 leaf）之 Pre-Condition 缺
  `Country_Code` 之值

### 這不是問句，是索取一個具名檔

**指名來源**（逐字，`LID Proxi & Configuration r43` c7）：

> `See latest version of 'CIP Market Configuration Table v*.xlsx',
>  worksheet 'Marke…'`

### 實測依據

1. **PROXI `Format` r468** 之 `Country_Code` 值表**無 Hong Kong**：
   `0 = World／2 = USA／4 = Canada／14 = Mexico／16 = China Mainland／
   18 = Bahrain／97 = Iraq／104 = Jordan／108 = Kuwait／112 = Lebanon／
   149 = Oman／160 = Qatar／165 = Saudi Arabia／204 = UAE／215 = Yemen`
2. **該列 c18 自陳為部分列舉**：`See Country Code Table`
3. **該檔不在 `inputs/`、不在 `forms/`、不在任何已綁之 `reference`**

### 問

> Please provide the latest `CIP Market Configuration Table v*.xlsx`
> (worksheet 'Market…'), which `Logical Identifiers and CAN Mapping v1_76`
> (sheet `Proxi & Configuration`, row 43) names as the authoritative source
> for the `Country_Code` value domain.
>
> The PROXI file we hold (`PROXI_HDCC27_R3_20250424.xlsx`, sheet `Format`,
> row 468) lists 15 country values and **does not include Hong Kong**; that
> same row states `See Country Code Table`, i.e. its list is partial.
>
> Rows `SWE1-RA-Driver_Distraction-017` ~ `-028` require the Hong Kong value
> to state their Pre-Condition.

### ⚠ 與 DR-DD1 之關係

**二個獨立阻斷，不可互抵。** DR-DD1 定「市場為何」，DR-DD3 給「值為何」。
**本註記維持** —— DR-DD3 之值到位**不使 DR-DD1 得解**（下放包 06 §三 T-登）。

---

### 狀態更新（下放包 06，T-登）—— **ANSWERED-PENDING-CONFIRM**

**Pei 已置入 `forms/SR24 R1 Market Configuration Table v1.6.xlsx`**（2026-08-27）。

**`$Country_Code$` 之 Hong Kong 值 = `91`（十進位；Hex `5B`）** ——
執行層獨立重讀複核（T11b），六欄值與下放包 §1.1 **全數相符**：

| 欄（Excel）| 表頭 | 值 |
|---|---|---|
| H | `Destination Country` | `HONG KONG` |
| P | `Region (Ref-only for FGA Default Regional Settings)` | `APAC` |
| Q | `Value in <Dest> Signal - Hex` | `5B` |
| R | `Value in <Dest> Signal - Decimal` | `91` |
| **S** | **`PROXI3 <Country_Code>Signal - Decimal`** | **`91`** |
| BF | `Navigation Driver Distraction Lockout Disabled (Y=Yes, N=No)` | `N` |

**⚠ 尚未 RESOLVED** —— **Q9 待 Pei 確認**：本檔與 LID
`Proxi & Configuration r43` c7 所指名之 `CIP Market Configuration Table v*.xlsx`
**檔名不同**，二者是否同一屬文件識別之裁定。

- **Q9 = 是** → 本 DR **RESOLVED**，`Country_Code = 91` 入 profile §3
- **Q9 = 否／不確定** → 值仍取 `91` 但標 `[ASSUMPTION A-DD5]`，本 DR 續開

狀態：~~**ANSWERED-PENDING-CONFIRM**~~ → **RESOLVED**（下放包 13 §二）。

### 結案（下放包 13 §二；Pei 2026-08-28 確認識別）

**結案依據**（逐字）：

```
Pei 2026-08-28 確認 SR24 R1 MCT v1.6 即 LID 所指之 CIP MCT（取檔出處為其發佈渠道）
```

| 項 | 處置 |
|---|---|
| 本 DR | **RESOLVED** |
| **A-DD5** | **撤銷** —— 識別已確認，assumption 不復存在（條目不刪，狀態改 RESOLVED）|
| `Country_Code = 91` | 由 assumption 轉**確定值** |
| profile §3 該列 | 「凡用及者標 `[ASSUMPTION A-DD5]`」**移除**（分析層自辦）|
| 影響 leaf | `-017`~`-028` 之 A-DD5 標記義務解除；**pilot 四則與 B1 十則皆未用及，無回修** |

> **與 DR-DD1 之獨立性註記，其效力隨本 DR 結案而終** ——
> 該註記所防者為「以 DD3 之值到位推論 DD1 得解」。DD3 已結，
> ~~**`-025`~`-028` 之凍結僅餘 A-DD1／DR-DD1 一個成因。**~~
> **（下放包 20 更正）該四列已由 R-DD25(b) 判為範圍外，凍結狀態終止**
> —— 成因之討論隨之失效。

---

### 狀態確認（下放包 07 §三 R-DD8(c)，T-登）—— 維持 **ANSWERED-PENDING-CONFIRM**

Q9 已由 Pei 下放、分析層即裁為 **R-DD8**。**所裁者為「處置」，非「識別」** ——

| 項 | 結果 |
|---|---|
| 值 | `91`（十進位，Hex `5B`）**採用** |
| marker | 用及該值之 TC 一律標 `[ASSUMPTION A-DD5]`（新立，見 ANOMALIES） |
| 本 DR 狀態 | **不結案**，維持 `ANSWERED-PENDING-CONFIRM` |
| 轉 RESOLVED 之條件 | **上游確認二檔為同一份**；確認後始撤 A-DD5 |
| 與 DR-DD1 | **不變** —— 市場歸屬仍懸，二者為獨立阻斷，不互抵 |

> **不得以該表 c58（`Navigation Driver Distraction Lockout Disabled`）推論 A-DD1**
> —— 該欄對應 CFTS022 `-136`（Out of scope），範圍不同（下放包 06 §1.2）。

### ⚠ 引用格式之補正（R-DD6(c)，隨下放包 07 生效）

本節上文（§「這不是問句」、§「問」、§「⚠ 尚未 RESOLVED」）之
`LID Proxi & Configuration r43 c7` **只標列號、未標架構欄**，
依 R-DD6(c) **視同未標**。

- **保留原文不改**（DR 問稿為待發送之逐字文稿；R-TM13 精神：留痕不湮滅）
- **正確引用為**：`LID Proxi & Configuration r43 [Powernet 欄]`
  —— c7 屬 Powernet 帶（表頭 r2 c5 `Powernet`，涵 c5–c9）之 `Format` 欄（r3 c7）
- 往後新寫之引用一律具架構欄

---

## DR-DD4 —— 速度門檻之判定單位與取整規則（A-DD6）

- **標的**：上游（CFTS022／037 作者）
- **狀態**：**PARTIALLY ANSWERED (unit: km/h, per SYSAD)** ／ 改稿後 **DRAFTED（縮為一問，緩發）**（下放包 13 §五）
- **由來**：A-DD6；R-DD7(c) 之 raw 邊界為**分析層依 DBC 實測值所推導**
- **阻斷範圍**：**不阻斷生成** —— 依 R-DD7 產出之 TC 標 `[ASSUMPTION A-DD6]` 即可入批次
- **適用 leaf（本輪實測）**：037 `Analysis Report` 全 28 列中**書有 MPH 字樣者 9 列**

| leaf | 037 列 | MPH 字樣 | 備註 |
|---|---|---|---|
| `-003` | r11 | `5 MPH`／`3 MPH` | 可生成 |
| `-005` | r13 | `3 MPH` | 可生成 |
| `-007` | r15 | `5 MPH` | 可生成 |
| `-009` | r17 | `5 MPH` | 可生成 |
| `-011` | r19 | `5 MPH` | 可生成 |
| `-013` | r21 | `5 MPH` | 可生成 |
| `-015` | r23 | `5 MPH` | 可生成 |
| `-025` | r33 | `5 MPH` | **範圍外**（R-DD25(b)）—— 不生成，故不帶 marker |
| `-027` | r35 | `3 MPH` | **範圍外**（R-DD25(b)）—— 同上 |

  其偶數配對列（`-004`／`-006`／`-008`／`-026`／`-028`）為 **AC2 之
  訊號失效／逾時分支**，文中無門檻值 —— **A-DD6 不及於彼**。

  > **即：A-DD6 之波及面比 A-DD1 廣。** 7 列不在凍結名單內卻要帶 marker，
  > 這 7 列是 pilot 會先碰到的。
  >
  > **（下放包 20 更正）** `-025`／`-027` 轉範圍外後**不生成、不帶 marker**，
  > 故 A-DD6 之實際波及面收為 **7 列**（`-003`／`-005`／`-007`／`-009`／`-011`／`-013`／`-015`），
  > 與已交付產物之實測相符（pilot 2 ＋ B1 5）。
- **回修範圍（受限）**：DR 回覆若與 R-DD7(c) 不同，
  **只動速度類 leaf 之 ER 數值，不動其結構**

### 實測依據

綁定匯流排之速度訊號（`LID Proxi & Configuration` 之 `$Speedometer$`，
ATLANTIS 欄，下放包 03 T9a 實測）：

```
STATUS_CCAN3.VehicleSpeedVSOSig   13 bit, factor 0.0625, unit Km/h
```

`1 MPH = 1.609344 km/h`（單位定義，IN §8.4.1 domain constant，援用不構成造值）：

```
5 MPH = 8.04672 km/h  → raw 128.74752   ← 不落於整數格
3 MPH = 4.828032 km/h → raw  77.248512  ← 不落於整數格
```

**即此匯流排上不存在「等於 5 MPH」之格。**

### 問

> **DR-DD4 — Evaluation unit and rounding rule for the 5 MPH / 3 MPH
> Driver Distraction lockout thresholds**
>
> CFTS022 SYSRA (FM-WI-FSM-035-A02) rows `-132` / `-133`, and the SWE1 rows
> derived from them, state the lockout thresholds in **MPH**
> ("equal or greater than 5MPH" to lock, "equal or less than 3MPH" to unlock).
>
> The vehicle-speed signal bound to our test bench is
> `STATUS_CCAN3.VehicleSpeedVSOSig` (13 bit, factor **0.0625**, unit **Km/h**),
> i.e. raw = km/h x 16. Converting with the SI definition
> `1 MPH = 1.609344 km/h`:
>
> ```
> 5 MPH = 8.04672 km/h   -> raw 128.74752
> 3 MPH = 4.828032 km/h  -> raw  77.248512
> ```
>
> **Neither threshold lands on a representable raw value**, so there is no
> bus value that is exactly 5 MPH or exactly 3 MPH. For test-case generation
> we currently take the first representable step on the crossing side implied
> by each inequality:
>
> | Requirement | raw | km/h | MPH |
> |---|---|---|---|
> | lock, `>= 5 MPH`   | **129** | 8.0625 | 5.0097 |
> | (step below)       | 128 | 8.0000 | 4.9710 |
> | unlock, `<= 3 MPH` | **77**  | 4.8125 | 2.9903 |
> | (step above)       | 78  | 4.8750 | 3.0292 |
>
> Questions:
> 1. In what unit does the DUT evaluate the thresholds — raw counts, km/h,
>    or MPH after an internal conversion?
> 2. What conversion factor and rounding rule does the DUT apply
>    (truncate / round-half-up / a fixed integer km/h threshold)?
> 3. Are the boundary raw values 129 (lock) and 77 (unlock) correct for
>    pass/fail judgement, or should different values be used?
>
> The difference is one raw step (~0.04 MPH) but it decides the verdict of
> the boundary-value test cases directly. Until answered, the affected test
> cases carry an explicit assumption marker.

### 縮問改稿（下放包 13 §五）—— 三問 → 一問

**第一問（判定單位）已由 SYSAD 答**：分析層 SYSAD 全文掃描（母體 2,075 單元／
281,916 字元）得具名常數 **`VEHICLE_SPEED_THREE_MPH_TO_KMPH`** ——
**判定單位為 km/h，門檻由 MPH 換算而來**。

| 原三問 | 處置 |
|---|---|
| 1. DUT 以何單位判定（raw／km/h／MPH）| **已答：km/h**（SYSAD 具名常數）→ 記 `PARTIALLY ANSWERED` |
| 2. 換算係數與取整規則 | **保留** —— 即改稿後之唯一一問 |
| 3. 邊界 raw 129／77 是否正確 | **併入第 2 問** —— 其答案由取整規則決定 |

**改稿後之問**：

> **DR-DD4 (revised) — Value and rounding of `VEHICLE_SPEED_THREE_MPH_TO_KMPH`**
>
> The System Architectural Design (FM-WI-FSM-015-A01) names the constant
> `VEHICLE_SPEED_THREE_MPH_TO_KMPH`, indicating that the Driver Distraction
> thresholds are evaluated in km/h after conversion from MPH.
>
> Question: what is the implemented value of that constant (and of its 5 MPH
> counterpart), and what rounding rule is applied — is 3 MPH stored as
> `4.828032`, `4.83`, or `4.8` km/h, and 5 MPH as `8.04672`, `8.05`, or
> `8.0` km/h?
>
> The value decides whether raw 128 (8.0000 km/h) falls on the locked or the
> unlocked side of the 5 MPH threshold, which in turn decides the verdict of
> the boundary test cases.

**降為非阻斷、緩發**，其前提為以下拘束隨包生效（下放包 13 §五）：

```
B1 拘束補（併入包 12 §6.2）：
ER 不得斷言 128（不應鎖）／78（不應解）之邊界格 —— 除非 037 該列明書。
跨越側（129／77）之斷言不受限。A-DD6 marker 維持至 DR-DD4 回覆。
```

**本輪已生成之 14 TC 對該拘束之符合性，見 `docs/upstream/09_batch_b1.md` 之自檢第 12 項與 §6.3（「§6.2 六項拘束之對照」）。**

### ⚠ 分析層之自認

**R-DD7(c) 之邊界是推導，不是上游所給。** 產出上以 `[ASSUMPTION A-DD6]`
使其可見（R-DD7(f)），並依 R-DD7(d) 於 TC 內具名 raw 並附 km/h 與 MPH 實值
—— **不讓執行者自行換算**，換算之責留在分析層且可被回查。


---

## DR-DD6 —— `$VC_Trans_Equipped$` 之列舉對應（`-017`~`-024`）

- **標的**：上游（CFTS022 作者）
- **狀態**：**DRAFTED**（下放包 08 §五 之文稿，逐字保留；待 Pei 發送）
- **由來**：上繳包 05 §3.5(甲) —— 值域不共格，分析層全採
- **阻斷範圍**：`-017`~`-024`（8 leaf）**不入 pilot**
- **編號**：**號隨事項配，不隨時序配**。DR-DD5 保留給 r420／r421 件
  （下放包 08 §四，T13a 後定），本件取 DR-DD6，不因 DD5 未建而順移

### 形態 —— 二值制對六值制

| 來源 | 值域 | 值數 |
|---|---|---|
| CFTS022 規範欄 `-126`~`-129` | `[Automatic]`／`[Manual]` | 2 |
| `LID Proxi & Configuration r421 [Powernet 欄]` H 欄 `Format` | `0 = Automatic & 1 = Manual` | 2 |
| `PROXI Format r443` I 欄 `Table` | `0=Not valid／1=MTX／2=MTA (Robotized Gearbox)／3=DDCT／4=ATX／5=CVT` | **6** |

**規範文係對著二值制寫的**；六值制中 `MTA`／`DDCT` 歸於何側，**無任一庫載明**。

> `MTX` 對上 `Manual` 順、raw 又恰同為 `1` —— **順與對是兩件事**。
> PROXI G 欄 `Annotation` 逐字 `General gear box (ex: manual, MTA, automatic, DDTC)`
> 把 manual 與 MTA **並列為不同項**，恰是反證；但 Annotation 為舉例、
> 非歸屬定義，**故亦不得反過來據以排除**。兩個方向都不足以定案。

### 文稿（下放包 08 §五，逐字）

> **DR-DD6 — Enumeration mapping for `$VC_Trans_Equipped$` = `[Manual]` / `[Automatic]`**
>
> CFTS022 SYSRA rows `SYS-RA-Driver_Distraction-126` ~ `-129` specify the
> condition as `$VC_Trans_Equipped$ = [Automatic]` or `= [Manual]` — a
> two-valued domain, consistent with the Powernet-side format recorded in
> `Logical Identifiers and CAN Mapping v1_76`, sheet `Proxi & Configuration`,
> row 421, Powernet band `Format` column: `Transmission equipped:
> 0 = Automatic & 1 = Manual`.
>
> On the Atlantis side the same LID row points to the PROXI parameter
> `Gear_Box_Type` (`PROXI_HDCC27_R3_20250424.xlsx`, sheet `Format`, row 443:
> parameter group `Powertrain_Configuration_4`, byte 101, bits 0–2), whose
> table is six-valued: `0 = Not valid / 1 = MTX / 2 = MTA (Robotized Gearbox)
> / 3 = DDCT / 4 = ATX / 5 = CVT`.
>
> Question: for the purpose of the Hong Kong market requirements above,
> which `Gear_Box_Type` values constitute `[Manual]` and which constitute
> `[Automatic]`? In particular, do `2 = MTA (Robotized Gearbox)` and
> `3 = DDCT` fall on the `[Manual]` or the `[Automatic]` side? The parameter
> annotation (`General gear box (ex: manual, MTA, automatic, DDTC)`) lists
> manual and MTA as separate items but does not define the grouping.
>
> For reference: the decision-relevant criterion appears to be encoded in
> the requirement structure itself — rows `-126`/`-127` condition on
> `$PresentGear$ = [P]` (a Park position must exist), while `-128`/`-129`
> condition on the parking brake (no Park position). The question therefore
> reduces to: do `MTA` and `DDCT` gearboxes have a Park position for the
> purpose of these requirements?
>
> SWQT test case generation for the affected rows proceeds under a
> documented assumption (parameter path per row 421; `MTX`/`ATX` as the
> representative Manual/Automatic values); the affected test cases carry
> assumption markers and will be revised if the answer differs.

### ⚠ 執行層之揭露 —— 文稿引之 LID 版本非 R-DD5 所綁

文稿書 `Logical Identifiers and CAN Mapping **v1_78**`；
**R-DD5 所綁者為 `v1_76`**（`features/vehicle_setting/inputs/`），
`v1_78` 在 `forms/`，未入本 feature 之 reference 綁定。

**本輪實測二版之該列**（`Proxi & Configuration`，皆 449 列）：

| | v1_76（綁定）| v1_78（文稿所引）|
|---|---|---|
| r421 A `Logical Identifier` | `VC_Trans_Equipped` | `VC_Trans_Equipped` |
| r421 F `Signal Name`（Powernet）| `VehCfg7.VC_Trans_Equipped` | 同 |
| r421 G `CAN`（Powernet）| `CAN-B` | 同 |
| r421 H `Format`（Powernet）| `Transmission equipped: 0 = Automatic & 1 = Manual` | 同 |
| r421 K `Signal Name`（CUSW）| `Gear_Box_Type` | 同 |
| r421 P `Signal Name`（Atlantis & Atlantis High）| `Gear_Box_Type` | 同 |
| `VC_Trans_Equipped` 所在列 | r420／r421 | r420／r421 |
| `Country_Code` 所在列 | r43 | r43 |

**所引各欄逐字相同，列號未位移 —— 文稿之內容不誤。**
但**所引版本與綁定版本不一致**，此屬綁定之事，非文稿之事：

- **文稿逐字照錄，不改** —— 改之即非「Pei 發送之版本」
- 發送前請分析層擇一：**(甲) 文稿改書 `v1_76`**，或
  **(乙) 依 R-DD5 重綁 `v1_78` 並重算 sha256**
- **執行層不逕改，也不逕綁**（R-DD5 之綁定為裁決事項）


---

## DR-DD5 —— `VC_Trans_Equipped` 之 r420／r421 互斥（`-017`~`-024`）

- **標的**：上游（LID 維護者）
- **狀態**：**DRAFTED**（下放包 09 §二 之文稿，逐字保留；待 Pei 發送）
- **由來**：T13a 之分布量測（上繳包 06 §3.2–§3.5）
- **阻斷範圍**：`-017`~`-024`（8 leaf）**不入 pilot**

### 裁定所據 —— 「不合慣例」，非「哪一列看起來對」

| 判準 | r420／r421 |
|---|---|
| 配對系統性 | 合（17 組全 2 列）|
| 主形態（G 欄 `CAN-C`→`CAN-B`）| **部分合** —— G 欄合，但另有 F／K／P 三欄衝突，為 17 組中衝突欄最多者 |
| 衝突值含 `Not Applicable` | **全分頁唯一** |
| CUSW 與 Atlantis 訊號名同時衝突 | **全分頁唯一** |

**主形態解釋不了 K／P 欄之衝突** —— CUSW 與 Atlantis 是**架構**欄，
同一 LID 不會因 Powernet 走 C 或 B 而變成 `Not Applicable`；
11 組只差 G 欄者，其 K／P 欄全部一致或全空。

> **不以「r421 較完整」裁之**（形態當證據，同下放包 08 §一 誤 2）；
> **不以 PROXI 側證據反推**（循環論證，上繳 05 §5.3）。

### 文稿（下放包 09 §二，逐字）

> **DR-DD5 — Conflicting rows for LID `VC_Trans_Equipped` in the Logical
> Identifier table**
>
> In `Logical Identifiers and CAN Mapping v1_76`, sheet
> `Proxi & Configuration`, the logical identifier `VC_Trans_Equipped`
> appears twice, in rows 420 and 421, with conflicting content:
>
> - Row 420 — Powernet `Signal Name` = `VC_Trans_Equipped`, Powernet `CAN`
>   = `CAN-C`; CUSW `Signal Name` = `Not Applicable`;
>   Atlantis & Atlantis High `Signal Name` = `Not Applicable`.
> - Row 421 — Powernet `Signal Name` = `VehCfg7.VC_Trans_Equipped`,
>   Powernet `CAN` = `CAN-B`, Powernet `Format` = `Transmission equipped:
>   0 = Automatic & 1 = Manual`; CUSW `Signal Name` = `Gear_Box_Type`;
>   Atlantis & Atlantis High `Signal Name` = `Gear_Box_Type`.
>
> The sheet contains 17 logical identifiers that appear on two rows each.
> In 14 of those pairs the difference is confined to the Powernet `CAN`
> column (11 of them differ in that column only), following a consistent
> `CAN-C` → `CAN-B` pattern. `VC_Trans_Equipped` is the only pair whose
> conflict extends to the CUSW and Atlantis signal-name columns, and the
> only pair where one row states `Not Applicable` while the other names a
> parameter.
>
> Question: for the Atlantis architecture, which row governs
> `VC_Trans_Equipped` — is the identifier not applicable (row 420), or is
> it realised through the PROXI parameter `Gear_Box_Type` (row 421)?
>
> SWQT test case generation for the affected rows proceeds under a
> documented assumption (parameter path per row 421; `MTX`/`ATX` as the
> representative Manual/Automatic values); the affected test cases carry
> assumption markers and will be revised if the answer differs.

### 與 DR-DD6 之關係 —— 二個獨立阻斷，不可互抵

| | 所定者 | 若單獨回覆 |
|---|---|---|
| **DR-DD5** | `$VC_Trans_Equipped$` 在 Atlantis 架構下**有無施加路徑** | 即使裁 r421（有路徑），`[Manual]` 之歸屬仍懸 |
| **DR-DD6** | `[Manual]`／`[Automatic]` 對 `Gear_Box_Type` 六值制**如何對應** | 即使給出歸屬，r420 為準時該歸屬無處施加 |

**須分別追**（同 DR-DD1／DR-DD3 之理）。


---

## DR-DD7 —— AC2 逐字全等（**4 組、11/28 leaf**）（A-DD7）

- **標的**：上游（037 作者）
- **狀態**：**DRAFTED**（下放包 10 §四 之文稿，逐字保留；待 Pei 發送）
- **由來**：**A-DD7**（執行層 T15 生成過程所登，下放包 10 §四 採認並命立 DR）
- **阻斷範圍**：**不阻斷** —— 二 TC 皆保留（追溯要求每 leaf 有 TC）

### 分析層所補之後果（下放包 10 §四）

`-010` 與 `-012` 之 037 原文 18/20 欄全等 → 其衍生之二 TC，
**區別僅在於「取樣 feature」，而取樣 feature 是作者所選、非 spec 所定**。

依 **IN §4.6 之等價判準**（same trigger + outcome + input + verification target）
**四者皆同** —— 若非追溯需求，其為重複。

### 處置

- 二 TC **皆保留**
- `newR1L-DD-004` 之 `reasoning` **已明記**「本列與 `newR1L-DD-002` 之驗證目標
  實質相同，區別僅在取樣 feature 與追溯 ID」；`newR1L-DD-002` 亦互指
- **不得以取樣 feature 之不同偽稱為不同之驗證目標**

### 文稿（**下放包 14 §五 之改稿，整段替換**，逐字）

> 舊稿（包 10 §四）只問 `-010`／`-012`；執行層以 18 欄為鍵之分組實測得
> **4 組、11/28 leaf**（上繳 09 §5）。**稿由分析層改**，本輪整段替換。

> **DR-DD7 — Identical AC2 text across multiple leaf pairs in FM-WI-FSM-037-A03**
>
> Four groups of leaves in FM-WI-FSM-037-A03 are byte-identical across all
> 18 content columns, differing only in the leaf id and the Source
> Requirement ID:
>
> - `-004` / `-006` / `-008` — sources `SYS-RA-Driver_Distraction-114`,
>   `-115`, `-116`
> - `-010` / `-012` / `-014` / `-016` — sources `-117`, `-118`, `-120`, `-121`
> - `-018` / `-020` — sources `-125`+`-126`, `-125`+`-127`
> - `-022` / `-024` — sources `-125`+`-128`, `-125`+`-129`
>
> In total 11 of the 28 leaves, all of them AC2 rows. The corresponding AC1
> rows do differ from one another, each following the wording of its own
> source requirement.
>
> The effect is most visible for `-012`: its source `-118` specifies the
> lockout-notification behaviour, but its AC2 text states
> `HMI keeps the corresponding feature locked`, which is the `-117` outcome.
>
> Question: are these AC2 rows intended to be identical (i.e. a single
> fail-safe behaviour restated once per source requirement), or should each
> follow the outcome of its own source requirement? As written, each group
> yields test cases with the same verification target, distinguished only by
> traceability.

### 與 A-DD7 之連結

本 DR 之台帳對應項為 **A-DD7**（`ANOMALIES.md`）——
該條為執行層 Tier 1 登記（record + propose），本 DR 為其 Tier 2 處置。
---

## DR-DD8 —— Driver Distraction Lockout Table 之機器可讀本（`[CG-DD1]`）

**狀態：DRAFTED**（下放包 16 §二，T-登建檔；待 Pei 發送）。等級：**必發**。

### 形態

CFTS022 `-120`／`-121` 之 verification criteria 明載負向側
（`Features not listed in the table remain accessible and unaffected` ／
`Features not included in the table remain accessible and function normally`），
其 verification method 更有 `4. Verify allowed features — Access features
not in the table`。而該表在需求本文中**只以內嵌物件引用**
（`image: 1-_3bc8e108-12c5-4694-a9e9-80b1f915b9af.rtf`），
交付之 SYSRA 工作簿**無任何內嵌物件**，HMI Logic and Flow（May 3 2021）
**只列 `L/O` 列** —— 即所有列皆為上鎖，**無一列可充當「表外功能」**。

**故負向側之測試步驟無來源可書**，非「未做」而是「做不了」。

### 文稿（下放包 16 §二，逐字）

> **DR-DD8 — Machine-readable copy of the Driver Distraction Lockout Table**
>
> CFTS022 rows `SYS-RA-Driver_Distraction-120` / `-121` require the HU to
> apply lockout to "the features in the The Driver Distraction Lockout
> Table", and their verification criteria explicitly include the negative
> side: `Features not listed in the table remain accessible and unaffected`
> (row `-120`) / `Features not included in the table remain accessible and
> function normally` (row `-121`), with verification method step
> `4. Verify allowed features — Access features not in the table`.
>
> The table itself is referenced in the requirement text only as an embedded
> object (`image: 1-_3bc8e108-12c5-4694-a9e9-80b1f915b9af.rtf`); the
> delivered SYSRA workbook contains no embedded objects, and the HMI Logic
> and Flow document (May 3 2021) lists only rows marked `L/O` — it contains
> no row that is *not* locked out, so no "feature not in the table" can be
> identified from the bound sources.
>
> Request: please provide the Driver Distraction Lockout Table in a
> machine-readable form (the referenced `.rtf`, or an equivalent
> spreadsheet/text export), so that verification method step 4 (allowed
> features remain accessible) can be implemented. Until then this negative
> aspect is recorded as a coverage gap ([CG-DD1]) in SWQT test case
> generation.
>
> The following bound and shared sources were searched without finding a
> machine-readable form of the table: the SYSRA workbook (no embedded
> objects), the Driver Lockout HMI Logic and Flow document (May 3 2021,
> `L/O`-marked rows only), `DTCs Matrix Core List Rev. 1.6`, and
> `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)` (lockout appears
> only as free-text notes in the Notes column, which itself refers back to
> CFTS022 for the requirements).

### 與 [CG-DD1] 之連結

本 DR 之台帳對應項為 **[CG-DD1]**（`COVERAGE_GAPS.md`）——
該缺口在 DR-DD8 回覆前不關閉；回覆到達且表中確有非 `L/O` 列時，
`-021`~`-024` 須補負向側 TC。

---

## DR-DD9 —— Body OFF 電源時序之具名激勵（`-001`／`-002`；A-DD10）

**狀態：DRAFTED**（下放包 16 §三，T-登建檔；待 Pei 發送）。等級：**必發**。

### 形態

`-001`／`-002`（source `SYS-RA-Driver_Distraction-113`，CFTS022-4915104）
之激勵為「Body OFF power sequence（進入 sleep／喚醒）」，`-002` 另加
「terminate the DD process in the test environment」。
**037 與 CFTS022 皆未給該時序之 logical identifier／signal／parameter**；
Logical Identifier 表、PROXI 檔、二綁定 DBC 與 SYSAD 皆查無。

`-002` 之 process 名同樣無來源 —— 依 **R-DD20(c)**，其 `$` 指令行
（IN §5.4）寫 `PENDING: DR-DD9 <DD process 終止指令>`，
**不得自 SYSAD 取服務名充之**（R-DD4：SYSAD 不入語料）。

### 文稿（下放包 16 §三，逐字）

> **DR-DD9 — Named stimulus for the Body OFF power sequence
> (`SWE1-RA-Driver_Distraction-001` / `-002`)**
>
> Rows `-001` and `-002` (source `SYS-RA-Driver_Distraction-113`,
> CFTS022-4915104) are stimulated by the "Body OFF power sequence"
> (enter sleep / wake) and, for `-002`, by terminating the DD process in
> the test environment. Neither FM-WI-FSM-037-A03 nor CFTS022 names a
> logical identifier, signal, or parameter for this power sequence; the
> Logical Identifier table, PROXI file, both bound DBCs and the SYSAD were
> searched without result.
>
> Two questions:
> 1. What is the named identifier (LID / signal / parameter / bench
>    command) for driving the Body OFF sleep and wake sequence on the test
>    bench for these rows?
> 2. What is the process or service name (and the accepted termination
>    method) intended by "terminate the DD process in the test environment"
>    in row `-002`?
>
> SWQT test case generation for these rows proceeds under a documented
> assumption (the sequence is driven via the platform power-moding
> procedures already established for CFTS009, marked `[ASSUMPTION A-DD10]`);
> the affected test cases will be revised if the answer differs, and the
> process-termination command line is held as `PENDING: DR-DD9` until
> question 2 is answered.

### 與 A-DD10 之連結

本 DR 之台帳對應項為 **A-DD10**（`ANOMALIES.md`）。
**不減其必發等級**（R-DD20(d)）：回覆與 R-DD20(a) 相符 → 撤 A-DD10；
不符 → 回修範圍為 2 TC 之電源時序步驟，`test_item` verbatim 不動。

### ⚠ 執行層之揭露 —— 文稿第 1 問所指之「已建立程序」，power 線查無

文稿末段書：`the sequence is driven via the platform power-moding procedures
already established for CFTS009`。**T22c 唯讀傾印之實測**（上繳 13 §六）：
power 線之狀態進入步驟**全為通稱式**（`Bring the HU to Timed mode`、
`Bring the TLM through the switch on sequence` 等），
**無一則帶訊號名／值／格式**；`Body OFF` 之 sleep／wake 亦無任何施加步驟。

**故 R-DD20(b) 之「只得逐字取自 power 線已裁之施加式」目前無可取之物。**
本輪依 T22c 拘束**不判、不代擬**，僅傾印並回報；包 17 之規格須據此重定。
