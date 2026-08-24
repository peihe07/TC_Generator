"""W-VF43 —— `R-VS59`–`R-VS66` 之 164 處現行引用逐處判線別（R-VF49 階段一）。

**只判不改。** 階段二（取代）待核可後另行，且須逐處取代不得全域
（鑑別錨點 `docs/handoff/64_review_round40.md` 已證誤傷風險為實）。

**判別依據為上下文，非編號**（V17 §5.2：該判斷不可由編號決定）。
本腳本以各號**兩義之主題詞**為據，逐處比對其鄰近文字；
兩義皆命中或皆不命中者標 `待人工`，**不臆測**。

依 R-VF21／R-VF28 附三錨點，以內容定錨。

輸出：docs/reports/wvf43_lineside.md ＋ data/_wvf43_lineside.json
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 各號之兩義（自 `RULINGS.md` 之條文標題逐字取，非本層自擬）
MEANING = {
    "R-VS59": (["B 欄", "238", "序號", "續號"], ["委派", "不等於不寫", "R-VS7(a)"]),
    "R-VS60": (["併入", "vehicle_setting", "feature slug", "另開"],
               ["跨列引入", "A-VS103", "Vented_seat"]),
    "R-VS61": (["素材補入", "Pei 執行", "搬檔", "INPUTS.sha256"],
               ["DR-19", "匯流排對應", "分析所載之名", "值未解"]),
    "R-VS62": (["output/", "參考素材", "非權威"],
               ["DR-8", "車型碼", "PROXI 表", "VC_VEH_LINE"]),
    "R-VS63": (["REF 素材", "代用", "DBC", "專案級"], ["編號分線", "命名空間"]),
    "R-VS64": (["W 號改編", "W-110", "W-115"], ["升級門檻", "常數"]),
    "R-VS65": (["token 掃描", "DR 波及", "掃描定義"], ["44 輪", "69 包"]),
    "R-VS66": (["正規化", "Layer 2", "複驗", "NFKC"],
               ["規格明確", "實作未見", "71 包"]),
}
WIN = 260          # 上下文取樣寬度（字元），前後各半


def side(num: str, ctx: str) -> tuple[str, str]:
    vf, p1 = MEANING[num]
    hv = [k for k in vf if k in ctx]
    hp = [k for k in p1 if k in ctx]
    if hv and not hp:
        return "VF230", "命中 VF230 義之主題詞：" + "／".join(hv)
    if hp and not hv:
        return "Part 1", "命中 Part 1 義之主題詞：" + "／".join(hp)
    if hv and hp:
        return "待人工", ("兩義皆命中 —— VF230：" + "／".join(hv)
                          + "；Part 1：" + "／".join(hp))
    return "待人工", "兩義皆未命中，須讀全段"


def main() -> None:
    scope = json.loads((ROOT / "data" / "_wvf39_scope.json").read_text(encoding="utf-8"))
    live = [r for r in scope["rows"] if r["cls"] == "現行"]
    cache: dict[str, str] = {}
    rows = []
    for r in live:
        f = r["file"]
        if f not in cache:
            cache[f] = (ROOT / f).read_text(encoding="utf-8") if (ROOT / f).is_file() else ""
        txt = cache[f]
        # 以**內容片段**定位其上下文（R-VF28：不以行號）
        i = txt.find(r["frag"][:40])
        ctx = txt[max(0, i - WIN // 2): i + WIN // 2] if i >= 0 else r["frag"]
        for num in r["nums"]:
            if num not in MEANING:
                continue
            sd, why = side(num, ctx)
            rows.append({"file": f, "num": num, "frag": r["frag"][:90],
                         "side": sd, "why": why})

    # --- 錨點（R-VF21／R-VF28）---
    a_vf = next((x for x in rows if x["num"] == "R-VS59" and "238" in x["frag"]), None)
    a_p1 = next((x for x in rows if x["num"] == "R-VS59" and "不寫" in x["frag"]), None)
    if a_vf and a_vf["side"] != "VF230":
        raise SystemExit(f"必命中錨點不符：含 `238` 之 R-VS59 判 {a_vf['side']}，停")
    if a_p1 and a_p1["side"] != "Part 1":
        raise SystemExit(f"必不命中錨點不符：含「不寫」之 R-VS59 判 {a_p1['side']}，停")
    # 鑑別錨點：`docs/handoff/64_review_round40.md`（Part 1 檔名而引用 VF230 線）
    # —— 其於本表之範圍外（該檔為歷史包），故本處以其存在為據具名
    disc = [x for x in scope["rows"]
            if x["file"].startswith("docs/handoff/") and re.match(r"\d{2}_", Path(x["file"]).name)
            and ("VF230" in x["frag"] or "vf230" in x["frag"])]

    dist = Counter(x["side"] for x in rows)
    per_file = Counter(x["file"] for x in rows)

    L = ["# W-VF43 —— `R-VS59`–`R-VS66` 現行引用之線別判定（R-VF49 階段一）", "",
         "**只判不改。** 階段二（取代）待核可，且須逐處取代不得全域。", "",
         "## 0. 錨點（R-VF21 ／ R-VF28：以內容定錨）", "",
         "| 錨點 | 處 | 期望 | 實測 |", "|---|---|---|---|",
         (f"| 必命中 | `R-VS59` 之引用含 `238` | VF230 | {a_vf['side']} ✅ |"
          if a_vf else "| 必命中 | 含 `238` 之 R-VS59 引用 | VF230 | **不存在** |"),
         (f"| 必不命中 | `R-VS59` 之引用含「不寫」 | Part 1 | {a_p1['side']} ✅ |"
          if a_p1 else "| 必不命中 | 含「不寫」之 R-VS59 引用 | Part 1 | **不存在** |"),
         (f"| **鑑別** | `docs/handoff/` 之 Part 1 檔而引用 VF230 線者 | "
          f"**須排除於取代範圍外** | {len(disc)} 處，皆為歷史包 ✅ |"), "",
         "> **鑑別錨點之意義**：Part 1 檔名之歷史包內引用 VF230 線條文者確實存在，",
         "> **全域取代必誤傷之**。其於本表範圍外（歷史不追改，R-VF45 二），",
         "> 惟階段二之逐處取代須以其為必不取代之標的。", "",
         "## 1. 判別依據", "",
         "**依上下文，非依編號**（V17 §5.2）。各號之兩義主題詞取自",
         "`RULINGS.md` 之條文標題逐字，非本層自擬：", "",
         "| 號 | VF230 義 | Part 1 義 |", "|---|---|---|"]
    for k, (a, b) in MEANING.items():
        L.append(f"| `{k}` | {'／'.join(a)} | {'／'.join(b)} |")
    L += ["", "取上下文 260 字元（前後各半），兩義皆命中或皆不命中者標 **待人工**，"
          "**不臆測**。", "",
          f"## 2. 結果：{len(rows)} 處", "",
          f"- **VF230 線 {dist['VF230']}**",
          f"- **Part 1 線 {dist['Part 1']}**",
          f"- **待人工 {dist['待人工']}**", "",
          "| 檔 | 處 |", "|---|---:|"]
    for f, n in per_file.most_common():
        L.append(f"| `{f}` | {n} |")

    for sd in ("VF230", "Part 1", "待人工"):
        sub = [x for x in rows if x["side"] == sd]
        if not sub:
            continue
        L += ["", f"### 2.{'123'[('VF230', 'Part 1', '待人工').index(sd)]} "
              f"{sd}（{len(sub)}）", "",
              "| 檔 | 號 | 內容片段 | 依據 |", "|---|---|---|---|"]
        for x in sub[:60]:
            L.append(f"| `{x['file']}` | `{x['num']}` | `{x['frag'][:60]}` | {x['why']} |")
        if len(sub) > 60:
            L.append(f"| …（其餘 {len(sub)-60} 處見 JSON）| | | |")

    L += ["", "## 3. 階段二之前提（未執行）", "",
          "1. **逐處取代，不得全域** —— 鑑別錨點已證誤傷風險為實。",
          "2. **僅取代判為 VF230 線者**，且僅於現行有效之陳述"
          "（R-VF45 一）；歷史包不動（R-VF45 二）。",
          "3. **待人工之項須先判**，其不得以任一方向預設。",
          "4. `RULINGS.md` 之永久對照表（R-VF45 三）須同時置入。", ""]

    p = ROOT / "docs" / "reports" / "wvf43_lineside.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf43_lineside.json").write_text(
        json.dumps({"rows": rows, "dist": dict(dist),
                    "disc_historical": len(disc)},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(rows)} 處；{dict(dist)}")
    print(f"鑑別錨點（Part 1 歷史包引用 VF230 線）：{len(disc)} 處")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
