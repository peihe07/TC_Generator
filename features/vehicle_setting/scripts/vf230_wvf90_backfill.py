"""W-VF90 — pilot #1／#2 之 20 條補入（R-VF140）。

**本檔只產出候選 JSON，不寫工作簿** —— 寫回為另一步（W-VF90.2／.4）。

R-VF140 令「不重新生成，惟須過現行自檢；未過者依現行判準重寫該欄」。
**實測顯示其前提不成立於三處，其二已消解、第三處待裁**：
  一、2 條首報「事實抽不出」，**其為抽取式之缺陷非條文之缺** ——
      條文之值帶引號（`receives the value as "Absent" via signal`）而字元類不含 `"`。
      **已修並依 R-VF82 量兩側**：偽陰回收 2、偽陽引入 0、量產 501 條事實相異 0。
      **20 條之事實現全數可抽。**
  二、1 條（`SWITCH1Type-002`）與已寫入之 `-029` 可執行四欄及 `tc_title` 逐字相同
      —— 依 W-VF74 剔除；**其 `test_item` 相異，故為上游需求集之重複**，已開 **DR-48**。
      **故補入之數為 19。**
  三、**須改之欄不止 `test_item`**（`tc_title` 13／`expected_result` 12／
      `test_procedure` 11／`pre_conditions` 3／`input_test_data` 2／`writable` 2）——
      **「只改一欄」與「須過現行自檢」於本料上不可兼得**，採用範圍待裁。
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FEAT / "scripts"))
import vf230_wvf69_facts as FACTS      # noqa: E402
import vf230_wvf69_batches as B        # noqa: E402
import vf230_wvf61_pilot as P1         # noqa: E402
import vf230_wvf44_writability as WR   # noqa: E402

OUT = FEAT / "generated/vf230_backfill.json"
EXEC_KEYS = ("pre_conditions", "test_procedure", "expected_result", "input_test_data")


def _fp(t: dict) -> str:
    return hashlib.sha1("\x00".join(str(t[k]) for k in EXEC_KEYS).encode()).hexdigest()


def main() -> None:
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    refs = P1.spec_refs()
    vcvm = WR.vcvm()

    pilots, old = set(), {}
    for f in ("generated/vf230_pilot1.json", "generated/vf230_pilot2.json"):
        for t in json.loads((FEAT / f).read_text(encoding="utf-8"))["tcs"]:
            pilots.add(t["leaf_id"])
            old[t["leaf_id"]] = t
    print(f"pilot #1／#2 之 leaf {len(pilots)}")

    prod, _ = FACTS.load_all()
    bf, skipped = FACTS.load_all(only=pilots)
    print(f"事實可抽出 {len(bf)}｜抽不出 {len(skipped)}")
    for s in skipped:
        print(f"  ✋ 抽不出 {s['leaf_id']} —— {s.get('why')}")

    # 家族計數以**全集**計（量產 ＋ 補入）——
    # 家族成員跨二側者，只算一側會把跨側之手足誤判為單條（R-VF98）。
    fam: dict[str, int] = {}
    for x in prod + bf:
        if x.get("pending") or x.get("pilot3"):
            continue
        k = re.sub(r"-?\d+$", "", x["leaf_id"])
        fam[k] = fam.get(k, 0) + 1

    # 已寫入者之指紋 —— 補入之條與其逐字相同者為重複（W-VF74）
    written: dict[str, str] = {}
    for row in csv.DictReader((FEAT / "data/vf230_batches.tsv").open(encoding="utf-8"),
                              delimiter="\t"):
        for t in json.loads((FEAT / row["file"]).read_text(encoding="utf-8"))["tcs"]:
            written[_fp(t)] = t["leaf_id"]

    tcs, dropped, rejected = [], [], []
    for f in bf:
        lid = f["leaf_id"]
        # seq 於下方去重之後才定 —— 先以 0 建，其值不入 TC 之任何欄位判準
        t, why = B.build(f, 0, wr, refs, lv, fam, vcvm)
        if t is None:
            rejected.append({"leaf_id": lid, "why": why})
            print(f"  ✋ build 回 None {lid} —— {why}")
            continue
        fp = _fp(t)
        if fp in written:
            dropped.append({"dropped": lid, "kept": written[fp],
                            "why": "可執行四欄逐字相同（W-VF74）"})
            print(f"  ✋ 去重 {lid} ↔ 已寫入之 {written[fp]}")
            continue
        tcs.append(t)

    # ---- seq 改編為接續 batch09（702）之連號 ----
    # **不沿用 pilot 原 seq（238–247／258–267）** —— 其間本有斷點（248–257），
    # 去重又移走 262，**自檢之「連號」項遂失敗**。
    # 該項所防者為「批內有條被靜默丟棄」，**其不應為遷就舊號而放寬**（R-VF130）。
    # seq 為內部編號，不寫入工作簿之任何欄；工作簿之號為 B 欄，另行續編。
    SEQ0 = 703
    for i, t in enumerate(tcs):
        t["seq"] = SEQ0 + i          # 各批之 seq 皆為 int，型別須一致

    KEYS = ['tc_title', 'test_item', 'pre_conditions', 'input_test_data',
            'test_procedure', 'expected_result', 'specification_reference',
            'priority', 'priority_class', 'design_method', 'writable', 'value_source']
    changed = {k: [t["leaf_id"] for t in tcs
                   if str(t.get(k, '')) != str(old[t["leaf_id"]].get(k, ''))]
               for k in KEYS}

    doc = {
        "batch": "vf230_backfill",
        "line": "VF230",
        "feature": "vehicle_setting / VF230",
        "test_group": "Vehicle Setting",
        "handoff": "docs/handoff/V68_pilot_backfill.md",
        "work_order": "W-VF90",
        "ruling": "R-VF140（Pei 裁定 2026-08-25：直接補入）",
        "source": "generated/vf230_pilot1.json（其 batch 欄為 vf230_pilot1_v4）"
                  "＋ generated/vf230_pilot2.json",
        "note": "**下放包指名之 `generated/vf230_pilot1_v4.json` 不存在** —— "
                "v4 已就地覆蓋 `vf230_pilot1.json`，其 `batch` 欄逐字為 `vf230_pilot1_v4`。",
        "seq_policy": "改編為 703– 之連號（接續 batch09 之 702）—— "
                      "沿用 pilot 原 seq 者其間有斷點（248–257）且去重移走 262，"
                      "自檢之連號項失敗；該項所防為「批內有條被靜默丟棄」，不為遷就舊號而放寬。",
        "write_back": "**本檔未寫工作簿**；寫回為 W-VF90.2／.4，其採用範圍待裁。",
        "counts": {"pilot_leaf": len(pilots), "facts_ok": len(bf),
                   "facts_skipped": len(skipped), "built": len(tcs),
                   "dropped_dup": len(dropped), "rejected": len(rejected)},
        "field_changed_vs_pilot": {k: len(v) for k, v in changed.items()},
        "field_changed_detail": changed,
        "skipped": [{"leaf_id": s["leaf_id"], "why": s.get("why")} for s in skipped],
        "dropped": dropped,
        "rejected": rejected,
        "tcs": tcs,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n產出 {len(tcs)} 條 → {OUT.relative_to(FEAT)}")
    print("逐欄相異:", {k: v for k, v in doc["field_changed_vs_pilot"].items() if v})


if __name__ == "__main__":
    main()
