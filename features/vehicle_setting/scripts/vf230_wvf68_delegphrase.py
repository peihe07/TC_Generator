"""VF230：條文委派語路徑（R-VF75 二、A-VF21）。

既有之委派判定（W-VF48）比對之對象為**他 feature 之 037**，
其結論 627 條全 `no`。但 `E-Save-095` 之條文自陳
「managed in CFTS 088」—— CFTS 088 不在 `features/` 之下，
比對不到，故該路徑**恆不可能報出**。

本式為**第二路徑**：直接讀條文之委派語。
其結論**獨立成表**，不改動既有 627 個 `no`（R-VF75 二）。
"""
import csv, json, re
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent

# 委派語之已知樣式。**已知集合，非全集**（R-VF71 三）——
# 未列之措辭不會被報出，其值為「未查」而非「無」。
DELEG = [
    (re.compile(r"managed in\s+(CFTS\s*\d+)", re.I), "managed in"),
    (re.compile(r"(?:defined|specified|described|covered)\s+in\s+(CFTS\s*\d+)", re.I), "defined in"),
    (re.compile(r"refer to\s+(CFTS\s*\d+)", re.I), "refer to"),
    (re.compile(r"(?:handled|implemented)\s+by\s+(CFTS\s*\d+)", re.I), "handled by"),
]


def main() -> None:
    lv = list(csv.DictReader(open(FEAT / "data/vf230_leaves.tsv", encoding="utf-8"),
                             delimiter="\t"))
    rows = []
    for lf in lv:
        text = re.sub(r"\s+", " ", (lf["title"] + " " + lf["desc"]).replace("\\n", " "))
        for rx, kind in DELEG:
            m = rx.search(text)
            if m:
                target = re.sub(r"\s+", " ", m.group(1)).upper()
                rows.append({
                    "leaf_id": lf["swe_id"],
                    "deleg_phrase": kind,
                    "deleg_target": target,
                    "target_in_features": "no",   # 皆不在 features/ 之下，逐條複核於下
                    "quote": text[max(0, m.start() - 60):m.end() + 20].strip(),
                })
                break

    out = FEAT / "docs/reports/vf230_deleg_phrase.tsv"
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else
                           ["leaf_id", "deleg_phrase", "deleg_target",
                            "target_in_features", "quote"], delimiter="\t")
        w.writeheader(); w.writerows(rows)

    # 逐條複核 target 是否在 features/ 之下 —— 有則為真委派，須升為 blocker
    feats = {p.name.lower() for p in (FEAT.parent).iterdir() if p.is_dir()}
    print(f"條文委派語路徑：{len(rows)} 條命中（獨立表，既有 627 個 `no` 不動）")
    for r in rows:
        hit = any(r["deleg_target"].replace(" ", "").lower() in f.replace("_", "")
                  for f in feats)
        r["target_in_features"] = "yes" if hit else "no"
        print(f"  {r['leaf_id'][:40]:42} [{r['deleg_phrase']:11}] -> {r['deleg_target']:10} "
              f"在 features/ 之下：{'**是**' if hit else '否'}")
        print(f"      「{r['quote']}」")
    print(f"\n  → {out.relative_to(FEAT)}")
    print("  既有 delegation 表未動：以下為複核")
    d = list(csv.DictReader(open(FEAT / "docs/reports/vf230_delegation.tsv",
                                 encoding="utf-8"), delimiter="\t"))
    from collections import Counter
    print(f"    {len(d)} 列，verdict {dict(Counter(x['delegate'] for x in d))}")


if __name__ == "__main__":
    main()
