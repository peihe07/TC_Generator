"""G157 —— 改寫前備份（R-P228）。

31 包執行 R-P225 之全掃重跑時毀損 `b4_material.md` / `b5_material.md`，
執行層以 `git restore` 還原 —— 其成因為分析層之指令（R-P227 已認），
**惟 R-P228 明訂往後不得以 git 為退路**：

  (a) 任何可能改寫既有產物之操作（重跑、批次改寫、格式轉換），
      **執行前須先將受影響檔案複製至 `sandbox/`**（不入版控）
  (b) 損壞時**自該備份還原**，不動 git
  (c) 無備份而已損壞者 → **停並回報**
  (d) R-P149 對「自造損壞」之禁令不變

「**版本控管本不應承擔作業安全網之角色**」（R-P228 逐字）。

備份形式：`sandbox/backup/<UTC 時戳>/<原相對路徑>`，並附 `MANIFEST.tsv`
（相對路徑、SHA256、位元組數），供 `--verify` 與 `--restore` 使用。
`sandbox/` 不入版控（其已存在於本 repo 且未被追蹤）。

用法：
    python features/power/scripts/backup_before_rewrite.py            # 備份 data/ 全部
    python features/power/scripts/backup_before_rewrite.py --verify <標籤>
    python features/power/scripts/backup_before_rewrite.py --restore <標籤> [檔名…]
    python features/power/scripts/backup_before_rewrite.py --list
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
POWER = ROOT / "features/power"
DATA = POWER / "data"
BACKUP = POWER / "sandbox" / "backup"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def make(label: str | None = None) -> Path:
    label = label or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = BACKUP / label
    (dest / "data").mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(DATA.iterdir()):
        if not p.is_file():
            continue
        shutil.copy2(p, dest / "data" / p.name)
        rows.append((f"data/{p.name}", sha(p), p.stat().st_size))
    (dest / "MANIFEST.tsv").write_text(
        "path\tsha256\tbytes\n" + "".join(f"{a}\t{b}\t{c}\n" for a, b, c in rows),
        encoding="utf-8")
    print(f"備份 {len(rows)} 檔 → {dest.relative_to(ROOT)}")
    return dest


def verify(label: str) -> int:
    dest = BACKUP / label
    bad = 0
    for line in (dest / "MANIFEST.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        rel, h, n = line.split("\t")
        cur = POWER / rel
        if not cur.exists():
            print(f"  **缺失** {rel}")
            bad += 1
        elif sha(cur) != h:
            print(f"  **相異** {rel}（備份 {h[:12]}… vs 現況 {sha(cur)[:12]}…）")
            bad += 1
    print(f"\n比對 {label}：{'**全數相同**' if not bad else f'**{bad} 檔相異或缺失**'}")
    return bad


def restore(label: str, names: list[str]) -> None:
    dest = BACKUP / label
    todo = names or [p.name for p in (dest / "data").iterdir()]
    for n in todo:
        src = dest / "data" / n
        if not src.exists():
            print(f"  **備份中無** {n}")
            continue
        shutil.copy2(src, DATA / n)
        print(f"  還原 data/{n}")


def main() -> None:
    a = sys.argv[1:]
    if not a:
        make()
    elif a[0] == "--list":
        for d in sorted(BACKUP.glob("*")):
            n = len((d / "MANIFEST.tsv").read_text(encoding="utf-8").splitlines()) - 1
            print(f"  {d.name}  {n} 檔")
    elif a[0] == "--verify":
        raise SystemExit(1 if verify(a[1]) else 0)
    elif a[0] == "--restore":
        restore(a[1], a[2:])
    else:
        raise SystemExit(f"未知參數：{a[0]}")


if __name__ == "__main__":
    main()
