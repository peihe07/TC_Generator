# lint036 報告：security_pilot01.xlsx

- 來源：`features/security/sandbox/pilot01/security_pilot01.xlsx`（唯讀）
- 資料列數：10
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`security`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 6 | 6 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 4 | 4 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 1 | 1 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 58 | 10 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v2 | 0 | 0 | 每次命中 | 已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 3 | 3 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |
| V | 行首空白（IN §11） | 0 | 0 | 每行每欄 | 未校準（IN §11，27 包新增） |
| I-cross | 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3） | 10 | 10 | 每列每配對（一組命中記二列） | 警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL |
| W | ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6） | 3 | 3 | 每次命中 | **待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述 |
| X | 導航路徑無固定入口（§5.8／R-G71） | 0 | 0 | 每行 | 未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改** |
| Y | PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式） | 0 | 0 | 每行 | 未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72 |
| SC | 步驟無執行通道／ER 無觀察手段（R-SEC7，Security profile 專屬） | 0 | 0 | 每編號步驟／每 ER 行 | 未校準（R-SEC7，SEC-02 新增）—— **feature 專屬**，僅 `--profile security` 啟用。對既有語料之假陽性率 Procedure 98.4%／ER 74.9%（九本 1,700 列實測，SEC-01 上繳包 8-2），**故絕不可入 PROFILE_CHECKS**；對 Security 自身之假陽性率待 Pilot |
| SS | 最終驗證步驟之 Remarks 無 `source:` 標記（R-SEC4(a)，Security profile 專屬） | 0 | 0 | 每列 | 未校準（R-SEC4(a)，SEC-02 新增）—— **feature 專屬**。判準面之偏差：R-SEC4(a) 原文為「於 reasoning 註明來源」，而 reasoning 在生成側 JSON、不在工作簿；本檢查改以 **Remarks 欄**之 `source:` 標記為判準，待 Pei 覆核（SEC-02 上繳包自報）。R-SEC14(c)：`<…>` 佔位不報 |

**總計：行計 85**（列計不加總——同一列可觸發多項檢查）

## 明細

### A — 禁用動詞 (proc)（行計 6／列計 6）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-CP-001 | proc | 禁用動詞 '2. Verify' | erts/cert-provider/ ⏎ 2. Verify the leaf certificate against the trusted chain on |
| 11 | NR1L-CP-002 | proc | 禁用動詞 '1. Verify' | 1. Verify the broken leaf certificate against the trusted chain on the host. ⏎ $ o |
| 12 | NR1L-CP-003 | proc | 禁用動詞 '3. Verify' | ovider/{TYPE}/cfgs/ ⏎ 3. Verify the leaf certificate against the trusted chain on |
| 13 | NR1L-CP-004 | proc | 禁用動詞 '2. Verify' | -in leaf.crt -text ⏎ 2. Verify the wrong-subject leaf certificate against the tru |
| 15 | NR1L-CP-005 | proc | 禁用動詞 '2. Verify' | -in leaf.crt -text ⏎ 2. Verify the leaf certificate against the trusted chain on |
| 19 | NR1L-SAM-002 | proc | 禁用動詞 '2. Verify' | n SAMcert.pem -text ⏎ 2. Verify the SAM certificate against the OEM issued root ch |

### E — proc/er 編號行數不對齊（行計 4／列計 4）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-CP-001 | proc/er | proc 4 步 vs er 3 步 |  |
| 12 | NR1L-CP-003 | proc/er | proc 4 步 vs er 3 步 |  |
| 14 | NR1L-SAM-001 | proc/er | proc 4 步 vs er 2 步 |  |
| 17 | NR1L-ECUC-001 | proc/er | proc 4 步 vs er 2 步 |  |

### H — ER 模糊語 (er)（行計 1／列計 1）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 14 | NR1L-SAM-001 | er | 關係模糊語 'corresponds to' | an error entry that corresponds to the fail reason; the exact keyword is `PENDIN |

### N — 行尾多餘句號（行計 58／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-CP-001 | proc | 行尾多餘句號 | 1. List the certificate assets under the source path on the host. |
| 10 | NR1L-CP-001 | proc | 行尾多餘句號 | 2. Verify the leaf certificate against the trusted chain on the host. |
| 10 | NR1L-CP-001 | proc | 行尾多餘句號 | 3. Run the Cert Provider instrumentation test for the FOTA MCPU certificate norm |
| 10 | NR1L-CP-001 | proc | 行尾多餘句號 | 4. Confirm the Cert Provider verification result in the log. |
| 10 | NR1L-CP-001 | er | 行尾多餘句號 | 1. The openssl command prints `SAMcert.pem: OK` on stdout. |
| 10 | NR1L-CP-001 | er | 行尾多餘句號 | 2. The instrumentation runner reports `OK (1 test)` for fotaMcpuCertTestNormalFl |
| 10 | NR1L-CP-001 | er | 行尾多餘句號 | 3. `$ adb logcat -s MelcoCertProviderTest` contains no `ERR_` entry for the leaf |
| 11 | NR1L-CP-002 | proc | 行尾多餘句號 | 1. Verify the broken leaf certificate against the trusted chain on the host. |
| 11 | NR1L-CP-002 | proc | 行尾多餘句號 | 2. Run the Cert Provider instrumentation test for the broken certificate flow. |
| 11 | NR1L-CP-002 | proc | 行尾多餘句號 | 3. Confirm the rejection reason in the Cert Provider log. |
| 11 | NR1L-CP-002 | er | 行尾多餘句號 | 1. The openssl command prints `error 2 at 0 depth lookup: unable to get issuer c |
| 11 | NR1L-CP-002 | er | 行尾多餘句號 | 2. The instrumentation runner reports `OK (1 test)` for fotaMcpuCertTestBrokenCe |
| 11 | NR1L-CP-002 | er | 行尾多餘句號 | 3. `$ adb logcat -s MelcoCertProviderTest` contains `MelcoCertProviderTest: ECU  |
| 12 | NR1L-CP-003 | proc | 行尾多餘句號 | 1. Read the Subject field of the leaf certificate on the host. |
| 12 | NR1L-CP-003 | proc | 行尾多餘句號 | 2. List the configuration files that carry the expected subject name. |
| 12 | NR1L-CP-003 | proc | 行尾多餘句號 | 3. Verify the leaf certificate against the trusted chain on the host. |
| 12 | NR1L-CP-003 | proc | 行尾多餘句號 | 4. Confirm the Cert Provider accepts the certificate. |
| 12 | NR1L-CP-003 | er | 行尾多餘句號 | 1. The openssl output shows `Subject: O = Stellantis N.V., CN = CS_{SupplierID}_ |
| 12 | NR1L-CP-003 | er | 行尾多餘句號 | 2. The openssl command prints `SAMcert.pem: OK` on stdout. |
| 12 | NR1L-CP-003 | er | 行尾多餘句號 | 3. The instrumentation runner reports `OK (1 test)` for samCertTestNormalFlow. |
| 13 | NR1L-CP-004 | proc | 行尾多餘句號 | 1. Read the Subject field of the wrong-subject leaf certificate on the host. |
| 13 | NR1L-CP-004 | proc | 行尾多餘句號 | 2. Verify the wrong-subject leaf certificate against the trusted chain on the ho |
| 13 | NR1L-CP-004 | proc | 行尾多餘句號 | 3. Confirm the Cert Provider rejects the certificate. |
| 13 | NR1L-CP-004 | er | 行尾多餘句號 | 1. The openssl output shows a `Subject:` line whose CN differs from the configur |
| 13 | NR1L-CP-004 | er | 行尾多餘句號 | 2. The openssl command prints `SAMcert.pem: OK` on stdout, so the chain is valid |
| 13 | NR1L-CP-004 | er | 行尾多餘句號 | 3. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry for the subj |
| 14 | NR1L-SAM-001 | proc | 行尾多餘句號 | 1. Clear the log buffer before the verification attempt. |
| 14 | NR1L-SAM-001 | proc | 行尾多餘句號 | 2. Record the installed AuthData before the verification attempt. |
| 14 | NR1L-SAM-001 | proc | 行尾多餘句號 | 4. Confirm DebugAuth logged the failure reason and kept the installed AuthData. |
| 14 | NR1L-SAM-001 | er | 行尾多餘句號 | 1. `$ adb shell ls -l /data/vendor/dauth` shows the previously installed AuthDat |
| 14 | NR1L-SAM-001 | er | 行尾多餘句號 | 2. `$ adb logcat -s logdog` contains an error entry that corresponds to the fail |
| 15 | NR1L-CP-005 | proc | 行尾多餘句號 | 1. Read the certificate extensions on the host. |
| 15 | NR1L-CP-005 | proc | 行尾多餘句號 | 2. Verify the leaf certificate against the trusted chain on the host. |
| 15 | NR1L-CP-005 | proc | 行尾多餘句號 | 3. Confirm the Cert Provider accepts the certificate. |
| 15 | NR1L-CP-005 | er | 行尾多餘句號 | 1. The openssl output shows `X509v3 Certificate Policies: critical` and `Policy: |
| 15 | NR1L-CP-005 | er | 行尾多餘句號 | 2. The openssl command prints `SAMcert.pem: OK` on stdout. |
| 15 | NR1L-CP-005 | er | 行尾多餘句號 | 3. The instrumentation runner reports `OK (1 test)`. |
| 16 | NR1L-CP-006 | proc | 行尾多餘句號 | 1. Read the certificate extensions of the wrong-OID certificate on the host. |
| 16 | NR1L-CP-006 | proc | 行尾多餘句號 | 2. Confirm the Cert Provider rejects the certificate and returns the error code. |
| 16 | NR1L-CP-006 | er | 行尾多餘句號 | 1. The openssl output shows no `X509v3 Certificate Policies: critical` line, or  |
| 16 | NR1L-CP-006 | er | 行尾多餘句號 | 2. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry with the cor |
| 17 | NR1L-ECUC-001 | proc | 行尾多餘句號 | 1. Enter the supplier diagnostic session. |
| 17 | NR1L-ECUC-001 | proc | 行尾多餘句號 | 3. Export the CSR file from the DUT to the host. |
| 17 | NR1L-ECUC-001 | proc | 行尾多餘句號 | 4. Confirm the exported file is present on the DUT. |
| 17 | NR1L-ECUC-001 | er | 行尾多餘句號 | 1. Positive response is received: 62 29 65 <CSR bytes>, up to 1000 bytes (CS.001 |
| 17 | NR1L-ECUC-001 | er | 行尾多餘句號 | 2. `$ adb shell ls -l /data/misc/ecuidentity` lists the exported CSR file. |
| 18 | NR1L-KI-001 | proc | 行尾多餘句號 | 1. Read the installation state file in the secure partition. |
| 18 | NR1L-KI-001 | proc | 行尾多餘句號 | 2. Query the installation status through the Binder interface. |
| 18 | NR1L-KI-001 | proc | 行尾多餘句號 | 3. Confirm the diagnostic view of the same state. |
| 18 | NR1L-KI-001 | er | 行尾多餘句號 | 1. `$ adb shell od -t x1 /mnt/vendor/oemkeys` shows the installstate value 2. |
| 18 | NR1L-KI-001 | er | 行尾多餘句號 | 2. The instrumentation runner reports `OK (1 test)` and getStatus() returns `INS |
| 18 | NR1L-KI-001 | er | 行尾多餘句號 | 3. Positive response is received: 62 FF 02 00. |
| 19 | NR1L-SAM-002 | proc | 行尾多餘句號 | 1. Read the SAM certificate format and subject on the host. |
| 19 | NR1L-SAM-002 | proc | 行尾多餘句號 | 2. Verify the SAM certificate against the OEM issued root chain on the host. |
| 19 | NR1L-SAM-002 | proc | 行尾多餘句號 | 3. Confirm DebugAuth accepts the SAM certificate. |
| 19 | NR1L-SAM-002 | er | 行尾多餘句號 | 1. The openssl output shows the certificate is in PEM form and its `Subject:` li |
| 19 | NR1L-SAM-002 | er | 行尾多餘句號 | 2. The openssl command prints `SAMcert.pem: OK` on stdout. |
| 19 | NR1L-SAM-002 | er | 行尾多餘句號 | 3. The instrumentation runner reports `OK (1 test)` for samCertTestNormalFlow. |

### U — PENDING 佔位（四欄全掃，含 ER 側）（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 13 | NR1L-CP-004 | er | PENDING 佔位（DR-SEC-h） | 3. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry for the subj |
| 14 | NR1L-SAM-001 | er | PENDING 佔位（DR-SEC-h） | 2. `$ adb logcat -s logdog` contains an error entry that corresponds to the fail |
| 16 | NR1L-CP-006 | er | PENDING 佔位（DR-SEC-h） | 2. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry with the cor |

### I-cross — 跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）（行計 10／列計 10）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 10 | NR1L-CP-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 11 | NR1L-CP-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 12 | NR1L-CP-003 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 13 | NR1L-CP-004 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 14 | NR1L-SAM-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 15 | NR1L-CP-005 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 16 | NR1L-CP-006 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 17 | NR1L-ECUC-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 18 | NR1L-KI-001 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |
| 19 | NR1L-SAM-002 | expected_result | **窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖） | 起 availability-check → 訖 **未載** |

### W — ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）（行計 3／列計 3）

| 列 | TC ID | 欄位 | 說明 | 片段 |
| ---: | --- | --- | --- | --- |
| 13 | NR1L-CP-004 | er | 比較關係 'differs from'，而 test_item 上半無數值 | ect:` line whose CN differs from the configured name. ⏎ 2. The openssl command pri |
| 14 | NR1L-SAM-001 | er | 比較關係 'corresponds to'，而 test_item 上半無數值 | an error entry that corresponds to the fail reason; the exact keyword is `PENDIN |
| 16 | NR1L-CP-006 | er | 比較關係 'differs from'，而 test_item 上半無數值 | cy:` line whose OID differs from 1.3.6.1.4.1.57872.<…>. ⏎ 2. `$ adb logcat -s Melc |

