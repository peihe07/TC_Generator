"""R-P395(a) —— 複合觀察目標之原子 token 供料（70 包 §H 第 3 步）。

母體：三閘未歸零之條（G245 家族 A 上界 ∪ G250 `Read the HU mode/state`
∪ G247 Proc/ER 非 PENDING 之內部訊號句）。

取 `Read <X> …` / `Check that <X> …` 之 `<X>`，以 ` and ` / ` against ` / `, `
拆為**原子 token**，全案去重。

**不判定、不預填代理量**（R-P395(a) / §I）；
**不合併同義**（`HU mode` 與 `TLM state` 為二 token，是否同物由分析層判）。

用法：
    python features/power/scripts/composite_tokens_70.py
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
TEXT = ROOT / "features/power/data/textlayer"
OUT = ROOT / "features/power/data/composite_tokens_70.md"

READ = re.compile(r"^\s*\d*\.?\s*(?:Read|Check that)\s+(.*?)"
                  r"(?:\s+(?:and check that|to check).*)?$", re.I)
SPLIT = re.compile(r"\s+and\s+|\s+against\s+|,\s*")
ANCHOR = re.compile(r"^(49\d{5}):")
INT = re.compile(r"\b([A-Za-z0-9_]+\.(?:Info|Req))\b|\b(RemStartFail)\b")


def paragraphs() -> dict[str, str]:
    out = {}
    for src in ("cfts009", "cfts010", "sys3"):
        f = TEXT / f"{src}_plain.txt"
        if not f.exists():
            continue
        lines = f.read_text(errors="ignore").splitlines()
        for i, ln in enumerate(lines):
            m = ANCHOR.match(ln)
            if m:
                body = []
                for nxt in lines[i + 1:]:
                    if ANCHOR.match(nxt) or re.match(r"^\d+(\.\d+)* ", nxt):
                        break
                    body.append(nxt)
                out[m.group(1)] = "\n".join(body).strip()
    return out


def leaf_anchors() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    with (ROOT / "features/power/data/layer3_full.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out.setdefault(row["leaf"], []).extend(
                i.strip() for i in (row.get("item_ids") or "").split(",") if i.strip())
    return out


def main() -> None:
    cur = rm.load_current()
    paras, anchors = paragraphs(), leaf_anchors()

    # 母體：三閘未歸零者
    pool = []
    for t in cur:
        g245 = rm.DETECTORS["A_upper"](t)
        g250 = rm.DETECTORS["G"](t)
        g247 = any(INT.search(l) and "PENDING" not in l
                   for f in ("test_procedure", "expected_result")
                   for l in (t.get(f) or "").splitlines())
        if g245 or g250 or g247:
            pool.append(t)

    tok_tc: defaultdict = defaultdict(list)
    tok_n: defaultdict = defaultdict(int)
    for t in pool:
        for f in ("test_procedure", "expected_result"):
            for line in (t.get(f) or "").splitlines():
                m = READ.match(line)
                if not m:
                    continue
                x = m.group(1).strip()
                if rm.whitelisted(x) and not SPLIT.search(x):
                    continue
                for tok in SPLIT.split(x):
                    tok = re.sub(r"^(the|a|an)\s+", "", tok.strip(), flags=re.I)
                    tok = tok.strip(" .,;:")
                    if not tok or len(tok) < 3:
                        continue
                    if rm.whitelisted(tok):
                        continue          # 已為白名單之原子，不入字典母體
                    tok_n[tok] += 1
                    if t["tc_id"] not in tok_tc[tok]:
                        tok_tc[tok].append(t["tc_id"])

    # 既裁之解 —— **非本層指定之代理量**，僅引既有條文供分析層對照（§I 不預填）
    KNOWN = {
        "TLM_Status.Info": ("`$STATUS_TELEMATIC.PowerSts_Telematic$`", "R-P368 段 1–3 解得"),
        "$Telematic_Power$": ("`$STATUS_TELEMATIC.PowerSts_Telematic$`",
                              "R-P368；LID r2069 `Telematic_Power` 逐字"),
        "$Radio_Theme$": ("`$RADIO_B4.Radio_Theme$`", "R-P368；LID r1531"),
        "$PowerMode$": ("`$STATUS_BH_BCM2.CmdIgnSts$`", "R-P385(b) 強候選"),
        "LTM_OperationalModeSts.Info": ("`$STATUS_BH_BCM1.OperationalModeSts$`",
                                        "R-P368；LID r1286，DR-PW26(1a) 待確認"),
        "shown Splash Screen": ('`"Splash Screen"`', "R-P387(b)；`4941453` 之 `(*)` 註腳"),
    }

    md = [
        "# 複合觀察目標之原子 token（70 包 / R-P395(a)）",
        "",
        "> **執行層供料，不判定、不預填代理量**（R-P395(a) / §I）。",
        "> **不合併同義** —— `HU mode` 與 `TLM state` 為二 token，是否同物由分析層判（§I）。",
        "",
        "> 母體：三閘未歸零之條（G245 家族 A 上界 ∪ G250 `Read the HU mode/state`",
        f"> ∪ G247 Proc/ER 非 PENDING 之內部訊號句）＝ **{len(pool)}** 條。",
        "> 拆分符：` and ` / ` against ` / `, `。**已為白名單之原子不入母體**",
        "> （`$MESSAGE.Signal$`、引號具名元件、音訊詞、log 詞）。",
        "",
        f"## 相異 token **{len(tok_n)}** 個（出現 {sum(tok_n.values())} 次）",
        "",
        "> 末欄「既裁之解」**非本層指定之代理量**，僅引**既有條文**供分析層對照；",
        "> 空白者即無既裁，須於 71 包裁（R-P395(b)）。",
        "",
        "| token | 出現 | TC 數 | tc_id（前 8）| 代表錨點 | 既裁之解（引條文，非本層指定）|",
        "|---|---|---|---|---|---|",
    ]
    reps = {}
    for tok, n in sorted(tok_n.items(), key=lambda kv: -kv[1]):
        tcs = tok_tc[tok]
        rep = ""
        for tid in tcs:
            t = next(x for x in cur if x["tc_id"] == tid)
            oids = sorted(set(re.findall(r"\b(49\d{5})\b", t.get("reasoning_note") or ""))
                          | set(anchors.get(t["req_id"], [])))
            if oids:
                rep = oids[0]
                break
        reps[tok] = rep
        kn = KNOWN.get(tok)
        md.append(f"| `{tok}` | {n} | {len(tcs)} | "
                  f"{'、'.join(t[-3:] for t in tcs[:8])} | "
                  f"{'`CFTS009-' + rep + '`' if rep else '—'} | "
                  f"{kn[0] + '（' + kn[1] + '）' if kn else '—'} |")
    md.append("")
    md += ["## 代表錨點段落全文（逐字，供分析層建字典時引用）", ""]
    seen = set()
    for tok, rep in reps.items():
        if not rep or rep in seen:
            continue
        seen.add(rep)
        md += [f"### `CFTS009-{rep}`", "", "```",
               paras.get(rep, "（文字層查無該 ObjectID）").replace("\xa0", " "),
               "```", ""]
    OUT.write_text("\n".join(md))
    print(f"母體 {len(pool)} 條；相異 token {len(tok_n)}；"
          f"代表錨點 {len(seen)} 個 → {OUT.relative_to(ROOT)}")
    print("\n出現次數前 20：")
    for tok, n in sorted(tok_n.items(), key=lambda kv: -kv[1])[:20]:
        print(f"  {n:4d}  {tok[:70]}")


if __name__ == "__main__":
    main()
