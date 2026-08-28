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


# 標題式登記：`## A-POP9 —— …` 與 `## [A-AM01] …` 兩式皆認（R-POP18）。
# audio_mgmt／driver_distraction／sxm 用方括號式，不認它就會把整本簿子
# 看成空的 —— A-POP11 之 sxm 兩筆假陽性即由此而來。
RE_HEAD_ID = re.compile(r"^#{2,4}\s+\[?((?:A|DR|R)-[A-Z]{1,6}-?\d+)\]?(?:\s|$|—|\|)")

# 登記表之門檻。**兩條任一成立即算**：
#   (1) 首欄有 ≥ 2 列合系列編號形態（R-POP18 之明文判準）
#   (2) 只有 1 列，但它佔該表首欄非空格之 ≥ 50%
# (2) 是為了接住**被空行切成單列的續段**（power 之 A-PW 主表即如此）——
# 只用 (1) 會把續段整段丟掉，等於用另一種方式重蹈 A-POP10。
# 兩條都擋得住 `privacy` 之 `| S10 | \`NA\`（Functional Safety）|`：
# 該表首欄 6 格中只有 `S10` 一格合形態（1/6 = 17%），兩條皆不過。
REGISTER_MIN_ROWS = 2
REGISTER_MIN_RATIO = 0.5

HEAD_TABLE = -1        # 標題式登記之虛擬表序（與任何真表格皆不同表）


def register_tables(all_tables: list) -> list[int]:
    """**內容判準**（R-POP18）：首欄有 ≥ 2 列合系列編號形態者即登記表。

    取代 R-POP16 乙之「檔內首個表格」—— 那條的理由「首個表格為三簿體例
    之不變量」經實測不成立（A-POP10）：sxm／audio_mgmt／projection／privacy
    之首個表格皆非登記表，而 power 之登記表又被空行切成多段。
    **位置不是不變量，內容才是。**

    一檔可有多張登記表（power 之切段情形），其編號由 `series_in` 合併為
    同一序列後再判跳號 —— 不合併就會把切段處判成跳號。
    """
    out = []
    for i, table in enumerate(all_tables):
        cells_ = [bare(row[0]) for row in table if bare(row[0])]
        hits = sum(1 for c in cells_ if RE_SERIES.match(c))
        if hits >= REGISTER_MIN_ROWS:
            out.append(i)
        elif hits and hits / len(cells_) >= REGISTER_MIN_RATIO:
            out.append(i)
    return out


def series_in(text: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    """`(前綴 → [(編號, 表序)], 被略過之首格數, 合系列形態但不在登記表者)`。

    收集之來源有二，**兩者皆收，但角色不同**：

    1. 登記表（`register_tables`）之首欄 —— 記其表序，參與重複判定與跳號
    2. 標題式登記（`## A-XXn`／`## [A-XXn]`）—— 表序記為 `HEAD_TABLE`，
       **只作存在性佐證，不參與重複判定**（見 `check_series`）

    「不參與重複判定」是必要的：popup 那種「主表一列 ＋ `## A-POPn`
    明細節一節」兩式併存，若一併算進重複，每一號都會變成跨表同號。
    而若反過來「有表格就不看標題」，則 sxm 那種「回顧表只列部分號、
    完整登記在標題」的檔會把未列於回顧表的號判成跳號 —— A-POP11 之
    `A-SX18`／`A-SX19` 兩筆假陽性正是此形。**兩式都要收，只是用途分開。**

    逐列掃描，不跳過表首 —— 長條目常被空行切成獨立表格，
    若跳過首列即會漏掉其編號並誤報跳號（本工具開發時實際踩到）。

    第二個回傳值為 **G-D 之被抑制條數**：首格非空但不合系列編號形態者。
    第三個為合系列形態卻不在任何登記表、亦無標題式可回退者 —— 同屬 G-D。
    """
    all_tables = tables(text)
    reg = set(register_tables(all_tables))

    found: dict[str, list[tuple[int, int]]] = {}
    skipped = 0
    stray: dict[str, int] = {}
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
            if ti not in reg:
                stray[pfx] = stray.get(pfx, 0) + 1
                continue
            found.setdefault(pfx, [])
            SEPARATORS.setdefault(pfx, cell[len(pfx):-len(m.group("num"))])
            found[pfx].append((int(m.group("num")), ti))

    for line in text.splitlines():
        h = RE_HEAD_ID.match(line)
        if h is None:
            continue
        m = RE_SERIES.match(bare(h.group(1)))
        if m is None:
            continue
        pfx = m.group("prefix")
        ident = bare(h.group(1))
        SEPARATORS.setdefault(pfx, ident[len(pfx):-len(m.group("num"))])
        found.setdefault(pfx, []).append((int(m.group("num")), HEAD_TABLE))
        stray.pop(pfx, None)

    return found, skipped, sum(n for p, n in stray.items() if p not in found)


def check_series(root: Path, rel: str, prefix: str | None = None) -> list[Finding]:
    """跳號檢查。`prefix=None`（預設）＝ 自登記表／標題式抽取之**每個**前綴都查。

    R-POP16 乙：`編號重複` 之判準改為**同一表格內**重複才判紅；
    同號分散於不同表格（主表一列、回顧表一列）降為 note。
    放寬只及於「跨表」這一項 —— 主表內真的寫了兩次，仍判紅。
    R-POP18 只換掉「哪些表算登記表」，本函式之兩段判準不變；
    另加一條：**標題式登記（`HEAD_TABLE`）不參與重複判定**，只計入跳號之
    存在性。理由見 `series_in` 之 docstring。
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
            # 標題式登記不參與重複判定：一號只在標題出現（tis 為空）或
            # 只在一張表格出現，皆非重複。
            tis = [t for t in where[num] if t != HEAD_TABLE]
            if len(tis) <= 1:
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
    print(f"前綴（自 {f} 之 DR／ANOMALIES 登記表／標題式抽取）：{seen or '（無）'}"
          f"　新受檢（硬寫清單外）：{newly or '（無）'}"
          f"　首格不合系列形態而略過：{skipped - prefix_reconciliation_off()}"
          f"　合系列形態但不在登記表而略過：{prefix_reconciliation_off()}")

    # R-POP16 丙（G-D）：抽得前綴集為空時**明示回報**，不得靜默 PASS。
    # 「沒有跳號」與「沒有東西受檢」在舊輸出裡是同一行字。
    blind = not seen
    if blind:
        print(f"no series detected —— {f} 之 DR／ANOMALIES 抽不到任何登記表或標題式登記，"
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
