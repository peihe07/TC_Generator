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


LIVE_SCOPE = ("RULINGS.md", "ANOMALIES.md", "DATA_REQUESTS.md", "CROSSLINE.md",
              "framework.md", "feature.yaml", "docs/INDEX.md")


def check_rvf48() -> list[str]:
    """檢查三（R-VF48）—— 引用而無定義。

    R-VF10 之檢查驗「同號不得兩義」，**未驗「有引用而無定義」**。
    `R-VF9` 被引用 3 處逾三包而無人察覺，即該缺口之實例。

    **豁免** `docs/handoff/`／`docs/upstream/`／`docs/reports/` ——
    下放包必先於落檔，將其納入會使檢查恆為失敗而喪失區辨力。

    錨點：
      必命中   人為於 `framework.md` 插入「依 R-VF99」→ 須失敗
      必不命中 現行全庫（`R-VF9` 已補落後）→ 應通過
      鑑別     `docs/handoff/V16_*.md` 對 `R-VF48` 之引用 —— 在豁免內，
               不得被計為「引用而無定義」
    """
    defined = set()
    r = (ROOT / "RULINGS.md").read_text(encoding="utf-8")
    defined |= set(re.findall(r"^### (R-V[SF]\d+) ——", r, re.M))
    a = (ROOT / "ANOMALIES.md").read_text(encoding="utf-8")
    # 表列首欄之三種書寫皆為定義：`| **A-VSnn**`／`| A-VSnn`／`| ~~A-VSnn~~`
    # （早期列不加粗、除役者加刪除線）。首版只認第一種，
    # 致 A-VS01–A-VS11 等被誤報為「引用而無定義」。
    # 取**列首之第一個編號**，不限定其後之修飾 —— 該欄可含加粗、刪除線、
    # 以及 R-VF10 所令之【VF230 線舊制編號】標記。首版要求編號後緊接 `|`，
    # 致加了標記之 A-VS129–136 被誤報。
    defined |= set(re.findall(r"^\|\s*[~*\s]*(A-V[SF]\d+)", a, re.M))
    d = (ROOT / "DATA_REQUESTS.md").read_text(encoding="utf-8")
    defined |= set(re.findall(r"^## (DR-\d+)", d, re.M))
    # 「仍開啟」表以**裸號**定義 DR（`| **5-A** |`／`| **8** |`／`| **9（新）** |`）
    for m in re.finditer(r"^\|\s*\*{0,2}(\d+)(?:-[A-Z])?", d, re.M):
        defined.add("DR-" + m.group(1))
    # `RULINGS.md` 檔首之「來源／條」對照表 —— 其列出**正文在他處之條文**
    # （canon §8.7：下放包已落檔且入版控，本檔不重複轉錄以免二處分岔）。
    # **故定義之全集為：本檔之條文起始 ∪ 該對照表所列 ∪ fenced block 起始。**
    # 首版只認條文起始，致 R-VS1–R-VS53 等大量被誤報。
    # 以**水平線**切，不以任何 `---` 切 —— 表格之分隔列 `|---|---|`
    # 亦含 `---`，首版因而在對照表之表頭處即截斷，其列全數落空。
    head = re.split(r"\n---+\n", r, 1)[0]
    for m in re.finditer(r"(R-V[SF])(\d+)\s*[~\uff5e]\s*(?:R-V[SF])?(\d+)", head):
        pre, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        defined |= {pre + str(i) for i in range(a, b + 1)}
    defined |= set(re.findall(r"\b(R-V[SF]\d+)", head))
    defined |= set(re.findall(r"^(R-V[SF]\d+)\uff08", r, re.M))

    # 編號**區間記法**為對編號空間之描述，非對特定條文之引用 ——
    # 依 R-VF52(c) 以判準精確化排除，不以白名單。
    RANGE = re.compile(r"`?([A-Z]-V[SF]\d+)`?\s*[~\uff5e\u2013\u2014]\s*`?([A-Z]-V[SF]\d+)`?")
    DOC = re.compile(r'"""(?:.|\n)*?"""')

    def refs(txt, is_py):
        if is_py:
            # R-VF52(c)：排除 docstring 與註解 —— 其內之編號為說明用例，非引用
            txt = DOC.sub("", txt)
            txt = re.sub(r"#[^\n]*", "", txt)
        txt = RANGE.sub(" ", txt)
        return re.findall(r"\b(R-V[SF]\d+|A-V[SF]\d+|DR-\d+)\b", txt)

    bad, seen = [], {}
    for rel in LIVE_SCOPE:
        f = ROOT / rel
        if not f.is_file():
            continue
        for tok in refs(f.read_text(encoding="utf-8"), False):
            if tok not in defined:
                seen.setdefault(tok, set()).add(rel)
    for f in sorted((ROOT / "scripts").glob("*.py")):
        for tok in refs(f.read_text(encoding="utf-8"), True):
            if tok not in defined:
                seen.setdefault(tok, set()).add("scripts/" + f.name)
    for tok, where in sorted(seen.items()):
        bad.append(f"`{tok}` 被引用而無定義 —— 見 "
                   + "／".join(sorted(where)[:3]))
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
        # R-VF46：各項獨立執行、各自輸出，一項失敗不中止其餘；
        # 末尾列總表；整體 exit code 仍為「任一失敗即非 0」（閘不放寬）；
        # 已知且已登記之失敗標其 anomaly 編號，使「新失敗」與「已知未解」可分辨。
        # **不得以抑制、跳過、白名單解決** —— 抑制即回到 A-VS106 之形態。
        results: list[tuple[str, bool, list[str], str]] = []

        bad = []
        for r in ovr:
            cur, want = by_w[r["leaf_id"]], expected_row(r)
            for col, exp in want.items():
                if cur.get(col, "") != exp:
                    bad.append(f"{r['leaf_id']} · {col}: 現為 {cur.get(col,'')!r}，"
                               f"應為 {exp!r}")
        results.append((f"覆寫層（R-VF17／R-VF20；{len(ovr)} 筆 × "
                        f"{len(expected_row(ovr[0]))} 欄）", not bad, bad, ""))

        b23 = check_rvf23()
        results.append(("R-VF23 檔名合規", not b23, b23, ""))

        b10 = check_rvf10()
        results.append(("R-VF10 編號唯一性", not b10, b10, "A-VF10"))

        b48 = check_rvf48()
        results.append(("R-VF48 引用而無定義", not b48, b48, ""))

        for name, ok, msgs, known in results:
            tag = "PASS" if ok else ("FAIL（已知：" + known + "）" if known else "FAIL")
            out = sys.stdout if ok else sys.stderr
            print(f"[{tag}] {name}", file=out)
            for m in msgs:
                print(f"      {m}", file=out)

        print("\n---- 總表 ----")
        for name, ok, msgs, known in results:
            mark = "PASS" if ok else ("FAIL ← 已知未解 " + known if known else "FAIL ← 新")
            print(f"  {mark:22} {name}"
                  + (f"（{len(msgs)} 項）" if msgs else ""))
        nfail = sum(1 for _, ok, _, _ in results if not ok)
        new_fail = sum(1 for _, ok, _, k in results if not ok and not k)
        print(f"  —— {len(results)-nfail} PASS ／ {nfail} FAIL"
              f"（其中新失敗 {new_fail}）")
        if nfail:
            sys.exit(1)          # 閘不放寬：任一失敗即非 0
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
