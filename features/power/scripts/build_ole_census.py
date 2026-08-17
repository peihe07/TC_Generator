"""B2 — CFTS010 之 OLE2 storage / stream 目錄清點（R-P48 / G30）。

R-P48 釐清：R-P39「不得解 RTF」指不解析 RTF **內容**，
不涵蓋「檢視 OLE2 之 storage 目錄結構」。列出目錄清單屬清點。

**本腳本只讀目錄項（名稱、型別、大小），不讀任何 stream 之內容位元組。**

實作採 Python 標準函式庫自行解析 Compound File Binary（MS-CFB）之
標頭、FAT 與目錄鏈 —— `olefile` 未安裝，且 CLAUDE.md 要求優先用內建函式庫。
解析範圍僅及目錄樹，不觸及任何 stream 之資料扇區。

用法：
    python features/power/scripts/build_ole_census.py
"""

from __future__ import annotations

import struct
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

CFB_SIGNATURE = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
FREESECT = 0xFFFFFFFF
ENDOFCHAIN = 0xFFFFFFFE
NOSTREAM = 0xFFFFFFFF
ENTRY_TYPES = {0: "empty", 1: "storage", 2: "stream", 5: "root"}

# R-P55 回歸斷言（06 包 G30 基線）
EXPECTED_ENTRIES = 14
EXPECTED_OBJECT_POOL = False
EXPECTED_OLE_MARKERS = 0


def read_directory(path: Path) -> tuple[list[dict], dict]:
    """解析 CFB 標頭與目錄鏈，回傳目錄項清單與標頭資訊。"""
    data = path.read_bytes()
    if not data.startswith(CFB_SIGNATURE):
        raise ValueError(f"非 OLE2/CFB：{path.name}")

    sector_shift = struct.unpack_from("<H", data, 30)[0]
    mini_shift = struct.unpack_from("<H", data, 32)[0]
    sector_size = 1 << sector_shift
    fat_count = struct.unpack_from("<I", data, 44)[0]
    first_dir = struct.unpack_from("<I", data, 48)[0]
    difat_extra = struct.unpack_from("<I", data, 68)[0]

    # DIFAT：標頭內 109 筆
    difat = [struct.unpack_from("<I", data, 76 + 4 * i)[0] for i in range(109)]
    difat = [s for s in difat if s != FREESECT][:fat_count]

    def sector_offset(sector: int) -> int:
        return (sector + 1) * sector_size

    fat: list[int] = []
    for s in difat:
        off = sector_offset(s)
        fat += list(struct.unpack_from(f"<{sector_size // 4}I", data, off))

    # 目錄鏈
    entries: list[dict] = []
    sector = first_dir
    visited = set()
    while sector not in (ENDOFCHAIN, FREESECT) and sector not in visited:
        visited.add(sector)
        off = sector_offset(sector)
        for i in range(sector_size // 128):
            raw = data[off + 128 * i: off + 128 * (i + 1)]
            if len(raw) < 128:
                break
            name_len = struct.unpack_from("<H", raw, 64)[0]
            name = raw[: max(0, name_len - 2)].decode("utf-16-le", errors="replace")
            entry_type = raw[66]
            size = struct.unpack_from("<Q", raw, 120)[0]
            if entry_type == 0:
                continue
            entries.append({
                "name": name,
                "type": ENTRY_TYPES.get(entry_type, f"unknown({entry_type})"),
                "size": size,
            })
        sector = fat[sector] if sector < len(fat) else ENDOFCHAIN

    header = {
        "sector_size": sector_size,
        "mini_sector_size": 1 << mini_shift,
        "fat_sectors": fat_count,
        "difat_extra": difat_extra != ENDOFCHAIN,
        "bytes": len(data),
    }
    return entries, header


def main() -> None:
    path = next(x for x in IN.iterdir() if x.suffix == ".doc")
    entries, header = read_directory(path)

    types = Counter(e["type"] for e in entries)
    # 疑似嵌入物件之目錄項（MS-DOC：ObjectPool 之下每個物件一個 storage）
    pool = [e for e in entries if e["name"] == "ObjectPool"]
    obj_like = [e for e in entries
                if e["type"] == "storage" and e["name"].startswith("_")]
    ole_streams = [e for e in entries if e["name"] in ("\x01Ole", "\x01CompObj", "\x01Ole10Native")]
    ole_marker = [e for e in entries if e["name"] == "\x01Ole"]

    out = [
        "# B2 — CFTS010 之 OLE2 目錄清點（R-P48 / G30）\n",
        f"\n檔案：`{path.name}`（{header['bytes']:,} bytes，OLE2）\n",
        "\n> 依 **R-P48**：R-P39「不得解 RTF」指不解析 RTF **內容**，"
        "不涵蓋檢視 OLE2 之 storage 目錄結構。\n",
        "> **本檔只列目錄項（名稱、型別、大小），未讀任何 stream 之內容位元組。**\n",
        "> `olefile` 未安裝；依 CLAUDE.md「優先用內建函式庫」，"
        "以標準函式庫自行解析 MS-CFB 之標頭、FAT 與目錄鏈"
        "（`scripts/build_ole_census.py`），解析範圍僅及目錄樹。\n",
        "\n## 1. 容器標頭\n\n| 項目 | 值 |\n|---|---|\n",
        f"| sector size | {header['sector_size']} bytes |\n",
        f"| mini sector size | {header['mini_sector_size']} bytes |\n",
        f"| FAT 扇區數 | {header['fat_sectors']} |\n",
        f"| DIFAT 延伸 | {'有' if header['difat_extra'] else '無（109 筆表頭內 DIFAT 已足）'} |\n",
        f"\n## 2. 目錄項總計\n\n| 型別 | 數量 |\n|---|---|\n",
    ]
    for k, v in types.most_common():
        out.append(f"| {k} | **{v}** |\n")
    out.append(f"| **合計** | **{len(entries)}** |\n")

    out.append("\n## 3. 全部目錄項\n\n| 名稱 | 型別 | 大小 (bytes) |\n|---|---|---|\n")
    for e in sorted(entries, key=lambda x: (x["type"], x["name"])):
        display = e["name"].replace("\x01", "\\x01").replace("\x05", "\\x05")
        out.append(f"| `{display}` | {e['type']} | {e['size']:,} |\n")

    out.append(
        f"\n## 4. 疑似嵌入物件\n\n"
        f"| 判準 | 數量 |\n|---|---|\n"
        f"| `ObjectPool` storage 是否存在 | {'**是**' if pool else '**否**'} |\n"
        f"| 名稱以 `_` 起始之 storage（MS-DOC 之物件容器慣例） | **{len(obj_like)}** |\n"
        f"| `\\x01Ole` / `\\x01CompObj` / `\\x01Ole10Native` 等 OLE 標記 stream | {len(ole_streams)}（其中 root 層之 `\\x01CompObj` 為容器自身之標記，任何 OLE2 文件皆有，非嵌入物件） |\n"
        f"| 其中 `\\x01Ole`（每個嵌入 OLE 物件必有一個） | **{len(ole_marker)}** |\n"
    )

    upper = max(len(obj_like), len(ole_marker))
    out.append(
        f"\n## 5. 與 05 包下界之對照（G30）\n\n"
        f"| 來源 | 數量 |\n|---|---|\n"
        f"| 05 包下界（`textutil -convert html` 之 `WrapperResource` 字樣） | **15** |\n"
        f"| 本包上界（OLE2 目錄之嵌入物件容器） | **{upper}** |\n"
        f"| 差額 | **{upper - 15:+d}** |\n"
    )
    if upper == 0:
        out.append(
            "\n### 差額成因\n\n"
            "**OLE2 容器內無任何嵌入物件容器**（無 `ObjectPool`、無 `\\x01Ole` 標記 stream、"
            "無 `_`-起始之物件 storage）。\n\n"
            "即 CFTS010 之 15 處 `WrapperResource` 與 CFTS009 之 16 處**性質相同**：\n"
            "**皆為純字面文字之懸空參照，非嵌入物件之錨**。\n\n"
            "上界 0 < 下界 15 並非矛盾 —— 二者量的不是同一件事：\n"
            "下界 15 量的是**文字層中的參照字樣**，上界 0 量的是**容器中實際存在的嵌入物件**。\n"
            "兩數併觀所得之結論即 **A-PW23 之訂正形態**："
            "參照存在，而其所指之資源不存在於交付文件中。\n\n"
            "**故 CFTS010 之嵌入物件數為 0，此為確定值而非下界。**\n"
        )
    else:
        out.append(
            f"\n### 差額成因\n\n"
            f"容器內實際存在 {upper} 個嵌入物件容器，而文字層僅見 15 處參照字樣。\n"
            f"差額須逐一比對；本檔只清點，不解析內容。\n"
        )

    out_path = DATA / "b2_cfts010_ole.md"
    out_path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)} — {out_path.stat().st_size} bytes")
    print(f"G30 目錄項 {len(entries)}（{dict(types)}）")
    print(f"  ObjectPool: {'有' if pool else '無'}；_ 起始 storage {len(obj_like)}；"
          f"\\x01Ole 標記 {len(ole_marker)}")
    print(f"  上界 {upper} vs 05 包下界 15 → 差額 {upper - 15:+d}")

    # R-P55 回歸斷言
    problems = []
    if len(entries) != EXPECTED_ENTRIES:
        problems.append(f"目錄項 {len(entries)} ≠ 期望 {EXPECTED_ENTRIES}")
    if bool(pool) != EXPECTED_OBJECT_POOL:
        problems.append(f"ObjectPool 存在={bool(pool)} ≠ 期望 {EXPECTED_OBJECT_POOL}")
    if len(ole_marker) != EXPECTED_OLE_MARKERS:
        problems.append(f"\\x01Ole 標記 {len(ole_marker)} ≠ 期望 {EXPECTED_OLE_MARKERS}")
    if problems:
        print("\n**回歸斷言失敗（R-P55）**：" + "；".join(problems))
        raise SystemExit(1)
    print("回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
