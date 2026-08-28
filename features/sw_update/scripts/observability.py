#!/usr/bin/env python3
"""T33b／T33c —— 內部服務主體之普查、觀測通道之盤查（下放包 20 §五）。

**執行層只分類語形，不裁定該列是否真無可觀測後果**（下放包 20 §五 T33b）。

Usage: python3 scripts/observability.py 33b 33c
"""

import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, _rows_desc                                # noqa: E402
from anchor_table import CFTS, C_ID                                        # noqa: E402
from framework_survey import a03_rows, group_by_heading, C_CAT, C_TITLE, IN_SCOPE  # noqa: E402
from layer2_close import SETS, H                                           # noqa: E402

# ── 判準（逐一揭露，下放包 20 §五 T33b）───────────────────────────────
# (1) 內部服務主體 —— 取自全 311 列之主詞普查（見上繳包 19 §T33b 之主詞表）
INTERNAL = [
    r"SWMC", r"WiFi\s*Update\s*Service", r"WiFiUpdateService",
    r"USB\s*Update\s*Service", r"ROV\s*Update\s*Service",
    r"TBM\s*Update\s*Service", r"Arbiter\s*Service", r"WiFi\s*Manager",
    r"Connectivity\s*Manager", r"Update\s*Engine(?:\s*Manager)?",
    r"SW\s*Updater\s*(?:Service|Manager)", r"Redbend\s*(?:SWMC|Update\s*Agent)",
    r"ROV\s*FOTA\s*AppService", r"OTA\s*[Cc]lient",
]
RE_INTERNAL = re.compile("|".join(INTERNAL), re.I)

# (2) 外部可觀測面之語形（R-SU25(a) 所列之面）
EXTERNAL = {
    "HMI／畫面": r"\bHMI\b|screen|display|displayed|popup|pop-up|PU\d{3,4}|notification|prompt|message|icon|banner|toast",
    "使用者互動": r"\buser\b|press|touch|tap|select|button|opt[- ]?in|opt[- ]?out|defer|accept|decline",
    "版本／設定值": r"\bversion\b|software\s*version|SW\s*version|configuration\s*report|inventory",
    "CAN／訊號": r"\bCAN\b|\bsignal\b|\bDID\b|\$[A-Z_]+\.",
    "檔案／儲存": r"\bfile\b|filesystem|file\s*system|storage|partition|\bflash\b",
    "聲音／燈": r"\bchime\b|\bsound\b|\baudio\b|\bLED\b",
}
RE_EXTERNAL = {k: re.compile(v, re.I) for k, v in EXTERNAL.items()}


def classify(text):
    """回傳 (是否內部列, 命中之外部面清單)。

    判準：**主詞命中內部服務** 且 **全句無任何外部面語形** → 內部列。
    """
    hits = [k for k, r in RE_EXTERNAL.items() if r.search(text)]
    return bool(RE_INTERNAL.search(text)) and not hits, hits


def t33b():
    rows, d = _rows_desc()
    by = {str(r[C_ID]).strip(): r for r in a03_rows() if r[C_CAT] in IN_SCOPE}
    groups = group_by_heading(a03_rows())[1:]
    gmap = {g["id"]: g for g in groups}
    num = lambda s: int(s.rsplit("-", 1)[1])
    owner = {}
    for name, items in SETS:
        for it in items:
            if isinstance(it, str):
                for r in gmap[H(it)]["rows"]:
                    owner[str(r[C_ID]).strip()] = name
            else:
                for i in d:
                    if it[1] <= num(i) <= it[2]:
                        owner[i] = name

    print("## T33b —— 內部服務主體之普查（全 311 列）\n")
    print("### 判準（逐一揭露）\n")
    print("**(1) 內部服務主體**（取自全 311 列之主詞普查，見 §主詞表）：\n")
    print("```\n" + "\n".join(INTERNAL) + "\n```\n")
    print("**(2) 外部可觀測面之語形**（R-SU25(a) 所列之面）：\n")
    print("| 面 | regex |")
    print("|---|---|")
    for k, v in EXTERNAL.items():
        print(f"| {k} | `{v}` |")
    print("\n**分類**：主詞命中 (1) **且**全句無任何 (2) 之命中 → **內部列**。")
    print("> **執行層只分類語形，不裁定該列是否真無可觀測後果**（下放包 20 §五）。\n")

    # 主詞表
    subj = Counter()
    for t in d.values():
        for s in re.split(r"(?<=[.;])\s+|\*\s*", t):
            m = re.match(r"(?:The|the)?\s*([A-Za-z][A-Za-z0-9 _/\-]{2,40}?)\s+"
                         r"(?:shall|will|SHALL|should|must|is |are |can )", s.strip())
            if m:
                subj[m.group(1).strip()] += 1
    print("### 主詞表（前 16，供判準 (1) 之依據）\n")
    print("| 主詞 | 次數 | 內部？ |")
    print("|---|---:|:--:|")
    for k, v in subj.most_common(16):
        print(f"| `{k}` | {v} | {'✅' if RE_INTERNAL.search(k) else '—'} |")

    internal, mixed = [], []
    for i in sorted(d, key=num):
        is_int, hits = classify(d[i])
        (internal if is_int else mixed).append((i, hits))

    print(f"\n### 結果\n")
    print("| 類 | 列數 | 佔 311 |")
    print("|---|---:|---:|")
    print(f"| **內部列**（主詞為內部服務且無外部面語形） | **{len(internal)}** | "
          f"**{len(internal)/311*100:.0f}%** |")
    print(f"| 非內部列（有外部面語形，或主詞非內部服務） | {len(mixed)} | "
          f"{len(mixed)/311*100:.0f}% |")
    print(f"| **合計** | **{len(internal)+len(mixed)}** | 100% |")

    print(f"\n### 內部列之 id 清單（{len(internal)} 列）\n")
    print("；".join(f"`{i.rsplit('-',1)[1]}`" for i, _ in internal))

    print(f"\n\n### 內部列於 21 個 Test Set 之分佈\n")
    tot = Counter(owner[i] for i in d)
    cnt = Counter(owner[i] for i, _ in internal)
    print("| Test Set | 內部列 | 該組總列數 | 佔比 |")
    print("|---|---:|---:|---:|")
    for name, _ in SETS:
        c, t = cnt.get(name, 0), tot.get(name, 0)
        print(f"| `{name}` | {'**' + str(c) + '**' if c else 0} | {t} | "
              f"{c/t*100:.0f}% |" if t else f"| `{name}` | {c} | {t} | — |")
    print(f"| **合計** | **{len(internal)}** | **311** | "
          f"**{len(internal)/311*100:.0f}%** |")

    print(f"\n### 外部面之命中分佈（非內部列，{len(mixed)} 列）\n")
    fc = Counter(h for _, hs in mixed for h in hs)
    print("| 外部面 | 命中列數 |")
    print("|---|---:|")
    for k in EXTERNAL:
        print(f"| {k} | {fc.get(k,0)} |")
    nosubj = [i for i, hs in mixed if not RE_INTERNAL.search(d[i])]
    print(f"\n非內部列中，**主詞未命中內部服務清單者 {len(nosubj)} 列**"
          + (f"：{'、'.join('`'+x.rsplit('-',1)[1]+'`' for x in nosubj[:20])}"
             + ("…" if len(nosubj) > 20 else "") if nosubj else ""))
    return internal, mixed, owner


# ── T33c —— 觀測通道之盤查 ────────────────────────────────────────────
CHANNEL = {
    "adb": r"\badb\b", "logcat": r"\blogcat\b", "dumpsys": r"\bdumpsys\b",
    "log": r"\blog\b|\blogs\b|\blogging\b|log\s*tag",
    "trace": r"\btrace\b|\btracing\b",
    "diagnostic": r"\bdiagnostic|\bdiagnosis\b|\bUDS\b|\bDID\b|\bDTC\b",
    "debug": r"\bdebug\b|\bdeveloper\s*mode\b",
    "test hook": r"\btest\s*(?:hook|mode|interface)\b",
    "shell": r"\bshell\b|\bconsole\b",
}
RE_CH = {k: re.compile(v, re.I) for k, v in CHANNEL.items()}


def t33c():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    from anchor_table import A03
    print("\n\n## T33c —— 觀測通道之盤查\n")
    print("掃描語形（**查得與否皆如實回報，查無不得代以推定**）：\n")
    print("| 通道 | regex |")
    print("|---|---|")
    for k, v in CHANNEL.items():
        print(f"| {k} | `{v}` |")

    # (i) 037 全欄
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    ws = wb["AnalysisReport_FULL"]
    hits037 = defaultdict(list)
    n037 = 0
    for r in ws.iter_rows(min_row=8, values_only=True):
        if r[0] in (None, ""):
            continue
        n037 += 1
        blob = " ".join(str(x) for x in r if x not in (None, ""))
        for k, rx in RE_CH.items():
            if rx.search(blob):
                hits037[k].append(str(r[0]).strip())

    # (ii) CFTS 487 物件全文
    objs = corpus_v2()[0]
    hitsc = defaultdict(list)
    for o in objs:
        for k, rx in RE_CH.items():
            if rx.search(o["text"]):
                hitsc[k].append(o["oid"])

    # (iii) SYSAD 全文
    sysad = next(Path("inputs").glob("*SYSAD*.docx"))
    raw = zipfile.ZipFile(sysad).read("word/document.xml").decode("utf8", "replace")
    txt = re.sub(r"<[^>]+>", " ", raw)
    hitss = {k: len(rx.findall(txt)) for k, rx in RE_CH.items()}

    print(f"\n### 結果\n")
    print(f"| 通道 | (i) 037 全欄（{n037} 資料列） | (ii) CFTS_57（487 物件） | "
          f"(iii) SYSAD 全文 |")
    print("|---|---:|---:|---:|")
    for k in CHANNEL:
        a, b, c = len(hits037[k]), len(hitsc[k]), hitss[k]
        print(f"| `{k}` | {'**'+str(a)+'**' if a else 0} | "
              f"{'**'+str(b)+'**' if b else 0} | {'**'+str(c)+'**' if c else 0} |")
    tot = sum(len(v) for v in hits037.values()) + sum(len(v) for v in hitsc.values()) + sum(hitss.values())
    print(f"\n**三源合計命中：{tot}**")
    for lbl, hits in (("037", hits037), ("CFTS_57", hitsc)):
        for k, v in hits.items():
            print(f"\n- **{lbl} / `{k}`（{len(v)}）**："
                  + "、".join(f"`{x}`" for x in v[:12]) + ("…" if len(v) > 12 else ""))
    if hitss and any(hitss.values()):
        print("\n- **SYSAD**：" + "、".join(f"`{k}`×{v}" for k, v in hitss.items() if v))
    return hits037, hitsc, hitss


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"33b", "33c"}
    if "33b" in want:
        t33b()
    if "33c" in want:
        t33c()
