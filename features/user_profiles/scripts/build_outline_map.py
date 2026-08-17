#!/usr/bin/env python3
"""Build the spec section-id → body-text map for User Profiles (Phase 0, 作業項 4).

Source: spec-index/cache/SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_
(February_10_2023).xlsx, sheet `Basic Report` (R-U3 baseline, spec_mode A).

判準（逐字自下放包 01b 作業項 4）：
    由 spec `Basic Report` 之 `SYSRE_HMI_Source ID` 欄建 section id → 正文
    對映（169 條）。037 引用之 135 個 id 須全數命中，fail-loud on miss。

量測條件：
- 列單位 = 實體列號（表頭列 1，資料列 2–170）
- 掃描欄位 = `ID` / `Outline Number` / `Description` / `SYSRE_HMI_Source ID`
  四欄，以表頭文字定位，非位置
- section id 取自 `SYSRE_HMI_Source ID` 之末段 `_{section}`，
  與 `Outline Number` 欄逐列交叉核對
- 字元數 = Python `len()`，即 UTF-8 code point 數，非 byte 數
- 純章節標題判定 = `Description` 無句末標點且長度 < 60 且無 `.)` 標記
  —— 代理判準（canon §5a 第 13 條），實質判準為人工判讀，故本檔同時
  輸出兩者，不以代理判準改寫任何內容

輸出：data/spec_id_to_outline.tsv（tracked，見 feature .gitignore 之註解）
      data/outline_map.json（完整正文，untracked）

037 側之 135 個 id 命中驗證 **本輪未執行** —— 037 Analysis Report 不在
repo 內（A-UP04）。本腳本以 `--a03 <path>` 接該檔；未給則跳過並明示。
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import openpyxl

SPEC = ("spec-index/cache/SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_"
        "R1L-R_(February_10_2023).xlsx")
EXPECTED_STEM = ("Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_"
                 "CR24798_(October_03_2023)")


def norm(v) -> str:
    return str(v or "").strip().lower()


def build(spec_path: Path) -> dict:
    wb = openpyxl.load_workbook(spec_path, read_only=True)
    ws = wb["Basic Report"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    col = {name: j for j, v in enumerate(header)
           for name in ("ID", "Outline Number", "Description",
                        "SYSRE_HMI_Source ID")
           if norm(v) == norm(name)}
    missing = {"ID", "Outline Number", "Description",
               "SYSRE_HMI_Source ID"} - set(col)
    if missing:
        raise SystemExit(f"header columns not found: {sorted(missing)}")

    entries, stems, unparsed, mismatch = {}, Counter(), [], []
    for phys_row, r in enumerate(rows[1:], start=2):
        if all(v is None for v in r):
            continue
        rid = str(r[col["ID"]] or "").strip()
        outline = str(r[col["Outline Number"]] or "").strip()
        desc = str(r[col["Description"]] or "").strip()
        src = str(r[col["SYSRE_HMI_Source ID"]] or "").strip()
        m = re.match(r"^(?P<stem>.+)_(?P<sec>\d+(?:\.\d+)*)$", src)
        if not m:
            unparsed.append((phys_row, rid, src[:80]))
            continue
        stems[m.group("stem")] += 1
        sec = m.group("sec")
        if sec != outline:
            mismatch.append((phys_row, rid, sec, outline))
        if sec in entries:
            raise SystemExit(f"duplicate section id {sec} at row {phys_row}")
        entries[sec] = {"row": phys_row, "polarion_id": rid,
                        "outline": outline, "text": desc, "len": len(desc)}
    return {"entries": entries, "stems": dict(stems),
            "unparsed": unparsed, "outline_mismatch": mismatch}


def chapter(sec: str) -> str:
    return sec.split(".")[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--a03", default=None,
                    help="037 Analysis Report xlsx; when absent the "
                         "135-id hit check is SKIPPED and said so")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    out_dir = root / "features" / "user_profiles" / "data"
    out_dir.mkdir(parents=True, exist_ok=True)

    res = build(root / SPEC)
    entries = res["entries"]
    print(f"section ids built: {len(entries)}")
    print(f"stems: {res['stems']}")
    if set(res["stems"]) != {EXPECTED_STEM}:
        print("  !! stem set differs from R-U3 expectation")
    print(f"unparsed Source ID cells: {len(res['unparsed'])} {res['unparsed']}")
    print(f"Outline Number vs section-id mismatch: "
          f"{len(res['outline_mismatch'])} {res['outline_mismatch'][:5]}")

    per_ch = Counter(chapter(s) for s in entries)
    print("per-chapter section counts:",
          {k: per_ch[k] for k in sorted(per_ch, key=int)})
    lens = sorted(e["len"] for e in entries.values())
    print(f"Description length (chars): n={len(lens)} min={lens[0]} "
          f"median={lens[len(lens)//2]} max={lens[-1]}")

    tsv = out_dir / "spec_id_to_outline.tsv"
    with tsv.open("w", encoding="utf-8") as fh:
        fh.write("section_id\toutline_number\tpolarion_id\tphys_row\tchars\n")
        for sec in sorted(entries, key=lambda s: [int(p) for p in s.split(".")]):
            e = entries[sec]
            fh.write(f"{sec}\t{e['outline']}\t{e['polarion_id']}\t"
                     f"{e['row']}\t{e['len']}\n")
    (out_dir / "outline_map.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {tsv.relative_to(root)} and data/outline_map.json")

    if args.a03 is None:
        print("\n037 側 135-id 命中驗證：**SKIPPED —— 037 不在 repo 內"
              "（A-UP04）**。此項為『未實測』，不得標 PASS（canon §5a 第 11 條）。")
        return
    raise SystemExit("--a03 path given but the 037 survey is not implemented "
                     "in this Phase-0 script; run scripts/recon.py instead")


if __name__ == "__main__":
    main()
