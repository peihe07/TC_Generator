#!/usr/bin/env python3
"""Layer 2 逐列歸屬 —— 下放包 §5 案 A 之表逐字落地（任務 4）。

**不自行改 Layer 2 名稱**；只把 §5 表之歸屬展開為逐列檔，並以 trace_matrix
回填 leaf 數與 ccvr_batch 數。歸屬與 §5 不一致者於 `notes` 欄逐筆記明。

產物：features/security/data/layer2_assign.tsv
欄：component | test_set | swe1_id | ccvr_batch | verification_method | note
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features" / "security" / "data"

# 下放包 §5 Layer 2 表（案 A）。key = (Test Group, Test Set)，value = SWE1 序號尾碼。
# ECUCert 以 037 之 Excel 列號（R9~R21）指涉 —— 該本 A 欄全空（R-SEC3(b)）。
ASSIGN = {
    ("Cert Provider", "Chain Verification"): ["001"],
    ("Cert Provider", "Field Matching"): ["002", "003", "011"],
    ("Cert Provider", "Revocation"): ["004", "005"],
    ("Cert Provider", "Trust Store"): ["007", "009"],
    ("Cert Provider", "Client Interface"): ["008"],
    ("Cert Provider", "Service Robustness"): ["006", "010"],
    ("Key Install", "Temporary Key"): ["001"],
    ("Key Install", "Installation"): ["002", "003", "004", "007"],
    ("Key Install", "Overwrite Protection"): ["005"],
    ("Key Install", "Install State"): ["006", "011"],
    ("Key Install", "Persistence"): ["008"],
    ("Key Install", "Crypto Service"): ["009", "010"],
    ("Key Install", "Platform Compliance"): ["012", "013"],
    ("SAM", "AuthData Reception"): ["0003"],
    ("SAM", "AuthData Verification"): ["0005", "0006", "0007", "0010", "0012"],
    ("SAM", "Installation"): ["0009", "0011", "0018"],
    ("SAM", "Target Notification"): ["0013", "0014", "0015", "0016", "0017"],
    ("SAM", "Error Handling"): ["0004"],
    ("SAM", "Service Environment"): ["0001", "0002", "0008", "0019"],
    ("ECU Cert", "Certificate Lifecycle"): ["R18", "R19", "R20", "R21"],
    ("ECU Cert", "Verification"): ["R9", "R10", "R11"],
    ("ECU Cert", "Diagnostic Access"): ["R12", "R13"],
    ("ECU Cert", "Internal Interfaces"): ["R14", "R15", "R16", "R17"],
    ("SWDL Secure Lib", "Package Decryption"): ["003"],
    ("SWDL Secure Lib", "Signature Verification"): ["004"],
    ("SWDL Secure Lib", "Key Retrieval"): ["002", "005"],
    ("SWDL Secure Lib", "Library Scope"): ["001"],
    ("Log Encrypt", "Encryption Procedure"): ["006"],
    ("Log Encrypt", "Encryption Services"): ["001", "002", "003", "004", "005", "007", "008", "009"],
}

GROUP_OF_COMPONENT = {
    "CertProvider": "Cert Provider",
    "KeyInstall": "Key Install",
    "SAM": "SAM",
    "ECUCert": "ECU Cert",
    "SwdlSecureLib": "SWDL Secure Lib",
    "libLogEncrypt": "Log Encrypt",
}


def tail(row: dict) -> str:
    if row["component"] == "ECUCert":
        return f"R{row['excel_row']}"
    return row["swe1_id"].rsplit("-", 1)[-1]


def main() -> int:
    rows = list(csv.DictReader((DATA / "trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t"))
    lookup = {}
    for (group, tset), tails in ASSIGN.items():
        for t in tails:
            lookup[(group, t)] = tset

    out, unassigned = [], []
    seen = Counter()
    for r in rows:
        group = GROUP_OF_COMPONENT[r["component"]]
        tset = lookup.get((group, tail(r)))
        note = ""
        if tset is None:
            tset = "(未歸屬)"
            note = "§5 表未列；待 Pei 補"
            unassigned.append(r["swe1_id"])
        seen[(group, tset)] += 1
        out.append([group, tset, r["swe1_id"], r["ccvr_batch"], r["verification_method"], note])

    with (DATA / "layer2_assign.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["test_group", "test_set", "swe1_id", "ccvr_batch", "verification_method", "note"])
        w.writerows(out)

    # §5 表之 leaf 數對帳
    expected = {(g, s): len(v) for (g, s), v in ASSIGN.items()}
    print(f"layer2_assign.tsv {len(out)} 列；未歸屬 {len(unassigned)}")
    bad = [(k, expected[k], seen.get(k, 0)) for k in expected if expected[k] != seen.get(k, 0)]
    if bad:
        for k, e, a in bad:
            print(f"  ✗ {k}: §5 表 {e} 列，實測 {a} 列")
    else:
        print(f"  ✓ {len(ASSIGN)} 組 Test Set 之 leaf 數與 §5 表逐組相符")

    batch = defaultdict(Counter)
    for g, s, _sid, b, _vm, _n in out:
        batch[(g, s)][b] += 1
    print()
    print("| Test Group | Test Set | leaf | batch 1 | batch 2 |")
    print("|---|---|---:|---:|---:|")
    for (g, s) in ASSIGN:
        c = batch[(g, s)]
        print(f"| {g} | `{s}` | {sum(c.values())} | {c['1']} | {c['2']} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
