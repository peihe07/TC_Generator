"""G181 —— §12 第 8 列之「功能數」謂詞（R-P259）。

**訂正之緣由**：§12 第 8 列之**條件欄**逐字為 `End-to-end flow, ≥3 features`，
其 tie-break 逐字為 `Scenario = ≥3 steps crossing features`。
31 包所建之謂詞取 tie-break 之「≥ 3 steps」，**非該列條件之「≥ 3 features」**——
只數步數，未要求跨三個功能。

**「功能」之界定（R-P250：先量語料再寫）**

`test_procedure` 全批之子系統／訊號族詞頻實測：
`TLM` 137、`HU` 90、`screen` 97、`call` 55、`audio` 30、`display` 23、
`antitheft` 23、`theme` 19、`panel` 16、`logo` 15、`ignition` 11、`menu` 11、
`phone` 11、`volume` 10、`bus` 9、`CAN` 8、`AUD_LVL` 6、`ICS` 5、`camera` 5、
`ETM` 4、`HVAC` 2、`backlight` 2、`timer` 2、`LIN` 2。

據此界定 **11 個功能族**。三項界定原則：

  1 **`TLM` / `HU` / `ETM` 不計為功能** —— 其為受測件本身（137 / 90 / 4 次，
    幾乎每條皆有），計之則全批同時 +1，不具區辨力。
  2 **匯流排與模擬工具不計為功能** —— `CAN` / `LIN` / `bus` 為**施測手段**，
    非被測之功能；R-P259 所指之 feature 為車機功能。
  3 **同族詞歸一** —— `audio` / `volume` / `AUD_LVL` / `speaker` / `mute` / `chime`
    同屬音訊輸出，計為一個功能而非四個。

用法：
    python features/power/scripts/count_features.py
    python features/power/scripts/count_features.py --self-test
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

# 11 個功能族。鍵為族名，值為其詞彙（同族詞歸一）。
FEATURES: dict[str, re.Pattern] = {
    "音訊輸出": re.compile(
        r"\baudio\b|\bvolume\b|AUD_LVL|\bspeaker\b|\bmute[ds]?\b|\bchime", re.I),
    "電話": re.compile(
        r"\bcall\b|\bcalls\b|\bphone\b|\bbluetooth\b|\bhead ?set\b|"
        r"Phone_Call\.", re.I),
    "畫面顯示": re.compile(
        r"\bdisplay\b|\bscreen\b|\bsplash\b|\bbacklight\b|\bimages?\b|"
        r"\bvisuali[sz]", re.I),
    "品牌與主題": re.compile(
        r"\btheme\b|\blogo\b|\bfont\b|\bicon\b|\bbrand", re.I),
    "後視攝影機": re.compile(r"\bcamera\b|Rear_View|Rear_Camera", re.I),
    "防盜": re.compile(r"\bantitheft\b|Antitheft_", re.I),
    "電源狀態": re.compile(
        r"\bBODY (?:ON|OFF)|\bStandby\b|\bSleep\b|\bTimed\b|\bIdle\b|"
        r"\bFull-Operation\b|\bPartial Operation\b|\bignition\b|"
        r"\bpower (?:state|down|up)\b|TLM_Status\.", re.I),
    "設定與選單": re.compile(
        r"\bmenu\b|\bsetting\b|\bsettings\b|PROXI|Timeout\d*|"
        r"_Setting\.|_Timeout_", re.I),
    "實體控制": re.compile(
        r"\bfront panel\b|\bpanel\b|\bbutton\b|Front_Panel_|CLIMATIC_PANEL", re.I),
    "HVAC": re.compile(r"\bHVAC\b", re.I),
    "ICS 模組": re.compile(r"\bICS\b", re.I),
}

# 受測件本身與施測手段 —— 明示排除，理由見模組首段。
EXCLUDED = ("TLM / HU / ETM（受測件本身）", "CAN / LIN / bus（施測手段）")


def features_of(text: str) -> list[str]:
    """`test_procedure` 所觸及之相異功能族。"""
    return sorted(name for name, pat in FEATURES.items() if pat.search(text))


def self_test() -> int:
    """R-P259(a) / R-P250 —— 以**已知實例**驗證其界定。

    三個實例取自 R-P259 之分析層逐條複核（其判定為外部給定，非執行層自擬），
    另加二個應達 3 之實例以證該謂詞會命中。
    """
    tcs = load()
    by = {t["tc_id"][-3:]: t for t in tcs}
    CASES = [
        ("026", 1, "R-P259 分析層判：開 menu → 選值 → 讀回，**僅一個功能**（逾時設定）"),
        ("027", 1, "R-P259 分析層判：同上"),
        ("028", 2, "R-P259 分析層判：撥出 → 接聽 → 讀路由與狀態，**跨二個功能**，未達三"),
    ]
    failures = 0
    print("R-P259(a) —— 「功能」界定之已知實例驗證\n")
    for tid, want, why in CASES:
        got = features_of(by[tid]["test_procedure"])
        ok = len(got) == want
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] `…-{tid}` 期望 {want} 個，"
              f"實測 {len(got)} 個：{got}")
        print(f"          外部依據：{why}")
    print(f"\n  G181 已知實例全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def load() -> list[dict]:
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    return tcs


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    tcs = load()
    rows = [(t["tc_id"], t["req_id"], features_of(t["test_procedure"])) for t in tcs]
    dist = collections.Counter(len(f) for _, _, f in rows)
    hit = [r for r in rows if len(r[2]) >= 3]

    out = ["# G181 —— 第 8 列之功能數謂詞（R-P259）\n",
           "\n> §12 第 8 列之**條件欄**為 `End-to-end flow, ≥3 features`；\n",
           "> 舊謂詞取其 tie-break 之「≥ 3 steps」，**只數步數不數功能**。\n",
           "> 「功能」＝ `test_procedure` 所觸及之**相異子系統／訊號族**。\n",
           "> **排除**：" + "、".join(EXCLUDED) + "。\n",
           f"\n## 一、功能族（{len(FEATURES)} 個）\n\n| 族 | 詞彙 |\n|---|---|\n"]
    for name, pat in FEATURES.items():
        out.append(f"| {name} | `{pat.pattern[:70]}` |\n")
    out.append(f"\n## 二、全批之功能數分布\n\n| 功能數 | 條數 |\n|---|---|\n")
    for k in sorted(dist):
        out.append(f"| {k} | {dist[k]} |\n")
    out.append(f"\n**≥ 3 者：{len(hit)} 條**\n")
    out.append(f"\n## 三、≥ 3 之逐條\n\n| tc | leaf | 功能 |\n|---|---|---|\n")
    for tid, req, f in hit:
        out.append(f"| `…-{tid[-3:]}` | `{req}` | {'、'.join(f)} |\n")

    p = DATA / "g181_feature_count.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"功能數分布：{dict(sorted(dist.items()))}")
    print(f"≥ 3 者 {len(hit)} 條：{[t[0][-3:] for t in hit]}")


if __name__ == "__main__":
    main()
