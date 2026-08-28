# 上繳包 14 —— Layer 2 材料傾印、framework 骨架、R-SU18 抄錄

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/15_framework_draft.md`
  （SHA256 `7c0aa64d46dd81160630910e5c378d1e65f2e5fde0c947ecf62bd7cb82cb27f1`，133 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜新腳本：`scripts/framework_draft.py`
- 新建檔：**`features/sw_update/framework.md`**

## 本輪三個主結果

1. **`SWE1-FOTA-022`（Communication Security）在 §4.2 中無歸屬** ——
   既不在 12 組，也不在 PENDING 之二群。其所轄 in-scope 列為 **0**，
   故**列數閉合（234 + 77 = 311）照樣通過**，群數閉合才揭出它（44/45）。
   已於 `framework.md` 專列為 `UNASSIGNED`，**執行層不自行歸屬**。
2. **§4.1 之二數皆與實測相符**：含 HMI 列之群 **17**（原則 3）、
   逾 40 列之群 **1**（`309`，70 列，原則 4）。
   但**原則 4 若及於 Test Set 而非只及於 Heading 群，則已定稿之
   `TBM Update`（50 列）與 `Session Flows`（42 列）二組亦逾界** —— 待裁。
3. **T28a 之標題足以支撐能力性質之判斷，但有一個明確的例外**：
   標題**分不出「統攝型」與「其兄弟」**。`313` 之標題
   `Software Update Error Handling Coordination` 讀起來與 `315`–`320`
   同級，而它實為統攝該六列之上位列（GT-A1 自證錨已裁）。詳見 §5.1。

---

## 1. T28e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU18 | 757 | **OK** | `018160d1a8ad` |

逐字 append，**既有 28 個條文區塊未受影響** ✅（現 29 塊）。
索引表現行 **18 條**（新增 R-SU18）；留存不得引用者 **11 條**（無變動）。
與下放包 15 §五 T28e 所定之「18 條現行」一致。

`PLAYBOOK.md` §7 追加 **(12)**「導航面之推定與交付面之依據須分層 ——
前者可 provisional，後者不可」，並寫明其解開之僵局：
「錨定不夠嚴謹所以 framework 不能定稿」在此不成立，
因不夠嚴謹的只是 Layer 3，而 Layer 3 本就不進工作簿。

---

## 2. T28a —— `SWE1-FOTA-309` 群列標題傾印（70 列）

Heading 群 `SWE1-FOTA-309`｜所轄 in-scope 列 **70**｜id 範圍 `310`–`383`

> **僅三欄**（下放包 15 §五）：不附分數、不附候選 —— Layer 2 之切分依 R-SU18(b) 不依賴逐列錨定。

| # | 037 列 | Requirement Title | Sub Cat |
|---:|---|---|---|
| 1 | `SWE1-FOTA-310` | OMA-DM Message Integrity Verification | Service |
| 2 | `SWE1-FOTA-311` | DM Tree Encryption and Protection | Service |
| 3 | `SWE1-FOTA-312` | Deployment Package Integrity Verification | Service |
| 4 | `SWE1-FOTA-313` | Software Update Error Handling Coordination | Service |
| 5 | `SWE1-FOTA-315` | Socket Read/Write Error Handling | Service |
| 6 | `SWE1-FOTA-316` | Network Loss Handling | Service |
| 7 | `SWE1-FOTA-317` | User-Initiated Network Deactivation Handling | Service |
| 8 | `SWE1-FOTA-318` | Emergency State Handling | Service |
| 9 | `SWE1-FOTA-319` | Power Loss Handling | Service |
| 10 | `SWE1-FOTA-320` | Host System Disconnection Handling | Service |
| 11 | `SWE1-FOTA-321` | Interruption Recovery Handling | Service |
| 12 | `SWE1-FOTA-322` | Insufficient Storage Space Handling | Service |
| 13 | `SWE1-FOTA-323` | Concurrent NIA Handling | Service |
| 14 | `SWE1-FOTA-324` | Partial Download Preservation | Service |
| 15 | `SWE1-FOTA-325` | Download Interruption Handling | Service |
| 16 | `SWE1-FOTA-326` | Download Resume Verification | Service |
| 17 | `SWE1-FOTA-327` | Download Resume Based on Interruption Type | Service |
| 18 | `SWE1-FOTA-328` | Internal Network Interruption Recovery | Service |
| 19 | `SWE1-FOTA-329` | External Network Interruption Retry Handling | Service |
| 20 | `SWE1-FOTA-330` | OTA Session Completion Reporting | Service |
| 21 | `SWE1-FOTA-331` | OTA Session Report Retry Handling | Service |
| 22 | `SWE1-FOTA-332` | OTA Session Report Resend | Service |
| 23 | `SWE1-FOTA-333` | OTA Session Report Retry | Service |
| 24 | `SWE1-FOTA-334` | Reflash Failure Reporting to OTA Server | Service |
| 25 | `SWE1-FOTA-336` | OTA Update Enable/Disable Handling | Service |
| 26 | `SWE1-FOTA-337` | Deployment Flow Initiation | Service |
| 27 | `SWE1-FOTA-338` | Pre-Deployment Package Authenticity Verification | Service |
| 28 | `SWE1-FOTA-339` | OTA Status Reporting via Backchannel | Service |
| 29 | `SWE1-FOTA-340` | Configurable Installation Conditions | Service |
| 30 | `SWE1-FOTA-341` | Deployment Condition Evaluation | Service |
| 31 | `SWE1-FOTA-343` | Vehicle Condition Provision | Service |
| 32 | `SWE1-FOTA-344` | Deployment Condition Validation and Notification | Service |
| 33 | `SWE1-FOTA-345` | Vehicle Condition Provision for Download Control | Service |
| 34 | `SWE1-FOTA-346` | Firmware Download Storage Allocation | Service |
| 35 | `SWE1-FOTA-347` | Vehicle-Initiated Polling Interval Configuration | Service |
| 36 | `SWE1-FOTA-348` | Polling Interval Configuration Parameter | Service |
| 37 | `SWE1-FOTA-349` | Polling Timer Monitoring | Service |
| 38 | `SWE1-FOTA-350` | Session Precondition Evaluation | Service |
| 39 | `SWE1-FOTA-351` | Server-Initiated Session Flow | Service |
| 40 | `SWE1-FOTA-352` | Software Inventory Request Handling | Service |
| 41 | `SWE1-FOTA-353` | Deployment Download Sequence | Service |
| 42 | `SWE1-FOTA-354` | Download Acceptance Processing | Service |
| 43 | `SWE1-FOTA-355` | Download Precondition Data Provision | Service |
| 44 | `SWE1-FOTA-356` | Deployment Package Notification | Service |
| 45 | `SWE1-FOTA-357` | Installation Interruption State Management | Service |
| 46 | `SWE1-FOTA-358` | Update Status Reporting to SWMC | Service |
| 47 | `SWE1-FOTA-359` | OTA Flow Concurrency Control | Service |
| 48 | `SWE1-FOTA-360` | Download Interruption Recovery | Service |
| 49 | `SWE1-FOTA-361` | Server-Initiated OTA Background Execution | Service |
| 50 | `SWE1-FOTA-363` | TC Communication Establishment | Service |
| 51 | `SWE1-FOTA-364` | TC Subscription for OTA Updates | Service |
| 52 | `SWE1-FOTA-365` | Server-Initiated Session Handling from TC | Service |
| 53 | `SWE1-FOTA-366` | FOTA Update Availability Check | Service |
| 54 | `SWE1-FOTA-367` | Server-Initiated Session Forwarding from TC | Service |
| 55 | `SWE1-FOTA-368` | OTA Session Precondition Evaluation and Queueing | Service |
| 56 | `SWE1-FOTA-369` | Server-Initiated Flow Alignment with Vehicle-Initiated Flow | Service |
| 57 | `SWE1-FOTA-370` | Update Deployment Method Support | Service |
| 58 | `SWE1-FOTA-371` | Target Selection and Installer Assignment | Service |
| 59 | `SWE1-FOTA-372` | Dependency-Based Installation Ordering | Service |
| 60 | `SWE1-FOTA-373` | Update Progress API Provision | Service |
| 61 | `SWE1-FOTA-374` | UA Integration API Provision | Service |
| 62 | `SWE1-FOTA-375` | Deterministic Software Image Installation | Service |
| 63 | `SWE1-FOTA-376` | Update Agent Self-Update Capability | Service |
| 64 | `SWE1-FOTA-377` | A/B Update Mechanism Support | Service |
| 65 | `SWE1-FOTA-378` | Update Interruption Failsafe Mechanism | Service |
| 66 | `SWE1-FOTA-379` | Update Bricking Prevention | Service |
| 67 | `SWE1-FOTA-380` | Update Recovery Mechanism | Service |
| 68 | `SWE1-FOTA-381` | Differential Update Technology Support | Service |
| 69 | `SWE1-FOTA-382` | Pre-Update and post-update Differential Compatibility Verification | Service |
| 70 | `SWE1-FOTA-383` | Deployed Software Validation | Service |

**小計 70 列** —— Service 70

---

## 3. T28b —— `SWE1-FOTA-170` 群列標題傾印（7 列）

Heading 群 `SWE1-FOTA-170`｜所轄 in-scope 列 **7**｜id 範圍 `171`–`177`

> **僅三欄**（下放包 15 §五）：不附分數、不附候選 —— Layer 2 之切分依 R-SU18(b) 不依賴逐列錨定。

| # | 037 列 | Requirement Title | Sub Cat |
|---:|---|---|---|
| 1 | `SWE1-FOTA-171` | Verification and Validation FCA Signed Deployment Packages | Service |
| 2 | `SWE1-FOTA-172` | Validate Source Version for Differential Update Package | Service |
| 3 | `SWE1-FOTA-173` | Integrate with Signature Verification Module for Deployment Packages | Service |
| 4 | `SWE1-FOTA-174` | Verify Each File in Multi-File Deployment Package Before Installation | Service |
| 5 | `SWE1-FOTA-175` | Execute Silent Update Without User Interaction | Service |
| 6 | `SWE1-FOTA-176` | Restrict Silent Session Notifications to Safety-Required Cases | Service |
| 7 | `SWE1-FOTA-177` | Restrict Opt-Out and Deferral Options in HMI | HMI |

**小計 7 列** —— HMI 1／Service 6

---

## 4. T28c —— 全 45 Heading 群之列數與 HMI／Service 對照

| # | Heading id | 標題原文 | 列數 | HMI | Service | blank | 逾 40 |
|---:|---|---|---:|---:|---:|---:|:--:|
| 1 | `SWE1-FOTA-001` | Firmware Over-the-air Updates (FOTA) | 6 | 2 | 4 | 0 |  |
| 2 | `SWE1-FOTA-009` | Critical Updates | 6 | 1 | 5 | 0 |  |
| 3 | `SWE1-FOTA-016` | Session Flows | 0 | 0 | 0 | 0 |  |
| 4 | `SWE1-FOTA-017` | Deployment Flow | 0 | 0 | 0 | 0 |  |
| 5 | `SWE1-FOTA-018` | Installation and Download Conditions | 1 | 0 | 1 | 0 |  |
| 6 | `SWE1-FOTA-020` | Re-Flashing Requirements | 0 | 0 | 0 | 0 |  |
| 7 | `SWE1-FOTA-022` | Communication Security | 0 | 0 | 0 | 0 |  |
| 8 | `SWE1-FOTA-024` | Critical Updates | 11 | 3 | 8 | 0 |  |
| 9 | `SWE1-FOTA-038` | OTA download via Wi-Fi | 15 | 10 | 5 | 0 |  |
| 10 | `SWE1-FOTA-055` | Non-Critical Updates | 2 | 1 | 1 | 0 |  |
| 11 | `SWE1-FOTA-058` | Connection to Wi-Fi network | 12 | 1 | 11 | 0 |  |
| 12 | `SWE1-FOTA-072` | OTA Client Architecture | 0 | 0 | 0 | 0 |  |
| 13 | `SWE1-FOTA-073` | Operating Environment | 0 | 0 | 0 | 0 |  |
| 14 | `SWE1-FOTA-074` | Over The Air (OTA) Deployment of Software | 0 | 0 | 0 | 0 |  |
| 15 | `SWE1-FOTA-076` | Local Deployment of Software | 0 | 0 | 0 | 0 |  |
| 16 | `SWE1-FOTA-078` | Media Reflash Requirements | 5 | 0 | 5 | 0 |  |
| 17 | `SWE1-FOTA-085` | FOTA ROV Reflash Requirements | 0 | 0 | 0 | 0 |  |
| 18 | `SWE1-FOTA-086` | Post-Installation | 3 | 2 | 1 | 0 |  |
| 19 | `SWE1-FOTA-091` | Installation Progress | 4 | 4 | 0 | 0 |  |
| 20 | `SWE1-FOTA-096` | Pre-Installation | 13 | 10 | 3 | 0 |  |
| 21 | `SWE1-FOTA-110` | TBM FOTA Reflash | 14 | 11 | 3 | 0 |  |
| 22 | `SWE1-FOTA-125` | Appendix B Configurable Parameters | 1 | 0 | 1 | 0 |  |
| 23 | `SWE1-FOTA-127` | Download Descriptor Format | 1 | 0 | 1 | 0 |  |
| 24 | `SWE1-FOTA-129` | User Experience (UX)/HMI | 6 | 5 | 1 | 0 |  |
| 25 | `SWE1-FOTA-137` | Deployment flow | 26 | 9 | 17 | 0 |  |
| 26 | `SWE1-FOTA-168` | Vehicle-Initiated Session Flow | 1 | 0 | 1 | 0 |  |
| 27 | `SWE1-FOTA-170` | Deployment Package Security | 7 | 1 | 6 | 0 |  |
| 28 | `SWE1-FOTA-178` | For a silent update, the OTA client follows  | 6 | 1 | 5 | 0 |  |
| 29 | `SWE1-FOTA-185` | OTA client sessions | 1 | 0 | 1 | 0 |  |
| 30 | `SWE1-FOTA-188` | User initiated sessions | 3 | 2 | 1 | 0 |  |
| 31 | `SWE1-FOTA-192` | Bus communications | 3 | 0 | 3 | 0 |  |
| 32 | `SWE1-FOTA-200` | OTA Client Configuration options | 1 | 0 | 1 | 0 |  |
| 33 | `SWE1-FOTA-202` | OTA Architecture Requirements | 10 | 4 | 6 | 0 |  |
| 34 | `SWE1-FOTA-214` | HU FOTA with TBM | 36 | 20 | 16 | 0 |  |
| 35 | `SWE1-FOTA-251` | High Level FOTA Diagram | 7 | 0 | 7 | 0 |  |
| 36 | `SWE1-FOTA-259` | Vehicle Properties | 3 | 0 | 2 | 1 |  |
| 37 | `SWE1-FOTA-263` | OTA Architecture Requirements | 2 | 0 | 2 | 0 |  |
| 38 | `SWE1-FOTA-266` | OTA Client Configuration options | 4 | 0 | 4 | 0 |  |
| 39 | `SWE1-FOTA-271` | OTA server initiated sessions | 6 | 0 | 6 | 0 |  |
| 40 | `SWE1-FOTA-278` | User initiated sessions | 1 | 0 | 1 | 0 |  |
| 41 | `SWE1-FOTA-280` | Interface Definitions | 4 | 0 | 4 | 0 |  |
| 42 | `SWE1-FOTA-285` | OTA Client Performance Requirements | 1 | 0 | 1 | 0 |  |
| 43 | `SWE1-FOTA-287` | OTA client Flows | 3 | 0 | 3 | 0 |  |
| 44 | `SWE1-FOTA-291` | Bearer selection: | 16 | 0 | 16 | 0 |  |
| 45 | `SWE1-FOTA-309` | OMA-DM Security | 70 | 0 | 70 | 0 | ⚠ |
| | **合計** | | **311** | **87** | **223** | **1** | |

**閉合檢查**：87 + 223 + 1 = 311；驗證母體（R-SU3）= 311 —— 閉合 ✅

### §4.1 原則 3、4 之複核

- **原則 3（純 Service 群之健康判準）**：含 ≥1 個 HMI 列之群 **17** 群 —— 下放包 15 §4.1 稱「17 個含 HMI 列之群」，**與實測一致**。純 Service 群 **19** 群；45 群中另有 **9** 群無 in-scope 列（17 + 19 + 9 = 45）
- **原則 4（逾 40 列者須檢視）**：逾 40 列之群 **1** 群 —— `SWE1-FOTA-309`（70 列，OMA-DM Security）

### 4.1 ⚠ `SWE1-FOTA-022` 無歸屬

下放包 15 §4.2 之 12 組共列 **42** 個 Heading id，加上 PENDING 之
`309`／`170` 共 44，而全體為 **45 群**。差額為 `SWE1-FOTA-022`
（`Communication Security`，**0 列**）。

已列入定稿表之 0 列群有 `016`／`017`／`020`／`072`／`073`／`074`／`076`／`085`
共 8 個 —— 即下放包**確有意將 0 列群納入歸屬**，`022` 之遺漏因此不像是
刻意排除。**執行層不自行歸屬**（Test Set 之切分屬 R-SU18(b) 之分析層裁定），
於 `framework.md` 專列一節標 `UNASSIGNED`。

**值得記的是它為什麼差點看不見**：其所轄 in-scope 列為 0，
故列數閉合 234 + 77 = 311/311 **完全通過**。
只有加算群數（42 + 2 = 44 ≠ 45）才會撞到它。
**一個只查列數的閉合式，對 0 列群是全盲的。**

### 4.2 原則 4 之射程待裁

原則 4 為「單群列數上限以『可作為索引』為度 —— 逾 40 列者須檢視」。
若「單群」指 **Heading 群**，則唯一逾界者為 `309`（70 列），已在 PENDING。

若「單群」指 **Test Set**，則已定稿之二組亦逾界：

| Test Set | 列數 | 所轄群 |
|---|---:|---|
| `TBM Update` | **50** | `110`(14) + `214`(36) |
| `Session Flows` | **42** | 10 群（其中 `137` 佔 26） |

**執行層不判其是否須拆**，僅陳報此二數。

---

## 5. T28d —— `framework.md` 全文

已建於 `features/sw_update/framework.md`（172 行）。結構：

| 節 | 內容 | 狀態標示 |
|---|---|---|
| 檔首 | R-SU18 三級標示表 + Layer 3 覆蓋狀態（已裁 28／PROVISIONAL 279／311） | — |
| Part I | Layer 1 = `SW Update` | **定稿** |
| Part II | 切分原則 5 條 + 定稿 12 組（234 列，含 Heading 標題原文）+ PENDING 二群（77 列）+ UNASSIGNED 1 群 + 雙重閉合 | **定稿（77 列 PENDING）** |
| Part III | 空，僅列現階段之 GT 材料狀態與 R-SU17 v2(e) 揭露 | **PROVISIONAL — 待下放包 16** |

**雙重閉合**（列數與群數皆查，沿上繳包 06 §3.1 之教訓）：

| 判準 | 實測 | 應為 | |
|---|---:|---:|:--:|
| 定稿 234 + PENDING 77 | **311** | 311（R-SU3） | ✅ |
| 定稿 42 群 + PENDING 2 + UNASSIGNED 1 | **45** | 45 | ✅ |

R-SU18(c) 之拘束（provisional 不得外溢至 `specification_reference`）
已逐字載於檔首之引述框。

---

## 6. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

### 待分析層確認之事項（非 DR，無外部資料需求）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **`SWE1-FOTA-022`（0 列）之歸屬** —— 併入某組或維持 UNASSIGNED | §4.1 |
| 2 | **原則 4 之射程**：「單群」指 Heading 群或 Test Set。若指後者，`TBM Update`(50)／`Session Flows`(42) 亦須檢視 | §4.2 |
| 3 | **T28a 之標題不足以分辨統攝型** —— 是否加碼 Description（下放包令不自行補，故僅指出） | §7.1 |

---

## 7. 獨立自評

### 7.1 §六.6 所問：T28a 只給標題不給描述，是否足以支撐能力性質之判斷

**大致足夠，且好得出乎意料 —— 但有一個結構性的例外，該例外恰好落在本群。**

**足夠的部分。** `309` 之 70 個標題並非泛稱，而是能力級之短語，
逐段讀下來叢集邊界相當清楚：

| 段 | 037 列 | 標題所示之能力 |
|---|---|---|
| A | `310`–`312` | OMA-DM／部署包之完整性與加密 |
| B | `313`、`315`–`329` | **中斷處理與續傳**（Socket／網路／電源／緊急／儲存／並行…） |
| C | `330`–`334` | 工作階段回報與其重送 |
| D | `336`–`346` | 部署條件之組態、評估、車輛條件提供 |
| E | `347`–`358` | 輪詢與 server-initiated session flow |
| F | `359`–`369` | 並行控制、TC（Telematics Client）介接 |
| G | `370`–`383` | Update Agent：目標選擇、A/B、失效保護、差分更新 |

七段皆可由標題單獨讀出，**不需描述**。`170` 群更明顯：
`171`–`174` 為簽章驗證、`175`–`177` 為靜默更新 —— **4 + 3 之切分由標題即可見**，
且與已裁事實吻合（`176` 之正解在 `4.7.3.2 Silent Updates`，下放包 15 §4.3）。
**這是一個獨立的佐證：標題所示之切分，在唯一有人裁的那一列上與正解一致。**

**不足的部分 —— 標題分不出「統攝型」與「其兄弟」。**

`313` 之標題為 `Software Update Error Handling Coordination`，
讀起來與 `315 Socket Read/Write Error Handling`、`319 Power Loss Handling`
**同級**。但 GT-A1 已裁：`313` 之 Description 逐字列出六個 id
（`4907667`–`4907672`），**它是統攝該六列之上位列**，不是第七個兄弟。
**這件事在標題裡沒有任何跡象** —— `Coordination` 一字事後看有指示性，
但事前不足以與 `Handling` 區分。

同型之風險點另有二處（僅指出，不判）：
- `321 Interruption Recovery Handling` 與 `325 Download Interruption Handling`、
  `360 Download Interruption Recovery` —— 三個近義標題散在三段，
  標題無法判其為同一能力之三面或三個不同能力
- `347 Vehicle-Initiated Polling Interval Configuration` 與
  `348 Polling Interval Configuration Parameter` —— 近乎同名

**這對 Layer 2 之影響有多大**：**很小。** 統攝型與其兄弟**屬於同一個能力叢集**
（都在 B 段），Layer 2 之切分不會因分不出上下位而放錯組。
分不出上下位真正影響的是 **Layer 3 與 `specification_reference`** ——
而那正是 R-SU18(c) 已經隔開的東西。

**故結論**：就 **Layer 2 之用途**而言，標題**足夠**；
就辨識統攝型而言不足，但那不是本輪的用途。
**依下放包之指示未自行補描述**，是否加碼由分析層裁（待確認 #3）。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §5 之「雙重閉合皆通過」。**

那兩個 ✅ 看起來像是「framework 的歸屬全部查清了」。
實際上它們只證明了**沒有列或群被弄丟**，完全沒有證明**分得對**。
`TBM Update` 把 50 列放進一組、`Session Flows` 把 10 個 Heading 群
（含 26 列的 `137`）併成一組 —— 這兩個決定的對錯，
閉合式一個字都不會說。

而 §4.2 剛好指出這兩組**都逾原則 4 之 40 列界**。
**即：閉合式全綠的同時，唯一一條能查「分得對不對」的原則正在報警。**
把二者並陳才是誠實的呈現，只報前者會讓 framework 看起來比實際確定。

### 7.3 一項我做了而下放包未要求的事

**群數之閉合檢查。**

T28d 只令「寫入 §4.2 之定稿表」。照做並查列數，會得到 234 + 77 = 311 ✅，
一切正常。**群數是我另加的**，加的理由是上繳包 06 §3.1 之教訓
（雙重閉合：id 數**與**非空文字數都要查）在此的同型套用 ——
列數與群數是同一份歸屬的兩個投影，只查一個就會漏掉
**「列數為 0 的群」這一整類物件**。

結果它立刻抓到 `SWE1-FOTA-022`。
**這一群 0 列，所以它被漏掉不影響任何交付數字** ——
但它是一個 Heading 群，日後若 037 改版而該群長出列，
它會以「framework 從未涵蓋過的群」之形態出現，而那時沒有人會記得它是舊漏。

**記明此事**：0 列之物件是閉合檢查的系統性盲區，
因為每一種「以量為準」的檢查對零都無感。要抓它只能改查**種類**。
