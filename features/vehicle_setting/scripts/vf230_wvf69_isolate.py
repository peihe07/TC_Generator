"""VF230：26 條隔離表與量產母體（W-VF69 §3，依 R-VF77 一）。

隔離之二類：
  純 `propId` 式 —— 訊號送出型中**只有** Android 屬性層寫法者。
                    其條文無 `TELEMATIC_*` 訊號名，TC 之訊號從何而來未驗。
  `<Name>.Info` 式 —— 分類為「其他」之 4 條。DBC 查無同名，
                    可能為 service 層介面而非 CAN 訊號（DR-36）。

**分類式不改**（R-VF77 三）：本檔只讀 `_vf230_forms.json` 之既有結論，
318／124 之分界維持。
"""
import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent

PROPID = re.compile(r"propId\s*=", re.I)
TVS = re.compile(r"TELEMATIC_\w+\.[A-Za-z]\w+", re.I)
INFO = re.compile(r"\b([A-Z][A-Za-z0-9_]*)\.Info\b")


def main() -> None:
    forms = {r["leaf_id"]: r["form"]
             for r in json.loads((FEAT / "data/_vf230_forms.json").read_text())["rows"]}
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}

    rows = []
    for leaf, form in forms.items():
        text = re.sub(r"\s+", " ", lv[leaf]["desc"].replace("\\n", " "))
        if form == "訊號送出型" and PROPID.search(text) and not TVS.search(text):
            rows.append({"leaf_id": leaf, "form": form, "class": "純 propId 式",
                         "reason": "條文無 TELEMATIC_* 訊號名，TC 之訊號來源未驗",
                         "dr": "", "unblock": "須完成一次書寫式查證（R-VF74）"})
        elif form == "其他":
            sigs = sorted({m.group(0) for m in INFO.finditer(text)})
            rows.append({"leaf_id": leaf, "form": form, "class": "<Name>.Info 式",
                         "reason": f"DBC 查無同名；條文之訊號 {', '.join(sigs) or '(未抽出)'}",
                         "dr": "DR-36", "unblock": "須先解 DR-36（是否為 CAN 訊號）"})

    out = FEAT / "data/vf230_isolated.tsv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    dist = Counter(r["class"] for r in rows)
    print(f"隔離表 {len(rows)} 條 → {out.relative_to(FEAT)}")
    for k, v in dist.items():
        print(f"  {v:3}  {k}")

    # ---- 量產母體之算式（逐項可稽，不寫死）----
    pool = {k for k, v in wr.items() if v["writable"] in ("W0", "W1")}
    pilots = set()
    for f in ("generated/vf230_pilot1.json", "generated/vf230_pilot2.json"):
        pilots |= {t["leaf_id"] for t in json.loads((FEAT / f).read_text())["tcs"]}
    iso = {r["leaf_id"] for r in rows}

    print(f"\n量產母體之算式：")
    print(f"  選池（writability W0+W1）      {len(pool)}")
    print(f"  扣 pilot #1／#2                −{len(pilots & pool)}")
    print(f"  扣隔離                          −{len(iso & pool)}")
    body = pool - pilots - iso
    print(f"  **量產母體                      {len(body)}**")
    if iso - pool:
        print(f"  ⚠ 隔離中不在選池者 {len(iso - pool)}：{sorted(iso - pool)}")
    if pilots - pool:
        print(f"  ⚠ pilot 中不在選池者 {len(pilots - pool)}：{sorted(pilots - pool)}")

    (FEAT / "data/_vf230_body.json").write_text(
        json.dumps({"body": sorted(body), "n": len(body),
                    "pool": len(pool), "pilots": len(pilots & pool),
                    "isolated": len(iso & pool)}, ensure_ascii=False, indent=1),
        encoding="utf-8")


if __name__ == "__main__":
    main()
