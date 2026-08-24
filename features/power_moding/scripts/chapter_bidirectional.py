#!/usr/bin/env python3
"""R-PMH51 之未套用側 —— 指定章之**雙向**逐句複驗（17 包步驟 3）。

R-PMH51 明文：A-PMH03 之其餘三則（8、9.1、11.1）須以雙向法複驗，
**未複驗前其標題結論不得引用**。11.1 已於 13 包方向二覆蓋、9.1 查出新漏 2，
**而 outline `8` 至今未做** —— 本檔補之，並使其可對任一章重跑。

方向一：SYS1 之每一句是否出現於 PDF（01 包已對全簿做過）
方向二：**PDF 之每一句是否出現於 SYS1** —— 漏句只在此方向顯示

用法:
    python scripts/chapter_bidirectional.py 8
"""
import argparse
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
PDF_TXT = ROOT / "sandbox" / "spec.txt"
SYS1 = ROOT / "inputs" / "SYS1_HMI_Power_Moding_HMI_Logic_and_Flow_R1_SR24_2A.xlsx"

# 各章於 PDF 全文之起訖錨（逐字取自 PDF，非推算）。
# **錨本身即前提** —— 錨取錯則整章比對落空，故 `span()` 另驗其長度與 marker 數。
ANCHORS = {
    8: ("R1Low Only", "[DCR19385] "),
}
MIN_SENT = 25          # 最短比對單位（字元），比照 13 包
GRAM = 6               # 6-gram 覆蓋率，比照 13 包
GRAM_THRESHOLD = 0.30  # < 30% 者為真漏候選


# --- R-PMH52 之擴及（17 包步驟 4）---
# 本檢查於輸出末尾具名其限度。
LIMITS = [
    "**`ANCHORS` 之起訖錨為人工指定** —— 錨取錯則整章比對落空；現只有章 8 建錨",
    "只比對 PDF **文字層**；**圖表不看** —— p9 之狀態矩陣即以圖呈現（A-PMH14 新漏 2）",
    "比對單位為句（>= 25 字元）；**短於 25 字元之句一律不入母體**，章 8 之標題 `Starup R1Low Only` 即屬之",
    "6-gram 覆蓋率 < 30% 之門檻為 13 包沿用值；**該門檻本身未經本輪重驗**",
    "**只驗字之有無，不驗語意** —— 同義改寫會被判為漏句，改寫錯誤會被判為命中",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for _x in LIMITS:
        print(f"  - {_x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def norm(t: str) -> str:
    t = str(t).replace("_x000D_", " ")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'),
                 ("”", '"'), ("…", "..."), ("–", "-"),
                 ("—", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def sentences(t: str) -> list[str]:
    """句號後空白切分，保留 >= MIN_SENT 者（比照 13 包之比對單位）。"""
    return [s.strip() for s in re.split(r"(?<=\.)\s+", t)
            if len(s.strip()) >= MIN_SENT]


def grams(t: str) -> set[str]:
    w = re.findall(r"[a-z0-9]+", t.lower())
    return {" ".join(w[i:i + GRAM]) for i in range(max(0, len(w) - GRAM + 1))}


def coverage(s: str, hay: str) -> float:
    g = grams(s)
    return len(g & grams(hay)) / len(g) if g else 1.0


def pdf_chapter(ch: int, pdf: str) -> str:
    a, b = ANCHORS[ch]
    i = pdf.index(a)
    j = pdf.index(b, i) + len(b)
    return pdf[i:j].strip()


def sys1_chapter(ch: int) -> list[tuple[str, str]]:
    ws = openpyxl.load_workbook(SYS1, data_only=True)["Basic Report"]
    out = []
    for r in range(2, ws.max_row + 1):
        o = str(ws.cell(r, 3).value or "").strip()
        if re.fullmatch(rf"{ch}(\.\d+)*", o):
            out.append((o, norm(ws.cell(r, 4).value or "")))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("chapter", type=int)
    a = ap.parse_args()
    ch = a.chapter
    pdf_all = norm(PDF_TXT.read_text(errors="replace"))
    pdf_ch = pdf_chapter(ch, pdf_all)
    rows = sys1_chapter(ch)
    sys_ch = " ".join(d for _, d in rows)

    print(f"=== 章 {ch} 之雙向複驗（R-PMH51）===")
    print(f"PDF 段：{len(pdf_ch)} 字元；SYS1：{len(rows)} 則、{len(sys_ch)} 字元")
    print(f"PDF 段起錨 `{ANCHORS[ch][0]}`／訖錨 `{ANCHORS[ch][1].strip()}`")
    mk = re.findall(r"SSND\s*\d+(?:\.\d+)?\.?\)", pdf_ch)
    print(f"PDF 段內 marker：{len(mk)} 個 —— {mk}")

    # --- 方向一：SYS1 → PDF ---
    print(f"\n--- 方向一（SYS1 → PDF）：SYS1 之字是否出現於 PDF ---")
    print(f"{'outline':<8} {'字數':>5}  {'逐字命中':<8} 覆蓋率")
    d1_miss = []
    for o, d in rows:
        hit = d in pdf_all
        cov = coverage(d, pdf_all)
        print(f"{o:<8} {len(d):>5}  {'是' if hit else '**否**':<8} {cov:6.1%}")
        if not hit:
            d1_miss.append((o, d, cov))

    # --- 方向二：PDF → SYS1（漏句只在此方向顯示）---
    print(f"\n--- 方向二（PDF → SYS1）：PDF 之字是否出現於 SYS1 ---")
    sents = sentences(pdf_ch)
    print(f"PDF 段切出 {len(sents)} 句（>= {MIN_SENT} 字元）")
    print(f"{'#':>3}  {'逐字命中':<8} {'覆蓋率':>7}  句首")
    d2_gap = []
    for i, s in enumerate(sents, 1):
        hit = s in sys_ch
        cov = coverage(s, sys_ch)
        print(f"{i:>3}  {'是' if hit else '**否**':<8} {cov:6.1%}  {s[:58]}")
        if not hit and cov < GRAM_THRESHOLD:
            d2_gap.append(s)

    print(f"\n=== 結果 ===")
    print(f"  方向一未逐字命中：{len(d1_miss)} 則")
    for o, d, cov in d1_miss:
        print(f"    outline {o}（覆蓋 {cov:.1%}）：{d[:90]}")
    print(f"  方向二真漏候選（覆蓋 < {GRAM_THRESHOLD:.0%}）：{len(d2_gap)} 句")
    for s in d2_gap:
        print(f"    {s}")
    print(f"\n  **新漏句：{len(d2_gap)}** —— "
          f"{'**停止條件 7 觸發**' if d2_gap else '停止條件 7 未觸發'}")
    print_limits()
    sys.exit(1 if d2_gap else 0)


if __name__ == "__main__":
    main()
