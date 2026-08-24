"""W-167／W-169 —— R-VS6 之 **L3 驗**（87 包 §5；88 包 §2.1 改全量）。

R-VS79 之三層：
  L1 產物 ↔ 解析結果（兩側同解析層，其偏差不可見）
  L2 產物 ↔ 原始文件
  **L3 解析結果 ↔ 原始文件 —— 驗解析層本身**

本檔以 `zipfile` 直讀 `word/document.xml`，**不經 `inscope_w39`**，
自其 `<w:t>` 重建段落文字，與 `blocks_with_sec()` 所得之條文逐字比對。

**W-169（88 包 §2.1）**：R-VS79 之「至少一次抽驗」已改為「**全量驗**」——
其理由為「不可見的東西，抽 10 條看不見它，和它不存在，是兩回事」。
故本檔預設**全量**（225 條）；傳入整數引數則退回抽樣（保留 W-167 之可重跑性）。
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches      # noqa: E402
from defect_scan_w157 import clause_of, L2R   # noqa: E402

DOCX = FEAT / ("inputs/R1LR_Atl-H_25PI3.5_Activation and Configuration_"
               "CFTS_044_Vehicle Controls_SR26_20250909-1816.docx")


def raw_paragraphs() -> list[str]:
    """直讀 `word/document.xml`，自 `<w:t>` 重建段落 —— **不經既有解析層**。"""
    with zipfile.ZipFile(DOCX) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        txt = "".join(re.findall(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", p, re.S))
        txt = txt.replace("<w:tab/>", "\t")
        if txt.strip():
            out.append(txt)
    return out


def norm(x: str) -> str:
    """比較用之正規化 —— **只壓空白**，不還原實體、不動標點。

    實體之處置為兩側之別本身：`document.xml` 之 `<w:t>` 內文為 XML 實體形式，
    與 `blocks_with_sec()` 所存者同源，故此處不解實體 —— **若解，即掩蓋其別**。
    """
    return re.sub(r"\s+", " ", x.replace("\xa0", " ")).strip()


def main() -> int:
    tcs = []
    for f in latest_batches():
        tcs += json.loads(f.read_text(encoding="utf-8"))["tcs"]
    tcs.sort(key=lambda t: (t["leaf_id"], t["tc_title"]))
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if n:
        step = len(tcs) // n
        sample, how = [tcs[i * step] for i in range(n)], f"等距取 {n}（步長 {step}）"
    else:
        sample, how = tcs, "**全量**"

    paras = raw_paragraphs()
    joined = norm(" ".join(paras))

    print(f"R-VS79 之 L3 驗 —— 母體 {len(tcs)} 條，{how}")
    print(f"原始文件：`{DOCX.name}`（{len(paras)} 段，直讀 `word/document.xml`）\n")
    bad = 0
    for i, t in enumerate(sample, 1):
        leaf = t["leaf_id"]
        parsed = clause_of(leaf)
        reqid = re.findall(r"\d{7}", L2R.get(leaf, {}).get("reqid_list", ""))
        rid = reqid[0] if reqid else "—"
        if not parsed:
            print(f"{i:2d}. {leaf}  [{rid}]  —— 無解析所得之條文，略過")
            continue
        hit = norm(parsed) in joined
        if not hit or n:
            print(f"{i:2d}. {leaf}  [{rid}]  "
                  f"{'✅ 逐字命中' if hit else '❌ 不符'}")
        if not hit:
            bad += 1
            n = norm(parsed)
            # 自首字起逐段延長，找其首次失配之位置
            lo, hi = 0, len(n)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if n[:mid] in joined:
                    lo = mid
                else:
                    hi = mid - 1
            print(f"      首次失配於第 {lo} 字元")
            print(f"      解析所得 …{n[max(0, lo - 40):lo + 40]}…")
            near = [p for p in paras if norm(p)[:30] == n[:30]]
            if near:
                m = norm(near[0])
                print(f"      原始文件 …{m[max(0, lo - 40):lo + 40]}…")
            else:
                print("      原始文件：無以相同前 30 字起首之段落")
    print(f"\n命中 **{len(sample) - bad}** ／ 不符 **{bad}** ／ 共 {len(sample)}")
    if bad:
        print("**R-VS6 之全部結論須加註其前提不成立**（R-VS79）")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
