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

---

## FB-DIAG-g　`SWE1-Diagnostics-154` 之標題與描述互不相稱

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID |
|---:|---|---|---:|---|
| 161 | `SWE1-Diagnostics-154` | `SYS-RA-DIAG-367` | 368 | `4940482` |

- **Title**：`Audio - Return NRC 0x31 Request Out of Range when the channel number does not correspond to a valid AV input using DID $0312`
- **Description**：`Audio - Return detection result indication for Video, Audio Left, and Audio Right signals using DID $0312`

兩者不是同一件事：

- Description 與本列所掛之 `SYS-RA-DIAG-367`（CFTS004 r368：「The return results of this routine shall
  indicate for each of the Video, Audio Left and Audio Right signals, whether a signal was detected or not supported.」）**一致**。
- Title 之內容對應的是 **另一條** 需求 `SYS-RA-DIAG-371`（CFTS004 r372：「If the radio receives a channel number
  that does not correspond to an audio or video input, it shall return a "Request Out of Range" negative response,
  code $31.」），而該條在 037 已另有列 —— **row 167 `SWE1-Diagnostics-160`**。

另：本列之 Description 為單一句、無編號步驟，與 037 其餘列之三段式體例不同，形似誤貼之標題。

**測試側處置**：依來源規格勝出原則，取 Description ＋ 所掛之 `SYS-RA-DIAG-367` 產出正向結果回報測試用例。
**建議修正 Title，使其與 Description 及所掛來源一致。**

---

## FB-DIAG-h　`SWE1-Diagnostics-340`（row 347）之 NRC 名稱與 CFTS004 不符

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID |
|---:|---|---|---:|---|
| 347 | `SWE1-Diagnostics-340` | `SYS-RA-DIAG-264` | 265 | `4940355` |

037 之 Title 與 Description 皆書 **`"Previous Out of Range"`**：

> 1. If the new input source is not compatible with the radio, the radio shall return a "Previous Out of Range" negative response.

同一 `$500D - Video Input Settings` 節下之 CFTS004 r267（`SYS-RA-DIAG-266`，ObjectID `4940356`）書：

> If the new input is not compatible with the radio, the radio shall return a "Request Out of Range" negative response, code $31.

`"Previous Out of Range"` 在 ISO 14229-1 無對應之 NRC 名稱；`requestOutOfRange`（`$31`）才有。
CFTS004 其餘三處（r267、r372、`SYS-RA-DIAG-270`）一律書 `"Request Out of Range"`。

**測試側處置**：依來源規格勝出原則取 CFTS004 用字與 `$31`。
**建議 037 下一版更正為 `"Request Out of Range"`。**

---

## FB-DIAG-i　`SWE1-Diagnostics-331`／`-332` 之標題與所掛來源不符

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID | CFTS004 原文 |
|---:|---|---|---:|---|---|
| 336 | `SWE1-Diagnostics-329` | `SYS-RA-DIAG-043` | 44 | `4939921` | This DID shall report the current number of **enumerated USB devices, excluding Hubs and SD Card readers** |
| 338 | `SWE1-Diagnostics-331` | `SYS-RA-DIAG-045` | 46 | `4939919` | This DID shall report the current number of **detected USB Hub devices** |

兩列之 037 Title 幾乎相同：

- row 336：`USB - Report current number of connected USB devices the current number of enumerated USB devices, excluding Hubs and SD Card`
- row 338：`USB - Report current number of connected USB devices via DID 2870`

row 338 之 Title 與 Description 皆未提及 **Hub**，而其所掛之 `SYS-RA-DIAG-045` 正是 Hub 數。
其 negative 對應列（row 337 `-330`／row 339 `-332`）之 Title 亦逐字相同，無法由 Title 區辨所驗對象。

**測試側處置**：依來源規格勝出原則，row 338 產為「detected USB Hub devices」之測試用例。
**建議修正 row 338／339 之 Title，使其標明 USB Hub。**

---

## FB-DIAG-j　`SWE1-Diagnostics-333` 將 UDS 負回應與資料值混寫

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID |
|---:|---|---|---:|---|
| 340 | `SWE1-Diagnostics-333` | `SYS-RA-DIAG-046` | 47 | `4939922` |

037 之 Description：

> SW shall ensure no internal state or functionality is affected by unsupported service requests and shall
> return the negative response – **Service Not Supported $FF** as the result if the USB detection is not available.

CFTS004 r47 原文：

> The radio shall report **$FF as the result** if the USB detection is not available.

`$FF` 在 CFTS004 是 **USB 偵測不可用時之回報資料值**，不是 UDS 負回應碼；
而 `Service Not Supported` 在 ISO 14229-1 為 NRC `$11`。037 將兩件事寫進同一句，
使該列既像 unsupported-service 測試又像資料值回報測試。

**測試側處置**：依來源規格勝出原則，產為「USB 偵測不可用時正向回報 `$FF`」之測試用例，
非 negative response 測試。
**建議 037 下一版拆為兩句，或刪去與本列來源無關之 `Service Not Supported`。**

---

## FB-DIAG-k　I/O Control（`$2F`）是否受 Security Access（`$27`）保護 —— 詢 SYSAD 作者

`SYS3_CFTS_004_General Diagnostics_System Architectural Design_SYSAD.docx` §4.5
「Session & Security Assumptions」逐字：

> ECU starts in Default Session.
> Security access (0x27) is required for:
> - Write DID
> - Routine execution
> - DTC clearing

**列舉未含 I/O Control（`$2F`，InputOutputControlByIdentifier）。**

本 feature 之 CFTS004 有 **15 個 I-O Control DID 節、114 個 037 列**使用 `$2F`
（`$5000` Buzzer Control、`$5001` Speaker Quadrant Selection、`$5002`–`$5006` Tone Settings、
`$5008`／`$5009`／`$500A`–`$500D`、`$5100` 等），數量遠多於 Routine（27 列）。

**問**：此為漏列，抑或 I/O Control 刻意不需 Security Access？

**測試側現況**：`$2F` 之測試用例一律先取得 Security Access（保守寫法）。
若實機不需要，此前提為多餘但無害；若實機需要而測試用例未寫，測試者會得到
`7F 2F 33 (securityAccessDenied)` 並誤判為缺陷。**回覆後可據以移除或保留。**

---

## FB-DIAG-l　CFTS004 引用 `$D013` 而文件內無該章節

| 引用處 | CFTS004 列 | ObjectID | 原文 |
|---|---:|---|---|
| `$5000 - Buzzer Control` | 325 | `4940296` | Tool controlled tones shall be output to each speaker output unless specific outputs are requested using **$D013** |
| 同上 | 327 | `4940283` | Typically, this DID is used with **$D013** to direct test tones to specific speaker outputs |

`$D013` 在 CFTS004 全文**無對應章節**，其功能、參數與編碼皆無處可查。

037 之 `SWE1-Diagnostics-115`／`-116`／`-117`（row 122–124）據該引用寫成
「`0x31 (RoutineControl)` request for DID `0xD013`」—— 但：

1. `$D013` 在 CFTS004 無定義，無從得知其服務與參數；
2. 037 稱其為 `0x31` RoutineControl，而 CFTS004 將該要件置於 **I/O Control 之 `$5000` 節**；
3. 同段另一處（CFTS004-4940283）說 `$D013` 與 `$5000` **並用**，語意上更像另一個 I/O Control DID 而非常式。

**測試側處置**：依來源規格勝出原則，以 CFTS004 所載之
「未請求特定輸出時，tool-controlled tone 預設送至每個喇叭輸出」為驗證點，受測 DID 取 `$5000`。
**建議**：(1) 確認 `$D013` 是否應收入 CFTS004；(2) 若不屬本文件，於引用處註明其出處文件。

---

## FB-DIAG-m　`SWE1-Diagnostics-048` 述「診斷 session 不支援」之失效而無 NRC

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID |
|---:|---|---|---:|---|
| 55 | `SWE1-Diagnostics-048` | `SYS-RA-DIAG-047` | 30 | `4939942` |

037 之 Description 述**兩種**失效：

> 2) IOC will validate the current diagnostic session for the DID and rerturn the negative response
> if the **current diagnostic session is not supported**.
> 4) if requested command is invalid format or invalid in length or invalid parameters then SW return
> the Negative response

第二種（格式／長度／參數）已依既有判準拆為兩條測試用例。
第一種（**session 不支援**）之 NRC 在 CFTS004、037、SYSAD **三處皆未載**——
SYSAD §4.5 只述「ECU starts in Default Session」而無對應碼。

**測試側處置**：不為該軸產出測試用例（無可斷言之 NRC，產出即造值）。
**建議**：037 或 CFTS004 補明該情形之 NRC。

（另：本列 Description 之 `rerturn` 為 `return` 之誤，一併回報。）

---

## FB-DIAG-n　`$5006`／`$5005`（fade／balance）無 negative 與 unsupported 需求列

| DID | CFTS004 節 | 037 列 | 型態 |
|---|---|---|---|
| `$5006 - Fade Settings` | r294–r297 | `SWE1-Diagnostics-064`（row 71）／`-065`（row 72）| **全為 positive** |
| `$5005 - Balance Settings` | r298–r301 | `SWE1-Diagnostics-066`（row 73）／`-067`（row 74）| **全為 positive** |

對照同組其他 DID：

| DID | positive | negative | unsupported |
|---|---:|---:|---:|
| `$5004` Treble | 3 | 1 | 1 |
| `$5003` Bass | 3 | 3 | 3 |
| `$5002` Volume | 3 | 3 | 3 |
| **`$5006` Fade** | **2** | **0** | **0** |
| **`$5005` Balance** | **2** | **0** | **0** |

CFTS004-4940326 明載 `Valid values for fade control step shall be from 9 front to 9 rear`，
CFTS004-4940322 明載 `from 9 left to 9 right` —— **值域存在，但 037 未收「超出值域」與
「不支援之服務請求」兩種行為**，而同組其餘三個 DID 都收了。

**測試側處置**：因該二 DID 無 negative 列可掛，越界行為改以**邊界值分析**掛在其值域列
（`-064`／`-066`）之下，取 `=min`／`=max`／`min−1`／`max+1` 四點；
`$5004`／`$5003`／`$5002` 因已有 negative 列，只取有效邊界二點，避免重複。

**建議**：037 下一版為 `$5006`／`$5005` 補 negative 與 unsupported 列，與同組其餘 DID 一致。

---

## FB-DIAG-o　`$030A - Clear Key Sense PIN` 之行為只指向本文件外之規格

| 037 列 | SWE-Requirement ID | Source Requirement ID | CFTS004 列 | ObjectID |
|---:|---|---|---:|---|
| 354 | `SWE1-Diagnostics-346` | `SYS-RA-DIAG-373` | 374 | `4940469` |

CFTS004 原文全句：

> When commanded to perform this routine, the radio shall behave per the **KeySense HMI Logic and Flow**.

該常式之**全部行為**指向「KeySense HMI Logic and Flow」，而：

1. 該文件**不在本 feature 之來源集**（`sources/MANIFEST.tsv` 無此件，`REF/` 17 檔亦無）；
2. CFTS004 未載其文件編號、版本或章節，無從索取；
3. `$030A` 節下無其他條目可補其行為。

**測試側處置**：依 §8.4.1（不造值），ER 只斷言常式回正回應且完成，
不斷言任何 KeySense 行為。此為 Layer 2 #20 之唯一一列，故該組之測試深度受限於此。

**建議**：(1) 提供「KeySense HMI Logic and Flow」之文件編號與版本；
(2) 或於 CFTS004 補述該常式之可觀察結果。

---

## FB-DIAG-p　`SWE1-Diagnostics-154` 之 Title 與 `-160` 重複（batch 4 再度確認）

CDD-02 已以 **FB-DIAG-g** 回報 `-154`（row 161）之 Title 與 Description 不相稱。
batch 4 產出 `-160`（row 167）時確認：**`-154` 之 Title 與 `-160` 之 Title 為同一件事**——

| 037 列 | SWE1 ID | Title（節錄）| 所掛來源 | CFTS004 原文 |
|---:|---|---|---|---|
| 161 | `-154` | `Return NRC 0x31 Request Out of Range when the channel number does not correspond to a valid AV input` | `SYS-RA-DIAG-367` | The return results … Video, Audio Left and Audio Right … |
| 167 | `-160` | `Return NRC 0x31 Request Out of Range when the AV Channel Number does not correspond to a valid audio or video input` | `SYS-RA-DIAG-371` | If the radio receives a channel number that does not correspond … `"Request Out of Range"`, code `$31` |

`-160` 之 Title 與其來源相稱；`-154` 之 Title 是**同一句話貼錯列**。
兩列之 Description 與來源則各自正確。

**建議**：`-154` 之 Title 改為與其 Description 及 `SYS-RA-DIAG-367` 一致
（即三訊號之偵測結果回報），與 FB-DIAG-g 併處。

---

## FB-DIAG-t —— `CIP Radio Tables v6.7`：`MPFA Select Process` 之 NOTE 與同圖本體矛盾

**對象**：CIP Radio Tables 維護者（v6.7，2023-03-03，Marcio Luz）

`MPFA Select Process(X65, X40)` 分頁之流程圖，其 NOTE 首行為：

```text
-3 retries with:  600 ms Timeout, Transaction ID = 0x02, Option = 0x02 (Return $FF)
```

而同一張圖之節點 4／5 為 `TransactionID = 0x01, Option = 0x01`（Select 之值）。
`MPFA Validate Process` 分頁之 NOTE 與其本體則一致（皆 `0x02`）。

**判斷**：Select 圖之 NOTE 係自 Validate 分頁複製而未改 `TransactionID`／`Option`。
**影響**：retry 五結局之語意兩圖相同，測試用例不受影響；但文件讀者會誤以為 Select 的重試判斷用 `0x02`。
**建議**：Select 圖 NOTE 首行改為 `Transaction ID = 0x01, Option = 0x01`。

> **FB-DIAG-r 改述**：原書「`SX-9830-0095` 與 `CIP Radio Tables` 流程圖兩件皆不在來源集」——
> `CIP Radio Tables` **實已於 2026-09-16 置於 `forms/`**，CDD-12 已登錄並轉錄兩張流程圖。
> 本項改為只求 **`SX-9830-0095` 本文**與 **vehicle sales code → PkgIndex 對照表**（`DR-DIAG-8` 現為 PARTIAL）。
