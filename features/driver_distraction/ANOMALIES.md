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

### 處置

- **`-025`~`-028` 凍結**，不入任何批次（下放包 02 §二，隨包生效）。
- framework 組 6 `Market Speed Gating` 維持市場中立佔位名，**組名不寫入工作簿任何列**。
- 其餘 24 leaf 之生成**不受阻**。
- **DR-DD1** 已登記（DRAFTED，待 Pei 發送）。

狀態：PENDING（待 DR-DD1）。

---

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

狀態：PENDING（待 DR-DD2）。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-DRnn]`.
