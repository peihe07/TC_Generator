"""R-P396(a) —— 原子 token 字典之機器套用（71 包 §H 第 3 步）。

字典逐字取自 71 包 §1 表（`data/proxy_dictionary_71.md`）。
**字典外之代理量不得自填**（R-P396(e) / §I）—— 未覆蓋之 token 原句保留，回報。

套用規則（R-P395(c)）：
  `Read <X> …` / `Check that <X> …` 之 `<X>` 以 ` and ` / ` against ` / `, ` 拆為原子 token；
  **每 token 一句 check**，ER 逐句對齊。

用法：
    python features/power/scripts/apply_dictionary_71.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"

READ = re.compile(r"^(?:Read|Check that)\s+(.*?)(?:\s+(?:and check that|to check)\b.*)?$", re.I)
SPLIT = re.compile(r"\s+and\s+|\s+against\s+|,\s*")

# ── 字典（71 包 §1 表逐字）──────────────────────────────────────────
STATE = f"Read the signal {PS} and check that it is the expected <raw> (<STATE>)"
FUNC = "Apply FUNC_STATE_<STATE> and check its {sub} sub-item"

D: dict[str, str] = {}


def put(toks, val):
    for t in toks:
        D[t.lower()] = val


# A. 狀態機（五 token 同物，R-P396(b)）
put(["TLM_Status.Info", "$Telematic_Power$", "TLM state", "HU mode", "power mode",
     "its power mode", "TLM power indication"], STATE)
put(["HU timer"], "PENDING: DR-PW26 Suspend-to-RAM 觀察面")
# B. 畫面
put(["screen", "display", "TLM display"], FUNC.format(sub="Display"))
put(["shown Splash Screen"], 'Read the HU screen and check that the "Splash Screen" is shown on it')
put(["TLM display before", "after SplashScreen_Time", "TLM display through SplashScreen_Time"],
    'PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen and check the '
    '"Splash Screen" against that time on the recording')
put(["its duration"], "PENDING: DR-PW30 Response_Wait_Time 之值")
put(["display backlight"],
    "Read the HU screen and check that the backlight is off when no HMI screen is shown")
put(["screen sequence"],
    'Read the HU screen and check that the "Start-up Animation", the "Splash Screen" and '
    'the "Disclaimer" are shown separately in that order')
put(["startup flow", "HMI"],
    'Read the HU screen and check that the "Geolocation + SOS" pop-up is shown on it'
    "  —— PENDING: DR-PW27 GDPR flow in HMI")
put(["avatar list in the profile screen"],
    'Read the "Profile" screen and check that its avatar list is the "<Brand> avatars"')
put(["shown seat graphic"], "PENDING: DR-PW27 seat graphic 指派")
put(["applied theme", "configured value"], "PENDING: DR-PW27 [PDO Theme Configuration]")
put(["its timing"], "PENDING: DR-PW27 <Tsend> 之值")
put(["played animation", "season the HU determines"],
    "Read the recording and check which start-up animation is played "
    "(new season animation or normal brand animation)")
# C. 音訊
put(["audio", "entertainment audio", "audio output", "audio output state",
     "TLM audio output state", "audio path", "AMP"],
    "Read the HU speakers and check whether entertainment audio output is present on them")
put(["active source", "active audio source"],
    "Read the source indicator and record its value, then check it against the recorded value")
put(["volume limit"],
    "Read the signal $TELEMATIC_FD_13.AUD_LVL$ and check that it is the expected level")
put(["audio output for ANC", "chimes"],
    "Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and check that the chime "
    "is audible on the left hand front speaker  —— PENDING: DR-PW29 ANC 之刺激與觀察面")
put(["ACN"], "PENDING: DR-PW29 ACN 之刺激與觀察面")
# D. 功能可用性
put(["ICS", "ICS functionality availability"],
    "Touch the screen and read the bus trace, and check whether "
    "$TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) with coordinates")
put(["DTV state", "DTV states", "DTV functionality availability"],
    FUNC.format(sub="Display") + "  (DTV 影像僅經顯示可見；規格無獨立 DTV 觀察面)")
put(["TLM", "active functionality"], "Apply FUNC_STATE_<STATE> and check all of its sub-items")
put(["FPDM"], FUNC.format(sub="Display / Illumination")
    + "  (FPDM 對應為分析層判斷，非規格明文 —— R-P396(c)，併 DR-PW29)")
put(["network state"],
    "Read the bus trace and check whether the HU keeps transmitting the "
    "$STATUS_TELEMATIC$ message")
# E. 內部變數（維持佔位）
put(["VPLastStatus", "stored last status"], "PENDING: DR-PW23 VPLastStatus")
put(["antitheft request", "Antitheft_Activation.Req"], "PENDING: DR-PW23 Antitheft_Activation.Req")
put(["RemStartFail"], "PENDING: DR-PW23 RemStartFail")
put(["SwitchOff_Timeout_Setting.Req"], "PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req")
put(["Auto_SwitchOn_Setting.Req"], "PENDING: DR-PW25 Auto_SwitchOn_Setting.Req 之設定項名")
# F. 其他
put(["HU reaction"],
    'Read the HU screen and check that the "Call Screen" is shown on it, and check that the '
    f"call audio is present on the HU speakers, and read the signal {PS}")
put(["HU behavior"],
    'Read the HU screen and check that it goes dark and then shows the "Splash Screen" again, '
    "and read the bus trace and check that the $STATUS_TELEMATIC$ message stops and resumes")
put(["$Radio_Theme$"], "Read the signal $RADIO_B4.Radio_Theme$ and check its value")
put(["$PowerMode$"], "Read the signal $STATUS_BH_BCM2.CmdIgnSts$ and check its value (DR-PW26)")
put(["LTM_OperationalModeSts.Info"],
    "Read the signal $STATUS_BH_BCM1.OperationalModeSts$ and check its value (DR-PW26)")


def rewrite_line(line: str, miss: Counter) -> str:
    body = re.sub(r"^\s*\d+\.\s*", "", line).strip()
    if "PENDING" in body:
        return body
    m = READ.match(body)
    if not m:
        return body
    x = m.group(1).strip()
    toks = [re.sub(r"^(the|a|an)\s+", "", t.strip(), flags=re.I).strip(" .,;:")
            for t in SPLIT.split(x)]
    toks = [t for t in toks if t]
    if not toks:
        return body
    outs, unresolved, touched = [], False, False
    for t in toks:
        if rm.whitelisted(t):
            # 已為白名單之原子 —— **原文保留**，不經字典（不得破壞既有正確內容）
            piece = f"Read {t}" if not outs else t
            if piece not in outs:
                outs.append(piece)
            continue
        v = D.get(t.lower())
        if v is None:
            miss[t] += 1
            unresolved = True
            continue
        touched = True
        if v not in outs:
            outs.append(v)
    if unresolved or not touched:
        return body                      # 未覆蓋或無可換者 → 原句保留（R-P396(e)）
    return "; ".join(outs)


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    cur = [tc for d in files.values() for tc in d["tcs"]]
    # 母體：三閘未歸零之條（同 `composite_tokens_70.py`）—— 其餘不動，
    # 避免破壞 55–70 包已改寫且六閘已過之內容
    INT = re.compile(r"\b([A-Za-z0-9_]+\.(?:Info|Req))\b|\b(RemStartFail)\b")
    pool = {tc["tc_id"] for tc in cur
            if rm.DETECTORS["A_upper"](tc) or rm.DETECTORS["G"](tc)
            or any(INT.search(l) and "PENDING" not in l
                   for f in ("test_procedure", "expected_result")
                   for l in (tc.get(f) or "").splitlines())}
    print(f"母體（三閘未歸零）{len(pool)} 條 / 全案 {len(cur)}")
    miss: Counter = Counter()
    changed = 0
    for p, d in files.items():
        hit = False
        for tc in d["tcs"]:
            if tc["tc_id"] not in pool:
                continue
            for f in ("test_procedure", "expected_result"):
                src = tc.get(f) or ""
                out = [rewrite_line(l, miss) for l in src.splitlines() if l.strip()]
                new = "\n".join(f"{i}. {l}" for i, l in enumerate(out, 1))
                if new != src:
                    tc[f] = new
                    hit = True
            if hit and "R-P396" not in (tc.get("remarks") or ""):
                tc["remarks"] = ((tc.get("remarks") or "").strip() + " (R-P396 字典套用)")
                tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
                    "\n\n**R-P396(a) 字典套用（71 包）**：複合觀察目標依 "
                    "`data/proxy_dictionary_71.md` 逐 token 換為白名單代理量，"
                    "每 token 一句 check。**字典外之代理量未自填**（R-P396(e)）。")
                changed += 1
        if hit and not dry:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"套用 {changed} 條")
    print(f"字典未覆蓋 token {len(miss)} 個（出現 {sum(miss.values())} 次）")
    for t, n in miss.most_common(20):
        print(f"   {n:4d}  {t[:70]}")
    if dry:
        print("（dry-run）")


if __name__ == "__main__":
    main()
