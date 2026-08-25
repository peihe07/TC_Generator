#!/usr/bin/env python3
"""batch 6 —— `Voice Assistant Key`（ch 11，5 leaf）之 TC 產出（37 包步驟 4）。

**本 feature 之最後一批。**

**四項拘束**（37 包 §五步驟 4）：
  (a) `source_clause` 取自 **PDF**，`origin` = `spec_pdf p10`（R-PMH50）；
  (b) 產出後即跑 `desc_coverage`（正向＋反向），不待下一輪；
  (c) 限定依 R-PMH94／R-PMH97／R-PMH101 逐斷言導出，
      **依 R-PMH126 逐條具名，不得樣板**；
  (d) **ch 11 × 矩陣已於 22 包全對照（牴觸 0）** —— 其結果直接引用，不重跑。

**`-026-02`～`-026-05` 之四個結果為許可式**（`may result in` ／ `depends on
outcome`）—— 依 **R-PMH140** 逐條具名三事。

**`tc_id` 續為 provisional**；**零寫回工作簿**。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"
VAK = "Voice Assistant Key"

PDF = {
 "VRLP1": ("VRLP1: VR hard key to activate SIRI/non-native Voice Assistants (eg. Long press "
           "of VR HK) shall be functional when radio is OFF and KEY ON or ACC."),
 "OUT": "Radio status after interaction with SIRI depends on outcome of the interaction:",
 "S_OFF_A_OFF": "Screen Off and Audio OFF (i.e. radio back to off),",
 "S_ON_A_OFF": "Screen ON and Audio OFF,",
 "S_OFF_A_ON": "Screen Off, and Audio ON,",
 "S_ON_A_ON": "Screen ON and Audio ON.",
}

# R-PMH140 —— 許可式之三事具名（`-050`～`-053` 共用其形態而**逐條具名其所指之結果**）
def perm(outcome: str) -> str:
    return ("⚠ **許可式之處置（R-PMH140）** —— 具名三事："
            "(a) **其來源為許可式** —— 規格逐字為 `Radio status after interaction with SIRI "
            "**depends on outcome of the interaction**`，037 之 DESC 逐字為 "
            "`the system **may** result in the following status`；其保證該狀態之**容許**，"
            "**不保證其必然發生**；"
            f"(b) **本 TC 所驗者為「當互動之結果為 {outcome} 時，收音機確實進入該狀態」**，"
            "非其於任何互動皆進入該狀態；"
            "(c) **其不發生不必然為缺陷** —— **判 fail 前須先確認該次互動之結果確為本條所述者**。"
            "**不另開 DR**（R-PMH140）—— 許可式為規格之常見書寫，非未定義之記法。")


CH11 = ("⚠ **ch 11 × State Matrix 之全對照已於 22 包完成，牴觸 0**（`VRLP1` × `r11`／`r12`／"
        "`r28`／`r29`，即 `VR button long press without/at Projection` 四列）——"
        "**其結果直接引用，本批不重跑**（37 包 §五步驟 4(d)）。"
        "**故本條無事件層限定** —— 逐斷言導出之結果為「無素材與其取相反值」。")

TCS = [
 dict(leaf="SWE1-HMI-PM-026-01", outline="11.1", src="VRLP1", dm=EP, pri="P1",
   title="VR hard key long press activates the voice assistant when the radio is off",
   item="(等價類：KEY ON 與 ACC 二個點火位置 —— 二者同結果，故為一類)",
   pre=["The radio is OFF",
        "The ignition is in KEY ON or ACC",
        "SIRI or a non-native voice assistant is available in the vehicle"],
   proc=["Long press the VR hard key with the ignition in KEY ON",
         "Repeat the long press with the ignition in ACC",
         "Check that the voice assistant was activated in both cases"],
   er=["The voice assistant is activated by the long press with the ignition in KEY ON",
       "The voice assistant is activated by the long press with the ignition in ACC",
       "The VR hard key is functional in both ignition positions"],
   reason=("**P1 —— 主要功能邏輯**：其失效使使用者於收音機關閉時無法叫出語音助理，"
     "**惟不阻斷開機或安全功能**，故不落 P0。設計方法 EP —— "
     "`KEY ON` 與 `ACC` 為**同一等價類之二成員**（規格以 `or` 並列而給同一結果 "
     "`shall be functional`），**非兩個獨立分支**，故不依 §8.2.2 拆分。"
     "⚠ **`SIRI/non-native Voice Assistants` 二者本條不拆** —— 同理（規格以 `/` 並列）。"
     "⚠ **`(eg. Long press of VR HK)` 為舉例而非唯一手段** —— 規格用 `eg.`；"
     "**本條取長按一路，其餘手段未驗，據實記載為限度**（§8.4.1 不造值）。"
     "⚠ **本條為強制式**（`shall be functional`）—— **與本批四個互動結果條之許可式不同類**"
     "（**跨軸故不以 tc_id 指涉**，R-PMH53 之限度見 34 包 §6.3）："
     "其 ER 因而得無條件斷言。" + CH11),
   axis="謂詞：VR 硬鍵之可用性（對四個互動結果狀態條）"),

 dict(leaf="SWE1-HMI-PM-026-02", outline="11.1", src="S_OFF_A_OFF", dm=EP, pri="P2",
   title="Radio returns to off when the interaction ends with screen off and audio off",
   item="(四個互動結果之第一 —— 螢幕關、音訊關，即回到關閉狀態)",
   pre=["The radio was OFF and the voice assistant was activated by the VR hard key",
        "The interaction with the voice assistant has ended"],
   proc=["Read the screen state and the audio state after the interaction",
         "Check that the radio returned to its off state"],
   er=["The screen is off and the audio is off after the interaction",
       "The radio is back to its off state"],
   reason=("**P2 —— 次要／支援功能**：本條所驗者為互動**結束後之狀態**，"
     "其偏差使收音機停在非預期狀態而**不使任何功能缺失**（§10.2 之 P2 定義）；"
     "**與本批 VR 硬鍵可用性條之 P1 不同級而不矛盾**（R-PMH59）—— 該條驗「叫得出來」，本條驗「結束後停在哪」。"
     "**設計方法 EP** —— 四個結果為同一輸出之四個等價類（螢幕開／關 × 音訊開／關），"
     "**各為一條**（依 R-PMH118，一條只含一類者其技術仍為 EP）。"
     "⚠ **四條之拆分依 §8.2.2** —— 四者**互斥且獨立**，"
     "併為一條則「其一失效」之 pass/fail 判定不明確。"
     + perm("螢幕關閉且音訊關閉") + CH11),
   axis="互動結果之等價類：螢幕關／音訊關（對 -051／-052／-053 之其餘三類）"),

 dict(leaf="SWE1-HMI-PM-026-03", outline="11.1", src="S_ON_A_OFF", dm=EP, pri="P2",
   title="Screen stays on with audio off after the voice assistant interaction",
   item="(四個互動結果之第二 —— 螢幕開、音訊關)",
   pre=["The radio was OFF and the voice assistant was activated by the VR hard key",
        "The interaction with the voice assistant has ended"],
   proc=["Read the screen state and the audio state after the interaction",
         "Check that the screen is on and the audio is off"],
   er=["The screen is on after the interaction",
       "The audio is off after the interaction"],
   reason=("**P2 —— 同本批第一個互動結果條之依據**（R-PMH59：批內依據互不矛盾）。設計方法 EP。"
     + perm("螢幕開啟且音訊關閉") + CH11),
   axis="互動結果之等價類：螢幕開／音訊關（對 -050／-052／-053 之其餘三類）"),

 dict(leaf="SWE1-HMI-PM-026-04", outline="11.1", src="S_OFF_A_ON", dm=EP, pri="P2",
   title="Audio stays on with the screen off after the voice assistant interaction",
   item="(四個互動結果之第三 —— 螢幕關、音訊開)",
   pre=["The radio was OFF and the voice assistant was activated by the VR hard key",
        "The interaction with the voice assistant has ended"],
   proc=["Read the screen state and the audio state after the interaction",
         "Check that the screen is off and the audio is on"],
   er=["The screen is off after the interaction",
       "The audio is on after the interaction"],
   reason=("**P2 —— 同本批第一個互動結果條之依據**。設計方法 EP。"
     + perm("螢幕關閉且音訊開啟") + CH11),
   axis="互動結果之等價類：螢幕關／音訊開（對 -050／-051／-053 之其餘三類）"),

 dict(leaf="SWE1-HMI-PM-026-05", outline="11.1", src="S_ON_A_ON", dm=EP, pri="P2",
   title="Screen and audio both stay on after the voice assistant interaction",
   item="(四個互動結果之第四 —— 螢幕開、音訊開)",
   pre=["The radio was OFF and the voice assistant was activated by the VR hard key",
        "The interaction with the voice assistant has ended"],
   proc=["Read the screen state and the audio state after the interaction",
         "Check that both the screen and the audio are on"],
   er=["The screen is on after the interaction",
       "The audio is on after the interaction"],
   reason=("**P2 —— 同本批第一個互動結果條之依據**。設計方法 EP。"
     + perm("螢幕開啟且音訊開啟") + CH11),
   axis="互動結果之等價類：螢幕開／音訊開（對 -050／-051／-052 之其餘三類）"),
]

BASE = 48        # batch 1–5 用 001–047（`-024` 位次空出），本批續 049 起


def norm_item(s: str) -> str:
    return s.replace("‘", "'").replace("’", "'")


def main() -> None:
    out = []
    for n, t in enumerate(TCS, BASE + 1):
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",
            "test_set": VAK,
            "tc_title": t["title"],
            "test_item": norm_item(f"{PDF[t['src']]}\n\n{t['item']}"),
            "pre_conditions": "\n".join(f"{i}. {x}" for i, x in enumerate(t["pre"], 1)),
            "input_test_data": "NA",
            "test_procedure": "\n".join(f"{i}. {x}" for i, x in enumerate(t["proc"], 1)),
            "expected_result": "\n".join(f"{i}. {x}" for i, x in enumerate(t["er"], 1)),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",
            "vehicle_models": "",
            "remarks": f"Test Set: {VAK}",
            "reasoning": t["reason"],
            "distinguishing_axis": t["axis"],
            "source_clause": PDF[t["src"]],
            "source_clause_origin": "spec_pdf p10",
        })
    doc = {
        "batch": "batch06",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        "test_sets": [VAK],
        "handoff": "docs/handoff/37_batch6.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Voice Assistant Key`（ch 11，5 leaf）—— **本 feature 之最後一批**。"
                      "**5 條 TC** —— 037 已將 `VRLP1` 之四個互動結果各立一 leaf，"
                      "本批逐 leaf 一條，無須再拆。"),
        "tc_id_status": "provisional",
        "leaf_scope": sorted({t["leaf"] for t in TCS}),
        "source_clause_basis": "R-PMH50 —— 取自 spec_pdf p10。",
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        # 逐斷言導出之結果為「無素材與其取相反值」（ch 11 × 矩陣牴觸 0，22 包），故無限定。
        "limits": {},
        "tcs": out,
    }
    p = ROOT / "generated" / "batch06.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 {len(doc['leaf_scope'])} leaf）")


if __name__ == "__main__":
    main()
