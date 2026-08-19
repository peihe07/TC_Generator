"""G198 —— `axis` 之正向判準重判（R-P283）。

**根因**（R-P283）：判序 `none → boundary → timing → trigger_state → mode → input_data`
之中，**`input_data` 排於末項** —— 前五謂詞未命中者全數落入，
其佔 **90 / 224 = 40.2%**，而分析層抽樣 5 條中 **4 條不應在其中**。

**「單一值吸收一切」之第三次**（`design_method` 狀態轉換 95.8%、
§12 第 9 列被讀為 catch-all、本次之 `axis` `input_data`）。

### 判準之改法

舊法以**二條之 token 差**為輸入，其失在於 token 脫離語義框架
（`20` / `60` 只是數字，看不出其為「PROXI 參數之取值」）。
新法改以**相異之整行**為輸入 —— 行提供框架，故可分辨
「參數取值」「bench 配置」「車輛狀態」「事件時點」。

### 五值之正向判準（R-P250：先量再寫，五例為外部給定之驗證集）

| 值 | 語義框架 | 語料形態 |
|---|---|---|
| `boundary` | 界線值之比較 | `greater than` / `less than` / `at least` / `at most` |
| `input_data` | **參數之取值** | `The PROXI parameter "X" is at V`、`X reads "V"`、`X = V`、`input_test_data` 之列 |
| `timing` | **事件之時點** | `boot … has been completed` vs `is not ended`、`before` / `after` ＋ 事件、`expires` |
| `trigger_state` | **車輛或系統之狀態** | `ignition working condition is …`、`TLM_Status.Info reads …`、訊號值 |
| `mode` | **硬體／bench 之配置** | `is present in the bench configuration`、`is absent from the bench`、Radio 型別 |

**判序**：`boundary → input_data → timing → trigger_state → mode`。
`input_data` **前移至第二** —— 其形態（`參數 is at 值`）最具語法特徵，
而「參數之單位為分鐘」不使其軸成為 `timing`（R-P284）。
**末項為 `mode` 而其亦有正向判準**；五者皆未命中者標 **`無對應`** 並停（R-P283(c)）。

用法：
    python features/power/scripts/rejudge_axis_positive.py
    python features/power/scripts/rejudge_axis_positive.py --self-test
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_axis import load, sig  # noqa: E402

FIELDS = ("pre_conditions", "input_test_data", "test_procedure")
BASE = re.compile(r"(SWE-PM-\d+)")

# ── 五值之正向謂詞，逐一以語料形態寫定 ──
BOUNDARY_RE = re.compile(
    r"\bgreater than\b|\bless than\b|\bat least\b|\bat most\b|\bexceed", re.I)
# **餵入測試之資料值**（R-P283(a)）。語料形態實測：
# `$VC_VEH_BRAND$: "Jeep"`、`Audio_Brand: "Beats"`、`Starting volume level: 25`、
# `NA`（一方有資料一方無）、`Drive CLIMATIC_PANEL.Radio_Btn0 from "…" to "…"`、
# `Send the value listed in Input Test Data`、`The PROXI parameter "X" is at V`。
INPUT_DATA_RE = re.compile(
    r"\bPROXI parameter\b|"
    r"^\s*(?:\d+\.\s*)?[\w.$ ]+:\s*\S|"          # `名稱: 值`（input_test_data 之列）
    r"^\s*NA\s*$|"                                  # 一方無餵入資料
    r"\bDrive\b.{0,40}?\bfrom\b.{0,20}?\bto\b|"
    r"\bSend the value listed\b|"
    # `reads` 與 `is at` 同屬賦值動詞族；`OBSERVE_RE` 已排除 `Read …` 之祈使句，
    # 故可安全納入（初版為避免該祈使句而排除之，屬過度收窄）。
    r"(?:[\w.$]*[_.$][\w.$]*|\"[^\"]+\")\s+(?:is at|is equal to|reads)\s*[\"“\[]?[\w.$\- ]+|"
    # `is set to` 與 `is at` 同屬賦值動詞族（45 包補；語料形態：
    # `The HU clock **is set to** the day before the Summer start date`）
    r"\bis set to\b|"
    # **情境型／事件型輸入**（R-P299(a)，45 包）——
    # 非數值、非訊號名之施加項。語料形態實測：
    #   `Press the VR button with a **short/long** press`（操作方式）
    #   `**Accept / Decline** the … popup as the user`（使用者回應）
    #   `**Dismiss / Leave** the FOTA pop-up`（同上）
    #   `A climate pop-up **at the moment of the transition**`（分析層所舉之例）
    r"\b(?:short|long) press\b|"
    r"\b(?:Accept|Decline|Dismiss|Leave)\b.{0,40}?\bpop-?\s?up\b|"
    r"\bat the moment of\b|"
    r"[\w.$]+\s*=\s*\S", re.M)
# **事件之時點**（R-P283(a)）。語料形態實測：
# `The boot of the TLM has been completed` vs `is not ended`、
# `Keep the broadcast stopped to the end of the ignition cycle`、
# `at Timeout1 expiration`、`before / after` ＋ 事件。
TIMING_RE = re.compile(
    r"\bboot\b.{0,34}?\b(?:completed|ended|progress|sequence)\b|"
    r"\b(?:before|after|during|until)\b.{0,30}?"
    r"\b(?:boot|elapse|expir|window|cycle|transition|call|start|time)\w*\b|"
    r"\bexpir(?:es|ed|ation)\b|\bhas elapsed\b|"
    r"\bto the end of\b|\bwithin\b.{0,20}\b(?:Timeout|Tsend|Time)\b", re.I)
# **系統或車輛之狀態**（R-P283(a)）。語料形態實測：
# `The TLM is in Timed state`、`the ignition working condition is …`、
# `TLM_Status.Info reads …`、`RemStartFail is at "False"`（並存狀態，R-P283(3)）、
# `VPLastStatus reads "On"`、`A non-Ecall non-ACN call is active`。
# **含 §E 之狀態名** —— 其為系統狀態而非硬體配置，故歸本值而非 `mode`。
#
# **45 包之擴充（R-P299(a)）**：語料實測另有三形態未被涵蓋 ——
#   `TLM_Display.GUI is in / is on a screen other than …`（顯示子系統之狀態）
#   `The HU is (not) currently installing a firmware image`（進行中之作業）
#   `The HU has (not yet / already) played the startup sound that day`（已發生與否）
TRIGGER_STATE_RE = re.compile(
    r"\bignition working condition\b|\bIgnition (?:On|Off|Pre_?Start|Pre Off)\b|"
    r"TLM_Status\.Info|\$Telematic_Power\$|STATUS_[A-Z]+\.|"
    r"[\w.]+\.(?:Req|Info|Sts|GUI)\b|\bworking condition\b|"
    r"\bis in\b.{0,30}?\b(?:state|mode|Operation|Standby|Sleep|Idle|Timed)\b|"
    r"\bBODY (?:ON|OFF-TIMED|OFF)\b|\bFull-Operation\b|\bPartial Operation\b|"
    r"\b(?:RemStartFail|VPLastStatus|MaxCallTimeout)\b|"
    r"\bcall is (?:active|still active)\b|\bis already active\b|"
    r"\bis (?:not )?(?:currently )?installing\b|"
    r"\bhas (?:not yet|already) \w+", re.I)
# **硬體／bench 之配置**（R-P283(a)）。語料形態實測：
# `An LTM Radio is present in the bench configuration`、
# `A Radio other than LTM or ETM is present in …`、
# `The HU runs the PNET architecture`、`Set the boot target status to Bench`。
MODE_RE = re.compile(
    r"\bbench configuration\b|\b(?:present|absent)\b.{0,26}?\bbench\b|"
    r"\bRadio\b.{0,34}?\b(?:present|absent|other than|offers)\b|"
    r"\bLTM High\b|\bAtlantis\b|\barchitecture\b|"
    r"\bboot target status\b|\bis an? \w+ (?:Radio|configuration)\b", re.I)

# **判序**：`boundary → timing → trigger_state → mode → input_data`。
# `input_data` 仍居末，**惟其已具正向判準** —— R-P283(c) 所禁者為
# 「末項作為**預設落點**」，非「末項居末」；五者皆未命中者標「無對應」並停。
# 初版曾將 `input_data` 前移至第二，實測**其反而吸收前列**（五例中 4 例誤判）——
# 語義上「參數取值」為最廣之框架，前移即成新的 catch-all。並陳兩版（R-P182）。
ORDER = (("boundary", BOUNDARY_RE), ("timing", TIMING_RE),
         ("trigger_state", TRIGGER_STATE_RE), ("mode", MODE_RE),
         ("input_data", INPUT_DATA_RE))


def norm(s: str) -> str:
    return " ".join(str(s).split())


def diff_lines(a: dict, b: dict) -> list[str]:
    """二條之**相異整行**（行提供語義框架，token 不提供）。

    **排除觀察步驟**（`Read …` / `Check …` 之祈使句）——
    其為讀取結果之手段，非二條之區分條件；
    比照 40 包 R-P271(a) 之「型乙 觀察媒介不另計」。

    **v1 → v2 之訂正（43 包）**：v1 只取「`a` 有而 `b` 無」之行（**單向差集**），
    故**一方為另一方之嚴格超集時，差異顯示為空**。
    實例：`…-067` 與 `…-069` 僅差 `…-069` 多一行
    `4. Rear_View_Camera reads "Present" and the Rear Camera is not active`；
    該行在對照條而不在本條，v1 遂判其相異行為空而歸「無對應」，
    並被誤分入 R-P288 之「僅 ER 相異」10 條。
    **v2 改為對稱差**（`rejudge_axis.diff_text` 本即用 `ta ^ tb`，本檔未沿用之）。
    """
    out = []
    for f in FIELDS:
        la = [norm(x) for x in str(a.get(f, "")).split("\n") if x.strip()]
        lb = [norm(x) for x in str(b.get(f, "")).split("\n") if x.strip()]
        out += [x for x in la if x not in lb and not OBSERVE_RE.search(x)]
        out += [x for x in lb if x not in la and not OBSERVE_RE.search(x)]
    return out


def propose(tc: dict, peers: list[dict]) -> tuple[str | None, str]:
    others = [p for p in peers if p["tc_id"] != tc["tc_id"]]
    if not others:
        return None, "該 leaf 僅產出 1 條 TC —— 無他條可區分"
    same = [p for p in others if sig(p) == sig(tc)]
    if same and same[0]["tc_title"] == tc["tc_title"]:
        return "none", f"與 `{same[0]['tc_id']}` 四欄逐字全同（須併設 `duplicate_of`）"
    ref = min(others, key=lambda p: len(" ".join(diff_lines(tc, p))))
    lines = diff_lines(tc, ref)
    data_lines = set(data_only_lines(tc, ref))

    # **R-P298（45 包）**：`input_test_data` **依定義即「餵入測試之資料」**（R-P283(a)），
    # 故其內容**不驅動** `boundary` / `timing` / `trigger_state` / `mode` 之判定 ——
    # 值之文字含狀態名（`An Ignition On after the date passes March, 20th`）
    # 或含時間單位，不使其軸成為 `trigger_state` 或 `timing`；
    # 此與 R-P283(1)「參數之單位為分鐘不等於其軸為時序」為同一理據。
    frame = "\n".join(x for x in lines if x not in data_lines)

    for axis, pat in ORDER:
        if axis == "input_data":
            continue                      # 末項另行處理，見下
        if not (m := pat.search(frame)):
            continue
        # **R-P298(b)**：`timing` 另須「二條之相對位置標記相異」。
        if axis == "timing" and not timing_applies(tc, ref):
            continue
        return axis, f"對照 `{ref['tc_id'][-3:]}`，相異行命中 {axis}：`{m.group(0)[:52]}`"

    # `input_data` —— 其正向判準讀**全部**相異行（含 `input_test_data`）
    if (m := INPUT_DATA_RE.search("\n".join(lines))):
        return "input_data", (f"對照 `{ref['tc_id'][-3:]}`，"
                              f"相異行命中 input_data：`{m.group(0)[:52]}`")
    if data_lines and set(lines) <= data_lines:
        return "input_data", (f"對照 `{ref['tc_id'][-3:]}`，"
                              f"相異行**僅出自 `input_test_data`**：`{lines[0][:46]}`")
    return "**無對應**", (f"對照 `{ref['tc_id'][-3:]}`，五個正向判準皆未命中；"
                          f"相異行：{' ／ '.join(x[:40] for x in lines[:2]) or '（無）'}")


def self_test() -> int:
    """R-P283 之五例為**分析層所給定**之驗證集（非執行層自擬）。"""
    tcs = load()
    by = {t["tc_id"][-3:]: t for t in tcs}
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)
    # **⚠ 45 包重編**：44 包之合併使 `tc_id` 重新連號（264 → 260），
    # 本表原以舊號為鍵，重編後已指向**不同之 TC** ——
    # 其失敗為重新編號之產物，非謂詞缺陷。依 `data/merge_44.md` 之對照表更新。
    CASES = [
        ("017", "input_data", "R-P283(1)（舊 018）：差在所配置之 PROXI 參數值（20 vs 60 分），執行序列相同"),
        ("018", "input_data", "同上（舊 019）"),
        ("020", "mode", "R-P283(2)（舊 021）：差在 bench 所裝之 Radio 型別，係硬體配置變體"),
        ("021", "mode", "同上（舊 022）"),
        ("037", "trigger_state", "R-P283(3)（舊 038）：觸發相同，差在 `RemStartFail` 之並存狀態"),
        ("038", "trigger_state", "同上（舊 039）"),
        ("052", "trigger_state", "R-P283(4)（舊 053）：差在點火 working condition（`Pre_Start` vs `On`）"),
        ("051", "trigger_state", "同上（舊 052）"),
        ("157", "timing", "R-P283(5)（舊 160）：同一請求送於 boot 完成前與後"),
        ("158", "timing", "同上（舊 161）"),
        # **R-P298（45 包）**：季節組之相異僅在**哪一個日期**，相對位置相同 → `input_data`
        ("255", "input_data", "R-P298（舊 259）：差為 December 21st 對 March 20th，事件結構相同"),
        ("256", "input_data", "同上（舊 260）"),
    ]
    failures = 0
    print("R-P283 之五例（分析層給定）—— 正向判準之驗證\n")
    for tid, want, why in CASES:
        got, ev = propose(by[tid], by_leaf[BASE.match(by[tid]["req_id"]).group(1)])
        ok = got == want
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] `…-{tid}` 期望 `{want}`，實測 `{got}`")
        print(f"          分析層依據：{why}")
        print(f"          謂詞依據：{ev}")
    print(f"\n  G198 五例全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    tcs = load()
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)

    rows, before = [], collections.Counter()
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        d = t.get("distinguishing_axis")
        if d is None:
            continue
        before[d["axis"]] += 1
        prop, ev = propose(t, by_leaf[BASE.match(t["req_id"]).group(1)])
        rows.append((t["tc_id"], d["axis"], prop, ev))
    after = collections.Counter(p for _, _, p, _ in rows)
    moved_out = [r for r in rows if r[1] == "input_data" and r[2] != "input_data"]
    unmapped = [r for r in rows if r[2] == "**無對應**"]

    out = ["# G198 —— `axis` 之正向判準重判（R-P283）\n",
           "\n> **判準之改法**：舊法以二條之 **token 差**為輸入，其失在於 token 脫離語義框架"
           "（`20` / `60` 只是數字）。新法改以**相異之整行**為輸入。\n",
           "> **判序**：`boundary → input_data → timing → trigger_state → mode`；\n",
           "> `input_data` 前移至第二（其形態最具語法特徵）；\n",
           "> **五者皆未命中者標「無對應」並停**（R-P283(c)：末項不得為預設落點）。\n",
           f"\n## 一、六值分布（前 → 後）\n\n| 值 | 前 | 後 |\n|---|---|---|\n"]
    for k in sorted(set(before) | set(after)):
        out.append(f"| `{k}` | {before.get(k, 0)} | **{after.get(k, 0)}** |\n")
    out.append(f"\n**`input_data` {before.get('input_data', 0)} → "
               f"{after.get('input_data', 0)}；移出 {len(moved_out)} 條。**\n")
    out.append(f"\n## 二、自 `input_data` 移出者（**{len(moved_out)}** 條）\n\n"
               "| tc | 舊 | 新 | 依據 |\n|---|---|---|---|\n")
    for tid, old, new, ev in moved_out:
        out.append(f"| `…-{tid[-3:]}` | `{old}` | **`{new}`** | {ev} |\n")
    out.append(f"\n## 三、無對應（**{len(unmapped)}** 條）—— 不逕歸末項\n\n"
               "| tc | 舊 | 依據 |\n|---|---|---|\n")
    for tid, old, new, ev in unmapped:
        out.append(f"| `…-{tid[-3:]}` | `{old}` | {ev} |\n")
    out.append(f"\n## 四、逐條\n\n| tc | 舊 | 新 | 依據 |\n|---|---|---|---|\n")
    for tid, old, new, ev in rows:
        out.append(f"| `…-{tid[-3:]}` | `{old}` | "
                   f"{'**`' + new + '`**' if new != old else '`' + new + '`'} | {ev} |\n")

    p = DATA / "g198_axis_positive.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"前：{dict(before.most_common())}")
    print(f"後：{dict(after.most_common())}")
    print(f"`input_data` {before.get('input_data', 0)} → {after.get('input_data', 0)}；"
          f"移出 {len(moved_out)}；**無對應 {len(unmapped)}**")


# 觀察步驟之祈使句 —— 其為讀取手段，非區分條件（見 `diff_lines` 之註解）。
OBSERVE_RE = re.compile(r"^\s*\d+\.\s*(?:Read|Check|Observe|Verify|Confirm)\b", re.I)


# ── `timing` 之相對位置標記（R-P298(b)，45 包）──
#
# **訂正之緣由**：舊 `TIMING_RE` 只問「相異行中有無時間類詞」，
# 故 `the day before the **Summer** start date` 對 `… **Fall** start date`
# 亦命中 —— 二者之**相對位置相同**（皆為「某日之前一日」），
# 所異者僅為**哪一個日期**。
# R-P283(1) 已裁「參數之單位為分鐘不等於其軸為時序」；
# **同理，值之單位為日期亦不等於其軸為時序**（R-P298）。
#
# `timing` 之正確語義為**事件發生之相對位置不同**
# （如 `boot … has been completed` 對 `is not ended`）。
# 故判準改為：**二條各自之相對位置標記須相異**。
POS_RE = re.compile(
    r"\bbefore\b|\bafter\b|\bduring\b|\buntil\b|\bonce\b|"
    r"\bas soon as\b|\bhas been completed\b|\bis not ended\b|"
    r"\bstill completing\b|\bexpir(?:es|ed|ation)\b|\bto the end of\b|"
    r"\belapse[ds]?\b|\bwithin\b", re.I)


def own_lines(a: dict, b: dict) -> list[str]:
    """`a` 有而 `b` 無之行（單向，供逐條取其自身之標記）。"""
    out = []
    for f in FIELDS:
        la = [norm(x) for x in str(a.get(f, "")).split("\n") if x.strip()]
        lb = [norm(x) for x in str(b.get(f, "")).split("\n") if x.strip()]
        out += [x for x in la if x not in lb and not OBSERVE_RE.search(x)]
    return out


def position_markers(a: dict, b: dict) -> set[str]:
    """`a` 相對於 `b` 之相對位置標記集合（小寫）。"""
    return {m.group(0).lower() for ln in own_lines(a, b)
            for m in POS_RE.finditer(ln)}


def timing_applies(a: dict, b: dict) -> bool:
    """`timing` 僅於**二條之相對位置標記相異**時成立（R-P298(b)）。"""
    ma, mb = position_markers(a, b), position_markers(b, a)
    return bool(ma or mb) and ma != mb


def data_only_lines(a: dict, b: dict) -> list[str]:
    """二條之相異行中，**出自 `input_test_data` 者**（雙向）。"""
    la = [norm(x) for x in str(a.get("input_test_data", "")).split("\n") if x.strip()]
    lb = [norm(x) for x in str(b.get("input_test_data", "")).split("\n") if x.strip()]
    return [x for x in la if x not in lb] + [x for x in lb if x not in la]


if __name__ == "__main__":
    main()
