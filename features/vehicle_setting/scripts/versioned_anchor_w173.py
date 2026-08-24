"""W-173 之錨點（R-VS54，兩側皆須有標的）—— **於暫存目錄為之**。

必命中（須 raise）：以現行任一批之**最大版號**為目標輸出
必不命中（須成功）：以 `_v{n+1}` 為目標輸出
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from versioned_out import (OverwriteRefused, next_version,  # noqa: E402
                           versions, write_versioned)


def main() -> int:
    tmp = Path(tempfile.mkdtemp()) / "generated"
    tmp.mkdir(parents=True)
    stem = "batch17"
    for _, p in versions(FEAT / "generated", stem):
        shutil.copy(p, tmp / p.name)
    have = [p.name for _, p in versions(tmp, stem)]
    print(f"暫存目錄之 `{stem}` 既有版本：{have}")

    payload = {"tcs": [], "batch": stem}
    ok = True

    # ── 必命中：以現行最大版號為目標 ───────────────────────────────
    cur_max = versions(tmp, stem)[-1][1]
    try:
        write_versioned(tmp, stem, payload, work_order="W-173",
                        ruling="R-VS81", target=cur_max)
        print(f"  必命中側：以 `{cur_max.name}` 為目標 —— **未 raise，錨點失效**")
        ok = False
    except OverwriteRefused as e:
        print(f"  必命中側：以 `{cur_max.name}` 為目標 —— **raise** ✅")
        print(f"      {e}")

    # ── 必不命中：以 _v{n+1} 為目標 ────────────────────────────────
    nxt, prev = next_version(tmp, stem)
    try:
        out = write_versioned(tmp, stem, payload, work_order="W-173",
                              ruling="R-VS81")
        rev = json.loads(out.read_text(encoding="utf-8"))["revision"]
        print(f"  必不命中側：輸出 `{out.name}` —— **成功** ✅")
        print(f"      revision: {rev}")
        assert out.name == nxt.name and prev is not None
    except OverwriteRefused as e:
        print(f"  必不命中側：**誤 raise，錨點失效** —— {e}")
        ok = False

    # ── R-VS81(2)：不以「內容相同」為由略過 ────────────────────────
    same = json.loads(cur_max.read_text(encoding="utf-8"))
    try:
        write_versioned(tmp, stem, same, work_order="W-173",
                        ruling="R-VS81", target=cur_max)
        print("  內容相同之覆蓋 —— **未 raise，違 R-VS81(2)**")
        ok = False
    except OverwriteRefused:
        print("  內容相同之覆蓋 —— **仍 raise** ✅（R-VS81(2)：不以內容相同為由略過）")

    print("  錨點：", "**兩側皆有標的，PASS**" if ok else "**FAIL**")
    print(f"  （暫存目錄 {tmp}；`generated/` 未動）")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
