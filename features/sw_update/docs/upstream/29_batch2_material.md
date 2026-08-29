# 上繳包 29 —— T45 執行結果（下放包 32）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`docs/handoff/32_batch2_probe.md`（沿用下放包 31 之上繳檔名）
- **下放包 32 之落檔驗證：無不符**（見 §0）
- **T45b 有一項範圍限制須裁**（見 §3）

---

## 0. 落檔驗證 —— 下放包 32 無不符

| 主張 | 實測 | |
|---|---|:--:|
| §1.1 之 105 數字 | 照抄執行層實測，逐項相符 | ✅ |
| §1.2 裁 13 列 + 獨立觀測 2 | GT-A1 11 列（`313`／`315`–`324`）+ GT-B 2 列（`328`／`329`）= 13；獨立觀測第 13、14 組 = 2 | ✅ |
| §2.1 `315`–`320` 之 105 = **4／6**（`315`／`316`／`318`／`319`） | 分類器實測**完全相符**，`317`／`320` 不屬 | ✅ |
| §2.1 GT-A1 已裁六列全部，錨逐位對應 | `315`→`4907667` … `320`→`4907672`，**六列六錨一一對應** | ✅ |
| §2.1「R-SU16 之首例區塊」 | 上繳包 10 §3.3 記 #8 為「**已驗之** #8」（§3.2 為其獨立驗證） | ✅ |
| §2.2 `Update HMI` 105 = 0、Layer 3 TBD | T39c 實測 0；`framework.md` Layer 3 表列其於「其餘 11 組 TBD」 | ✅ |
| R-SU37(e)「現為 `313`／`327`」 | 上繳包 09 §T23a 實測「全母體之統攝型需求僅 `313`、`327` 二列」 | ✅ |
| R-SU37 之 `313` 錨集 = 六列錨之聯集 | `313` 之 Description 二句各列同一組六 id，unique 6，與 `315`–`320` 之錨全等 | ✅ |

> **附帶佐證**：`327` 之自證錨為 `4907683`／`4907684`，
> 而 GT-B 記 `328`→`4907683`、`329`→`4907684` ——
> **`327` 與其所統攝二列之關係，與 `313`／`315`–`320` 同構**。
> R-SU37 之餘量判準對 `327` **同樣適用**，(e) 之射程成立。

---

## 1. T45f —— 抄錄與索引

| 條文 | 來源 | 逐字相符 |
|---|---|:--:|
| `R-SU33 v3（觀測窗法 —— (c) 之起訖點再分二級）` | 31 §三（**原 T44e 未執行，本輪補**） | **True** |
| `R-SU34 v3（跨 req_id 之偽通過 —— 粒度、交集與人裁判準）` | 31 §三（同上） | **True** |
| `R-SU37（統攝型需求之驗證點 —— 餘量判準）` | 32 §三 | **True** |

| 項 | T45f 之預期 | 實測 | |
|---|---:|---:|:--:|
| 現行 | **37** | **37** | ✅ |
| 留存 | **23** | **23** | ✅ |

`R-SU1` – `R-SU37` 無缺號無重複。PLAYBOOK 追加 **(33)**（前提寫死在檢查裡）
與 **(34)**（兩端都失敗時問題在定義），二則出自下放包 31 T44e。

---

## 2. T45c —— `003` 之改寫

**pilot 升 `pilot05`**（`pilot01`–`04` 不覆寫）。

| 欄 | 前 | **後** |
|---|---|---|
| proc 2 | `Record … continuously **from the start of the session**` | `Record … **as continuous video capture from the availability check**` |
| er 2 | `The head unit screen content **from the start of the session** is recorded` | `… **from the availability check** is recorded **as continuous video capture**` |

起點依 **R-SU33 v3(c1)** 判為原理上不可觀測（靜默 session 無外部表徵），
改為可用性查詢。`continuously` 一併明文化之理由已記入腳本沿革。

**lint：`pilot05` U=3 不變** ✅（其三個 `PENDING` 為 DR-SU1，未受影響）。

---

## 3. T45b —— `I-cross` 併入 `lint036.py`

### 3.1 併入內容

第 22 項，**profile 專屬**（`PROFILE_CHECKS`）—— 未指定 `--profile` 時
既有八本之報告基線完全不動。輸出 `I-cross=n`。
粒度標「每列每配對（一組命中記二列）」，狀態標
**「警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL」**。

比對範圍加二項限定：**同 `req_id` 者跳過**（由 `I-sibling` 管）、
**跨 Test Set 者不比**（R-SU34 v2(b) 之「同一 Test Set 內」）。

`IX_NORMALISE` 之來源裁定與「改裁須同步改」之警語**已寫入該區塊之檔內註解**
（R-SU34 v3(b) 之明令、PLAYBOOK (33)）。

### 3.2 ⚠ 回測 —— **逐簿執行時無法與獨立腳本相同**，須裁

T45b 令「以現有 10 TC 回測須與獨立腳本逐項相同，**不同即停並回報**」。
**逐簿執行時不同**，成因如下：

| 執行環境 | `I-cross` | 配對數 | 對照 |
|---|---:|---:|---|
| `sandbox/pilot05`（5 TC） | **2** | 1 | TC-1 vs TC-2 |
| `sandbox/batch01`（5 TC） | **4** | 2 | TC-6 vs TC-8、TC-7 vs TC-8 |
| **合計（逐簿）** | 6 | **3** | **少 2 組** |
| **獨立腳本**（10 TC 為一集合） | — | **5** | 另含 TC-1 vs TC-8、TC-2 vs TC-8 |

**少的二組皆跨簿** —— pilot 與 batch 1 分屬二本工作簿，
而 `lint036.py` **逐簿執行**。

**這與 `I-sibling` 之範圍問題是同一件事**（上繳包 25 §2.3）：
併入 lint 補上了「跨 req_id」這一維，**但沒有補上「跨簿」那一維**。

### 3.3 等價環境下之回測 —— **逐項相同** ✅

以併簿探針（`scripts/probe_sibling_9.py`，10 列同簿，落 `sandbox/probe_all10/`）
建立與獨立腳本等價之執行環境：

```
python3 scripts/lint036.py <probe_all10 之簿> --profile sw_update
  行計 … I-sibling=0 … U=11  V=0  I-cross=10        exit 0
```

`I-cross=10`（行計）= **5 組配對**（一組記二列），與獨立腳本**逐項相同**：

| # | 配對 | 共同窗 | 違例類交集 |
|---:|---|---|---|
| 1 | `SU-001` vs `SU-002` | availability-check → version-change | `progress-notification` |
| 2 | `SU-001` vs `SU-008` | 同上 | `progress-notification`／`prompt` |
| 3 | `SU-002` vs `SU-008` | 同上 | `progress-notification` |
| 4 | `SU-006` vs `SU-008` | 同上 | `confirmation-screen` |
| 5 | `SU-007` vs `SU-008` | 同上 | `confirmation-screen` |

**`TC-6` vs `TC-7` 未命中** ✅（上下位判定：二子類彼此不相交）。

### 3.4 待裁

**交付簿為一本**（寫回 036 母本），故**交付時本限制不存在** ——
屆時 10 個 TC 在同一本，逐簿執行即等於全集執行。

**惟開發期之 sandbox 分簿**（pilot／batch01／batch2a…）**會持續分裂比對範圍**，
且**分得越細，漏得越多** —— batch 2a 起草時，其 6 列與既有 10 列之配對
在逐簿執行下**一組都比不到**。

二個處置方向（**執行層不逕定**）：

- **(甲)** 每批起草後跑一次併簿探針（現行作法，人工記得），或
- **(乙)** `lint036.py` 增一個「多簿合併比對」模式，
  使 `I-cross` 之範圍與交付簿一致。

**在其一落地前，跨簿之偽通過無機器覆蓋** —— 依 R-SU34 v1(d) 逐包揭露。

---

## 4. T45d —— batch 2a 材料（`315`–`320` 六列）

- 機制 3 之門檻（R-SU23(b)，`≤` 為攔下）：首選分 **≤ 0.267**
- **執行層不撰寫 TC、不裁定錨**；GT-A1 已裁之錨照抄，候選錯誤碼為**候選非裁定**

| # | 037 列 | 標題 | Sub Cat | **105？** | **GT-A1 錨** | 首選分 | 機制 3 |
|---:|---|---|---|:--:|---|---:|:--:|
| 1 | `SWE1-FOTA-315` | Socket Read/Write Error Handling | Service | **⚠** | `4907667` | 0.481 | — |
| 2 | `SWE1-FOTA-316` | Network Loss Handling | Service | **⚠** | `4907668` | 0.586 | — |
| 3 | `SWE1-FOTA-317` | User-Initiated Network Deactivatio | Service | — | `4907669` | 0.346 | — |
| 4 | `SWE1-FOTA-318` | Emergency State Handling | Service | **⚠** | `4907670` | 0.575 | — |
| 5 | `SWE1-FOTA-319` | Power Loss Handling | Service | **⚠** | `4907671` | 0.174 | **⚠ 攔下** |
| 6 | `SWE1-FOTA-320` | Host System Disconnection Handling | Service | — | `4907672` | 0.174 | **⚠ 攔下** |

- **105 列：4 / 6** —— `315`、`316`、`318`、`319`；不屬者 `317`、`320`
- **GT-A1 已裁 6 / 6**，其錨 `4907667`–`4907672` **逐位對應**；該六 id 亦即 `313` 自證錨之全集（R-SU37(a)）

---

### 逐列材料


---

#### 1. `SWE1-FOTA-315` — Socket Read/Write Error Handling

- 分類：**105 列**（內部列且 VC 亦無外部面）｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-190`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907667` —— Socket 讀寫錯誤

**Requirement Description 全文**：

> The SWMC shall detect and handle socket read/write errors during OTA server communication, flashing, or software component update, and shall report the error status to WiFiUpdateService.

**`Verification Criteria` 全文**：

> Trigger a socket read or write error during OTA communication.
>
> Verify that the socket error is detected and handled appropriately.
>
> Confirm that the error status is reported after the error is detected.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907667` — 章 **4.12** Interrupt Handling — 分 **0.481** ✅ **= GT-A1 之正解**
   > 1. Socket read/write error

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.189**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.168**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.

4. `4907524` — 章 **4.9.1** Update Agent Requirements — 分 **0.152**
   > Update Agent component shall be able to handle both file system and binary image updates.

5. `4907765` — 章 **4.13.4.2** Appendix B Configurable Parameters — 分 **0.143**
   > The OTA Client MAY support the following configurable parameters in its flows; The OTA client MAY support modification of these parameters via the OTA server. If a proprietary protocol is used these values SHALL still be server configurable. Table B-1: DM Tree Interval Descriptions Interval Description Default Value RecoveryPollingInterval Amount of time, in minutes, after an unsuccessful poll. If…

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `262145` | Redbend result file read/write error *Not support at | `Install ( M-CPU )` | `error`／`read`／`write` |
| `458763` | Not an actual error | `Install ( SXM )` | `error`／`update` |
| `458762` | Common SXM installation error | `Install ( SXM )` | `error`／`update` |
| `458761` | Common SXM installation error | `Install ( SXM )` | `error`／`update` |
| `458760` | Not an actual error | `Install ( SXM )` | `error`／`update` |


---

#### 2. `SWE1-FOTA-316` — Network Loss Handling

- 分類：**105 列**（內部列且 VC 亦無外部面）｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-191`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907668` —— 網路遺失之五種情形

**Requirement Description 全文**：

> The SWMC shall detect network loss conditions, including network errors, no data coverage, loss of Wi-Fi connection, phone tether disconnection, and embedded modem roaming, during OTA server communication, flashing, or software component update, and shall report the network loss status to WiFiUpdateService.

**`Verification Criteria` 全文**：

> Simulate a network loss during OTA communication or software update.
>
> Verify that the network loss condition is detected and handled appropriately.
>
> Confirm that the network loss status is reported.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907668` — 章 **4.12** Interrupt Handling — 分 **0.586** ✅ **= GT-A1 之正解**
   > 2. Network loss: Network error or no data coverage, No Wi-Fi connection, Phone tether is disconnected, Embedded modem moves to roaming network

2. `4907671` — 章 **4.12** Interrupt Handling — 分 **0.196**
   > 5. Loss of power(battery disconnect)

3. `4907825` — 章 **7.1** Critical Updates — 分 **0.195**
   > If there is no Wi-Fi network saved or HU is not able to download the package then download shall happen via embedded modem or TBM

4. `4907822` — 章 **7** Firmware Over-the-air Updates (FOTA) — 分 **0.175**
   > If HU is not able to connect to a Wi-Fi network or unable to download the package for 7 days, then download shall happen via embedded modem

5. `4907526` — 章 **4.9.1** Update Agent Requirements — 分 **0.142**
   > Update Agent shall have a recovery mechanism in the event of a power failure, communications loss, or other event which interrupts the update.

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `393217` | Report HU is in bricked state - two or more VCPU upd | `After HU start-up, suddenl` | `report`／`update` |
| `393216` | Report PBL mode enter | `After HU start-up, suddenl` | `report`／`update` |
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | `software`／`update` |
| `196634` | Update data incompatible | `Install ( M-CPU )` | `data`／`update` |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend )` | `software`／`update` |


---

#### 3. `SWE1-FOTA-317` — User-Initiated Network Deactivation Handling

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-192`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907669` —— 使用者關閉行動數據／Wi-Fi

**Requirement Description 全文**：

> The WiFiUpdateService shall handle user-initiated deactivation of mobile data usage or an active Wi-Fi connection reported by SWMC during OTA server communication, flashing, or software component update.

**`Verification Criteria` 全文**：

> Disable mobile data or disconnect the active Wi-Fi connection during an OTA operation.
>
> Verify that the network deactivation is handled appropriately.
>
> Confirm that the OTA operation responds according to the network deactivation condition.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907669` — 章 **4.12** Interrupt Handling — 分 **0.346** ✅ **= GT-A1 之正解**
   > 3. The end-user deactivates data usage or active Wi-Fi connection

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.190**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907567` — 章 **4.10.2** Server-Initiated Session Flow — 分 **0.187**
   > Server initiated session - Communication between FOTA Client &amp; TC

4. `4907559` — 章 **4.10.1** Self Registration Flow — 分 **0.179**
   > 1. The OTA client runs the server-initiated session, client-initiated session or user-initiated session.

5. `4907301` — 章 **4.4** OTA Client Architecture — 分 **0.164**
   > Data connection &amp; Socket interface. This component is the same as for the Vehicle Manager. It provides the connectivity to the server.

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | `software`／`update` |
| `196634` | Update data incompatible | `Install ( M-CPU )` | `data`／`update` |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend )` | `software`／`update` |
| `-` | Cannot update software. Software not compatible with | `Precondition` | `software`／`update` |
| `65555` | VCPU update binary is missed in the package | `Package Header check & unp` | `update` |


---

#### 4. `SWE1-FOTA-318` — Emergency State Handling

- 分類：**105 列**（內部列且 VC 亦無外部面）｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-193`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907670` —— 車輛處於緊急狀態

**Requirement Description 全文**：

> The WiFiUpdateService shall handle the vehicle emergency state (accident detection) notified by the appropriate system component during OTA server communication, flashing, or software component update.

**`Verification Criteria` 全文**：

> Simulate a vehicle emergency state during an OTA operation.
>
> Verify that the emergency state is detected and handled appropriately.
>
> Confirm that the OTA operation responds according to the emergency condition.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907670` — 章 **4.12** Interrupt Handling — 分 **0.575** ✅ **= GT-A1 之正解**
   > 4. The vehicle is in an emergency state(accident detection)

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.220**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907524` — 章 **4.9.1** Update Agent Requirements — 分 **0.198**
   > Update Agent component shall be able to handle both file system and binary image updates.

4. `4907368` — 章 **4.5.3** Vehicle initiated sessions — 分 **0.178**
   > Detection of ECU configuration changes, such as detection of manual diagnostic reflash or component replacement by service technician SHALL trigger a vehicle initiated session. This trigger shall be handled with the same event based interface into the OTA client.01

5. `4907642` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.160**
   > Emergency Call shall be functional at all times during the download and post installation process.

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `-` | Cannot update software. Software not compatible with | `Precondition` | `software`／`update`／`vehicle` |
| `393217` | Report HU is in bricked state - two or more VCPU upd | `After HU start-up, suddenl` | `state`／`update` |
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | `software`／`update` |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend )` | `software`／`update` |
| `65555` | VCPU update binary is missed in the package | `Package Header check & unp` | `update` |


---

#### 5. `SWE1-FOTA-319` — Power Loss Handling

- 分類：**105 列**（內部列且 VC 亦無外部面）｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-194`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907671` —— 電源遺失 —— **正解不在前 20**（D-1 缺字）

**Requirement Description 全文**：

> The WiFiUpdateService shall coordinate the handling of condition during OTA server communication, flashing, or software component update by interacting with SWMC and the appropriate installer component.

**`Verification Criteria` 全文**：

> Simulate a power loss during an OTA operation.
>
> Verify that the power loss condition is handled appropriately.
>
> Confirm that the OTA operation responds according to the power loss condition.
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907380` — 章 **4.5.4.1** SMS/MQTT Push Support — 分 **0.174**
   > Communication and update implementation to individual components shall be the responsibility of the implementation of the abstracted installer of the relevant component type. Some examples would be the application installer providing an application to the host OS's application manager or an ECU update installer managing the serial communication with HU daughter board required for re-flash.

2. `4907707` — 章 **4.13.1** SCOMO Support — 分 **0.173**
   > OTA client shall support hand off ECU components to appropriate ECU installers for individual bus communication. 4. Map Update Data(MOTA): The OTA client shall be able to install map updates, which the OTA server provides in a deployment package format. The OTA client shall support hand off to a Map management installer

3. `4907361` — 章 **4.5.2** User initiated sessions — 分 **0.168**
   > OTA client SHALL define event handling interface for communication with HMI and be able to respond to user input for support of these requirements.

4. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.166**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

5. `4907590` — 章 **4.10.3** Vehicle-Initiated Session Flow — 分 **0.155**
   > 8. After installation pre-condition check the OTA client shall parse the deployment package and invoke installers (see Deployment Flow) and update agents for the component types in the deployment package, to deploy the software updates.

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | `software`／`update` |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend )` | `software`／`update` |
| `-` | Cannot update software. Software not compatible with | `Precondition` | `software`／`update` |
| `65555` | VCPU update binary is missed in the package | `Package Header check & unp` | `update` |
| `65554` | MCPU update binary is missed in the package | `Package Header check & unp` | `update` |


---

#### 6. `SWE1-FOTA-320` — Host System Disconnection Handling

- 分類：非內部列｜Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-195`
- `Verification Method`：`Unit Test / Integration Test / System Test`
- **GT-A1 已裁之錨**：`CFTS057-4907672` —— 主機實體斷開 —— 正解排第 14

**Requirement Description 全文**：

> The WiFiUpdateService shall detect end-user physical disconnection of the host system (HU/TBM) during OTA server communication, flashing, or software component update and notify SWMC. The SWMC shall handle the OTA session based on the notification and report the update status to the WiFiUpdateService.

**`Verification Criteria` 全文**：

> Simulate a physical disconnection of the host system during an OTA operation.
>
> Verify that the disconnection is detected and handled appropriately.
>
> Confirm that the update status is reported after the disconnection is handled
>

**路徑 A（語料 v2）前 5 候選**：

1. `4907279` — 章 **4.2.3** HU FOTA with TBM — 分 **0.174**
   > When TBM receives a notification from the server that an update is available, the TBM shall send $HUReflash$ = [Update Available] to the HU.

2. `4907665` — 章 **4.12** Interrupt Handling — 分 **0.161**
   > There are several kinds of interrupts that can be handled while an OTA client is connected to the OTA server and while flashing or updating a software component. This section describes how to handle interrupts and how the client should interact with the OTA server when interrupts are resolved.

3. `4907802` — 章 **6** TBM Algorithm Requirements — 分 **0.154**
   > When TBM has completed the download of a FOTA update with notification package, then the TBM shall send $TBMUpdate$ = [Update_Available]

4. `4907811` — 章 **6** TBM Algorithm Requirements — 分 **0.151**
   > During any Ignition conditions, When an update installation has been successfully completed, then the TBM shall send $TBMUpdate$ = [Update_End] for &lt;T_FOTA_END&gt;

5. `4907606` — 章 **4.10.5** Deployment Flow — 分 **0.147**
   > 5. The installers then notify the OTA client of their update status, in the event of a failure they also provide individual ECU DP status codes.

**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，非階段名字面 —— R-SU20(d)）**：

| 碼 | Description | 階段 | 共同詞 |
|---|---|---|---|
| `393217` | Report HU is in bricked state - two or more VCPU upd | `After HU start-up, suddenl` | `report`／`update` |
| `393216` | Report PBL mode enter | `After HU start-up, suddenl` | `report`／`update` |
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | `software`／`update` |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend )` | `software`／`update` |
| `-` | Cannot update software. Software not compatible with | `Precondition` | `software`／`update` |


### 4.1 三項須記之觀察（材料之外）

1. **`319`／`320` 之首選分皆 0.174，二者皆被機制 3 攔下**（門檻 ≤ 0.267）。
   `319` 之成因 GT-A1 已記為 **D-1 之缺字**（`SWE1-FOTA-319` 即 D-1 本身，
   其正解不在前 20）；`320` 之正解 GT 記為**排第 14**。
   **本二列之錨不靠路徑 A 而靠 GT-A1／區塊錨** —— 起草時勿以首選為錨。

2. **六列全為 `Service`，`Sub Cat` 無一為 HMI** ——
   與 `framework.md` 第 16 組之 HMI 0／Service 19 一致。

3. **候選錯誤碼之產出極不均勻**：`315`（socket／network 詞彙）與 `316`
   有具體候選，而 `318`（Emergency State）多半落空 ——
   **碼側用 `abort`／`suspend` 描述同一件事，需求側用 `emergency`**。
   此即檔首所記之詞彙法之漏，**「無候選」不等於「無對應碼」**。

---

## 5. T45e —— `Update HMI` 六列之材料索引（不重新傾印）

材料在 **`docs/upstream/25a_parallel_material.md`**：

| 區間 | 內容 |
|---|---|
| **行 859** | `## 節 —— \`Update HMI\`（6 列）` 起 |
| 行 861–872 | 六列總表（Sub Cat／Priority／105？／首選分／機制 3） |
| 行 877–916 | 1. `SWE1-FOTA-130` Support NAFTA Region Languages for SW Update HMI |
| 行 917–956 | 2. `SWE1-FOTA-131` Support Server-Configured Update Types With Consistent User Experience |
| 行 957–996 | 3. `SWE1-FOTA-132` Enforce Terms and Conditions Acceptance Before Download |
| 行 997–1036 | 4. `SWE1-FOTA-133` Display Release Notes and Interactive Links from DD |
| 行 1037–1076 | 5. `SWE1-FOTA-134` Display Post-Download Installation Options |
| 行 1077–1113 | 6. `SWE1-FOTA-136` Control Deployment Rejection Based on OTA Flags |

**105 列：0**｜Layer 3：**TBD**（21 組中 11 個 TBD 之一）｜HMI 5／Service 1。

---

## 6. T45a —— DR 文本更新

`docs/upstream_requests/DR-SU1_SU2_request.md`：

- §3.4 之表增 `SWE1-FOTA-184` 一列，**其成因句以上游讀得懂的話寫** ——
  「三階段在台架上沒有可觀測之界線；靜默更新畫面什麼都不顯示，
  故沒有東西標示 check 何時結束、download 何時開始」，
  並列明其三類違例已分別由 `175`／`180`／`182` 之 TC 覆蓋。
- §3.4 前言由 "Two requirements" 改 "Three requirements"，
  並補「或**無法量測之限定詞**」一類（`181` 屬之，非「不可區辨」）。
- §6 摘要表之 DR-SU2 (c) 由「2 test cases, 5 placeholders」
  改 **「3 test cases, 8 placeholders」**。
- 檔首增 **Revision** 行記本次修訂。

**發送者為 Pei，執行層只落檔，未發送。**

---

## 7. T45g —— git

本輪之前已 commit 二次（stage 區積二輪）：

| commit | 內容 |
|---|---|
| `965b44f` | `feat(sw_update): execute T43 …` —— 13 檔，+1078/−50 |
| `eae176c` | `docs(sw_update): land handoffs 31 and 32` —— 2 檔，+389 |

本輪 T45 之產出另行 commit（訊息見交付時）。
`sandbox/` 與 `inputs/` 依例不進版控。

---

## 8. 未結 DR 清單（**2 筆**）

| DR | 標的 | 進度 |
|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | `newR1L-SU-003` 三個 `PENDING` |
| **DR-SU2 v2** | (a) 顯示途徑／(b) Wi-Fi 正向狀態／(c) **第三型之區辨手段（`179`／`181`／`184`）** | 第二型 **5 / 106**；**第三型 3 列，母群未知** |

`PENDING` 總計 **11 行**。DR 文本已同步（§6）。

---

## 9. 獨立自評 —— §五-6 所問：就 `313` 實際回答 R-SU37(c) 之判別問句

**問**：若 `315`–`320` 六列各自都通過，還有什麼情形能使 `313` 失敗？

**答：我找到一個，但它撐不住 —— 結論是餘量為空，適用 R-SU37(b)。**

**(甲) 我找到的那個情形。** `313` 之餘量為
`coordinate the handling …` 與 `by interacting with SWMC and the
appropriate installer component`。**協調之可觀測失敗形態，其最強候選為
「多個中斷條件同時或接連發生時，處理錯亂」** ——
如：下載中先失去網路（`316`）、恢復後隨即斷電（`319`），
二者各自單獨測皆通過，而併發時系統重複下載、或狀態機卡在中間態。

**這是一個具體情形，且它不是任一單列之驗證點。**

**(乙) 但它撐不住，理由有二，且第二個是決定性的。**

**其一，它不在 `313` 之 Description 裡。** `313` 說的是「協調六個條件之處理」，
**沒有說「併發時仍正確」**。併發情形是我從「協調」一詞**推想**出來的 ——
**推想不是需求**（IN §8.4.1）。若據此寫 TC，其驗的是一個沒人寫過的需求。

**其二，併發之情形另有其列。** `framework.md` 第 16 組之能力叢集載明
「六種中斷、復原、儲存、**併發**」—— 併發屬本組**其他列**
（`321`–`329` 之範圍，本輪未讀畢）。若併發已有專屬列，
則該情形是**那一列**的驗證點，不是 `313` 的。

**(丙) 故答案是：答不出一個「屬於 `313` 且有需求支持」的具體情形。**

`313` 之 Description 二句所述，逐句拆開後為：
- 「WiFiUpdateService 應協調 4907667–4907672 六個錯誤條件之處理」
  → 該六條件之處理即 `315`–`320` 各列；
- 「SWMC 應處理該六條件並向 WiFiUpdateService 回報狀態」
  → **回報**之部分，其對象為服務間訊息（R-SU25 之不可觀測面），
  且 `358` Update Status Reporting to SWMC 為其專屬列。

**兩句拆完，沒有剩下任何有外部表徵且無他列承擔者。餘量為空。**

**(丁) 故 `313` 適用 R-SU37(b)：不產出獨立 TC，其驗證併入所統攝六列 ——
惟併入須上游確認**（同 R-SU32(d)），分析層與執行層皆不得逕併。

**(戊) 一項須一併提出者**：若上游確認可併，則 **`313` 這一列沒有自己的 TC**，
而 SWE.6 之追溯性要求每一需求列有其 TC。
**其解不是替它寫一個 TC，而是在追溯矩陣中記其併入之去向** ——
此為交付面之處置，**現行流程未定義該記法**。建議與 DR 一併問，或立為新條。

**(己) 對 R-SU37 之一點回饋**：(c) 之判別問句很有效，
**但它會把「我想得到的失敗情形」誤認為「需求所要求的驗證點」** ——
本次我第一輪就想出了併發，若不追問其需求依據，就會據以寫出一個
**驗一個沒人寫過的需求**之 TC。建議 (c) 增一句：
**「該情形須在統攝列自身之 Description 中有文字依據，
推想出來的失敗情形不算。」**
