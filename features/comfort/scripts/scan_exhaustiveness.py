#!/usr/bin/env python3
"""Exhaustiveness scans over all 129 clauses — handoff 17 §3.1 / §3.2.

Profile §3.2 says the configuration axes appear "逐節出現"; §3.4 lists four
classes of source token. Both are UNIVERSAL claims, and a universal claim can
be checked mechanically. That is what this does — and only that.

  §3.1 → data/source_tokens.tsv         token | count | outlines
  §3.2 → data/config_axis_candidates.tsv  outline | pattern | full sentence

TWO THINGS THIS DOES NOT DO, on instruction:
  - It does not judge whether a token should be quoted verbatim (17 §3.1:
    「不判斷是否應照錄，僅列全集」).
  - It does not judge whether a candidate is a configuration axis (17 §3.2:
    「這算不算一個配置軸」= 判斷，分析層).

R-C13 DISCIPLINE: this is a lexical tool. A pattern that matches nothing is
an index-layer fact, never "this clause has no configuration condition". So
the script also samples 15 clauses at a fixed seed for a human read-through,
because the only way to find a condition phrased outside the pattern list is
to read clauses that the pattern list did not select.

Usage:
    python3 features/comfort/scripts/scan_exhaustiveness.py
"""

import csv
import re
import random
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
SRC = FEATURE / "data" / "section_fulltext.tsv"
OUT_TOKENS = FEATURE / "data" / "source_tokens.tsv"
OUT_AXES = FEATURE / "data" / "config_axis_candidates.tsv"

EXPECTED_ROWS = 129
SAMPLE_N = 15
SAMPLE_SEED = 20260815      # fixed and recorded, so the read-through repeats

# ---- §3.1 token classes (17 §3.1, verbatim list) ------------------------
QUOTE_CHARS = set('"\'[]<>')
NUM_PATTERNS = [
    ("digit+h", r"\b\d+h\b"),
    ("digit/digit", r"\b\d+/\d+\b"),
    ("digit-digit", r"\b\d+-\d+\b"),
    ("digit°", r"\b\d+°"),
]
ALLCAPS = re.compile(r"\b[A-Z][A-Z0-9]*(?:[ /][A-Z][A-Z0-9]*)*\b")
ALLCAPS_MIN = 2             # at least two chars, so "A" alone is not a token

# ---- §3.2 configuration-axis patterns (17 §3.2, verbatim list) ----------
# 19 §6 —— 九軸複掃。判準為 profile §3.2 之八軸 ＋ 19 §2.1 之第九軸
# （secondary lower screen）之**字面表述全集**，而非 17 §3.2 之泛用條件句式。
# 17 §3.2 之句式表實測會漏掉 profile 自己已列的軸（Standard 座椅、MTC、
# 單區），故本輪改以軸名直掃，兩表並用。
NINE_AXES = [
    ("軸1 ATC/MTC", r"\b(ATC|MTC)\b"),
    ("軸2 zone", r"\b(single|dual|quad|two|three|four)[- ]zone\b|\bzone climate\b"),
    ("軸3 tri-mode", r"\btri[- ]?mode\b"),
    ("軸4 MAX A/C", r"\bMAX A/C\b"),
    ("軸5 MAX DEF", r"\bMAX DEF(ROST)?\b"),
    ("軸6 獨立座椅分區", r"\b(independent )?seat zone\b"),
    ("軸7 加熱方向盤等級", r"\b(Multi[- ]Level|Single[- ]Level).{0,40}(wheel|steering)|"
                        r"(wheel|steering).{0,40}(Multi[- ]Level|Single[- ]Level)"),
    ("軸8 座椅等級", r"\b(Standard|Multi[- ]Level)\s+Heated/Vented\b"),
    ("軸9 lower screen", r"\blower screen\b|\bsecondary lower screen\b|"
                        r"\blower comfort screen\b|\blower hvac screen\b"),
]

AXIS_PATTERNS = [
    ("Some vehicles", r"\bsome vehicles\b"),
    ("In some vehicles", r"\bin some vehicles\b"),
    ("For vehicles with", r"\bfor vehicles (with|equipped|that)\b"),
    ("if the vehicle is configured", r"\bif the vehicle is configured\b"),
    ("when equipped", r"\b(when|if) equipped\b"),
    ("in certain modes", r"\bin certain\b"),
    ("R1 Low / R1 High / R1H", r"\bR1\s?(Low|High|H|M|L)\b"),
    ("is available", r"\bis (available|unavailable)\b"),
    ("if this feature available", r"\bif (this )?feature\b"),
    ("depending on vehicle configuration", r"\bdepending on\b"),
    ("(… only)", r"\(\s*[^)]*\bonly\b[^)]*\)"),
]
SENT_SPLIT = re.compile(r"(?<=[.;:])\s+|\n")


def load() -> list[dict]:
    rows = list(csv.DictReader(SRC.open(encoding="utf-8"), delimiter="\t"))
    for r in rows:
        r["text"] = r["full_text"].replace("\\n", "\n")
    return rows


def scan_tokens(rows) -> list[tuple]:
    counts: Counter = Counter()
    where: dict = defaultdict(set)

    def add(tok, outline):
        counts[tok] += 1
        where[tok].add(outline)

    for r in rows:
        o, t = r["outline"], r["text"]
        for ch in t:
            if ord(ch) > 127:
                add(f"NONASCII {ch!r} U+{ord(ch):04X} "
                    f"{unicodedata.name(ch, '?')}", o)
            elif ch in QUOTE_CHARS:
                add(f"QUOTE {ch!r}", o)
        for name, pat in NUM_PATTERNS:
            for m in re.findall(pat, t):
                add(f"NUM[{name}] {m if isinstance(m, str) else m[0]}", o)
        for m in ALLCAPS.findall(t):
            if len(m.replace(" ", "").replace("/", "")) >= ALLCAPS_MIN:
                add(f"ALLCAPS {m}", o)

    def okey(s):
        return tuple(int(p) for p in s.split("."))
    return [(tok, counts[tok],
             ",".join(sorted(where[tok], key=okey)))
            for tok in sorted(counts, key=lambda k: (-counts[k], k))]


def scan_nine_axes(rows) -> tuple[dict, list]:
    """19 §6 —— 以九軸之字面表述直掃全 129 節。

    R-C13 重申：未命中任何軸而含條件句式者，只是索引層事實，**不得作為
    「無其他軸」之結論**，只得作為「已盡機械之力」之記錄。
    """
    hits: dict = {name: [] for name, _ in NINE_AXES}
    per_clause: dict = {}
    for r in rows:
        found = [name for name, pat in NINE_AXES
                 if re.search(pat, r["text"], re.I)]
        per_clause[r["outline"]] = found
        for n in found:
            hits[n].append(r["outline"])
    return hits, per_clause


def scan_axes(rows) -> list[tuple]:
    out = []
    for r in rows:
        o, t = r["outline"], r["text"]
        for sent in [s.strip() for s in SENT_SPLIT.split(t) if s.strip()]:
            for name, pat in AXIS_PATTERNS:
                if re.search(pat, sent, re.I):
                    out.append((o, name, sent.replace("\t", " ")))
    return out


def main() -> None:
    rows = load()
    if len(rows) != EXPECTED_ROWS:
        sys.exit(f"expected {EXPECTED_ROWS} clauses, read {len(rows)}")

    tokens = scan_tokens(rows)
    OUT_TOKENS.write_text(
        "\n".join(["token\tcount\toutlines"] +
                  ["\t".join([t, str(c), w]) for t, c, w in tokens]) + "\n",
        encoding="utf-8")

    axes = scan_axes(rows)
    OUT_AXES.write_text(
        "\n".join(["outline\tpattern\tsentence"] +
                  ["\t".join(a) for a in axes]) + "\n", encoding="utf-8")

    print(f"clauses scanned      : {len(rows)}")
    print(f"§3.1 distinct tokens : {len(tokens)}  -> "
          f"{OUT_TOKENS.relative_to(ROOT)}")
    print(f"§3.2 axis matches    : {len(axes)} across "
          f"{len({a[0] for a in axes})} clauses -> "
          f"{OUT_AXES.relative_to(ROOT)}")

    hit = {a[0] for a in axes}
    miss = [r["outline"] for r in rows if r["outline"] not in hit]
    print(f"\nclauses with NO axis pattern hit: {len(miss)}")
    print("  (R-C13: an index-layer fact only — NOT 'these have no "
          "configuration condition')")

    # ---- 19 §6 nine-axis rescan over all 129 clauses ---------------------
    nine, per_clause = scan_nine_axes(rows)
    print(f"\n{'=' * 72}\n19 §6 —— 九軸機械複掃（全 {len(rows)} 節）\n{'=' * 72}")
    for name, _ in NINE_AXES:
        outs = nine[name]
        print(f"  {name:22} {len(outs):3} 節  {outs[:12]}{' …' if len(outs) > 12 else ''}")
    covered = [o for o, f in per_clause.items() if f]
    print(f"\n  命中至少一軸: {len(covered)} / {len(rows)} 節")
    # clauses with a conditional phrase but no axis hit -> for the analysis layer
    cond = {a[0] for a in axes}
    residue = sorted(cond - set(covered), key=lambda s: [int(p) for p in s.split(".")])
    print(f"  含條件句式但九軸皆未命中: {len(residue)} 節 -> {residue}")
    print("  （R-C13：此為索引層事實，不得作為「無其他軸」之結論）")

    # ---- the read-through the pattern list cannot replace -----------------
    rnd = random.Random(SAMPLE_SEED)
    sample = rnd.sample(rows, SAMPLE_N)
    print(f"\n{'=' * 72}\n隨機 {SAMPLE_N} 節人工過目（seed={SAMPLE_SEED}，固定可重現）\n{'=' * 72}")
    for r in sample:
        tag = "PATTERN-HIT" if r["outline"] in hit else "no-pattern-hit"
        print(f"\n--- {r['outline']}  [{tag}]  ({r['test_set']}) ---")
        print(r["text"])


if __name__ == "__main__":
    main()
