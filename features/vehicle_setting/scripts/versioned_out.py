"""R-VS81（89 包 §2）—— 生成器與修正腳本之輸出**須帶版號、不得覆蓋**。

R-VS81 逐字：

  (1) 輸出前先掃 `generated/` 之同批既有版本，取其最大版號 `n`，
      輸出至 `_v{n+1}`（首次輸出為無後綴之基準檔）
  (2) 目標檔已存在者，**raise，不覆蓋** —— 不以「內容相同」為由略過
  (3) 其 `revision` 記其作業號、所依條文、**及其所本之前版檔名**

**其解 R-VS53 與 R-VS80 之衝突**：改生成器後重跑者，其產出為新版，
前版保留 —— 可重製性與不可就地改二者同時成立。
"""
from __future__ import annotations

import json
import re
from pathlib import Path


class OverwriteRefused(Exception):
    """目標檔已存在 —— R-VS81(2)：raise，不覆蓋，不以內容相同為由略過。"""


def versions(gen_dir: Path, stem: str) -> list[tuple[int, Path]]:
    """該批之既有版本，依版號升冪。基準檔（無後綴）計為版 1。"""
    out = []
    for p in gen_dir.glob(f"{stem}*.json"):
        m = re.fullmatch(rf"{re.escape(stem)}(?:_v(\d+))?\.json", p.name)
        if m:
            out.append((int(m.group(1) or 1), p))
    return sorted(out)


def next_version(gen_dir: Path, stem: str) -> tuple[Path, Path | None]:
    """（下一版之路徑, 其所本之前版）—— R-VS81(1)。

    無既有版本者，下一版即基準檔 `{stem}.json`，其前版為 None。
    """
    vs = versions(gen_dir, stem)
    if not vs:
        return gen_dir / f"{stem}.json", None
    n, prev = vs[-1]
    return gen_dir / f"{stem}_v{n + 1}.json", prev


def write_versioned(gen_dir: Path, stem: str, data: dict, *,
                    work_order: str, ruling: str,
                    target: Path | None = None) -> Path:
    """依 R-VS81 寫出。`target` 得指定（供錨點測其拒絕覆蓋之行為）。"""
    nxt, prev = next_version(gen_dir, stem)
    if target is not None:
        nxt = Path(target)
    if nxt.exists():
        raise OverwriteRefused(
            f"R-VS81(2)：`{nxt.name}` 已存在，拒絕覆蓋。"
            f"其下一可用版為 `{next_version(gen_dir, stem)[0].name}`")
    # (3) revision 記作業號、所依條文、所本之前版
    data = {**data, "revision": f"{work_order}：依 {ruling}；"
                                f"所本之前版 `{prev.name if prev else '（無，本批首版）'}`"}
    nxt.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return nxt
