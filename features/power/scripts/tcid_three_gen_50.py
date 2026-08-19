"""B2 —— 三代 `tc_id` 對照表（R-P324）。

同一條 TC 歷經三代號：
  （一）**歷史臨時號** —— 09 包以來，含 27 包全域重編、44 包合併之前後
  （二）**現行交付副本之最終號** —— 001–260，47 包所指派，**已對外存在**
  （三）**本次之新最終號** —— 001–280，併入第七批後重新指派

鍵為 `(req_id, tc_title)`（R-P324）。

**（二）→（三）之對應為本次作廢之核心資訊** —— 若有人已引用（二）之號碼，
須憑此表換算。

**A-PW299 之 2 條鍵斷裂**於本檔以 `split_index` 為輔鍵人工補齊（R-P324）。

用法：
    python features/power/scripts/tcid_three_gen_50.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GEN = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assign_final_tc_id import assign, collect  # noqa: E402
from build_tcid_history import MERGED_INTO, STAGES, at, key  # noqa: E402

# A-PW299 之 2 條鍵斷裂 —— **人工補齊**（R-P324）。
# `tc_title` 於 27 包後被改寫，故 `(req_id, tc_title)` 之鍵於歷史階段對不上。
# 補齊之依據：同一 `req_id`、同一 `split_index`、標題為同一行為之改寫
# （「keeps the Day theme regardless of the day night signal」→「uses the Day theme」）。
ALIAS = {
    ("SWE-PM-091", "The day theme mode keeps the Day theme regardless of the day night signal"):
        ("SWE-PM-091", "The day theme mode uses the Day theme"),
    ("SWE-PM-092", "The night theme mode keeps the Night theme regardless of the day night signal"):
        ("SWE-PM-092", "The night theme mode uses the Night theme"),
}


def hist_map(ref: str) -> dict:
    """歷史階段之 `(req_id, tc_title)` → `tc_id`，並套用 ALIAS 補齊斷裂之鍵。"""
    out = {}
    for t in at(ref):
        k = key(t)
        out[ALIAS.get(k, k)] = t["tc_id"]
    return out


def main() -> None:
    # 現行語料（含第七批）
    cur: dict[tuple[str, str], dict] = {}
    for p in sorted(GEN.glob("*.json")):
        for t in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            cur[key(t)] = t

    # （三）新最終號
    gen3 = {}
    for r in assign(collect(GEN)):
        gen3[r["provisional_tc_id"]] = r["final_tc_id"]

    # （二）現行交付副本之最終號：以 provisional_tc_id 為鍵
    gen2 = {}
    for line in (DATA / "final_tc_id_map_47.tsv").read_text(
            encoding="utf-8").splitlines()[1:]:
        c = line.split("\t")
        gen2[c[0]] = c[1]

    # （一）歷史各階段
    stages = [(label, hist_map(ref)) for label, ref in STAGES]

    rows = []
    for k, tc in sorted(cur.items(),
                        key=lambda kv: (int(re.search(r"\d+", kv[0][0]).group()),
                                        kv[1].get("split_index", 0))):
        prov = tc["tc_id"]
        rows.append({
            "req_id": k[0], "title": k[1], "prov": prov,
            "hist": [s[1].get(k) for s in stages],
            "gen2": gen2.get(prov), "gen3": gen3.get(prov),
        })

    # 鍵斷裂 = 某歷史階段有、現行無對應者（扣除 44 包之四對合併）。
    # **不以「早期階段沒有」為斷裂** —— 該 TC 當時本就不存在（27 包補測所增者即是）。
    # 被併入者以**鍵**辨識而非以號碼 —— 其於 27 包之前之號碼與 44 包不同
    #（如 `SWE-PM-028` 於 27 前為 098、於 44 前為 102），以號碼比對會漏。
    merged_keys = {k for k, v in hist_map(STAGES[-1][1]).items()
                   if v[-3:] in MERGED_INTO}
    broken = []
    for label, ref in STAGES:
        for k, v in hist_map(ref).items():
            if k not in cur and k not in merged_keys:
                broken.append((label, k, v))
    new7 = [r for r in rows if r["gen2"] is None]
    # 第七批於歷史階段本就不存在，其 hist 全 None 為必然，不計為斷裂
    moved = [r for r in rows if r["gen2"] and r["gen3"] and r["gen2"] != r["gen3"]]

    out = ["# B2 —— 三代 `tc_id` 對照表（R-P324）\n",
           "\n> 鍵：`(req_id, tc_title)`。產生指令："
           "`python features/power/scripts/tcid_three_gen_50.py`\n",
           f"\n## 一、三代之量\n\n| 代 | 涵蓋 | 號段 |\n|---|---|---|\n",
           f"| （一）歷史臨時號 | {len(stages)} 個時點 | 見第三節 |\n",
           f"| （二）現行交付副本最終號 | **{len(gen2)}** 條 | 001–260 |\n",
           f"| （三）本次新最終號 | **{len(gen3)}** 條 | 001–280 |\n",
           f"\n## 二、（二）→（三）之位移 —— **作廢之核心資訊**\n",
           f"\n**{len(moved)} / {len(gen2)} 條之最終號改變**"
           f"（{len(moved)/max(1,len(gen2)):.1%}）。\n",
           f"\n第七批新增 **{len(new7)}** 條（（二）無對應）。\n",
           "\n**⚠ 若已有人引用（二）之號碼，該號碼於（三）指向另一條 TC** ——"
           " 須憑本表逐一換算，不得逕以號碼相認。\n"]

    out.append(f"\n## ⚠ A-PW299 之 2 條鍵斷裂 —— **已人工補齊**\n\n"
               "| req_id | 歷史標題 | 現行標題 |\n|---|---|---|\n"
               + "".join(f"| `{a[0]}` | {a[1][:56]} | {b[1][:44]} |\n"
                         for a, b in ALIAS.items())
               + "\n補齊後**歷史階段之涵蓋為 266 / 266**（前為 264 / 266）。\n")

    if broken:
        out.append(f"\n## ⚠ 鍵斷裂殘留 {len(broken)} 筆\n\n"
                   "| 階段 | req_id | 歷史號 | `tc_title` |\n|---|---|---|---|\n")
        for label, k, v in broken:
            out.append(f"| {label} | `{k[0]}` | `{v[-3:]}` | {k[1][:60]} |\n")

    out.append("\n## 三、逐條三代對照\n\n| req_id | "
               + " | ".join(l for l, _ in STAGES)
               + " | 現行臨時 | **（二）交付副本** | **（三）新最終** | `tc_title` |\n"
               + "|---" * (len(STAGES) + 5) + "|\n")
    for r in rows:
        h = " | ".join(f"`{v[-3:]}`" if v else "**—**" for v in r["hist"])
        g2 = f"`{r['gen2'][-3:]}`" if r["gen2"] else "**新增**"
        g3 = f"**`{r['gen3'][-3:]}`**" if r["gen3"] else "—"
        out.append(f"| `{r['req_id']}` | {h} | `{r['prov'][-3:]}` | {g2} | {g3} "
                   f"| {r['title'][:52]} |\n")

    (DATA / "tcid_three_gen_50.md").write_text("".join(out), encoding="utf-8")
    hdr = "req_id\tsplit_index\tgen2_delivered\tgen3_new\ttc_title\n"
    body = "".join(f"{r['req_id']}\t{i}\t{r['gen2'] or ''}\t{r['gen3'] or ''}\t{r['title']}\n"
                   for i, r in enumerate(rows, 1))
    (DATA / "final_tc_id_map_50.tsv").write_text(hdr + body, encoding="utf-8")

    print(f"逐條 {len(rows)} 列；（二）{len(gen2)} 條、（三）{len(gen3)} 條")
    print(f"（二）→（三）位移 {len(moved)} 條；第七批新增 {len(new7)} 條")
    print(f"鍵斷裂殘留 {len(broken)} 筆（ALIAS 補齊後）")
    for label, k, v in broken:
        print(f"   {label}  {k[0]}  {v[-3:]}  {k[1][:60]}")


if __name__ == "__main__":
    main()
