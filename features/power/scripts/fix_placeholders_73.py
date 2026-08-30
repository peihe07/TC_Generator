"""73 包 —— 佔位符替換 ＋ `;` 拆步 ＋ G257 拆步（R-P398(b)(c) / R-P366(b)）。

⚠ **執行層自陳之缺陷**：71 包字典套用時，字典之模板值
（`<STATE>` / `<raw>` / `FUNC_STATE_<STATE>`）**被逐字寫入 corpus 而未逐條實例化** ——
R-P396(a) 明載「`<STATE>` = 該 TC ER 所期望之狀態」，本層漏了替換。
71 包「六閘全綠」係量在含佔位符之文字上（佔位符落在 `$…$` 句內，白名單判準看不見）。

本腳本三事：
  1. `<STATE>` / `<raw>` 依該條之 `Apply ENTER_<X>` → `tc_title` / `test_item` 推定並替換；
     **推不出者不猜**（§8.4.1），標 `(站④-2)` 交分析層
  2. Procedure 內之 `; ` 一律拆步（R-P398(c)），ER 對齊
  3. 拆步後重量 G257，**逾限者不逕拆**（見下），據實回報

⚠ **本腳本不做 G257 之拆步。** 首版曾實作，實測其切法會把
`Read the signal $X$ and check that it is <raw> (<STATE>)` 拆為
`Read the signal $X$` ＋ `Check that it is …` 二步 ——
**驗證擁有者失去 `check that`（違 IN §5.5），且 `Check that it is …` 之主詞被孤立**。
其代價大於字數逾限本身，故撤回；逾限步交分析層裁。

用法：
    python features/power/scripts/fix_placeholders_73.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"

# `VAL_ 1470 PowerSts_Telematic`（forms BHCAN2）
RAW = {"Full_Operation": 4, "Full-Operation": 4, "FULL OPERATION": 4,
       "Idle": 3, "IDLE": 3, "Timed": 2, "Standby": 1, "Sleep": 0,
       "Bench": 6, "Partial_Operation": 7, "Partial Operation": 7,
       "Partial-Operation": 7, "Logistic_On": 5}
CANON = {"Full-Operation": "Full_Operation", "FULL OPERATION": "Full_Operation",
         "IDLE": "Idle", "Partial Operation": "Partial_Operation",
         "Partial-Operation": "Partial_Operation"}
ENTER2STATE = {"FULL_OPERATION": "Full_Operation", "IDLE": "Idle", "TIMED": "Timed",
               "STANDBY": "Standby", "SLEEP": "Sleep", "BENCH": "Bench",
               "PARTIAL_OPERATION": "Partial_Operation", "INIT": "INIT",
               "LOGISTIC_ON": "Logistic_On"}
FIELDS = ("pre_conditions", "input_test_data", "test_procedure", "expected_result")
TO_CLAUSE = re.compile(r"\bto\s+\w", re.I)


def derive(tc: dict) -> str | None:
    src = " ".join((tc.get(f) or "") for f in ("pre_conditions", "test_procedure"))
    m = re.search(r"Apply ENTER_([A-Z_]+)", src)
    if m and m.group(1) in ENTER2STATE:
        return ENTER2STATE[m.group(1)]
    txt = (tc.get("tc_title") or "") + " " + (tc.get("test_item") or "")
    for s in RAW:
        if s in txt:
            return CANON.get(s, s)
    return None


def steps(s: str) -> list[str]:
    return [re.sub(r"^\s*\d+\.\s*", "", l).strip()
            for l in (s or "").splitlines() if re.match(r"^\s*\d+\.", l)]


def number(items: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))


def limit(step: str, is_last: bool) -> int:
    return 18 if (is_last or TO_CLAUSE.search(step)) else 12


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    subst = unresolved = semi = split_n = 0
    for p, d in files.items():
        hit = False
        for tc in d["tcs"]:
            note = []
            # 1) 佔位符
            if any("<STATE>" in (tc.get(f) or "") or "<raw>" in (tc.get(f) or "")
                   for f in FIELDS):
                st = derive(tc)
                if st and st in RAW:
                    for f in FIELDS:
                        v = tc.get(f) or ""
                        if v:
                            tc[f] = (v.replace("<raw>", str(RAW[st]))
                                     .replace("<STATE>", st))
                    subst += 1
                    note.append(f"佔位符依本條推定之狀態 `{st}`（raw {RAW[st]}）替換")
                    hit = True
                else:
                    unresolved += 1
                    if "(站④-2)" not in (tc.get("remarks") or ""):
                        tc["remarks"] = ((tc.get("remarks") or "").strip()
                                         + " (站④-2：`<STATE>` 未能由本條推定，待分析層指定)")
                    hit = True
            # 2) Procedure 之 `;` 拆步（R-P398(c)）
            ps, es = steps(tc.get("test_procedure") or ""), steps(tc.get("expected_result") or "")
            if any("; " in s for s in ps):
                np_, ne = [], []
                for i, s in enumerate(ps):
                    parts = [x.strip() for x in s.split("; ") if x.strip()]
                    np_ += parts
                    e = es[i] if i < len(es) else ""
                    eparts = [x.strip() for x in e.split("; ") if x.strip()]
                    ne += eparts if len(eparts) == len(parts) else [e] * len(parts)
                tc["test_procedure"], tc["expected_result"] = number(np_), number(ne)
                semi += 1
                note.append("Procedure 之 `;` 串接依 R-P398(c) 拆為逐步，ER 對齊")
                hit = True
            # 3) G257 之拆步 —— **不做**（見檔頭）。逾限步由 G257 回報，交分析層裁。
            if note:
                tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
                    "\n\n**73 包補正（R-P398(b)(c) / R-P366(b)）**：" + "；".join(note) + "。")
        if hit and not dry:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"佔位符替換 {subst} 條；**推不出而標 (站④-2) {unresolved} 條**；"
          f"`;` 拆步 {semi} 條（G257 之拆步不做，見檔頭）")
    if dry:
        print("（dry-run）")


if __name__ == "__main__":
    main()
