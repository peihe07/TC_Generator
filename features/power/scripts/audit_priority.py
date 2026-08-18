"""G162 —— P0 分布與 §10.2 七類對照（R-P235）。

P0 佔全批 **73.1%**（193 / 264）。§10.2 之 P0 定義為窄類：
「safety, boot/recovery, connection, audio output, eCall,
  vehicle-critical CAN signal, data-loss risk」。
**近四分之三之 TC 落入該窄類，其合理性未經檢驗。**

此與 `design_method` 為同型風險：一個由執行層逐條指派、
**無閘門驗其正確性**、且高度集中於單一值之欄位。
R-P8 令 priority 依 TC 實際測項套 §10.2 判定 —— 而該判定之結果從未被複核。

**本閘不改任何 priority 值**（R-P235 / §I）—— 只量測與對照，裁定於 34 包。

用法：
    python features/power/scripts/audit_priority.py
"""

from __future__ import annotations

import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

SEED = 33
RATE = 1 / 6

# §10.2 之 P0 七類（逐字）
P0_CLASSES = ["safety", "boot/recovery", "connection", "audio output",
              "eCall", "vehicle-critical CAN signal", "data-loss risk"]

# 逐條對照 —— **人工判定**，值：(所屬類別 or None, 依據)
CLASSIFY: dict[str, tuple[str | None, str]] = {
 "007": ("audio output", "Load Shed 限制音量並靜音 —— 直接為音訊輸出"),
 "033": ("vehicle-critical CAN signal", "`STATUS_BH_BCM2.RemStActvSts` 觸發之電源轉換"),
 "038": ("boot/recovery", "Timeout1 到期後轉入 Standby —— 電源狀態之復歸"),
 "053": ("vehicle-critical CAN signal", "`STATUS_BH_BCM2.RemStActvSts` 之回報"),
 "068": ("boot/recovery", "關機鍵觸發之 Idle 轉換"),
 "083": ("boot/recovery", "Logistic mode 之電源狀態轉換"),
 "085": ("vehicle-critical CAN signal", "`RemStActvSts` 轉換所致之旗標清除"),
 "086": ("connection", "通話中之轉接 popup —— 其標的為通話之保持"),
 "088": (None, "**依據薄弱** —— 所驗為「拒絕 popup 後**維持** Timed」，"
                "既非通話之建立或中斷，亦非電源轉換；較近 §10.2 之 P1"
                "「key operational logic flow」"),
 "101": (None, "**無法歸類** —— Timeout1 自 PROXI 取值，為參數設定，"
                "不屬七類任一"),
 "105": (None, "**無法歸類** —— 同 `101`，參數取值"),
 "110": (None, "**依據薄弱** —— 後視影像之顯示；§10.2 之 `audio output` "
                "不含 video，七類無「影像輸出」"),
 "113": ("boot/recovery", "Ignition Off → Standby 之電源轉換"),
 "115": ("boot/recovery", "防盜成功後之開機流程（→ Full-Operation）"),
 "116": ("boot/recovery", "防盜成功後之開機流程（→ Idle）"),
 "117": ("boot/recovery", "同上，Recall_Last 分支"),
 "129": ("boot/recovery", "進入 TLM off 狀態之關機流程"),
 "133": ("boot/recovery", "Sleep 下之喚醒流程（防盜啟動 ＋ Splash）"),
 "135": ("boot/recovery", "同 `133`，另一觸發鍵"),
 "138": (None, "**依據薄弱** —— 後視影像之提供；同 `110`，七類無影像輸出"),
 "139": (None, "**依據薄弱** —— 同 `138`"),
 "154": (None, "**無法歸類** —— Sirius logo 之呈現；"
                "屬 §10.2 之 P3「cosmetic detail / low-impact customization」"),
 "171": ("boot/recovery", "FOTA 更新致 HU 轉入 Timed —— 電源狀態轉換"),
 "182": ("boot/recovery", "模式變更取消開機動畫並切換電源模式"),
 "184": ("boot/recovery", "同 `182`"),
 "191": (None, "**依據薄弱** —— 開機音效之伴隨播放；其為裝飾性音效，"
                "非 §10.2 之 `audio output`（音訊輸出功能）"),
 "208": ("boot/recovery", "開機序列之 splash 與免責畫面呈現"),
 "212": ("connection", "通話中之畫面略過 —— 其前提為通話進行中"),
 "230": ("connection", "來電所致之畫面延後補顯"),
 "237": (None, "**無法歸類** —— 品牌字型之選用；屬 P3 cosmetic"),
 "240": (None, "**無法歸類** —— 品牌 App icon 之選用；屬 P3 cosmetic"),
 "241": (None, "**無法歸類** —— 同 `240`"),
 "257": (None, "**無法歸類** —— 日間主題之採用；屬 P3 cosmetic"),
 "259": (None, "**無法歸類** —— 季節判定；不屬七類任一"),
}


def load() -> list[dict]:
    out = []
    for p in sorted(GENERATED.glob("*.json")):
        out += json.loads(p.read_text(encoding="utf-8"))["tcs"]
    return out


def main() -> None:
    tcs = load()
    by = defaultdict(Counter)
    for t in tcs:
        by[t["test_set"]][t["priority"]] += 1
    tot = Counter(t["priority"] for t in tcs)
    n = len(tcs)

    out = ["# G162 —— P0 分布與 §10.2 七類對照（R-P235）\n",
           "\n> **本閘不改任何 `priority` 值**（R-P235 / §I）—— 只量測與對照，裁定於 34 包。\n",
           f"\n## 1. 全批分布（{n} 條）\n\n| priority | 條 | 佔比 |\n|---|---|---|\n"]
    for k in ("P0", "P1", "P2", "P3"):
        if tot[k]:
            out.append(f"| {k} | **{tot[k]}** | {tot[k]/n*100:.1f}% |\n")

    out.append("\n## 2. 逐 Test Set 之 P0 佔比\n\n"
               "| Test Set | 條 | P0 | 佔比 |\n|---|---|---|---|\n")
    for ts in sorted(by):
        s = sum(by[ts].values())
        out.append(f"| {ts} | {s} | **{by[ts]['P0']}** | {by[ts]['P0']/s*100:.1f}% |\n")

    p0 = defaultdict(list)
    for t in tcs:
        if t["priority"] == "P0":
            p0[t["test_set"]].append(t)
    rng = random.Random(SEED)
    sel = []
    out.append(f"\n## 3. 抽樣（種子 `random.Random({SEED})`，率 ≥ 16.7%）\n\n"
               "| Test Set | 母體 | 抽樣 | 率 |\n|---|---|---|---|\n")
    for ts in sorted(p0):
        k = max(1, -(-len(p0[ts]) * 1 // 6))
        s = rng.sample(p0[ts], k)
        sel += s
        out.append(f"| {ts} | {len(p0[ts])} | **{k}** | {k/len(p0[ts])*100:.1f}% |\n")
    sel.sort(key=lambda t: t["tc_id"])
    tot_p0 = sum(len(v) for v in p0.values())
    out.append(f"| **合計** | {tot_p0} | **{len(sel)}** | {len(sel)/tot_p0*100:.1f}% |\n")

    ok = [t for t in sel if CLASSIFY.get(t["tc_id"][-3:], (None, ""))[0]]
    bad = [t for t in sel if not CLASSIFY.get(t["tc_id"][-3:], (None, ""))[0]]
    out.append(f"\n## 4. 逐條對照 §10.2 七類\n\n"
               f"**可歸類 {len(ok)} / {len(sel)}；"
               f"無法歸類或依據薄弱 {len(bad)} / {len(sel)} = "
               f"{len(bad)/len(sel)*100:.1f}%**\n\n"
               "| tc_id | Test Set | 測項 | §10.2 類別 | 依據 |\n|---|---|---|---|---|\n")
    for t in sel:
        cls, why = CLASSIFY[t["tc_id"][-3:]]
        out.append(f"| `{t['tc_id'][-3:]}` | {t['test_set']} | {t['test_item'][:44]} | "
                   f"{cls if cls else '**—**'} | {why} |\n")

    ts_bad = Counter(t["test_set"] for t in bad)
    out.append("\n## 5. 無法歸類者之 Test Set 分布\n\n"
               "| Test Set | 無法歸類 / 抽樣 |\n|---|---|\n")
    for ts in sorted(p0):
        s = sum(1 for t in sel if t["test_set"] == ts)
        out.append(f"| {ts} | **{ts_bad.get(ts, 0)}** / {s} |\n")

    (DATA / "g162_priority.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g162_priority.md').relative_to(ROOT)}")
    print(f"  P0 {tot['P0']} / {n} = {tot['P0']/n*100:.1f}%")
    print(f"  抽樣 {len(sel)} / {tot_p0} = {len(sel)/tot_p0*100:.1f}%（種子 {SEED}）")
    print(f"  **可歸類 {len(ok)}、無法歸類或依據薄弱 {len(bad)} "
          f"（{len(bad)/len(sel)*100:.1f}%）**")
    for ts in sorted(p0):
        s = sum(1 for t in sel if t["test_set"] == ts)
        print(f"     {ts:22s} 無法歸類 {ts_bad.get(ts,0)} / 抽樣 {s}")


if __name__ == "__main__":
    main()
