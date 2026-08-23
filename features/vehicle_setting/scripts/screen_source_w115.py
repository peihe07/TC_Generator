"""W-115(2)（64 包 §5）—— `screen_source.tsv` 之判準改逐 leaf 行為層。

W-112 之舊判準以 **Layer 3 群**比對（該功能群於 Comfort 有無條文），
其對 `Fail_Present` 類回報「查得」而 Comfort 之 seat 條文含 fail 者實為 0
—— 即該判準無偵測力（A-VS139）。

新判準：**該 leaf 之行為 ↔ Comfort 條文之行為**，兩者須同時命中
  (a) **對象**（heated seat／vented seat／heated steering wheel …）
  (b) **行為**（失效彈窗／圖示變更／階數顯示／灰階／標籤左右 …）

**錨點（R-VS54）**：`Fail_Present` 類之 16 leaf 須**全數判「查無」**
—— 舊判準對其回報「查得」，即失準之直接證據。
"""
from __future__ import annotations

import collections
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec        # noqa: E402
from screen_source_w112 import comfort_rows    # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

# (a) 對象
OBJECT = {
    "heated seat": [r"heated\s+seat", r"seat\s+heat"],
    "vented seat": [r"vented\s+seat", r"ventilated\s+seat", r"seat\s+vent"],
    "heated steering wheel": [r"heated\s+steering", r"steering\s+wheel\s+heat"],
    "head restraint": [r"head\s*rest", r"head\s+restraint"],
    "rear camera": [r"rear\s+(view\s+)?camera"],
    "display": [r"screen\s+off", r"display\s+off", r"touchscreen"],
}
# (b) 行為 —— 鍵為判準名，值為 (leaf 側樣式, Comfort 側樣式)
BEHAVIOUR = {
    "failure-popup": (r"popup relative to the failure|informative popup",
                      r"(fail|error|malfunction)[^.]{0,60}(popup|pop-up)"),
    "failure-icon": (r"Fail_Present.{0,80}icon|icon.{0,80}Fail_Present",
                     r"(fail|error|malfunction)[^.]{0,60}icon"),
    "level-display": (r"shall (change|update|set) the (stored )?(display|status)|displayed as|icon status|relative icon|shall .{0,40}(display|show)",
                      r"(display|icon|indicator)[^.]{0,60}(level|state|status)"),
    "greyed-out": (r"greyed out|not selectable|selectable only",
                   r"(grey|gray|disable|not selectable)"),
    "side-label": (r"Driver_Side|driver and passenger|mirrored",
                   r"(driver|passenger)[^.]{0,40}(side|label|swap|mirror)"),
    "presence": (r"equipped|is present|configured|PROXI",
                 r"(equipped|present|configur)"),
}


def leaf_clause(blocks: dict, l2r: dict, leaf: str) -> str:
    qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
    return " ".join(re.sub(r"\s+", " ", "\n".join(blocks[q]["text"].split("\n")[1:]))
                    for q in qs if q in blocks)


def tags(text: str, side: int) -> set[str]:
    return {k for k, pats in BEHAVIOUR.items() if re.search(pats[side], text, re.I)}


def objs(text: str) -> set[str]:
    return {k for k, pats in OBJECT.items() if any(re.search(p, text, re.I) for p in pats)}


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    lookup = list(csv.DictReader(
        (FEAT / "docs/reports/delegation_lookup.tsv").open(encoding="utf-8"), delimiter="\t"))
    func = [r for r in comfort_rows() if r["cat"].casefold().startswith("functional")]
    for c in func:
        blob = c["title"] + " " + c["desc"]
        c["objs"], c["tags"] = objs(blob), tags(blob, 1)

    out, found, missing = [], 0, 0
    for r in lookup:
        # R-VS59 已廢除 `blocked` 之值；`delegation_lookup.tsv` 尚未同步，
        # 故三值皆為委派標的（`no` 者非委派）。
        if r["delegate"] == "no":
            continue
        leaf = r["leaf_id"]
        text = leaf_clause(blocks, l2r, leaf)
        lo, lt = objs(text), tags(text, 0)
        hits = [c for c in func if (lo & c["objs"]) and (lt & c["tags"])]
        if not lt:
            # 行為抽不出者**不計為查無** —— 其為抽取式之涵蓋不足，非 Comfort 之缺
            out.append({"leaf_id": leaf, "layer3": r["layer3"], "delegate": r["delegate"],
                        "leaf_objects": ";".join(sorted(lo)), "leaf_behaviours": "",
                        "status": "unextracted", "comfort_leaf_ids": "",
                        "screen_text": "", "source": "", "comfort_hit_count": 0})
            continue
        if hits:
            found += 1
            status = "found"
            quote = " ⏐ ".join(f"{h['id']}：{h['desc'][:140]}" for h in hits[:2])
            src = ";".join(f"Comfort 037／Analysis Report:{h['row']}" for h in hits[:2])
            ids = ";".join(sorted({h["id"] for h in hits})[:8])
        else:
            missing += 1
            status, quote, src, ids = "PENDING", "PENDING", "", ""
        out.append({"leaf_id": leaf, "layer3": r["layer3"], "delegate": r["delegate"],
                    "leaf_objects": ";".join(sorted(lo)),
                    "leaf_behaviours": ";".join(sorted(lt)),
                    "status": status, "comfort_leaf_ids": ids,
                    "screen_text": quote, "source": src,
                    "comfort_hit_count": len(hits)})

    p = FEAT / "docs/reports/screen_source.tsv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    print(f"標的（`delegate ∈ {{yes, pending}}`）：{len(out)}")
    unext = sum(1 for r in out if r["status"] == "unextracted")
    print(f"**查得 {found}／查無 {missing}／行為未抽出 {unext}**"
          f"（舊判準：查得 174／查無 0）")
    print(f"相異 `comfort_leaf_ids` 組合：{len({r['comfort_leaf_ids'] for r in out})}"
          f"（舊判準：3）")

    fp = [r["leaf_id"] for r in out
          if "Fail_Present" in leaf_clause(blocks, l2r, r["leaf_id"])]
    bad = [l for l in fp if next(r for r in out if r["leaf_id"] == l)["status"] != "PENDING"]
    print(f"\n錨點（必命中）`Fail_Present` 類 {len(fp)} leaf 須全數判「查無」 —— "
          f"不符 {len(bad)}   {'PASS，可失敗' if not bad and fp else '⚠'}")
    for l in bad[:6]:
        print("   ", l)
    by = collections.Counter((r["status"]) for r in out)
    print("\n狀態分布：", dict(by))
    tb = collections.Counter(r["leaf_behaviours"] or "（無行為標記）" for r in out)
    print("leaf 行為標記分布（前 8）：")
    for k, v in tb.most_common(8):
        print(f"    {k:44s} {v}")


if __name__ == "__main__":
    main()
