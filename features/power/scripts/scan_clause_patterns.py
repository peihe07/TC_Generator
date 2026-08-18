"""26 包之三項掃描：逗號列舉（G131）、適用性條件（G132）、重疊對（G133）。

**B8 / R-P192 —— 逗號列舉規模**
G113 只認得 `OR` / `nor`，逗號型列舉看不見。本掃描先量規模，
**不擴充 G113 之辨識規則**（R-P192 明令）。
判準：冒號後、或「In the following …:」型之句中，以逗號分隔**三項以上**
且各項為名詞短語者，計為一個列舉。抽樣率 ≥ 16.7%，**種子載明**。

**B9 / R-P193 —— 適用性條件盤點**
掃 `source_clause` 中含品牌 / 車型 / 市場 / 配備等**適用性條件**之 leaf。
詞表逐字取自已見於語料之欄位名與值，非憑印象列舉。

**B12 / R-P196 —— 重疊對掃描**
以 `source_clause` 之正規化文字相似度找出重疊對。
**門檻載明**：Jaccard(實詞集合) ≥ 0.60，且二 leaf 之錨點集合**不相同**
（錨點相同者已由 A-PW137 登記，不重複計）。

用法：
    python features/power/scripts/scan_clause_patterns.py
"""

from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reverse_coverage import normalize, words  # noqa: E402

SEED = 26          # 種子 = 本包往返 NN，載明以可重現
SAMPLE_RATE = 1 / 6
SIM_THRESHOLD = 0.60

# 逗號列舉：三項以上，項與項之間為逗號，且不含句末標點。
ENUM_RE = re.compile(
    r"(?::|following[^:]{0,40}:)\s*([^.;:]{10,400}?)(?=\.|;|$)", re.I)

# 適用性條件之詞彙。**逐字取自語料中實際出現之欄位名與值**。
APPLICABILITY = [
    "Brand_Configuration_2", "$VC_Veh_Brand$", "$VC_VEH_BRAND$", "Maserati",
    "Jeep", "Fiat Latam", "$VC_VEH_LINE$", "$VC_MODEL_YEAR$", "Audio_Brand",
    "SDARS_Presence", "PROXI", "$Country_Code$", "Market", "LTM High",
    "$TBM_Present$", "$VC_SpecialPKG_IC$", "$Themed_Sound$", "Beats",
    "screen sizes", "$DriverDoorOnOffSts$", "Engineering Line",
]


def leaves() -> list[dict]:
    out = []
    for p in sorted(GENERATED.glob("*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        for leaf in b.get("leaves", []):
            out.append({**leaf, "batch": b.get("batch", "?")})
    return out


def enumerations(clause: str) -> list[str]:
    hits = []
    for m in ENUM_RE.finditer(normalize(clause)):
        seg = m.group(1).strip()
        parts = [p.strip() for p in seg.split(",") if p.strip()]
        if len(parts) >= 3:
            hits.append(seg)
    return hits


def _fold(text: str) -> str:
    """摺除識別子內之空白（R-P201(c)）—— `Brand_Configuration _2` ≡ `Brand_Configuration_2`。

    27 包 G136 查出：本表原以逐字字串比對，`Brand_Configuration_2` 遂無法命中
    原文之 `Brand_Configuration _2`，致 `SWE-PM-014` 於 G132 漏列。
    **修正方向為增加發現（對執行層不利），依 R-P187 自行修正並回報**（見上繳 §四）。
    """
    return re.sub(r"\s*_\s*", "_", text)


def applicability(clause: str) -> list[str]:
    text = _fold(normalize(clause)).lower()
    return [t for t in APPLICABILITY if _fold(t).lower() in text]


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if (a | b) else 0.0


def main() -> None:
    lv = leaves()
    rng = random.Random(SEED)
    out = ["# 26 包 —— 三項掃描（G131 / G132 / G133）\n"]

    # ── B8 / G131 逗號列舉 ──
    enum_rows = [(l["parent"], l["batch"], e)
                 for l in lv for e in enumerations(str(l.get("source_clause", "")))]
    enum_leaves = sorted({r[0] for r in enum_rows})
    k = max(1, round(len(enum_rows) * SAMPLE_RATE))
    sample = rng.sample(enum_rows, k) if enum_rows else []
    out.append(f"\n## G131 —— 逗號列舉規模（R-P192）\n\n"
               f"- 判準：冒號後（或 `In the following …:` 型）以逗號分隔**三項以上**者計一個列舉\n"
               f"- **出現次數 {len(enum_rows)}**，分布於 **{len(enum_leaves)} 個 leaf**\n"
               f"- 抽樣：**{k} / {len(enum_rows)} = {k/max(1,len(enum_rows))*100:.1f}%**"
               f"（≥ 16.7%），**種子 = {SEED}**（`random.Random({SEED}).sample`）\n"
               f"- **未擴充 G113 之辨識規則**（R-P192）\n\n"
               f"所在 leaf：{'、'.join('`' + x + '`' for x in enum_leaves)}\n\n"
               "### 抽樣明細（判別欄由執行層人工填寫）\n\n"
               "| leaf | 批次 | 列舉（截斷 90 字）| 項數 |\n|---|---|---|---|\n")
    for leaf, batch, seg in sample:
        n = len([p for p in seg.split(",") if p.strip()])
        out.append(f"| `{leaf}` | {batch.split('_')[1]} | {seg[:90]} | {n} |\n")

    # ── B9 / G132 適用性條件 ──
    app_rows = [(l["parent"], l["batch"], applicability(str(l.get("source_clause", ""))))
                for l in lv]
    app_rows = [r for r in app_rows if r[2]]
    out.append(f"\n## G132 —— 適用性條件盤點（R-P193）\n\n"
               f"含品牌 / 車型 / 市場 / 配備條件之 leaf：**{len(app_rows)} / {len(lv)}**\n\n"
               "| leaf | 批次 | 命中之條件詞 |\n|---|---|---|\n")
    for leaf, batch, hits in app_rows:
        out.append(f"| `{leaf}` | {batch.split('_')[1]} | "
                   f"{'、'.join('`' + h + '`' for h in hits)} |\n")

    # ── B12 / G133 重疊對 ──
    wsets = {l["parent"]: words(str(l.get("source_clause", ""))) for l in lv}
    anchors = {l["parent"]: frozenset(str(l.get("source_anchor", "")).split(","))
               for l in lv}
    names = sorted(wsets)
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if not wsets[a] or not wsets[b]:
                continue
            s = jaccard(wsets[a], wsets[b])
            if s >= SIM_THRESHOLD:
                pairs.append((a, b, s, anchors[a] == anchors[b]))
    pairs.sort(key=lambda x: -x[2])
    same_anchor = [p for p in pairs if p[3]]
    diff_anchor = [p for p in pairs if not p[3]]
    out.append(f"\n## G133 —— 重疊對掃描（R-P196）\n\n"
               f"- **門檻：Jaccard(實詞集合) ≥ {SIM_THRESHOLD:.2f}**"
               f"（實詞集合取自 `reverse_coverage.words()`，含詞幹化與停用詞移除）\n"
               f"- 重疊對合計 **{len(pairs)}**：錨點集合**相同**者 **{len(same_anchor)}**"
               f"（已由 A-PW137 登記）、**不同**者 **{len(diff_anchor)}**（本條之對象）\n\n"
               "### 錨點不同而內容重疊者\n\n"
               "| leaf A | leaf B | 相似度 | A 之錨點 | B 之錨點 |\n|---|---|---|---|---|\n")
    for a, b, s, _ in diff_anchor:
        out.append(f"| `{a}` | `{b}` | **{s:.2f}** | "
                   f"`{','.join(sorted(anchors[a]))[:34]}` | "
                   f"`{','.join(sorted(anchors[b]))[:34]}` |\n")
    out.append("\n### 錨點相同者（A-PW137 已登記，列此以示未遺漏）\n\n"
               "| leaf A | leaf B | 相似度 |\n|---|---|---|\n")
    for a, b, s, _ in same_anchor:
        out.append(f"| `{a}` | `{b}` | {s:.2f} |\n")

    (DATA / "b8_b9_b12_scans.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'b8_b9_b12_scans.md').relative_to(ROOT)}")
    print(f"  G131 逗號列舉：{len(enum_rows)} 次 / {len(enum_leaves)} leaf；"
          f"抽樣 {k}（種子 {SEED}）")
    print(f"  G132 適用性條件：{len(app_rows)} / {len(lv)} leaf")
    print(f"  G133 重疊對：合計 {len(pairs)}（錨點相同 {len(same_anchor)}、"
          f"不同 {len(diff_anchor)}），門檻 {SIM_THRESHOLD}")


if __name__ == "__main__":
    main()
