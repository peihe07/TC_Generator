"""W-VF46 —— VF230 之委派判定（V17 §5；**不生成 TC**）。

**沿用 Part 1 之委派判準，不新設**（V17 §5 第 1 項）：
  判準為「**同一實體功能於 Comfort 037 全集是否有對應**」，
  於 **Layer 3（簇）層級**判定（Part 1 之 `delegation_lookup.tsv` 之 `basis`
  逐字為「同一實體功能：…｜Layer 3 層級，未逐 leaf 收斂」／
  「Comfort 037 全集無同一實體功能之對應」）。

**委派之效果依 Part 1 之 R-VS59（Pei 2026-08-23）** ——
**委派不免除產出 TC 之義務**；其作用為「該 leaf 之畫面層內容取自 Comfort 素材」，
非「故不寫」。R-VS7(a) 之原效果已撤回。

依 R-VF21／R-VF28 附三錨點；**鑑別錨點為「簇名含 Comfort 而實不應委派」者**。

輸出：docs/reports/vf230_delegation.tsv ＋ data/_vf230_delegation.json
"""
import csv
import glob
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
COMFORT = Path("/Users/peihe/Work_Projects/TC_Generator/features/comfort/inputs")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def comfort_titles() -> set[str]:
    """Comfort 037 之 Requirement Title 全集（正規化）。"""
    g = sorted(COMFORT.glob("*037*.xlsx"))
    if not g:
        raise SystemExit("找不到 Comfort 之 037")
    wb = openpyxl.load_workbook(g[0], read_only=True, data_only=True)
    out = set()
    for nm in wb.sheetnames:
        rs = list(wb[nm].iter_rows(values_only=True))
        i = next((j for j, r in enumerate(rs)
                  if any("requirement description" in norm(str(v or "")).replace(" ", " ")
                         for v in r)), None)
        if i is None:
            continue
        ti = next((j for j, v in enumerate(rs[i]) if "title" in str(v or "").lower()), None)
        if ti is None:
            continue
        for r in rs[i + 1:]:
            if r[0] and r[ti]:
                out.add(norm(str(r[ti])))
        break
    wb.close()
    return out


# Comfort 所擁有之實體功能域（自其 037 之簇名歸納，逐字列出供覆核）
COMFORT_DOMAIN = ("hvac", "climate", "atc", "mtc", "defrost", "fan speed",
                  "sync", "recirculation", "air distribution", "temperature control",
                  "heated seat", "vented seat", "heated steering")


def main() -> None:
    ct = comfort_titles()
    lv = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    enum = json.loads((ROOT / "data" / "_wvf35_enum.json").read_text(encoding="utf-8"))
    ts_of = {c: t for t, cs in enum["final"].items() for c in cs}

    by_cluster: dict[str, list] = defaultdict(list)
    for r in lv:
        by_cluster[r["title"]].append(r)

    rows = []
    for title, leaves in sorted(by_cluster.items()):
        n = norm(title)
        exact = n in ct
        # **詞界比對，非子字串**（R-VF52：誤報以判準精確化消除，不以白名單）。
        # 首版以 `d in n` 比對，致 `sync` 誤配 `Enhanced Display
        # Synchronization`（6 leaf）—— 逐條比對後確認二者為不同功能：
        # VF230 為 SRT PROXI 配置之顯示同步，Comfort 為空調雙區溫度同步。
        domain = [d for d in COMFORT_DOMAIN
                  if re.search(rf"\b{re.escape(d)}\b", n)]
        if exact:
            dele, basis = "yes", f"同一實體功能：Comfort 037 有同名簇 `{title}`"
        elif domain:
            dele, basis = "pending", ("簇名落於 Comfort 之實體功能域（"
                                      + "／".join(domain) + "）而 Comfort 037 無同名簇"
                                      " —— 須逐條比對條文，本輪標 pending")
        else:
            dele, basis = "no", "Comfort 037 全集無同一實體功能之對應"
        for lf in leaves:
            rows.append({"leaf_id": lf["swe_id"],
                         "test_set": ts_of.get(title, ""),
                         "layer3": title.replace("\\n", " "),
                         "delegate": dele, "target_feature": "comfort" if dele != "no" else "",
                         "basis": basis,
                         "screen_source": "comfort" if dele == "yes" else ""})

    # --- 錨點（R-VF21／R-VF28）---
    def dele_of(t):
        return next((r["delegate"] for r in rows if r["layer3"] == t), None)

    # 必不命中：`Speed Unit` 為單位顯示，Comfort 無此功能
    if dele_of("Speed Unit") != "no":
        raise SystemExit("必不命中錨點不符：`Speed Unit` 應判 no，停")
    # 鑑別：簇名含 `Comfort` 而實為車輛設定，不應委派
    disc = [t for t in by_cluster if "comfort" in norm(t)]
    bad = [t for t in disc if dele_of(t) != "no"]
    if bad:
        raise SystemExit(f"鑑別錨點不符：簇名含 Comfort 而被判委派 —— {bad}，停")
    print(f"鑑別錨點：簇名含 `Comfort` 者 {len(disc)} 個"
          f"（{'／'.join(disc)}），皆判 no ✅")
    # 必命中：Comfort 037 有同名簇者（若不存在則具名）
    hit = [t for t in by_cluster if norm(t) in ct]
    if hit:
        print(f"必命中錨點：Comfort 037 有同名簇者 {len(hit)} 個 —— {hit[:3]}")
    else:
        print("必命中錨點：**不存在** —— VF230 之 106 簇無一與 Comfort 037 同名")
    if len(rows) != 627:
        raise SystemExit(f"R-VF16：應為 627 列，實得 {len(rows)}")

    p = ROOT / "docs" / "reports" / "vf230_delegation.tsv"
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    dist = Counter(r["delegate"] for r in rows)
    per = defaultdict(Counter)
    for r in rows:
        per[r["test_set"]][r["delegate"]] += 1
    (ROOT / "data" / "_vf230_delegation.json").write_text(json.dumps({
        "dist": dict(dist), "per_test_set": {k: dict(v) for k, v in per.items()},
        "comfort_titles": len(ct), "vf230_clusters": len(by_cluster),
        "exact_hits": hit, "name_contains_comfort": disc},
        ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nComfort 037 之相異簇 {len(ct)}；VF230 之簇 {len(by_cluster)}")
    print(f"委派分布（627 leaf）：{dict(dist)}")
    for t, c in sorted(per.items(), key=lambda x: -sum(x[1].values())):
        print(f"  {sum(c.values()):4}  {t:24} {dict(c)}")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
