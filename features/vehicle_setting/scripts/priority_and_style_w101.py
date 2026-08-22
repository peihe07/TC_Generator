"""W-101（58 包 §5）—— Priority 逐條重判 ＋ design_method 對齊 ＋ -038 退回。

(1) 依 **R-VS56** 逐條重判 76 條之 Priority，並於各 TC 之 `reasoning`
    記其所依類別（`P0(a)`／`P0(b)`／`P1`／`P2`）
(2) 依 57 包 §4 之一對一對照，`design_method` 對齊交付本之受控值域
    （`中文 (English)` 形態，9 值）
(3) `ThirdRowHeadrestDump-038` 依 57 包 §3.3 退回記錄形態並命名；
    其比較步驟無值可比，標 `PENDING: DR-26`
"""
from __future__ import annotations

import json
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

SRC = {
    "batch01": ("generated/batch01_v5.json", "generated/batch01_v6.json"),
    "batch02": ("generated/batch02_v3.json", "generated/batch02_v4.json"),
    "batch03": ("generated/batch03_v4.json", "generated/batch03_v5.json"),
    "batch04": ("generated/batch04_v5.json", "generated/batch04_v6.json"),
    "batch05": ("generated/batch05_v3.json", "generated/batch05_v4.json"),
    "batch06": ("generated/batch06_v3.json", "generated/batch06_v4.json"),
    "batch07": ("generated/batch07_v3.json", "generated/batch07_v4.json"),
    "batch08": ("generated/batch08_v4.json", "generated/batch08_v5.json"),
    "batch10": ("generated/batch10_v3.json", "generated/batch10_v4.json"),
    "batch11": ("generated/batch11_v3.json", "generated/batch11_v4.json"),
    "batch12": ("generated/batch12_v3.json", "generated/batch12_v4.json"),
}

# ── (2) 交付本之受控值域（`下拉選單` 分頁，9 值）───────────────────
CONTROLLED = {
    "Functional Based": "功能測試 (Functional based ; no specific technique)",
    "State Transition": "狀態轉換 (State Transition Testing)",
    "Decision Table": "決策表 (Decision Table Testing)",
    "Equivalence Partitioning": "等價劃分 (Equivalence Partitioning, EP)",
    "Negative / Invalid": "負向測試 (Negative / Invalid)",
}
CONTROLLED_DOMAIN = frozenset(CONTROLLED.values()) | {
    "邊界值分析 (Boundary Value Analysis, BVA)",
    "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
    "情境 / 用例 (Scenario / Use Case Testing)",
    "基礎故障注入 (Fault Injection Lite)",
}

# ── (1) R-VS56 之逐條判定 ──────────────────────────────────────────
# P0(a) 實體致動且具傷害可能 —— 限致動本身
P0A = {"SWE1-VC-ThirdRowHeadrestDump-025": "P0(a)：第三排頭枕之下放致動"}
# P0(b) 加熱元件之啟用 —— 限開啟；階數之顯示同步屬 P1；貫通座椅（vented）非熱源
P0B = {
    "SWE1-VC-HeatedSteeringWheel-015": "P0(b)：加熱方向盤之啟用",
    "SWE1-VC-HeatedSteeringWheel-021": "P0(b)：加熱方向盤之啟用",
    "SWE1-VC-HeatedSteeringWheelManagement-028": "P0(b)：加熱方向盤之按壓啟用",
    "SWE1-VC-TwoStagesHeatedSeat-057": "P0(b)：加熱座椅之按壓啟用",
    "SWE1-VC-ThreeStagesHeatedSeat-080": "P0(b)：加熱座椅之按壓啟用",
}
# P2 次要與診斷 —— 無效值之忽略、SNA 之處置、時序、前言型
P2 = {
    "SWE1-VC-LeftFrontHeatedSeat-008": "P2：無效值之忽略",
    "SWE1-VC-RightFrontHeatedSeat-026": "P2：無效值之忽略",
    "SWE1-VC-LeftFrontVentedSeat-006": "P2：無效值之忽略",
    "SWE1-VC-RightFrontVentedSeat-023": "P2：無效值之忽略",
    "SWE1-VC-HeatedSteeringWheel-006": "P2：未定義編碼之忽略",
    "SWE1-VC-Stop-StartSystem-007": "P2：SNA 之處置",
}
P1_DEFAULT = "P1：主要功能邏輯"


def priority_of(leaf: str) -> tuple[str, str]:
    if leaf in P0A:
        return "P0", P0A[leaf]
    if leaf in P0B:
        return "P0", P0B[leaf]
    if leaf in P2:
        return "P2", P2[leaf]
    return "P1", P1_DEFAULT


# ── (3) -038 之退回（57 包 §3.3）──────────────────────────────────
REVERT_038 = [
    ('Read the state of the virtual "Rear View Camera" button and check that it is not selectable',
     'Read the state of the virtual "Rear View Camera" button and record as RVC_button_ign_lk'),
    ('The virtual "Rear View Camera" button reads not selectable',
     "RVC_button_ign_lk is recorded"),
    ('and check that the virtual "Rear View Camera" button is selectable',
     'and check that the virtual "Rear View Camera" button is selectable and that its state relative to RVC_button_ign_lk is as specified'),
    ('The virtual "Rear View Camera" button is selectable',
     'The virtual "Rear View Camera" button is selectable; its state relative to RVC_button_ign_lk is PENDING: DR-26'),
]


def main() -> None:
    changes, dm_changes, before, after = [], 0, {}, {}
    for src, dst in SRC.values():
        d = json.loads((FEAT / src).read_text(encoding="utf-8"))
        for tc in d["tcs"]:
            leaf = tc["leaf_id"]
            old_p = tc["priority"]
            before[old_p] = before.get(old_p, 0) + 1
            new_p, why = priority_of(leaf)
            after[new_p] = after.get(new_p, 0) + 1
            if new_p != old_p:
                changes.append((leaf, old_p, new_p, why))
            tc["priority"] = new_p
            tc["reasoning"] = why

            dm = tc["design_method"]
            if dm in CONTROLLED:
                tc["design_method"] = CONTROLLED[dm]
                dm_changes += 1

            if leaf == "SWE1-VC-ThirdRowHeadrestDump-038":
                for old, new in REVERT_038:
                    hits = sum(tc[f].count(old) for f in ("test_procedure", "expected_result"))
                    if hits != 1:
                        raise SystemExit(f"-038 退回：命中 {hits} 次 —— {old!r}")
                    for f in ("test_procedure", "expected_result"):
                        if old in tc[f]:
                            tc[f] = tc[f].replace(old, new)
        d["revision"] = "W-101（36 輪）：Priority 依 R-VS56 重判；design_method 對齊受控值域"
        d["design_method_domain"] = "SWC 0708 交付本之 `下拉選單` 分頁，9 值"
        (FEAT / dst).write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                                encoding="utf-8")

    print(f"Priority 重判前：{before}")
    print(f"Priority 重判後：{after}")
    print(f"變動 {len(changes)} 條：")
    for leaf, a, b, why in changes:
        print(f"   {leaf:46s} {a} → {b}   {why}")
    print(f"\ndesign_method 對齊 {dm_changes} 條")


if __name__ == "__main__":
    main()
