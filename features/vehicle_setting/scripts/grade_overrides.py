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


def expected_row(r: dict) -> dict:
    """一筆覆寫所要求之**逐欄**終態 —— `--apply` 與 `--check` 共用此單一定義。

    R-VF29 第 6 項：檢查面須等於變更面。二者共用本函式即結構上保證相等，
    不靠兩處程式碼各自維護一份欄位清單。
    """
    return {
        "writable": r["to_grade"],
        "blocker_class": "",
        "blocker_detail": "",
        # R-VF29 第 5 項：註記依清單重生，非附加 —— 故其為終態之一部分
        "evidence_note": (f"{r['ruling']}：值域來源為 {r['source_column']}，"
                          f"reqid {r['reqid']}，逐字 `{r['source_verbatim']}`"),
    }


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
        bad = []
        for r in ovr:
            cur, want = by_w[r["leaf_id"]], expected_row(r)
            for col, exp in want.items():
                if cur.get(col, "") != exp:
                    bad.append((r["leaf_id"], col, cur.get(col, ""), exp))
        if bad:
            print("覆寫未生效 —— driver 已重跑而後置步驟未跑：", file=sys.stderr)
            for lid, col, cur, want in bad:
                print(f"  {lid} · {col}: 現為 {cur!r}，應為 {want!r}", file=sys.stderr)
            print(f"\n修法：python3 {Path(__file__).name} --apply", file=sys.stderr)
            sys.exit(1)
        print(f"覆寫層 OK —— {len(ovr)} 筆 × "
              f"{len(expected_row(ovr[0]))} 欄皆為其應有之值")
        return

    gcols, grows = read_tsv(GEN)
    by_g = {r["leaf_id"]: r for r in grows}
    changed = []
    for r in ovr:
        w, want = by_w[r["leaf_id"]], expected_row(r)
        if all(w.get(c, "") == v for c, v in want.items()):
            continue
        if w["writable"] not in (r["from_grade"], r["to_grade"]):
            raise SystemExit(f"{r['leaf_id']}：現為 {w['writable']}，"
                             f"既非 {r['from_grade']} 亦非 {r['to_grade']}，停")
        # R-VF29 第 5 項：**重生**而非附加 —— 重跑 N 次後筆數與 N 無關。
        # 文字比對去重曾因新舊腳本措辭不同而失效（A-VF6 同輪）。
        w.update(want)
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
