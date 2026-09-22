#!/usr/bin/env python3
"""CMF-04 §5 之 JSON 層 —— CMF-03_review §2 之裁定（**不涉車型**）。

套用對象為 `generated/*.json`，內容只有一項：

  R-C61   `006-04`（`-439`）與 `122-02`（`-462`）補自足之 ambiguity Remarks
          並登 `AMBIGUITY_REMARKS` —— 二者與已登錄之 `096-03`（`-376`）同型：
          條文把某物之外觀委託給一份「對照表／system configuration」，而該對照
          於 129 節全無內容，ER 依 §8.4.1 保留其模糊，`H`／`W` 遂命中。

**不在本檔之項**（各有其理由，見上繳包 §3）：

  R-C60   條文側查無雙鍵操作之逐字 → **整行維持原樣，不改**，只出 plan
  `-146`  裁定所指之 `-146` 是**工作簿 F 欄**之值，其列即 `030-04`（`json-275`），
          Remarks 已於 CMF-03 補齊 —— **無第四條可補**，不動
  軸 2    CMF-03 已落地且經核，本輪不動
  DR-46   四行維持 PENDING（`alt-mi ＝ Atlantis MID？` 一問未答）
  車型欄  §3 四個停點全數命中，T–Z 與 sibling **一格未動**

**一次性**：先斷言其被取代之原值為空，第二次執行即中止。

Usage:
    python3 features/comfort/scripts/cmf04_apply.py            # 套用
    python3 features/comfort/scripts/cmf04_apply.py --dry-run  # 只驗斷言、不寫檔
"""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W                                   # noqa: E402

GEN = W.GEN
REPORTS = W.FEATURE / "docs" / "reports"
EXPECT_TOTAL = 476                                       # CMF-03 之語料，本輪不增減


def T(n: int) -> str:
    return f"NR1L-ComfortHMI-{n:03d}"


# Remarks：英文、自足、≥ 40 字元、無內部代號；登錄簿之片段各異（68 §2）
RC61_REMARKS = {
    T(439): ("The clause points to a table of vehicle-model specific recirc "
             "icons, but no cited section contains that table, so which icon "
             "is correct for a given vehicle model cannot be determined from "
             "the specification alone"),
    T(462): ("The clause makes the seat off icon depend on the system "
             "configuration and refers the reader to the Climate section, but "
             "no cited section gives the configuration-to-icon mapping, so the "
             "icon expected on this vehicle cannot be determined from the "
             "specification alone"),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths = sorted(GEN.glob("*.json"))
    docs = {p: json.loads(p.read_text(encoding="utf-8")) for p in paths}
    tcs = {t["tc_id"]: t for d in docs.values() for t in d["tcs"]}
    if len(tcs) != EXPECT_TOTAL:
        raise SystemExit(f"expected the {EXPECT_TOTAL}-TC corpus of CMF-03, "
                         f"found {len(tcs)} — already applied?")

    rows = []
    for tid, text in RC61_REMARKS.items():
        tc = tcs[tid]
        if tc["remarks"] != "":
            raise SystemExit(f"{tid}.remarks: 斷言不符 —— 已非空 {tc['remarks'][:50]!r}")
        tc["remarks"] = text
        rows.append({"tc_id": tid, "field": "remarks", "item": "R-C61",
                     "before": "", "after": text})

    print(f"TCs: {len(tcs)}（本輪不增減）")
    print(f"change-log rows: {len(rows)}")
    if args.dry_run:
        print("dry-run — nothing written")
        return 0
    for p, d in docs.items():
        text = json.dumps(d, ensure_ascii=False, indent=1)
        if text != p.read_text(encoding="utf-8"):
            p.write_text(text, encoding="utf-8")
    out = REPORTS / "cmf04_json_change_log.tsv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out.relative_to(W.FEATURE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
