"""B3 前置 —— 代理量錨點可及性報告（R-P367 / G252）。

R-P367：代理量之錨點得取自 **G0 台帳所列文件**，台帳外一律不得為錨。
本 feature `sys1_export: null`，故 R-P353 / R-P354(b) 之「SYS1」為空集（A-PW354）。

母體：現行 corpus 之 `Read <X>` / `Check that <X>` 中**非白名單**之 `<X>`，
按原文去重。逐名標「台帳內有錨 / 無錨」，**不填代理量**
（R-P367：可及性報告經分析層覆核後始填代理量表）。

台帳可搜之文字面：
  - CFTS009 / CFTS010 / SYS3 之文字層，以 `{ObjectID}` 段落為錨單位
  - BHCAN2 / FDCAN8 之 `VAL_` 標籤（R-P367：`VAL_` 本身即為錨點）

用法：
    python features/power/scripts/proxy_reachability_59.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
TEXT = ROOT / "features/power/data/textlayer"
OUT = ROOT / "features/power/data/proxy_reachability_55.md"

READ_RE = re.compile(
    r"^\s*\d*\.?\s*(?:Read|Check that)\s+(.*?)"
    r"(?:\s+(?:and check that|to check).*)?$", re.I)
ANCHOR_RE = re.compile(r"^(49\d{5}):")
STOP = {"the", "a", "an", "and", "or", "of", "for", "in", "on", "to", "is",
        "it", "its", "that", "then", "with", "against", "through", "at"}


def anchored_paragraphs() -> list[tuple[str, str, str]]:
    """(來源, ObjectID, 段落文字)。以 `49xxxxx:` 為錨單位。"""
    out = []
    for src in ("cfts009", "cfts010", "sys3"):
        f = TEXT / f"{src}_plain.txt"
        if not f.exists():
            continue
        lines = f.read_text(errors="ignore").splitlines()
        for i, ln in enumerate(lines):
            m = ANCHOR_RE.match(ln)
            if m:
                body = " ".join(lines[i + 1:i + 4])
                out.append((src.upper(), m.group(1), body.lower()))
    return out


def val_labels() -> str:
    buf = []
    for p in ("forms/PDT27_E2A_R1_BHCAN2.dbc", "forms/PDT27_E2A_R1_FDCAN8.dbc"):
        t = (ROOT / p).read_text(encoding="cp1252", errors="replace")
        buf += re.findall(r"^VAL_ .*$", t, re.M)
        buf += re.findall(r"^CM_ SG_ .*$", t, re.M)
    return " ".join(buf).lower()


def tokens(x: str) -> list[str]:
    x = re.sub(r"^(the|a|an)\s+", "", x, flags=re.I)
    return [w for w in re.findall(r"[A-Za-z_$][A-Za-z0-9_$.]*", x.lower())
            if w not in STOP and len(w) > 2]


def main() -> None:
    cur = rm.load_current()
    counts: Counter = Counter()
    tcs: defaultdict = defaultdict(set)
    for tc in cur:
        for f in ("test_procedure", "expected_result"):
            for line in (tc.get(f) or "").splitlines():
                m = READ_RE.match(line)
                if not m:
                    continue
                obj = m.group(1).strip()
                if rm.whitelisted(obj):
                    continue
                obj = re.sub(r"^(the|a|an)\s+", "", obj, flags=re.I).strip(" .,")
                counts[obj] += 1
                tcs[obj].add(tc["tc_id"])

    paras = anchored_paragraphs()
    vals = val_labels()

    rows, has, none, subcount = [], 0, 0, 0
    for x, n in counts.most_common():
        tk = tokens(x)
        hits = []
        if tk:
            for src, oid, body in paras:
                if all(t in body for t in tk):
                    hits.append(f"{src}-{oid}")
                    if len(hits) >= 3:
                        break
        in_val = bool(tk) and all(t in vals for t in tk)
        ok = bool(hits) or in_val
        kind = "**有**" if ok else ""

        # 複合 `<X>`（`A and the B`／逗號並列）：全詞同段過嚴，改逐項判。
        # 每一項各自有錨者記「有（分項）」—— 代理量本就可分項指定。
        if not ok:
            parts = [q.strip(" .,") for q in re.split(r",| and ", x) if q.strip()]
            if len(parts) > 1:
                sub = []
                for q in parts:
                    qt = tokens(q)
                    if not qt:
                        continue
                    got = next((f"{sc}-{oid}" for sc, oid, b in paras
                                if all(t in b for t in qt)), None)
                    if got is None and all(t in vals for t in qt):
                        got = "DBC"
                    sub.append(f"{q[:24]}→{got or '無'}")
                if sub and all("→無" not in t for t in sub):
                    ok, kind = True, "**有（分項）**"
                    subcount += 1
                    hits = sub[:3]

        has += ok
        none += (not ok)
        if not kind:
            kind = "**無**"
        anchors = "、".join(hits) if hits else ("DBC `VAL_`/`CM_`" if in_val else "**無**")
        rows.append(f"| `{x[:72]}` | {n} | {len(tcs[x])} | {kind} | {anchors} |")

    body = [
        "# B3 前置 —— 代理量錨點可及性報告（59 包 / R-P367 / G252）",
        "",
        "> **本檔不填代理量。** R-P367 令可及性報告經分析層覆核後始填代理量表。",
        "> 母體：現行 corpus（283 條）之 `Read <X>` / `Check that <X>` 中"
        "**非白名單**之 `<X>`，按原文去重。",
        "> 錨點來源限 **G0 台帳**（CFTS009 / CFTS010 / SYS3 文字層之 `{ObjectID}` 段落"
        "＋ BHCAN2 / FDCAN8 之 `VAL_` / `CM_`）。台帳外文件一律不得為錨。",
        "> ⚠ 本 feature `sys1_export: null` —— R-P353 / R-P354(b) 之「SYS1」"
        "為空集（A-PW354），不列入錨點來源。",
        "",
        "## 判準",
        "",
        "`<X>` 去冠詞、去停用詞後取內容詞；**全部內容詞同時出現於同一錨點段落**"
        "者記「有錨」。此為**保守之機器判準**：",
        "",
        "- 偽陽性風險低（要求全詞同段），",
        "- **偽陰性風險高** —— 同義改寫、跨段落陳述皆會漏。",
        "",
        "故「無錨」之列**不等於查無**，只等於「以本判準未命中」，"
        "須人讀該 `<X>` 所屬 TC 之 `test_item` 上半 verbatim 再判。",
        "依 R-G13，本檔不得作為登記「查無」之依據。",
        "",
        f"## 總計：相異 `<X>` **{len(counts)}** 個"
        f"（出現 {sum(counts.values())} 次）",
        "",
        "| 判定 | 數 | 佔比 |",
        "|---|---|---|",
        f"| 有錨（全詞同段） | **{has - subcount}** | "
        f"{(has - subcount) / len(counts) * 100:.1f}% |",
        f"| 有錨（分項） | **{subcount}** | {subcount / len(counts) * 100:.1f}% |",
        f"| 無錨（本判準未命中）| **{none}** | {none / len(counts) * 100:.1f}% |",
        "",
        "## 逐名",
        "",
        "| `<X>`（原文） | 出現 | TC 數 | 錨 | 錨點（至多 3）|",
        "|---|---|---|---|---|",
    ] + rows + [""]
    OUT.write_text("\n".join(body))
    print(f"相異 <X>: {len(counts)}；有錨 {has}、無錨 {none}")
    print(f"→ {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
