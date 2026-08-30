"""69 包 §H 第 2 步 —— 已改寫 75 條之站④ 目視包（R-P394(d)）。

`sandbox/b55/pm_55.xlsx` 尚未生成，故先以現行 batch JSON 出 Markdown：
每條列 tc_id、req_id、五欄、Remarks。**不判定、不摘要**（逐字）。

另出 §H 第 4 步之丁案候選 `data/pattern_d_candidates_69.md` ——
R-P376(a) 三要件之機器篩，**不逕改**（R-P394(b) / §I）。

用法：
    python features/power/scripts/reviewed_75_69.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
TEXT = ROOT / "features/power/data/textlayer"
OUT = ROOT / "features/power/data/reviewed_75_69.md"
OUT_D = ROOT / "features/power/data/pattern_d_candidates_69.md"

MARKS = ("R-P386 第一批", "R-P386 第二批", "R-P376 丁案", "R-P383", "R-P393(c)")
FIVE = ("test_item", "pre_conditions", "input_test_data",
        "test_procedure", "expected_result")
ANCHOR = re.compile(r"^(49\d{5}):")
PAT_INT = re.compile(r"\b([A-Za-z][A-Za-z0-9_]*)\.(Info|Req)\b|\b(RemStartFail)\b")
SIGNAL = re.compile(r"\$[A-Z][A-Z0-9_]*\.[A-Za-z0-9_]+\$")


def leaf_anchors() -> dict[str, list[str]]:
    """`leaf` → 錨點 ObjectID（`data/layer3_full.tsv`，G94 / G99 之來源）。

    現行 corpus 之 `specification_reference` 為 `{檔名}_{章節}` 而無 ObjectID
    （A-PW344），`reasoning_note` 亦非每條皆載 —— 同 `g252_six_63.py` 之取徑。
    """
    import csv
    out: dict[str, list[str]] = {}
    with (ROOT / "features/power/data/layer3_full.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out.setdefault(row["leaf"], []).extend(
                i.strip() for i in (row.get("item_ids") or "").split(",") if i.strip())
    return out


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


def main() -> None:
    cur = rm.load_current()
    done = [t for t in cur
            if any(x in (t.get("remarks") or "") for x in MARKS)]
    done.sort(key=lambda t: t["tc_id"])

    md = [
        "# 已改寫 75 條 —— 站④ 目視包（69 包 / R-P394(d)）",
        "",
        "> `sandbox/b55/pm_55.xlsx` 尚未生成，本檔先以現行 `generated/batch_*.json` 出。",
        "> **逐字，不判定、不摘要。** 抽查結果可隨時叫停 B5（R-P394(d)）。",
        "",
        f"> 共 **{len(done)}** 條。改寫依據見各條 Remarks 與 `reasoning_note`。",
        "",
        "| # | tc_id | req_id | 改寫依據（Remarks）|",
        "|---|---|---|---|",
    ]
    for i, t in enumerate(done, 1):
        md.append(f"| {i} | `{t['tc_id']}` | `{t['req_id']}` | "
                  f"{(t.get('remarks') or '').strip()} |")
    md.append("")
    for t in done:
        md += [f"## `{t['tc_id']}`　`{t['req_id']}`　{t.get('tc_title', '')}", ""]
        for f in FIVE:
            label = {"test_item": "Test Item", "pre_conditions": "Pre-Conditions",
                     "input_test_data": "Input Test Data",
                     "test_procedure": "Test procedure",
                     "expected_result": "Expected Result"}[f]
            md += [f"**{label}**", "", "```",
                   (t.get(f) or "").replace("\xa0", " "), "```", ""]
        md += ["**Remarks**", "", "```", (t.get("remarks") or "").strip(), "```", ""]
    OUT.write_text("\n".join(md))
    print(f"目視包 {len(done)} 條 → {OUT.relative_to(ROOT)}")

    # ── §H 第 4 步：丁案候選（R-P376(a) 三要件之機器篩）──
    paras = paragraphs()
    anchors = leaf_anchors()
    und = [t for t in cur if t not in done]
    rows = []
    for t in und:
        ints = set()
        for f in FIVE:
            for m in PAT_INT.finditer(t.get(f) or ""):
                ints.add((m.group(1) + "." + m.group(2)) if m.group(1) else m.group(3))
        ints -= {"TLM_Status.Info", "LTM_OperationalModeSts.Info"}
        if not ints:
            continue
        oids = sorted(set(re.findall(r"\b(49\d{5})\b", t.get("reasoning_note") or ""))
                      | set(anchors.get(t["req_id"], [])))
        hit = []
        for oid in oids:
            body = paras.get(oid, "")
            if not body:
                continue
            # (i) 因果同段落：段落同時含 DBC 型訊號名與內部變數
            has_sig = bool(re.search(r"STATUS_[A-Z0-9_]+\.[A-Za-z0-9_]+", body))
            has_int = any(n.split(".")[0] in body for n in ints)
            has_state = "Telematic_Power" in body or "TLM_Status" in body
            if has_sig and has_int and has_state:
                hit.append(oid)
        if hit:
            rows.append((t["tc_id"], t["req_id"], sorted(ints), hit))

    dmd = [
        "# 丁案候選（69 包 §H 第 4 步 / R-P394(b)）",
        "",
        "> **機器篩，不逕改**（R-P394(b) / §I）。由分析層核 R-P376(a) 三要件後始得施作。",
        "",
        "> 篩法（保守）：未改寫之 212 條中，其錨點（`reasoning_note` ∪ `layer3_full.tsv` 之
> `leaf → item_ids`）之段落**同時含**",
        "> (1) `STATUS_*.*` 型 DBC 訊號名、(2) 該條所用之內部變數名、",
        "> (3) `TLM_Status` / `Telematic_Power`（下游狀態）—— 即「因與果同段落」之機器近似。",
        "> **三要件之 (ii)(iii) 仍須人核**：上游是否確為可送之 `$MESSAGE.Signal$`、",
        "> 下游是否確落白名單。",
        "",
        f"## 候選 **{len(rows)}** 條",
        "",
        "| tc_id | req_id | 內部變數 | 同段落錨點 |",
        "|---|---|---|---|",
    ]
    for tid, rid, ints, hit in rows:
        dmd.append(f"| `{tid}` | `{rid}` | {'、'.join(f'`{i}`' for i in ints)} | "
                   f"{'、'.join(f'`CFTS009-{h}`' for h in hit)} |")
    dmd.append("")
    OUT_D.write_text("\n".join(dmd))
    print(f"丁案候選 {len(rows)} 條 → {OUT_D.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
