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

**二筆皆為 DRAFTED，尚未發送。**

---

## DR-DD1 —— 市場條件衝突（`-025`~`-028`）

- **標的**：037 作者／上游
- **狀態**：DRAFTED（下放包 02 §三 之文稿，逐字保留；待 Pei 發送）
- **阻斷範圍**：`-025`~`-028` 四 leaf 凍結（A-DD1 暫行處置）

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
