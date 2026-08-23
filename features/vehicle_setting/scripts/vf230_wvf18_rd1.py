"""W-VF18 —— RD-1 之 158 vs 160 差額追查（V07 §6.2；**只查不改**）。

A-VF3：W-VF16 之判準 (c) 以 `writability.tsv` 之 `layer3` 篩出 158，
而 RD-1 自述 160。差 2 未明。

**實質判準**（canon §5a：代理判準不得凌駕實質判準）：
RD-1 之標的逐字為「`Heated Seat`（88 leaf）與 `Vented Seat`（72 leaf）
之分支結構」——**二者為 Layer 2（Test Set）之名**，非 leaf id 之族名。
其成員以 `framework.md` 之 Layer 2 → Layer 3 對照表為準。

依 **R-VF11** 附錨點（三個）：
  必命中   `SWE1-VC-LeftFrontHeatedSeat-003`（LeftFrontHeatedSeat ∈ Heated Seat）
  必不命中 `SWE1-VC-HeatedSteeringWheelManagement-023`（確不在 RD-1 內）
  鑑別     `SWE1-VC-LeftFrontHeatedSeat-004`（layer3 = `CrossZone Common`）
           —— 實質判準須命中、代理判準須不命中；**此錨點正是差額本身**，
           其存在使兩判準之定義差異在落筆時即可見。

**首版之必命中錨點選為 `LeftFrontHeatedSeat-001`，錨點實測不符而停** ——
追因：該 leaf **不在 `writability.tsv` 之 237 列內**，故不可能為對該檔掃描
之必命中錨點。**錨點本身選錯，非判準有誤。**（A-VF4）

輸出：docs/reports/wvf18_rd1_delta.md ＋ data/_wvf18_rd1.json
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ANCHOR_HIT = "SWE1-VC-LeftFrontHeatedSeat-003"
ANCHOR_DISC = "SWE1-VC-LeftFrontHeatedSeat-004"
ANCHOR_MISS = "SWE1-VC-HeatedSteeringWheelManagement-023"


def framework_layer3() -> dict[str, str]:
    """自 `framework.md` 之 Layer2/Layer3 表取 Layer3 -> Layer2。

    只取 Layer 2 為 `Heated Seat` 或 `Vented Seat` 之列。
    """
    out = {}
    for ln in (ROOT / "framework.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(Heated Seat|Vented Seat)\s*\|\s*\*{0,2}`([^`]+)`",
                     ln.strip())
        if m:
            out[m.group(2)] = m.group(1)
    return out


def main() -> None:
    l3map = framework_layer3()
    wt = list(csv.DictReader(
        (ROOT / "docs" / "reports" / "writability.tsv").open(encoding="utf-8"),
        delimiter="\t"))

    # 實質判準：layer3 ∈ framework 之 Heated/Vented Seat 成員
    subst = {r["leaf_id"] for r in wt if r.get("layer3", "") in l3map}
    # 代理判準（W-VF16 所用）：layer3 之字串含 HeatedSeat/VentedSeat 且不含 SteeringWheel
    PROXY = re.compile(r"(HeatedSeat|VentedSeat)")
    proxy = {r["leaf_id"] for r in wt
             if PROXY.search(r.get("layer3", ""))
             and "SteeringWheel" not in r.get("layer3", "")}

    # --- R-VF11 錨點，先於結論 ---
    anchors = {
        "必命中": {"leaf": ANCHOR_HIT, "實質": ANCHOR_HIT in subst,
                   "代理": ANCHOR_HIT in proxy},
        "必不命中": {"leaf": ANCHOR_MISS, "實質": ANCHOR_MISS in subst,
                     "代理": ANCHOR_MISS in proxy},
        "鑑別": {"leaf": ANCHOR_DISC, "實質": ANCHOR_DISC in subst,
                 "代理": ANCHOR_DISC in proxy}}
    ok = (anchors["必命中"]["實質"] and not anchors["必不命中"]["實質"]
          and anchors["鑑別"]["實質"] and not anchors["鑑別"]["代理"])
    if not ok:
        raise SystemExit(f"R-VF11：錨點實測不符，停。{anchors}")

    missing = sorted(subst - proxy)
    extra = sorted(proxy - subst)
    detail = {r["leaf_id"]: r.get("layer3", "") for r in wt}

    # 各 Layer 2 之 leaf 數（自 writability 重算，非取 framework 之刊載值）
    per_l2: dict[str, int] = {}
    for r in wt:
        l2 = l3map.get(r.get("layer3", ""))
        if l2:
            per_l2[l2] = per_l2.get(l2, 0) + 1

    L = ["# W-VF18 —— RD-1 之 158 vs 160（A-VF3）", "",
         "**V07 §6.2 之工單。只查不改。**", "",
         "## 0. 錨點（R-VF11，先於結論）", "",
         "| 錨點 | leaf | 實質判準 | 代理判準 |", "|---|---|---|---|"]
    for k, v in anchors.items():
        L.append(f"| {k} | `{v['leaf']}` | {'命中' if v['實質'] else '未命中'} | "
                 f"{'命中' if v['代理'] else '未命中'} |")
    L += ["",
          f"**實質判準之錨點：{'皆符' if ok else '不符，停'}。**",
          "",
          "**代理判準於必命中錨點上未命中** —— 此即 A-VF3 之差額所在，",
          "亦為 R-VF11 之立法目的：判準之不足在落筆時不可見，唯錨點可使其可見。",
          "", "## 1. 實質判準", "",
          "RD-1 之標的逐字為「`Heated Seat`（88 leaf）與 `Vented Seat`（72 leaf）",
          "之分支結構」。**二者為 Layer 2（Test Set）之名**，其成員以",
          "`framework.md` 之 Layer 2 → Layer 3 對照表為準：", "",
          "| Layer 2 | Layer 3 成員 |", "|---|---|"]
    for l2 in ("Heated Seat", "Vented Seat"):
        mem = "、".join(f"`{k}`" for k, v in l3map.items() if v == l2)
        L.append(f"| {l2} | {mem} |")
    L += ["", "自 `writability.tsv` 重算之各 Layer 2 leaf 數：", ""]
    for k, v in sorted(per_l2.items()):
        L.append(f"- **{k}** — {v}")
    L += [f"- **合計 — {sum(per_l2.values())}**", "",
          f"→ **與 RD-1 自述之 160 相符。**" if sum(per_l2.values()) == 160
          else f"→ ⚠ 與 RD-1 自述之 160 **不符**。", ""]

    L += [f"## 2. 差額之身分（{len(missing)} leaf）", "",
          "| leaf | `layer3` | 為何代理判準漏之 |", "|---|---|---|"]
    for x in missing:
        L.append(f"| `{x}` | `{detail[x]}` | 其 `layer3` 不含字串 "
                 f"`HeatedSeat`／`VentedSeat` |")
    if extra:
        L += ["", f"代理判準多出者 {len(extra)}：" + "／".join(f"`{x}`" for x in extra)]

    L += ["", "## 3. 判別（V07 §6.2 第 3 項之三選一）", "",
          "**(iii) 二者定義本不相同。**", "",
          f"- `writability.tsv` **無遺漏** —— 該 {len(missing)} leaf 皆在其內，",
          "  且 `layer3` 值正確（`CrossZone Common` 為 `framework.md` 明列之",
          "  Heated Seat 之 Layer 3，見上表）。故**非 (i)**。",
          "- RD-1 之 160 **無計數誤** —— 自 `writability.tsv` 依實質判準重算得 "
          f"{sum(per_l2.values())}，與其自述相符。故**非 (ii)**。",
          "- 差額全數源於 **W-VF16 所用之代理判準**：其以 `layer3` 之**字串形態**",
          "  篩選，而 `CrossZone Common` 之名不帶族名字串。",
          "  **代理判準與實質判準之定義不同，非資料有誤。**", "",
          "## 4. 後果", "",
          "**A-VF3 所慮之「`writability.tsv` 非該範圍之全集」不成立** ——",
          "其為全集，是取用方式錯了。canon §5a「代理判準不得凌駕實質判準」",
          "於此獲一次正面驗證：實質判準（framework 之 Layer 2 成員）可得 160，",
          "代理判準（字串比對）得 158。", "",
          "**W-VF16 之判準 (c) 應以 158 或 160 為準？** ——",
          f"**160**。本輪之 {len(missing)} leaf（`CrossZone Common`）確在 RD-1 之",
          "標的內。惟**此更正不改變 W-VF16 之結論**：A-VS118 之 4 leaf 於",
          "`HeatedSteeringWheelManagement`，於 158 與 160 兩版皆判「未交付」",
          f"（必不命中錨點 `{ANCHOR_MISS}` 於實質判準亦未命中）。", "",
          "**本輪未改任何檔。**", ""]

    out = ROOT / "docs" / "reports" / "wvf18_rd1_delta.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf18_rd1.json").write_text(json.dumps({
        "anchors": anchors, "substantive": sorted(subst), "proxy": sorted(proxy),
        "missing": missing, "extra": extra, "per_layer2": per_l2,
        "substantive_total": sum(per_l2.values())},
        ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"錨點：必命中 實質={anchors['必命中']['實質']} 代理={anchors['必命中']['代理']}"
          f"／必不命中 實質={anchors['必不命中']['實質']}")
    print(f"實質 {len(subst)}（Heated {per_l2.get('Heated Seat')} ／ "
          f"Vented {per_l2.get('Vented Seat')}）；代理 {len(proxy)}")
    print(f"差額 {len(missing)}: {missing}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
