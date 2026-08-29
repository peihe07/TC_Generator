# ER_ASSERTIONS — ER 斷言之分類台帳（R-SU42 回溯掃描）

**T49c**（下放包 36 §四）之一次性回溯：現有 **17 個 TC**、**75 行 ER**、
**38 句相異**，逐句標其為 **(a) 物理必然**／**(b) 設計選擇**／**(c) 不適用**。

**R-SU42 之判別問句**：**「這件事若不是這樣，是否意味硬體壞了？」**
答是 → (a)，**不需來源文件明載**；答否 → (b)，**須有來源，無來源即為造值**（§8.4.1）。
**拘束 2：不確定一律歸 (b)** —— 二者之代價不對稱。

**(c) 不適用**：該行不是對系統行為之斷言，而是**測試作業本身之記錄確認**
（如「Version_initial 已記錄」）。其真假由測試者之動作決定，不由系統決定。

> ⚠ **本表以「相異句」為單位（38），不以「行」為單位（75）** ——
> 同一句出現於多個 TC 者其分類與來源相同，分開列會使同一個問題看起來像多個。

---

## 一、總計

### v2 —— R-SU42 v2 之重分類（T50b，下放包 37）

| 類 | 相異句 | 行次 | 說明 |
|---|---:|---:|---|
| **(a) 物理必然** | **1** | 1 | 斷電則裝置停止 |
| **(a2) 測試者操作之直接反映**（v2 新類） | **4** | 4 | **由 (b) 無來源改判** —— 見 §三 v2 |
| **(b) 設計選擇・有來源** | **17** | 47 | 來源為 037 該列自身或其 CFTS 錨 |
| **(b) 設計選擇・⚠ 無來源** | **2** | **8** | **`remains operable` 族，見 §四** |
| **(c) 不適用** | **7** | 8 | 記錄確認 |
| **(c) `PENDING` 佔位** | **7** | 7 | 其內容未定，暫不分類（**落地時須回本表，R-SU42 v2(d)**） |
| **合計** | **38** | **75** | |

**(b) 無來源者由 6 句降至 2 句** —— 與下放包 37 §五-3 之預期相符。

〔v1 之計數，保留為沿革〕(a) 1／(b) 有來源 17／**(b) 無來源 6**／(c) 14。

---

## 二、(a) 物理必然（**1** 句）

| 句 | TC | 判別 |
|---|---|---|
| `The head unit powers off` | `015` | 切斷電源供應則裝置停止運作 —— **若不停止即意味硬體故障**。R-SU42(a) |

> **拘束 1 之套用**：本句之 (a) 資格**限於「停止」這個後果本身**。
> 若寫成「於 2 秒內停止」「停止時顯示關機動畫」，其細節即為 (b)。
> 本句未帶任何細節，故成立。
>
> **`The head unit completes start-up`（句 16）之前半同屬 (a)**
> （恢復供電則啟動），惟該句後半為 (b)，故整句列於 §三。

---

## 三 v2、(a2) 測試者操作之直接反映（**4** 句，由 (b) 無來源改判）

**R-SU42 v2(a2)**：測試者於 Procedure 執行某操作後，該操作在 UI 或系統狀態上之
**直接反映**。其非「被驗證之系統行為」，而是**測試者確認自己的操作已生效**。
**不需來源。**

| 句 | TC | 為何屬 (a2) | 二項拘束 |
|---|---|---|---|
| `the head unit settings show Wi-Fi as disabled` | `013` | 測試者剛於設定關閉之直接反映 | 測試者所造成 ✅；於 Final Step 為 `while` 限定 ✅ |
| `the head unit settings still show Wi-Fi as enabled with no connection present` | `012` | 測試者關閉之對象為 **AP**，HU 設定未被觸碰 —— 其「仍為啟用」即該操作**未觸及 HU 設定**之反映 | ✅／✅ |
| `the head unit shows no Wi-Fi connection` | `012` | AP 關閉之直接反映 | ✅／✅（ER 第 3 行，非判定核心） |
| `The host system connector is disconnected` | `016` | **本輪改寫**（下放包 37 §3.3）—— 原句 `The head unit loses the host system connection` 斷言 HU 之狀態，需消歧「HU 是被拔者還是觀察者」；改寫後陳述**連接器**之狀態，不涉 HU 之角色 | ✅／✅ |

> ### ⚠ **§三 v1 所記之「條文交互作用」已消解**
>
> R-SU41(c) 令把觸發側狀態帶進 Final Step、R-SU42(b) 令此類狀態須有來源 ——
> 二者曾使 `012`／`013` 之區分**無處可放**。
>
> **其成因不是二條文衝突，是 R-SU42 v1 之分類不完備**（缺 (a2)）。
> v2 增設該類後，**為履行 R-SU41(c) 而帶入之觸發側狀態，
> 若為測試者操作之反映，即不因入判定對象而需要來源**。
>
> **(a2) 之二項拘束缺一不可** —— 尤其第 2 項：
> 其**只得作為判定之限定條件**（`while …`／`after …`），
> **不得作為判定之核心**。核心仍須為 (a) 或有來源之 (b)。
> 否則「測試者做了什麼」會取代「系統做了什麼」成為驗證點。

---

## 三 v1〔沿革〕、(b) 設計選擇・無來源（**6** 句）—— 其中 4 句已改判 (a2)

**以下六句於 CFTS_57 語料與 037 該列之 Description 中皆查無依據。**
實測：`operable`／`responds to user input`／`home screen` 於 CFTS 全語料**命中 0**。

| # | 句 | TC | 為何是 (b) | 處置建議 |
|---:|---|---|---|---|
| 1 | `the head unit remains operable and its screen responds to user input`（六句之共同尾句） | `011`–`016`（**6 列**） | HU 於更新中斷後是否仍可操作，取決於實作之強健性；**不可操作不意味硬體壞了，只意味軟體沒做好** | **見 §四 —— 有一個部分來源** |
| 2 | `the head unit shows no Wi-Fi connection` | `012` | 連線確實中斷是物理的，**但 HU 是否顯示該事實是 UI 之設計** | 求 HMI 規格之連線狀態顯示 |
| 3 | `the head unit settings still show Wi-Fi as enabled with no connection present` | `012` | 同上，且「啟用但無連線」之並存狀態**尤其是設計選擇** | 同上 |
| 4 | `the head unit settings show Wi-Fi as disabled` | `013` | 使用者於設定關閉後設定顯示停用 —— 形式上自明，**但「設定頁存在且如此顯示」仍是設計** | 同上（弱） |
| 5 | `The head unit loses the host system connection` | `016` | **預設 HU 為觀察者而非被拔除之一方**，而 `320` 原文為 `the host system (HU/TBM)` | **見 §五** |
| 6 | `its screen responds to user input`（`015` 第 4 行、`016` 第 4 行之後半） | `015`／`016` | 同 #1 | 同 #1 |

### ⚠ **一項條文交互作用，須明記**

**R-SU41(c) 令把觸發側之狀態帶進 Final Step；R-SU42(b) 令此類狀態須有來源。**

上表 #2／#3／#4 **正是為履行 R-SU41(c) 而寫進去的** ——
`012` 與 `013` 之區分（`enabled with no connection` vs `disabled`）
**就是這三句**。

即：**滿足 R-SU41 的動作，製造了三個 R-SU42(b) 之無來源斷言。**
二條文各自成立，其交會處**產生了一個新的來源需求**，
而下放包 35／36 皆未預見。

**若該三句取不到來源**，則 `012`／`013` 之區分**又回到無依據之狀態** ——
但這一次它是在判定對象內，**其代價比寫在第 3 行更高**
（前者是交付物中之無來源斷言，後者只是區分不足）。

---

## 四、#1 之部分來源 —— `CFTS057-4907440`

實測全語料後，**唯一相關者**：

> **`4907440`（章 4.7.1 OTA Client Performance Requirements）**
> `OTA client shall be a low priority process when active such that it does not
> impact normal functionality of the host system (ex, navigation/radio shall not
> be impacted).`

**其射程與本句不吻合**：

| | `4907440` | 六 TC 之斷言 |
|---|---|---|
| 時點 | **更新進行中**（`when active`） | **中斷發生之後** |
| 對象 | OTA client 不影響 host system 之正常功能 | HU 於中斷後仍可操作 |

**「更新中不影響正常功能」不蘊含「中斷後仍可操作」** ——
後者是關於**失敗路徑之強健性**，而 `4907440` 講的是**正常路徑之資源佔用**。

**故本句之來源為「部分」**：其精神有據，其射程無據。
**執行層不逕自引用該錨**（引之即等於宣稱射程吻合），列為待裁：

- **(甲)** 引 `4907440` 並於 `reasoning` 明記其射程差；或
- **(乙)** 求一條關於中斷後系統狀態之需求（可能落在 `321` `4907673` 之復原表）；或
- **(丙)** 刪除該尾句 —— **惟刪除後六列之 Final Step 只剩版本比對**，
  而「更新未完成」與「更新未完成且系統壞了」**在 ER 上將無從分辨**，
  中斷處理之驗證意義大幅縮小。

---

## 五、#5 之新證據 —— host system 之多主機讀法有據，惟未消歧

下放包 36 §1.3 之論證依賴「拔除主機連接器不影響 HU 自身之寫入」，
執行層前一輪指其與 `320` 原文之 `the host system (HU/TBM)` 不合。

**本輪查得一條相關依據**：

> **`4907340`（章 4.4.2 OTA Client Configuration options）**
> `In the event that the OTA client components are on **multiple host systems**
> (tethered phone for example), common communications interfaces shall be defined
> in order to communicate between components…`

**故「host system 可為多個，HU 為其一，另一個被拔除時 HU 為觀察者」之讀法有據** ——
分析層之論證**不是憑空**。

**惟其未消歧**：`320` 原文並列 `HU/TBM`，**未指明被拔者為何者**。
若被拔者即 HU，則 §1.3 之論證仍不成立。
**本項仍待分析層確認，但其性質由「無據」降為「有據而未消歧」。**

---

## 六、(b) 設計選擇・有來源（**17** 句 / 47 行次）

其來源為 **037 該列自身之 Description** 或**其已裁之 CFTS 錨** ——
即該句所斷言者，正是該需求所要求者。**此類為 ER 之正常形態。**

| 句（節錄） | TC | 來源 |
|---|---|---|
| `The update availability check completes and an update is reported as available` | 16 列 | 更新可用性查詢為各列之共同前置；其行為載於 CFTS 4.7 之 availability check 段 |
| `The recorded screen content contains no download confirmation screen` | `006` | `180` Description 第一句 ＋ `4907482` |
| `The recorded screen content contains no deployment confirmation screen` | `007` | `182` ＋ `4907484` |
| `The recorded screen content contains no update progress notification at any point of the session` | `002` | `176` facet A ＋ `4907476` |
| `The recorded screen content contains no opt-out control and no defer control` | `004` | `177` ＋ `4907478` |
| `The safety-related notification is displayed on the head unit and the session continues` | `003` | `176` facet B ＋ `4907477`（其**條件**為 DR-SU1） |
| `The head unit displays the update success notification and the What's New details of the deployed package` | `005` | `183` ＋ `4907485` |
| `Version_after differs from Version_initial; …no SW Update prompt and no progress notification` | `001` | `175` ＋ `4907475` |
| `Version_after differs from Version_initial; …no…confirmation screen`（TC-8 之長句） | `008` | `184` ＋ `4907486` |
| `Version_after differs from Version_initial; no user input occurred between download completion and installation` | `010` | `181` ＋ `4907483` |
| `No user interaction occurs before the download request is issued` | `009` | `179` ＋ `4907481` |
| `The software version shown on the head unit differs from Version_initial` | `005` | 更新完成之定義，各列共用 |
| `The Wi-Fi access point is switched off` | `012` | 測試者動作之後果（觸發側） |
| `The Wi-Fi connection is switched off` | `013` | 同上 |
| `The host system connector is reconnected` | `016` | 同上 |
| `The head unit completes start-up`（句 16 之前半） | `015` | **(a)** —— 見 §二之註 |
| `…recorded as continuous video capture`（四句，觀測手段） | `001`–`004`／`006`／`007`／`010` | **R-SU36(b)** 之明令寫法 |

---

## 七、(c) 不適用（**7** 句 / 8 行次）＋ `PENDING` 佔位（**7** 句）

| 類 | 句 | 說明 |
|---|---|---|
| 記錄確認 | `Version_initial is recorded`（13 行）／`Version_after is recorded`（9 行） | 其真假由測試者之動作決定，非系統行為 |
| `PENDING` 佔位 | 七句（DR-SU1 一、DR-SU2 五、DR-SU3 一） | **其內容未定，暫不分類** —— DR 有答案後須逐句回本表分類 |

> **記明**：`PENDING` 佔位落地時**即為新的 R-SU42 判別時點** ——
> 上游給的觀測手段若含 UI 狀態之描述，該描述同樣須有來源。
> **不得因其出自上游即免於分類**（上游給的是**手段**，不是**需求**）。

---

## 八、待裁清單

| # | 事項 | §|
|---:|---|---|
| 1 | **六列共同尾句之處置**（甲引 `4907440` 記射程差／乙另求來源／丙刪除） | §四 |
| 2 | **`012`／`013` 之區分句無來源** —— 而其為履行 R-SU41(c) 之產物 | §三 |
| 3 | `016` 之 `loses the host system connection` —— 有據而未消歧 | §五 |
| 4 | `PENDING` 落地時之回本表分類義務，是否立為條文 | §七 |
