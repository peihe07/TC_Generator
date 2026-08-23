"""W-VF24 —— 收斂為單一套之前置清單（V09 §2；**只列不改**）。

R-VF23 第四項令收斂方向為 `V{NN}_` 平鋪，且
**「全部檔案搬移與 git 操作屬 Pei。兩層只備清單，不執行。」**

本腳本**不執行任何搬移、不改名、不 `git mv`、不刪目錄**，
僅產出可供 Pei 逐條核對之表。

現況以**當下之檔案系統**復測（V09 §2 第 1 項：不以 V07／V08 之目錄列表
為來源）。

輸出：docs/reports/wvf24_converge_plan.md
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HO, UP = ROOT / "docs" / "handoff", ROOT / "docs" / "upstream"

# R-VF10 §3.2（V04）＋ R-VF23 第四項（V09）之對照，逐條列出
MOVES = [
    ("docs/handoff/ZZ_vf230_numbering_collision.md",
     "docs/handoff/V00_numbering_collision.md", "V04 §3.2"),
    ("docs/handoff/61_vf230_intake.md",
     "docs/handoff/V01_vf230_intake.md", "V04 §3.2"),
    ("docs/handoff/62_vf230_recon_review.md",
     "docs/handoff/V02_vf230_recon_review.md", "V04 §3.2"),
    ("docs/handoff/63_test_group_ruling.md",
     "docs/handoff/V03_test_group_ruling.md", "V04 §3.2"),
    ("docs/upstream/vf230/00_intake.md",
     "docs/upstream/V01_vf230_intake.md", "V09 §1 第四項"),
    ("docs/upstream/vf230/01_recon.md",
     "docs/upstream/V02_vf230_recon.md", "V09 §1 第四項"),
]
TARGETS = ["vf230/00_intake", "vf230/01_recon",
           "61_vf230_intake", "62_vf230_recon"]

# 「須同步更新」= 現行有效之陳述（R-VF18 之同一判準）
def live(f: str) -> bool:
    if f.startswith(("docs/handoff/", "docs/upstream/")):
        return False          # 下放／上繳為歷史紀錄
    if f.startswith("docs/reports/"):
        return False          # 已結案之報告
    return True               # RULINGS／INDEX／scripts／feature.yaml 等


def main() -> None:
    ho = sorted(p.name for p in HO.glob("*.md"))
    up = sorted(p.name for p in UP.glob("*.md"))
    sub = sorted(p.name for p in (UP / "vf230").glob("*.md")) \
        if (UP / "vf230").is_dir() else []

    vf_ho = [n for n in ho
             if re.match(r"^(V\d{2}|ZZ)_", n)
             or n in ("61_vf230_intake.md", "62_vf230_recon_review.md",
                      "63_test_group_ruling.md")]
    vf_up = [n for n in up if n.startswith("V")]

    # 兩線同號者
    dup = sorted({n[:2] for n in ho if re.match(r"^\d{2}_", n)}
                 & {n[:2] for n in vf_ho if re.match(r"^\d{2}_", n)})

    out = subprocess.run(
        ["grep", "-rn", "-E", "|".join(re.escape(t) for t in TARGETS),
         "--include=*.md", "--include=*.py", "--include=*.yaml", "."],
        capture_output=True, text=True, cwd=ROOT).stdout
    refs = []
    for ln in out.splitlines():
        m = re.match(r"^\./([^:]+):(\d+):(.*)$", ln)
        if not m:
            continue
        f, n, txt = m.group(1), int(m.group(2)), m.group(3).strip()
        hit = next((t for t in TARGETS if t in txt), "")
        refs.append({"file": f, "line": n, "target": hit, "live": live(f)})
    live_refs = [r for r in refs if r["live"]]

    L = ["# W-VF24 —— 收斂為單一套之前置清單（V09 §2）", "",
         "**只列不改。** R-VF23 第四項：全部檔案搬移與 git 操作屬 Pei，",
         "兩層只備清單，不執行。**本輪未搬移、未改名、未 `git mv`、未刪目錄。**", "",
         "## 1. 現況（本輪復測，不以 V07／V08 之目錄列表為來源）", "",
         f"- `docs/handoff/` 共 **{len(ho)}** 檔，其中屬 VF230 線 **{len(vf_ho)}**",
         f"- `docs/upstream/` 一層共 **{len(up)}** 檔，其中 `V*` **{len(vf_up)}**",
         f"- `docs/upstream/vf230/` **{len(sub)}** 檔："
         + "／".join(f"`{n}`" for n in sub), "",
         "**VF230 線之 handoff 逐檔**：", ""]
    L += [f"- `{n}`" for n in vf_ho]
    L += ["", "**VF230 線之 upstream 逐檔**：", ""]
    L += [f"- `docs/upstream/{n}`" for n in vf_up]
    L += [f"- `docs/upstream/vf230/{n}`" for n in sub]

    L += ["", "## 2. 兩線同號之殘留（handoff 側）", ""]
    if dup:
        L += ["| 號 | Part 1 線 | VF230 線 |", "|---|---|---|"]
        for d in dup:
            p1 = next((n for n in ho if n.startswith(d + "_") and n not in vf_ho), "—")
            p2 = next((n for n in vf_ho if n.startswith(d + "_")), "—")
            L.append(f"| {d} | `{p1}` | `{p2}` |")
        L += ["", f"**{len(dup)} 個號各有兩義，撞號於 handoff 側仍為現行狀態。**",
              "upstream 側已無同號（VF230 線為 `V*` 或 `vf230/`）。", ""]
    else:
        L += ["無。", ""]

    L += ["## 3. 搬移表（供 Pei 逐條核對；**本層未執行**）", "",
          "| # | 舊路徑 | 新路徑 | 線 | 依據 | 現況 |",
          "|---:|---|---|---|---|---|"]
    for i, (a, b, why) in enumerate(MOVES, 1):
        exists = (ROOT / a).exists()
        tgt = (ROOT / b).exists()
        st = ("**新路徑已存在，須先確認**" if tgt else
              ("待搬" if exists else "**舊路徑不存在，無須搬**"))
        L.append(f"| {i} | `{a}` | `{b}` | VF230 | {why} | {st} |")
    L += ["",
          "搬移後另須 **移除空目錄 `docs/upstream/vf230/`**（V09 §1 第四項）。",
          "",
          "**Part 1 之 `00_`–`38_` 一律不列入**（V09 §2 第 2 項）。", ""]

    L += [f"## 4. 交叉引用（{len(refs)} 處 ／ "
          f"{len({r['file'] for r in refs})} 檔）", "",
          f"- **搬移後須同步更新 {len(live_refs)} 處**（現行有效之陳述）",
          f"- 其餘 **{len(refs) - len(live_refs)}** 處位於 `docs/handoff/`／",
          "  `docs/upstream/`／`docs/reports/`，依 **R-VF18** 為歷史紀錄，**不追改**",
          "", "### 4.1 須同步更新者（逐處）", "",
          "| 檔:行 | 所指 |", "|---|---|"]
    for r in sorted(live_refs, key=lambda x: (x["file"], x["line"])):
        L.append(f"| `{r['file']}:{r['line']}` | `{r['target']}` |")

    L += ["", "### 4.2 不追改者（逐檔計數）", "", "| 檔 | 處 |", "|---|---:|"]
    cnt: dict[str, int] = {}
    for r in refs:
        if not r["live"]:
            cnt[r["file"]] = cnt.get(r["file"], 0) + 1
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        L.append(f"| `{k}` | {v} |")

    L += ["", "## 5. 與併行線之協調點（V09 §2 第 4 項）", "",
          "`docs/upstream/vf230/` 二檔係**併行線**於 `7a7747e`／`942f0d7` 所搬。",
          "**搬回之衝突點如下，本層不逕行。**", ""]
    par = sorted({r["file"] for r in refs
                  if r["target"].startswith("vf230/")
                  and re.match(r"docs/handoff/\d{2}_", r["file"])})
    if par:
        L += ["**併行線之檔案已引用新路徑**，搬回將使其引用失效：", ""]
        L += [f"- `{f}`" for f in par]
        L += ["", "→ **此為實質衝突**：該等檔為 Part 1 線之下放包，"
              "依 R-VF18 為歷史紀錄不追改，"
              "但搬移後其所指之路徑將不存在。", "",
              "**兩種處置，本層不擇一**：", "",
              "1. 搬回並接受 Part 1 下放包內留有失效路徑"
              "（與 R-VF18「歷史不追改」一致，代價是連結斷）",
              "2. 不搬回，改令 R-VF23 第四項之收斂方向為 `vf230/`"
              "（與 R-VF23 第三項「R-VF10 維持原文」相牴觸）", ""]
    else:
        L += ["併行線之檔案未引用該二路徑，搬回無引用面之衝突。", ""]
    L += ["**另**：本層未查併行線是否有未提交之作業正在動該二檔。",
          "`git status` 於本輪執行時之結果須由 Pei 於實際搬移前復查 ——",
          "**本清單之有效期止於下一次併行線提交。**", ""]

    p = ROOT / "docs" / "reports" / "wvf24_converge_plan.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"handoff {len(ho)}（VF230 線 {len(vf_ho)}）／upstream {len(up)}"
          f"（V* {len(vf_up)}）／vf230/ {len(sub)}")
    print(f"兩線同號 {len(dup)}: {dup}")
    print(f"搬移表 {len(MOVES)} 列；交叉引用 {len(refs)} 處，"
          f"須同步 {len(live_refs)}，不追改 {len(refs) - len(live_refs)}")
    print(f"併行線引用新路徑之檔 {len(par)}: {par}")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
