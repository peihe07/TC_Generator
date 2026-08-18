"""G160 —— 不可再生產物之寫入保護（R-P233）。

32 §一與 §九第 3 項：`edit_integrity_baseline.json` 屬 (c) 時點相依型 ——
**其為 G108 之基準，重跑即等於重設基準，其後任何損壞都不會被攔下，
且不會有人發現**。31 包之全掃未及於它，**係因其產生腳本不在當時之清單內
—— 是運氣不是流程**。

判準（R-P233(d)）：**凡「其價值來自記錄某一時點」者皆屬之** ——
baseline、before-snapshot、dry-run 結果、對照表。

保護（R-P233(b)）：其產生腳本執行前須檢查該產物是否已存在；
**已存在者拒寫並回報**，除非帶明示之覆寫參數 `--overwrite-protected`。

`edit_integrity_baseline.json` 另加一層（R-P233(c)）：
其重設須留下**重設紀錄**（時點、重設前後之雜湊），使「基準何時被重設」可事後查核。

用法（供其他腳本匯入）：
    from protect_products import guard_write
    guard_write(path)          # 於 write_text 之前呼叫

自檢：
    python features/power/scripts/protect_products.py --self-test
"""

from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
RESET_LOG = DATA / "edit_integrity_reset_log.tsv"

# (c) 時點相依型產物 —— 與 `classify_products.py` 之判類一致（12 份）。
PROTECTED = {
    "b4_material.md", "b5_material.md", "b4_batch2_snapshot.md",
    "b1_before16.json", "b1_before17.json", "b2_before13.json",
    "b2_before15.json", "b3_before14.json", "b3_dryrun.json",
    "b2b3_writeback_path.json", "edit_integrity_baseline.json",
    "final_tc_id_map.tsv",
}
OVERRIDE = "--overwrite-protected"


class ProtectedWrite(Exception):
    """對已存在之 (c) 型產物之寫入嘗試。"""


def guard_write(path: Path, argv: list[str] | None = None) -> None:
    """(c) 型產物已存在且未帶明示覆寫參數者 → 拒寫並回報。"""
    argv = sys.argv if argv is None else argv
    if path.name not in PROTECTED or not path.exists():
        return
    if OVERRIDE in argv:
        print(f"  **覆寫受保護之產物**（{OVERRIDE} 已指定）：{path.name}")
        return
    raise ProtectedWrite(
        f"**拒寫** `{path.name}` —— 其為 (c) 時點相依型產物（R-P233），"
        f"已存在且未帶 `{OVERRIDE}`。\n"
        f"        其價值來自記錄某一時點，重寫即摧毀該紀錄；"
        f"若確需重設，請帶 `{OVERRIDE}` 並於上繳說明其理由。")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "（不存在）"


def log_baseline_reset(before: str, after: str, note: str = "") -> None:
    """R-P233(c)：基準重設之紀錄（時點、前後雜湊），append-only。"""
    new = not RESET_LOG.exists()
    with RESET_LOG.open("a", encoding="utf-8") as f:
        if new:
            f.write("utc\tbefore_sha256\tafter_sha256\tnote\n")
        f.write(f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\t"
                f"{before}\t{after}\t{note}\n")


def self_test() -> int:
    import tempfile
    failures = 0

    def case(label: str, name: str, exists: bool, argv: list[str], want_raise: bool):
        nonlocal failures
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / name
            if exists:
                p.write_text("x", encoding="utf-8")
            try:
                guard_write(p, argv)
                got = False
            except ProtectedWrite:
                got = True
            ok = got == want_raise
            failures += not ok
            print(f"  [{'PASS' if ok else '**FAIL**'}] G160 {label}")
            print(f"          期望 {'拒寫' if want_raise else '放行'}；"
                  f"實際 {'拒寫' if got else '放行'}")

    case("(c) 型且已存在、無覆寫參數 → 拒寫",
         "edit_integrity_baseline.json", True, [], True)
    case("(c) 型且已存在、帶覆寫參數 → 放行",
         "edit_integrity_baseline.json", True, [OVERRIDE], False)
    case("(c) 型但不存在（首次產生）→ 放行",
         "b4_material.md", False, [], False)
    case("非 (c) 型且已存在 → 放行",
         "g150_design_method.md", True, [], False)
    print(f"\n  G160 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    print(f"受保護之 (c) 型產物：{len(PROTECTED)}")
    for n in sorted(PROTECTED):
        p = DATA / n
        print(f"  {'存在' if p.exists() else '不存在'}  {n}")


if __name__ == "__main__":
    main()
