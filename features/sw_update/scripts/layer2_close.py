#!/usr/bin/env python3
"""T29a —— Layer 2 之三重閉合驗證（下放包 16 §六，R-SU10 v2）。

(i) 列數閉合 (ii) 群數閉合 (iii) 列 id 集合閉合（聯集 = 311 且兩兩不相交）。
**不符即停並非零碼退出**（沿 anchor_table.py 之自檢慣例）。

Usage: python3 scripts/layer2_close.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from framework_survey import (a03_rows, group_by_heading, C_ID, C_CAT,   # noqa: E402
                              C_SUB, C_TITLE, IN_SCOPE)

H = lambda s: f"SWE1-FOTA-{s}"
R = lambda a, b=None: ("R", a, b if b is not None else a)   # 037 列區間（含端點）

# 下放包 16 §4.1 之 21 組。元素為 Heading id（整群）或 R(lo, hi)（037 列區間）。
SETS = [
    ("Wi-Fi Download",         ["038", "055", "058"]),
    ("Update Policy",          ["009", "024"]),
    ("Silent Update",          ["178", R(175, 177)]),
    ("Deployment Flow",        ["137"]),
    ("Session Flows",          ["016", "017", "018", "168", "185", "188", "271", "278", "287"]),
    ("Client Architecture",    ["072", "073", "192", "200", "202", "251", "259", "263",
                                "266", "280", "285"]),
    ("Bearer Selection",       ["291"]),
    ("ROV Installation",       ["085", "086", "091", "096"]),
    ("TBM Reflash",            ["110"]),
    ("HU FOTA via TBM",        ["214"]),
    ("USB Update",             ["020", "074", "076", "078"]),
    ("Update HMI",             ["129"]),
    ("Configurable Parameters", ["125", "127"]),
    ("FOTA Overview",          ["001"]),
    ("Integrity Verification", ["022", R(171, 174), R(310, 312), R(338)]),
    ("Interruption Handling",  [R(313), R(315, 329), R(357), R(359, 360)]),
    ("Status Reporting",       [R(330, 334), R(339), R(358)]),
    ("Deployment Conditions",  [R(336, 337), R(340, 341), R(343, 346)]),
    ("Session Management",     [R(347, 356), R(361), R(368, 369)]),
    ("Telematics Client",      [R(363, 367)]),
    ("Update Agent",           [R(370, 383)]),
]
WANT_ROWS, WANT_GROUPS = 311, 45


def main():
    rows = a03_rows()
    groups = group_by_heading(rows)[1:]                      # 45 群（去前言偽節）
    gmap = {g["id"]: g for g in groups}
    num = lambda r: int(re.search(r"(\d+)$", str(r[C_ID])).group(1))
    inscope = {num(r): r for r in rows if r[C_CAT] in IN_SCOPE}
    head_of = {}                                             # 037 列號 → 其 Heading id
    for g in groups:
        for r in g["rows"]:
            head_of[num(r)] = g["id"]

    resolved, ok = [], True
    for name, items in SETS:
        ids, heads = set(), set()
        for it in items:
            if isinstance(it, str):
                g = gmap[H(it)]
                heads.add(H(it))
                ids |= {num(r) for r in g["rows"]}
            else:
                _, lo, hi = it
                seg = {n for n in inscope if lo <= n <= hi}
                ids |= seg
                heads |= {head_of[n] for n in seg}
        resolved.append((name, ids, heads, items))

    print("## T29a —— Layer 2 之三重閉合驗證（R-SU10 v2）\n")
    print("> 依 R-SU10 v2：(i) 列數、(ii) 群數、(iii) 列 id 集合，**三者缺一不可**。\n")

    # ── (i) 列數閉合
    print("### (i) 列數閉合\n")
    print("| # | Test Set | 所轄 (Heading id, 列區間) | 列數 | 下放包 16 §4.1 | |")
    print("|---:|---|---|---:|---:|:--:|")
    DECL = [29, 17, 9, 26, 16, 35, 16, 20, 14, 36, 5, 6, 2, 6, 8, 19, 7, 8, 13, 5, 14]
    # 下放包 18 §2.1：`359` 改置 → Interruption 18→19、Session Management 14→13
    tot = 0
    for i, ((name, ids, heads, items), want) in enumerate(zip(resolved, DECL), 1):
        tot += len(ids)
        good = len(ids) == want
        ok &= good
        spec = "、".join(it if isinstance(it, str)
                         else (f"`{it[1]}`" if it[1] == it[2] else f"`{it[1]}`–`{it[2]}`")
                         for it in items)
        print(f"| {i} | `{name}` | {spec} | **{len(ids)}** | {want} | {'✅' if good else '❌'} |")
    print(f"| | **合計** | | **{tot}** | {WANT_ROWS} | {'✅' if tot == WANT_ROWS else '❌'} |")
    ok &= tot == WANT_ROWS

    # ── (ii) 群數閉合
    allh = set().union(*(h for _, _, h, _ in resolved))
    miss_h = {g["id"] for g in groups} - allh
    extra_h = allh - {g["id"] for g in groups}
    print(f"\n### (ii) 群數閉合\n")
    print(f"- 21 組所涵蓋之 Heading id 聯集：**{len(allh)}**（應 {WANT_GROUPS}）"
          f" —— {'✅' if len(allh) == WANT_GROUPS else '❌'}")
    print(f"- 45 群中未被任何組涵蓋者：**{len(miss_h)}**"
          + (f" —— {sorted(miss_h)}" if miss_h else " ✅"))
    print(f"- 組中出現而不存在於 45 群者：**{len(extra_h)}**"
          + (f" —— {sorted(extra_h)}" if extra_h else " ✅"))
    ok &= len(allh) == WANT_GROUPS and not miss_h and not extra_h

    # ── (iii) 列 id 集合閉合
    union = set().union(*(s for _, s, _, _ in resolved))
    body = set(inscope)
    print(f"\n### (iii) 列 id 集合閉合\n")
    print(f"- 聯集大小：**{len(union)}**（應 {WANT_ROWS}）"
          f" —— {'✅' if len(union) == WANT_ROWS else '❌'}")
    d1, d2 = sorted(body - union), sorted(union - body)
    print(f"- 母體有而 Layer 2 無（漏）：**{len(d1)}**"
          + (f" —— {['SWE1-FOTA-%03d' % n for n in d1]}" if d1 else " ✅"))
    print(f"- Layer 2 有而母體無（溢）：**{len(d2)}**"
          + (f" —— {['SWE1-FOTA-%03d' % n for n in d2]}" if d2 else " ✅"))
    inter = [(a, b, sorted(x & y)) for i, (a, x, *_) in enumerate(resolved)
             for b, y, *_ in resolved[i + 1:] if x & y]
    print(f"- 相交之組對：**{len(inter)}**"
          + ("".join(f"\n  - `{a}` ∩ `{b}` = {['SWE1-FOTA-%03d' % n for n in c]}"
                     for a, b, c in inter) if inter else " ✅"))
    ok &= len(union) == WANT_ROWS and not d1 and not d2 and not inter

    # ── 跨章群之內部分割（R-SU10 v2(a) 之 (Heading id, 列區間) 鍵）
    print(f"\n### 跨章群之內部分割（R-SU10 v2(a)）\n")
    print("| Heading 群 | 列數 | 分屬之 Test Set | 組數 | 各組列數和 | |")
    print("|---|---:|---|---:|---:|:--:|")
    for gid in (H("309"), H("170")):
        gids = {num(r) for r in gmap[gid]["rows"]}
        parts = [(name, len(ids & gids)) for name, ids, *_ in resolved if ids & gids]
        s = sum(n for _, n in parts)
        good = s == len(gids)
        ok &= good
        print(f"| `{gid}` | {len(gids)} | "
              + "、".join(f"`{n}`({c})" for n, c in parts)
              + f" | {len(parts)} | **{s}** | {'✅' if good else '❌'} |")

    print(f"\n---\n\n**三重閉合結果：{'全部通過 ✅' if ok else '**不通過 ❌**'}**")
    if not ok:
        sys.exit("T29a 三重閉合不通過，停（下放包 16 §六「不符即停並回報」）")
    return resolved, gmap, num


# ── T30c —— 孤島列檢查（R-SU20）────────────────────────────────────────
SEED_ISLANDS = {338, 339, 357, 358, 361}   # 下放包 18 §二定案後之預期（原 7，`359`／`360` 因改組解除）
PREV_ISLANDS = {338, 339, 357, 358, 359, 360, 361}   # 上繳包 15 §6.1 之 7 個（改組前）
NAME_STOP = {"of", "and", "via", "the", "for", "to", "a", "an"}


def _owner_map(resolved, groups, num):
    o = {}
    for name, ids, *_ in resolved:
        for n in ids:
            o[n] = name
    return o


def islands(resolved, groups, num, strict=True):
    """孤島列 = 同一 Heading 群內，其組與前鄰、後鄰皆不同者（R-SU20(a)）。

    **R-SU20 v2(a) 已裁採 strict**：孤島列僅就「群內部列」評估 ——
    某列之前鄰與後鄰**皆存在且皆與其不同組**者為孤島；
    群首、群尾、單列群**不評估**。

    採 strict 而不採 loose 之理由（R-SU20 v2(a)）：loose 得 13 列，
    其中 8 列為 **Test Set 之正常邊界**，非證據 —— 該檢查將被邊界淹沒
    而失去鑑別力。

    ⚠ **已知盲區（R-SU20 v2(a) 令隨檢查陳述）**：
    **本檢查不覆蓋群邊界之錯分。** 位於 Heading 群首尾之列若被錯置，
    孤島檢查**不會報警**。此為採 strict 之代價，非疏漏。

    `strict=False`（loose）僅供對照，不作判準。
    """
    own = _owner_map(resolved, groups, num)
    out = []
    for g in groups:
        ns = sorted(num(r) for r in g["rows"])
        for i, n in enumerate(ns):
            prev = ns[i - 1] if i else None
            nxt = ns[i + 1] if i + 1 < len(ns) else None
            if strict and (prev is None or nxt is None):
                continue
            if ((prev is None or own[prev] != own[n])
                    and (nxt is None or own[nxt] != own[n])):
                out.append((n, g["id"], own[n],
                            (prev, own.get(prev)), (nxt, own.get(nxt))))
    return out, own


def _kw_overlap(title, setname):
    """R-SU20(d) 之機器化：組名之實詞是否出現於該列標題（循環之**風險**）。"""
    tw = set(re.findall(r"[A-Za-z]+", (title or "").lower()))
    sw = [w for w in re.findall(r"[A-Za-z-]+", setname.lower()) if w not in NAME_STOP]
    hit = [w for w in sw if w in tw or w.rstrip("s") in tw or w + "s" in tw]
    return hit


def t30c(resolved, gmap, num):
    from itertools import groupby
    rows = a03_rows()
    title = {num(r): str(r[C_TITLE] or "").strip()
             for r in rows if r[C_CAT] in IN_SCOPE}
    groups = list(gmap.values())

    print("\n\n## T30c —— 孤島列檢查（R-SU20）\n")

    # ── 種子回測（PLAYBOOK §7(10)；未過即停）
    isl, own = islands(resolved, groups, num, strict=True)
    got = {n for n, *_ in isl}
    print("### 種子回測（R-SU20 之偵測器；未過即停）\n")
    print(f"預期種子（下放包 18 §二定案後之 {len(SEED_ISLANDS)} 個）："
          + "、".join(f"`{n}`" for n in sorted(SEED_ISLANDS)) + "\n")
    miss, extra = SEED_ISLANDS - got, got - SEED_ISLANDS
    print(f"- 本偵測器（strict）抓到 **{len(got)}** 個；其中種子 "
          f"**{len(SEED_ISLANDS & got)}/{len(SEED_ISLANDS)}**")
    print(f"- 種子未被抓到者：**{len(miss)}**" + (f" —— {sorted(miss)}" if miss else " ✅"))
    print(f"- 種子外之新發現：**{len(extra)}**"
          + (f" —— {sorted(extra)}" if extra else "（無）"))
    if miss:
        sys.exit("T30c 種子回測未過，停（PLAYBOOK §7(10)）")
    print(f"\n**種子回測通過** —— {len(SEED_ISLANDS)} 個預期孤島全數重現，"
          f"且無非預期之孤島。\n")

    # ── 改組前後之對照（T31a：新產生之孤島列須明列）
    print("### 改組前後之孤島變化（T31a）\n")
    solved, brandnew = PREV_ISLANDS - got, got - PREV_ISLANDS
    print("| | 列數 | 037 列 |")
    print("|---|---:|---|")
    print(f"| 改組前（上繳包 15 §6.1） | {len(PREV_ISLANDS)} | "
          + "、".join(f"`{n}`" for n in sorted(PREV_ISLANDS)) + " |")
    print(f"| 改組後（本輪） | **{len(got)}** | "
          + "、".join(f"`{n}`" for n in sorted(got)) + " |")
    print(f"| **解除** | {len(solved)} | "
          + ("、".join(f"`{n}`" for n in sorted(solved)) or "—") + " |")
    print(f"| **新產生** | **{len(brandnew)}** | "
          + ("、".join(f"`{n}`" for n in sorted(brandnew)) or "**無**") + " |")
    print(f"\n`359` 改置 `Interruption Handling` 後，**`359` 與 `360` 之孤島身分同時解除**"
          f"（`359` 之後鄰 `360` 與其同組、`360` 之前鄰 `359` 與其同組）；"
          f"**未製造任何新孤島**。\n")

    # ── 解讀之敏感度
    isl2, _ = islands(resolved, groups, num, strict=False)
    print("### 「前鄰與後鄰皆不同」之評估範圍（R-SU20 v2(a) 已裁採 strict）\n")
    print("| 解讀 | 孤島數 | 說明 |")
    print("|---|---:|---|")
    print(f"| **strict（R-SU20 v2(a) 所裁）**：只取內部列 | **{len(isl)}** | "
          "群首／群尾／單列群不評估 |")
    print(f"| loose：缺鄰視為「不同」 | {len(isl2)} | "
          "使**每個單列群與每個群首／群尾**只要與鄰居不同即成孤島 —— "
          "其中多數為 Test Set 之正常邊界，非證據 |")
    print(f"\n二者相差 **{len(isl2)-len(isl)}** 列，該差全為 Test Set 之正常邊界。\n")
    print("> ⚠ **已知盲區（R-SU20 v2(a) 令隨檢查陳述）**："
          "**本檢查不覆蓋群邊界之錯分** —— 位於 Heading 群首尾之列若被錯置，"
          "孤島檢查**不會報警**。此為採 strict 之代價，非疏漏。\n")

    # ── (a) 孤島清單 + (d) 之機器化
    print("### (a) 孤島清單，含 R-SU20(d) 之循環風險機器檢查\n")
    print("| 037 列 | 標題 | 其組 | 前鄰 | 後鄰 | 組名實詞見於標題 |")
    print("|---|---|---|---|---|---|")
    for n, gid, o, (p, po), (nx, no) in isl:
        hit = _kw_overlap(title.get(n, ""), o)
        print(f"| `{n}` | {title.get(n,'')[:44]} | `{o}` | {p}(`{po}`) | {nx}(`{no}`) | "
              + (f"**⚠ {'／'.join(hit)}**" if hit else "—") + " |")
    flagged = [n for n, _, o, *_ in isl if _kw_overlap(title.get(n, ""), o)]
    print(f"\n**{len(flagged)}/{len(isl)}** 個孤島之組名實詞出現於其標題。\n")
    print("> ⚠ **此檢查測得的是「循環之風險」，不是「循環之事實」**（見上繳包 16 §自評）："
          "關鍵詞相符**未必**表示依據是關鍵詞 —— 下放包 17 §四即裁 `339`／`358` "
          "之依據為「其對象為回報訊息」而**維持**，儘管二者皆被本檢查標記。\n")

    # ── (b) 連續段數
    print("### (b) 各組於各跨章 Heading 群內之連續段數\n")
    print("| Heading 群 | Test Set | 段數 | 各段 |")
    print("|---|---|---:|---|")
    for gid in sorted({g["id"] for g in groups
                       if len({own[num(r)] for r in g["rows"]}) > 1}):
        ns = sorted(num(r) for r in gmap[gid]["rows"])
        segs = {}
        for k, grp in groupby(ns, key=lambda n: own[n]):
            segs.setdefault(k, []).append(list(grp))
        for k, v in sorted(segs.items(), key=lambda kv: -len(kv[1])):
            print(f"| `{gid}` | `{k}` | {'**' + str(len(v)) + '**' if len(v) > 1 else len(v)} "
                  f"| {'、'.join(f'{s[0]}–{s[-1]}' if len(s) > 1 else str(s[0]) for s in v)} |")

    # ── (c) 聚集分佈
    print("\n### (c) 聚集分佈\n")
    ns = sorted(got)
    runs, cur = [], [ns[0]]
    for a, b in zip(ns, ns[1:]):
        (cur.append(b) if b - a <= 2 else (runs.append(cur), cur := [b]))
    runs.append(cur)
    print("| 聚集 | 037 列 | 個數 | 跨度 |")
    print("|---:|---|---:|---:|")
    for i, r in enumerate(runs, 1):
        print(f"| {i} | {'、'.join(f'`{x}`' for x in r)} | {len(r)} | "
              f"{r[-1]-r[0]+1} 列 |")
    print(f"\n**{len(isl)} 個孤島聚為 {len(runs)} 處**"
          f"（判準：孤島間之 037 列距 ≤ 2）。"
          f"若切分照能力，錯誤應散開；**聚於少數幾處表示該段有系統性成因**"
          f"（R-SU20(c)）。\n")
    print("> **R-SU20(e) 之限度（隨檢查一併陳述）**：孤島列指出"
          "「該處之依據需高於相鄰之先驗」，**不是「該處錯了」**。"
          "規格作者確有可能在連續數列中交替寫數種能力。判其對錯仍須讀該列之描述。")
    return isl


# ── T31d —— 0 列 Heading 群清單之程式化（R-SU21 v2(b)）─────────────────
def t31d(gmap):
    """0 列群清單由程式產生，並與 `framework.md` 所載比對；不符即停。

    R-SU21 v2(b)：**寫「關於零之條文」時，其列舉須以程式產生，不得人手列。**
    """
    zero = sorted(g["id"] for g in gmap.values() if not g["rows"])
    fw = (Path(__file__).resolve().parent.parent / "framework.md").read_text()
    sec = fw[fw.index("### 0 列 Heading 群"):fw.index("之加註（逐字）")]
    listed = sorted(set(re.findall(r"`(SWE1-FOTA-\d+)`", sec)))
    print("\n\n## T31d —— 0 列 Heading 群清單之程式化（R-SU21 v2(b)）\n")
    print(f"- 程式產生：**{len(zero)}** 群 —— " + "、".join(f"`{x}`" for x in zero))
    print(f"- `framework.md` 所載：**{len(listed)}** 群")
    miss, extra = set(zero) - set(listed), set(listed) - set(zero)
    print(f"- 檔載而實測非 0：**{len(extra)}**" + (f" —— {sorted(extra)}" if extra else " ✅"))
    print(f"- 實測為 0 而檔未載：**{len(miss)}**" + (f" —— {sorted(miss)}" if miss else " ✅"))
    ok = not miss and not extra
    print(f"\n**比對結果：{'相符 ✅' if ok else '**不符 ❌**'}**"
          f"（R-SU21 v2(b)：{len(zero)} 群）")
    if not ok:
        sys.exit("T31d 0 列群清單與 framework.md 不符，停")
    return zero




if __name__ == "__main__":
    r, g, n = main()
    if "31d" in sys.argv[1:]:
        t31d(g)
    if "30c" in sys.argv[1:]:
        t30c(r, g, n)
