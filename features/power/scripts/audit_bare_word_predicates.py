"""G195 —— 28 個裸詞謂詞之逐一實測（R-P280）。

40 §十第 3 項：第 6 列之 `limit` 係**因其影響面被察覺才查出** ——
**影響面小者不會被察覺，而其偽陽性同樣存在**。

R-P280：28 個逐一實測，逐個回報命中數、抽樣其命中之實例
（每個至少 3 條，不足者全取），逐條判真陽性／偽陽性。

**判準（本包所立）**：一個命中為**偽陽性**，若該裸詞於命中處之語義
**與該謂詞之用途無關**。例：`ROW6_RE` 之 `limit` 命中
「the volume **limit** returns to its normal maximum」——
該 `limit` 為音量上限之名詞，與「界線值測試」無關 → 偽陽性。

**本檔只實測與呈；不改任何 TC 值**（R-P280(d) / §I）。
謂詞之重寫另行為之，其結論於 42 包裁定。

用法：
    python features/power/scripts/audit_bare_word_predicates.py
"""

from __future__ import annotations

import collections
import glob
import json
import importlib
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent
SEED = 41
sys.path.insert(0, str(SCRIPTS))

from audit_duplicate_predicates import collect_patterns, BARE_WORD_RE, SKIP  # noqa: E402
from audit_style_predicates import corpus  # noqa: E402

# 各謂詞之語料類別（其自身之輸入）。未列者以 TC 六欄為預設。
# 各謂詞之語料 = **其自身之輸入**。
#
# ⚠ 初版以「命中最多之語料類別」為準，該法**偏向最大之語料**（文字層），
# 致 `lint_tcs` / `confirm_row4` 等之實測落在其根本不會讀的文字上 ——
# 與 36 包 G176 之量測設計缺陷同型。改為逐模組指定。
CORPUS_OF = {
    "extract_textlayer": "文字層",
    "build_dangling": "文字層", "build_dangling_rulecheck": "文字層",
    "g113_buckets": "規格", "scan_clause_patterns": "規格",
    "reverse_coverage": "規格", "confirm_row4": "規格",
    "build_er_restatement": "規格", "build_precond_verbs": "TC",
    "lint_tcs": "TC", "rejudge_design_method": "TC", "rejudge_axis": "TC",
    "rejudge_priority": "TC", "audit_precond_state": "TC",
    "reverse_probe_rows": "TC", "build_swepm025_triggers": "規格",
    "build_b4_signals": "規格",
}


def main() -> None:
    cor = corpus()
    rng = random.Random(SEED)
    rows = []
    for mod, name, src in collect_patterns():
        words = sorted({w for w in BARE_WORD_RE.findall(src)
                        if w not in SKIP and len(w) >= 4})
        if not words:
            continue
        # ⚠ 初版以 `re.compile(src, re.I)` 取上界，**該作法製造非真實之偽陽性** ——
        # 謂詞實際未必帶 `re.I`（如 `audit_precond_state.MODE_RE` 刻意區分大小寫）。
        # 改為**匯入該模組取其真正編譯之物件**，連旗標一併取得。
        try:
            mod_obj = importlib.import_module(mod)
            pat = getattr(mod_obj, name)
        except Exception:
            continue
        if not isinstance(pat, re.Pattern):
            continue
        # **以該謂詞自身之輸入為語料**（見 `CORPUS_OF` 之註解）
        best = CORPUS_OF.get(mod, "TC")
        text = cor[best]
        n = len(pat.findall(text))
        hits = [(m.start(), m.group(0)) for m in pat.finditer(text)]
        k = min(len(hits), max(3, 0))
        sample = rng.sample(hits, min(len(hits), 3)) if hits else []
        ctx = [(t, " ".join(text[max(0, p - 46):p + len(t) + 40].split()))
               for p, t in sorted(sample)]
        rows.append({"mod": mod, "name": name, "words": words,
                     "corpus": best, "n": n, "ctx": ctx})

    out = ["# G195 —— 裸詞謂詞之逐一實測（R-P280）\n",
           "\n> **本檔只實測與呈；不改任何 TC 值**（R-P280(d)）。\n",
           "> **判準**：一個命中為**偽陽性**，若該裸詞於命中處之語義"
           "**與該謂詞之用途無關**。\n",
           f"> 抽樣種子 `random.Random({SEED})`；每謂詞抽 3 條，不足者全取。\n",
           f"\n## 一、彙總（{len(rows)} 個謂詞）\n\n"
           "| 模組.謂詞 | 語料 | 命中 | 裸詞 |\n|---|---|---|---|\n"]
    for r in rows:
        out.append(f"| `{r['mod']}.{r['name']}` | {r['corpus']} | {r['n']} | "
                   f"{'、'.join('`' + w + '`' for w in r['words'][:8])} |\n")
    out.append("\n## 二、逐一之抽樣實例\n")
    for r in rows:
        out.append(f"\n### `{r['mod']}.{r['name']}` —— 命中 {r['n']}（語料：{r['corpus']}）\n\n"
                   "| 命中字串 | 語境 |\n|---|---|\n")
        for tok, c in r["ctx"]:
            out.append(f"| `{tok}` | `{c}` |\n")
        if not r["ctx"]:
            out.append("| （命中 0） | |\n")

    p = DATA / "g195_bare_word_predicates.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"謂詞 {len(rows)} 個，抽樣實例已列於報表")
    for r in rows:
        print(f"\n--- {r['mod']}.{r['name']}  [{r['corpus']}]  命中 {r['n']}")
        for tok, c in r["ctx"]:
            print(f"      `{tok}`  …{c[:96]}…")


# ── 逐一裁定（R-P280(b)(c)）──
# 每項為（真陽性？, 說明）。判準見模組首段。
# **⚠ 稽核方式之二次訂正已記於上繳**：初版以「命中最多之語料」選語料（偏向文字層）、
# 且以 `re.compile(src, re.I)` 取上界（製造非真實之偽陽性）；
# 現版以**逐模組指定之語料**與**模組內真正編譯之謂詞物件**（連旗標）為之。
VERDICT: dict[str, tuple[bool, str]] = {
    "audit_precond_state.MODE_RE": (False,
        "**偽陽性** —— 其第二 alternative `\\b([A-Z]{3,}…)\\b` 命中 `TLM` / `CAN` 等"
        "純大寫縮寫，非模式名。惟其用途為**列出候選供人工判讀**，非自動判定，"
        "偽陽性之代價為人工過濾；**不重寫**"),
    "audit_precond_state.BENCH_RE": (True, "命中皆為 `simulation tool is connected` 等真樣板句"),
    "build_dangling.WRAPPER_RE": (True, "命中皆為 `*.rtf/.xls WrapperResource` 之真資源列"),
    "build_dangling_rulecheck.RESOURCE_RE": (True, "同上"),
    "confirm_row4.COND_RE": (True, "命中 `When` / `IF` / `if` 皆為真條件子句起首"),
    "g113_buckets.ILLUSTRATIVE_RE": (True, "命中 `for example` / `refer to … Specification` 皆為真例示語"),
    "lint_tcs.ENV_STABILITY_RE": (False,
        "**命中 0** —— 依 R-P250「一個都取不到者，該謂詞不得使用」。"
        "該閘門自建立以來**從未觸發**，其 PASS 不具意義（同 R-P251 之形態）"),
    "lint_tcs.TABLE_RE": (False, "**命中 0** —— 同上；TC 六欄中無表格標記"),
    "lint_tcs.PRECOND_BEHAVIOUR_RE": (True, "命中 `passes to` / `transition to` / `occurred` 皆為真行為語"),
    "lint_tcs.TEST_QUANTITY_RE": (True, "命中 `event burst` / `intervals` / `measurement window` 皆為真測試量"),
    "lint_tcs.FINAL_STEP_INTENT_RE": (True, "命中皆為 `to check` 之真末步意圖語"),
    "lint_tcs.TIME_TOKEN_RE": (True, "命中 `10 seconds` / `00 min` 皆為真時間量"),
    "lint_tcs.TIME_EQUALITY_RE": (True,
        "**訂正：真陽性** —— 初判為偽（`equal to 2025` 車型年、`matches the assignment` "
        "座椅圖形皆非時間之相等），惟查其生產路徑為 "
        "`if eq and TIME_TOKEN_RE.search(line)` —— **二謂詞須同行併中**；"
        "實測生產路徑之命中為 **0**，上列偽陽性**不出現**。"
        "**此為稽核方式之假象，與 `rejudge_design_method.BENCH_RE` 同型** —— "
        "單獨量測一個僅供併用之謂詞會誇大其偽陽性"),
    "rejudge_axis.TIMING_RE": (True, "命中 `00 min` / `20 minutes` / `timeout` 皆為真時間量"),
    "rejudge_axis.BOUNDARY_RE": (False,
        "**偽陽性** —— `other than \"00 min\"` 為**等價劃分**（§12 第 5 列之措詞），非界線值。"
        "37 包立本謂詞正是為修 `limit` 之同型缺陷，而 `other than` 為新引入之同型問題"),
    "rejudge_design_method.NO_TRANSITION_RE": (True, "命中 `no change` / `still at` / `stays in` 皆為真不轉換語"),
    "rejudge_design_method.ROW1_RE": (True, "唯一命中 `Attempt to change the offered timeout parameter` 為真"),
    "rejudge_design_method.ROW2_RE": (True,
        "二命中皆為 `battery is disconnected` / `battery disconnection` —— "
        "**其為情境建構之前提，依 R-P232 第 2 列不命中**；謂詞本身之命中為真，"
        "其排除由 `propose()` 之欄位限定為之"),
    "rejudge_design_method.POSITIVE_RE": (True, "命中 `is in BODY OFF-TIMED mode` 等皆為真狀態語"),
    "rejudge_design_method.ROW6_RE": (True,
        "39 包已移除裸詞 `limit`；現命中 `the day before` / `after the date passes` 皆為真界線"),
    "rejudge_design_method.BENCH_RE": (True,
        "抽樣中 `The second call is connected` 之 `is connected` 為偽，"
        "**惟其在 ER 欄** —— 生產路徑上 `substantive_conditions` 只掃 `pre_conditions` 之編號行，"
        "該命中不出現。**本稽核以全六欄為語料，故此偽陽性為稽核方式所致，非謂詞缺陷**"),
    "rejudge_design_method.ROW5_RE": (True, "命中 `out of range` / `a value other than` 皆為真等價切分"),
    "rejudge_priority.COSMETIC_RE": (False,
        "**偽陽性，且在生產路徑上** —— `Brand_Configuration _2` 為**參數名**而非裝飾性；"
        "實測 **6 條**僅因該參數名而命中，其中 **3 條（`…-063` / `…-065` / `…-095`）"
        "之現值已因此被改為 P3**（38 包）"),
    "rejudge_priority.BENCH_RE": (True, "命中皆為 `simulation tool is connected` 之真樣板"),
    "reverse_coverage.SPLIT_RE": (True, "其為分隔符謂詞，命中空白／換行屬設計本意"),
    "reverse_probe_rows.PARAM_RE": (True, "命中 `RemStartFail is at \"False\"` 等皆為真參數取值"),
    "reverse_probe_rows.REMOVE_RE": (True, "二命中皆為 `Stop the broadcast …` 之真移除動作"),
    "scan_clause_patterns.ENUM_RE": (True, "命中 `Behaviour 2: \"…\"` 等皆為真枚舉標記"),
}


if __name__ == "__main__":
    main()
