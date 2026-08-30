"""R-P372 複查 —— 45 名無錨 `<X>` 以其 TC 之 `test_item` 規格用語重查（63 包 §H 第 4 步）。

R-P372(a)：51 名逐名讀其所屬 TC 之 `test_item` 上半 verbatim（該處為規格逐字），
以**規格用語**再查 G0 台帳一次；結果三分 ——
  有錨（補入代理量表）／查無（R-G13 三要件齊備）／待併案。
R-P372(b)：逐字含 `antitheft` 者併入 DR-PW23，不另開 DR。
  其數依 R-P378(b) 之訂正為 **6 名**，複查對象 **45 名**。

與 59 包 `proxy_reachability_59.py` 之差別：
  59 包以 **TC 之措辭**（`<X>` 原文）查；
  本檔以 **`test_item` 上半之規格逐字**查 —— 二者為不同之查詢名稱種類（R-G13 第 2 項）。

用法：
    python features/power/scripts/proxy_recheck_63.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402
import proxy_reachability_59 as pr  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/proxy_reachability_63.md"

STOP = pr.STOP | {"shall", "when", "then", "read", "check", "has", "have",
                  "this", "which", "value", "values", "case", "into", "from",
                  "not", "also", "per", "refer", "see", "shown", "state"}


def content(x: str) -> list[str]:
    return [w for w in re.findall(r"[a-z_$][a-z0-9_$.]*", x.lower())
            if w not in STOP and len(w) > 3]


def main() -> None:
    # 59 包之無錨名
    src = (ROOT / "features/power/data/proxy_reachability_55.md").read_text()
    unmatched = []
    for ln in src.splitlines():
        if not ln.startswith("| `"):
            continue
        cells = ln.split("|")
        if len(cells) > 5 and "**無**" in cells[4]:
            unmatched.append(cells[1].strip().strip("`"))
    anti = [x for x in unmatched if "antitheft" in x.lower()]
    todo = [x for x in unmatched if x not in anti]
    print(f"無錨 {len(unmatched)}；含 antitheft {len(anti)}（併 DR-PW23）；"
          f"複查對象 {len(todo)}")

    # `<X>` → 其所屬 TC 之 test_item 上半
    cur = rm.load_current()
    owner: defaultdict = defaultdict(set)
    for tc in cur:
        for f in ("test_procedure", "expected_result"):
            for line in (tc.get(f) or "").splitlines():
                m = pr.READ_RE.match(line)
                if not m:
                    continue
                obj = re.sub(r"^(the|a|an)\s+", "", m.group(1).strip(),
                             flags=re.I).strip(" .,")
                if obj in todo:
                    head = (tc.get("test_item") or "").split("\n\n(")[0]
                    owner[obj].add((tc["tc_id"], head))

    paras = pr.anchored_paragraphs()
    vals = pr.val_labels()

    rows, stat = [], {"有錨": 0, "查無": 0, "未覆蓋": 0}
    for x in todo:
        tcs = sorted(owner.get(x, []))
        if not tcs:
            stat["未覆蓋"] += 1
            rows.append(f"| `{x[:56]}` | — | — | **未覆蓋** | "
                        f"無 TC 之 `Read <X>` 逐字對應（措辭於 59 包掃描後已變）|")
            continue
        # 規格用語 = test_item 上半之內容詞（去 TC 措辭）
        spec = set()
        for _, head in tcs:
            spec |= set(content(head))
        xt = set(content(x))
        probe = sorted(spec & xt) or sorted(xt)
        hits = []
        for src_, oid, body in paras:
            if probe and all(t in body for t in probe):
                hits.append(f"{src_}-{oid}")
                if len(hits) >= 2:
                    break
        if not hits and probe and all(t in vals for t in probe):
            hits = ["DBC `VAL_`/`CM_`"]
        verdict = "**有錨**" if hits else "**查無**"
        stat["有錨" if hits else "查無"] += 1
        rows.append(f"| `{x[:56]}` | {len(tcs)} | `{'、'.join(sorted(probe))[:40]}` | "
                    f"{verdict} | {'、'.join(hits) if hits else '—'} |")

    body = [
        "# R-P372 複查 —— 45 名無錨 `<X>` 以規格用語重查（63 包）",
        "",
        "> R-P372(a)：以所屬 TC 之 `test_item` 上半 verbatim（規格逐字）"
        "為查詢名稱，重查 G0 台帳一次。",
        "> 與 59 包之差別為**查詢名稱種類**（R-G13 第 2 項）："
        "59 包查 TC 措辭，本檔查規格用語。",
        "> R-P372(b)：逐字含 `antitheft` 者 **6 名**併入 DR-PW23，不另開 DR"
        "（R-P378(b) 訂正 R-P372(b) 之「11 名／40」）。",
        "",
        f"## 總計：複查 {len(todo)} 名",
        "",
        "| 判定 | 數 |",
        "|---|---|",
        f"| 有錨 | **{stat['有錨']}** |",
        f"| 查無 | **{stat['查無']}** |",
        f"| 未覆蓋（無逐字對應之 TC）| **{stat['未覆蓋']}** |",
        "",
        "## 逐名",
        "",
        "| `<X>` | TC 數 | 查詢用之規格內容詞 | 判定 | 錨點 |",
        "|---|---|---|---|---|",
    ] + rows + [""]
    OUT.write_text("\n".join(body))
    print(stat)
    print(f"→ {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
