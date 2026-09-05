#!/usr/bin/env python3
"""產出物落點檢查（R-G64）。

R-G64 之政策**自生效日管新檔；既有檔案不搬移**——故本工具以一份
基線（`docs/fw036/PATH_POLICY_BASELINE.tsv`）記下生效日當時之全部
不符落點，其後只對**基線外**之路徑判紅。基線**只減不增**：
既有檔案被搬到合規落點後自基線消失，新違規則無處可躲。

另檢 `delivered/` 之 sha 對照（R-G64 末句）：
每個 `delivered/*.xlsx` 須於同目錄 `MANIFEST.tsv` 有列且 sha256 相符。

唯讀；`--emit-baseline` 時只寫基線 tsv。
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

BASELINE_DEFAULT = "docs/fw036/PATH_POLICY_BASELINE.tsv"
BASELINE_COLUMNS = ("path", "suffix", "reason")
MANIFEST_NAME = "MANIFEST.tsv"

# R-G64 之表：各副檔名於 `features/<f>/` 下之合法第一層目錄。
# `inputs/` 為來源投遞之最終落點（R-G63 附記），非產出物，一併視為合法。
# `docs/`／`scripts/`／`forms/` 非產出物目錄，其下之檔不入本檢查。
# `sandbox/` 為作業區，三種副檔名皆容——R-G64 之表對其只限定 xlsx 之
# **可改處**，未限定其內容型別。不予放行者，基線會吞下 698 個正常之
# sandbox 工作檔，而基線一大就沒有人看得出新違規（G-D 之同一形態）。
ALLOWED = {
    ".json": {"generated", "data", "inputs", "sandbox"},
    ".xlsx": {"sandbox", "delivered", "inputs"},
    ".tsv": {"data", "delivered", "reports", "sandbox"},
}
EXEMPT_TOPS = {"docs", "scripts", "forms", "output", "_intake"}
SKIP_PARTS = {".git", "__pycache__", ".venv", "node_modules"}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def feature_artifacts(root: Path):
    """逐一產出 `(相對路徑, feature, 第一層目錄, 副檔名)`。"""
    for path in sorted((root / "features").rglob("*")):
        if not path.is_file() or SKIP_PARTS & set(path.parts):
            continue
        rel = path.relative_to(root)
        parts = rel.parts                       # features/<f>/<top>/...
        if len(parts) < 4:
            continue
        suffix = path.suffix.lower()
        if suffix not in ALLOWED or parts[2] in EXEMPT_TOPS:
            continue
        yield rel, parts[1], parts[2], suffix


def offenders(root: Path) -> list[tuple[str, str, str]]:
    out = []
    for rel, _feature, top, suffix in feature_artifacts(root):
        if top not in ALLOWED[suffix]:
            out.append((str(rel), suffix,
                        f"{suffix} 之合法落點為 {sorted(ALLOWED[suffix])}，實為 {top}/"))
    return out


def load_baseline(path: Path) -> set[str]:
    if not path.exists():
        return set()
    rows = path.read_text(encoding="utf-8").splitlines()[1:]
    return {r.split("\t")[0] for r in rows if r.strip()}


def check_delivered(root: Path) -> list[str]:
    """`delivered/` 之 sha 對照（R-G64 末句）。"""
    problems: list[str] = []
    for manifest in sorted(root.glob("features/*/delivered/" + MANIFEST_NAME)):
        folder = manifest.parent
        rows = manifest.read_text(encoding="utf-8").splitlines()
        listed: dict[str, str] = {}
        for row in rows[1:]:
            if not row.strip():
                continue
            cells = row.split("\t")
            if len(cells) < 2:
                problems.append(f"{manifest.relative_to(root)}：列欄數不足 —— {row[:60]!r}")
                continue
            listed[cells[0]] = cells[1]
        for name, sha in listed.items():
            target = folder / name
            if not target.exists():
                problems.append(f"{folder.relative_to(root)}/{name}：對照表有列而檔不存在")
            elif sha256_of(target) != sha:
                problems.append(f"{folder.relative_to(root)}/{name}：sha256 與對照表不符")
        for book in sorted(folder.glob("*.xlsx")):
            if book.name not in listed:
                problems.append(f"{book.relative_to(root)}：delivered/ 內而對照表未列")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="產出物落點檢查（R-G64）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--baseline", default=BASELINE_DEFAULT)
    ap.add_argument("--emit-baseline", action="store_true",
                    help="以現況產出基線（生效日一次性；其後只減不增）")
    ap.add_argument("--gate", action="store_true", help="有基線外違規時 exit 1")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    bad = offenders(root)

    if args.emit_baseline:
        out = root / args.baseline
        out.parent.mkdir(parents=True, exist_ok=True)
        body = "\n".join(["\t".join(BASELINE_COLUMNS)]
                         + ["\t".join(r) for r in bad]) + "\n"
        out.write_text(body, encoding="utf-8")
        print(f"寫入基線 {args.baseline}：{len(bad)} 列（既有不符落點，不搬移）")
        return 0

    baseline = load_baseline(root / args.baseline)
    fresh = [r for r in bad if r[0] not in baseline]
    stale = sorted(baseline - {r[0] for r in bad})
    delivered = check_delivered(root)

    print(f"落點檢查：掃得不符 {len(bad)} 筆，基線 {len(baseline)} 列，"
          f"**基線外 {len(fresh)}**")
    for path, _suffix, reason in fresh:
        print(f"  紅  {path}\n      {reason}")
    if stale:
        print(f"  基線已消解 {len(stale)} 列（檔已搬走或刪除，得自基線移除）")
    print(f"delivered/ sha 對照：{'OK' if not delivered else f'{len(delivered)} 筆不符'}")
    for problem in delivered:
        print(f"  紅  {problem}")

    fail = len(fresh) + len(delivered)
    print(f"\n{'FAIL' if fail else 'PASS'}: 基線外違規 + delivered 不符 = {fail}")
    return 1 if (args.gate and fail) else 0


if __name__ == "__main__":
    sys.exit(main())
