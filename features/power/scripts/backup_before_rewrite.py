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
    python features/power/scripts/backup_before_rewrite.py            # 備份 data/ + generated/ + scripts/
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

# R-P234（33 包）：備份範圍擴及 `generated/` 與 `scripts/`。
# 32 包所持之二理由已被否決 ——
#   `generated/`：「已入版控」意味損壞後須以 git 還原，而 R-P228 正為使 git
#                 不再是唯一退路而設；其 TC 內容為本 feature 之**主產出**
#   `scripts/`  ：G108 掌管者為**語法與符號完整性**，非其內容之正確性 ——
#                 「改壞了但仍能載入」G108 攔不住
DIRS = ("data", "generated", "scripts")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def make(label: str | None = None) -> Path:
    label = label or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = BACKUP / label
    dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for d in DIRS:
        src_dir = POWER / d
        if not src_dir.exists():
            continue
        (dest / d).mkdir(parents=True, exist_ok=True)
        for p in sorted(src_dir.iterdir()):
            if not p.is_file() or p.name == "__pycache__":
                continue
            shutil.copy2(p, dest / d / p.name)
            rows.append((f"{d}/{p.name}", sha(p), p.stat().st_size))
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
    todo = names or [f"{d}/{p.name}" for d in DIRS
                     if (dest / d).exists() for p in (dest / d).iterdir()]
    for rel in todo:
        rel = rel if "/" in rel else f"data/{rel}"
        src = dest / rel
        if not src.exists():
            print(f"  **備份中無** {rel}")
            continue
        shutil.copy2(src, POWER / rel)
        print(f"  還原 {rel}")


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
