"""G172 —— `priority` 重判謂詞之 fixture（R-P245）。

34 §九第 4 項：G164 之 v2 謂詞未經 fixture 驗證；其 v1 之缺陷係由
Branding 之 34 / 34 異常比率**反推**而得，非由 fixture 攔下。
依 R-P214，自設、自實作、自回報之判準其首次適用不足以證其正確。

**fixture 全部為本檔自撰之虛構 TC，不取自 `features/power/generated/`**
（R-P245 / §I）—— 以既有 TC 為對照即以待驗對象驗判準。
虛構 TC 之題材取自一般車機領域，刻意**不使用**本語料之訊號名與措詞。

十案：§10.2 七類正例各一 ＋ 三個應判 P3 之負例。
另加**三個對抗案**，針對 v1 之已知缺陷（bench 樣板句、英文字 “can”）——
若 v2 仍誤判，該三案會失敗。

用法：
    python features/power/scripts/fixture_priority.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_priority import classify  # noqa: E402

BENCH = "1. The rig is powered\n2. A CAN simulation tool is connected to the network"


def tc(title: str, er: str, pre: str = BENCH, proc: str = "1. Run the step",
       data: str = "NA") -> dict:
    return {"tc_title": title, "test_item": title, "pre_conditions": pre,
            "input_test_data": data, "test_procedure": proc, "expected_result": er}


# （類別, 期望命中之 §10.2 類別 或 None, fixture）
CASES: list[tuple[str, str | None, dict]] = [
    # ── 七類正例 ──
    ("正例 safety", "safety（安全）",
     tc("Collision detected disables the touch input",
        "1. The unit registers the crash flag\n2. Touch input is disabled")),
    ("正例 boot / recovery", "boot / recovery（開機與復原）",
     tc("Unit reboots after a watchdog reset",
        "1. The unit reboots\n2. The home screen is restored")),
    ("正例 connection", "connection（連線）",
     tc("Bluetooth handset reconnects after ignition cycle",
        "1. The paired handset is listed\n2. The Bluetooth link is re-established")),
    ("正例 audio output", "audio output（音訊輸出）",
     tc("Navigation prompt ducks the media volume",
        "1. The media volume is reduced\n2. The prompt is audible on the speaker")),
    ("正例 eCall", "eCall",
     tc("eCall button places an emergency call",
        "1. The emergency call is placed\n2. The SOS indicator is lit")),
    ("正例 vehicle-critical CAN signal", "vehicle-critical CAN signal（車輛關鍵 CAN 訊號）",
     tc("Critical battery status is honoured",
        "1. The unit registers the value\n2. The current draw is reduced",
        data="STATUS_LIN.Batt_ST_Crit = [1h]")),
    ("正例 data-loss risk", "data-loss risk（資料遺失風險）",
     tc("Trip log survives an unexpected power cut",
        "1. The trip log is written to NVM\n2. The entries are not lost after the cut")),
    # ── 三個應判 P3 之負例 ──
    ("負例 外觀", None,
     tc("Marque logo is centred on the welcome screen",
        "1. The logo is centred\n2. The colour matches the brand palette")),
    ("負例 客製化", None,
     tc("User selects an alternative icon pack",
        "1. The chosen icon pack is applied\n2. The wallpaper is unchanged")),
    ("負例 罕用情境", None,
     tc("Seasonal greeting animation plays on the first day of Spring",
        "1. The seasonal animation plays\n2. The normal animation resumes the next day")),
    # ── 三個對抗案：針對 v1 之已知缺陷 ──
    ("對抗 bench 樣板句不得使 connection 命中", None,
     tc("Font weight follows the theme setting",
        "1. The chosen font weight is applied\n2. No other typography changes")),
    ("對抗 英文字 “can” 不得使 CAN 命中", None,
     tc("The user can change the wallpaper at any time",
        "1. The wallpaper can be changed\n2. The change is kept after a restart")),
    ("對抗 `audio and video` 之 audio 為偶然共現", "audio output（音訊輸出）",
     tc("Camera feed is shown with its audio channel",
        "1. The camera provides audio and video\n2. The feed is shown")),
]


def main() -> None:
    failures = 0
    print("G172 —— `priority` 謂詞 fixture（**未取自本語料**，全部自撰）\n")
    for label, want, fx in CASES:
        hits, cosmetic = classify(fx)
        names = [n for n, _ in hits]
        ok = (want in names) if want else (not names)
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] {label}")
        print(f"          期望 {want or '無 P0 類別命中'}；"
              f"實測 {names or '（無）'}；裝飾性={cosmetic}")
    print(f"\n  G172 十三案全數如期：{'是' if not failures else '否'}"
          f"（{len(CASES) - failures} / {len(CASES)}）")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
