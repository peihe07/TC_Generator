"""R-P382 —— 39 個有錨 `<X>` 之代理量表（64 包 §H 第 4 步）。

格式（R-P353）：`<原 X> | <代理量（白名單類別）> | <錨點> | <影響列>`。
代理量須為 R-P353 白名單四類之一：
  (i)   `$MESSAGE.Signal$`
  (ii)  具名 UI 元件（以 `"..."` 標示）
  (iii) 可量測音訊（source indicator / `AUD_LVL` / 指定揚聲器有無輸出）
  (iv)  log / trace 之具名行或具名計數器

**填不出白名單類者不得硬填，回報**（R-P382 明文 / 64 包 §I）。

作法：自該 `<X>` 之錨點段落**逐字**抽出白名單類候選 ——
  (i)  段落中之 `$…$`（再經 R-P368 三段鏈確認其在 forms DBC 有 `SG_`）
  (ii) 段落中之 `"…"` 引號名或 `[…]` 方括號值
  (iii)/(iv) 音訊／log 之具名詞
段落中無任一類者，記「**填不出**」並列其原因。**不自造**（R-P353 / §8.4.1）。

用法：
    python features/power/scripts/observable_proxy_64.py
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402
import proxy_reachability_59 as pr  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/observable_proxy_64.md"

DOLLAR = re.compile(r"\$[A-Za-z0-9_.]+\$")
QUOTED = re.compile(r'"([^"]{2,40})"|\[([A-Za-z0-9_ ]{2,30})\]')
# R-P353(ii) 要的是**具名 UI 元件**（如 `"Splash Screen"`），不是欄位之**值**
# （如 `"present"` / `"00 min"`）。以 UI 名詞為準，值一律不取。
UI_NOUN = re.compile(
    r"screen|icon|pop-?up|popup|menu|logo|banner|splash|disclaimer|animation"
    r"|button|list|graphic|font|avatar|wording|display", re.I)
VALUE_LIKE = re.compile(r"^\s*(\d|on$|off$|true$|false$|present$|absent$"
                        r"|undefined$|sna$|yes$|no$)", re.I)
AUDIO = re.compile(r"\bAUD_LVL\b|source indicator|speaker|\bmuted?\b|audio", re.I)
LOGS = re.compile(r"\blogs?\b|\btrace\b|counter", re.I)


def lid_chain() -> dict[str, list[str]]:
    """規格 `$X$` → LID `Atlantis High` 之 `MESSAGE.Signal`（R-P368 段 1→2）。

    段 1 之比對面為 `Logical Identifier`(c1)。逐字命中方取，
    前後綴差異不在此處放寬（放寬須逐筆載明依據，非本表之職）。
    """
    import openpyxl
    wb = openpyxl.load_workbook(
        ROOT / "forms/Logical Identifiers and CAN Mapping v1_78.xlsx",
        data_only=True, read_only=True)
    out: dict[str, list[str]] = {}
    for row in wb["CAN Mapping"].iter_rows(min_row=4, values_only=True):
        lid, ah = row[0], (row[25] if len(row) > 25 else None)
        if not isinstance(lid, str) or not isinstance(ah, str):
            continue
        vals = [v.strip() for v in ah.splitlines() if "." in v]
        if vals:
            out[lid.strip().lower()] = vals
    wb.close()
    return out


def dbc_signals() -> set[str]:
    out = set()
    for p in ("forms/PDT27_E2A_R1_BHCAN2.dbc", "forms/PDT27_E2A_R1_FDCAN8.dbc"):
        t = (ROOT / p).read_text(encoding="cp1252", errors="replace")
        out |= set(re.findall(r"^\s*SG_\s+(\w+)\s*:", t, re.M))
    return out


def main() -> None:
    src = (ROOT / "features/power/data/proxy_reachability_63.md").read_text()
    anchored = []
    for ln in src.splitlines():
        if ln.startswith("| `") and "**有錨**" in ln:
            cells = ln.split("|")
            anchored.append((cells[1].strip().strip("`"), cells[5].strip()))
    print(f"有錨名 {len(anchored)}")

    cur = rm.load_current()
    owners: defaultdict = defaultdict(list)
    for tc in cur:
        for f in ("test_procedure", "expected_result"):
            for line in (tc.get(f) or "").splitlines():
                m = pr.READ_RE.match(line)
                if not m:
                    continue
                obj = re.sub(r"^(the|a|an)\s+", "", m.group(1).strip(),
                             flags=re.I).strip(" .,")
                if tc["tc_id"] not in owners[obj]:
                    owners[obj].append(tc["tc_id"])

    paras = {f"{s}-{o}": b for s, o, b in pr.anchored_paragraphs()}
    sgs = dbc_signals()
    lid = lid_chain()
    print(f"LID 段 1→2 對照 {len(lid)} 列")

    rows, filled, unfilled = [], 0, []
    for x, anchor in anchored:
        body = ""
        for a in [t.strip() for t in anchor.replace("、", ",").split(",")]:
            body += paras.get(a, "") + " "
        cands = []
        for d in dict.fromkeys(DOLLAR.findall(body)):
            bare = d.strip("$")
            # 直接同名者
            if bare.split(".")[-1] in sgs:
                cands.append(f"(i) `{d}`")
                continue
            # 否則走 R-P368 段 1→2：規格名 → LID → `MESSAGE.Signal` → 段 3
            for ms in lid.get(bare.lower(), []):
                if ms.split(".")[-1] in sgs:
                    cands.append(f"(i) `${ms}$`（規格名 `{d}` 經 LID 解得）")
        for m in QUOTED.finditer(body):
            v = (m.group(1) or m.group(2) or "").strip()
            if not v or VALUE_LIKE.match(v) or not UI_NOUN.search(v):
                continue
            cands.append(f'(ii) `"{v}"`')
        # 段落內未加引號但為具名 UI 元件者（`Splash Screen` 之類），
        # 取其首字大寫之連續詞組，仍須含 UI 名詞。
        for m in re.finditer(r"\b([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+){0,3})\b", body):
            v = m.group(1)
            if UI_NOUN.search(v) and f'(ii) `"{v}"`' not in cands:
                cands.append(f'(ii) `"{v}"`')
        if AUDIO.search(body):
            cands.append("(iii) 音訊面 —— 段落載有音訊詞，**具體量須人定**")
        if LOGS.search(body):
            cands.append("(iv) log 面 —— 段落載有 log 詞，**具名行須人定**")
        cands = list(dict.fromkeys(cands))[:3]
        tcs = owners.get(x, [])
        if cands:
            filled += 1
            rows.append(f"| `{x}` | {'<br>'.join(cands)} | {anchor} | "
                        f"{len(tcs)}（{'、'.join(t[-3:] for t in tcs[:6])}）|")
        else:
            unfilled.append((x, anchor, len(tcs)))
            rows.append(f"| `{x}` | **填不出** | {anchor} | "
                        f"{len(tcs)}（{'、'.join(t[-3:] for t in tcs[:6])}）|")

    body_md = [
        "# 代理量表（64 包 / R-P382 / R-P353）",
        "",
        "> 母體：`proxy_reachability_63.md` 之 **有錨 39 名**，"
        "R-P382 覆核通過後填。",
        "> 代理量須為 R-P353 白名單四類；**填不出白名單類者不硬填**（R-P382 / §I）。",
        "> 候選自該名之錨點段落**逐字**抽出：`$…$` 再經 forms DBC `SG_` 確認；"
        "(ii) 只取**具名 UI 元件**（含 screen／icon／pop-up／menu／logo／button 等 UI 名詞），"
        "**欄位之值**（`\"present\"`／`\"00 min\"`／`\"True\"`）一律不取；"
        "(iii)(iv) 只標面向，具體量須人定。**不自造**（§8.4.1）。",
        "",
        "> ⚠ **本表為候選抽取，非最終代理量。** 一個 `<X>` 可能抽出多個候選，"
        "**擇一為代理量仍是判斷**（R-P353 令『由執行層為每一功能指定**一個**』），"
        "而該判斷與 R-P381 之人讀同性質。本層列全部候選並標類別，"
        "**未擇一**，待分析層覆核時定。",
        "",
        f"## 總計：{len(anchored)} 名 —— 可填 **{filled}**、填不出 **{len(unfilled)}**",
        "",
        "| `<原 X>` | 代理量（白名單類別）| 錨點 | 影響列 |",
        "|---|---|---|---|",
    ] + rows + [""]
    if unfilled:
        body_md += [
            "## 填不出白名單類者（R-P382 令回報）", "",
            "| `<原 X>` | 錨點 | 影響列 | 原因 |", "|---|---|---|---|",
        ] + [f"| `{x}` | {a} | {n} | 錨點段落內無 `$…$`（經 DBC `SG_` 確認）、"
             f"無引號具名值、無音訊／log 具名詞 |" for x, a, n in unfilled] + [""]
    OUT.write_text("\n".join(body_md))
    print(f"可填 {filled}、填不出 {len(unfilled)}")
    print(f"→ {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
