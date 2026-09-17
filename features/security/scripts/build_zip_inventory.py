#!/usr/bin/env python3
"""SEC-07 §2.1 —— 三個 zip 之清單、測試方法、測試資產（唯讀）。

zip 只在 `_intake/Security/unzip/` 解壓；解壓物不投遞 `sources/raw/`。
apk 不反編譯、不執行。
"""
from __future__ import annotations

import csv
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features" / "security" / "data"
BASE = "/Users/peihe/Work/02_Project_R1LR/2_Architecture/CCVR/To Validation team"
ZIPS = {
    "Z1": f"{BASE}/Secure Log CS.212/StevenJSHsu/KeyInstall_IntegrationTests.zip",
    "Z2": f"{BASE}/Cert Val CS.98/IntegrationTests.zip",
    "Z3": f"{BASE}/Secure Log CS.212/StevenJSHsu/CertProvider_IntegrationTests.zip",
}
UNZ = {"Z1": ROOT / "_intake/Security/unzip/Z1", "Z2": ROOT / "_intake/Security/unzip/Z2"}
KIND = {".py": "py", ".sh": "sh", ".md": "other", ".p8": "pem", ".pem": "pem", ".crt": "crt",
        ".der": "der", ".json": "json", ".sig": "sig", ".bp": "bp", ".gradle": "gradle",
        ".xml": "xml", ".java": "java", ".kt": "kt", ".pyc": "other", ".bin": "other",
        ".gitignore": "other", ".TAG": "other"}
RE_TESTDEF = re.compile(r"^def (test_\w+)", re.M)
RE_INSTR = re.compile(
    r'"adb shell am instrument -w -e "\s*\\?\s*"class ([\w.]+)#%s "\s*\\?\s*"([\w./]+)"', re.S)
RE_CONST = re.compile(r"^(\w+) = (\w+) % \"(\w+)\"", re.M)
RE_ASSET = re.compile(r'["\']([\w./\-{}]+\.(?:pem|crt|der|json|sig|p8|bin|key))["\']')
ASSET_037 = ("SecurityAssets/oem-certs/cert-provider", "{TYPE}/cfgs", "_SAM_", "rawkey", "cfgs")


def main() -> int:
    inv, meth, assets = [], [], []
    for zid, path in ZIPS.items():
        with zipfile.ZipFile(path) as z:
            for i in z.infolist():
                if i.is_dir():
                    continue
                ext = Path(i.filename).suffix
                inv.append([zid, i.filename, i.file_size, KIND.get(ext, "other")])
    for zid, d in UNZ.items():
        for f in sorted(d.rglob("*.py")):
            rel = str(f.relative_to(d))
            text = f.read_text(encoding="utf-8", errors="replace")
            fqcns = {}
            for m in re.finditer(r'"class ([\w.]+)#%s "\s*\\?\s*"([\w./]+)"', text):
                fqcns[m.group(1)] = m.group(2)
            consts = {c[0]: c[2] for c in RE_CONST.findall(text)}
            base_of = {c[0]: c[1] for c in RE_CONST.findall(text)}
            for t in RE_TESTDEF.findall(text):
                body = text.split(f"def {t}(", 1)[1].split("\ndef ", 1)[0]
                used = [c for c in consts if re.search(rf"\b{c}\b", body)]
                for c in used or [""]:
                    java = consts.get(c, "")
                    fq = ""
                    if c:
                        bm = re.search(rf"{base_of[c]}\s*=\\?\s*\n?\s*\"adb shell am instrument[^\"]*\"\s*\\?\s*\n?\s*\"class ([\w.]+)#%s \"\s*\\?\s*\n?\s*\"([\w./]+)\"", text)
                        if bm:
                            fq = bm.group(1)
                            runner = bm.group(2)
                            cmd = (f"$ adb shell am instrument -w -e class {fq}#{java} {runner}")
                        else:
                            cmd = ""
                    else:
                        cmd = ""
                    meth.append([zid, rel, t, fq, java, cmd])
            for a in sorted(set(RE_ASSET.findall(text))):
                assets.append([zid, rel, a,
                               "Y" if any(k in a for k in ASSET_037) else "N"])
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.suffix in (".p8", ".pem", ".crt", ".der", ".sig", ".json"):
                assets.append([zid, str(f.relative_to(d)), f.name, "Y" if "rawkey" in f.name else "N"])

    for name, hdr, rows in (
            ("zip_inventory.tsv", ["zip", "path_in_zip", "size", "kind"], inv),
            ("zip_methods.tsv", ["zip", "source_file", "pytest_func", "class_fqcn",
                                 "java_method", "instrument_cmd"], meth),
            ("zip_assets.tsv", ["zip", "source_file", "asset", "matches_037"], assets)):
        with (DATA / name).open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(hdr)
            w.writerows(rows)

    ti = set(re.findall(r":\s*(\w+)\s*$",
                        (ROOT / "sources/raw/ccvr_cs98_test_items").glob("*.txt").__next__()
                        .read_text(encoding="utf-8"), re.M))
    zip_methods = {r[4] for r in meth if r[4]}
    print(f"zip_inventory.tsv {len(inv)} 列｜kind: {dict(Counter(r[3] for r in inv))}")
    print(f"zip_methods.tsv   {len(meth)} 列｜相異 java 方法 {len(zip_methods)}｜pytest 函式 {len({r[2] for r in meth})}")
    print(f"  Test_Items.txt 15 條 ∩ zip = {len(ti & zip_methods)}")
    print(f"  new（zip 有、Test_Items 無）= {len(zip_methods - ti)}")
    print(f"  missing（Test_Items 有、zip 無）= {len(ti - zip_methods)} {sorted(ti - zip_methods)}")
    print(f"zip_assets.tsv    {len(assets)} 列｜matches_037 = {sum(1 for r in assets if r[3]=='Y')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
