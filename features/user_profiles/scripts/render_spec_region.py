#!/usr/bin/env python3
"""spec PDF 之版面重繪與表格判讀（J-2，17 包）。

## 為什麼需要它

`pdf_text` 是**攤平**的：一張兩欄表在文字層裡只剩一串字，
欄別、列界、勾記全部消失 —— 16 輪之 Table CPA2 即因此被誤讀成五列，
且欄別一度被判為「永久限制」。

**但版面一直都在。** 三種東西可各自取出：

| 物 | API | 用途 |
|---|---|---|
| 文字與其座標 | `page.get_text("dict")` | 列標題、欄標題 |
| 格線（向量）| `page.get_drawings()` | 列界與欄界 |
| 勾記（小圖之置放）| `page.get_image_rects(xref)` | **哪一格有標記** |

勾記常是**同一張小圖置放多次**（Table CPA2 為 61×64 之 PNG 置放 5 次），
故「哪一列屬哪一欄」是**可機器判定**的，不必只靠肉眼。

## 用法

    # 1) 重繪某頁之某區（人工判讀用）
    python3 scripts/render_spec_region.py --page 17 --zoom 6 \
        --clip 0.02,0.45,0.46,0.80 --out /tmp/p17_table.png

    # 2) 判讀某區之表格（格線 ＋ 勾記 → 矩陣）
    python3 scripts/render_spec_region.py --page 17 --table 24,300,334,532

    # 3) 回歸案例：重跑 p17 之 Table CPA2，與 16 輪之判讀比對
    python3 scripts/render_spec_region.py --regression

`--clip` 為**頁面比例**（0–1），`--table` 為**頁面座標**（pt）。
兩者刻意不同單位：前者給人抓大概位置，後者要精確。
"""

import argparse
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent
SPEC_PDF = (FEATURE.parent.parent / "spec-index" / "sources" /
            "Personal Account HMI Logic and Flow R1L-R "
            "(February 10 2023).pdf")

# 16 輪之判讀（F-2），逐格。**本檔之回歸案例即以此為預期值。**
# 來源：上繳 16 §2.2；當時為肉眼判讀，本檔改以座標判定複驗。
CPA2_EXPECTED = {
    "grid": {"rows": 4, "cols": 2},
    "col_labels": ["Connected FCA Account", "Local Profile"],
    "rows": [
        ("Personalization", [True, True]),
        ("App Store", [True, False]),
        ("Marketplace", [True, False]),
        ("****Connected Navigation", [True, False]),
    ],
}
CPA2_CLIP = (24, 300, 334, 532)   # pt，p17 之 Table CPA2


def _doc():
    import fitz
    return fitz.open(SPEC_PDF)


def render(page_no: int, clip_frac, zoom: float, out: Path) -> None:
    import fitz
    with _doc() as doc:
        pg = doc[page_no - 1]
        r = pg.rect
        clip = None
        if clip_frac:
            x0, y0, x1, y1 = clip_frac
            clip = fitz.Rect(r.x0 + r.width * x0, r.y0 + r.height * y0,
                             r.x0 + r.width * x1, r.y0 + r.height * y1)
        pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
        pix.save(out)
        print(f"p{page_no} → {out}  ({pix.width}×{pix.height}, zoom={zoom})")


def read_table(page_no: int, box) -> dict:
    """以格線與勾記之座標判讀一個表格區。

    回傳 {'rows': [(列標題, [各欄是否有標記]), …], 'col_labels': [...]}。
    **不判斷語意** —— 它只回答「哪一格有東西」。
    """
    import fitz
    x0, y0, x1, y1 = box
    box_r = fitz.Rect(*box)
    with _doc() as doc:
        pg = doc[page_no - 1]

        # 1) 格線 —— 取落在區內之水平／垂直線段
        hs, vs = set(), set()
        for d in pg.get_drawings():
            r = d["rect"]
            # **判準改過一次（R-U37）。**
            # v1 要求線段之**起點**落在框內 —— 而表格外框之垂直線常起於
            # 框線之上一點點（p16 之 PIP1 表：線起 y=59.7，框給 y=60）。
            # 差 0.3pt 就整條被排除，結果是「垂直線 0 條」→ 欄數為 0 →
            # **整張表讀不出來，而且看起來像「這張表沒有欄」。**
            # v2：以**相交**判定（線段與框有重疊即納入）。
            # **不可用 `Rect &` 或 `.intersects()`** —— 格線是**零寬（零高）**之
            # 矩形，PyMuPDF 一律視其為 empty，兩者都會回 False。
            # 以座標自行判重疊。
            if not (r.x0 <= box_r.x1 and r.x1 >= box_r.x0
                    and r.y0 <= box_r.y1 and r.y1 >= box_r.y0):
                continue
            # **須橫跨（縱貫）表寬（表高）之過半** —— 只用「細長」認格線
            # 會把**表頭 `FCA` 之刪除線**（25pt 寬之填色矩形）當成一條列界，
            # 於是表頭被切成兩帶、多出一個空白列。
            # 判準之要點：格線與刪除線的差別不在細長，在**跨不跨整張表**。
            if r.height < 1 and r.width > box_r.width * 0.5:
                hs.add(round(r.y0, 1))
            if r.width < 1 and r.height > box_r.height * 0.5:
                vs.add(round(r.x0, 1))
        # **去重（容差 1pt）** —— 表格外框常由兩條幾乎重合之線段構成
        # （本表之頂線即 300.2 與 300.6 兩條）。不去重會多出一個列帶，
        # 於是每一列都往下錯一格，讀出來的欄別全部是錯的 —— 而它「看起來」
        # 像是判讀不一致，其實是我把兩條線當成兩個列界。
        def dedupe(vals, tol=1.0):
            out = []
            for v in sorted(vals):
                if not out or v - out[-1] > tol:
                    out.append(v)
            return out

        hs, vs = dedupe(hs), dedupe(vs)

        # 2) 勾記 —— 小圖之置放矩形（同一 xref 常置放多次）
        marks = []
        for im in pg.get_images(full=True):
            xref = im[0]
            info = doc.extract_image(xref)
            if info["width"] > 120 or info["height"] > 120:
                continue          # 大圖是截圖，不是勾記
            for r in pg.get_image_rects(xref):
                if box_r.contains(fitz.Point(r.x0, r.y0)):
                    marks.append((round(r.x0 + r.width / 2, 1),
                                  round(r.y0 + r.height / 2, 1)))
        # **同一個勾記常以兩個 xref 疊放**（本表為 99 與 101，位置完全相同，
        # 各 61×64、各 177 bytes —— 可能是描邊與填色兩層）。
        # 不去重會得到 10 個勾記而非 5 個。**格數不會因此變**，
        # 但「勾記置放數」這個報出來的量測值會錯一倍。
        marks = sorted(set(marks))

        # 3) 文字 —— 每格之文字，用來取列標題與欄標題
        spans = []
        for b in pg.get_text("dict")["blocks"]:
            if b["type"] != 0:
                continue
            for ln in b["lines"]:
                for s in ln["spans"]:
                    t = s["text"].strip()
                    if t and box_r.contains(fitz.Point(*s["bbox"][:2])):
                        spans.append((s["bbox"][1], s["bbox"][0], t))

    def band(v, edges):
        for i in range(len(edges) - 1):
            if edges[i] <= v < edges[i + 1]:
                return i
        return None

    # 第一列（表頭）為欄標題；其後每列為資料列
    n_rows, n_cols = len(hs) - 1, len(vs) - 1
    col_labels = [" ".join(t for _, x, t in sorted(spans)
                           if band(x, vs) == c and band(_, hs) == 0)
                  for c in range(1, n_cols)]
    out_rows = []
    for r_i in range(1, n_rows):
        title = [t for y, x, t in sorted(spans)
                 if band(y, hs) == r_i and band(x, vs) == 0]
        # 列標題取該列帶之**第一行**（其後為說明文字）
        cells, texts = [], []
        for c_i in range(1, n_cols):
            cells.append(any(band(mx, vs) == c_i and band(my, hs) == r_i
                             for mx, my in marks))
            # **文字表**（如 p16 之 PIP1）之格內無勾記，其內容在文字裡 ——
            # 只回報「有無標記」會把整張文字表讀成一片 False。
            texts.append(" ".join(t for y, x, t in sorted(spans)
                                  if band(y, hs) == r_i and band(x, vs) == c_i))
        out_rows.append((" ".join(title) if title else "?", cells, texts))
    return {"grid": {"rows": n_rows - 1, "cols": n_cols - 1},
            "col_labels": col_labels, "rows": out_rows,
            "h_edges": hs, "v_edges": vs, "marks": len(marks)}


def regression() -> int:
    """重跑 p17 之 Table CPA2，與 16 輪之判讀比對（J-2 明文要求）。"""
    got = read_table(17, CPA2_CLIP)
    ok = True

    def chk(name, a, b):
        nonlocal ok
        good = a == b
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}")
        if not good:
            print(f"      16 輪判讀：{b}")
            print(f"      本次重跑：{a}")

    print("## 回歸 —— p17 Table CPA2（16 輪為肉眼判讀，本次以座標判定複驗）\n")
    print(f"  格線：水平 {got['h_edges']}")
    print(f"        垂直 {got['v_edges']}")
    print(f"  勾記置放數：{got['marks']}\n")
    chk("列數 × 欄數", got["grid"], CPA2_EXPECTED["grid"])
    chk("欄標題", got["col_labels"], CPA2_EXPECTED["col_labels"])
    for (gt, gc, _tx), (et, ec) in zip(got["rows"], CPA2_EXPECTED["rows"]):
        chk(f"列「{et}」之欄別 {ec}", [gt.startswith(et[:12]), gc],
            [True, ec])

    # 對照向（R-G9）：把某一格之預期翻面，須紅
    print("\n## 對照向 —— 翻掉一格之預期，須偵測出不符\n")
    bad = [(t, c[:]) for t, c in CPA2_EXPECTED["rows"]]
    bad[1][1][1] = True          # App Store 之 Local 欄改為「有標記」
    caught = any(g[1] != b[1] for g, b in zip(got["rows"], bad))
    ok &= caught
    print(f"  {'PASS' if caught else '**FAIL**'} — "
          f"App Store × Local 由『無』改『有』→ "
          f"{'偵測出不符' if caught else '**未偵測**'}")

    n = 2 + len(CPA2_EXPECTED["rows"]) + 1
    print(f"\n{n if ok else '<' + str(n)} / {n} checks "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--page", type=int)
    ap.add_argument("--clip", help="頁面比例 x0,y0,x1,y1（0–1）")
    ap.add_argument("--zoom", type=float, default=4.0)
    ap.add_argument("--out", default="/tmp/spec_region.png")
    ap.add_argument("--table", help="頁面座標 x0,y0,x1,y1（pt）")
    ap.add_argument("--regression", action="store_true")
    a = ap.parse_args()

    if a.regression:
        sys.exit(regression())
    if not a.page:
        ap.error("--page 為必要（除非 --regression）")
    if a.table:
        t = read_table(a.page, [float(x) for x in a.table.split(",")])
        print(f"格線：水平 {t['h_edges']}\n      垂直 {t['v_edges']}")
        print(f"勾記：{t['marks']} 處")
        print(f"欄：{t['col_labels']}")
        for title, cells, texts in t["rows"]:
            body = " | ".join(x for x in texts if x)
            print(f"  {title:<34}{cells} {body}")
        sys.exit(0)
    render(a.page, [float(x) for x in a.clip.split(",")] if a.clip else None,
           a.zoom, Path(a.out))
