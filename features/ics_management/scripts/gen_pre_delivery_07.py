#!/usr/bin/env python3
"""交付前體檢 v2 —— 含**未錨定斷言檢查**（下放包 07 作業 G、R-ICS28(b)）。

取代 `gen_pre_delivery_05.py` 之報告（舊檔與舊報告皆保留，不刪）。

## 未錨定斷言之判準（R-ICS28(b)）

對每條 TC 之**每一行 ER**，判其能否指回：
  (甲) 該條 `specification_reference` 所錨物件之**來源句**（含其所引之
       DBC `VAL_`／LID／DTCs Matrix —— 凡經裁決採認之編碼皆計入）；或
  (乙) **已登之 A-**（如 A-ICS16 之 popup 顯示條件）。
二者皆無者為**未錨定斷言**。

**這是人工判，不是機械輸出。** 本檔以「規則＋具名例外」承載該判斷：
規則涵蓋可歸類者，例外表逐行列出判為未錨定者及其理由。
規則與例外皆寫在本檔內，可逐行覆核 —— 不寫成不可查的黑箱。

### 規則（依序 first-match）
  R1 記錄步驟之對應行（`is recorded`／`is felt`）→ **非斷言**，不判錨
  R2 訊號觀察行（含 `$MESSAGE.Signal$`）→ 已錨（值取自 DBC `VAL_`，
     其路徑經 R-ICS8／R-ICS13／R-ICS14 採認）
  R3 DTC 行（含 `B14DA-2A`）→ 已錨（R-ICS16(c) 採認其具名）
  R4 `"TOUCH SCREEN TO TURN ON"`／`"HU Screen ON"`／`"VOLUME POP_UP"` 等
     **來源句逐字之 token** → 已錨；其中 popup 之**顯示條件**另見 A-ICS16
  R5 螢幕明暗（`screen is dark`／`shows no content`）→ 已錨（R-ICS22(b)：
     HMI 現象為主錨，其與 `[DISP_OFF]`＋`[0% Intensity]` 之對應由該條採認）
  R6 例外表命中 → **未錨定**
  R7 其餘 → 已錨（來源句之直接改寫）

輸出：docs/reports/07_pre_delivery_check.md
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCHES = ["b01", "b02", "b03", "b04", "b05"]
FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
          "expected_result", "test_item", "specification_reference"]
PAT = re.compile(r"PENDING: (DR-ICS\d+) <([^>]+)>")

# 例外表：判為**未錨定斷言**者（逐行具名 ＋ 理由）。E6 之回報對象。
UNANCHORED = {
 ("Knob 2 held stationary", 4):
   "4819582 之來源句為 `the value ... shall be ignored by the receiving components and "
   "no action taken on the value` —— **「不做事」**。本行斷言「畫面內容不變」，"
   "是以一個**可觀察之無變化**承載一個**不可觀察之不作為**；來源句未承諾畫面必然不變。",
 ("Press ignored during stuck condition", 5):
   "4819617 之來源句為 `the HU shall ignore the press request`。本行斷言「HU 狀態與基線相同」"
   "—— 同上之不作為問題；且來源句未載「忽略」之可觀察後果為何。",
 ("Button responsive after release", 5):
   "4819617 之後半為 `until a signal has been received that the button has been released`，"
   "只說「恢復處理」，**未載恢復後必產生可見變化**。本行斷言「HU 狀態改變」逾其所載。",
 ("Knob 2 signals acted on by the HU", 4):
   "4819586 之來源句自帶 **`if any`** —— 規格明示可能無對應畫面。"
   "本行斷言「HU 狀態與步驟 1 不同」，在 `if any` 為真（無對應）時即為 **False Fail**（IN §7）。",
 ("Knob 2 rotated on a scrollable screen", 4):
   "同上之 `if any` 問題（4819586）。本行斷言「畫面內容不同」。",
 ("Knob 2 rotated on a tuner source", 4):
   "同上之 `if any` 問題（4819586）。本行斷言「Entertainment Audio 狀態不同」。",
 ("Enter button pressed", 4):
   "4819555 之來源句自帶 **`if any`**。本行斷言「畫面與步驟 1 不同」，"
   "在無對應畫面時為 False Fail。R-ICS30(b) 已裁「目標畫面未具名維持現狀」，"
   "但**該裁定治的是「不得自行指定畫面名」，未治本行之斷言逾越**。",
}

# 已登之 A- 所涵蓋者（乙類）
LOGGED = {
 ("VOLUME knob rotated clock-wise", 1): "A-ICS16",
 ("VOLUME knob rotated clock-wise", 3): "A-ICS16",
 ("VOLUME knob rotated counter clock-wise", 1): "A-ICS16",
 ("VOLUME knob rotated counter clock-wise", 3): "A-ICS16",
 ("Three detents rotated clock-wise", 1): "A-ICS16",
 ("Three detents rotated clock-wise", 3): "A-ICS16",
}


def classify(title: str, idx: int, line: str) -> tuple[str, str]:
    key = (title, idx)
    if key in LOGGED:
        return "已標明", f"乙類：{LOGGED[key]}（popup 之顯示條件未載，已登異常）"
    if key in UNANCHORED:
        return "**未錨定**", UNANCHORED[key]
    body = re.sub(r"^\d+\.\s*", "", line)
    if re.search(r"\bis recorded\b|\bis felt\b|are recorded", body):
        return "非斷言", "R1 記錄步驟之對應行"
    if "$" in body:
        return "已錨", "R2 訊號觀察行（值取自 DBC `VAL_`，路徑經 R-ICS8／13／14 採認）"
    if "B14DA-2A" in body:
        return "已錨", "R3 DTC 具名（R-ICS16(c) 採認）"
    if re.search(r'TOUCH SCREEN TO TURN ON|HU Screen ON|VOLUME POP_UP', body):
        return "已錨", "R4 來源句逐字之 token"
    if re.search(r"screen is dark|shows no content", body):
        return "已錨", "R5 HMI 現象為主錨（R-ICS22(b)）"
    return "已錨", "R7 來源句之直接改寫"


def main() -> None:
    tcs = []
    for b in BATCHES:
        p = ROOT / "generated" / b / f"{b}_tcs.json"
        if not p.exists():
            continue
        for t in json.loads(p.read_text())["tcs"]:
            t["_batch"] = b
            tcs.append(t)

    L = ["# 交付前體檢 v2 — b01 ~ b05 全 %d 條（2026-08-29）" % len(tcs), "",
         "> 下放包 07 作業 G，依 **R-ICS28(b)**。**取代 `05_pre_delivery_check.md`**",
         "> （舊報告與其產生器皆保留不刪，回溯用）。",
         "> 未錨定斷言之判準、規則與例外表**全部寫在 `scripts/gen_pre_delivery_07.py` 檔頭與常數表**，",
         "> 可逐行覆核 —— 這是人工判，不偽裝成機械輸出。", ""]

    rows = []
    for t in tcs:
        for i, line in enumerate(t["expected_result"].split("\n"), 1):
            v, why = classify(t["tc_title"], i, line)
            rows.append((t["_batch"], t["tc_title"], i, line, v, why))

    c = Counter(r[4] for r in rows)
    L += ["## §1 未錨定斷言檢查 —— 總計", "",
          f"- ER 行總數 **{len(rows)}**（{len(tcs)} 條 TC）",
          f"- **已錨** {c['已錨']}／**已標明**（乙類，指回已登 A-）{c['已標明']}／"
          f"**非斷言**（記錄行）{c['非斷言']}／**未錨定** {c['**未錨定**']}", ""]

    L += ["## §2 【E6】未錨定斷言 —— 逐行具名（**未自行刪改該 ER 行**）", "",
          "| 批 | tc_title | ER 行 | 內容 | 理由 |", "|---|---|---|---|---|"]
    for b, title, i, line, v, why in rows:
        if v == "**未錨定**":
            L.append(f'| {b} | {title} | {i} | {re.sub(chr(94)+chr(92)+"d+.  *", "", line)[:70]} | {why} |')
    L += ["", "**共通形態**：七行分屬兩族 ——",
          "(i) **不作為之可觀察化**（B3／I1／I2）：來源句說「忽略」「不做事」，"
          "TC 以「狀態不變／改變」承載；",
          "(ii) **`if any` 之逾越**（B6／Scroll／Tune／N1）：來源句自帶 `if any`，"
          "即規格明示可能無對應後果，而 TC 斷言必有可觀察之差異 —— **此四行為潛在 FF**（IN §7）。", ""]

    L += ["## §3 已標明者（乙類，指回已登之 A-）", "",
          "| 批 | tc_title | ER 行 | 已登異常 |", "|---|---|---|---|"]
    for b, title, i, line, v, why in rows:
        if v == "已標明":
            L.append(f"| {b} | {title} | {i} | {why.split('：')[1]} |")

    L += ["", "## §4 Test Set／priority／trace 覆蓋", "",
          "| Test Set | 條數 |", "|---|---|"]
    for k, v in sorted(Counter(t["test_set"] for t in tcs).items()):
        L.append(f"| {k} | {v} |")
    L += ["", "| priority | 條數 |", "|---|---|"]
    for k, v in sorted(Counter(t["priority"] for t in tcs).items()):
        L.append(f"| {k} | {v} |")
    L += ["", "| RD | TC 數 |", "|---|---|"]
    cov = Counter(t["req_id"] for t in tcs)
    for i in range(1, 13):
        rid = f"SWE-ICS-{i:03d}"
        L.append(f"| {rid} | {cov.get(rid, 0) or '**0**'} |")

    L += ["", "## §5 佔位分佈（`pending_census.py` 之口徑；**區分缺值與待回填**，R-ICS27(d)）", "",
          "| DR | 佔位處數 | 涉 TC 數 | 態 |", "|---|---|---|---|"]
    per_dr = defaultdict(list)
    for t in tcs:
        for f in FIELDS:
            for dr, item in PAT.findall(t[f]):
                per_dr[dr].append(t["tc_title"])
    STATE = {"DR-ICS4": "**缺值**（CFTS019 版本未確認）",
             "DR-ICS6": "**缺值**（HMI L&F 畫面流未提供）",
             "DR-ICS8": "**缺值**（`$TGW_DISP_STAT$`；b07 作業 C 判 E3，先決不成立）"}
    tot = 0
    for dr in sorted(per_dr, key=lambda s: int(s.split("ICS")[1])):
        L.append(f"| {dr} | {len(per_dr[dr])} | {len(set(per_dr[dr]))} | {STATE.get(dr, '—')} |")
        tot += len(per_dr[dr])
    L.append(f"| **合計** | **{tot}** | | |")
    L += ["", "**b07 後已無「待回填」態之佔位** —— DR-ICS10／DR-ICS12 之 6 處已於作業 B 回填。", ""]

    Path(ROOT / "docs/reports/07_pre_delivery_check.md").write_text("\n".join(L) + "\n")
    print(f"寫入 docs/reports/07_pre_delivery_check.md")
    print(f"  TC {len(tcs)}／ER 行 {len(rows)}")
    print(f"  {dict(c)}")


if __name__ == "__main__":
    main()
