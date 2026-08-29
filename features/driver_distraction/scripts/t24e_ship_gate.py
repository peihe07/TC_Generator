#!/usr/bin/env python3
"""T24e／T26b（下放包 18 §四、20 §五）—— 出貨就緒盤點。**只盤點，不寫回。**

可否出貨之判準**由產物導出**（IN §8.4.3：含 PENDING 之工作簿不得出貨），
非以 leaf 號或批次名硬編（R-DD23(ii)）。
**範圍外名單同樣不硬編** —— 自 profile §5 與 framework.md **二處各自導出並交叉核對**
（T26b；`-025`~`-028` 已由 R-DD25(b) 自凍結改判範圍外）。
"""
import json
import re
import unicodedata
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
#
# ⚠ 本註前版所記之前提**不實，已更正**（下放包 22 §1.1；上繳 18 §4.3 之實測）：
#   前版書「二者會一致地取到空集合而通過交叉核對 —— 一致地錯比不一致更難發現」。
#   **實測舊解析器對該注入為 `exit 1`** —— 交叉核對確實通過，但整體閘門仍由
#   閉合總數（範圍外 0 → 24 ≠ 28）與第三項覆核（既未產出亦未範圍外）各自攔下。
#   **故其失效態不是「靜默地錯」，是「停對了，但指錯地方」。**
#   本改法之淨新增價值在**二式混用**（一方區間、一方列舉）—— 舊版誤停，新版正確通過。
#
# 故：(i) 二式皆解析；(ii) 標記與解析結果須自洽（見下方 _oos_sources）。
# ── T28c（下放包 22 §六 11-5）：解析之收斂 ────────────────────────
# (1) 破折號不再手列 —— 以 Unicode 類別 `Pd`（Dash_Punctuation）判定，
#     另明列非 Pd 之波浪號例外（`~` 為 Sm、`〜` 為 Po）。**手列字集自此不再擴充。**
# (2) `RE_SINGLE` 加**值域閘**：所得三位數須落於本 feature 之 leaf 域；
#     域外命中**不靜默丟棄**，一律 WARN 並列出其原文（R-DD24 之精神）。
LEAF_LO, LEAF_HI = 1, TOTAL_LEAF          # 本 feature 之 leaf 域 001–028
_PD = "".join(chr(c) for c in range(0x2010, 0x2016)) + "-֊־᐀᠆"
_DASH = "".join(sorted({c for c in _PD if unicodedata.category(c) == "Pd"}
                       | {"-"} | {"~", "～", "〜"}))   # 非 Pd 之波浪號例外
RE_RANGE = re.compile(r"(\d{3})\s*[" + re.escape(_DASH) + r"]\s*(\d{3})")
RE_SINGLE = re.compile(r"(?<!\d)(\d{3})(?!\d)")
oos_warn = []                              # 值域外之命中（WARN，不靜默丟棄）


def _span(text, where):
    """解析 leaf 名單：先取區間式，再把區間外之孤立三位數視為逐列列舉。

    值域外之命中不計入名單，但**逐筆記入 `oos_warn`** —— 母體乾淨不等於判準嚴謹。
    """
    out, consumed = set(), []
    for m in RE_RANGE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        if not (LEAF_LO <= lo <= LEAF_HI and LEAF_LO <= hi <= LEAF_HI):
            oos_warn.append((where, "區間", m.group(0)))
            continue
        out |= {f"{n:03d}" for n in range(lo, hi + 1)}
        consumed.append((m.start(), m.end()))
    for m in RE_SINGLE.finditer(text):
        if any(s <= m.start() < e for s, e in consumed):
            continue                       # 已由區間式吃掉，不重複計
        if not (LEAF_LO <= int(m.group(1)) <= LEAF_HI):
            oos_warn.append((where, "單值", m.group(1)))
            continue
        out.add(m.group(1))
    return out


# ── T28b（下放包 22 §五 11-4）：空集合之出口 ──────────────────────
# 前版之「framework 組 6 恆存在」為**外部事實假設**，範圍外名單日後合法為空時會誤停。
# 改為**自結構導出**：以「該來源有無範圍外之標記」與「其解析結果是否為空」之**自洽**為準。
def _oos_sources():
    """回傳 {來源名: (有無標記, 解析所得之 leaf 集合)}。"""
    sec = PROFILE.read_text("utf-8").split("## §5 凍結與未結")[1].split("\n---")[0]
    p_marked, p_set = False, set()
    for line in sec.split("\n"):
        if line.startswith("|") and "範圍外" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                p_marked = True
                p_set |= _span(cells[1], "profile §5")      # 「範圍」欄

    fw = (ROOT / "framework.md").read_text("utf-8")
    f_marked, f_set = False, set()
    for line in fw.split("\n"):
        if re.match(r"^\|\s*\d+\s*\|", line) and "OUT OF SCOPE" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3:
                f_marked = True
                f_set |= _span(cells[2], "framework Part II")   # 「leaf」欄
    return {"profile §5": (p_marked, p_set), "framework Part II": (f_marked, f_set)}


SRC_OOS = _oos_sources()

# (i) 標記有無須二來源一致 —— 一有一無與名單不一致同級
_marks = {k: v[0] for k, v in SRC_OOS.items()}
if len(set(_marks.values())) != 1:
    raise SystemExit(f"**範圍外標記之有無二來源不一致** —— {_marks}；停並回報")

# (ii) 有標記而解析為空 → 停（解析失敗之徵候）；無標記而為空 → **合法，通過**
for _n, (_mk, _s) in SRC_OOS.items():
    if _mk and not _s:
        raise SystemExit(f"**{_n} 有範圍外之標記而解析結果為空** —— "
                         f"解析失敗之徵候，非合法狀態；停並回報")

# (iii) 再比名單相等
oos_p, oos_f = SRC_OOS["profile §5"][1], SRC_OOS["framework Part II"][1]
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
_mk = SRC_OOS["profile §5"][0]
print(f"範圍外（profile §5 ∩ framework Part II，二來源一致；標記 "
      f"{'有' if _mk else '**無** —— 合法為空'}）{len(oos)}：{oos}")
if oos_warn:
    print(f"[WARN] leaf 域（{LEAF_LO:03d}–{LEAF_HI:03d}）外之命中 {len(oos_warn)} 筆，"
          f"**未計入名單，亦未靜默丟棄**：{oos_warn}")
tot = len(ship) + len(hold) + len(oos)
print(f"閉合：可出貨 {len(ship)} ＋ 不得出貨 {len(hold)} ＋ 範圍外 {len(oos)} ＝ {tot}"
      f"　對 28 leaf：{'✅ 閉合' if tot == TOTAL_LEAF else '❌ **不閉合**'}")
overlap = sorted(gen & set(oos))
missing = sorted({f"{n:03d}" for n in range(1, TOTAL_LEAF + 1)} - gen - set(oos))
print(f"已產出∩範圍外（須為空）：{overlap or '空 ✓'}")
print(f"既未產出亦未範圍外（須為空）：{missing or '空 ✓'}")
print(W)
raise SystemExit(0 if tot == TOTAL_LEAF and not overlap and not missing else 1)
