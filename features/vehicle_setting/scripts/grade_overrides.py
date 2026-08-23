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

**R-VF40 之兩條跨線檢查併入本檢查點**（不另立入口）：
  檢查一（R-VF23 檔名合規）／檢查二（R-VF10 編號唯一性）

用法：
    python3 scripts/grade_overrides.py --check     # 只驗，不寫；不符則 exit 1
    python3 scripts/grade_overrides.py --apply     # 套用覆寫並留快照
"""
import csv
import re
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


def check_rvf23() -> list[str]:
    """檢查一（R-VF40）—— `docs/handoff`／`docs/upstream` 之檔名合規。

    判準：檔名含 `vf230`／`test_group_ruling`／`numbering_collision`
    而**不以 `V` 起首**者即為違反；`docs/upstream/vf230/` 目錄存在亦為違反。

    錨點（R-VF21／R-VF28，以內容定錨）：
      必命中   `99_vf230_test.md`（人為建）→ 須被列為違反
      必不命中 `61_review_round37.md`（Part 1，含 `61_` 而非 VF230 線）
      鑑別     `V01_vf230_intake.md` —— 含 `vf230` 而合規；
               一條過寬之「檔名不得含 vf230」規則會誤殺之
    """
    bad = []
    marks = ("vf230", "test_group_ruling", "numbering_collision")
    for d in ("docs/handoff", "docs/upstream"):
        base = ROOT / d
        if not base.is_dir():
            continue
        for f in sorted(base.iterdir()):
            if f.is_dir() and f.name == "vf230":
                bad.append(f"{d}/vf230/ 目錄仍存在（R-VF23 第四項令收斂後移除）")
                continue
            if not f.is_file() or not f.name.endswith(".md"):
                continue
            low = f.name.lower()
            if any(m in low for m in marks) and not f.name.startswith("V"):
                bad.append(f"{d}/{f.name}：VF230 線之檔而未以 `V` 起首（R-VF23）")
    return bad


def check_rvf10() -> list[str]:
    """檢查二（R-VF40）—— `RULINGS.md`／`ANOMALIES.md` 之編號唯一性。

    同一編號不得有兩個**條文起始**。註記行（如「【VF230 線舊制編號…】」）
    不得被計為第二次定義 —— 故 `RULINGS.md` 只認 `### R-Vx{n} ——` 之標題行，
    `ANOMALIES.md` 只認表列首欄之 `| **A-Vx{n}**`。

    錨點：
      必命中   人為插入重複之 `### R-VF17 ——` → 須被列為違反
      必不命中 現行兩檔 → 應通過
      鑑別     `A-VS129`–`A-VS136` 之舊制標記行（其與編號同列，非新定義）
    """
    import collections
    bad = []
    r = (ROOT / "RULINGS.md").read_text(encoding="utf-8")
    heads = re.findall(r"^### (R-V[SF]\d+) ——", r, re.M)
    for k, n in collections.Counter(heads).items():
        if n > 1:
            bad.append(f"RULINGS.md：`{k}` 有 {n} 個條文起始（R-VF10）")
    a = (ROOT / "ANOMALIES.md").read_text(encoding="utf-8")
    ids = re.findall(r"^\| \*\*(A-V[SF]\d+)\*\*", a, re.M)
    for k, n in collections.Counter(ids).items():
        if n > 1:
            bad.append(f"ANOMALIES.md：`{k}` 有 {n} 個表列定義（R-VF10）")
    return bad


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
        # R-VF40：兩條跨線檢查併入同一檢查點
        cross = check_rvf23() + check_rvf10()
        if cross:
            print("跨線檢查失敗（R-VF40）：", file=sys.stderr)
            for b in cross:
                print(f"  {b}", file=sys.stderr)
            sys.exit(1)
        print(f"覆寫層 OK —— {len(ovr)} 筆 × "
              f"{len(expected_row(ovr[0]))} 欄皆為其應有之值")
        print("R-VF23 檔名合規 OK ／ R-VF10 編號唯一性 OK")
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
