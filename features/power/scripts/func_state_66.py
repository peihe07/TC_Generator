"""R-P387(b) —— `FUNC_STATE_<STATE>` 標準片段（66 包 §H 第 3 步之一）。

A1 家族（`<X> functionality is (not) available`）之代理量**不必另造**：
`CFTS009-4941453` 為規格自帶之狀態表，每一態逐欄給
Source / Audio Power amplifier / Display / BoosterOUT / Antenna / MCU 之 ON-OFF。

本腳本自文字層**逐字**解析該表（13 列 × 9 欄），為每態產出一組 ER 子項，
另加 `PowerSts_Telematic` 該態值 (i) 與 OFF 態之觸控無反應 (ii)。

白名單對應（R-P353 ＋ R-P387(a) 之 (v)）：
    Source / AMP        → (iii) 音訊有無
    Display             → (ii)  畫面有無／內容
    BoosterOUT / Antenna→ (v)   腳位電壓（位準值須規格載明，查無者 PENDING）
    MCU (USB) / (AUX)   → (iii) 列舉／播放

用法：
    python features/power/scripts/func_state_66.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEXT = ROOT / "features/power/data/textlayer/cfts009_plain.txt"
OUT = ROOT / "features/power/data/func_state_66.md"

# `VAL_ 1470 PowerSts_Telematic`（forms BHCAN2）
RAW = {"Full-Operation": (4, "Full_Operation"), "Idle": (3, "Idle"),
       "Partial Operation": (7, "Partial_Operation"), "Timed": (2, "Timed"),
       "Standby": (1, "Standby"), "Sleep": (0, "Sleep"), "Bench": (6, "Bench"),
       "Logistic Idle": (5, "Logistic_On"), "Logistic Standby": (5, "Logistic_On"),
       "Logistic Sleep": (5, "Logistic_On")}

COLS = ["Source", "Audio Power amplifier", "Display / Illumination",
        "BoosterOUT", "Antenna / Analog tuner", "Antenna / Digital tuner",
        "MCU (USB)", "MCU (AUX)"]

# `4941453` 之星號註腳，其定義在**相鄰之獨立錨點**（非同段），逐字引：
#   4941454 / 4941455 → `(*)`；4941457 → `(**)`；4941459 → `(***)`
# 註腳改變 ER —— 例如 Idle 之 Display 為 `OFF (*)`，而 `(*)` 明載
# Splash Screen 仍顯示，故不得寫成「畫面全暗且不回應觸控」。
FOOTNOTE = {
    "(*)": ("CFTS009-4941454 / CFTS009-4941455",
            'with exception of: Front_Panel_OnOff.Req icon (i.e. TLM Power button); '
            'Splash Screen visualization; HMI Antitheft Screens'),
    "(**)": ("CFTS009-4941457",
             "with exception of HMI Antitheft Screens"),
    "(***)": ("CFTS009-4941459",
              "with exception of Advanced Driving Assistance System requests"),
}


def marks(val: str) -> list[str]:
    """該格所帶之星號註腳，長者優先（`(***)` 先於 `(*)`）。"""
    return [m for m in ("(***)", "(**)", "(*)") if m in val.replace(" ", "")]


def er_line(col: str, val: str) -> str:
    on = val.upper().startswith("ON")
    v = val.split("Refer")[0].split("DCSD")[0].strip()
    if col == "Source":
        return ("(iii) The audio active source is playing on the HU speakers" if not
                val.upper().startswith("OFF") else
                "(iii) No audio source is playing on the HU speakers")
    if col == "Audio Power amplifier":
        if "Muted" in val:
            out = "(iii) The amplifier is on and the audio output is muted"
            for mk in marks(val):
                src, txt = FOOTNOTE[mk]
                out += f"，**惟 `{mk}`（{src}）例外**：{txt}"
            return out
        return ("(iii) The amplifier output is present on the HU speakers" if on
                else "(iii) No amplifier output is present on the HU speakers")
    if col == "Display / Illumination":
        if on:
            return "(ii) The HU display is on"
        base = "(ii) The HU display is off"
        for mk in marks(val):
            src, txt = FOOTNOTE[mk]
            base += (f"，**惟 `{mk}`（{src}）例外**：{txt} —— "
                     f"該例外項須逐一驗其仍可顯示")
        return base
    if col in ("BoosterOUT", "Antenna / Analog tuner", "Antenna / Digital tuner"):
        name = {"BoosterOUT": "BoosterOUT",
                "Antenna / Analog tuner": "analog tuner antenna supply",
                "Antenna / Digital tuner": "digital tuner antenna supply"}[col]
        lvl = "ON" if on else "OFF"
        return (f"(v) Measure the voltage at the {name} output and check that it is "
                f"the {lvl} level  —— PENDING: DR-PW27 {name} 位準值"
                f"（CFTS024 / VF654 在台帳外）")
    if col == "MCU (USB)":
        return ("(iii) A USB device inserted on the bench is enumerated and can be played"
                if on else "(iii) A USB device inserted on the bench is not enumerated")
    return ("(iii) The AUX input plays on the HU speakers" if on
            else "(iii) The AUX input does not play on the HU speakers")


def main() -> None:
    t = TEXT.read_text().splitlines()
    i = next(k for k, l in enumerate(t) if l.startswith("4941453:"))
    end = next((k for k in range(i + 1, len(t)) if re.match(r"^49\d+:", t[k])),
               i + 130)
    body = [l.strip() for l in t[i + 1:end]]
    rows = body[9:]

    seen, out = set(), []
    md = [
        "# `FUNC_STATE_<STATE>` 標準片段（66 包 / R-P387(b)）",
        "",
        "> 來源：**`CFTS009-4941453`** —— 規格自帶之狀態表，逐字解析（13 列 × 9 欄）。",
        "> A1 家族（`<X> functionality is (not) available`）之代理量**直接取該表該態之列**，",
        "> 不另造（R-P387(b)）。`PowerSts_Telematic` 之 raw 值取 `VAL_ 1470`（forms BHCAN2）。",
        "",
        "> ⚠ **BoosterOUT／天線供電為 (v) 類電氣量測**（R-P387(a)）。",
        "> 其 **ON/OFF 位準值規格未載**（`4941453` 之該欄逐字為",
        "> `ON Refer to {CFTS024} …` / `ON Refer to {VF654} …`），二文件在 G0 台帳外，",
        "> 故該子項一律 **`PENDING: DR-PW27`**，**不得自造位準**（R-P387(a) / §I）。",
        "",
        "> ⚠ **星號註腳之定義不在 `4941453` 段內**，而在相鄰之獨立錨點",
        "> （`4941454` / `4941455` = `(*)`；`4941457` = `(**)`；`4941459` = `(***)`）。",
        "> **註腳改變 ER** —— 例如 `Idle` 之 Display 為 `OFF (*)`，而 `(*)` 明載",
        "> Splash Screen 仍顯示，故**不得寫成「畫面全暗」**。已逐格併入。",
        "",
        "> ⚠ **`4941453` 有二列 `Full-Operation` 與二列 `Timed`**（音源清單不同：",
        "> 後者多 `SDCARD, BT Music streaming or Phone Call`）—— 本表取其**聯集**，",
        "> 差異記於各該節，**不擇一**（§8.4.1）。",
        "",
    ]
    dupes = []
    for j in range(0, len(rows) - 8, 9):
        blk = rows[j:j + 9]
        state = blk[0]
        if state in seen:
            dupes.append(state)
            continue
        seen.add(state)
        const = "FUNC_STATE_" + re.sub(r"[^A-Za-z]+", "_", state).upper().strip("_")
        md += [f"## `{const}`　（`4941453` 之 `{state}` 列）", ""]
        if state in RAW:
            raw, label = RAW[state]
            md += [f"- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ "
                   f"and check that it is {raw} ({label})`", ""]
        else:
            md += [f"- **態確認**：`{state}` 不在 `VAL_ 1470` 之列舉內 → "
                   f"**PENDING: DR-PW26**（同 `ENTER_INIT`，R-P363(c)）", ""]
        md += ["| 欄（`4941453`）| 原值逐字 | ER 子項 |", "|---|---|---|"]
        for c, v in zip(COLS, blk[1:9]):
            md.append(f"| {c} | `{v[:60]}` | {er_line(c, v)} |")
        md.append("")
        out.append(const)

    md += ["## 重複列", "",
           f"`4941453` 中重複出現之態：{'、'.join(dupes) if dupes else '無'}。",
           "二列之差在 `Source` 欄之音源清單（後者多 `SDCARD, BT Music streaming or Phone Call`），",
           "其餘八欄逐字相同。本表取聯集，**差異不擇一**。", "",
           f"## 產出 {len(out)} 個片段", "",
           "、".join(f"`{c}`" for c in out), ""]
    OUT.write_text("\n".join(md))
    print(f"{len(out)} 個 FUNC_STATE 片段（重複列 {dupes}）→ {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
