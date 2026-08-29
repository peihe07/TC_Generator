#!/usr/bin/env python3
"""交付前體檢報告之產生器（下放包 05 作業 E）。

**A-ICS34 之衝擊已反映於強度與出貨欄之理由**：`<Tstuck_button>`／
`<TPeriodToCountKnobDetents>`／`<TPeriodToSendNoChange>` 之值實存於
`CFTS020-4819541`（§1.8.1，v2 判適用，SFR 型）。本包**未回填**（A-ICS34
將逐物件驗證交 b06、下放包 05 §1 禁區令佔位維持），故判定不變，
但「無值」之理由一律更正為「值查得而未回填」。

機械部分（Test Set／priority／trace 覆蓋／佔位／錨分佈）由本腳本自
`generated/b0*/b0*_tcs.json` 實測產生，**不人工謄寫**。
「驗證強度自評」與「出貨判斷」為執行層之判斷，以下方常數表承載，
其判準逐條寫於報告 §5 檔頭；**判斷本身不可機械化，故不偽裝成機械輸出**。

輸出：docs/reports/05_pre_delivery_check.md
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCHES = ["b01", "b02", "b03", "b04"]
FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
          "expected_result", "test_item", "specification_reference"]
PAT = re.compile(r"PENDING: (DR-ICS\d+) <([^>]+)>")

# 強度自評（執行層判斷）：(強度, 理由)
# 判準——強：末步之主錨可單獨判定通過與否，且其執行不依賴未解之佔位。
#         弱：主錨依賴未解之佔位，或以「不變／相同」承載，或其斷言之前提未載。
STRENGTH = {
 "Stuck button held over 120 s": ("強", "主錨為診斷工具上之 DTC B14DA-2A 置位，可單獨判定；訊號名已實名"),
 "Stuck fault held until de-bounced not-pressed": ("強", "主錨為 DTC 清除，可單獨判定"),
 "Button held exactly 120 s": ("強", "主錨為 DTC 未置位，可單獨判定"),
 "VOLUME knob rotated clock-wise": ("弱", "ER 斷言 \"VOLUME POP_UP\" 顯示，而其顯示條件四包追索仍查無（A-ICS16／DR-ICS4）—— 若該 popup 僅特定條件出現，該行即為潛在 FF"),
 "VOLUME knob rotated counter clock-wise": ("弱", "同上"),
 "Three detents rotated clock-wise": ("弱", "同上，另有 DR-ICS4／DR-ICS12 二處佔位落於 pre_conditions"),
 "Press ignored during stuck condition": ("弱", "門檻 `<Tstuck_button>` 於 TC 內仍為 DR-ICS10 佔位（**值已於 `CFTS020-4819541` 逐字查得 `120 sec`，b05 未回填 —— A-ICS34 交 b06**）；主錨另以「狀態不變」承載"),
 "Button responsive after release": ("弱", "門檻同上（`4819541` 載 `120 sec`，未回填）；主錨為「狀態改變」雖可判，但觸發步驟於 TC 內仍為佔位"),
 "Power hardkey pressed while HU screen on": ("強", "b05 作業 A 後主錨為 HMI 現象（螢幕暗），可單獨判定；TGW 佔位僅及於輔助觀察行"),
 "Power hardkey pressed at Telematic Power full operation": ("強", "同上"),
 "Power hardkey pressed while HU screen off": ("強", "主錨為前一畫面之回復，可單獨判定"),
 "Power hardkey pressed at Telematic Power idle": ("強", "同上"),
 "Screen off hardkey starts the three second timer": ("強", "主錨為 \"TOUCH SCREEN TO TURN ON\" 之持續顯示，可單獨判定"),
 "Screen off hardkey pressed again within three seconds": ("強", "主錨為前一畫面之回復，可單獨判定"),
 "Three second period completed after screen off hardkey": ("強", "主錨為螢幕轉暗，可單獨判定"),
 "Screen off hardkey pressed while HU screen off": ("強", "主錨為前一畫面之回復，可單獨判定"),
 "Knob 2 rotated clock-wise": ("弱", "訊號已實名且主錨可判，但觀察時點依 `<TPeriodToSendNoChange>`（DR-ICS12 佔位）。**`4819541` 逐字載其為 `20 msec`**，遠小於本條所用之 2 秒觀察點 —— 即該觀察點**實際上是安全的**，然值未回填前不得如此宣稱"),
 "Knob 2 rotated counter clock-wise": ("弱", "同上（`20 msec` < 2 秒，觀察點實際安全，惟未回填）"),
 "Knob 2 held stationary": ("弱", "末步以「畫面不變」承載條文之 `ignored by the receiving components` —— 「不做事」無直接訊號面可觀察"),
 "Knob 2 no change sent periodically": ("強", "末步為再次轉動後 `$CLIMATIC_PANEL.Radio_Knob2_DIR$` = 1 (Knob_increment)，訊號已實名且可單獨判定"),
 "Three detents counted in one rotation": ("弱", "`= 3` 之正確性繫於 detent 計數窗（DR-ICS12 佔位）。**`4819541` 載 `initial value 50 msec` 且明標待 parameter tuning 優化** —— 即該值本身為暫定，回填後仍須注意其非定值"),
 "Knob 2 signals acted on by the HU": ("弱", "末步之預期行為為 DR-ICS6 佔位 —— **主錨本身依賴未解之 DR**"),
 "Enter button pressed": ("弱", "末步之目標畫面為 DR-ICS6 佔位 —— **主錨本身依賴未解之 DR**"),
}

# 出貨判斷（執行層判斷）：假設 17 條 DR 全無回覆
SHIP = {
 "Stuck button held over 120 s": ("可", "無佔位；DTC 號與 120 s／8 ms 皆自 DTCs Matrix r57 逐字取得"),
 "Stuck fault held until de-bounced not-pressed": ("可", "同上"),
 "Button held exactly 120 s": ("可", "同上"),
 "VOLUME knob rotated clock-wise": ("**不可**", "無佔位而仍不可 —— 其 ER 有 2 行斷言 popup 顯示，顯示條件未載即為潛在 FF（IN §7）。**無佔位不等於可出貨**"),
 "VOLUME knob rotated counter clock-wise": ("**不可**", "同上"),
 "Three detents rotated clock-wise": ("**不可**", "同上，另有二處佔位"),
 "Press ignored during stuck condition": ("**不可**", "步驟 3 之門檻於 TC 內為佔位，照現狀交付台架無從執行。**理由已更正**：非「無值」（`4819541` 載 `120 sec`），而是「值查得而未回填」——回填屬 b06"),
 "Button responsive after release": ("**不可**", "同上（值查得而未回填）"),
 "Power hardkey pressed while HU screen on": ("可", "R-ICS22(b) 明裁「不因 (a) 之佔位而阻出貨」；主錨為 HMI 現象，佔位僅及輔助行。**出貨時該輔助行應標明未解**"),
 "Power hardkey pressed at Telematic Power full operation": ("可", "同上"),
 "Power hardkey pressed while HU screen off": ("可", "同上"),
 "Power hardkey pressed at Telematic Power idle": ("可", "同上"),
 "Screen off hardkey starts the three second timer": ("可", "同上；3 秒為 4819572 逐字之 spec 值"),
 "Screen off hardkey pressed again within three seconds": ("可", "同上"),
 "Three second period completed after screen off hardkey": ("可", "同上"),
 "Screen off hardkey pressed while HU screen off": ("可", "同上"),
 "Knob 2 rotated clock-wise": ("**不可**", "TC 內帶未回填之佔位。**惟其風險已知為低**：`4819541` 之 `20 msec` 遠小於 2 秒觀察點，回填後本條預期即可出貨"),
 "Knob 2 rotated counter clock-wise": ("**不可**", "同上"),
 "Knob 2 held stationary": ("可（弱）", "無佔位，可執行；但其主錨為「不變」，通過不足以證成條文，**出貨時應標為弱驗證**"),
 "Knob 2 no change sent periodically": ("可", "無佔位，訊號實名，主錨可單獨判定"),
 "Three detents counted in one rotation": ("**不可**", "計數窗於 TC 內為佔位；`4819541` 之 `50 msec` 為 **initial value 且待調校**，回填後仍非定值"),
 "Knob 2 signals acted on by the HU": ("**不可**", "主錨即佔位"),
 "Enter button pressed": ("**不可**", "主錨即佔位"),
}


def load():
    out = []
    for b in BATCHES:
        for t in json.loads((ROOT / "generated" / b / f"{b}_tcs.json").read_text())["tcs"]:
            t["_batch"] = b
            out.append(t)
    return out


def main() -> None:
    tcs = load()
    L = ["# 交付前體檢 — b01 ~ b04 全 23 條（2026-08-29）", "",
         "> 下放包 05 作業 E。**本包不改任何 TC 內容，只出報告。**",
         "> 機械部分（分佈、覆蓋、佔位、錨）由 `scripts/gen_pre_delivery_05.py` 自",
         "> `generated/b0*/b0*_tcs.json` 實測產生；**驗證強度自評與出貨判斷為執行層之判斷**，",
         "> 不偽裝成機械輸出，其判準見 §5／§6 檔頭。", ""]

    L += [f"## §1 總數：**{len(tcs)}** 條", "",
          "| 批 | 條數 |", "|---|---|"]
    for b, n in Counter(t["_batch"] for t in tcs).items():
        L.append(f"| {b} | {n} |")

    L += ["", "## §2 Test Set 分佈", "", "| Test Set | 條數 | 對應 RD |", "|---|---|---|"]
    ts = defaultdict(list)
    for t in tcs:
        ts[t["test_set"]].append(t["req_id"])
    for k in sorted(ts):
        L.append(f"| {k} | {len(ts[k])} | {'、'.join(sorted(set(ts[k])))} |")

    L += ["", "## §3 priority 分佈", "", "| priority | 條數 |", "|---|---|"]
    for k, v in sorted(Counter(t["priority"] for t in tcs).items()):
        L.append(f"| {k} | {v} |")

    L += ["", "## §4 trace 覆蓋（SWE-ICS-001 ~ 012）", "",
          "| RD | TC 數 | Test Set |", "|---|---|---|"]
    cov = defaultdict(list)
    for t in tcs:
        cov[t["req_id"]].append(t["test_set"])
    for i in range(1, 13):
        rid = f"SWE-ICS-{i:03d}"
        rows = cov.get(rid, [])
        L.append(f"| {rid} | {len(rows)} | {'、'.join(sorted(set(rows))) or '**無**'} |")

    L += ["", "## §5 佔位分佈（`scripts/pending_census.py` 之口徑）", "",
          "| DR | 佔位處數 | 涉 TC 數 |", "|---|---|---|"]
    per_dr = defaultdict(list)
    for t in tcs:
        for f in FIELDS:
            for dr, item in PAT.findall(t[f]):
                per_dr[dr].append(t["tc_title"])
    tot = 0
    for dr in sorted(per_dr, key=lambda s: int(s.split("ICS")[1])):
        L.append(f"| {dr} | {len(per_dr[dr])} | {len(set(per_dr[dr]))} |")
        tot += len(per_dr[dr])
    L.append(f"| **合計** | **{tot}** | **{len({t['tc_title'] for t in tcs for f in FIELDS if PAT.search(t[f])})}** |")

    L += ["", "## §6 `specification_reference` 之錨分佈", "",
          "| 文件 | 條數 | 相異 ObjectID 數 |", "|---|---|---|"]
    fam = defaultdict(set)
    cnt = Counter()
    for t in tcs:
        for line in t["specification_reference"].split("\n"):
            doc, oid = line.split("-")
            fam[doc].add(oid)
            cnt[doc] += 1
    for doc in sorted(fam):
        L.append(f"| {doc} | {cnt[doc]} | {len(fam[doc])} |")

    L += ["", "## §7 驗證強度自評（**執行層判斷**）", "",
          "判準 —— **強**：末步之主錨可單獨判定通過與否，且其執行不依賴未解之佔位。",
          "**弱**：主錨依賴未解之佔位，或以「不變／相同」承載，或其斷言之前提未載。", "",
          "| 批 | tc_title | 強度 | 理由 |", "|---|---|---|---|"]
    for t in tcs:
        s, why = STRENGTH[t["tc_title"]]
        L.append(f'| {t["_batch"]} | {t["tc_title"]} | **{s}** | {why} |')
    sc = Counter(STRENGTH[t["tc_title"]][0] for t in tcs)
    L += ["", f"**強 {sc['強']} 條／弱 {sc['弱']} 條**。", ""]

    L += ["## §8 出貨判斷 —— 假設上游 17 條 DR **全部無回覆**（**執行層判斷**）", "",
          "| 批 | tc_title | 可否現狀出貨 | 理由 |", "|---|---|---|---|"]
    for t in tcs:
        s, why = SHIP[t["tc_title"]]
        L.append(f'| {t["_batch"]} | {t["tc_title"]} | {s} | {why} |')
    ok = sum(1 for t in tcs if not SHIP[t["tc_title"]][0].startswith("**不可"))
    L += ["", f"**可出貨 {ok} 條／不可 {len(tcs) - ok} 條**。", ""]

    (ROOT / "docs/reports/05_pre_delivery_check.md").write_text("\n".join(L) + "\n")
    print(f"寫入 docs/reports/05_pre_delivery_check.md；{len(tcs)} 條，"
          f"強 {sc['強']}／弱 {sc['弱']}，可出貨 {ok}／不可 {len(tcs)-ok}")


if __name__ == "__main__":
    main()
