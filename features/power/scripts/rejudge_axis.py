"""G173 —— `axis` 全批重判提案（R-P248(b)）。

§4.6 之六值（R-P248 逐字）：
`trigger_state` / `input_data` / `timing` / `boundary` / `mode` / `none`。
現行語料使用 `behaviour`(245) / `branch`(6) / `trigger`(3)，**皆不在列舉內**。

**判準之選擇（R-P250：先量再寫）**：
`delta` 與 `split_reason` 之散文詞頻實測 —— 「分支」112、「狀態」30、
「觸發」17、「Standby」25、「模式」10、「界線」8、「時序」3、
而「輸入」/「boundary」/「duplicate」皆 **0**。
**「分支」為最高頻而不對應任一 axis** —— 故散文不足為判準之基礎。

改以**該 TC 相對其同 leaf 姊妹之實際結構差異**為判準 ——
`axis` 之本義即「此二條 TC 藉何者區分」，
結構差異為其直接證據，散文僅為其描述。

判序（first-match，理由見各項）：
  1 `none`         —— 與姊妹之六欄逐字全同（真重複）
  2 `boundary`     —— 差異落在界線值上（沿用 G6 之 `ROW6_RE`，不另立）
  3 `timing`       —— 差異落在時間量／時序上
  4 `trigger_state`—— 差異落在觸發訊號或其值上
  5 `mode`         —— 差異落在 TLM 之運作模式／狀態上
  6 `input_data`   —— 差異落在其餘輸入參數之取值上
`boundary` 先於 `timing`：界線值多以時間表述（`SplashScreen_Time`），
若 `timing` 在前將吸收全部界線案例。
`trigger_state` 先於 `mode`：模式常為觸發之後果，
而觸發訊號為主動施加者 —— 以主動者為區分軸較貼近 `axis` 之本義。

**無姊妹者（該 leaf 僅產出 1 條 TC）在 §4.6 中無對應值** ——
六值皆預設「與他條之區分」，而該 TC 無他條可區分。
逐條列出，**不新增列舉值**（R-P248(b) / §I）。

用法：
    python features/power/scripts/rejudge_axis.py
    python features/power/scripts/rejudge_axis.py --self-test
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_design_method import ROW6_RE  # noqa: E402  界線值謂詞，沿用不另立
from verify_axis import AXIS_ENUM  # noqa: E402

FIELDS = ("pre_conditions", "input_test_data", "test_procedure", "expected_result")

# ── 各軸之形態，皆先經語料量測（R-P250）──
# 時間量：`SplashScreen_Time` / `Response_Wait_Time` / `10 seconds` / `20 minutes`
TIMING_RE = re.compile(
    r"\b\w*_Time\b|\bTimeout\d*\b|\b\d+\s*(?:seconds?|minutes?|min|ms)\b|"
    r"\bwait time\b|\bexpir\w+|\bwindow\b", re.I)
# 觸發訊號：語料之訊號書寫形態為 `A.B` / `$X$` / `STATUS_LIN.*` / `*.Req` / `*.Info`
TRIGGER_RE = re.compile(
    r"\b[A-Za-z]\w*\.(?:Req|Info|Sts)\b|\bSTATUS_[A-Z]+\.\w+|"
    r"\$[A-Za-z_]\w*\$|\b\w+_Enable\b|\bFront_Panel_OnOff\b")
# 運作模式／狀態：值自 §E 之狀態名，非自由詞
MODE_RE = re.compile(
    r"\bBODY (?:ON|OFF-TIMED|OFF)\b|\bFull-Operation\b|\bPartial Operation\b|"
    r"\bTimed\b|\bStandby\b|\bSleep\b|\bIdle\b|\bBench\b|\bOff\b", re.I)


def norm(s: str) -> str:
    return " ".join(str(s).split())


def sig(tc: dict) -> tuple[str, ...]:
    return tuple(norm(tc.get(f, "")) for f in FIELDS)


def diff_text(a: dict, b: dict) -> str:
    """二條 TC 之 **token 層**差異（僅 a 有而 b 無、或 b 有而 a 無之 token）。

    **v1 → v2 之訂正（R-P250 之實例驗證所攔下，並陳兩版）**
    v1 取**行層**差異（相異之整行），故一行內二條**共有**之 token 亦被帶入 ——
    `…-002` / `…-003` 僅差 boot target（Standby vs Bench），
    而其差異行同時含二條皆有之 `SplashScreen_Time`，
    致 `TIMING_RE` 誤命中，判為 `timing` 而非 `mode`。
    v2 改取 token 層，只留**真正相異**之 token。
    **本訂正發生於謂詞產出任何結果之前** —— 係 R-P250 所令之
    「已知應命中實例」驗證所攔下，非事後回頭調整判準。
    """
    ta, tb = set(), set()
    for f in FIELDS:
        ta |= set(TOKEN_RE.findall(str(a.get(f, ""))))
        tb |= set(TOKEN_RE.findall(str(b.get(f, ""))))
    return " ".join(sorted(ta ^ tb))


def propose_axis(tc: dict, peers: list[dict]) -> tuple[str | None, str]:
    """回傳（提案之 axis, 依據）。無姊妹者回傳 (None, 理由)。"""
    others = [p for p in peers if p["tc_id"] != tc["tc_id"]]
    if not others:
        return None, "該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應"
    same = [p for p in others if sig(p) == sig(tc)]
    if same:
        dup = same[0]
        # **四欄全同而 `tc_title` 相異者不是重複**（36 包實例驗證所得）：
        # `…-087` ≡ `…-091` / `…-088` ≡ `…-092`（`SWE-PM-025`），
        # 其 title 分別載 `Front_Panel_OnOff.Req` 與 `CLIMATIC_PANEL.Radio_Btn0`，
        # 即 R-P179 所裁之二觸發訊號 ——
        # **TC 內文未寫入其宣稱之區分觸發**，此為內容缺陷，非重複。
        if dup["tc_title"] != tc["tc_title"]:
            return "trigger_state", (
                f"**內容缺陷** —— 與 `{dup['tc_id'][-3:]}` 之四欄逐字全同，"
                f"惟 `tc_title` 所載之觸發訊號相異；區分軸為 `trigger_state`，"
                f"**而該觸發未寫入內文**，須於 37 包補入")
        return "none", f"與 `{dup['tc_id']}` 之四欄逐字全同（須併設 `duplicate_of`）"
    # 取與本條差異最小之姊妹作為對照 —— 差異最小者即其真正之區分軸
    ref = min(others, key=lambda p: len(diff_text(tc, p)))
    d = diff_text(tc, ref)
    for axis, pat, label in (
            ("boundary", BOUNDARY_RE, "界線值"),
            ("timing", TIMING_RE, "時間量／時序"),
            ("trigger_state", TRIGGER_RE, "觸發訊號"),
            ("mode", MODE_RE, "運作模式／狀態")):
        if (m := pat.search(d)):
            return axis, f"對照 `{ref['tc_id'][-3:]}`，差異落在{label}：`{m.group(0)}`"
    return "input_data", f"對照 `{ref['tc_id'][-3:]}`，差異為其餘輸入之取值"


def load() -> list[dict]:
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    return tcs


def self_test() -> int:
    """R-P250 —— 每一軸取語料中人工確認應命中之實例，證明謂詞確實命中。

    實例之選取依據載於各案；**取不到三例之軸即標明**（R-P250）。
    """
    tcs = load()
    by = {t["tc_id"][-3:]: t for t in tcs}
    by_leaf: dict[str, list[dict]] = {}
    for t in tcs:
        by_leaf.setdefault(re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1), []).append(t)

    def leafpeers(tid: str) -> list[dict]:
        t = by[tid]
        return by_leaf[re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)]

    # （tc_id 末三碼, 期望軸, 人工確認之依據）
    CASES = [
        # 每一案之期望值皆經**實讀該 TC 與其對照條**後確認（R-P250）。
        # ⚠ 本檔於 36 包驗證中曾二度以**未讀即推想**之期望值送驗
        # （`…-001` 判 `timing`、`…-008` 判 `timing`），二次皆是**期望值錯而謂詞對**。
        # 依 R-P64 據實記錄：R-P250 之保障確實生效，
        # 惟其攔下的是「執行層的臆測」，非謂詞之缺陷 —— 二者須分辨。
        ("002", "mode", "實讀：與 `…-003` 僅差 boot target（Standby vs Bench）"),
        ("003", "mode", "實讀：同上，對照方向相反"),
        ("133", "mode", "實讀：與 `…-132` 僅差 `Standby` vs `Sleep`"),
        ("009", "mode", "實讀：與 `…-014` 僅差 BODY ON vs BODY OFF-TIMED"),
        ("014", "mode", "實讀：同上"),
        ("001", "mode", "**訂正**：三條皆含 `SplashScreen_Time`，其差為 boot target，非時序"),
        ("156", "boundary", "實讀：`$VC_MODEL_YEAR$` 之 `equal to` vs `greater than`"),
        ("200", "boundary", "實讀：同型"),
        ("105", "timing", "實讀：Timeout1 之驅動者為 `Switch_Off_Time` 20 min vs `$PwrAccDelayAct$` 10 min"),
        ("106", "timing", "實讀：同上，對照方向相反"),
        ("012", "trigger_state", "實讀：與 `…-013` 之差為 `STATUS_LIN.Batt_ST_Crit`"),
        ("008", "trigger_state", "**訂正**：與 `…-011` 之差在 `input_test_data`（`NA` vs 二訊號 `[0h]`），確為觸發"),
        ("087", "trigger_state", "實讀：與 `…-091` 四欄全同而 title 之觸發訊號相異（內容缺陷）"),
        ("088", "trigger_state", "實讀：同上，declining 分支"),
        ("025", "input_data", "實讀：`Auto_SwitchOn_Setting.Req` 之 `Active` vs `Recall_Last`"),
        ("027", "input_data", "實讀：同上，對照方向相反"),
    ]
    failures = 0
    print("R-P250 —— 已知應命中實例之驗證\n")
    for tid, want, why in CASES:
        got, ev = propose_axis(by[tid], leafpeers(tid))
        ok = got == want
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] `…-{tid}` 期望 `{want}`，實測 `{got}`")
        print(f"          人工依據：{why}")
        print(f"          謂詞依據：{ev}")
    print(f"\n  全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    tcs = load()
    by_leaf: dict[str, list[dict]] = {}
    for t in tcs:
        by_leaf.setdefault(re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1), []).append(t)

    rows, stat, unmapped = [], collections.Counter(), []
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        leaf = re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)
        cur = t["distinguishing_axis"]["axis"]
        prop, ev = propose_axis(t, by_leaf[leaf])
        stat[prop or "**無對應**"] += 1
        if prop is None:
            unmapped.append((t["tc_id"], leaf, cur))
        rows.append((t["tc_id"], leaf, cur, prop, ev))

    illegal = [r for r in rows if r[2] not in AXIS_ENUM]
    out = ["# G173 —— `axis` 全批重判提案（R-P248）\n",
           "\n> **本檔只出提案，不改值**（R-P248(d)）。\n",
           "> §4.6 之六值：" + "、".join(f"`{a}`" for a in AXIS_ENUM) + "。\n",
           "> 判準為**結構差異**而非 `delta` 之散文 —— 理由見腳本首段（R-P250 之量測）。\n",
           f"\n## 一、現行違規（G173）\n\n"
           f"現行 `axis` 不在六值內者 **{len(illegal)} / {len(rows)}**：\n\n"
           "| 現行值 | 條數 | 合法 |\n|---|---|---|\n"]
    for k, v in collections.Counter(r[2] for r in rows).most_common():
        out.append(f"| `{k}` | {v} | {'是' if k in AXIS_ENUM else '**否**'} |\n")

    out.append(f"\n## 二、重判提案之分布\n\n| 提案 axis | 條數 |\n|---|---|\n")
    for k, v in stat.most_common():
        out.append(f"| `{k}` | **{v}** |\n")

    out.append(f"\n## 三、無可映者 —— **{len(unmapped)}** 條\n\n"
               "> 六值皆預設「與他條之區分」，而該 leaf 僅產出 1 條 TC，無他條可區分。\n"
               "> **不新增列舉值**（R-P248(b)）；處置屬分析層。\n\n"
               "| tc | leaf | 現行 axis |\n|---|---|---|\n")
    for tid, leaf, cur in unmapped:
        out.append(f"| `…-{tid[-3:]}` | `{leaf}` | `{cur}` |\n")

    out.append("\n## 四、逐條\n\n| tc | leaf | 現行 | 提案 | 依據 |\n|---|---|---|---|---|\n")
    for tid, leaf, cur, prop, ev in rows:
        out.append(f"| `…-{tid[-3:]}` | `{leaf}` | `{cur}` | "
                   f"{'`' + prop + '`' if prop else '**無對應**'} | {ev} |\n")

    p = DATA / "g173_axis_rejudge.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"現行違規 {len(illegal)} / {len(rows)}")
    for k, v in stat.most_common():
        print(f"  提案 {k}: {v}")


# token 之切分（R-P250 先量：語料之識別子含 `.` / `_` / `$`，
# 界線值含 `[1h]` 形態，時間量含數字＋單位）——
# 故 token 不得以純 `\w+` 切，否則 `STATUS_LIN.Batt_ST_Crit` 會裂為三段。
TOKEN_RE = re.compile(r"\$?[A-Za-z][\w.\-]*\$?|\[\d+h\]|\d+")


# 界線值（R-P250 先量再寫）。
#
# **不沿用 G6 之 `ROW6_RE`** —— v1 曾沿用（腳本首段原載「不另立」），
# 實例驗證顯示其不可移轉：`ROW6_RE` 為 `design_method` 第 6 列而設，
# 命中裸詞 `limit` / `maximum`，而本用途之輸入為**二條 TC 之 token 差**，
# 其中 `limit` 多來自「the volume limit returns to its normal maximum」之偶然共現。
# v1 之 7 條 boundary 提案中 **3 條為偽**（`…-008` / `…-011` / `…-015`，
# token 差各 45 / 40 / 48 個，`limit` 與該差異無關），**4 條為真**
# （`…-156` / `…-157` / `…-200` / `…-201`，token 差僅 7 個，
#  即 `$VC_MODEL_YEAR$ equal to "2025"` vs `greater than "2025"`）。
# v2 只取**顯式之比較形態**，語料實測其書寫為 `greater than` / `equal to` /
# `other than` / `<>` / `==`，無 `>=` / `at least` / `exceed` 之用例。
BOUNDARY_RE = re.compile(
    r"\bgreater than\b|\bless than\b|\bother than\b|\bat least\b|"
    r"\bat most\b|\bexceed\w*\b|<>|>=|<=", re.I)


if __name__ == "__main__":
    main()
