#!/usr/bin/env python3
"""交付前體檢 v3 —— 含**候選篩（每包必跑）＋ 人工複核（每包必做）**。

依 **R-ICS32(c)**：未錨定斷言檢查確立為常設項，二層式 ——
  第一層 **候選篩**：機械，每包必跑。量 ER 行之實詞對「所錨來源句 ＋ 本條
        `test_item`」之涵蓋度；未被涵蓋之實詞即候選。
        **它抓不到「未錨定」，只抓得到「明顯逾越」**，成本近零。
  第二層 **人工複核**：每包必做，不交給腳本。判準與例外表寫在本檔常數區。
理由（upstream-07 §13-3）：b07 之七行全數通過 19 項機檢與逐字比對 ——
機檢抓不到的正是這一類；而語意保留（`if any`、`no action taken`）正則抓不到。

取代 `gen_pre_delivery_07.py` 之報告（舊檔與舊報告皆保留不刪）。

## 候選篩之掃描條件（逐項揭露）
  - 實詞：ER 行小寫化後之 `[a-z]{4,}` token，扣除下列**測試載具詞表**
    （harness vocabulary —— 這些詞屬 TC 之書寫形式，不屬被驗行為）：
      step/steps, check, checked, read, record, recorded, observe, observed,
      value, values, signal, signals, received, receive, trace, supporting,
      observation, state, states, that, this, with, from, into, then, than,
      shall, will, does, been, have, has, is, are, the, and, for, not
  - 來源句：該 TC `specification_reference` 所列每一 ObjectID 之本文，
    CFTS020 取自 `cfts020_probe.parse()`，CFTS022 自 `inputs/` 之 26PI2.5 本抽取
  - 比對面：來源句 ∪ 本條 `test_item`（上半為來源逐字，下半為作者所書之測試目的）
  - 大小寫不敏感；`$MESSAGE.Signal$` 之 token 先剝去 `$` 與 `.`

## 噪音之處置（本包實測後所加）

首版之候選篩對 127 行中 **122 行**命中 —— **一支命中率 96% 之篩等於沒有篩**
（G-D 之形態：永遠紅之閘與沒有閘，行為上相同）。成因為手寫載具詞表太短，
而來源句普遍比 TC 短得多。

改法（**不改判準，只分層**）：對「未涵蓋實詞」計其**跨 TC 之出現數**，
於 **≥ 5 條 TC** 出現者列為**衍生載具詞**（自動導出、逐個印出、可覆核），
自候選中扣除；餘者為**殘餘候選**，即人工複核之實際對象。
門檻 5 之依據：27 條 TC 中出現於 ≥5 條者，其為「本產線之書寫慣用語」
而非「某條特有之逾越」——此為操作型判準，非語意判斷；門檻值可調而其效果可量。
**二數皆印**（原始命中／殘餘候選），不以分層掩蓋原始噪音。
"""
from __future__ import annotations

import html
import importlib.util
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCHES = ["b01", "b02", "b03", "b04", "b05", "b06", "b07"]
FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
          "expected_result", "test_item", "specification_reference"]
PAT = re.compile(r"PENDING: (DR-ICS\d+) <([^>]+)>")
CFTS022 = ROOT / ("inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 "
                  "Functional Specification_20260608-1205.docx")

STOP = set("""step steps check checked read record recorded observe observed
value values signal signals received receive trace supporting observation
state states that this with from into then than shall will does been have
has are the and for not is""".split())

spec = importlib.util.spec_from_file_location("probe", ROOT / "scripts/cfts020_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

# ── 人工複核之判斷（R-ICS32(c) 第二層）────────────────────────────────
# b08 後：if-any 四行已由作業 C 改寫（佔位移至 Pre-Condition，前提排除 `if any`
# 之否定分支），**不再列為未錨定**；不作為三行依 R-ICS32(a) 保留並標弱驗證。
UNANCHORED = {
 ("Knob 2 held stationary", 4):
   "來源句 4819582 為 `no action taken on the value`；本行以「畫面內容不變」承載"
   "一個**不可觀察之不作為**。R-ICS32(a)：保留，標**弱驗證**。",
 ("Press ignored during stuck condition", 5):
   "來源句 4819617 為 `the HU shall ignore the press request`；本行以「狀態不變」承載。"
   "R-ICS32(a)：保留，標**弱驗證**。",
 ("Button responsive after release", 5):
   "來源句只說「恢復處理」，未載恢復後必產生可見變化。R-ICS32(a)：保留，標**弱驗證**。",
}
# b11 新增四條之人工複核（下放包 11 §五-15：新四條須一併納入）
#   · 009「Back button pressed」ER4 —— 其母條 4821704 之 `Depending on what TLM is
#     currently showing` 與 `if any` 同形，生成時即依 b08 作業 C 之處置把佔位置於
#     Pre-Condition，使該條件成為**前提**而非**斷言** → 判已錨。
#   · G2／G3／G9 之 16 行 ER 全為訊號觀察行或按鍵狀態行，無 `if any`／不作為之形，
#     依規則 R2／R7 判已錨，不入例外表。
RESOLVED_B08 = {
 ("Back button pressed", 4),
 ("Knob 2 signals acted on by the HU", 4),
 ("Knob 2 rotated on a scrollable screen", 4),
 ("Knob 2 rotated on a tuner source", 4),
 ("Enter button pressed", 4),
}
LOGGED = {("VOLUME knob rotated clock-wise", 1), ("VOLUME knob rotated clock-wise", 3),
          ("VOLUME knob rotated counter clock-wise", 1),
          ("VOLUME knob rotated counter clock-wise", 3),
          ("Three detents rotated clock-wise", 1), ("Three detents rotated clock-wise", 3)}


def cfts022_objects() -> dict[str, str]:
    xml = zipfile.ZipFile(CFTS022).read("word/document.xml").decode("utf8")
    xml = re.sub(r"</w:p>", "\n", xml)
    lines = html.unescape(re.sub(r"<[^>]+>", "", xml)).split("\n")
    out = {}
    for i, l in enumerate(lines):
        s = l.strip()
        if re.match(r"^\d{7}: \[", s) and i + 1 < len(lines):
            out[s[:7]] = lines[i + 1].strip()
    return out


def words(text: str) -> set[str]:
    t = text.replace("$", " ").replace(".", " ").replace("_", " ").lower()
    return {w for w in re.findall(r"[a-z]{4,}", t)} - STOP


def main() -> None:
    src020 = {o["id"]: o["text"] for o in probe.parse()}
    src022 = cfts022_objects()
    tcs = []
    for b in BATCHES:
        p = ROOT / "generated" / b / f"{b}_tcs.json"
        if p.exists():
            for t in json.loads(p.read_text())["tcs"]:
                t["_batch"] = b
                tcs.append(t)

    screen = []          # 候選篩之輸出（原始）
    verdicts = []        # 人工複核之輸出
    for t in tcs:
        base = set()
        for line in t["specification_reference"].split("\n"):
            doc, oid = line.split("-")
            base |= words((src020 if doc == "CFTS020" else src022).get(oid, ""))
        base |= words(t["test_item"])
        for i, line in enumerate(t["expected_result"].split("\n"), 1):
            cand = sorted(words(re.sub(r"^\d+\.\s*", "", line)) - base)
            if cand:
                screen.append((t["_batch"], t["tc_title"], i, cand))
            key = (t["tc_title"], i)
            if key in UNANCHORED:
                verdicts.append((t["_batch"], t["tc_title"], i, "**未錨定（弱驗證）**",
                                 UNANCHORED[key]))
            elif key in RESOLVED_B08:
                verdicts.append((t["_batch"], t["tc_title"], i, "已錨（b08 改寫後）",
                                 "作業 C 已將佔位移至 Pre-Condition，"
                                 "`if any` 之否定分支由前提排除，差異斷言方為有據"))
            elif key in LOGGED:
                verdicts.append((t["_batch"], t["tc_title"], i, "已標明", "A-ICS16"))

    # 衍生載具詞：未涵蓋實詞中，跨 TC 出現 >= 5 條者
    per_word_tc = defaultdict(set)
    for b, title, i, cand in screen:
        for w in cand:
            per_word_tc[w].add(title)
    DERIVED = {w for w, s_ in per_word_tc.items() if len(s_) >= 5}
    residual = [(b, ti, i, [w for w in cand if w not in DERIVED])
                for b, ti, i, cand in screen]
    residual = [r for r in residual if r[3]]

    L = [f"# 交付前體檢 v3 — b01 ~ b06 全 {len(tcs)} 條（2026-08-29）", "",
         "> 下放包 08 作業 E，依 **R-ICS32(c)** 之二層式常設項。",
         "> **取代 `07_pre_delivery_check.md`**（舊報告與其產生器皆保留不刪）。",
         "> 候選篩之掃描條件、載具詞表與人工複核之例外表，"
         "**全部寫在 `scripts/gen_pre_delivery_08.py` 檔頭與常數區**，可逐行覆核。", "",
         "## §1 第一層 —— 候選篩（機械，每包必跑）", "",
         f"- ER 行總數 **{sum(len(t['expected_result'].split(chr(10))) for t in tcs)}**",
         f"- **原始命中 {len(screen)} 行**（未涵蓋實詞 ≥ 1）",
         f"- 衍生載具詞 **{len(DERIVED)}** 個（跨 ≥ 5 條 TC，自動導出）：",
         "  `" + "`、`".join(sorted(DERIVED)) + "`",
         f"- **殘餘候選 {len(residual)} 行** —— 此為人工複核之實際對象", "",
         "**殘餘率 %d%%**（基線 53%%，R-ICS34(c)：連續三包 > 60%% 須重議門檻）。"
         % (len(residual) * 100 // max(1, sum(len(t['expected_result'].split(chr(10))) for t in tcs))),
         "",
         "> **R-ICS34(d)：篩之命中率不得作為品質指標。** 上列原始命中數與殘餘數"
         "**量的是篩自身之噪音**，不是 TC 之品質；篩只產候選，未錨定之認定仍為人工（§2）。"
         "原始命中率之所以仍列出，是為使門檻之效果可量（R-ICS34(b)：二數必並報，"
         "不得以分層掩蓋原始噪音）。",
         "", "### 殘餘候選（逐行）", "",
         "| 批 | tc_title | ER 行 | 殘餘實詞 |", "|---|---|---|---|"]
    for b, title, i, cand in residual:
        L.append(f'| {b} | {title} | {i} | `{"`、`".join(cand)}` |')

    L += ["", "## §2 第二層 —— 人工複核（每包必做）", "",
          "| 批 | tc_title | ER 行 | 判 | 理由 |", "|---|---|---|---|---|"]
    for b, title, i, v, why in verdicts:
        L.append(f"| {b} | {title} | {i} | {v} | {why} |")
    c = Counter(v[3] for v in verdicts)
    L += ["", f"**未錨定 {c['**未錨定（弱驗證）**']} 行**（b07 為 7 行；"
          f"作業 C 已解 4 行、作業 D 標弱驗證 3 行）；"
          f"已標明（A-ICS16）{c['已標明']} 行。", ""]

    L += ["## §3 Test Set／priority／trace 覆蓋", "", "| Test Set | 條數 |", "|---|---|"]
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

    L += ["", "## §4 佔位分佈", "", "| DR | 佔位處數 | 涉 TC 數 |", "|---|---|---|"]
    per = defaultdict(list)
    for t in tcs:
        for f in FIELDS:
            for dr, _ in PAT.findall(t[f]):
                per[dr].append(t["tc_title"])
    tot = 0
    for dr in sorted(per, key=lambda s: int(s.split("ICS")[1])):
        L.append(f"| {dr} | {len(per[dr])} | {len(set(per[dr]))} |")
        tot += len(per[dr])
    L.append(f"| **合計** | **{tot}** | |")

    Path(ROOT / "docs/reports/08_pre_delivery_check.md").write_text("\n".join(L) + "\n")
    print("寫入 docs/reports/08_pre_delivery_check.md")
    print(f"  TC {len(tcs)}／候選篩命中行 {len(screen)}／人工複核 {dict(c)}")


if __name__ == "__main__":
    main()
