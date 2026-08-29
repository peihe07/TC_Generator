#!/usr/bin/env python3
"""T24e／T26b（下放包 18 §四、20 §五）—— 出貨就緒盤點。**只盤點，不寫回。**

可否出貨之判準**由產物導出**（IN §8.4.3：含 PENDING 之工作簿不得出貨），
非以 leaf 號或批次名硬編（R-DD23(ii)）。
**範圍外名單同樣不硬編** —— 自 profile §5 與 framework.md **二處各自導出並交叉核對**
（T26b；`-025`~`-028` 已由 R-DD25(b) 自凍結改判範圍外）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "generated"
PROFILE = ROOT.parent.parent / "docs" / "runtime" / "profiles" / \
    "FW036_R1L_DriverDistraction_Profile.md"
FOUR = ["pre_conditions", "input_test_data", "test_procedure", "expected_result"]
ARTS = ["pilot_group3.json", "batch_b1.json", "batch_b2.json",
        "batch_body_off_init.json"]
TOTAL_LEAF = 28                      # 037 之 28 leaf（framework.md Part I）

rows = []
for a in ARTS:
    for tc in json.loads((GEN / a).read_text("utf-8")):
        body = " ".join(tc[f] for f in FOUR)
        pend = re.findall(r"PENDING: DR-\w+\d+", body)          # IN §8.4.3
        mk = sorted(set(re.findall(r"\[ASSUMPTION (A-DD\d+)\]", body)))
        rows.append({
            "art": a.replace(".json", ""), "tc_id": tc["tc_id"],
            "leaf": tc["req_id"][-3:], "set": tc["test_set"],
            "pri": tc["priority"], "mk": mk, "pend": pend,
            "ship": not pend,
        })
rows.sort(key=lambda r: r["leaf"])

# ── 範圍外 leaf（T26b；下放包 20 §五）────────────────────────────
# **判準改讀「範圍外名單」**，且**不硬編 leaf 號** —— 自二處各自導出後**交叉核對**：
#   (甲) profile §5：狀態欄含「範圍外」之列，取其「範圍」欄之 leaf 區間
#   (乙) framework.md Part II：能力叢集欄含 `OUT OF SCOPE` 之組，取其 leaf 區間
# 二者須**完全相同**；不同即停並回報（單一來源會讓其中一處漏改而無人知）。
# 10-5（下放包 21 §四）：**支援逐列列舉**，且**空集合即異常**。
# 執行層上繳 17 §8.2-2 所指之最壞失效態：前版只認 `NNN–NNN`，
# 若二來源同時改以逐列列舉書寫，**二者會一致地取到空集合而通過交叉核對**
# —— **一致地錯比不一致更難發現**（不一致至少會停）。
# 故：(i) 二式皆解析；(ii) 任一來源取得空集合即 SystemExit
#（framework 組 6 恆存在，空集合本身即為解析失敗之徵候，非合法狀態）。
RE_RANGE = re.compile(r"(\d{3})\s*[–—\-~〜]\s*(\d{3})")
RE_SINGLE = re.compile(r"(?<!\d)(\d{3})(?!\d)")


def _span(text):
    """解析 leaf 名單：先取區間式，再把區間外之孤立三位數視為逐列列舉。"""
    out, consumed = set(), []
    for m in RE_RANGE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        out |= {f"{n:03d}" for n in range(lo, hi + 1)}
        consumed.append((m.start(), m.end()))
    for m in RE_SINGLE.finditer(text):
        if any(s <= m.start() < e for s, e in consumed):
            continue                      # 已由區間式吃掉，不重複計
        out.add(m.group(1))
    return out


def _from_profile():
    sec = PROFILE.read_text("utf-8").split("## §5 凍結與未結")[1].split("\n---")[0]
    out = set()
    for line in sec.split("\n"):
        if not line.startswith("|") or "範圍外" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2:
            out |= _span(cells[1])          # 「範圍」欄
    return out


def _from_framework():
    fw = (ROOT / "framework.md").read_text("utf-8")
    out = set()
    for line in fw.split("\n"):
        if re.match(r"^\|\s*\d+\s*\|", line) and "OUT OF SCOPE" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3:
                out |= _span(cells[2])      # 「leaf」欄
    return out


oos_p, oos_f = _from_profile(), _from_framework()
# (ii) 空集合即異常 —— 二來源同時解析失敗時，`oos_p == oos_f == set()` 會通過
# 相等比對而「一致地錯」。故先各自驗非空，再比相等。
for _name, _s in (("profile §5", oos_p), ("framework Part II", oos_f)):
    if not _s:
        raise SystemExit(f"**{_name} 之範圍外名單解析為空** —— framework 組 6 恆存在，"
                         f"空集合為解析失敗之徵候，非合法狀態；停並回報")
if oos_p != oos_f:
    raise SystemExit(f"**範圍外名單二來源不一致** —— profile §5 {sorted(oos_p)} "
                     f"／framework Part II {sorted(oos_f)}；停並回報")
oos = sorted(oos_p)

gen = {r["leaf"] for r in rows}
ship = [r for r in rows if r["ship"]]
hold = [r for r in rows if not r["ship"]]

W = "=" * 96
print(W); print("T24e —— 出貨就緒盤點（只盤點，不寫回）"); print(W)
print(f"{'tc_id':<16}{'leaf':<6}{'Test Set':<22}{'pri':<5}{'marker':<26}出貨")
print("-" * 96)
for r in rows:
    flag = "可" if r["ship"] else f"**不可**（{'／'.join(r['pend'])}）"
    print(f"{r['tc_id']:<16}{r['leaf']:<6}{r['set']:<22}{r['pri']:<5}"
          f"{'／'.join(r['mk']) or '（無）':<26}{flag}")
print("-" * 96)
print(f"已產出 {len(rows)}　＝　可出貨 {len(ship)} ＋ 不得出貨 {len(hold)}")
print(f"範圍外（profile §5 ∩ framework Part II，二來源一致）{len(oos)}：{oos}")
tot = len(ship) + len(hold) + len(oos)
print(f"閉合：可出貨 {len(ship)} ＋ 不得出貨 {len(hold)} ＋ 範圍外 {len(oos)} ＝ {tot}"
      f"　對 28 leaf：{'✅ 閉合' if tot == TOTAL_LEAF else '❌ **不閉合**'}")
overlap = sorted(gen & set(oos))
missing = sorted({f"{n:03d}" for n in range(1, TOTAL_LEAF + 1)} - gen - set(oos))
print(f"已產出∩範圍外（須為空）：{overlap or '空 ✓'}")
print(f"既未產出亦未範圍外（須為空）：{missing or '空 ✓'}")
print(W)
raise SystemExit(0 if tot == TOTAL_LEAF and not overlap and not missing else 1)
