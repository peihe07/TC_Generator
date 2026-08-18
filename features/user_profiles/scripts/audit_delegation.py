#!/usr/bin/env python3
"""委派之可驗化（23 包 M-2）—— A-UP12 之成因閘。

## 為什麼 A-UP12 不可能被舊閘攔下

`TC-020` 寫「由 **11.3** 承擔」——**指節**。節是一段文字，
「那段文字含不含這個行為」要判讀，故不可測。
G17 驗引用欄有無登記、G18 驗字面值溯不溯得到源 —— **兩者都不讀那句話**。
於是 `TC-020` ↔ `TC-040` 之互指委派兩份記載都通得過，
**覆蓋稽核之分子分母都不會動**。

## 本閘之三項

| 閘 | 判準 | 性質 |
|---|---|---|
| D-1 | 委派句須**指名** leaf id（`SWE1-HMI-PROF-…`）或 tc_id（`NR1L-UserProfiles-…`）| 可測 |
| D-2 | 被指名者存在於 037 之 180 母體或語料內 | 可測 |
| D-3 | 被指名者所屬節之 `pdf_text` 須含**自委派句抽出之關鍵詞** | **啟發式** |

## D-3 不求完備 —— 這一點必須寫在條文裡而不是註腳裡

D-3 擋不住所有假委派。它擋得下的是**已知的那一類**：
`TC-020` → `SWE1-HMI-PROF-109`（11.3）之節文**不含** `connected profile
feature`，故轉紅。**擋得下已知的那一類，即為進步**（23 包原話）。

**盲區（R-G11），逐條具名**：

1. **關鍵詞抽取靠停用詞表**。委派句若以中文轉述而不帶英文術語
   （「由某某承擔那個反面情形」），抽不出關鍵詞 → 本閘**放行**。
   故 D-3 對**無關鍵詞可抽**者一律標黃列入人工清單，不當作綠。
2. **命中不等於承擔**。節文含該關鍵詞，不代表該節**斷言**了那個行為 ——
   可能只是提到。D-3 是必要條件，不是充分條件。
3. **(b) 類（指向未取樣 leaf）之承諾無法由本閘兌現**。
   它只能驗那個 leaf 存在，不能驗它日後真的被生成 ——
   兌現與否須靠第三批開批時之複查（`audit_variant_pairs` 之 `pending` 同理）。

Usage:
    python3 scripts/audit_delegation.py             # 掃語料
    python3 scripts/audit_delegation.py --self-test # 方向性案例
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent

# 委派句 —— **抽取判準改過一次（R-U37）。**
#
# v1 為 `[^。；\n]{0,160}?承擔…` 之非貪婪回看：它取**最短**前綴，
# 於是把剛指名之 leaf id 切在窗外，一批已指名者被誤報為 D-1。
# **判準把自己要找的東西切掉了。**
#
# v2：先切句，再於句內找 `由 … 承擔` 之結構，X 為其間之文字。
# 兩個好處 ——
#   1. 論述句（「指錯承擔者比不指更糟」）無 `由…承擔` 結構，**自然排除**
#   2. X 之範圍明確，指名與否可判
SENT = re.compile(r"[^。；\n]+")
BY_CARRY = re.compile(r"由\s*(?P<x>[^，。；]{1,80}?)\s*(?:之 leaf\s*)?(?:已)?承擔")
# 歷史陳述（「**原**稱由 9.2 承擔」）是在記錄一個已修正之錯誤，不是現行委派。
# 不排除它，22 輪之更正文字本身會把本閘點紅 —— **那會逼人刪掉自陳。**
HISTORIC = re.compile(r"原(?:稱|記|本|為|記載為|記為)")
LEAF_RE = re.compile(r"SWE1-HMI-PROF-[0-9]{3}(?:-[0-9]{2})?")
TCID_RE = re.compile(r"NR1L-UserProfiles-[0-9]{3}")
# `TC-039` 之簡寫在本 feature 內無歧義（tc_id 為 001–078），一併認
SHORT_TC = re.compile(r"\bTC-([0-9]{3})\b")

# D-3 之關鍵詞抽取：委派句內之英文術語（≥4 字母），去停用詞。
#
# **停用詞表補過一次（R-U37）。** v1 只去一般虛詞，於是 `TC-028` 之委派句
# 「…由 `SWE1-HMI-PROF-097`（9.5.2）承擔，兩者之 **pre-condition** 互斥」
# 抽出唯一術語 `pre-condition` —— 它是**方法學詞彙**，spec 節文當然不會有，
# 於是一個**正確**之委派被判為假委派。
# 複核 9.5.2 之節文（`If the active Profile was **not** previously linked…`）
# 確認該委派成立。**紅的是判準，不是案例。**
# v2 併去方法學詞彙；去完若無術語可抽，落**黃**（人工清單），不落綠也不落紅。
STOP = {"the", "and", "for", "with", "that", "this", "will", "from", "have",
        "does", "not", "show", "when", "user", "tab", "leaf", "note", "only",
        # 方法學／流程詞彙 —— 出現在 reasoning 裡是常態，spec 節文裡不會有
        "pre-condition", "preconditions", "pre-conditions", "precondition",
        "reasoning", "remarks", "spec", "leaf。", "batch", "lint", "gate"}
TERM = re.compile(r"[A-Za-z][A-Za-z0-9.'’\-]{3,}")


def rows() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append((t["tc_id"], d["outline"], t.get("req_id", ""),
                        d.get("reasoning", ""), t.get("remarks", "")))
    return sorted(out)


def phrase_of(sentence: str) -> str:
    """委派句中**最長之連續英文詞串**（去識別碼與方法學詞）。

    ## 為什麼必須是「詞串」而不是「詞」

    **判準改過兩次（R-U37）。** v2 以單詞比對，而 `TC-020` → `109` 那一案
    之詞（`support`／`connected`／`profile`）**每一個都出現在 11.3 之節文裡**
    （`does not support connectivity`、`The Connected Account line item`）——
    於是 23 包點名要擋下的那一案，v2 判它為綠。
    **單詞比對測不出差別，因為差別在詞的組合上**：
    `does not support connectivity` 與
    `does not support the connected profile feature` 共用三個詞。
    v3 取最長連續英文詞串整串比對；串長 < 3 者無法判 → 落黃。
    """
    # **v4（34 包）—— v3 之抽取會把詞串中間的短詞丟掉。**
    #
    # v3 只收 ≥4 字母之詞（`TERM`），而把 1–3 字母之詞（`to`／`the`／`not`／`of`）
    # 既不收進詞串、也不當成斷點 —— **於是 `switch system to that Profile`
    # 被抽成 `switch system that Profile`**，再拿去逐字比對節文，
    # 節文裡當然沒有，遂誤報為假委派（`TC-121`）。
    #
    # **這個 bug 讓 D-3 之判別力有一部分是意外得來的**：
    # 22 包那個要抓的案例（`does not support the connected profile feature`）
    # 之所以轉紅，**有一半是因為詞串被 v3 打斷**，不全是因為內容不符。
    # v4 修正後複驗：該案例仍紅（`does not support connectivity` 確實不含它），
    # **但這次是為對的理由紅的**。
    #
    # v4：短詞在詞串**已開始**時併入（保持連續），但不得作為詞串之起點。
    runs, cur = [], []
    for tok in re.split(r"([A-Za-z][A-Za-z0-9.'’\-]*)", sentence):
        w = tok.strip()
        if not w:
            continue
        is_word = bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9.'’\-]*", w))
        if is_word and not w.startswith(("SWE1", "NR1L", "PROF")):
            if not cur and (len(w) < 4 or w.lower() in STOP):
                continue          # 不以短詞或停用詞起首
            cur.append(w)
        elif not w.isspace():
            if cur:
                runs.append(cur)
                cur = []
    if cur:
        runs.append(cur)
    runs = [r for r in runs if not all(w.lower() in STOP for w in r)]
    if not runs:
        return ""
    best = max(runs, key=len)
    return " ".join(best) if len(best) >= 3 else ""


def audit(data=None, leaves=None, corpus_ids=None) -> tuple:
    """回傳 (red, yellow)。**黃不是綠** —— 它是人工判讀清單。"""
    data = rows() if data is None else data
    leaves = set(B.leaf_rows()) if leaves is None else leaves
    lrows = B.leaf_rows()
    corpus_ids = ({t[0] for t in rows()} if corpus_ids is None else corpus_ids)
    red, yellow = [], []

    for tid, sec, _rid, reasoning, remarks in data:
        for field, blob in (("reasoning", reasoning), ("remarks", remarks)):
            for sm in SENT.finditer(blob or ""):
                sent = " ".join(sm.group(0).split())
                if "承擔" not in sent:
                    continue
                if HISTORIC.search(sent):
                    continue              # 歷史陳述，非現行委派
                bm = BY_CARRY.search(sent)
                if not bm:
                    continue              # 論述句，無 `由…承擔` 結構
                target_txt = bm.group("x")
                named = (LEAF_RE.findall(target_txt)
                         + TCID_RE.findall(target_txt)
                         + [f"NR1L-UserProfiles-{n}"
                            for n in SHORT_TC.findall(target_txt)])
                # ── D-1
                if not named:
                    red.append(f"D-1 {tid}（{field}）: 委派句未指名 leaf/tc_id "
                               f"→ 「{sent[:70]}」")
                    continue
                for target in named:
                    # ── D-2
                    if target.startswith("SWE1") and target not in leaves:
                        red.append(f"D-2 {tid}: 被指名之 {target} 不在 037 之 "
                                   f"180 母體內")
                        continue
                    if target.startswith("NR1L") and target not in corpus_ids:
                        red.append(f"D-2 {tid}: 被指名之 {target} 不在語料內")
                        continue
                    # ── D-3（啟發式）
                    if not target.startswith("SWE1"):
                        continue          # tc_id 之覆蓋已由語料本身證明
                    tsec = lrows[target]["section"]
                    body = (B.spec_body(tsec) or "").lower()
                    ph = phrase_of(sent)
                    if not ph:
                        yellow.append(f"D-3 {tid} → {target}（{tsec}）: "
                                      f"委派句無 ≥3 詞之英文詞串可比對 —— "
                                      f"**須人工判讀**（盲區 1）→ 「{sent[:56]}」")
                        continue
                    norm = " ".join(ph.lower().split())
                    if norm not in " ".join(body.split()):
                        red.append(f"D-3 {tid} → {target}（{tsec}）: 該節之 "
                                   f"pdf_text 不含委派句之詞串「{ph[:52]}」"
                                   f" —— 疑為假委派")
    return red, yellow


def self_test() -> int:
    ok, n = True, 0
    leaves = set(B.leaf_rows())
    ids = {t[0] for t in rows()}

    def case(name, data, expect_red, expect_yellow=None):
        nonlocal ok, n
        n += 1
        red, yel = audit(data, leaves, ids)
        good = (bool(red) == expect_red)
        if expect_yellow is not None:
            good &= (bool(yel) == expect_yellow)
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"紅{len(red)} 黃{len(yel)}，期望紅{'有' if expect_red else '無'}"
              + ("" if expect_yellow is None
                 else f" 黃{'有' if expect_yellow else '無'}"))
        for b in (red + yel)[:2]:
            print(f"      └ {b}")

    # D-1 —— 指節而不指名（**A-UP12 之原始形狀**）
    case("D-1：委派句寫「由 11.3 承擔」（指節）→ 紅",
         [("FAKE-1", "9.2", "SWE1-HMI-PROF-088",
           "刻意略過：車輛不支援一側由 11.3（CPA1）之 leaf 承擔。", "")], True)
    # D-1 綠向 —— 指名 leaf
    case("D-1：指名 `SWE1-HMI-PROF-090` → 綠",
         [("FAKE-2", "9.3.2", "SWE1-HMI-PROF-091-01",
           "刻意略過：選取受限項目由 `SWE1-HMI-PROF-090`（9.3.1）承擔 —— "
           "bonk 與 message。", "")], False)
    # D-2 —— 指名一個不存在之 leaf
    case("D-2：指名不存在之 `SWE1-HMI-PROF-999` → 紅",
         [("FAKE-3", "9.2", "SWE1-HMI-PROF-088",
           "由 `SWE1-HMI-PROF-999` 承擔 connected profile feature 一側。", "")],
         True)
    # D-3 —— **A-UP12 之那一案**：指名 109（11.3），而該節文無該術語
    case("D-3：`TC-020` → `SWE1-HMI-PROF-109` 之原委派 → 紅（23 包點名之案）",
         [("FAKE-4", "9.2", "SWE1-HMI-PROF-088",
           "車輛不支援一側由 `SWE1-HMI-PROF-109` 承擔，其文為 does not "
           "support the connected profile feature。", "")], True)
    # D-3 綠向 —— 指名 109 而術語確實在 11.3 節文內
    case("D-3：指名 `SWE1-HMI-PROF-109` 且術語為 connectivity → 綠",
         [("FAKE-5", "6.4.1", "SWE1-HMI-PROF-053",
           "連網之顯示規則由 `SWE1-HMI-PROF-109` 承擔 —— connectivity "
           "與 Connected Account line item。", "")], False)
    # **判準修正之回歸**（v1 之誤報）：委派句唯一之英文術語為方法學詞彙
    case("TC-028 之形狀：唯一術語為 `pre-condition` → **黃，不得為紅**",
         [("FAKE-7", "9.5.1", "SWE1-HMI-PROF-096",
           "為什麼這樣切：前置未連結之情形由 `SWE1-HMI-PROF-097`（9.5.2）承擔，"
           "兩者之 pre-condition 互斥。", "")], False, True)
    # 盲區 1 —— 無英文術語可抽 → **黃，不是綠**
    case("盲區 1：委派句全中文、無術語可抽 → **黃（不放行）**",
         [("FAKE-6", "4.1", "SWE1-HMI-PROF-001-01",
           "刻意略過：其反面由 `SWE1-HMI-PROF-047` 承擔。", "")],
         False, True)
    # 現行語料
    red, yel = audit(None, leaves, ids)
    n += 1
    good = not red
    ok &= good
    print(f"  {'PASS' if good else '**FAIL**'} — 現行語料 → 紅{len(red)} 黃{len(yel)}")
    for b in red[:3]:
        print(f"      └ {b}")

    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    red, yellow = audit()
    print(f"語料 {len({r[0] for r in rows()})} 條\n")
    print(f"## 紅 —— {len(red)} 處\n")
    for b in red:
        print(f"  {b}")
    print(f"\n## 黃 —— {len(yellow)} 處（**人工判讀清單，非放行**）\n")
    for b in yellow:
        print(f"  {b}")
    sys.exit(1 if red else 0)
