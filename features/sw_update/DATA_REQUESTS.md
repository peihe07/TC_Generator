# DATA REQUESTS — SW Update (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/sw_update/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| **DR-SU2** | **v2（縮編，下放包 29 §二）** —— **(a)** Error Code 之**顯示途徑**確認；**(b)** Wi-Fi FOTA session 之**正向狀態**觀測；**(c)** **第三型之區辨手段**（`179`／`181`）。「106 列全部之觀測手段」**已不再請求** —— 其負向半由 `Error_Code_List.xlsx` 覆蓋（R-SU35） | **OPEN**｜**第二型 5 / 106**；**第三型 3 列（母群未經盤點）** | 第二型 5 列（`363`–`367`）＋第三型 **3 列**（`179`／`181`／`184`） | 三段式台帳（R-SU32 v2(f)）——**(b) 段之 106 僅對第二型有意義，不得冒充全體上界** | — | **High** |
| **DR-SU1** | **靜默期間之安全相關通知條件清單**（pattern：規格側之 safety-related notification 條件表；來源未定，得為 CFTS_57 之補件或 SYSAD 之安全需求節） | **OPEN** | `SWE1-FOTA-176`（facet B） | `newR1L-SU-003`（v2）之 `pre`／`proc`／`er` 三欄各掛一**英文** `PENDING`；該 TC 不可執行 | — | **High** —— pilot 批已受阻，Silent Update 之 9 列尚有 5 列未撰 |

## DR-SU2 —— 詳（下放包 23 §3.1）

**其標的為上游文件之內在不一致，非我方之困難** ——
此為本輪對該 DR 立論之關鍵改變：

> 037 自身將該 105 列之 **85% 標為含 `System Test`**，
> 而其 `Verification Criteria` **未指出任何外部可觀測面**。
> **文件說要做系統測，卻沒說系統測時要看哪裡。**

（先前之立論為「我們找不到通道」—— 對上游而言那是我方之困難，
非其文件之缺陷。上繳包 21 §2 之實測把它變成了文件內在之不一致。）

**佐證之三項實測**：

| 項 | 實測 | 出處 |
|---|---|---|
| 需求本文未提外部面之列 | **126／311（41%）** | 上繳包 19 §T33b |
| 其中 `Verification Criteria` 亦未提者 | **105／126（83%）** | 上繳包 20 §2.0 |
| 三源素材之觀測通道語形（`adb`／`logcat`／`dumpsys`／`debug`／`shell`） | **皆 0** | 上繳包 19 §4.1 |
| 105 列中標「僅 `Integration Test`」者 | **15%**（對照：非內部列 35%） | 上繳包 21 §T35a |

**初始清單（5 列，`Telematics Client`）**：

| 037 列 | 標題 | `Verification Method` | VC 之檢查對象 |
|---|---|---|---|
| `363` | TC Communication Establishment | Unit/Integration/**System** | communication **is established** ❌ |
| `364` | TC Subscription for OTA Updates | Unit/Integration/**System** | the **callback is registered** ❌ |
| `365` | Server-Initiated Session Handling from TC | Unit/Integration/**System** | the request **is received**／**forwarded** ❌ |
| `366` | FOTA Update Availability Check | Unit/Integration/**System** | the OTA server **is queried** ❌ |
| `367` | Server-Initiated Session Forwarding from TC | Unit/Integration/**System** | the request **is forwarded**／**queued** ❌ |

### ⚠ 三段式台帳（**R-SU32 v2(f)**，由二段改）

**改三段之理由**：R-SU30 v2(f) 之母群定義（語形條件 ∪ 已人裁為無觀測面者）
**涵蓋不了第三型** —— 第三型之列可能完全不符語形條件（`181` 即是，見下）。
二段式會把第三型硬塞進一個測不到它的母群裡。

| 段 | 定義（R-SU32 v2(f)） | 現況 |
|---|---|---:|
| **(a) 已確認・第二型** | 已逐列判定，**無任何外部可觀測後果**。所求為**觀測手段** | **5 列**（`363`–`367`） |
| **(b) 未確認之母群** | 「符合語形條件者」∪「已由人裁判定為無觀測面者」—— **僅對第二型有意義** | **106 列** |
| **(c) 已確認・第三型** | 有外部後果但**不可區辨**，或限定詞**不可量**。所求為**區辨手段** | **3 列**（`179`／`181`／**`184`**） |

**確認進度之記法**：**第二型 5 / 106**；**第三型 3 列，母群未知**。

> ### ⚠ **(c) 段無上界可報**（R-SU32 v2(f)）
>
> **第三型之母群未經盤點，其規模未知，且不可由語形估計。**
> `181` 為 R-SU32 v2(e) 之首例 —— 其 `Verification Criteria` **含外部面之語形**，
> **語形判準未攔下它**，而其限定詞「immediately after download」同樣不可完整驗證。
>
> **故 106 是第二型之上界，不是全體之上界。**
> 陳述時不得以 106 冒充全體 —— 二個集合正交（PLAYBOOK (28)）。

**記法之拘束（R-SU30(b)）**：不得只寫母群數而使人誤以為 106 列皆已確認。

### 已確認段之二型分記（**R-SU32(b)**）

**二型之 DR 請求內容不同，故須分記** —— 混記會使上游備錯東西。

| 型 | 成因 | **所求為何** | 列 |
|---|---|---|---|
| **第二型**（R-SU29(ii)） | **無任何外部可觀測後果** | **觀測手段** —— log tag／診斷 DID／服務介面定義／HMI 間接後果之對照 | `363`／`364`／`365`／`366`／`367`（5 列） |
| **第三型**（R-SU32(iii)） | **有外部後果，但與鄰列不可區辨** | **區辨手段** —— 可觀測其下載請求已發出之跡象，**或**上游確認該列之驗證得併入鄰列 | `179`（1 列） |
| **第三型**（R-SU32 v2(e)） | **限定詞不可量** —— `immediately after download`：下載完成時點無觀測通道，且規格未給閾值 | **區辨手段** —— 下載完成時點之可觀測跡象 | `181`（1 列）**⚠ 不屬 105 列** |
| **第三型**（R-SU32(iii)） | **與鄰列不可區辨** —— 其增額驗證點**為空**：`no confirmation screen` 已由 TC-6／TC-7 覆蓋、`no prompt`／`no progress notification` 已由 TC-1 覆蓋、`across the three phases` **不可觀測** | **區辨手段** —— 三階段之界線在外部如何辨識；若無，其驗證應**併入 `175`**（須上游確認，R-SU32(d)） | **`184`**（1 列，下放包 30 §2.2 改判） |

**`179` 之詳**（下放包 26 §4.1）：其外部後果為「使用者未做任何操作，
而下載自動開始並終至安裝」，**與 `175`（`newR1L-SU-001`）完全相同**；
二列之差別全在內部（DD metadata 之分析與下載請求之發出 vs 整體之背景執行），
**該差別無任何外部表徵**。

> ⚠ **不得以「無後果」記之**（R-SU32(a)）—— `179` 之後果存在。
> 記錯型別會使上游備一份觀測手段（log tag 之類），
> **而那份東西解不開本列** —— 本列要的是把它與 `175` 分開的方法。

> ⚠ **併入 `175` 是一種合法解，但須由上游確認**（R-SU32(d)）——
> 分析層與執行層皆不得逕定，逕定即等於代上游合併需求單元。

**二段之語意逐次載明**：
- **「已在 (a) 段」= 已逐列試過且取不到**
- **「不在 (a) 段」≠ 已確認有解** —— 其餘 100 列**尚未逐列試過**
- **二者不可互推。** 且 (b) 為 (a) 之**潛在上界**：DR-SU2 之規模可能達 106 列（母體 34%），
  而非現有之 6 列

> **進度為 6/106 —— 本 DR 不得被陳述為「已盤點完成」**（R-SU30(d)）。

### DR-SU2 v2 —— 縮編（下放包 29 §二，逐字）

**Pei 裁 `Error_Code_List.xlsx` 可用**（R-SU35）後，本 DR 之請求範圍縮編。
**縮編不是撤銷** —— 解掉的是**負向路徑**（失敗／中斷／拒絕之情形有碼可觀測），
正向路徑與讀碼位置皆未解。

```
DR-SU2 v2（縮編，2026-08-28）：

(a) Error Code 之顯示途徑確認 —— 錯誤碼於 HU 上如何呈現
    （開機後畫面？彈窗？工程模式頁？）。Error_Code_List 表首
    「After HU start-up, suddenly…」暗示畫面顯示，但未明載途徑。
(b) Wi-Fi FOTA session 之正向狀態觀測 —— Error Code List 覆蓋
    USB／SWDL 路徑之失敗面；Wi-Fi 路徑之進行中狀態
    （session 建立、下載中、DD 解析）仍無觀測定義。
(c) 第三型之區辨手段 —— `179`（下載請求 vs 背景執行）、
    `181`（下載完成時點）。不變。

已不再請求者：「106 列全部之觀測手段」—— 其負向半已由
Error_Code_List 覆蓋（R-SU35）。

舉證附件：診斷側三源窮舉（§1.2 之表，含版本號與筆數，可覆核）。
```

### 診斷側三源之窮舉（DR 之舉證附件，下放包 29 §1.2）

| 來源 | 規模 | FOTA／OTA／SW-update 觀測定義 | 執行層可覆核？ |
|---|---:|---:|:--:|
| `DTCs Matrix Core List Rev. 1.6.xlsx` | 7 分頁／254 筆 DTC | **0** | **✅ 已覆核** |
| `CFTS_004 General Diagnostic Requirements`（Jun 2026）+ SYSAD | 554 物件／168 DID／112 routine | **0** | ❌ 不在 repo |
| `SWE1_Diagnostics_V1.xlsx`（037 A03，395 列） | 395 需求列 | **0** | ❌ 不在 repo |

**執行層之覆核（T42d）**：`forms/DTCs Matrix Core List Rev. 1.6.xlsx` 以
`FOTA|OTA|CFTS057|software update|SW update` 正則掃全簿全頁 —— **0 命中**，
下放包 29 §1.2 之主張成立。

> ⚠ **另二源不在 repo 內**（其素材由 Pei 上傳至分析層側，分析層親測）。
> §二稱本表「含版本號與筆數，**可覆核**」—— 對上游而言確實可覆核，
> **但此側無法重現其中二筆**。DR 發出前宜將該二份原件或其掃描輸出一併落檔，
> 否則附件之三分之二在 repo 中無跡證。

> **另記**：下放包 29 §1.2 記 `DTCs Matrix` 為 **6 分頁**，實測 **7**
> （多一頁僅 1 列之 `Sheet1`）。不影響 0 命中之結論，記錄即止。

### 母群數之沿革（**R-SU30 v2(f)**：變動須逐次記明成因）

| 版 | 母群 | 已確認 | 成因 |
|---|---:|---:|---|
| 下放包 23 | 105 | 5 | 初始 —— (b) 段以語形條件圈定，(a) 段以人裁 |
| **下放包 26** | **106** | **6** | **(1) `365` 補入母群**：其 VC 首句含 `notification`（**服務間訊息**，非使用者通知），命中語形判準之**偽陰性**（上繳包 19 §7.1(甲) 已預告之類），致 (a) 非 (b) 之子集 —— 母群定義改為語形聯集人裁（R-SU30 v2(f)）；**(2) `179` 入已確認段**：第三型，見上 |
| **下放包 29** | **106**（第二型之上界） | 第二型 **5**／第三型 **2** | **(1) 台帳改三段**（R-SU32 v2(f)）—— 第三型另立 (c) 段，其母群**未經盤點**；**(2) `181` 入第三型**（R-SU32 v2(e) 首例，**不屬 105 列**）；**(3) 請求範圍縮編** —— 負向半由 `Error_Code_List.xlsx` 覆蓋（R-SU35），「106 列全部之觀測手段」不再請求 |
| **下放包 30** | **106**（不變） | 第二型 **5**／第三型 **3** | **`184` 入第三型** —— 下放包 28 §2.2 之否證係以一段**不存在之引文**（TC-1「自更新開始執行起錄」，`sandbox/pilot03` 實為 `…continuously until the update finishes`，**無起點**）為據，已撤銷；上繳包 25 §6.1(丙) 之原結論成立。**其成因為不可區辨，非無後果** |

> **`365` 一案之意義**（R-SU30 v2(f) 逐字）：該偽陰性**於 DR 清單本身出現，
> 是它首次造成台帳之邏輯不一致** —— 在此之前，語形偽陰性只是估計偏差；
> 在此之後，它使「6 / 106」這個比值一度不成立（分子不在分母裡）。

> ⚠ **本項之發現途徑**：非由 lint、非由 review，而是執行層在做**別的任務**
> （難類盤點，T38c）時撞到的。**二段判準不一致在台帳上看不出來** ——
> 二欄都是數字，數字都對，只有把二段之**入列條件**並排寫出才顯形。
> 已入 PLAYBOOK (27)。

---

## DR-SU1 —— 詳（下放包 19 §四 TC-3）

`CFTS057-4907477` 與 037 `SWE1-FOTA-176` 皆僅稱
「necessary for **safety requirements**」，**未列舉何者為安全相關條件**。
無此清單則**無可執行之觸發步驟** —— TC-3 之 Procedure 第 3 步
（「觸發一項安全相關條件」）無從寫成實機可跑之動作。

依 IN §8.4.3 掛 `PENDING`，**不得自行舉例**（如 eCall、碰撞偵測）
—— 舉例即造值（下放包 19 §四）。

**執行層之補充實測**：

| 版 | lint | 說明 |
|---|---|---|
| v1（`sandbox/pilot01`，上繳包 18 §T32b） | **K=3／T=3／U=3** | K 與 T 為草案本身之缺陷（PENDING 說明以中文書寫，違 R-14）；U 為計數用 |
| **v2（`sandbox/pilot02`，上繳包 19 §T33a）** | **K=0／T=0／U=3** | 下放包 20 §四已英文化，K 與 T 清零；**U=3 為 DR-SU1 之三個佔位，仍在** |

v2 之三行佔位（逐字）：

```
pre  3. PENDING: DR-SU1 list of safety-related notification conditions applicable during a silent session
proc 3. PENDING: DR-SU1 step to bring one safety-related condition into effect
er   3. PENDING: DR-SU1 observable state showing the safety-related condition is in effect
```

**U=3 唯有 DR-SU1 落地方能清零** —— 其為 DR 之直接量度，非格式問題。

## 本輪（下放包 01 + 02，2026-08-27）之結案記錄

Q5 裁定不發 DR，本輪執行後**維持 0 筆**。逐項確認：

- **CFTS_57 Reflash 原件**：不需 DR —— repo 側為真 OOXML（A-SU1），
  R-SU4 v2(a) 之 Q3 裁定照舊。
- **HMI 規格本文**：不需 DR —— 真 PDF 1.6，68 頁全文字層（A-SU1／R-SU6 v2）。
- **VF747**：已在 `inputs/`，並已綁定於 `feature.yaml` 之 `reference.vf747`。
  A-SU2 之 10 個 VF747 族 source id 因此**不構成外部引用**，不入本表。
- **PROXI**：`Brand_Configuration_2`（SWE1-FOTA-208 引用）於
  `forms/PROXI_HDCC27_R3_20250424.xlsx` `Format` 表 row 566 查得，
  已綁 `reference.proxi`，不需 DR。
- **Pop Up List**：`forms/Pop Up List HMI R1 (26PI).xlsx` 在場；
  A-SU3 之 `PU971` 為清單內查無，屬判讀問題非缺件，**不發 DR**。
- **DBC / LID**：037 無 CAN frame 與 Logical Identifier 引用（T4' 掃描），
  無外部引用可登記。

Standing rule 照常生效：日後新發現之外部引用仍須於登記 anomaly 之同時新增一列。
