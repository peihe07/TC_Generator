"""B1 —— G113 未覆蓋分支之逐支裁決（R-P325）。

R-P325 令 78 支逐項裁決三選一，不得帶入寫回。

**本檔只做機械可判之一層**，其餘留給人工逐支裁決 —— 理由如下。

## 已量測而**遭否決**之謂詞（R-P250 / R-P182 —— 各版並陳）

**版本一：leaf 級文件頻率（df）** —— 「獨有詞若於全語料多數 leaf 之
`source_clause` 出現，則其為通用連接詞而非可測標的」。
實測 111 個 leaf：`equal` df=13、`user` df=12、`due` df=11，
**而已知真缺口之標記 `pre` df=8、`ltm` df=8**，
與 `case`(8) / `logic`(8) / `need`(8) 同帶。
**任何能濾掉 `equal` 之門檻（df ≥ 9）都貼著 `pre` / `ltm` 的頭皮過** ——
且 `see`(21) / `hmi`(19) / `refer`(5) 正是外部參照之標記、
`off`(22) / `show`(21) / `stay`(14) 為實質領域詞，皆會被誤濾。
**該謂詞不得使用**（R-P250），本檔不含之。

**版本二：詞形關係（三個子謂詞）** —— 只判「該獨有詞是否為**同一個詞**之變體」：
  (a) **標點變體** —— 去尾標點後見於 TC（`state.` / `modes.` / `respectively.`）
  (b) **詞幹前綴** —— 該詞為某 TC 詞之前綴或反之（`mod` ⊂ `mode`、`doe` ⊂ `does`）
  (c) **黏連產物** —— 可切為 ≥2 段而每段皆見於 TC 或屬 THEN/IF/AND/ELSE/EVEN
      （`valuethentlm` = value+then+tlm、`standbythen`、`theneven`、`state.in`）

**版本三（採用）：(b) 遭驗證條件否決，刪除；只留 (a)(c)。**
驗證條件當場攔下 —— **`pre` 被判為 TC 之 `pres` 之前綴變體而排除**。
`mod` ⊂ `mode`（切詞產物）與 `pre` ⊂ `pres`（真缺口）**其詞形關係完全同型**
（皆為尾差一字母），**無任何寫法能分辨之** —— 故 (b) 不得使用。
其代價：`mod` / `doe` / `pas` / `ups` 等四類落回人工池，由人逐支判。
**寧可多判，不可誤排除。**

(a)(c) 為結構性關係（標點、黏連），不涉語義輕重，故保留。

## 驗證條件（R-P250：≥3 個已知應命中之實例）

本謂詞之方向與 R-P250 之常例相反 —— 其為**排除**謂詞，
故驗證條件為「**三個已知真缺口之標記皆不得被本謂詞排除**」：
`off-tim`（16 包）、`pre`（18 包）、`ltm`（22 包）。
**任一被排除即本謂詞不得使用。**

**驗證環境之訂正（並陳，R-P182）**：初版以**現況全語料**之 TC 詞集為測試環境，
其為誤 —— `off-tim` / `ltm` 於現況 TC 中**本來就在**（該三處缺口已於 16 / 18 / 22 包補齊），
故必然「命中」而該命中無意義。訂正為**以當時快照之該 leaf TC 詞集**為環境
（`or_branch_coverage._reconstruct`，與 G113 自驗同源）。
`pre` 之否決在二種環境下皆成立，故版本二之刪除不因環境訂正而改變。

用法：
    python features/power/scripts/adjudicate_g113_50.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from or_branch_coverage import _reconstruct, analyse, uncovered  # noqa: E402
from reverse_coverage import tc_text, words  # noqa: E402

# 黏連之接合詞：規格原文之 `valueTHENTLM` 類黏連，其接合處為這些字
JOINERS = {"then", "if", "and", "else", "even", "in", "or"}
PUNCT = ".,;:)('\"’”"


def punct_variant(d: str, tcw: set[str]) -> str | None:
    """(a) 標點變體。"""
    s = d.strip(PUNCT)
    return f"標點變體 —— 去尾標點得 `{s}`，見於 TC" if s != d and s in tcw else None


def glued(d: str, tcw: set[str]) -> str | None:
    """(c) 黏連產物 —— 可切為 ≥2 段，每段皆見於 TC 或屬接合詞，且至少一段為接合詞。"""
    n = len(d)
    if n < 6:
        return None

    def ok(seg: str) -> bool:
        return seg in tcw or seg in JOINERS

    # 動態規劃：能否完全切分
    reach = [False] * (n + 1)
    reach[0] = True
    back: dict[int, list[str]] = {0: []}
    for i in range(1, n + 1):
        for j in range(max(0, i - 16), i):
            if reach[j] and ok(d[j:i].strip(PUNCT)) and len(d[j:i].strip(PUNCT)) >= 2:
                reach[i] = True
                back[i] = back[j] + [d[j:i]]
                break
    if not reach[n]:
        return None
    parts = back[n]
    if len(parts) < 2 or not any(p.strip(PUNCT) in JOINERS for p in parts):
        return None
    return "黏連產物 —— 可切為 `" + " + ".join(parts) + "`"


def classify_token(d: str, tcw: set[str]) -> str | None:
    """該獨有詞是否為**同一詞之書寫變體**（非實質）。"""
    # (b) 詞幹前綴已遭驗證條件否決（見模組首段版本三），不在此列。
    return punct_variant(d, tcw) or glued(d, tcw)


def collect() -> list[dict]:
    rows = []
    for p in sorted(GENERATED.glob("*.json")):
        batch = json.loads(p.read_text(encoding="utf-8"))
        by_leaf: dict[str, list[dict]] = {}
        for tc in batch.get("tcs", []):
            by_leaf.setdefault(tc["req_id"], []).append(tc)
        for leaf, r in uncovered(analyse(batch)):
            tcw: set[str] = set()
            for tc in by_leaf.get(leaf, []):
                tcw |= words(tc_text(tc))
            marks = {d: classify_token(d, tcw) for d in r["missing"]}
            rows.append({
                "batch": p.stem, "leaf": leaf,
                "group": r["group"], "branch": r["branch"],
                "text": r["text"], "missing": r["missing"],
                "marks": marks,
                "substantive": [d for d, m in marks.items() if m is None],
            })
    return rows


def validate(rows: list[dict]) -> bool:
    """R-P250 驗證：三個已知真缺口之標記皆不得被排除謂詞排除。"""
    print("  驗證條件 —— 三個已知真缺口之標記不得被排除：")
    ok = True
    # 環境：**當時快照**之該 leaf TC 詞集（與 G113 自驗同源），非現況全語料
    for marker, src, leaf in (("off-tim", "b1_before16.json", "SWE-PM-073"),
                              ("pre", "_batch2_pre043", "SWE-PM-038"),
                              ("ltm", "_batch3_pre", "SWE-PM-014")):
        snap = (_reconstruct(src) if src.startswith("_")
                else json.loads((DATA / src).read_text(encoding="utf-8")))
        tcw: set[str] = set()
        for tc in snap.get("tcs", []):
            if tc["req_id"] == leaf:
                tcw |= words(tc_text(tc))
        m = classify_token(marker, tcw)
        ok &= m is None
        print(f"    [{'PASS' if m is None else '**FAIL**'}] `{marker}` "
              f"{'未被排除' if m is None else '被排除 —— ' + m}")
    return ok


def main() -> None:
    rows = collect()
    if not validate(rows):
        raise SystemExit("排除謂詞未通過驗證條件（R-P250），不得使用")
    zero = [r for r in rows if not r["substantive"]]
    rest = [r for r in rows if r["substantive"]]
    print(f"\n  未覆蓋分支 {len(rows)}")
    print(f"  機械層：全部獨有詞皆為書寫變體 → **{len(zero)}** 支（其區辨實質為零）")
    print(f"  留待人工逐支裁決 → **{len(rest)}** 支\n")
    for r in rest:
        print(f"  {r['leaf']} 組{r['group']}支{r['branch']}  實質詞 {r['substantive']}")
        print(f"      {r['text'][:96]}")
    (DATA / "g113_adjudication_50.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n  wrote data/g113_adjudication_50.json")


if __name__ == "__main__":
    main()
