#!/usr/bin/env python3
"""batch 3（SEC-11 §2）—— DEFERRED 19 列依 R-SEC20 文件審查定式產出。

R-SEC23：`disposition = D` 之 19 列先行產出，使 70 列全覆蓋；上游回 DR-a／i／r 後再 Revise。
要件（`req`）與 artifact 皆取 037 `Verification Criteria`／`Requirement Description` **逐字**
（中英並列者取英文，R-SEC15(f) amend）；`rule` 欄記其出處。
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

_s = importlib.util.spec_from_file_location("g1", Path(__file__).parent / "gen_batch1.py")
g1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(g1)
_t = importlib.util.spec_from_file_location("btm", Path(__file__).parent / "build_trace_matrix.py")
btm = importlib.util.module_from_spec(_t)
_t.loader.exec_module(btm)

DATA = ROOT / "features" / "security" / "data"
SB = ROOT / "features" / "security" / "sandbox"
OUT_DIR = ROOT / "features" / "security" / "sandbox" / "batch3"
VER = os.environ.get("SEC_VER", "v06")
OUT_XLSX = OUT_DIR / "security_batch3_v01.xlsx"

# R-SEC20(d) 之 `<component>`：037 之元件寫法
COMPONENT = {"libLogEncrypt": "Log Encryption", "SAM": "DebugAuth",
             "SwdlSecureLib": "SwdlSecureLib", "ECUCert": "ECU Cert"}
def start_numbers() -> dict[str, int]:
    """各組續號之起點 = batch1／batch2 之現行末號（SEC-20：原硬編 12 使 ECUC 與 batch1 撞號）。"""
    import re as _re
    mx: dict[str, int] = {}
    for d in ("batch1", "batch2"):
        for f in (SB / d).glob("NR1L-*.json"):
            m = _re.match(r"NR1L-([A-Z]+)-(\d{3})", f.stem)
            grp = {v: k for k, v in g1.ABBR.items()}[m.group(1)]
            mx[grp] = max(mx.get(grp, 0), int(m.group(2)))
    return mx

# (swe1_id, sibling_no, artifact, 037 逐字要件, lower_half, axis, rule)
PLAN: list[tuple[str, int, str, str, str, str, str]] = [
    ("SWE1-LOGENC-001", 1, "the Log Encrypt source code",
     "the code is integrated with Android 14",
     "the source code is integrated with Android 14", "build integration", "VC THEN 3."),
    ("SWE1-LOGENC-002", 1, "the project build environment",
     "logdog could link to Log Encryption without link error",
     "logdog links to Log Encryption without link error", "link integration", "VC THEN 3."),
    ("SWE1-LOGENC-003", 1, "the LogEncrypt library",
     "LogEncrypt library should provide API for LogDog: encryptLogFile(const std::string& "
     "plainLogFilename, const std::string& protectedLogFilename, const std::string& "
     "protectedKeyFilename) to encrypt log files",
     "the encryptLogFile API is provided for LogDog", "API provision", "VC item 1"),
    ("SWE1-LOGENC-004", 1, "the Log Encryption source code",
     "AES is used for symmetric encryption of log files",
     "AES is used for symmetric encryption", "symmetric algorithm", "VC THEN 3.1"),
    ("SWE1-LOGENC-004", 2, "the Log Encryption source code",
     "LogEncrypt feature uses OpenSSL library primitives for generating unique AES-256 "
     "symmetric keys to encrypt log files",
     "unique AES-256 keys are generated with OpenSSL primitives", "key generation source",
     "VC trailing sentence (independent requirement outside THEN)"),
    ("SWE1-LOGENC-005", 1, "the Log Encryption source code",
     "Log Encrypt will get RSA symmetric key to encrypt symmetric key",
     "the symmetric key is encrypted with the RSA key", "asymmetric wrapping", "VC THEN 3.1"),
    ("SWE1-LOGENC-007", 1, "the Log Encryption source code",
     "AES key is get from BoringSSL",
     "the AES key is obtained from BoringSSL", "AES key source", "VC THEN 3."),
    ("SWE1-LOGENC-008", 1, "the Log Encryption source code",
     "AES key is get from KeyInstall",
     "the key is obtained from KeyInstall", "RSA key source", "VC THEN 3."),
    ("SWE1-LOGENC-009", 1, "the Log Encryption source code",
     "there exists a interface for file operation",
     "a file operation interface exists", "file interface", "VC THEN 3."),
    ("SWE1-SAM-0001", 1, "the DebugAuth source code",
     "the code is integrated with Android 14",
     "the source code is integrated with Android 14", "build integration", "VC THEN 3.1"),
    ("SWE1-SAM-0019", 1, "the DebugAuth source code about AuthData checking",
     "DebugAuth is using assigned SW components",
     "the assigned SW components are used", "external component usage", "VC THEN 3.1"),
    ("SWE1-SRA-SECURITY-SWDL-001", 1, "the SwdlSecureLib library",
     "keep SWDL config", "the SWDL configuration is kept", "config retention", "VC item 1"),
    ("SWE1-SRA-SECURITY-SWDL-001", 2, "the SwdlSecureLib library",
     "control KEY / certificate interface", "the KEY / certificate interface is controlled",
     "key and certificate control", "VC item 2"),
    ("SWE1-SRA-SECURITY-SWDL-002", 1, "the key agent implementation",
     "interact to KEY and certificate provider",
     "the key and certificate provider is used", "provider interaction", "VC item 1"),
    ("SWE1-SRA-SECURITY-SWDL-005", 1, "the client-side key update interface",
     "update current key and check the return value",
     "the current key is updated and the return value is checked", "key update", "VC item 1"),
    ("SWE1-SRA-SECURITY-SWDL-005", 2, "the client-side key update interface",
     "use differ key to decrypt", "a different key is used for decryption",
     "key mismatch handling", "VC item 2"),
    ("SYSAD_SEC_ECUCERT_ECUCERT_SERVICE_BINDER", 1, "the ECUCertService AIDL interface",
     "Client can communicate to service through binder",
     "the client communicates with the service through the binder", "IPC provision", "VC"),
    ("SYSAD_SEC_ECUCERT_ECUONLINE_BINDER", 1, "the ECUOnlineService AIDL interface",
     "Client can communicate to service through binder",
     "the client communicates with the service through the binder", "IPC provision", "VC"),
    ("SYSAD_SEC_ECUCERT_ECUCERT_JNI", 1, "the ECU Cert JNI layer",
     "jbyteArray and jstring are correctly converted to uint8_t* and std::string without "
     "memory leaks",
     "the Java types are converted without memory leaks", "type conversion", "VC (English sentence)"),
    ("SYSAD_SEC_ECUCERT_ECUCERT_STORAGE_IO", 1,
     "the Cert Store file path access implementation",
     "jbyteArray and jstring are correctly converted to uint8_t* and std::string without "
     "memory leaks",
     "the Java types are converted without memory leaks", "type conversion",
     "VC (English sentence; identical to the JNI row in 037 — see SEC-11 submission)"),
    ("SYSAD_SEC_ECUCERT_ECUONLINE", 1, "the ECU Online module",
     "input parameter range test", "the input parameter range is handled",
     "parameter range", "VC item 1"),
    ("SYSAD_SEC_ECUCERT_ECUONLINE", 2, "the ECU Online module",
     "test interface can handle decrypt data pass and failed",
     "both decrypt pass and decrypt failure are handled", "decrypt outcome", "VC item 2"),
    ("SYSAD_SEC_ECUCERT_ECUONLINE_DOWNLOADCERT_INTF", 1, "the certificate download interface",
     "Connect to STLA", "the STLA connection is provided", "backend connection", "VC item 1"),
    ("SYSAD_SEC_ECUCERT_ECUONLINE_DOWNLOADCERT_INTF", 2, "the certificate download interface",
     "Download ECU ID", "the ECU ID download is provided", "download", "VC item 2"),
]


def d_first_map() -> dict[str, str]:
    """037 D 欄首句（與 `gen_batch1.py` 同法）。"""
    out: dict[str, str] = {}
    for doc_id, _comp in btm.SWE1_BOOKS:
        wb = openpyxl.load_workbook(btm.only(doc_id, "*.xlsx"), read_only=True, data_only=True)
        grid = list(wb["Analysis Report"].iter_rows(values_only=True))
        for row in grid[8:]:
            a = "" if row[0] is None else str(row[0]).strip()
            b = "" if row[1] is None else str(row[1]).strip()
            if not a and not b:
                continue
            key = a or btm.split_source_ids(b)[0].replace(" ", "")
            out[key] = g1.first_sentence(str(row[3] or ""))
        wb.close()
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tm = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t")}
    l2 = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "layer2_assign.tsv").open(encoding="utf-8"), delimiter="\t")}
    d_first = d_first_map()
    spec_ref = g1.spec_ref_values()

    # `sibling_plan_deferred.tsv`（欄同 SEC-04 4.2 ＋ `artifact`／`requirement`）
    with (DATA / "sibling_plan_deferred.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "sibling_no", "lower_half(English)", "axis",
                    "trigger_channel", "pending_expected", "priority", "rule",
                    "artifact", "requirement(037 verbatim)"])
        for swe1, no, art, req, lower, axis, rule in PLAN:
            w.writerow([swe1, no, lower, axis, "DOC", "N", "P2", f"R-SEC23(b) {rule}",
                        art, req])

    wb = openpyxl.load_workbook(g1.TEMPLATE)
    ws = wb[g1.SHEET]
    counter: Counter = Counter(start_numbers())
    rows = []
    order = [r["swe1_id"] for r in csv.DictReader(
        (DATA / "layer2_assign.tsv").open(encoding="utf-8"), delimiter="\t")]
    rank = {s: i for i, s in enumerate(order)}
    plan = sorted(PLAN, key=lambda p: (rank[p[0]], p[1]))
    for n, (swe1, no, art, req, lower, axis, rule) in enumerate(plan):
        comp = tm[swe1]["component"]
        group = g1.GROUP[comp]
        counter[group] += 1
        tc_id = f"NR1L-{g1.ABBR[group]}-{counter[group]:03d}"
        steps = [g1.doc_obtain(art), g1.doc_review(art, req)]
        proc, er = [], []
        for i, (desc, cmd, exp) in enumerate(steps, 1):
            proc.append(f"{i}. {desc}")
            if cmd:
                proc.append(cmd)
            er.append(f"{i}. {exp}")
        remarks = [
            "verification: document review (R-SEC23; upstream DR-a/i/r pending)",
            f"source: 037 {swe1} Requirement Description and Verification Criteria",
            f"sibling axis: {axis}; rule R-SEC23(b) {rule}",
            f'channel_feasible: {tm[swe1]["channel_feasible"]}',
        ]
        if tm[swe1]["nrl_swe1"] != "-":
            remarks.insert(2, f'Polarion: {tm[swe1]["nrl_swe1"]}')
        if swe1.startswith("SYSAD_SEC_ECUCERT"):
            remarks.append("SWE ID pending DR-a; Source Requirement ID used per R-SEC3(b)")
        if swe1 in g1.CONFLICT_NOTE:                              # R-SEC22(a)
            remarks.append(g1.CONFLICT_NOTE[swe1])
        r = {"req_id": swe1, "tc_id": tc_id, "test_group": group,
             "test_set": l2[swe1]["test_set"],
             "test_item": f"{d_first[swe1]}\n({lower} (document review))",
             "pre": f"1. Access to the RD build environment for {COMPONENT[comp]} is granted",
             "input": "NA", "proc": "\n".join(proc), "er": "\n".join(er),
             "spec": spec_ref[swe1],
             "tc_ref": "NEW", "priority": "P2", "design": g1.FUNC, "fs": "No",
             "author": "PeiPYHsu", "remarks": "\n".join(remarks)}
        row = g1.FIRST_ROW + n
        for key, col in g1.COLS.items():
            ws[f"{col}{row}"] = r[key]
        for col, val in zip(g1.VM_COLS, g1.VM_VALUES):
            ws[f"{col}{row}"] = val
        (OUT_DIR / f"{tc_id}.json").write_text(
            json.dumps({**r, "vehicle_model": dict(zip(g1.VM_NAMES, g1.VM_VALUES)),
                        "placeholders": []}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        rows.append(r)

    report = surgical_save(wb, g1.TEMPLATE, OUT_XLSX)
    print(f"batch3：{len(rows)} TC → {OUT_XLSX.relative_to(ROOT)}")
    print("  逐組:", dict(Counter(r["test_group"] for r in rows)))
    print("  涉及 037 列:", len({r["req_id"] for r in rows}))
    print("  PENDING 行", sum(1 for r in rows
                              for line in (r["proc"] + r["er"]).splitlines()
                              if re.search(r"PENDING:", line)))
    print("  surgical:", {k: v for k, v in report.items() if k != "members_patched"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
