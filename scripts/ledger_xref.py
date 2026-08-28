#!/usr/bin/env python3
"""包內台帳引用對照（R-POP17 第 2 項，下放包 03 §五-3）。

**由來 —— A-POP9(1)**：下放包 02 之上繳回報把 anomaly 編號寫錯，
而分析層落 R-POP12／13／14 時又**轉抄了那份摘要**而未 live 查
`ANOMALIES.md`，於是 `RULINGS.md` 內三條條文各自掛錯了 anomaly。
三簿彼此矛盾，而當時沒有任何一支工具在看這件事。

**這正是 `ledger_xref` 設計目的（把同一標的之記載並列）之內、
而既有實作未涵蓋的型態**：既有的
`features/vehicle_category/scripts/ledger_xref.py` 之 ROOT 硬綁該
feature，且其對象是「同一標的的多處記載並列供人判讀」；本檔要的是
**機械可判之對照**，且須跨 feature 通用，故另立於 `scripts/`。
二者是否合併，屬全域政策，留待 Pei 裁（見上繳包 03）。

三檢：

| 檢 | 判準 | 何以機械可判 |
|---|---|---|
| `unknown_id` | 下放／上繳包與 `RULINGS.md` 內之 `A-<F>n`／`DR-<F>n` 引用，須實存於該 feature 台帳（全檔所有表格） | 號碼是不是在簿上，不需語意判斷 |
| `pairing` | `RULINGS.md` 之**條文標題列**所掛之 anomaly／DR 號，其台帳列之處分欄須回指同一條 | A-POP9(1) 之原型：R-POP12 掛 A-POP6，而 A-POP6 之列寫的是 R-POP16 |
| `ledger_shape` | 於**採明細節體例的台帳**內，每一號須有 `## <id>` 節，反之亦然 | 標題層之對照；A-POP9 當時只有主表列而無明細節 |

**盲區（明說）**：`pairing` **只掃 `RULINGS.md` 之 `### R-…` 標題列**。
下放／上繳包正文之敘述句常在同一行並列多個號碼而彼此無隸屬關係
（如「已更正為 A-POP7／A-POP9／A-POP8…寫入 R-POP15 F5」），
以行為單位配對即爆假陽性。正文之引用只受 `unknown_id` 之檢。
**他 feature 之號碼（如 popup 包內引用之 `A-SX18`）一律不對照，只報數。**
`ledger_shape` **只施於該檔自己已在用明細節體例時**：`DATA_REQUESTS.md`
多為純表格簿，對它要求 `## DR-POPn` 是把一種體例強加於另一種，
而 R-POP16 丙 已裁「不強制統一版面」。

唯讀，絕不寫入任何檔案。`--gate` 指定時任一違規 exit 1。

Usage:
    python scripts/ledger_xref.py --feature popup
    python scripts/ledger_xref.py --feature popup --gate
    python scripts/ledger_xref.py --feature popup --live   # 供上繳包 live 貼用
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_docs036 import bare, tables  # noqa: E402

RE_REF = re.compile(r"\b(A|DR)-([A-Z]{1,6})(\d+)\b")
RE_RULING_REF = re.compile(r"\bR-([A-Z]{1,6})(\d+)\b")
RE_RULING_HEAD = re.compile(r"^#{2,4}\s+R-([A-Z]{1,6})(\d+)\b")
# `## A-POP9 —— …` 與 `## [A-AM01] …` 兩種體例都認 —— 方括號式為
# audio_mgmt／driver_distraction 之寫法，不認它就會把整本簿子看成空的。
RE_SECTION_HEAD = re.compile(r"^#{2,4}\s+\[?((?:A|DR)-[A-Z]{1,6}\d+)\]?\b")

# 狀態／處分欄之表頭字面。各 feature 之台帳欄序不一（popup 之 ANOMALIES
# 為第 3 欄、DATA_REQUESTS 為第 5 欄），故以表頭定位而非以欄序。
STATUS_HEADERS = {"狀態", "Status", "狀態／處分", "處置", "處分"}


@dataclass
class Entry:
    """台帳主表之一列。"""
    ident: str
    title: str
    status: str
    rulings: set[str]      # 處分欄所指之條號
    has_section: bool = False


@dataclass
class Finding:
    check: str
    where: str
    detail: str
    # 補零寫法不一（`A-PW1` ↔ `A-PW01`）降 note：那是體例不齊，
    # 不是引用了不存在的號。混在紅裡會把真的 `unknown_id` 埋掉。
    severity: str = "red"


def key(ident: str) -> tuple[str, str, int]:
    """比對鍵：補零不計。`A-PW1` 與 `A-PW01` 指同一件事。"""
    m = RE_REF.fullmatch(ident)
    return (m.group(1), m.group(2), int(m.group(3)))


def parse_ledger(path: Path) -> tuple[dict[str, Entry], bool, bool]:
    """讀一本台帳。回傳 `(號 → Entry, 該檔是否採明細節體例, 表格內是否有號碼)`。

    **號碼之收集跨全檔所有表格，與 `lint_docs036.series_in` 之「限主表」
    刻意不同**，理由是兩者在問不同的問題：那裡問「本 feature 該對哪些
    系列負跳號之責」，答錯會把別人的簿子拖進來；這裡問「這個號碼在不在
    簿上」，而長台帳常被空行切成數十個 markdown 表格
    （`features/power/ANOMALIES.md` 之 A-PW 主表即被切成多段，
    只認首段會少掉 A-PW100 以後全部，一次生出 640 筆假的 `unknown_id`）。
    **存在性不需要先認定哪一張才是主表。**
    """
    if not path.is_file():
        return {}, False, False
    text = path.read_text(encoding="utf-8")
    all_tables = tables(text)
    out: dict[str, Entry] = {}
    # 處分條號只自**狀態欄**取。取整列會把「內容」欄裡順帶提到的條號
    # 當成處分（A-POP6 之內容欄就寫著「R-POP10 新規使…」），
    # 對照本身就先被自己的雜訊淹掉。欄序各 feature 不一，故以表頭定位；
    # 表頭只在首個表格出現，其後之續段沿用它。
    status_i = None
    if all_tables:
        header = [bare(c) for c in all_tables[0][0]]
        status_i = next((i for i, h in enumerate(header)
                         if h in STATUS_HEADERS), None)
    for table in all_tables:
        for row in table:
            ident = bare(row[0])
            if not RE_REF.fullmatch(ident) or ident in out:
                continue
            body = (row[status_i] if status_i is not None and status_i < len(row)
                    else " ".join(row[2:]))
            out[ident] = Entry(
                ident=ident,
                title=bare(row[1]) if len(row) > 1 else "",
                status=(bare(row[status_i])
                        if status_i is not None and status_i < len(row)
                        else (bare(row[2]) if len(row) > 2 else "")),
                rulings={f"R-{p}{n}" for p, n in RE_RULING_REF.findall(body)},
            )
    for line in text.splitlines():
        m = RE_SECTION_HEAD.match(line)
        if m and m.group(1) in out:
            out[m.group(1)].has_section = True
    # 有明細節而台帳表格無列者，補一筆空殼 —— 兩向都要看得見。
    for line in text.splitlines():
        m = RE_SECTION_HEAD.match(line)
        if m and m.group(1) not in out:
            out[m.group(1)] = Entry(m.group(1), "", "（台帳表格無列）", set(),
                                    has_section=True)
    from_tables = {i for i, e in out.items() if e.status != "（台帳表格無列）"}
    return out, any(e.has_section for e in out.values()), bool(from_tables)


def feature_prefixes(ledger: dict[str, Entry]) -> set[str]:
    """本 feature 之系列前綴，自台帳實存號碼抽取（不硬寫）。"""
    return {RE_REF.fullmatch(i).group(2) for i in ledger}


def scan_files(root: Path, feature: str) -> list[Path]:
    base = root / "features" / feature
    files = sorted((base / "docs/handoff").glob("*.md"))
    files += sorted((base / "docs/upstream").glob("*.md"))
    if (base / "RULINGS.md").is_file():
        files.append(base / "RULINGS.md")
    return files


def check(root: Path, feature: str) -> tuple[list[Finding], dict, list[Path]]:
    base = root / "features" / feature
    ledger: dict[str, Entry] = {}
    sectioned: set[str] = set()   # 該檔採明細節體例 → 缺節可判
    tabled: set[str] = set()      # 該檔表格內確有號碼 → 缺列可判
    empty_books: list[str] = []
    for name in ("ANOMALIES.md", "DATA_REQUESTS.md"):
        part, uses_sections, has_rows = parse_ledger(base / name)
        if (base / name).is_file() and not part:
            empty_books.append(name)
        ledger |= part
        if uses_sections:
            sectioned |= set(part)
        if has_rows:
            tabled |= set(part)
    out: list[Finding] = []
    if not ledger:
        return ([Finding("ledger_shape", feature, "台帳主表抽不到任何號碼")],
                {}, [])

    # 該 feature 之台帳裡完全抽不到號碼者（版面不同），其對應之引用一律
    # 不判 `unknown_id` —— 拿一本空簿子去否定 129 處引用，報出來的是
    # 工具自己的盲區，不是語料的缺陷（G-D）。
    kinds_present = {key(i)[0] for i in ledger}
    for name in empty_books:
        out.append(Finding("ledger_shape", f"{feature}/{name}",
                           "抽不到任何號碼（版面不同，G-D 盲區）——"
                           "其對應之引用本輪不受 unknown_id 之檢",
                           severity="note"))

    prefixes = feature_prefixes(ledger)
    by_key = {key(i): i for i in ledger}
    stats = {"refs": 0, "foreign": 0, "padding": 0, "prefixes": sorted(prefixes)}

    # --- ledger_shape：主表列 ↔ 明細節，兩向 --------------------------------
    for ident, e in sorted(ledger.items()):
        if not e.has_section and ident in sectioned:
            out.append(Finding("ledger_shape", ident,
                               f"台帳有列（{e.title[:24]}…）而無 `## {ident}` 明細節"))
        if e.status == "（台帳表格無列）" and ident in tabled | sectioned & tabled:
            out.append(Finding("ledger_shape", ident,
                               "有明細節而表格無列 —— 摘要 live 產時抓不到它"))

    for path in scan_files(root, feature):
        rel = path.relative_to(root)
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            # --- unknown_id ------------------------------------------------
            for kind, pfx, num in RE_REF.findall(line):
                ident = f"{kind}-{pfx}{num}"
                if pfx not in prefixes:
                    stats["foreign"] += 1
                    continue
                stats["refs"] += 1
                if ident in ledger:
                    continue
                if kind not in kinds_present:
                    continue     # 該類（A-／DR-）在本 feature 之台帳裡整本抽不到
                same = by_key.get(key(ident))
                if same is not None:
                    stats["padding"] += 1
                    out.append(Finding(
                        "padding", f"{rel}:{lineno}",
                        f"引用 {ident}，台帳寫作 {same} —— 補零寫法不一",
                        severity="note"))
                else:
                    out.append(Finding("unknown_id", f"{rel}:{lineno}",
                                       f"引用 {ident}，台帳無此號"))
            # --- pairing：只及於 RULINGS.md 之條文標題列 ---------------------
            head = RE_RULING_HEAD.match(line)
            if head is None or path.name != "RULINGS.md":
                continue
            ruling = f"R-{head.group(1)}{head.group(2)}"
            for kind, pfx, num in RE_REF.findall(line):
                ident = f"{kind}-{pfx}{num}"
                e = ledger.get(ident) or ledger.get(by_key.get(key(ident), ""))
                if e is None or pfx not in prefixes:
                    continue
                if not e.rulings:
                    continue          # 台帳未載處分條號，無從對照，不報
                if ruling not in e.rulings:
                    out.append(Finding(
                        "pairing", f"{rel}:{lineno}",
                        f"{ruling} 之標題掛 {ident}，但台帳 {ident} 之處分欄"
                        f"載為 {'／'.join(sorted(e.rulings))} —— 兩處不相認"))
    return out, stats, scan_files(root, feature)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="ledger_xref.py", description=__doc__)
    ap.add_argument("--root", default=".")
    ap.add_argument("--feature", default="popup")
    ap.add_argument("--gate", action="store_true", help="任一違規 exit 1")
    ap.add_argument("--live", action="store_true",
                    help="印台帳現況表（R-POP17-1：上繳摘要自此產，不手寫）")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    findings, stats, files = check(root, args.feature)

    if args.live:
        base = root / "features" / args.feature
        ledger: dict[str, Entry] = {}
        for name in ("ANOMALIES.md", "DATA_REQUESTS.md"):
            ledger |= parse_ledger(base / name)[0]
        print(f"# {args.feature} 台帳現況（自 repo live 產，R-POP17-1）\n")
        print("| 號 | 狀態 | 處分條 |")
        print("|---|---|---|")
        for ident, e in sorted(ledger.items(),
                               key=lambda kv: (kv[0].split("-")[0],
                                               int(re.search(r"\d+$", kv[0]).group()))):
            print(f"| {ident} | {e.status or '（空）'} | "
                  f"{'／'.join(sorted(e.rulings)) or '—'} |")
        print()

    print(f"掃 {len(files)} 檔（handoff／upstream／RULINGS）"
          f"　本 feature 前綴 {stats.get('prefixes')}"
          f"　本 feature 引用 {stats.get('refs', 0)} 處"
          f"　他 feature 引用 {stats.get('foreign', 0)} 處（不對照，R-POP16 甲）"
          f"　補零寫法不一 {stats.get('padding', 0)} 處（降 note）")

    reds = [x for x in findings if x.severity != "note"]
    notes = [x for x in findings if x.severity == "note"]
    if notes:
        print(f"note（不判紅）：{len(notes)} 項")
        for x in notes[:20]:
            print(f"  [{x.check}] {x.where}：{x.detail}")
        if len(notes) > 20:
            print(f"  …另 {len(notes) - 20} 項同型，未逐筆列出")

    if not reds:
        print(f"ledger_xref：PASS（{args.feature}）")
        return 0
    print(f"ledger_xref：{len(reds)} 項")
    for x in reds:
        print(f"  [{x.check}] {x.where}：{x.detail}")
    return 1 if args.gate else 0


if __name__ == "__main__":
    raise SystemExit(main())
