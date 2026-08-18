"""B1 / B2 —— 第一級改值（R-P256 / R-P257）。

**第一級＝事實明確者**：現值違反明文契約，其錯誤無須判斷即可確認。
第二級（`design_method` / `priority` / `axis` 之其餘映射）**不在本檔**，
其前提為分析層之抽樣複核（R-P256 / §I）。

本檔之五＋一項：

  (a) `axis` —— 只改**明確可映者**：重判提案之依據 token
      **逐字見於該 TC 之 `split_reason` 或 `tc_title`**（R-P256(a)）。
      「無對應」40 條與依據不逐字可見者一律不動。
  (b) `split_index = 0` —— 違反 R-P115「同一 leaf 內依規格原文子句出現序」。
  (c) `split_flag = True` 而該 leaf 僅 1 條 TC。
  (d) `remarks` —— 對帳表載有 DR 之 leaf 而其 TC 未註記者補註。
      ⚠ R-P256(d) 書為「無 DR 而註記（8 條）」，而 35 包實測之 8 條
      實為**應註記而未註記**；「無 DR 而註記」者僅 `…-015` 1 條，
      且 35 包已判其**不一致方可能是對帳表而非該 TC**（A-PW199）——
      故 `…-015` **不在本次改值範圍**，依條文所指之「8 條」處理。
  (e) `delta` 逐字重複（`SWE-PM-071` 之 `…-002` / `…-003`）。
  (B2) `SWE-PM-025` 之 `087`/`091`、`088`/`092` 內文補入其觸發訊號（R-P257）。

序列化以 `indent=1` / `ensure_ascii=False` 寫回 —— 已驗其對未改動之檔
**位元組完全還原**，故 diff 中所見即實際改動。

用法：
    python features/power/scripts/apply_tier1_edits.py --dry-run
    python features/power/scripts/apply_tier1_edits.py --apply
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GEN = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_axis import propose_axis  # noqa: E402

BASE = re.compile(r"(SWE-PM-\d+)")

# R-P257：二對之觸發訊號，取自其 `tc_title` 之逐字。
SWEPM025 = {
    "NR1L-PowerManagement-087": "Front_Panel_OnOff.Req",
    "NR1L-PowerManagement-088": "Front_Panel_OnOff.Req",
    "NR1L-PowerManagement-091": "CLIMATIC_PANEL.Radio_Btn0",
    "NR1L-PowerManagement-092": "CLIMATIC_PANEL.Radio_Btn0",
}


def load_dr() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for ln in (DATA / "leaf_batch_reconciliation.tsv").read_text(
            encoding="utf-8").split("\n")[1:]:
        c = ln.split("\t")
        if len(c) >= 6:
            drs = [x.strip() for x in (c[4], c[5]) if x.strip() not in ("—", "")]
            if drs:
                out[c[0]] = drs
    return out


def main() -> None:
    apply = "--apply" in sys.argv
    if not apply and "--dry-run" not in sys.argv:
        raise SystemExit("須指定 --dry-run 或 --apply")

    files = {p: json.loads(p.read_text(encoding="utf-8"))
             for p in sorted(GEN.glob("*.json"))}
    tcs = [t for d in files.values() for t in d["tcs"]]
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)
    dr = load_dr()

    log: list[tuple[str, str, str, str, str]] = []   # 項, tc, 欄, 舊, 新

    def setv(t: dict, field: str, new, item: str) -> None:
        old = t.get(field)
        if old == new:
            return
        log.append((item, t["tc_id"], field, json.dumps(old, ensure_ascii=False),
                    json.dumps(new, ensure_ascii=False)))
        t[field] = new

    for t in tcs:
        leaf = BASE.match(t["req_id"]).group(1)
        peers = by_leaf[leaf]

        # (a) axis —— 僅明確可映者
        ax, ev = propose_axis(t, peers)
        if ax is not None:
            m = re.search(r"：`([^`]+)`$", ev)
            tok = m.group(1) if m else None
            hay = f"{t.get('split_reason', '')} {t.get('tc_title', '')}"
            if tok and tok in hay and t["distinguishing_axis"]["axis"] != ax:
                old = dict(t["distinguishing_axis"])
                log.append(("(a) axis", t["tc_id"], "distinguishing_axis.axis",
                            old["axis"], ax))
                t["distinguishing_axis"]["axis"] = ax

        # (b) split_index = 0
        if t.get("split_index") == 0:
            order = sorted(peers, key=lambda x: x["tc_id"])
            setv(t, "split_index", order.index(t) + 1, "(b) split_index=0")

        # (c) split_flag True 而該 leaf 僅 1 條
        if t.get("split_flag") is True and len(peers) < 2:
            setv(t, "split_flag", False, "(c) split_flag 單條")
            setv(t, "split_index", 1, "(c) split_flag 單條")

        # (d) remarks 補註
        if leaf in dr and not str(t.get("remarks", "")).strip():
            setv(t, "remarks", f"{' / '.join(dr[leaf])} 待範圍確認",
                 "(d) remarks 補註")

        # (B2) SWE-PM-025 內文補入觸發訊號（R-P257）——
        # `test_procedure` 與 `pre_conditions` 二處皆須具名：
        # 該 popup 係由二控制之一所觸發，**其來源即為二條之唯一區分**，
        # 故僅改 procedure 而不改 pre 仍留有「popup 從何而來」之空白。
        if t["tc_id"] in SWEPM025:
            sig = SWEPM025[t["tc_id"]]
            if sig not in t["test_procedure"]:
                setv(t, "test_procedure",
                     t["test_procedure"].replace("the popup", f"the {sig} popup"),
                     "(B2) SWE-PM-025 觸發具名")
            if sig not in t["pre_conditions"]:
                setv(t, "pre_conditions",
                     t["pre_conditions"].replace(
                         "The transfer popup is shown",
                         f"The transfer popup is shown after the {sig} press"),
                     "(B2) SWE-PM-025 觸發具名")

    # (e) delta 逐字重複 —— 同 leaf 內
    for leaf, group in by_leaf.items():
        seen: dict[str, list[dict]] = collections.defaultdict(list)
        for t in group:
            seen[t["distinguishing_axis"]["delta"]].append(t)
        for delta, dupes in seen.items():
            if len(dupes) < 2:
                continue
            for t in dupes:
                # 自 `tc_title` 取其獨有之區分語 —— 不新造事實
                tail = t["tc_title"].split(" when ")[-1].split(" passes to ")[-1]
                new = f"{delta}；本條之分支為：{tail}"
                old = t["distinguishing_axis"]["delta"]
                log.append(("(e) delta 重複", t["tc_id"],
                            "distinguishing_axis.delta", old[:40] + "…", new[-40:]))
                t["distinguishing_axis"]["delta"] = new

    by_item = collections.Counter(x[0] for x in log)
    print(f"{'（乾跑）' if not apply else '（套用）'}改動 {len(log)} 處：")
    for k, v in sorted(by_item.items()):
        print(f"  {k}: {v}")

    lines = ["# B1 / B2 —— 第一級改值紀錄（R-P256 / R-P257）\n",
             f"\n> 模式：**{'套用' if apply else '乾跑'}**；改動 **{len(log)}** 處。\n",
             "\n| 項 | 條數 |\n|---|---|\n"]
    for k, v in sorted(by_item.items()):
        lines.append(f"| {k} | **{v}** |\n")
    lines.append("\n| 項 | tc | 欄 | 舊值 | 新值 |\n|---|---|---|---|---|\n")
    for item, tid, field, old, new in log:
        lines.append(f"| {item} | `…-{tid[-3:]}` | `{field}` | {old} | {new} |\n")
    (DATA / "tier1_edits.md").write_text("".join(lines), encoding="utf-8")

    if apply:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                         encoding="utf-8")
        print(f"已寫回 {len(files)} 檔")
    else:
        print("未寫回（乾跑）")


if __name__ == "__main__":
    main()
