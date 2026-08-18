"""G150 —— `design_method` 分布與 §12 first-match 走查（R-P223 / T24）。

現行 G72 只驗 `design_method` 是否為下拉選單九詞條之一，
**不驗其選得對不對**。分析層於批次四尾段讀四條見二條可疑，
惟其為推測（R-P64）；本閘為其實測。

§12 之判準（逐字，`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §12，**first-match**）：

  1 Invalid input / illegal op            → Negative / Invalid
  2 Simulated fault (disconnect, timeout) → Fault Injection
  3 State A → State B transition          → State Transition
  4 Multiple conditions → outcome         → Decision Table
  5 Input partitioned valid / invalid     → Equivalence Partitioning
  6 Boundary (=limit, limit±1)            → Boundary Value Analysis
  7 Multi-parameter combination           → Combinatorial
  8 End-to-end flow, ≥3 features          → Scenario / Use Case
  9 Single feature check                  → Functional Based

  Tie-break：State Transition = state-change focus；
             Scenario = ≥3 steps crossing features；
             Functional = 1–2 steps single feature。

**本閘不改任何值**（R-P223(c) / §I）—— 只量測與走查，裁定於 32 包。

用法：
    python features/power/scripts/audit_design_method.py
"""

from __future__ import annotations

import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

SEED = 31            # = 本包往返 NN，載明以可重現
RATE = 1 / 6         # ≥ 16.7%
THRESHOLD = 0.60     # R-P223(b)；**§K 第 1 項自陳其為憑印象所訂，非判準**

# ── 走查結果 ──
# 鍵：tc_id 末三碼。值：(§12 首個命中列, 該列之 method, 是否與現值相符, 依據)
# **逐條由執行層讀其 procedure 與 ER 判定**，非機械推導。
WALK: dict[str, tuple[int, str, bool, str]] = {
 # ── 相符（17）──
 "029": (3, "State Transition", True, "ER 載 TLM **leaves Full-Operation state**，為 A → B"),
 "037": (3, "State Transition", True, "ER 載 `TLM_Status.Info` 轉 `Standby`"),
 "048": (3, "State Transition", True, "FULL OPERATION → IDLE"),
 "051": (3, "State Transition", True, "INIT → Sleep"),
 "055": (3, "State Transition", True, "進入 Partial Operation 並以 `$Telematic_Power$` 回報"),
 "061": (3, "State Transition", True, "→ Timed"),
 "062": (3, "State Transition", True, "→ Standby（雖有多條件，第 3 列先於第 4 列命中）"),
 "070": (3, "State Transition", True, "→ Idle"),
 "073": (3, "State Transition", True, "Idle → Standby"),
 "111": (3, "State Transition", True, "Standby → Partial Operation"),
 "112": (3, "State Transition", True, "Partial Operation → Standby"),
 "229": (3, "State Transition", True, "IDLE → FULL OPERATION"),
 "173": (3, "State Transition", True, "Timed → Standby"),
 "174": (3, "State Transition", True, "Timed → Standby"),
 "185": (3, "State Transition", True, "power mode 變更確有發生（動畫略過為其伴隨結果）"),
 "207": (3, "State Transition", True, "→ Timed mode 之首次轉換"),
 "219": (3, "State Transition", True, "→ Full Operation 之再次轉換"),
 # ── 不相符（26）──
 "024": (1, "Negative / Invalid", False,
         "**第 1 列即命中** —— procedure 為 `Attempt to change` 而 ER 為「控制項停用／值未變」，"
         "即對不允許之操作之否定驗證；全條無任何 A → B"),
 "025": (9, "Functional Based", False,
         "選單設值後讀回，**無狀態轉換**；tie-break 之 Functional（單一功能）較合，"
         "惟其為 3 步，與 tie-break 之「1–2 steps」不完全吻合 —— 仍不屬第 3 列"),
 "030": (9, "Functional Based", False,
         "計時器到期觸發計數器啟動，**ER 未斷言任何狀態變更**；"
         "第 2 列之 `timeout` 指**注入之故障**，本條為正常行為，不命中"),
 "058": (9, "Functional Based", False, "ER 僅 `RemStartFail reads \"True\"` —— 旗標設定，無狀態變更"),
 "096": (4, "Decision Table", False,
         "**ER 逐字為 `still reads \"Timed\"` 與 `stays in Timed state`** —— 明示不轉換；"
         "其為門開啟＋前狀態＋通話三條件之組合結果，命中第 4 列"),
 "101": (4, "Decision Table", False,
         "條件（防盜成功 ＋ `SwitchOff_Timeout_Setting.Req == 00 min`）→ Timeout1 取值；無狀態變更"),
 "128": (9, "Functional Based", False, "查 FPDM / AMP / ICS / DTV 之可用性，無狀態變更"),
 "135": (9, "Functional Based", False,
         "ER 為旗標設為 `True` 與畫面顯示，**未斷言狀態變更**"),
 "137": (4, "Decision Table", False, "**ER 明示 `stays in the original Sleep state`** —— 不轉換"),
 "138": (9, "Functional Based", False, "提供影音，無狀態變更"),
 "140": (4, "Decision Table", False, "**ER 明示 `stays in the original Standby state`** —— 不轉換"),
 "177": (4, "Decision Table", False,
         "條件（長按 ＋ 韌體安裝中）→ 不重置；**ER 為否定結果且無狀態變更**"),
 "202": (9, "Functional Based", False, "查音訊關閉與畫面限制，無狀態變更"),
 "203": (9, "Functional Based", False, "同 `202`"),
 "204": (9, "Functional Based", False, "同 `202`"),
 "152": (4, "Decision Table", False,
         "`SDARS_Presence` ＋ `Audio_Brand` 二條件 → logo 呈現；無狀態變更"),
 "156": (4, "Decision Table", False,
         "`$VC_SpecialPKG_IC$` ＋ `$VC_MODEL_YEAR$` ＋ `$VC_VEH_LINE$` → 畫面；無狀態變更"),
 "158": (9, "Functional Based", False, "單一 DID 值 → logo 取代，無狀態變更"),
 "190": (9, "Functional Based", False, "設定值 → 是否伴隨開機音，無狀態變更"),
 "222": (9, "Functional Based", False,
         "跨多個點火循環查顯示頻率；**非第 6 列之邊界值**（30 為週期而非門檻±1）"),
 "231": (9, "Functional Based", False, "設定值 → 主題來源，無狀態變更"),
 "235": (9, "Functional Based", False, "觀察匯流排送值，無狀態變更"),
 "238": (9, "Functional Based", False,
         "品牌值 → 字型映射，無狀態變更（其亦近第 5 列之值域切分，惟第 5 列在第 9 列之前，"
         "**若視為值域切分則應為 Equivalence Partitioning** —— 二者皆非現值）"),
 "243": (9, "Functional Based", False, "同 `238`，映射至 avatar 清單"),
 "255": (4, "Decision Table", False,
         "`Theme Mode == Auto` ＋ `$Day_Night_Mode$` 二條件 → 主題；無狀態變更"),
 "261": (6, "Boundary Value Analysis", False,
         "**第 6 列即命中** —— `An Ignition On **after the date passes June, 21st**` "
         "為日期界線之驗證，屬 limit / limit±1"),
}


def load() -> dict[str, list[dict]]:
    out = defaultdict(list)
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        for tc in b["tcs"]:
            out[tc["test_set"]].append(tc)
    return out


def main() -> None:
    tcs = load()
    total = Counter()
    for ts in tcs:
        for t in tcs[ts]:
            total[t["design_method"]] += 1
    n = sum(total.values())

    out = ["# G150 —— `design_method` 分布與 §12 first-match 走查（R-P223 / T24）\n",
           "\n> **本閘不改任何值**（R-P223(c) / §I）—— 只量測與走查，裁定於 32 包。\n",
           f"\n## 1. 全批分布（{n} 條）\n\n| design_method | 條 | 佔比 |\n|---|---|---|\n"]
    for v, c in total.most_common():
        out.append(f"| {v} | **{c}** | {c/n*100:.1f}% |\n")

    out.append("\n## 2. 逐 Test Set 分布\n\n"
               "| Test Set | 條 | 最大值 | 佔比 | ≥ 60% |\n|---|---|---|---|---|\n")
    groups = []
    for ts in sorted(tcs):
        c = Counter(t["design_method"] for t in tcs[ts])
        top, cnt = c.most_common(1)[0]
        s = sum(c.values())
        hit = cnt / s >= THRESHOLD
        if hit:
            groups.append((ts, top))
        out.append(f"| {ts} | {s} | {top} | **{cnt/s*100:.1f}%** | "
                   f"{'**是**' if hit else '否'} |\n")

    rng = random.Random(SEED)
    sampled = []
    out.append(f"\n## 3. 抽樣（種子 `random.Random({SEED})`，率 ≥ 16.7%）\n\n"
               "| Test Set | 母體 | 抽樣 | 率 |\n|---|---|---|---|\n")
    for ts, top in groups:
        pool = [t for t in tcs[ts] if t["design_method"] == top]
        k = max(1, -(-len(pool) * 1 // 6))
        s = rng.sample(pool, k)
        sampled += s
        out.append(f"| {ts} | {len(pool)} | **{k}** | {k/len(pool)*100:.1f}% |\n")
    out.append(f"| **合計** | {sum(len([t for t in tcs[ts] if t['design_method']==top]) for ts, top in groups)} | "
               f"**{len(sampled)}** | {len(sampled)/sum(len([t for t in tcs[ts] if t['design_method']==top]) for ts, top in groups)*100:.1f}% |\n")

    sampled.sort(key=lambda t: t["tc_id"])
    ok = [t for t in sampled if WALK.get(t["tc_id"][-3:], (0, "", None, ""))[2]]
    bad = [t for t in sampled if WALK.get(t["tc_id"][-3:], (0, "", None, ""))[2] is False]
    out.append(f"\n## 4. §12 逐列 first-match 走查\n\n"
               f"**相符 {len(ok)} / {len(sampled)}；不符 {len(bad)} / {len(sampled)} "
               f"= {len(bad)/len(sampled)*100:.1f}%**\n\n"
               "| tc_id | Test Set | 現值 | §12 首個命中列 | 應為 | 相符 | 依據 |\n"
               "|---|---|---|---|---|---|---|\n")
    # **R-P227 / R-P214（38 包）**：`WALK` 為 **32 包之人工走查結果**，
    # 其母體為當時之 `design_method` 值。38 包第二級改值後母體改變，
    # 抽樣會取到未走查之 TC —— **人工走查不可機械重生**，
    # 故不補寫，改為明確標示並回報其數。
    unwalked = [t for t in sampled if t["tc_id"][-3:] not in WALK]
    if unwalked:
        print(f"  **{len(unwalked)} / {len(sampled)} 條不在 32 包之人工走查表內** "
              f"{[t['tc_id'][-3:] for t in unwalked]}")
        print("  —— 母體因 38 包改值而變；人工走查不可機械重生（R-P214），本表之"
              "「不符率」自此僅對其交集有效。")
    for t in sampled:
        if t["tc_id"][-3:] not in WALK:
            out.append(f"| `{t['tc_id'][-3:]}` | {t['test_set']} | "
                       f"{t['design_method'].split(' (')[0]} | — | — | "
                       f"**未走查** | 母體因 38 包改值而變（R-P227） |\n")
            continue
        row, method, same, why = WALK[t["tc_id"][-3:]]
        out.append(f"| `{t['tc_id'][-3:]}` | {t['test_set']} | "
                   f"{t['design_method'].split(' (')[0]} | 第 **{row}** 列 | {method} | "
                   f"{'是' if same else '**否**'} | {why} |\n")

    (DATA / "g150_design_method.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g150_design_method.md').relative_to(ROOT)}")
    print(f"  全批 {n} 條；狀態轉換 {total['狀態轉換 (State Transition Testing)']} "
          f"（{total['狀態轉換 (State Transition Testing)']/n*100:.1f}%）")
    print(f"  ≥ {THRESHOLD:.0%} 之 Test Set：{len(groups)}")
    print(f"  抽樣 {len(sampled)}；**相符 {len(ok)}、不符 {len(bad)} "
          f"（{len(bad)/len(sampled)*100:.1f}%）**")


if __name__ == "__main__":
    main()
