#!/usr/bin/env python3
"""下放包之預期數字表（R-G16）。

R-G16 令下放包之預期數字由本工具自 `feature.yaml` + 批次清單 + `lint_defs`
推導產生，分析層覆核後簽入包內；手算僅限工具未覆蓋之新指標，逐項標
`[MANUAL]`。工具產出與上繳實測不符時，**工具與語料兩側皆查**（FO §5a-16），
不得預設任一側為準。

**本工具只推導，不調和**（FO §8.5-2）。`--verify` 逐項列「推導 vs 手算」，
不符者標 `**不符**` 並回報，**不改任何一側**。

**手算值之來源**：批次 manifest 之 `selection` 欄逐字記載該批下放包之
選池算式（例：`量產母體 574（620 − pilot 20 − 隔離 26，R-VF77 二）`）。
本工具自該字串抽其數，作為 §5a-12 之「已知全集」。

**seq 連續性為第二層檢驗之落點**：R-VF83 令 B 欄自 `seq_start` 起
**連續遞增**。逐產出檔取 seq 之聯集，驗其為一段無洞之區間 ——
**洞不會使任何 lint 轉紅**（每批各自連續即可），只有跨批之聯集看得出來。
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

RE_HAND = re.compile(r"母體\s*(?P<pool_net>\d+)\s*[（(]\s*(?P<pool>\d+)\s*[-−]\s*pilot\s*"
                     r"(?P<pilot>\d+)\s*[-−]\s*隔離\s*(?P<iso>\d+)")


@dataclass
class Metric:
    key: str
    label: str
    derived: object
    hand: object = None          # 手算值；None = 手算包未載此項
    note: str = ""

    @property
    def verdict(self) -> str:
        if self.hand is None:
            return "無手算值"
        return "符" if str(self.derived) == str(self.hand) else "**不符**"


@dataclass
class Corpus:
    root: Path
    feature: str
    profile: str
    cfg: dict = field(default_factory=dict)

    @property
    def fdir(self) -> Path:
        return self.root / "features" / self.feature

    def load(self) -> None:
        self.cfg = yaml.safe_load((self.fdir / "feature.yaml").read_text(encoding="utf-8"))

    def profile_cfg(self) -> dict:
        return (self.cfg.get("profiles") or {}).get(self.profile, {})

    def tsv_rows(self, rel: str) -> list[dict]:
        p = self.fdir / rel
        if not p.exists():
            return []
        return list(csv.DictReader(p.read_text(encoding="utf-8").splitlines(), delimiter="\t"))

    def artifacts(self) -> list[tuple[str, dict]]:
        """該 profile 之 pilot 與批次產出，依檔名排序。"""
        out = []
        for p in sorted((self.fdir / "generated").glob(f"{self.profile}_*.json")):
            try:
                out.append((p.name, json.loads(p.read_text(encoding="utf-8"))))
            except json.JSONDecodeError:
                continue
        return out


def seq_report(arts: list[tuple[str, dict]], start: int | None) -> dict:
    """seq 之聯集、區間、空洞 —— 跨批方能看見（第二層檢驗）。"""
    per, all_seq = [], []
    for name, d in arts:
        seqs = sorted(t["seq"] for t in (d.get("tcs") or []) if isinstance(t.get("seq"), int))
        per.append((name, len(d.get("tcs") or []), seqs))
        all_seq += seqs
    uniq = sorted(set(all_seq))
    holes, dupes = [], len(all_seq) - len(uniq)
    if uniq:
        expect = set(range(uniq[0], uniq[-1] + 1))
        holes = sorted(expect - set(uniq))
    lead = []
    if start is not None and uniq and uniq[0] > start:
        lead = list(range(start, uniq[0]))
    return {"per": per, "uniq": uniq, "holes": holes, "dupes": dupes, "lead_gap": lead}


def hand_values(arts: list[tuple[str, dict]]) -> tuple[dict, str]:
    """自批次 manifest 之 `selection` 抽手算值。"""
    for name, d in arts:
        m = RE_HAND.search(d.get("selection", "") or "")
        if m:
            return ({k: int(v) for k, v in m.groupdict().items()}, name)
    return {}, ""


def build(c: Corpus) -> tuple[list[Metric], dict]:
    pcfg = c.profile_cfg()
    leaves = c.tsv_rows(pcfg.get("leaves", "").replace(f"{c.feature}/", "") or "")
    iso = c.tsv_rows(f"data/{c.profile}_isolated.tsv")
    arts = c.artifacts()
    hand, hand_src = hand_values(arts)
    start = pcfg.get("seq_start")
    sr = seq_report(arts, start)

    pilots = [(n, k, s) for n, k, s in sr["per"] if "pilot" in n]
    batches = [(n, k, s) for n, k, s in sr["per"] if "batch" in n]

    disagree = sum(1 for r in leaves if str(r.get("disagree", "0")).strip() == "1")
    m: list[Metric] = [
        Metric("leaves_rows", f"`{pcfg.get('leaves')}` 資料列", len(leaves)),
        Metric("leaves_disagree", "其中 `disagree = 1`", disagree),
        Metric("leaves_net", "扣 disagree 後之 leaf 數", len(leaves) - disagree,
               hand.get("pool"), "手算值為「選池」，其基準未必等於本項（見上繳追因）"),
        Metric("pilot_files", "pilot 檔數", len(pilots)),
        Metric("pilot_tcs", "pilot 條數", sum(k for _, k, _ in pilots), hand.get("pilot")),
        Metric("isolated_rows", f"`data/{c.profile}_isolated.tsv` 資料列",
               len(iso), hand.get("iso"), "手算值為立條時之數；其後各輪擴增屬正常"),
        Metric("batch_files", "量產批數", len(batches)),
        Metric("batch_tcs", "量產條數", sum(k for _, k, _ in batches)),
        Metric("seq_start", "`seq_start`（feature.yaml）", start),
        Metric("seq_min", "seq 實測最小", sr["uniq"][0] if sr["uniq"] else None),
        Metric("seq_max", "seq 實測最大", sr["uniq"][-1] if sr["uniq"] else None),
        Metric("seq_count", "seq 相異數", len(sr["uniq"])),
        Metric("seq_dupes", "seq 重複數", sr["dupes"]),
        Metric("seq_holes", "seq 區間內之空洞數", len(sr["holes"]),
               0, "R-VF83：B 欄自 seq_start 起連續遞增 → 預期 0"),
        Metric("seq_lead_gap", "seq_start 至實測最小之未佔用數", len(sr["lead_gap"]), 0),
    ]
    return m, {"seq": sr, "hand_src": hand_src, "hand": hand}


def render(c: Corpus, metrics: list[Metric], extra: dict) -> str:
    sr, hand_src = extra["seq"], extra["hand_src"]
    L = [f"# 預期數字表 —— {c.feature} / {c.profile}（`expected_numbers.py` 產出，R-G16）",
         "",
         "**量測條件**：`feature.yaml` 之 `profiles.%s`；`generated/%s_*.json` 之 `tcs`；"
         "`data/%s_isolated.tsv` 逐列（不含表頭）。" % (c.profile, c.profile, c.profile),
         f"**手算值來源**：`generated/{hand_src}` 之 `selection` 欄。" if hand_src
         else "**手算值來源**：未找到可解析之 `selection` 算式。",
         "",
         "| 指標 | 推導 | 手算 | 判 | 註 |", "|---|---|---|---|---|"]
    for x in metrics:
        L.append(f"| {x.label} | **{x.derived}** | {x.hand if x.hand is not None else '—'} "
                 f"| {x.verdict} | {x.note} |")
    L += ["", "## 產出逐檔", "", "| 檔 | 條數 | seq 區間 |", "|---|---|---|"]
    for name, k, s in sr["per"]:
        rng = f"{s[0]}–{s[-1]}" if s else "無 seq"
        L.append(f"| `{name}` | {k} | {rng} |")
    if sr["holes"]:
        L += ["", f"## ⚠ seq 空洞 {len(sr['holes'])} 個", "",
              "```", ", ".join(map(str, sr["holes"])), "```", "",
              "**空洞不使任何 lint 轉紅** —— 各批自身連續即可，"
              "只有跨批之 seq 聯集看得出來。此即第二層檢驗之落點。"]
    if sr["lead_gap"]:
        L += ["", f"## ⚠ seq_start 之前導空缺 {len(sr['lead_gap'])} 個", "",
              "```", ", ".join(map(str, sr["lead_gap"])), "```"]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="預期數字表（R-G16）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--feature", required=True)
    ap.add_argument("--profile", required=True)
    ap.add_argument("--out", default=None, help="輸出 markdown（省略則印至 stdout）")
    ap.add_argument("--gate", action="store_true", help="任一項不符即 exit 1")
    args = ap.parse_args()

    c = Corpus(Path(args.root).resolve(), args.feature, args.profile)
    c.load()
    metrics, extra = build(c)
    text = render(c, metrics, extra)
    if args.out:
        p = c.root / args.out
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        print(f"寫入 {args.out}")
    else:
        print(text)

    bad = [x for x in metrics if x.verdict == "**不符**"]
    print(f"不符 {len(bad)} 項" + ("：" + "、".join(x.key for x in bad) if bad else ""),
          file=sys.stderr)
    return 1 if (args.gate and bad) else 0


if __name__ == "__main__":
    sys.exit(main())
