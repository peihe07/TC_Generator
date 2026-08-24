"""W-160(2)（84 包 §5，R-VS77）—— R-VS6 之全母體回復。

55 輪之 D-5 只掃 `split_flag = true`（7 條），得 2 leaf。
**R-VS77 令回掃全母體** —— 225 條中 `test_item` 上半段非條文逐字者 **44**，
其分二類：

  (a) **僅實體解碼／空白差異** 27 —— `&lt;&gt;` → `<>`、`&amp;&amp;` → `&&`、
      `\\xa0` → 空白。**本層判其為「呈現」而非「改寫」**：來源文件所顯示之字元
      即 `<>`／`&&`，XML 之實體只是其編碼。**回復實體會使工作簿顯示原始實體，
      對讀者更差。** —— **不改，具名於上繳 §2**
  (b) **實質字詞改寫** 17 —— `HU`／`HU/CCDMR` → `HMI`、`When`／`Wherever`／`IF`
      → `If`、`THEN` → `then`、`Softkey button` → `softkey`、彎引號 → 直引號，
      另有數條其上半段取自條文之他句或漏其前言。**回復條文逐字。**

窄化（拆分者）之記述留於括號內之下半段，不動。
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches        # noqa: E402
from defect_scan_w157 import clause_of          # noqa: E402


def norm(x: str) -> str:
    """實體解碼 ＋ 空白正規化 —— 用以分辨 (a) 與 (b)。"""
    return re.sub(r"\s+", " ", html.unescape(x).replace("\xa0", " ")).strip()


def main() -> int:
    log, out = [], []
    for f in latest_batches():
        d = json.loads(f.read_text(encoding="utf-8"))
        touched = 0
        for t in d["tcs"]:
            cl = clause_of(t["leaf_id"])
            item = t.get("test_item", "") or ""
            upper, sep, lower = item.partition("\n\n(")
            upper = upper.strip()
            if not (cl and upper and upper not in cl):
                continue
            if norm(upper) in norm(cl):
                continue                      # (a) 僅實體／空白 —— 不改
            t["test_item"] = cl + (sep + lower if sep else "")
            touched += 1
            log.append(f"  {t['leaf_id']} [{f.name}] 上半段回復條文逐字（R-VS6）")
        if not touched:
            continue
        m = re.match(r"(batch\d+(?:_[a-z]+)?)(?:_v(\d+))?\.json$", f.name)
        nxt = f.parent / f"{m.group(1)}_v{int(m.group(2) or 1) + 1}.json"
        d["revision"] = ("W-160（56 輪，R-VS77 之首次全母體回掃）："
                         "`test_item` 上半段回復條文逐字（R-VS6）—— "
                         "55 輪之 D-5 只掃 `split_flag`，本輪掃全母體")
        nxt.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        out.append(nxt.name)
    print("產出：", out)
    print("\n".join(log))
    print(f"回復 **{len(log)}** 條")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
