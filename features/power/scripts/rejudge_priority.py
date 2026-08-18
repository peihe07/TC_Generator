"""G164 —— `priority` 全面重判提案（R-P237，34 包）。

32 包之 G162 僅取樣 34 條，其中 13 條（38.2%）無法歸入 §10.2 任一 P0 類別，
Branding and Theme 更是 **5/5 全數無法歸入**。取樣結論不足以推及全體，
故本檔改為**全量**：全部 193 條 P0 ＋ Branding and Theme 全 34 條。

判準即 §10.2 之 P0 類別，逐類設謂詞；**謂詞取自 §10.2 之字面類別，
非自語料回推**。命中者列出其命中字串為證；無一命中者提案改判。

**本檔只出提案，不改任何 JSON 之 `priority` 值**（§H「不改值」）。
代理判準不得凌駕實質判準 —— 逐條之最終判定屬人工。

用法：
    python features/power/scripts/rejudge_priority.py
"""

from __future__ import annotations

import collections
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# §10.2 之 P0 類別 —— 一類一謂詞。詞彙取自該節之字面表述。
#
# **v1 → v2 之訂正（R-P187 / R-P182，並陳兩版）**
#   v1 之 `\bCAN\b` 加了 `re.I`，於是吃到英文常用字 “can”；
#   v1 之 connection 含 `connect(?:ion|ed|ivity)` / `network`，
#   於是吃到 bench 樣板句「the CAN simulation tool is connected to the network」——
#   **該句存在於每一條 TC**，故 connection 與 CAN 二類各命中 34/34。
#   v1 結果：Branding and Theme **34/34 判「P0 成立」**；
#   v2 結果見報表。
#   **偏誤方向：偏向「P0 成立」**，即偏向確認現值、免除重判作業之方向 ——
#   此為對執行層有利之方向，故依 R-P187 明載。
#   結構性理由：謂詞讀入了 `pre_conditions` 之 bench 樣板列，
#   該列與受測行為無關；v2 於 `evidence()` 濾除之，並令 `CAN` 區分大小寫。
P0_RULES: list[tuple[str, re.Pattern]] = [
    ("safety（安全）", re.compile(
        r"\bsafety|crash|airbag|collision|hazard|warning lamp|brake|"
        r"reverse gear|rear ?view camera|\bRVC\b", re.I)),
    ("boot / recovery（開機與復原）", re.compile(
        r"\bboot|start ?up|power ?on|power ?down|reboot|recover|"
        r"BODY (?:ON|OFF)|OFF-TIMED|STANDBY|shut ?down|ignition (?:on|off)", re.I)),
    ("connection（連線）", re.compile(
        r"\bBluetooth\b|\bWi-?Fi\b|\bUSB\b|pair(?:ed|ing)\b|"
        r"\btethering\b|\bAndroid Auto\b|\bCarPlay\b", re.I)),
    ("audio output（音訊輸出）", re.compile(
        r"\baudio|sound|volume|mute|speaker|chime|amplifier", re.I)),
    ("eCall", re.compile(r"\beCall|emergency call|\bSOS\b", re.I)),
    ("vehicle-critical CAN signal（車輛關鍵 CAN 訊號）", re.compile(
        r"STATUS_LIN\.|Batt_ST_Crit|Vehicle_Speed|Door_Ajar_Status|"
        r"Ignition_St|\bCAN\b")),          # **不加 re.I** —— 否則吃到英文字 “can”
    ("data-loss risk（資料遺失風險）", re.compile(
        r"\bdata loss|is not (?:saved|stored|retained)|\bNVM\b|"
        r"non-?volatile", re.I)),
]

# 裝飾性／個人化 —— §10.2 歸 P3。僅在無任何 P0 類別命中時作為提案依據。
COSMETIC_RE = re.compile(
    r"\blogo|brand|theme|font|icon|colou?r|wallpaper|skin|animation|"
    r"splash|season|welcome (?:screen|image)|customi[sz]", re.I)


BENCH_RE = re.compile(
    r"simulation tool|test bench|is connected to|is available|is paired with|"
    r"equipped with|clock is set|carries the ex-factory", re.I)


def evidence(tc: dict) -> str:
    """受檢文字。**濾除 `pre_conditions` 之 bench 樣板列**（v2 訂正）——
    該列（如「the CAN simulation tool is connected to the network」）
    存在於每一條 TC，與受測行為無關，v1 因未濾而使 connection / CAN 二類全數命中。"""
    parts = []
    for f in ("tc_title", "test_item", "input_test_data",
              "test_procedure", "expected_result"):
        parts.append(str(tc.get(f, "")))
    for ln in str(tc.get("pre_conditions", "")).split("\n"):
        if not BENCH_RE.search(ln):
            parts.append(ln)
    return " ".join(parts)


def classify(tc: dict) -> tuple[list[tuple[str, str]], bool]:
    """回傳（命中之 §10.2 P0 類別與其證據字串, 是否命中裝飾性）。"""
    txt = evidence(tc)
    hits = [(name, m.group(0)) for name, pat in P0_RULES
            if (m := pat.search(txt))]
    return hits, bool(COSMETIC_RE.search(txt))


def main() -> None:
    tcs, ts_of = [], {}
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for t in d["tcs"]:
            ts_of[t["tc_id"]] = Path(f).stem
        tcs += d["tcs"]

    # 受檢範圍（R-P237）：全部 P0 ＋ Branding and Theme 全 34 條
    scope = [t for t in tcs if t["priority"] == "P0"
             or ts_of[t["tc_id"]] == "batch_006_branding_theme"]

    rows, stat = [], collections.Counter()
    for t in sorted(scope, key=lambda x: x["tc_id"]):
        hits, cosmetic = classify(t)
        if hits:
            verdict = "P0 成立"
            proposal = t["priority"] if t["priority"] == "P0" else f'{t["priority"]}（維持）'
        elif cosmetic:
            verdict = "**無 P0 類別命中；命中裝飾性／個人化**"
            proposal = "**提案 P3**"
        else:
            verdict = "**無 P0 類別命中，亦非裝飾性**"
            proposal = "**提案人工裁決**"
        stat[verdict] += 1
        rows.append((t["tc_id"], ts_of[t["tc_id"]], t["priority"],
                     hits, verdict, proposal))

    out = ["# G164 —— `priority` 全面重判提案（R-P237）\n",
           "\n> **本檔只出提案，不改任何 `priority` 值。**\n",
           "> 受檢範圍：全部 **P0 193 條** ＋ Branding and Theme 全 **34** 條，"
           f"去重後 **{len(scope)}** 條 / 264。\n",
           "> 謂詞取自 §10.2 之字面 P0 類別，非自語料回推；"
           "命中字串逐條列出為證。\n",
           "> 代理判準不得凌駕實質判準（§5a）—— 最終判定屬人工。\n",
           "\n## 一、彙總\n\n| 判定 | 條數 |\n|---|---|\n"]
    for k, v in stat.most_common():
        out.append(f"| {k} | **{v}** |\n")

    out.append("\n## 二、逐條\n\n"
               "| tc_id | test set | 現值 | 命中之 §10.2 P0 類別（證據） | 判定 | 提案 |\n"
               "|---|---|---|---|---|---|\n")
    for tid, ts, pri, hits, verdict, prop in rows:
        ev = "；".join(f"{n} → `{s}`" for n, s in hits) or "（無）"
        out.append(f"| `{tid[-3:]}` | {ts.replace('batch_00', '')} | {pri} | "
                   f"{ev} | {verdict} | {prop} |\n")

    path = DATA / "g164_priority_rejudge.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")
    print(f"受檢 {len(scope)} 條")
    for k, v in stat.most_common():
        print(f"  {k}: {v}")
    bt = [r for r in rows if r[1] == "batch_006_branding_theme"]
    print(f"\nBranding and Theme {len(bt)} 條：",
          dict(collections.Counter(r[4] for r in bt)))


if __name__ == "__main__":
    main()
