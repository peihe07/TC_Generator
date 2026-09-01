#!/usr/bin/env python3
"""上繳前之必跑閘（26 包 §C 裁定 2；S3 啟用）。

依序跑各支、**逐支列出 exit code**、任一非零則總 exit 1。
FO §8.2 令上繳包附本工具之輸出。

| 閘 | 管什麼 |
|---|---|
| `lint_docs036.py --gate` | 治理三簿（裁決台帳／DATA_REQUESTS／ANOMALIES）之結構 |
| `canon_refs.py --waiver --gate` | canon 引用之唯一可解析（R-G18）|
| `rulings_hash.py --check` | 條文指紋表與現行條文相符（R-G13）|
| `gates_tsv.py --check` | 閘登錄簿與現行閘相符（R-G17）|
| `lint_paths.py --gate` | 產出物落點與 delivered/ 之 sha 對照（R-G25，27 包接入）|
| `lint_delivery_spec.py --gate` | 交付規格表（R-G42，73 包接入；基線內之檔只計警示）|

**`expected_numbers.py --gate` 不在其列**（26 包 §C 裁定 2）：其現為紅，
且成因為基準未落檔而非語料有誤。**先接一支已知會紅而被容忍之閘，
就是 G-D 之另一面** —— 一個永遠紅而無人處置之閘，與沒有這支閘，
在行為上相同。俟 seq 缺口結案且 pool 算式落檔後由 Pei 另裁。

**逐支列出而非只給總結果**：總 exit 1 說得出「有問題」，說不出「哪一支」。
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

GATES = [
    ("lint_docs036", ["scripts/lint_docs036.py", "--gate"]),
    ("canon_refs", ["scripts/canon_refs.py", "--waiver", "--gate"]),
    ("rulings_hash", ["scripts/rulings_hash.py", "--check"]),
    ("gates_tsv", ["scripts/gates_tsv.py", "--check"]),
    ("lint_paths", ["scripts/lint_paths.py", "--gate"]),
    ("lint_delivery_spec", ["scripts/lint_delivery_spec.py", "--gate"]),
]


def run_one(root: Path, argv: list[str]) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, *argv], cwd=root,
                          capture_output=True, text=True)
    tail = (proc.stdout.strip().splitlines() or [""])[-1]
    if proc.returncode != 0 and proc.stderr.strip():
        tail = proc.stderr.strip().splitlines()[-1]
    return proc.returncode, tail


def main() -> int:
    ap = argparse.ArgumentParser(description="上繳前必跑閘（S3）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--verbose", action="store_true", help="附各閘之完整輸出")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    results = []
    for name, argv in GATES:
        code, tail = run_one(root, argv)
        results.append((name, code, tail))
        mark = "PASS" if code == 0 else "**FAIL**"
        print(f"{mark:<9} exit {code:<3} {name:<16} {tail}")
        if args.verbose:
            proc = subprocess.run([sys.executable, *argv], cwd=root,
                                  capture_output=True, text=True)
            for line in (proc.stdout + proc.stderr).splitlines():
                print(f"           {line}")

    bad = [n for n, c, _ in results if c != 0]
    print()
    if bad:
        print(f"總判：**FAIL** —— {len(bad)} 支未過：{'、'.join(bad)}")
        print("依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。")
        return 1
    print(f"總判：PASS —— {len(results)} 支全過")
    return 0


if __name__ == "__main__":
    sys.exit(main())
