"""W-VF64(2) —— pilot #2 之分層取樣（R-VF72 二）。

**依 R-VF61 二，分層取樣得偏離選池序**（對 R-VS58 之明示例外，僅適用 pilot 批）。

R-VF72 二之維度，並具名二處偏離：

  訊號送出型   ≥ 4   （R-VF72 稱「訊號斷言型」，本輪細分為送出／上行二型）
  狀態轉換型   ≥ 1   → **池內 0 條，具名「不存在」**
  值域切換型   ≥ 1   → 池內 1 條，取之
  PROXI 型     ≤ 2   （已由 pilot #1 檢畢，僅為對照）
  **訊號上行型 ≥ 2**  → **R-VF72 未列**：其為本輪分類修正後方浮現之形態
                        （124 條，佔池 20%），同屬未檢。**具名為增列。**
  其他         1     → 11 條之未歸類者，取 1 以查其性質
  writability  W1 ≥ 1（池中 W1 僅存於 PROXI 型，故其必自該型出）
  Priority     P0／P1／P2 各 ≥ 1
  Test Set     同一不超過 2

輸出：data/_vf230_pilot2_sel.json
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUOTA = [("訊號送出型", 4), ("訊號上行型", 2), ("PROXI 型", 2),
         ("設定顯示與修改型", 2)]


def main() -> None:
    rows = json.loads((ROOT / "data" / "_vf230_forms.json")
                      .read_text(encoding="utf-8"))["rows"]
    # **排除 pilot #1 之十條** —— 同一 leaf 不得於二 pilot 重複，
    # 否則其第二次之通過不構成新形態之證據（首版未排除，seq 259 命中
    # `PowerLiftgate/TailgateAlert-016`，其已為 pilot #1 之 seq 238）。
    done = {t["leaf_id"] for t in json.loads(
        (ROOT / "generated" / "vf230_pilot1_v4.json").read_text(encoding="utf-8"))["tcs"]}
    rows = [r for r in rows if r["leaf_id"] not in done]
    print(f"池 {len(rows)}（已扣 pilot #1 之 {len(done)} 條）")
    by_form = defaultdict(list)
    for r in rows:
        by_form[r["form"]].append(r)

    # **無可測內容者一律排除**（R-VS71 之 W2(a)）—— 其現判 W0 為分級之誤，
    # 見 A-VF21。本輪於選樣端排除，**未改 writability.tsv**（其須重跑全量）。
    rows = [r for r in rows if r["form"] != "無可測內容"]
    by_form = defaultdict(list)
    for r in rows:
        by_form[r["form"]].append(r)
    absent = [f for f in ("狀態轉換型", "值域切換型") if not by_form.get(f)]
    sel, ts_count = [], Counter()

    def take(cands, n, need_pri=None, need_w=None):
        got = []
        for r in cands:
            if len(got) >= n:
                break
            if ts_count[r["test_set"]] >= 2:
                continue
            if need_pri and r["priority"] != need_pri:
                continue
            if need_w and r["writable"] != need_w:
                continue
            if any(x["leaf_id"] == r["leaf_id"] for x in sel + got):
                continue
            got.append(r)
        for r in got:
            ts_count[r["test_set"]] += 1
            sel.append(r)
        return got

    # PROXI：先取 1 條 W1（池中 W1 僅存於此型），再取 1 條 W0
    take(by_form["PROXI 型"], 1, need_w="W1")
    take(by_form["PROXI 型"], 1, need_w="W0")
    # 訊號送出型 4：P0／P1／P2 各 1，餘 1 不限
    for p in ("P0", "P1", "P2"):
        take(by_form["訊號送出型"], 1, need_pri=p)
    take(by_form["訊號送出型"], 1)
    # 訊號上行型 2
    take(by_form["訊號上行型"], 2)
    # 設定顯示與修改型 2（本輪分類修正後方浮現之第六型，R-VF72 未列）
    take(by_form["設定顯示與修改型"], 2)

    # 補足至 10（若某型不足）
    if len(sel) < 10:
        take(by_form["訊號送出型"], 10 - len(sel))

    fdist = Counter(r["form"] for r in sel)
    pdist = Counter(r["priority"] for r in sel)
    wdist = Counter(r["writable"] for r in sel)
    tdist = Counter(r["test_set"] for r in sel)

    print(f"選 {len(sel)} 條")
    print(f"{'seq':>4} {'leaf':44} {'形態':10} {'W':3} {'Pri':4} Test Set")
    for i, r in enumerate(sel):
        print(f"{258+i:4} {r['leaf_id'][:42]:44} {r['form']:10} "
              f"{r['writable']:3} {r['priority']:4} {r['test_set']}")
    print(f"\n形態命中：{dict(fdist)}")
    print(f"Priority：{dict(pdist)}  writability：{dict(wdist)}")
    print(f"Test Set：{dict(tdist)}  最大 {max(tdist.values())}（上限 2）")
    print(f"**不存在之維度**：{absent or '無'}")
    ok = (fdist["訊號送出型"] >= 4 and fdist["PROXI 型"] <= 2
          and wdist["W1"] >= 1 and all(pdist[p] >= 1 for p in ("P0", "P1", "P2"))
          and max(tdist.values()) <= 2)
    print(f"R-VF72 二之約束：{'全部滿足 ✅' if ok else '⚠ 未滿足'}")
    (ROOT / "data" / "_vf230_pilot2_sel.json").write_text(json.dumps(
        {"sel": sel, "form": dict(fdist), "priority": dict(pdist),
         "writable": dict(wdist), "test_set": dict(tdist), "absent": absent},
        ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
