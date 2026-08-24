"""W-VF64(4) —— 621 池之條文形態分類（**逐條讀全文**，非以首句判）。

上繳 V25 §5 第 2 項自承前次以首句判，本輪改為全文掃描。
**分類判準逐字如下**（依序判，先命中者為準）：

  訊號送出型  全文含 `setProperty()`（含 `invoke setProperty()`）
              或 `TELEMATIC_VEHICLE_SETUP` 之訊號賦值
              —— 顧客操作 → HMI **送出**訊號；其可測結果為匯流排上之訊號
  訊號上行型  全文含 `HW supplier shall notify/provide` ＋ `IPC_VEHICLE_SETUP`
              或 `retrieve the <Sig> signal through`
              —— HW **送入**訊號 → HMI 更新；其可測結果為畫面之更新
              **二者之測試形狀不同**：前者以操作為刺激、斷言訊號；
              後者以訊號為刺激、斷言畫面
  狀態轉換型  全文含 `passes to` / `changes from ... to` / `transitions`
              —— 其可測結果為**狀態之遷移**
  值域切換型  全文列舉同一設定之 ≥3 個離散值（`[A]`／`[B]`／`[C]`）
              且無上二者 —— 其可測結果為**值之逐一切換**
  PROXI 型    全文含 `PROXI configuration` 或 `configuration value`
              —— 其可測結果為**設定項之有無**
  其他        以上皆非，**具名不歸類**

輸出：data/_vf230_forms.json
"""
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# **首版之缺陷**：要求 `CarPropertyManager.setProperty()` 之連寫，
# 而條文實為「CarPropertyManager shall **invoke** setProperty()」，
# 致 170 條落入「其他」。**以動詞之呼叫式為準，不以物件.方法之連寫為準。**
SIG_OUT = re.compile(r"setProperty\(\)|TELEMATIC_VEHICLE_SETUP\w*\.[A-Za-z]\w+"
                     r"|TELEMATIC_VEHICLE_SETUP\b.{0,40}signal value")
SIG_IN = re.compile(r"HW supplier shall (notify|provide)|retrieve the \w+ signal "
                    r"through|IPC_VEHICLE_SETUP")
TRANS = re.compile(r"\bpasses to\b|\bchanges from\b.{0,30}\bto\b|\btransitions?\b", re.I)
ENUM = re.compile(r"\[[^\]]{1,40}\]")
PROXI = re.compile(r"PROXI configuration|configuration value|PROXI value", re.I)


NOTE_ONLY = re.compile(r"^\s*Note[:：]|managed in CFTS", re.I)
DISPLAY = re.compile(r"shall (display|default) the .{0,40}(customer )?setting"
                     r"|allow the customer to modify", re.I)


def form_of(text: str) -> str:
    # **無可測內容**（R-VS71 之 W2(a)）—— 其非一種形態，是不可測之標記
    if NOTE_ONLY.search(text):
        return "無可測內容"
    if SIG_OUT.search(text):
        return "訊號送出型"
    if SIG_IN.search(text):
        return "訊號上行型"
    if TRANS.search(text):
        return "狀態轉換型"
    # **PROXI 先於 ENUM** —— 首版之序使雙參數之 PROXI 條文
    # （`retrieve the Hybrid_Type and SRT … PROXI configurations`）
    # 因其方括號 ≥3 而誤歸「值域切換型」。**取得之來源先於值之個數。**
    if PROXI.search(text):
        return "PROXI 型"
    if len({m.group(0) for m in ENUM.finditer(text)}) >= 3:
        return "值域切換型"
    if DISPLAY.search(text):
        return "設定顯示與修改型"
    return "其他"


def main() -> None:
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (ROOT / "docs" / "reports" / "vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    pri = json.loads((ROOT / "data" / "_vf230_priority.json").read_text(encoding="utf-8"))
    prio = {}
    for p in ("P0", "P1", "P2"):
        pass
    # Priority 逐 leaf：自 priority 報告之 pool 序與 dist 無法回推，改重算
    import importlib.util
    sp = importlib.util.spec_from_file_location(
        "pr", ROOT / "scripts" / "vf230_wvf45_priority.py")
    pr = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(pr)

    rows = []
    for leaf in pri["pool"]:
        txt = re.sub(r"\s+", " ", lv[leaf]["desc"].replace("\\n", " "))
        w = wr[leaf]
        title = lv[leaf]["title"].replace("\\n", " ")
        p = ("P0" if (title in getattr(pr, "P0A", {}) or title in getattr(pr, "P0_SAFETY", {}))
             else ("P1" if title in getattr(pr, "P1_SAFETY_PRESENTATION", {})
                   else ("P2" if pr.P2_PAT.search(txt) else "P1")))
        rows.append({"leaf_id": leaf, "form": form_of(txt), "writable": w["writable"],
                     "priority": p, "test_set": w["test_set"], "layer3": title})

    dist = Counter(r["form"] for r in rows)
    print(f"池 {len(rows)} 條之形態分布：")
    for k, v in dist.most_common():
        print(f"  {v:5}  {k}")
    print("\n形態 × writability：")
    x = defaultdict(Counter)
    for r in rows:
        x[r["form"]][r["writable"]] += 1
    for k, c in x.items():
        print(f"  {k:10} {dict(c)}")
    print("\n形態 × Priority：")
    y = defaultdict(Counter)
    for r in rows:
        y[r["form"]][r["priority"]] += 1
    for k, c in y.items():
        print(f"  {k:10} {dict(c)}")
    (ROOT / "data" / "_vf230_forms.json").write_text(
        json.dumps({"rows": rows, "dist": dict(dist)}, ensure_ascii=False, indent=2),
        encoding="utf-8")


if __name__ == "__main__":
    main()
