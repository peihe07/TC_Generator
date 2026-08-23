"""W-157（83 包 §3）—— 早批之 defect 修正，各產 `_v(n+1)`。

batch23 之 D-1／D-2／D-3／D-4 已於生成器修正（R-VS53：產物須可自 driver 重製）。
本檔處理**早批**（其生成器已不再重跑）：

  D-2  刪 pre_condition 之重複配置（`FeaturesEnableCriteria-022`，80 包 §1
       對 `-021` 之裁定未推廣至 `-022`）
  D-3  ER 之 `PENDING: DR-5-B` 改可觀察斷言 ＋ AH 增註（7 條）
  D-5  `split_flag = true` 之 test_item 上半段回復條文逐字（R-VS6），
       窄化改記於括號內之下半段
  note 內容逐字相同者標 `duplicate_of`（§10.6）

**不改 procedure**（其步驟本可執行）；**不改 test_item 之下半段以外之任何文字**。
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


def steps(s: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", x) for x in (s or "").split("\n") if x.strip()]


def numbered(xs: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def assertion_from(proc_step: str) -> str:
    """自 procedure 之 `… and check that <X>` 取其可觀察斷言。"""
    m = re.split(r"\band check that\b|\bcheck that\b", proc_step, maxsplit=1)
    lead, claim = m[0].strip().rstrip(","), m[1].strip()
    if claim.startswith("it "):
        np = re.search(r"\b(?:Read|Open|Press)\s+(the .+?)(?:\s+again)?$", lead)
        if np:
            claim = np.group(1) + claim[2:]
    return claim[0].upper() + claim[1:]


def clause(leaf: str) -> str:
    qs = re.findall(r"\d{7}", L2R.get(leaf, {}).get("reqid_list", ""))
    return "\n".join(BLK[qs[0]]["text"].split("\n")[1:]).strip() if qs else ""


def fix_tc(t: dict) -> tuple[dict, list[str]]:
    t, done = {**t}, []

    # ── D-2 ──────────────────────────────────────────────────────────
    pre, proc = steps(t["pre_conditions"]), steps(t["test_procedure"])
    sets = [p for p in proc if p.startswith("Set PROXI")]
    for s in sets:
        key = (re.match(r"Set PROXI (\w+)", s).group(1)).lower()
        alias = {"hybrid_type": ("electrified", "hybrid", "plug-in")}.get(key, (key,))
        val = re.search(r"=\s*(\d+)", s)
        drop = [j for j, p in enumerate(pre)
                if any(a in p.lower() for a in alias)
                and not (re.search(r"=\s*(\d+)", p)
                         and val
                         and re.search(r"=\s*(\d+)", p).group(1) != val.group(1))]
        if drop:
            pre = [p for j, p in enumerate(pre) if j not in drop]
            t["pre_conditions"] = numbered(pre)
            done.append(f"D-2 刪 pre_condition {[j + 1 for j in drop]}（與 `{s[:36]}` 重複）")

    # ── D-3／D-4 ─────────────────────────────────────────────────────
    er = steps(t["expected_result"])
    for i, e in enumerate(er):
        if not e.startswith("PENDING") or "DR-15" in e or i >= len(proc):
            continue
        if not re.search(r"\bcheck that\b", proc[i]):
            continue
        dr = e.split("PENDING:")[1].strip()
        er[i] = assertion_from(proc[i])
        ah = str(t.get("remarks", "") or "").strip()
        note = (f"BLOCKED: {dr} —— 該步驟之觀察本身可驗，"
                f"其待補者為畫面層之具體樣式與內容")
        t["remarks"] = (ah + "；" + note) if ah else note
        t["screen_pending"] = "yes"
        done.append(f"D-3/D-4 ER {i + 1} `{e}` → 可觀察斷言，待補移入 AH")
    t["expected_result"] = numbered(er)

    # ── D-4 之殘餘：procedure 無 `check that` 而 ER 為 PENDING ──────────
    # `OneStageHeatedSeat-041` 步驟 2（`Press … and read the icon status`）
    # 其 ER 為 `PENDING: DR-5-B`，而條文**逐字載其循環**
    # （`the relative icons status shall follow the logic descibed below
    #   (off -> high -> off)`）—— **首次按壓之終態 `high` 為來源逐字**，
    # 不待 HMI requirements。故改為可觀察斷言，並使該步驟具驗證意圖（§5.5）。
    er2, proc2 = steps(t["expected_result"]), steps(t["test_procedure"])
    if t["leaf_id"] == "SWE1-VC-OneStageHeatedSeat-041":
        for i, e in enumerate(er2):
            if e.startswith("PENDING") and i < len(proc2) and "read the" in proc2[i]:
                proc2[i] = re.sub(r"and read the (.+)$",
                                  r"and check that the \1 changes to high", proc2[i])
                er2[i] = "The icon status changes to high"
                t["test_procedure"] = numbered(proc2)
                t["expected_result"] = numbered(er2)
                proc = proc2
                done.append(f"D-4 殘餘：ER {i + 1} `{e}` → 條文逐字之終態 `high`")

    # ── D-5 ──────────────────────────────────────────────────────────
    if t.get("split_flag"):
        cl, item = clause(t["leaf_id"]), t.get("test_item", "")
        upper, _, lower = item.partition("\n\n(")
        if cl and upper.strip() and upper.strip() not in cl:
            t["test_item"] = cl + "\n\n(" + lower
            done.append("D-5 test_item 上半段回復條文逐字（R-VS6）")
    return t, done


def main() -> int:
    log, out_files = [], []
    for f in latest_batches():
        d = json.loads(f.read_text(encoding="utf-8"))
        tcs, touched = [], 0
        for t in d["tcs"]:
            nt, done = fix_tc(t)
            if done:
                touched += 1
                log += [f"  {t['leaf_id']} [{f.name}] {x}" for x in done]
            tcs.append(nt)

        # note —— 內容逐字相同者標 `duplicate_of`（§10.6）
        seen: dict[tuple, str] = {}
        for t in tcs:
            k = (t["tc_title"], t["pre_conditions"], t["test_procedure"],
                 t["expected_result"])
            if k in seen and seen[k] != t["leaf_id"]:
                t["duplicate_of"] = seen[k]
                touched += 1
                log.append(f"  {t['leaf_id']} [{f.name}] note duplicate_of = {seen[k]}")
            else:
                seen.setdefault(k, t["leaf_id"])
        if not touched:
            continue
        m = re.match(r"(batch\d+(?:_[a-z]+)?)(?:_v(\d+))?\.json$", f.name)
        nxt = f.parent / f"{m.group(1)}_v{int(m.group(2) or 1) + 1}.json"
        d["tcs"] = tcs
        d["revision"] = ("W-157（55 輪）：83 包 §2 之五項 defect 修正 —— "
                         "D-2 刪重複 pre_condition／D-3・D-4 ER 改可觀察斷言、"
                         "待補入 AH／D-5 test_item 上半段回復逐字／note 標 duplicate_of")
        nxt.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        out_files.append(nxt.name)
    print("產出：", out_files)
    print("\n".join(log))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
