#!/usr/bin/env python3
"""工作區清理候選（R-G65，27 包 §D-6）。

**本工具不刪任何檔。** 其只做三件事：

1. **列候選** —— 被同目錄更高版取代之產出、帶作廢標記之檔、被同名新報告
   取代之舊 lint 報告
2. **引用懸空檢查** —— 候選之檔名若被現行治理面（`RULINGS.md`／
   `ANOMALIES.md`／`DATA_REQUESTS.md`／`DECISIONS.md`／waiver／各對照表／
   兩 canon）指名，即**不得移除**，逐筆載明其引用處
3. **既有懸空之具名回報** —— 治理面指名而檔已不存在者（27 包 §F-5：
   既有懸空，非本包所致，具名回報不修）

刪除由 Pei 依清單以**專門 commit** 為之（R-G26）。
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# 首輪範圍：已結案 feature（27 包 §D-6）。`vehicle_setting` 延至 V33 收訖。
CLOSED_DEFAULT = ["amfm", "power_moding", "home", "media", "projection", "power"]

GOVERNANCE_NAMES = {"RULINGS.md", "ANOMALIES.md", "DATA_REQUESTS.md", "DECISIONS.md"}
GOVERNANCE_EXTRA = [
    "docs/fw036/FEATURE_ONBOARDING.md",
    "docs/runtime/ASPICE_SWE6_AI_Instruction.md",
    "docs/fw036/CANON_REFS_WAIVER.tsv",
    "docs/fw036/RULINGS.sha.tsv",
    "docs/runtime/GATES.tsv",
]
# 版本家族：`<stem>_v3.json`／`<stem>-v3.json`／`<stem>.v3.json`
RE_VERSIONED = re.compile(r"^(?P<stem>.+?)[._-]v(?P<n>\d+)(?P<ext>\.[A-Za-z0-9]+)$")
RE_DEAD_MARK = re.compile(r"SUPERSEDED|DEPRECATED|_old|_bak|_backup", re.IGNORECASE)
# 治理面之路徑式引用（反引號內）
RE_PATH_TOKEN = re.compile(r"`([\w][\w./-]*\.(?:json|tsv|md|xlsx|py|ya?ml))`")

SKIP_PARTS = {".git", "__pycache__", ".venv", "node_modules", "output"}
CANDIDATE_SUFFIXES = {".json", ".tsv", ".md"}


def tracked_files(root: Path, feature: str) -> list[Path]:
    base = root / "features" / feature
    return [p for p in sorted(base.rglob("*"))
            if p.is_file() and not SKIP_PARTS & set(p.parts)]


def candidates_of(root: Path, feature: str) -> list[tuple[Path, str]]:
    """回傳 `(路徑, 成為候選之理由)`。"""
    files = tracked_files(root, feature)
    out: list[tuple[Path, str]] = []

    families: dict[tuple[Path, str, str], list[tuple[int, Path]]] = defaultdict(list)
    for path in files:
        if path.suffix.lower() not in CANDIDATE_SUFFIXES:
            continue
        if RE_DEAD_MARK.search(path.name):
            out.append((path, "檔名帶作廢標記"))
            continue
        m = RE_VERSIONED.match(path.name)
        if m:
            families[(path.parent, m.group("stem"), m.group("ext"))].append(
                (int(m.group("n")), path))

    for (_parent, stem, ext), members in sorted(families.items()):
        if len(members) < 2:
            continue                                    # 單一版本者非「被取代」
        members.sort()
        newest = members[-1][1].name
        for _n, path in members[:-1]:
            out.append((path, f"同目錄有更高版 {newest}（家族 {stem}{ext}）"))

    return sorted(set(out))


def governance_surface(root: Path) -> list[Path]:
    surface = [root / rel for rel in GOVERNANCE_EXTRA]
    for path in sorted(root.glob("features/*/*")):
        if path.name in GOVERNANCE_NAMES:
            surface.append(path)
    for path in sorted(root.glob("features/*/delivered/MANIFEST.tsv")):
        surface.append(path)
    return [p for p in surface if p.exists()]


def index_references(root: Path) -> dict[str, list[str]]:
    """治理面所指名之檔名 -> 其引用處（`檔:行`）。以 basename 為鍵。"""
    index: dict[str, list[str]] = defaultdict(list)
    for doc in governance_surface(root):
        try:
            lines = doc.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        rel = doc.relative_to(root)
        for lineno, line in enumerate(lines, 1):
            for token in RE_PATH_TOKEN.findall(line):
                name = Path(token).name
                if name[: name.rfind(".")].isdigit():
                    continue        # `gen_batch04/05/06.py` 之 `06.py` —— 簡寫碎片非檔名
                index[name].append(f"{rel}:{lineno}")
    return index


def dangling(root: Path, index: dict[str, list[str]]) -> list[tuple[str, str]]:
    """治理面指名而全 repo 找不到同名檔者（§F-5，具名回報不修）。"""
    # **`output/` 不在此處排除** —— 其不入版控，但檔仍在盤上；
    # 排除者會把 `features/privacy/output/x.xlsx` 這種活引用誤報為懸空。
    skip = SKIP_PARTS - {"output"}
    present = {p.name for p in root.rglob("*")
               if p.is_file() and not skip & set(p.parts)}
    out = []
    for name, where in sorted(index.items()):
        if name not in present:
            out.append((name, where[0] + (f"（共 {len(where)} 處）" if len(where) > 1 else "")))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="工作區清理候選（R-G65）；本工具不刪檔")
    ap.add_argument("--root", default=".")
    ap.add_argument("--feature", action="append", default=None,
                    help="指定 feature（可重複）；預設為已結案六線")
    ap.add_argument("--out", default=None, help="候選清單輸出 tsv")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    features = args.feature or CLOSED_DEFAULT
    index = index_references(root)
    same_name: dict[str, int] = defaultdict(int)
    for path in root.rglob("*"):
        if path.is_file() and not SKIP_PARTS & set(path.parts):
            same_name[path.name] += 1

    rows: list[tuple[str, str, str, str]] = []
    for feature in features:
        if not (root / "features" / feature).is_dir():
            rows.append((feature, "—", "未掃", "feature 目錄不存在"))
            continue
        found = candidates_of(root, feature)
        if not found:
            rows.append((feature, "—", "無候選", "已掃，無符合 R-G26 之候選"))
            continue
        for path, reason in found:
            rel = str(path.relative_to(root))
            where = index.get(path.name, [])
            verdict = "留（被引用）" if where else "可移除"
            note = reason + ("；引用於 " + "／".join(where[:3]) if where else "")
            if where and same_name.get(path.name, 0) > 1:
                note += (f"；**同名檔全 repo 有 {same_name[path.name]} 份**，"
                         "引用比對以檔名為之，此筆之「被引用」為保守判定")
            rows.append((feature, rel, verdict, note))

    print(f"清理候選（首輪範圍 {len(features)} 線）—— **本工具不刪檔**")
    for feature, rel, verdict, note in rows:
        print(f"  {verdict:<12} {feature:<14} {rel}")
        print(f"               {note}")
    removable = [r for r in rows if r[2] == "可移除"]
    print(f"\n可移除 {len(removable)} 檔；留（被引用）"
          f"{sum(1 for r in rows if r[2].startswith('留'))} 檔；實刪 0")

    hanging = dangling(root, index)
    print(f"\n既有引用懸空 {len(hanging)} 筆（§F-5：具名回報，本包不修）")
    for name, where in hanging:
        print(f"  {name:<44} {where}")

    if args.out:
        out = root / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        body = "\n".join(["\t".join(("feature", "path", "verdict", "note"))]
                         + ["\t".join(r) for r in rows]) + "\n"
        out.write_text(body, encoding="utf-8")
        print(f"\n寫入 {args.out}：{len(rows)} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
