#!/usr/bin/env python3
"""CFTS022 改綁覆驗（下放包 07 作業 F，R-ICS12(b)(c)）。

比對舊版（25PI3.5，privacy/inputs）與新版（26PI2.5，ics_management/inputs）：
  · 4 句 verbatim（4914956/57/75/76）
  · 7 物件之屬性三軸（ECU / Radio / EE Architecture）
不自行調和不符；不符即由呼叫者判 E4。
"""

import hashlib
import html
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

OLD = ROOT / "features/privacy/inputs/R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708.docx"
NEW = ROOT / "features/ics_management/inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 Functional Specification_20260608-1205.docx"

TARGET_SENT = ["4914956", "4914957", "4914975", "4914976"]
TARGET_ATTR = ["4914956", "4914957", "4914958", "4914974", "4914975", "4914976", "4914993"]
AXES = ["ECU", "Radio", "EE Architecture"]

HEAD_RE = re.compile(r"^(\d{7}): \[")
ATTR_RE = re.compile(r"\[([^\[\]:]+):([^\[\]]*)\]")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def extract_text(path: Path) -> str:
    """讀 word/document.xml，</w:p>→換行、</w:tc>→tab、去標籤、unescape。"""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "\n").replace("</w:tc>", "\t")
    xml = re.sub(r"<[^>]+>", "", xml)
    return html.unescape(xml)


def parse_objects(text: str) -> dict:
    """物件屬性頭 `^(\\d{7}): [`；本文為次一行。回傳 {oid: {attrs, body, head}}。"""
    lines = text.split("\n")
    out = {}
    for i, line in enumerate(lines):
        m = HEAD_RE.match(line.strip())
        if not m:
            continue
        oid = m.group(1)
        attrs = {k.strip(): v.strip() for k, v in ATTR_RE.findall(line)}
        body = lines[i + 1].strip() if i + 1 < len(lines) else ""
        # 首次出現為準（同 oid 重覆則記入 dup 清單）
        if oid in out:
            out[oid].setdefault("dups", []).append({"attrs": attrs, "body": body})
        else:
            out[oid] = {"attrs": attrs, "body": body, "head": line.strip()}
    return out


def norm(s: str) -> str:
    """五項正規化：彎引號、NBSP、非斷字連字號、空白摺疊、句末單一句號。"""
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace(" ", " ")
    s = s.replace("‑", "-").replace("‐", "-")
    s = re.sub(r"\s+", " ", s).strip()
    if s.endswith(".") and not s.endswith(".."):
        s = s[:-1]
    return s


def eq_verbatim(a: str, b: str) -> bool:
    """正規化後比對，另允許句首字母大小寫差異（R-4）。"""
    na, nb = norm(a), norm(b)
    if na == nb:
        return True
    if na and nb and na[0].lower() == nb[0].lower() and na[1:] == nb[1:]:
        return True
    return False


def v2a(attrs: dict) -> bool:
    """R-ICS2 v2(a)：CFTS022 三軸交集。"""
    def vals(k):
        return {x.strip() for x in attrs.get(k, "").split(",") if x.strip()}
    ecu = vals("ECU") & {"ICS", "LTM"}
    radio = vals("Radio") & {"R1L", "R1L-R", "allSys"}
    ee = vals("EE Architecture") & {"Atlantis High", "All"}
    return bool(ecu and radio and ee)


def main() -> int:
    for p in (OLD, NEW):
        if not p.exists():
            print(f"MISSING: {p}", file=sys.stderr)
            return 2

    old_t, new_t = extract_text(OLD), extract_text(NEW)
    old_o, new_o = parse_objects(old_t), parse_objects(new_t)

    print("== §0 檔案 ==")
    for tag, p, objs in (("OLD", OLD, old_o), ("NEW", NEW, new_o)):
        print(f"{tag}\tname={p.name}\tsha256={sha256(p)}\tobjects={len(objs)}")

    print("\n== §1 基本比較 ==")
    so, sn = set(old_o), set(new_o)
    print(f"old_total={len(so)} new_total={len(sn)} common={len(so & sn)} "
          f"only_old={len(so - sn)} only_new={len(sn - so)}")

    print("\n== §2 四句 verbatim ==")
    mismatch = []
    for oid in TARGET_SENT:
        ob = old_o.get(oid, {}).get("body", "<ABSENT>")
        nb = new_o.get(oid, {}).get("body", "<ABSENT>")
        ok = oid in old_o and oid in new_o and eq_verbatim(ob, nb)
        if not ok:
            mismatch.append(f"SENT:{oid}")
        print(f"[{oid}] MATCH={ok}")
        print(f"  OLD: {ob}")
        print(f"  NEW: {nb}")

    print("\n== §3 七物件三軸 ==")
    for oid in TARGET_ATTR:
        oa = old_o.get(oid, {}).get("attrs", {})
        na = new_o.get(oid, {}).get("attrs", {})
        row_ok = True
        set_ok = True
        for ax in AXES:
            ov, nv = oa.get(ax, "<ABSENT>"), na.get(ax, "<ABSENT>")
            same = norm(ov) == norm(nv)
            # 集合比：多值屬性以逗號切分後比集合（順序不計）
            sset = {x.strip() for x in ov.split(",")} == {x.strip() for x in nv.split(",")}
            row_ok = row_ok and same
            set_ok = set_ok and sset
            print(f"[{oid}] {ax}: OLD={ov!r} NEW={nv!r} SAME={same} SET_SAME={sset}")
        ov2, nv2 = v2a(oa), v2a(na)
        print(f"[{oid}] AXES_MATCH={row_ok} SET_MATCH={set_ok} v2a OLD={ov2} NEW={nv2} "
              f"VERDICT_CHANGED={ov2 != nv2}")
        if not row_ok:
            mismatch.append(f"ATTR:{oid}")
        if ov2 != nv2:
            mismatch.append(f"V2A:{oid}")

    print("\n== §4 4914993 完整 ==")
    for tag, objs in (("OLD", old_o), ("NEW", new_o)):
        o = objs.get("4914993")
        if not o:
            print(f"{tag}: <ABSENT>")
            continue
        print(f"{tag} HEAD: {o['head']}")
        print(f"{tag} BODY: {o['body']}")
        print(f"{tag} v2a: {v2a(o['attrs'])}")

    print("\n== §5 結論 ==")
    print("E4_TRIGGERED=" + ("YES  " + ",".join(mismatch) if mismatch else "NO"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
