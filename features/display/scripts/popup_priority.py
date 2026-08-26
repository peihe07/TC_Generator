#!/usr/bin/env python3
"""29 包步驟 3：`popup_priority.tsv` —— 以**類別碼**為鍵之仲裁順序表。

DM2 由「索件阻斷」降為「可建，帶已知缺口」（29 包 §三.1）。本表之鍵
**不是 popup id** —— 2021 之 Priority Matrix 全篇 0 個 PU 編號，
其以類別（`RVC`／`Cat. X`／`Cat. SL`／…）排序；接合點在
`Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁之**欄 5**（無表頭）。

序來源：矩陣 page 4 之明序清單（逐字）。
**`Cat. SL` 之位置未裁定**（B17：p4／p9／p10 三處說法不同），
故凡 SL 一律 `PENDING: DR-DM2 Cat SL precedence`（R-G33 之同型揭露）。

三項強制揭露（29 包 §三.2）全數寫入 sidecar 之 `notes`，缺一不得交付。
"""
import collections
import re
import subprocess
import sys
import warnings
from pathlib import Path

import fitz
import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tsv_meta import write_meta  # noqa: E402

warnings.filterwarnings("ignore")
FEAT = Path(__file__).resolve().parents[1]
PDF = FEAT / "inputs/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf"
XLS = FEAT / "inputs/Pop Up List HMI R1 (26PI).xlsx"
OUT = FEAT / "data/popup_priority.tsv"
CAT_COL = 5          # `Main` 分頁之類別欄，**無表頭**
ORDER_PAGE = 4       # 明序清單所在頁（1-based）

# 矩陣 page 4 之明序清單（逐字，higher to lower）→ 清單欄 5 之寫法
LADDER = [
    ("RVC", "RVC"),
    ("Cat. X", "X"),
    ("Cat. SL", "SL"),
    ("Anti-Theft  (Keypad and Anti-Theft pop-ups)", None),
    ("Cat. 1", "1"),
    ("Display off (black curtain, which is not a pop-up but a window layer)", None),
    ("Cat. 2  and Cat. VR", "2"),
    ("Cat. 2  and Cat. VR", "VR"),
    ("Cat. 3", "3"),
]
# `Cat. 1` 之兩個子類（矩陣 page 7 逐字：`1P (Phone)`／`1T (Temperature)`）
SUBCAT = {"1P": "1", "1T": "1"}
SL_PENDING = "PENDING: DR-DM2 Cat SL precedence"


def _verify_bindings():
    r = subprocess.run([sys.executable, str(FEAT / "scripts/verify_reference_binding.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("binding check failed:\n" + r.stdout + r.stderr)
    return re.search(r"^entries: (\d+)$", r.stdout, re.M).group(1)


def main() -> int:
    entries = _verify_bindings()

    doc = fitz.open(PDF)
    page4 = [x.strip() for x in doc[ORDER_PAGE - 1].get_text().splitlines() if x.strip()]

    rank, code_rank = {}, {}
    for i, (label, code) in enumerate(LADDER, 1):
        rank.setdefault(label, i)
        if code:
            code_rank.setdefault(code, i)
    for sub, parent in SUBCAT.items():
        code_rank[sub] = code_rank[parent]

    ws = openpyxl.load_workbook(XLS, data_only=True)["Main"]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    pus = [r for r in rows if r and r[0] and str(r[0]).strip().startswith("PU")]

    out = []
    for r in pus:
        pu = str(r[0]).strip()
        raw = "" if r[CAT_COL] is None else str(r[CAT_COL]).strip()
        code = raw.replace("\n", " ")
        pr = code_rank.get(raw)
        if pr is None:
            out.append(dict(popup_id=pu, category_raw=code or "NA",
                            category_code="UNRESOLVED", priority_rank="UNRESOLVED",
                            ladder_label="UNRESOLVED",
                            note="欄 5 之值非單一矩陣類別（複合／無類別）；解析規則未定（B19）"))
            continue
        label = next(l for l, c in LADDER if c == SUBCAT.get(raw, raw))
        out.append(dict(popup_id=pu, category_raw=code, category_code=raw,
                        priority_rank=str(pr), ladder_label=label,
                        note=SL_PENDING if raw == "SL" else ""))

    cols = ["popup_id", "category_raw", "category_code", "priority_rank",
            "ladder_label", "note"]
    OUT.write_text("\t".join(cols) + "\n"
                   + "".join("\t".join(x[c] for c in cols) + "\n" for x in out),
                   encoding="utf-8")

    unresolved = sum(1 for x in out if x["priority_rank"] == "UNRESOLVED")
    sl = sum(1 for x in out if x["category_code"] == "SL")
    write_meta(
        OUT, cols, len(out),
        generated_by="features/display/scripts/popup_priority.py",
        inputs=[f"{PDF.name} (reference: popup_priority_matrix)",
                f"{XLS.name} (reference: popup_list)"],
        rulings=["R-G36", "R-DM30", "R-G23", "R-G26", "R-G33"],
        measurement_conditions=(
            f"序來源：矩陣 page {ORDER_PAGE} 之 `Window Pop-up priorities (higher to lower)` "
            f"明序清單，逐字九列；對應來源：`{XLS.name}` `Main` 分頁**欄 {CAT_COL}"
            f"（無表頭）**；popup 列之判準為欄 0 以 `PU` 起始；"
            f"`1P`/`1T` 依矩陣 page 7 之逐字定義併入 `Cat. 1`；"
            f"綁定檢查 entries: {entries}"),
        notes=(
            "**三項強制揭露（29 包 §三.2），缺一不得交付：**\n"
            f"(1) **B17 —— `Cat. SL` 之位置未裁定**：矩陣 page 4 之明序清單置其於 "
            "`Cat. X` 之下；page 9 逐字稱其 `This category is maximum priority`；"
            "page 10 稱 `Cat. SL is stacked under RVC`。**三處說法不同。** "
            f"本表暫依 page 4 給 rank 3，並於該 {sl} 列之 `note` 標 "
            f"`{SL_PENDING}`。凡涉 SL 之仲裁不得逕用本表。\n"
            "(2) **B18 —— 類別語意漂移未測**：本表之效力以「2021 SR24 1A 之類別定義"
            "於 26PI 仍適用」為前提。**該前提未經證明** —— 逐字比對只能證明六個類別 "
            "token 之詞彙未漂移，不能證明同一個 `1T` 在 2021 與 2026 指同一件事。\n"
            f"(3) **B19 —— {unresolved} 列未覆蓋**，於表中標 `UNRESOLVED`，未省略。"
            "其值為 `---`／`RVC-X`／空／`2 SL`／`Custom`／`RVC\\n2`／`-`；"
            "**複合值須另定解析規則，本輪不定**。\n\n"
            "**本表之鍵為類別碼，非 popup id** —— 矩陣全篇 0 個 PU 編號。"),
        ladder_verbatim=[l for l in page4],
    )

    c = collections.Counter(x["priority_rank"] for x in out)
    print("# popup_priority —— 以類別碼為鍵之仲裁順序（R-G36 機器抽取）")
    print(f"binding: entries: {entries}")
    print(f"母體   : `Main` 之 PU 列 **{len(pus)}**")
    print(f"已解析 : **{len(out) - unresolved}**   UNRESOLVED: **{unresolved}**")
    print()
    print("| rank | ladder_label（矩陣 p4 逐字） | code | 列數 |")
    print("|---|---|---|---:|")
    for label, code in LADDER:
        if not code:
            print(f"| {rank[label]} | {label} | （清單欄 5 無對應寫法） | — |")
            continue
        n = sum(1 for x in out if x["category_code"] == code)
        star = " **← PENDING**" if code == "SL" else ""
        print(f"| {code_rank[code]} | {label}{star} | `{code}` | {n} |")
        for sub, parent in SUBCAT.items():
            if parent != code:
                continue
            ns = sum(1 for x in out if x["category_code"] == sub)
            print(f"| {code_rank[sub]} | {label} —— 子類（矩陣 p7 逐字） | `{sub}` | {ns} |")
    print(f"| — | （未覆蓋） | `UNRESOLVED` | {unresolved} |")
    tot = sum(1 for x in out if x["priority_rank"] != "UNRESOLVED") + unresolved
    print(f"\n**合計 {tot} 列 = PU 母體 {len(pus)} 列**"
          f"（{'相符' if tot == len(pus) else '**不符**'}）")
    print()
    print(f"-> {OUT.relative_to(FEAT.parents[1])}")
    print(f"-> {OUT.name}.meta.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
