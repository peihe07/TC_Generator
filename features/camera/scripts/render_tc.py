"""TC json -> 同名 .md（決定式重生）。

json 為真本；.md 為其可讀投影。本工具之輸出於 A 本既有 240 檔上逐位元相符
（`--verify` 即施該比對），故可安全用於 B 本之生成。

    python3 features/camera/scripts/render_tc.py <目錄> [...]        # 重生
    python3 features/camera/scripts/render_tc.py --verify <目錄> [...]  # 只比對
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

VM_ORDER = ["HDCC27", "DT27", "VF(ProMaster)637", "Commander (598)",
            "Regengade (5210)", "Toro(2261)", "Fastack (376)"]


def render(doc: dict) -> str:
    tc = doc["tcs"][0]
    book = "SYS1" if doc["req_id"].startswith("SWE1-") else "SYS2"
    vm = "｜".join(f"{k}={doc['vehicle_model'][k]}" for k in VM_ORDER)
    spec = "`／`".join(tc["specification_reference"].split("\n"))
    out = [
        f"# {doc['tc_id']} — {doc['req_id']}",
        "",
        f"- **Test Group**：{doc['test_group']}｜**Test Set**：{doc['test_set']}",
        f"- **Vehicle Model**：{vm}",
        f"- **priority**：{tc['priority']}｜**design_method**：{tc['design_method']}",
        f"- **specification_reference**：`{spec}`（來源列 `{doc['source_object_id']}`）",
        "",
        f"## test_item 上半（verbatim，{book} 逐字）",
        "",
        f"> {doc['test_item_verbatim']}",
        "",
        "## reasoning",
        "",
        doc["reasoning"],
        "",
        "## pre_conditions",
        "",
        "```",
        tc["pre_conditions"],
        "```",
        "",
        "## input_test_data",
        "",
    ]
    itd = tc["input_test_data"]
    out += [f"`{itd}`"] if "\n" not in itd else ["```", itd, "```"]
    out += ["", "## test_procedure", "", "```", tc["test_procedure"], "```",
            "", "## expected_result", "", "```", tc["expected_result"], "```", ""]
    if doc.get("remarks"):
        out += ["## remarks", "", doc["remarks"], ""]
    return "\n".join(out)


def main() -> None:
    args = sys.argv[1:]
    verify = args and args[0] == "--verify"
    dirs = [Path(a) for a in (args[1:] if verify else args)]
    same = diff = written = 0
    for d in dirs:
        for p in sorted(d.glob("NR1L-*.json")):
            md = p.with_suffix(".md")
            txt = render(json.loads(p.read_text(encoding="utf-8")))
            if verify:
                old = md.read_text(encoding="utf-8") if md.exists() else None
                if old == txt:
                    same += 1
                else:
                    diff += 1
                    print(f"  [異] {md}")
            else:
                md.write_text(txt, encoding="utf-8")
                written += 1
    print(f"逐位元相符 {same}｜相異 {diff}" if verify else f"重生 {written} 檔")
    sys.exit(1 if diff else 0)


if __name__ == "__main__":
    main()
