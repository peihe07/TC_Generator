# 上繳包 24 —— batch 1 材料重列、`C`／`E` 陳報、難類涵蓋盤點

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/25_batch1_relist.md`
  （SHA256 `fd7032f17a9a75d3d09ff68812e1078319e489203668c3488d28f586840a0825`，143 行）
- **未結 DR：2 筆**（DR-SU1；DR-SU2 確認進度 **5/105**）
- 新腳本：`scripts/ce_columns.py`；`scripts/batch1_material.py` 增 T38b

## 本輪四個主結果

1. **`C` 欄之鏈路在 `vehicle_category` **126/126 全數成立**，
   而**在本 feature 完全不存在** —— sw_update 之 037 為 18 欄舊版面、
   **無 `HMI Source ID` 欄**，且其 `Source Requirement ID`
   與 SYS1 之三個識別碼欄**交集皆為 0**。**無可用之取值路徑。** §3.1。
2. **難類涵蓋表：105 列佔比 ≥60% 者 5 組**，最高為
   `Telematics Client`（80%）、`Interruption Handling`（74%）；
   **0% 者僅 2 組**（`ROV Installation` 20 列、`Update HMI` 6 列）。
3. **⚠ 發現一處台帳不一致**：DR-SU2 之已確認段 5 列中，
   **`SWE1-FOTA-365` 不在其未確認母群 105 列之內** ——
   成因為上繳包 19 §7.1(甲) 已指認之 `notification` 語形偽陰性。§7.1。
4. **`E` 欄於 15 本簿之 2167 列中填值數為 0**；`C`／`E` 於母本
   **無 DV、無 x14 DV、無條件式格式**（全簿條件式格式計數為 0）。

---

## 1. T38d —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU31 | 631 | **OK** | `0478462c4ec3` |

逐字 append，**既有 47 個條文區塊未受影響** ✅（現 48 塊）。
索引表現行 **31 條**（新增 R-SU31）；留存 **17 條**（無變動）。
與下放包 25 §五 T38d 所定之「31 條現行」一致。

`PLAYBOOK.md` §7 追加 **(25)**「一批樣本『全部通過』之意義取決於它涵蓋了哪些類」，
並指出其與取樣偏誤之別：**取樣偏誤是分佈歪了（看得出來），
本條是某一整類完全沒被抽到（沒有數字，而沉默看起來像沒問題）**。
判準為**「問這批**沒有**包含什麼」**。

---

## 2. T38b —— batch 1 材料重列（本輪核心）

- Test Set：**`Silent Update`**｜Layer 3 provisional：`4.7.3.2`
- 其 `Verification Criteria` **已於上繳包 23 §2 備妥，本節不再列**
- 機制 3 之門檻（R-SU23(b) 改 `≤`）：首選分 **≤ 0.267**

> **執行層不撰寫 TC、不裁定錨。**

| # | 037 列 | 標題 | Sub Cat | **105 列？** | 首選分 | 機制 3 |
|---:|---|---|---|:--:|---:|:--:|
| 1 | `SWE1-FOTA-179` | Start Silent Update Download Autom | Service | **⚠ 是** | 0.200 | **⚠ 攔下** |
| 2 | `SWE1-FOTA-180` | Optionally Suppress Download Confi | Service | — | 0.386 | — |
| 3 | `SWE1-FOTA-181` | Start Silent Update Installation I | Service | — | 0.317 | — |
| 4 | `SWE1-FOTA-182` | Optionally Suppress Deployment Con | Service | — | 0.376 | — |
| 5 | `SWE1-FOTA-184` | Apply Silent Update to All Session | Service | — | 0.311 | — |

---

### 逐列材料


---

#### 1. `SWE1-FOTA-179` — Start Silent Update Download Automatically

- 分類：**105 列** —— 其 TC 將撞上 R-SU29(c)（R-SU31(c)：本 feature 首個進入撰寫之 105 列）
- Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-366`

**Requirement Description 全文**：

> The SWMC shall provide the downloaded Download Descriptor (DD) metadata to the WiFi Update Service after update availability is confirmed. The WiFi Update Service shall analyze the DD metadata to determine whether the update type is classified as Silent Update. If the DD metadata indicates a Silent Update, the WiFi Update Service shall automatically request SWMC to initiate deployment package download.

**路徑 A（語料 v2）前 5 候選**：

1. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.200**
   > 1. The download of the deployment package shall start automatically.

2. `4907487` — 章 **4.7.3.2** Silent Updates — 分 **0.200**
   > If the DDF does not include whether the update is silent or not, the HU shall treat the update as a non-silent update

3. `4907806` — 章 **6** TBM Algorithm Requirements — 分 **0.199**
   > When TBM has completed the download of TBM FOTA Silent update package, then the TBM shall send $TBMUpdate$ = [Silent_Update]

4. `4907453` — 章 **4.7.3** Main Update Configuration Options — 分 **0.187**
   > Update type:

5. `4907656` — 章 **4.11** User Experience (UX)/HMI — 分 **0.176**
   > User experience shall be same for all update types and updates (regular/critical/silent) SHOULD be configurable from the server so that the FOTA service administrator can select the relevant option depending on the type and urgency of the update being performed.


---

#### 2. `SWE1-FOTA-180` — Optionally Suppress Download Confirmation Screen

- 分類：非內部列
- Sub Cat：Service｜Priority：Low｜Source：`SYS-RA-FOTA-367`

**Requirement Description 全文**：

> When the update type is identified as Silent Update, the WiFi Update Service shalll not trigger the SW Update HMI to display a download confirmation screen. The WiFi Update Service shall automatically request SWMC to initiate deployment package download without user interaction.

**路徑 A（語料 v2）前 5 候選**：

1. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.386**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

2. `4907482` — 章 **4.7.3.2** Silent Updates — 分 **0.285**
   > The OTA client MAY NOT display a download confirmation screen.

3. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.277**
   > Silent updates run automatically without any progress notifications or end user interaction.

4. `4907484` — 章 **4.7.3.2** Silent Updates — 分 **0.272**
   > The OTA client MAY NOT display a deployment confirmation screen.

5. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.261**
   > 1. The download of the deployment package shall start automatically.


---

#### 3. `SWE1-FOTA-181` — Start Silent Update Installation Immediately After Download

- 分類：**126 內部列**（但 VC 有外部面）
- Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-368`

**Requirement Description 全文**：

> The SWMC shall notify the WiFi Update Service upon successful completion of deployment package download for update packages classified as Silent Update. Upon receiving deployment package download completion status, the WiFi Update Service shall immediately start installation prechecks and deployment.

**路徑 A（語料 v2）前 5 候選**：

1. `4907483` — 章 **4.7.3.2** Silent Updates — 分 **0.317**
   > 2. After the deployment package is downloaded, its deployment shall start immediately.

2. `4907481` — 章 **4.7.3.2** Silent Updates — 分 **0.262**
   > 1. The download of the deployment package shall start automatically.

3. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.201**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

4. `4907515` — 章 **4.8.3** Deployment Package Security — 分 **0.195**
   > The OTA client shall ensure integrity of the deployment package before it is installed, immediately pre installation.

5. `4907514` — 章 **4.8.3** Deployment Package Security — 分 **0.192**
   > The OTA client shall verify integrity of the deployment package once it is received from the server, immediately post download.


---

#### 4. `SWE1-FOTA-182` — Optionally Suppress Deployment Confirmation Screen

- 分類：非內部列
- Sub Cat：Service｜Priority：Low｜Source：`SYS-RA-FOTA-369`

**Requirement Description 全文**：

> The WiFi Update Service shall not trigger the SW Update HMI to display a deployment confirmation screen when the update type is identified as Silent Update. The WiFi Update Service shall automatically initiate deployment of the downloaded package without user interaction.

**路徑 A（語料 v2）前 5 候選**：

1. `4907470` — 章 **4.7.3.1** Critical Updates — 分 **0.376**
   > 1. The download of the deployment package shall start automatically; The OTA client SHALL NOT display a download confirmation screen.

2. `4907471` — 章 **4.7.3.1** Critical Updates — 分 **0.351**
   > 2. When the deployment package is downloaded, the OTA client shall display a deployment confirmation screen. The deployment shall start after a confirmation screen or when a timeout occurs.

3. `4907484` — 章 **4.7.3.2** Silent Updates — 分 **0.322**
   > The OTA client MAY NOT display a deployment confirmation screen.

4. `4907475` — 章 **4.7.3.2** Silent Updates — 分 **0.300**
   > Silent updates run automatically without any progress notifications or end user interaction.

5. `4907482` — 章 **4.7.3.2** Silent Updates — 分 **0.260**
   > The OTA client MAY NOT display a download confirmation screen.


---

#### 5. `SWE1-FOTA-184` — Apply Silent Update to All Session Flows

- 分類：非內部列
- Sub Cat：Service｜Priority：High｜Source：`SYS-RA-FOTA-371`

**Requirement Description 全文**：

> The WiFi Update Service shall apply Silent Update execution rules to all supported update session flows, including update check, deployment package download and installation processing. During Silent Update execution, the WiFi Update Service shall not trigger the SW Update HMI for customer-facing interaction, progress notifications, prompts, or confirmation flows unless required for safety-related conditions.

**路徑 A（語料 v2）前 5 候選**：

1. `4907486` — 章 **4.7.3.2** Silent Updates — 分 **0.311**
   > Silent update shall be applicable for all session flows.

2. `4907455` — 章 **4.7.3** Main Update Configuration Options — 分 **0.281**
   > Silent update: An update that does not display any notifications during the session (there is no end-user interaction)—the end-user cannot reject the update. Network bearer rules for minimizing download cost apply.

3. `4907476` — 章 **4.7.3.2** Silent Updates — 分 **0.245**
   > Silent updates shall not display progress notifications and shall NOT require end-user interaction.

4. `4907618` — 章 **4.10.5.1** Installation and Download Conditions — 分 **0.244**
   > Download of the file shall not be customer facing.

5. `4907477` — 章 **4.7.3.2** Silent Updates — 分 **0.234**
   > During silent sessions the user SHALL NOT be notified unless necessary for safety requirements.


---

## 3. T38a —— `C`／`E` 二欄之陳報

### (i) `vehicle_category` 之 `C` 欄填值來源之追查

`vehicle_category` 之 037：**20 欄 rev D**，其欄 2 為 **`HMI Source ID`**（本 feature 之 037 為 **18 欄舊版面，無該欄**）。

**逐列比對（前 12 列）**：037 之 `HMI Source ID` → SYS1 之 `SYSRE_HMI_Source ID` → SYS1 之 `ID` → 036 之 `C`

| 036 `D`（037 列 id） | 037 `HMI Source ID`（尾） | SYS1 `ID` | 036 `C` | 相符 |
|---|---|---|---|:--:|
| `SWE1-HMI-VC-001-01` | …`r_27_2023)_2.2` | `NRL-171043` | `NRL-171043` | ✅ |
| `SWE1-HMI-VC-001-02` | …`r_27_2023)_2.2` | `NRL-171043` | `NRL-171043` | ✅ |
| `SWE1-HMI-VC-001-03` | …`r_27_2023)_2.2` | `NRL-171043` | `NRL-171043` | ✅ |
| `SWE1-HMI-VC-002` | …`r_27_2023)_2.3` | `NRL-171044` | `NRL-171044` | ✅ |
| `SWE1-HMI-VC-003` | …`27_2023)_2.3.1` | `NRL-171045` | `NRL-171045` | ✅ |
| `SWE1-HMI-VC-004` | …`27_2023)_2.3.2` | `NRL-171046` | `NRL-171046` | ✅ |
| `SWE1-HMI-VC-005` | …`27_2023)_2.3.3` | `NRL-171047` | `NRL-171047` | ✅ |
| `SWE1-HMI-VC-006` | …`27_2023)_2.3.4` | `NRL-171048` | `NRL-171048` | ✅ |
| `SWE1-HMI-VC-007-01` | …`r_27_2023)_2.4` | `NRL-171049` | `NRL-171049` | ✅ |
| `SWE1-HMI-VC-007-02` | …`r_27_2023)_2.4` | `NRL-171049` | `NRL-171049` | ✅ |
| `SWE1-HMI-VC-007-03` | …`r_27_2023)_2.4` | `NRL-171049` | `NRL-171049` | ✅ |
| `SWE1-HMI-VC-007-04` | …`r_27_2023)_2.4` | `NRL-171049` | `NRL-171049` | ✅ |

**全 126 列之比對：相符 126／不符 0** —— **鏈路成立**

即 `C` 之取值路徑為：

```
037 之 `HMI Source ID`  ──match──▶  SYS1 `SYSRE_HMI_Source ID`
                                          │
                                          ▼
                                    SYS1 `ID`（NRL-…）
                                          │
                                          ▼
                                     036 之 `C` 欄
```

**`vehicle_category` 之 037 之 `Sub Categorization` 分佈**：`HMI` 103／`Service` 42

純 Service 列：**42** 列
其中無 `HMI Source ID` 者：**0** 列

### (ii) `E` 欄之標頭原文與已交付簿之填值

- 標頭原文（`E9`）：`Test Case ID (TestRail)
測試用例 ID (TestRail)`

| feature | 簿 | 資料列 | `E` 非空 |
|---|---|---:|---:|
| power | `delivered/pm_29.xlsx…` | 390 | 0 |
| bed_lowering | `output/FM-WI-FSM-03…` | 151 | 0 |
| comfort | `output/FM-WI-FSM-03…` | 466 | 0 |
| display | `output/FM-WI-FSM-03…` | 24 | 0 |
| popup | `output/FM-WI-FSM-03…` | 5 | 0 |
| power_moding | `output/FM-WI-FSM-03…` | 51 | 0 |
| power_moding | `output/FM-WI-FSM-03…` | 51 | 0 |
| power_moding | `output/FM-WI-FSM-03…` | 51 | 0 |
| privacy | `output/FM-WI-FSM-03…` | 11 | 0 |
| sxm | `output/FM-WI-FSM-03…` | 215 | 0 |
| time_management | `output/FM-WI-FSM-03…` | 59 | 0 |
| user_profiles | `output/FM-WI-FSM-03…` | 189 | 0 |
| user_profiles | `output/FM-WI-FSM-03…` | 189 | 0 |
| user_profiles | `output/FM-WI-FSM-03…` | 189 | 0 |
| vehicle_category | `output/FM-WI-FSM-03…` | 126 | 0 |
| **合計** | | **2167** | **0** |

**`E` 欄於全部已交付／產出簿**皆為空**。**

### (iii) `C`／`E` 於 036 母本之 DV 與條件式格式

| 欄 | 標準 DV | x14 DV | 條件式格式 |
|---|---|---|---|
| `C` | **無** | **無** | **無** |
| `E` | **無** | **無** | **無** |

全簿之 `<conditionalFormatting` 計數：**0**（sheet6）

### 3.1 ⚠ 本 feature 之關鍵差異 —— 鏈路之第一環不存在

| | `vehicle_category` | **`sw_update`** |
|---|---|---|
| 037 版面 | **20 欄 rev D** | **18 欄舊版面**（下放包 01 §3.2） |
| `HMI Source ID` 欄 | **有**（欄 2） | **無** |
| 純 Service 列有無該欄值 | **42 列全有** —— 故「純 Service 怎麼填」在該 feature **不成為問題** | —— |
| `C` 之鏈路 | **126/126 成立** | **第一環即缺** |

**替代鍵之實測（本項下放包未令，見 §7.3）**：
以 sw_update 之 037 `Source Requirement ID`（三形態，R-SU5 v2）
對 SYS1 之三欄取交集：

| 037 之 `Source Requirement ID` vs SYS1 | 交集 |
|---|---:|
| SYS1 `ID`（`NRL-168414` …） | **0** |
| SYS1 `SYSRE_HMI_Source ID` | **0** |
| SYS1 `Outline Number`（`1`／`1.1` …） | **0** |

其形態分佈：`SYS-RA-FOTA-N` 298 列／`SYS-RA-VFN_VN-N` 10 列／
`SYS-RA-FOTA-N/SYS-RA-FOTA-N` 3 列 —— **與 SYS1 之任一識別碼形態皆不同族**。

**結論（陳報，不裁）**：**本 feature 無可用之 `C` 欄取值路徑。**
`vehicle_category` 之作法**不可移植** —— 其可行係因其 037 版面較新。
若仍要填 `C`，須另有來源（例如上游補一份 037↔Polarion 之對照），
**而那將是一筆新 DR**；**執行層不代為開立。**

---

## 4. T38c —— 難類涵蓋之全案盤點

> 用途：分析層據以排後續批次之順序，並使**每批之難類涵蓋可見**。

| Test Set | 總列數 | 126 內部列 | **105 列** | 105 佔比 | 含 GT 之列 |
|---|---:|---:|---:|---:|---:|
| `Telematics Client` | 5 | 5 | **4** | **80%** | 0 |
| `Interruption Handling` | 19 | 14 | **14** | **74%** | 13 |
| `Status Reporting` | 7 | 5 | **5** | **71%** | 1 |
| `Session Flows` | 16 | 11 | **10** | **62%** | 0 |
| `Bearer Selection` | 16 | 11 | **10** | **62%** | 1 |
| `Update Agent` | 14 | 9 | **8** | **57%** | 0 |
| `Configurable Parameters` | 2 | 1 | **1** | **50%** | 0 |
| `Client Architecture` | 35 | 21 | **17** | **49%** | 5 |
| `Session Management` | 13 | 8 | **5** | **38%** | 1 |
| `Integrity Verification` | 8 | 4 | **3** | **38%** | 3 |
| `Update Policy` | 17 | 8 | **6** | **35%** | 3 |
| `FOTA Overview` | 6 | 2 | **2** | **33%** | 0 |
| `Deployment Flow` | 26 | 10 | **8** | **31%** | 0 |
| `Deployment Conditions` | 8 | 2 | **2** | **25%** | 0 |
| `USB Update` | 5 | 1 | **1** | **20%** | 0 |
| `Wi-Fi Download` | 29 | 7 | **5** | **17%** | 0 |
| `Silent Update` | 9 | 2 | **1** | **11%** | 3 |
| `TBM Reflash` | 14 | 1 | **1** | **7%** | 0 |
| `HU FOTA via TBM` | 36 | 3 | **2** | **6%** | 2 |
| `ROV Installation` | 20 | 1 | 0 | **0%** | 0 |
| `Update HMI` | 6 | 0 | 0 | **0%** | 0 |
| **合計** | **311** | **126** | **105** | **34%** | **32** |

- **105 佔比 ≥60% 之組**：**5** —— `Telematics Client`（4/5）、`Interruption Handling`（14/19）、`Status Reporting`（5/7）、`Session Flows`（10/16）、`Bearer Selection`（10/16）
- **105 列為 0 之組**：**2** —— `ROV Installation`（20 列）、`Update HMI`（6 列）
- 含 GT 之列合計 **32**（GT-A1 28 + GT-B 4 = 32；相符）

### 4.1 三個讀法（陳報，不裁）

- **`Update HMI`（6 列）與 `ROV Installation`（20 列）之 105 列為 0** ——
  該二組在現況下**可完整撰寫**，共 26 列。
- **五個 ≥60% 之組合計 63 列**（`Telematics Client` 5／`Interruption Handling` 19／
  `Status Reporting` 7／`Session Flows` 16／`Bearer Selection` 16），
  其中 105 列共 **43 列**。
- **`Interruption Handling` 之特殊處**：其 105 列 14 列為全案最多，
  **而其含 GT 之列亦為全案最多（13 列）** ——
  即該組同時是「錨定證據最厚」與「觀測面最缺」的一組。
  二者不衝突：GT 解的是**錨到哪一條規格**，不是**測試時看哪裡**。

---

## 5. 未結 DR 清單（2 筆）

| # | 事項 | 狀態 | 確認進度 | Urgency |
|---|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | OPEN | —（單列標的） | High |
| **DR-SU2** | 105 列於系統測層級之觀測手段 | OPEN | **5 / 105（5%）** | High |

> DR-SU2 之進度為 5%，**不得被陳述為「已盤點完成」**（R-SU30(d)）。
> ⚠ 其二段之一致性有一處問題，見 §7.1。

---

## 6. 待分析層確認之事項（非 DR）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **`C` 欄無取值路徑** —— 填則須新 DR，或裁定留空 | §3.1 |
| 2 | **`E` 欄**：15 本簿 2167 列全空、母本無 DV —— 疑可裁「不用（測試管理端）」 | §3 |
| 3 | **DR-SU2 二段之一致性**：`365` 在 (a) 段而不在 (b) 段之母群內 | §7.1 |
| 4 | **後續批次之順序**（§六.6 之問，見 §7.2） | §4.1 |

---

## 7. 獨立自評

### 7.1 ⚠ 一處我在做 T38c 時撞到的台帳不一致

DR-SU2 之二段為：**(a) 已確認段 5 列**（`363`–`367`）／
**(b) 未確認母群 105 列**。

T38c 之逐組盤點顯示 `Telematics Client` 之 105 列為 **4**，非 5。
逐列查之，**`SWE1-FOTA-365` 不在 105 列之內**，其成因為：

> 其 `Verification Criteria` 首句為
> 「Send a server-initiated OTA **notification** through the TC client.」
> —— `notification` 命中我之「HMI／畫面」regex，故其 VC 被判為「有外部面」。

**而該 `notification` 是服務間之訊息，不是使用者通知** ——
即上繳包 19 §7.1(甲) 已指認之偽陰性類，**現在出現在 DR-SU2 之清單本身裡**。

**其後果是台帳之邏輯不一致**：**(a) 段不是 (b) 段之子集**。
R-SU30(b) 令 (b) 為「符合同一語形條件但尚未逐列判定者」，
而 (a) 之 `365` 由分析層逐列判定為無觀測面 —— **人裁與語形判準在此列上不一致**。

**二者何者為準是明確的**：**人裁為準**（語形判準只是上界之估計工具，
上繳包 20 §7.1(乙2) 已裁其地位）。
故 (b) 之母群**應為 106 列**（105 + `365`），或
**105 之定義應改為「扣除已人裁者之餘數」**。

**執行層不自行改母群數**（DR 之台帳體例屬分析層），
但**已於 §5 加註其不一致**，列為待確認 #3。

**記明此事之理由**：R-SU30 之二段設計是為了防「未確認被讀成已確認」，
**而它防不到「二段之成員資格用了兩套不同的判準」** ——
(a) 用人裁、(b) 用 regex。**一個台帳若二段來源不同，其比值就不是進度。**

### 7.2 §六.6 所問：105 佔比極高之組，該排前面還是後面

**我認為該排前面，而且理由不是「早點撞牆」。**

**(甲) 「等 DR-SU2 有回應再做」之路，其問題是它假設了 DR 會有回應。**
DR-SU2 之標的為上游文件之內在不一致，其期程不可控（上繳包 22 §3.1）。
把 43 列（五個高佔比組之 105 列）押在一個期程不可控之 DR 上，
**等於把 34% 之母體變成無限期待辦**。

**(乙) 排前面之實質理由：DR-SU2 之清單本身需要它。**
DR-SU2 現有 5 列，**上界 105 列，確認進度 5%**。
而 R-SU30(a) 令入清單者須**已逐列判定**。
即：**要讓 DR-SU2 成為一份有說服力之請求，就必須先逐列判過** ——
**先做高佔比組，等於先把 DR 的內容備齊。**
反過來先做低佔比組，DR-SU2 會在很長一段時間內停在 5/105，
而 5 列之請求對上游之說服力遠低於 43 列。

**(丙) 但有一個更強的相反理由，我必須並陳。**
R-SU31(c) 已裁：`SWE1-FOTA-179` 為**首個進入撰寫之 105 列**，
其處理結果**才是 105 列可寫性之首例證據**。
**在 `179` 之結果出來前，我們不知道 R-SU25(c) 之三個作法對 105 列是否夠用。**

若 `179` 顯示那些作法**夠用**，則 105 之上界會大幅鬆動 ——
那時高佔比組不是「難組」，只是「還沒做的組」，排序問題消失。
若顯示**不夠用**，才需要上述之甲／乙權衡。

**故我之建議是三段，不是二選一**：
1. **先完成 batch 1（含 `179`）** —— 取得首例證據，成本 5 列
2. 依 `179` 之結果**分岔**：夠用 → 依原有順序（規模／GT 厚度）排；
   不夠用 → 高佔比組優先，以最快速度把 DR-SU2 之確認段做厚
3. **無論哪一岔，`ROV Installation`＋`Update HMI` 之 26 列（105 為 0）
   可隨時併行** —— 其不受本議題影響

**執行層不裁批次順序**（屬分析層），以上為陳報與建議。

### 7.3 一項我做了而下放包未要求的事

**§3.1 之替代鍵實測。**

T38a 只令追查 `vehicle_category` 之 `C` 欄填值來源。
查完會得到一條漂亮的鏈路（126/126 全對），**而那條鏈路對本 feature 沒有用** ——
因為它的第一環 `HMI Source ID` 在 sw_update 之 037 裡不存在。

**若只交那條鏈路，讀者會合理推論「照做即可」**，
而下一輪才會發現第一環缺了。

我另做的是**反過來問一次：本 feature 有沒有別的鍵可以接上 SYS1？**
以 037 之 `Source Requirement ID` 對 SYS1 之三欄取交集 —— **三個都是 0**，
且其形態（`SYS-RA-FOTA-N`）與 SYS1 之 `NRL-N` 根本不同族。

**記明此事之理由**：查一條路走得通，與查**所有路都走不通**，是兩件事。
前者只需要一個成功案例，後者需要窮舉。
**而「有沒有別的路」這個問題，通常不會出現在任務清單裡** ——
因為任務是照著已知的那條路寫的。
