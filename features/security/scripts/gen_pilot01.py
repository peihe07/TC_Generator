#!/usr/bin/env python3
"""Pilot01 —— SEC-02 §8 之 10 TC。

每步依 **R-SEC7(a)** 寫執行通道（`$` 指令行或實體操作），ER 依 **R-SEC7(c)** 寫觀察手段；
DID／RID 步驟依 **R-SEC6**；`specification_reference` 依 **R-SEC10(c)**；
Vehicle Model 依 **R-SEC10(f)**；Remarks 之 `source:` 依 **R-SEC4(a)**。

寫檔一律走 `backend.xlsx_surgical.surgical_save`（R18-3；不得 openpyxl `wb.save()`）。
"""

# superseded by gen_batch1.py (SEC-04); do not run — constants frozen per R-TM13
# （SEC-15 review §三：apk 檔名常數停在 R-SEC24 之前，僅加註不改值、不刪檔）
from __future__ import annotations

import json
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import surgical_save          # noqa: E402

TEMPLATE = ROOT / "forms" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                             "STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx")
SHEET = "Test Case Specification 測試用例規範"
OUT_DIR = ROOT / "features" / "security" / "sandbox" / "pilot01"
OUT_XLSX = OUT_DIR / "security_pilot01.xlsx"
FIRST_ROW = 10

COLS = {"req_id": "D", "tc_id": "F", "test_group": "G", "test_set": "H",
        "test_item": "I", "pre": "J", "input": "K", "proc": "L", "er": "M",
        "spec": "N", "tc_ref": "O", "priority": "P", "design": "R",
        "fs": "S", "author": "AA", "remarks": "AH"}
VM_COLS = ["T", "U", "V", "W", "X", "Y", "Z"]      # R-SEC10(f)
VM_VALUES = ["1", "1", "1", "0", "0", "1", "1"]

TOKEN = {
    "Cert Provider": "SWE1-CertProvider-SWE1R1-V1.0",
    "Key Install": "SWE1-KeyInstall-SWE1R1-V1.0",
    "SAM": "SWE1-SAM-SWE1R1-V1.1",
    "ECU Cert": "SWE1_ECUCert_FM-WI-FSM-037-A03",
}
RUNNER = ("com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test"
          "/androidx.test.runner.AndroidJUnitRunner")
FQCN = ("com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test"
        ".CertProviderServiceManagerTest")
ADB_ROOT = "DUT is connected via ADB with root permission (Dev/Eng build)"
RUNNER_READY = "Test runner CertProviderServiceManagerTest.apk is installed"
ASSETS = "SecurityAssets/oem-certs/cert-provider/"

OPENSSL_VERIFY = ("$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem "
                  "-untrusted L2.pem -untrusted L3.pem SAMcert.pem")


def instrument(method: str) -> str:
    return f"$ adb shell am instrument -w -e class {FQCN}#{method} {RUNNER}"


TCS = [
    dict(tc_id="NR1L-CP-001", group="Cert Provider", tset="Chain Verification",
         req="SWE1-CertProvider-001", nrl="NRL-349384", design="Functional Based",
         item_top="Verification of X.509 Leaf Certificate against Trusted Chain",
         item_bot="(valid leaf certificate; OpenSSL chain verification passes)",
         pre=[ADB_ROOT, RUNNER_READY,
              f"Certificate assets of group X-e are present under {ASSETS}"],
         inp=f"Valid leaf certificate SAMcert.pem and chain RootCert.pem / L1.pem / L2.pem / L3.pem under {ASSETS}",
         steps=[("1. Run the OpenSSL chain verification of the leaf certificate on the host",
                 OPENSSL_VERIFY,
                 "1. The openssl command prints `SAMcert.pem: OK` on stdout"),
                ("2. Run the Cert Provider instrumentation test for the FOTA MCPU certificate normal flow",
                 instrument("fotaMcpuCertTestNormalFlow"),
                 "2. The instrumentation runner reports `OK (1 test)` for fotaMcpuCertTestNormalFlow"),
                ("3. Confirm the Cert Provider log carries no error entry for the leaf certificate",
                 "$ adb logcat -s MelcoCertProviderTest",
                 "3. `$ adb logcat -s MelcoCertProviderTest` shows no `ERR_` entry for the leaf certificate")],
         remarks=["source: 037 SWE1-CertProvider-001 Verification Criteria (WHEN/THEN, openssl command verbatim); "
                  "Test_Items.txt #01; CertProfile r11/r18",
                  "apk pairing: high (apk_pairing.tsv #01)"]),

    dict(tc_id="NR1L-CP-002", group="Cert Provider", tset="Chain Verification",
         req="SWE1-CertProvider-001", nrl="NRL-349384", design="Negative / Invalid",
         item_top="Verification of X.509 Leaf Certificate against Trusted Chain",
         item_bot="(broken certificate chain; verification is rejected)",
         pre=[ADB_ROOT, RUNNER_READY,
              f"Certificate assets of group X-e (broken variant) are present under {ASSETS}"],
         inp=f"Broken leaf certificate SAMcert.pem whose issuer is absent from the chain, under {ASSETS}",
         steps=[("1. Run the OpenSSL chain verification of the broken leaf certificate on the host",
                 OPENSSL_VERIFY,
                 "1. The openssl command prints `error 2 at 0 depth lookup: unable to get issuer certificate` on stdout"),
                ("2. Run the Cert Provider instrumentation test for the broken certificate flow",
                 instrument("fotaMcpuCertTestBrokenCert"),
                 "2. The instrumentation runner reports `OK (1 test)` for fotaMcpuCertTestBrokenCert"),
                ("3. Confirm the rejection entry in the Cert Provider log",
                 "$ adb logcat -s MelcoCertProviderTest",
                 "3. `$ adb logcat -s MelcoCertProviderTest` contains "
                 "`MelcoCertProviderTest: ECU certificate verification broken chain = ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY`")],
         remarks=["source: 037 SWE1-CertProvider-001 Verification Criteria; Test_Items.txt #02; "
                  "CCVR Secure Log CS.212 row 1 (log string verbatim, per CS.212 draft 20260826)",
                  "apk pairing: high (apk_pairing.tsv #02)"]),

    dict(tc_id="NR1L-CP-003", group="Cert Provider", tset="Field Matching",
         req="SWE1-CertProvider-002", nrl="NRL-349385", design="Functional Based",
         item_top="Verification of Certificate Subject Field",
         item_bot="(subject name identical to the configuration; certificate is accepted)",
         pre=[ADB_ROOT, RUNNER_READY, "SAM Dongle is inserted into the DUT",
              "Configuration files are present under " + ASSETS + "{TYPE}/cfgs/"],
         inp="Leaf certificate leaf.crt whose Subject CN is identical to the configured name",
         steps=[("1. Read the Subject field of the leaf certificate on the host",
                 "$ openssl x509 -in leaf.crt -text",
                 "1. The openssl output shows `Subject: O = Stellantis N.V., CN = CS_{SupplierID}_{Node}_{OPT - chipset}_ {ECUSWmodule}`"),
                ("2. Run the OpenSSL chain verification of the leaf certificate on the host",
                 OPENSSL_VERIFY,
                 "2. The openssl command prints `SAMcert.pem: OK` on stdout"),
                ("3. Confirm the Cert Provider accepts the certificate",
                 instrument("samCertTestNormalFlow"),
                 "3. The instrumentation runner reports `OK (1 test)` for samCertTestNormalFlow")],
         remarks=["source: 037 SWE1-CertProvider-002 Verification Criteria (openssl x509 / cfgs path verbatim); "
                  "CertProfile r13-r19; Test_Items.txt #04",
                  "apk pairing: high (apk_pairing.tsv #04)"]),

    dict(tc_id="NR1L-CP-004", group="Cert Provider", tset="Field Matching",
         req="SWE1-CertProvider-002", nrl="NRL-349385", design="Negative / Invalid",
         item_top="Verification of Certificate Subject Field",
         item_bot="(subject name differs from the configuration; certificate is rejected)",
         pre=[ADB_ROOT, RUNNER_READY, "SAM Dongle is inserted into the DUT",
              "Configuration files are present under " + ASSETS + "{TYPE}/cfgs/"],
         inp="Leaf certificate leaf.crt whose Subject CN differs from the configured name (wrong-subject variant of X-e)",
         steps=[("1. Read the Subject field of the wrong-subject leaf certificate on the host",
                 "$ openssl x509 -in leaf.crt -text",
                 "1. The openssl output shows a `Subject:` line whose CN differs from the configured name"),
                ("2. Run the OpenSSL chain verification of the wrong-subject leaf certificate on the host",
                 OPENSSL_VERIFY,
                 "2. The openssl command prints `SAMcert.pem: OK` on stdout, so only the Subject field differs"),
                ("3. Confirm the Cert Provider rejects the certificate",
                 "$ adb logcat -s MelcoCertProviderTest",
                 "3. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry for the subject mismatch; "
                 "the exact keyword is `PENDING: DR-SEC-h log keyword`")],
         remarks=["source: 037 SWE1-CertProvider-002 Verification Criteria (correct/wrong subject branch); CertProfile r18",
                  "ER 3 keyword pending DR-SEC-h (CS.212 package not released)"]),

    dict(tc_id="NR1L-SAM-001", group="SAM", tset="Error Handling",
         req="SWE1-SAM-0004", nrl="-", design="Negative / Invalid",
         item_top="DebugAuth shall log an error via logdog and keep the state of all target functions "
                  "when verification of AuthData from external memory failed",
         item_bot="(AuthData verification fails; the installed AuthData is retained)",
         pre=[ADB_ROOT, "AuthData of group X-g is already installed on the DUT",
              "SAM dongle is inserted into the DUT"],
         inp="AuthData package whose signature does not match the manifest (invalid variant of X-g)",
         steps=[("1. Clear the log buffer before the verification attempt",
                 "$ adb logcat -c",
                 "1. `$ adb logcat -s logdog` returns an empty buffer before the attempt"),
                ("2. Insert USB drive containing the invalid AuthData package into HU USB port",
                 None,
                 "2. `$ adb shell ls -l /data/vendor/dauth` shows the previously installed AuthData is still present"),
                ("3. Confirm DebugAuth logged the failure reason",
                 "$ adb logcat -s logdog",
                 "3. `$ adb logcat -s logdog` contains an error entry for the fail reason; "
                 "the exact keyword is `PENDING: DR-SEC-h log keyword`")],
         remarks=["source: 037 SWE1-SAM-0004 Verification Criteria 3.1/3.2 (logdog assertion, R-SEC5(a) amend hit)",
                  "channel_feasible = N (trace_summary 4b) — sampled per SEC-02 §8 constraint"]),

    dict(tc_id="NR1L-CP-005", group="Cert Provider", tset="Field Matching",
         req="SWE1-CertProvider-011", nrl="NRL-349394", design="Functional Based",
         item_top="Verification of Project-Specific Critical Extension",
         item_bot="(extension value is the project identifier; certificate is accepted)",
         pre=[ADB_ROOT, RUNNER_READY,
              "A leaf certificate with the NR1L project-specific critical extension is available"],
         inp="Leaf certificate carrying CertificatePolicies marked critical with OID 1.3.6.1.4.1.57872.<…>",
         steps=[("1. Read the certificate extensions on the host",
                 "$ openssl x509 -in leaf.crt -text",
                 "1. The openssl output shows `X509v3 Certificate Policies: critical` and `Policy: 1.3.6.1.4.1.57872.<…>`"),
                ("2. Run the OpenSSL chain verification of the leaf certificate on the host",
                 OPENSSL_VERIFY,
                 "2. The openssl command prints `SAMcert.pem: OK` on stdout"),
                ("3. Confirm the Cert Provider accepts the certificate",
                 instrument("fotaMcpuCertTestNormalFlow"),
                 "3. The instrumentation runner reports `OK (1 test)` for fotaMcpuCertTestNormalFlow")],
         remarks=["source: CertProfile r36 (CertificatePolicies critical, OID prefix verbatim); "
                  "037 SWE1-CertProvider-011 Verification Criteria",
                  "OID suffix kept as `<…>` placeholder — CertProfile does not give the value (IN §8.4.1)"]),

    dict(tc_id="NR1L-CP-006", group="Cert Provider", tset="Field Matching",
         req="SWE1-CertProvider-011", nrl="NRL-349394", design="Negative / Invalid",
         item_top="Verification of Project-Specific Critical Extension",
         item_bot="(extension value is incorrect or the critical extension is missing; certificate is rejected)",
         pre=[ADB_ROOT, RUNNER_READY,
              "A leaf certificate without the NR1L project-specific critical extension is available "
              "(wrong-OID variant of X-e)"],
         inp="Leaf certificate whose CertificatePolicies OID differs from the project identifier, "
             "or which omits the critical extension",
         steps=[("1. Read the certificate extensions of the wrong-OID certificate on the host",
                 "$ openssl x509 -in leaf.crt -text",
                 "1. The openssl output shows no `X509v3 Certificate Policies: critical` line, "
                 "or a `Policy:` line whose OID differs from 1.3.6.1.4.1.57872.<…>"),
                ("2. Confirm the Cert Provider rejects the certificate and returns the error code",
                 "$ adb logcat -s MelcoCertProviderTest",
                 "2. `$ adb logcat -s MelcoCertProviderTest` contains an `ERR_` entry with the error code; "
                 "the exact keyword is `PENDING: DR-SEC-h log keyword`")],
         remarks=["source: CertProfile r36; 037 SWE1-CertProvider-011 Verification Criteria (second WHEN/THEN pair)",
                  "ER 2 keyword pending DR-SEC-h"]),

    dict(tc_id="NR1L-ECUC-001", group="ECU Cert", tset="Certificate Lifecycle",
         req="SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCSR_INTF", nrl="-", design="Functional Based",
         item_top="ECUCert CSR export interface",
         item_bot="(CSR is read over DID $2965 and exported to a file)",
         pre=[ADB_ROOT, "Diagnostic session is SystemSupplierSpecific (60)",
              "ADA Active Roles permit ADA+ protected data identifiers"],
         inp="DUT whose ECU serial number has been written; CSR is generated automatically at boot",
         steps=[("1. Send UDS request DiagnosticSessionControl for SystemSupplierSpecific session",
                 "$ 10 60",
                 "1. Positive response is received: 50 60"),
                ("2. Send UDS request ReadDataByIdentifier for DID $2965 (CSR Read)",
                 "$ 22 29 65",
                 "2. Positive response is received: 62 29 65 <CSR bytes>, up to 1000 bytes "
                 "(CS.00102 5.2.2.75, SYS-RA-CS00102-415)"),
                ("3. Confirm the exported CSR file is present on the DUT",
                 "$ adb shell ls -l /data/misc/ecuidentity",
                 "3. `$ adb shell ls -l /data/misc/ecuidentity` lists the exported CSR file")],
         remarks=["source: R-SEC6(a) UDS step form; CS.00102 5.2.2.75 (SYS-RA-CS00102-415~418); "
                  "ECU Cert Test Steps PDF Step 2",
                  "SWE ID pending; SYSAD used per R-SEC8(a). DID value per CS.00102; "
                  "R1L Diag SWQT 22403/22404 returns up to 2048 bytes (A-SEC-3)"]),

    dict(tc_id="NR1L-KI-001", group="Key Install", tset="Install State",
         req="SWE1-KeyInsyall-011", nrl="-", design="State Transition",
         item_top="Key Installation Status Query Interface",
         item_bot="(installation completed; the interface returns INSTALLED (2))",
         pre=[ADB_ROOT, "Key installation has completed successfully on the DUT",
              "Diagnostic session is SystemSupplierSpecific (60)"],
         inp="USB drive containing valid platform keys of group X-f, already installed",
         steps=[("1. Read the installation state file in the secure partition",
                 "$ adb shell od -t x1 /mnt/vendor/oemkeys",
                 "1. `$ adb shell od -t x1 /mnt/vendor/oemkeys` shows the installstate value 2"),
                ("2. Query the installation status through the Binder interface",
                 "$ adb shell am instrument -w -e class "
                 "com.mitsubishielectric.ahu.efw.keyinstall.test.KeyInstallStatusTest#getStatus "
                 "com.mitsubishielectric.ahu.efw.keyinstall.test/androidx.test.runner.AndroidJUnitRunner",
                 "2. The instrumentation runner reports `OK (1 test)` and getStatus() returns `INSTALLED (2)`"),
                ("3. Send UDS request ReadDataByIdentifier for DID $FF02 (SecurityKeyInstallStatus)",
                 "$ 22 FF 02",
                 "3. Positive response is received: 62 FF 02 00")],
         remarks=["source: 037 SWE1-KeyInsyall-011 Verification Criteria 1.1/2.1/3.1 (Binder getStatus verbatim); "
                  "R1L Diag SWQT 22345/22346 for DID FF02",
                  "RD ID spelling as delivered. DID 22 FF 02 is supplementary observation only, "
                  "not a pass/fail criterion (R-SEC8(e))"]),

    dict(tc_id="NR1L-SAM-002", group="SAM", tset="AuthData Verification",
         req="SWE1-SAM-0007", nrl="-", design="Functional Based",
         item_top="DebugAuth shall verify certificate",
         item_bot="(SAM certificate is x509 PEM, chains to the OEM issued root, and carries the SAM subject)",
         pre=[ADB_ROOT, RUNNER_READY, "SAM dongle is inserted into the DUT",
              "AuthData of group X-g is available on a USB drive"],
         inp="SAM certificate SAMcert.pem in x509 PEM format, signed by the OEM issued root certificate",
         steps=[("1. Read the SAM certificate format and subject on the host",
                 "$ openssl x509 -in SAMcert.pem -text",
                 "1. The openssl output shows the certificate is in PEM form and its `Subject:` line "
                 "carries the SAM market field"),
                ("2. Run the OpenSSL chain verification of the SAM certificate against the OEM issued root chain",
                 OPENSSL_VERIFY,
                 "2. The openssl command prints `SAMcert.pem: OK` on stdout"),
                ("3. Confirm DebugAuth accepts the SAM certificate",
                 instrument("samCertTestNormalFlow"),
                 "3. The instrumentation runner reports `OK (1 test)` for samCertTestNormalFlow")],
         remarks=["source: 037 SWE1-SAM-0007 Verification Criteria 3.1/3.2/3.3 (037 wording granularity, R-SEC8(h)); "
                  "Test_Items.txt #04",
                  "batch: manual override per R-SEC12 (apk samCertTestNormalFlow). "
                  "SAM tree cert profile is reference only (DR-SEC-q). "
                  "channel_feasible = N — sampled per SEC-02 §8 constraint",
                  "apk pairing: high (apk_pairing.tsv #04)"]),
]

def render(tc: dict) -> dict:
    proc_lines, er_lines = [], []
    for desc, cmd, er in tc["steps"]:
        proc_lines.append(desc)
        if cmd:
            proc_lines.append(cmd)
        er_lines.append(er)
    # E 檢查：proc 之編號步數須與 er 之編號行數相等（R-SEC7(f) 亦要求 1:1）
    assert len(er_lines) == len(tc["steps"]), tc["tc_id"]
    spec = f'{TOKEN[tc["group"]]}_{tc["req"]}'
    remarks = list(tc["remarks"])
    if tc["nrl"] != "-":
        remarks.insert(1, f'Polarion: {tc["nrl"]}')
    return {
        "req_id": tc["req"], "tc_id": tc["tc_id"], "test_group": tc["group"],
        "test_set": tc["tset"],
        "test_item": f'{tc["item_top"]}\n{tc["item_bot"]}',
        "pre": "\n".join(f"{i}. {x}" for i, x in enumerate(tc["pre"], 1)),
        "input": tc["inp"], "proc": "\n".join(proc_lines), "er": "\n".join(er_lines),
        "spec": spec, "tc_ref": "NEW", "priority": "High",
        "design": tc["design"], "fs": "No", "author": "PeiPYHsu",
        "remarks": "\n".join(remarks),
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.load_workbook(TEMPLATE)
    ws = wb[SHEET]
    for n, tc in enumerate(TCS):
        row = FIRST_ROW + n
        r = render(tc)
        for key, col in COLS.items():
            ws[f"{col}{row}"] = r[key]
        for col, val in zip(VM_COLS, VM_VALUES):
            ws[f"{col}{row}"] = val
        (OUT_DIR / f'{tc["tc_id"]}.json').write_text(
            json.dumps({**r, "vehicle_model": dict(zip(
                ["HDCC27", "DT27", "VF(ProMaster)637", "Commander (598)",
                 "Regengade (5210)", "Toro(2261)", "Fastack (376)"], VM_VALUES))},
                ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = surgical_save(wb, TEMPLATE, OUT_XLSX)
    print(f"pilot01：{len(TCS)} TC → {OUT_XLSX.relative_to(ROOT)}")
    print("  surgical_save:", {k: v for k, v in report.items() if k != "members_patched"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
