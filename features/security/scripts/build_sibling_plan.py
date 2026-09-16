#!/usr/bin/env python3
"""SEC-04 §4.2 —— batch 1 產出群 38 列之 sibling 推導（機械，先於寫 TC）。

規則（逐條標於每列之 `rule` 欄）：
  1 037 `Verification Criteria` 之每一 WHEN/THEN 對 = 至少 1 TC
  2 列舉之支援項／狀態值 → 每值 1 TC
  3 有「接受」路徑者必配「拒絕」負向；負向無觸發手段者仍出 TC，觸發步驟 PENDING
  4 同一觸發之多重後果 = 一 TC 多行 ER，不拆
  5 持久化（reboot／factory reset）為獨立 sibling
  6 每 sibling 之 `distinguishing_axis` 必填；同 SWE1 之括號下半不得重複

Priority 依 R-SEC16。`trigger_channel` 依 R-SEC7(a) 之閉合清單。
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features" / "security" / "data" / "sibling_plan.tsv"

# (swe1_id, [(lower_half, axis, channel, pending, priority, rule)])
P = "PENDING"
SPEC: list[tuple[str, list[tuple[str, str, str, str, str, str]]]] = [
 ("SWE1-CertProvider-001", [
  ("valid leaf certificate; chain verification passes", "verification outcome", "HOST/ADB", "N", "P0", "1,3"),
  ("broken certificate chain; verification is rejected", "verification outcome", "HOST/ADB", "N", "P0", "1,3")]),
 ("SWE1-CertProvider-002", [
  ("subject name identical to the configuration; certificate is accepted", "subject match", "HOST/ADB", "N", "P1", "1,3"),
  ("subject name not identical to the configuration; certificate is rejected", "subject match", "HOST/PENDING", "Y", "P1", "1,3")]),
 ("SWE1-CertProvider-003", [
  ("issuer name identical to the configuration; certificate is accepted", "issuer match", "HOST/ADB", "N", "P1", "1,3"),
  ("issuer name not identical to the configuration; certificate is rejected", "issuer match", "HOST/PENDING", "Y", "P1", "1,3")]),
 ("SWE1-CertProvider-004", [
  ("certificate listed in the local revocation list; certificate is rejected", "revocation outcome", "ADB/PENDING", "Y", "P0", "1,3"),
  ("OpenSSL verification with the local revocation list on the host", "verification path", "HOST", "N", "P0", "1")]),
 ("SWE1-CertProvider-005", [
  ("certificate revoked at the distribution point; certificate is rejected", "revocation outcome", "PENDING", "Y", "P0", "1,3"),
  ("no revocation list file is written to the storage partitions", "storage side effect", "ADB", "N", "P0", "1")]),
 ("SWE1-CertProvider-006", [
  ("build files use Android.bp instead of legacy Makefiles", "build system", "PENDING", "Y", "P2", "1"),
  ("logs follow the Logdog error-level policy", "logging policy", "PENDING", "Y", "P2", "1"),
  ("onStartCommand returns START_STICKY", "service lifecycle", "PENDING", "Y", "P2", "1"),
  ("security scan reports no CWE/SANS Top 25 or OWASP Top 10 finding", "security scan", "PENDING", "Y", "P2", "1")]),
 ("SWE1-CertProvider-007", [
  ("trusted certificate chain is present at the deployed store path", "store presence", "ADB", "N", "P1", "1"),
  ("trusted certificate chain survives a factory reset and still verifies a leaf", "persistence after factory reset", "PHYS/ADB", "N", "P1", "4,5")]),
 ("SWE1-CertProvider-008", [
  ("Java client invokes the Binder interface for certificate validation", "client type", "ADB", "N", "P1", "1,4"),
  ("Native client uses the libCertProvider C++ API for leaf verification", "client type", "ADB", "N", "P1", "1,4")]),
 ("SWE1-CertProvider-009", [
  ("Development configuration; the matching certificate chain is deployed", "configuration version", "ADB", "N", "P1", "1,2"),
  ("Product configuration; the matching certificate chain is deployed", "configuration version", "ADB", "N", "P1", "1,2")]),
 ("SWE1-CertProvider-010", [
  ("resource usage stays within the estimated limits during repeated verification", "resource consumption", "ADB", "N", "P2", "1,4")]),
 ("SWE1-CertProvider-011", [
  ("extension value is the project identifier; certificate is accepted", "extension value", "HOST/PENDING", "Y", "P1", "1,3"),
  ("extension value is incorrect or missing; certificate is rejected", "extension value", "HOST/PENDING", "Y", "P1", "1,3")]),

 ("SWE1-KeyInsyall-001", [
  ("keys are not installed; a temporary key is provided", "key source", "ADB", "N", "P1", "1"),
  ("keys are installed; the installed key is provided", "key source", "PHYS/ADB", "N", "P1", "1")]),
 ("SWE1-KeyInsyall-002", [
  ("not valid private keys; verification fails and stored keys are removed", "verification outcome", "PHYS/ADB", "N", "P0", "1,4")]),
 ("SWE1-KeyInsyall-003", [
  ("non-platform raw keys; installstate is ERROR (3)", "key platform scope", "PHYS/ADB", "N", "P0", "1,4"),
  ("R1LRefresh keys are used for the installation attempt", "key platform scope", "PHYS/ADB", "N", "P0", "1")]),
 ("SWE1-KeyInsyall-004", [
  ("installation is re-triggered after a failed attempt", "re-attempt", "PHYS/ADB", "N", "P0", "1")]),
 ("SWE1-KeyInsyall-005", [
  ("keys already installed; a new installation is not started", "overwrite prevention", "PHYS/ADB", "N", "P1", "1")]),
 ("SWE1-KeyInsyall-006", [
  ("installstate file contains NOT_INSTALLED (0)", "installstate value", "ADB", "N", "P1", "2"),
  ("installstate file contains VERIFICATION_REQUIRED (1)", "installstate value", "ADB", "N", "P1", "2"),
  ("installstate file contains INSTALLED (2)", "installstate value", "ADB", "N", "P1", "2"),
  ("installstate file contains ERROR (3)", "installstate value", "ADB", "N", "P1", "2")]),
 ("SWE1-KeyInsyall-007", [
  ("keys imported from USB; secrets stored and installstate is VERIFICATION_REQUIRED (1)", "import stage", "PHYS/ADB", "N", "P0", "1,4"),
  ("after reboot the installation status changes to INSTALLED (2)", "persistence after reboot", "PHYS/ADB", "N", "P0", "5")]),
 ("SWE1-KeyInsyall-008", [
  ("key blob remains accessible after a factory reset", "persistence trigger", "PHYS/ADB", "N", "P1", "5"),
  ("key blob is still usable after an OTA or HAL version upgrade", "persistence trigger", "PENDING", "Y", "P1", "5")]),
 ("SWE1-KeyInsyall-009", [
  ("keys in VERIFICATION_REQUIRED state; the crypto service refuses the operation", "key state", "PENDING", "Y", "P1", "1,3"),
  ("keys in INSTALLED state; sign, verify, encrypt and decrypt succeed", "key state", "PENDING", "Y", "P1", "1,3")]),
 ("SWE1-KeyInsyall-010", [
  ("authorized application; access is granted and the operation completes", "client authorization", "PENDING", "Y", "P1", "1,3"),
  ("unauthorized application; the request is refused and a security violation is logged", "client authorization", "PENDING", "Y", "P1", "1,3,4")]),
 ("SWE1-KeyInsyall-011", [
  ("installation completed; the status is INSTALLED (2)", "queried status", "ADB/PENDING", "Y", "P1", "1"),
  ("unsuccessful installation; the status is ERROR (3)", "queried status", "ADB/PENDING", "Y", "P1", "1,3")]),
 ("SWE1-KeyInsyall-012", [
  ("no SELinux denial is recorded while KeyInstall runs in enforcing mode", "compliance check", "ADB", "N", "P2", "1"),
  ("an Android.bp build file is present and functional", "compliance check", "PENDING", "Y", "P2", "1"),
  ("static analysis passes CERT and CWE compliance", "compliance check", "PENDING", "Y", "P2", "1")]),
 ("SWE1-KeyInsyall-013", [
  ("RAM usage and the oemkeys partition size stay within the stated targets", "resource target", "ADB", "N", "P2", "1,4")]),

 ("SYSAD_SEC_ECUCERT_ECUCERT_API", [
  ("verification function returns OK for an unchanged certificate file", "verification status", "ADB", "N", "P1", "1,3"),
  ("verification function returns FAIL for a changed certificate file", "verification status", "ADB", "N", "P1", "1,3")]),
 ("SYSAD_SEC_ECUCERT_ECUCERT_SERVICE", [
  ("service returns OK for an unchanged certificate file", "verification status", "ADB", "N", "P1", "1,3"),
  ("service returns FAIL for a changed certificate file", "verification status", "ADB", "N", "P1", "1,3")]),
 ("SYSAD_SEC_ECUCERT_DIAG", [
  ("diagnostic interface handles an input parameter at the range boundary", "input range", "UDS", "N", "P1", "1"),
  ("diagnostic interface reports a successful verification", "verification status", "UDS", "N", "P1", "1,3"),
  ("diagnostic interface reports a failed verification", "verification status", "UDS/PENDING", "Y", "P1", "1,3")]),
 ("SYSAD_SEC_ECUCERT_DEALER", [
  ("dealer service updates the current key and returns the status", "key update", "UI/PENDING", "Y", "P1", "1"),
  ("decryption with a different key is rejected", "key mismatch", "UI/PENDING", "Y", "P1", "1,3")]),
 ("SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCSR_INTF", [
  ("CSR is read over DID 2965 and exported to a file", "export target", "UDS/ADB/HOST", "N", "P1", "1")]),
 ("SYSAD_SEC_ECUCERT_ECUCERT_SRV_EXPORTCERT_INTF", [
  ("ECU certificate is exported to a file", "export target", "ADB/HOST", "N", "P1", "1")]),
 ("SYSAD_SEC_ECUCERT_ECUCERT_SRV_IMPORTCERT_INTF", [
  ("ECU certificate is imported to the device", "import target", "ADB", "N", "P1", "1")]),

 ("SWE1-SRA-SECURITY-SWDL-003", [
  ("decryption interface handles an input parameter at the range boundary", "input range", "PENDING", "Y", "P2", "1"),
  ("decryption of a valid package succeeds", "decryption outcome", "PENDING", "Y", "P2", "1,3"),
  ("decryption of an invalid package fails", "decryption outcome", "PENDING", "Y", "P2", "1,3")]),
 ("SWE1-SRA-SECURITY-SWDL-004", [
  ("verification interface handles an input parameter at the range boundary", "input range", "PENDING", "Y", "P0", "1"),
  ("verification of a correctly signed package succeeds", "verification outcome", "PENDING", "Y", "P0", "1,3"),
  ("verification of a tampered package fails", "verification outcome", "PENDING", "Y", "P0", "1,3")]),

 ("SWE1-SAM-0002", [
  ("DebugAuth runs as a native daemon after the head unit boots", "process form", "PHYS/ADB", "N", "P2", "1")]),
 ("SWE1-SAM-0004", [
  ("AuthData verification fails; the error is logged and the installed AuthData is retained", "verification outcome", "ADB/PHYS", "N", "P0", "1,4")]),
 ("SWE1-SAM-0007", [
  ("SAM certificate is x509 PEM, anchors to the OEM issued root, and carries the SAM subject", "certificate validity", "HOST/ADB", "N", "P0", "1,4"),
  ("SAM certificate does not anchor to the OEM issued root; verification fails", "certificate validity", "HOST/PENDING", "Y", "P0", "3")]),
 ("SWE1-SAM-0015", [
  ("sequence ID is included, logged and incremented when a status message is sent", "message content", "ADB", "N", "P1", "1,4")]),
 ("SWE1-SAM-0018", [
  ("AuthData files are stored in the data partition and labeled by SELinux", "storage location", "ADB", "N", "P2", "1,4")]),
]


def main() -> int:
    rows, seen = [], {}
    for swe1, sibs in SPEC:
        lowers = [s[0] for s in sibs]
        assert len(lowers) == len(set(lowers)), f"{swe1}: 括號下半重複（規則 6）"
        prio = {s[4] for s in sibs}
        assert len(prio) == 1, f"{swe1}: sibling priority 不一致（R-SEC16）"
        for i, (lower, axis, ch, pend, pr, rule) in enumerate(sibs, 1):
            rows.append([swe1, str(i), lower, axis, ch, pend, pr, rule])
        seen[swe1] = len(sibs)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "sibling_no", "lower_half(English)", "axis",
                    "trigger_channel", "pending_expected", "priority", "rule"])
        w.writerows(rows)

    tm = {r["swe1_id"]: r for r in csv.DictReader(
        (ROOT / "features/security/data/trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t")}
    per = Counter()
    for swe1, n in seen.items():
        per[tm[swe1]["component"]] += n
    print(f"sibling_plan.tsv {len(rows)} 列（SWE1 {len(seen)} 列）")
    print("  逐 Test Group:", dict(per))
    print("  priority:", dict(Counter(r[6] for r in rows)))
    print("  pending_expected=Y:", sum(1 for r in rows if r[5] == "Y"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
