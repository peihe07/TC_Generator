# Diagnostics 037 需求回饋 —— 給 RD（Nik）

母體：`SWE1_Diagnostics_V1 (3).xlsx`（sha16 `d317a38f249b7bd8`，C 版，389 列／166 源）
追溯索引：`SYS2_CFTS_004_General_Diagnostic_Requirements_All_Accepted_Done State.xlsx`
（sha16 `ffcb202fff92007e`，`Basic Report` 404 列）
出具：測試設計側，2026-09-17。列號皆為 Excel 實際列號（037 之 `Analysis Report`／CFTS004 之 `Basic Report`）。

**六項皆不阻斷測試用例產出**，已各自以裁定處置；此表供 037 下一版根除用。

---

## FB-DIAG-a　`SWE1-Diagnostics-340` 重號

同一個 SWE1 ID 出現在兩列，指向**不同**的來源需求：

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | 標題領域 |
|---:|---|---|---:|---|---|
| 347 | `SWE1-Diagnostics-340` | `SYS-RA-DIAG-264` | 265 | `4940355` | Audio（`$500D` Video Input Settings）|
| 348 | `SWE1-Diagnostics-340` | `SYS-RA-DIAG-188` | 189 | `4939684` | Clock Defrost（`$280C` ECU Current Internal Settings）|

**測試側處置**：工作簿以 `SWE1-Diagnostics-340-001`（row 347）／`-340-002`（row 348）區分，
037 不改。**建議 037 下一版改為兩個獨立 ID。**

---

## FB-DIAG-b　`SWE1-Diagnostics-189`～`192` 之 Verification Method 空白

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | Verification Method |
|---:|---|---|---:|---|---|
| 196 | `SWE1-Diagnostics-189` | `SYS-RA-DIAG-124` | 125 | `4939821` | **（空白）** |
| 197 | `SWE1-Diagnostics-190` | `SYS-RA-DIAG-124` | 125 | `4939821` | **（空白）** |
| 198 | `SWE1-Diagnostics-191` | `SYS-RA-DIAG-125` | 126 | `4939820` | **（空白）** |
| 199 | `SWE1-Diagnostics-192` | `SYS-RA-DIAG-125` | 126 | `4939820` | **（空白）** |

全 389 列中僅此 4 列空白。同組之 `SWE1-Diagnostics-187`／`-188`
（row 194/195，`SYS-RA-DIAG-123`，CFTS004 r124，ObjectID `4939819`）為同型且有值。

**測試側處置**：依 `-187`／`-188` 之步驟型態產出，Remarks 註
`037 VM blank; procedure derived from Description + CFTS004`。**建議補填。**

---

## FB-DIAG-c　`SWE1-Diagnostics-057` 引用 CFTS004 之 Out of Scope 條目

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | CFTS004 Category |
|---:|---|---|---:|---|---|
| 64 | `SWE1-Diagnostics-057` | `SYS-RA-DIAG-248` | 249 | `4940710` | **`Out of Scope`** |

該來源於 CFTS004 之 `SYS2 限定地區 Region` 欄亦為空白（全 166 個被引用來源中唯一）。
其 Description 為「AMP shall process any chimes, and the HU shall switch phone call to cell phone.」，
所屬章節為 `$1801 - Screen Test Pattern (Read/Write)`。

**測試側處置**：不產測試用例；工作簿保留一列，`Test Result` 欄填 `Out of Scope`，
Remarks 註 `CFTS004 Category: Out of Scope`。
**建議確認：此條目是否應收入 037。**

---

## FB-DIAG-d　CFTS004 有 52 條功能需求未收入 037

CFTS004 `Basic Report` 中 Category = `Functional Requirement` 而未被 037 任何列引用者共 **52** 條
（另有 13 條 Category = `Out of Scope` 亦未引用，不列入）。

母節分佈：Read/Write DID Requirements **36**／I/O Control DID Requirements **6**／
Diagnostic Routine ID Requirements **10**。

集中處（前幾名）：`$280E - Splash Screen` 5 條、`$1806 - Current Frequency Settings` 5 條、
`$2974 - Suspend to RAM Configuration` 3 條、`$2843 - X65 Module Version` 3 條、
`$280B - SCL/PCL/Sales Code Configuration` 3 條。

逐條清單（含 CFTS004 列號、`SYS-RA-DIAG` 號、ObjectID、章節、原文）見所附
`features/diagnostics/data/cfts004_uncited_fr.tsv`（52 列）。

**測試側處置**：不補產（依裁定，範圍以 037 為準）。
**建議確認：此 52 條是否為有意不收。**

---

## FB-DIAG-e　negative／unsupported 之定型句未載 NRC 值

037 之三段式中，negative response 列（133）與 Service Not Supported 列（93）共 **226 列**，
其 Description 為全本共用之定型句，措辭為：

> 3. The SW shall respond with an appropriate negative response code (NRC).

**未指明是哪一個 NRC**。226 列中：

| NRC 值之來源 | 列數 |
|---|---:|
| CFTS004 原文明載 | 5 |
| 037 自身明載（如 `Service Not Supported (NRC $11)`）| 20 |
| 兩者皆無值，但 037 已述失效型態（invalid length／unsupported DID／…）| 198 |
| 兩者皆無值且**未述失效型態** | **3** |

CFTS004 側全 404 列中提及 negative response 者僅 7 列，帶值者 5 列
（`$22, Conditions Not Correct` ×2；`"Request Out of Range", code $31` ×3）。

最後 3 列為：

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | 問題 |
|---:|---|---|---:|---|---|
| 163 | `SWE1-Diagnostics-156` | `SYS-RA-DIAG-369` | 370 | `4940477` | Description 為標題之複製，未述失效型態 |
| 164 | `SWE1-Diagnostics-157` | `SYS-RA-DIAG-369` | 370 | `4940477` | 同上 |
| 244 | `SWE1-Diagnostics-237` | `SYS-RA-DIAG-056` | 57 | `4939892` | 只書「an appropriate NRC」；其 CFTS004 來源亦只書「shall provide a negative response」|

**測試側處置**：198 列依 ISO 14229-1 標準碼（限 `0x11`／`0x12`／`0x13`／`0x22`／`0x31` 五碼，
且只在 037 已述失效型態時）補值，Remarks 註 `NRC per ISO 14229-1 (037 unspecified)`；
3 列標 PENDING。
**建議 037 下一版於定型句中直接寫出 NRC 值，可根除此項。**

---

## FB-DIAG-f　V1 (3) 刪除 GPS Date-Month／Date-Day 六列

`SWE1_Diagnostics_V1 (3).xlsx` 相對於 `V1 (2)` 僅刪除末 6 列，其餘 383 列 × 35 欄零格差，
封面仍為 C 版、修訂履歷無對應之新列：

| V1 (2) 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | 標題 |
|---:|---|---|---:|---|---|
| 397 | `SWE1-Diagnostics-389` | `SYS-RA-DIAG-167` | 168 | `4939716` | GPS - Report the Date - Month using this DID `$2812` |
| 398 | `SWE1-Diagnostics-390` | `SYS-RA-DIAG-167` | 168 | `4939716` | GPS - Handle the negative response while reporting the Date - Month |
| 399 | `SWE1-Diagnostics-391` | `SYS-RA-DIAG-167` | 168 | `4939716` | GPS - Handle the Unsupported service requests while reporting the Date - Month |
| 400 | `SWE1-Diagnostics-392` | `SYS-RA-DIAG-168` | 169 | `4939717` | GPS - Report the Date - Day using this DID `$2812` |
| 401 | `SWE1-Diagnostics-393` | `SYS-RA-DIAG-168` | 169 | `4939717` | GPS - Handle the negative response while reporting the Date - Day |
| 402 | `SWE1-Diagnostics-394` | `SYS-RA-DIAG-168` | 169 | `4939717` | GPS - Handle the Unsupported service requests while reporting the Date - Day |

`SYS-RA-DIAG-167`／`-168` 於 CFTS004 仍為 `Functional Requirement`，因本次刪除而
**回歸「未收入 037」清單**（FB-DIAG-d 之 50 → 52）。

**測試側處置**：此 6 列不產測試用例；以 V1 (3) 為母體。
**建議確認：(1) 刪除是否有意；(2) 若有意，CFTS004 之 `SYS-RA-DIAG-167`／`-168`
是否應同步改為 Out of Scope；(3) 修訂履歷未記此次變更，建議補一列。**
