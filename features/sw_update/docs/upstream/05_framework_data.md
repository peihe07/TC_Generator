# 上繳包 05 —— T-抄（R-SU10／R-SU11）、T19a–e 定稿前置量測

- 日期：2026-08-27
- 對應下放：`docs/handoff/06_framework_draft.md`
  （SHA256 `568b973779a966fea31b545e284101c565fd69964af0f3b65848f160eca0e4a2`，172 行）
- **結論：T-抄完成（逐字元核對相符）；T19a–e 全數執行。**
- **⚠ 本輪最重要之結果是否定性的**：逐列字面比對在此母體上**幾乎無判別力**
  —— 311 列中 **286 列（92%）未達門檻**。見 §0。
- 未起草 framework、未命名 Test Set、未寫回、未進行任何 git 操作。

---

## 0. ⚠ 先看這一件：T19 之工具在此母體上判別力極低

下放包 §四要求「詞集重疊比之參數與 T18d **完全一致**」，我照做了。
**結果是：同一套參數，在逐 Heading 之 T18d 上 CFTS 對應率 42/45（93%），
在逐列之 T19 上只有 25/311（8%）。**

| 量 | 列數 | 佔比 |
|---|---:|---:|
| 列之最佳候選**未達門檻**（`?`）| **286** | 92.0% |
| 其 Heading 之候選未達門檻（無可比對象）| 1 | 0.3% |
| **可比且不一致** | **23** | 7.4% |
| 可比且一致 | 1 | 0.3% |

**閉合**：286 + 1 + 23 + 1 = 311 ✅

**成因（推測，未驗）**：Heading 標題是**章節名**（與 CFTS 章節名同體例），
列標題是**需求句之摘要**（如 `Fallback to TBM Network for FOTA Download`）——
二者不同體例，字面重疊自然低。

**這對下放包之三個問題各有不同影響**，見 §2–§4。
**不建議改參數** —— 改門檻只會把雜訊拉進來；
真正的問題是「列標題與章節名不可比」，那不是門檻能解的。

---

## 1. T-抄 —— R-SU10／R-SU11

逐字 append 入 `RULINGS.md`，**程式回讀逐字元核對**：

```
R-SU10: 逐字元核對 **相符**  sha d2d0a93a46c4a8fa / d2d0a93a46c4a8fa
R-SU11: 逐字元核對 **相符**  sha c7f2ea4047d8059f / c7f2ea4047d8059f
```

索引表依 R-SU8(b) 同步 —— **現行 11 條、留存 2 條**（與下放包要求相符）：

## 現行版索引（R-SU8(b)）

> 判準（R-SU8(a)）：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-SU1 | v1 | feature 身分與 test_group（`SW Update`／`sw_update`；前綴 R-SU／A-SU／DR-SU） | 01 §二 |
| R-SU2 | v1 | 036 母本與 workbook_state = BLANK；寫回採 XML 外科式修改 | 01 §二 |
| R-SU3 | v1 | 驗證母體 311 = FR 307 + NFR 4；範圍以 037 實際納入為準 | 01 §二 |
| R-SU4 | **v2** | spec_reference 雙家族錨點（CFTS057-{ObjectID}／SYS1 章節 token）+ 錨點池範圍 (a2) | 02 §二 |
| R-SU5 | **v2** | 037 Source Requirement ID 欄之三形態；該欄不取為 spec_reference | 03 §2.1 |
| R-SU6 | **v2** | HMI 規格本文為真 PDF，全文字層；一律機器抽取，p.{n} 為覆核義務 | 02 §二 |
| R-SU7 | **v2** | Description 物件不入池；錨點池 574 = 章節 87 + 需求 487，Description 137 | 04 §1.2 |
| R-SU8 | v1 | 本表之判準：v 字尾最大者為現行；檔首須維持索引表 | 05 §二 |
| R-SU9 | v1 | recon 產物之重生條件（未簽佔位得刪檔重生並揭露；已簽或含人手內容不得刪） | 05 §二 |
| R-SU10 | v1 | Layer 2 分群鍵為 Heading id（非標題字串）；Test Set 名稱另命名 | 06 §二 |
| R-SU11 | v1 | framework Layer 3 主軸為 CFTS_57；SYS1 不作章對章橋接，其接點為 HMI 87 列 | 06 §二 |

**留存之被取代條文（依 R-TM13 不刪不改，不得引用）**：

| 條號版本 | 已被取代於 | 其所載之失效值 |
|

---

## 2. T19a —— `SWE1-FOTA-309`（70 列）：**§3.1(a) 之假設證實**

### T19a —— `SWE1-FOTA-309` OMA-DM Security

所轄 in-scope 列 **70** 筆（id 區間 310–383）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-310` | OMA-DM Message Integrity Verification | Service | SYS-RA-FOTA-340 | **?** | 0.20 |
| `SWE1-FOTA-311` | DM Tree Encryption and Protection | Service | SYS-RA-FOTA-339 | **?** | 0.14 |
| `SWE1-FOTA-312` | Deployment Package Integrity Verification | Service | SYS-RA-FOTA-335 | 4.8.3 Deployment Package Securit | 0.40 |
| `SWE1-FOTA-313` | Software Update Error Handling Coordination | Service | SYS-RA-FOTA-188 | **?** | 0.17 |
| `SWE1-FOTA-315` | Socket Read/Write Error Handling | Service | SYS-RA-FOTA-190 | **?** | 0.17 |
| `SWE1-FOTA-316` | Network Loss Handling | Service | SYS-RA-FOTA-191 | **?** | 0.25 |
| `SWE1-FOTA-317` | User-Initiated Network Deactivation Handling | Service | SYS-RA-FOTA-192 | **?** | 0.33 |
| `SWE1-FOTA-318` | Emergency State Handling | Service | SYS-RA-FOTA-193 | **?** | 0.25 |
| `SWE1-FOTA-319` | Power Loss Handling | Service | SYS-RA-FOTA-194 | **?** | 0.25 |
| `SWE1-FOTA-320` | Host System Disconnection Handling | Service | SYS-RA-FOTA-195 | **?** | 0.20 |
| `SWE1-FOTA-321` | Interruption Recovery Handling | Service | SYS-RA-FOTA-196 | **?** | 0.25 |
| `SWE1-FOTA-322` | Insufficient Storage Space Handling | Service | SYS-RA-FOTA-198 | **?** | 0.20 |
| `SWE1-FOTA-323` | Concurrent NIA Handling | Service | SYS-RA-FOTA-199 | **?** | 0.25 |
| `SWE1-FOTA-324` | Partial Download Preservation | Service | SYS-RA-FOTA-201 | **?** | 0.25 |
| `SWE1-FOTA-325` | Download Interruption Handling | Service | SYS-RA-FOTA-202 | **?** | 0.25 |
| `SWE1-FOTA-326` | Download Resume Verification | Service | SYS-RA-FOTA-203 | **?** | 0.25 |
| `SWE1-FOTA-327` | Download Resume Based on Interruption Type | Service | SYS-RA-FOTA-204 | **?** | 0.17 |
| `SWE1-FOTA-328` | Internal Network Interruption Recovery | Service | SYS-RA-FOTA-205 | **?** | 0.20 |
| `SWE1-FOTA-329` | External Network Interruption Retry Handling | Service | SYS-RA-FOTA-206 | **?** | 0.17 |
| `SWE1-FOTA-330` | OTA Session Completion Reporting | Service | SYS-RA-FOTA-208 | **?** | 0.20 |
| `SWE1-FOTA-331` | OTA Session Report Retry Handling | Service | SYS-RA-FOTA-209 | **?** | 0.17 |
| `SWE1-FOTA-332` | OTA Session Report Resend | Service | SYS-RA-FOTA-210 | **?** | 0.20 |
| `SWE1-FOTA-333` | OTA Session Report Retry | Service | SYS-RA-FOTA-211 | **?** | 0.20 |
| `SWE1-FOTA-334` | Reflash Failure Reporting to OTA Server | Service | SYS-RA-FOTA-212 | **?** | 0.29 |
| `SWE1-FOTA-336` | OTA Update Enable/Disable Handling | Service | SYS-RA-FOTA-225 | **?** | 0.17 |
| `SWE1-FOTA-337` | Deployment Flow Initiation | Service | SYS-RA-FOTA-229 | 4.10.5 Deployment Flow | 0.67 |
| `SWE1-FOTA-338` | Pre-Deployment Package Authenticity Verification | Service | SYS-RA-FOTA-230 | **?** | 0.33 |
| `SWE1-FOTA-339` | OTA Status Reporting via Backchannel | Service | SYS-RA-FOTA-233 | **?** | 0.33 |
| `SWE1-FOTA-340` | Configurable Installation Conditions | Service | SYS-RA-FOTA-235 | 4.10.5.1 Installation and Download  | 0.50 |
| `SWE1-FOTA-341` | Deployment Condition Evaluation | Service | SYS-RA-FOTA-236 | **?** | 0.25 |
| `SWE1-FOTA-343` | Vehicle Condition Provision | Service | SYS-RA-FOTA-238 | **?** | 0.20 |
| `SWE1-FOTA-344` | Deployment Condition Validation and Notification | Service | SYS-RA-FOTA-240 | **?** | 0.20 |
| `SWE1-FOTA-345` | Vehicle Condition Provision for Download Control | Service | SYS-RA-FOTA-241 | **?** | 0.17 |
| `SWE1-FOTA-346` | Firmware Download Storage Allocation | Service | SYS-RA-FOTA-267 | **?** | 0.20 |
| `SWE1-FOTA-347` | Vehicle-Initiated Polling Interval Configuration | Service | SYS-RA-FOTA-274 | **?** | 0.33 |
| `SWE1-FOTA-348` | Polling Interval Configuration Parameter | Service | SYS-RA-FOTA-275 | **?** | 0.17 |
| `SWE1-FOTA-349` | Polling Timer Monitoring | Service | SYS-RA-FOTA-277 | **?** | 0.00 |
| `SWE1-FOTA-350` | Session Precondition Evaluation | Service | SYS-RA-FOTA-278 | **?** | 0.25 |
| `SWE1-FOTA-351` | Server-Initiated Session Flow | Service | SYS-RA-FOTA-279 | 4.10.2 Server-Initiated Session F | 1.00 |
| `SWE1-FOTA-352` | Software Inventory Request Handling | Service | SYS-RA-FOTA-280 | **?** | 0.20 |
| `SWE1-FOTA-353` | Deployment Download Sequence | Service | SYS-RA-FOTA-281 | **?** | 0.25 |
| `SWE1-FOTA-354` | Download Acceptance Processing | Service | SYS-RA-FOTA-282 | **?** | 0.25 |
| `SWE1-FOTA-355` | Download Precondition Data Provision | Service | SYS-RA-FOTA-283 | **?** | 0.20 |
| `SWE1-FOTA-356` | Deployment Package Notification | Service | SYS-RA-FOTA-284 | 4.8.3 Deployment Package Securit | 0.50 |
| `SWE1-FOTA-357` | Installation Interruption State Management | Service | SYS-RA-FOTA-286 | **?** | 0.25 |
| `SWE1-FOTA-358` | Update Status Reporting to SWMC | Service | SYS-RA-FOTA-287 | **?** | 0.20 |
| `SWE1-FOTA-359` | OTA Flow Concurrency Control | Service | SYS-RA-FOTA-289 | **?** | 0.20 |
| `SWE1-FOTA-360` | Download Interruption Recovery | Service | SYS-RA-FOTA-290 | **?** | 0.25 |
| `SWE1-FOTA-361` | Server-Initiated OTA Background Execution | Service | SYS-RA-FOTA-293 | 4.5.4 OTA server initiated sessi | 0.50 |
| `SWE1-FOTA-363` | TC Communication Establishment | Service | SYS-RA-FOTA-296 | **?** | 0.33 |
| `SWE1-FOTA-364` | TC Subscription for OTA Updates | Service | SYS-RA-FOTA-297 | **?** | 0.25 |
| `SWE1-FOTA-365` | Server-Initiated Session Handling from TC | Service | SYS-RA-FOTA-298 | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-366` | FOTA Update Availability Check | Service | SYS-RA-FOTA-299 | **?** | 0.20 |
| `SWE1-FOTA-367` | Server-Initiated Session Forwarding from TC | Service | SYS-RA-FOTA-302 | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-368` | OTA Session Precondition Evaluation and Queueing | Service | SYS-RA-FOTA-303 | **?** | 0.17 |
| `SWE1-FOTA-369` | Server-Initiated Flow Alignment with Vehicle-Initiat | Service | SYS-RA-FOTA-304 | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-370` | Update Deployment Method Support | Service | SYS-RA-FOTA-314 | **?** | 0.20 |
| `SWE1-FOTA-371` | Target Selection and Installer Assignment | Service | SYS-RA-FOTA-315 | **?** | 0.00 |
| `SWE1-FOTA-372` | Dependency-Based Installation Ordering | Service | SYS-RA-FOTA-316 | **?** | 0.25 |
| `SWE1-FOTA-373` | Update Progress API Provision | Service | SYS-RA-FOTA-317 | **?** | 0.20 |
| `SWE1-FOTA-374` | UA Integration API Provision | Service | SYS-RA-FOTA-318 | **?** | 0.00 |
| `SWE1-FOTA-375` | Deterministic Software Image Installation | Service | SYS-RA-FOTA-319 | **?** | 0.25 |
| `SWE1-FOTA-376` | Update Agent Self-Update Capability | Service | SYS-RA-FOTA-320 | 4.9.1 Update Agent Requirements | 0.50 |
| `SWE1-FOTA-377` | A/B Update Mechanism Support | Service | SYS-RA-FOTA-321 | **?** | 0.25 |
| `SWE1-FOTA-378` | Update Interruption Failsafe Mechanism | Service | SYS-RA-FOTA-322 | **?** | 0.20 |
| `SWE1-FOTA-379` | Update Bricking Prevention | Service | SYS-RA-FOTA-323 | **?** | 0.25 |
| `SWE1-FOTA-380` | Update Recovery Mechanism | Service | SYS-RA-FOTA-324 | **?** | 0.25 |
| `SWE1-FOTA-381` | Differential Update Technology Support | Service | SYS-RA-FOTA-325 | **?** | 0.20 |
| `SWE1-FOTA-382` | Pre-Update and post-update Differential Compatibilit | Service | SYS-RA-FOTA-331 | **?** | 0.14 |
| `SWE1-FOTA-383` | Deployed Software Validation | Service | SYS-RA-FOTA-333 | **?** | 0.20 |

**跨章測度**：命中 10 列 / 未達門檻 `?` 60 列；**相異候選章 6 個** —— {'4.8.3': 2, '4.10.5': 1, '4.10.5.1': 1, '4.10.2': 4, '4.5.4': 1, '4.9.1': 1}

### 2.1 判讀

**10 個命中列無一指向 4.8.2（其 Heading 之對應章）**，而分布於
**6 個不同章**：`4.10.2`（5 列）、`4.8.3`（2）、`4.10.5`、`4.10.5.1`、
`4.5.4`、`4.9.1` 各 1。

其中 **`SWE1-FOTA-351 Server-Initiated Session Flow` → `4.10.2` 分數 1.00**
（詞集完全重疊）。

**§3.1(a) 之假設「該 Heading 之標題不描述其所轄之全部區間」——
在可比之 10 列上成立**。60 列未達門檻，**其歸屬本量測答不出來**。

---

## 3. T19b —— `291`（16 列）與 `259`（3 列）：**證據仍不足**

### T19b-1 —— `SWE1-FOTA-291` Bearer selection:

所轄 in-scope 列 **16** 筆（id 區間 292–308）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-292` | Configurable Network Priority Support | Service | SYS-RA-FOTA-384 | **?** | 0.20 |
| `SWE1-FOTA-293` | DDF Update Type Processing | Service | SYS-RA-FOTA-380 | **?** | 0.20 |
| `SWE1-FOTA-294` | DDF Silent Update Processing | Service | SYS-RA-FOTA-372 | **?** | 0.20 |
| `SWE1-FOTA-295` | Silent Install Command Processing | Service | SYS-RA-FOTA-364 | **?** | 0.20 |
| `SWE1-FOTA-297` | Digital Signature and Transport Security Verificatio | Service | SYS-RA-FOTA-352 | **?** | 0.20 |
| `SWE1-FOTA-298` | Proprietary Communication Protocol Support | Service | SYS-RA-FOTA-351 | **?** | 0.20 |
| `SWE1-FOTA-299` | SWMC Security Requirement Compliance | Service | SYS-RA-FOTA-350 | **?** | 0.33 |
| `SWE1-FOTA-300` | TLS 1.2 Server Authentication Support | Service | SYS-RA-FOTA-349 | **?** | 0.20 |
| `SWE1-FOTA-301` | Server Authentication During Session Initiation | Service | SYS-RA-FOTA-348 | **?** | 0.29 |
| `SWE1-FOTA-302` | SWMC Authentication Information Support | Service | SYS-RA-FOTA-347 | **?** | 0.20 |
| `SWE1-FOTA-303` | Vehicle Information for Server Authentication | Service | SYS-RA-FOTA-346 | **?** | 0.17 |
| `SWE1-FOTA-304` | Authenticated Message Processing | Service | SYS-RA-FOTA-345 | **?** | 0.00 |
| `SWE1-FOTA-305` | Authorized Server Communication | Service | SYS-RA-FOTA-344 | **?** | 0.25 |
| `SWE1-FOTA-306` | Secure Communication Port Management | Service | SYS-RA-FOTA-343 | **?** | 0.20 |
| `SWE1-FOTA-307` | Application Layer Authentication Support | Service | SYS-RA-FOTA-342 | **?** | 0.20 |
| `SWE1-FOTA-308` | OMA-DM Security Compliance | Service | SYS-RA-FOTA-341 | 4.8.2 OMA-DM Security | 0.67 |

**跨章測度**：命中 1 列 / 未達門檻 `?` 15 列；**相異候選章 1 個** —— {'4.8.2': 1}

### T19b-2 —— `SWE1-FOTA-259` Vehicle Properties

所轄 in-scope 列 **3** 筆（id 區間 260–262）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-260` | OMA-DM Protocol Communication Support | — | SYS-RA-FOTA-476 | **?** | 0.33 |
| `SWE1-FOTA-261` | Download Descriptor Processing Support | Service | SYS-RA-FOTA-477 | **?** | 0.33 |
| `SWE1-FOTA-262` | Vehicle Property Access through Vehicle Integration  | Service | SYS-RA-FOTA-479 | **?** | 0.12 |

**跨章測度**：命中 0 列 / 未達門檻 `?` 3 列；**相異候選章 0 個** —— 無

### 3.1 判讀

- **`291 Bearer selection:`**：16 列中 **15 列 `?`**，唯一命中者指向
  **`4.8.2`** —— 而 §3.2 之候選為 `4.5 Interface Definitions`／`4.6`。
  **1/16 之單點命中不足以定對應**，且其指向與候選不符。
  **維持不判定為正確**（IN §8.4.1）。
- **`259 Vehicle Properties`**：3 列**全部 `?`**。
  **零證據。維持不判定為正確。**

---

## 4. T19c —— `214`（36 列）與 `137`（26 列）

### T19c-1 —— `SWE1-FOTA-214` HU FOTA with TBM

所轄 in-scope 列 **36** 筆（id 區間 215–250）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-215` | Trigger TBM Update Check on Scheduled Event | Service | SYS-RA-FOTA-505 | **?** | 0.14 |
| `SWE1-FOTA-216` | Trigger Server Update Check on HUReflash Availabilit | Service | SYS-RA-FOTA-506/SYS-RA-FOT | **?** | 0.12 |
| `SWE1-FOTA-217` | Prioritize FOTA Updates Based on Defined Update Type | Service | SYS-RA-FOTA-518 | **?** | 0.18 |
| `SWE1-FOTA-218` | Maintain FMVSS 111 Rear Visibility Compliance During | HMI | SYS-RA-FOTA-519 | **?** | 0.11 |
| `SWE1-FOTA-219` | Preserve Backup Camera Availability During Update Re | HMI | SYS-RA-FOTA-520 | **?** | 0.12 |
| `SWE1-FOTA-220` | Prevent Backup Camera Feed Interruption During Refla | HMI | SYS-RA-FOTA-522 | **?** | 0.12 |
| `SWE1-FOTA-221` | Validate Software Version Compatibility with MCPU Ha | Service | SYS-RA-FOTA-523 | **?** | 0.11 |
| `SWE1-FOTA-222` | Prioritize Software Update Over Map Update | Service | SYS-RA-FOTA-524 | **?** | 0.25 |
| `SWE1-FOTA-223` | Suspend Update HMI While Reverse Camera Is Active | Service | SYS-RA-FOTA-525 | **?** | 0.12 |
| `SWE1-FOTA-224` | Suspend Update HMI While Reverse Camera Is Active | HMI | SYS-RA-FOTA-526 | **?** | 0.12 |
| `SWE1-FOTA-225` | Suppress Forced Update HMI on No FOTA Event | Service | SYS-RA-VF747_V2-1348 | **?** | 0.14 |
| `SWE1-FOTA-226` | Display Stored FOTA Cancellation Reason on Next Igni | HMI | SYS-RA-VF747_V2-1067 | **?** | 0.12 |
| `SWE1-FOTA-227` | Force User to Schedule Update When Delay Is Prohibit | HMI | SYS-RA-VF747_V2-1061 | **?** | 0.12 |
| `SWE1-FOTA-228` | Use FOTA_Status from SGW as Master HMI Trigger Signa | Service | SYS-RA-VF747_V2-1066 | **?** | 0.10 |
| `SWE1-FOTA-229` | Process ROV HMI Information from Ethernet Message | HMI | SYS-RA-FOTA-113 | **?** | 0.11 |
| `SWE1-FOTA-230` | Prompt User for Accept Delay or Schedule Decision | HMI | SYS-RA-VF747_V2-1062 | **?** | 0.12 |
| `SWE1-FOTA-231` | Display What’s New Popup on User Selection | HMI | SYS-RA-FOTA-105 | **?** | 0.12 |
| `SWE1-FOTA-232` | Populate Installation Progress Popup Using SGW Statu | HMI | SYS-RA-FOTA-112 | **?** | 0.25 |
| `SWE1-FOTA-233` | Display Estimated Time for TBM Software Update | HMI | SYS-RA-FOTA-147 | **?** | 0.14 |
| `SWE1-FOTA-234` | Receive TBM Update Metadata from GSDP | Service | SYS-RA-FOTA-150 | **?** | 0.14 |
| `SWE1-FOTA-235` | Receive MQTT FOTA Topic Data from SWMC | Service | SYS-RA-FOTA-151 | **?** | 0.12 |
| `SWE1-FOTA-236` | Display What's New Pop-up for ROV Forced Update | HMI | SYS-RA-FOTA-121 | **?** | 0.12 |
| `SWE1-FOTA-237` | Populate Installation Progress Popup Using SGW Statu | HMI | SYS-RA-FOTA-112 | **?** | 0.25 |
| `SWE1-FOTA-238` | Display “Conditions Not Met” Pop-up with Cached Canc | HMI | SYS-RA-FOTA-119 | **?** | 0.10 |
| `SWE1-FOTA-239` | Set Install Acceptance to “Accepted” on User Approva | HMI | SYS-RA-VF747_V2-1064 | **?** | 0.12 |
| `SWE1-FOTA-240` | Set Install Acceptance to “Nothing to Report” on No  | HMI | SYS-RA-VF747_V2-1063 | **?** | 0.12 |
| `SWE1-FOTA-241` | Maintain Boolean TBM Update Type Indicators for Next | Service | SYS-RA-VF747_V6-175 | **?** | 0.10 |
| `SWE1-FOTA-242` | Visualize TBM Update Pop-up via Visual Instructions | HMI | SYS-RA-VF747_V6-183 | **?** | 0.12 |
| `SWE1-FOTA-243` | Visualize Forced Update Pop-up via Visual Instructio | HMI | SYS-RA-VF747_V6-184 | **?** | 0.12 |
| `SWE1-FOTA-244` | Align FOTA HMI Implementation with Defined HMI Logic | HMI | SYS-RA-FOTA-218 | **?** | 0.12 |
| `SWE1-FOTA-245` | Display Phase-Based HMI During Download Lifecycle | HMI | SYS-RA-FOTA-222 | **?** | 0.12 |
| `SWE1-FOTA-246` | Restrict Installation When Battery SOC Is Below Thre | Service | SYS-RA-FOTA-246 | **?** | 0.14 |
| `SWE1-FOTA-247` | Automatically Start Server-Initiated Update Session  | Service | SYS-RA-FOTA-292 | **?** | 0.33 |
| `SWE1-FOTA-248` | Receive Server-Initiated Session Trigger Through TC  | Service | SYS-RA-FOTA-294 | 4.10.2 Server-Initiated Session F | 0.38 |
| `SWE1-FOTA-249` | Verify Deployment Package Integrity Before Installat | Service | SYS-RA-FOTA-334 | **?** | 0.29 |
| `SWE1-FOTA-250` | Trigger Vehicle Initiated Session on ECU Configurati | Service | SYS-RA-FOTA-421 | 4.10.3 Vehicle-Initiated Session  | 0.38 |

**跨章測度**：命中 2 列 / 未達門檻 `?` 34 列；**相異候選章 2 個** —— {'4.10.2': 1, '4.10.3': 1}

### T19c-2 —— `SWE1-FOTA-137` Deployment flow

所轄 in-scope 列 **26** 筆（id 區間 138–167）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-138` | Extract Deployment Package and Route Component Packa | Service | SYS-RA-FOTA-231 | **?** | 0.29 |
| `SWE1-FOTA-139` | Collect Installer Status and Report ECU Failure Code | Service | SYS-RA-FOTA-232 | **?** | 0.12 |
| `SWE1-FOTA-140` | Determine Installation Start Time After Download | HMI | SYS-RA-FOTA-234 | **?** | 0.29 |
| `SWE1-FOTA-141` | Display Update Message and Reconfirm Package Before  | Service | SYS-RA-FOTA-239 | **?** | 0.14 |
| `SWE1-FOTA-142` | Execute Background Download Without Customer Visibil | Service | SYS-RA-FOTA-242 | **?** | 0.14 |
| `SWE1-FOTA-143` | Continue Download During IGN OFF Extended Wake Perio | Service | SYS-RA-FOTA-243 | **?** | 0.11 |
| `SWE1-FOTA-144` | Execute Extended-Time Download Without Visible Vehic | Service | SYS-RA-FOTA-244 | **?** | 0.11 |
| `SWE1-FOTA-145` | Block Installation When Battery State of Charge Is B | Service | SYS-RA-FOTA-245 | **?** | 0.12 |
| `SWE1-FOTA-146` | Block Installation When IBS_SOC Accuracy Is Invalid | Service | SYS-RA-FOTA-247 | **?** | 0.14 |
| `SWE1-FOTA-147` | Start Installation Only in IGN_OFF Power Mode | Service | SYS-RA-FOTA-250 | **?** | 0.14 |
| `SWE1-FOTA-148` | Display Estimated Installation Time in Popup PU0304 | HMI | SYS-RA-FOTA-251 | **?** | 0.17 |
| `SWE1-FOTA-149` | Dismiss Installation Popup on IGN_RUN or Timed Mode  | Service | SYS-RA-FOTA-252 | **?** | 0.12 |
| `SWE1-FOTA-150` | Enter Forced Update Lock State After Popup Dismissal | HMI | SYS-RA-FOTA-253 | **?** | 0.11 |
| `SWE1-FOTA-151` | Block Installation During Active Download Session | Service | SYS-RA-FOTA-254 | **?** | 0.29 |
| `SWE1-FOTA-152` | Execute Scheduled Installation Based on Precondition | Service | SYS-RA-FOTA-255 | **?** | 0.20 |
| `SWE1-FOTA-153` | Display What's New Details from Deployment Package | HMI | SYS-RA-FOTA-256 | **?** | 0.25 |
| `SWE1-FOTA-154` | Display Conditions Not Met With Specific Cancellatio | HMI | SYS-RA-FOTA-257 | **?** | 0.11 |
| `SWE1-FOTA-155` | Display Cancellation Reason Based on Hybrid Type Dur | HMI | SYS-RA-FOTA-258 | **?** | 0.10 |
| `SWE1-FOTA-156` | Keep Display ON During Installation | HMI | SYS-RA-FOTA-259 | **?** | 0.25 |
| `SWE1-FOTA-157` | Retry Installation Once After Failure | Service | SYS-RA-FOTA-260 | **?** | 0.20 |
| `SWE1-FOTA-160` | Ensure eCall Functionality During Download and Post- | Service | SYS-RA-FOTA-263 | **?** | 0.29 |
| `SWE1-FOTA-161` | Warn User Not to Drive During Installation | HMI | SYS-RA-FOTA-264 | **?** | 0.17 |
| `SWE1-FOTA-162` | Enable User-Initiated Retry After Installation Failu | Service | SYS-RA-FOTA-265 | **?** | 0.25 |
| `SWE1-FOTA-163` | Continue Installation When Vehicle Starts Moving | Service | SYS-RA-FOTA-266 | **?** | 0.17 |
| `SWE1-FOTA-165` | Post Installation Power Mode Handling | Service | SYS-RA-FOTA-269 | 9.3 Post-Installation | 0.40 |
| `SWE1-FOTA-167` | Handle Installation Failure and Unrecoverable State  | HMI | SYS-RA-FOTA-271 | **?** | 0.20 |

**跨章測度**：命中 1 列 / 未達門檻 `?` 25 列；**相異候選章 1 個** —— {'9.3': 1}

### 4.1 判讀

- **`214 HU FOTA with TBM`**：36 列僅 2 列命中，指向 `4.10.2`／`4.10.3`
  —— **非其 Heading 之 `4.2.3`**。跨章之嫌**存在但證據薄**（2/36）。
- **`137 Deployment flow`**：26 列僅 1 列命中（`9.3 Post-Installation`）
  —— 同樣非其 Heading 之 `4.10.5`。**1/26，證據更薄。**

**二群皆未能確認「未同樣跨章」** —— 下放包 §四 T19c 之目的
（「須確認其未同樣跨章」）**本量測達不到**：
它只能顯示「有跨章跡象」，不能顯示「沒有」。

---

## 5. T19e —— `178`（6 列）：**分析層之判定無法由本量測複核**

### T19e —— `SWE1-FOTA-178` For a silent update, the OTA client follows these steps for the download

所轄 in-scope 列 **6** 筆（id 區間 179–184）

| id | Requirement Title | Sub Cat | Source Requirement ID | 最佳 CFTS 候選 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-179` | Start Silent Update Download Automatically | Service | SYS-RA-FOTA-366 | **?** | 0.17 |
| `SWE1-FOTA-180` | Optionally Suppress Download Confirmation Screen | Service | SYS-RA-FOTA-367 | **?** | 0.17 |
| `SWE1-FOTA-181` | Start Silent Update Installation Immediately After D | Service | SYS-RA-FOTA-368 | **?** | 0.25 |
| `SWE1-FOTA-182` | Optionally Suppress Deployment Confirmation Screen | Service | SYS-RA-FOTA-369 | **?** | 0.17 |
| `SWE1-FOTA-183` | Display Silent Update Completion and What's New Deta | HMI | SYS-RA-FOTA-370 | **?** | 0.12 |
| `SWE1-FOTA-184` | Apply Silent Update to All Session Flows | Service | SYS-RA-FOTA-371 | **?** | 0.33 |

**跨章測度**：命中 0 列 / 未達門檻 `?` 6 列；**相異候選章 0 個** —— 無

### 5.1 判讀

**6 列全部 `?`。**

下放包 §3.2 稱「178 之判定為分析層對自身可見證據所作，
**仍須 T19 之列標題複核**」——**該複核無法完成**：
6 列之標題與 87 個 CFTS 章節名之詞集重疊皆未達門檻。

**本量測既不支持也不反對 `178 → 4.7.3.2 Silent Updates`。**
其判定之依據仍只有分析層 §3.2 所述之一項（037 標題為 CFTS 該節之內文引導句）。

---

## 6. T19d —— 全 311 列之逐列對照（本輪最關鍵之產出）

## T19d —— 全 311 列之 CFTS 逐列對照

**母體**：311 列（應 311）—— 閉合 ✅

| 量 | 列數 |
|---|---:|
| 列之最佳候選未達門檻（`?`）| 286 |
| 其 Heading 之候選未達門檻（無可比對象）| 1 |
| **可比且不一致** | **23** |
| 可比且一致 | 1 |

**閉合**：286 + 1 + 23 + 1 = 311 ✅

### 不一致列清單（本輪最關鍵之產出）

| Heading id | Heading 之候選章 | 列 id | 列標題 | 列之候選章 | 分 |
|---|---|---|---|---|---:|
| `SWE1-FOTA-009` | 4.7.3.1 | `SWE1-FOTA-010` | Fallback to TBM Network for FOTA Download | 4.2.3 HU FOTA with TBM | 0.40 |
| `SWE1-FOTA-009` | 4.7.3.1 | `SWE1-FOTA-011` | User Navigation to Wi-Fi Software Download | 4.6.3 Software Download via Wi-F | 0.40 |
| `SWE1-FOTA-038` | 4.6 | `SWE1-FOTA-047` | Store Wi-Fi Network Credentials for Future C | 4.6.1 Connection to Wi-Fi networ | 0.40 |
| `SWE1-FOTA-058` | 4.6.1 | `SWE1-FOTA-060` | Wi-Fi Network Selection for OTA Download | 4.6 OTA download via Wi-Fi | 0.40 |
| `SWE1-FOTA-110` | 5 | `SWE1-FOTA-123` | Clear TBM FOTA UI on No Updates Available | 4.2.3 HU FOTA with TBM | 0.40 |
| `SWE1-FOTA-110` | 5 | `SWE1-FOTA-124` | Clear TBM FOTA UI on No Update State | 4.2.3 HU FOTA with TBM | 0.40 |
| `SWE1-FOTA-129` | 4.11 | `SWE1-FOTA-134` | Display Post-Download Installation Options | 9.3 Post-Installation | 0.40 |
| `SWE1-FOTA-137` | 4.10.5 | `SWE1-FOTA-165` | Post Installation Power Mode Handling | 9.3 Post-Installation | 0.40 |
| `SWE1-FOTA-214` | 4.2.3 | `SWE1-FOTA-248` | Receive Server-Initiated Session Trigger Thr | 4.10.2 Server-Initiated Session F | 0.38 |
| `SWE1-FOTA-214` | 4.2.3 | `SWE1-FOTA-250` | Trigger Vehicle Initiated Session on ECU Con | 4.10.3 Vehicle-Initiated Session  | 0.38 |
| `SWE1-FOTA-251` | 4.3 | `SWE1-FOTA-258` | Update Agent Bootloader Integration | 4.9.1 Update Agent Requirements | 0.50 |
| `SWE1-FOTA-271` | 4.5.4 | `SWE1-FOTA-274` | OTA Communication / Vehicle-Initiated Sessio | 4.10.3 Vehicle-Initiated Session  | 0.50 |
| `SWE1-FOTA-271` | 4.5.4 | `SWE1-FOTA-277` | Server-Initiated Session Event Interface | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-312` | Deployment Package Integrity Verification | 4.8.3 Deployment Package Securit | 0.40 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-337` | Deployment Flow Initiation | 4.10.5 Deployment Flow | 0.67 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-340` | Configurable Installation Conditions | 4.10.5.1 Installation and Download  | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-351` | Server-Initiated Session Flow | 4.10.2 Server-Initiated Session F | 1.00 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-356` | Deployment Package Notification | 4.8.3 Deployment Package Securit | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-361` | Server-Initiated OTA Background Execution | 4.5.4 OTA server initiated sessi | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-365` | Server-Initiated Session Handling from TC | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-367` | Server-Initiated Session Forwarding from TC | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-369` | Server-Initiated Flow Alignment with Vehicle | 4.10.2 Server-Initiated Session F | 0.50 |
| `SWE1-FOTA-309` | 4.8.2 | `SWE1-FOTA-376` | Update Agent Self-Update Capability | 4.9.1 Update Agent Requirements | 0.50 |

**不一致之 Heading 分布**（10 個 Heading）：
- `SWE1-FOTA-309` OMA-DM Security —— **10** 列
- `SWE1-FOTA-009` Critical Updates —— **2** 列
- `SWE1-FOTA-110` TBM FOTA Reflash —— **2** 列
- `SWE1-FOTA-214` HU FOTA with TBM —— **2** 列
- `SWE1-FOTA-271` OTA server initiated sessions —— **2** 列
- `SWE1-FOTA-038` OTA download via Wi-Fi —— **1** 列
- `SWE1-FOTA-058` Connection to Wi-Fi network —— **1** 列
- `SWE1-FOTA-129` User Experience (UX)/HMI —— **1** 列
- `SWE1-FOTA-137` Deployment flow —— **1** 列
- `SWE1-FOTA-251` High Level FOTA Diagram —— **1** 列

> 分數為詞集重疊比（Jaccard，停用詞表 13 字、門檻 0.34），
> **與 T18d 共用同一支函式**。`?` 只表示自動比對不達門檻，
> 不表示無對應。**本表為量測，不是對應之結論。**

### 6.1 判讀

**23 筆不一致集中於 10 個 Heading**，其中 `SWE1-FOTA-309` 獨佔 10 筆。

**另有二筆值得單獨看**：
- **`SWE1-FOTA-110 TBM FOTA Reflash` 之 Heading 候選章為 `5`** ——
  單一數字之章號，其標題與 `TBM FOTA Reflash` 之重疊達門檻純屬巧合之嫌高。
  **該 Heading 之對應本身可疑**，而 §三草案將其 50 列全數歸入第 7 群
  `TBM Update`。
- **`SWE1-FOTA-251 High Level FOTA Diagram`（Heading 候選 `4.3`）之
  `SWE1-FOTA-258 Update Agent Bootloader Integration` → `4.9.1` 分 0.50**
  —— 第 5 群 `Client Architecture` 之異質性（§3.1(b)）之一個具體例。

---

## 7. 未結 DR

**0 筆。** `DATA_REQUESTS.md` 之表列為「本輪 0 筆」，
Q5 裁定不發 DR，本輪執行後維持。**本輪未新增任何外部引用。**

---

## 8. 獨立自評

1. **我照參數拘束做了，而結果顯示該拘束下的工具答不出下放包的問題。**
   §四之三個目的（測定 309 橫跨幾章／確認 214、137 未跨章／複核 178），
   **只有第一個得到部分答案**（10/70 可比）。
   第二個**結構上答不到**（本工具不能證明「沒有跨章」），
   第三個**完全答不到**（6 列全 `?`）。
   **這是工具之限制，不是量測之失敗** —— 但若我只交表不說這件事，
   讀表的人會以為 `?` 是「無對應」。

2. **`?` 之語意在 T19 比在 T18d 更容易被誤讀。**
   T18d 之 `?` 佔 3/45，是少數；T19 之 `?` 佔 286/311，是**絕大多數**。
   同一個記號，在後者幾乎等於「本表沒有結論」。已於各節逐一標明。

3. **重構之風險我先擋掉了**：把 `STOP`／`toks`／`best`／`THRESHOLD`
   提到模組層供 T18d 與 T19 共用（否則「參數一致」只是規定），
   **並以 byte-level diff 證明 T18d 之輸出未變**
   （SHA `ba83f3a7e28f57a5…`，重構前後相同）。
   下放包 §四要求「加項次，不改既有項之行為」——**已證明，非聲稱**。

4. **我沒有改門檻、沒有改停用詞、沒有改用語意比對。**
   §0 之低命中率是誘因很強的改參數理由 —— 但改了就不再是 T18d 之同一把尺，
   而下放包 §1.1 之整個論證（字面比對之偏差方向可預期）就失去依據。

---

## 9. 量測條件揭露（R-G8）

### 詞集參數與 T18d 之逐項對照

| 參數 | T18d | T19 | 一致 |
|---|---|---|---|
| 停用詞表 | 13 字（`the a of and for to in on is shall with requirements requirement`）| **同一個 `STOP` 常數** | ✅ |
| 門檻 | 0.34 | **同一個 `THRESHOLD` 常數** | ✅ |
| 正規化 | `norm()`：小寫、非英數轉空白 | 同一支 | ✅ |
| 詞長下限 | > 2 字元 | 同一支 `toks()` | ✅ |
| 相似度 | Jaccard（交集／聯集）| 同一支 `best()` | ✅ |

**一致性由「共用同一支函式」保證，非由二處各寫一份而聲稱一致。**

### 比對之標的

- T18d：**Heading 標題** × 87 個 CFTS 章節標題
- T19：**每列之 `Requirement Title`** × 同一批 87 個 CFTS 章節標題

**CFTS 側之母體完全相同**（87 章，閉合檢查 487 需求物件 ✅）。

### 本輪未做者

- **未讀任何列之 `Description`** —— T19 只用 `Requirement Title`
  （下放包 §四所指定之欄位）。若標題不足以定位而描述可以，本量測看不到。
- **未對 SYS1 做逐列對照** —— R-SU11(b) 已裁其接點為 HMI 87 列，
  且下放包 §四未要求。
- **未驗證 CFTS 章節標題本身之品質** —— 若某章標題過短或過泛，
  其與任何列之重疊皆低，該章在本表中永不出現。**未量測此效應。**

### 閉合

- T19d 母體 311 ✅（＝ R-SU3 之驗證母體）
- 四類計數之和 = 311 ✅
- T18c 之 CFTS 章節 87、需求物件 487 ✅（本輪重跑，與上繳包 04 相同）
