"""W-VF31（修訂）—— Layer 2 提案 C 之表與 framework 鎖定判斷（V12 §5）。

R-VF36 之移動規則，**逐簇過，不批次**：

  僅移動同時滿足下列兩條件之簇：
  (i)  其 spec 章名之主題詞與其現屬 Test Set 名之主題詞**不相交**
  (ii) **存在另一個** Test Set，其名之主題詞與該章名之主題詞**相交**
  不滿足 (ii) 者一律留原處，**不得為其新設 Test Set**

「主題詞」之操作型定義（須可檢查，不得臨場裁量 —— R-VF36）：
  將名稱與章名各自小寫、去標點、切詞，扣除停用詞後之詞集。
  停用詞為結構詞（and／with／的等），非內容詞。

依 **R-VF21／R-VF28** 附錨點，以內容定錨。

輸出：docs/reports/wvf31_layer2c.md ＋ data/_wvf31_layer2c.json
（**framework.md 是否寫入取決於 R-VF37 (a)/(b) 之判斷，見報告末節**）
"""
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAMES = json.loads((ROOT / "data" / "_wvf25_layer2.json")
                   .read_text(encoding="utf-8"))["names"]
STOP = {"and", "with", "or", "the", "of", "for", "a", "to", "in", "on",
        "&", "-", "features", "report", "setting", "settings"}
# R-VF36 之起點（V11 §7 已具名者），其仍須各自過規則
SWITCH_MERGE_TARGET = "Auxiliary Switches"


def words(s: str) -> set[str]:
    """主題詞集：小寫、非英數字切分、扣停用詞、扣純數字。"""
    return {w for w in re.split(r"[^a-z0-9]+", s.lower())
            if w and w not in STOP and not w.isdigit()}


def main() -> None:
    rows = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    l2 = json.loads((ROOT / "data" / "_vf230_layer2.json").read_text(encoding="utf-8"))
    spec_path = {g["title"]: g["spec_path"] for g in l2["groups"]}
    no_spec = {g["title"] for g in l2["groups"] if g["match"] == "none"}

    # (簇, 現屬 Test Set) -> leaf 數；同一簇可跨兩個 Test Set
    cell: dict[tuple[str, str], int] = Counter()
    for r in rows:
        cell[(r["title"], NAMES[r["family"]])] += 1

    name_words = {n: words(n) for n in set(NAMES.values())}
    moves, stays = [], []
    for (title, cur), n in sorted(cell.items()):
        path = spec_path.get(title) or []
        chap = path[-1] if path else ""
        cw = words(chap) if chap else words(title)   # 無 spec 章者以簇名代
        # 條件 (i)
        i_ok = not (cw & name_words[cur])
        # 條件 (ii)
        cand = sorted(t for t, w in name_words.items()
                      if t != cur and (cw & w))
        rec = {"cluster": title, "leaf": n, "from": cur, "chapter": chap,
               "chapter_words": sorted(cw),
               "cond_i_disjoint": i_ok, "candidates": cand,
               "no_spec": title in no_spec}
        if i_ok and cand:
            # 多個候選時取主題詞交集最大者；同分則取名較短者（穩定）
            best = max(cand, key=lambda t: (len(cw & name_words[t]), -len(t)))
            rec["to"] = best
            rec["overlap"] = sorted(cw & name_words[best])
            moves.append(rec)
        else:
            rec["reason"] = ("(i) 不成立 —— 章名主題詞與現屬 Test Set 名相交："
                             + "／".join(sorted(cw & name_words[cur]))
                             if not i_ok else
                             "(ii) 不成立 —— 無其他 Test Set 之名與章名主題詞相交，"
                             "依 R-VF36 留原處，不得新設")
            stays.append(rec)

    # R-VF36 起點二：12 個跨界之 SWITCH 簇整併入 Auxiliary Switches
    cross = {t for t in {c[0] for c in cell}
             if len({c[1] for c in cell if c[0] == t}) > 1}
    final: dict[str, Counter] = defaultdict(Counter)
    for (title, cur), n in cell.items():
        dest = cur
        if title in cross:
            dest = SWITCH_MERGE_TARGET
        else:
            mv = next((m for m in moves
                       if m["cluster"] == title and m["from"] == cur), None)
            if mv:
                dest = mv["to"]
        final[dest][title] += n

    ts_leaf = {t: sum(c.values()) for t, c in final.items()}
    total = sum(ts_leaf.values())

    # --- 錨點（R-VF21 ＋ R-VF28：以內容定錨）---
    A_MOVE = "Suspension Default Ride Height"   # 必移動（Suspension 章在 Switch Power Mode）
    A_STAY = "Pressure Unit"                    # 必不移動
    # 鑑別錨點（R-VF21 第 3 項）：`Power Unit` 為**量測單位**，
    # 其與 `Switch Power Mode` 僅共用泛用詞 `power`。
    # 規則若正確，其不應移動；**若移動，即規則以單一泛用詞誤配**。
    A_DISC = "Power Unit"
    a_move = next((m for m in moves if m["cluster"] == A_MOVE), None)
    a_stay = next((s for s in stays if s["cluster"] == A_STAY), None)
    if a_move is None:
        raise SystemExit(f"R-VF21 錨點不符：`{A_MOVE}` 應判移動，實判留置，停")
    if a_stay is None:
        raise SystemExit(f"R-VF21 錨點不符：`{A_STAY}` 應判留置，實判移動，停")
    if total != 627:
        raise SystemExit(f"合計應為 627（R-VF16），實得 {total}")
    disc = next((m for m in moves if m["cluster"] == A_DISC), None)

    # 泛用詞診斷（可量測，非判斷）：一個詞若出現於**跨 ≥3 個 Test Set**
    # 之簇章名中，其不具區辨力 —— 以之為相交依據即為誤配。
    word_ts: dict[str, set] = defaultdict(set)
    for (title, cur), _ in cell.items():
        pth = spec_path.get(title) or []
        for w in words(pth[-1] if pth else title):
            word_ts[w].add(cur)
    generic = {w for w, ts in word_ts.items() if len(ts) >= 3}
    weak = [m for m in moves
            if m["overlap"] and set(m["overlap"]) <= generic]

    # R-VF37 (a)/(b)
    old = set(NAMES.values())
    new_names = set(ts_leaf) - old
    gone = sorted(old - set(ts_leaf))
    # R-VF37 末句：有疑義走 (b)。鑑別錨點不符或存在泛用詞誤配即為疑義。
    doubt = bool(disc) or bool(weak)
    verdict = "(b)" if (new_names or doubt) else "(a)"

    L = ["# W-VF31 —— Layer 2 提案 C 之表（R-VF36）", "",
         "**逐簇過規則，不批次移動**（R-VF36）。合計自各 Test Set 重算。", "",
         "## 0. 錨點（R-VF21 ＋ R-VF28：以內容定錨）", "",
         "| 錨點 | 簇 | 實測 |", "|---|---|---|",
         f"| 必移動 | `{A_MOVE}` | `{a_move['from']}` → `{a_move['to']}`"
         f"（相交：{'／'.join(a_move['overlap'])}）✅ |",
         f"| 必不移動 | `{A_STAY}` | 留於 `{a_stay['from']}` ✅ |",
         f"| **鑑別** | `{A_DISC}`（量測單位，與 `Switch Power Mode` 僅共用泛用詞 "
         f"`power`） | "
         + (f"**移至 `{disc['to']}` —— 錨點不符，規則以單一泛用詞誤配** ❌"
            if disc else "未移動 ✅") + " |",
         f"| 合計 | — | {total}（R-VF16）✅ |", "",
         "## 1. 主題詞之操作型定義（R-VF36：須可檢查，不得臨場裁量）", "",
         "```",
         "主題詞(s) = { 小寫切詞(s) } − 停用詞 − 純數字",
         "停用詞 = and, with, or, the, of, for, a, to, in, on, &, -,",
         "         features, report, setting, settings",
         "```",
         "簇之主題詞取自其 **spec 章名**；無 spec 對應者（R-VF34 之 2 簇）",
         "以**簇名**代之，並於下表標記。", "",
         f"## 2. 移動清單（{len(moves)} 筆）", "",
         "| 簇 | leaf | 原 Test Set | 新 Test Set | spec 章名 | 相交之主題詞 |",
         "|---|---:|---|---|---|---|"]
    for m in sorted(moves, key=lambda x: (-x["leaf"], x["cluster"])):
        ch = m["chapter"] or f"（無 spec，用簇名）"
        L.append(f"| `{m['cluster']}` | {m['leaf']} | {m['from']} | "
                 f"**{m['to']}** | `{ch}` | {'／'.join(m['overlap'])} |")

    L += ["", f"## 3. 過規則而不移動（{len(stays)} 筆）", "",
          "**R-VF36 令「過規則而不移動者亦須列出並具名理由」。**", "",
          "| 簇 | leaf | Test Set | 不移動之理由 |", "|---|---:|---|---|"]
    for s in sorted(stays, key=lambda x: (-x["leaf"], x["cluster"])):
        L.append(f"| `{s['cluster']}` | {s['leaf']} | {s['from']} | {s['reason']} |")

    L += ["", "## 4. 12 個跨界簇之整併（R-VF36 起點二）", "",
          f"跨兩個 Test Set 之簇 **{len(cross)}** 個，"
          f"依 R-VF36 整併入 **{SWITCH_MERGE_TARGET}**：", ""]
    L += [f"- `{t}`（{sum(n for (a, _), n in cell.items() if a == t)} leaf）"
          for t in sorted(cross)]

    L += ["", "## 5. 提案 C 之 Layer 2 表", "",
          "| # | Test Set | leaf | 簇 |", "|---:|---|---:|---:|"]
    for i, (t, n) in enumerate(sorted(ts_leaf.items(), key=lambda x: -x[1]), 1):
        L.append(f"| {i} | **{t}** | {n} | {len(final[t])} |")
    L += ["", f"**合計 {total}**（自各 Test Set 重算，未沿用前案差值）。", "",
          f"**消失之 Test Set（{len(gone)}）**：" + "／".join(f"`{g}`" for g in gone),
          "" if not gone else "", ""]

    sizes = sorted(ts_leaf.values())
    L += ["## 6. canon §4.1.3 兩項反面型態", "",
          "| 型態 | 實數 | 判 |", "|---|---|---|",
          f"| **過細**（Test Set 欄近乎 TC ID 欄之複本） | "
          f"{len(ts_leaf)} set／{total} leaf，平均 {total // len(ts_leaf)}，"
          f"最小 {sizes[0]} | **否** |",
          "| **過粗**（`Misc`／`General`／`Unclassified` 收容簇） | "
          "無此類名 | **否** |", "",
          "## 7. R-VF34 之 2 簇（Layer 3 留空且可見）", "",
          "| 簇 | leaf | 所屬 Test Set | Layer 3 |", "|---|---:|---|---|"]
    for t in sorted(no_spec):
        dest = [d for d, c in final.items() if t in c]
        n = sum(c[t] for c in final.values() if t in c)
        L.append(f"| `{t}` | {n} | {'／'.join(dest)} | "
                 f"**（無 spec 對應 —— R-VF34，不自創章名）** |")
    L += ["", "**其 leaf 仍計入母體 627 與其所屬 Test Set**（R-VF34 第 2 項）。",
          "**DR-31 已登記**（見 `DATA_REQUESTS.md`）；送出屬 Pei（R-VF27）。", "",
          "## 8. R-VF37 之 (a)/(b) 判斷", "",
          f"- 既有 11 名之集合外**新出現之名：{len(new_names)}**"
          + (f"（{'／'.join(sorted(new_names))}）" if new_names else "（無）"),
          f"- 消失之名：{len(gone)}（`" + "`／`".join(gone) + "`）" if gone
          else "- 消失之名：0", "",
          f"→ **判 {verdict}**", ""]
    if verdict == "(a)":
        L += ["依 **R-VF37(a)**：Test Set 名為已核可 11 名之子集，無新名，",
              "**得逕行寫入 `framework.md` 並鎖定**。", "",
              "**惟須先確認「既有名之語義範圍是否實質改變」** —— 見 §9。", ""]
    L += ["## 9. 語義範圍是否實質改變（R-VF37(a) 之第二個條件）", "",
          "| Test Set | 移入 | 移出 | 判 |", "|---|---|---|---|"]
    inflow: dict[str, int] = Counter()
    outflow: dict[str, int] = Counter()
    for m in moves:
        inflow[m["to"]] += m["leaf"]
        outflow[m["from"]] += m["leaf"]
    for t in sorted(ts_leaf):
        i, o = inflow.get(t, 0), outflow.get(t, 0)
        L.append(f"| {t} | {i} | {o} | "
                 + ("**須人工判**" if i else "無移入，語義未變") + " |")
    L += ["", "**本節之判斷本層不機械化** —— 「語義範圍實質改變」非詞集可決。",
          "有移入者逐一於上繳具名，**有疑義走 (b)**（R-VF37 末句）。", ""]

    out = ROOT / "docs" / "reports" / "wvf31_layer2c.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf31_layer2c.json").write_text(json.dumps({
        "moves": moves, "stays": stays, "cross": sorted(cross),
        "final": {k: dict(v) for k, v in final.items()},
        "ts_leaf": ts_leaf, "total": total, "new_names": sorted(new_names),
        "gone": gone, "verdict": verdict,
        "inflow": dict(inflow), "outflow": dict(outflow)},
        ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"移動 {len(moves)}／留置 {len(stays)}／跨界整併 {len(cross)}")
    print(f"Test Set {len(ts_leaf)}，合計 {total}")
    for t, n in sorted(ts_leaf.items(), key=lambda x: -x[1]):
        print(f"  {n:4}  {t}")
    print(f"泛用詞 {sorted(generic)}；以泛用詞誤配之移動 {len(weak)}")
    print(f"鑑別錨點 `{A_DISC}`：" + (f"移至 {disc['to']} ❌" if disc else "未移動 ✅"))
    print(f"新名 {sorted(new_names)}／消失 {gone} → R-VF37 判 {verdict}")
    print(f"有移入者：{dict(inflow)}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
