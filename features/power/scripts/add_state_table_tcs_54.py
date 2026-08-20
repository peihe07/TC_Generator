"""B2 —— `4941453` 可行三項補測（R-P349(b)）。

53 包查得：`Logistic Idle` / `Logistic Standby` / `Logistic Sleep`
之定義錨點全屬 `SWE-PM-008`，該 leaf 受 **DR-PW11（High, live）** 阻斷
—— 該三項登記為受阻，入驗證邊界，**不於本包產出**（§I）。

**可行三項於本包補測**：
  (1) `Bench` 之輸出組合            → `SWE-PM-007`
  (2) `Full-Operation` 二列之 `Source` 分辨 → `SWE-PM-001`
  (3) `Timed` 二列之 `Source` 分辨          → `SWE-PM-004`

表之二列差異僅在 `Source` 是否含 `SDCARD` / `BT Music streaming` / `Phone Call`
—— 依 §8.3（mode 為拆分軸）各補一條。

`test_item` 首段依 **R-P344** 取該狀態列在攤平串流中之**連續片段**，
照原分隔逐字取，**不加 `=`、不加 `,`、不重排欄序**；
起訖字元位置記入 `reasoning_note`（R-P343(c)）。

`tc_id` 自 **281** 起附加 —— **既有 280 條之號碼不變**，
故本次補測不使舊號位移（與 R-P322 之 100% 位移不同性質）。

用法：
    python features/power/scripts/add_state_table_tcs_54.py --dry-run
    python features/power/scripts/add_state_table_tcs_54.py --apply
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCH7 = ROOT / "features/power/generated/batch_007_power_state_c.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402

SPEC = ("R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_"
        "Wake-up and Power-up_SR26_20250909-1658_")

# (列索引, leaf, 章節, split_index, 標題, 前提, 步驟, ER, 軸, 拆分理由)
NEW = [
    (8, "SWE-PM-007", "1.6.2.1.8", 2,
     "Bench powers the amplifier, booster, antennas and MCU on",
     "1. A LIN and CAN simulation tool is connected\n"
     "The ignition working condition is Ignition Off\n"
     "The Engineering Line is activated\n"
     "TLM_Status.Info reads \"Bench\"",
     "1. Read the audio power amplifier and the BoosterOUT states\n"
     "2. Read the analog and digital antenna supplies\n"
     "3. Read the USB and AUX MCU states to check that both are on",
     "1. The audio power amplifier is ON and not muted, and the BoosterOUT is ON\n"
     "2. The analog and digital antenna supplies are ON\n"
     "3. The USB and AUX MCU are ON when present",
     {"axis": "output_set",
      "delta": "本條驗 Bench 列之八個輸出取值；`-277` 驗其 prose 錨點之 TLM/AMP/ICS/DTV 為 ON"},
     "本條驗狀態表 Bench 列之輸出組合（R-P340(b)）—— `-277` 未涵蓋該八欄"),

    (1, "SWE-PM-001", "1.6.2.1.1", 3,
     "Full-Operation plays SDCARD, BT streaming and call audio as the source",
     "1. A LIN and CAN simulation tool is connected\n"
     "TLM_Status.Info and $Telematic_Power$ read \"Full-Operation\"\n"
     "An SDCARD, a paired BT audio device and an active phone call are available",
     "1. Select SDCARD as the audio active source and read the played source\n"
     "2. Select BT Music streaming as the audio active source and read the played source\n"
     "3. Place a phone call and read the played source to check the call audio",
     "1. The TLM plays the SDCARD as the audio active source\n"
     "2. The TLM plays the BT Music streaming as the audio active source\n"
     "3. The TLM plays the phone call as the audio active source",
     {"axis": "input_data",
      "delta": "本條驗 Source 含 SDCARD / BT Music streaming / Phone Call 之列；"
               "`-261` / `-262` 驗 Tuner / USB / AUX_IN 之列"},
     "狀態表之 Full-Operation 有二列，差異在 Source 是否含 SDCARD / BT / Phone Call，"
     "依 §8.3 各一條（R-P340(b)）"),

    (5, "SWE-PM-004", "1.6.2.1.5", 3,
     "Timed plays SDCARD, BT streaming and call audio as the source",
     "1. A LIN and CAN simulation tool is connected\n"
     "TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n"
     "An SDCARD, a paired BT audio device and an active phone call are available",
     "1. Select SDCARD as the audio active source and read the played source\n"
     "2. Select BT Music streaming as the audio active source and read the played source\n"
     "3. Place a phone call and read the played source to check the call audio",
     "1. The TLM plays the SDCARD as the audio active source\n"
     "2. The TLM plays the BT Music streaming as the audio active source\n"
     "3. The TLM plays the phone call as the audio active source",
     {"axis": "input_data",
      "delta": "本條驗 Source 含 SDCARD / BT Music streaming / Phone Call 之列；"
               "`-271` / `-272` 驗 Tuner / USB / AUX_IN 之列"},
     "狀態表之 Timed 有二列，差異在 Source 是否含 SDCARD / BT / Phone Call，"
     "依 §8.3 各一條（R-P340(b)）"),
]


def row_fragment(idx: int) -> tuple[str, int, int]:
    """第 idx 列（9 欄）在 `4941453` 攤平串流中之連續片段與其起訖字元位置。"""
    paras = anchor_bodies()["4941453"]
    offs, pos = [], 0
    for p in paras:
        offs.append(pos)
        pos += len(p) + 1
    start = 9 + idx * 9                      # 前 9 段為表頭
    frag = "\n".join(paras[start:start + 9])
    lo = offs[start]
    return frag, lo, lo + len(frag)


def second_segment(proc: str, er: str) -> str:
    import re
    act = re.sub(r"^\s*\d+\.\s*", "", proc.split("\n")[-1]).strip()
    act = re.sub(r"\s+to check\b.*$", "", act, flags=re.I).strip().rstrip(".")
    exp = re.sub(r"^\s*\d+\.\s*", "", er.split("\n")[-1]).strip().rstrip(".")
    act = " ".join(act.split())
    if act[:1].isupper() and act.split(" ", 1)[0].isalpha() \
            and not act.split(" ", 1)[0].isupper():
        act = act[0].lower() + act[1:]
    return f"({act} -> {' '.join(exp.split())})"


def main() -> int:
    apply = "--apply" in sys.argv
    d = json.loads(BATCH7.read_text(encoding="utf-8"))
    nxt = max(int(t["tc_id"].rsplit("-", 1)[1]) for t in d["tcs"]) + 1
    added = []
    for idx, leaf, sec, sidx, title, pre, proc, er, axis, sr in NEW:
        frag, lo, hi = row_fragment(idx)
        tc = {
            "req_id": leaf,
            "tc_id": f"NR1L-PowerManagement-{nxt:03d}",
            "tc_title": title,
            "test_group": "Power Management",
            "test_set": "Power State",
            "test_item": f"{frag}\n\n{second_segment(proc, er)}",
            "pre_conditions": pre,
            "input_test_data": "NA",
            "test_procedure": proc,
            "expected_result": er,
            "specification_reference": SPEC + sec,
            "priority": "P0",
            "design_method": "決策表 (Decision Table Testing)",
            "split_flag": True,
            "split_reason": sr,
            "functional_safety": "NA",
            "estimated_test_time": "",
            "remarks": "",
            "distinguishing_axis": axis,
            "reasoning_note": (
                f"**首段取自錨點 `4941453` 之連續片段**（R-P343(c) / R-P344）——"
                f"該錨點 4,259 字元逾 1,000；片段起訖字元位置 {lo}–{hi}，"
                f"即該狀態列之九欄，照原分隔逐字取，未加 `=`、未加 `,`、未重排欄序。"),
            "split_index": sidx,
        }
        added.append(tc)
        print(f"  + {tc['tc_id']}  {leaf}  片段 {lo}-{hi}  「{title}」")
        nxt += 1
    if apply:
        d["tcs"].extend(added)
        BATCH7.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"已寫入 —— 280 → {280 + len(added)} 條")
    else:
        print("（--dry-run，未寫入）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
