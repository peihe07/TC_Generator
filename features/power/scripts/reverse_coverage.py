"""B1 —— 反向涵蓋（R-P118）。

G82 問「ER 之具名標的在不在 `source_clause` 裡」。
本腳本問**相反方向**：**`source_clause` 裡有而 TC 裡沒有的，是什麼。**

R-P118 明訂本檢查**不做成 pass / fail 閘門**：
「無對應」者不判 FAIL、不使 exit=1，另列一節輸出，逐項須人工裁決三選一
（`真缺口` / `規格未給門檻，不可獨立驗證` / `已由他條涵蓋`）。
沉默不算裁決。

**兩道獨立之透鏡**（其一漏掉者，其二未必漏）：

  透鏡 1 —— **行為項層**。將 `source_clause` 拆為行為項，
            以實詞重疊率找出無 TC 對應者。
  透鏡 2 —— **規格標的層**。取 `source_clause` 之**具名標的**
            （訊號名、全大寫術語、`_Time` 類參數、模式名、數值），
            列出**未出現於該 leaf 任何一條 TC** 者。
            此即 G82 之鏡像 —— G82 由 ER 看向 spec，本透鏡由 spec 看向 TC。
  透鏡 3 —— **逐項殘差詞**。對**每一個**行為項（不論其判為已覆蓋與否），
            列出「該項有而其最佳對應 TC 沒有」之實詞。
            **本透鏡係於透鏡 1 漏掉 R-P117(a) 之後才加**（見上繳 §一之驗證條件）——
            此順序必須明載：它不是預先設計，是被漏檢逼出來的。
            它不改動任何門檻或拆句規則，只是把殘差列出來而非丟棄。

**拆句規則於本檔一次寫定，對三個 leaf 一體適用**，
不因結果好看與否而調整（17 §I）。

用法：
    python features/power/scripts/reverse_coverage.py
    python features/power/scripts/reverse_coverage.py --batch <path.json>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
DEFAULT_BATCH = ROOT / "features/power/generated/batch_001_power_down.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_er_restatement import STOP, WORD_RE, _stem  # noqa: E402

# 行為項之切分點。句末標點之外，另切「引入獨立行為或終止條件」之連接詞：
#   `;`            —— 規格以分號並列獨立條款
#   ` until `      —— 終止條件（一個行為之結束＝另一個可觀察之行為）
#   ` and if `     —— 附條件之第二動作
#   ` If ` / ` Under ` / ` While ` / ` Unless ` —— 條件子句起首
# 切得細會多問問題（偽陽性），切得粗會漏問（偽陰性）。
# **本規則偏向切細** —— R-P118 之產物是「該問的問題」，多問之成本低於漏問。
SPLIT_RE = re.compile(
    r"(?<=[.;])\s+|\s+(?=until\s)|\s+(?=and\s+if\s)|"
    r"\s+(?=If\s)|\s+(?=Under\s)|\s+(?=While\s)|\s+(?=Unless\s)",
)

# 具名標的（透鏡 2）。刻意不含一般英文詞 —— 措詞本就不會逐字相同。
NAMED_RE = re.compile(
    r"[A-Za-z][A-Za-z0-9]*(?:[._][A-Za-z0-9]+)+"      # STATUS_LIN.Batt_ST_Crit / SplashScreen_Time
    r"|\b[A-Z]{2,}(?:[-\s][A-Z]{2,}(?:-[A-Z]+)?)*\b"  # BODY ON / BODY OFF-TIMED / ICS / TLM
    r"|\[\d+h\]"                                       # [1h]
    r"|\b\d+\b"                                        # 20 / 10
)
# 全 leaf 通用之載體詞，非可測標的
NAMED_SKIP = {"TLM", "CAN", "LIN", "HMI", "ID"}


def normalize(text: str) -> str:
    """NBSP → 空格。規格原文之 `BODY\xa0OFF-TIMED` 與 TC 之 `BODY OFF-TIMED`
    語義相同而位元組不同；不正規化會產生純字元層之偽陽性。
    此為字元正規化，對三個 leaf 一體適用，非判準之調整。"""
    return text.replace("\xa0", " ").replace("\u2009", " ")


def words(text: str) -> set[str]:
    return {_stem(w.lower()) for w in WORD_RE.findall(text)} - STOP


def named(text: str) -> set[str]:
    out = set()
    for m in NAMED_RE.findall(text):
        tok = m.strip()
        if tok and tok not in NAMED_SKIP:
            out.add(tok)
    return out


def behaviour_items(clause: str) -> list[str]:
    items = []
    for part in SPLIT_RE.split(" ".join(normalize(clause).split())):
        part = part.strip(" ;.")
        if len(part.split()) >= 3:          # 三字以下非行為陳述
            items.append(part)
    return items


def tc_text(tc: dict) -> str:
    return normalize(" ".join(str(tc.get(f, "")) for f in
                    ("tc_title", "test_item", "pre_conditions", "input_test_data",
                     "test_procedure", "expected_result")))


def analyse(batch: dict, threshold: float) -> dict:
    leaves = {l["parent"]: l for l in batch.get("leaves", [])}
    by_leaf: dict[str, list[dict]] = {}
    for tc in batch.get("tcs", []):
        by_leaf.setdefault(tc["req_id"], []).append(tc)

    result = {}
    for parent, leaf in leaves.items():
        clause = normalize(str(leaf.get("source_clause", "")))
        tcs = by_leaf.get(parent, [])
        texts = {tc["tc_id"]: tc_text(tc) for tc in tcs}
        tc_words = {k: words(v) for k, v in texts.items()}
        tc_named: set[str] = set()
        for v in texts.values():
            tc_named |= named(v)

        # 透鏡 1
        items = []
        for i, item in enumerate(behaviour_items(clause), 1):
            iw = words(item)
            best, score = None, 0.0
            for tid, tw in tc_words.items():
                s = len(iw & tw) / max(1, len(iw))
                if s > score:
                    best, score = tid, s
            residual = sorted(iw - tc_words.get(best, set())) if best else sorted(iw)
            items.append({"n": i, "text": item, "best": best,
                          "score": round(score, 3),
                          "covered": score >= threshold,
                          "residual": residual})

        # R-P127 —— 殘差詞分桶（機械可判者先分，其餘留待人工）
        all_tc_words: set[str] = set()
        for v in tc_words.values():
            all_tc_words |= v
        buckets = {"已由他條涵蓋": [], "候選（須人工判 措詞差異 / 真缺口）": []}
        for x in items:
            for w in x["residual"]:
                key = ("已由他條涵蓋" if w in all_tc_words
                       else "候選（須人工判 措詞差異 / 真缺口）")
                buckets[key].append((x["n"], w))

        # 透鏡 2
        spec_named = named(clause)
        missing = sorted(t for t in spec_named if t not in tc_named)

        result[parent] = {
            "clause_chars": len(clause), "tc_ids": sorted(texts),
            "items": items,
            "n_items": len(items),
            "n_covered": sum(1 for x in items if x["covered"]),
            "n_uncovered": sum(1 for x in items if not x["covered"]),
            "spec_named": sorted(spec_named),
            "named_missing": missing,
            "buckets": {k: sorted(v) for k, v in buckets.items()},
            "n_residual": sum(len(x["residual"]) for x in items),
        }
    return result


def render(res: dict, threshold: float, label: str) -> str:
    out = [f"\n## {label}\n",
           f"\n門檻 `overlap >= {threshold}`（透鏡 1）。\n"]
    tot = cov = 0
    for parent, r in res.items():
        tot += r["n_items"]; cov += r["n_covered"]
        out.append(f"\n### {parent} —— 行為項 {r['n_items']}，"
                   f"已覆蓋 {r['n_covered']}，無對應 **{r['n_uncovered']}**\n\n"
                   f"TC：{', '.join(x[-3:] for x in r['tc_ids'])}\n\n"
                   "| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |\n"
                   "|---|---|---|---|---|---|\n")
        for x in r["items"]:
            out.append(f"| {x['n']} | {x['text'][:78]} | "
                       f"{(x['best'] or '—')[-3:]} | {x['score']:.2f} | "
                       f"{'已覆蓋' if x['covered'] else '**無對應**'} | "
                       f"{'、'.join('`'+w+'`' for w in x['residual']) or '（無）'} |\n")
        out.append(f"\n**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**："
                   f"{'、'.join('`'+t+'`' for t in r['named_missing']) or '（無）'}\n")
        out.append(f"\n**R-P127 殘差詞分桶**（合計 {r['n_residual']}）：\n\n"
                   "| 桶 | 計數 | 例（前 12）|\n|---|---|---|\n")
        for k, v in r["buckets"].items():
            ex = "、".join(f"`{w}`(#{n})" for n, w in v[:12]) or "（無）"
            out.append(f"| {k} | **{len(v)}** | {ex} |\n")
    out.append(f"\n**合計**：行為項 **{tot}**，已覆蓋 **{cov}**，"
               f"無對應 **{tot - cov}**。\n")
    return "".join(out)


def main() -> None:
    threshold = 0.45
    args = sys.argv[1:]
    batch_path = Path(args[args.index("--batch") + 1]) if "--batch" in args else DEFAULT_BATCH
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    res = current = analyse(batch, threshold)

    out = ["# B1 —— 反向涵蓋報告（R-P118）\n",
           "\n> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。\n",
           "> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。\n",
           "> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。\n",
           f"> 產生指令：`python features/power/scripts/reverse_coverage.py"
           f"{'' if batch_path == DEFAULT_BATCH else ' --batch ' + batch_path.name}`\n"]
    out.append(render(current, threshold, f"現況（{batch_path.name}，"
                                          f"{len(batch['tcs'])} 條 TC）"))

    # 驗證條件：對**修補前**之資料（16 包 R-P117 之前）須能重現三項已知缺口
    before = DATA / "b1_before16.json"
    if before.exists() and batch_path == DEFAULT_BATCH:
        prev = json.loads(before.read_text(encoding="utf-8"))
        res_before = analyse(prev, threshold)
        out.append("\n---\n")
        out.append(render(res_before, threshold,
                          f"驗證條件 —— 修補前（`b1_before16.json`，"
                          f"{len(prev['tcs'])} 條 TC，R-P117 之三項缺口尚存）"))

    stem = batch_path.stem.replace("batch_", "").replace("_", "-")
    path = DATA / f"reverse_coverage_{stem}.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes\n")
    for parent, r in current.items():
        print(f"{parent}: 行為項 {r['n_items']}，已覆蓋 {r['n_covered']}，"
              f"無對應 {r['n_uncovered']}")
        for x in r["items"]:
            if not x["covered"]:
                print(f"   無對應 #{x['n']} ({x['score']:.2f}) {x['text'][:76]}")
            elif x["residual"]:
                print(f"   殘差 #{x['n']} ({x['score']:.2f}) 缺 {x['residual']} "
                      f"| {x['text'][:52]}")
        print(f"   透鏡2 未見標的：{r['named_missing']}")
        for k, v in r["buckets"].items():
            print(f"   分桶 {k}: {len(v)}")
            if k.startswith("候選"):
                print(f"      {sorted(set(w for _, w in v))}")


if __name__ == "__main__":
    main()
