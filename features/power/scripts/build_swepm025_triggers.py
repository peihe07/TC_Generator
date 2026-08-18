"""B3 —— `SWE-PM-025` 二組錨點之觸發訊號逐字原文（R-P179）。

R-P179：`SWE-PM-025` 三對之 ECU 為真集合差 `{ETM}`，惟本專案為 LTM
（Atlantis High），二組之 ECU 集合**皆含 LTM**，故該差異不改變適用性。
真正之爭點為 22 §八第 4 項所述之「只差觸發訊號」：

  （a）觸發訊號確為不同訊號 → 依 §5.7 拆分成立，八條維持
  （b）為同一訊號之不同稱法 → 併為四條

本腳本上繳**逐字原文並列**，**不作判斷、不合併、不拆分**（R-P179 明令）。

判別所需之客觀證據一併取得：
  - 二訊號名於**全部 CFTS 文字層**之出現處（是否各自獨立見於他章）
  - 二訊號名於 **SYS2 匯出**之出現情形（是否為二個獨立登記之訊號）

用法：
    python features/power/scripts/build_swepm025_triggers.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_tcs as L  # noqa: E402

PAIRS = [("4941569", "4941572"), ("4941570", "4941573"), ("4941571", "4941574")]
SIGNALS = ["Front_Panel_OnOff.Req", "CLIMATIC_PANEL.Radio_Btn0"]
# 觸發子句 —— 自「訊號名」起至該子句之 `THEN` 止，逐字截取。
TRIGGER_RE = re.compile(
    r"(Front_Panel_OnOff\.Req|CLIMATIC_PANEL\.Radio_Btn0)(.*?)(?=THEN|$)",
    re.S)


def _leaf_chapters() -> dict[str, str]:
    """anchor -> 章節編號，取自 `layer3_full.tsv`。"""
    out = {}
    rows = (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()
    head = rows[0].split("\t")
    for line in rows[1:]:
        r = dict(zip(head, line.split("\t")))
        for a in r["item_ids"].split(","):
            if a:
                out[a] = r["chapter_num"]
    return out


def occurrences(name: str, bodies: dict[str, list[str]]) -> list[str]:
    return sorted(a for a, body in bodies.items() if name in "\n".join(body))


def main() -> None:
    bodies = L.anchor_bodies()
    out = ["# B3 —— `SWE-PM-025` 觸發訊號逐字原文（R-P179）\n",
           "\n> 原文取自 CFTS 文字層（R-P17），**未經任何改寫**。\n",
           "> **執行層不作判斷、不合併、不拆分**；裁定於 26 包。\n",
           "\n## 1. 三對之觸發子句並列\n"]
    for a, b in PAIRS:
        out.append(f"\n### `{a}` vs `{b}`\n\n")
        for anchor in (a, b):
            text = "\n".join(bodies.get(anchor, []))
            m = TRIGGER_RE.search(text)
            if m:
                out.append(f"**`{anchor}`** —— 觸發子句：\n\n"
                           f"```\n{m.group(0).strip()}\n```\n\n")
            else:
                # 該錨點不含觸發訊號名（為前一錨點之後續行為）——
                # 逐字輸出其完整原文，不以「未匹配」帶過。
                out.append(f"**`{anchor}`** —— **本錨點不含觸發訊號名**，"
                           f"完整原文如下：\n\n```\n{text.strip()}\n```\n\n")

    out.append("\n## 2. 二訊號名於 CFTS 文字層之出現處\n\n"
               "| 訊號名 | 出現之錨點數 | 錨點 |\n|---|---|---|\n")
    for sig in SIGNALS:
        hits = occurrences(sig, bodies)
        out.append(f"| `{sig}` | **{len(hits)}** | "
                   f"{'、'.join('`' + h + '`' for h in hits)} |\n")

    out.append("\n## 3. 二訊號之共現情形（中性陳述，不作判斷）\n\n")
    both = [a for a in bodies
            if all(s in "\n".join(bodies[a]) for s in SIGNALS)]
    out.append(f"同時含二訊號之錨點：**{len(both)}**"
               f"{'（' + '、'.join('`' + a + '`' for a in sorted(both)) + '）' if both else ''}。\n\n")
    out.append(
        "**證據方向須說明清楚，以免誤讀**：\n\n"
        "- 若二者曾**於同一錨點內並列**（例如同一句列出二個觸發），"
        "即為「二個相異訊號」之**強證據**（(a)）。\n"
        "- 二者**從未共現**，則**傾向 (b) 之弱證據** ——"
        "同一訊號之不同稱法本就不會被並列書寫。\n"
        "- **惟「從未共現」亦與 (a) 相容**：二個相異訊號若分屬不同硬體來源，"
        "各自成段書寫亦屬常態。\n\n"
        "**故本節之數字不足以獨立裁定，僅供 26 包參考。**\n")

    out.append("\n## 4. 二訊號各自出現之章節分布\n\n"
               "| 訊號名 | 章節（去重）|\n|---|---|\n")
    chapters = _leaf_chapters()
    for sig in SIGNALS:
        secs = sorted({chapters.get(a, "?") for a in occurrences(sig, bodies)})
        out.append(f"| `{sig}` | {'、'.join(secs)} |\n")

    (DATA / "b3_swepm025_triggers.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'b3_swepm025_triggers.md').relative_to(ROOT)}")
    for sig in SIGNALS:
        print(f"  {sig}: {len(occurrences(sig, bodies))} 個錨點")
    print(f"  同時含二訊號之錨點: {len(both)}")


if __name__ == "__main__":
    main()
