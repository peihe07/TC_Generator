"""B2 — R-P42 閘門 (b) 之偽陽性量測（R-P61 / G41 / G42）。

G33 只驗「該觸發時會觸發」。本腳本驗反面：**不該觸發時不會觸發**。

(a) 主要 —— 合成 22 條合法 Power TC（涵蓋五個 Test Set），
    內容為**被引用錨點之改寫**（同義重寫，非逐字抄錄）。
    期望誤觸發 0。合成而非取自 repo，依 07 / 08 §I。

(b) 次要，**非權威** —— 以其他 feature 之已交付 TC 語料試跑。
    該等 TC 屬不同規格，理應 0 命中；若有命中即證特徵字串過於通用。
    **此為訊號非判準。**

用法：
    python features/power/scripts/build_false_positive.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import (  # noqa: E402
    CONTENT_FIELDS, anchor_bodies, build_fingerprints,
    check_rp42_unreferenced_anchor, load_blacklist,
)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# R-P55 回歸斷言
EXPECTED_FALSE_POSITIVES = 0

# 合成之合法 Power TC 語料（22 條，涵蓋五個 Test Set）。
# 內容為被引用錨點之**改寫** —— 用詞取自 Power 領域（電源狀態、訊號、逾時、
# splash、branding、power down），但句子由執行層重寫，非逐字抄錄。
CORPUS: list[tuple[str, str, str, str, str]] = [
    # (test_set, test_item, pre_conditions, test_procedure, expected_result)
    ("Power State", "Full-Operation policy is applied on state entry",
     "1. Vehicle in Ignition On", "1. Drive the power mode signal to Full-Operation",
     "1. Display is on, audio is unmuted, tuner and USB are available"),
    ("Power State", "Idle policy mutes audio and keeps the display off",
     "1. Head unit in Full-Operation", "1. Request a transition to Idle",
     "1. The display turns off and audio is muted"),
    ("Power State", "Partial Operation shows only the antitheft screen",
     "1. Head unit in Sleep", "1. Assert the remote start status signal",
     "1. Only the antitheft screen is rendered and chimes remain audible"),
    ("Power State", "Standby is entered when ignition moves to Off",
     "1. Head unit in Idle", "1. Move ignition to the Off position",
     "1. The unit reports Standby through the custom power interface"),
    ("Power State", "Sleep is entered after the network goes down",
     "1. Head unit in Standby", "1. Remove bus activity and wait for the timer",
     "1. The unit reports Sleep and stops all wake sources"),
    ("Power State", "Bench mode is reported when the harness is detected",
     "1. Bench harness attached", "1. Power the unit from the bench supply",
     "1. Bench is reported and diagnostics remain reachable"),
    ("Power State", "Logistic Idle is reported while logistic mode is on",
     "1. Logistic mode enabled", "1. Set ignition to On with logistic mode active",
     "1. Logistic Idle is reported and no source is playable"),
    ("Power State", "Logistic Standby keeps the network alive",
     "1. Logistic mode enabled", "1. Move ignition to Off with the bus still active",
     "1. Logistic Standby is reported"),
    ("Power State", "Logistic Sleep is reported with the network down",
     "1. Logistic mode enabled", "1. Move ignition to Off and drop the bus",
     "1. Logistic Sleep is reported"),
    ("Power State", "Init state is reported during boot",
     "1. Unit powered off", "1. Apply battery and observe the first reported state",
     "1. Init is reported before any operative state"),
    ("Power State", "Telematic power signal follows the internal state",
     "1. Head unit in Full-Operation", "1. Transition through Idle and Standby",
     "1. The telematic power signal mirrors each internal state"),
    ("Power State", "Phone call keeps the unit out of Idle",
     "1. Head unit in Full-Operation", "1. Start an incoming call and let the timer run",
     "1. The unit stays in Full-Operation while the call is connected"),
    ("Startup Display", "Splash logo is rendered on a cold boot",
     "1. Unit fully powered down", "1. Apply battery and observe the first frames",
     "1. The branded splash logo is shown before the home screen"),
    ("Startup Display", "Splash logo is rendered on a warm boot",
     "1. Head unit in Standby", "1. Wake the unit with the power button",
     "1. The splash logo is shown for the configured duration"),
    ("Startup Display", "No splash is shown on Idle to Full-Operation",
     "1. Head unit in Idle", "1. Trigger a transition to Full-Operation",
     "1. The home screen appears without a splash frame"),
    ("Startup Display", "Startup animation can be skipped by user input",
     "1. Startup animation playing", "1. Touch the screen during the animation",
     "1. The animation stops and the home screen is shown"),
    ("Branding and Theme", "Branded font is applied after boot",
     "1. Brand parameter configured", "1. Boot the unit and open any menu",
     "1. All labels render with the branded font"),
    ("Branding and Theme", "Branded map theme follows the vehicle brand",
     "1. Brand parameter configured", "1. Open the navigation surface",
     "1. The map uses the branded palette"),
    ("Branding and Theme", "Contextual theme switches with day and night",
     "1. Luminosity sensor present", "1. Change the ambient light level",
     "1. The theme switches between the day and night variants"),
    ("Timeout Settings", "Switch off timeout can be set to zero minutes",
     "1. Configuration parameter set to twenty minutes",
     "1. Open the telematics menu and choose the zero minute option",
     "1. The timeout takes the zero minute value"),
    ("Timeout Settings", "Switch off timeout can be set to sixty minutes",
     "1. Configuration parameter set to sixty minutes",
     "1. Open the telematics menu and choose the sixty minute option",
     "1. The unit stays awake for sixty minutes after ignition off"),
    ("Power Down", "Shutdown completes after the power down request",
     "1. Head unit in Full-Operation", "1. Issue a power down request over the bus",
     "1. The unit completes shutdown and stops reporting a power state"),
]


def synth_corpus() -> list[dict]:
    return [
        {
            "tc_id": f"FP-{i + 1:03d}",
            "test_set": ts,
            "test_item": item,
            "pre_conditions": pre,
            "input_test_data": "NA",
            "test_procedure": proc,
            "expected_result": exp,
            "specification_reference": "CFTS009_1.6.2.1.1_4941357",
        }
        for i, (ts, item, pre, proc, exp) in enumerate(CORPUS)
    ]


def other_feature_tcs() -> tuple[list[dict], list[str]]:
    """其他 feature 之已交付 TC —— 非權威訊號（R-P61(b)）。"""
    tcs, sources = [], []
    for feature_dir in sorted((ROOT / "features").iterdir()):
        if feature_dir.name == "power" or not (feature_dir / "generated").is_dir():
            continue
        files = sorted((feature_dir / "generated").glob("*.json"))
        if not files:
            continue
        sources.append(f"{feature_dir.name}（{len(files)} 檔）")
        for path in files:
            for tc in json.loads(path.read_text(encoding="utf-8")).get("tcs", []):
                tc = dict(tc)
                tc["tc_id"] = f"{feature_dir.name}:{tc.get('tc_id', path.stem)}"
                tcs.append(tc)
    return tcs, sources


def main() -> None:
    blacklist = load_blacklist()
    fingerprints = build_fingerprints(blacklist, anchor_bodies())
    total_prints = sum(len(v) for v in fingerprints.values())

    corpus = synth_corpus()
    hits_a = check_rp42_unreferenced_anchor(corpus, blacklist, fingerprints)
    hits_a_b = [f for f in hits_a if f["rule"] == "R-P42(b)"]

    others, sources = other_feature_tcs()
    hits_b = [f for f in check_rp42_unreferenced_anchor(others, blacklist, fingerprints)
              if f["rule"] == "R-P42(b)"]

    out = [
        "# B2 — R-P42 閘門 (b) 之偽陽性量測（R-P61 / G41 / G42）\n",
        "\n> G33 只驗「該觸發時會觸發」；本檔驗反面：**不該觸發時不會觸發**。\n",
        "> 產生指令：`python features/power/scripts/build_false_positive.py`\n",
        f"\n特徵字串母體：**{len(fingerprints)} 個黑名單錨點、{total_prints} 條句子**"
        f"（`MIN_FINGERPRINT = 40`，依 R-P62 不調）。\n",
        f"\n## 1. G41 —— 合成合法 Power 語料（主要，權威）\n\n",
        f"語料：**{len(corpus)} 條**合成 TC，涵蓋五個 Test Set。\n"
        "內容為被引用錨點之**改寫**（同義重寫），非逐字抄錄；"
        "合成而非取自 repo（07 / 08 §I）。\n\n",
        "| Test Set | 條數 |\n|---|---|\n",
    ]
    from collections import Counter
    for ts, n in Counter(t["test_set"] for t in corpus).most_common():
        out.append(f"| {ts} | {n} |\n")
    out.append(
        f"\n**誤觸發（R-P42(b)）：{len(hits_a_b)} / {len(corpus)}**"
        f"{'  —— 期望 0，達成。' if not hits_a_b else '  —— **未達期望**。'}\n"
    )
    if hits_a_b:
        out.append("\n| TC | 錨點 | 特徵字串 |\n|---|---|---|\n")
        for f in hits_a_b:
            out.append(f"| `{f['tc_id']}` | `{f['anchor']}` | {f['detail'][:120]} |\n")

    out.append(
        f"\n## 2. G42 —— 其他 feature 之已交付 TC（次要，**非權威**）\n\n"
        f"> **此為訊號非判準**（R-P61(b)）。該等 TC 屬不同規格，理應 0 命中；\n"
        f"> 若有命中即證特徵字串過於通用。命中與否皆不改變 G41 之結論。\n\n"
        f"語料來源：{'、'.join(sources) or '（無）'}，共 **{len(others)} 條 TC**。\n\n"
        f"**命中（R-P42(b)）：{len(hits_b)} / {len(others)}**"
        f"{'  —— 0 命中，與預期一致。' if not hits_b else '  —— **有命中，須逐條判斷**。'}\n"
    )
    if hits_b:
        out.append("\n| TC | 錨點 | 特徵字串 | 是否為通用語句 |\n|---|---|---|---|\n")
        for f in hits_b:
            out.append(f"| `{f['tc_id']}` | `{f['anchor']}` | {f['detail'][:110]} | 待判 |\n")

    out.append(
        "\n## 3. 結論\n\n"
        f"- **G41 = {len(hits_a_b)}**（合成合法 Power 語料之誤觸發）\n"
        f"- **G42 = {len(hits_b)}**（跨 feature 命中，非權威訊號）\n\n"
        "偽陽性率之量測已完成，滿足 **R-P61** 與 **R-P65(b)**。\n"
        "依 **R-P62**，`MIN_FINGERPRINT` 於本包不調整；本量測為日後另案再議之基準。\n\n"
        "### 本量測之效力範圍（執行層自陳）\n\n"
        f"語料 {len(corpus)} 條為執行層自撰，其用詞雖取自 Power 領域，"
        "但**句式必然帶有撰寫者之習慣**。真實 Phase 4 之 TC 由不同流程產生，"
        "其句式分布未必相同。**G41 = 0 證明「這 22 條不會被誤殺」，"
        "不等於「任何合法 TC 都不會被誤殺」。**\n"
        "G42 之跨 feature 語料句式獨立於本包撰寫者，故其結果之獨立性較高 ——"
        "但它屬不同規格領域，命中率天然偏低，**低估了同領域之碰撞風險**。\n"
        "二者皆非完整之偽陽性率估計，此限制登記於上繳包 §七。\n"
    )

    path = DATA / "b2_false_positive.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G41 合成合法語料 {len(corpus)} 條 → 誤觸發 **{len(hits_a_b)}**")
    print(f"G42 其他 feature {len(others)} 條（{'、'.join(sources) or '無'}）→ 命中 **{len(hits_b)}**（非權威）")
    for f in hits_a_b + hits_b:
        print(f"   {f['tc_id']} ← {f['anchor']}: {f['detail'][:100]}")

    if len(hits_a_b) != EXPECTED_FALSE_POSITIVES:
        print(f"\n**回歸斷言失敗（R-P55）**：G41 {len(hits_a_b)} ≠ 期望 {EXPECTED_FALSE_POSITIVES}")
        raise SystemExit(1)
    print("\n回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
