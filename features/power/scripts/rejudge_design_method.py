"""G154 / G155 —— `design_method` 之機械提案與「明示不轉換」閘門（R-P226）。

31 包實測不符率 **60.5%**（26 / 43，抽樣率 17.4%）。R-P226：
「抽樣之不符率不得僅套用於抽中之 26 條 —— 其餘 204 條之不符率應與之相當，
 **故須全數重判**」，且「**重判不得由同一理解逕行為之**」。

方法（R-P226(a)–(d)）：
  (a) 將 §12 之**可機械判定者**實作為逐列謂詞，產出**首個命中列之提案**
  (b) 機械提案與現值相同者 → 「相符」，不改
  (c) 二者相異者 → **逐條人工裁決**，列首個命中列、命中字串、依據
  (d) 機械無法判定者（如第 4 列「多條件 → 結果」）→ **全數入人工裁決**，
      不得由機械預設

**詞彙自本語料導出**（比照 R-P83）—— 其出現次數見上繳 §五之導出表，
非憑印象列舉。

**本腳本不改任何值**（R-P226 / §I）—— 只產出提案與裁決清單，改值於 33 包。

用法：
    python features/power/scripts/rejudge_design_method.py
    python features/power/scripts/rejudge_design_method.py --self-test   # G154 fixture
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

ST = "狀態轉換 (State Transition Testing)"

# ── G154：ER 之「明示不轉換」措詞 ──
# **自本語料導出**（括號內為全批出現次數，31→32 包實測）：
#   stays in 15、still reads 7、remains in 5、unchanged 2、still at 2、
#   does not change 1、does not pass 1、no change 1、not reset 1
NO_TRANSITION_RE = re.compile(
    r"stays? in|still reads?|remains? in|unchanged|still at|"
    r"does not change|does not pass|no change|does not reset|not reset", re.I)

# ── §12 逐列謂詞（可機械判定者）──
# 第 1 列 Negative / Invalid：對不被允許之操作之驗證
ROW1_RE = re.compile(r"attempt to|invalid|illegal|not allowed", re.I)
# 第 2 列 Fault Injection：**注入之故障**。
# `bus error` 不納入 —— 其於本語料皆為 `without a bus error` 之否定斷言（45 次）
ROW2_RE = re.compile(r"disconnect|inject(?:ed|ion)? (?:a )?fault|fault injection", re.I)
# **R-P232（33 包）**：`050` 之 `disconnect` 出自前提 `The battery is disconnected`，
# 其所驗者為「重接後之還原與起始狀態」，**非斷電本身之反應** —— 故第 2 列不命中。
# 判準立為通則：作為情境建構之前提者不適用第 2 列。
# ── 第 3 列 State Transition ──
#
# **R-P231（33 包）：`ROW3_RE` 不放寬** —— 放寬使 174 條落回現值，
# 而現值正是 95.8% 偏向之來源；該作法以判準遷就既有答案。
# **改建對稱之正向謂詞 `POSITIVE_RE`**：命中者為第 3 列之**正向確認**，非默認。
#
# 詞彙**自本語料導出**（ER 全文之實測次數，33 包）：
#   passes to 38、reaches 21、is in <X> state/mode 12、transitions to 6、
#   leaves 6、switches to 4、transitions from 4、returns to 4、
#   transition to 3、transitions back 2、goes to 2、enters 1、starts from 1
#
# `reaches`（21）**不納入** —— 其於本語料多為 `reaches its expiration`
# （計時器到期）與 `reaches Timed mode`，前者非狀態轉換；
# 為免以高頻詞灌入第 3 列，僅取其 `reaches <狀態名> mode/state` 之形態。
POSITIVE_RE = re.compile(
    r"passes to|passes in|transitions? (?:to|from|back to)|transition to|"
    r"goes to|switches to|returns to \w+ (?:state|mode)|"
    r"enters? (?:low power|standby|sleep|idle|timed|full)|"
    r"leaves? \w+ (?:state|mode)|starts from \w+ state|"
    r"is in [A-Za-z][\w -]*? (?:state|mode)|"
    r"reaches [A-Za-z][\w -]*? (?:state|mode)", re.I)
ROW3_RE = POSITIVE_RE          # 舊名保留，指向正向謂詞
# 第 6 列 Boundary：界線值
ROW6_RE = re.compile(r"after the date passes|boundary|the day before|"
                     r"limit(?:\b|±)|greater than", re.I)
# 第 4 列之「多條件」—— **不機械判定**（R-P226(d)），僅計前提中之條件數供人參考
COND_RE = re.compile(r"^\s*\d+\.", re.M)



# ── 人工裁決（R-P226(c)(d)）──
# 鍵：tc_id 末三碼。值：(裁定列, 裁定 method, 依據)
# **本包不改值** —— 此為裁決紀錄，改值於 33 包。
ADJUDICATION: dict[str, tuple[int | None, str, str]] = {
 # 二矛盾之裁決（R-P231(d)，33 包）—— 正向謂詞與 G154 同時命中
 "034x": (4, "Decision Table（維持 32 包之裁決）",
          "**矛盾成因**：正向謂詞命中之 `transition to` 位於**否定句** "
          "`no transition to …`；ER 另載 `remains in Timed state`。"
          "**實質為不轉換**，32 包之第 4 列裁決正確"),
 "071x": (9, "Functional Based（維持 32 包之裁決）",
          "**矛盾成因**：正向謂詞命中之 `passes to` 其主語為**訊號值**"
          "（`Rear_Camera_Enable.Info passes to \"False\"`）**而非狀態**；"
          "ER1 載 `stays in Full-Operation state`。"
          "**正向謂詞未區分狀態轉換與訊號值變化**，此為其已知限度"),
 "050x": (3, "State Transition（維持現值）",
          "依 **R-P232** 第 2 列不命中（斷電為情境建構），first-match 續判；"
          "ER1 載 `The TLM **leaves INIT state** once the voltage is within its "
          "thresholds` → 第 3 列正向命中。**32 包之待裁就此結案**"),
 # 8 條「相異」之裁決
 "010": (3, "State Transition（維持現值）",
         "**謂詞偽陽性** —— 命中之 `limit` 出自 `volume limit`（音量上限），"
         "非 §12 第 6 列之 limit / limit±1。ER2 載 `returns to its normal maximum`，確有恢復之變化"),
 "011": (4, "Decision Table（維持現值）", "同 `010` 之偽陽性；現值決策表不動"),
 "024": (1, "Negative / Invalid", "procedure 為 `Attempt to change`，ER 為控制項停用／值未變；全條無 A → B"),
 "050": (None, "**待裁**",
         "命中之 `disconnect` 出自前提 `The battery is disconnected` —— "
         "§12 第 2 列逐字列 `disconnect` 為 simulated fault 之例，"
         "**惟本條之斷電為情境建構（重接後驗設定還原），非注入故障以觀察容錯**。"
         "二讀皆有據，**執行層不自行決定**"),
 "259": (6, "Boundary Value Analysis", "季節起始日（12/21）為界線值"),
 "260": (6, "Boundary Value Analysis", "季節起始日（3/20）為界線值"),
 "261": (6, "Boundary Value Analysis", "季節起始日（6/21）為界線值"),
 "262": (6, "Boundary Value Analysis", "季節起始日（9/23）為界線值"),
}
# G154 命中者之裁決 —— 皆為「ER 明示不轉換而標狀態轉換」，**全部不符**。
# 其應落之列依「條件數 → 結果」與「單一功能檢查」二分。
_G154_ROW4 = ["031", "034", "035", "075", "077", "081", "088", "092", "095",
              "096", "097", "099", "136", "137", "140", "141", "150", "177"]
_G154_ROW9 = ["028", "030", "032", "056", "071", "130"]
for _k in _G154_ROW4:
    ADJUDICATION.setdefault(_k, (4, "Decision Table",
        "ER **明示不轉換**（G154 命中）；其結果由二個以上之條件決定 → 第 4 列"))
for _k in _G154_ROW9:
    ADJUDICATION.setdefault(_k, (9, "Functional Based",
        "ER **明示不轉換**（G154 命中）；單一功能之檢查 → 第 9 列"))


def fields(tc: dict) -> tuple[str, str, str, str]:
    return (str(tc.get("expected_result", "")), str(tc.get("test_procedure", "")),
            str(tc.get("input_test_data", "")), str(tc.get("pre_conditions", "")))


def propose(tc: dict) -> tuple[int | None, str, str]:
    """回傳（首個命中列, 該列之 method, 命中字串）；None 表機械無法判定。"""
    er, proc, data, pre = fields(tc)
    allt = f"{proc}\n{data}\n{er}"
    m = ROW1_RE.search(proc) or ROW1_RE.search(er)
    if m:
        return 1, "Negative / Invalid", m.group(0)
    # 第 2 列（R-P232，33 包）：**其故障須為驗證之對象** ——
    # 作為情境建構之前提者不適用（其故障不被觀察，僅用以建立起始條件）。
    # 實作：故障詞須見於 `input_test_data` 或 `test_procedure`（即注入之刺激），
    # **僅見於 `pre_conditions` 者不命中**。
    m = ROW2_RE.search(f"{data}\n{proc}")
    if m:
        return 2, "Fault Injection", m.group(0)
    # 第 3 列：**正向確認**（R-P231(b)）。
    # 「明示不轉換」與正向謂詞同時命中者 → **矛盾**，逐條人工裁決（R-P231(d)）。
    neg = NO_TRANSITION_RE.search(er)
    pos = POSITIVE_RE.search(er)
    if neg and pos:
        return -1, "**矛盾（正向與明示不轉換同時命中）**", f"{pos.group(0)} ／ {neg.group(0)}"
    if pos:
        return 3, "State Transition", pos.group(0)
    m = ROW6_RE.search(allt)
    if m:
        return 6, "Boundary Value Analysis", m.group(0)
    # R-P231(c)：§12 為 first-match 且第 9 列為 catch-all ——
    # **「機械無法判定」不應存在為一個結果類別**；其真正意義為「未命中任何前列，故落底」。
    return 9, "Functional Based（落底）", "（未命中第 1–8 列）"


def g154(tcs: list[dict]) -> list[dict]:
    """G154：ER 含「明示不轉換」而 `design_method` 為狀態轉換者 → 觸發。"""
    out = []
    for tc in tcs:
        er = str(tc.get("expected_result", ""))
        m = NO_TRANSITION_RE.search(er)
        if m and tc.get("design_method") == ST:
            out.append({"tc_id": tc["tc_id"], "hit": m.group(0),
                        "line": next((l.strip() for l in er.split("\n")
                                      if m.group(0).lower() in l.lower()), "")})
    return out


def load() -> list[dict]:
    out = []
    for p in sorted(GENERATED.glob("*.json")):
        out += json.loads(p.read_text(encoding="utf-8"))["tcs"]
    return out


def self_test() -> int:
    """R-P226：以 `096` / `137` / `140` 為已知實例，須能重現；另以 fixture 證明會 FAIL。"""
    tcs = load()
    hits = {h["tc_id"][-3:] for h in g154(tcs)}
    failures = 0
    for known in ("096", "137", "140"):
        ok = known in hits
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G154 重現已知實例 `{known}`")
    synth = [{"tc_id": "X-001", "design_method": ST,
              "expected_result": '1. The step completes\n2. TLM_Status.Info still reads "Timed"'},
             {"tc_id": "X-002", "design_method": ST,
              "expected_result": '1. The step completes\n2. The TLM passes to Standby state'},
             {"tc_id": "X-003", "design_method": "決策表 (Decision Table Testing)",
              "expected_result": '1. The step completes\n2. The TLM stays in Timed state'}]
    exp = {"X-001"}
    got = {h["tc_id"] for h in g154(synth)}
    ok = got == exp
    failures += not ok
    print(f"  [{'PASS' if ok else '**FAIL**'}] G154 fixture —— "
          f"明示不轉換＋狀態轉換 → 觸發；有轉換 → 不觸發；非狀態轉換 → 不觸發")
    print(f"          期望 {sorted(exp)}；實際 {sorted(got)}")
    print(f"\n  G154 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    tcs = load()
    same = diff = undecided = 0
    rows = []
    for tc in tcs:
        row, method, hit = propose(tc)
        cur = tc.get("design_method", "")
        if row is None:
            undecided += 1
            state = "**機械無法判定 → 人工裁決**"
        elif (row == 3 and cur == ST) or (row == 1 and cur.startswith("負面")) or \
             (row == 2 and cur.startswith("基礎故障")) or (row == 6 and cur.startswith("邊界")):
            same += 1
            state = "相符"
        else:
            diff += 1
            state = "**相異 → 人工裁決**"
        rows.append((tc["tc_id"], tc["test_set"], cur, row, method, hit, state))

    hits154 = g154(tcs)
    out = ["# G154 / G155 —— `design_method` 機械提案與「明示不轉換」閘門（R-P226）\n",
           "\n> **本腳本不改任何值**（R-P226 / §I）—— 只產出提案與裁決清單，改值於 33 包。\n",
           f"\n## G155 —— 機械提案 vs 現值（{len(tcs)} 條）\n\n| 類 | 數 | 佔比 |\n|---|---|---|\n"
           f"| 相符（不改）| **{same}** | {same/len(tcs)*100:.1f}% |\n"
           f"| **相異 → 人工裁決** | **{diff}** | {diff/len(tcs)*100:.1f}% |\n"
           f"| **機械無法判定 → 人工裁決** | **{undecided}** | {undecided/len(tcs)*100:.1f}% |\n"
           f"| **合計入人工裁決** | **{diff + undecided}** | "
           f"{(diff+undecided)/len(tcs)*100:.1f}% |\n",
           f"\n## G154 —— 明示不轉換而標為狀態轉換：**{len(hits154)} 條**\n\n"
           "| tc_id | 命中字串 | ER 該行 |\n|---|---|---|\n"]
    for h in hits154:
        out.append(f"| `{h['tc_id'][-3:]}` | `{h['hit']}` | {h['line'][:80]} |\n")

    adjudicated = [k for k in ADJUDICATION]
    out.append(f"\n## 人工裁決（R-P226(c)(d)）—— 已裁 **{len(adjudicated)}** 條\n\n"
               "| tc_id | 現值 | 裁定列 | 裁定 | 依據 |\n|---|---|---|---|---|\n")
    cur_by = {t["tc_id"][-3:]: t.get("design_method", "") for t in tcs}
    for k in sorted(ADJUDICATION):
        row, method, why = ADJUDICATION[k]
        out.append(f"| `{k}` | {cur_by.get(k, '?').split(' (')[0]} | "
                   f"{row if row else '—'} | {method} | {why} |\n")
    pend = [r for r in rows if r[6] != "相符" and r[0][-3:] not in ADJUDICATION]
    out.append(f"\n**尚未裁決 {len(pend)} 條** —— 其成因為**謂詞過窄**："
               "`ROW3_RE` 未涵蓋 `is in <X> state` 一類措詞，"
               "致大量確為狀態轉換者落入「機械無法判定」。\n\n"
               "**放寬該謂詞會使更多條判為「相符現值」—— 方向對執行層有利，"
               "依 R-P187 不自行為之**；具體之放寬提案見上繳 §五。\n")

    out.append("\n## 入人工裁決之逐條（G155）\n\n"
               "| tc_id | Test Set | 現值 | 提案列 | 提案 | 命中字串 | 狀態 |\n"
               "|---|---|---|---|---|---|---|\n")
    for tid, ts, cur, row, method, hit, state in rows:
        if state == "相符":
            continue
        out.append(f"| `{tid[-3:]}` | {ts} | {cur.split(' (')[0]} | "
                   f"{row if row else '—'} | {method} | `{hit}` | {state} |\n")

    (DATA / "g155_design_method_rejudge.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g155_design_method_rejudge.md').relative_to(ROOT)}")
    print(f"  G155：相符 {same}、**相異 {diff}**、**機械無法判定 {undecided}** "
          f"→ 入人工裁決 **{diff + undecided}** / {len(tcs)}")
    print(f"  G154：**{len(hits154)} 條**明示不轉換而標為狀態轉換")


if __name__ == "__main__":
    main()
