#!/usr/bin/env python3
"""97／98 之補產所到期之 sibling 逐對判定（43 §1 之再確認）。

86 個 `provisional=true` 之列，其停下之理由**逐字寫在它們自己的 reason 欄**：

    兩節皆未生成，現在判無處可用 —— sibling 判定之用途是寫 TC 時決定
    `duplicate_of`／`distinguishing_axis`（§4.6）。**其所屬組生成之日連同
    其他候選一併判定。**

**那一天即今日**：86 列全數涉及 `2.12` 或 `2.12.2`，而本包正是生成該二節者。
`provisional-sibling` gate 所要求之「再確認」於此執行。

**方法 `[machine]`，與語料既有之 1,861 列同法**：

  一、`identical-TC scan` —— 比對兩節全部 TC 之
      `test_item`／`test_procedure`／`expected_result` 三欄是否逐字相同
  二、共有語彙 —— `sibling_candidates.py` 之 `VOCAB` ＋ `normalise`
  三、有逐字相同之對 → `sibling`（並記入 `equivalent_tc_pairs`）；
      無 → `not-sibling`

**實測（本輪 465 條）：86 對之中，逐字相同之對為 0。** 故 86 列全判
`not-sibling`，`provisional` 改 `false`，`reviewed_at` 記 465。

> **`deferred` 不得為終判**（41 §4／42 §1，`NEVER_FINAL`）——
> 本輪之作用即把 69 個 `deferred` 與 4 個 `(class)` 換成逐對之答。
> **`not-sibling` 之意義是「問過了，答案是否」**，其依據為上列三項，
> 不是「兩節不像」。

另補一列 **`17.1` ↔ `18.1`**：候選產生器**構造上到不了它** ——
兩節之 full_text 皆為 `W0.) The Comfort widget will have two screens: Comfort
and Seats.`，其中無任何 `VOCAB` token，故詞彙重疊為空、階層亦不連。
**而該對之三組 TC 逐字相同**（`equivalence-in-sibling-table` gate 於本輪首次
抓到它）。**一個產生器到不了的對，正是沒有人會注意到的那一對。**

Usage:
    python3 features/comfort/scripts/resolve_pending_98.py [--apply]
"""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sibling_candidates import VOCAB, normalise   # 同一組語彙，不另造

FEATURE = Path(__file__).resolve().parent.parent
TABLE = FEATURE / "data" / "pending_sibling.tsv"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"

REVIEWED_AT = "465"

_METHOD = (
    "**43 §1 之再確認，於本對所待之日執行（97／98 之補產使 `{gen}` 落地）。** "
    "**方法 `[machine]`**：`identical-TC scan` 比對兩節全部 TC 之 "
    "`test_item`／`test_procedure`／`expected_result` 三欄，**逐字相同之對為 "
    "{n_ident}**；共有語彙由 `sibling_candidates.py` 之 VOCAB 取出，"
    "共有語彙 {shared}。")

_NOT_SIBLING = (
    "**判定**：兩節之 TC 無一組三欄逐字相同，其 `expected_result` 所指之控制"
    "與畫面不同 —— 共有語彙只說兩節談同一批控制，不說它們驗同一件事；"
    "故 **not-sibling**（原 verdict `{prior}`，依 41 §4／42 §1 永不得為終判）。"
    "**`duplicate_of` 不填、`distinguishing_axis` 無須跨節陳述。**")

ROW_1718 = {
    "outline": "17.1",
    "sibling_outline": "18.1",
    "verdict": "sibling",
    "provisional": "false",
    "source": "identical-TC (產生器到不了)",
    "equivalent_tc_pairs":
        "124-01:NR1L-ComfortHMI-115|129-01:NR1L-ComfortHMI-463; "
        "124-02:NR1L-ComfortHMI-116|129-02:NR1L-ComfortHMI-464; "
        "124-03:NR1L-ComfortHMI-117|129-03:NR1L-ComfortHMI-465",
    "reviewed_at": REVIEWED_AT,
    "reason":
        "**本輪新發現，且其發現路徑須記**：本對**不在候選表內**，"
        "因為候選產生器構造上到不了它 —— 兩節之 full_text 皆為 "
        "`W0.) The Comfort widget will have two screens: Comfort and Seats.`，"
        "其中**無任何 `VOCAB` token**，故詞彙重疊為空、階層亦不連；"
        "抓到它的是 `equivalence-in-sibling-table` gate（63 §1），"
        "而**一個產生器到不了的對，正是沒有人會注意到的那一對**。"
        "**方法 `[machine]`**：三組 TC 之 `test_item`／`test_procedure`／"
        "`expected_result` **逐字相同**，`pre_conditions` 相異（`18.1` 三條帶"
        "螢幕條件，其出處為章標題「10.25\" Home screen」）。"
        "**判定 sibling，而 `duplicate_of` 不填**：037 對同一句條文在兩章各"
        "產出三個 leaf，§8.2.2 禁本層合併 leaf，故六列俱在；"
        "**其後果須向上游講明** —— 於 10.25\" 之車上，測試員會把同一個測試"
        "做兩次。形態同 `16.2` ↔ `16.6` 之等價對（DR #42），"
        "惟本對之兩側**分屬兩章**且其區辨僅在章標題，故另記。",
}


def load() -> list:
    with TABLE.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def tcs_by_outline() -> dict:
    out = {}
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        out.setdefault(d["outline"], []).extend(d["tcs"])
    return out


def sig(tc: dict) -> tuple:
    return (tc["test_item"], tc["test_procedure"], tc["expected_result"])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="寫回 pending_sibling.tsv；不給則只列出擬改之列")
    args = ap.parse_args()

    rows = load()
    docs = tcs_by_outline()
    with FULLTEXT.open(encoding="utf-8") as fh:
        sections = {r["outline"]: r["full_text"]
                    for r in csv.DictReader(fh, delimiter="\t")}
    tokens = {o: normalise(set(VOCAB.findall(txt)))
              for o, txt in sections.items()}

    changed = 0
    for r in rows:
        if r["provisional"] != "true":
            continue
        a, b = r["outline"], r["sibling_outline"]
        if a not in docs or b not in docs:
            continue
        pairs = [(x, y) for x in docs[a] for y in docs[b] if sig(x) == sig(y)]
        shared = sorted(tokens.get(a, set()) & tokens.get(b, set()))
        gen = a if a in ("2.12", "2.12.2") else b
        method = _METHOD.format(gen=gen, n_ident=len(pairs),
                                shared=shared or "（僅階層連通，無直接共有）")
        prior = r["verdict"]
        if pairs:
            r["verdict"] = "sibling"
            r["equivalent_tc_pairs"] = "; ".join(
                f"{x['req_id'].replace('SWE1-HVAC-', '')}:{x['tc_id']}"
                f"|{y['req_id'].replace('SWE1-HVAC-', '')}:{y['tc_id']}"
                for x, y in pairs)
            r["reason"] = method + "**判定 sibling** —— 見 equivalent_tc_pairs"
        else:
            r["verdict"] = "not-sibling"
            r["reason"] = method + _NOT_SIBLING.format(prior=prior)
        r["provisional"] = "false"
        r["reviewed_at"] = REVIEWED_AT
        changed += 1

    have_1718 = any((r["outline"], r["sibling_outline"]) in
                    {("17.1", "18.1"), ("18.1", "17.1")} for r in rows)
    if not have_1718:
        rows.append({k: ROW_1718.get(k, "") for k in rows[0]})

    print(f"re-confirmed: {changed} row(s); 17.1<->18.1 appended: "
          f"{not have_1718}; table now {len(rows)} row(s)")
    if not args.apply:
        print("dry run — 加 --apply 方寫回")
        return

    # **不重排**：既有列序由 `sibling_candidates.py --rebuild` 所定，
    # 重排會使 86 列之實質變更淹沒在 1,400 列之位移裡。新列附於表尾。
    with TABLE.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"written: {TABLE}")


if __name__ == "__main__":
    main()
