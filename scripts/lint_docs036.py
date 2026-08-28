#!/usr/bin/env python3
"""FW036 治理文件之結構檢查（`docs_structure`，21 包 §五）。

`lint036.py` 檢查工作簿，本工具檢查**支撐工作簿的三份文件**：
裁決台帳、DATA_REQUESTS、ANOMALIES。二者互補 —— A-PM17 之成因
（落檔位置表以「同上」串接指涉，插入列即靜默改變其後各列之指涉對象）
於工作簿層無從察覺，須由本工具承接。

唯讀，絕不寫入任何檔案。`--gate` 指定時任一違規 exit 1。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

LEDGER = "docs/fw036/RULINGS_LEDGER.md"
LEGAL_STATUS = {"ACTIVE", "[DEFAULT]", "SUPERSEDED", "WITHDRAWN"}
RE_ROW = re.compile(r"^\|(.+)\|\s*$")
RE_SEP = re.compile(r"^\|[\s:\-|]+\|\s*$")
RE_STRIKE = re.compile(r"~~(.*?)~~")
RE_RULING_ID = re.compile(r"^(R-\d+[a-z]?|R-1 v\d+|S\d+|N-\d+)$")
# R-POP10（Pei 2026-08-27）：前綴不再硬寫。`A-POP`／`DR-POP` 之所以能整輪
# 不受檢而 gate 全綠，正是因為清單是人手維護的枚舉（G-B：枚舉型判準一律
# 接對照）。改為自語料抽取 `(A|DR|R)-[A-Z]+`，並保留下方之時代清單
# 專供差集對照 —— 保留它不是為了再用它判斷，是為了讓「新抽到了什麼、
# 舊清單漏了什麼」在紙上看得見。
#
# 交替之順序有意義：`R`／`S` 之單字母分支須排在複合前綴之前，
# 而複合分支 `(?:A|DR|R)-[A-Z]{1,6}` 靠回溯接手 `R-POP5` 這類 ——
# 先試 `R` 剩下 `-POP5` 不合 `-?\d+`，回溯後才取 `R-POP`＋`5`。
RE_SERIES = re.compile(r"^(?P<prefix>R|S|(?:A|DR|R)-[A-Z]{1,6})-?(?P<num>\d+)$")

# 硬寫時代之清單。**不再參與判斷**，只作 G-B 差集之被減數。
LEGACY_PREFIXES = ("DR-PW", "A-PW", "A-PM")

# 前綴 → 語料中該前綴與數字之間實際的字串（`R-27` 為 "-"，`A-POP4` 為 ""）。
# 以首次見到者為準；跳號回報照它重組編號，回報出來的字串才 grep 得到。
SEPARATORS: dict[str, str] = {}

# `prefix_reconciliation` 最近一次跑之「主表外前綴命中數」（A-POP10）。
LAST_OFF_PRIMARY = 0


@dataclass
class Finding:
    check: str
    where: str
    detail: str
    # R-POP16 乙：跨表重複降為 note。note 照印但不計入 `--gate` 之 exit ——
    # 「印出來」與「擋下來」是兩件事，混為一談就只剩得下其中一件。
    severity: str = "red"


def cells(line: str) -> list[str]:
    m = RE_ROW.match(line.rstrip())
    return [c.strip() for c in m.group(1).split("|")] if m else []


def tables(text: str) -> list[list[list[str]]]:
    """抽出所有 markdown 表格（各為 rows × cells，不含分隔列）。"""
    out, current = [], []
    for line in text.splitlines():
        if RE_SEP.match(line.rstrip()):
            continue
        row = cells(line)
        if row:
            current.append(row)
        elif current:
            out.append(current)
            current = []
    if current:
        out.append(current)
    return out


def bare(text: str) -> str:
    """去除刪除線與強調標記，取其識別字。"""
    text = RE_STRIKE.sub(r"\1", text)
    return text.replace("**", "").replace("`", "").strip()


def check_ledger(root: Path) -> list[Finding]:
    path = root / LEDGER
    out: list[Finding] = []
    if not path.is_file():
        return [Finding("docs_structure", LEDGER, "檔案不存在")]
    text = path.read_text(encoding="utf-8")

    main, location = None, None
    for table in tables(text):
        head = [bare(c) for c in table[0]]
        if head[:3] == ["編號", "日期", "標題"]:
            main = table[1:]
        elif head[:2] == ["編號", "條文全文所在"]:
            location = table[1:]

    if main is None:
        return [Finding("docs_structure", LEDGER, "找不到裁決主表")]
    if location is None:
        return [Finding("docs_structure", LEDGER, "找不到「條文落檔位置」表")]

    ids = []
    for row in main:
        rid = bare(row[0])
        ids.append(rid)
        if not RE_RULING_ID.match(rid):
            out.append(Finding("ledger_id", rid, "編號格式不合"))
        if len(row) < 4 or not bare(row[3]):
            out.append(Finding("ledger_status", rid, "狀態欄為空"))
        elif bare(row[3]) not in LEGAL_STATUS:
            out.append(Finding("ledger_status", rid,
                               f"狀態值不合法：{bare(row[3])!r}"))
        if len(row) < 3 or not bare(row[2]):
            out.append(Finding("ledger_text", rid, "條文欄為空"))

    dupes = {i for i in ids if ids.count(i) > 1}
    for i in sorted(dupes):
        out.append(Finding("ledger_id", i, "編號重複"))

    nums = sorted(int(m.group("num")) for m in
                  (RE_SERIES.match(i) for i in ids) if m and m.group("prefix") == "R")
    out += gaps("ledger_series", "R", nums)

    located = {bare(row[0]) for row in location}
    for rid in ids:
        if rid not in located:
            out.append(Finding("ledger_location", rid, "未列於落檔位置表"))
    for row in location:
        body = " ".join(row[1:])
        if "同上" in body:
            out.append(Finding("ledger_location", bare(row[0]),
                               "落檔位置以「同上」串接 —— 插入列將靜默改指（A-PM17）"))
    return out


def gaps(check: str, prefix: str, nums: list[int], sep: str = "-") -> list[Finding]:
    """`sep` 取自語料中該前綴實際的寫法 —— `R-27` 有連字號，`A-POP4`／`S3`
    沒有。寫死 `-` 會報出 `A-POP-4` 這種語料裡不存在的編號，讓人拿著它
    grep 不到東西。"""
    if not nums:
        return []
    missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    return [Finding(check, f"{prefix}{sep}{n}", "序號跳號（撤回列亦須保留，R-TM13）")
            for n in missing]


RE_ROW_START = re.compile(r"^\|.*[^|\s]\s*$")


def check_malformed_rows(root: Path, rel: str) -> list[Finding]:
    """表格列以 `|` 起而不以 `|` 收 —— 該列於 markdown 下渲染錯位。"""
    path = root / rel
    if not path.is_file():
        return []
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if RE_ROW_START.match(line.rstrip()):
            head = line.split("|")[1].strip()[:24] if "|" in line else ""
            out.append(Finding("table_row", f"{rel}:{n}",
                               f"表格列缺結尾 `|`（{head!r}）"))
    return out


def series_in(text: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    """`(前綴 → [(編號, 表序)], 被略過之首格數, 非主表前綴之命中數)`。

    **R-POP16 乙（Pei 2026-08-27）**：前綴抽取限定於**檔內首個表格**。
    主表之辨識方式定為此而非「表頭首欄字面」—— 各 feature 表頭不一致
    （`| A |`／`| DR |`／`| 編號 |` 都有），而「首個表格即登記主表」
    是三簿體例之不變量。`privacy` 之假前綴 `S`（欄位值表，
    `ANOMALIES.md` 中段）即由此自然排除。

    **編號仍跨全檔收集**，只是併記其表序：回顧／彙整表之列仍算「該號
    存在」，否則把它們排除掉會把回顧表獨有的號碼變成跳號 —— 修一個
    誤報生一個誤報。同號是否判紅，由 `check_series` 依表序決定。

    逐列掃描，不跳過表首 —— 長條目常被空行切成獨立表格，
    若跳過首列即會漏掉其編號並誤報跳號（本工具開發時實際踩到）。

    第二個回傳值為 **G-D 之被抑制條數**：首格非空但不合系列編號形態者。
    第三個為合系列形態但其前綴不在主表內者 —— 同屬 G-D，須報數，
    否則「限定首表」到底扔掉了多少東西，在紙上看不見。
    """
    all_tables = tables(text)
    if not all_tables:
        return {}, 0, 0

    primary: set[str] = set()
    for row in all_tables[0]:
        m = RE_SERIES.match(bare(row[0]))
        if m:
            primary.add(m.group("prefix"))

    found: dict[str, list[tuple[int, int]]] = {p: [] for p in primary}
    skipped = 0
    off_primary = 0
    for ti, table in enumerate(all_tables):
        for row in table:
            cell = bare(row[0])
            if not cell:
                continue
            m = RE_SERIES.match(cell)
            if not m:
                skipped += 1
                continue
            pfx = m.group("prefix")
            if pfx not in primary:
                off_primary += 1
                continue
            SEPARATORS.setdefault(pfx, cell[len(pfx):-len(m.group("num"))])
            found[pfx].append((int(m.group("num")), ti))
    return found, skipped, off_primary


def check_series(root: Path, rel: str, prefix: str | None = None) -> list[Finding]:
    """跳號檢查。`prefix=None`（預設）＝ 自主表抽取之**每個**前綴都查。

    R-POP16 乙：`編號重複` 之判準改為**同一表格內**重複才判紅；
    同號分散於不同表格（主表一列、回顧表一列）降為 note。
    放寬只及於「跨表」這一項 —— 主表內真的寫了兩次，仍判紅。
    """
    path = root / rel
    if not path.is_file():
        return [Finding("docs_structure", rel, "檔案不存在")]
    found, _, _ = series_in(path.read_text(encoding="utf-8"))
    if prefix is not None:
        found = {prefix: found.get(prefix, [])}

    out: list[Finding] = []
    for pfx, entries in sorted(found.items()):
        where: dict[int, list[int]] = {}
        for num, ti in entries:
            where.setdefault(num, []).append(ti)
        for num in sorted(where):
            tis = where[num]
            if len(tis) == 1:
                continue
            if len(set(tis)) < len(tis):
                out.append(Finding(f"{pfx}_id", f"{pfx}{num}",
                                   "編號重複（同一表格內）"))
            else:
                out.append(Finding(
                    f"{pfx}_id", f"{pfx}{num}",
                    f"同號見於 {len(tis)} 個表格（回顧／彙整表；R-POP16 乙降 note）",
                    severity="note"))
        out += gaps(f"{pfx}_series", pfx, sorted(where), SEPARATORS.get(pfx, "-"))
    return out


def prefix_reconciliation(root: Path, rels: list[str]) -> tuple[list[str], list[str], int]:
    """G-B 對照：抽得之前綴集 vs 硬寫時代清單。回傳 `(抽得, 差集, 略過數)`。"""
    seen: set[str] = set()
    skipped = 0
    off_primary = 0
    for rel in rels:
        path = root / rel
        if not path.is_file():
            continue
        found, n, off = series_in(path.read_text(encoding="utf-8"))
        seen |= set(found)
        skipped += n
        off_primary += off
    newly = sorted(seen - set(LEGACY_PREFIXES))
    # 第三個回傳值仍為「被抑制」總數（向下相容既有測試），
    # `LAST_OFF_PRIMARY` 另記其中屬「主表外前綴」者 —— R-POP16 乙
    # 之限縮到底扔掉了多少東西，不另計就看不見（A-POP10）。
    global LAST_OFF_PRIMARY
    LAST_OFF_PRIMARY = off_primary
    return sorted(seen), newly, skipped + off_primary


def prefix_reconciliation_off() -> int:
    """R-POP16 乙之限縮所丟棄的條目數（A-POP10 之量）。"""
    return LAST_OFF_PRIMARY


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="lint_docs036.py",
        description="FW036 治理文件結構檢查（唯讀）")
    parser.add_argument("--root", default=".", help="repo 根目錄")
    parser.add_argument("--feature", default="power",
                        help="檢查哪一個 feature 之 DR／ANOMALIES（預設 power）")
    parser.add_argument("--gate", action="store_true", help="任一違規 exit 1")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    f = args.feature
    findings = check_ledger(root)
    for rel in (LEDGER, f"features/{f}/DATA_REQUESTS.md",
                f"features/{f}/ANOMALIES.md"):
        findings += check_malformed_rows(root, rel)
    series_files = [f"features/{f}/DATA_REQUESTS.md",
                    f"features/{f}/ANOMALIES.md"]
    for rel in series_files:
        findings += check_series(root, rel)

    # G-B 餘數對照 ＋ G-D 被抑制條數。**恆印**，PASS 與否都印 ——
    # 一個抓不到任何前綴的抽取器，其 PASS 與真的沒有跳號長得一樣。
    seen, newly, skipped = prefix_reconciliation(root, series_files)
    print(f"前綴（自 {f} 之 DR／ANOMALIES 主表抽取）：{seen or '（無）'}"
          f"　新受檢（硬寫清單外）：{newly or '（無）'}"
          f"　首格不合系列形態而略過：{skipped - prefix_reconciliation_off()}"
          f"　合系列形態但前綴不在主表而略過：{prefix_reconciliation_off()}")

    # R-POP16 丙（G-D）：抽得前綴集為空時**明示回報**，不得靜默 PASS。
    # 「沒有跳號」與「沒有東西受檢」在舊輸出裡是同一行字。
    blind = not seen
    if blind:
        print(f"no series detected —— {f} 之 DR／ANOMALIES 主表首格不是系列編號，"
              f"本輪跳號／重複兩檢**未涵蓋任何條目**（G-D 盲區；PASS ≠ 已驗）")

    reds = [x for x in findings if x.severity != "note"]
    notes = [x for x in findings if x.severity == "note"]
    if notes:
        print(f"note（不判紅，R-POP16 乙）：{len(notes)} 項")
        for x in notes:
            print(f"  [{x.check}] {x.where}：{x.detail}")

    if not reds:
        tail = "（**未涵蓋任何條目**，見上 no series detected）" if blind else ""
        print(f"docs_structure：PASS（台帳＋{f} 之 DR／ANOMALIES）{tail}")
        return 0
    print(f"docs_structure：{len(reds)} 項")
    for x in reds:
        print(f"  [{x.check}] {x.where}：{x.detail}")
    return 1 if args.gate else 0


if __name__ == "__main__":
    raise SystemExit(main())
