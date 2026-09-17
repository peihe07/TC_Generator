# ANOMALIES — FW036 Security HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-SEnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

| 標記 | 狀態 | 事實（實測） | 影響 | 處置 |
|---|---|---|---|---|
| `[A-SE01]` | PENDING | `SWE1_ECUCert` 037 之 `SWE-Requirement ID`（A 欄）**13 列全空**，僅 `Source Requirement ID` 有 `SYSAD_SEC_ECUCERT_*` | 該 13 列無 RD ID | 依 **R-SEC3(b)** 暫以 `Source Requirement ID` 首值代入，Remarks 註 `SWE ID pending DR`；登 **DR-SEC-a** |
| `[A-SE02]` | PENDING | `SWE1-KeyInsyall-001~013` —— 原檔 `Install` 拼作 `Insyall`，13 列全數 | RD ID 逐字入簿即帶錯字 | 依 **R-SEC3(a)** 保留原字，Remarks 註 `RD ID spelling as delivered`；登 **DR-SEC-b** |
| `[A-SE03]` | PENDING | `SWE1-SAM-0017`（037 row 25）之 **`Verification Method` 欄空白** —— 六本 70 列中唯一 | 無法依 VM 分類；下放包 §1 表記 SAM「16 Testing」實為 15 ＋ 1 空 | 暫比照同群（SAM `Target Notification` 其餘四列皆 `Testing`）處理，**不自行填值**；登 **DR-SEC-j**，Pei 於 SEC-02 裁 |
| `[A-SE04]` | RESOLVED | `Source Requirement ID` 之分隔符三式並存（換行／逗號／空格），且 libLogEncrypt 另有 **ID 內含空格**（`SYSAD_SECURITY_ LOGENCRYPT_ENCRYPTION_COMP`）—— 純以空白切會把後者切碎 | 解析面 | `build_trace_matrix.py` 之 `split_source_ids()` 改切在每個 `SYSAD` 起點；切出片段再由 `norm()` 去空白。**70/70 exact 命中** |
| `[A-SE05]` | PENDING | `Secure Log CS.212` 在 `Mapping detail` 僅對 `SYS-RA-SEC-671`（`Reference only`），而六本 037 之鏈**皆不經 671** | 機械判準下 CS.212 無任何 SWE1 列落點；`SWE1-KeyInsyall-010`／`-012`、`SWE1-SAM-0004` 之 log 斷言接不上 CCVR | 不自行接線。CS.212 五情境之 package 待 **DR-SEC-h**；Pei 裁是否以 037 原文之 log 斷言另立落點 |
| `[A-SE06]` | PENDING | `Cert Val CS.98` STEPS 欄實測為 **E 欄**，下放包 §4 任務 3 規則 7 記為 D 欄 | 若逐字照 D 欄取值會取到 `DTC/NRC Results`（全空） | 實作改以**欄名定位**（`STEPS` 起首）而非欄索引；條文未改，登記備查 |
| `[A-SE07]` | PENDING | 下放包規則 7 之 apk 正則 `[a-z][A-Za-z]+Test[A-Za-z]*` **無左邊界**，會自 `CertProviderServiceManagerTest` 內部切出 `ertProviderServiceManagerTest` | 污染 `apk_method` 與 `step_assets` | 補左邊界 `(?<![A-Za-z])`，其餘逐字不動 |
| `[A-SE08]` | PENDING | 下放包 §4 任務 3 規則 3／4 之「style A ＝ CertProvider／KeyInstall；style B ＝ 其餘四本」**與實測不符** —— 六本**皆**有每元素一表（style A），四本**另**有 Table 11（style B） | 只照規則 4 會漏掉四本之元素表對應（含 `SYSAD_SAM_PACKAGE_INTF` 之介面表） | 實作兩式**並用取聯集**，`prov` 欄記其出處。差異見上繳包 §4-1～4-3 |

| `[A-SE09]` | PENDING | `_D` §1.1 記 F000 回應碼表為 `image249.png`；實測該圖掛在 `SYS-RA-CS00102-698`（**FF01**），F000 之圖為 `image247.png`。且 **xlsx 之 `xl/media/` 為 0 件**，全機查無同名檔 | 「解圖」任務不可執行 | 改自 `SYS2 System-HW` 欄之 RQMT 文字取得語意（byte 4 bit field），見 DATA_REQUESTS；DR-SEC-l 部分結案 |
| `[A-SE10]` | PENDING | `R1L_Diag_Software_Qualification_Test_Design.xlsx` **同名異體**：`Desktop/` 本 954,818 B sha `96a06f0d50d33c1b`（＝_C §1 所載）；`01_Project_R1L/.../M-CPU(Diag)/SW_test_design/` 本 1,012,479 B sha `29e12844bb52d2a6` | 取錯本即取到不同之 DID 值 | 以 `_C` §1 所載 sha 之 `Desktop/` 本為準，已登錄 |

| `[A-SE11]` | PENDING | CCVR `Auth-Prog CS.93` 之 r7 與 r8 **同稱「Flashing lower rollback id」而回值不同** —— r7 回 `0x71 01 F0 00 01`（已遞增版本後回刷舊版），r8 回 `0x71 01 F0 00 02`（未遞增版本後回刷舊版）| R-SEC8(i) 之「`02`（lower rollback id）」若不帶列號，同一敘述會對到兩個值 | 引用時一律連 `per CCVR Auth-Prog CS.93 evidence, row <n>` 標明（R-SEC8(i) 本已要求標 row，本項只是說明其必要性）|

| `[A-SE12]` | PENDING | SEC-01 審閱 三-1 之規則文字為「只計 **THEN**／`3.x`／`THEN.` 子句內之命中」，惟其所列 7 列含 `SWE1-CertProvider-005` —— 該列命中在 **WHEN**（`Monitor system logs during verification`），THEN 無命中 | 逐字照規則得 6 列，照所列集合得 7 列 | 取 **WHEN ∪ THEN** 以重現審閱指名之集合；**兩解不改 batch 總數**（005 本有 CS.98 落點）。請分析層於 SEC-02 明示 |

## 回饋 RD 之 ANOMALIES（`_D` §1.3，非裁定）

| 標記 | 事實（執行層複驗） | 影響 |
|---|---|---|
| `[A-SEC-1]` | CCVR `DID CS.102`／`Cyber DIDs R&P-CS.102` 之「`2951` Certificate Store UUID」**不見於 CS.00102**（731 個 SYS2 ID 全表現查，無 2951）。R1L Diag SWQT 之 2951 = **Software Inventory** | Cert Val 第 1 項之 DID 面改以 `2955`／`295D`／`295E`；DR-SEC-p 結案 |
| `[A-SEC-2]` | `SWE1_Diagnostics_V1 (2).xlsx`（037，`b985e09ac42cece7`）**不含任何 Security DID**（`2965`／`2031`／`2955`／`2966`／`F1B6` 等） | 此類 DID 之 SWE1 歸屬（ECUCert R12 DIAG service？）待 RD 說明。本檔**不投遞** |
| `[A-SEC-3]` | R1L SWQT `2965` 回 **≤2048 bytes**；CS.00102 `2965` 為 **1000 bytes** | ECUCert R18 之 ER 長度斷言；併入 DR-SEC-n 之實作選項 |

## Assumption markers

- `[ASSUMPTION A-SE03]` —— SAM-0017 之 Verification Method 以同群推定，未經 Pei 裁。

| `[A-SE09]` | PENDING | `_D` §1.1 記 F000 回應碼表為 `image249.png`；實測該圖掛在 `SYS-RA-CS00102-698`（**FF01**），F000 之圖為 `image247.png`。且 **xlsx 之 `xl/media/` 為 0 件**，全機查無同名檔 | 「解圖」任務不可執行 | 改自 `SYS2 System-HW` 欄之 RQMT 文字取得語意（byte 4 bit field），見 DATA_REQUESTS；DR-SEC-l 部分結案 |
| `[A-SE10]` | PENDING | `R1L_Diag_Software_Qualification_Test_Design.xlsx` **同名異體**：`Desktop/` 本 954,818 B sha `96a06f0d50d33c1b`（＝_C §1 所載）；`01_Project_R1L/.../M-CPU(Diag)/SW_test_design/` 本 1,012,479 B sha `29e12844bb52d2a6` | 取錯本即取到不同之 DID 值 | 以 `_C` §1 所載 sha 之 `Desktop/` 本為準，已登錄 |

| `[A-SE11]` | PENDING | CCVR `Auth-Prog CS.93` 之 r7 與 r8 **同稱「Flashing lower rollback id」而回值不同** —— r7 回 `0x71 01 F0 00 01`（已遞增版本後回刷舊版），r8 回 `0x71 01 F0 00 02`（未遞增版本後回刷舊版）| R-SEC8(i) 之「`02`（lower rollback id）」若不帶列號，同一敘述會對到兩個值 | 引用時一律連 `per CCVR Auth-Prog CS.93 evidence, row <n>` 標明（R-SEC8(i) 本已要求標 row，本項只是說明其必要性）|

| `[A-SE12]` | PENDING | SEC-01 審閱 三-1 之規則文字為「只計 **THEN**／`3.x`／`THEN.` 子句內之命中」，惟其所列 7 列含 `SWE1-CertProvider-005` —— 該列命中在 **WHEN**（`Monitor system logs during verification`），THEN 無命中 | 逐字照規則得 6 列，照所列集合得 7 列 | 取 **WHEN ∪ THEN** 以重現審閱指名之集合；**兩解不改 batch 總數**（005 本有 CS.98 落點）。請分析層於 SEC-02 明示 |

## 回饋 RD 之 ANOMALIES（`_D` §1.3，非裁定）

| 標記 | 事實（執行層複驗） | 影響 |
|---|---|---|
| `[A-SEC-1]` | CCVR `DID CS.102`／`Cyber DIDs R&P-CS.102` 之「`2951` Certificate Store UUID」**不見於 CS.00102**（731 個 SYS2 ID 全表現查，無 2951）。R1L Diag SWQT 之 2951 = **Software Inventory** | Cert Val 第 1 項之 DID 面改以 `2955`／`295D`／`295E`；DR-SEC-p 結案 |
| `[A-SEC-2]` | `SWE1_Diagnostics_V1 (2).xlsx`（037，`b985e09ac42cece7`）**不含任何 Security DID**（`2965`／`2031`／`2955`／`2966`／`F1B6` 等） | 此類 DID 之 SWE1 歸屬（ECUCert R12 DIAG service？）待 RD 說明。本檔**不投遞** |
| `[A-SEC-3]` | R1L SWQT `2965` 回 **≤2048 bytes**；CS.00102 `2965` 為 **1000 bytes** | ECUCert R18 之 ER 長度斷言；併入 DR-SEC-n 之實作選項 |

## Assumption markers

Inline format in generated JSON reasoning: `[ASSUMPTION A-SEnn]`。
Phase 2 生成前須先結 `[A-SE03]`。

## 回饋 RD 之 ANOMALIES —— CCVR 落地審計（SEC-09 審計；SEC-10 落檔，2026-09-17）

| 標記 | 事實（執行層複驗） | 影響 | 處置 |
|---|---|---|---|
| `[A-SEC-8]` | CCVR `NEW-CERT-02`（Audit minimal TLS CA list）要求「清出未使用／已到期／安全性過時之 root，並留定期稽核紀錄」；037 `SWE1-CertProvider-007`（Secure and Persistent Storage for Trusted Certificates）與 `-009`（Product and Application Dependent Configuration）之 Description／Verification Criteria **無到期、稽核、清理之語意**（逐字查無 `expire`／`audit`／`obsolete`）| 該軸（boundary：憑證到期／過時）在本 feature 無 037 依據，拆 sibling 即越 037（IN §8.4.2）| **不拆**；回饋 037 作者評估是否補 SWE1 要求 |
| `[A-SEC-9]` | CCVR `NEW-ID-01`（Validate all identity-certificate installation fields）要求「recovery 之後仍不得生效」；對 ECUCert 037 **十三列**之 `Requirement Description` 與 `Verification Criteria` 逐列 grep `reboot`／`recovery`／`restart`／`power cycle`（大小寫不計）**命中 0** | 持久化／recovery 軸（IN §8.3）在 037 無載，無從逐字落地 | **不拆**（SEC-10 §3-4 之「無命中」分支）；回饋 037 作者 |
| `[A-SEC-10]` | CCVR `New test cases` 47 條中 **12 條**落不到 037 任何列（`NEW-CERT-10` Apps signer validity period、`NEW-REV-05` revocation triggers／approvals、`NEW-BOOT-01` startup authentication scope、`NEW-DIAG-01` diagnostic role permissions、`NEW-NET-01` external TLS、`NEW-NET-02` server allowlist／URL、`NEW-FW-01`／`NEW-FW-02` firewall／anti-spoofing、`NEW-BT-01` Bluetooth、`NEW-WIFI-01` Wi-Fi AP、`NEW-DATA-01` user data 保護／抹除、`NEW-PROC-01` 驗證計畫治理）| 題域落在網路／藍牙／Wi-Fi／OS／診斷權限／流程治理，非 Security feature 六元件之射程；**SWE.1 層之覆蓋缺口**，不是 SWE.6 之漏寫 | 不由 Security 承接；整份清單回饋 RD／037 作者（`data/audit_ccvr/audit_newtc.tsv` 之 `class = NO_SWE1` 十二列）|
