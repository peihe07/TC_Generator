#!/usr/bin/env python3
"""CMF-03 §2 之 JSON 層 —— CMF-02 審閱裁定之落實（下放包 CMF-03／CMF-03_A）。

套用對象為 `generated/*.json`，內容依序：

  R-C54          `003-06` 補產 front defrost sibling（-475）
  R-C55          `005-04` 補產 RECIRC sibling（-476）；原條 `json-139` 同步瘦身
  R-C56          -467／-468 之 `PENDING: DR-47` 兩行改為條文逐字 ER；
                 該二條與 `json-275` 三條加自足之 ambiguity Remarks
  R-C50(amend)   14 條摘句之首字母轉大寫（canon R-4 之排版正規化）
  M7             引號套用 —— `label_quote_plan.tsv` 之 label 類，
                 加上 CMF-02_review §2-1 七問之逐項裁定
  R-C58          **不改 JSON**：四條之 PENDING 行維持（停點命中，見上繳包）

**一次性**：每一處改寫皆先斷言其被取代之原值，第二次執行會在第一處斷言
即中止，不會重複套用。下半（test_item 之括號）只在末步或末行 ER 改變時
重算（`test_item.situation()`），其餘不動；M7 之引號則逐行套於下半。

產出 `docs/reports/cmf03_json_change_log.tsv`（tc_id／field／item／before／after）
供候選本之逐格對帳歸因，與 `docs/reports/cmf03_m7_apply.tsv`（M7 逐行之套用紀錄）。

Usage:
    python3 features/comfort/scripts/cmf03_apply.py            # 套用
    python3 features/comfort/scripts/cmf03_apply.py --dry-run  # 只驗斷言、不寫檔
"""

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W                                   # noqa: E402
from test_item import situation                          # noqa: E402

FEATURE = W.FEATURE
GEN = W.GEN
REPORTS = FEATURE / "docs" / "reports"
QUOTE_PLAN = REPORTS / "label_quote_plan.tsv"
TEST_GROUP = "Climate Control Interface"                 # R-C6(amend)
EXPECT_BEFORE = 474                                      # CMF-02 之語料
SIBLING_FIRST_ID = 475                                   # R-C46，接 -474


def T(n: int) -> str:
    return f"NR1L-ComfortHMI-{n:03d}"


# ===================================================================== R-C56
# 與 `json-275` 同句（CMF-02_review §2 R-C56：ER 照錄條文逐字，不寫 PENDING）。
RC56_ER = ('The "AUTO" button is no longer highlighted and the system is in '
           "the manual mode that most closely matches the exited AUTO mode")
RC56_PENDING = ("PENDING: DR-47 the manual mode the system goes to when AUTO "
                "is broken without a mode button")

# Remarks 之 ambiguity 句：英文、自足、≥ 40 字元、無內部 id（`R-C`／`DR #`／`§`）。
# 登錄簿之片段各異（`lint_tcs.AMBIGUITY_REMARKS`，68 §2）。
RC56_REMARKS = {
    T(467): ("The specification does not name which manual mode the system "
             "enters when AUTO is broken by pressing A/C, so the mode reached "
             "after this step cannot be determined from the specification alone"),
    T(468): ("The specification does not name which manual mode the system "
             "enters when AUTO is broken by changing the fan speed, so the mode "
             "reached after this step cannot be determined from the "
             "specification alone"),
    T(275): ("The specification does not name which manual mode the rear system "
             "enters when rear AUTO is broken by changing the rear fan speed, so "
             "the mode reached after that step cannot be determined from the "
             "specification alone"),
}
RC55_REMARKS = (
    "The specification states that Recirc can automatically turn on A/C but, "
    "unlike the Defrost sentence in the same clause, it does not say whether "
    "that change is shown on the A/C button; the expected result follows the "
    "analysis report leaf, which records the change as not shown")

# ===================================================================== 軸 2
# M7 第 5 問把 `Sync is on` 正規化為 `SYNC is on` 之後，`axis-type-reverse-test`
# 之 `removed-interface-keywords`（其表列 `SYNC is on` 而無 `Sync is on`）開始命中
# 本二條：它們以 SYNC 指示為可觀察量，而未宣告軸 2 之值。2.11 之
# `Sync is not shown for single zone climate configurations` 使該指示於單區車不存在。
# 補之以工作簿既有之同一句（15 條在用），並同步補其出處節次於 N 欄。
AXIS2_PC = ("[spec-derived] The vehicle is not a single zone climate "
            "configuration, for which Sync is not shown (2.11)")
AXIS2_TCS = [T(19), T(35)]

# ===================================================================== R-C50(amend)
# 摘句自句中段起者首字母轉大寫。清單為實測所得（CMF-02 §6 之 J＝14）——
# 逐條斷言其原值仍以小寫起首，不以「掃到就改」替代斷言。
RC50_UPPER_FIRST = [T(n) for n in
                    (36, 37, 38, 453, 454, 455, 87, 88, 255, 258, 259, 260, 426, 261)]

# ===================================================================== R-C54 / R-C55
SIBLINGS = [
    {   # R-C54 —— `(including front defrost)` 為具名納入之控制，非舉例清單之一員
        "req": "SWE1-HVAC-003-06", "src": T(132),
        "title": "Turning front defrost on breaks AUTO",
        "proc": ["Turn AUTO on from the climate screen", 'Turn "FRONT DEF" on'],
        "er": ['The "AUTO" button is highlighted',
               'The "AUTO" button is no longer highlighted'],
        "split_append": (
            " （**R-C54，CMF-02_review §2**）：同句之 `(including front defrost)` "
            "為條文**具名納入**之一個控制，句中無 `e.g.`／`etc`／`such as`，"
            "不落 R-C44 三之舉例，故補產本條。前排之四個 airflow mode 與 front "
            "defrost 於 2.3 為並列之兩物（`Auto is mutually exclusive with the "
            "four airflow modes and front defrost`），故同 leaf 之「另一 airflow "
            "mode」一條不含本條之觸發，原條無須瘦身。"),
    },
    {   # R-C55 —— 037 leaf 自己寫了 `(change not shown)`，ER 取其對應之可觀察句
        "req": "SWE1-HVAC-005-04", "src": T(139),
        "title": "Recirc turns A/C on without showing it",
        "upper": "Recirc can automatically turn on AC.",
        "proc": ['Turn "A/C" off from the climate screen and note the "A/C" button',
                 'Turn "RECIRC" on and read the "A/C" button'],
        "er": ['The "A/C" button is not highlighted',
               'The "A/C" button is not highlighted'],
        "remarks": RC55_REMARKS,
        "split_append": (
            " （**R-C55，CMF-02_review §2**）：2.4（C3）之末句 `Recirc can "
            "automatically turn on AC.` 為獨立之一個連動，與 Defrost 一句各自可"
            "失效，故自原條拆出。ER 取 037 leaf `SWE1-HVAC-005-04` 逐字之 "
            "`(change not shown)` 所對應之可觀察句，措辭與原條第 3 步一致，非造值；"
            "條文 2.4 之 `(Do not show this change)` 只附於 Defrost 一句，"
            "該不對稱載於 Remarks。"),
    },
]
# `json-139` 之瘦身：移出拆給 -476 之第 3 步（其後仍餘兩步，守 §10.5）
SLIM_139 = {
    "step": 3,
    "proc": 'Turn "RECIRC" on and read the "A/C" button',
    "er": 'The "A/C" button is not highlighted',
    "title": ("Defrost and Recirc turn A/C on without showing it",
              "Defrost turns A/C on without showing it"),
    "split_reason": (
        "§8.2.2 之拆分，依 R-C44 三問（**R-C55，CMF-02_review §2**）：2.4（C3）之 "
        "`Defrost can automatically turn on AC (Do not show this change).` 與 "
        "`Recirc can automatically turn on AC.` 為兩句各自具名之連動，條文逐字列舉、"
        "各為一種操作、無舉例語 —— 三問皆是，故一觸發一條。本條留 Defrost 一句，"
        "Recirc 一句移出為同 req 之另一列。"),
}

# ===================================================================== M7
# CMF-02_review §2-1 之七問。plan 之 label 類逐行套用；下列為七問所加之裁定。
#
#   1  `The X airflow mode is active` → state，不加（91 列維持）—— plan 已判 state
#   2  `read the RECIRC state` 指按鈕 → 統一為 `read the "RECIRC" button state`
#   3  `Set RECIRC to …`／`Change RECIRC` → label —— plan 已判 label
#   4  `Set the airflow mode to Face` → `Select the "Face" airflow mode`
#   5  `Sync`／`SYNC` → 取 SR24 之按鍵標籤拼寫 `SYNC`，全本一致
#   6  `AUTO pop up` → verbatim，不動 —— plan 已判 verbatim
#   7  Tri-Mode `MODE` 等 → 本輪不擴
M7_Q2 = [  # (原行, 新行)  —— 第 2 問
    ('2. Press the RECIRC button again and read the RECIRC state',
     '2. Press the "RECIRC" button again and read the "RECIRC" button state'),
    ('7. Read the RECIRC state and its LED',
     '7. Read the "RECIRC" button state and its LED'),
    ('2. Press "MAX DEF" and read the RECIRC state and its LED',
     '2. Press "MAX DEF" and read the "RECIRC" button state and its LED'),
    ('2. Read the "RECIRC" state',
     '2. Read the "RECIRC" button state'),
]
# 第 4 問：只套單一模式名。`Face/Feet`／`Feet plus Windshield` 為兩個模式之合稱，
# 工作簿與條文皆無該字面之按鍵標籤，加引號即造出一個不存在之 label —— 不套，回報。
M7_Q4 = [
    ('1. Set the airflow mode to Face', '1. Select the "Face" airflow mode'),
    ('1. Set the airflow mode to Feet', '1. Select the "Feet" airflow mode'),
]
M7_Q4_HELD = ['1. Set the airflow mode to Face/Feet',
              '1. Set the airflow mode to Feet plus Windshield']
# 第 5 問：SR24 export 實測 `SYNC` 20／`Sync` 10／`sync` 7；用於**按鍵標籤**者
# 取 `SYNC`（`highlight button if SYNC`，C12／CR7／ICE10），與工作簿既有之
# `Turn "SYNC" on` 一致。全本之孤立 token `Sync` 一律正規化為 `SYNC`。
M7_SYNC = re.compile(r"\bSync\b")

TOKENS = re.compile(r"\b(AUTO|Face|Feet|RECIRC|SYNC|Sync)\b")
QUOTED_SPAN = re.compile(r'"[^"]*"')
NUM_PREFIX = re.compile(r"^(\s*\d+\.\s*)")


def _strip_no(line: str) -> tuple:
    m = NUM_PREFIX.match(line)
    return (m.group(1), line[m.end():]) if m else ("", line)


def load_label_map() -> dict:
    """plan 之 label 類：`context` → `suggestion`（逐行整行取代）。"""
    text = "".join(l for l in QUOTE_PLAN.read_text(encoding="utf-8").splitlines(True)
                   if not l.startswith("#"))
    out = {}
    for r in csv.DictReader(io.StringIO(text), delimiter="\t"):
        if r["class"] != "label":
            continue
        ctx, sug = r["context"], r["suggestion"]
        if out.setdefault(ctx, sug) != sug:
            raise SystemExit(f"plan 之同一 context 有兩個 suggestion：{ctx!r}")
    return out


class Log:
    def __init__(self):
        self.rows = []

    def add(self, tc, field, item, before, after):
        self.rows.append({"tc_id": tc["tc_id"], "field": field, "item": item,
                          "before": before, "after": after})


def _items(block: str) -> list:
    return [re.sub(r"^\s*\d+\.\s*", "", s) for s in block.split("\n") if s.strip()]


def _numbered(items: list) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


def _setf(tc, field, new, item, log, expect=None):
    before = tc[field]
    if expect is not None and before != expect:
        raise SystemExit(f"{tc['tc_id']}.{field}: 斷言不符\n"
                         f"  expected {expect!r}\n  found    {before!r}")
    if before == new:
        return
    tc[field] = new
    log.add(tc, field, item, before, new)


def set_lower(tc, lower, item, log):
    upper, _ = tc["test_item"].split("\n\n")
    _setf(tc, "test_item", f"{upper}\n\n{lower}", item, log)


# --------------------------------------------------------------------- M7
def m7_line(line: str, label_map: dict, q2: dict, q4: dict, stat: dict) -> str:
    """一行之 M7 套用。順序：七問之裁定優先，其次 plan 之 label 類，最後拼寫。"""
    out = q2.get(line) or q4.get(line) or label_map.get(line) or line
    if out is not line:
        stat["line"] += 1
    new = M7_SYNC.sub("SYNC", out)
    if new != out:
        stat["sync"] += 1
    return new


def m7_lower(seg: str, label_map: dict, q2: dict, q4: dict, stat: dict) -> str:
    """下半括號內之一段（`<動作> -> <結果>`）。

    下半之動作段為末步首字母轉小寫之形，故以首字母大小寫正規化查表，
    命中後把新行之首字母還原為原來之大小寫。plan 只掃 L／M 兩欄，
    下半不在其內 —— 但下半是 L／M 之複述，不同步即自相矛盾。
    """
    if not seg:
        return seg
    lead_lower = seg[0].islower()
    probe = (seg[0].upper() + seg[1:]) if lead_lower else seg
    hit = q2.get(probe) or q4.get(probe) or label_map.get(probe)
    if hit is None:
        # 未編號之下半以無號形入表查一次
        for table in (q2, q4, label_map):
            for ctx, sug in table.items():
                pre, body = _strip_no(ctx)
                if pre and body == probe:
                    hit = _strip_no(sug)[1]
                    break
            if hit:
                break
    if hit is not None:
        hit = _strip_no(hit)[1]
        out = (hit[0].lower() + hit[1:]) if lead_lower else hit
        stat["lower"] += 1
    else:
        out = seg
    new = M7_SYNC.sub("SYNC", out)
    if new != out:
        stat["sync"] += 1
    return new


def unquoted_tokens(text: str) -> int:
    spans = [(m.start(), m.end()) for m in QUOTED_SPAN.finditer(text)]
    return sum(1 for m in TOKENS.finditer(text)
               if not any(a <= m.start() < b for a, b in spans))


def apply_m7(tcs: dict, log) -> dict:
    label_map = load_label_map()
    q2, q4 = dict(M7_Q2), dict(M7_Q4)
    stat = {"line": 0, "lower": 0, "sync": 0}
    rows = []
    for tc in tcs.values():
        for field in ("test_procedure", "expected_result"):
            src = tc[field]
            if not src:
                continue
            lines = src.split("\n")
            new = "\n".join(m7_line(l, label_map, q2, q4, stat) for l in lines)
            if new != src:
                for a, b in zip(lines, new.split("\n")):
                    if a != b:
                        rows.append({"tc_id": tc["tc_id"], "field": field,
                                     "before": a, "after": b})
                _setf(tc, field, new, "M7", log)
        upper, lower = tc["test_item"].split("\n\n")
        if lower.startswith("(") and lower.endswith(")"):
            inner = lower[1:-1]
            parts = inner.split(" -> ")
            new_inner = " -> ".join(
                m7_lower(p, label_map, q2, q4, stat) for p in parts)
            if new_inner != inner:
                rows.append({"tc_id": tc["tc_id"], "field": "test_item(下半)",
                             "before": inner, "after": new_inner})
                set_lower(tc, f"({new_inner})", "M7", log)
    held = sorted({r for tc in tcs.values() for f in
                   ("test_procedure", "expected_result")
                   for r in tc[f].split("\n") if r in M7_Q4_HELD})
    return {"stat": stat, "rows": rows, "held": held}


# --------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths = sorted(GEN.glob("*.json"))
    docs = {p: json.loads(p.read_text(encoding="utf-8")) for p in paths}
    tcs = {t["tc_id"]: t for d in docs.values() for t in d["tcs"]}
    doc_of = {t["tc_id"]: d for d in docs.values() for t in d["tcs"]}
    if len(tcs) != EXPECT_BEFORE:
        raise SystemExit(f"expected the {EXPECT_BEFORE}-TC corpus of CMF-02, "
                         f"found {len(tcs)} — already applied?")
    log = Log()
    before_unq = sum(unquoted_tokens(t[f]) for t in tcs.values()
                     for f in ("test_procedure", "expected_result"))

    # ---- R-C56 -----------------------------------------------------------
    for tid in (T(467), T(468)):
        tc = tcs[tid]
        er = _items(tc["expected_result"])
        if er[-1] != RC56_PENDING:
            raise SystemExit(f"{tid}: ER 末行非 DR-47 之 PENDING —— {er[-1]!r}")
        er[-1] = RC56_ER
        _setf(tc, "expected_result", _numbered(er), "R-C56", log)
        set_lower(tc, situation(tc), "R-C56", log)
    for tid, text in RC56_REMARKS.items():
        _setf(tcs[tid], "remarks", text, "R-C56", log, expect="")

    # ---- R-C50(amend) ----------------------------------------------------
    for tid in RC50_UPPER_FIRST:
        tc = tcs[tid]
        upper, lower = tc["test_item"].split("\n\n")
        if not upper[:1].islower():
            raise SystemExit(f"{tid}: 上半已非小寫起首 —— {upper[:40]!r}")
        _setf(tc, "test_item", f"{upper[0].upper()}{upper[1:]}\n\n{lower}",
              "R-C50(amend)", log)
    still = [t["tc_id"] for t in tcs.values()
             if t["test_item"].split("\n\n")[0][:1].islower()]
    if still:
        raise SystemExit(f"R-C50(amend)：仍以小寫起首者 {still}")

    # ---- 軸 2 之 PC（M7 第 5 問之連帶）-------------------------------------
    for tid in AXIS2_TCS:
        tc = tcs[tid]
        lines = _items(tc["pre_conditions"])
        if AXIS2_PC in lines:
            raise SystemExit(f"{tid}: 軸 2 之 PC 已存在")
        lines.insert(len(lines) - 2, AXIS2_PC)     # 置於兩個排除式 PC 之前
        _setf(tc, "pre_conditions", _numbered(lines), "軸 2 PC", log)
        refs = [x.strip() for x in tc["specification_reference"].split(";")]
        ref211 = W.SYS1_STEM + "_2.11"
        if ref211 not in refs:
            refs.append(ref211)
            _setf(tc, "specification_reference", "; ".join(refs), "軸 2 PC", log)

    # ---- R-C55 之原條瘦身（先瘦身，後產 sibling）---------------------------
    tc139 = tcs[T(139)]
    proc, er = _items(tc139["test_procedure"]), _items(tc139["expected_result"])
    k = SLIM_139["step"]
    if proc[k - 1] != SLIM_139["proc"] or er[k - 1] != SLIM_139["er"]:
        raise SystemExit(f"{T(139)}: 第 {k} 步之斷言不符")
    del proc[k - 1], er[k - 1]
    _setf(tc139, "test_procedure", _numbered(proc), "R-C55 slim", log)
    _setf(tc139, "expected_result", _numbered(er), "R-C55 slim", log)
    set_lower(tc139, situation(tc139), "R-C55 slim", log)
    _setf(tc139, "tc_title", SLIM_139["title"][1], "R-C55 slim", log,
          expect=SLIM_139["title"][0])
    # `req-id-unique`：同 req 之每一列皆須宣告其拆分（§8.2.2），原條亦然
    _setf(tc139, "split_flag", True, "R-C55 slim", log, expect=False)
    _setf(tc139, "split_reason", SLIM_139["split_reason"], "R-C55 slim", log,
          expect="")

    # ---- R-C54 / R-C55 之 sibling ----------------------------------------
    n = SIBLING_FIRST_ID
    for s in sorted(SIBLINGS, key=lambda x: x["req"]):
        base = tcs[s["src"]]
        d = doc_of[s["src"]]
        if base["req_id"] != s["req"]:
            raise SystemExit(f"sibling src {s['src']} is {base['req_id']}")
        upper = s.get("upper") or base["test_item"].split("\n\n")[0]
        if " ".join(upper.split()) not in " ".join(d["source_clause"].split()):
            raise SystemExit(f"{s['req']}: sibling upper 非 source_clause 之連續子字串")
        tc = {
            "req_id": s["req"], "tc_id": T(n), "tc_title": s["title"],
            "test_group": TEST_GROUP, "test_set": base["test_set"],
            "test_item": "", "pre_conditions": base["pre_conditions"],
            "input_test_data": "NA",
            "test_procedure": _numbered(s["proc"]),
            "expected_result": _numbered(s["er"]),
            "specification_reference": base["specification_reference"],
            "priority": base["priority"], "design_method": base["design_method"],
            "split_flag": True,
            "split_reason": base["split_reason"] + s["split_append"],
            "functional_safety": "NA", "estimated_test_time": "",
            "remarks": s.get("remarks", ""),
        }
        if "emea_ics_review" in base:
            tc["emea_ics_review"] = base["emea_ics_review"]
        tc["test_item"] = f"{upper}\n\n{situation(tc)}"
        d["tcs"].append(tc)
        tcs[tc["tc_id"]] = tc
        doc_of[tc["tc_id"]] = d
        log.add(tc, "(new TC)", "R-C54/R-C55 sibling", "", tc["tc_id"])
        n += 1

    # ---- M7 ---------------------------------------------------------------
    m7 = apply_m7(tcs, log)
    after_unq = sum(unquoted_tokens(t[f]) for t in tcs.values()
                    for f in ("test_procedure", "expected_result"))

    total = sum(len(d["tcs"]) for d in docs.values())
    print(f"TCs after: {total} ({EXPECT_BEFORE} + {len(SIBLINGS)} siblings)")
    print(f"M7 —— L/M 行改 {m7['stat']['line']}、下半段改 {m7['stat']['lower']}、"
          f"Sync→SYNC {m7['stat']['sync']}")
    print(f"M7 —— L/M 未加引號之 token：before {before_unq} → after {after_unq}")
    print(f"M7 —— 第 4 問未套之合稱行：{m7['held']}")
    print(f"change-log rows: {len(log.rows)}")
    if args.dry_run:
        print("dry-run — nothing written")
        return 0
    for p, d in docs.items():
        text = json.dumps(d, ensure_ascii=False, indent=1)
        if text != p.read_text(encoding="utf-8"):
            p.write_text(text, encoding="utf-8")
    out = REPORTS / "cmf03_json_change_log.tsv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(log.rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(log.rows)
    m7out = REPORTS / "cmf03_m7_apply.tsv"
    with m7out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["tc_id", "field", "before", "after"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(m7["rows"])
    print(f"wrote {out.relative_to(FEATURE)}, {m7out.relative_to(FEATURE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
