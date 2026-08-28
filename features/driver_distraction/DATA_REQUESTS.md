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
| **DR-DD1** | 037 作者／上游 | **DRAFTED**（待 Pei 發送）| `-025`~`-028`（4） | 該 4 leaf **凍結**，不入任何批次 | A-DD1 | 高 —— framework 組 6 之歸屬待此 |
| **DR-DD2** | 上游（CFTS022 作者）| **DRAFTED**（待 Pei 發送）| `-021`~`-024`（4） | 不阻斷生成；ER／Pre-Condition 之訊號名待定 | **A-DD2** | 中 |
| **DR-DD3** | 上游（素材提供）| **ANSWERED-PENDING-CONFIRM** | `-017`~`-028`（12） | **值已查得（91）；識別仍懸，標 A-DD5** | **A-DD5** | 中 |
| **DR-DD4** | 上游（CFTS022／037 作者）| **DRAFTED**（待 Pei 發送）| **9 列書 MPH 門檻者**：`-003`／`-005`／`-007`／`-009`／`-011`／`-013`／`-015`（7，可生成）＋ `-025`／`-027`（2，另因 A-DD1 凍結）| 不阻斷生成；ER 之 raw 數值標 A-DD6 | **A-DD6** | 中 |
| **DR-DD5** | 上游（LID 維護者）| **DRAFTED**（待 Pei 發送）| `-017`~`-024`（8）| **該 8 leaf 不入 pilot**；`$VC_Trans_Equipped$` 有無施加路徑未定 | — | 高 —— 與 DR-DD6 並列 |
| **DR-DD6** | 上游（CFTS022 作者）| **DRAFTED**（待 Pei 發送）| `-017`~`-024`（8）| **該 8 leaf 不入 pilot**；`$VC_Trans_Equipped$` 之列舉對應未定 | — | 高 —— 組 1／2 待此 |

**DR-DD1／DR-DD2／DR-DD4／DR-DD6 為 DRAFTED 未發送；DR-DD3 之標的已到位，狀態
ANSWERED-PENDING-CONFIRM（下放包 07 §三 R-DD8(c) 明定不結案）。**

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
- **狀態**：DRAFTED（下放包 02 §三 之文稿，逐字保留；待 Pei 發送）
- **阻斷範圍**：`-025`~`-028` 四 leaf 凍結（A-DD1 暫行處置）
- **⚠ 與 DR-DD3 為二個獨立阻斷，不可互抵**（下放包 05 §四 採認執行層所指）：
  **DR-DD1 裁 HK 只定「市場為何」，仍不給出 `Country_Code` 之值。**
  即使 DR-DD1 先回，HK 段（`-017`~`-028`）仍卡於 DR-DD3。**二者須分別追。**

### 文稿（下放包 02 §三，逐字）

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
> Until clarified, the four rows are on hold in SWQT test case generation.

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

## DR-DD2 —— `$PARK_BRK_EGD$` 之 LID 名稱拼法（`-021`~`-024`）

- **標的**：上游（CFTS022 作者）
- **狀態**：DRAFTED（待 Pei 發送）
- **由來**：A-DD2；R-DD5 之 T6 逐訊號查對，五訊號中**唯一四庫皆查無者**
- **阻斷範圍**：不阻斷生成 —— 該 4 leaf 之 ER／Pre-Condition 於訊號名定案前
  依 IN §8.7.5(d)(g) **保留來源名稱**（`$PARK_BRK_EGD$`），不代以他訊號（R-13）

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

### ⚠ 執行層未自行採用 `EDG`

**答案看起來就在來源自己的欄位裡**，但：
- `Description` 為**規範欄**，其餘為註記／回饋欄 —— **二者位階不同**；
- `-129` **未被更正**，故「已定案」之推定不成立；
- R-DD5 明文「查無者逐項登 DR，**不得代以語意相近之他訊號**」（R-13）。

**故本輪保留 `$PARK_BRK_EGD$` 原名並登 DR。**

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

狀態：**ANSWERED-PENDING-CONFIRM**。

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
- **狀態**：**DRAFTED**（下放包 07 §二 R-DD7(f) 所命；待 Pei 發送）
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
| `-025` | r33 | `5 MPH` | **另因 A-DD1 凍結** |
| `-027` | r35 | `3 MPH` | **另因 A-DD1 凍結** |

  其偶數配對列（`-004`／`-006`／`-008`／`-026`／`-028`）為 **AC2 之
  訊號失效／逾時分支**，文中無門檻值 —— **A-DD6 不及於彼**。

  > **即：A-DD6 之波及面比 A-DD1 廣。** 7 列不在凍結名單內卻要帶 marker，
  > 這 7 列是 pilot 會先碰到的。
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
> Until clarified, the affected rows are on hold in SWQT test case generation.

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
> Until clarified, requirements conditioned on `$VC_Trans_Equipped$` are on
> hold in SWQT test case generation.

### 與 DR-DD6 之關係 —— 二個獨立阻斷，不可互抵

| | 所定者 | 若單獨回覆 |
|---|---|---|
| **DR-DD5** | `$VC_Trans_Equipped$` 在 Atlantis 架構下**有無施加路徑** | 即使裁 r421（有路徑），`[Manual]` 之歸屬仍懸 |
| **DR-DD6** | `[Manual]`／`[Automatic]` 對 `Gear_Box_Type` 六值制**如何對應** | 即使給出歸屬，r420 為準時該歸屬無處施加 |

**須分別追**（同 DR-DD1／DR-DD3 之理）。
