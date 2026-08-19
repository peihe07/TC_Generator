"""G226 —— WrapperResource 轉檔之獨立重跑（R-P319）。

R-P319 令執行層依 R-P317 所載之路徑**獨立重跑一次**，
比對其輸出與分析層所產之 WMF 是否位元組相同。

**路徑（R-P317 逐字）**：
    RTF → 抽 `\\*\\objdata` 之 hex → OLE2 compound file
        → `OlePres000` stream → 自 offset 40 之標準 WMF 簽章（`01 00 09 00`）切出
        → LibreOffice --convert-to png → JPEG

**本檔僅重跑至 WMF**（比對之標的即為 WMF）；
PNG/JPEG 之步驟依賴 LibreOffice，其輸出隨版本而異，不作位元組比對。

**⚠ 實作差異須明載**：分析層使用 `olefile 0.47`，**本機未安裝該套件**。
為免為一次比對而引入新依賴（且新依賴之版本差異本身即為變因），
本檔**以標準庫自行解析 OLE2 compound file** —— 其為讀取，不改任何位元組。
**若二者所得之 WMF 位元組相同，即證該切出不依賴特定套件**；
不同者則須查明係解析之差異抑或分析層之路徑有誤。

用法：
    python features/power/scripts/rerun_wrapper_convert.py
"""

from __future__ import annotations

import binascii
import hashlib
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DERIVED = IN / "derived"
SANDBOX = ROOT / "features/power/sandbox/derived_rerun"

PAIRS = [("4942177- CFTSMV009_CIP_R4_O829_4_inline.rtf", "O829_std.wmf"),
         ("4942178- CFTSMV009_CIP_R4_O1584_5_inline.rtf", "O1584_std.wmf")]
WMF_SIG = b"\x01\x00\x09\x00"


def read_ole_streams(blob: bytes) -> dict[str, bytes]:
    """以標準庫解析 OLE2 compound file，回傳 {stream 名: 內容}。

    僅實作讀取所需之最小子集：標頭 → FAT/DIFAT → 目錄鏈 → mini/常規串流。
    """
    assert blob[:8] == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", "非 OLE2 標頭"
    sect_shift, mini_shift = struct.unpack_from("<HH", blob, 0x1E)
    ssz, msz = 1 << sect_shift, 1 << mini_shift
    n_fat, dir_start, _, mini_cut, mini_start, n_mini, difat_start, n_difat = \
        struct.unpack_from("<I I I I I I I I", blob, 0x2C)

    def sect(i: int) -> bytes:
        off = (i + 1) * ssz
        return blob[off:off + ssz]

    # DIFAT → FAT
    difat = list(struct.unpack_from("<109I", blob, 0x4C))
    nxt = difat_start
    for _ in range(n_difat):
        if nxt >= 0xFFFFFFFA:
            break
        s = sect(nxt)
        difat += list(struct.unpack_from(f"<{ssz // 4 - 1}I", s, 0))
        nxt = struct.unpack_from("<I", s, ssz - 4)[0]
    fat: list[int] = []
    for fs in difat[:n_fat]:
        if fs >= 0xFFFFFFFA:
            continue
        fat += list(struct.unpack_from(f"<{ssz // 4}I", sect(fs), 0))

    def chain(start: int) -> list[int]:
        out, cur = [], start
        while cur < 0xFFFFFFFA and len(out) < 1_000_000:
            out.append(cur)
            cur = fat[cur] if cur < len(fat) else 0xFFFFFFFE
        return out

    def read_chain(start: int, size: int) -> bytes:
        data = b"".join(sect(i) for i in chain(start))
        return data[:size]

    # 目錄
    dir_data = b"".join(sect(i) for i in chain(dir_start))
    entries = []
    for off in range(0, len(dir_data), 128):
        e = dir_data[off:off + 128]
        if len(e) < 128:
            break
        nlen = struct.unpack_from("<H", e, 0x40)[0]
        name = e[:max(0, nlen - 2)].decode("utf-16-le", "replace")
        typ = e[0x42]
        start, size = struct.unpack_from("<I", e, 0x74)[0], \
            struct.unpack_from("<Q", e, 0x78)[0]
        entries.append((name, typ, start, size))

    root = next(e for e in entries if e[1] == 5)
    mini_data = read_chain(root[2], root[3]) if root[2] < 0xFFFFFFFA else b""
    mini_fat: list[int] = []
    if mini_start < 0xFFFFFFFA:
        md = b"".join(sect(i) for i in chain(mini_start))
        mini_fat = list(struct.unpack_from(f"<{len(md) // 4}I", md, 0))

    def read_mini(start: int, size: int) -> bytes:
        out, cur = b"", start
        while cur < 0xFFFFFFFA and len(out) < size:
            out += mini_data[cur * msz:(cur + 1) * msz]
            cur = mini_fat[cur] if cur < len(mini_fat) else 0xFFFFFFFE
        return out[:size]

    streams = {}
    for name, typ, start, size in entries:
        if typ != 2:
            continue
        streams[name] = (read_mini(start, size) if size < mini_cut
                         else read_chain(start, size))
    return streams


def main() -> None:
    SANDBOX.mkdir(parents=True, exist_ok=True)
    rows = []
    for src_name, out_name in PAIRS:
        src = IN / src_name
        data = src.read_bytes()
        m = re.search(rb"\\\*\\objdata\s+([0-9a-fA-F\s]+)", data)
        if not m:
            rows.append((out_name, None, "**未找到 `\\*\\objdata`**"))
            continue
        hexs = re.sub(rb"\s+", b"", m.group(1))
        if len(hexs) % 2:
            hexs = hexs[:-1]
        raw_obj = binascii.unhexlify(hexs)
        # **OLE1 包裝須先剝除**（R-P317 之路徑未載此步，實測補之）：
        # `\*\objdata` 之內容並非直接為 OLE2，其前有 OLE1 標頭 ——
        # 實測為 `01 05 00 00 02 00 00 00 11 00 00 00` ＋ `Visio.Drawing.11\0`
        # ＋ 保留欄位 ＋ 4-byte 長度，OLE2 標頭自 **offset 41** 起。
        # 以 OLE2 之魔術數搜尋其起點，不依賴固定偏移。
        k = raw_obj.find(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1")
        if k < 0:
            rows.append((out_name, None, "**未找到 OLE2 標頭**"))
            continue
        streams = read_ole_streams(raw_obj[k:])
        pres = [k for k in streams if "OlePres000" in k]
        if not pres:
            rows.append((out_name, None, f"無 `OlePres000`；streams={sorted(streams)}"))
            continue
        blob = streams[pres[0]]
        i = blob.find(WMF_SIG)
        # **依 WMF 標頭所載之大小截斷**（R-P317 之路徑未載此步，實測補之）：
        # `OlePres000` 之尾端有 stream 填充（`O829` 實測多 26 bytes，含 `NANI` 標記），
        # 其非 WMF 內容。WMF placeable/standard 標頭 offset 6 之 DWORD 為
        # **檔案大小（單位：word）**；以之截斷方得與分析層所產位元組相同。
        declared = struct.unpack_from("<I", blob, i + 6)[0] * 2
        wmf = blob[i:i + declared] if 0 < declared <= len(blob) - i else blob[i:]
        p = SANDBOX / out_name
        p.write_bytes(wmf)
        got = hashlib.sha256(wmf).hexdigest()
        ref = DERIVED / out_name
        want = hashlib.sha256(ref.read_bytes()).hexdigest()
        rows.append((out_name, (len(wmf), i, got, ref.stat().st_size, want),
                     "**位元組相同**" if got == want else "**相異**"))

    print("G226 —— 轉檔之獨立重跑（以標準庫解析 OLE2，未用 `olefile`）\n")
    ok = True
    for name, info, verdict in rows:
        print(f"  {name}: {verdict}")
        if info:
            n, off, got, rn, want = info
            print(f"      重跑 {n:,} bytes（WMF 簽章 offset {off}）  SHA256 {got[:32]}…")
            print(f"      分析層 {rn:,} bytes                       SHA256 {want[:32]}…")
            ok &= got == want
        else:
            ok = False
    print(f"\n  G226：{'二份皆位元組相同' if ok else '**有相異**'}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
