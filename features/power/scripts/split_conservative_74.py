"""G257 拆步（保守版）—— Pei 2026-08-30 授權執行層直接處置。

73 包之激進版已撤回（`split_steps_73.py`）：其在**裸** ` and check that ` 處切，
把 `Read the signal $X$ and check that it is <raw> (<STATE>)` 這個
**R-P354(a) 所定之原子**拆散，驗證擁有者失去 `check that`（違 IN §5.5），G245 由 0 升至 60。

本版之差別：**只在帶逗號之並列連接處切**，故第二段**必自帶動詞與 check**，
`Read … and check that …` 之原子不被拆。

切點（依序，皆為並列而非動賓）：
    ` —— `（`PENDING` 標記與其動作之間）
    `, and check that `　→ 第二段補 `Check that `
    `, and read `／`, then read `　→ 第二段補 `Read `
    `, then `／`, and `

**不刪任何字**（R-P366(b) 明文）。切不動而仍逾限者原樣保留，由 G257 回報。

用法：
    python features/power/scripts/split_conservative_74.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from g257_steplen_73 import limit  # noqa: E402  —— 判準與 G257 同源，避免二源漂移

TO_CLAUSE = re.compile(r"\bto\s+\w", re.I)
# ⚠ 一律帶逗號 —— 裸 ` and check that ` **不切**（否則拆散 R-P354(a) 之原子）
SEPS = [(" —— ", ""), (", and check that ", "Check that "),
        (", and read ", "Read "), (", then read ", "Read "),
        (", then ", ""), (", and ", "")]


def steps(s: str) -> list[str]:
    return [re.sub(r"^\s*\d+\.\s*", "", l).strip()
            for l in (s or "").splitlines() if re.match(r"^\s*\d+\.", l)]


def number(items):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1))


def cut(step: str):
    for sep, prefix in SEPS:
        i = step.find(sep)
        if i <= 0:
            continue
        head, tail = step[:i].strip(), step[i + len(sep):].strip()
        if not head or not tail:
            continue
        return [head, (prefix + tail) if prefix else tail[:1].upper() + tail[1:]]
    return None


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    touched, stuck = 0, []
    for p, d in files.items():
        hit = False
        for tc in d["tcs"]:
            ps = steps(tc.get("test_procedure") or "")
            es = steps(tc.get("expected_result") or "")
            for _ in range(6):
                np_, ne, changed = [], [], False
                for i, s in enumerate(ps):
                    e = es[i] if i < len(es) else ""
                    if len(s.split()) > limit(s, i == len(ps) - 1):
                        parts = cut(s)
                        if parts:
                            np_ += parts
                            ne += [e, e]
                            changed = True
                            continue
                    np_.append(s)
                    ne.append(e)
                ps, es = np_, ne
                if not changed:
                    break
            new_p = number(ps)
            if new_p != (tc.get("test_procedure") or ""):
                tc["test_procedure"], tc["expected_result"] = new_p, number(es)
                tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
                    "\n\n**G257 拆步（保守版，74 包）**：逾 IN §5.2 之步"
                    "**只在帶逗號之並列連接處**切，故 `Read … and check that …` 之原子"
                    "（R-P354(a)）不被拆、§5.5 之驗證擁有者保有 `check that`；"
                    "**未刪任何字**（R-P366(b)）；ER 逐步對齊。")
                touched += 1
                hit = True
            for i, s in enumerate(ps):
                if len(s.split()) > limit(s, i == len(ps) - 1):
                    stuck.append((tc["tc_id"], i + 1, len(s.split()),
                                  limit(s, i == len(ps) - 1), s[:80]))
        if hit and not dry:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"拆步 {touched} 條；**切不動而仍逾限 {len(stuck)} 步**")
    for t in stuck[:10]:
        print(f"   {t[0][-3:]} 步{t[1]} {t[2]}/{t[3]} 字 | {t[4]}")
    if dry:
        print("（dry-run）")


if __name__ == "__main__":
    main()
