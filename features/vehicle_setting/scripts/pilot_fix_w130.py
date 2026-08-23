"""W-130（72 包 §6）—— pilot 七項 defect 之全母體修正。

D-1  刪 `pre_conditions` 之架構條目（`The vehicle architecture is Atlantis Mid`）
     —— 其為**來源沿革**（R-VS19″），非前置條件；改記於 `reasoning`
D-4  剝除 `test_item` 上半段吞入之**下一節標題**
D-5  還原 HTML 實體（`&lt;`／`&gt;`／`&amp;`）
D-7  時限（`within a time period of <T…>`）之處置 —— ER 寫可觀察終態，
     時限以 `remarks` 標 `BLOCKED: DR-24′`

**錨點（R-VS54，須可失敗）**：修正前之版本須各自報出違規。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

ARCH = re.compile(r"^\s*\d+\.\s*The vehicle architecture is Atlantis Mid\s*$", re.M)
# 區塊尾端吞入之下一節標題：`1.3.3.3.2 Two Stages … {4859374}`
TAIL_HEAD = re.compile(r"\s*\d+(?:\.\d+)+\s[^\n]*?\{\d{7}\}\s*$")
ENT = {"&lt;": "<", "&gt;": ">", "&amp;": "&", "&quot;": '"', "&apos;": "'"}
TLIMIT = re.compile(r"within a time period of\s*<?T\w+>?", re.I)


def latest() -> list[Path]:
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(groups.items())]


def scan(tcs: list[dict]) -> dict:
    """錨點用之違規計數。"""
    return {
        "D-1 架構條目": sum(1 for t in tcs if ARCH.search(t["pre_conditions"])),
        "D-4 節標題": sum(1 for t in tcs if TAIL_HEAD.search(
            t["test_item"].split("\n\n")[0].strip())),
        "D-5 HTML 實體": sum(1 for t in tcs if any(e in json.dumps(t, ensure_ascii=False)
                                                   for e in ENT)),
        "D-7 時限未標": sum(1 for t in tcs if TLIMIT.search(t["test_item"])
                          and "DR-24" not in str(t.get("remarks", ""))),
    }


def fix(tc: dict) -> dict[str, int]:
    hit = collections.Counter()
    # D-1
    if ARCH.search(tc["pre_conditions"]):
        items = [l for l in tc["pre_conditions"].split("\n") if not ARCH.match(l)]
        tc["pre_conditions"] = "\n".join(
            re.sub(r"^\s*\d+\.", f"{i}.", l, count=1) for i, l in enumerate(items, 1))
        tc["reasoning"] = (str(tc.get("reasoning", "")) +
                           "；來源條文之 `EE Architecture` 為 Atlantis Mid —— "
                           "依 R-VS19″ 其為**來源沿革**而非適用性，"
                           "依 72 包 §2 之 D-1 自 `pre_conditions` 刪除，記於此")
        hit["D-1"] += 1
    # D-4
    up, _, lo = tc["test_item"].partition("\n\n")
    up2 = up.strip()
    while TAIL_HEAD.search(up2):
        up2 = TAIL_HEAD.sub("", up2)
        hit["D-4"] += 1
    if up2 != up.strip():
        tc["test_item"] = up2 + "\n\n" + lo
    # D-5
    for k in ("test_item", "pre_conditions", "test_procedure", "expected_result"):
        v = tc[k]
        for e, c in ENT.items():
            if e in v:
                v = v.replace(e, c)
                hit["D-5"] += 1
        tc[k] = v
    # D-7
    if TLIMIT.search(tc["test_item"]) and "DR-24" not in str(tc.get("remarks", "")):
        tc["remarks"] = ((str(tc.get("remarks", "")) + "；") if tc.get("remarks") else "") \
            + "BLOCKED: DR-24′ —— 時限之上限值待覆，ER 只寫可觀察終態"
        hit["D-7"] += 1
    return hit


def main() -> None:
    before = collections.Counter()
    after = collections.Counter()
    total = collections.Counter()
    print("| batch | 條數 | D-1 | D-4 | D-5 | D-7 |")
    print("|---|---:|---:|---:|---:|---:|")
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        pre = scan(d["tcs"])
        for k, v in pre.items():
            before[k] += v
        c = collections.Counter()
        for tc in d["tcs"]:
            c.update(fix(tc))
        post = scan(d["tcs"])
        for k, v in post.items():
            after[k] += v
        total.update(c)
        if c:
            d["revision"] = ("W-130（46 輪）：pilot 七項 defect 之全母體修正 —— "
                             "D-1 刪架構前置條件／D-4 剝節標題／D-5 還原 HTML 實體／"
                             "D-7 時限改 remarks 標 BLOCKED")
            out = FEAT / "generated" / f"{name}_v{ver + 1}.json"
            out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
        print(f"| `{name}` | {len(d['tcs'])} | {c['D-1']} | {c['D-4']} | "
              f"{c['D-5']} | {c['D-7']} |")
    print(f"\n**修正合計**：D-1 {total['D-1']}／D-4 {total['D-4']}／"
          f"D-5 {total['D-5']}／D-7 {total['D-7']}")
    print("\n錨點（修正前 vs 修正後）")
    print("| 項 | 修正前 | 修正後 | 判 |")
    print("|---|---:|---:|---|")
    for k in before:
        ok = before[k] > 0 and after[k] == 0
        print(f"| {k} | {before[k]} | {after[k]} | "
              f"{'PASS，可失敗' if ok else ('無標的' if before[k] == 0 else '⚠')} |")


if __name__ == "__main__":
    main()
