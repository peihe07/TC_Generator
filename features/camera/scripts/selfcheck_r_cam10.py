#!/usr/bin/env python3
"""R-CAM10 自檢 —— 錨是否被 SWE ID 較小者共引（CAM-04 §1(d)，不入 lint 序列）。

R-CAM10：A 本兩列以上共引同一 SYS-RA 來源時，該來源之驗證由 SWE ID 較小者承接；
較大者不得再以該來源作 `specification_reference` 錨。

資料：`features/camera/data/layer3_a_vf_chapters.tsv`（A 本 541 個來源引用之全量展開，
含 swe_id、source_requirement_id 與其所屬 SYS2 本）。owner = 引用該來源之最小 SWE ID。

    python features/camera/scripts/selfcheck_r_cam10.py [批次目錄 …]

批次目錄預設 `features/camera/generated/pilot02`。命中即 exit 1。
"""
from __future__ import annotations

import csv
import glob
import json
import re
import sys
import warnings
from collections import defaultdict
from pathlib import Path

import openpyxl

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[3]
XREF = ROOT / "features/camera/data/layer3_a_vf_chapters.tsv"
SYS2 = {"CFTS092": "sys2_cfts092_sysra_v01", "VF551_V2": "sys2_vf551_v2_sysra_v01",
        "VF551_V3": "sys2_vf551_v3_sysra_v01", "VF551_V33": "sys2_vf551_v33_sysra_v01",
        "VF551_V4": "sys2_vf551_v4_sysra_v01", "VF551_V42": "sys2_vf551_v42_sysra_v01"}


def _txt(v) -> str:
    return "" if v is None else re.sub(r"\s+", " ", str(v).replace("\xa0", " ")).strip()


def owners() -> dict[str, str]:
    """SYS-RA id -> 承接之 SWE ID（最小者）。"""
    out: dict[str, str] = {}
    with XREF.open(encoding="utf-8") as fh:
        for row in list(csv.reader(fh, delimiter="\t"))[1:]:
            swe, sid = row[0], row[1]
            if sid not in out or swe < out[sid]:
                out[sid] = swe
    return out


def anchor_to_sysra() -> dict[str, str]:
    """spec_reference 之錨（VF anchor 或 CFTS ObjectID）-> SYS-RA id。

    R-CAM11 之後 `specification_reference` 寫 SYS2 `F` 欄之值，故須反查。
    """
    out: dict[str, str] = {}
    for label, doc in SYS2.items():
        path = glob.glob(str(ROOT / f"sources/raw/{doc}/*.xlsx"))[0]
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for r in wb["Basic Report"].iter_rows(values_only=True):
            sid, anchor = _txt(r[1]), _txt(r[5])
            if not sid or sid == "SYS2 Sys-RA-Feature-ID" or not anchor:
                continue
            key = f"CFTS092-{anchor}" if label == "CFTS092" else anchor
            out.setdefault(key, sid)
        wb.close()
    return out


def main() -> None:
    dirs = [Path(a) for a in sys.argv[1:]] or [ROOT / "features/camera/generated/pilot02"]
    own, a2s = owners(), anchor_to_sysra()
    hits, checked = [], 0
    unresolved = []
    for d in dirs:
        for p in sorted(d.glob("NR1L-*.json")):
            doc = json.loads(p.read_text(encoding="utf-8"))
            req = doc["req_id"]
            for tc in doc["tcs"]:
                for anchor in tc["specification_reference"].split("\n"):
                    anchor = anchor.strip()
                    if not anchor:
                        continue
                    checked += 1
                    sid = a2s.get(anchor)
                    if sid is None:
                        unresolved.append((doc["tc_id"], anchor))
                        continue
                    holder = own.get(sid)
                    if holder != req:
                        hits.append((doc["tc_id"], req, anchor, sid, holder))
    print(f"R-CAM10 自檢：批次 {[str(d) for d in dirs]}")
    print(f"  檢查錨 {checked} 個；無法反查 {len(unresolved)}；**命中 {len(hits)}**")
    for tc_id, anchor in unresolved:
        print(f"  [反查失敗] {tc_id}  {anchor}")
    for tc_id, req, anchor, sid, holder in hits:
        print(f"  [違反] {tc_id}（{req}）錨 {anchor} = {sid}，承接列為 {holder}")
    sys.exit(1 if hits or unresolved else 0)


if __name__ == "__main__":
    main()
