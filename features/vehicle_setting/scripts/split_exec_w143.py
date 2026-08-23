"""W-143(2)（77 包 §2）—— 依 W-145 之稽核拆分既有 TC。

拆分軸依 canon §8.2.2：**不同控制實體 → 拆為獨立 TC**；
同一控制元件之多列 ER **維持一條**。

拆出之各條：`split_flag = true`、`split_reason` 記其軸；
`Requirement or Design ID`（leaf_id）同值，Test Case ID 各自遞增（§10.3）。
"""
from __future__ import annotations

import collections
import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
ECHO = re.compile(r"\bis sent\b|\bis accepted\b|\bis recorded\b|completes start-up|"
                  r"^\s*\d+\.\s*PENDING")
ENTITY = {"heated seat": r"heated seat", "vented seat": r"vented seat",
          "heated steering wheel": r"heated steering wheel",
          "head restraint": r"head restraint|headrest",
          "rear camera": r"rear (view )?camera",
          "touchscreen": r"touchscreen|screen off|display state",
          "audio": r"audio|track"}
SCREEN = re.compile(r"Heated\s*/\s*Vented Seats screen", re.I)


def latest():
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(g.items())]


def entities(tc: dict) -> list[str]:
    ents = []
    for line in tc["expected_result"].split("\n"):
        if ECHO.search(line):
            continue
        clean = SCREEN.sub("«screen»", line)
        for name, pat in ENTITY.items():
            if re.search(pat, clean, re.I) and name not in ents:
                ents.append(name)
    return ents


def narrow(text: str, keep: str, drop: list[str]) -> str:
    """把提及多實體之句子窄化為單一實體。"""
    out = []
    for line in text.split("\n"):
        clean = SCREEN.sub("«screen»", line)
        hit = [n for n, p in ENTITY.items() if re.search(p, clean, re.I)]
        if len(hit) >= 2 and keep in hit:
            # `the heated seat, vented seat and heated steering wheel switch …`
            line = re.sub(r"the heated seat, vented seat and heated steering wheel",
                          f"the {keep}", line, flags=re.I)
            line = re.sub(r"All heat and vent switches",
                          f"The {keep} switch", line, flags=re.I)
            for d in drop:
                line = re.sub(rf"\s*(and|,)\s*{ENTITY[d]}[a-z ]*", "", line, flags=re.I)
        out.append(line)
    return "\n".join(out)


def main() -> None:
    aud = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/split_audit.tsv").open(encoding="utf-8"), delimiter="\t")}
    made = []
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        new_tcs, changed = [], False
        for tc in d["tcs"]:
            a = aud.get(tc["leaf_id"], {})
            cur, tgt = int(a.get("current_tc", 1) or 1), int(a.get("target_tc", 1) or 1)
            ents = entities(tc)
            if tgt <= cur or len(ents) < 2:
                new_tcs.append(tc)
                continue
            for i, e in enumerate(ents):
                c = json.loads(json.dumps(tc))
                drop = [x for x in ents if x != e]
                c["test_procedure"] = narrow(c["test_procedure"], e, drop)
                c["expected_result"] = narrow(c["expected_result"], e, drop)
                c["tc_title"] = f"{tc['tc_title']} — {e}"[:110]
                c["split_flag"] = True
                c["split_reason"] = (f"§8.2.2 不同控制實體 → 拆；本條之實體為 {e}"
                                     f"（原條涵蓋 {'、'.join(ents)}）")
                new_tcs.append(c)
                made.append((name, tc["leaf_id"], e))
            changed = True
        if changed:
            d["tcs"] = new_tcs
            d["revision"] = ("W-143(2)（50 輪）：依 W-145 之稽核拆分 —— "
                             "§8.2.2 不同控制實體各為一條")
            (FEAT / "generated" / f"{name}_v{ver + 1}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"**拆出 {len(made)} 條**（原 {len({(b, l) for b, l, _ in made})} 條）")
    for b, l, e in made:
        print(f"  `{b}`  `{l}`  → {e}")


if __name__ == "__main__":
    main()
