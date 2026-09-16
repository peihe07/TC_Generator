#!/usr/bin/env python3
"""既有素材之指令／路徑／值全表（下放包 addendum §3「任務 3-7 改為必交」）。

R-SEC4(a) 五類落地來源逐一掃描，逐字（verbatim）抽出可入 Procedure／ER 之
資產，供 profile [ADD §5.3] 常數候選與 DR 清單使用。

產物：features/security/data/step_assets.tsv
欄：asset | value(verbatim) | source | source_loc | used_by_swe1
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
OUT = ROOT / "features" / "security" / "data"

_spec = importlib.util.spec_from_file_location("btm", HERE.parent / "build_trace_matrix.py")
btm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(btm)

# 資產類型 → 正則。逐字抽出，不正規化（IN §8.4.1）。
PATTERNS = [
    ("cmd_adb", re.compile(r"adb\s+(?:-s\s+\S+\s+)?shell[^\n]*")),
    ("cmd_openssl", re.compile(r"openssl\s+[^\n]*")),
    ("cmd_od", re.compile(r"od\s+-t\s+[^\n]*")),
    ("cmd_shell", re.compile(r"\b(?:getsslog|logdecrypt_Ver2\.sh|logcat)[^\n]*")),
    ("path", re.compile(r"(?<![\w./])/(?:[A-Za-z0-9_.@{}\[\]-]+/)*[A-Za-z0-9_.@{}\[\]-]+")),
    ("filename", re.compile(r"\b[A-Za-z0-9_.<>{}-]+\.(?:sh|enc|apk|der|pem|crt|cer|txt|bin|zip|img)\b")),
    ("state_value", re.compile(r"\b(?:installstate|ecucertstatus|seqId|status)\b[^\n]{0,60}")),
    ("hex_blob", re.compile(r"\b(?:[0-9a-fA-F]{4}\s+){3,}[0-9a-fA-F]{4}\b")),
    ("junit_method", re.compile(r"\b[a-z][A-Za-z]*(?:Test|Cert)[A-Za-z]*\b")),
    ("placeholder", re.compile(r"<[A-Za-z_ ]+>|\{[A-Z_]+\}|HUssss_YYYYMMDD_HHMMSS_XXXX")),
]

NOISE = re.compile(r"^/(?:\d+|[A-Za-z]{1,2})$")

# R-SEC7(a)(c)（_E §1）：執行通道與觀察手段之閉合清單。每筆資產標其所屬。
CHANNEL_OF = {
    "cmd_adb": "ADB", "cmd_od": "ADB", "cmd_shell": "ADB",
    "cmd_openssl": "HOST",
    "path": "-", "filename": "-", "state_value": "-", "hex_blob": "-",
    "placeholder": "-", "junit_method": "ADB",
}
# 觀察手段以值之形態判：logcat/log → LOG；od/cat/ls → FILE；UDS bytes → UDS；
# instrument → RC；openssl → HOST；Send CAN → CAN。
OBSERVE_RULES = [
    ("RC", re.compile(r"am instrument")),
    ("LOG", re.compile(r"logcat|getsslog|MLog\.|Tag:|logdog", re.I)),
    ("UDS", re.compile(r"^\$?\s*(?:22|2E|31|10|27|19)\s+[0-9A-Fa-f]{2}")),
    ("HOST", re.compile(r"openssl|logdecrypt_Ver2\.sh")),
    ("FILE", re.compile(r"\bod -t x1\b|adb shell (?:cat|ls)|/(?:data|mnt|odm|vendor)/")),
    ("CAN", re.compile(r"Send CAN:")),
]


def classify(kind: str, value: str) -> tuple[str, str]:
    """→ (channel, observe)；無法歸類者回 `-`。"""
    ch = CHANNEL_OF.get(kind, "-")
    if ch == "-" and re.match(r"^\$?\s*(?:22|2E|31|10|27|19)\s+[0-9A-Fa-f]{2}", value):
        ch = "UDS"
    ob = "-"
    for name, rx in OBSERVE_RULES:
        if rx.search(value):
            ob = name
            break
    return ch, ob


# _E §2：既有素材中可直接沿用之通道句，逐字登錄（該表之值不經正則抽取，直接入表）。
CHANNEL_SENTENCES = [
    ("channel_line", "$ adb root", "R1L-SWQT", "Diag基本機能 00053", "ADB", "-"),
    ("channel_line", "$ adb shell am instrument -w -e class com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test.CertProviderServiceManagerTest#<method> com.mitsubishielectric.ahu.efw.lib.melcocertprovider.libcertproviderservice.test/androidx.test.runner.AndroidJUnitRunner", "APK", "Test_Items.txt", "ADB", "RC"),
    ("channel_line", "$ adb pull /data/misc/ecuidentity/ecu.crt", "PDF", "ECU Cert Test Steps", "ADB", "FILE"),
    ("channel_line", "$ adb push ecu.cacert /data/misc/ecuidentity/", "PDF", "ECU Cert Test Steps", "ADB", "FILE"),
    ("channel_line", "$ adb shell \"printf '\\x01' > /mnt/vendor/oemkeys/ecu/state/ecucertstatus\"", "PDF", "ECU Cert Test Steps", "ADB", "FILE"),
    ("channel_line", "$ adb shell \"od -t x1 /mnt/vendor/oemkeys/ecu/state/ecucertstatus\"", "PDF", "ECU Cert Test Steps", "ADB", "FILE"),
    ("channel_line", "$ adb shell getsslog", "VC", "SWE1-LOGENC-006", "ADB", "LOG"),
    ("channel_line", "$ ./logdecrypt_Ver2.sh HUssss_YYYYMMDD_HHMMSS_XXXX.enc HUssss_YYYYMMDD_HHMMSS_XXXX_enckey.enc", "VC", "SWE1-LOGENC-006", "HOST", "HOST"),
    ("channel_line", "$ openssl verify -verbose -CAfile RootCert.pem -untrusted L1.pem -untrusted L2.pem -untrusted L3.pem SAMcert.pem", "VC", "SWE1-CertProvider-001/004", "HOST", "HOST"),
    ("channel_line", "$ openssl x509 -in leaf.crt -text", "VC", "SWE1-CertProvider-002/003", "HOST", "HOST"),
    ("channel_line", "$ adb logcat -c", "CS98", "Cert Val CS.98", "ADB", "LOG"),
    ("channel_line", "$ adb shell pm list instrumentation | grep melcocertprovider", "CS98", "Cert Val CS.98", "ADB", "RC"),
    ("channel_line", "$ 22 FF 02", "R1L-SWQT", "22345/22346", "UDS", "UDS"),
    ("channel_line", "$ 22 29 65", "R1L-SWQT", "22403/22404", "UDS", "UDS"),
    ("channel_line", "$ 10 60", "R1L-SWQT", "session 切換（ENTER_SUPPLIER_SESSION）", "UDS", "UDS"),
    ("channel_line", "$ 22 F1 B6", "CS00102", "5.2.1.44", "UDS", "UDS"),
    ("channel_line", "$ 22 20 31", "CS00102", "5.2.2.43", "UDS", "UDS"),
    ("channel_line", "$ 22 29 55", "CS00102", "5.2.2.62", "UDS", "UDS"),
    ("channel_line", "$ 22 29 5D", "CS00102", "5.2.2.70", "UDS", "UDS"),
    ("channel_line", "$ 22 29 5E", "CS00102", "5.2.2.71", "UDS", "UDS"),
    ("channel_line", "$ 31 01 F0 00", "CS00102", "5.2.7.19", "UDS", "UDS"),
    ("channel_line", "$ 31 01 FF 01", "CS00102", "5.2.7.23", "UDS", "UDS"),
    ("channel_line", "$ 2E 28 50 05", "VHAL-R5", "§2.4（Atl-Hi；03 = Atl-Mid）", "UDS", "UDS"),
    ("channel_line", "Insert USB drive containing <資產名> into HU USB port", "VC", "SWE1-KeyInsyall-002/003/007", "PHYS", "-"),
    ("channel_line", "Insert SAM dongle", "VC", "SWE1-LOGENC-006／SAM 群", "PHYS", "-"),
    ("channel_line", "Power cycle HU (IGN OFF → IGN ON)", "VC", "SWE1-SAM-0017", "PHYS", "-"),
    ("channel_line", "Send CAN: BCM_FD_10.CmdIgnSts = <raw> (<label>)", "VHAL-R5", "§2.4 IGNITION_STATE", "CAN", "CAN"),
    ("channel_line", "$ adb shell \"ps -A | grep keyinstall\"", "R1L-SWQT", "Diag基本機能 00053", "ADB", "RC"),
]


def scan(text: str, source: str, loc: str, swe1: str, sink: dict) -> None:
    for kind, rx in PATTERNS:
        for hit in rx.findall(text or ""):
            val = hit.strip().rstrip(".,;:）)")
            if not val or NOISE.match(val) or len(val) < 3:
                continue
            key = (kind, val)
            sink[key]["source"].add(source)
            sink[key]["loc"].add(loc)
            if swe1:
                sink[key]["swe1"].add(swe1)


# _F §2：CertProfile（Code Signing 樹）之欄位斷言，逐字入表（R-SEC4(a) 第 8 類）。
# 只適用 Code Signing 場景（FOTA MCPU/VCPU、SWDL、Second Party）；SAM 樹與 ECU Identity
# 樹另有 profile，未到手（DR-SEC-q）。BETA/preprod ROW 本，PROD 樹之 CN 與 CDP 必不同。
CERTPROFILE_ASSETS = [
    ("cert_field", "BETA_ROW_VHL_ROOT_G1", "CertProfile", "CertProfile:r11", "HOST", "HOST"),
    ("cert_field", "BETA_ROW_CS_SUBCA_G1", "CertProfile", "CertProfile:r11,r18", "HOST", "HOST"),
    ("cert_field", "CS_{SupplierID}_{Node}_{OPT - chipset}_ {ECUSWmodule}", "CertProfile", "CertProfile:r18", "HOST", "HOST"),
    ("cert_field", "Stellantis N.V.", "CertProfile", "CertProfile:r9,r16", "HOST", "HOST"),
    ("cert_field", "99991231235959Z", "CertProfile", "CertProfile:r12", "HOST", "HOST"),
    ("cert_field", "2 (X.509v3)", "CertProfile", "CertProfile:r3", "HOST", "HOST"),
    ("cert_field", "ecdsa-with-SHA384", "CertProfile", "CertProfile:r5,r44（L1）", "HOST", "HOST"),
    ("cert_field", "ecdsa-with-SHA256", "CertProfile", "CertProfile:r5,r44（leaf）", "HOST", "HOST"),
    ("cert_field", "ECParameters (namedCurve secp256r1)", "CertProfile", "CertProfile:r22", "HOST", "HOST"),
    ("cert_field", "key size 256", "CertProfile", "CertProfile:r20", "HOST", "HOST"),
    ("cert_field", "keyCertSign / cRLSign（L1，critical）", "CertProfile", "CertProfile:r25,r31,r32", "HOST", "HOST"),
    ("cert_field", "digitalSignature（leaf，critical）", "CertProfile", "CertProfile:r25,r26", "HOST", "HOST"),
    ("cert_field", "BasicConstraints CA:TRUE, pathlen:0（critical，L1）", "CertProfile", "CertProfile:r37,r39", "HOST", "HOST"),
    ("cert_field", "CertificatePolicies（critical）OID 1.3.6.1.4.1.57872.<…>", "CertProfile", "CertProfile:r36", "HOST", "HOST"),
    ("cert_field", "http://vpki.preprod.stellantis.com/crls/STLAroot", "CertProfile", "CertProfile:r40（L1）", "HOST", "HOST"),
    ("cert_field", "http://vpki.preprod.stellantis.com/crls/L1CS", "CertProfile", "CertProfile:r40（leaf）", "HOST", "HOST"),
    ("cert_field", "http://vpki.preprod.stellantis.com/aia/L1CS", "CertProfile", "CertProfile:r43", "HOST", "HOST"),
    ("channel_line", "$ openssl x509 -in <L1> -text", "CertProfile", "_F §2 ER 觀察手段", "HOST", "HOST"),
    ("channel_line", "$ 19 02 FF", "DTCMatrix", "_F §4（讀 DTC；ER 以 3-byte HEX 對照 J2012）", "UDS", "UDS"),
    ("dtc_precond", "EC1: DTC Setting Enabled", "DTCMatrix", "DTCs for R1H", "-", "-"),
    ("dtc_precond", "EC2: $PowerMode$ = [IGN_RUN]", "DTCMatrix", "DTCs for R1H", "-", "-"),
    ("dtc_precond", "EC4: [10.0] <= $BatteryVoltage$ <= [16.0]", "DTCMatrix", "DTCs for R1H", "-", "-"),
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    sink = defaultdict(lambda: {"source": set(), "loc": set(), "swe1": set()})

    # (a)1 —— 037 之 Verification Criteria
    for row in btm.read_swe1():
        scan(row["verification_criteria"], "VC",
             f"{row['swe1_file']}!Analysis Report!R{row['excel_row']}", row["swe1_id"], sink)

    # (a)2 —— Test_Items.txt 之 15 條 JUnit 方法 ＋ 全式指令
    ti = btm.only("ccvr_cs98_test_items", "*.txt").read_text(encoding="utf-8")
    scan(ti, "APK", "Test_Items.txt", "", sink)

    # (a)3 —— ECU Cert Test Steps PDF 六步
    pdf_path = btm.only("ccvr_ecu_cert_test_steps_20260826", "*.pdf")
    with pdfplumber.open(pdf_path) as pdf:
        pages = len(pdf.pages)
        for n, page in enumerate(pdf.pages, start=1):
            scan(page.extract_text() or "", "PDF", f"ECU Cert Test Steps p{n}", "", sink)

    # (a)4 —— SYS2_Mapped 之 Cert Val CS.98 STEPS ／ ECU ID CS.165 三欄
    for key, meta in btm.read_cs98_steps().items():
        scan(meta["steps"], "CS98", f"Cert Val CS.98!R{meta['row']}", "", sink)
    for key, meta in btm.read_cs165_steps().items():
        scan(meta["body"], "CS165", f"ECU ID CS.165!R{meta['row']}", "", sink)

    # (a)5 —— SYS3 SYSAD 之 Interface 表三欄
    import docx
    for doc_id in btm.SYSAD_BOOKS:
        doc = docx.Document(str(btm.only(doc_id, "*.docx")))
        book = doc_id.replace("sys3_sysad_", "")
        for ti_, tbl in enumerate(doc.tables):
            cells = [[c.text.strip() for c in r.cells] for r in tbl.rows]
            if not cells or not cells[0] or not cells[0][0].startswith("SYSAD_ID"):
                continue
            for r in cells:
                lab = re.sub(r"\s+", " ", r[0])
                if lab.startswith(("Flow chart", "Input Criteria", "Output Criteria")):
                    scan(" ".join(r[1:]), "SYSAD", f"{book}!T{ti_}", "", sink)

    extra = list(CHANNEL_SENTENCES) + list(CERTPROFILE_ASSETS)
    rows = sorted(((k[0], k[1], "、".join(sorted(v["source"])),
                    "；".join(sorted(v["loc"])[:4]) + ("…" if len(v["loc"]) > 4 else ""),
                    "；".join(sorted(v["swe1"])))
                   for k, v in sink.items()))
    out_rows = []
    for kind, val, src, loc, used in rows:
        ch, ob = classify(kind, val)
        out_rows.append([kind, val, src, loc, used, ch, ob])
    for kind, val, src, loc, ch, ob in extra:
        out_rows.append([kind, val, src, loc, "", ch, ob])
    with (OUT / "step_assets.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["asset", "value(verbatim)", "source", "source_loc", "used_by_swe1",
                    "channel", "observe"])
        w.writerows(out_rows)

    from collections import Counter
    c = Counter(r[0] for r in out_rows)
    ch = Counter(r[5] for r in out_rows)
    ob = Counter(r[6] for r in out_rows)
    print(f"step_assets.tsv {len(out_rows)} 列（含 _E §2 通道句 {len(CHANNEL_SENTENCES)} 列、_F §2 CertProfile {len(CERTPROFILE_ASSETS)} 列）；PDF {pages} 頁")
    for k, v in c.most_common():
        print(f"  {k:14s} {v}")
    print(f"  channel: {dict(ch.most_common())}")
    print(f"  observe: {dict(ob.most_common())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
