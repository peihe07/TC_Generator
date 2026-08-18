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

    path = DATA / "b5_residual_sample.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"母體 {len(wording)}（候選 {len(cand)} － 委由他節 {len(deleg)}）；"
          f"抽 {SAMPLE_N}（seed={SEED}，抽樣率 {SAMPLE_N/len(wording)*100:.1f}%）")
    missing = sorted({c["word"] for c in sample if c["word"] not in REASON})
    print(f"缺理由之詞：{missing or '（無）'}")


if __name__ == "__main__":
    main()
