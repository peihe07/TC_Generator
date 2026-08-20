"""R-P345(a) —— 錨點歸屬之提案（B1 之前半）。

R-P343 令 `test_item` 首段 = **該 TC 所直接驗證之錨點之文字，逐字**。
125 / 280 條之 leaf 只有一個錨點，歸屬唯一；其餘 **155 條**須判斷。

## 與 52 包選句器之別

52 包之 `pick_first_segment.py` 自**連續文字中切句**，實測 4 / 6，
依 R-P250 判定不得使用（R-P345 追認）。本檔之單位不同 ——
**自 N 個既已切開之錨點中擇一**，其邊界由 §C 之錨點鏈給定而非由本檔劃出，
且 `split_reason` 多已言明該 TC 所驗之面向（155 / 155 皆有）。

計分為 IDF 加權之 **F1**（覆蓋率與精確率之調和平均）——
只用覆蓋率會使長錨點（`4941453` 之 4,259 字元）恆勝。

**其為提案，非裁決**（R-P345）。分析層抽樣複核 ≥ 20% 見 `--review`。

用法：
    python features/power/scripts/propose_anchor_53.py --self-test
    python features/power/scripts/propose_anchor_53.py --propose
    python features/power/scripts/propose_anchor_53.py --review [種子]
"""

from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402

# 49 包 R-P319 入庫之二份 RTF，其文字層僅存檔名一行 ——
# 非規格陳述，不得為任一 TC 之主要錨點。
STUB = re.compile(r"WrapperResource\s*$")

STOP = set("""a an the is are was were be been being of to in on at by for with
from as and or not no if then this that these those it its shall must has have
had do does did will would can could may might been which when while after
before only also into out up down over under such per each any all both same
other another there their they them we you i""".split())


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[A-Za-z_$][A-Za-z0-9_$.]*", text.lower())
            if w not in STOP and len(w) > 2}


def load():
    rows = []
    for f in sorted(GENERATED.glob("batch_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        bp = {l["parent"]: l for l in d["leaves"]}
        for tc in d["tcs"]:
            rows.append((tc, bp[tc["req_id"]], f.name))
    return rows


def propose_one(tc: dict, leaf: dict, bodies: dict) -> tuple[str, float, list]:
    ans = [a.strip() for a in str(leaf["source_anchor"]).split(",") if a.strip()]
    texts = {a: "\n".join(bodies.get(a, [])) for a in ans}
    live = [a for a in ans if texts[a].strip() and not STUB.search(texts[a].strip())]
    if len(live) <= 1:
        only = live[0] if live else ans[0]
        return only, 1.0, [(only, 1.0)]

    target = words(" ".join((tc.get("tc_title", ""),
                             tc.get("expected_result", ""),
                             tc.get("test_procedure", ""),
                             str(tc.get("split_reason", "")))))
    df = {}
    for a in live:
        for w in words(texts[a]):
            df[w] = df.get(w, 0) + 1
    n = len(live)
    idf = {w: (n / k) ** 0.5 for w, k in df.items()}

    def wsum(s):
        return sum(idf.get(w, 1.0) for w in s)

    scored = []
    for a in live:
        cw = words(texts[a])
        inter = wsum(cw & target)
        if not inter:
            scored.append((a, 0.0))
            continue
        rec = inter / wsum(target) if target else 0.0
        pre = inter / wsum(cw) if cw else 0.0
        scored.append((a, 2 * rec * pre / (rec + pre) if rec + pre else 0.0))
    scored.sort(key=lambda x: -x[1])
    return scored[0][0], scored[0][1], scored


# R-P250：跑之前依人讀 `split_reason` / ER / 錨點文字判定
EXPECTED = {
    "NR1L-PowerManagement-060": "4941507",   # SR「Behaviour 1 之通話中分支」→ Phone_Call.Info == Active
    "NR1L-PowerManagement-095": "4941577",   # SR「前狀態為 Standby 之分支」
    "NR1L-PowerManagement-150": "4941674",   # SR「組合二（Absent ＋ Beats Brand White）」
    "NR1L-PowerManagement-200": "4941365",   # 所驗之行為（audio OFF＋僅 Splash）；4941364 為情境前提
    "NR1L-PowerManagement-255": "4942096",   # 12/21 之日期只在此錨點
    "NR1L-PowerManagement-270": "4941400",   # SR「Stolen Vehicle Mode 之否定規定」
}


def self_test() -> int:
    bodies = anchor_bodies()
    rows = {tc["tc_id"]: (tc, leaf) for tc, leaf, _ in load()}
    bad = 0
    for tid, want in EXPECTED.items():
        tc, leaf = rows[tid]
        got, s, scored = propose_one(tc, leaf, bodies)
        ok = got == want
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} {tid}  提案={got} (F1={s:.2f})"
              + ("" if ok else f"  期望={want}"))
        if not ok:
            for a, sc in scored[:4]:
                print(f"      {a} {sc:.3f}{'  ← 期望' if a == want else ''}")
    print(f"\n自驗：{len(EXPECTED) - bad} / {len(EXPECTED)} 相符")
    return 1 if bad else 0


def propose() -> int:
    bodies = anchor_bodies()
    rows = load()
    out, uniq, multi = [], 0, 0
    for tc, leaf, _ in rows:
        ans = [a.strip() for a in str(leaf["source_anchor"]).split(",") if a.strip()]
        a, s, _ = propose_one(tc, leaf, bodies)
        determined = len(ans) == 1
        uniq += determined
        multi += not determined
        out.append({"tc_id": tc["tc_id"], "req_id": tc["req_id"],
                    "anchor": a, "f1": round(s, 3),
                    "determined": determined,
                    "n_candidates": len(ans),
                    "basis": str(tc.get("split_reason", "")).strip(),
                    "anchor_len": len("\n".join(bodies.get(a, [])))})
    (DATA / "anchor_attribution_53.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"提案 {len(out)} 條：歸屬唯一 {uniq}、須判斷 {multi}")
    print(f"逾 1,000 字元（R-P343(c) 須取片段）：{sum(1 for x in out if x['anchor_len'] > 1000)}")
    print(f"→ features/power/data/anchor_attribution_53.json")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    raise SystemExit(propose())
