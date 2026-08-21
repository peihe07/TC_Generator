"""LID 表儲存格之解析（W-23(a)，C3 缺陷之修正）。

## 為何要有這個模組

`Logical Identifiers and CAN Mapping` 之 `Signal Name`／`CAN`／`Format`
三欄，**同一儲存格得載多個訊號**：以換行或空白分隔之 `MESSAGE.Signal` 對，
`CAN` 欄同序列出其網段（`CAN-B` / `FD` / `CAN-FD` / `BH-CAN`）。

**只取第一個即為 C3 缺陷。** 其已三度現身而每次面貌不同：

  W-8      值域切分 —— `Format` 以逗號切，而該欄無逗號分隔
  W-15b′   交叉配   —— 取第一個 message 名對每一個 DBC 出現處
  A-VS26   message 歸屬 —— `ESS_ENG_ST` 之單格載兩個 message 兩個網段

三次都被當成「這一次的錯」修掉，未修解析器本身；本模組為其修正。

用法：
    from lid_parse import parse_signal_cell, parse_format_cell, unescape_cell
    python features/vehicle_setting/scripts/lid_parse.py --self-test
"""

from __future__ import annotations

import re
import sys

# `MESSAGE.Signal` 對；message 得省略（裸 signal 名）
PAIR = re.compile(r"([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)")
BARE = re.compile(r"(?<![\w.])([A-Za-z0-9_]{3,})(?![\w.])")
# `Format` 之鍵值：以**下一個鍵 =** 為邊界，非以逗號（該欄無逗號分隔）
KV = re.compile(r"(-?[0-9A-Fa-f#]+)\s*[=:]\s*(.*?)(?=\s+-?[0-9A-Fa-f#]+\s*[=:]|$)", re.S)

STOP = {"bit", "signal", "the", "and", "for", "hex", "not", "used",
        "present", "absent", "see", "proxi", "table"}


def unescape_cell(value: str) -> str:
    """還原 `data/lid_pairs.tsv` 之逸出（R-VS26(1)）。

    寫出端以 `\\n` 保留來源之換行、`\\\\` 保留反斜線。
    **直接讀該 TSV 而不還原者，會看到字面 `\\n` 而非換行**，
    多訊號之切分因而失效 —— 05 輪 §6.2-3 具名之缺口，本函式為其公開介面。
    """
    return value.replace("\\n", "\n").replace("\\\\", "\\")


def _split_cell(cell: str) -> list[str]:
    """儲存格切為條目 —— 換行優先；無換行者以連續二空白切。"""
    if not cell:
        return []
    parts = [x.strip() for x in str(cell).split("\n") if x.strip()]
    if len(parts) == 1:
        parts = [x.strip() for x in re.split(r"\s{2,}", parts[0]) if x.strip()]
    return parts


def parse_signal_cell(signal_cell: str, can_cell: str = "") -> list[dict]:
    """回傳 [{message, signal, can}, …] —— **逐對展開，不只取第一個**。

    `can_cell` 與 `signal_cell` 同序對應；長度不等時以位置對齊，
    不足者留空（**不猜、不循環補**）。
    """
    sig_items = _split_cell(signal_cell)
    can_items = _split_cell(can_cell)
    out: list[dict] = []
    for i, item in enumerate(sig_items):
        can = can_items[i] if i < len(can_items) else ""
        found = False
        for m in PAIR.finditer(item):
            out.append({"message": m.group(1), "signal": m.group(2), "can": can})
            found = True
        if not found:
            for m in BARE.finditer(item):
                if m.group(1).lower() in STOP:
                    continue
                out.append({"message": None, "signal": m.group(1), "can": can})
    return out


def parse_format_cell(fmt_cell: str) -> list[tuple[str, str]]:
    """回傳 [(鍵, 值), …]。多訊號之 `Format` 亦逐條切後再解。"""
    out: list[tuple[str, str]] = []
    for item in _split_cell(fmt_cell) or []:
        out += [(k, v.strip()) for k, v in KV.findall(item)]
    return out


# ── 驗證錨點（下放包 W-23(a) 指定）────────────────────────────
ANCHORS = [
    ("ESS_ENG_ST 須解出兩對",
     "STATUS_CCAN3.ESS_ENG_ST\nENGINE_FD_2.ESS_ENG_ST", "CAN-B\nFD",
     [("STATUS_CCAN3", "ESS_ENG_ST", "CAN-B"), ("ENGINE_FD_2", "ESS_ENG_ST", "FD")]),
    ("HSW_Stat 須解出兩支",
     "STATUS_CSWM.HSW_STATSts\nSTATUS_CSWM.HSW_STATFailSts", "CAN-B\nCAN-B",
     [("STATUS_CSWM", "HSW_STATSts", "CAN-B"), ("STATUS_CSWM", "HSW_STATFailSts", "CAN-B")]),
]
# 反向：`Format` 之已知全集（W-8 已驗過五例，此處保留為回歸）
FMT_ANCHORS = [
    ("0 = Not Pressed 1 = Pressed", [("0", "Not Pressed"), ("1", "Pressed")]),
    ("0 = 1 Level 1 = 2 Levels 2 = 3 Levels # = Not Used",
     [("0", "1 Level"), ("1", "2 Levels"), ("2", "3 Levels"), ("#", "Not Used")]),
]


def self_test() -> int:
    bad = 0
    for name, sig, can, want in ANCHORS:
        got = [(d["message"], d["signal"], d["can"]) for d in parse_signal_cell(sig, can)]
        ok = got == want
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} {name}")
        if not ok:
            print(f"    期望 {want}\n    實得 {got}")
    for fmt, want in FMT_ANCHORS:
        got = parse_format_cell(fmt)
        ok = got == want
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} Format 回歸：{fmt[:34]}…")
        if not ok:
            print(f"    期望 {want}\n    實得 {got}")
    print(f"\n自驗：{len(ANCHORS) + len(FMT_ANCHORS) - bad} / {len(ANCHORS) + len(FMT_ANCHORS)}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(self_test() if "--self-test" in sys.argv else 0)
