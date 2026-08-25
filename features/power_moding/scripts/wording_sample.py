#!/usr/bin/env python3
"""22 包步驟 7 —— 停止條件 8 之**偽陰抽樣**（R-PMH67）。

21 包之停止條件 8 為：「步驟 2 之重記後，仍有任一項記為
**『無矛盾』或『非牴觸』**」—— **列舉式判準，只攔兩個詞**。
21 包 §6 之自檢已具名該弱點：**若改寫成「相容」「未發現問題」，本條攔不下。**

R-PMH67 要求列舉式判準附偽陰之抽樣估計：
自**未被該判準攔下**之母體隨機抽 N >= 10，人讀判其是否「應被攔而未被攔」，
命中數即偽陰率之估計，**與判準、偽陽數及 Wilson 區間一併回報**。

母體：`docs/upstream/*.md` 中含「對照結論型措詞」而**不含該二詞**之行。

用法:
    python scripts/wording_sample.py
"""
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from challenge_rulings import wilson          # noqa: E402  —— 19 包所建，不另維護副本

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "docs" / "upstream"

CAUGHT = ["無矛盾", "非牴觸"]                    # 停止條件 8 所攔者
CANDIDATE = ["一致", "相容", "符合", "吻合", "不衝突", "無衝突",
             "無牴觸", "未發現問題"]              # 可能之同義措詞（**本身亦為列舉**）

SAMPLE_N = 10
SAMPLE_SEED = 22                                # = 本包編號，可重現

LIMITS = [
    "**母體之界定本身是列舉** —— `CANDIDATE` 之八詞為人工列舉，"
    "其外之措詞（如「二者並存」「無此問題」）不入母體，**故本抽樣之母體亦有偽陰**",
    "只掃 `docs/upstream/*.md`；`ANOMALIES.md`／`DECISIONS.md`／程式輸出不入母體",
    "**行級抽樣** —— 一行可能同時是對照結論與別的敘述；其是否為「對照結論」由人讀判",
    "N = 10 之 Wilson 區間寬達數十個百分點 —— **點估計不得單獨引用**",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


# 抽樣之人讀判定 —— 鍵為 (檔名, 行號)
SAMPLE_VERDICT: dict[tuple[str, int], tuple[bool, str]] = {
    ("01_intake.md", 535):
        (False, "非規格×素材之對照結論 —— 其為 `D5` 值於 037／SYS1／封面三方之**同值查核**（identity），且結論為「支持填…惟本包不寫回，待裁」"),
    ("03_testgroup_and_dv.md", 138):
        (True, "**應被攔** —— 此為**對照結論**（母本 DV 之 priority 值 vs canon §10.2）而以「三方一致」記之。若該對照實為「只涵蓋前兩項、後兩項無對應」，「一致」二字會掩蓋之。**與 `10.5` 之「一致（軸層面）」同型**（21 §2 已改記為未對照）"),
    ("03_testgroup_and_dv.md", 148):
        (False, "停止條件之敘述（「…不一致）未觸發」），非對照結論本身"),
    ("03_testgroup_and_dv.md", 563):
        (False, "程式輸出之**同值查核**（`… 與 … 一致 : True`）—— 二者為同一欄位之兩處副本，其「一致」為 identity 而非對照"),
    ("06_framework_proposal.md", 232):
        (False, "anomaly 之描述（「表單層之不一致」）—— 其為**指出不一致**，非以「一致」作結"),
    ("13_batch1_rework.md", 161):
        (False, "條文名稱之引用（R-PMH53 之「語意相容」），非對照結論"),
    ("17_scope_of_inventory.md", 406):
        (False, "lint 之檢查項名稱（程式輸出），非對照結論"),
    ("19_broken_source.md", 322):
        (False, "重跑 diff = 0 之**同值查核** —— identity，非對照"),
    ("21_predicate_criterion.md", 187):
        (False, "停止條件之**自檢**結論（字面與目的是否一致），非規格×素材之對照"),
    ("21_predicate_criterion.md", 286):
        (False, "程式輸出之**同值查核**（靜態彙集 vs 執行期），identity"),
}


def population() -> list[tuple[str, int, str]]:
    out = []
    for f in sorted(UPSTREAM.glob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if any(c in line for c in CAUGHT):
                continue                       # 已被停止條件 8 攔下者不入母體
            if any(c in line for c in CANDIDATE):
                out.append((f.name, i, line.strip()))
    return out


def main() -> None:
    pop = population()
    print("=== 停止條件 8 之偽陰抽樣（R-PMH67）===")
    print(f"停止條件 8 所攔之詞：{CAUGHT}（**2 個**）")
    print(f"母體：`docs/upstream/*.md` 中含 {CANDIDATE} 之一"
          f"**而不含上列二詞**之行 = **{len(pop)}**")
    rng = random.Random(SAMPLE_SEED)
    n = min(SAMPLE_N, len(pop))
    sample = sorted(rng.sample(pop, n))
    print(f"抽樣 N = {n}；種子 = {SAMPLE_SEED}"
          f"（`random.Random({SAMPLE_SEED}).sample`，**可重現**）\n")
    named, pos = 0, 0
    for f, i, line in sample:
        v = SAMPLE_VERDICT.get((f, i))
        print(f"  {f}:{i}")
        print(f"    {line[:150]}")
        if v is None:
            print("    **人讀判定：未具名 ← 抽樣未完成**")
            continue
        named += 1
        pos += 1 if v[0] else 0
        print(f"    {'**應被攔**' if v[0] else '不應被攔'} —— {v[1]}")
    if named == n:
        lo, hi = wilson(pos, n)
        print(f"\n  **偽陰率之點估計 = {pos}/{n} = {pos/n:.0%}**；"
              f"**Wilson 95% 區間 = [{lo:.0%}, {hi:.0%}]**")
        print(f"  推估母體 {len(pop)} 行中應被攔者："
              f"點估計 **{round(len(pop)*pos/n)}** 行，"
              f"**區間 [{round(len(pop)*lo)}, {round(len(pop)*hi)}] 行**")
    else:
        print(f"\n  **抽樣未完成：{n - named} 行未具名人讀判定**")
    print_limits()
    sys.exit(0 if named == n else 1)


if __name__ == "__main__":
    main()
