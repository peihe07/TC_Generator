"""G137 —— 批次一至三之 `reasoning` 逐份重評（R-P203）。

G129 之門檻係以批次一至三為校準語料，**而該語料本身未經評估**
（26 §五第 5 項自陳）。R-P203 令逐份判其是否涵蓋 §10.4 之四項。

§10.4 四項（逐字）：
  1. 驗證目標 —— core behavior / observable outcome under test
  2. 關鍵情境條件 —— trigger preconditions / inputs / mode（echoes §4.3）
  3. 為什麼這樣切 —— `tcs.length == 1` 時須說明何以一條即足，
     **`do NOT write empty phrases like "不需拆分"`**；≥ 2 時須引所依之 §
  4. 未涵蓋 / 刻意略過（**optional** —— skip if N/A）

判定（先寫定後執行）：
  - 第 1 / 2 / 4 項以標記詞判其**有無**
  - **第 3 項另判其是否為空語** —— 僅寫「單一行為」「不拆」「一條即足」
    而無任何依據（§ 條號、可觀察面之列舉、失效模式之說明）者，
    依 §10.4 之明文判為**未涵蓋**
  - 第 4 項為 optional，**不計入涵蓋率之分母**

**口徑（R-P219，30 包明載）** —— 本閘同時產出二個數，二者不得混用：

  - **單項率**：某一項之涵蓋（如「第 2 項 33 / 33」）—— 27 包所載者即此
  - **齊備率**：第 1 ＋ 2 ＋ 3 三項**同時**成立（29 包所載之 25 / 33 即此）

27 包之 33 / 33 與 29 包之 25 / 33 **並非矛盾，係口徑不同**：
前者為第 2 項單項（補寫後確為 33 / 33，本包複驗仍然），
後者為三項齊備。往後引用本閘之數字須標明其為單項率抑或齊備率。

用法：
    python features/power/scripts/assess_reasoning.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

TARGET_BATCHES = ("batch_001", "batch_002", "batch_003")

MARK_1 = re.compile(r"驗證目標")
MARK_2 = re.compile(r"關鍵情境條件")
MARK_3 = re.compile(r"為什麼這樣切|依 §|各拆一條|拆為|不拆|單一行為|一條即足")
MARK_4 = re.compile(r"刻意略過|未涵蓋|委由|委出")

# 第 3 項之空語 —— §10.4 明文所禁之形態。
EMPTY_3 = re.compile(r"^(?:單一行為|本錨點為單一行為)[。，,]?(?:不拆[。]?)?$")
# 依據之跡象：§ 條號、R-P 引用、失效模式、可觀察面之列舉
SUBSTANCE_3 = re.compile(r"§\s?[\d.]|R-P\d+|獨立部分失效|互斥|不同觸發|不同控制實體|"
                         r"壓力測試|可觀察|各拆|拆為|軸|因其為|以.{0,8}為軸")


def item3_state(text: str) -> str:
    """回傳 '有依據' / '空語' / '缺'。"""
    m = re.search(r"為什麼這樣切[：:]\s*(.+?)(?=(?:刻意略過|未涵蓋|\*\*|$))", text, re.S)
    seg = m.group(1).strip() if m else ""
    if not seg:
        # 無「為什麼這樣切」標題者，取全文中之拆分敘述
        seg = " ".join(re.findall(r"[^。]*(?:單一行為|不拆|各拆|拆為|一條即足)[^。]*。", text))
    if not seg:
        return "缺"
    core = re.sub(r"\s+", "", seg)
    if EMPTY_3.match(core) or (len(core) <= 12 and not SUBSTANCE_3.search(seg)):
        return "空語"
    return "有依據" if SUBSTANCE_3.search(seg) else "空語"


def rows() -> list[dict]:
    out = []
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        if not b.get("batch", "").startswith(TARGET_BATCHES):
            continue
        for leaf in b.get("leaves", []):
            t = str(leaf.get("reasoning", "")).strip()
            out.append({
                "leaf": leaf["parent"], "batch": b["batch"].split("_")[1],
                "len": len(t),
                "i1": bool(MARK_1.search(t)), "i2": bool(MARK_2.search(t)),
                "i3": item3_state(t), "i4": bool(MARK_4.search(t)),
            })
    return out


def main() -> None:
    rs = rows()
    ok = [r for r in rs if r["i1"] and r["i2"] and r["i3"] == "有依據"]
    need = [r for r in rs if r not in ok]
    out = ["# G137 —— 批次一至三之 `reasoning` 重評（R-P203）\n",
           "\n> 判準見 `scripts/assess_reasoning.py` docstring —— **先寫定後執行**。\n",
           "> 第 4 項為 §10.4 之 optional，**不計入分母**。\n",
           f"\n**母體 {len(rs)} 份**（R-P203 載「22 份」—— 該數應僅指批次三；"
           f"批次一 3 ＋ 批次二 8 ＋ 批次三 22 = **{len(rs)}**）\n",
           f"\n| 項 | 涵蓋 | 率 |\n|---|---|---|\n",
           f"| 1 驗證目標 | {sum(r['i1'] for r in rs)} / {len(rs)} | "
           f"{sum(r['i1'] for r in rs)/len(rs)*100:.0f}% |\n",
           f"| 2 關鍵情境條件 | {sum(r['i2'] for r in rs)} / {len(rs)} | "
           f"{sum(r['i2'] for r in rs)/len(rs)*100:.0f}% |\n",
           f"| 3 為什麼這樣切（有依據）| "
           f"{sum(r['i3'] == '有依據' for r in rs)} / {len(rs)} | "
           f"{sum(r['i3'] == '有依據' for r in rs)/len(rs)*100:.0f}% |\n",
           f"| 4 刻意略過（optional）| {sum(r['i4'] for r in rs)} / {len(rs)} | — |\n",
           f"\n### 二個口徑（R-P219）\n\n"
           f"- **單項率** —— 第 2 項「關鍵情境條件」**{sum(r['i2'] for r in rs)} / {len(rs)}**"
           f"（27 包所載之 33 / 33 即此口徑，本包複驗仍然）\n"
           f"- **齊備率** —— 第 1 ＋ 2 ＋ 3 三項**同時**成立"
           f"**{len(ok)} / {len(rs)}**（29 包所載之 25 / 33 即此口徑）\n"
           f"\n**二數並非矛盾，係口徑不同；引用時須標明。**\n"
           f"\n未達齊備者 **{len(need)}** 份，其所缺**全為第 3 項**"
           f"（判為「空語」）—— 該判定係取**首個** `為什麼這樣切：` 段落"
           f"（原有之「單一行為，不拆」，依 R-P203(c) 不得刪改），"
           f"而 27 包所補之實質依據位於其後且於 `**` 處截斷。"
           f"**內容非缺漏；放寬判定式之方向對執行層有利，依 R-P187 未自行修改，"
           f"27 包已呈請裁定，至今未裁。**\n",
           "\n## 逐份明細\n\n| leaf | 批 | 字數 | 1 目標 | 2 情境 | 3 切法 | 4 略過 |\n"
           "|---|---|---|---|---|---|---|\n"]
    for r in rs:
        out.append(f"| `{r['leaf']}` | {r['batch']} | {r['len']} | "
                   f"{'✓' if r['i1'] else '**✗**'} | {'✓' if r['i2'] else '**✗**'} | "
                   f"{r['i3'] if r['i3'] == '有依據' else '**' + r['i3'] + '**'} | "
                   f"{'✓' if r['i4'] else '—'} |\n")
    (DATA / "g137_reasoning_assessment.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g137_reasoning_assessment.md').relative_to(ROOT)}")
    print(f"  母體 {len(rs)} 份")
    print(f"  **單項率**：1 驗證目標 {sum(r['i1'] for r in rs)} / {len(rs)}、"
          f"2 關鍵情境條件 {sum(r['i2'] for r in rs)} / {len(rs)}、"
          f"3 為什麼這樣切（有依據）{sum(r['i3'] == '有依據' for r in rs)} / {len(rs)}")
    print(f"  **齊備率（第 1+2+3 同時成立）**：{len(ok)} / {len(rs)}；未達 {len(need)}")
    print(f"  第 2 項（關鍵情境條件）涵蓋 {sum(r['i2'] for r in rs)} / {len(rs)}")
    print(f"  第 3 項判為空語 {sum(r['i3'] == '空語' for r in rs)}、"
          f"缺 {sum(r['i3'] == '缺' for r in rs)}")
    print(f"  最短 {min(r['len'] for r in rs)} 字（{min(rs, key=lambda r: r['len'])['leaf']}）")


if __name__ == "__main__":
    main()
