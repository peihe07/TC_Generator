#!/usr/bin/env python3
"""下放包 10a：PM 整批回修之編輯集產生器。

本包實際執行 A1／A6／A4，以及 A2／A3 之 **can／internal 兩類**。
proxi／free／can+free 三類與 A5 因需內容判斷或前置資料不足而保留，
理由與清單見上繳 10a。
"""

from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint036 as L                                    # noqa: E402
import signals as S                                    # noqa: E402
import inline as I                                     # noqa: E402

SANDBOX = ROOT / "features/power/sandbox/b10"
NUM = re.compile(r"^(\s*)(\d+)\.\s*(.*)$")
NOT_EQUAL = re.compile(r"^(a value other than|not\b|greater than|less than)")
DRIVE_TRIPLET = re.compile(
    r"^(\s*\d+\.\s*)Drive\s+(.+?)\s+from\s+\"([^\"]+)\"\s+to\s+\"([^\"]+)\"\s*$")


def renumber(lines: list[str]) -> list[str]:
    """步驟重新編號，維持原有縮排。"""
    out, n = [], 0
    for line in lines:
        m = NUM.match(line)
        if m:
            n += 1
            out.append(f"{m.group(1)}{n}. {m.group(3)}")
        else:
            out.append(line)
    return out


def split_can_step(line: str) -> tuple[list[str], list[str]] | None:
    """`Drive <三件組> from "A" to "B"` → 兩則 (a) 式步驟＋兩則 (b) 式 ER。"""
    m = DRIVE_TRIPLET.match(line)
    if not m:
        return None
    dotted = S.to_dotted(m.group(2)).strip()
    if dotted not in S.VAL_LABELS:
        return None
    raws = [S.resolve_raw(dotted, m.group(3)), S.resolve_raw(dotted, m.group(4))]
    if any(r is None for r in raws):
        return None
    return ([f"1. {S.send_step(dotted, r)}" for r in raws],
            [f"1. {S.er_sent(dotted, r)}" for r in raws])


def main() -> None:
    rows = json.loads((SANDBOX / "rows.json").read_text(encoding="utf-8"))
    changes: dict[int, dict[str, str]] = collections.defaultdict(dict)
    log = {"a1_prose": [], "a1_split": [], "a2_inlined": [],
           "a4_proxi": [], "a4_held": [], "held": []}

    for r in rows:
        pre, proc, er, inp = r["pre"], r["proc"], r["er"], r["input"]

        # ── A1／A6：proc 之 transition 型拆步（ER 同步增列）──
        proc_lines, er_lines = proc.split("\n"), er.split("\n")
        new_proc: list[str] = []
        inserted_at: list[int] = []
        step_no = 0
        for line in proc_lines:
            if NUM.match(line):
                step_no += 1
            split = split_can_step(line)
            if split:
                new_proc.extend(split[0])
                inserted_at.append((step_no, split[1]))
                log["a1_split"].append(r["row"])
            else:
                new_proc.append(line)
        if inserted_at:
            new_er, seen = [], 0
            for line in er_lines:
                if NUM.match(line):
                    seen += 1
                    match = next((x for x in inserted_at if x[0] == seen), None)
                    if match:
                        new_er.append(match[1][0])          # 新增之 (b) 式 ER
                        new_er.append(line)                 # 原 ER 保留於第二步
                        continue
                new_er.append(line)
            er_lines = new_er
        proc_lines = new_proc

        # ── A2／A3：can／internal 兩類之內聯 ──
        if inp.strip() != "NA":
            lines = [x for x in inp.split("\n") if x.strip()]
            rendered = [I.render(x) for x in lines]
            kinds = {k for k, _ in rendered} if all(rendered) else {"?"}
            if all(rendered) and kinds <= {"can", "internal"} and len(lines) == 1:
                kind, values = rendered[0]
                idx = next((i for i, x in enumerate(proc_lines)
                            if "listed in Input Test Data" in x), None)
                if idx is None:
                    log["held"].append({"row": r["row"], "why": "回指行不在 proc"})
                else:
                    m = NUM.match(proc_lines[idx])
                    if kind == "can":
                        body = [f"Send CAN: {v}" for v in values]
                    else:
                        verb = "Drive" if " from " in values[0] else "Set"
                        body = [f"{verb} {values[0]}"]
                    proc_lines[idx:idx + 1] = [f"{m.group(1)}1. {b}" for b in body]
                    if len(body) > 1:                        # 拆步 → ER 同步
                        pos = int(m.group(2))
                        new_er, seen = [], 0
                        for line in er_lines:
                            if NUM.match(line):
                                seen += 1
                                if seen == pos:
                                    sig = values[0].split(" = ")[0]
                                    new_er.append(f"1. {values[0]} is sent")
                            new_er.append(line)
                        er_lines = new_er
                    changes[r["row"]]["input"] = "NA"
                    log["a2_inlined"].append({"row": r["row"], "kind": kind})
            else:
                log["held"].append({"row": r["row"],
                                    "why": "／".join(sorted(kinds)) + " 類，需內容判斷"})

        # ── A1：pre／proc／er 之散文型三件組（僅換記法）──
        pre_new = S.to_dotted(pre)
        proc_lines = [S.to_dotted(x) for x in proc_lines]
        er_lines = [S.to_dotted(x) for x in er_lines]
        if pre_new != pre:
            log["a1_prose"].append({"row": r["row"], "field": "pre"})

        # ── A4：PROXI 前綴與 `$` 式（Pre-Condition，R-1 v2(c)）──
        # 僅轉「明確等值」之行。`reads a value other than …`、`is marked as …`、
        # `greater than …` 等非等值述語無法以 `PROXI $X$ = <值>` 表達，
        # 硬轉即改變語意，故保留原句並登記待判。
        pre_lines = []
        for line in pre_new.split("\n"):
            if "$" not in line or "PROXI" in line:
                pre_lines.append(line)
                continue
            converted = None
            eq = re.match(r"^(\s*\d+\.\s*)(\$[^$]+\$)\s*(?:=|reads)\s+(.+)$", line)
            carries = re.match(
                r"^(\s*\d+\.\s*)The ETM carries\s+(\$[^$]+\$)\s+equal to\s+(.+)$", line)
            if eq and not NOT_EQUAL.search(eq.group(3)):
                converted = f"{eq.group(1)}PROXI {eq.group(2)} = {eq.group(3)}"
            elif carries:
                converted = f"{carries.group(1)}PROXI {carries.group(2)} = {carries.group(3)}"
            if converted:
                pre_lines.append(converted)
                log["a4_proxi"].append({"row": r["row"], "was": line.strip()[:70]})
            else:
                pre_lines.append(line)
                if re.match(r"^\s*\d+\.\s*\$[^$]+\$", line) or "The ETM carries" in line:
                    log["a4_held"].append({"row": r["row"], "line": line.strip()[:70]})
        pre_new = "\n".join(pre_lines)

        proc_new = "\n".join(renumber(proc_lines))
        er_new = "\n".join(renumber(er_lines))
        for key, before, after in (("pre", pre, pre_new), ("proc", proc, proc_new),
                                   ("er", er, er_new)):
            if after != before:
                changes[r["row"]][key] = after

    payload = {"changes": {str(k): v for k, v in sorted(changes.items())}, "log": log}
    (SANDBOX / "edits.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"變動列 {len(changes)}｜格 {sum(len(v) for v in changes.values())}")
    print(f"  A1 散文換記法 {len(log['a1_prose'])}｜A1 拆步 {len(set(log['a1_split']))} 列")
    print(f"  A2 內聯 {len(log['a2_inlined'])} 列"
          f"（{dict(collections.Counter(x['kind'] for x in log['a2_inlined']))}）")
    print(f"  A4 PROXI 轉換 {len(log['a4_proxi'])} 行｜非等值述語保留 {len(log['a4_held'])} 行")
    print(f"  保留待判 {len(log['held'])} 列"
          f"（{dict(collections.Counter(x['why'] for x in log['held']))}）")


if __name__ == "__main__":
    main()
