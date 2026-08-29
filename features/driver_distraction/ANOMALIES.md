# ANOMALIES — FW036 driver_distraction HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-DRnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

(no entries yet)

---

## [A-DD1] `-025`~`-028` 之市場條件衝突（下放包 01 §二；執行層複測成立）

037 之 `-025`~`-028` 同時引 `SYS-RA-Driver_Distraction-125`
（HK 章閘）與 `-132`／`-133`（5／3 MPH 門檻），而其 Description 與
Verification Criteria 均書 `When Country_Code is Hong Kong`。

**CFTS022 之章結構實測**（`Basic Report`，逐列）：

```
-122 [Heading]      Market-Specific Regulations and Brand-Specific Exceptions
-123 [Heading]      Hong Kong Market Regulations
-124 [Information]  For Hong Kong market, the features … will be locked …
-125 [FR]           The requirements in the section shall be implemented if $Country_Code$ = [Hong Kong].
-126 [FR] -127 [FR] -128 [FR] -129 [FR]      ← HK 章之需求
-130 [Heading]      LATAM Market Regulations
-131 [Information]  The requirements in this section apply to the LATAM market only.
-132 [FR] -133 [FR]                          ← LATAM 章之需求
```

**`-125` 為 HK 之章閘；`-132`／`-133` 在 LATAM 章下，且 `-131` 明文限 LATAM。**

### ⚠ 執行層複測所得之補充證據

| 037 列 | 所引 source | 章歸屬 | 內部一致？ |
|---|---|---|---|
| `-017`~`-024`（8）| `-125` ＋ `-126`~`-129` | 全在 HK 章 | ✅ |
| **`-025`~`-028`（4）** | `-125` ＋ `-132`／`-133` | **跨 HK／LATAM 二章** | ❌ |

**同一作者在 12 列上一致地以 `-125` 為 HK 章閘，唯獨最後 4 列把它接到
LATAM 章之需求上。** 此為量測，**非結論** —— 判斷屬上游。

### ~~處置（凍結期，包 02–19）~~ —— **已由 R-DD25 結案**

- ~~**`-025`~`-028` 凍結**，不入任何批次（下放包 02 §二，隨包生效）。~~
- framework 組 6 `Market Speed Gating` 維持市場中立佔位名，**組名不寫入工作簿任何列**。
- 其餘 24 leaf 之生成**不受阻**。
- **DR-DD1** 已登記（改稿為確認件，待 Pei 發送）。

### 結案（下放包 20 §二，R-DD25(b)(c)）

**狀態：`CLOSED-BY-SCOPE`** —— **非以 DR 回覆結案**（R-DD25(c) 明命須註此點）。

**結案依據（R-DD25(b) 逐字，三項獨立收斂）**：

```
1. 其 Source 之 `-132`／`-133` 屬 CFTS022 之 LATAM 章
2. SYSAD 載速度遲滯判定為 `JudgmentProcessorType4to6 … for LATAM`
3. (a) 之範圍裁定：LATAM 不在案
```

**範圍裁定（R-DD25(a)，Pei 2026-08-28 Tier 3）**：本案 **NAFTA 在案、LATAM 不在案**；
`Hong Kong` 在案，其依據為**右駕（RHD）**而非區域 —— 市場表 `Market Config - R1`
c14 載 HONG KONG(r97)＝RHD，與 UNITED KINGDOM(r216) 同；其 Region(c16) 為 **APAC**。
**區域與駕駛側為二個獨立維度，不得互相蘊含。**

> **本條與凍結之性質不同**：凍結（本條 2026-08-27 至 2026-08-28）是
> **「該測而資訊不足」**；範圍外是 **「不該測」**。
> 二者若混為一談，會讓「等到回覆就能補做」這個錯誤預期一直掛著。

**不及於 `-017`~`-024`**（R-DD25(e)）：其在案依據為 RHD，與 LATAM 之範圍裁定無涉；
亦不改 R-DD19 之 A-DD8／A-DD9（施加路徑之假設，與市場範圍無涉）。

**差額之記錄義務**：四列入 `COVERAGE_GAPS.md` 之 **[CG-DD2]**（R-DD25(d)）——
**不得於任何統計中把 28 寫成 24 而不交代差額**（R-DD10(c)）。

---

> **編號歸屬（下放包 03 §二）**：台帳**先登先得**。
> 包 01 §二文中之候選編號 `A-DD2`／`A-DD3` 已由該包 §二 重配，**以本台帳為準**。
> `A-DD2` = PARK_BRK 件（執行層所登，定案）；`A-DD3` 見下；
> 包 01 之「`_x000D_` 正規化」候選**作廢，不登異常**（下放包 03 §二-3 自認之分析層一誤）。

## [A-DD2] `$PARK_BRK_EGD$` 四庫皆查無；來源自身之註記欄指其應為 `PARK_BRK_EDG`（新立，T6）

R-DD5 之五訊號查對，**唯一四庫皆查無者**：

| 訊號 | LID | DBC | PROXI |
|---|---|---|---|
| `$Speedometer$` | ✅ | — | ✅ |
| `$VC_Trans_Equipped$` | ✅ | — | — |
| `$PresentGear$` | ✅ | — | — |
| **`$PARK_BRK_EGD$`** | **✗** | **✗** | **✗** |
| `$Country_Code$` | ✅ | — | ✅ |

> DBC 欄之 `—` 為**預期狀態**：`$…$` 為**邏輯識別碼**（LID 之標的），
> 非 CAN 訊號名；其 CAN 對應由 LID 之 `CAN Mapping` 分頁承載。
> **不因此登異常。**

### 近似拼法之實測（**量測，非代換**）

`Logical Identifiers and CAN Mapping v1_76.xlsx` `CAN Mapping` **r1310**：

```
c0  PARK_BRK_EDG
c15 STATUS_BH_BCM1.ParkBrakeSts   c16 CAN-B
c25 BCM_FD_9.ParkBrakeSts         c26 CAN-FD
```

**`EDG` vs `EGD` —— 二字母倒置。**

### ⚠ 來源自身已記載此事，但只改了一半

CFTS022 `Basic Report` r129（`-128`）逐欄：

| 欄 | 拼法 | 逐字 |
|---|---|---|
| c3 `Description`（**規範欄**）| `EGD` | `If $VC_Trans_Equipped$ = [Manual] then when $PARK_BRK_EGD$ = [ON] …` |
| c13 `SYS2 System-HW` | **`EDG`** | `…supplier shall provide API to read, for LID $PARK_BRK_EDG$` |
| c14 `SYS2 System-SW` | **`EDG`** | `…AND $PARK_BRK_EDG$ = [ON], implement Driver lockout feature…` |
| c16 `SYS2 HARMAN Comments` | **`EDG`** | `…looks incorret. Does the expected LID name is "PARK_BRK_EDG".` |
| c18 `SYS2 MD Feedback` | **`EDG`** | `The LID which is referred here is $PARK_BRK_EDG$` |
| c38／c39 驗證標準／方法 | `EGD` | `Set $PARK_BRK_EGD$ = ON …` |

**r130（`-129`）未被更正** —— 其 c14 `System-SW` 仍作 `EGD`。

即：**供應商提出、上游回覆確認，而規範欄與驗證欄未隨之更正，
且第二列完全沒動。**

### 處置 —— 執行層**未自行採用 `EDG`**

理由三：
1. `Description` 為**規範欄**，`Comments`／`MD Feedback` 為註記欄 —— **位階不同**；
2. **`-129` 未被更正**，故「已定案」之推定不成立；
3. R-DD5 明文「查無者逐項登 DR，**不得代以語意相近之他訊號**」（R-13、IN §8.7.5(d)(g)）。

`-021`~`-024` 之 ER／Pre-Condition **保留來源名稱 `$PARK_BRK_EGD$`**，
**DR-DD2** 已登記（DRAFTED）。**不阻斷該 4 leaf 之生成。**

### 處分（下放包 13 §三）—— **R-DD18 劃出採認與代換之界線**

**R-DD18(a)**：上游於其自身文件內對同一疑問留有**書面回覆**者
（本案即上表 c16／c18 之提問與回覆），得採認該回覆所指之名為**施加名**
—— 此為 lookup ＋ 上游書面確認，**非 R-DD5／R-13 所禁之語意代換**。

**上述三項「未自行採用」之理由未被推翻**，而是各自被限縮到其真正的範圍：

| 原理由 | R-DD18 之處置 |
|---|---|
| 1. `Description` 為規範欄，位階不同 | 採認**僅及施加路徑**；`test_item` 上半仍照原文 `EGD`（R-DD18(b)）|
| 2. `-129` 未被更正，「已定案」之推定不成立 | 未更正前用及者標 `[ASSUMPTION A-DD2]`，上游正式更正後撤 |
| 3. R-DD5／R-13 禁代以語意相近之他訊號 | 所禁者為**自行推定**；本案有書面回覆，不屬之（R-DD18(a)）|

**施加名 = `PARK_BRK_EDG`**，其 CAN 對應**仍須自 LID 該列實測查得**
（R-DD18(b) 明文不得因勘誤成立而略過查證）—— **T19c 已查，見 `docs/upstream/10_dr_triage.md` §3**。

**DR-DD2 隨之降轉為格式更正件**（請上游更正規範欄與 `-129`），**非阻斷、緩發**。

> **R-DD18(c)**：本條不得反向援引。**書面回覆之有無是採認與代換之全部界線。**

狀態：**PENDING**（待 DR-DD2 之規範欄更正；**施加路徑已解**）。

---

## Assumption markers

現行 marker：`A-DD2`／`A-DD6`／`A-DD7`／`A-DD8`／`A-DD9`／`A-DD10`。
Inline format in generated JSON reasoning: `[ASSUMPTION A-DDnn]`.

---

## [A-DD3] 狀態命名兩制（CFTS `Locked/Unlocked` vs 037 `RESTRICTED/NOT_RESTRICTED`）—— **RESOLVED**

**形態**：同一個狀態變數，二份上游各用一套列舉名。

| 來源 | 措辭 |
|---|---|
| CFTS022（`-126`~`-129`／`-132`／`-133`）| `"Lock Out State" variable to "Locked"／"Unlocked"` |
| 037（`Verification Criteria`／`Description`）| `Lock Out State is RESTRICTED／NOT_RESTRICTED`、`Listener receives a RESTRICTED callback` |

### 處置（下放包 03 §二-2，登記即結案）

**R-DD3 已定 ER 之主錨為 HMI 現象** —— 故：

- **兩套列舉皆不得出現於 `expected_result`**（R-DD3(b)：callback／內部狀態
  非 SWQT 觀察面）。
- `test_item` 上半 **verbatim 照 037 原文**（含 `RESTRICTED` 措辭），**不改字**。

**即：二制之衝突不落到產出上** —— 一個在 ER 被 R-DD3 擋掉，
另一個在上半以 verbatim 保留。**無待決事項。**

狀態：**RESOLVED**（下放包 03 §二-2）。

---

## 台帳之編號拘束（下放包 03 §一-5）

`Sub Categorization` 欄之實測值為 `Driver_Distraction `（**末有一個空白**）。

```
日後任何以該欄為鍵之比對一律 verbatim 含尾空白，
或於比對端明文 rstrip 並揭露；**不得靜默修資料**。
```

---

## [A-DD4] 共用路徑之寫入歸屬（新立，下放包 05 §二 逐字）

`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md` 檔首出現
一行**非分析層所寫**之落檔註記，且其所述之「ENOENT 後重寫」對該檔不成立
（該情形發生於下放包 04，非 profile）。

**Pei 2026-08-27 告知：三個 feature session 平行進行中。**

- 事實：分析層送出之稿與磁碟內容差一行；`features/driver_distraction/docs/handoff/` 無競包
- **成因未量測，不臆斷寫入者**
- 已於 profile 檔首更正該行（保留痕跡，非刪除；R-TM13 精神）

### 處置拘束（隨本包生效）

`features/{slug}/` 為該線私有，撞寫風險低；
**`docs/runtime/`、`docs/fw036/`、`forms/`、`scripts/` 為共用路徑**，
三線皆可觸及。於共用路徑之寫入：

1. **一律 `edit_file` 局部改，不得整檔 `write_file` 覆寫** —— 覆寫會湮滅他線之字
2. 改動前 `read_multiple_files` 回讀現況，改動後回讀驗 diff
3. 發現非本線所寫之內容：**保留並註記**，不刪除、不逕改其語意

狀態：OPEN（成因未明；拘束已生效，不待成因查明）。

---

### 執行層之遵行紀錄（本輪）

本輪之寫入**全在 `features/driver_distraction/` 私有路徑**
（`ANOMALIES.md`／`DATA_REQUESTS.md`／`docs/upstream/`／`scripts/`），
**未觸及任何共用路徑** —— 故 §處置拘束 之三項於本輪無適用對象。

**上一輪（下放包 04）曾寫入共用路徑**
`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`：
該次為 `git add` 既有檔案（分析層所落），**執行層未改其內容一字**。

**拘束自本包生效，往後於共用路徑一律 `edit_file` 局部改。**

---

## [A-DD5] `SR24 R1 Market Configuration Table v1.6.xlsx` 之識別未確認（新立，下放包 07 §三 R-DD8）

**形態**：值已得，來源身分未定。

**`LID Proxi & Configuration r43 [Powernet 欄]`**（R-DD6(c) 之引用格式）
c7 `Format`（Powernet 帶 c5–c9 之 `Format` 欄）逐字指名之權威來源為：

```
See latest version of 'CIP Market Configuration Table v*.xlsx', worksheet 'Market Configuration'.
```

到位者為 `forms/SR24 R1 Market Configuration Table v1.6.xlsx`。
**檔名不同（`CIP` vs `SR24 R1`）；二者是否同一份為事實問題，分析層無證據可定。**

### 處置（R-DD8 逐字所裁，本台帳僅登記）

- **採其值** —— `$Country_Code$` Hong Kong = `91`（十進位，Hex `5B`），
  取自 `Market Config - R1` r97 c19，表頭逐字 `PROXI3  <Country_Code>Signal - Decimal`
- 凡用及該值之 TC **一律標 `[ASSUMPTION A-DD5]`**
- **DR-DD3 不結案**，狀態 `ANSWERED-PENDING-CONFIRM` —— 值已得、識別未確認；
  上游確認後始轉 RESOLVED 並撤本 marker
- 本條**不改變 A-DD1／DR-DD1**：市場歸屬仍懸，二者為獨立阻斷；
  亦不得以該表 c58（Navigation DD Lockout Disable）推論 A-DD1
  —— 該欄對應 CFTS022 `-136`（Out of scope），範圍不同

**適用範圍**：`-017`~`-028`（HK 全段 12 leaf）之 Pre-Condition。
（其中 `-025`~`-028` 另因 A-DD1 凍結 —— 二阻斷並存，不互抵。）

### 撤銷（下放包 13 §二；Pei 2026-08-28 確認識別）

**撤銷依據**（逐字）：

```
Pei 2026-08-28 確認 SR24 R1 MCT v1.6 即 LID 所指之 CIP MCT（取檔出處為其發佈渠道）
```

**識別已確認 → 本 assumption 不復存在。**

- `$Country_Code$` Hong Kong = `91` 由 assumption 轉**確定值**
- `[ASSUMPTION A-DD5]` 之標記義務**解除**（`-017`~`-028`）
- profile §3 該列之標記要求由**分析層**移除
- **回修範圍：無** —— pilot 四則與 B1 十則皆未用及該值（其 leaf 為 `-003`~`-016`）
- **條目不刪**（R-TM13 精神），狀態改 RESOLVED，保留其成立期間之軌跡

> 本條撤銷**不影響 A-DD1**：市場歸屬仍懸。
> 惟原「二者為獨立阻斷」之註記，其防範對象（以 DD3 之值推論 DD1）
> **隨 DD3 結案而消失** —— `-025`~`-028` 之凍結現僅餘 A-DD1 一個成因。

狀態：~~PENDING~~ → **RESOLVED**（下放包 13 §二）。

---

## [A-DD6] 速度門檻之 raw 邊界為分析層推導，非上游所給（新立，下放包 07 §二 R-DD7(f)）

**形態**：spec 之門檻單位（MPH）與可施加訊號之單位（km/h, factor 0.0625）
不共格 —— 此匯流排上**不存在「等於 5 MPH」之格**。

```
5 MPH = 8.04672 km/h  → raw 128.74752
3 MPH = 4.828032 km/h → raw  77.248512
```

R-DD7(c) 依條文之不等號方向取跨越側之第一個可表示格：

| 條文 | raw | km/h | MPH | 判 |
|---|---|---|---|---|
| `equal or greater than 5MPH` | **129** | 8.0625 | 5.0097 | ≥ 5 ✓ |
| （其下一格）| 128 | 8.0000 | 4.9710 | < 5 ✗ |
| `equal or less than 3MPH` | **77** | 4.8125 | 2.9903 | ≤ 3 ✓ |
| （其上一格）| 78 | 4.8750 | 3.0292 | > 3 ✗ |

### 為何登異常

**(c) 之推導為分析層依 DBC 實測值所為，DUT 內部之取整可能相異**
（±1 raw ≈ 0.04 MPH）。上游未給判定單位與取整規則。

### 處置（R-DD7 逐字所裁，本台帳僅登記）

- **全部依 R-DD7 產出之 TC 標 `[ASSUMPTION A-DD6]`**
- TC 內**一律具名 raw 並附其 km/h 與 MPH 實值**，不得只寫「5 MPH」
  而讓執行者自行換算（R-DD7(d)）
- BVA（IN §12）之 limit±1 依 (c)：上鎖側 128（不應鎖）／129（應鎖）；
  解鎖側 77（應解）／78（不應解）
- **DR-DD4** 已建檔（DRAFTED）向上游確認判定單位與取整規則
- **回修範圍受限**：DR 回覆若與 (c) 不同，只動速度類 leaf 之 ER 數值，
  **不動其結構**

> `1 MPH = 1.609344 km/h` 為單位定義，屬 IN §8.4.1 之 domain constant，
> 援用**不構成造值** —— 本異常所指者非換算本身，而是取整規則之未定。

### 適用範圍（本輪實測，037 `Analysis Report` 全 28 列）

**書有 MPH 字樣者 9 列**：

| 可生成（7）| 另因 A-DD1 凍結（2）|
|---|---|
| `-003`（r11，`5`／`3`）`-005`（r13，`3`）`-007`（r15，`5`）`-009`（r17，`5`）`-011`（r19，`5`）`-013`（r21，`5`）`-015`（r23，`5`）| `-025`（r33，`5`）`-027`（r35，`3`）|

偶數配對列（`-004`／`-006`／`-008`／`-026`／`-028`）為 **AC2 之訊號失效／
逾時分支**，文中無門檻值 —— **A-DD6 不及於彼**。

> **A-DD6 之波及面比 A-DD1 廣** —— 7 列不在凍結名單內卻須帶 marker。
> 此 7 列即 pilot 最先會碰到者。

**覆核（T13b，下放包 08 §七）**：上輪僅掃 `MPH` 字樣，為自陳之已知邊界。
本輪以 **`MPH`／`mph`／`mile`／`km/h`／`kph` 五組**重掃 037 全 28 列 ——
**命中集合不變，仍為同 9 列**；`mph`／`mile`／`km/h`／`kph` 四組**全 28 列 0 命中**。
即 037 之門檻**只以大寫 `MPH` 表述**，無其他措辭。**該邊界關閉。**

狀態：**PENDING**（待 DR-DD4）。

---

## [A-DD4] 遵行紀錄（本輪，下放包 07）

本輪之寫入全在 `features/driver_distraction/` 私有路徑
（`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`docs/upstream/`），
**未觸及 `docs/runtime/`、`docs/fw036/`、`forms/`、`scripts/` 任一共用路徑**。

profile §3（`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`）
**本輪未寫入一字** —— 拘束一（T12 只量測，不寫 profile）。
四庫（LID／DBC／PROXI）**全程唯讀開啟**（`read_only=True`），未落任何寫入。

---

### 遵行紀錄（下放包 08 之輪）

本輪寫入亦全在私有路徑（`RULINGS.md`／`DATA_REQUESTS.md`／`ANOMALIES.md`／
`docs/upstream/`／`scripts/`）。

- profile §3 由**分析層自辦**（下放包 08 §六），**執行層本輪未觸及該檔一字**
- 本輪**讀**了一個共用路徑檔：`forms/Logical Identifiers and CAN Mapping v1_78.xlsx`
  （為核 DR-DD6 文稿所引之版本，見 DATA_REQUESTS）——
  **`read_only=True` 開啟，未寫入**。A-DD4 之拘束為**寫入**之拘束，讀不受限
- 四庫（LID v1_76／二 DBC／PROXI）全程唯讀

---

## [A-DD7] `-010` 與 `-012` 之 20 欄中 18 欄逐字全等，其 AC2 未隨 source 分化（新立，執行層登記，T15）

**形態**：同一 AC2 被套用於二個不同之 source requirement，**未隨之調整**。

### 實測（037 `Analysis Report`，逐欄比對）

| 比較對 | 相異欄數／全欄 | 相異之欄 |
|---|---|---|
| **`-010`（r18）vs `-012`（r20）** | **2 / 20** | c0 leaf id、c1 Source Requirement ID |
| 對照：`-009`（r17）vs `-011`（r19） | **4 / 20** | c0、c1、**c3 Requirement Description**、**c17 Verification Criteria** |

即：**AC1 之一對隨 source 分化，AC2 之一對沒有。**

### 何以是問題

二列所引之 source 不同，而該二 source 之斷言面本身不同：

| source | 其 AC1 衍生列之 Then 句（逐字）|
|---|---|
| `-117` | `Then DD Service outputs RESTRICTED and HMI prevents access to the feature` |
| `-118` | `Then DD Service reports RESTRICTED and HMI displays the driver-distraction lockout notification` |

**`-117` 為存取阻擋面，`-118` 為通知呈現面。**
而 `-012`（源自 `-118`）之 AC2 逐字為：

```
Then DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked
```

—— **是 `-117` 之存取阻擋面，非 `-118` 之通知面。**

### 處置 —— 執行層未代上游改寫

- `newR1L-DD-012`（`-012`）**依 037 原文斷言存取阻擋**，
  **不改寫為通知面**（IN §8.4.2：不得造範圍）
- 二列之區別落在**取樣 feature 與 spec_reference**，非斷言內容 ——
  此為 037 現狀之忠實反映，非 TC 之設計缺陷
- **`-012` 之 `test_item` 上半與 `-010` 逐字全等**（各 47 token，皆未逾 50 而全文照錄）。
  下放包 09 §6.2-1 之「同一 Requirement ID 衍生之列不得逐字相同」
  **不及於本對**（二者 Requirement ID 不同），故非違規；
  **但二 TC 之上半確實一字不差**，記於此以免日後被讀為生成之疏漏

### 待上游

`-012` 之 AC2 是否應改為 `-118` 之通知面（即「訊號逾時後，
lockout 通知仍呈現／該 feature 仍不可用」）？
若是，`-012` 之 TC 須隨之重寫其 ER 錨（觀察面 A → 觀察面 B）。

**本項為 Tier 1 登記（record + propose），處置屬 Tier 2。
是否另立 DR 由分析層定 —— 執行層不代登。**

### 處分（下放包 10 §四）—— **立 DR-DD7**

分析層採認執行層之處置（依原文斷言存取阻擋，不代上游改寫），並補一項後果：

> 二列之 037 原文 18/20 欄全等 → 其衍生之二 TC，**區別僅在於取樣 feature，
> 而取樣 feature 是作者所選、非 spec 所定**。依 **IN §4.6** 之等價判準
> （same trigger + outcome + input + verification target）**四者皆同** ——
> 若非追溯需求，其為重複。

- 二 TC **皆保留**（追溯要求每 leaf 有 TC）
- `newR1L-DD-012` 之 `reasoning` 已明記其與 `newR1L-DD-010` 之實質同一，
  `newR1L-DD-010` 亦互指（T16c）
- **不得以取樣 feature 之不同偽稱為不同之驗證目標**
- **DR-DD7 已建檔**（DRAFTED，見 `DATA_REQUESTS.md` §`DR-DD7 —— AC2 逐字全等`）

### ⚠ 擴大量測（T18b 順帶所得，2026-08-28）—— **本異常之範圍遠不止 `-010`／`-012`**

以「除 c0 leaf id、c1 Source Requirement ID 外之 **18 欄**」為鍵，
對 037 **全 28 leaf** 分組。逐字全等之組：

| 組 | leaf | 各自之 source | AC |
|---|---|---|---|
| 1 | `-004`／`-006`／`-008`（**3**）| `-114`／`-115`／`-116` | AC2 速度輸入逾時 |
| 2 | `-010`／`-012`／**`-014`／`-016`**（**4**）| `-117`／`-118`／`-120`／`-121` | AC2 訊號停送逾時 |
| 3 | `-018`／`-020`（2）| `-125`+`-126`／`-125`+`-127` | AC2（HK 段）|
| 4 | `-022`／`-024`（2）| `-125`+`-128`／`-125`+`-129` | AC2（HK 段）|

**4 組，涉及 11 / 28 leaf（39%）。全部為 AC2。**

**本異常初登時記為 2 leaf（`-010`／`-012`），實為組 2 之 4 leaf 中的 2 個。**
即：**AC2 之「未隨 source 分化」是 037 之系統性形態，非個案。**

對照：AC1 各列**皆隨其 source 分化**（`-009` vs `-011` 差 4 欄，含 Description 與 VC）。

### ⚠ DR-DD7 之文稿範圍窄於本量測

`DR-DD7` 之文稿（下放包 10 §四，逐字，DRAFTED 未發送）**只問 `-010` 與 `-012`**。
依本量測，同一問題另涉 **9 個 leaf**（組 1 之 3、組 2 之另 2、組 3／4 之 4）。

**執行層不改該文稿**（逐字文稿，改之即非所擬之版本）。
**是否擴大其範圍，屬分析層。** 若不擴大，`-004`／`-006`／`-008`／`-014`／`-016`
之同一形態將無 DR 承載（`-018`~`-024` 另因 A-DD5／DR-DD5／DR-DD6 未入批次）。

狀態：**PENDING**（待 DR-DD7；**範圍待分析層裁**）。

---

### 遵行紀錄（下放包 10 之輪）

本輪寫入全在私有路徑（`RULINGS.md`／`DATA_REQUESTS.md`／`ANOMALIES.md`／
`docs/upstream/`／`scripts/`／`generated/`）。

- profile §2.5（R-DD12）／§2.6（R-DD11）由**分析層自辦**，
  **執行層本輪未觸及該檔一字**（拘束四）—— 僅唯讀回讀以取 §2.5／§2.6 之判準
- 037／DBC／LID 全程唯讀
- **未寫回工作簿、未執行 git**


---

## [A-DD8] 假設：`$VC_Trans_Equipped$` 之施加路徑（新立，下放包 15 §一，R-DD19(a)）

**條目逐字**（下放包 15 §一）：

```
A-DD8（假設：VC_Trans_Equipped 之施加路徑）
狀態 OPEN。內容：依 R-DD19(a)，-017~-024 之生成假設 r421 為準
（PROXI Gear_Box_Type）。撤銷條件：DR-DD5 回覆確認。
用及之 TC 標 [ASSUMPTION A-DD8]。
```

### 採認基礎（R-DD19(a) 逐字）

> r420／r421 之三種自洽讀法中**二種收斂於此**（新舊列讀法、訊號/參數分答讀法），
> 唯一阻斷之讀法（r421 該格為孤立筆誤）**無任何形態支持**
> —— 此為**讀法收斂之採認，非文件記載**，故掛 marker。

**施加路徑**：LID `Proxi & Configuration r421 [Atlantis 欄]` → PROXI 參數
`Gear_Box_Type`（`Powertrain_Configuration_4`，byte 101，bit 0–2）
—— 該定義為上繳包 05 §3.1 之實測（PROXI `Format` r443）。

### 與 DR-DD5 之關係

**不減其必發等級**（R-DD19(e)）。DR-DD5 所問者為「r420／r421 何者為準」，
本 marker 所記者為「未回覆期間之生成假設」。**二者並存，非互斥。**

狀態：**OPEN**（撤銷條件：DR-DD5 回覆確認）。

---

## [A-DD9] 假設：`[Manual]`／`[Automatic]` 之兩極代表值（新立，下放包 15 §一，R-DD19(b)）

**條目逐字**（下放包 15 §一）：

```
A-DD9（假設：Manual/Automatic 之兩極代表值）
狀態 OPEN。內容：依 R-DD19(b)，[Manual]=1 (MTX)、[Automatic]=4 (ATX)。
MTA/DDCT 之歸屬未決（DR-DD6），不入任何 TC。
撤銷條件：DR-DD6 回覆確認。用及之 TC 標 [ASSUMPTION A-DD9]。
```

### 採認基礎（R-DD19(b) 逐字）

> `MTX`／`ATX` 為**兩極之無疑義代表** —— MTX 之 M 為業界命名之 manual
> （IN §8.4.1 domain constant 家族），PROXI Annotation 之 `manual` 舉例對應之；
> ATX 同理。

對照上繳包 05 §3.5(甲) 之量測 —— PROXI `Format` r443 c8 `Table` 逐字六值：

```
0 = Not valid ／ 1 = MTX ／ 2 = MTA (Robotized Gearbox) ／
3 = DDCT ／ 4 = ATX ／ 5 = CVT
```

### ⚠ R-DD19(c) —— **硬邊界**

```
`MTA`（2）與 `DDCT`（3）之歸屬為 DR-DD6 之未決問題，
**不得以該二值作任何 TC 之 Pre-Condition 或輸入** ——
乙案採認之範圍止於兩極，不及於邊界。
```

**執行層之落實**：B2 八則之 PROXI 值只出現 `1 (MTX)` 與 `4 (ATX)`；
自檢新增一項**逐產物掃 `Gear_Box_Type = 2`／`= 3`／`MTA`／`DDCT`**，命中即 FAIL。

> 上繳包 05 §3.5(甲) 當時所指者正是此處：
> 「PROXI `Annotation` 逐字 `(ex: manual, MTA, automatic, DDTC)`
> 把 manual 與 MTA **並列為不同項**，恰是反證；但 Annotation 為舉例、
> 非歸屬定義，**故亦不得反過來據以排除**。」
> **乙案未推翻該判斷** —— 它只在**兩極**上採認，邊界仍懸，故立為硬邊界。

狀態：**OPEN**（撤銷條件：DR-DD6 回覆確認）。
---

## [A-DD10] 假設：Body OFF 之同一性（新立，下放包 16 §一 R-DD20(a)；**基礎於下放包 17 §二 R-DD20 v2(a) 改述**）

**條目逐字**（下放包 16 §一）：

```
A-DD10（假設：Body OFF 之同一性）
狀態 OPEN。內容：依 R-DD20(a)，CFTS022 之 Body OFF HU System Sleep Mode
與 power 線 BODY OFF 狀態族採認為同一概念；-001/-002 之電源時序步驟
沿 power 線已裁程序。撤銷條件：DR-DD9 回覆確認。
用及之 TC 標 [ASSUMPTION A-DD10]。
```

### 採認基礎（**R-DD20 v2(a) 逐字；下放包 17 §二**）

> CFTS022 `-113` 之 `Body OFF HU System Sleep Mode` 與 CFTS009 §1.3 所定義之
> `Body Off HU System Sleep Mode`（文字層錨點 4941238，逐字同名；
> `OFF`／`Off` 之大小寫差屬排版正規化，R-4 同型）採認為同一。
> v2 之基礎為**定義級**：CFTS009 4941238 定義該模式、CFTS022 -113 引用之。
> **殘餘假設（本 marker 所標者）＝台架實現與 DR-DD9 回覆之一致性。**

**CFTS009 4941238 逐字**（`features/power/data/textlayer/cfts009_plain.txt`，唯讀）：

```
In the system transitions to the Body OFF mode, the A&T system shall go into
Standby Mode and then if there is no CAN-I and no CAN-C activity, the A&T system
shall go to Body Off HU System Sleep Mode.
```

### ~~⚠ 執行層之實測與所書不符 —— 「78 處命中」未能重現~~ —— **已結案**

> 上繳包 13 §6.1 所報之不符（`features/power/RULINGS.md` 之 `BODY OFF` 命中為 **0**，
> 11 處皆為 `BODY OFF-TIMED`）**已由分析層採認並改條**：
> 下放包 17 §一-1 記明該數為關鍵詞**族**之計數（含 `BODY ON`／`BODY OFF-TIMED`），
> 分析層在 v1 條文中把它具體化為單一詞之計數，**成因與 D8 同族**
> —— 把一個母體不同的數字搬進新語境而未重測。
> **R-DD20 v2(a) 已撤該引數，改採定義級基礎**（見上）。
> v1 依 R-TM13 留存於 `RULINGS.md`（`## R-DD20 v1`，`sha8 00912428`），不得引用。

**本節於本輪（包 17）結案。** A-DD10 之狀態不因改條而變 —— 見末段。

### 與 DR-DD9 之關係

**不減其必發等級**（R-DD20(d)）。DR-DD9 所問者為施加識別碼與 process 名，
本 marker 所記者為「未回覆期間之同一性採認」。**二者並存，非互斥。**

### 適用範圍

`-001`／`-002`（`SWE1-RA-Driver_Distraction-001`／`-002`）。
**二則已於包 17（T23a）生成**，其電源時序步驟依 R-DD20 v2(b)(4) 標
`[ASSUMPTION A-DD10]`；產物 `generated/batch_body_off_init.json`。

### 殘餘假設之範圍（v2 之收窄）

| | v1 | **v2（現行）** |
|---|---|---|
| 所假設者 | **同一性本身**（跨文件同名之採認）| **台架實現與 DR-DD9 回覆之一致性** |
| 基礎 | 命中計數（**已撤**）| CFTS009 `4941238` 之**定義**，CFTS022 `-113` 引用之 |
| 回覆不符時之回修 | 2 TC 之電源時序步驟 | **不變**（R-DD20 v2(d)）|

**同一性已不在假設之列** —— marker 現所標者為「照 CFTS009 所定義之時序在台架上
確實可如此驅動」。此為**收窄**，非撤銷。

狀態：**OPEN**（撤銷條件：DR-DD9 回覆確認）。

---

## [A-DD11] 彈出字串之二變體（新立，下放包 19 §1.2；**INFORMATIONAL，不阻斷**）

- 登記：2026-08-28（分析層 forms/ 查證之順帶所得）
- 狀態：**INFORMATIONAL** —— **不阻斷、不登 DR、不入 marker 登記表**
- **對已生成 TC 之影響：無**

### 二變體（下放包 19 §1.2 逐字）

| 變體 | 出處 | 與已生成 TC 之關係 |
|---|---|---|
| `Feature not available while the vehicle is in motion` | `HMI Settings List` `Settings` r666 c7 | **與 profile §2.1 觀察面 B 逐字相同**（源 HMI spec p4）|
| `Function not available while vehicle is in motion` | 同檔 `Settings` r151 c7 | **不同**：`Function`／無 `the` |

### 何以不回修任何 TC

觀察面 B 之權威為 **Driver Lockout HMI spec p4**（R-DD5 所綁）。
`HMI Settings List` **未綁於本 feature，非語料** —— 故：

- **不回修任何 TC**
- **不改 profile §2.1**
- **不登 DR** —— 該不一致存在於**未綁之文件內**

> **這一條的價值在它記下了一件「現在不必處理」的事。**
> 若日後綁定該檔、或 Settings 側之 popup 進入範圍，
> 二變體之取捨會立刻變成問題 —— 屆時不必重新發現它。

### 何以不入 marker 登記表（下放包 19 §七 T-登 明命）

marker 登記表之每一列課予**生成義務**（用及某物即須標）。
本條為 INFORMATIONAL，**不課任何生成義務** —— 入表即等於要求 TC 標一個
沒有假設內容的 marker。**登記表只登有義務者。**

狀態：**INFORMATIONAL**（無撤銷條件；隨綁定範圍變更而重新評估）。
