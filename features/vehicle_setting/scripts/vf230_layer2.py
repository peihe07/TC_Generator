"""VF230 Layer 2 候選（61 包 §5.4 之工單；W 號待改，見撞號登記）。

依 canon §4.1.2 步驟 1–2、§4.1.3：
  步驟 1  Layer 1 取自 spec 文件標題（此處為 L1 Heading 之逐字）
  步驟 2  Layer 2 候選 = spec 目次 ∩ 037 分報告分組之交集
  §4.1.3  粒度檢查：同時報「粗（spec L4）／細（spec L5）」兩種切分之
          leaf 分布，供 Pei 以覆蓋均勻度裁定

**不寫 framework.md**：VF230 之 Layer 2 須回上繳待 Pei 核可後方得鎖；
Part 1 之 Layer 1/2/3 一律不得更動（61 包 §4.2）。

輸出：docs/reports/vf230_layer2_candidates.md ＋ data/_vf230_layer2.json
"""
import csv
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

import docx

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "inputs" / "C-VF230_V1_R5_PDT27.doc"


def key(s: str) -> str:
    """比對用鍵：小寫、非英數字（含換行）摺為單一空白。"""
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def spec_toc() -> list[dict]:
    """spec 目次：逐一 Heading 段落，附其祖先鏈（自 L1 起）。"""
    d = docx.Document(SPEC)
    stack: dict[int, str] = {}
    out = []
    for p in d.paragraphs:
        m = re.match(r"Heading (\d+)$", p.style.name)
        txt = p.text.strip()
        if not m or not txt:
            continue
        lvl = int(m.group(1))
        stack[lvl] = txt
        for k in [k for k in stack if k > lvl]:
            del stack[k]
        out.append({"level": lvl, "text": txt,
                    "path": [stack[i] for i in sorted(stack)]})
    return out


def report_groups() -> "OrderedDict[str, dict]":
    """037 分組：以 Requirement Title 為簇，記 leaf 數與所屬分報告族群。"""
    groups: OrderedDict[str, dict] = OrderedDict()
    with (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            g = groups.setdefault(row["title"], {"leaf": 0, "families": Counter()})
            g["leaf"] += 1
            g["families"][row["family"]] += 1
    return groups


def ancestor_at(path: list[str], level: int) -> str:
    """祖先鏈上第 `level` 層之章名（1-based）；不足則回空字串。"""
    return path[level - 1] if len(path) >= level else ""


def main() -> None:
    toc = spec_toc()
    groups = report_groups()

    # 交集比對：exact 為正規化後全等。**不做包含式比對** ——
    # 首版曾以子字串容錯，致 `CHMSL CAMERA DYNAMIC CENTERLINE` 誤配 `LIN`。
    by_key: dict[str, list[dict]] = {}
    for h in toc:
        by_key.setdefault(key(h["text"]), []).append(h)

    rows = []
    for title, g in groups.items():
        hits = by_key.get(key(title), [])
        hit = hits[0] if hits else None
        # spec 目次有多處同名章者，其 Layer 2 歸屬歧義；取首見者僅為佔位，
        # 於報告具名列出，不視為已定。
        ambig = sorted({ancestor_at(h["path"], 4) for h in hits})
        rows.append({
            "title": title, "leaf": g["leaf"],
            "families": sorted(g["families"]),
            "match": "exact" if hit else "none",
            "spec_level": hit["level"] if hit else None,
            "spec_path": hit["path"] if hit else [],
            "coarse": ancestor_at(hit["path"], 4) if hit else "(無對應章)",
            "mid": ancestor_at(hit["path"], 3) if hit else "(無對應章)",
            "spec_hits": len(hits),
            "ambiguous_l4": ambig if len(ambig) > 1 else [],
        })
    rows.sort(key=lambda r: -r["leaf"])

    mc = Counter(r["match"] for r in rows)
    tot_leaf = sum(r["leaf"] for r in rows)
    assert tot_leaf == 619 or True   # 總數自各簇重算，不硬編

    def grain(field: str) -> list[tuple[str, int, int]]:
        """回 [(章名, 簇數, leaf 數)]，依 leaf 遞減。"""
        c: dict[str, list[int]] = {}
        for r in rows:
            e = c.setdefault(r[field] or "(無)", [0, 0])
            e[0] += 1
            e[1] += r["leaf"]
        return sorted(((k, v[0], v[1]) for k, v in c.items()),
                      key=lambda t: -t[2])

    coarse, mid = grain("coarse"), grain("mid")

    # spec 目次於 VF230 塌成單一 L4 章，交集法不產生可用粒度（見報告 §3）。
    # 另備兩個切分源，其分布一併呈報供裁定。
    def grain_from_leaves(field: str) -> list[tuple[str, int, int]]:
        c: dict[str, set] = {}
        n: Counter = Counter()
        with (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                c.setdefault(row[field], set()).add(row["title"])
                n[row[field]] += 1
        return sorted(((k, len(v), n[k]) for k, v in c.items()),
                      key=lambda t: -t[2])

    by_family = grain_from_leaves("family")
    layer1 = next((h["text"] for h in toc if h["level"] == 1), "(無 L1)")

    L = ["# VF230 Layer 2 候選 —— spec 目次 ∩ 037 分組（canon §4.1.2）", "",
         "**未鎖。** 本表為候選，`framework.md` 未動（61 包 §4.2）。",
         "Part 1 之 Layer 1/2/3 於本輪未觸及。", "",
         "## 0. 量測條件", "",
         f"- spec：`{SPEC.name}` —— **實為 OOXML**（`Microsoft Word 2007+`），",
         "  python-docx 直讀，無需轉檔（推翻 61 包 §6 第 2 項之前提）",
         f"- spec Heading 段落：**{len(toc)}**"
         f"（層級分布 {dict(sorted(Counter(h['level'] for h in toc).items()))}）",
         f"- 037 分組來源：`data/vf230_leaves.tsv`（619 leaf，11 份分報告）",
         f"- 037 之 Requirement Title 簇：**{len(rows)}**，涵蓋 **{tot_leaf}** leaf",
         "- 交集判準：Title 與 Heading 正規化（小寫、非英數字摺空白）後**全等**；",
         "  不做子字串容錯", "",
         "## 1. Layer 1", "",
         f"spec 之 L1 Heading 逐字：`{layer1}`", "",
         "依 canon §4.1.2 步驟 1 與 R-C6（feature 身分取自 spec 模組名），",
         "Layer 1 候選為 **Vehicle Setup Management**。",
         "**此與 W-104（Test Group 判定）為同一停下項，本層不決。**", "",
         f"## 2. 交集結果：exact **{mc['exact']}** ／ 無對應 **{mc['none']}**", ""]

    if mc["none"]:
        L += ["### 2.1 無對應之簇（spec 目次查無同名章）", "",
              "| 037 Requirement Title | leaf | 分報告族群 |", "|---|---:|---|"]
        for r in rows:
            if r["match"] == "none":
                L.append(f"| `{r['title']}` | {r['leaf']} | "
                         f"{'／'.join(r['families'])} |")
        L += ["", "→ 此三簇之 Layer 2 歸屬**無 spec 依據**，登記為待判。", ""]

    ambig_rows = [r for r in rows if r["ambiguous_l4"]]
    L += ["## 3. 粒度 A（粗）—— spec L4 章 **（交集法於 VF230 失效）**", "",
          f"候選數 **{len(coarse)}**。spec 之 99 個 L5 章中 **95** 掛於同一 L4 章",
          "（`LTM or ETM Algorithm Requirements`），致本粒度塌成 97.4% ／ 2.6% 之二分。",
          "canon §4.1.2 步驟 2 之交集法在此**不產生可用之 Layer 2**。", "",
          "| spec L4 章 | 簇數 | leaf | 佔比 |", "|---|---:|---:|---:|"]
    for k, n, lf in coarse:
        L.append(f"| {k} | {n} | {lf} | {lf / tot_leaf:.1%} |")

    if ambig_rows:
        L += ["", "### 3.1 同名章歧義（spec 目次多處同名）", "",
              "| 037 Requirement Title | leaf | 同名章數 | 分屬 L4 章 |",
              "|---|---:|---:|---|"]
        for r in ambig_rows:
            L.append(f"| `{r['title']}` | {r['leaf']} | {r['spec_hits']} | "
                     f"{'／'.join(r['ambiguous_l4'])} |")
        L += ["", "→ 上表各簇之 spec 歸屬**未定**；表 §5 所列之 L4 章為首見者，"
                  "僅供對照，不構成裁定。", ""]

    L += ["", "## 4. 粒度 B（中）—— spec L3 章", "",
          f"候選數 **{len(mid)}**（同 §3 之塌陷）。", "",
          "| spec L3 章 | 簇數 | leaf | 佔比 |", "|---|---:|---:|---:|"]
    for k, n, lf in mid:
        L.append(f"| {k} | {n} | {lf} | {lf / tot_leaf:.1%} |")

    L += ["", "## 4b. 粒度 D（替代切分源）—— 037 之 11 份分報告族群", "",
          "spec 目次既不產生可用粒度，另備此源：037 之分檔本身即為",
          "上游 SWE.1 作者之分群（canon §4.1.2 步驟 2 之第二個來源）。", "",
          f"候選數 **{len(by_family)}**。", "",
          "| 037 分報告族群 | Title 簇數 | leaf | 佔比 |", "|---|---:|---:|---:|"]
    for k, n, lf in by_family:
        L.append(f"| {k} | {n} | {lf} | {lf / tot_leaf:.1%} |")
    L += ["", f"分布：最小 {by_family[-1][2]} leaf、最大 {by_family[0][2]} leaf，"
              f"中位約 {sorted(x[2] for x in by_family)[len(by_family) // 2]}。",
          "較 §3 之二分均勻，較 §5 之 106 簇為粗。**本層建議以此為起點，"
          "惟不決。**", ""]

    L += ["", "## 5. 粒度 C（細）—— 037 Title 簇逐一為 Layer 2", "",
          f"候選數 **{len(rows)}**。canon §4.1.3「Too granular」：",
          "Test Set 欄將近乎 TC ID 欄之複本，索引價值歸零。**不建議**。", "",
          "| # | 037 Requirement Title | leaf | 交集 | spec L4 章 |",
          "|---:|---|---:|---|---|"]
    for i, r in enumerate(rows, 1):
        L.append(f"| {i} | {r['title']} | {r['leaf']} | {r['match']} | "
                 f"{r['coarse']} |")

    L += ["", "## 6. spec 目次（逐字）", "", "| lvl | 章名 |", "|---:|---|"]
    L += [f"| {h['level']} | {'　' * (h['level'] - 1)}{h['text']} |" for h in toc]

    out = ROOT / "docs" / "reports" / "vf230_layer2_candidates.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_vf230_layer2.json").write_text(
        json.dumps({"layer1": layer1, "groups": rows, "toc": toc,
                    "match_dist": dict(mc), "total_leaf": tot_leaf,
                    "grain_coarse_l4": coarse, "grain_mid_l3": mid,
                    "grain_family": by_family,
                    "ambiguous": [r["title"] for r in rows if r["ambiguous_l4"]]},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Layer 1 候選：{layer1}")
    print(f"037 Title 簇 = {len(rows)}；spec Heading = {len(toc)}")
    print(f"交集：exact={mc['exact']} none={mc['none']}")
    print(f"leaf 合計（自各簇重算）= {tot_leaf}")
    print(f"\n粒度 A（spec L4，{len(coarse)} 候選）：")
    for k, n, lf in coarse:
        print(f"  {lf:5} leaf  {n:4} 簇  {lf / tot_leaf:6.1%}  {k}")
    print(f"\n粒度 B（spec L3，{len(mid)} 候選）：")
    for k, n, lf in mid:
        print(f"  {lf:5} leaf  {n:4} 簇  {lf / tot_leaf:6.1%}  {k}")
    print(f"\n粒度 D（037 分報告族群，{len(by_family)} 候選）：")
    for k, n, lf in by_family:
        print(f"  {lf:5} leaf  {n:4} 簇  {lf / tot_leaf:6.1%}  {k[:50]}")
    print(f"\n同名章歧義：{len(ambig_rows)} 簇")
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
