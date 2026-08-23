"""分級覆寫層（R-VF20）—— driver 之後置步驟。

**跑 `writability_driver.py --write` 之後必跑本腳本**（R-VF20 第 4 項；
已列入 `RUNBOOK.md`／`PLAYBOOK.md`）。

R-VF20 之四項：
  1. 由一次性腳本改為具名之 driver 後置步驟
  2. 覆寫清單落為獨立檔 `data/grade_overrides.tsv`，
     **清單即證據，不得以程式碼內嵌之條件式代替**；新增覆寫須引用裁決編號
  3. `--check`：若 `writability.tsv` 中清單所列之 leaf 不為新級，
     即為 driver 已重跑而後置步驟未跑 —— **該檢查須能失敗**
  4. 於 RUNBOOK／PLAYBOOK 明列

**不改 `scripts/writability_driver.py`** —— 改其 `value_sourced()` 會令
driver 對全部 leaf 重評值域來源，即全面回溯重跑，違反 R-VF14 第 4 項。

用法：
    python3 scripts/grade_overrides.py --check     # 只驗，不寫；不符則 exit 1
    python3 scripts/grade_overrides.py --apply     # 套用覆寫並留快照
"""
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVR = ROOT / "data" / "grade_overrides.tsv"
WRIT = ROOT / "docs" / "reports" / "writability.tsv"
GEN = ROOT / "docs" / "reports" / "generatable.tsv"


def load_overrides() -> list[dict]:
    with OVR.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    for r in rows:
        if not r.get("ruling"):
            raise SystemExit(f"{r['leaf_id']}：無 `ruling` 欄 —— "
                             "R-VF20 第 2 項令新增覆寫須引用裁決編號")
        if not r.get("source_verbatim"):
            raise SystemExit(f"{r['leaf_id']}：無 `source_verbatim` —— 清單即證據")
    return rows


def read_tsv(p: Path):
    with p.open(encoding="utf-8") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        return list(rd.fieldnames or []), list(rd)


def write_tsv(p: Path, cols, rows) -> None:
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    mode = "--check" if "--check" in sys.argv else (
        "--apply" if "--apply" in sys.argv else None)
    if mode is None:
        raise SystemExit("須指定 --check 或 --apply")

    ovr = load_overrides()
    wcols, wrows = read_tsv(WRIT)
    by_w = {r["leaf_id"]: r for r in wrows}

    # R-VF21 第 1 項：錨點（此處為覆寫標的本身）須先驗其存在於被掃描集合內
    absent = [r["leaf_id"] for r in ovr if r["leaf_id"] not in by_w]
    if absent:
        raise SystemExit(f"覆寫標的不存在於 writability.tsv：{absent}。"
                         "「不在檔內」與「已為新級」不可分辨，停。")

    if mode == "--check":
        bad = [(r["leaf_id"], by_w[r["leaf_id"]]["writable"], r["to_grade"])
               for r in ovr if by_w[r["leaf_id"]]["writable"] != r["to_grade"]]
        if bad:
            print("覆寫未生效 —— driver 已重跑而後置步驟未跑：", file=sys.stderr)
            for lid, cur, want in bad:
                print(f"  {lid}: 現為 {cur}，應為 {want}", file=sys.stderr)
            print(f"\n修法：python3 {Path(__file__).name} --apply", file=sys.stderr)
            sys.exit(1)
        print(f"覆寫層 OK —— {len(ovr)} 筆皆為其應有之級")
        return

    gcols, grows = read_tsv(GEN)
    by_g = {r["leaf_id"]: r for r in grows}
    changed = []
    for r in ovr:
        w = by_w[r["leaf_id"]]
        if w["writable"] == r["to_grade"]:
            continue
        if w["writable"] != r["from_grade"]:
            raise SystemExit(f"{r['leaf_id']}：現為 {w['writable']}，"
                             f"既非 {r['from_grade']} 亦非 {r['to_grade']}，停")
        w["writable"] = r["to_grade"]
        w["blocker_class"] = ""
        w["blocker_detail"] = ""
        note = (f"{r['ruling']}：值域來源為 {r['source_column']}，reqid "
                f"{r['reqid']}，逐字 `{r['source_verbatim']}`")
        prev = w.get("evidence_note", "")
        # 去重：本層須可重跑，而重跑不得使註記累積。
        # 以「同一裁決編號 ＋ 同一 reqid」為同一筆註記之鍵。
        key = f"{r['ruling']}：值域來源為 {r['source_column']}，reqid {r['reqid']}"
        if key not in prev:
            w["evidence_note"] = (prev + " ｜ " if prev else "") + note
        if r["leaf_id"] in by_g:
            by_g[r["leaf_id"]]["writable"] = r["to_grade"]
        changed.append(r["leaf_id"])

    if not changed:
        print(f"覆寫層 OK —— {len(ovr)} 筆皆已為其應有之級，無須套用")
        return
    shutil.copy(WRIT, WRIT.with_name("writability_pre_override.tsv"))
    shutil.copy(GEN, GEN.with_name("generatable_pre_override.tsv"))
    write_tsv(WRIT, wcols, wrows)
    write_tsv(GEN, gcols, grows)
    for lid in changed:
        print(f"  覆寫 {lid} -> {by_w[lid]['writable']}")
    print(f"套用 {len(changed)} 筆；快照 writability_pre_override.tsv")


if __name__ == "__main__":
    main()
