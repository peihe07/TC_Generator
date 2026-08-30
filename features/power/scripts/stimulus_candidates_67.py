"""R-P390 —— 刺激訊號候選供料（67 包 §H 第 3 步）。

規格只述「有 chime」「ICS 可用」而未指名訊號，屬**測試刺激之設計選擇**，
非規格名之識別，R-P368(b) 之「逐字」要件不適用；
但仍不得憑訊號名語意擇定（R-P390(b)）。

執行層之職：**逐候選列 `MESSAGE.Signal` / `CM_` 註解全文 / 發送·接收節點 / `VAL_`**，
**不擇定**。分析層以 `CM_` 是否明述該功能擇定；`CM_` 無明述者不選；全無者開 DR。

用法：
    python features/power/scripts/stimulus_candidates_67.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/stimulus_candidates_67.md"

DBCS = {"BHCAN2": "forms/PDT27_E2A_R1_BHCAN2.dbc",
        "FDCAN8": "forms/PDT27_E2A_R1_FDCAN8.dbc"}

# §1 表所需之二項刺激；關鍵詞取自規格用語，非訊號名
TOPICS = {
    "chime（`-055`：ANC/ACN/chime 可用之驗證刺激）":
        (r"chime", r"chime"),
    "ICS 面板觸控回應（`-202`：ICS 功能可用之驗證刺激）":
        (r"DCSD|CLIMATIC_PANEL", r"touch|panel|button|centerstack|climatic"),
}


def parse(path: Path):
    """回傳 [(msg, sig, senders, receivers)] 與 {sig: CM_}, {sig: VAL_}。"""
    t = path.read_text(encoding="cp1252", errors="replace")
    sigs, cur, sender = [], None, None
    for line in t.splitlines():
        m = re.match(r"^BO_ (\d+) (\w+)\s*:\s*\d+\s+(\w+)", line)
        if m:
            cur, sender = m.group(2), m.group(3)
            continue
        m = re.match(r"^\s*SG_\s+(\w+)\s*:.*\"\s*(.*)$", line)
        if m and cur:
            sigs.append((cur, m.group(1), sender, m.group(2).strip()))
    cms = dict(re.findall(r'^CM_ SG_ \d+ (\w+) "(.*)";$', t, re.M))
    vals = dict(re.findall(r"^VAL_ \d+ (\w+) (.*);$", t, re.M))
    return sigs, cms, vals


def main() -> None:
    md = [
        "# 刺激訊號候選（67 包 / R-P390(a)(c)）",
        "",
        "> **執行層供料，不擇定**（R-P390(b)：由分析層以 `CM_` 是否**明述**該功能擇定；",
        "> `CM_` 無明述者不選；全無者開 DR）。",
        "",
        "> 判準：規格只述功能（「有 chime」「ICS 可用」）而未指名訊號 —— "
        "屬**測試刺激之設計選擇**，R-P368(b) 之逐字要件不適用（R-P390 明示）。",
        "> 候選以**規格用語**之關鍵詞掃 forms 二本 DBC，非以訊號名語意挑選。",
        "",
    ]
    for topic, (sig_pat, cm_pat) in TOPICS.items():
        md += [f"## {topic}", ""]
        rows = []
        for tag, rel in DBCS.items():
            sigs, cms, vals = parse(ROOT / rel)
            for msg, sig, sender, recv in sigs:
                full = f"{msg}.{sig}"
                cm = cms.get(sig, "")
                if not (re.search(sig_pat, full, re.I) or
                        (cm and re.search(cm_pat, cm, re.I))):
                    continue
                rows.append((tag, full, cm, sender, recv, vals.get(sig, "")))
        if not rows:
            md += ["**候選 0** —— 依 R-P390(b) 全無者開 DR。", ""]
            continue
        md += [f"候選 **{len(rows)}** 個。", "",
               "| DBC | `MESSAGE.Signal` | `CM_` 註解全文 | 發送節點 | 接收節點 | `VAL_` |",
               "|---|---|---|---|---|---|"]
        for tag, full, cm, sender, recv, val in rows:
            md.append(f"| {tag} | `{full}` | {cm or '**無 `CM_`**'} | `{sender}` | "
                      f"`{recv or '—'}` | {val[:70] or '—'} |")
        md.append("")
        no_cm = [r for r in rows if not r[2]]
        md += [f"> ⚠ 其中 **{len(no_cm)} 個無 `CM_` 註解** —— 依 R-P390(b)"
               "「`CM_` 無明述者不選」，該等候選**不可選**，列此僅為完整性。", ""]
    OUT.write_text("\n".join(md))
    print(f"→ {OUT.relative_to(ROOT)}")
    print("\n".join(md[:6]))


if __name__ == "__main__":
    main()
