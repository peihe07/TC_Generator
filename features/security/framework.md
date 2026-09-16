# FW036 Security — framework（Layer 1–3）

規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、FO §0（Tier 2：Test Set derivation 屬 Pei 簽核）。
本檔依 **R-SEC10** 鎖定；Test Set 名稱逐字取下放包 `SEC-01 §5` 之案 A 表，**未改任何名稱**。

**LOCKED 2026-09-16 (R-SEC10)**

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

## Part II — Layer 2（Test Set，寫入工作簿）—— 30 組，全定稿

`leaf` 自 `features/security/data/layer2_assign.tsv` 回填；`batch` 自 `batch_order.tsv`；
`D` 為 **R-SEC11(b)** 之 DEFERRED（不產 TC，計入 leaf 但不計入產出群）。

| # | Test Group | Test Set | leaf | batch 1 | batch 2 | D | 產出 |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | Cert Provider | `Chain Verification` | 1 | 1 | 0 | 0 | 1 |
| 2 | Cert Provider | `Field Matching` | 3 | 3 | 0 | 0 | 3 |
| 3 | Cert Provider | `Revocation` | 2 | 2 | 0 | 0 | 2 |
| 4 | Cert Provider | `(非功能)` | 2 | 2 | 0 | 0 | 2 |
| 5 | Cert Provider | `Trust Store` | 2 | 2 | 0 | 0 | 2 |
| 6 | Cert Provider | `Client Interface` | 1 | 1 | 0 | 0 | 1 |
| 7 | Key Install | `Temporary Key` | 1 | 1 | 0 | 0 | 1 |
| 8 | Key Install | `Installation` | 4 | 4 | 0 | 0 | 4 |
| 9 | Key Install | `Overwrite Protection` | 1 | 1 | 0 | 0 | 1 |
| 10 | Key Install | `Install State` | 2 | 2 | 0 | 0 | 2 |
| 11 | Key Install | `Persistence` | 1 | 1 | 0 | 0 | 1 |
| 12 | Key Install | `Crypto Service` | 2 | 2 | 0 | 0 | 2 |
| 13 | Key Install | `(非功能)` | 2 | 2 | 0 | 0 | 2 |
| 14 | SAM | `(環境)` | 4 | 3 | 1 | 2 | 2 |
| 15 | SAM | `AuthData Reception` | 1 | 0 | 1 | 0 | 1 |
| 16 | SAM | `Error Handling` | 1 | 1 | 0 | 0 | 1 |
| 17 | SAM | `AuthData Verification` | 5 | 1 | 4 | 0 | 5 |
| 18 | SAM | `Installation` | 3 | 1 | 2 | 0 | 3 |
| 19 | SAM | `Target Notification` | 5 | 1 | 4 | 0 | 5 |
| 20 | ECU Cert | `Verification` | 3 | 3 | 0 | 1 | 2 |
| 21 | ECU Cert | `Diagnostic Access` | 2 | 2 | 0 | 0 | 2 |
| 22 | ECU Cert | `(IPC／JNI／IO)` | 4 | 4 | 0 | 4 | 0 |
| 23 | ECU Cert | `Certificate Lifecycle` | 4 | 4 | 0 | 1 | 3 |
| 24 | SWDL Secure Lib | `(總則)` | 1 | 1 | 0 | 1 | 0 |
| 25 | SWDL Secure Lib | `Key Retrieval` | 2 | 2 | 0 | 2 | 0 |
| 26 | SWDL Secure Lib | `Package Decryption` | 1 | 1 | 0 | 0 | 1 |
| 27 | SWDL Secure Lib | `Signature Verification` | 1 | 1 | 0 | 0 | 1 |
| 28 | Log Encrypt | `(其餘)` | 8 | 0 | 8 | 8 | 0 |
| 29 | Log Encrypt | `Encryption Procedure` | 1 | 0 | 1 | 0 | 1 |
| **合計** | **6 群** | **30 組** | **70** | **49** | **21** | **19** | **51** |

> **R-SEC10(b) 之占號**：同組內 batch 1 先占號、batch 2 接續，**不得交錯**。
> D 群不占號（解凍時自該組末號續編）。

## Part III — Layer 3

**不入工作簿**（IN §4.1.5）。依 **R-SEC10(e)**：Layer 3 = **SYSAD ID**
（SWE1 `Source Requirement ID` 之首值），同時是 SYS3 章節單位與 SYS2 對應單位。

## Part IV — 鎖定狀態

| 項 | 值 | 權威 |
|---|---|---|
| Layer 1 | **定稿**（案 A，六 Test Group）| R-SEC10(a) |
| Layer 2 | **定稿**（30 組，無 provisional 列）| R-SEC10(a)；SEC-01 §5 逐字 |
| Layer 3 | **定稿**（SYSAD ID，不入簿）| R-SEC10(e) |
| `spec_mode` | **`F`**（037-SWRA 母體）| R-SEC10(d) |
| Vehicle Model | 五有效車型 `1`、598／5210 `0`，70 列一律相同 | R-SEC10(f) |
| 產出群／D 群 | **51 ／ 19** | R-SEC11(c) |

**LOCKED 2026-09-16 (R-SEC10)** —— 此後之變更一律走 R-G72 Revise。

