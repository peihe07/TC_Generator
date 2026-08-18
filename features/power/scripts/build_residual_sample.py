"""B5 —— 殘差詞「措詞差異」抽樣覆核（R-P138）。

18 §七(甲)4 自陳：信噪比之分母（123 個「措詞差異」）**由同一人判定**，
判別者與被判別之工作同源；分桶降低了回報成本，未降低誤判風險。

R-P138：自「措詞差異」桶中**固定亂數種子**隨機抽 20 個，逐一列出
殘差詞、所屬行為項、最佳對應 TC、判為措詞差異之理由，由分析層覆核。

**種子值 SEED = 19（＝本包編號），載明於此與報告中，抽樣可重現。**

用法：
    python features/power/scripts/build_residual_sample.py
"""

from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
BATCH = ROOT / "features/power/generated/batch_002_timeout_settings.json"

SEED = 19
SAMPLE_N = 20

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reverse_coverage import analyse  # noqa: E402

# 依 R-P42 委由他節／他 leaf 者，不屬「措詞差異」桶
DELEGATED = {("SWE-PM-057", 8, w) for w in
             ("auto_switchon_setting.req", "section", "see", "management", "through")}

REASON = json.loads((Path(__file__).parent / "residual_reasons.json")
                    .read_text(encoding="utf-8"))

# R-P146 —— 抽取層之排版黏連。CFTS 原文之 `00 minutesAND`、`expirationTHENat`、
# `THENTLM` 等係轉檔時空白遺失所致，**非語義單位**。
# 判準（機械）：原文中之詞**內嵌全大寫之流程連接詞**
# （`AND` / `THEN` / `OR` / `IF` / `WHEN` / `ELSE`）而未以空白分隔。
#
# 判準演進（如實記錄）：初版以「內部大小寫轉折 `[a-z][A-Z]`」判定，
# 誤將 `MaxCallTimeout` 這類 **CamelCase 參數名**判為黏連（黏連數虛報 23）；
# 次版改以子字串精確化仍留 `maxcalltimeout`（10）。
# 現版限定「內嵌全大寫連接詞」——此為黏連之真正特徵，參數名不具之。
# **判準不改**（R-P146）：黏連僅供另列一行並存之信噪比，不自母體剔除。
GLUE_RE = re.compile(r"\b\w*[a-z](?:AND|THEN|OR|IF|WHEN|ELSE)\w*\b")


def main() -> None:
    batch = json.loads(BATCH.read_text(encoding="utf-8"))
    res = analyse(batch, 0.45)

    cand = []
    for leaf, r in res.items():
        for n, w in r["buckets"]["候選（須人工判 措詞差異 / 真缺口）"]:
            item = next(x for x in r["items"] if x["n"] == n)
            cand.append({"leaf": leaf, "n": n, "word": w, "best": item["best"],
                         "score": item["score"], "text": item["text"]})
    deleg = [c for c in cand if (c["leaf"], c["n"], c["word"]) in DELEGATED]
    wording = [c for c in cand if c not in deleg]

    random.seed(SEED)
    sample = sorted(random.sample(wording, SAMPLE_N),
                    key=lambda c: (c["leaf"], c["n"], c["word"]))

    out = ["# B5 —— 殘差詞「措詞差異」抽樣覆核（R-P138）\n",
           f"\n> 母體：第二批之「措詞差異」桶，共 **{len(wording)}** 個"
           f"（候選 {len(cand)} － 依 R-P42 委由他節者 {len(deleg)}）。\n",
           f"> 抽樣：`random.seed({SEED})` ＋ `random.sample(母體, {SAMPLE_N})`；"
           f"**種子值 {SEED}（＝本包編號）載明於本檔與 `build_residual_sample.py`**，可重現。\n",
           f"> 抽樣率 **{SAMPLE_N / len(wording) * 100:.1f}%**。**由分析層覆核。**\n",
           "> 註：18 包所報之唯一真缺口（`pre`）已由 `043` 補測，故不再出現於本母體。\n",
           "\n| leaf | 行為項 | 殘差詞 | 最佳對應 | overlap | 判為措詞差異之理由 |\n"
           "|---|---|---|---|---|---|\n"]
    for c in sample:
        reason = REASON.get(c["word"], "**（未列理由 —— 須補）**")
        out.append(f"| `{c['leaf']}` | #{c['n']} | `{c['word']}` | "
                   f"`{(c['best'] or '—')[-3:]}` | {c['score']:.2f} | {reason} |\n")

    out.append("\n## 抽中之行為項原文（供對照）\n\n")
    seen = set()
    for c in sample:
        if (c["leaf"], c["n"]) in seen:
            continue
        seen.add((c["leaf"], c["n"]))
        out.append(f"- `{c['leaf']}` #{c['n']}（最佳對應 `{(c['best'] or '—')[-3:]}`，"
                   f"overlap {c['score']:.2f}）：{c['text'][:170]}\n")

    # ---- B4（R-P145）：「已由他條涵蓋」桶之覆核 ----
    covered = []
    for leaf, r in res.items():
        for n, w in r["buckets"]["已由他條涵蓋"]:
            item = next(x for x in r["items"] if x["n"] == n)
            covered.append({"leaf": leaf, "n": n, "word": w,
                            "best": item["best"], "score": item["score"]})
    out.append(f"\n---\n\n## B4 —— 「已由他條涵蓋」桶之覆核（R-P145）\n\n"
               f"該桶共 **{len(covered)}** 項，**全數列出（覆核率 100%，"
               f"高於「措詞差異」桶之 {SAMPLE_N / len(wording) * 100:.1f}%）**。\n\n"
               f"> 該桶雖為機械判定（該殘差詞見於同 leaf 之他條 TC），"
               f"**其判定規則仍為執行層所訂** —— 故一併送覆核。\n\n"
               "| leaf | 行為項 | 殘差詞 | 最佳對應 | overlap | 見於同 leaf 之他條 |\n"
               "|---|---|---|---|---|---|\n")
    by_leaf_words = {}
    for leaf, r in res.items():
        for tc in batch["tcs"]:
            if tc["req_id"] != leaf:
                continue
            by_leaf_words.setdefault(leaf, []).append(tc["tc_id"])
    for c in sorted(covered, key=lambda x: (x["leaf"], x["n"], x["word"])):
        out.append(f"| `{c['leaf']}` | #{c['n']} | `{c['word']}` | "
                   f"`{(c['best'] or '—')[-3:]}` | {c['score']:.2f} | "
                   f"同 leaf 共 {len(by_leaf_words.get(c['leaf'], []))} 條 |\n")

    # ---- B5（R-P146）：黏連正規化後之信噪比，與原值並存 ----
    glue = set()
    for leaf in res:
        clause = next(l["source_clause"] for l in batch["leaves"] if l["parent"] == leaf)
        for w in GLUE_RE.findall(clause):
            glue.add(w.lower())
    # **判為黏連者須為該黏連詞本身，非其子字串。**
    # 初版以 `word in g` 判定，致 `expiration` / `maxcalltimeout` / `s` / `set` /
    # `time` 等正常詞被誤判為黏連（因其為 `expirationTHENat` 等之子字串），
    # 黏連數虛報為 23。改為對黏連詞取詞幹後**精確相等**。
    from build_er_restatement import _stem
    glue_stems = {_stem(g) for g in glue}
    glue_hits = sorted({c["word"] for c in cand if c["word"] in glue_stems})
    n_total = len(cand) + sum(len(r["buckets"]["已由他條涵蓋"]) for r in res.values())
    n_glue = sum(1 for leaf, r in res.items()
                 for x in r["items"] for w in x["residual"] if w in glue_stems)
    out.append(f"\n---\n\n## B5 —— 信噪比：原值與黏連正規化後之值並存（R-P146）\n\n"
               f"> **判準未改**（20 §I）—— 黏連僅另列一行，不自母體剔除，"
               f"**不以任一值取代另一值**。\n\n"
               f"| 口徑 | 分子（真缺口）| 分母（殘差詞）| 信噪比 |\n|---|---|---|---|\n"
               f"| **原值**（19 包所報）| 1 | {n_total} | **{1 / n_total * 100:.1f}%** |\n"
               f"| **黏連正規化後** | 1 | {n_total - n_glue} | "
               f"**{1 / max(1, n_total - n_glue) * 100:.1f}%** |\n\n"
               f"被判為抽取層黏連之殘差詞（**{n_glue}** 項，"
               f"{len(glue_hits)} 個相異詞）：\n\n"
               + ("、".join(f"`{w}`" for w in glue_hits) or "（無）") + "\n\n"
               f"其原文形態取自 `source_clause` 中含內部大小寫轉折之詞"
               f"（如 `00 minutesAND`、`expirationTHENat`、`THENTLM`）——\n"
               f"係轉檔時空白遺失所致，**非語義單位**。\n")

    path = DATA / "b5_residual_sample.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"母體 {len(wording)}（候選 {len(cand)} － 委由他節 {len(deleg)}）；"
          f"抽 {SAMPLE_N}（seed={SEED}，抽樣率 {SAMPLE_N/len(wording)*100:.1f}%）")
    missing = sorted({c["word"] for c in sample if c["word"] not in REASON})
    print(f"缺理由之詞：{missing or '（無）'}")


if __name__ == "__main__":
    main()
