"""G121 —— 全量對帳表（R-P178）。第五批之前置。

R-P177：批次範圍一律以 **Test Set 成員資格**定義，不得以 SWE-PM ID 區間定義。
本表即該規則之依據 —— 逐 leaf 一列，往後任何批次自本表取成員清單。

欄位（R-P178 明列）：
    `leaf` / `test_set`（依 §E 定版，取自 `leaf_testset.tsv`）/
    `batch`（`001`–`004` 或 `未產出`）/ `tc_count` / `blocking_dr`

合計須滿足（R-P178）：
    Power State 63 / Startup Display 24 / Branding and Theme 16 /
    Timeout Settings 8 / Power Down 3 = 114
    ＋ `SWE-PM-089`（R-P141 留空，不在 `leaf_testset.tsv` 內）= 115
**任一 Test Set 之合計不符即停並上繳**（§E 明令不得自行調整 §E）。

DR 影響面逐字取自 `DATA_REQUESTS.md` 之「影響面」欄，於下方一次寫定；
**阻斷**與**不阻斷**分列 —— 只有阻斷者才使該 leaf 不可產出。

用法：
    python features/power/scripts/build_reconciliation.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

# §E 定版之各 Test Set leaf 數（R-P35）。**期望值，非由資料推得。**
EXPECTED = {"Power State": 63, "Startup Display": 24,
            "Branding and Theme": 16, "Timeout Settings": 8, "Power Down": 3}
# R-P141 / R-P1：留空之 leaf，不在 `leaf_testset.tsv` 內。
BLANK_LEAF = "SWE-PM-089"

# live DR 之影響面。**阻斷者**（該 leaf 於此 DR 獲解前不可產出）。
BLOCKING_DR = {
    **{f"SWE-PM-{i:03d}": ["DR-PW6"] for i in range(1, 10)},
    "SWE-PM-008": ["DR-PW6", "DR-PW11"],
    "SWE-PM-010": ["DR-PW11"],
    # R-P185（26 包）：DR-PW9 之阻斷欄修訂後明載「阻斷 `SWE-PM-112` 之 TC 撰寫」。
    # 25 包時該欄未承接立條意旨，執行層以保守解自行排除；本包起為明文阻斷。
    "SWE-PM-112": ["DR-PW9"],
    BLANK_LEAF: ["DR-PW1"],
}
# **不阻斷者**（影響內容或範圍歸屬，不阻斷撰寫）。一併列出以免誤讀為「無 DR」。
ADVISORY_DR = {
    "SWE-PM-003": ["DR-PW5"],
    "SWE-PM-007": ["DR-PW7"],
    "SWE-PM-038": ["DR-PW10"],
}
ADVISORY_DR.setdefault("SWE-PM-008", []).append("DR-PW7")


def leaf_testset() -> dict[str, str]:
    out = {}
    for line in (DATA / "leaf_testset.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if parts and parts[0]:
            out[parts[0]] = parts[1]
    return out


def produced() -> tuple[dict[str, str], dict[str, int]]:
    """leaf -> 批次代號；leaf -> TC 數。"""
    batch_of, tc_count = {}, {}
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        code = b.get("batch", "?").split("_")[1]          # `batch_003_…` -> `003`
        for leaf in b.get("leaves", []):
            batch_of[leaf["parent"]] = code
        for tc in b.get("tcs", []):
            tc_count[tc["req_id"]] = tc_count.get(tc["req_id"], 0) + 1
    return batch_of, tc_count


def build() -> list[dict]:
    ts, (batch_of, tc_count) = leaf_testset(), produced()
    rows = []
    for leaf in sorted(set(ts) | {BLANK_LEAF}):
        rows.append({
            "leaf": leaf,
            "test_set": ts.get(leaf, "（留空 —— R-P141）"),
            "batch": batch_of.get(leaf, "未產出"),
            "tc_count": tc_count.get(leaf, 0),
            "blocking_dr": ",".join(BLOCKING_DR.get(leaf, [])) or "—",
            "advisory_dr": ",".join(ADVISORY_DR.get(leaf, [])) or "—",
        })
    return rows


def main() -> None:
    rows = build()
    counts: dict[str, int] = {}
    for r in rows:
        if r["leaf"] != BLANK_LEAF:
            counts[r["test_set"]] = counts.get(r["test_set"], 0) + 1

    header = ["leaf", "test_set", "batch", "tc_count", "blocking_dr", "advisory_dr"]
    tsv = ["\t".join(header)]
    tsv += ["\t".join(str(r[k]) for k in header) for r in rows]
    (DATA / "leaf_batch_reconciliation.tsv").write_text("\n".join(tsv) + "\n",
                                                        encoding="utf-8")

    ok = all(counts.get(k) == v for k, v in EXPECTED.items()) and \
        len(rows) == sum(EXPECTED.values()) + 1
    md = ["# G121 —— 全量對帳表（R-P178）\n",
          "\n> 逐 leaf 一列，見 `data/leaf_batch_reconciliation.tsv`。\n",
          "> 本表為往後全部批次之範圍依據（R-P177(b)）——"
          "**批次範圍取自 Test Set 成員資格，不得以 ID 區間表述。**\n",
          "\n## 1. 各 Test Set 合計對 §E 定版\n\n"
          "| Test Set | §E 定版 | 實測 | 相符 |\n|---|---|---|---|\n"]
    for k, v in EXPECTED.items():
        got = counts.get(k, 0)
        md.append(f"| {k} | {v} | **{got}** | {'是' if got == v else '**否**'} |\n")
    md.append(f"| **合計（不含留空）** | **{sum(EXPECTED.values())}** | "
              f"**{sum(counts.values())}** | "
              f"{'是' if sum(counts.values()) == sum(EXPECTED.values()) else '**否**'} |\n")
    md.append(f"| ＋ `{BLANK_LEAF}`（R-P141 留空）| 1 | 1 | 是 |\n")
    md.append(f"| **總計** | **115** | **{len(rows)}** | "
              f"{'是' if len(rows) == 115 else '**否**'} |\n")
    md.append(f"\n**G121：{'PASS' if ok else '**MISMATCH —— 依 §E 停並上繳**'}。**\n")

    md.append("\n## 2. 產出狀態\n\n"
              "| Test Set | leaf | 已產出 | 未產出 | 其中受阻斷 | 未產出且未阻斷 |\n"
              "|---|---|---|---|---|---|\n")
    for k in EXPECTED:
        sub = [r for r in rows if r["test_set"] == k]
        done = [r for r in sub if r["batch"] != "未產出"]
        todo = [r for r in sub if r["batch"] == "未產出"]
        blocked = [r for r in todo if r["blocking_dr"] != "—"]
        md.append(f"| {k} | {len(sub)} | {len(done)} | {len(todo)} | "
                  f"{len(blocked)} | **{len(todo) - len(blocked)}** |\n")

    md.append("\n## 3. 未產出且未受阻斷之 leaf —— 逐一列出（R-P181(e)）\n\n"
              "| leaf | Test Set | 諮詢性 DR |\n|---|---|---|\n")
    free = [r for r in rows if r["batch"] == "未產出" and r["blocking_dr"] == "—"
            and r["leaf"] != BLANK_LEAF]
    for r in free:
        md.append(f"| `{r['leaf']}` | {r['test_set']} | {r['advisory_dr']} |\n")
    md.append(f"\n**合計 {len(free)} leaf。**\n")

    md.append("\n## 4. 未產出且受阻斷之 leaf\n\n"
              "| leaf | Test Set | 阻斷之 DR |\n|---|---|---|\n")
    for r in rows:
        if r["batch"] == "未產出" and r["blocking_dr"] != "—":
            md.append(f"| `{r['leaf']}` | {r['test_set']} | **{r['blocking_dr']}** |\n")

    (DATA / "g121_reconciliation.md").write_text("".join(md), encoding="utf-8")
    print(f"wrote {(DATA / 'leaf_batch_reconciliation.tsv').relative_to(ROOT)}")
    print(f"wrote {(DATA / 'g121_reconciliation.md').relative_to(ROOT)}")
    for k, v in EXPECTED.items():
        got = counts.get(k, 0)
        print(f"  {k:22s} §E {v:3d}  實測 {got:3d}  {'相符' if got == v else '**不符**'}")
    print(f"  {'總計（含留空）':20s}     115  實測 {len(rows):3d}  "
          f"{'相符' if len(rows) == 115 else '**不符**'}")
    print(f"\nG121：{'PASS' if ok else '**MISMATCH**'}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
