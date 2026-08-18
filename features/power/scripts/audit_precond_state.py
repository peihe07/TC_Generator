"""G142 —— `pre_conditions` 之狀態值依據（R-P210）。

R-P204 只處理 **§8.4.2 之依據越界**（前提所指之訊號是否為本 leaf 所有），
**未處理 §8.4.1 之造值** —— §8.4.1 之禁止清單逐字含 `default states`：
選定一個 clause 未載之起始狀態，即為造一個 default state。

風險為實：若待驗行為僅於某些狀態下發生，
將起始狀態定為 clause 未載之值，可能使測試根本未觸及該行為。

判準（R-P210）：
  (a) 該狀態值**逐字見於本 leaf 之 `source_clause`** → 合法
  (b) 該狀態值**未見於 clause** → 須於 `reasoning` 載明
      （i）選擇依據；（ii）待驗行為是否隨該狀態而異

**狀態值之抽取**（先寫定後執行）：
  自 `pre_conditions` 各行取其**被斷言之值** ——
    - 雙引號內之值（`read "Standby"`）
    - `is in <MODE>` / `is in the <X> state` 之模式名
    - 全大寫之模式詞（`STANDBY MODE` / `IDLE`）
  bench 環境語（模擬工具、按鍵、配對裝置）不計 —— 其非受測件之狀態。

比對採 **R-P201(c) 之空白摺除** 與大小寫不敏感 ——
`Partial Operation` 與 `Partial_Operation`、`STANDBY` 與 `Standby` 視為同一。
**此為字面比對之正規化，非語義推定**；
正規化後仍不命中者一律列為 (b)，由人判其依據。

用法：
    python features/power/scripts/audit_precond_state.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

# 被斷言之狀態值。
QUOTED_RE = re.compile(r'"([^"]{2,40})"|“([^”]{2,40})”')
MODE_RE = re.compile(
    r"\bis in (?:the )?([A-Z][A-Za-z_\- ]{2,30}?)(?: mode| state| status)?\b"
    r"|\b([A-Z]{3,}(?:[ _][A-Z]{2,})*)\b")

# bench 環境語 —— 非受測件之狀態，不納入判定。
BENCH_RE = re.compile(
    r"simulation tool|bench|injection tool|is connected|is available|"
    r"is paired|equipped|present in the bench|clock is set|network is awake|"
    r"tool is connected", re.I)

# 非狀態值之常見誤抓（訊號值以外之引號內容、載體詞）。
VALUE_SKIP = {"NA", "TLM", "HU", "ICS", "CAN", "LIN", "AND", "OR", "IF"}


def fold(text: str) -> str:
    """R-P201(c)：識別子內之空白摺除；另摺 `_` 與空白之互換。"""
    t = re.sub(r"\s*_\s*", "_", text)
    return re.sub(r"[\s_]+", " ", t).strip().casefold()


def state_values(pre: str) -> list[str]:
    out = []
    for line in pre.split("\n"):
        line = re.sub(r"^\s*\d+\.\s*", "", line)
        if BENCH_RE.search(line):
            continue
        for m in QUOTED_RE.finditer(line):
            v = (m.group(1) or m.group(2)).strip()
            if v and v.upper() not in VALUE_SKIP:
                out.append(v)
        for m in MODE_RE.finditer(line):
            v = (m.group(1) or m.group(2) or "").strip()
            if v and v.upper() not in VALUE_SKIP and len(v) > 2:
                out.append(v)
    seen, uniq = set(), []
    for v in out:
        if fold(v) not in seen:
            seen.add(fold(v))
            uniq.append(v)
    return uniq


# R-P217 之第 5 / 6 欄 —— **摘自 29 包所寫入各該 leaf 之 `reasoning`**，
# 非本包新增之判斷；其全文見 `generated/*.json` 之 leaf `reasoning`。
BASIS: dict[str, tuple[str, str]] = {
    "SWE-PM-057": ("規格他處明文 —— `SWE-PM-061` clause 載"
                   "「These settings could be only done in TLM Full-Operation Status」",
                   "**是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1）"),
    "SWE-PM-060": ("同 `SWE-PM-057`（`SWE-PM-061` 之明文）",
                   "**是**；否定側由 `024` 承擔"),
    "SWE-PM-062": ("同 `SWE-PM-057`（`SWE-PM-061` 之明文）",
                   "**是**；否定側由 `024` 承擔"),
    "SWE-PM-061": ("否定側需一非 Full-Operation 狀態；`Timed` 為 §E 既有狀態",
                   "**是，而本條所驗即該差異**；規格僅二分，取任一即足"),
    "SWE-PM-064": ("他 leaf 之定義 —— `Timeout1` 之計時與到期依 "
                   "`SWE-PM-038` / `063` 發生於 Timed",
                   "**規格未載** —— 依據為他 leaf 明文而非推定，故不列待查"
                   "（**R-P218 送複核**）"),
    "SWE-PM-019": ("clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值",
                   "**是**，二分支皆已成條"),
    "SWE-PM-027": ("clause 之「set … **back to** `False`」蘊含起始為 `True`",
                   "**是** —— 起始若已為 `False` 則無可觀察變化"),
    "SWE-PM-028": ("同 `SWE-PM-027`", "**是**，同 `SWE-PM-027`"),
    "SWE-PM-029": ("同 `SWE-PM-027`", "**是**，同 `SWE-PM-027`"),
    "SWE-PM-031": ("測試可執行性需一具體狀態；`Standby` 為 §E 既有狀態",
                   "**否** —— clause 逐字載 `regardless of TLM_Status.Info and "
                   "$Telematic_Power$ value`"),
    "SWE-PM-094": ("他 leaf 明文 —— `SWE-PM-093` 列三模式，此為其一",
                   "**無法說明** —— clause 一字未載；已標待查並開 **DR-PW14**"),
}


def collect() -> list[dict]:
    rows = []
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        clause = {l["parent"]: fold(str(l.get("source_clause", "")))
                  for l in b["leaves"]}
        reasoning = {l["parent"]: str(l.get("reasoning", "")) for l in b["leaves"]}
        for tc in b["tcs"]:
            src = clause.get(tc["req_id"], "")
            vals = state_values(str(tc.get("pre_conditions", "")))
            absent = [v for v in vals if fold(v) not in src]
            if absent:
                pre = str(tc.get("pre_conditions", ""))
                hit = [ln.strip() for ln in pre.split("\n")
                       if any(v in ln for v in absent)]
                rows.append({
                    "tc_id": tc["tc_id"], "leaf": tc["req_id"],
                    "batch": b["batch"].split("_")[1],
                    "values": vals, "absent": absent,
                    "precond_line": hit[0] if hit else "（未定位）",
                    "basis": BASIS.get(tc["req_id"], ("（未載）", ""))[0],
                    "varies": BASIS.get(tc["req_id"], ("", "（未載）"))[1],
                    "note": str(tc.get("reasoning_note", "")),
                    "leaf_reasoning": reasoning.get(tc["req_id"], ""),
                })
    return rows


def main() -> None:
    total = sum(len(json.loads(p.read_text(encoding="utf-8"))["tcs"])
                for p in sorted(GENERATED.glob("*.json")))
    rows = collect()
    out = ["# G142 —— `pre_conditions` 之狀態值依據（R-P210）\n",
           "\n> 判準見 `scripts/audit_precond_state.py` docstring —— **先寫定後執行**。\n",
           "> 比對採空白摺除與大小寫不敏感之**字面**正規化，非語義推定；\n"
           "> 正規化後仍不命中者一律列為 (b)，由人判其依據。\n",
           f"\n## 計數\n\n| 類 | 數 | 佔比 |\n|---|---|---|\n"
           f"| (a) 狀態值逐字見於 clause | **{total - len(rows)}** | "
           f"{(total-len(rows))/total*100:.1f}% |\n"
           f"| **(b) 有狀態值未見於 clause** | **{len(rows)}** | "
           f"{len(rows)/total*100:.1f}% |\n"
           f"| **合計** | **{total}** | 100% |\n"]
    if rows:
        # G147 / R-P217：六欄逐項表，供分析層以原始素材複核。
        out.append("\n## (b) 型逐項表（G147 / R-P217）\n\n"
                   "> 欄位依 R-P217：`tc_id` / `leaf` / **前提行逐字** / "
                   "該狀態值是否見於 clause / 執行層所載之選擇依據 / "
                   "待驗行為是否隨該狀態而異。\n"
                   "> **前提行為逐字轉錄，未經改寫**；後二欄取自該 leaf 之 `reasoning`。\n\n"
                   "| # | tc_id | leaf | 前提行（逐字）| 見於 clause | 選擇依據 | 行為隨狀態而異 |\n"
                   "|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(rows, 1):
            line = r["precond_line"].replace("|", "\\|")
            out.append(f"| {i} | `{r['tc_id']}` | `{r['leaf']}` | `{line}` | "
                       f"**否**（{'、'.join('`' + v + '`' for v in r['absent'])}）| "
                       f"{r['basis']} | {r['varies']} |\n")
    (DATA / "g142_precond_state.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g142_precond_state.md').relative_to(ROOT)}")
    print(f"  全批 {total} 條；(a) {total - len(rows)}、**(b) {len(rows)}**")
    for r in rows:
        print(f"    {r['tc_id']} ({r['leaf']}, 批{r['batch']}): {r['absent']}")


if __name__ == "__main__":
    main()
