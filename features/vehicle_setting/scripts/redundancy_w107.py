"""W-107（61 包 §5）—— 母體層之冗餘掃描（A-VS119 之未量部分）。

現行唯一性掃描只施於已交付之 TC。本檔改施於**母體 237 leaf 之來源條文**：

(1) 逐 leaf 取其 reqid 之條文正文，**去除 `[…]` 屬性段與節號**後正規化
    （R-VS39 之鍵：casefold ＋ 空白壓縮 ＋ 去首尾；另加數詞↔數字）
(2) 兩兩比對，列出**可測內容無法分辨**之組數與其 leaf id
(3) 其中已交付者、未交付者分列

**該數決定交付時「237 個 leaf 對應幾個相異驗證點」。**
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

NUM = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
       "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
# **不**去除值之方括號 —— 其為可測內容之一部分（`[Off]` vs `[High]`）。
# 屬性段已由 `norm_clause()` 之「捨去第一行」去除。
# 僅去除值內之 raw 碼前綴（`[1h: On]` → `[On]`）—— 二者指同一值，
# 其差別為書寫而非語意（R-VS39 之正規化精神）。
RAWPFX = re.compile(r"\[\s*[0-9A-Fa-f]{1,2}h\s*:\s*")
SEC = re.compile(r"^\s*\d+(?:\.\d+)*\s*")
LEAD_ID = re.compile(r"^\s*\d{7}\s*:\s*")
# 區塊之末尾會吸入**下一節之標題**（`blocks_with_sec()` 以區塊 id 切割，
# 節標題落在前一區塊之尾）。不去除者，該節之最後一個 leaf 恆不與人成組。
# 實例：`4858545` 吸入 `1.3.2.1.3.12 Stop-Start System Feature … {4858546}`，
# 致其與 `4858539` 不成組（38 輪 W-107 實測，A-VS122）。
TAIL_HEAD = re.compile(r"\s*\d+(?:\.\d+)+\s[^\n]*?\{\d{7}\}\s*$")


def norm_clause(text: str) -> str:
    """R-VS39 之鍵 ＋ 去屬性段／節號／前導 reqid ＋ 數詞→數字。"""
    body = "\n".join(text.split("\n")[1:]) if "\n" in text else text
    body = LEAD_ID.sub("", body)
    body = RAWPFX.sub("[", body)
    body = SEC.sub(" ", body)
    body = re.sub(r"\s+", " ", body).strip()
    while TAIL_HEAD.search(body):
        body = TAIL_HEAD.sub("", body)
    body = body.casefold()
    for w, d in NUM.items():
        body = re.sub(rf"\b{w}\b", d, body)
    return body


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}

    groups: dict[str, list[tuple[int, Path]]] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    delivered = set()
    for v in groups.values():
        delivered |= {tc["leaf_id"] for tc in
                      json.loads(max(v)[1].read_text(encoding="utf-8"))["tcs"]}

    # 母體 = `generatable.tsv` 之全部列（237 個 Functional leaf）
    key: dict[str, list[str]] = collections.defaultdict(list)
    missing = 0
    for leaf in gen:
        qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
        texts = [norm_clause(blocks[q]["text"]) for q in qs if q in blocks]
        if not texts:
            missing += 1
            continue
        key["\n@@\n".join(texts)].append(leaf)

    dups = sorted((v for v in key.values() if len(v) > 1), key=len, reverse=True)
    involved = sum(len(v) for v in dups)
    print(f"母體 {len(gen)} leaf（無條文可取者 {missing}）")
    print(f"相異之正規化條文鍵：**{len(key)}**")
    print(f"**可測內容無法分辨之組數：{len(dups)}**；涉及 leaf **{involved}**")
    print(f"→ 237 個 leaf 實際對應之相異驗證點 = {len(key)} ＋ 無條文 {missing} "
          f"= **{len(key) + missing}**\n")

    d_all, d_none, d_mix = [], [], []
    for grp in dups:
        n = sum(1 for x in grp if x in delivered)
        (d_all if n == len(grp) else d_none if n == 0 else d_mix).append((grp, n))
    print(f"| 類 | 組數 | leaf 數 |")
    print(f"|---|---:|---:|")
    for name, arr in (("組內全部已交付", d_all), ("組內全部未交付", d_none),
                      ("組內部分已交付", d_mix)):
        print(f"| {name} | {len(arr)} | {sum(len(g) for g, _ in arr)} |")
    print()
    for name, arr in (("組內全部已交付", d_all), ("組內部分已交付", d_mix),
                      ("組內全部未交付", d_none)):
        if not arr:
            continue
        print(f"### {name}")
        for grp, n in arr:
            mark = ["✅" if x in delivered else "⬜" for x in grp]
            print(f"  ({len(grp)}) " + "  ".join(f"{m}{x}" for m, x in zip(mark, grp)))
        print()


if __name__ == "__main__":
    main()
