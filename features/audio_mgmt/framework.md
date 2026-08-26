# framework.md — Audio Management（audio_mgmt）

鎖定狀態：LOCKED（Pei 2026-08-26 裁：「1採 2採 B1准」）
依據：02 包全表歸位；IN §4.1

## Layer 1（Test Group）
Audio Management

## Layer 2（Test Set）× Layer 3（CFTS 章節，僅本檔，不入簿）

| Test Set | Layer 3 | 葉數 |
|---|---|---|
| Audio Sources | 1.3.1.1–1.3.1.3 | 37 |
| Source Transition | 1.3.3.15, 1.3.3.19 | 34 |
| Audio Arbitration | 1.3.3.1–1.3.3.4, 1.3.3.17, 1.3.3.18 | 29 |
| Focus and Ducking | 1.3.2.14, 1.3.3（Focus/Ducking/Mixing） | 18 |
| Mute Requests | 1.3.3.5–1.3.3.7, 1.3.3.12 | 32 |
| Volume Control | 1.3.2.10–1.3.2.12 | 50 |
| Tones and Alerts | 1.3.1.4–1.3.1.6, 1.3.2.6 | 32 |
| Audio Processing | 1.3.2.7–1.3.2.9, 1.3.2.15, 1.3.2.17–1.3.2.22 | 34 |
| Surround and Fade | 1.3.2.13, 1.3.2.16 | 24 |
| Power and Persistence | 1.3.2.2–1.3.2.4＋Volume Restoration／Persistent Storage 群 | 25 |
| Logistic Mode | 1.3.5.1–1.3.5.2 | 3 |

合計 318 列（317 唯一 SWE ID；SWE1_AMM_076 碰撞見 R-AM6）。

## 備註
- 1.3.4 Arbitration Conditions Tables：條件表素材，隨 Audio Arbitration 引用，不獨立成集。
- **1.3.3.11 Carplay Alternate Audio：在範圍內（R-AM14，2026-08-26 Pei 裁「准」）。**
  SWE1_AMM_286（→4866817 混音）、SWE1_AMM_287（→4866818 `<vent off>` 衰減）
  均為本 SWE.1 之葉，Layer 2 = Focus and Ducking。章節標題掛 CarPlay 僅說明
  觸發來源型別，需求本體為混音與衰減之音訊行為。
  ~~原註「本 SWE.1 零葉，由 Projection feature（SWE1-PROJ）承接」~~ **已撤回**：
  該判定係以 CarPlay／Android Auto／Projection 三詞掃描而得，而原文寫
  Alternate Audio，關鍵詞過窄致誤（分析層之誤）。
- 殘留 coverage gap（維持揭露，不擴編）：4866819（細節指向 Apple AIS）、
  1.3.3.14 Android Auto Certification —— 確無 SWE.1 葉。
- 新 RD 進場：先歸位本表；無適集者先修本檔再寫 TC（IN §4.1）。
- 逐葉明細：`docs/handoff/02_framework_assignment.md` §二。
