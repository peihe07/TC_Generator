#!/usr/bin/env python3
"""M17-PM（canon §5.1）：禁用動詞 20 列改寫。

下放包 05 §一之規則為「`to check whether` → `to check that`，並**依該列
ER 之實際極性**調整述語，不得機械替換」，且明訂「改寫須以 ER 為準」。

該包附表宣稱「全 18 列皆為肯定式，無否定分支」——**實測不成立**：
rows 86、178、205、238、242、292 之 ER 為否定式或「skipped／bypassed」，
附表給定之述語與其 ER 相反。本模組依規則（ER 為準）取值，
與附表相異者於 `TABLE_DIVERGENCE` 逐列具名，供分析層覆核。

每列僅改動含禁用動詞之該一行，其餘行、ER 欄、test_item 欄不動。
"""

from __future__ import annotations

# row -> (原行, 新行)。原行逐字比對，不符即中止，避免改錯行。
REPLACEMENTS: dict[int, tuple[str, str]] = {
    # ── 型 A：`to check whether` → `to check that`（18 列）──
    15: ("2. Read the TLM display to check whether the images are provided",
         "2. Read the TLM display to check that the images are provided"),
    86: ("2. Read TLM_Status.Info to check whether the transition of this clause occurs",
         "2. Read TLM_Status.Info to check that the transition of this clause "
         "does not occur"),
    128: ("2. Read the display backlight to check whether it stays off",
          "2. Read the display backlight to check that the backlight is off"),
    178: ("2. Read the HU mode and the screen to check whether the disclaimer appears",
          "2. Read the HU mode and the screen to check that the disclaimer screen "
          "is bypassed"),
    205: ("2. Read the HU behavior to check whether a reset occurs",
          "2. Read the HU behavior to check that no reset occurs"),
    238: ("2. Read the screen to check whether an animation is played",
          "2. Read the screen to check that the start-up animation is skipped"),
    242: ("2. Read the screen to check whether an animation is played",
          "2. Read the screen to check that the start-up animation is skipped"),
    292: ("2. Read the HU mode and the screen to check whether the disclaimer appears",
          "2. Read the HU mode and the screen to check that the disclaimer screen "
          "is bypassed"),
    # ── 型 B：`Observe` 作主動詞（2 列）──
    210: ("1. Observe the bus traffic while the CAN network stays awake",
          "1. Read the bus traffic while the CAN network stays awake and record "
          "the $Radio_Theme$ message"),
    225: ("1. Observe the bus traffic while the CAN network stays awake",
          "1. Read the bus traffic while the CAN network stays awake and record "
          "the $Radio_Theme$ message"),
}

# 兩組同文列，逐字相同，照附表給定值（該二組附表與 ER 相符）
for _row in (255, 256, 257):
    REPLACEMENTS[_row] = (
        "2. Read the audio output to check whether a new day is granted",
        "2. Read the audio output to check that a startup sound accompanies "
        "the animation")
for _row in range(275, 282):
    REPLACEMENTS[_row] = (
        "2. Read the screen to check whether the startup screens appear",
        "2. Read the screen to check that the disclaimer and splash screen "
        "are skipped")

# 與下放包附表相異之列：附表值 vs 本包依 ER 取值
TABLE_DIVERGENCE: dict[int, tuple[str, str, str]] = {
    86: ("…that the transition occurs",
         "…that the transition of this clause does not occur",
         'ER：TLM_Status.Info **does not** pass to "Standby" …'),
    178: ("…that the disclaimer appears",
          "…that the disclaimer screen is bypassed",
          "ER：The disclaimer screen is **bypassed**"),
    292: ("…that the disclaimer appears",
          "…that the disclaimer screen is bypassed",
          "ER：The disclaimer screen is **bypassed**"),
    205: ("…that a reset occurs",
          "…that no reset occurs",
          "ER：The HU **does not** reset due to a power button reset"),
    238: ("…that the animation is played",
          "…that the start-up animation is skipped",
          "ER：The HU **skips** the start-up animation"),
    242: ("…that the animation is played",
          "…that the start-up animation is skipped",
          "ER：The HU **skips** the start-up animation"),
}


def rewrite_proc(proc: str, row: int) -> str:
    """替換該列 proc 中之目標行；原行須逐字命中且唯一。"""
    old, new = REPLACEMENTS[row]
    lines = proc.split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.strip() == old]
    if len(hits) != 1:
        raise ValueError(f"row {row}：目標行命中 {len(hits)} 次，預期 1 次")
    lines[hits[0]] = lines[hits[0]].replace(old, new)
    return "\n".join(lines)
