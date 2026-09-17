# Security Test Execution Guide — FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Security_20260917.xlsx

Generated 2026-09-17 from `sandbox/batch1|2|3/*.json` — the same source as the delivery workbook. **Every command, path, tag and artifact below appears verbatim in at least one test case**; nothing here is new material.

Cross-check against the source registers (reported, not a gate — the workbook is authoritative):

- `apk_pairing.tsv` — 6/6 instrumentation methods are listed in apk_pairing.tsv (17 paired methods)
- `step_assets.tsv` — 30/41 ADB/RC/HOST command lines have a matching `value(verbatim)` row in step_assets.tsv (152 asset rows); the remainder are mostly `adb logcat -s <TAG>` lines, whose tags are sourced per test case in the Remarks (037 verification criteria / CS.212), plus commands added by later packages (Z1 integration tests, 037 resource monitoring)
- `diag_items.tsv` — 3/3 data identifiers read over UDS are registered in diag_items.tsv (['2965', '2966', 'F1B6'])

Scope: 124 test cases, 58 distinct command lines.

## 1. One-time environment setup

### 1.1 ADB

Pre-conditions used by the test cases (verbatim, with the number of cases that carry them):

- `DUT is connected via ADB with root permission (Dev/Eng build)` — 94 TC
- `Test runner CertProviderAndroidInstrumentalTest.apk is installed` — 19 TC
- `Certificate assets are available under SecurityAssets/oem-certs/cert-provider/` — 13 TC

Instrumentation runners invoked by the test cases:

- `com.mitsubishielectric.ahu.efw.lib.testkeymasterwrapper.aes.KeyMasterWrapperAesTests#encryptDecryptNormalFlow` — 4 TC
- `com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#samCertTestNormalFlow` — 3 TC
- `com.mitsubishielectric.ahu.efw.lib.testkeyinstalldiagservicemanager.KeyInstallDiagServiceManagerTests#getInstalledKeysStatus` — 2 TC
- `com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertTestNormalFlow` — 1 TC
- `com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertTestBrokenCert` — 1 TC
- `com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertVerifyStressTest` — 1 TC

> The APK file name appears in the workbook only as `CertProviderAndroidInstrumentalTest.apk` (Pre-Condition above). For the KeyInstall and KeyMaster runners the workbook names the instrumentation class but no APK file, so install them from `<apk provided by RD>`.

### 1.2 UDS

Request bytes used by the test cases (each line is a Procedure step verbatim):

- `$ 10 60` — 4 TC (ECUCert/NR1L-ECUC-007, ECUCert/NR1L-ECUC-008, ECUCert/NR1L-ECUC-009, ECUCert/NR1L-ECUC-016)
- `$ 22 29 65` — 1 TC (ECUCert/NR1L-ECUC-016)
- `$ 22 29 66` — 1 TC (ECUCert/NR1L-ECUC-007)
- `$ 22 F1 B6` — 1 TC (ECUCert/NR1L-ECUC-008)
- `$ 31 01 F0 00` — 2 TC (SwdlSecureLib/NR1L-SWDL-008, SwdlSecureLib/NR1L-SWDL-009)

Diagnostic session access (Pre-Condition verbatim):

- `ADA Active Roles permit ADA+ protected data identifiers` — 6 TC

> The workbook carries no diagnostic CAN identifier and no session other than the bytes listed above, so none is stated here; use the tester configuration of the Diagnostics feature.

### 1.3 CAN

Signal lines used by the test cases:

- `Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)` — 2 TC (SAM/NR1L-SAM-022, SAM/NR1L-SAM-030)
- `Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)` — 2 TC (SAM/NR1L-SAM-023, SAM/NR1L-SAM-031)

Source of the signal definitions (from the Remarks of those cases):

- `CAN signal per VHAL User Guide R5 section 2.4; BCM_FD_10 is 0x481; raw and label verbatim from PDT27_E2A_R1_FDCAN8.dbc` — 2 TC
- `CAN signal per VHAL User Guide R5 section 2.4; STATUS_BH_BCM2 is 0x46C; raw and label verbatim from P363_BH-CAN [07338]_3A_R2.dbc` — 2 TC

### 1.4 Host tools

- `$ ./logdecrypt_Ver2.sh HUssss_YYYYMMDD_HHMMSS_XXXX.enc HUssss_YYYYMMDD_HHMMSS_XXXX_enckey.enc` — 2 TC
- `$ openssl req -in ecu.crt -noout -verify` — 1 TC
- `$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem -untrusted L3.pem -untrusted CRL.pem SAMcert.pem` — 1 TC
- `$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem -untrusted L3.pem SAMcert.pem` — 12 TC
- `$ openssl x509 -in SAMcert.pem -text` — 4 TC
- `$ openssl x509 -in ecu.crt -noout -text` — 1 TC
- `$ openssl x509 -in leaf.crt -text` — 6 TC

### 1.5 Document review

Artifacts to obtain from the RD build environment (23 distinct, 32 TC):

- `the Log Encryption source code` — 6 TC
- `the ECU Online module` — 2 TC
- `the SwdlSecureLib library` — 2 TC
- `the certificate download interface` — 2 TC
- `the client-side key update interface` — 2 TC
- `the Cert Provider build files` — 1 TC
- `the Cert Provider security scan report` — 1 TC
- `the Cert Provider source code and logs` — 1 TC
- `the Cert Store file path access implementation` — 1 TC
- `the DebugAuth source code` — 1 TC
- `the DebugAuth source code about AuthData checking` — 1 TC
- `the ECU Cert JNI layer` — 1 TC
- `the ECUCertService AIDL interface` — 1 TC
- `the ECUOnlineService AIDL interface` — 1 TC
- `the KeyInstall code implementation` — 1 TC
- `the KeyInstall source code` — 1 TC
- `the Log Encrypt source code` — 1 TC
- `the LogEncrypt library` — 1 TC
- `the Native client implementations` — 1 TC
- `the key agent implementation` — 1 TC
- `the onStartCommand implementation in the Cert Provider Service` — 1 TC
- `the project build environment` — 1 TC
- `the source code and dependency graph of the Java clients` — 1 TC

Access required (Pre-Conditions verbatim):

- `Access to the RD build environment for Cert Provider is granted` — 6 TC
- `Access to the RD build environment for DebugAuth is granted` — 2 TC
- `Access to the RD build environment for ECU Cert is granted` — 8 TC
- `Access to the RD build environment for KeyInstall is granted` — 2 TC
- `Access to the RD build environment for Log Encryption is granted` — 9 TC
- `Access to the RD build environment for SwdlSecureLib is granted` — 5 TC

## 1.6 Environment knowledge (not from test cases)

Each line below is cited to a source outside the workbook; **nothing here is asserted by any test case**, so the `⊆` check does not apply to this section.

- Runner install: `$ adb install -r -t CertProviderServiceManagerTest.apk` — CCVR SYS2_Mapped, sheet `Cert Val CS.98`, STEPS column, items 2 and 5 (verbatim). The CCVR directory listing names the file `CertProviderAndroidInstrumentalTest.apk` (handoff `down/20260916_SEC-01.md` line 125); the workbook Pre-Condition follows the directory listing per R-SEC24 — confirm with RD which file is shipped
- Runner check: `$ adb shell pm list instrumentation | grep melcocertprovider` — CCVR SYS2_Mapped, sheet `Cert Val CS.98`, STEPS column, items 2-10 (verbatim)
- KeyInstall / KeyMaster integration tests are run with `$ pytest` and `$ pytest --html=report.html --self-contained-html`; preconditions are `Build with BUILD_INTEGRATION_TESTS checked`, `python3 (>=3.6)`, pip3 `cryptography`/`pytest (>=6.2.4)`/`pytest-html`, and `Connected device`. No APK file name is stated, so install from `<apk provided by RD>` — Z1 `IntegrationTests/PythonTests/README.md` lines 4-18
- Cert Provider integration tests are run the same way, with the additional precondition `$ adb remount` — Z2 `IntegrationTests/README.md` lines 4-18
- Root shell: `$ adb root` — Z1 `IntegrationTests/PythonTests/common/adb_wrapper.py` lines 41-42 (`def root(): os.system("adb root")`)
- `installstate` byte values: `0x00` not installed — Z1 `IntegrationTests/PythonTests/KeysInstallationTests/test_default_keys_unprovisioned.py` lines 43-46
- `installstate` byte values: `0x01` verification pending, `0x02` installed, `0x03` error — Z1 `IntegrationTests/PythonTests/common/keys_install_helper.py` — `assert_verification` lines 204-206, `assert_success` lines 209-211, `assert_error` lines 214-216
- `/mnt/vendor/oemkeys/status/keyinstall` 8-byte values: verification `02 00 00 00 00 00 00 00`, success `00 00 00 00 00 00 00 00`, error `08 00 00 00 00 00 00 00` — Z1 `IntegrationTests/PythonTests/common/keys_install_helper.py` lines 206, 211, 216
- Diagnostic CAN identifiers: Atlantis High `0x7BF` and `0x53F`; Atlantis Mid `0x18DA87F1` and `0x18DAF187` — `forms/VHAL_User_Guide_R5.pdf` section 2.4, `Setting Arch Type DID using RAFT Tool`
- Architecture DID: write `$2850` with `2E 28 50 03` for Atlantis Mid or `2E 28 50 05` for Atlantis High (Atlantis High is the default), then `setprop persist.vendor.can.arch <value>` and reboot the head unit — `forms/VHAL_User_Guide_R5.pdf` section 2.4

## 2. How to read observations

### RC — 6 distinct assertions, 12 TC

- `The instrumentation runner reports "OK (1 test)" for encryptDecryptNormalFlow` — 4 TC
- `The instrumentation runner reports "OK (1 test)" for samCertTestNormalFlow` — 3 TC
- `The instrumentation runner reports "OK (1 test)" for getInstalledKeysStatus` — 2 TC
- `The instrumentation runner reports "OK (1 test)" for fotaMcpuCertTestBrokenCert` — 1 TC
- `The instrumentation runner reports "OK (1 test)" for fotaMcpuCertTestNormalFlow` — 1 TC
- `The instrumentation runner reports "OK (1 test)" for fotaMcpuCertVerifyStressTest` — 1 TC


### LOG — 10 distinct assertions, 16 TC

- `The adb logcat -s dauth output contains the OFF notification to the target functions` — 4 TC
- `The adb logcat -s ECU_CERT_SERVICE_FUNCTION_ID output contains "ECU_INSTALLATION_STATUS value : 2 -> 1"` — 2 TC
- `The adb logcat -s dauth output contains the AuthData in-use entry` — 2 TC
- `The adb logcat -s dauth output contains the current status notification` — 2 TC
- `The adb logcat -s MelcoCertProviderTest output contains no error entry for the leaf certificate` — 1 TC
- `The adb logcat -s avc output contains no "avc: denied" entry related to KeyInstall` — 1 TC
- `The adb logcat -s dauth output contains the ON notification to the target functions` — 1 TC
- `The adb logcat -s dauth output contains the sent message with the sequence ID` — 1 TC

> 2 further LOG assertions follow the same shape; the workbook is authoritative.

### FILE — 44 distinct assertions, 52 TC

- `The adb shell od -t x1 /mnt/vendor/oemkeys/installstate output shows the installstate value 2` — 6 TC
- `The adb shell od -t x1 /mnt/vendor/oemkeys/installstate output shows the installstate value 3` — 5 TC
- `The adb shell od -t x1 /mnt/vendor/oemkeys/installstate output shows the installstate value 1` — 4 TC
- `The adb pull command reports "1 file pulled" and ecu.crt is present on the host` — 2 TC
- `The adb shell cat /data/vendor/dauth/seqId output shows the sequence ID 0` — 2 TC
- `The adb shell cat /data/vendor/dauth/ts output shows the stored timestamp` — 2 TC
- `The adb shell ls -l /data/vendor/logdog output lists the encrypted log and the encrypted key` — 2 TC
- `The adb shell ls -l /odm/etc/cert_store output lists the trusted certificate chain files` — 2 TC

> 36 further FILE assertions follow the same shape; the workbook is authoritative.

### UDS — 6 distinct assertions, 6 TC

- `Positive response is received: 50 60` — 4 TC
- `Positive response is received: 62 29 65 <CSR bytes>, up to 1000 bytes` — 1 TC
- `Positive response is received: 62 29 66 <1 byte>` — 1 TC
- `Positive response is received: 62 F1 B6 <certificate bytes>` — 1 TC
- `Positive response is received: 71 01 F0 00 00` — 1 TC
- `Positive response is received: 71 01 F0 00 01` — 1 TC


### HOST — 15 distinct assertions, 18 TC

- `The openssl command prints "SAMcert.pem: OK" on stdout` — 10 TC
- `The logdecrypt_Ver2.sh tool creates the folder HUssss_YYYYMMDD_HHMMSS_XXXX on the host` — 2 TC
- `The openssl command prints "unable to get issuer certificate" on stdout` — 2 TC
- `The openssl x509 output shows the certificate in x509 PEM format` — 2 TC
- `The openssl command prints "certificate revoked" on stdout` — 1 TC
- `The openssl command prints "verify OK" on stdout` — 1 TC
- `The openssl output shows an "Issuer:" line and a "Subject:" line for the ECU certificate` — 1 TC
- `The openssl x509 output shows "X509v3 Certificate Policies: critical" and a "Policy:" line with the OID 1.3.6.1.4.1.57872.<…>` — 1 TC

> 7 further HOST assertions follow the same shape; the workbook is authoritative.

### CAN — 2 distinct assertions, 4 TC

- `BCM_FD_10.CmdIgnSts = 4 (RUN) is sent` — 2 TC
- `STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent` — 2 TC


### DOC — 51 distinct assertions, 32 TC

- `The Log Encryption source code is available for review` — 6 TC
- `The ECU Online module is available for review` — 2 TC
- `The SwdlSecureLib library is available for review` — 2 TC
- `The certificate download interface is available for review` — 2 TC
- `The client-side key update interface is available for review` — 2 TC
- `The Cert Provider build files satisfy "Android.bp must be used instead of legacy Makefiles"` — 1 TC
- `The Cert Provider security scan report is available for review` — 1 TC
- `The Cert Provider security scan report satisfies "The module must be free of vulnerabilities listed in CWE/SANS Top 25 and OWASP Top 10"` — 1 TC

> 43 further DOC assertions follow the same shape; the workbook is authoritative.

Log tags used (`adb logcat -s <TAG>`):

- `dauth` — 16 TC
- `MelcoCertProviderTest` — 2 TC
- `Logdog` — 2 TC
- `ECU_CERT_SERVICE_FUNCTION_ID` — 2 TC
- `KeyInstall` — 1 TC
- `avc` — 1 TC
- `logdog` — 1 TC

Device paths read or written:

- `/mnt/vendor/oemkeys/installstate` — 17 TC
- `/data/vendor/dauth` — 11 TC
- `/odm/etc/cert_store` — 6 TC
- `/mnt/vendor/oemkeys` — 5 TC
- `/data/vendor/dauth/seqId` — 4 TC
- `/data/vendor/dauth/ts` — 4 TC
- `/data/misc/ecuidentity/` — 3 TC
- `/data/vendor/dauth/vc` — 3 TC
- `/data/misc/ecuidentity` — 2 TC
- `/data/misc/ecuidentity/ecu.crt` — 2 TC
- `/data/vendor/logdog` — 2 TC
- `/mnt/vendor/oemkeys/ecu/state/ecucertstatus` — 2 TC
- `/mnt/vendor/oemkeys/<status` — 1 TC
- `/sys/devices/soc0/serial_number` — 1 TC

## 3. Command index

| # | Command (verbatim) | TC |
| ---: | --- | --- |
| 1 | `$ <command provided by RD (X-g)>` | SAM/NR1L-SAM-004, SAM/NR1L-SAM-006, SAM/NR1L-SAM-007, SAM/NR1L-SAM-008, SAM/NR1L-SAM-009, SAM/NR1L-SAM-011 …(+12) |
| 2 | `$ adb shell od -t x1 /mnt/vendor/oemkeys/installstate` | KeyInstall/NR1L-KI-001, KeyInstall/NR1L-KI-002, KeyInstall/NR1L-KI-003, KeyInstall/NR1L-KI-004, KeyInstall/NR1L-KI-005, KeyInstall/NR1L-KI-006 …(+11) |
| 3 | `$ adb logcat -s dauth` | SAM/NR1L-SAM-006, SAM/NR1L-SAM-007, SAM/NR1L-SAM-008, SAM/NR1L-SAM-009, SAM/NR1L-SAM-013, SAM/NR1L-SAM-019 …(+10) |
| 4 | `$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem -untrusted L3.pem SAMcert.pem` | CertProvider/NR1L-CP-001, CertProvider/NR1L-CP-002, CertProvider/NR1L-CP-003, CertProvider/NR1L-CP-004, CertProvider/NR1L-CP-005, CertProvider/NR1L-CP-006 …(+6) |
| 5 | `$ adb shell ls -l /data/vendor/dauth` | SAM/NR1L-SAM-003, SAM/NR1L-SAM-004, SAM/NR1L-SAM-005, SAM/NR1L-SAM-012, SAM/NR1L-SAM-014, SAM/NR1L-SAM-015 …(+2) |
| 6 | `$ <command provided by RD (X-e)>` | CertProvider/NR1L-CP-004, CertProvider/NR1L-CP-006, CertProvider/NR1L-CP-007, CertProvider/NR1L-CP-009, CertProvider/NR1L-CP-016, CertProvider/NR1L-CP-022 …(+1) |
| 7 | `$ adb shell ls -l /odm/etc/cert_store` | CertProvider/NR1L-CP-007, CertProvider/NR1L-CP-010, CertProvider/NR1L-CP-015, CertProvider/NR1L-CP-016, CertProvider/NR1L-CP-019, CertProvider/NR1L-CP-020 |
| 8 | `$ openssl x509 -in leaf.crt -text` | CertProvider/NR1L-CP-003, CertProvider/NR1L-CP-004, CertProvider/NR1L-CP-005, CertProvider/NR1L-CP-006, CertProvider/NR1L-CP-022, CertProvider/NR1L-CP-023 |
| 9 | `$ 10 60` | ECUCert/NR1L-ECUC-007, ECUCert/NR1L-ECUC-008, ECUCert/NR1L-ECUC-009, ECUCert/NR1L-ECUC-016 |
| 10 | `$ <command provided by RD (X-l)>` | SwdlSecureLib/NR1L-SWDL-004, SwdlSecureLib/NR1L-SWDL-005, SwdlSecureLib/NR1L-SWDL-006, SwdlSecureLib/NR1L-SWDL-007 |
| 11 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.testkeymasterwrapper.aes.KeyMasterWrapperAesTests#encryptDecryptNormalFlow com.mitsubishielectric.ahu.efw.lib.testkeymasterwrapper.aes/androidx.test.runner.AndroidJUnitRunner` | KeyInstall/NR1L-KI-001, KeyInstall/NR1L-KI-002, KeyInstall/NR1L-KI-016, KeyInstall/NR1L-KI-017 |
| 12 | `$ adb shell cat /data/vendor/dauth/seqId` | SAM/NR1L-SAM-027, SAM/NR1L-SAM-030, SAM/NR1L-SAM-031 |
| 13 | `$ adb shell cat /data/vendor/dauth/ts` | SAM/NR1L-SAM-016, SAM/NR1L-SAM-017 |
| 14 | `$ adb shell ls -l /mnt/vendor/oemkeys` | KeyInstall/NR1L-KI-003, KeyInstall/NR1L-KI-007, KeyInstall/NR1L-KI-012, KeyInstall/NR1L-KI-014 |
| 15 | `$ openssl x509 -in SAMcert.pem -text` | SAM/NR1L-SAM-006, SAM/NR1L-SAM-010, SAM/NR1L-SAM-011, SAM/NR1L-SAM-012 |
| 16 | `$ <command provided by RD (X-f-2)>` | KeyInstall/NR1L-KI-018, KeyInstall/NR1L-KI-019, KeyInstall/NR1L-KI-022 |
| 17 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#samCertTestNormalFlow com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | CertProvider/NR1L-CP-003, CertProvider/NR1L-CP-005, SAM/NR1L-SAM-010 |
| 18 | `$ adb shell cat /data/vendor/dauth/vc` | SAM/NR1L-SAM-019, SAM/NR1L-SAM-020, SAM/NR1L-SAM-021 |
| 19 | `$ ./logdecrypt_Ver2.sh HUssss_YYYYMMDD_HHMMSS_XXXX.enc HUssss_YYYYMMDD_HHMMSS_XXXX_enckey.enc` | libLogEncrypt/NR1L-LOGENC-009 |
| 20 | `$ 31 01 F0 00` | SwdlSecureLib/NR1L-SWDL-008, SwdlSecureLib/NR1L-SWDL-009 |
| 21 | `$ <command provided by RD (X-k)>` | ECUCert/NR1L-ECUC-010, ECUCert/NR1L-ECUC-011 |
| 22 | `$ <command provided by RD (X-n)>` | SAM/NR1L-SAM-024, SAM/NR1L-SAM-025 |
| 23 | `$ <command provided by STLA (X-d)>` | ECUCert/NR1L-ECUC-001, ECUCert/NR1L-ECUC-009 |
| 24 | `$ adb logcat -c` | SAM/NR1L-SAM-005, SAM/NR1L-SAM-027 |
| 25 | `$ adb logcat -s ECU_CERT_SERVICE_FUNCTION_ID` | ECUCert/NR1L-ECUC-001, ECUCert/NR1L-ECUC-002 |
| 26 | `$ adb logcat -s Logdog` | CertProvider/NR1L-CP-017, CertProvider/NR1L-CP-018 |
| 27 | `$ adb logcat -s MelcoCertProviderTest` | CertProvider/NR1L-CP-001, CertProvider/NR1L-CP-002 |
| 28 | `$ adb pull /data/misc/ecuidentity/ecu.crt` | ECUCert/NR1L-ECUC-016, ECUCert/NR1L-ECUC-017 |
| 29 | `$ adb push ecu.cacert /data/misc/ecuidentity/` | ECUCert/NR1L-ECUC-002, ECUCert/NR1L-ECUC-004 |
| 30 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.testkeyinstalldiagservicemanager.KeyInstallDiagServiceManagerTests#getInstalledKeysStatus com.mitsubishielectric.ahu.efw.lib.testkeyinstalldiagservicemanager/androidx.test.runner.AndroidJUnitRunner` | KeyInstall/NR1L-KI-020, KeyInstall/NR1L-KI-021 |
| 31 | `$ adb shell ls -l /data/misc/ecuidentity` | ECUCert/NR1L-ECUC-001, ECUCert/NR1L-ECUC-018 |
| 32 | `$ adb shell ls -l /data/vendor/logdog` | libLogEncrypt/NR1L-LOGENC-007, libLogEncrypt/NR1L-LOGENC-008 |
| 33 | `$ adb shell od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus` | ECUCert/NR1L-ECUC-003, ECUCert/NR1L-ECUC-004 |
| 34 | `$ adb shell procrank` | CertProvider/NR1L-CP-021, KeyInstall/NR1L-KI-025 |
| 35 | `Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)` | SAM/NR1L-SAM-022, SAM/NR1L-SAM-030 |
| 36 | `Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)` | SAM/NR1L-SAM-023, SAM/NR1L-SAM-031 |
| 37 | `$ 22 29 65` | ECUCert/NR1L-ECUC-016 |
| 38 | `$ 22 29 66` | ECUCert/NR1L-ECUC-007 |
| 39 | `$ 22 F1 B6` | ECUCert/NR1L-ECUC-008 |
| 40 | `$ <command provided by RD (X-j)>` | KeyInstall/NR1L-KI-015 |
| 41 | `$ <command provided by RD (X-m)>` | libLogEncrypt/NR1L-LOGENC-009 |
| 42 | `$ <command provided by STLA (X-c)>` | CertProvider/NR1L-CP-020 |
| 43 | `$ adb logcat -s KeyInstall` | KeyInstall/NR1L-KI-019 |
| 44 | `$ adb logcat -s avc` | KeyInstall/NR1L-KI-022 |
| 45 | `$ adb logcat -s logdog` | SAM/NR1L-SAM-005 |
| 46 | `$ adb push ecu.crt /data/misc/ecuidentity/` | ECUCert/NR1L-ECUC-018 |
| 47 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertTestBrokenCert com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | CertProvider/NR1L-CP-002 |
| 48 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertTestNormalFlow com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | CertProvider/NR1L-CP-001 |
| 49 | `$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#fotaMcpuCertVerifyStressTest com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner` | CertProvider/NR1L-CP-021 |
| 50 | `$ adb shell cat /sys/devices/soc0/serial_number` | SAM/NR1L-SAM-008 |
| 51 | `$ adb shell df /mnt/vendor/oemkeys` | KeyInstall/NR1L-KI-025 |
| 52 | `$ adb shell getsslog` | libLogEncrypt/NR1L-LOGENC-007 |
| 53 | `$ adb shell ls -Z /data/vendor/dauth` | SAM/NR1L-SAM-032 |
| 54 | `$ adb shell od -t x1 /mnt/vendor/oemkeys/<status file>` | KeyInstall/NR1L-KI-004 |
| 55 | `$ adb shell ps -A` | SAM/NR1L-SAM-002 |
| 56 | `$ openssl req -in ecu.crt -noout -verify` | ECUCert/NR1L-ECUC-016 |
| 57 | `$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem -untrusted L3.pem -untrusted CRL.pem SAMcert.pem` | CertProvider/NR1L-CP-008 |
| 58 | `$ openssl x509 -in ecu.crt -noout -text` | ECUCert/NR1L-ECUC-017 |

## 4. Assets still to be provided

From `placeholder_by_token.tsv`; the placeholders inside the workbook carry the same code. See `asset_request.md` for who to ask and the urgency order. The 50 rows containing placeholders are shaded light orange (FCE4D6) in the delivery workbooks (`placeholder_rows.tsv` lists them).

| Token | Placeholder lines | TC | Fields |
| --- | ---: | ---: | --- |
| `X-c` | 1 | 1 | proc=1 |
| `X-d` | 7 | 5 | er=5 proc=2 |
| `X-e` | 7 | 7 | proc=7 |
| `X-f-2` | 6 | 3 | er=3 proc=3 |
| `X-g` | 36 | 19 | er=18 proc=18 |
| `X-h` | 19 | 18 | er=19 |
| `X-j` | 2 | 1 | er=1 proc=1 |
| `X-k` | 4 | 2 | er=2 proc=2 |
| `X-l` | 8 | 4 | er=4 proc=4 |
| `X-m` | 2 | 1 | er=1 proc=1 |
| `X-n` | 4 | 2 | er=2 proc=2 |

## 5. Automation mapping (for the later script phase)

| Channel | Helper | TC | Note |
| --- | --- | ---: | --- |
| ADB | `adb(cmd)` | 70 |  |
| RC | `instrument(class, method)` | 12 |  |
| UDS | `uds(bytes)` | 6 |  |
| CAN | `can_send(msg, sig, raw)` | 4 |  |
| HOST | `host(cmd)` | 18 |  |
| PHYS | `pause(prompt)` | 2 | manual step — the runner stops and prompts |
| DOC | `doc_review()  # not generated` | 32 | document review — no execution generated |

> Not a channel: 41 test cases carry a placeholder command line (`<command provided by …>`, written as a `$` step) and cannot be automated until the asset arrives; 50 test cases carry a placeholder in any field and are the shaded rows — see section 4.

Manual (PHYS) steps, verbatim:

- `Insert USB drive containing the AuthData package into HU USB port` — SAM/NR1L-SAM-003
- `Insert USB drive containing the invalid AuthData package into HU USB port` — SAM/NR1L-SAM-005
