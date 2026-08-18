"""G108 —— 切片編輯後之完整性檢查（R-P150）。

20 §八(丙)6：過寬切片第三次（05 包 §E 偏移、11 包誤刪二常數、20 包誤刪四函式）。
前二次之既有規則為「每次編輯獨立進行、不共用位移」，
**而第三次係切片邊界選錯，非位移問題** —— 舊規則未涵蓋此形態。

R-P150：任何以字串切片或範圍替換方式修改程式碼之編輯，
**替換後須立即以語法或載入層檢查驗證該檔完整性**。

本檔即該檢查之落實形式：對指定 Python 檔逐一驗

  （1）**語法層**：`ast.parse` 通過
  （2）**載入層**：`importlib` 可載入（攔下 `NameError` 這類語法正確而符號消失者）
  （3）**符號層**：該檔之頂層函式／常數集合與**基準快照**相同 ——
       **此層才攔得住「刪掉四個函式而語法仍正確」**

基準快照存於 `data/edit_integrity_baseline.json`，
以 `--update-baseline` 更新（更新須為有意之介面變更）。

用法：
    python features/power/scripts/check_edit_integrity.py
    python features/power/scripts/check_edit_integrity.py --update-baseline
    python features/power/scripts/check_edit_integrity.py --self-test
"""

from __future__ import annotations

import ast
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))
from protect_products import guard_write, log_baseline_reset, sha  # R-P233：基準之保護與重設紀錄
DATA = ROOT / "features/power/data"
BASELINE = DATA / "edit_integrity_baseline.json"

# R-P242(a)：基線擴及 `features/power/scripts/` **全部** `.py`。
# 34 §1.1 之教訓 —— 舊 WATCHED 僅 7 檔（7 / 59 = 11.9%），
# `dryrun_write_back.py` 之損壞自 33 包起潛伏兩包未被發現。
# **「G108 未報錯」不得作為「腳本無損壞」之證據**（R-P242）。
#
# 載入層之安全性已以 AST 實測（35 包）：排除 `sys.path.insert` 後，
# 59 檔中僅 2 檔有模組層陳述（`build_reconciliation.py` / `rejudge_design_method.py`），
# 二者皆為記憶體內字典操作，**無檔案寫入** ——
# 故 `exec_module` 不觸發 R-P227(c) 之時點相依產物再生。
WATCHED = sorted(p.name for p in SCRIPTS.glob("*.py"))


def symbols(source: str) -> list[str]:
    tree = ast.parse(source)
    out = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            out.append(node.name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    out.append(tgt.id)
    return sorted(out)


def check(name: str, source: str, base: dict) -> dict:
    r = {"file": name, "syntax": False, "load": None, "symbols_ok": None,
         "missing": [], "added": []}
    try:
        ast.parse(source)
        r["syntax"] = True
    except SyntaxError as e:
        r["error"] = f"SyntaxError: {e}"
        return r
    got = symbols(source)
    want = base.get(name)
    if want is not None:
        r["missing"] = sorted(set(want) - set(got))
        r["added"] = sorted(set(got) - set(want))
        r["symbols_ok"] = not r["missing"]
    return r


def load_ok(path: Path) -> bool:
    spec = importlib.util.spec_from_file_location(path.stem + "_probe", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(SCRIPTS))
    try:
        spec.loader.exec_module(mod)
        return True
    except Exception:
        return False


def self_test() -> int:
    """R-P150 / G108 —— 以刻意刪函式之案例證明其會攔下。"""
    src = (SCRIPTS / "lint_tcs.py").read_text(encoding="utf-8")
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    failures = 0

    def case(label: str, text: str, want_ok: bool) -> None:
        nonlocal failures
        r = check("lint_tcs.py", text, base)
        ok = (r["syntax"] and r["symbols_ok"]) == want_ok
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G108 {label}")
        print(f"          syntax={r['syntax']} symbols_ok={r['symbols_ok']} "
              f"missing={r['missing'][:4]}")

    case("應 PASS —— 現況原檔", src, True)
    # 刻意刪去四個函式（即 20 包之實際損壞形態），語法仍正確
    cut = src
    for fn in ("check_s52b_final_step_intent", "check_source_clause",
               "check_misread_terms", "check_er_clause_coverage"):
        i = cut.index(f"def {fn}(")
        j = cut.index("\ndef ", i + 1)
        cut = cut[:i] + cut[j + 1:]
    case("應 FAIL —— 刻意刪去四個函式（語法仍正確）", cut, False)
    case("應 FAIL —— 語法破壞", src.replace("def main() -> None:", "def main( -> None:"), False)
    print(f"\n  G108 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--update-baseline" in sys.argv:
        base = {n: symbols((SCRIPTS / n).read_text(encoding="utf-8")) for n in WATCHED}
        # R-P233(b)(c)：基準之重設須帶明示參數，且留下重設紀錄
        _before = sha(BASELINE)
        guard_write(BASELINE)
        BASELINE.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        log_baseline_reset(_before, sha(BASELINE),
                           note="--update-baseline")
        print(f"baseline updated — {len(base)} files, "
              f"{sum(len(v) for v in base.values())} symbols")
        return
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    bad = 0
    for n in WATCHED:
        path = SCRIPTS / n
        r = check(n, path.read_text(encoding="utf-8"), base)
        r["load"] = load_ok(path) if r["syntax"] else False
        ok = r["syntax"] and r["load"] and r["symbols_ok"] is not False
        bad += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] {n}  syntax={r['syntax']} "
              f"load={r['load']} symbols_ok={r['symbols_ok']}"
              + (f"  缺 {r['missing']}" if r["missing"] else ""))
    print(f"\nG108：{len(WATCHED) - bad} / {len(WATCHED)} 完整")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
