# 上繳包 19 —— pilot v2 lint、內部服務主體普查、觀測通道盤查

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/20_observability.md`
  （SHA256 `6bba31c9e6429e175ae6aab5a200609ef17448b436d717caed3c75d5a7fe65fd`，357 行）
- **未結 DR：1 筆（DR-SU1）**｜新登 anomaly：0 筆
- 新腳本：`scripts/observability.py`；`scripts/gen_pilot.py` 改 v2

## 本輪四個主結果

1. **pilot v2 之 lint 與預期完全相符**：**K=0／T=0／U=3**，
   21 項中 **20 項全 0**。U=3 為 DR-SU1 之三個佔位，**唯 DR 落地方能清零**。
2. **內部服務主體之列為 126／311（41%）**，分佈極不均：
   `Telematics Client` **100%**、`Interruption Handling` 74%、
   `Session Flows`／`Bearer Selection` 69%；而 `Update HMI` **0%**。
3. **觀測通道盤查：`adb`／`logcat`／`dumpsys`／`debug`／`shell` 三源皆 0。**
   `log`／`diagnostic` 之命中共 34 處，**逐一檢視後無一為測試觀測通道** ——
   全部是「軟體自己寫 log」或「車輛診斷作為需求主題」。§4.2。
4. **答案已在 repo 裡（第四次）**：037 有 **`Verification Criteria`（310 列非空）**
   與 **`Verification Method`（311 列全非空）** 兩欄，本 feature 自 T2 起
   **從未讀過**。其中 **32 列之 Method 明載 `HMI Validation Testing`，
   且該 32 列與本輪之 126 個內部列交集為 0** —— 完美分離。§4.3。

---

## 1. T33e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU25 | 869 | **OK** | `0b079ed3cb96` |

逐字 append，**既有 38 個條文區塊未受影響** ✅（現 39 塊）。
索引表現行 **25 條**（新增 R-SU25）；留存 **14 條**（無變動）。
與下放包 20 §五 T33e 所定之「25 條現行」一致。

`PLAYBOOK.md` §7 追加 **(19)**「lint 全綠不等於 TC 對」，
並列出 lint **查不到**之三類（驗錯了東西／跑不起來／錨錯了），
與交付前該問之三句（首句即 R-SU25(e) 之「台架上的人要看哪裡？」）。

---

## 2. T33a —— pilot v2 之產出與 lint

產出：`sandbox/pilot02/…_ext.xlsx`（R-G25，5 列 × 14 欄）。
TC ID 沿用 `newR1L-SU-001`–`005`（同列同 ID，未重新編號）。
v1 之 `sandbox/pilot01/` 保留為 v1 受檢物，**不覆寫、不作交付**。

```
python3 scripts/lint036.py <pilot02 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=3  V=0        exit 0
```

### 2.1 與下放包所載預期之比對

| 項 | 下放包 20 §五 T33a 之預期 | 實測 | |
|---|---|---|:--:|
| K（CJK 字元） | **0** | **0** | ✅ |
| T（PENDING 說明非英文） | **0** | **0** | ✅ |
| U（PENDING 佔位） | **3** | **3** | ✅ |
| 其餘 18 項 | （未載） | 全 **0** | — |

**三項預期全中，無不符。** v1 → v2 之差為 **K 3→0、T 3→0**，
成因即下放包 20 §四之英文化；**U 不變（3）**，因 DR-SU1 仍 OPEN。

### 2.2 v1 與 v2 之對照

| | v1（`pilot01`） | v2（`pilot02`） |
|---|---|---|
| lint 違規 | K=3／T=3／U=3 | **K=0／T=0／U=3** |
| 全 0 之項數 | 18/21 | **20/21** |
| 台架可執行性 | **5 個 TC 皆有不可執行步驟**（上繳包 18 §7.1） | 已改寫（下放包 20 §四之三個作法） |

> ⚠ **v2 之可執行性未被 lint 驗證，亦非本輪任務。** lint 之 20/21 全 0
> 與 v1 之 18/21 一樣**不涵蓋可執行性**（PLAYBOOK §7(19)）。
> v2 是否真的可跑，仍待實機或分析層之判斷 —— 見 §6.2。

---

## 3. T33b —— 內部服務主體之普查（全 311 列）

### 判準（逐一揭露）

**(1) 內部服務主體**（取自全 311 列之主詞普查，見 §主詞表）：

```
SWMC
WiFi\s*Update\s*Service
WiFiUpdateService
USB\s*Update\s*Service
ROV\s*Update\s*Service
TBM\s*Update\s*Service
Arbiter\s*Service
WiFi\s*Manager
Connectivity\s*Manager
Update\s*Engine(?:\s*Manager)?
SW\s*Updater\s*(?:Service|Manager)
Redbend\s*(?:SWMC|Update\s*Agent)
ROV\s*FOTA\s*AppService
OTA\s*[Cc]lient
```

**(2) 外部可觀測面之語形**（R-SU25(a) 所列之面）：

| 面 | regex |
|---|---|
| HMI／畫面 | `\bHMI\b|screen|display|displayed|popup|pop-up|PU\d{3,4}|notification|prompt|message|icon|banner|toast` |
| 使用者互動 | `\buser\b|press|touch|tap|select|button|opt[- ]?in|opt[- ]?out|defer|accept|decline` |
| 版本／設定值 | `\bversion\b|software\s*version|SW\s*version|configuration\s*report|inventory` |
| CAN／訊號 | `\bCAN\b|\bsignal\b|\bDID\b|\$[A-Z_]+\.` |
| 檔案／儲存 | `\bfile\b|filesystem|file\s*system|storage|partition|\bflash\b` |
| 聲音／燈 | `\bchime\b|\bsound\b|\baudio\b|\bLED\b` |

**分類**：主詞命中 (1) **且**全句無任何 (2) 之命中 → **內部列**。
> **執行層只分類語形，不裁定該列是否真無可觀測後果**（下放包 20 §五）。

### 主詞表（前 16，供判準 (1) 之依據）

| 主詞 | 次數 | 內部？ |
|---|---:|:--:|
| `SWMC` | 146 | ✅ |
| `WiFi Update Service` | 137 | ✅ |
| `WiFiUpdateService` | 47 | ✅ |
| `SW Update HMI` | 38 | — |
| `ROV Update Service` | 37 | ✅ |
| `ROV FOTA HMI` | 29 | — |
| `TBM Update Service` | 26 | ✅ |
| `WiFi Update Service/USB Update Service` | 21 | ✅ |
| `TBM FOTA HMI` | 17 | — |
| `HMI` | 16 | — |
| `Arbiter Service` | 10 | ✅ |
| `WiFi Manager` | 9 | ✅ |
| `When the update type` | 4 | — |
| `Update Engine` | 4 | ✅ |
| `SWMC and WiFi Update Service` | 4 | ✅ |
| `Redbend Update Agent` | 4 | ✅ |

### 結果

| 類 | 列數 | 佔 311 |
|---|---:|---:|
| **內部列**（主詞為內部服務且無外部面語形） | **126** | **41%** |
| 非內部列（有外部面語形，或主詞非內部服務） | 185 | 59% |
| **合計** | **311** | 100% |

### 內部列之 id 清單（126 列）

`005`；`008`；`010`；`012`；`014`；`019`；`025`；`026`；`028`；`033`；`034`；`047`；`054`；`057`；`061`；`067`；`070`；`071`；`080`；`107`；`111`；`126`；`138`；`139`；`143`；`146`；`147`；`151`；`157`；`160`；`163`；`165`；`169`；`171`；`173`；`179`；`181`；`205`；`206`；`207`；`208`；`209`；`210`；`216`；`246`；`249`；`252`；`253`；`255`；`256`；`258`；`260`；`261`；`262`；`264`；`267`；`268`；`269`；`272`；`273`；`274`；`275`；`277`；`279`；`281`；`282`；`286`；`288`；`289`；`290`；`297`；`298`；`299`；`300`；`301`；`302`；`303`；`305`；`306`；`307`；`308`；`311`；`312`；`313`；`315`；`316`；`318`；`319`；`321`；`323`；`324`；`327`；`328`；`329`；`330`；`331`；`332`；`333`；`341`；`345`；`347`；`349`；`350`；`355`；`356`；`357`；`358`；`359`；`360`；`361`；`363`；`364`；`365`；`366`；`367`；`368`；`369`；`370`；`372`；`373`；`374`；`376`；`379`；`380`；`381`；`383`


### 內部列於 21 個 Test Set 之分佈

| Test Set | 內部列 | 該組總列數 | 佔比 |
|---|---:|---:|---:|
| `Wi-Fi Download` | **7** | 29 | 24% |
| `Update Policy` | **8** | 17 | 47% |
| `Silent Update` | **2** | 9 | 22% |
| `Deployment Flow` | **10** | 26 | 38% |
| `Session Flows` | **11** | 16 | 69% |
| `Client Architecture` | **21** | 35 | 60% |
| `Bearer Selection` | **11** | 16 | 69% |
| `ROV Installation` | **1** | 20 | 5% |
| `TBM Reflash` | **1** | 14 | 7% |
| `HU FOTA via TBM` | **3** | 36 | 8% |
| `USB Update` | **1** | 5 | 20% |
| `Update HMI` | 0 | 6 | 0% |
| `Configurable Parameters` | **1** | 2 | 50% |
| `FOTA Overview` | **2** | 6 | 33% |
| `Integrity Verification` | **4** | 8 | 50% |
| `Interruption Handling` | **14** | 19 | 74% |
| `Status Reporting` | **5** | 7 | 71% |
| `Deployment Conditions` | **2** | 8 | 25% |
| `Session Management` | **8** | 13 | 62% |
| `Telematics Client` | **5** | 5 | 100% |
| `Update Agent` | **9** | 14 | 64% |
| **合計** | **126** | **311** | **41%** |

### 外部面之命中分佈（非內部列，185 列）

| 外部面 | 命中列數 |
|---|---:|
| HMI／畫面 | 133 |
| 使用者互動 | 92 |
| 版本／設定值 | 11 |
| CAN／訊號 | 22 |
| 檔案／儲存 | 15 |
| 聲音／燈 | 1 |

非內部列中，**主詞未命中內部服務清單者 9 列**：`039`、`042`、`130`、`177`、`212`、`224`、`231`、`240`、`244`



### 3.1 分佈之三個極端（供分析層排序）

| Test Set | 內部列／總列 | 讀法 |
|---|---|---|
| `Telematics Client` | **5 / 5（100%）** | **全組皆內部列** —— TC 通訊建立、訂閱、session 轉送，無一句提及外部面 |
| `Interruption Handling` | 14 / 19（74%） | 其外部面之 5 列多為「不觸發 HMI」之否定式 |
| `Update HMI` | **0 / 6（0%）** | 全組皆有外部面 —— 與其命名一致，可作判準之正向校準 |

**`Update HMI` 之 0% 與 `Telematics Client` 之 100% 是判準之兩端校準點**：
前者證明判準不會把明顯之 HMI 列誤判為內部；後者指出一整組在現況下
可能一列都寫不出可執行之 TC。

---

## 4. T33c —— 觀測通道之盤查

掃描語形（**查得與否皆如實回報，查無不得代以推定**）：

| 通道 | regex |
|---|---|
| adb | `\badb\b` |
| logcat | `\blogcat\b` |
| dumpsys | `\bdumpsys\b` |
| log | `\blog\b|\blogs\b|\blogging\b|log\s*tag` |
| trace | `\btrace\b|\btracing\b` |
| diagnostic | `\bdiagnostic|\bdiagnosis\b|\bUDS\b|\bDID\b|\bDTC\b` |
| debug | `\bdebug\b|\bdeveloper\s*mode\b` |
| test hook | `\btest\s*(?:hook|mode|interface)\b` |
| shell | `\bshell\b|\bconsole\b` |

### 結果

| 通道 | (i) 037 全欄（383 資料列） | (ii) CFTS_57（487 物件） | (iii) SYSAD 全文 |
|---|---:|---:|---:|
| `adb` | 0 | 0 | 0 |
| `logcat` | 0 | 0 | 0 |
| `dumpsys` | 0 | 0 | 0 |
| `log` | **4** | **3** | **6** |
| `trace` | **4** | 0 | 0 |
| `diagnostic` | **6** | **14** | **1** |
| `debug` | 0 | 0 | 0 |
| `test hook` | **1** | 0 | **1** |
| `shell` | 0 | 0 | 0 |

**三源合計命中：40**

- **037 / `trace`（4）**：`SWE1-FOTA-031`、`SWE1-FOTA-042`、`SWE1-FOTA-045`、`SWE1-FOTA-060`

- **037 / `log`（4）**：`SWE1-FOTA-142`、`SWE1-FOTA-325`、`SWE1-FOTA-329`、`SWE1-FOTA-334`

- **037 / `diagnostic`（6）**：`SWE1-FOTA-150`、`SWE1-FOTA-197`、`SWE1-FOTA-198`、`SWE1-FOTA-199`、`SWE1-FOTA-205`、`SWE1-FOTA-250`

- **037 / `test hook`（1）**：`SWE1-FOTA-241`

- **037 / `adb`（0）**：

- **037 / `logcat`（0）**：

- **037 / `dumpsys`（0）**：

- **037 / `debug`（0）**：

- **037 / `shell`（0）**：

- **CFTS_57 / `diagnostic`（14）**：`4907320`、`4907326`、`4907336`、`4907368`、`4907388`、`4907389`、`4907392`、`4907393`、`4907394`、`4907631`、`4907635`、`4907641`…

- **CFTS_57 / `log`（3）**：`4907673`、`4907680`、`4907690`

- **CFTS_57 / `adb`（0）**：

- **CFTS_57 / `logcat`（0）**：

- **CFTS_57 / `dumpsys`（0）**：

- **CFTS_57 / `trace`（0）**：

- **CFTS_57 / `debug`（0）**：

- **CFTS_57 / `test hook`（0）**：

- **CFTS_57 / `shell`（0）**：

- **SYSAD**：`log`×6、`diagnostic`×1、`test hook`×1

### 4.1 五個開發工具語形：三源皆 0

`adb`／`logcat`／`dumpsys`／`debug`／`shell` 於
**037 全欄（383 列）／CFTS_57（487 物件）／SYSAD 全文** 三源之命中**皆為 0**。

**無任何素材指名一條可供測試者讀取內部狀態之工具通道。**

### 4.2 ⚠ `log` 與 `diagnostic` 之 34 處命中，逐一檢視後**無一為觀測通道**

命中不等於通道。逐條讀其原文：

| 類 | 例（原文摘） | 判讀 |
|---|---|---|
| `log` — 037 `325` | 「The SWMC shall suspend the OTA update session, **record the interruption in the log**」 | **軟體自己寫 log**；**無任何素材說明測試者如何讀它**（無路徑、無 tag、無工具） |
| `log` — 037 `329` | 「the SWMC shall **log the failure** and abort」 | 同上 |
| `log` — 037 `334` | 「including … **CAN communication log** associated with the failure」 | log 之**內容**被上傳到 OTA server，非測試者可讀之面 |
| `log` — CFTS `4907673`/`4907680` | 「**Write the interruption to the log**」 | 同 037，需求主體之行為 |
| `diagnostic` — 037 `150` | 「The Head Unit shall continue to support **diagnostic mode** requests while the locked state is active」 | **診斷模式是被測之主題**，不是觀測手段 |
| `diagnostic` — 037 `198` | 「no unintended **diagnostic trouble codes (DTCs)**」 | DTC 為被測之副作用 |
| `diagnostic` — 037 `199` | 「transmit periodic **diagnostic Tester Present** messages to external ECUs」 | 需求主體之行為 |
| `diagnostic` — 037 `205` | 「read required **vehicle diagnostic signals through CarProperty Manager** including ignition state, battery voltage, vehicle speed」 | **最接近通道者** —— 但其為**被測軟體**讀取車輛狀態之介面，非測試者讀取軟體狀態之介面 |
| `diagnostic` — CFTS `4907320` | 「OTA client shall have access to **diagnostic information about the current state of the vehicle**」 | 同 `205`，方向相反 |

**結論（如實回報，不代以推定）**：
**本 feature 之三源素材中，查無任何可作觀測通道者。**
`log` 與 `diagnostic` 之全部命中皆為**需求所述之軟體行為**或**被測主題**，
其方向與觀測通道相反 —— 軟體寫 log／軟體讀車輛診斷，
而**沒有一句說明測試者讀什麼**。

### 4.3 ⚠ 答案已在 repo 裡（第四次）—— 037 之二欄從未被讀過

盤查過程中發現 037 有二欄本 feature **自 T2 起從未使用**：

| 欄 | 標頭 | 非空列數 |
|---|---|---:|
| 16 | `Verification Criteria` | **310 / 383** |
| 17 | `Verification Method` | **311 / 383** |

`Verification Method` 之值分佈（前 3）：

| 值 | 列數 |
|---|---:|
| `Unit Test / Integration Test / System Test` | 180 |
| **`Integration Test`（僅此一項）** | **87** |
| `Unit Test / Integration Test / System Test` + `HMI Validation Testing`（及其延伸串接） | 32 |

`Verification Criteria` 之語形為 `Ensure…`／`Simulate…`／`Monitor…`／`Observe…`
—— **即該列作者對「怎麼驗」之既有判斷**。

#### 交叉核對：一支持、一否證

以 `Verification Method` 對本輪之 126 個內部列做交叉表：

| Verification Method | 內部列 | 非內部列 | 合計 |
|---|---:|---:|---:|
| `Integration Test`（僅此一項） | 23 | 64 | 87 |
| `Unit Test / Integration Test / System Test`（含各種串接） | 103 | 121 | 224 |
| **合計** | **126** | **185** | **311** |

**(否證)** 若「內部列較難系統測」，內部列應**較常**被標 `Integration Test`。
實測相反：**內部列中僅 18% 標之，非內部列則有 35%** ——
**方向與假說相反。** 即 037 作者之測試層級判斷與本輪之語形分類
**測的不是同一件事**。

**(支持)** `Verification Method` 含 **`HMI Validation Testing`** 者共 **32 列**，
**其中內部列 0 列** —— **完美分離**。
即：凡 037 作者明載「須做 HMI 驗證」之列，本輪判準**一列都沒有誤判為內部**。
**這是對判準之特異度（不誤判外部列）之獨立佐證**，
而其獨立性來自：該欄由 037 作者所填，與本輪之 regex 無任何共用輸入。

**執行層不裁定該二欄之地位**（其是否可作 Layer 3、可作 TC 之素材、
或其 `Integration Test` 之標記是否即「不可系統測」），列為待確認。

**依 PLAYBOOK §7.3 之附註**（「方案評估時，先掃他 feature 之 `scripts/`」）
之同型：**本次是「先掃本 feature 之素材有沒有未讀之欄」**。
037 之 18 欄中，本 feature 迄今只用了 6 欄（`A`/`B`/`C`/`D`/`F`/`G`）。

---

## 5. T33d —— DR-SU1 之更新

`DATA_REQUESTS.md` 之 DR-SU1：

- `Batch impact` 改為指向 **v2 之三行英文佔位**（逐字載於檔內）
- 狀態**維持 `OPEN`**、Urgency 維持 `High`
- 新增 v1／v2 之 lint 對照表（K/T 由 3→0，**U 不變為 3**）
- 明載：**U=3 唯有 DR-SU1 落地方能清零** —— 其為 DR 之直接量度，非格式問題

---

## 6. 未結 DR 清單

| # | 事項 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | **OPEN** | `newR1L-SU-003` 三欄 PENDING（U=3） |

**未結 1 筆。**

### 待分析層確認之事項（非 DR）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **037 之 `Verification Criteria`／`Verification Method` 二欄之地位** —— 是否入 TC 素材；`Integration Test`（87 列）之標記是否即「不可系統測」 | §4.3 |
| 2 | **126 個內部列之處置** —— 逐列判其有無可觀測後果（R-SU25(c)），或整組掛 PENDING 並發第二筆 DR 求觀測通道 | §3 |
| 3 | **`Telematics Client`（5/5 全內部）** 是否在現況下整組無法產出可執行之 TC | §3.1 |
| 4 | **v2 之可執行性未被驗證** —— lint 不涵蓋，本輪亦未有實機 | §2.2 |

---

## 7. 獨立自評

### 7.1 §六.6 所問：語形判準之偽陽性與偽陰性方向

**二者皆有，且皆可量化。**

#### (甲) 偽陰性 —— 真內部列被漏掉：**至少 11 列**，成因單一

`notification` 與 `message` 二詞被我放進「HMI／畫面」之 regex，
**而該二詞在本 feature 同時指「使用者通知」與「服務間訊息」**。

實測：185 個非內部列中，**59 列僅因「HMI／畫面」一面而被排除**；
其中 **11 列只命中 `notification`／`message` 而無 `HMI`／`screen`／`prompt`
等強語形**：

`199`、`201`、`235`、`241`、`248`、`250`、`254`、`304`、`310`、`337`、`353`

逐條看其原文，**全部是服務間訊息**：

| 列 | 原文摘 |
|---|---|
| `199` | 「transmit periodic diagnostic Tester Present **messages** to external ECUs」 |
| `201` | 「exchange OTA session information … and control **messages** through standardized communication」 |
| `235` | 「subscribe to the MQTT FOTA topic "FOTA" to receive OTA-related **messages**」 |
| `241` | 「maintain FOTA_TBM_**Notification**, FOTA_TBM_Forced … as Boolean status indicators」 |
| `248` | 「receive server-initiated update session trigger **notifications**」 |

**修正後內部列將由 126 增為 137（44%）。**
**本輪不自行修正判準** —— 改 regex 即為看著結果轉旋鈕（PLAYBOOK §7(7)）；
**列出其方向與量，由分析層裁是否改**。

#### (乙) 偽陽性 —— 其實有可觀測後果之列被判為內部

**有二個不同的成因，而第二個嚴重得多。**

**(b1) 詞彙落在 EXTERNAL 表之外。** 126 個內部列中，
**28 列含車輛狀態／連線語形**（`ignition`／`battery voltage`／`vehicle speed`／
`current draw`／`Wi-Fi connect`／`CarProperty`），例如 `205`。
但此為**條件面**（依 R-SU25(d) 屬 Pre-Condition），
**不等於有可觀測之結果面** —— 故只是候選，不是確認之偽陽性。

**(b2) 可觀測後果存在但文字裡沒有它 —— 這一類我的判準在原理上看不見。**

**本輪之 pilot v2 自己就是證據。** 下放包 20 §四把
「更新在背景執行」之驗證面改成**版本號之前後變化**（`Version_initial` /
`Version_after`）—— 而**「version」一詞在 `SWE1-FOTA-175` 之 Description 裡
一個字都沒有**。

即：**一個需求可以毫無外部面之字眼，而其行為仍有可觀測之後果。**
我的判準測的是「**文字裡有沒有提到外部面**」，
**不是「這件事有沒有可觀測之後果」** —— 二者不同，且後者不可由語形判定。

**故 126 這個數字之正確讀法是**：
**「Description 全文未提及任何外部面之列數」之上界**，
**不是「無可觀測後果之列數」**。
真正之後者只能逐列人裁 —— 而那正是下放包 20 §五所令
「執行層只分類語形，不裁定該列是否真無可觀測後果」之理由。

**能誠實說的是**：126 列**需要逐列被問一次**「它的可觀測後果是什麼」，
而不是 126 列**沒有**可觀測後果。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §2 之「20/21 全 0」與「三項預期全中」。**

那兩格合起來讀像是「v2 已驗證通過」。實際上：
- **lint 之 20/21 全 0 不涵蓋可執行性** —— 而可執行性正是 v2 存在的唯一理由
  （v1 之 lint 是 18/21，其失分全在 PENDING 之語言，與可執行性無關）。
  **v1 → v2 修的是可執行性，而 lint 之改善來自英文化 —— 二者無關。**
- **「三項預期全中」之預期是我自己依改寫內容推出來的**，
  與 PLAYBOOK §7(17)（種子須為獨立觀測）同型：K/T 由 3→0 是因為
  下放包把中文改成英文，**這件事不需要 lint 也知道**。

**真正有鑑別力的是 `U=3` 不變** —— 它證明改寫**沒有偷偷把 PENDING 拿掉**
（把 PENDING 刪掉會使 U 歸零、報告全綠，而 DR 仍未解決）。
**那一格才是本輪 lint 唯一驗到東西的地方。**

### 7.3 一項我做了而下放包未要求的事

**§4.3 —— 盤查通道時順手數了 037 之欄，發現二欄從未被讀過。**

T33c 只令查三源有無 `adb`／`log`／診斷之字樣。照做會得到
「五個開發工具語形三源皆 0、log/diagnostic 之命中皆非通道」，**答案完整**。

我另做的是**看那些命中落在哪一欄** —— 因為 037 之掃描是全欄 join 的。
於是撞到 `Verification Criteria`（310 列非空）與 `Verification Method`
（311 列**全**非空）**兩欄**，而本 feature 自 T2 建 `feature.yaml` 起，
037 之 18 欄只用了 6 欄。

**其中 `Verification Method` 是直接相關的**：它是 037 作者對每一列
「該用什麼方法驗」之既有判斷，而本輪整包在問的正是「這列驗得起來嗎」。

**記明此事之理由**：這是「答案已在 repo 裡」之第四次
（前三次為 DR-VC6 佐證欄、R-VC19 加註、display 之外科式實作），
且**這次不在他 feature，而在本 feature 自己的主素材裡** ——
盲區從「沒去看別人的目錄」變成「沒去看自己手上這份檔的全部欄位」。
**掃描寫得再全，掃的範圍是自己選的**。
