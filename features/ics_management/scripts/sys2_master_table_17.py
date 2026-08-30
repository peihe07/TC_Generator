#!/usr/bin/env python3
"""SYS2 主鍵對照表（下放包 17 作業 A＋B；R-ICS43(b)①、R-G41(c)）。

**主鍵是 SYS2 之 333 個資料列，不是 CFTS020 之 2180 個物件。**
本線前十二包以 CFTS020 為掃描起點，SYS2 中 21.9% 之列從未進入視野（A-ICS78）。
本表把該事實變成一個可查之工具：覆蓋率自需求側直接數出，不自規格側推算。

輸出：`docs/reports/17_sys2_master_table.tsv`（機器再用）＋統計（stdout）。
本腳本**唯讀**，不改任何 TC、錨或台帳。
"""
from __future__ import annotations
import json, glob, re, sys, unicodedata
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cfts020_probe as P

SYS2 = ROOT / "inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx"


def norm(v) -> str:
    """NBSP → space、collapse 連續空白（A-ICS32／66 之教訓）。"""
    if v is None:
        return ""
    s = unicodedata.normalize("NFKC", str(v)).replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def col_of(hdr, *keys):
    for i, h in enumerate(hdr):
        if h and all(k in str(h) for k in keys):
            return i
    return None


def main() -> int:
    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    ws = wb["Basic Report"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    C = {
        "doc_id": col_of(hdr, "文件識別碼"),
        "src": col_of(hdr, "來源需求項目ID"),
        "cat": col_of(hdr, "分類 Category"),
        "verif": col_of(hdr, "驗證性", "(Y/N/NA)"),
        "crit": col_of(hdr, "驗證標準"),
        "desc": col_of(hdr, "Description"),
    }
    assert all(v is not None for v in C.values()), C
    data = rows[1:]

    # CFTS020 三層 + 軸層
    objs = {o["id"]: o for o in P.parse()}
    doc_tokens = set(re.findall(r"\b\d{7}\b", "\n".join(P.doc_lines())))

    # TC 之錨
    anchors, tcs = {}, []
    for f in sorted(glob.glob(str(ROOT / "generated/b*/b*_tcs.json"))):
        d = json.load(open(f))
        for t in (d if isinstance(d, list) else d.get("test_cases", d.get("tcs", []))):
            tcs.append(t)
            for ln in t["specification_reference"].split("\n"):
                m = re.match(r"\s*CFTS\d+-(\d{7})\s*$", ln)
                if m:
                    anchors.setdefault(m.group(1), []).append(t["tc_title"])

    out = [["sys2_row", "doc_id", "src_id", "src_bucket", "category", "verifiability",
            "axis_verdict", "variant", "scope", "tc_coverage", "cover_basis",
            "covering_tcs", "verif_criteria", "er_match"]]
    for i, r in enumerate(data, start=2):
        src = norm(r[C["src"]])
        sid = src if re.fullmatch(r"\d{7}", src) else ("EMPTY" if not src else src)
        if sid == "EMPTY":
            bucket = "來源空白"
        elif sid in objs:
            bucket = "物件頭"
        elif sid in doc_tokens:
            bucket = "節標題錨"
        else:
            bucket = "指向他文件"
        o = objs.get(sid)
        cov = "有" if sid in anchors else "無"
        basis = "錨命中" if sid in anchors else "無"
        crit = norm(r[C["crit"]])
        out.append([str(i), norm(r[C["doc_id"]]), sid, bucket, norm(r[C["cat"]]),
                    norm(r[C["verif"]]),
                    o["v2"] if o else "NA",
                    o["variant_fits_dut"] if o else "NA",
                    o["scope"] if o else "NA",
                    cov, basis, "|".join(sorted(set(anchors.get(sid, [])))) or "",
                    crit or "EMPTY",
                    "不可比" if (cov == "無" or not crit) else "待人工"])
    tsv = ROOT / "docs/reports/17_sys2_master_table.tsv"
    tsv.write_text("\n".join("\t".join(c.replace("\t", " ") for c in row) for row in out) + "\n")
    print(f"已寫 {tsv.relative_to(ROOT.parents[1])}｜資料列 {len(out)-1}｜欄 {len(out[0])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
