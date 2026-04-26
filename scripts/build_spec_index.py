#!/usr/bin/env python3
"""離線預處理 SYS1/HMI spec xlsx：解析 + 算 embedding → 輸出 JSON 快取。

典型用法
--------
預處理所有 ``spec-index/cache/`` 下的 xlsx（JSON 快取舊於 xlsx 時才重算）：

    python scripts/build_spec_index.py

只處理指定檔案：

    python scripts/build_spec_index.py spec-index/cache/SYS1_HMI_Comfort_*.xlsx

強制重算全部（例如換 embedding 模型後）：

    python scripts/build_spec_index.py --force

只解析不算 embedding（省錢、僅得 Jaccard 級比對）：

    python scripts/build_spec_index.py --no-embed
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# 允許從 repo 根目錄直接執行
ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

from spec_matcher import (  # noqa: E402
    DEFAULT_EMBEDDING_MODEL,
    attach_embeddings,
    build_spec_index,
    is_index_fresh,
    save_spec_index,
    update_manifest,
)


DEFAULT_CACHE_DIR = ROOT / "spec-index" / "cache"
MANIFEST_PATH = ROOT / "spec-index" / "manifest.json"


def _resolve_inputs(paths: list[str], cache_dir: Path) -> list[Path]:
    """未指定檔案時掃 cache_dir；指定時轉成絕對路徑並排除非 xlsx。"""
    if paths:
        resolved = [Path(p).resolve() for p in paths]
    else:
        resolved = sorted(cache_dir.glob("*.xlsx"))
    return [p for p in resolved if p.suffix.lower() == ".xlsx" and p.exists()]


def process_one(
    xlsx_path: Path,
    *,
    model: str,
    embed: bool,
    force: bool,
    manifest_path: Path,
) -> str:
    """處理單一 xlsx，回傳狀態字串供 log。"""
    index_path = xlsx_path.with_suffix(".json")
    if not force and is_index_fresh(xlsx_path, index_path):
        return f"skip  (fresh)    {xlsx_path.name}"

    index = build_spec_index(str(xlsx_path))
    if embed:
        attach_embeddings(index, model=model)

    save_spec_index(
        index,
        index_path,
        name=xlsx_path.stem,
        source_file=xlsx_path,
    )
    update_manifest(
        manifest_path,
        name=xlsx_path.stem,
        source_file=xlsx_path.name,
        entries_count=len(index.entries),
        embedding_model=index.embedding_model,
    )
    tag = "embed" if embed else "parse"
    return f"{tag:<5} ({len(index.entries):4d} rows) {xlsx_path.name}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "paths",
        nargs="*",
        help="要處理的 xlsx 檔；未指定則處理 spec-index/cache/*.xlsx",
    )
    parser.add_argument(
        "--cache-dir",
        default=str(DEFAULT_CACHE_DIR),
        help=f"預設掃描資料夾（預設：{DEFAULT_CACHE_DIR.relative_to(ROOT)}）",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_EMBEDDING_MODEL,
        help=f"embedding 模型名稱（預設：{DEFAULT_EMBEDDING_MODEL}）",
    )
    parser.add_argument(
        "--no-embed",
        dest="embed",
        action="store_false",
        help="只解析不算 embedding",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="忽略 mtime 比較，強制重算",
    )
    args = parser.parse_args()

    cache_dir = Path(args.cache_dir).resolve()
    inputs = _resolve_inputs(args.paths, cache_dir)
    if not inputs:
        print(f"No xlsx files found under {cache_dir}", file=sys.stderr)
        return 1

    if args.embed and not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not set. Use --no-embed to skip embedding.", file=sys.stderr)
        return 2

    print(f"Processing {len(inputs)} file(s)  model={args.model}  embed={args.embed}  force={args.force}")
    failures = 0
    for xlsx in inputs:
        try:
            msg = process_one(
                xlsx,
                model=args.model,
                embed=args.embed,
                force=args.force,
                manifest_path=MANIFEST_PATH,
            )
            print(f"  {msg}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL  {xlsx.name}: {exc}", file=sys.stderr)

    print(f"Done. manifest: {MANIFEST_PATH.relative_to(ROOT)}")
    return 0 if failures == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
