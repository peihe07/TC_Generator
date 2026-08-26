#!/usr/bin/env python3
"""T52 —— A-VC14 之同型矛盾全表掃描（下放包 09 §六）。

A-VC14 之形態：`Requirement Title` 與 `Requirement Description` 對同一
可測量之門檻給出不同的值 —— `VC-033-01` 之 Title「After three sequential
wrong PINs」（第 3 次觸發）vs Description「more than three times」（第 4 次）。
**數字相同，門檻差一** —— 差在比較器，不在數字。

母體：**117 leaf**（母體標註依 R-VC15）。

方法：自二欄各抽出 (類別, 值, 比較器)，同類別而 (值, 比較器) 不同者列為
候選，逐筆人工判讀。比較器必須一併比對 —— 只比數字會漏掉本案。

⚠ **初版曾漏抓 A-VC14 本身**。初版把 `count`（times/attempts）與
`quantity`（裸數字）分為二類：Title 之「three sequential wrong PINs」
判為 quantity、Desc 之「three times」判為 count，類別不同即不進比對 ——
**掃描器漏掉了它被造出來要抓的那一筆**。二類已合併為 `count`：
「三次」與「三個」在門檻語意上是同一個量，分類本不該把它們拆開。
此事記於上繳包 10 §3.2。

只讀不寫。偽陰性見上繳包 10 §3.4。
"""
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

WORD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}

CMP = re.compile(r"\b(more than|at least|no more than|up to|after|before|"
                 r"longer than|greater than|less than|below|above|within|"
                 r"exactly|only|maximum|minimum|no upper limit|unlimited)\b",
                 re.I)

# count 與 quantity 已合併（見檔頭）。僅 digits／time 另立類別。
UNIT = [
    ("digits", re.compile(r"\b(digits?)\b", re.I)),
    ("time",   re.compile(r"\b(minutes?|mins?|seconds?|secs?|ms|hours?)\b|'",
                          re.I)),
]
NUM = re.compile(r"\b(\d+)\b|\b(" + "|".join(WORD) + r")\b", re.I)


def extract(text: str):
    """回傳 {(類別, 值, 修飾該值之比較器)}。"""
    out = set()
    for m in NUM.finditer(text):
        raw = m.group(0)
        val = int(raw) if raw.isdigit() else WORD[raw.lower()]
        tail = text[m.end():m.end() + 40]
        kind = "count"
        for k, pat in UNIT:
            if pat.search(tail):
                kind = k
                break
        head = text[max(0, m.start() - 40):m.start()]
        c = CMP.findall(head)
        out.add((kind, val, c[-1].lower() if c else ""))
    return out


def load_leaves():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    raw = list(wb["Analysis Report"].iter_rows(values_only=True))
    rows = [r for r in raw[7:] if r[0] not in (None, "")]
    P = re.compile(r"^SWE1-HMI-VC-(\d{3})$")
    C = re.compile(r"^SWE1-HMI-VC-(\d{3})-(\d{2})$")
    ids = [str(r[0]).strip() for r in rows]
    pc = {C.match(i).group(1) for i in ids if C.match(i)}
    return [r for r in rows
            if C.match(str(r[0]).strip())
            or (P.match(str(r[0]).strip())
                and P.match(str(r[0]).strip()).group(1) not in pc)]


def main():
    leaves = load_leaves()
    with_num, flagged = 0, []
    for r in leaves:
        rid, title, desc = str(r[0]).strip(), str(r[3]).strip(), str(r[4]).strip()
        t, d = extract(title), extract(desc)
        if not t and not d:
            continue
        with_num += 1
        for k in {x[0] for x in t} | {x[0] for x in d}:
            tv = {(v, c) for kk, v, c in t if kk == k}
            dv = {(v, c) for kk, v, c in d if kk == k}
            if not tv or not dv:
                continue          # 僅一欄載該類別 —— 屬 A-VC10 之形態，非本項
            if tv != dv:
                flagged.append((rid, k, sorted(tv), sorted(dv), title, desc))

    print(f"母體: {len(leaves)} leaf（117 leaf 母體）")
    print(f"二欄至少一方含數值者: {with_num}")
    print(f"同類別而 (值, 比較器) 不一致者: {len(flagged)}\n")
    for rid, k, tv, dv, title, desc in flagged:
        print(f"=== {rid}  類別={k}")
        print(f"    Title 抽出 {tv}")
        print(f"    Desc  抽出 {dv}")
        print(f"    Title: {title[:130]}")
        print(f"    Desc : {desc[:130]}\n")
    return flagged


if __name__ == "__main__":
    main()
    sys.exit(0)
