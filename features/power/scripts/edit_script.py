"""G165 —— 腳本之 AST 安全編輯（R-P238）。

33 §1.3 與 34 §一：執行層**二度**以正則定位插入點修改 `.py`，
二度將 import 誤置於函式體內（`check_edit_integrity.py` 於 33 包當場報錯；
**`dryrun_write_back.py` 則直到 34 包方發現** —— 因其不在 G108 之 7 檔基準內，
且該包未執行之）。

R-P238 **禁止以正則或字串位移定位插入點修改任何 `.py`**，
替代方式二擇一：
  (a) 以 `ast` 解析後於**明確之節點邊界**插入，並於寫回後重新 `ast.parse`
  (b) 以完整檔案重寫（先備份，R-P234），不作區域性插入

本模組實作 (a)：
  - `insert_module_import(path, line)` —— 於**最後一個頂層 import 節點之後**插入，
    其位置由 AST 之 `end_lineno` 決定，非由文字比對
  - `drop_lines(path, nums)` —— 以行號刪除（供修復誤置之插入）
  - 二者皆於寫回後 `ast.parse`；**失敗即自動回復原內容並拋出**

G108 之限度一併明載（R-P238）：其驗**語法、載入與符號之存在**，
**不驗語義** —— 語義偏差無任何機制可攔；
且其基準僅涵蓋 7 檔，**基準外之腳本連語法都不驗**。

用法：
    python features/power/scripts/edit_script.py --self-test
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


class EditFailed(Exception):
    """編輯後 `ast.parse` 失敗，已回復原內容。"""


def _write_verified(path: Path, lines: list[str], original: str) -> None:
    new = "\n".join(lines)
    path.write_text(new, encoding="utf-8")
    try:
        ast.parse(new)
    except SyntaxError as e:
        path.write_text(original, encoding="utf-8")
        raise EditFailed(f"{path.name}: 寫回後語法錯（{e}），**已回復原內容**") from e


def insert_module_import(path: Path, line: str) -> int:
    """於最後一個**頂層** import 之後插入一行；回傳插入之行號（1-indexed）。"""
    original = path.read_text(encoding="utf-8")
    tree = ast.parse(original)
    tops = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    if not tops:
        raise EditFailed(f"{path.name}: 無頂層 import，無明確之節點邊界可插入")
    after = max(n.end_lineno for n in tops)
    lines = original.split("\n")
    lines.insert(after, line)
    _write_verified(path, lines, original)
    return after + 1


def drop_lines(path: Path, nums: list[int]) -> list[str]:
    """以 1-indexed 行號刪除；回傳被刪之內容。"""
    original = path.read_text(encoding="utf-8")
    lines = original.split("\n")
    dropped = [lines[n - 1] for n in sorted(nums)]
    for n in sorted(nums, reverse=True):
        del lines[n - 1]
    _write_verified(path, lines, original)
    return dropped


def replace_node(path: Path, name: str, new_src: str,
                 with_comments: bool = False) -> tuple[int, int]:
    """以 AST 節點邊界替換一個頂層 def / class / 賦值；回傳被替換之行號區間。

    **R-P238(a)** —— 邊界由 `lineno` / `end_lineno` 決定，非由文字比對。
    def / class 含其上方之裝飾器。寫回後重新 `ast.parse`，失敗即回復。

    **本工具之限度（35 包實測）**：`ast` **不建模註解**，
    故節點上方之 `#` 註解不在節點邊界內；若新內容自帶註解而未設
    `with_comments=True`，舊註解將殘留而重複（35 包實際發生於 `COND_RE`）。
    `with_comments=True` 時起點上推至該節點上方之連續 `#` 行 ——
    該上推為**行首字元判斷**，非正則定位插入點，終點仍為 AST 邊界（R-P238(a)）。
    """
    original = path.read_text(encoding="utf-8")
    tree = ast.parse(original)

    def matches(n):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return n.name == name
        if isinstance(n, ast.Assign):
            return any(isinstance(t, ast.Name) and t.id == name for t in n.targets)
        if isinstance(n, ast.AnnAssign):
            return isinstance(n.target, ast.Name) and n.target.id == name
        return False

    node = next((n for n in tree.body if matches(n)), None)
    if node is None:
        raise EditFailed(f"{path.name}: 查無頂層節點 `{name}`")
    start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
    end = node.end_lineno
    lines = original.split("\n")
    if with_comments:
        while start > 1 and lines[start - 2].lstrip().startswith("#"):
            start -= 1
    lines[start - 1:end] = new_src.rstrip("\n").split("\n")
    _write_verified(path, lines, original)
    return start, end


def append_module_code(path: Path, code: str) -> int:
    """於頂層追加程式碼；回傳追加之起始行號。

    插入點為 **`if __name__ == "__main__":` 守衛之前**（無守衛則為模組末端）——
    二者皆為 AST 可判之明確邊界，非文字定位。
    置於守衛之前係因守衛會呼叫 `main()`，追加於其後者於執行時尚未定義。
    寫回後重新 `ast.parse`，失敗即回復。
    """
    original = path.read_text(encoding="utf-8")
    tree = ast.parse(original)
    guard = next((n for n in tree.body
                  if isinstance(n, ast.If)
                  and ast.dump(n.test).find("__main__") >= 0), None)
    lines = original.split("\n")
    if guard is not None:
        at = guard.lineno - 1
    else:
        while lines and not lines[-1].strip():
            lines.pop()
        at = len(lines)
    lines[at:at] = code.rstrip("\n").split("\n") + ["", ""]
    _write_verified(path, lines, original)
    return at + 1


def self_test() -> int:
    import tempfile
    failures = 0

    def case(label: str, src: str, fn, want_fail: bool):
        nonlocal failures
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "m.py"
            p.write_text(src, encoding="utf-8")
            try:
                fn(p)
                got = False
            except EditFailed:
                got = True
            ok = got == want_fail
            restored = p.read_text(encoding="utf-8") == src
            if want_fail and not restored:
                ok = False
            failures += not ok
            print(f"  [{'PASS' if ok else '**FAIL**'}] G165 {label}")
            print(f"          期望 {'失敗且回復' if want_fail else '成功'}；"
                  f"實際 {'失敗' if got else '成功'}"
                  f"{'，已回復' if got and restored else ''}")

    good = "import os\nimport sys\n\n\ndef f():\n    return 1\n"
    case("於頂層 import 之後插入 → 成功",
         good, lambda p: insert_module_import(p, "import json"), False)
    case("插入語法錯之行 → 失敗且回復",
         good, lambda p: insert_module_import(p, "import ("), True)
    case("無頂層 import → 拒絕（無明確節點邊界）",
         "def f():\n    return 1\n",
         lambda p: insert_module_import(p, "import os"), True)
    case("刪行後語法錯 → 失敗且回復",
         good, lambda p: drop_lines(p, [5]), True)
    print(f"\n  G165 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    print(__doc__.strip().split("\n")[0])


if __name__ == "__main__":
    main()
