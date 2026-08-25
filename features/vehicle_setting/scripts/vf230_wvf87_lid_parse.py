"""VF230：`lid_pairs.tsv` 之產生器（W-VF87.1；R-VF134 之施行所需）。

**其所以須新寫**：`data/lid_pairs.tsv` **無任何腳本寫入之**
（`grep` 寫入模式零命中）—— 其產生者不在 repo，**與 `_dbc_parsed.json` 同型**。
`R-VF134` 二令「改 `lid_parse.py` 之來源路徑」，**而該檔為解析函式庫 ＋ 自驗，
本無來源路徑** —— 其前提不成立，故另立本驅動。

**解析之核心逕用 `lid_parse.py` 之既有函式**（`parse_signal_cell`／
`parse_format_cell`），**不另寫解析**（R-VF74：用既有範例，不自創）。

**正確性之驗證（R-VF92 一）**：以本驅動重建 **v1_76** 之 `lid_pairs.tsv`，
與現行檔逐列比對；**全等方採信其對 v1_78 之產出**。不全等即停。
"""
from __future__ import annotations

import csv
import sys
import warnings
from pathlib import Path

import openpyxl

warnings.filterwarnings("ignore")
FEAT = Path(__file__).resolve().parents[1]
ROOT = FEAT.parents[1]
sys.path.insert(0, str(FEAT / "scripts"))
import lid_parse as LP                       # noqa: E402

SHEETS = ("CAN Mapping", "Proxi & Configuration")
HEADER_ROW = 3
COLS = ("lid", "sheet", "row", "scope", "message", "signal", "can", "fmt")


# ---- 欄組（列 2 之標籤）----
# LID 表之列 2 為**欄組標籤**：F–J `Powernet`／K–O `CUSW`／P–T `Atlantis`／
# U–Y `Compact`／**Z–AD `Atlantis High`**。列 3 為各組共用之欄名
# （`Signal Name`／`CAN`／`Format`／`SNA`／`VFs`），**故只取第一個 `Signal Name`
# 會讀到 `Powernet` 組** —— 首版即如此，自驗以「僅現行有 550」攔下。
#
# **現行 `lid_pairs.tsv` 之 `scope` 二值即其取法**（實測）：
#   `Atlantis High`    Z–AD 欄組（2160 列）
#   `Atlantis(&High)`  **Z 欄為空時回退 P–T（`Atlantis`）欄組**（550 列）
# **`Proxi & Configuration` 之欄組標籤不同**（實測）：其 P 欄組為
# `Atlantis & Atlantis High`（該分頁無 `Atlantis High` 一組），
# 其 `scope` 亦記為 `Atlantis(&High)` —— **逐字寫死之欄組名，其變體即漏**。
GROUPS = (("Atlantis High", "Atlantis High"),
          ("Atlantis & Atlantis High", "Atlantis(&High)"),
          ("Atlantis", "Atlantis(&High)"))


def _group_cols(row2: list, hdr: list[str]) -> dict[str, dict[str, int]]:
    """回 {欄組標籤: {signal/can/fmt: 欄索引}}，依列 2 之標籤切段。"""
    marks = [(i, str(v).strip()) for i, v in enumerate(row2) if v and str(v).strip()]
    out: dict[str, dict[str, int]] = {}
    for n, (i, label) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(hdr)
        seg = {}
        for j in range(i, end):
            k = (hdr[j] or "").strip().lower()
            if k == "signal name":
                seg["signal"] = j
            elif k == "can":
                seg["can"] = j
            elif k == "format":
                seg["fmt"] = j
        if "signal" in seg:
            out[label] = seg
    return out


def _lid_col(hdr: list[str]) -> int:
    return next(i for i, c in enumerate(hdr)
                if (c or "").strip().lower() == "logical identifier")


def build(src: Path) -> list[dict]:
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    rows: list[dict] = []
    for sh in SHEETS:
        ws = wb[sh]
        data = list(ws.iter_rows(values_only=True))
        hdr = [str(c).strip() if c is not None else "" for c in data[HEADER_ROW - 1]]
        grp = _group_cols(list(data[HEADER_ROW - 2]), hdr)
        lidc = _lid_col(hdr)
        for rn, r in enumerate(data[HEADER_ROW:], start=HEADER_ROW + 1):
            lid = "" if r[lidc] is None else str(r[lidc]).strip()
            if not lid:
                continue
            # **回退之條件為「該欄組之 `Signal Name` 儲存格為空」，
            # 非「其解析結果為空」** —— 二者之別實測於列 282／832：
            #   Z 欄為 `N/A`／`Not Used`（**非空而解不出訊號**），
            #   原產生者視其為「該 lid 已表態」而**不回退**，該 lid 遂無列；
            #   若以「解析為空」為回退之條件，則會回退至 `Atlantis` 而**多產 3 列**。
            for label, scope in GROUPS:
                seg = grp.get(label)
                if not seg:
                    continue
                get = lambda k: ("" if seg.get(k) is None or seg[k] >= len(r)
                                 or r[seg[k]] is None else str(r[seg[k]]).strip())
                if not get("signal"):
                    continue                      # 儲存格為空 → 回退下一組
                pairs = LP.parse_signal_cell(get("signal"), get("can"))
                if not pairs:
                    break                         # 有值而解不出 → 不回退，該 lid 無列
                # **`fmt` 須逸出換行** —— 現行 `lid_pairs.tsv` 之換行為字面
                # 二字元 `\\n`（`lid_parse.unescape_cell` 之對應，R-VS26(1)）。
                # **首版寫真換行，其鍵集自驗仍「全等」而 `fmt` 欄 1250 筆相異**
                # —— 自驗只比鍵集者，其射程不及於值。
                # **`fmt` 不得 `strip()`** —— 原產生者保留其前導換行
                # （實測 134 筆之差全為此，如 `\\n$00 = Not Present…`）。
                # `get()` 已 strip，故此處自原儲存格重取。
                _fc = seg.get("fmt")
                _raw = ("" if _fc is None or _fc >= len(r) or r[_fc] is None
                        else str(r[_fc]))
                # **Tab 須轉空白** —— 其為 tsv 之分隔符，留之則欄位錯位
                # （實測 4 筆，如 `… [1] = True<TAB>`）。原產生者轉為單一空白。
                fmt = (_raw.replace("\\", "\\\\").replace("\n", "\\n")
                       .replace("\r", "").replace("\t", " "))
                for p in pairs:
                    rows.append({"lid": lid, "sheet": sh, "row": str(rn),
                                 "scope": scope, "message": p["message"] or "",
                                 "signal": p["signal"], "can": p["can"],
                                 "fmt": fmt})
                break
    wb.close()
    return rows


def main() -> None:
    cur = list(csv.DictReader((FEAT / "data/lid_pairs.tsv").open(encoding="utf-8"),
                              delimiter="\t"))
    old = FEAT / "inputs" / "Logical Identifiers and CAN Mapping v1_76.xlsx"
    mine = build(old)
    print("=== 自驗（R-VF92 一）：本驅動 vs 現行 `lid_pairs.tsv`（v1_76）===")
    print(f"  現行 {len(cur)} 列｜本驅動 {len(mine)} 列")
    # **自驗須逐欄，非只比鍵集** —— 首版只比鍵集而宣稱「全等」，
    # 其時 `fmt` 欄實有 1250 筆相異（逸出之差）。**只比鍵之自驗，其射程不及於值。**
    key = lambda r: (r["lid"], str(r["row"]), r["signal"], r["message"], r["can"])
    a, b = {key(r) for r in cur}, {key(r) for r in mine}
    print(f"  鍵集：僅現行有 {len(a - b)}｜僅本驅動有 {len(b - a)}")
    bad = a != b
    if bad:
        for x in sorted(a - b)[:3]:
            print(f"     僅現行 {x}")
        for x in sorted(b - a)[:3]:
            print(f"     僅本驅動 {x}")
    else:
        ca = {key(r): r for r in cur}
        cb = {key(r): r for r in mine}
        for col in COLS:
            d = [x for x in a
                 if str(ca[x].get(col) or "") != str(cb[x].get(col) or "")]
            print(f"  欄 {col:8} 相異 {len(d):>5}  {'✅' if not d else '❌'}")
            if d:
                bad = True
                x = d[0]
                print(f"       例 {x[0]}／{x[2]}"
                      f"\n         現行 {str(ca[x][col])[:56]!r}"
                      f"\n         本檔 {str(cb[x][col])[:56]!r}")
    if bad:
        raise SystemExit("**自驗不等 —— 本驅動與原產生者不等價，停。**"
                         "不得以其產生 v1_78 之本。")
    print("\n**自驗全等（鍵集 ＋ 逐欄），得據以產生 v1_78 之本。**")

    if "--write" in sys.argv:
        new = ROOT / "forms" / "Logical Identifiers and CAN Mapping v1_78.xlsx"
        out = build(new)
        p = FEAT / "data/lid_pairs_v178.tsv"
        with p.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t")
            w.writeheader()
            w.writerows(out)
        print(f"\nv1_78 → {p.relative_to(FEAT)}（{len(out)} 列）")
        na, nb = {key(r) for r in mine}, {key(r) for r in out}
        print(f"  v1_76 vs v1_78：僅舊有 {len(na - nb)}｜僅新有 {len(nb - na)}")
        for x in sorted(na - nb)[:6]:
            print(f"     僅 v1_76 {x}")
        for x in sorted(nb - na)[:6]:
            print(f"     僅 v1_78 {x}")


if __name__ == "__main__":
    main()
