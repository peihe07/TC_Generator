#!/usr/bin/env python3
"""AD-1（56 包）—— `Test Item` 第二段之**資訊量**。

## 問題

`TI-2` 驗「第二段非僅重複第一段」，**而其比對為字面** ——
`New Profile Setup starts from the All Profiles tab` 與
`Verifies that the New Profile Setup starts from the All Profiles tab`
逐字不同，故 189／189 全綠，**而第二段沒有帶進任何新東西**。

> `TI-2` 忠實地執行了「非僅重複第一段」——
> **它只是不知道「換句話說」也是重複。**

## 代理判準與其門檻 —— **依據先講，不看結果再定**（Q-1 之教訓）

第二段去除 `Verifies that` 與停用詞後之**實詞**，
與第一段之實詞比對，取「**第二段帶進之新實詞數**」為量。

**門檻：新實詞 < 2 者列待判。** 其依據三項，皆為 a priori：

1. **一個新實詞可能只是語法產物** —— 複數（`popup`／`popups`）、
   同一詞之另一形態（`activate`／`activation`）、或冠詞級的名詞。
   **兩個彼此獨立的新實詞，是能承載一件「標題沒說的事」之最小量。**
2. **取計數而非比率**：實詞數在本語料為 4–15，
   比率門檻會**懲罰長句**（同一個新事實，句子越長比率越低）。
   計數與長度無關。
3. **列待判而非轉紅**：「有沒有帶進新資訊」是語意判斷，
   與 AB-1（兩端是否指同一件事）同類 —— 機械判不了（55 輪 §7-3 已具名）。

**被否決之另一選項**：`第二段實詞 ⊆ 第一段實詞`（純子集）。
其太嚴 —— 只抓得到「一個新詞都沒有」者，
而 `173`（`more`／`one`）與 `166`（`same`／`way`）各帶了新詞卻仍是改寫。
**先寫下這一段，再跑。**

## 盲區（R-G11）

1. **以同義詞改寫而實詞不重疊者抓不到。**
   `Welcome popup shown at ignition on` ↔
   `Verifies that a greeting message appears when the key turns` ——
   零重疊，本判準判它「帶進 5 個新實詞」，而它其實什麼也沒帶。
2. **不判新實詞之「重要性」** —— 帶進兩個無關緊要的詞亦會過關。
3. 詞形還原為**去尾 s** 之粗略作法，不處理不規則變化（`is`／`are`）。

Usage:
    python3 scripts/audit_second_segment.py
    python3 scripts/audit_second_segment.py --self-test
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
MIN_NEW_CONTENT_WORDS = 2          # ← 門檻，依據見 docstring

STOP = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on", "at", "for", "with",
    "that", "this", "these", "those", "is", "are", "be", "been", "it", "its",
    "as", "by", "from", "into", "than", "then", "when", "while", "which",
    "verifies", "no", "not", "only", "each", "every", "any", "all", "both",
    "one", "two", "three", "there", "their", "his", "her", "them", "they",
    "does", "do", "did", "has", "have", "had", "was", "were", "so", "if",
    "up", "out", "off", "over", "under", "again", "still", "already", "own",
    "other", "another", "same", "more", "most", "less", "least", "such",
}


def content_words(s: str) -> set:
    ws = re.findall(r"[A-Za-z][A-Za-z0-9'’\-]*", str(s or "").lower())
    out = set()
    for w in ws:
        if w in STOP or len(w) <= 2:
            continue
        out.add(w[:-1] if w.endswith("s") and not w.endswith("ss") else w)
    return out


def parts(test_item: str):
    lines = [x for x in str(test_item or "").splitlines() if x.strip()]
    if not lines:
        return "", ""
    head = lines[0].strip()
    rest = " ".join(x.strip() for x in lines[1:]).strip()
    if rest.startswith("(") and rest.endswith(")"):
        rest = rest[1:-1].strip()
    return head, rest


def corpus() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append(t)
    return out


def audit(rows=None, threshold=MIN_NEW_CONTENT_WORDS) -> list:
    rows = corpus() if rows is None else rows
    hits = []
    for t in rows:
        head, part2 = parts(t.get("test_item", ""))
        if not part2:
            continue
        h, p = content_words(head), content_words(part2)
        new = sorted(p - h)
        if len(new) < threshold:
            hits.append((t.get("tc_id", "?"), len(new), new, head, part2))
    return sorted(hits)


def self_test() -> int:
    ok, cases = True, []

    def case(name, fn, expect_hit):
        nonlocal ok
        cases.append(name)
        got = fn()
        good = bool(got) == expect_hit
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'命中' if got else '未命中'}，期望 "
              f"{'命中' if expect_hit else '未命中'}")
        for g in got[:1]:
            print(f"      └ {g[0]} 新實詞 {g[1]} 個 {g[2]}")

    corp = {t["tc_id"]: t for t in corpus()}

    # ── G-K：先證明它對 56 包點名之三條會叫
    #
    # **三條之原文以字面固定於此**（不讀語料）—— 56 輪已依 AD-1 改寫，
    # 若此處讀現況，改寫一落地 G-K 之證明就跟著消失，
    # 而**判準是否抓得到該病，與該病是否已被治好，是兩件事**。
    ORIG_168 = ("New Profile Setup starts from the All Profiles tab\n"
                "(Verifies that the New Profile Setup starts from the "
                "All Profiles tab)")
    ORIG_173 = ("The same username can be used by two Driver Profiles\n"
                "(Verifies that the same username can be used by more than "
                "one Driver Profile)")
    ORIG_166 = ("Valet Mode welcome popup clears like the other popups\n"
                "(Verifies that the Valet Mode welcome popup clears in the "
                "same way as the other welcome popups)")

    print("## G-K —— 先證明本判準對已知案例會叫（**56 包點名之三條，原文**）\n")
    for n, v in (("168", ORIG_168), ("173", ORIG_173), ("166", ORIG_166)):
        case(f"**56 包所點名之 `{n}` 之原文 → 須命中**",
             lambda v=v, n=n: audit([{"tc_id": f"ORIG-{n}", "test_item": v}]),
             True)

    print("\n## 對照 —— 寫得對者不得命中\n")
    for n in ("165", "164", "167"):
        tid = f"NR1L-UserProfiles-{n}"
        case(f"56 包所舉之正例 `{n}` → 不得命中",
             lambda tid=tid: audit([corp[tid]]), False)

    print("\n## 改寫之回歸 —— 三條改寫後不得再命中\n")
    for n in ("168", "173", "166"):
        tid = f"NR1L-UserProfiles-{n}"
        case(f"`{n}` 之**現況**（AD-1 改寫後）→ 不得命中",
             lambda tid=tid: audit([corp[tid]]), False)

    print("\n## 判準本身\n")
    T = "Welcome popup shown at ignition on"
    case("**逐字換句話說（零新實詞）→ 命中**",
         lambda: audit([{"tc_id": "F-1",
                         "test_item": f"{T}\n(Verifies that the welcome "
                                      f"popup is shown at ignition on)"}]),
         True)
    case("帶進兩個新實詞 → 不命中",
         lambda: audit([{"tc_id": "F-2",
                         "test_item": f"{T}\n(Verifies that the welcome popup "
                                      f"is displayed and cleared later)"}]),
         False)
    case("**門檻之邊界：剛好一個新實詞 → 命中**",
         lambda: audit([{"tc_id": "F-3",
                         "test_item": f"{T}\n(Verifies that the welcome popup "
                                      f"appears at ignition on)"}]), True)
    case("**盲區（R-G11-1）**：全同義改寫而實詞不重疊 → **不命中**（已具名）",
         lambda: audit([{"tc_id": "F-4",
                         "test_item": f"{T}\n(Verifies that a greeting "
                                      f"message appears when the key turns)"}]),
         False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    hits = audit()
    print(f"語料 {len(corpus())} 條；門檻＝新實詞 < "
          f"{MIN_NEW_CONTENT_WORDS}（依據見 docstring，**先定後跑**）\n")
    print(f"待判 {len(hits)} 條\n")
    for tid, n, new, head, p2 in hits:
        print(f"  {tid}  新實詞 {n} 個 {new}")
        print(f"      一段：{head}")
        print(f"      二段：{p2}")
    sys.exit(0)
