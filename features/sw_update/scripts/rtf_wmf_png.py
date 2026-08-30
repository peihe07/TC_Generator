#!/usr/bin/env python3
"""CFTS embedded object intake —— RTF(WMF) → PNG（下放包 53 T65a）.

RTF 內之 `{\\pict` 群組為 WMF 之 hex dump；去控制字後 unhexlify 得 .wmf，
再以 LibreOffice headless 轉 PNG，最後放大 2 倍以利閱讀。

用法：python3 scripts/rtf_wmf_png.py <src_dir> <out_dir>
"""
import binascii
import hashlib
import re
import subprocess
import sys
from pathlib import Path

# LibreOffice 於本機無 `libreoffice` 之名（下放包 53 落檔驗證 §核對）
SOFFICE_CANDIDATES = [
    "/opt/homebrew/bin/soffice",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "soffice",
]
RE_CONTROL = re.compile(r"\\[a-zA-Z]+-?\d*\s?")
RE_NON_HEX = re.compile(r"[^0-9a-fA-F]")
SCALE = 2


def soffice_path() -> str:
    """取本機可用之 LibreOffice 執行檔；皆不可用即拋出。"""
    for cand in SOFFICE_CANDIDATES:
        if Path(cand).exists():
            return cand
    return "soffice"


def extract_pict(raw: str) -> bytes:
    """自 RTF 文本取第一個 `{\\pict` 群組之 body，還原為二進位。"""
    start = raw.find("{\\pict")
    if start < 0:
        raise ValueError("RTF 中無 `{\\pict` 群組")
    depth = 0
    end = len(raw)
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
    hexs = RE_NON_HEX.sub("", RE_CONTROL.sub("", raw[start:end]))
    if len(hexs) % 2:
        hexs = hexs[:-1]
    return binascii.unhexlify(hexs)


def convert(wmf: Path, out_dir: Path) -> Path:
    """WMF → PNG，並放大 SCALE 倍（原輸出 794×1123，直接看不清）。"""
    subprocess.run(
        [soffice_path(), "--headless", "--convert-to", "png",
         str(wmf), "--outdir", str(out_dir)],
        check=True, capture_output=True, timeout=300,
    )
    png = out_dir / (wmf.stem + ".png")
    from PIL import Image
    img = Image.open(png)
    img.resize((img.width * SCALE, img.height * SCALE),
               Image.LANCZOS).save(png)
    return png


def main() -> None:
    src_dir, out_dir = Path(sys.argv[1]).expanduser(), Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for src in sorted(src_dir.glob("*.rtf")):
        obj_id = src.name.split("-")[0].strip()
        raw = src.read_bytes()
        wmf_bytes = extract_pict(raw.decode("latin-1"))
        wmf = out_dir / f"{obj_id}.wmf"
        wmf.write_bytes(wmf_bytes)
        png = convert(wmf, out_dir)
        from PIL import Image
        rows.append({
            "id": obj_id,
            "rtf_bytes": len(raw),
            "rtf_sha256": hashlib.sha256(raw).hexdigest(),
            "wmf_bytes": len(wmf_bytes),
            "wmf_sha256": hashlib.sha256(wmf_bytes).hexdigest(),
            "png_size": Image.open(png).size,
            "png_sha256": hashlib.sha256(png.read_bytes()).hexdigest(),
        })
        wmf.unlink()  # 中間產物不留
    for r in rows:
        print(f"{r['id']}  rtf={r['rtf_bytes']:>10,}  "
              f"wmf={r['wmf_bytes']:>9,}  png={r['png_size'][0]}x{r['png_size'][1]}")
        print(f"          rtf_sha={r['rtf_sha256']}")
        print(f"          wmf_sha={r['wmf_sha256']}")
        print(f"          png_sha={r['png_sha256']}")


if __name__ == "__main__":
    main()
