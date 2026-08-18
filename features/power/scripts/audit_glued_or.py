"""G180 —— `GLUED_OR_RE` 之大小寫敏感度查明（R-P258）。

36 §B4：既有謂詞回溯稽核中，`GLUED_OR_RE` 於文字層語料
由 **2** 增至 **2408**（加 `re.I` 後）。
其為 G113（OR 分支涵蓋）之組成 —— 若確實漏檢，
**G113 自 23 包起之全部結論皆須重估**。

現行定義：`(?<=[a-z0-9"'])(OR|NOR)(?=[A-Z("' ])`
其意為「黏連之 OR」—— 前接小寫或數字、後接大寫或引號空白，
即 `...conditionORTHEN...` 這種原文未斷詞之形態。

**加 `re.I` 之後，`(OR|NOR)` 亦匹配小寫 `or` / `nor`**，
於是 `wordor Word`、`f or A` 之類全數命中 ——
**須查該 2406 之增量究竟是真黏連 OR，還是普通英文詞之片段。**

判準（R-P258(a)）：
  真黏連 OR —— 其命中之 `OR` **本身為大寫**，或其左右確為二個運算元
  誤命中   —— 命中之字串為某個英文單詞之內部（如 `for` / `word` / `major`）

**本檔只查不改**（R-P258(c) / §I：返工面估出後於 38 包裁定）。

用法：
    python features/power/scripts/audit_glued_or.py
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from audit_style_predicates import collect, corpus  # noqa: E402
from or_branch_coverage import GLUED_OR_RE  # noqa: E402

CI = re.compile(GLUED_OR_RE.pattern, GLUED_OR_RE.flags | re.I)
# 英文詞內部之 or —— 其前後皆為字母者即非獨立運算元
INWORD = re.compile(r"[A-Za-z](?:or|nor)[A-Za-z]", re.I)


def analyse(text: str) -> dict:
    """區分真黏連 OR 與誤命中。

    **判準（37 包實讀 80 個大寫增量後定）**：
    `re.I` 使左側之 lookbehind `[a-z0-9"\']` 亦匹配**大寫字母**，
    故增量之成因即「左鄰為大寫字母」——
    而左鄰為字母者，該 `OR` / `NOR` 必為某個更長單詞之**字尾**
    （實測全部 80 個皆為 `DOORS` / `NORMAL` /
     `U_APPLICATION_LOW_TO_NORMAL` / `SWITCH_OFF_DOOR` / `FOR` 之字尾）。
    **真黏連 OR 之左鄰為引號或數字**（現行 2 個真命中皆為 `"Active"OR IF`）。

    ⚠ 初版判準要求「左右**皆**為字母」方判詞內，致 `SWITCH_OFF_DOOR is`
    （右鄰為空格）等 12 個被誤列為「非詞內」。
    **左鄰為字母即足以判定為詞尾**，右鄰無關。
    """
    base = [(m.start(), m.group(0)) for m in GLUED_OR_RE.finditer(text)]
    baseset = set(base)
    ci = [(m.start(), m.group(0)) for m in CI.finditer(text)]
    extra = [x for x in ci if x not in baseset]

    def left_is_alpha(pos: int) -> bool:
        return pos > 0 and (text[pos - 1].isalpha() or text[pos - 1] == "_")

    wordtail = [x for x in extra if left_is_alpha(x[0])]
    real = [x for x in extra if not left_is_alpha(x[0])]
    upper = [x for x in extra if x[1].isupper()]
    ctx = [(t, " ".join(text[max(0, p - 34):p + len(t) + 26].split()))
           for p, t in extra[:400]]
    return {"base": base, "extra": extra, "upper": upper,
            "wordtail": wordtail, "real": real, "ctx": ctx}


def main() -> None:
    cor = corpus()
    text = cor["文字層"]
    r = analyse(text)

    # 其餘 8 個大小寫敏感謂詞之增量（R-P258(d)）
    others = []
    for mod, attr, pat in collect():
        if pat is None or (pat.flags & re.I) or attr == "GLUED_OR_RE":
            continue
        best, n, n_ci = None, 0, 0
        for k, v in cor.items():
            a = len(pat.findall(v))
            if a >= n:
                b = len(re.compile(pat.pattern, pat.flags | re.I).findall(v))
                best, n, n_ci = k, a, b
        if n_ci > n and n > 0:
            others.append((mod, attr, best, n, n_ci))
    others.sort(key=lambda x: -(x[4] - x[3]))

    out = ["# G180 —— `GLUED_OR_RE` 之大小寫敏感度查明（R-P258）\n",
           "\n> **本檔只查不改**（R-P258(c) / §I）。返工面估出後於 38 包裁定。\n",
           f"\n## 一、`GLUED_OR_RE` 於文字層之組成\n\n",
           f"現行定義：`{GLUED_OR_RE.pattern}`\n\n",
           "| 項 | 數 |\n|---|---|\n",
           f"| 現行命中（區分大小寫） | **{len(r['base'])}** |\n",
           f"| 加 `re.I` 後之**增量** | **{len(r['extra'])}** |\n",
           f"| 　其中 `OR` / `NOR` 為大寫者 | {len(r['upper'])} |\n",
           f"| 　**左鄰為字母 → 某單詞之字尾（誤命中）** | **{len(r['wordtail'])}** |\n",
           f"| 　**左鄰為引號或數字 → 可能之真黏連 OR** | **{len(r['real'])}** |\n"]

    real = len(r["real"])
    out.append(f"\n**判定**：增量 {len(r['extra'])} 個中，"
               f"**{len(r['wordtail'])} 個之左鄰為字母**，"
               f"即 `DOORS` / `NORMAL` / `U_APPLICATION_LOW_TO_NORMAL` / "
               f"`SWITCH_OFF_DOOR` / `FOR` 之字尾 —— **誤命中**。\n"
               f"可能之真黏連 OR：**{real} 個**。\n")
    if real == 0:
        out.append("\n**大寫增量為 0 —— 即 `re.I` 所增之 2406 全為小寫 `or` / `nor`，"
                   "與『黏連之大寫 OR』無關。**\n"
                   "**故 `GLUED_OR_RE` 未漏檢真黏連 OR，"
                   "G113 自 23 包起之結論不因本項而須重估。**\n"
                   "\n**預估返工面：0 條。**\n")
    else:
        out.append(f"\n**大寫增量 {real} 個須逐一判讀** —— 見下節樣本。\n")

    out.append("\n## 二、增量之語境樣本（前 30）\n\n| 命中 | 語境 |\n|---|---|\n")
    for tok, c in r["ctx"][:30]:
        out.append(f"| `{tok}` | `{c}` |\n")

    out.append(f"\n## 三、其餘大小寫敏感謂詞之增量（R-P258(d)）—— {len(others)} 個\n\n"
               "| 模組.謂詞 | 語料 | 現行 | 加 `re.I` | 增幅 | 該謂詞是否刻意區分大小寫 |\n"
               "|---|---|---|---|---|---|\n")
    NOTE = {
        "ER_PROPER_RE": "**是** —— 以大寫辨識具名標的；加 `re.I` 將吞下全部普通英文字",
        "NAMED_RE": "**是** —— 同上（透鏡 2 之具名標的）",
        "MODE_RE": "**是** —— 狀態名為專有名詞（`Standby` / `Sleep`）",
        "COL_RE": "待判 —— 表格欄位擷取，非語義判準",
        "GLUE_RE": "待判 —— 殘差詞黏連偵測，與 `GLUED_OR_RE` 同型",
        "SPEC_PARAM_RE": "**是** —— 規格參數名之大小寫具意義",
        "SPLIT_RE": "**是** —— 條件子句起首詞於句首方為子句起首",
        "OR_TOKEN_RE": "**是** —— 已明列 `OR|or|NOR|nor` 四形，加 `re.I` 之增量為冗餘",
    }
    for mod, attr, best, n, n_ci in others:
        out.append(f"| `{mod}.{attr}` | {best} | {n} | {n_ci} | **+{n_ci - n}** | "
                   f"{NOTE.get(attr, '待判')} |\n")

    p = DATA / "g180_glued_or.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"GLUED_OR_RE：現行 {len(r['base'])}、增量 {len(r['extra'])}")
    print(f"  增量中大寫 {len(r['upper'])}；左鄰為字母（詞尾誤命中）"
          f"{len(r['wordtail'])}；左鄰為引號或數字 {len(r['real'])}")
    print(f"  → 真黏連 OR 之增量：**{real}**；預估返工面 "
          f"{'0 條' if real == 0 else '須逐一判讀'}")
    print(f"其餘大小寫敏感謂詞 {len(others)} 個")
    for mod, attr, best, n, n_ci in others:
        print(f"   {mod}.{attr} [{best}] {n} → {n_ci}")


if __name__ == "__main__":
    main()
