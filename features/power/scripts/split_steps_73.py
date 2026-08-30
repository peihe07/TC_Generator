"""**已撤回，不使用**（73 包）。

本腳本曾為 G257 之第二輪拆步，實測其切法會把
`Read the signal $X$ and check that it is <raw> (<STATE>)` 拆為
`Read the signal $X$` ＋ `Check that it is …` 二步 —— **驗證擁有者失去 `check that`**
（違 IN §5.5），且 `Check that it is …` 之主詞被孤立；實測後 G245 由 0 升至 60。
**代價大於字數逾限本身**，故撤回。逾限步改由 G257 回報，交分析層裁。
保留原碼於下供覆核（R-P329 之慣例：不刪）。
"""

# """G257 第二輪拆步（73 包 / R-P366(b)）。
#
# `fix_placeholders_73.py` 之 `split_long` 只切一次且分隔符少，餘 126 步逾限。
# 本腳本**反覆**在連接處切，直至無可切或已達上限；**不刪任何字**（R-P366(b) 明文）。
#
# 切點（依序試，皆為語意完整之連接處）：
#     ` —— `（PENDING 標記與其動作之間）
#     ` and check that `／`, and check that `
#     `, and read `／` and read `
#     `, then read `／`, then `
#     `, and `
#
# 切不動而仍逾限者**原樣保留**並回報 —— 交分析層裁（不得為湊字數刪資料）。
#
# 用法：
#     python features/power/scripts/split_steps_73.py [--dry-run]
# """
#
# from __future__ import annotations
#
# import json
# import re
# import sys
# from pathlib import Path
#
# ROOT = Path(__file__).resolve().parents[3]
# BATCHES = ROOT / "features/power/generated"
# TO_CLAUSE = re.compile(r"\bto\s+\w", re.I)
# SEPS = [" —— ", ", and check that ", " and check that ", ", and read ", " and read ",
#         ", then read ", ", then ", ", and "]
#
#
# def steps(s: str) -> list[str]:
#     return [re.sub(r"^\s*\d+\.\s*", "", l).strip()
#             for l in (s or "").splitlines() if re.match(r"^\s*\d+\.", l)]
#
#
# def number(items):
#     return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))
#
#
# def limit(step: str, is_last: bool) -> int:
#     return 18 if (is_last or TO_CLAUSE.search(step)) else 12
#
#
# def cut(step: str) -> list[str] | None:
#     for sep in SEPS:
#         i = step.find(sep)
#         if i <= 0:
#             continue
#         head, tail = step[:i].strip(), step[i + len(sep):].strip()
#         if not head or not tail:
#             continue
#         if sep.strip(", ") == "and check that":
#             tail = "Check that " + tail
#         elif sep.strip(", ") in ("and read", "then read"):
#             tail = "Read " + tail
#         return [head, tail]
#     return None
#
#
# def main() -> None:
#     dry = "--dry-run" in sys.argv
#     files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
#     touched = stuck = 0
#     stuck_list = []
#     for p, d in files.items():
#         hit = False
#         for tc in d["tcs"]:
#             ps, es = steps(tc.get("test_procedure") or ""), steps(tc.get("expected_result") or "")
#             changed = True
#             rounds = 0
#             while changed and rounds < 6:
#                 changed, rounds = False, rounds + 1
#                 np_, ne = [], []
#                 for i, s in enumerate(ps):
#                     e = es[i] if i < len(es) else ""
#                     if len(s.split()) > limit(s, i == len(ps) - 1):
#                         parts = cut(s)
#                         if parts:
#                             np_ += parts
#                             ne += [e, e]
#                             changed = True
#                             continue
#                     np_.append(s)
#                     ne.append(e)
#                 ps, es = np_, ne
#             new_p, new_e = number(ps), number(es)
#             if new_p != (tc.get("test_procedure") or ""):
#                 tc["test_procedure"], tc["expected_result"] = new_p, new_e
#                 tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
#                     "\n\n**G257 第二輪拆步（73 包 / R-P366(b)）**：逾 IN §5.2 之步"
#                     "於語意連接處反覆切分，**未刪任何字**；ER 逐步對齊。")
#                 touched += 1
#                 hit = True
#             for i, s in enumerate(ps):
#                 if len(s.split()) > limit(s, i == len(ps) - 1):
#                     stuck += 1
#                     stuck_list.append((tc["tc_id"], i + 1, len(s.split()), s[:70]))
#         if hit and not dry:
#             p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
#     print(f"再拆 {touched} 條；**切不動而仍逾限 {stuck} 步**")
#     for t in stuck_list[:12]:
#         print(f"   {t[0][-3:]} 步{t[1]} {t[2]} 字 | {t[3]}")
#     if dry:
#         print("（dry-run）")
#
#
# if __name__ == "__main__":
#     main()
