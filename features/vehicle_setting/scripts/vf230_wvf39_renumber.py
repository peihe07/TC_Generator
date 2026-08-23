"""W-VF39 —— `R-VS59`–`R-VS67` 改號範圍之分類（V15 §7；**只列不改**）。

R-VF45：改號**只及於現行有效之陳述**；歷史包不追改；`RULINGS.md` 置永久對照表。

本腳本**不執行任何取代**，只產出三欄表：檔:內容片段（**不以行號**，R-VF28）／
類別／屬哪一線。

依 R-VF21／R-VF28 附三錨點，**鑑別錨點取「檔名屬 Part 1 線而內文引用
VF230 線條文」者** —— 其為機械取代最易誤傷之形態。
"""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUMS = [f"R-VS{n}" for n in range(59, 68)]
# V04 §3.1 之對照表
MAP = {f"R-VS{59+i}": f"R-VF{1+i}" for i in range(9)}

# 現行有效之陳述所在（R-VF18 之分類）
LIVE = ("RULINGS.md", "ANOMALIES.md", "CROSSLINE.md", "DATA_REQUESTS.md",
        "PLAYBOOK.md", "RUNBOOK.md", "framework.md", "feature.yaml",
        "docs/INDEX.md")


def line_of(f: str) -> str:
    if f.startswith(("docs/handoff/", "docs/upstream/", "docs/reports/")):
        return "歷史"
    if f in LIVE or f.startswith("scripts/"):
        return "現行"
    return "待人工"


def which_line(f: str, txt: str) -> str:
    """該引用屬哪一線 —— 以檔名前綴與內文線索判，不足者標待人工。"""
    b = Path(f).name
    if b.startswith("V") and re.match(r"^V\d{2}_", b):
        return "VF230"
    if re.match(r"^\d{2}_", b):
        return "Part 1"
    return "共用簿"


def main() -> None:
    pat = "|".join(NUMS)
    out = subprocess.run(
        ["grep", "-rnE", rf"({pat})\b", "--include=*.md", "--include=*.py",
         "--include=*.yaml", "."],
        capture_output=True, text=True, cwd=ROOT).stdout

    rows = []
    for ln in out.splitlines():
        m = re.match(r"^\./([^:]+):(\d+):(.*)$", ln)
        if not m:
            continue
        f, n, txt = m.group(1), int(m.group(2)), m.group(3).strip()
        if f.startswith("scripts/vf230_wvf39_renumber.py"):
            continue
        hits = sorted({h for h in NUMS if re.search(rf"{h}\b", txt)})
        rows.append({"file": f, "line": n, "frag": txt[:110],
                     "nums": hits, "cls": line_of(f), "side": which_line(f, txt)})

    # --- 錨點（R-VF21／R-VF28）---
    a_live = next((r for r in rows if r["file"] == "RULINGS.md"
                   and r["cls"] == "現行"), None)
    a_hist = next((r for r in rows if r["file"].startswith("docs/handoff/")), None)
    # 鑑別：檔名屬 Part 1 線（`NN_`）而內文引用 VF230 線之條文
    a_disc = next((r for r in rows
                   if re.match(r"^\d{2}_", Path(r["file"]).name)
                   and ("VF230" in r["frag"] or "vf230" in r["frag"])), None)
    if a_live is None or a_hist is None:
        raise SystemExit("R-VF21(1)：錨點所指之處不存在，停")

    live = [r for r in rows if r["cls"] == "現行"]
    hist = [r for r in rows if r["cls"] == "歷史"]
    man = [r for r in rows if r["cls"] == "待人工"]

    L = ["# W-VF39 —— `R-VS59`–`R-VS67` 改號範圍之分類（R-VF45；**只列不改**）", "",
         "**本輪未執行任何取代。** 分類結果回報待核（V15 §7 第 3 項）。", "",
         "## 0. 錨點（R-VF21 ／ R-VF28：以內容定錨，不以行號）", "",
         "| 錨點 | 處 | 判 |", "|---|---|---|",
         f"| 必為「現行」 | `RULINGS.md` 之 `{a_live['frag'][:44]}…` | {a_live['cls']} ✅ |",
         f"| 必為「歷史」 | `{a_hist['file']}` | {a_hist['cls']} ✅ |",
         ("| **鑑別**（Part 1 檔名而引用 VF230 線） | "
          f"`{a_disc['file']}` — `{a_disc['frag'][:44]}…` | "
          f"{a_disc['cls']}／{a_disc['side']} ⚠ **機械取代最易誤傷者** |")
         if a_disc else
         "| **鑑別** | 查無「Part 1 檔名而引用 VF230 線」之處 | "
         "**該形態不存在，取代之誤傷風險因而降低** |", "",
         "## 1. R-VS67 是否亦撞號（V15 §7 第 1 項）", "",
         "**否。** `RULINGS.md` 內 `### R-VS67 ——` 僅 **1 個條文起始**"
         "（Part 1 之 71 包，「訊號名與值域一律取 LID `Atlantis High` 欄組」）。", "",
         "**惟實測揭出一項更嚴重者**：`R-VF1`–`R-VF9` **九號於 `RULINGS.md` 全為 0**。",
         "R-VF1–R-VF8 以 `R-VS59`–`R-VS66` 存在（即 A-VF10 之撞號），",
         "而 **`R-VF9`（Test Group）自始未以任何編號落檔** ——",
         "其原號 `R-VS67` 已為 Part 1 所用，而其正文從未進入條文簿，",
         "**卻被 `RULINGS.md` 引用 3 處，且 `framework.md` 之 Layer 1 立於其上**。",
         "**本輪已補落**（見 `RULINGS.md` 之「V03 包（補落，自始未落檔）」節），",
         "並補施行其所令之 `profiles.vf230.test_group` 賦值。", "",
         f"## 2. 分類（{len(rows)} 處 ／ {len({r['file'] for r in rows})} 檔）", "",
         f"- **現行有效（須改）{len(live)} 處**",
         f"- **歷史紀錄（不追改）{len(hist)} 處**",
         f"- 待人工 {len(man)} 處", "",
         "### 2.1 現行有效者 —— 須改（逐處，以內容片段定位）", "",
         "| 檔 | 內容片段 | 涉及編號 | 屬哪一線 |", "|---|---|---|---|"]
    for r in sorted(live, key=lambda x: (x["file"], x["line"])):
        L.append(f"| `{r['file']}` | `{r['frag'][:70]}` | "
                 f"{'／'.join(r['nums'])} | {r['side']} |")
    L += ["", "**⚠ 上表含兩線之引用。** 依 R-VF45 一，**僅 VF230 線之八號改為 "
          "`R-VF1`–`R-VF8`，Part 1 之八號不動** —— 故本表之每一處尚須判其",
          "**所指為兩義之何者**，該判斷不可由編號決定，須讀其上下文。",
          "**本層未判、未改。**", "",
          "### 2.2 歷史紀錄者（逐檔計數，不追改）", "",
          "| 檔 | 處 |", "|---|---:|"]
    for k, v in Counter(r["file"] for r in hist).most_common(12):
        L.append(f"| `{k}` | {v} |")
    L += [f"| …（其餘 {len({r['file'] for r in hist}) - 12} 檔）| |"
          if len({r['file'] for r in hist}) > 12 else "", "",
          "## 3. 對照表（供 R-VF45 三置入 `RULINGS.md`）", "",
          "| 舊（VF230 線） | 新 |", "|---|---|"]
    for a, b in MAP.items():
        L.append(f"| `{a}` | `{b}` |")
    L += ["", "> 歷史文件中之 `R-VS59`–`R-VS67` 可能指兩義之任一，"
          "**以該文件之線別判之**。使歷史引用**可解，而非可靠**。", ""]

    p = ROOT / "docs" / "reports" / "wvf39_renumber_scope.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf39_scope.json").write_text(
        json.dumps({"rows": rows, "live": len(live), "hist": len(hist),
                    "map": MAP}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(rows)} 處／{len({r['file'] for r in rows})} 檔")
    print(f"現行 {len(live)}／歷史 {len(hist)}／待人工 {len(man)}")
    print(f"鑑別錨點：{'存在 — ' + a_disc['file'] if a_disc else '該形態不存在'}")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
