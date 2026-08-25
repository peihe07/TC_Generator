#!/usr/bin/env python3
"""24-4（27 包解封）：`popup_priority.tsv` 之**來源登記**，機器抽取（R-G36）。

本腳本**不建仲裁順序表**（該表待 DR-DM2，見 BACKLOG A1）。它只登記
「哪一份素材、哪一個位置、逐字說了什麼」，使日後建表者不必重查。

登記標的（下放包 24 §2.4）：
  - `{CFTS013-937}` 之全文與其對 `PU0130` 之逐字指名
  - 該條所載之優先序行為（何者高於 `PU0130`）

**HU 側之事實**：CFTS013 之標的為 Associated Display（R-DM51），
非本 feature 之 DCSD。故 `side` 欄一律 `HU (Associated Display)`，
**其值不得代入 DCSD 標的**（R-DM51(a)）。

輸出：`data/popup_priority_sources.tsv` ＋ sidecar（R-DM30）。
"""
import re
import sys
import warnings
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tsv_meta import write_meta  # noqa: E402

warnings.filterwarnings("ignore")
FEAT = Path(__file__).resolve().parents[1]
SRC = FEAT / "inputs/SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx"
OUT = FEAT / "data/popup_priority_sources.tsv"
SHEET = "Analysis Report"
HEADER_ROW = 5          # 1-based，資料自第 6 列
POPUP = re.compile(r"\bPU\d{4}\b")

# 詞表為**人所給定**（同 B9／B11 之形態，故具名）。其來由：以 `PU\d{4}`
# 抽取只得 1 列，反向查證（上繳 27 §4.4）顯示本檔另有三列以文字指涉
# 同一 popup 而不帶編號。以編號為唯一判準會漏掉它們。
PHRASES = ("popup", "pop-up", "pop up", "Screen is Hot", "Display is Hot")


def _verify_bindings():
    """R-G23：使用受綁定素材前先比對（同 signal_resolution.py 之慣例）。"""
    import subprocess
    r = subprocess.run([sys.executable,
                        str(FEAT / "scripts/verify_reference_binding.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("binding check failed:\n" + r.stdout + r.stderr)
    return r.stdout


def main() -> int:
    binding = _verify_bindings()
    entries = re.search(r"^entries: (\d+)$", binding, re.M).group(1)

    wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
    rows = [list(r) for r in wb[SHEET].iter_rows(values_only=True)]
    hdr = [("" if c is None else str(c).strip()) for c in rows[HEADER_ROW - 1]]

    def col(sub):
        for i, h in enumerate(hdr):
            if sub in h:
                return i
        raise KeyError(sub)

    c_doc, c_desc, c_cat = (col("Document ID"), col("需求描述 Description"),
                            col("分類\nCategory"))

    found = []
    for ri, r in enumerate(rows[HEADER_ROW:], start=HEADER_ROW + 1):
        desc = "" if r[c_desc] is None else str(r[c_desc])
        ids = sorted(set(POPUP.findall(desc)))
        phrases = sorted(p for p in PHRASES if p.lower() in desc.lower())
        if not (ids or phrases):
            continue
        found.append({
            "source_locator": f"{SRC.name}!{SHEET}!r{ri}",
            "document_id": "" if r[c_doc] is None else str(r[c_doc]).strip(),
            "category": "" if r[c_cat] is None else str(r[c_cat]).strip(),
            "matched_by": "id" if ids else "phrase",
            "popup_ids": " ¦ ".join(ids) if ids else "NA",
            "matched_phrases": " ¦ ".join(phrases) if phrases else "NA",
            "side": "HU (Associated Display)",
            "verbatim": " ".join(desc.split()),
        })

    cols = ["source_locator", "document_id", "category", "matched_by",
            "popup_ids", "matched_phrases", "side", "verbatim"]
    OUT.write_text("\t".join(cols) + "\n"
                   + "".join("\t".join(row[c] for c in cols) + "\n"
                             for row in found), encoding="utf-8")

    write_meta(
        OUT, cols, len(found),
        generated_by="features/display/scripts/popup_priority_sources.py",
        inputs=[f"{SRC.name} (reference: cfts013_sysra)"],
        rulings=["R-G36", "R-DM51", "R-DM30", "R-G23", "R-G26"],
        measurement_conditions=(
            f"openpyxl read_only data_only；sheet={SHEET!r}；表頭列 {HEADER_ROW}，"
            f"資料自第 {HEADER_ROW + 1} 列；popup id 之抽取式 r'\\bPU\\d{{4}}\\b'；"
            f"verbatim 欄為 Description 之空白正規化（' '.join(split())），"
            f"未改動任何字元內容；綁定檢查 entries: {entries}"),
        notes=(
            "**來源登記，非仲裁順序表。** 仲裁表待 DR-DM2（BACKLOG A1）。"
            "本檔之全部內容為 Associated Display（HU 側）之事實；"
            "依 R-DM51(a) 不得代入 DCSD 標的 —— `verbatim` 欄內之溫度值"
            "（56／60 degrees C 等）為 HU 顯示器之門檻，**與 DCSD 之 85 無關**。"
            "以編號為唯一判準只得 1 列；反向查證後改為二擇一，得 4 列。"),
    )

    print(f"# popup_priority_sources —— 來源登記（R-G36 機器抽取）")
    print(f"source : {SRC.name}")
    print(f"binding: entries: {entries}（R-G23 已於入口比對）")
    print(f"母體   : {SHEET!r} 之資料列 {len(rows) - HEADER_ROW}"
          f"（第 {HEADER_ROW + 1} 列起）")
    print(f"命中   : 含 popup 指涉之列 **{len(found)}**")
    print()
    for row in found:
        print(f"## {row['document_id']}  ({row['category']})  @ {row['source_locator']}")
        print(f"   matched_by: {row['matched_by']}   "
              f"popup_ids: {row['popup_ids']}   phrases: {row['matched_phrases']}")
        print(f"   {row['verbatim']}")
        print()
    print(f"-> {OUT.relative_to(FEAT.parents[1])}")
    print(f"-> {OUT.name}.meta.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
