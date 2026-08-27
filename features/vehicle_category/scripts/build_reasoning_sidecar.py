#!/usr/bin/env python3
"""`reasoning` 側檔之產出與對應驗證（下放包 28 §2.2，T150）。

**為何另立側檔**（下放包 28 §2.2 之裁定）：
  - 併入 `AH 備註` 不採 —— `AH` 為**執行階段欄位**（測試員填），
    寫入我方內容混淆欄位所有權；且 `reasoning` 為繁中，
    而工作簿 TC 欄位為 English only（IN §1），混入破壞語言規則。
  - 不隨工作簿交付不採 —— 違 IN §10.4 之用意（audit trail）。

**鍵之形態**：`leaf_id#n` —— `n` 自 1 起，為該 leaf 於其批內之 TC 序。
拆分筆因此可區分（`SWE1-HMI-VC-038-03#1`／`#2`）。

**對應之可機械驗證**（§2.2 第三項）：側檔之鍵集合須等於
六批 JSON 展開後之鍵集合。本檔之 `--verify` 即為之，
且**它是雙向比對**：側檔多一鍵與少一鍵都 FAIL。

`split_flag`／`split_reason` **不入側檔**（profile §11：其資訊由
`split_delta` 與 req_id 重複承載；入側檔即第二來源）。
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
OUT = ROOT / "docs/REASONING_sidecar.md"
BATCH_ORDER = ["pilot_glovebox", "batch1_category_structure",
               "batch2_settings_list", "batch3_controls",
               "batch4_settings_behavior", "batch5_ignition_availability"]


def load():
    """[(key, batch, tc), …]，順序 = 批序 ＋ 批內原序。"""
    rows = []
    for name in BATCH_ORDER:
        p = GEN / f"{name}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text("utf-8"))
        seen: Counter = Counter()
        for t in d["tcs"]:
            seen[t["leaf_id"]] += 1
            rows.append((f'{t["leaf_id"]}#{seen[t["leaf_id"]]}', d["batch"], t))
    return rows


def build(rows):
    L = [
        "# `reasoning` 側檔 —— Vehicle Category\n",
        "> **隨工作簿一併交付**（下放包 28 §2.2）。",
        "> 工作簿之 TC 欄位為 English only（IN §1）；本檔為繁中之判讀紀錄，"
        "故不入工作簿而另立。\n",
        f"- 產出：`scripts/build_reasoning_sidecar.py`，下放包 28 T150",
        f"- 鍵：`leaf_id#n`，`n` 為該 leaf 於其批內之 TC 序（拆分筆據此區分）",
        f"- 筆數：**{len(rows)}**，與六批 JSON 之 TC 總數相同（`--verify` 驗之）",
        "- `split_flag`／`split_reason` 不入本檔（profile §11）\n",
        "---\n",
    ]
    cur = None
    for key, batch, t in rows:
        if batch != cur:
            cur = batch
            L.append(f"\n## 批次 `{batch}`\n")
        L.append(f"### `{key}` — {t['tc_title']}\n")
        L.append(f"- **`test_set`**：{t['test_set']}　"
                 f"**`priority`**：{t['priority']}　"
                 f"**`spec_ref`**：`…_{t['specification_reference'].rsplit('_', 1)[-1]}`")
        L.append(f"- **`distinguishing_axis`**：{t.get('distinguishing_axis', '—')}")
        L.append(f"- **`reasoning`**：{t['reasoning']}\n")
    return "\n".join(L) + "\n"


def verify(rows):
    """側檔之鍵集合 == 六批 JSON 展開後之鍵集合。雙向。"""
    if not OUT.exists():
        return ["側檔不存在"]
    import re
    txt = OUT.read_text("utf-8")
    got = set(re.findall(r"^### `([^`]+)` — ", txt, re.M))
    want = {k for k, _, _ in rows}
    bad = []
    if got - want:
        bad.append(f"側檔多出之鍵 {sorted(got - want)}")
    if want - got:
        bad.append(f"側檔缺少之鍵 {sorted(want - got)}")
    # 每一筆之 reasoning 須非空（空的側檔項與沒有它一樣沒用）
    empty = [k for k, _, t in rows if not t.get("reasoning", "").strip()]
    if empty:
        bad.append(f"reasoning 為空之 TC {empty}")
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verify", action="store_true", help="只驗對應，不重寫")
    args = ap.parse_args()
    rows = load()
    if not args.verify:
        OUT.write_text(build(rows), encoding="utf-8")
        print(f"{OUT.relative_to(ROOT)} —— {len(rows)} 筆")
    bad = verify(rows)
    n_split = sum(1 for k, _, _ in rows if not k.endswith("#1"))
    print(f"對應驗證：鍵 {len(rows)} 個（其中拆分之第 2 筆以上 {n_split} 個）；"
          f"{'PASS' if not bad else '**FAIL**'} {bad or ''}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
