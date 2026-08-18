"""G146 —— 台帳重複偵測（R-P215）。

現行之台帳檢查只驗**編號無斷點**，**抓不到重複** ——
29 包執行層於發現「重跑會把 R-P210–214 重覆抄進 `RULINGS.md`、
重覆開 DR-PW14」時停並詢問，其風險即由此而來。

該次之台帳完整性檢查**係臨時加驗**，非常設閘門；
R-P215 明訂「**臨時加驗不得取代常設閘門**」——
前者依賴當次執行者想到，後者每次必跑。

四項檢查（與現行之無斷點檢查併行，不取代之）：

  1. `RULINGS.md`      —— 條號（`[R-Pnnn]` 行首）不得重複
  2. `ANOMALIES.md`    —— 列（`| A-PWnnn |` 行首）不得重複
  3. `DATA_REQUESTS.md`—— 列（`| DR-PWnn |` 行首）不得重複
  4. `docs/INDEX.md`   —— 輪次（`| NN |` 行首）不得重複

用法：
    python features/power/scripts/verify_ledger_dup.py
    python features/power/scripts/verify_ledger_dup.py --self-test
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
POWER = ROOT / "features/power"

CHECKS = [
    ("RULINGS.md", "條號", re.compile(r"^\[(R-P\d+)\]", re.M)),
    ("ANOMALIES.md", "列", re.compile(r"^\|\s*(A-PW\d+)\s*\|", re.M)),
    ("DATA_REQUESTS.md", "列", re.compile(r"^\|\s*(DR-PW\d+)\s*\|", re.M)),
    ("docs/INDEX.md", "輪次", re.compile(r"^\|\s*(\d{2})\s*\|", re.M)),
]


def duplicates(text: str, pat: re.Pattern) -> list[tuple[str, int]]:
    seen: dict[str, int] = {}
    for m in pat.finditer(text):
        seen[m.group(1)] = seen.get(m.group(1), 0) + 1
    return sorted((k, n) for k, n in seen.items() if n > 1)


def check(root: Path = POWER) -> list[dict]:
    findings = []
    for name, kind, pat in CHECKS:
        p = root / name
        if not p.exists():
            findings.append({"file": name, "detail": "檔案不存在"})
            continue
        dups = duplicates(p.read_text(encoding="utf-8"), pat)
        for key, n in dups:
            findings.append({"file": name,
                             "detail": f"{kind} `{key}` 出現 **{n}** 次（應為 1）"})
    return findings


def self_test() -> int:
    """R-P215：以**刻意重複一列**之 fixture 證明其確實會 FAIL。"""
    import shutil
    import tempfile
    failures = 0

    def case(label: str, mutate, want_fail: bool) -> None:
        nonlocal failures
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "power"
            (tmp / "docs").mkdir(parents=True)
            for name, _, _ in CHECKS:
                shutil.copy(POWER / name, tmp / name)
            mutate(tmp)
            got = bool(check(tmp))
            ok = got == want_fail
            failures += not ok
            print(f"  [{'PASS' if ok else '**FAIL**'}] G146 {label}")
            print(f"          期望 {'FAIL' if want_fail else '通過'}；"
                  f"實際 {'FAIL（' + check(tmp)[0]['detail'] + '）' if got else '通過'}")

    def dup_line(path: str, pat: re.Pattern):
        def f(root: Path):
            p = root / path
            lines = p.read_text(encoding="utf-8").split("\n")
            i = next(k for k, l in enumerate(lines) if pat.match(l))
            lines.insert(i + 1, lines[i])          # 刻意重複該列
            p.write_text("\n".join(lines), encoding="utf-8")
        return f

    case("應通過 —— 現況之四份台帳", lambda root: None, False)
    for name, kind, pat in CHECKS:
        case(f"應 FAIL —— 刻意重複 `{name}` 之一{kind}",
             dup_line(name, pat), True)
    print(f"\n  G146 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    findings = check()
    for name, kind, pat in CHECKS:
        p = POWER / name
        n = len(set(pat.findall(p.read_text(encoding="utf-8")))) if p.exists() else 0
        dups = [f for f in findings if f["file"] == name]
        print(f"  {name}: {kind} {n} 個相異；重複 **{len(dups)}**")
        for f in dups:
            print(f"     **{f['detail']}**")
    print(f"\nG146：{'PASS —— 四項皆無重複' if not findings else f'**{len(findings)} 項重複**'}")
    raise SystemExit(0 if not findings else 1)


if __name__ == "__main__":
    main()
