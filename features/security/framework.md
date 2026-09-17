# FW036 Security — framework（Layer 1–3）

規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、FO §0（Tier 2：Test Set derivation 屬 Pei 簽核）。
本檔依 **R-SEC10** 鎖定；Test Set 名稱逐字取下放包 `SEC-01 §5` 之案 A 表，**未改任何名稱**。

**LOCKED 2026-09-16 (R-SEC10)** → **LOCKED v02 (R-SEC17)** → **LOCKED v03 2026-09-16 (R-SEC17 Revise)**

---

## Part I — Layer 1（Test Group）

依 **R-SEC10(a)**：一本 workbook，六個 Test Group（＝元件名）。

| # | Test Group | ABBR（TC ID `NR1L-{ABBR}-{nnn}`，R-SEC10(b)）| 037 母體 | 列 |
|---:|---|---|---|---:|
| 1 | `Cert Provider` | `CP` | `SWE1-CertProvider-SWE1R1-V1.0` | 11 |
| 2 | `Key Install` | `KI` | `SWE1-KeyInstall-SWE1R1-V1.0` | 13 |
| 3 | `SAM` | `SAM` | `SWE1-SAM-SWE1R1-V1.1` | 19 |
| 4 | `ECU Cert` | `ECUC` | `SWE1_ECUCert_FM-WI-FSM-037-A03` | 13 |
| 5 | `SWDL Secure Lib` | `SWDL` | `SWE1_SwdlSecureLib_FM-WI-FSM-037-A03` | 5 |
| 6 | `Log Encrypt` | `LOGENC` | `SWE1_libLogEncrypt_FM-WI-FSM-037-A03` | 9 |

## Part II — Layer 2（Test Set，寫入工作簿）—— **29 組**，全定稿

`leaf` 自 `features/security/data/layer2_assign.tsv` 回填；`batch` 自 `batch_order.tsv`；
`D` 為 **R-SEC11(b)** 之 DEFERRED（不產 TC，計入 leaf 但不計入產出群）。

| # | Test Group | Test Set | leaf | batch 1 | batch 2 | D | 產出 |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | Cert Provider | `Chain Verification` | 1 | 1 | 0 | 0 | 1 |
| 2 | Cert Provider | `Field Matching` | 3 | 3 | 0 | 0 | 3 |
| 3 | Cert Provider | `Revocation` | 2 | 2 | 0 | 0 | 2 |
| 4 | Cert Provider | `Service Robustness` | 2 | 2 | 0 | 0 | 2 |
| 5 | Cert Provider | `Trust Store` | 2 | 2 | 0 | 0 | 2 |
| 6 | Cert Provider | `Client Interface` | 1 | 1 | 0 | 0 | 1 |
| 7 | Key Install | `Temporary Key` | 1 | 1 | 0 | 0 | 1 |
| 8 | Key Install | `Installation` | 4 | 4 | 0 | 0 | 4 |
| 9 | Key Install | `Overwrite Protection` | 1 | 1 | 0 | 0 | 1 |
| 10 | Key Install | `Install State` | 2 | 2 | 0 | 0 | 2 |
| 11 | Key Install | `Persistence` | 1 | 1 | 0 | 0 | 1 |
| 12 | Key Install | `Crypto Service` | 2 | 2 | 0 | 0 | 2 |
| 13 | Key Install | `Platform Compliance` | 2 | 2 | 0 | 0 | 2 |
| 14 | SAM | `Service Environment` | 4 | 3 | 1 | 2 | 2 |
| 15 | SAM | `AuthData Reception` | 1 | 0 | 1 | 0 | 1 |
| 16 | SAM | `Error Handling` | 1 | 1 | 0 | 0 | 1 |
| 17 | SAM | `AuthData Verification` | 5 | 1 | 4 | 0 | 5 |
| 18 | SAM | `Installation` | 3 | 1 | 2 | 0 | 3 |
| 19 | SAM | `Target Notification` | 5 | 1 | 4 | 0 | 5 |
| 20 | ECU Cert | `Verification` | 3 | 3 | 0 | 1 | 2 |
| 21 | ECU Cert | `Diagnostic Access` | 2 | 2 | 0 | 0 | 2 |
| 22 | ECU Cert | `Internal Interfaces` | 4 | 4 | 0 | 4 | 0 |
| 23 | ECU Cert | `Certificate Lifecycle` | 4 | 4 | 0 | 1 | 3 |
| 24 | SWDL Secure Lib | `Library Scope` | 1 | 1 | 0 | 1 | 0 |
| 25 | SWDL Secure Lib | `Key Retrieval` | 2 | 2 | 0 | 2 | 0 |
| 26 | SWDL Secure Lib | `Package Decryption` | 1 | 1 | 0 | 0 | 1 |
| 27 | SWDL Secure Lib | `Signature Verification` | 1 | 1 | 0 | 0 | 1 |
| 28 | Log Encrypt | `Encryption Services` | 8 | 0 | 8 | 8 | 0 |
| 29 | Log Encrypt | `Encryption Procedure` | 1 | 0 | 1 | 0 | 1 |
| **合計** | **6 群** | **29 組** | **70** | **49** | **21** | **19** | **51** |

> **R-SEC10(b) 之占號**：同組內 batch 1 先占號、batch 2 接續，**不得交錯**。
> D 群不占號（解凍時自該組末號續編）。

## Part III — Layer 3

**不入工作簿**（IN §4.1.5）。依 **R-SEC10(e)**：Layer 3 = **SYSAD ID**
（SWE1 `Source Requirement ID` 之首值），同時是 SYS3 章節單位與 SYS2 對應單位。

## Part IV — 鎖定狀態

| 項 | 值 | 權威 |
|---|---|---|
| Layer 1 | **定稿**（案 A，六 Test Group）| R-SEC10(a) |
| Layer 2 | **定稿**（**29 組**，無 provisional 列）| R-SEC10(a)；SEC-01 §5 逐字；v02 改六名（R-SEC17）|
| Layer 3 | **定稿**（SYSAD ID，不入簿）| R-SEC10(e) |
| `spec_mode` | **`F`**（037-SWRA 母體）| R-SEC10(d) |
| Vehicle Model | 五有效車型 `1`、598／5210 `0`，70 列一律相同 | R-SEC10(f) |
| 產出群／D 群 | **51 ／ 19** | R-SEC11(c) |

**LOCKED 2026-09-16 (R-SEC10)** —— v01 之鎖定。

## REVISE v02 2026-09-16 (R-SEC17)

依 **R-G72** 解鎖一次，**僅改下列六個 Test Set 名稱**；其餘 23 組名稱、Layer 1、Layer 3 不動。

> **併同更正一項計數（執行層自報）**：Layer 2 之組數為 **29**，非先前各包所載之 30。
> 成因為 `build_layer2_assign.py` 之對帳訊息把組數**寫死為 30**，該字串經 SEC-02～SEC-04 之
> 上繳包與本檔 v01 沿用。逐組核對 SEC-01 §5 之表：Cert Provider 6／Key Install 7／SAM 6／
> ECU Cert 4／SWDL Secure Lib 4／Log Encrypt 2 = **29**。leaf 總數 70 與逐組 leaf 數**不受影響**。

成因（A-12，分析層）：SEC-01 §5 之 Layer 2 表以中文註記佔位未命名群，
SEC-02 §4 令「30 組逐字寫入」而未先命名，LOCKED 時把佔位鎖了進去 ——
違 IN §1（Test Set 英文）與 IN §4.2（不得 placeholder）。

| # | Test Group | old（v01 佔位）| **new（v02）** |
|---:|---|---|---|
| 1 | Cert Provider | `(非功能)` | **`Service Robustness`** |
| 2 | Key Install | `(非功能)` | **`Platform Compliance`** |
| 3 | SAM | `(環境)` | **`Service Environment`** |
| 4 | ECU Cert | `(IPC／JNI／IO)` | **`Internal Interfaces`** |
| 5 | SWDL Secure Lib | `(總則)` | **`Library Scope`** |
| 6 | Log Encrypt | `(其餘)` | **`Encryption Services`** |

Layer 2 名稱之 CJK 字元計數：**5 → 0**（六個名稱皆為能力層英文名，IN §4.2）。

> **執行層之一項回報（R-SEC17 指定之複核）**：`Service Environment` 所轄四列中，
> **`SWE1-SAM-0008`（Format of AuthData should follow SAM package definition）為資料格式需求，
> 非執行環境或部署前提**，與該 Test Set 之能力面不合。依條文回報，**不自行移組**。

**LOCKED v02 2026-09-16 (R-SEC17)** —— v02 之鎖定。

## REVISE v03 2026-09-16 (R-SEC17 Revise)

依 **R-G72** 解鎖一次，**只移一列**；Test Set 名稱、Layer 1、Layer 3 皆不動。

成因（A-17，分析層）：SEC-01 §5 之 `(環境)` 群把 `SWE1-SAM-0008` 誤放 ——
該列為 **AuthData 之資料格式**需求（manifest 檔名 `<SSN>_SAM_<SAMType>.json`、簽章、憑證），
非執行環境或部署前提。執行層於 SEC-05 §1-1 依 R-SEC17 之指定複核時回報，Pei 裁定移組。

| SWE1 | old Test Set | **new Test Set** | leaf 變動 |
|---|---|---|---|
| `SWE1-SAM-0008` | `Service Environment` | **`AuthData Verification`** | `Service Environment` 4 → **3**；`AuthData Verification` 5 → **6** |

**leaf 總數 70 不變**；Test Set 組數 **29 不變**。

**LOCKED v03 2026-09-16 (R-SEC17 Revise)** —— 此後之變更一律走 R-G72 Revise。



