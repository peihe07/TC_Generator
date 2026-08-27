# 上繳包 10 —— R-SU15 v2／R-SU16 抄錄、召回重估、列舉區塊普查

- 日期：2026-08-27
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/11_block_anchor.md`
  （SHA256 `e244dfb0f1df7f4fac87917dadffd2d43c71b919a82b6fa7c3b0b295afdc5d35`，232 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜新建台帳：`DESCRIPTION_DEFECTS.md`
- **本輪三個主結果**：
  1. **召回不是 100%** —— 累計 27 列地面真值下，N=5 為 **93%**、N=20 仍僅 **96%**。
     先前之「17/17（100%）」是小樣本假象
  2. **區塊普查獨立重現了地面真值** —— 4.12 區塊之滑動視窗對位得
     `315`–`320`，`top1=4`（恰為 315–318），**未使用任何地面真值資訊**
  3. **`292` 之 `4907460` 排名第 7** —— 在前 20 內，不是召回失敗

---

## 1. T24e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU15 v2 | 879 | **OK** | `7eb1ef43e8a6` |
| R-SU16 | 876 | **OK** | `20c87906b37c` |

**既有 19 個條文區塊未受影響** —— 逐一回讀比對 sha256，全數不變 ✅。

`PLAYBOOK.md` §7 追加 **(7)**「證明『零是真的零』與報『零』是兩件事」。

### 索引表（現行 16 條）

R-SU1(v1)／R-SU2(v1)／R-SU3(v1)／R-SU4(v2)／R-SU5(v2)／R-SU6(v2)／
R-SU7(v2)／R-SU8(v1)／R-SU9(v1)／R-SU10(v1)／R-SU11(v1)／R-SU12(v1)／
R-SU13(v2)／R-SU14(v2)／**R-SU15(v2)**／**R-SU16(v1)**

**留存之被取代條文（不得引用）5 條**：`R-SU5`(v1)、`R-SU7`(v1)、
`R-SU13`(v1)、`R-SU14`(v1)、**`R-SU15`(v1)**（其 (e) 未宣告語形掃描之界線）。

---

## 2. T24b —— 召回之重估（本輪核心）

累計地面真值 **27 列**（下放包 09 之 17 + 下放包 11 之 10；`292`／`217` 未裁不計）。

| N | 召回（≥1 正解在前 N） | 涵蓋（全部正解在前 N） |
|---:|---|---|
| **5** | **25/27（93%）** | 24/27（89%） |
| 10 | 25/27（93%） | 24/27（89%） |
| **15** | **26/27（96%）** | 25/27（93%） |
| 20 | 26/27（96%） | 25/27（93%） |

### 2.1 ⚠ 先前之「召回 100%」是小樣本假象

上繳包 08 §4 以 17 列回測得**召回 17/17（100%）**，
R-SU14 拘束 (a) 據此定「前 5」之 5 為地面真值回測值。

**新增 10 列後，N=5 之召回降為 93%**，且**加大 N 至 20 只回升到 96%**——
即缺口不是「N 不夠大」，是**有列之正解根本不在候選序列的前段**。

| 列 | 正解 | 前 20 內之排名 |
|---|---|---|
| `SWE1-FOTA-319` | `4907671` | **完全不在前 20** |
| `SWE1-FOTA-313` | 6 個 | `1, —, —, —, —, —`（只 1 個在內） |
| `SWE1-FOTA-320` | `4907672` | 第 **14** 名 |

`319`（D-1 缺字）與 `313`（統攝型）**皆為已知之結構性盲區**，
非參數問題。`320` 排第 14 —— **N=5 會漏，N=15 才進得來**。

### 2.2 對 R-SU14(a) 之影響（不裁，僅陳報）

R-SU14 拘束 (a) 已預留「若日後回測顯示召回不足，得由分析層調整並記其依據」。
本輪即該情形。可陳報之事實：

- N 由 5 加大至 15，召回 93%→96%、涵蓋 89%→93%（各多救 1 列，即 `320`）
- N 由 15 加大至 20，**無任何改善**
- 剩餘之 1 列（`319`）與 `313` 之 5 個正解，**加大 N 無效**

**代價未量**：N 加大會使階段二之人裁工作量成比例上升（5→15 為三倍），
而其收益為 27 列中之 1 列。**此權衡屬裁定，執行層不裁。**

### 2.3 `SWE1-FOTA-292` —— **不是召回失敗**

`4907460`（4.7.3，`The OTA client SHOULD support configurable network
priorities…`）**排名第 7**，分 0.171（首選 `4907569` 0.257）。

即：它**在前 20 內、不在前 5 內**。下放包 §3.3 之「疑似召回失敗」
應改為「**前 5 截斷**」—— 是 N 的問題，不是召回的問題。

前 20 全表見 §附錄 A。前 6 名皆為「建立連線／選網」類
（4.10.2／4.6／4.6.1×2／8.1／4.6.1），`4907460` 緊隨其後。
**正解之裁定仍屬分析層**（執行層不裁 `292` 之正解為何）。

---

## 3. T24c —— 列舉區塊之全母體普查

辨識法：需求物件之**自身文字**以 `n.` 或 `n)` 起首者為列舉項；
同母章內序號連續遞增（+1）且文件序相鄰者聚為一塊。

**辨識出 9 個列舉區塊，涵蓋 37 個需求物件**（487 之 7.6%）。

| # | 母章 | 起訖 ObjectID | 項數 | 各項首句 |
|---:|---|---|---:|---|
| 1 | 4.7.3.1 | `4907470`–`4907471` | 2 | 1. The download of the deployment pac ／ 2. When the deployment package is dow |
| 2 | 4.10.1 | `4907559`–`4907563` | 5 | 1. The OTA client runs the server-ini ／ 2. The OTA client runs a procedure to ／ 3. The OTA client initiates an OTA se ／ 4. It is RECOMMENDED that the  |
| 3 | 4.10.2 | `4907575`–`4907577` | 3 | 1. “Shoulder tap” message is received ／ 2. OTA client checks pre-condition li ／ 3. At this point the server initiated |
| 4 | 4.10.3 | `4907582`–`4907584` | 3 | 1. Vehicle polling timer causes a veh ／ 2. OTA client checks pre-condition li ／ 3. At this point the server initiated |
| 5 | 4.10.3 | `4907585`–`4907592` | 8 | 3. OTA server MAY request the client  ／ 4. OTA server MAY then provide a down ／ 5. OTA client SHALL download the DD a ／ 6. After acceptance, the OTA c |
| 6 | 4.10.4 | `4907596`–`4907597` | 2 | 1. User selects “check for vehicle so ／ 2. Client checks pre-condition list a |
| 7 | 4.10.5 | `4907602`–`4907607` | 6 | 1. Deployment package is made accessi ／ 2. The installation conditions are ch ／ 3. Deployment package signature verif ／ 4. Deployment package is parse |
| 8 | 4.12 | `4907667`–`4907672` | 6 | 1. Socket read/write error ／ 2. Network loss: Network error or no  ／ 3. The end-user deactivates data usag ／ 4. The vehicle is in an emergency sta ／ 5 |
| 9 | 4.12.1 | `4907683`–`4907684` | 2 | 1. Internal network interrupt: The OT ／ 2. External network interrupt: The OT |

### 對位候選（R-SU16(c)2／(c)3）

### 3.1 對位候選 —— 滑動視窗

| 區塊 | 母章 | 起訖 ObjectID | L | 最佳對位之 037 列 | in20 | top1 | 滿足 (d) |
|---:|---|---|---:|---|---:|---:|:--:|
| 1 | 4.7.3.1 | `4907470`–`4907471` | 2 | `SWE1-FOTA-030`–`SWE1-FOTA-031` | 2 | **2** | ✅ |
| 2 | 4.10.1 | `4907559`–`4907563` | 5 | `SWE1-FOTA-351`–`SWE1-FOTA-355` | 3 | **1** | ❌ |
| 3 | 4.10.2 | `4907575`–`4907577` | 3 | `SWE1-FOTA-349`–`SWE1-FOTA-351` | 2 | **0** | ❌ |
| 4 | 4.10.3 | `4907582`–`4907584` | 3 | `SWE1-FOTA-349`–`SWE1-FOTA-351` | 3 | **1** | ❌ |
| 5 | 4.10.3 | `4907585`–`4907592` | 8 | `SWE1-FOTA-351`–`SWE1-FOTA-358` | 5 | **3** | ✅ |
| 6 | 4.10.4 | `4907596`–`4907597` | 2 | — | 1 | 0 | ❌ |
| 7 | 4.10.5 | `4907602`–`4907607` | 6 | `SWE1-FOTA-133`–`SWE1-FOTA-140` | 2 | **2** | ✅ |
| 8 | 4.12 | `4907667`–`4907672` | 6 | `SWE1-FOTA-315`–`SWE1-FOTA-320` | 5 | **4** | ✅ |
| 9 | 4.12.1 | `4907683`–`4907684` | 2 | `SWE1-FOTA-328`–`SWE1-FOTA-329` | 2 | **2** | ✅ |

**連續對位候選 8 組。** 執行層產出候選，**不裁定對位成立**（R-SU16）。

### 3.2 ⚠ 區塊 8 **獨立重現了地面真值**

區塊 8（4.12，`4907667`–`4907672`，6 項）之最佳對位為
**`SWE1-FOTA-315`–`SWE1-FOTA-320`**，`in20=5`、`top1=4`。

**此結果未使用任何地面真值資訊** —— 對位純由「區塊邊界（CFTS 側編號連續）
+ 037 列序 + 前 20 候選之集合」導出。而下放包 §3.1 之人裁結果為：
`315`–`318` 四列之首選即其對位物件（`top1=4` ✅）、
`319` 之正解不在候選內（`in20=5`，缺的正是 `4907671` ✅）。

**兩者逐項相符。** 這是 R-SU16 之獨立驗證：該路確實不依賴文本相似度之排序
即可定出對位。

### 3.3 其餘 8 塊之對位候選 —— 執行層不裁

滿足 R-SU16(d)（`top1 ≥ 2`）者 **4 塊**：#1（4.7.3.1）、#5（4.10.3）、
#7（4.10.5）、#9（4.12.1），另加已驗之 #8。不滿足者 4 塊。

> **須留意 #7 之對位窗**：`SWE1-FOTA-133`–`SWE1-FOTA-140` 跨 8 個 id 而 L=6
> —— 因 037 之 in-scope 列不連號（Heading 已剔除），窗為**列序連續**而非
> **id 連續**。閱表時勿以 id 差判其長度。

### 3.4 初版對位邏輯之缺陷（自陳）

初版以「每項物件之**最小** 037 列號」判連續。該法錯誤：一個 CFTS 物件會出現在
許多 037 列之前 20 內，全域 `min` 取到的不是對位的那一列。
**其後果是連已知之 4.12 區塊都找不到（輸出 0 組）** ——
因為「已知答案對不上」而察覺，改為滑動視窗後方得上表。

**若無 `315`–`320` 這個已知標的，0 組會被當成「本語料沒有區塊」交出去。**

---

## 4. T24a —— `SWE1-FOTA-128` 之判定材料

材料見 §附錄 B（該列及其後 8 列之 id、title、Categorization、Description 全文）。
**執行層不裁定** `below mentioned parameters` 所指為何。

---

## 5. T24d —— 037 描述缺陷之語形掃描

新建台帳 **`features/sw_update/DESCRIPTION_DEFECTS.md`**，現載 2 筆：

| # | 037 列 | 形態 | 狀態 |
|---|---|---|---|
| D-1 | `SWE1-FOTA-319` | 缺字 —— 條件名脫落（`the handling of condition`） | **已確認**（下放包 11 §3.2） |
| D-2 | `SWE1-FOTA-248` | 缺字 —— 受詞脫落（`notify the to start`） | 待判定 |

六式掃描命中 3 處，其中 2 處為**偽陽性**：`SWE1-FOTA-295` 之
`evaluate the ./Ext/FCA/SilentInstall parameter` —— `the .` 為 DM tree 路徑之
起首點號，非孤立冠詞。

### 5.1 ⚠ 掃描漏掉了**種子案例本身**

D-1 之 `the handling of condition during…`：式1 要求
`(?:condition|state|…)\b(?!\s*\w)`（其後無詞），而該處後接 `during`，
**故不命中**。即：**若非下放包已指名 `319`，本掃描不會找到它。**

以**寬鬆式**（去 `(?!\s*\w)` 句尾條件）反向探測全母體：
命中 **1 處 / 1 列 —— 即 D-1 本身**。無其他同形態列。

### 5.2 缺字型缺陷之語形不穩定 —— 本台帳為下界

`the handling of condition` 之所以可偵測，是因為缺字處恰好落在
「介詞 + 抽象名詞」之間。若缺的是別的成分（如動詞、整個子句），
語形上與正常句無異。**缺字型缺陷之可偵測性取決於缺字後恰好接什麼**，
不是取決於缺陷之嚴重程度。

**故 `DESCRIPTION_DEFECTS.md` 所載為下界，非全集**，已於該檔明載。

---

## 6. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

---

## 7. 獨立自評

### 7.1 §六.6 所問：T24c 之區塊辨識對「CFTS 側未用編號但實質為列舉」者會如何

**會完全漏掉，而且不會有任何跡象。**

本輪之辨識法**只認 `n.` / `n)` 起首**。若 CFTS 之一組相鄰需求物件實質上
是列舉（如逐條描述六種錯誤情形）但**不加編號**——例如各項以
`The OTA client shall handle socket read/write errors.` / `…network loss.` /
`…user deactivation.` 之並列句式呈現——則：

- 辨識器輸出 0（不入 9 塊之列）
- **沒有任何訊號指出漏了東西** —— 不像 §3.4 之缺陷有「已知標的對不上」可察覺

已量之邊界：9 塊涵蓋 37 個物件，**佔 487 之 7.6%**。
其餘 **450 個物件（92.4%）之內部是否有無編號之列舉結構，本輪答不到。**

**可行之補強（提案，未做）**：以「同母章內相鄰物件之句首骨架相似度」
偵測無編號列舉（R-SU16(c)3 已預留此判準，惟該條亦明定
「僅有 (c)3 而無 (c)1／(c)2 者不足以定區塊」）。
本輪未做，因其屬新增偵測器而非本輪任務。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §3 的區塊普查表。**

「辨識出 9 個列舉區塊」讀起來像是普查完成。**它實際只說「9 個帶編號的
列舉區塊」** —— 而 R-SU16(f) 令的是「全母體之區塊普查」，
其中「區塊」之定義（(a)）為「以編號列舉呈現之一組相鄰需求物件」。

**條文之定義恰好與我的辨識法一致**（(a) 明寫「以編號列舉（`1.` `2.` `3.` …）」），
所以嚴格說我做到了條文所令。但**條文的定義本身可能窄於現象** ——
§7.1 之無編號列舉若存在，它在條文下不叫「列舉區塊」，
卻會有一模一樣的錨定價值。**這是定義的邊界，不是執行的缺口，
但結果是一樣的：那些列仍然無錨可落。**

### 7.3 一項我做了但下放包未要求的事

§5.1 之「對種子案例反向探測」。T24d 只令掃描並列出形態。

我另以寬鬆式回頭驗證 `319` 自己會不會被抓到 —— **答案是不會**。
若不做這一步，台帳會呈現為「掃描找到 D-1、D-2 兩筆」，
讀者會合理推論掃描是有效的；實際上 D-1 是下放包給的，掃描只找到 D-2。
**這個區別直接決定台帳該被當成全集還是下界。**

---

## 附錄 A —— `SWE1-FOTA-292` 之前 20 候選全表

Description：

> WiFiUpdateService shall manage the configured network priority and select the appropriate network for OTA communication. WiFiUpdateService shall establish the network connection and enable SWMC to communicate with the OTA Server

| # | ObjectID | 章 | 分 | 首句 |
|---:|---|---|---:|---|
| 1 | `4907569` | 4.10.2 | 0.257 | FOTA client shall establish communication with TC client.… |
| 2 | `4907400` | 4.6 | 0.256 | If an attempt to establish a connection to a Wi-Fi network has not succeeded within 3 minu… |
| 3 | `4907402` | 4.6.1 | 0.218 | The HU shall establish a Wi-Fi connection with saved Wi-Fi networks for OTA updates… |
| 4 | `4907403` | 4.6.1 | 0.203 | Upon an attempt to download via Wi-Fi and when multiple networks are configured, the HU wi… |
| 5 | `4907850` | 8.1 | 0.193 | When the NAV requests HU for a Wi-Fi connection, HU shall establish a connection when the … |
| 6 | `4907404` | 4.6.1 | 0.174 | When selecting a Wi-Fi network for a connection attempt, the HU shall exclude network(s) t… |
| 7 | `4907460` | 4.7.3 | 0.171 | The OTA client SHOULD support configurable network priorities in order to limit data costs… ⬅ **§3.3 所指之 `4907460`** |
| 8 | `4907450` | 4.7.3 | 0.169 | OTA client SHALL support the ability to switch the target OTA server URL and port number v… |
| 9 | `4907504` | 4.8.1 | 0.142 | OTA client shall NOT initiate communication to any unauthorized server.… |
| 10 | `4907684` | 4.12.1 | 0.141 | 2. External network interrupt: The OTA Client cannot know when the cause of the interrupt … |
| 11 | `4907689` | 4.12.2 | 0.138 | In the event that the cause of the interrupt and resume of service are not known to the OT… |
| 12 | `4907668` | 4.12 | 0.134 | 2. Network loss: Network error or no data coverage, No Wi-Fi connection, Phone tether is d… |
| 13 | `4907411` | 4.6.1 | 0.130 | For networks in the selected category, the HU shall give priority to network(s) for which … |
| 14 | `4907707` | 4.13.1 | 0.128 | OTA client shall support hand off ECU components to appropriate ECU installers for individ… |
| 15 | `4907355` | 4.5.1 | 0.123 | The OTA client is RECOMMENDED to use the open communication protocols defined in Table 4-3… |
| 16 | `4907412` | 4.6.1 | 0.121 | If all networks in the selected category have a calculated “effective download rate”, the … |
| 17 | `4907314` | 4.4.1 | 0.119 | It is RECOMMENDED that the OTA client implement the open OMA-DM protocol specification [OM… |
| 18 | `4907832` | 7.1 | 0.117 | During Requirement ID 4907831, the HU shall only check for saved and available Wi-Fi netwo… |
| 19 | `4907830` | 7.1 | 0.117 | During Requirement ID 4907829, the HU shall only check for saved and available Wi-Fi netwo… |
| 20 | `4907449` | 4.7.3 | 0.116 | The OTA client shall follow commands received from the OTA server on how to manage each up… |

**`4907460` 排名第 7**（分 0.171）。

---

## 附錄 B —— `SWE1-FOTA-128` 及其後 8 列

### `SWE1-FOTA-128` — Parse Download Descriptor XML and Extract Deployment Parameters｜Categorization：Functional Requirement

> The SWMC shall parse the Download Descriptor provided with the update. The SWMC shall process the Download Descriptor as an XML file. The SWMC shall extract deployment package parameters and metadata from the Download Descriptor. The SWMC shall use the extracted parameters and metadata from below mentioned parameters to control from below and execute the OTA update workflow. installParam --> Installation parameter associated with the download package; contains embedded XML with `<installerType>` tag and comma-separated installer types wrapped inside `<![CDATA[]]>`. DDVersion --> Defines the version of the Download Descriptor. description --> Short textual description of the package in format: `<Name>,<Version>,<Filename>;...;Settings`. objectURI --> URL used to download the package. size --> Size of the download package in bytes. type --> MIME media type of the download package. vendor --> Information about the organization providing the package. installNotifyURI --> URL used to send installation success/failure status reports. infoURL --> URL containing additional information about the package. message --> Multi-language consumer message describing package changes and affected vehicle modules; displayed based on HU language, default language is English (US).


### `SWE1-FOTA-129` — User Experience (UX)/HMI｜Categorization：Heading

> User Experience (UX)/HMI


### `SWE1-FOTA-130` — Support NAFTA Region Languages for SW Update HMI｜Categorization：Functional Requirement

> The MCPU platform software shall provide localization support for the three languages required for the NAFTA region. The supported languages shall include English, North American French, and North American Spanish. The HMI shall display update-related text and messages using the language currently configured in language settings.


### `SWE1-FOTA-131` — Support Server-Configured Update Types With Consistent User Experience｜Categorization：Functional Requirement

> The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The supported update types shall include regular, critical, and silent updates. The WiFi Update Service shall apply the update flow behavior according to the received update type configuration. The SW Update HMI shall provide a consistent user interaction flow across supported update types while applying update-type-specific notifications, restrictions, and interaction behavior. The WiFi Update Service shall control the applicable update flow according to the server-defined update type configuration.


### `SWE1-FOTA-132` — Enforce Terms and Conditions Acceptance Before Download｜Categorization：Functional Requirement

> The SWMC shall determine whether terms and conditions acceptance is required based on the Download Descriptor metadata. Before initiating the update download, the SWMC shall check the customer acceptance status from the FCA IT customer preference database. If the customer has not accepted the required terms and conditions, the SWMC shall provide SW Update HMI guidance describing how the customer can complete the acceptance process. The SWMC shall block update download initiation until terms and conditions acceptance is confirmed.


### `SWE1-FOTA-133` — Display Release Notes and Interactive Links from DD｜Categorization：Functional Requirement

> The SWMC shall parse the Download Descriptor after completion of the update download and extract consumer-approved release notes information, update-related information, and associated links. The SWMC shall provide the extracted release notes information and associated links to the SW Update HMI. The SW Update HMI shall display the release notes information, update-related information, and associated links during the opt-in and download screens. The SW Update HMI shall support user interaction with embedded links displayed as part of the update information.


### `SWE1-FOTA-134` — Display Post-Download Installation Options｜Categorization：Functional Requirement

> The SWMC shall detect completion of the deployment package download. After completion of the download, the SWMC shall provide deployment package details to the SW Update HMI through WiFi Update Service. The SW Update HMI shall display the deployment package details to the user . The SW Update HMI shall provide opt-in options including “Install” and “Schedule Later”.


### `SWE1-FOTA-135` — Deployments of the OTA client｜Categorization：Information

> Deployments (firmware updates, or software installation, updates, and removal) may be triggered as an immediate continuation of the download or by a manual launch of the OTA client application (provided that a full deployment package has already been downloaded)


### `SWE1-FOTA-136` — Control Deployment Rejection Based on OTA Flags｜Categorization：Functional Requirement

> The SWMC shall retrieve the Critical Update and Silent Install configuration flags from the OTA server deployment metadata. The SWMC shall determine whether end-user rejection of the OTA deployment is permitted based on the received Critical Update and Silent Install flag . The SW Update HMI shall allow or restrict user rejection options according to the deployment interaction policy received from the SWMC via WiFi Update Service.


