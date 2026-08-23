"""W-157（83 包 §3）—— 五項 defect 之全母體掃描。

**本檔只掃不改**，供修正前後之錨點（R-VS54：修正前須報出違規數，
修正後須為 0；兩側皆須有標的）。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches      # noqa: E402
from inscope_w39 import blocks_with_sec       # noqa: E402

BLK = {b["id"]: b for b in blocks_with_sec()}
L2R = {r["swe_id"]: r for r in csv.DictReader(
    (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}


def _steps(s: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", x) for x in (s or "").split("\n") if x.strip()]


def d1(t: dict) -> str | None:
    """procedure 含不可執行之描述性步驟，而 ER 已標 PENDING。"""
    for i, p in enumerate(_steps(t.get("test_procedure", ""))):
        if "a value outside the declared valid set" in p:
            er = _steps(t.get("expected_result", ""))
            if i < len(er) and er[i].startswith("PENDING"):
                return f"procedure step {i + 1} 為描述而非值，ER 已標 {er[i]}"
    return None


def d2(t: dict) -> str | None:
    """pre_condition 與 procedure 重複設定同一配置（§4.5）。"""
    pre = _steps(t.get("pre_conditions", ""))
    proc = _steps(t.get("test_procedure", ""))
    sets = [p for p in proc if p.startswith("Set PROXI")]
    for s in sets:
        m = re.match(r"Set PROXI (\w+)", s)
        key = (m.group(1) if m else "").lower()
        alias = {"hybrid_type": ("electrified", "hybrid", "plug-in"),
                 "vc_veh_line": ("vehicle line",),
                 "driver_side": ("left-hand", "right-hand", "lhd", "rhd"),
                 "stop_start": ("stop-start",)}.get(key, (key,))
        val = re.search(r"=\s*(\d+)", s)
        for j, p in enumerate(pre):
            if not any(a in p.lower() for a in alias):
                continue
            # **收窄（R-VS73 之逐條抽驗所得）**：pre 若自載一個**相異之值**，
            # 其與 procedure 構成「前後轉換」而非重複設定 ——
            # `HeatedSteeringWheelManagement-025`（pre `= 0 (Absent)`／
            # proc `= 1 (Present)`）即此，**不判為 defect**。
            pv = re.search(r"=\s*(\d+)", p)
            if pv and val and pv.group(1) != val.group(1):
                continue
            return f"pre_condition {j + 1} 與 procedure `{s[:40]}` 重複設定 `{key}`"
    return None


def d3(t: dict) -> str | None:
    """ER 為 PENDING 而同序之 procedure 已寫 check target（§6 1:1 不成立）。"""
    proc, er = _steps(t.get("test_procedure", "")), _steps(t.get("expected_result", ""))
    for i, e in enumerate(er):
        if not e.startswith("PENDING") or i >= len(proc):
            continue
        # **收窄（R-VS73 之逐條抽驗所得）**：83 包 §2 之 D-3 判準為
        # 「**不確定在前提**，而步驟之觀察本身可觀察」。
        # `PENDING: DR-15` 者其不確定**即結果本身**（所送之值為何），
        # 為 80 包 §1 所**明令**之形態 —— **不判為 defect**。
        if "DR-15" in e:
            continue
        if re.search(r"\bcheck that\b", proc[i]):
            return f"ER {i + 1} 為 `{e}` 而 procedure {i + 1} 已寫 check target"
    return None


def d4(t: dict) -> str | None:
    """screen_pending = yes 而 ER 為 PENDING —— 最弱斷言未套用。"""
    if str(t.get("screen_pending")) != "yes":
        return None
    er = _steps(t.get("expected_result", ""))
    bad = [i + 1 for i, e in enumerate(er) if e.startswith("PENDING")]
    if bad:
        return f"screen_pending = yes 而 ER {bad} 為 PENDING，最弱斷言未套用"
    return None


def d5(t: dict) -> str | None:
    """test_item 上半段須為條文逐字（R-VS6）；本項只掃 split_flag = true。"""
    if not t.get("split_flag"):
        return None
    qs = re.findall(r"\d{7}", L2R.get(t["leaf_id"], {}).get("reqid_list", ""))
    if not qs or qs[0] not in BLK:
        return None
    clause = "\n".join(BLK[qs[0]]["text"].split("\n")[1:]).strip()
    upper = (t.get("test_item", "") or "").split("\n\n(")[0].strip()
    if upper and upper not in clause:
        n = sum(1 for a, b in zip(upper.split(), clause.split()) if a != b)
        return f"test_item 上半段非條文逐字（首見差異約 {n} 詞）"
    return None


CHECKS = [("D-1", d1), ("D-2", d2), ("D-3", d3), ("D-4", d4), ("D-5", d5)]


def dup_missing(tcs: list[dict]) -> list[tuple[str, str]]:
    """內容逐字相同而未標 duplicate_of（§10.6）。"""
    seen: dict[tuple, list[dict]] = {}
    for t in tcs:
        k = (t["tc_title"], t.get("pre_conditions"), t.get("test_procedure"),
             t.get("expected_result"))
        seen.setdefault(k, []).append(t)
    out = []
    for group in seen.values():
        if len(group) > 1 and not all(g.get("duplicate_of") for g in group[1:]):
            out.append((group[0]["leaf_id"], group[1]["leaf_id"]))
    return out


def scan(files=None) -> dict:
    tcs = []
    for f in (files or latest_batches()):
        for t in json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]:
            tcs.append({**t, "_b": Path(f).name})
    hits = {k: [] for k, _ in CHECKS}
    for t in tcs:
        for k, fn in CHECKS:
            why = fn(t)
            if why:
                hits[k].append((t["leaf_id"], t["_b"], why))
    return {"total": len(tcs), "hits": hits, "dup": dup_missing(tcs)}


def main() -> int:
    r = scan()
    print(f"全母體 {r['total']} 條 —— 五項 defect 之掃描")
    n = 0
    for k, _ in CHECKS:
        h = r["hits"][k]
        n += len(h)
        print(f"  {k}  {len(h):3d}")
        for leaf, b, why in h[:3]:
            print(f"        {leaf}  [{b}]  {why}")
        if len(h) > 3:
            print(f"        … 另 {len(h) - 3} 條")
    print(f"  note 未標 duplicate_of  {len(r['dup'])}  {r['dup']}")
    print(f"  合計 **{n + len(r['dup'])}**")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
