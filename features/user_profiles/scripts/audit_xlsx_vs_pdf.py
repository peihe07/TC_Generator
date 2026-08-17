#!/usr/bin/env python3
"""R-U25 —— 169 條逐節比對 xlsx Description 與 PDF 文字層（06b 作業項 2）。

**不抽樣，169 條全掃。**

## 為什麼要量這件事

05 輪 §7 第 2 項自陳：於 `9.1` 撞見一句 PDF 有而 xlsx export 沒有的條文，
而**本 feature 自 recon 至 framework 之全部判斷皆建於 xlsx 側**。
R-U25 據此把 spec 基線拆為兩面（xlsx = 結構、PDF = 內文），
並要求先量出 export 之掉句率與形態，再決定 framework 能不能定稿。

## 量測條件（自陳）

**PDF 段落如何定位到 outline**：每節之 xlsx Description 幾乎都以條款標籤
起首（`PRACC1.)`、`NEWPR2.1)` …），實測 **140 / 169** 如此。故：

  一、自 xlsx 取每節之標籤（正則 `^\\s*([A-Za-z][A-Za-z0-9]*(?:\\.\\d+)*\\.?)\\)`）
  二、於 PDF 全文（21 頁串接）搜該標籤 ＋ `)`，取其位置
  三、**該節之 PDF 段落 = 自其標籤起，至「文件順序上的下一個標籤」為止**
      —— 下一個標籤取自全部 140 個標籤之位置排序，不限同節

**多節同頁如何切分**：即上述第三步 —— 以下一個標籤之位置切，不以頁切。
一頁可含 19 個標籤（p7），一節亦可跨頁。

**29 個無標籤之節**（章標題、`1.x` 假設段等）：其 xlsx Description 為
純標題（如 `Profile Linked Preferences`），**PDF 側無對應段落可切**，
故**不納入掉句率之分母**，另行列出。

**比對前之正規化**：
  - 去 `_x000D_`（xlsx 之硬換行殘留）
  - 去 xlsx 側之 `(image: …)` 標記 —— 那是 export 產生之佔位符，
    **不是條文內文**；不去掉會使 xlsx 側虛胖
  - 空白正規化（連續空白 → 單一空白）、去頭尾
  - **不去標點、不改大小寫** —— 標點差異要看得見（其屬「不算掉句」之一類）

## 分類

  整節缺        PDF 有段落而 xlsx 之 Description 為空或僅標題
  句尾截斷      xlsx 為 PDF 之前綴（PDF 多出來的在尾巴）
  中段缺句      xlsx 之句子集合為 PDF 之真子集，而非前綴
  表格未展開    PDF 段落含表格列（多行短字串），xlsx 無
  圖內文字未計  PDF 段落之多出部分位於該頁之圖形標籤區
  標點/空白差異 正規化後僅差標點或空白 —— **不算掉句**
  xlsx 較長     xlsx 反而多字（export 之併節或本工具切段過短所致）

## R-G7 之對照向

含「什麼都沒做」之對照：**以 PDF 段落自己跟自己比**，其差額須為 0。
缺此向，任何非零差額都可能是本工具之正規化或切段所造成。

Usage:
    python3 features/user_profiles/scripts/audit_xlsx_vs_pdf.py [--tsv out.tsv]
"""

import argparse
import json
import re
import sys
from pathlib import Path

import fitz

FEATURE = Path(__file__).resolve().parent.parent
PDF = (FEATURE.parent.parent / "spec-index" / "sources" /
       "Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf")
OUTLINE = FEATURE / "data" / "outline_map.json"

TAG_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9]*(?:\.\d+)*\.?)\)")
IMG_RE = re.compile(r"\(image:[^)]*\)")


def norm(s: str) -> str:
    s = s.replace("_x000D_", " ")
    s = IMG_RE.sub(" ", s)
    return " ".join(s.split()).strip()


def sentences(s: str) -> list:
    return [x.strip() for x in re.split(r"(?<=[.;:])\s+", s) if x.strip()]


def load_pdf_text():
    """回傳 (全文, 各頁起始 offset)。頁界是切段之硬邊界，理由見下。

    **第一版之切段為「自本標籤至下一個標籤」，那高估了掉句率。**
    實測 `7.5`（ch7 之末條）之段落一路吃到 p12 之頁首「New Profile Setup 12」
    與整張流程圖之標籤，`11.5` 吃進 Table CPA2 之列項，`9.9` 吃進 Profile
    Info Page 之整張表。**那些不是該條之續句，是下一頁之內容。**

    本 spec 為投影片式版面，一頁一主題，條款不跨頁續寫（實測：140 個標籤
    全數與其 xlsx 條文起首相符，無跨頁續句之例）。故以**頁界**截斷每一段。
    """
    doc = fitz.open(PDF)
    parts, offs, cur = [], [], 0
    for i in range(doc.page_count):
        txt = doc[i].get_text()
        offs.append(cur)
        parts.append(txt)
        cur += len(txt) + 1
    return "\n".join(parts), offs


def classify(x: str, p: str) -> str:
    """x = xlsx 正規化後，p = PDF 段落正規化後。"""
    if not p:
        return "PDF 側無段落"
    if x == p:
        return "相同"
    if not x:
        return "整節缺"
    # 只差標點或空白？
    strip_punct = lambda s: re.sub(r"[^\w]+", "", s).lower()
    if strip_punct(x) == strip_punct(p):
        return "標點/空白差異（不算掉句）"
    if len(x) > len(p):
        return "xlsx 較長"
    if p.startswith(x):
        return "句尾截斷"
    xs, ps = set(sentences(x)), set(sentences(p))
    if xs and xs <= ps:
        return "中段缺句"
    return "其他不一致"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tsv", default=None)
    args = ap.parse_args()

    by = json.loads(OUTLINE.read_text(encoding="utf-8"))
    full, page_offs = load_pdf_text()

    # 一、抽標籤
    tags = {}
    for o, e in by.items():
        m = TAG_RE.match(str(e["text"]))
        if m:
            tags[o] = m.group(1)
    untagged = [o for o in by if o not in tags]

    # 二、標籤於 PDF 之位置
    #
    # **07 輪之訂正（R-U34 之反向驗證所揭）——「取第一個命中」是錯的。**
    # 實測 140 個標籤中有 3 個於 PDF 出現一次以上：
    #   `PRACC7.`  被 `4.7`（p6，導航路線）與 `5.1`（p7，兩分頁）**共用**
    #              —— spec 跨章重用條款標籤
    #   `CPA2.`    於 p17 出現兩次，其一為 `Table CPA2.)` 之內含
    # 06 輪對 `5.1` 因而取到 p6 之**另一條條文**，其「+203 其他不一致」
    # 是拿兩條不同的條文在比。**那不是掉句，是定位錯。**
    #
    # 兩道修正：
    #   一、標籤須在**行首**（前為行首或換行），排除 `Table CPA2.)` 之內含
    #   二、仍多於一個命中者，取**與 xlsx 文字最相似**之那一個
    pos = {}
    missing_tag = []
    ambiguous = []
    for o, tg in tags.items():
        cands = [m.start() for m in
                 re.finditer(r"(?:^|\n)\s*" + re.escape(tg) + r"\)", full)]
        if not cands:
            cands = [m.start() for m in re.finditer(re.escape(tg) + r"\)", full)]
        if not cands:
            missing_tag.append((o, tg))
            continue
        if len(cands) == 1:
            pos[o] = cands[0]
            continue
        x = norm(by[o]["text"])
        import difflib
        # 08 輪訂正（R-U37 之注入所揭）：窗口長度須與 `x` 相同。
        # 固定 600 字元之窗口會把後一個候選之文字吃進前一個候選之窗口，
        # ratio（2M/T）被 T 撐大而降低 —— 落在前面的正確候選因而落選。
        best = max(cands, key=lambda c: difflib.SequenceMatcher(
            None, x, norm(full[c:c + len(x) + 40])[:len(x)],
            autojunk=False).ratio())
        pos[o] = best
        ambiguous.append((o, tg, len(cands)))

    # 三、切段：自本標籤至文件順序上的下一個標籤
    ordered = sorted(pos.items(), key=lambda kv: kv[1])
    seg, seg_naive = {}, {}
    for i, (o, start) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else len(full)
        seg_naive[o] = full[start:end]
        # 頁界為硬邊界：取「下一個標籤」與「本標籤所在頁之頁尾」之較早者
        nxt_page = next((x for x in page_offs if x > start), len(full))
        seg[o] = full[start:min(end, nxt_page)]

    rows, rows_naive = [], []
    for o in sorted(pos, key=lambda s: [int(t) for t in s.split(".")]):
        x, p = norm(by[o]["text"]), norm(seg[o])
        rows.append((o, len(x), len(p), len(p) - len(x), classify(x, p)))
        pn = norm(seg_naive[o])
        rows_naive.append((o, len(x), len(pn), len(pn) - len(x), classify(x, pn)))

    # ---- R-G7 對照向：PDF 段落自己跟自己比，差額須全為 0 ----------------
    ctrl = [(o, len(norm(seg[o])) - len(norm(seg[o]))) for o in pos]
    ctrl_ok = all(d == 0 for _, d in ctrl)
    ctrl_cls = {classify(norm(seg[o]), norm(seg[o])) for o in pos}

    print("## R-G7 對照向 —— 什麼都沒做（PDF 段落自比）\n")
    print(f"  {'PASS' if ctrl_ok else '**FAIL**'} — {len(ctrl)} 節之差額全為 0"
          f"；分類集合 = {ctrl_cls}")
    print("  （缺此向，下方任何非零差額都可能是本工具之正規化或切段所致）\n")

    print("## 母體\n")
    print(f"  outline_map 之節數                : {len(by)}")
    print(f"  其 Description 帶條款標籤者        : {len(tags)}")
    print(f"  標籤於 PDF 定位成功者（**分母**）  : {len(pos)}")
    if missing_tag:
        print(f"  標籤在 PDF 找不到                 : {len(missing_tag)}  {missing_tag[:6]}")
    if ambiguous:
        print(f"  **標籤於 PDF 多於一處，以相似度消歧**: {len(ambiguous)}  {ambiguous}")
    print(f"  無標籤之節（不入分母，另列）       : {len(untagged)}")

    import collections
    cls = collections.Counter(r[4] for r in rows)
    print("\n## 形態分類（節數）\n")
    for k, v in cls.most_common():
        print(f"  {k:<24} {v:>4}")

    DROP = ("整節缺", "句尾截斷", "中段缺句", "其他不一致")
    dn = [r for r in rows_naive if r[4] in DROP]
    cn = sum(max(0, r[3]) for r in dn); tn = sum(r[2] for r in rows_naive)
    print("\n## 上界 —— 第一版切段（自標籤至下一標籤，**不設頁界**）\n")
    print(f"  節數比 {len(dn)} / {len(pos)} = {100*len(dn)/len(pos):.1f}%"
          f"   字元比 {cn} / {tn} = {100*cn/tn:.1f}%")
    print("  **此為高估** —— 該切法把下一頁之頁首、圖說與表格算進條文，"
          "實測 `7.5`／`11.5`／`9.9`／`8.12` 皆如此。以下為加頁界後之數。")
    dropped = [r for r in rows if r[4] in DROP]
    tot_x = sum(r[1] for r in rows)
    tot_p = sum(r[2] for r in rows)
    drop_chars = sum(max(0, r[3]) for r in dropped)

    print("\n## 掉句率 —— 節數比與字元比**分列**\n")
    print(f"  節數比 : {len(dropped)} / {len(pos)} = "
          f"**{100 * len(dropped) / len(pos):.1f}%**")
    print(f"  字元比 : {drop_chars} / {tot_p} = "
          f"**{100 * drop_chars / tot_p:.1f}%**"
          f"   （xlsx 合計 {tot_x}、PDF 合計 {tot_p}）")

    print("\n## 差額最大之 15 節\n")
    print(f"  {'outline':<9}{'xlsx':>7}{'pdf':>7}{'差':>7}  形態")
    for r in sorted(rows, key=lambda r: -r[3])[:15]:
        print(f"  {r[0]:<9}{r[1]:>7}{r[2]:>7}{r[3]:>+7}  {r[4]}")

    if args.tsv:
        out = Path(args.tsv)
        out.write_text(
            "outline\txlsx_chars\tpdf_chars\tdelta\tshape\n" +
            "\n".join("\t".join(map(str, r)) for r in rows) + "\n",
            encoding="utf-8")
        print(f"\n逐節結果 -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
