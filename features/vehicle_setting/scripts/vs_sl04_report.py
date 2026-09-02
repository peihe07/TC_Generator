#!/usr/bin/env python3
"""VS-SL-04 §2 —— v4 報告與 vf230 沙盒稿重生。

v4 報告 = v3 報告，其 (3) 分支之 105 列依 `_v4_branch3_resolution.tsv` 更新：
  R1／R1b → 補 PROXI 行，分支改記，去 `PROXI_PENDING`
  R2      → 不加 PROXI 行、不 PENDING，掛登記旗（`FIP_ALWAYS_OFF`／`FIP_ALWAYS_ON`）
  R3      → 維持 `PENDING`，另掛 subcase 旗供 DR 第四節
其餘 352 列逐欄照抄。**BL／VC 本包不動。**
"""

from __future__ import annotations

import csv
import shutil
import sys
import warnings
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402
import vs_sl03_writeback as wb  # noqa: E402

warnings.filterwarnings("ignore")
ROOT = v1.ROOT
V3 = "features/vehicle_setting/reports/vf230_settings_dryrun_v3.tsv"
V4 = "features/vehicle_setting/reports/vf230_settings_dryrun_v4.tsv"
RESOLUTION = "features/vehicle_setting/reports/_v4_branch3_resolution.tsv"
SANDBOX = "features/vehicle_setting/sandbox/vssl/vf230_vssl.xlsx"
BACKUP = "features/vehicle_setting/sandbox/vssl/vf230_vssl.v3.bak.xlsx"

BRANCH = {"R1": "(2b) 家族閘 No.267", "R1b": "(2c) 解析器補（引號式條件）",
          "R2": "(2d) FIP 常數，無條件可加", "R3": "(3) 二來源皆空"}


def build_v4() -> list[dict]:
    res = {r["row"]: r for r in csv.DictReader(open(ROOT / RESOLUTION), delimiter="\t")}
    out = []
    for row in csv.DictReader(open(ROOT / V3), delimiter="\t"):
        r = res.get(row["row"])
        if r:
            flags = {f for f in row["flags"].split("｜")[0].split(";") if f}
            flags.discard("PROXI_PENDING")
            flags.add(r["subcase"])
            if r["resolution"] in ("R1", "R1b"):
                row["proxi_proposed"] = r["proxi_added"]
            elif r["resolution"] == "R2":
                row["proxi_proposed"] = ""
            else:
                flags.add("PROXI_PENDING")
            row["flags"] = ";".join(sorted(flags)) + f"｜分支 {BRANCH[r['resolution']]}"
        out.append(row)
    return out


def main() -> int:
    rows = build_v4()
    v1.write_tsv(ROOT / V4, rows)

    src, bak = ROOT / SANDBOX, ROOT / BACKUP
    # **不覆寫既有備份**：本腳本重跑時 `SANDBOX` 已是 v4 稿，
    # 覆寫會把 v4 當成 v3 存起來（本輪曾犯，見上繳 §5）。
    if src.exists() and not bak.exists():
        shutil.copy2(src, bak)
    wb.BOOKS["vf230"] = (v1.VF230, SANDBOX, V4)   # 沙盒稿改依 v4 報告重生
    s = wb.run("vf230")
    if s["removed"]:
        p = ROOT / "features/vehicle_setting/reports/vf230_removed_non_nafta.tsv"
        with open(p, "w", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["row", "req_id", "setting", "reason"],
                               delimiter="\t")
            w.writeheader()
            w.writerows(s["removed"])

    br = Counter(r["flags"].split("｜分支 ")[1] for r in rows)
    fc = Counter(f for r in rows for f in r["flags"].split("｜")[0].split(";") if f)
    print("v4 分支:", dict(br))
    print("v4 PROXI_PENDING:", fc.get("PROXI_PENDING", 0))
    print(f"沙盒稿重生：{s['rows_before']} → {s['rows_after']} 列；改動 {s['cells']} 處；"
          f"移除 {len(s['removed'])} 列（v3 稿存 {Path(BACKUP).name}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
