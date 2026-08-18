#!/usr/bin/env python3
"""記載一致性與指代之稽核（21 包 K-3／K-4）。

## 為什麼不是 lint 的閘

lint 之閘要能給出「紅／綠」之判定；本檔之三項掃描**產出的是待判清單** ——
命中不等於錯（`the message specified above` 之內容可能已由別節之逐字引用補上；
`Scenario` 之步數判準對某些流程本來就寬）。
**把待判清單做成閘，會逼人為了轉綠而改對的東西。**

## 三項

| # | 掃描 | 依據 |
|---|---|---|
| K-3 | ER 以**指代詞**引用表格內容而其後無 `a./b./c.` 列舉 | D-3（14 輪）、C-1（20 輪）之同型 |
| K-4a | `design_method` ↔ `input_test_data`／procedure 之實際形態 | C-2（20 輪）之記載矛盾 |
| K-4b | `priority` ↔ `priority_basis` 之措辭 | C-5（20 輪）|

## K-3 之盲區（R-G11，**下放包已先聲明**）

本掃描抓**指代詞**。抓不到「以自然語句概括表格內容而未用指代詞」者 ——
**C-1 之原句 `followed by the applicable examples` 正屬此型**：
`examples` 是複數名詞，句中無 `the rows of`／`described in` 之類。
故掃描結果為**下界**，另以「複數名詞 + 無列舉」之形態人工複讀補足（見 `--plural`）。

Usage:
    python3 scripts/audit_consistency.py            # 三項全跑
    python3 scripts/audit_consistency.py --plural   # K-3 之盲區補足清單
    python3 scripts/audit_consistency.py --self-test  # 方向性案例（R-G7）

## 為什麼需要 `--self-test`（21 輪 §6 第 7 項之自陳缺口）

三項掃描目前皆以「0 處」收尾。**一個永遠 0 處的掃描與一個壞掉的掃描，輸出相同** ——
語料全綠時，掃描本身是死是活看不出來。故每項各備紅／綠兩向案例，
其中**紅向優先取本 feature 真實出現過的形狀**：C-1 之原句（`--plural` 須紅）、
C-5 之 P1 basis 寫「非主路徑分支」（K-4b 須紅）、
TC-047 之無非法操作（K-4a 須紅）；綠向取**曾被誤判為紅者**：
TC-017 之行內逗號列舉、TC-022 之非法性顯示在 ER、
P0 之 basis 寫「防護本身」（v1 因詞表不全而誤紅）。
"""

import argparse
import json
import re
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent

# K-3 —— 指代詞
DEIXIS = re.compile(
    r"\b(the rows? of|the items? in|the info in|the list of|described in|"
    r"specified in|as (?:described|specified|shown) above|listed (?:above|in)|"
    r"the chart|the table)\b", re.I)
SUBLIST = re.compile(r"^\s+[a-z]\.\s", re.M)
# **判準改過一次（R-U37）。** v1 只認 `a./b./c.` 子層 —— 而 TC-017 之列舉是
# **行內逗號分隔**（`Resume Setup, Edit Name, Edit Avatar, …`）。
# 那是已列舉，不是指代。v2：同一 ER 內有 ≥3 個逗號分隔項亦視為已列舉。
INLINE_LIST = re.compile(r"(?:[^,\n]+,){3,}")

# K-3 之盲區補足：複數名詞而無列舉
PLURAL_VAGUE = re.compile(
    r"\b(the applicable \w+|the relevant \w+|the corresponding \w+|"
    r"\w+ examples|the (?:other )?(?:options|items|entries|examples|"
    r"categories|sections))\b", re.I)

# K-4a —— design_method 之形態要求
FORM_RULES = {
    "邊界值分析": ("邊界對（limit 與 limit±1，或界前／界上兩讀）",
                   lambda tc: bool(re.search(r"\d+\s*(?:→|->|,|s|min|"
                                             r"characters|attempts)?\s*(?:→|->|,)",
                                             tc["input_test_data"]))
                   or "→" in tc["input_test_data"]),
    # **詞表補過一次（R-U37，28 包）。** 第三批之三條真狀態轉換被判紅：
    #   `011`（刪除 profile → 現用者改變）、`048-del`（客製化 → 不再是預設）、
    #   `059-03`（自 popup 選另一 profile → 切換）
    # 三者皆造成**持續存在之系統狀態**改變，只是動作詞不在表內。
    # **34 包再補三種**：`save`（存座椅位置改變其歸屬）、
    # `select … Driver Profile`（以 username／avatar 選取即切換）——
    # 三條被判紅之 TC（`117`／`132`／`133`）皆為**真狀態遷移**，
    # 其所改變者為**持續存在之連結或現用者**，只是動作詞不在表內。
    # **未把 `open`／`read` 收進來** —— 那些不改變狀態；
    # 同輪之 `SWE1-HMI-PROF-015`（按鈕 highlight 隨區段開闔）即據此**改判為功能測試**，
    # 而非為了轉綠而放寬詞表。
    "狀態轉換": ("A→B 之狀態變化（procedure 內有造成狀態改變之步驟）",
                 lambda tc: bool(re.search(
                     r"\b(bring the vehicle into motion|activate|deactivate|"
                     r"exit|switch the ignition|disconnect|select memory seat|"
                     r"swap|delete|customize|save)\b",
                     tc["test_procedure"], re.I))
                 or bool(re.search(r"\bselect[^.\n]{0,25}driver profile\b",
                                   tc["test_procedure"], re.I))),
    # v1 只掃 procedure 之關鍵詞，漏掉「選取一個已鎖定之項目」這種寫法
    # （TC-022 之 `Select the greyed-out “Delete Profile” item`、
    #  TC-057 之 `Select Device Manager`）—— 動作本身讀不出它非法，
    # **非法性顯示在 ER**（不被接受／被鎖住）。v2 兩邊都看。
    # **判準補過一次（R-U37，24 包 P-2 之連帶）。**
    # v2 之 ER 側詞表要求 `is blocked` 之類的明說。24 包 P-2 把 TC-070 之 ER3
    # 由全稱之 `any popup … is blocked` 收斂為 `the PU0934 exit popup is not
    # shown` 之後，該條之 design_method（負向測試）遂轉紅 ——
    # **而它仍然是負向測試**：其 procedure 步驟 1「Press the Valet Profile
    # icon」正是對一個**不該生效之操作**的嘗試，ER1「does not open a
    # deactivation flow」即該嘗試**無作用**。
    # 漏的是「嘗試後無作用」這一種 ER 措辭，不是這條 TC 的方法判錯。
    # v3 補之；**未放寬到一般之缺席斷言** —— `no X is shown` 仍不算，
    # 否則 TC-047 那種「到兩個地方看，那裡沒有該控制」會被誤收為負向。
    "負向測試": ("無效輸入或非法操作（procedure 之嘗試，或 ER 明載其被擋／無作用）",
                 lambda tc: bool(re.search(
                     r"\b(attempt|greyed|incorrect|differs|other than)\b",
                     tc["test_procedure"], re.I))
                 or bool(re.search(
                     r"\b(not accepted|does not respond|is blocked|"
                     r"locked out|cannot be opened|not available|"
                     r"is not accessible|does not open|does not initiate)\b",
                     tc["expected_result"], re.I))),
    "情境 / 用例": ("≥3 步或跨 ≥3 功能",
                    lambda tc: len([x for x in tc["test_procedure"].splitlines()
                                    if x.strip()]) >= 3),
    "基礎故障注入": ("注入之故障（input_test_data 或 procedure 明載）",
                     lambda tc: "Fault injected" in tc["input_test_data"]
                     or bool(re.search(r"\b(disconnect|withhold)\b",
                                       tc["test_procedure"], re.I))),
}

# K-4b —— **判準改過一次（R-U37）。**
#
# v1 驗「該級之 basis 是否含該級之關鍵詞」—— 那測的是**用字是否落在我列的詞表裡**，
# 於是 13 條轉紅，其中絕大多數只是我的詞表不夠（`防護本身` 不在 P0 詞表裡，
# `開啟`／`落點` 不在 P2 詞表裡）。**詞表不全不等於記載矛盾。**
#
# C-5 要抓的是**相斥**：basis 用了**別級**之措辭
# （P1 之 basis 寫「非主路徑分支」而條文說 `will always be displayed`）。
# v2：只在 basis 出現**低於本級**之定性詞時轉紅。
LOWER_BAND_WORDS = {
    "P0": re.compile(r"呈現層|回饋|提示音|輔助功能|細節|罕用"),
    "P1": re.compile(r"呈現層|罕用|版面上限"),
    "P2": re.compile(r"核心五類|防線本身|資料遺失風險"),
    "P3": re.compile(r"核心五類|防線本身|資料遺失風險|邊界"),
}


# ── Q-1（25 包）—— **反向**：逐字引自 spec 而**未**加引號者
#
# G18 查的是「引號內之字面值溯不溯得到源」；**它查不到「該加而未加」**。
# 本掃描補其反向：ER 中**引號外**之連續 ≥7 詞若逐字見於被引之節，即列待判。
#
# ## 引號之適用界線（本輪立，25 包 Q-1）
#
# canon §11：顯示文字與指示值（非可點元素）比照 UI 標籤，用雙引號。
# 惟語料中有兩種形態，**現行做法已一致，本輪只是把它寫下來**：
#
# | 形態 | 例 | 加引號？ |
# |---|---|---|
# | **散文中內嵌**之顯示文字 | `TC-075`「The row reads “…”」、`TC-055`、`TC-072` | **是** |
# | **逐列轉錄**之表格內容 | `TC-039` 之 `a.`–`o.`、`TC-013` 之 `a.`–`d.` | 否 —— 列表形式本身即標示其為轉錄 |
#
# 故本掃描**排除子層列舉行**（`a.` / `b.` …）。
# **盲區（R-G11）**：此界線是我讀語料歸納的，非 canon 明文。
# 若分析層認為轉錄列亦須加引號，`TC-039`（15 列）與 `TC-013`（4 列）皆須改。
QUOTE_SPAN = re.compile(r"[“\"]([^”\"]{3,})[”\"]")
SUBLIST_LINE = re.compile(r"^\s+[a-z]\.\s")
NGRAM = 7


def q1_unquoted(rows) -> list:
    import build_batch_context as _B
    hits = []
    for _sec, t in rows:
        cited = [x.strip().replace(_B.SPEC_STEM + "_", "")
                 for x in str(t.get("specification_reference", "")).split("; ")]
        pool = " ".join((_B.spec_body(c) or "") for c in cited)
        pool += " " + " ".join(x["text"] for x in _B.must_carry_for(cited[0]))
        pool = " ".join(pool.split()).lower()
        for line in str(t.get("expected_result", "")).splitlines():
            if SUBLIST_LINE.match(line):
                continue                      # 逐列轉錄，不適用（見上）
            body = QUOTE_SPAN.sub(" ¶ ", line)
            body = re.sub(r"^\s*\d+\.", " ", body)
            words = re.findall(r"[A-Za-z0-9'’.\-]+", body)
            for i in range(len(words) - NGRAM + 1):
                g = " ".join(words[i:i + NGRAM]).lower()
                if g in pool:
                    hits.append((t["tc_id"], _sec, g))
                    break
            else:
                continue
            break
    return hits


# ── T-1（30 包）—— ER 引用之步驟須確有**該物**之記錄或讀取
#
# `TC-101` 之 ER3 寫 `differs from the icon **read in step 1**`，
# 而步驟 1 為 `Read the status bar and **check that a Profile button is
# present**` —— **它讀的是「按鈕在不在」，不是圖示**。
# 測試者執行到步驟 3 會卡住：手上沒有可比對的紀錄。
#
# ## 判準改過一次（R-U37）—— **v1 只查動詞，抓不到本案**
#
# v1 為「該步驟有無 record／read 之動詞」。**`TC-101` 之步驟 1 有 `Read`**，
# 故 v1 判它綠 —— **而它正是本包點名要抓的那一條**。
# 動詞在不代表讀的是同一個東西。
#
# v2 改抓**被比較之物**（`the <X> recorded/read in step N` 之 X）：
#   - X 為**具體物**（`icon`／`order`／`page`）→ 該步驟須提到 X
#   - X 為**泛稱或功能詞**（`value`／`those`／`as`）→ 退回查動詞
# 泛稱之退回是必要的：`the values recorded in step 1` 之步驟 1 寫的是
# `record the two **preferences**` —— **泛稱與具名本就不會字面相同**，
# 對它們要求字面相符會製造一批假紅。
STEP_REF = re.compile(
    r"(?:the\s+)?([A-Za-z][A-Za-z ]{0,28}?)\s+(?:recorded|read|noted)\s+"
    r"(?:in\s+)?steps?\s+(\d+)", re.I)
GENERIC_OBJ = {"value", "values", "one", "ones", "them", "it", "as",
               "those", "these", "that", "this", "same", "both", "all", "any"}
RECORD_ACT = re.compile(r"\b(record|records|note|notes|read|reads)\b", re.I)


def _sing(w: str) -> str:
    return w[:-1] if w.endswith("s") and len(w) > 3 else w


def t1_step_refs(rows) -> list:
    """ER 引用之步驟未建立該基準線者（§5.6：記錄步驟與比較步驟須成對）。"""
    bad = []
    for sec, t in rows:
        proc = [x for x in str(t.get("test_procedure", "")).splitlines()
                if x.strip()]
        for m in STEP_REF.finditer(str(t.get("expected_result", ""))):
            obj = m.group(1).split()[-1].lower()
            i = int(m.group(2))
            line = proc[i - 1] if 1 <= i <= len(proc) else "**該步驟不存在**"
            if obj in GENERIC_OBJ:
                ok = bool(RECORD_ACT.search(line))
                why = "該步驟無記錄／讀取之動作"
            else:
                ok = _sing(obj) in line.lower()
                why = f"該步驟未提及被比較之物「{obj}」"
            if not ok:
                bad.append((t["tc_id"], sec, i, obj, why, line.strip()[:70]))
    return bad


# ── U-1（31 包）—— ER 斷言之 popup 若有多個觸發條件，其分支是否被綁住
#
# `4.1.1` 有**兩句**都指向 `PU1088`：
#   `PU1088 is displayed when settings have been **successfully restored**`
#   `PU1088 is displayed **if HU or TBM do not confirm** complete restoring`
# **同一個 popup，成功與未確認都會出現。**
# 故一條只寫 `PU1088 is displayed` 之 ER，**兩個分支皆通過**（§7 false pass）。
#
# ## 為何列為「待判」而非直接判紅
#
# 綁定分支之方式不只一種：`TC-082` 靠**同一句**併驗回復結果；
# `TC-002` 靠**另一條 ER**（`The head unit does not receive the completion
# confirmation`）＋ procedure 之情境注入。
# **機械判準無法斷定「哪一條 ER 綁住了哪一個分支」** ——
# 若硬判，`TC-002` 那種正確作法會轉紅。故本掃描只負責**縮小人工範圍**：
# 把「ER 斷言了多觸發 popup」者列出來，逐條由人判。
PU_IN_TEXT = re.compile(r"PU[_ ]?(\d{3,4})")


def _pu_triggers() -> dict:
    """spec 全文中每個 PU id 之觸發句（節次, 句）。"""
    import json as _json
    m = _json.loads((FEATURE / "data" / "outline_map.json")
                    .read_text(encoding="utf-8"))
    out = {}
    for sec, v in m.items():
        if sec == "__meta__":
            continue
        for snt in re.split(r"(?<=\.)\s+", v.get("pdf_text") or ""):
            for g in set(PU_IN_TEXT.findall(snt)):
                out.setdefault(f"PU{int(g):04d}", []).append(
                    (sec, " ".join(snt.split())[:120]))
    return out


def u1_multi_trigger(rows) -> list:
    trig = _pu_triggers()
    hits = []
    for sec, t in rows:
        for g in set(PU_IN_TEXT.findall(str(t.get("expected_result", "")))):
            pid = f"PU{int(g):04d}"
            if len(trig.get(pid, [])) > 1:
                hits.append((t["tc_id"], sec, pid, len(trig[pid])))
    return sorted(set(hits))


# ── U-2（31 包）—— **T-1 之反向**：步驟記錄了某物而無任一 ER 引用它
#
# 30 輪自陳：T-1 抓「ER 引用步驟而該步驟未建立基準線」，
# **抓不到反向**（步驟建立了基準線而 ER 從未用它）。本掃描補之。
#
# 命中者有兩種，**處置不同**：
#   **多餘步驟** —— 該記錄本就不必要 → 刪步驟
#   **ER 漏斷言** —— 該記錄是基準線而 ER 忘了比對 → 補 ER
# 掃描只負責找出來；**兩者之分辨要讀條文**（該斷言需不需要基準線）。
#
# **判準寫過一次即錯（R-U37）**：v1 以 `\brecord` 比對，
# 於是把**比較步驟**（`check that it matches the value **recorded** in step 1`）
# 也當成記錄步驟，得 14 處假紅。
# `recorded in step N` 是**回指**，不是記錄動作。v2 排除 `recorded`。
REC_VERB = re.compile(r"\brecord\b(?!ed)", re.I)
REC_OBJ = re.compile(r"\brecord\b(?!ed)\s+(.{2,70}?)"
                     r"(?:$|,|\s+and\s+check|\s+and\s+read)", re.I)
REC_STOP = {"the", "a", "an", "its", "it", "which", "that", "and", "of",
            "for", "two", "three", "them", "was", "is", "are", "both",
            "each", "present", "shown", "under", "test", "new"}


def u2_unused_record(rows) -> list:
    bad = []
    for sec, t in rows:
        proc = [x for x in str(t.get("test_procedure", "")).splitlines()
                if x.strip()]
        er = str(t.get("expected_result", "")).lower()
        for i, line in enumerate(proc, 1):
            if not REC_VERB.search(line):
                continue
            m = REC_OBJ.search(line)
            obj = m.group(1).strip() if m else ""
            nouns = [w for w in re.findall(r"[A-Za-z][A-Za-z-]{2,}", obj)
                     if w.lower() not in REC_STOP]
            if re.search(rf"\bstep\s+{i}\b", er):
                continue
            if any(_sing(w.lower()) in er for w in nouns):
                continue
            bad.append((t["tc_id"], sec, i, obj[:40], line.strip()[:70]))
    return bad


# ── V-1（32 包）—— 條文含時序語者，其 procedure 之動作順序須與之一致
#
# `4.4` 逐字：`**At the start of a new key cycle**, Head Unit will load last
# known Profile **unless** a different Profile is detected or initiated`。
# 覆寫之發生點是 **key cycle 之起始**。
#
# `TC-091` 原序列為「熄火 → 開機（ER1 已斷言 **B active**）→ 按座椅鍵」——
# **覆寫在 ER1 那一刻就已經沒有發生**；其後測到的是「按座椅鍵可切換 profile」，
# 而那是 `004-03` 已覆蓋之行為。**同節之 `TC-090`（key fob）序列是對的。**
#
# ## 為何是「待判」而非「紅」
#
# 順序是否與條文一致，**需讀條文**：
#   `9.7.2` 之 `prior to the deleted one` 是**位置**，不是時間
#   `5.2` 之 `before creating a new one` 在 **popup 文字**裡，不約束測試順序
#   `12.8.2` 之 `prior to activating Valet Mode` 才真的要求「先記錄後啟用」
# **同一個詞，三種身分。** 機械判準分不出來 ——
# 硬判會把 `035`／`003` 那種正確的判成紅。
# 故本掃描只負責**縮小人工範圍**：把被引之節含時序語者列出，逐條由人判。
TIMING = re.compile(
    r"\b(at the start of|before|upon|prior to|as soon as|at the next)\b", re.I)


def v1_timing(rows) -> list:
    import build_batch_context as _B
    hits = []
    for sec, t in rows:
        cited = [x.strip().replace(_B.SPEC_STEM + "_", "")
                 for x in str(t.get("specification_reference", "")).split("; ")]
        body = _B.spec_body(cited[0]) or ""
        words = sorted({m.group(0).lower() for m in TIMING.finditer(body)})
        if words:
            hits.append((t["tc_id"], sec, words))
    return sorted(hits)


# ── W-1（33 包）—— pre-condition 以完成式描述動作結果者
#
# `TC-094` 之 pre-condition 原為 `Every Profile **has been deleted**`，
# 而 4.5 逐字載「全部刪除後車上**恆有**一個預設 profile」——
# **測試開始那一刻該狀態已經是假的**（Driver 1 早已被重建），
# 且其蘊含之結果（車上只剩 Driver 1）**正是該 TC 要驗的東西**。
# §4.4 禁止以受測特性為前提。
#
# ## 為何是「待判」而非「紅」
#
# 完成式之 pre-condition **多數是正當的**，它們描述的是**測試前之佈署**：
#   `093`：`The default Profile has been customized` —— 使刪除後之重建有意義
#   `104`：`The Profile button has been removed` —— 4.6.3 之適用條件本身
#   `005`：`No default Profile has been customized or deleted` —— 起始狀態
# **循環與否，取決於「該狀態是不是本 TC 的 ER 要斷言的東西」** ——
# 那要讀條文與 ER 才知道。硬判會把上列三條正確的判紅。
PERFECT_PRE = re.compile(r"\b(?:has|have|had)\s+been\s+(?:[a-z]+ed|[a-z]+n)\b",
                         re.I)


def w1_perfect_pre(rows) -> list:
    hits = []
    for sec, t in rows:
        for ln in str(t.get("pre_conditions", "")).splitlines():
            if PERFECT_PRE.search(ln):
                hits.append((t["tc_id"], sec, ln.strip()[:78]))
    return hits


# ── X-1（35 包）—— procedure 之動作會觸發**他節所定義**之 popup 而未處理
#
# `TC-128`（5.7）之步驟 2 存座椅位置到**非現用 profile 所連之座椅** ——
# 那正是 5.10.1 之觸發條件，**PU0588 會跳出來問**。
# 而其 procedure 完全沒提 PU0588：測試者會撞上一個未預期之 popup，
# **結果取決於他按了什麼**（選 Yes 則該座椅就會連到現用 profile，與 ER3 相反）。
# §2 之確定性與可重現性不成立。
#
# **兩條條文並不衝突**：5.7 之 `not **automatically**` 是「不經詢問即發生」，
# 5.10.1 是「問過且答 Yes 才發生」。**衝突的是 TC 之寫法。**
#
# ## 判準之收斂（**v1 得 60 處，等於沒有範圍**）
#
# v1 以「popup 觸發句之關鍵詞與 procedure 重疊 ≥3」比對，得 **60 處** ——
# 絕大多數只是**主題重疊**（`valet`／`mode`／`vehicle`／`popup`）。
# **一份 60 筆的待判清單不是縮小範圍，是噪音**；而噪音清單會被略過（R-G9）。
#
# v2 改為**登記表**：逐個 popup 登記其**觸發動作**之 regex 與**成立條件**，
# 兩者皆命中方列待判。登記表是人工的 —— **其盲區即未登記之 popup**（見下）。
POPUP_TRIGGERS = [
    # (popup, 定義節, 觸發動作 regex（掃 procedure）, 成立條件 regex（掃 pre＋proc）, 說明)
    ("PU0588", {"5.10.1", "9.6"},
     r"\bsav\w+\b[^.\n]{0,60}\bmemory seat\b|\bmemory seat\b[^.\n]{0,40}\bsav\w+",
     None, "存座椅位置到非現用 profile 所連之座椅"),
    ("PU0584", {"5.2"}, r"\bcreate\b[^.\n]{0,60}\bProfile\b",
     r"\bfive\b|\bmaximum\b|\bmax\b", "已達 5 個上限時建立 profile"),
    ("PU0626", {"5.13.2"}, r"Clear Personal Data", None, "確認清除個人資料"),
    ("PU0118", {"4.1.1"}, r"Restore Settings to Default", None, "選取回復預設"),
    ("PU0091", {"12.2.1"}, r"Valet Mode button", r"\bmotion\b",
     "行車中按 Valet 鍵"),
    ("PU0833", {"12.8.1"}, r"greyed[- ]out .{0,25}Glove Box Lock", None,
     "按已變灰之手套箱鎖按鈕"),
    ("PU0832", {"12.8.1"}, r"\benter\w*\b[^.\n]{0,30}Valet Mode|Valet Mode button",
     r"Glove Box", "具手套箱鎖之車輛進入 Valet 之提示"),
    ("PU0580", {"5.3.1"}, r"\bselect\b[^.\n]{0,40}Driver Profile\b", None,
     "切換 profile 後之 welcome popup"),
    ("PU0934", {"13.2"}, r"exit Valet Mode|deactivation control", r"SPAAK",
     "SPAAK 情境下自主機嘗試退出"),
]


def x1_unhandled_popup(rows) -> list:
    import build_batch_context as _B
    hits = []
    for sec, t in rows:
        cited = {x.strip().replace(_B.SPEC_STEM + "_", "")
                 for x in str(t.get("specification_reference", "")).split("; ")}
        proc = str(t.get("test_procedure", ""))
        scope = proc + " " + str(t.get("pre_conditions", ""))
        seen = (proc + " " + str(t.get("expected_result", "")) + " "
                + str(t.get("remarks", "")))
        for pid, secs, action, cond, why in POPUP_TRIGGERS:
            if pid in seen or (secs & cited):
                continue          # 已處理，或本來就是該 popup 之 leaf
            if not re.search(action, proc, re.I):
                continue
            if cond and not re.search(cond, scope, re.I):
                continue          # 觸發條件不成立
            hits.append((t["tc_id"], sec, pid, sorted(secs)[0], why))
    return hits


# ── Y-1（36 包）—— §7 配對之宣稱，其被指者是否真是配對之另一半
#
# `TC-121`（5.4）稱其 `only` 之反向「由 `SWE1-HMI-PROF-022` 承擔」，
# **而該 leaf 之 ER 只斷言「切換發生了」，未斷言「沒有進入編輯」** ——
# 一個既切換、又順手開啟編輯分頁之實作，兩條都會過。**該 `only` 無人驗。**
#
# 這是 **A-UP12 之同型**：委派指得到（D-2 過），**但被指者沒有那句話**。
#
# ## 本掃描之機械判準：**配對之兩條須屬同一 leaf 群**
#
# 「被指者之 ER 有沒有那句反向斷言」是語意，機械判不了。
# 但 §7 之配對有一個可測之必要條件：**正反兩條驗的是同一條條文之兩面**，
# 故其 `req_id` 之**基號**應相同（`030-01` ↔ `030-01-neg`、
# `010-01` ↔ `010-02`、`111` ↔ `111-neg`）。
#
# **這個判準抓得到本輪之兩處指錯**：
#   `096`（`009`）稱其反向為 `104`，而 `104` 之 leaf 是 `016`（4.6.3）——
#   正確者為 `105`（`009-neg`）
#   `127`（`030-01`）稱其反向為 `133`，而 `133` 之 leaf 是 `034-03` ——
#   正確者為 `134`（`030-01-neg`）
# **兩處都是我在 tc_id 尚未指派時寫下的號碼。**
#
# 跨 leaf 群之配對**不一定是錯的**（`121` → `022` 即為跨節之正當委派），
# 故列**待判**而非紅。
PAIR_CLAIM = re.compile(
    r"[^。；\n]*(?:正向為|反向為|反向由|對造)[^。；\n]*")
PAIR_ID = re.compile(r"NR1L-UserProfiles-(\d{3})|SWE1-HMI-PROF-([0-9]{3}(?:-[0-9]{2})?)")


def _leaf_base(req: str) -> str:
    """`SWE1-HMI-PROF-030-01-neg` → `030`；用於判定是否同一 leaf 群。"""
    m = re.search(r"PROF-(\d{3})", req or "")
    return m.group(1) if m else ""


def y1_pair_claims(rows) -> list:
    # **被指者一律對全語料解析**，不限傳入之 rows ——
    # 否則掃描一個子集時，指向子集外之 TC 會被靜靜略過（即本掃描要抓的形狀）。
    idx_tc = {}
    try:
        for _s, _t in tcs():
            idx_tc[_t["tc_id"][-3:]] = _t
    except Exception:
        pass
    for _sec, t in rows:
        idx_tc.setdefault(t["tc_id"][-3:], t)
    hits = []
    for sec, t in rows:
        base = _leaf_base(t.get("req_id", ""))
        for fld in ("reasoning", "remarks"):
            for m in PAIR_CLAIM.finditer(str(t.get(fld, "")) or ""):
                snt = " ".join(m.group(0).split())
                for g in PAIR_ID.finditer(snt):
                    num, leaf = g.group(1), g.group(2)
                    tgt = idx_tc.get(num) if num else None
                    tgt_base = _leaf_base(tgt["req_id"]) if tgt else (
                        _leaf_base("PROF-" + leaf) if leaf else "")
                    if not tgt_base:
                        continue
                    if tgt_base != base:
                        hits.append((t["tc_id"], sec, snt[:60], tgt_base, base))
    return hits


def tcs() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append((d["outline"], t))
    return sorted(out, key=lambda x: x[1]["tc_id"])


def k3(rows) -> list:
    hits = []
    for sec, t in rows:
        er = t["expected_result"]
        for m in DEIXIS.finditer(er):
            if SUBLIST.search(er) or INLINE_LIST.search(er):
                continue          # 已有 a./b./c. 子層或行內逗號列舉
            hits.append((t["tc_id"], sec, m.group(0),
                         er[max(0, m.start() - 50):m.end() + 50]
                         .replace("\n", " ")))
    return hits


def k3_plural(rows) -> list:
    hits = []
    for sec, t in rows:
        er = t["expected_result"]
        if SUBLIST.search(er):
            continue
        for m in PLURAL_VAGUE.finditer(er):
            hits.append((t["tc_id"], sec, m.group(0),
                         er[max(0, m.start() - 50):m.end() + 50]
                         .replace("\n", " ")))
    return hits


def k4a(rows) -> list:
    bad = []
    for sec, t in rows:
        key = t["design_method"].split(" (")[0]
        rule = FORM_RULES.get(key)
        if rule and not rule[1](t):
            bad.append((t["tc_id"], sec, key, rule[0]))
    return bad


def k4b(rows) -> list:
    bad = []
    for sec, t in rows:
        pat = LOWER_BAND_WORDS.get(t["priority"])
        m = pat.search(t.get("priority_basis", "")) if pat else None
        if m:
            bad.append((t["tc_id"], sec, t["priority"],
                        f"basis 用了低於本級之措辭「{m.group(0)}」："
                        + t.get("priority_basis", "")[:50]))
    return bad


# ---------------------------------------------------------------- 方向性案例
#
# 每案 = (說明, 掃描名, 假 TC, 期望紅?)。**紅向取本 feature 真實出現過之形狀，
# 綠向取曾被誤判為紅者** —— 後者即兩次判準修正（R-U37）之回歸。

def _tc(**kw) -> dict:
    base = {
        "tc_id": "FAKE-000", "expected_result": "1. NA", "test_procedure": "1. NA",
        "input_test_data": "NA", "design_method": "功能測試 (Functional based ; no specific technique)",
        "priority": "P2", "priority_basis": "呈現層",
        "specification_reference": (
            "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
            "(October_03_2023)_9.1.1"),
    }
    base.update(kw)
    return base


SELF_CASES = [
    # ---- K-3：指代詞而其後無列舉
    ("D-3／C-1 之同型：ER 指代一張表而未列舉 → **須紅**", "k3",
     _tc(expected_result="1. The page is displayed\n2. The categories described in "
                         "the table above are shown"), True),
    ("**TC-017 之形狀**：行內逗號列舉（v1 誤判為指代）→ **須綠**", "k3",
     _tc(expected_result="1. The tab is displayed\n2. The options are listed in the "
                         "Table EDPR1 order: Resume Setup, Edit Name, Edit Avatar, "
                         "Connected Account, Memory Seat, Welcome Pop Up"), False),
    ("已以 §6.1 子層逐列補上（現行 TC-039 之形狀）→ **須綠**", "k3",
     _tc(expected_result="2. The rows of Table PIP1 are shown:\n   a. Screen "
                         "Customization\n   b. Apps\n   c. Media"), False),

    # ---- K-3 盲區補足：複數名詞而無列舉
    ("**C-1 之原句**（無指代詞，故 k3 抓不到）→ `--plural` **須紅**", "k3_plural",
     _tc(expected_result="2. The page reads the intro text followed by the applicable "
                         "examples"), True),
    ("同句已補子層列舉 → **須綠**", "k3_plural",
     _tc(expected_result="2. The applicable examples are shown:\n   a. Screen "
                         "Customization\n   b. Apps"), False),

    # ---- K-4a：design_method ↔ 實際形態
    ("**TC-036 之形狀**：BVA 而 input 只有 limit、無 limit±1 → **須紅**", "k4a",
     _tc(design_method="邊界值分析 (Boundary Value Analysis)",
         input_test_data="Line count per page: 6 (limit)"), True),
    ("BVA 且有邊界對（TC-008 之形狀）→ **須綠**", "k4a",
     _tc(design_method="邊界值分析 (Boundary Value Analysis)",
         input_test_data="Timeout: 29 s → 30 s"), False),
    ("**TC-047 之形狀**：負向而 procedure 與 ER 皆無非法操作 → **須紅**", "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Open the Profile section\n2. Read the option list",
         expected_result="1. The tab is displayed\n2. No Valet control is shown"), True),
    ("**TC-070 之形狀**：嘗試後無作用（`does not open`）→ **須綠**（v2 誤判為紅）",
     "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Press the Valet Profile icon in the status bar\n"
                        "2. Read the screen and check that no path exits",
         expected_result="1. The Valet Profile icon does not open a "
                         "deactivation flow\n2. Valet Mode is still active"), False),
    ("**TC-047 之形狀**：純缺席斷言（`no X is shown`）→ **仍須紅**（判準未放寬到它）",
     "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Open the Profile section\n2. Read the option list",
         expected_result="1. The tab is displayed\n2. No Valet control is shown"), True),
    ("**TC-022 之形狀**：非法性顯示在 **ER** 而非 procedure（v1 誤判為紅）→ **須綠**",
     "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Select the greyed-out “Delete Profile” item",
         expected_result="1. The selection is not accepted"), False),
    ("**TC-099 之形狀**：刪除驅動之狀態遷移 → **須綠**（28 包補詞表）", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Delete Driver Profile A\n"
                        "2. Read the active Profile and check that it changed"),
     False),
    ("**TC-132 之形狀**：save 改變座椅歸屬 → **須綠**（34 包補詞表）", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Change the seat position and save it to the "
                        "memory seat linked to Driver Profile B\n"
                        "2. Read the seat links and check where it belongs"),
     False),
    ("**護欄**：只有開啟／讀取之 procedure 標狀態轉換 → **仍須紅**", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Open the Profile section\n"
                        "2. Read the button and check that it is highlighted"),
     True),
    ("狀態轉換而 procedure 無造成狀態改變之步驟 → **須紅**", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Read the screen\n2. Check the label"), True),
    ("狀態轉換且有 A→B（TC-021 之形狀）→ **須綠**", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Read the list\n2. Bring the vehicle into motion\n"
                        "3. Read the list"), False),
    ("情境／用例而只有 2 步 → **須紅**", "k4a",
     _tc(design_method="情境 / 用例 (Scenario / Use Case)",
         test_procedure="1. Open the tab\n2. Read the screen"), True),
    ("基礎故障注入而未載注入之故障 → **須紅**", "k4a",
     _tc(design_method="基礎故障注入 (Fault Injection)",
         test_procedure="1. Open the tab\n2. Read the screen",
         input_test_data="NA"), True),

    # ---- Y-1：§7 配對之宣稱（36 包）
    ("**TC-096 之原形**：反向宣稱指向他 leaf 群（`009` → `016`）→ **須列入待判**",
     "y1",
     _tc(req_id="SWE1-HMI-PROF-009", tc_id="NR1L-UserProfiles-096",
         remarks="§7 之列舉配對：反向為 `NR1L-UserProfiles-104`"), True),
    ("其更正後之形：指向同一 leaf 群（`009` → `009-neg`）→ **不得列入**", "y1",
     _tc(req_id="SWE1-HMI-PROF-009", tc_id="NR1L-UserProfiles-096",
         remarks="§7 之列舉配對：反向為 `NR1L-UserProfiles-105`"), False),
    ("**護欄**：無配對宣稱之 remarks → **不得列入**", "y1",
     _tc(req_id="SWE1-HMI-PROF-009", tc_id="NR1L-UserProfiles-096",
         remarks="座椅鍵編號為測試設置（J-12）"), False),

    # ---- X-1：跨節 popup 之未處理（35 包）
    ("**TC-128 之原形**：存座椅到他人所連之座椅而未提 PU0588 → **須列入待判**",
     "x1",
     _tc(specification_reference=(
             "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
             "(October_03_2023)_5.7"),
         test_procedure="1. Change the seat position\n2. Save the position to "
                        "the memory seat linked to Driver Profile B\n"
                        "3. Read the seat links and check"), True),
    ("其修正後之形：procedure 已處理 PU0588 → **不得列入**", "x1",
     _tc(specification_reference=(
             "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
             "(October_03_2023)_5.7"),
         test_procedure="1. Change the seat position\n2. Save the position to "
                        "the memory seat linked to Driver Profile B\n"
                        "3. Select No on PU0588\n4. Read the seat links"), False),
    ("**護欄**：觸發條件不成立（未達上限而建立 profile）→ **不得列入**", "x1",
     _tc(specification_reference=(
             "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
             "(October_03_2023)_5.5"),
         pre_conditions="1. Two Driver Profiles exist on the vehicle",
         test_procedure="1. Create one more Driver Profile\n"
                        "2. Read the list and check"), False),

    # ---- W-1：完成式 pre-condition 列入人工判讀（33 包）
    ("W-1：pre 以完成式述動作結果（`has been deleted`）→ **須列入待判**", "w1",
     _tc(pre_conditions="1. Every Profile has been deleted from the head unit"),
     True),
    ("**護欄**：pre 為狀態描述而非完成式（`is active`／`exists`）→ **不得列入**",
     "w1",
     _tc(pre_conditions="1. Two Driver Profiles exist on the vehicle\n"
                        "2. A Driver Profile is active"), False),

    # ---- V-1：被引之節含時序語者列入人工判讀（32 包）
    ("V-1：被引之節含 `at the start of` → **須列入待判**", "v1",
     _tc(specification_reference=(
         "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
         "(October_03_2023)_4.4")), True),
    ("**護欄**：被引之節無時序語 → **不得列入**（否則清單等於全語料）", "v1",
     _tc(specification_reference=(
         "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_"
         "(October_03_2023)_4.2")), False),

    # ---- U-2：步驟記錄之物須被 ER 引用（31 包，T-1 之反向）
    ("**TC-104 之原形**：步驟記錄 state 而 ER 從未引用 → **須紅**", "u2",
     _tc(test_procedure="1. Open the drawer and record its state\n"
                        "2. Open the Profile section\n"
                        "3. Read the button and check its highlight",
         expected_result="1. The button is shown in the drawer\n2. The "
                         "section is open\n3. The button is highlighted"), True),
    ("**其修正後之形**：ER1 記錄、ER3 比對 → **須綠**", "u2",
     _tc(test_procedure="1. Open the drawer and record its state\n"
                        "2. Open the Profile section\n"
                        "3. Read the button and check its highlight",
         expected_result="1. The button is shown and its highlight state is "
                         "recorded\n2. The section is open\n3. The button is "
                         "highlighted, differing from the state recorded in "
                         "step 1"), False),
    ("**護欄**：比較步驟之 `recorded in step N` 不得被當成記錄步驟 → **須綠**",
     "u2",
     _tc(test_procedure="1. Activate Profile A and record the preference\n"
                        "2. Read the preference and check that it matches "
                        "the value recorded in step 1",
         expected_result="1. The preference is recorded\n2. The preference "
                         "matches the value recorded in step 1"), False),

    # ---- T-1：ER 引用之步驟須確有該物之記錄（30 包）
    ("**TC-101 之原形**：ER 比對「步驟 1 所讀之 icon」而該步驟只查按鈕在否 → **須紅**",
     "t1",
     _tc(test_procedure="1. Read the status bar and check that a Profile "
                        "button is present\n2. Activate the other Profile\n"
                        "3. Read the button and check the icon",
         expected_result="1. A Profile button is present\n2. The other "
                         "Profile is active\n3. The icon differs from the "
                         "icon read in step 1"), True),
    ("**其修正後之形**：步驟 1 記錄 icon → **須綠**", "t1",
     _tc(test_procedure="1. Read the status bar and record the Profile "
                        "button icon\n2. Activate the other Profile\n"
                        "3. Read the button and check the icon",
         expected_result="1. The Profile button icon is recorded\n2. The "
                         "other Profile is active\n3. The icon differs from "
                         "the icon recorded in step 1"), False),
    ("**護欄**：泛稱 `values` 而步驟記的是 `preferences` → **須綠**（不得要求字面相符）",
     "t1",
     _tc(test_procedure="1. Activate Driver Profile A and record the two "
                        "preferences\n2. Read them and check",
         expected_result="1. The preferences are recorded\n2. They match "
                         "the values recorded in step 1"), False),
    ("引用之步驟根本不存在 → **須紅**", "t1",
     _tc(test_procedure="1. Read the screen\n2. Check the icon",
         expected_result="1. a\n2. The icon differs from the icon read in "
                         "step 5"), True),

    # ---- Q-1：引號外之逐字引用（25 包）
    ("**TC-075 之原形**：散文中內嵌之逐字顯示文字**未**加引號 → **須紅**", "q1",
     _tc(expected_result="1. The page is displayed\n2. The line reads 8.4inch "
                         "screen size will not show the username and avatar"), True),
    ("同句已加雙引號 → **須綠**", "q1",
     _tc(expected_result="1. The page is displayed\n2. The line reads “8.4inch "
                         "screen size will not show the username and avatar”"), False),
    ("**TC-039／TC-013 之形態**：逐列轉錄之子層行不適用 → **須綠**", "q1",
     _tc(expected_result="2. The rows are shown:\n   a. 8.4inch screen size "
                         "will not show the username and avatar"), False),

    # ---- K-4b：priority ↔ priority_basis 之措辭（測**相斥**，非詞表命中）
    ("**C-5 之形狀**：P1 之 basis 寫「呈現層」→ **須紅**", "k4b",
     _tc(priority="P1", priority_basis="連網配置之呈現層細節"), True),
    ("P0 之 basis 寫「輔助功能」→ **須紅**", "k4b",
     _tc(priority="P0", priority_basis="輔助功能之提示音"), True),
    ("P2 之 basis 寫「核心五類」→ **須紅**（反向：高於本級亦相斥）", "k4b",
     _tc(priority="P2", priority_basis="R-U5 核心五類之一"), True),
    ("**v1 之誤判**：P0 之 basis 寫「防護本身」（詞表無此詞）→ **須綠**", "k4b",
     _tc(priority="P0", priority_basis="啟用之 PIN —— Valet Mode 之防護本身"), False),
    ("P2 之 basis 寫「呈現層」（本級措辭）→ **須綠**", "k4b",
     _tc(priority="P2", priority_basis="變灰之外觀 —— 呈現層"), False),
]

SCANS = {"k3": k3, "k3_plural": k3_plural, "k4a": k4a, "k4b": k4b,
         "q1": q1_unquoted, "t1": t1_step_refs,
         "u2": u2_unused_record, "v1": v1_timing,
         "w1": w1_perfect_pre, "x1": x1_unhandled_popup,
         "y1": y1_pair_claims}


def self_test() -> int:
    ok = 0
    for desc, scan, tc, want_red in SELF_CASES:
        got = SCANS[scan]([("0.0", tc)])
        red = bool(got)
        mark = "PASS" if red == want_red else "**FAIL**"
        ok += red == want_red
        print(f"  {mark} — [{scan}] {desc}: "
              f"{'紅' if red else '綠'}，期望 {'紅' if want_red else '綠'}")
        if red != want_red:
            print(f"      └ 實得 {got}")
    print(f"\n{ok} / {len(SELF_CASES)} directional cases "
          f"{'PASS' if ok == len(SELF_CASES) else 'FAIL'}")
    return 0 if ok == len(SELF_CASES) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plural", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        sys.exit(self_test())

    rows = tcs()
    print(f"語料 {len(rows)} 條\n")

    if a.plural:
        h = k3_plural(rows)
        print(f"## K-3 盲區補足 —— 複數名詞而無列舉：{len(h)} 處\n")
        for tid, sec, w, ctx in h:
            print(f"  {tid} ({sec}) 「{w}」 … {ctx.strip()[:100]}")
        sys.exit(0)

    h = k3(rows)
    print(f"## K-3 —— 指代詞而其後無列舉：{len(h)} 處\n")
    for tid, sec, w, ctx in h:
        print(f"  {tid} ({sec}) 「{w}」 … {ctx.strip()[:100]}")

    b = k4a(rows)
    print(f"\n## K-4a —— design_method ↔ 實際形態：{len(b)} 處待判\n")
    for tid, sec, key, want in b:
        print(f"  {tid} ({sec}) {key} —— 缺 {want}")

    y1 = y1_pair_claims(rows)
    print(f"\n## Y-1 —— §7 配對之宣稱指向他 leaf 群：{len(y1)} 處待判\n")
    for tid, sec, snt, tb, b in y1:
        print(f"  {tid} ({sec}) 本 leaf 群 {b} → 所指者屬 {tb}：「{snt}」")

    x1 = x1_unhandled_popup(rows)
    print(f"\n## X-1 —— 動作會觸發他節之 popup 而 procedure 未處理："
          f"{len(x1)} 處待判\n")
    for tid, sec, pid, psec, why in x1:
        print(f"  {tid} ({sec}) → {pid}（定義於 {psec}）：{why}")

    w1 = w1_perfect_pre(rows)
    print(f"\n## W-1 —— pre-condition 以完成式描述動作結果：{len(w1)} 處待判\n")
    for tid, sec, ln in w1:
        print(f"  {tid} ({sec}) 「{ln}」—— 須人判該狀態是否即本 TC 之 ER 所斷言者")

    v1 = v1_timing(rows)
    print(f"\n## V-1 —— 被引之節含時序語：{len(v1)} 處待判\n")
    for tid, sec, w in v1:
        print(f"  {tid} ({sec}) {w} —— 須人判 procedure 之順序與條文一致否")

    u2 = u2_unused_record(rows)
    print(f"\n## U-2 —— 步驟記錄之物無任一 ER 引用：{len(u2)} 處\n")
    for tid, sec, i, obj, line in u2:
        print(f"  {tid} ({sec}) 步驟 {i} 記錄「{obj}」而 ER 未引用 → 「{line}」")

    u1 = u1_multi_trigger(rows)
    print(f"\n## U-1 —— ER 斷言之 popup 有多個觸發條件：{len(u1)} 處待判\n")
    for tid, sec, pid, n in u1:
        print(f"  {tid} ({sec}) {pid}（spec 內 {n} 句觸發）—— 須人判其 ER 綁不綁得住分支")

    tr = t1_step_refs(rows)
    print(f"\n## T-1 —— ER 引用之步驟未建立基準線：{len(tr)} 處\n")
    for tid, sec, i, obj, why, line in tr:
        print(f"  {tid} ({sec}) 步驟 {i} —— {why} → 「{line}」")

    q = q1_unquoted(rows)
    print(f"\n## Q-1 —— 引號外之逐字引用（≥{NGRAM} 詞）：{len(q)} 處待判\n")
    for tid, sec, g in q:
        print(f"  {tid} ({sec}) 「{g[:70]}」")

    c = k4b(rows)
    print(f"\n## K-4b —— priority ↔ priority_basis 之措辭：{len(c)} 處待判\n")
    for tid, sec, pri, msg in c:
        print(f"  {tid} ({sec}) {pri} —— {msg}")
