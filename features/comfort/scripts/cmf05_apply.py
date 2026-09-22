#!/usr/bin/env python3
"""CMF-05 §4／§5 之 JSON 層 —— DR-46 結案、命名以實際值為準、合稱去引號。

套用對象為 `generated/*.json`：

  R-C64/R-C65  DR-46 四條之 `PENDING: DR-46` 行 → `Send CAN:`（canon §8.7.5(c)），
               ER 依 §8.7.5(d)。訊號名取 **Atlantis（MID）** 欄之實際 CAN 名，
               label 逐字取三台 DBC 之 `VAL_`
  R-C64        `$Rear_HVAC_cfg$ = [Present]` 之 5 條 PC → `PROXI Rear_Climate = 1
               (Present)`（canon §8.7.5(e)）。其 source class 由 `[ext-verbatim]`
               改為 `[spec-derived]` —— 改寫後它已不是逐字引用，留著那個標籤即是
               對讀者宣稱一件不成立的事
  R-C60        合稱之既有引號拿掉（`Feet plus Windshield`／`Face + Feet`）

**不在本檔之項**：車型欄 T–Z（在 `cmf05_revise.py`，依 `vm_assign.tsv`）；
車型拆題（實產 0 條，理由見上繳包 §3）。

**一次性**：每一處先斷言其被取代之原值，第二次執行即中止。

Usage:
    python3 features/comfort/scripts/cmf05_apply.py            # 套用
    python3 features/comfort/scripts/cmf05_apply.py --dry-run  # 只驗斷言、不寫檔
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W                                   # noqa: E402

GEN = W.GEN
REPORTS = W.FEATURE / "docs" / "reports"
EXPECT_TOTAL = 476


def T(n: int) -> str:
    return f"NR1L-ComfortHMI-{n:03d}"


# ---------------------------------------------------------------- DR-46
# R-C65：本交付之平台 ＝ Atlantis（MID）。LID → CAN 取
# `forms/Logical Identifiers and CAN Mapping v1_78.xlsx` 之 `Atlantis` 欄。
# label 逐字取 DBC `VAL_`（三台中適用之兩台 —— Promaster／Fastback —— 皆 `BLINK`）。
RECIRC = "STATUS_CLIMATE2.HVACRecirc_Sts = 2 (BLINK)"
REARDEF = "STATUS_CLIMATE2.HVACRearDef_Sts = 2 (BLINK)"
OLD_PENDING = ('PENDING: DR-46 DBC message and raw value for ${name}$ = '
               '"not available/Blink"')
# tc_id -> (步驟序號, 需求側之 $名$, 實際 CAN 賦值)
DR46 = {
    T(141): (1, "RECIRC_STAT", RECIRC),
    T(158): (2, "RECIRC_STAT", RECIRC),
    T(160): (1, "EBL_Stat", REARDEF),
    T(250): (1, "EBL_Stat", REARDEF),
}
# 該步之 ER 原為 `wb-033` 同結構之佔位句（CMF-02 §2）；改為 §8.7.5(d) 之形
OLD_ER = "The climate screen is displayed"

# ---------------------------------------------------------------- R-C64 PROXI
OLD_PC = ("[ext-verbatim] The below requirements shall be implemented when the "
          "PROXI parameter $Rear_HVAC_cfg$ = [Present] — the vehicle is equipped "
          "with rear climate (CFTS043 NEWR1L-53677)")
NEW_PC = ("[spec-derived] PROXI Rear_Climate = 1 (Present) — the vehicle is "
          "equipped with rear climate (CFTS043 NEWR1L-53677)")

# ---------------------------------------------------------------- R-C60
# 合稱為兩個模式之合稱，非按鍵標籤（條文側雙鍵操作之逐字查無，CMF-04 §3-1）。
# `Face + Feet` 未見於 R-C60 之條文，但屬同類且同樣只有一處帶引號 —— 一併拿掉，
# 於上繳包具名（只此一處，回退成本為一行）。
COMPOUNDS = ("Feet plus Windshield", "Face/Feet", "Face & Feet", "Face + Feet")
UNQUOTE = re.compile(r'"(' + "|".join(re.escape(c) for c in COMPOUNDS) + r')"')


class Log:
    def __init__(self):
        self.rows = []

    def add(self, tc, field, item, before, after):
        self.rows.append({"tc_id": tc["tc_id"], "field": field, "item": item,
                          "before": before, "after": after})


def _items(block):
    return [re.sub(r"^\s*\d+\.\s*", "", s) for s in block.split("\n") if s.strip()]


def _numbered(items):
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    docs = {p: json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(GEN.glob("*.json"))}
    tcs = {t["tc_id"]: t for d in docs.values() for t in d["tcs"]}
    if len(tcs) != EXPECT_TOTAL:
        raise SystemExit(f"expected the {EXPECT_TOTAL}-TC corpus of CMF-04, "
                         f"found {len(tcs)} — already applied?")
    log = Log()

    # ---- DR-46 -----------------------------------------------------------
    for tid, (k, name, assign) in DR46.items():
        tc = tcs[tid]
        proc, er = _items(tc["test_procedure"]), _items(tc["expected_result"])
        want = OLD_PENDING.format(name=name)
        if proc[k - 1] != want:
            raise SystemExit(f"{tid} step {k}: expected {want!r}, found {proc[k-1]!r}")
        if er[k - 1] != OLD_ER:
            raise SystemExit(f"{tid} ER {k}: expected {OLD_ER!r}, found {er[k-1]!r}")
        proc[k - 1] = f"Send CAN: {assign}"
        er[k - 1] = f"{assign} is sent"
        _setf(tc, "test_procedure", _numbered(proc), "R-C64/DR-46", log)
        _setf(tc, "expected_result", _numbered(er), "R-C64/DR-46", log)

    # ---- R-C64：PROXI 參數名與值 --------------------------------------------
    n_pc = 0
    for tc in tcs.values():
        lines = _items(tc["pre_conditions"])
        if OLD_PC not in lines:
            continue
        lines[lines.index(OLD_PC)] = NEW_PC
        _setf(tc, "pre_conditions", _numbered(lines), "R-C64/PROXI", log)
        n_pc += 1

    # ---- R-C60：合稱去引號 --------------------------------------------------
    n_unq = 0
    for tc in tcs.values():
        for field in ("test_procedure", "expected_result", "test_item"):
            src = tc[field]
            new, k = UNQUOTE.subn(r"\1", src)
            if k:
                _setf(tc, field, new, "R-C60", log)
                n_unq += k

    # ---- 殘留自驗 ------------------------------------------------------------
    left = [(t["tc_id"], f, m.group(0))
            for t in tcs.values()
            for f in ("pre_conditions", "input_test_data", "test_procedure",
                      "expected_result")
            for m in re.finditer(r"\$[^$\n]+\$", t[f] or "")]
    print(f"DR-46 改寫 {len(DR46)} 條／PROXI PC {n_pc} 條／合稱去引號 {n_unq} 處")
    print(f"作者側四欄之 `$…$` 殘留：{len(left)} 處 {left}")
    print(f"change-log rows: {len(log.rows)}")
    if args.dry_run:
        print("dry-run — nothing written")
        return 0
    for p, d in docs.items():
        text = json.dumps(d, ensure_ascii=False, indent=1)
        if text != p.read_text(encoding="utf-8"):
            p.write_text(text, encoding="utf-8")
    out = REPORTS / "cmf05_json_change_log.tsv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(log.rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(log.rows)
    print(f"wrote {out.relative_to(W.FEATURE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
