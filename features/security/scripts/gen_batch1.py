#!/usr/bin/env python3
"""batch 1 正式產出（SEC-04 §4／§5）—— 冪等。

輸入：`data/sibling_plan.tsv` ＋ `sources/raw/` 之六本 037（Description 首句）。
輸出：`sandbox/batch1/security_batch1_v01.xlsx` ＋ 逐 TC json。

寫法一律沿 pilot02（SEC-03 通過本）並套 R-SEC16；四處小修（SEC-04 §2）已內含。
步驟一律由下列 builder 產生 —— 每個 builder 之指令皆取自 `step_assets.tsv` 之既有素材。
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import surgical_save          # noqa: E402

_s = importlib.util.spec_from_file_location("btm", Path(__file__).parent / "build_trace_matrix.py")
btm = importlib.util.module_from_spec(_s)
_s.loader.exec_module(btm)

TEMPLATE = ROOT / "forms" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                             "STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx")
SHEET = "Test Case Specification 測試用例規範"
DATA = ROOT / "features" / "security" / "data"
OUT_DIR = ROOT / "features" / "security" / "sandbox" / "batch1"
# 版本旗標：`SEC_VER=v03` 可重建 SEC-07 形態（R-SEC20／21 之前），供既有本復原；預設 v04。
VER = os.environ.get("SEC_VER", "v04")
SEC08 = VER != "v03"
OUT_XLSX = OUT_DIR / f"security_batch1_{VER}.xlsx"
FIRST_ROW = 10

COLS = {"req_id": "D", "tc_id": "F", "test_group": "G", "test_set": "H",
        "test_item": "I", "pre": "J", "input": "K", "proc": "L", "er": "M",
        "spec": "N", "tc_ref": "O", "priority": "P", "design": "R",
        "fs": "S", "author": "AA", "remarks": "AH"}
VM_COLS = ["T", "U", "V", "W", "X", "Y", "Z"]
VM_VALUES = ["1", "1", "1", "0", "0", "1", "1"]
VM_NAMES = ["HDCC27", "DT27", "VF(ProMaster)637", "Commander (598)",
            "Regengade (5210)", "Toro(2261)", "Fastack (376)"]
GROUP = {"CertProvider": "Cert Provider", "KeyInstall": "Key Install", "SAM": "SAM",
         "ECUCert": "ECU Cert", "SwdlSecureLib": "SWDL Secure Lib", "libLogEncrypt": "Log Encrypt"}
ABBR = {"Cert Provider": "CP", "Key Install": "KI", "SAM": "SAM",
        "ECU Cert": "ECUC", "SWDL Secure Lib": "SWDL", "Log Encrypt": "LOGENC"}
TOKEN = {"Cert Provider": "SWE1-CertProvider-SWE1R1-V1.0",
         "Key Install": "SWE1-KeyInstall-SWE1R1-V1.0", "SAM": "SWE1-SAM-SWE1R1-V1.1",
         "ECU Cert": "SWE1_ECUCert_FM-WI-FSM-037-A03",
         "SWDL Secure Lib": "SWE1_SwdlSecureLib_FM-WI-FSM-037-A03"}
FUNC = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
STATE = "狀態轉換 (State Transition Testing)"
FAULT = "基礎故障注入 (Fault Injection Lite)"
BVA = "邊界值分析 (Boundary Value Analysis, BVA)"

ADB_ROOT = "DUT is connected via ADB with root permission (Dev/Eng build)"
# R-SEC24（SEC-13）：apk 檔名逐字取 CCVR 外部目錄清單（A-33 更正；原值為類名接 .apk 之造值）。
RUNNER_READY = "Test runner CertProviderAndroidInstrumentalTest.apk is installed"
ASSETS = "SecurityAssets/oem-certs/cert-provider/"
STORE = "/odm/etc/cert_store"
FQCN = ("com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test"
        ".CertProviderServiceManagerTest")
RUNNER = ("com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test"
          "/androidx.test.runner.AndroidJUnitRunner")
SSL_VERIFY = ("$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem "
              "-untrusted L2.pem -untrusted L3.pem SAMcert.pem")

# ---- SEC-07 內查（Z1 = KeyInstall_IntegrationTests.zip）之逐字素材 ----
# source: Z1 IntegrationTests/PythonTests/common/keys_install_helper.py L50-L51
INSTALLSTATE = "/mnt/vendor/oemkeys/installstate"
KI_DIAG_RUNNER = (
    "$ adb shell am instrument -w -e class "
    "com.mitsubishielectric.ahu.efw.lib.testkeyinstalldiagservicemanager"
    ".KeyInstallDiagServiceManagerTests#getInstalledKeysStatus "
    "com.mitsubishielectric.ahu.efw.lib.testkeyinstalldiagservicemanager"
    "/androidx.test.runner.AndroidJUnitRunner")
KM_AES_RUNNER = (
    "$ adb shell am instrument -w -e class "
    "com.mitsubishielectric.ahu.efw.lib.testkeymasterwrapper.aes.KeyMasterWrapperAesTests"
    "#encryptDecryptNormalFlow "
    "com.mitsubishielectric.ahu.efw.lib.testkeymasterwrapper.aes"
    "/androidx.test.runner.AndroidJUnitRunner")


def ki_status(er="The instrumentation runner reports \u0022OK (1 test)\u0022 for getInstalledKeysStatus"):
    return ("Query the installed keys status through the DIAG service interface", KI_DIAG_RUNNER, er)


def km_aes():
    return ("Run the KeyMaster wrapper AES encrypt and decrypt normal flow", KM_AES_RUNNER,
            "The instrumentation runner reports \u0022OK (1 test)\u0022 for encryptDecryptNormalFlow")


# ---------------------------------------------------------------- builders
def ssl_verify(ok=True):
    er = ('The openssl command prints "SAMcert.pem: OK" on stdout' if ok else
          'The openssl command prints "unable to get issuer certificate" on stdout')
    return ("Run the OpenSSL chain verification of the certificate on the host", SSL_VERIFY, er)


def ssl_x509(target, er):
    return (f"Read the {target} of the certificate on the host",
            "$ openssl x509 -in leaf.crt -text", er)


def apk(method):
    return (f"Run the Cert Provider instrumentation test for {method}",
            f"$ adb shell am instrument -w -e class {FQCN}#{method} {RUNNER}",
            f'The instrumentation runner reports "OK (1 test)" for {method}')


def logcat(tag, er):
    return (f"Confirm the {tag} log after the previous step", f"$ adb logcat -s {tag}", er)


def ls(path, er, what="Confirm"):
    return (f"{what} the content of {path} on the DUT", f"$ adb shell ls -l {path}", er)


def od(path, value):
    return ("Read the installation state file in the secure partition",
            f"$ adb shell od -t x1 {path}",
            f"The adb shell od -t x1 {path} output shows the installstate value {value}")


def uds(desc, req, resp):
    return (f"Send UDS request {desc}", f"$ {req}", f"Positive response is received: {resp}")


def pend(token, er_token=None):
    return (f"PENDING: {token}", None, f"PENDING: {er_token or token}")


def phys(text, er):
    return (text, None, er)


# ---------------------------------------------------- R-SEC20：X-i 文件審查定式
# 取得方式 037 未載 → 整步為佔位（R-SEC20(b)）；不自擬 `$ grep`／`$ cat`。
PLURAL_ARTIFACT: set[str] = set()          # 複數主詞（動詞需一致）
VERB_PL = {"satisfies": "satisfy", "contains": "contain", "declares": "declare"}


def _agree(artifact: str, verb: str) -> str:
    """複數主詞取原形（避免 `files satisfies`）。"""
    return VERB_PL[verb] if artifact in PLURAL_ARTIFACT else verb


def _cap(text: str) -> str:
    return text[0].upper() + text[1:]


def doc_obtain(artifact: str) -> tuple[str, str, str]:
    be = "are" if artifact in PLURAL_ARTIFACT else "is"
    return (f"<obtain {artifact} per RD>", "",
            f"{_cap(artifact)} {be} available for review")


def doc_review(artifact: str, req: str, verb: str = "satisfies") -> tuple[str, str, str]:
    """`req` 為 037 Verification Criteria 之逐字要件。"""
    return (f'Review {artifact} against "{req}"', "",
            f'{_cap(artifact)} {_agree(artifact, verb)} "{req}"')


# R-SEC20：受本定式重寫之 sibling（鍵同 STEPS）；(d) Pre-Condition、(e) test_item 尾綴依此判。
# R-SEC20(d) 之 `<component>`：用 037 Requirement Title 之元件寫法（`Cert Provider`／`KeyInstall`）。
DOC_COMPONENT = {"CertProvider": "Cert Provider", "KeyInstall": "KeyInstall"}
DOC_REVIEW_PRE = {
    "SWE1-CertProvider-006": ["Access to the RD build environment for Cert Provider is granted"],
    # CP-008 之第三步仍為 logcat（037 第三個 THEN），故保留原 DUT 前提再加建置環境。
    "SWE1-CertProvider-008": None,
    "SWE1-KeyInsyall-012": ["Access to the RD build environment for KeyInstall is granted"],
}
# R-SEC20(amend)：混合型（CP-008 第三步仍為 log 觀察）之 test_item 尾綴。
DOC_SUFFIX_MIXED = {"SWE1-CertProvider-008"}
DOC_REVIEW = {"SWE1-CertProvider-006|1", "SWE1-CertProvider-006|2",
              "SWE1-CertProvider-006|3", "SWE1-CertProvider-006|4",
              "SWE1-CertProvider-008|1", "SWE1-CertProvider-008|2",
              "SWE1-KeyInsyall-012|2", "SWE1-KeyInsyall-012|3"}

# R-SEC20(b)：每一要件一步。artifact 與要件皆取 037 CP-006／CP-008／KI-012 VC 逐字。
_CP_BUILD = "the Cert Provider build files"
_CP_SRCLOG = "the Cert Provider source code and logs"
_CP_ONSTART = "the onStartCommand implementation in the Cert Provider Service"
_CP_SCAN = "the Cert Provider security scan report"
_CP_JAVA = "the source code and dependency graph of the Java clients"
_CP_NATIVE = "the Native client implementations"
_KI_SRC = "the KeyInstall source code"
_KI_CODE = "the KeyInstall code implementation"
PLURAL_ARTIFACT.update({_CP_BUILD, _CP_SRCLOG, _CP_JAVA, _CP_NATIVE})


# ------------------------------------------- 逐 sibling 之步驟（key = swe1_id|sibling_no）
LOGDOG_PEND = "X-h log keyword"
STEPS: dict[str, list] = {
 "SWE1-CertProvider-001|1": [ssl_verify(True), apk("fotaMcpuCertTestNormalFlow"),
   logcat("MelcoCertProviderTest",
          "The adb logcat -s MelcoCertProviderTest output contains no error entry for the leaf certificate")],
 "SWE1-CertProvider-001|2": [ssl_verify(False), apk("fotaMcpuCertTestBrokenCert"),
   logcat("MelcoCertProviderTest", f"PENDING: {LOGDOG_PEND}")],
 "SWE1-CertProvider-002|1": [
   ssl_x509("Subject field", 'The openssl x509 output shows a "Subject:" line identical to the subject name in '
            + ASSETS + "{TYPE}/cfgs/"),
   ssl_verify(True), apk("samCertTestNormalFlow")],
 "SWE1-CertProvider-002|2": [
   ssl_x509("Subject field", 'The openssl x509 output shows a "Subject:" line that is not identical to the subject name in '
            + ASSETS + "{TYPE}/cfgs/"),
   ssl_verify(True), pend("X-e wrong-subject certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-003|1": [
   ssl_x509("Issuer field", 'The openssl x509 output shows an "Issuer:" line identical to the issuer name in '
            + ASSETS + "{TYPE}/cfgs/"),
   ssl_verify(True), apk("samCertTestNormalFlow")],
 "SWE1-CertProvider-003|2": [
   ssl_x509("Issuer field", 'The openssl x509 output shows an "Issuer:" line that is not identical to the issuer name in '
            + ASSETS + "{TYPE}/cfgs/"),
   ssl_verify(True), pend("X-e wrong-issuer certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-004|1": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists "CRL.r0"'),
   pend("X-e revoked certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-004|2": [
   ("Run the OpenSSL chain verification with the local revocation list on the host",
    "$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem "
    "-untrusted L3.pem -untrusted CRL.pem SAMcert.pem",
    'The openssl command prints "certificate revoked" on stdout')],
 "SWE1-CertProvider-005|1": [pend("X-e revoked certificate at the distribution point + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-005|2": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists no revocation list file written during verification')],
 "SWE1-CertProvider-006|1": [doc_obtain(_CP_BUILD), doc_review(_CP_BUILD, "Android.bp must be used instead of legacy Makefiles", "satisfies")],
 "SWE1-CertProvider-006|2": [doc_obtain(_CP_SRCLOG), doc_review(_CP_SRCLOG, "logs must align with Logdog requirements (Error-level only for defects)", "satisfies")],
 "SWE1-CertProvider-006|3": [doc_obtain(_CP_ONSTART), doc_review(_CP_ONSTART, "It must return START_STICKY", "satisfies")],
 "SWE1-CertProvider-006|4": [doc_obtain(_CP_SCAN), doc_review(_CP_SCAN, "The module must be free of vulnerabilities listed in CWE/SANS Top 25 and OWASP Top 10", "satisfies")],
 "SWE1-CertProvider-007|1": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists the trusted certificate chain files')],
 "SWE1-CertProvider-007|2": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists the trusted certificate chain files'),
   ssl_verify(True),
   pend("X-e valid leaf certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-008|1": [
   doc_obtain(_CP_JAVA),
   doc_review(_CP_JAVA,
              "Verify they link against and invoke the CertProvider Binder interface "
              "for certificate validation"),
   logcat("Logdog", f"PENDING: {LOGDOG_PEND}")],
 "SWE1-CertProvider-008|2": [
   doc_obtain(_CP_NATIVE),
   doc_review(_CP_NATIVE,
              "Verify they utilize the libCertProvider C++ API for leaf certificate "
              "verification"),
   logcat("Logdog", f"PENDING: {LOGDOG_PEND}")],
 "SWE1-CertProvider-009|1": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists the Development certificate chain'),
   ssl_verify(True)],
 "SWE1-CertProvider-009|2": [
   ls(STORE, f'The adb shell ls -l {STORE} output lists the Product certificate chain'),
   pend("X-c NR1L production certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-010|1": [apk("fotaMcpuCertVerifyStressTest"),
   ("Read the process resource usage on the DUT", "$ adb shell procrank",
    "The adb shell procrank output shows the Cert Provider RAM usage within the stated limit")],
 "SWE1-CertProvider-011|1": [
   ssl_x509("certificate extensions",
            'The openssl x509 output shows "X509v3 Certificate Policies: critical" and a "Policy:" '
            "line with the OID 1.3.6.1.4.1.57872.<…>"),
   ssl_verify(True), pend("X-e OID certificate + trigger", LOGDOG_PEND)],
 "SWE1-CertProvider-011|2": [
   ssl_x509("certificate extensions",
            'The openssl x509 output shows no "X509v3 Certificate Policies: critical" line, or a '
            '"Policy:" line whose OID is not 1.3.6.1.4.1.57872.<…>'),
   pend("X-e OID certificate + trigger", LOGDOG_PEND)],

 "SWE1-KeyInsyall-001|1": [od("/mnt/vendor/oemkeys/installstate", 0), km_aes()],
 "SWE1-KeyInsyall-001|2": [od("/mnt/vendor/oemkeys/installstate", 2), km_aes()],
 "SWE1-KeyInsyall-002|1": [od("/mnt/vendor/oemkeys/installstate", 3),
   ls("/mnt/vendor/oemkeys", "The adb shell ls -l /mnt/vendor/oemkeys output lists no stored key material")],
 "SWE1-KeyInsyall-003|1": [od("/mnt/vendor/oemkeys/installstate", 3),
   ("Read the status value in the secure partition", "$ adb shell od -t x1 /mnt/vendor/oemkeys/<status file>",
    'The adb shell od -t x1 /mnt/vendor/oemkeys/<status file> output shows "0900 0000 0000 0000"')],
 "SWE1-KeyInsyall-003|2": [od("/mnt/vendor/oemkeys/installstate", 3)],
 "SWE1-KeyInsyall-004|1": [od("/mnt/vendor/oemkeys/installstate", 1)],
 "SWE1-KeyInsyall-005|1": [od("/mnt/vendor/oemkeys/installstate", 2),
   ls("/mnt/vendor/oemkeys", "The adb shell ls -l /mnt/vendor/oemkeys output lists the originally stored key material")],
 "SWE1-KeyInsyall-006|1": [od("/mnt/vendor/oemkeys/installstate", 0)],
 "SWE1-KeyInsyall-006|2": [od("/mnt/vendor/oemkeys/installstate", 1)],
 "SWE1-KeyInsyall-006|3": [od("/mnt/vendor/oemkeys/installstate", 2)],
 "SWE1-KeyInsyall-006|4": [od("/mnt/vendor/oemkeys/installstate", 3)],
 "SWE1-KeyInsyall-007|1": [
   ls("/mnt/vendor/oemkeys", "The adb shell ls -l /mnt/vendor/oemkeys output lists the stored key material"),
   od("/mnt/vendor/oemkeys/installstate", 1)],
 "SWE1-KeyInsyall-007|2": [od("/mnt/vendor/oemkeys/installstate", 2)],
 "SWE1-KeyInsyall-008|1": [
   ls("/mnt/vendor/oemkeys", "The adb shell ls -l /mnt/vendor/oemkeys output lists the stored key blob")],
 "SWE1-KeyInsyall-008|2": [pend("X-j OTA or HAL upgrade image + trigger")],
 "SWE1-KeyInsyall-009|1": [od("/mnt/vendor/oemkeys/installstate", 1), km_aes()],
 "SWE1-KeyInsyall-009|2": [od("/mnt/vendor/oemkeys/installstate", 2), km_aes()],
 "SWE1-KeyInsyall-010|1": [pend("X-f-2 KeyInstall status test runner")],
 "SWE1-KeyInsyall-010|2": [pend("X-f-2 KeyInstall status test runner"),
   logcat("KeyInstall", f"PENDING: {LOGDOG_PEND}")],
 "SWE1-KeyInsyall-011|1": [od("/mnt/vendor/oemkeys/installstate", 2), ki_status()],
 "SWE1-KeyInsyall-011|2": [od("/mnt/vendor/oemkeys/installstate", 3), ki_status()],
 "SWE1-KeyInsyall-012|1": [pend("X-f-2 KeyInstall designated task execution + trigger"),
   logcat("avc", 'The adb logcat -s avc output contains no "avc: denied" entry related to KeyInstall')],
 "SWE1-KeyInsyall-012|2": [doc_obtain(_KI_SRC), doc_review(_KI_SRC, "an Android.bp file must be present and functional", "satisfies")],
 "SWE1-KeyInsyall-012|3": [doc_obtain(_KI_CODE), doc_review(_KI_CODE, "it passes Static Analysis for CERT and CWE compliance", "satisfies")],
 "SWE1-KeyInsyall-013|1": [
   ("Read the process resource usage on the DUT", "$ adb shell procrank",
    "The adb shell procrank output shows the KeyInstall RAM usage within the stated limit"),
   ("Read the size of the oemkeys partition on the DUT", "$ adb shell df /mnt/vendor/oemkeys",
    "The adb shell df /mnt/vendor/oemkeys output shows the partition size within the stated target")],

 "SYSAD_SEC_ECUCERT_ECUCERT_API|1": [
   ls("/data/misc/ecuidentity", 'The adb shell ls -l /data/misc/ecuidentity output lists "ecu.cacert"'),
   pend("X-d ECU certificate chain for the DUT serial number + trigger"),
   logcat("ECU_CERT_SERVICE_FUNCTION_ID",
          "The adb logcat -s ECU_CERT_SERVICE_FUNCTION_ID output contains "
          '"ECU_INSTALLATION_STATUS value : 2 -> 1"')],
 "SYSAD_SEC_ECUCERT_ECUCERT_API|2": [
   ("Corrupt CERT 0 in ecu.cacert on the host and push it to the DUT",
    "$ adb push ecu.cacert /data/misc/ecuidentity/",
    "PENDING: X-d ECU certificate chain for the DUT serial number + trigger"),
   logcat("ECU_CERT_SERVICE_FUNCTION_ID",
          "The adb logcat -s ECU_CERT_SERVICE_FUNCTION_ID output contains "
          '"ECU_INSTALLATION_STATUS value : 2 -> 1"')],
 "SYSAD_SEC_ECUCERT_ECUCERT_SERVICE|1": [
   ("Read the ECU certificate status file on the DUT",
    "$ adb shell od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus",
    "The adb shell od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus output shows the status value")],
 "SYSAD_SEC_ECUCERT_ECUCERT_SERVICE|2": [
   ("Corrupt CERT 0 in ecu.cacert on the host and push it to the DUT",
    "$ adb push ecu.cacert /data/misc/ecuidentity/",
    "PENDING: X-d ECU certificate chain for the DUT serial number + trigger"),
   ("Read the ECU certificate status file on the DUT",
    "$ adb shell od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus",
    "The adb shell od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus output shows the status value")],
 "SYSAD_SEC_ECUCERT_DIAG|1": [
   uds("DiagnosticSessionControl for the SystemSupplierSpecific session", "10 60", "50 60"),
   uds("ReadDataByIdentifier for DID 2966 (ECU Identity Cert Error Enable)", "22 29 66", "62 29 66 <1 byte>")],
 "SYSAD_SEC_ECUCERT_DIAG|2": [
   uds("DiagnosticSessionControl for the SystemSupplierSpecific session", "10 60", "50 60"),
   uds("ReadDataByIdentifier for DID F1B6 (ECU Identity L0 Root certificate)", "22 F1 B6",
       "62 F1 B6 <certificate bytes>")],
 "SYSAD_SEC_ECUCERT_DIAG|3": [
   uds("DiagnosticSessionControl for the SystemSupplierSpecific session", "10 60", "50 60"),
   pend("X-d ECU certificate chain for the DUT serial number + trigger")],
 "SYSAD_SEC_ECUCERT_DEALER|1": [pend("X-k Dealer App access to the DUT")],
 "SYSAD_SEC_ECUCERT_DEALER|2": [pend("X-k Dealer App access to the DUT")],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCSR_INTF|1": [
   uds("DiagnosticSessionControl for the SystemSupplierSpecific session", "10 60", "50 60"),
   uds("ReadDataByIdentifier for DID 2965 (CSR Read)", "22 29 65",
       "62 29 65 <CSR bytes>, up to 1000 bytes"),
   ("Export the CSR file from the DUT to the host", "$ adb pull /data/misc/ecuidentity/ecu.crt",
    'The adb pull command reports "1 file pulled" and ecu.crt is present on the host'),
   ("Check the exported CSR on the host", "$ openssl req -in ecu.crt -noout -verify",
    'The openssl command prints "verify OK" on stdout')],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCERT_INTF|1": [
   ("Export the ECU certificate file from the DUT to the host",
    "$ adb pull /data/misc/ecuidentity/ecu.crt",
    'The adb pull command reports "1 file pulled" and ecu.crt is present on the host'),
   ("Check the exported certificate on the host", "$ openssl x509 -in ecu.crt -noout -text",
    'The openssl output shows an "Issuer:" line and a "Subject:" line for the ECU certificate')],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_IMPORTCERT_INTF|1": [
   ("Push the ECU certificate file from the host to the DUT",
    "$ adb push ecu.crt /data/misc/ecuidentity/",
    "PENDING: X-d ECU certificate chain for the DUT serial number + trigger"),
   ls("/data/misc/ecuidentity", 'The adb shell ls -l /data/misc/ecuidentity output lists "ecu.crt"')],

 "SWE1-SRA-SECURITY-SWDL-003|1": [pend("X-l SWDL decryption test entry point")],
 "SWE1-SRA-SECURITY-SWDL-003|2": [pend("X-l SWDL decryption test entry point")],
 "SWE1-SRA-SECURITY-SWDL-003|3": [pend("X-l SWDL decryption test entry point")],
 "SWE1-SRA-SECURITY-SWDL-004|1": [pend("X-l SWDL verification test entry point")],
 "SWE1-SRA-SECURITY-SWDL-004|2": [
   ("Send UDS request RoutineControl to start the Check Program routine", "$ 31 01 F0 00",
    "Positive response is received: 71 01 F0 00 00")],
 "SWE1-SRA-SECURITY-SWDL-004|3": [
   ("Send UDS request RoutineControl to start the Check Program routine", "$ 31 01 F0 00",
    "Positive response is received: 71 01 F0 00 01")],

 "SWE1-SAM-0002|1": [
   ("Read the running native processes on the DUT", "$ adb shell ps -A",
    "The adb shell ps -A output lists the DebugAuth native daemon")],
 "SWE1-SAM-0004|1": [
   ls("/data/vendor/dauth", "The adb shell ls -l /data/vendor/dauth output lists the installed AuthData",
      "Record"),
   ("Clear the log buffer before the verification attempt", "$ adb logcat -c",
    "The log buffer is cleared"),
   phys("Insert USB drive containing the invalid AuthData package into HU USB port",
        f"PENDING: {LOGDOG_PEND}"),
   logcat("logdog", f"PENDING: {LOGDOG_PEND}"),
   ls("/data/vendor/dauth",
      "The adb shell ls -l /data/vendor/dauth output lists the same installed AuthData as in step 1",
      "Record")],
 "SWE1-SAM-0007|1": [
   ("Read the SAM certificate format and subject on the host", "$ openssl x509 -in SAMcert.pem -text",
    'The openssl x509 output shows the certificate in x509 PEM format and a "Subject:" line intended '
    "for SAM and specific market"),
   ssl_verify(True), apk("samCertTestNormalFlow")],
 "SWE1-SAM-0007|2": [
   ("Read the SAM certificate format and subject on the host", "$ openssl x509 -in SAMcert.pem -text",
    'The openssl x509 output shows an "Issuer:" line that does not anchor to the OEM issued root certificate'),
   ssl_verify(False), pend("X-g SAM AuthData with a non-anchoring certificate + trigger", LOGDOG_PEND)],
 "SWE1-SAM-0015|1": [
   ("Clear the log buffer before the status message is sent", "$ adb logcat -c",
    "The log buffer is cleared"),
   ("Read the stored sequence ID before the status message is sent",
    "$ adb shell cat /data/vendor/dauth/seqId",
    "The adb shell cat /data/vendor/dauth/seqId output shows the current sequence ID"),
   pend("X-g SAM AuthData status change + trigger"),
   logcat("dauth", "The adb logcat -s dauth output contains the sent message with the sequence ID"),
   ("Read the stored sequence ID after the status message is sent",
    "$ adb shell cat /data/vendor/dauth/seqId",
    "The adb shell cat /data/vendor/dauth/seqId output shows the incremented sequence ID")],
 "SWE1-SAM-0018|1": [
   ls("/data/vendor/dauth", "The adb shell ls -l /data/vendor/dauth output lists the installed AuthData files"),
   ("Read the SELinux label of the AuthData directory on the DUT",
    "$ adb shell ls -Z /data/vendor/dauth",
    "The adb shell ls -Z /data/vendor/dauth output shows the SELinux label on the AuthData files")],
}


# ---------------------------------------------------- 逐 SWE1 之 Pre-Condition
_CP_ASSET = f"Certificate assets are available under {ASSETS}"

if not SEC08:          # 重建 v03：X-i 仍為 PENDING（R-SEC20 之前）
    _XI_CP = "X-i Cert Provider source and build environment"
    for _n in "1234":
        STEPS[f"SWE1-CertProvider-006|{_n}"] = [pend(_XI_CP)]
    for _n in "12":
        STEPS[f"SWE1-CertProvider-008|{_n}"] = [pend(_XI_CP),
                                                logcat("Logdog", f"PENDING: {LOGDOG_PEND}")]
    for _n in "23":
        STEPS[f"SWE1-KeyInsyall-012|{_n}"] = [pend("X-i KeyInstall source and build environment")]
    DOC_REVIEW.clear()

PRE: dict[str, list[str]] = {
 "SWE1-CertProvider-001": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-CertProvider-002": [ADB_ROOT, RUNNER_READY, "SAM Dongle is inserted into the DUT",
                           "Configuration files are available under " + ASSETS + "{TYPE}/cfgs/"],
 "SWE1-CertProvider-003": [ADB_ROOT, RUNNER_READY, "SAM Dongle is inserted into the DUT",
                           "Configuration files are available under " + ASSETS + "{TYPE}/cfgs/"],
 "SWE1-CertProvider-004": [ADB_ROOT, RUNNER_READY,
                           'A revocation list "CRL.r0" is preinstalled in the /odm partition', _CP_ASSET],
 "SWE1-CertProvider-005": [ADB_ROOT, "The DUT has network access",
                           "An ECU certificate carrying a valid revocation distribution point is available"],
 "SWE1-CertProvider-006": [ADB_ROOT, "The Cert Provider source code and build environment are available"],
 "SWE1-CertProvider-007": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-CertProvider-008": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-CertProvider-009": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-CertProvider-010": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-CertProvider-011": [ADB_ROOT, RUNNER_READY, _CP_ASSET],
 "SWE1-KeyInsyall-001": [ADB_ROOT, "A USB drive containing valid platform keys is inserted into the HU USB port"],
 "SWE1-KeyInsyall-002": [ADB_ROOT, "A USB drive containing not valid private keys has been inserted into the HU USB port"],
 "SWE1-KeyInsyall-003": [ADB_ROOT, "A USB drive containing non-platform raw keys has been inserted into the HU USB port"],
 "SWE1-KeyInsyall-004": [ADB_ROOT, "An unsuccessful installation has been made on the DUT",
                         "A USB drive containing valid platform keys has been inserted into the HU USB port"],
 "SWE1-KeyInsyall-005": [ADB_ROOT, "Keys have been successfully installed on the DUT",
                         "A USB drive containing valid platform keys has been inserted into the HU USB port"],
 "SWE1-KeyInsyall-006": [ADB_ROOT],
 "SWE1-KeyInsyall-007": [ADB_ROOT, "A USB drive containing valid platform keys has been inserted into the HU USB port",
                         "The DUT has been power cycled after the key material was imported"],
 "SWE1-KeyInsyall-008": [ADB_ROOT, "A key blob is installed on the DUT",
                         "A factory reset has been performed",
                         "The DUT has been power cycled"],
 "SWE1-KeyInsyall-009": [ADB_ROOT],
 "SWE1-KeyInsyall-010": [ADB_ROOT],
 "SWE1-KeyInsyall-011": [ADB_ROOT],
 "SWE1-KeyInsyall-012": [ADB_ROOT, "The DUT runs in SELinux enforcing mode"],
 "SWE1-KeyInsyall-013": [ADB_ROOT],
 "SYSAD_SEC_ECUCERT_ECUCERT_API": [ADB_ROOT, "An ECU certificate chain is present on the DUT"],
 "SYSAD_SEC_ECUCERT_ECUCERT_SERVICE": [ADB_ROOT, "An ECU certificate chain is present on the DUT"],
 "SYSAD_SEC_ECUCERT_DIAG": [ADB_ROOT, "ADA Active Roles permit ADA+ protected data identifiers"],
 "SYSAD_SEC_ECUCERT_DEALER": [ADB_ROOT, "ADA Active Roles permit ADA+ protected data identifiers"],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCSR_INTF": [
   ADB_ROOT, "ADA Active Roles permit ADA+ protected data identifiers",
   "The ECU serial number has been written", "The CSR is generated at boot"],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCERT_INTF": [ADB_ROOT, "An ECU certificate is present on the DUT"],
 "SYSAD_SEC_ECUCERT_ECUCERT_SRV_IMPORTCERT_INTF": [ADB_ROOT, "An ECU certificate file is available on the host"],
 "SWE1-SRA-SECURITY-SWDL-003": [ADB_ROOT, "An encrypted software package is available"],
 "SWE1-SRA-SECURITY-SWDL-004": [ADB_ROOT, "A signed software package is available"],
 "SWE1-SAM-0002": [ADB_ROOT, "The head unit has completed a boot cycle"],
 "SWE1-SAM-0004": [ADB_ROOT, "AuthData is already installed on the DUT",
                   "SAM dongle is inserted into the DUT",
                   "A USB drive containing an AuthData package with a mismatching signature is available"],
 "SWE1-SAM-0007": [ADB_ROOT, RUNNER_READY, "SAM dongle is inserted into the DUT",
                   "An AuthData package is available on a USB drive"],
 "SWE1-SAM-0015": [ADB_ROOT, "DebugAuth is running on the DUT"],
 "SWE1-SAM-0018": [ADB_ROOT, "AuthData has been successfully installed on the DUT"],
}
DESIGN_OVERRIDE = {"SWE1-KeyInsyall-006": STATE, "SWE1-KeyInsyall-007": STATE,
                   "SWE1-KeyInsyall-009": STATE, "SWE1-CertProvider-010": FAULT,
                   "SWE1-KeyInsyall-013": FAULT, "SYSAD_SEC_ECUCERT_DIAG": BVA}


def first_sentence(desc: str) -> str:
    """R-SEC15(f)＋amend：Description 首句；中英並列者取英文句。"""
    text = desc.replace("\r", "")
    blocks = [b.strip() for b in re.split(r"\n\s*\n|\n", text) if b.strip()]
    eng = [b for b in blocks if not re.search(r"[一-鿿]", b)]
    head = (eng[0] if eng else blocks[0])
    return re.split(r"(?<=\.)\s+", head)[0].strip()



# ---------------------------------------------------- R-SEC22：CCVR 衝突與範圍之 Remarks 定式
# (a) 衝突註 —— 依 SWE1 列指派（CCVR `Mapping notes` 之未解衝突）。
CONFLICT_NOTE: dict[str, str] = {
    "SWE1-CertProvider-007": "conflict: 543/546 vs 226; 517 vs 520 — root & CA lifecycle; "
                             "unresolved per CCVR Mapping notes row 12",
    "SWE1-CertProvider-009": "conflict: 543/546 vs 226; 517 vs 520 — root & CA lifecycle; "
                             "unresolved per CCVR Mapping notes row 12",
    "SWE1-CertProvider-004": "conflict: 529/383/532/539 — DCL not deployed; "
                             "unresolved per CCVR Mapping notes row 10",
    "SWE1-CertProvider-005": "conflict: 529/383/532/539 — DCL not deployed; "
                             "unresolved per CCVR Mapping notes row 10",
    "SWE1-KeyInsyall-009": "conflict: 376/509/511 vs 510 vs 514 — key strength; "
                           "unresolved per CCVR Mapping notes row 14",
    "SWE1-KeyInsyall-010": "conflict: 376/509/511 vs 510 vs 514 — key strength; "
                           "unresolved per CCVR Mapping notes row 14",
    # R-SEC22(a) amend（SEC-12）：C3 之落點加 LOGENC-004 兩 sibling
    "SWE1-LOGENC-004": "conflict: 376/509/511 vs 510 vs 514 — key strength; "
                       "unresolved per CCVR Mapping notes row 14",
    "SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCSR_INTF":
        "conflict: 562~565 — CSR format evidence pending; "
        "unresolved per CCVR Mapping notes row 15",
}
# SwdlSecureLib 全列（`NR1L-SWDL-001`~`-006`）
for _swdl in ("001", "002", "003", "004", "005"):
    CONFLICT_NOTE[f"SWE1-SRA-SECURITY-SWDL-{_swdl}"] = (
        "conflict: 344 vs Auth-Prog item 7 — rollback; "
        "unresolved per CCVR Mapping notes row 13")
# (b) 範圍註 —— CP 之負向 sibling ＋ CP-004／005 全部 sibling（CCVR Cert Val CS.98 rationale）。
SCOPE_NOTE = ("scope: service-level validation; reprogramming rejection owned by SWDL "
              "(CCVR Cert Val CS.98 rationale)")
SCOPE_ALL_SIBLINGS = ("SWE1-CertProvider-004", "SWE1-CertProvider-005")


# ---------------------------------------------------- R-SEC21：PENDING → 描述性佔位
# 供給方：多數為 RD；實體憑證鏈由 STLA 供（X-c／X-d 之 EXEC_ASSETS 所載）。
PROVIDER = {"X-c": "STLA", "X-d": "STLA"}
# 性質之敘述（取自原 PENDING 之尾語，去掉 `+ trigger`），使佔位「點名值之來源與性質」。
RE_PENDING_LINE = re.compile(r"^(\s*(?:\d+\.\s*)?)PENDING:\s*(X-[a-z0-9-]+)\s*(.*)$")


def _nature(rest: str) -> str:
    return re.sub(r"\s*\+\s*trigger\s*$", "", rest).strip() or "value"


def placeholder_for(tok: str, rest: str, kind: str) -> str:
    """kind：trigger／exec／command／outcome／value／env（R-SEC21(b) 三型之句式）。"""
    who = PROVIDER.get(tok, "RD")
    n = _nature(rest)
    if kind == "trigger":
        return f"<DUT-side trigger for {n} provided by {who} ({tok})>"
    if kind == "exec":
        return f"<{n} provided by {who} ({tok})> is executed"
    if kind == "command":
        return f"$ <command provided by {who} ({tok})>"
    if kind == "outcome":
        return f"<observable outcome provided by {who} ({tok})>"
    if kind == "env":
        return f"<{n} provided by {who} ({tok})> is available"
    return f"<{n} provided by {who} ({tok})>"


def placeholderise(proc_lines: list[str], er_lines: list[str]
                   ) -> tuple[list[str], list[str], list[dict]]:
    """把 PENDING 行換成描述性佔位；回傳 (proc, er, 逐行紀錄)。

    一行只換一處（R-SEC21(c)）。步驟型佔位另補一行 `$ <command provided by …>`，
    使該步驟仍有執行通道行（R-SEC7(a)）——原 PENDING 步驟係以「整行 PENDING」免通道，
    佔位化後不再具該豁免，故補之。
    """
    rec: list[dict] = []
    out_proc: list[str] = []
    for ln in proc_lines:
        m = RE_PENDING_LINE.match(ln)
        if not m:
            out_proc.append(ln)
            continue
        head, tok, rest = m.groups()
        kind = "trigger" if _nature(rest) != rest.strip() else "exec"
        ph, cmd = placeholder_for(tok, rest, kind), placeholder_for(tok, rest, "command")
        out_proc += [f"{head}{ph}", cmd]
        rec.append({"field": "proc", "line": len(out_proc) - 1, "x_token": tok,
                    "original_pending": ln.strip(), "placeholder": f"{head}{ph}".strip(),
                    "kind": kind, "converted_to": f"{head}{ph}".strip() + " ⏎ " + cmd})
    out_er: list[str] = []
    for ln in er_lines:
        m = RE_PENDING_LINE.match(ln)
        if not m:
            out_er.append(ln)
            continue
        head, tok, rest = m.groups()
        kind = "outcome" if _nature(rest) != rest.strip() else "value"
        ph = placeholder_for(tok, rest, kind)
        out_er.append(f"{head}{ph}")
        rec.append({"field": "er", "line": len(out_er), "x_token": tok,
                    "original_pending": ln.strip(), "placeholder": f"{head}{ph}".strip(),
                    "kind": kind, "converted_to": f"{head}{ph}".strip()})
    return out_proc, out_er, rec


def r_proc_probe(steps) -> str:
    """把該 sibling 之步驟與 ER 攤平為一字串，供 Remarks 之來源判定。"""
    return " ".join(f"{d} {c or ''} {e}" for d, c, e in steps)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plan = list(csv.DictReader((DATA / "sibling_plan.tsv").open(encoding="utf-8"), delimiter="\t"))
    tm = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t")}
    l2 = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "layer2_assign.tsv").open(encoding="utf-8"), delimiter="\t")}
    apk_pairs: dict[str, set[str]] = {}
    for line in (DATA / "apk_pairing.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        f = line.split("\t")
        for sid in f[2].split(";"):
            apk_pairs.setdefault(sid, set()).add(f[1])
    desc = {}
    for row in btm.read_swe1():
        wb_ = None
        desc[row["swe1_id"]] = row
    # Description 首句自 037 D 欄取
    import openpyxl as ox
    d_first = {}
    for doc_id, comp in btm.SWE1_BOOKS:
        wb2 = ox.load_workbook(btm.only(doc_id, "*.xlsx"), read_only=True, data_only=True)
        grid = list(wb2["Analysis Report"].iter_rows(values_only=True))
        for n, r in enumerate(grid[8:], start=9):
            a = "" if r[0] is None else str(r[0]).strip()
            b = "" if r[1] is None else str(r[1]).strip()
            if not a and not b:
                continue
            key = a or btm.split_source_ids(b)[0].replace(" ", "")
            d_first[key] = first_sentence(str(r[3] or ""))
        wb2.close()

    # TC ID：依 framework Layer 2 順序（`layer2_assign.tsv` 之列序）分組連號
    order = [r["swe1_id"] for r in csv.DictReader(
        (DATA / "layer2_assign.tsv").open(encoding="utf-8"), delimiter="\t")]
    rank = {s: i for i, s in enumerate(order)}
    plan.sort(key=lambda r: (rank[r["swe1_id"]], int(r["sibling_no"])))
    counter: Counter = Counter()

    wb = openpyxl.load_workbook(TEMPLATE)
    ws = wb[SHEET]
    out_rows, pend_rows = [], []
    for n, s in enumerate(plan):
        swe1 = s["swe1_id"]
        comp = tm[swe1]["component"]
        group = GROUP[comp]
        counter[group] += 1
        tc_id = f"NR1L-{ABBR[group]}-{counter[group]:03d}"
        key_sib = f'{swe1}|{s["sibling_no"]}'
        doc_rev = key_sib in DOC_REVIEW
        doc_suffix = ("" if not doc_rev else
                      " (document review + log observation)"
                      if swe1 in DOC_SUFFIX_MIXED else " (document review)")
        steps = STEPS[key_sib]
        proc, er = [], []
        for i, (d, cmd, e) in enumerate(steps, 1):
            proc.append(f"{i}. {d}")
            if cmd:
                proc.append(cmd)
            er.append(f"{i}. {e}")
        ph_rec: list[dict] = []
        if SEC08:
            proc, er, ph_rec = placeholderise(proc, er)
        design = DESIGN_OVERRIDE.get(swe1, NEG if s["priority"] and "reject" in s["lower_half(English)"]
                                     or "fails" in s["lower_half(English)"]
                                     or "not identical" in s["lower_half(English)"]
                                     or "refuse" in s["lower_half(English)"] else FUNC)
        remarks = [f'source: 037 {swe1} Requirement Description and Verification Criteria',]
        if doc_rev:          # R-SEC20(a)(f)：首行標驗證型態，並保留 X-i 代號
            remarks.insert(0, "verification: document review (R-SEC20)")
            remarks.append("asset: X-i — closed by R-SEC20 (document review; "
                           "no source/build-environment asset required)")
        if "installstate" in r_proc_probe(STEPS[f'{swe1}|{s["sibling_no"]}']):
            remarks.append("source: Z1 IntegrationTests/PythonTests/common/keys_install_helper.py "
                           "(installstate path and state values verbatim)")
        if "KeyInstallDiagServiceManagerTests" in r_proc_probe(STEPS[f'{swe1}|{s["sibling_no"]}']):
            remarks.append("source: Z1 IntegrationTests/PythonTests/KeysInstallationTests/"
                           "test_java_integration.py (instrument command verbatim)")
        if "KeyMasterWrapperAesTests" in r_proc_probe(STEPS[f'{swe1}|{s["sibling_no"]}']):
            remarks.append("source: Z1 IntegrationTests/PythonTests/KeysInstallationTests/"
                           "test_java_integration.py (instrument command verbatim)")
        if "31 01 F0 00" in r_proc_probe(STEPS[f'{swe1}|{s["sibling_no"]}']):
            remarks.append("source: CCVR Auth-Prog CS.93 evidence items 3/5/6/7/8; "  # R-SEC22(c)
                           "response byte 4 bit field per CS.00102 SYS-RA-CS00102-685")
        remarks += [
                   f'sibling axis: {s["axis"]}; rule {s["rule"]} of SEC-04 4.2',
                   f'channel_feasible: {tm[swe1]["channel_feasible"]}']
        if tm[swe1]["nrl_swe1"] != "-":
            remarks.insert(1, f'Polarion: {tm[swe1]["nrl_swe1"]}')
        for rc in ph_rec:                                        # R-SEC21(d)
            remarks.append(f'asset: {rc["x_token"]} — {rc["original_pending"]}')
        used = {m for m in re.findall(r"#([A-Za-z]+) ", " ".join(proc) + " ")}
        for meth in sorted(used):
            remarks.append(f"apk pairing: {meth} (apk_pairing.tsv)")
        if swe1 in CONFLICT_NOTE:                                # R-SEC22(a)
            remarks.append(CONFLICT_NOTE[swe1])
        if group == "Cert Provider" and (NEG.split(" (")[0] in design
                                         or swe1 in SCOPE_ALL_SIBLINGS):
            remarks.append(SCOPE_NOTE)                           # R-SEC22(b)
        r = {"req_id": swe1, "tc_id": tc_id, "test_group": group,
             "test_set": l2[swe1]["test_set"],
             "test_item": f'{d_first[swe1]}\n({s["lower_half(English)"]}'
                          f'{doc_suffix})',
             "pre": "\n".join(f"{i}. {x}" for i, x in enumerate(
                 (DOC_REVIEW_PRE.get(swe1) or
                  PRE[swe1] + ["Access to the RD build environment for "
                               f'{DOC_COMPONENT[tm[swe1]["component"]]} is granted'])
                 if doc_rev
                 else PRE[swe1], 1)),
             "input": "NA", "proc": "\n".join(proc), "er": "\n".join(er),
             "spec": f'{TOKEN[group]}_{swe1}', "tc_ref": "NEW",
             "priority": s["priority"], "design": design, "fs": "No",
             "author": "PeiPYHsu", "remarks": "\n".join(remarks)}
        row = FIRST_ROW + n
        for key, col in COLS.items():
            ws[f"{col}{row}"] = r[key]
        for col, val in zip(VM_COLS, VM_VALUES):
            ws[f"{col}{row}"] = val
        (OUT_DIR / f"{tc_id}.json").write_text(
            json.dumps({**r, "vehicle_model": dict(zip(VM_NAMES, VM_VALUES)),
                        "placeholders": ph_rec},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        out_rows.append(r)
        for line in (r["proc"] + "\n" + r["er"]).splitlines():
            m = re.match(r"^\s*(?:\d+\.\s*)?PENDING:\s*(\S+)", line)
            if m:
                pend_rows.append((m.group(1), tc_id))

    report = surgical_save(wb, TEMPLATE, OUT_XLSX)
    agg: dict[str, list[str]] = {}
    for token, tc in pend_rows:
        agg.setdefault(token, []).append(tc)
    # v04 之佔位總表由 `build_merged.py` 以合併本口徑產出（`placeholder_summary.tsv`）；
    # 此處只在 v03 模式維護原 `pending_summary.tsv`，v04 模式不另落 batch1 專屬表。
    if not SEC08:
        with (DATA / "pending_summary.tsv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["token", "count", "tc_ids"])
            for token in sorted(agg):
                w.writerow([token, len(agg[token]), ";".join(sorted(set(agg[token])))])

    print(f"batch1：{len(out_rows)} TC → {OUT_XLSX.relative_to(ROOT)}")
    print("  逐組:", dict(counter))
    print("  priority:", dict(Counter(r["priority"] for r in out_rows)))
    print("  design:", dict(Counter(r["design"][:6] for r in out_rows)))
    print(f"  PENDING 行 {len(pend_rows)}；token 群 {len(agg)}")
    print("  surgical:", {k: v for k, v in report.items() if k != "members_patched"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
