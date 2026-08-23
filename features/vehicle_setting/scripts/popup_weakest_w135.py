"""W-135（73 包 §3／§5）—— 彈窗類改採**最弱斷言**（選項二）。

72 包 §2 之 D-3 給二選項，46 輪取 `check whether` 者與 canon §5.5
（末步驟須有驗證意圖）相衝（A-VS150）。73 包 §3 裁定改採選項二：

    procedure  `3. Press … and check that an informative popup is shown`
    ER         `3. An informative popup is shown`
    AH         `BLOCKED: DR-5-B —— 彈窗之內容與樣式待 TLM HMI Document`

**彈窗之「存在」為來源逐字所載**（`shall show an informative popup`），
待補者為其**內容與樣式**，故最弱斷言成立。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
WHETHER = re.compile(r"check whether an informative popup relative to the failure is shown")


def latest():
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(g.items())]


def main() -> None:
    rows = []
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for tc in d["tcs"]:
            if not WHETHER.search(tc["test_procedure"]):
                continue
            tc["test_procedure"] = WHETHER.sub(
                "check that an informative popup relative to the failure is shown",
                tc["test_procedure"])
            er = tc["expected_result"].split("\n")
            er[-1] = "3. An informative popup relative to the failure is shown"
            tc["expected_result"] = "\n".join(er)
            tc["screen_pending"] = "no"
            tc["remarks"] = re.sub(r"BLOCKED: DR-5-B[^；]*", "",
                                   str(tc.get("remarks", ""))).strip("；")
            tc["remarks"] = ((tc["remarks"] + "；") if tc["remarks"] else "") + \
                "BLOCKED: DR-5-B —— 彈窗之內容與樣式待 TLM HMI Document"
            rows.append((name, tc["leaf_id"]))
            changed = True
        if changed:
            d["revision"] = ("W-135（47 輪）：彈窗類改採最弱斷言（73 包 §3），"
                             "§5.5 之衝突消解；內容與樣式以 remarks 承載")
            (FEAT / "generated" / f"{name}_v{ver + 1}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    sp = tot = 0
    for _, _, p in latest():
        for tc in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            tot += 1
            sp += tc.get("screen_pending") == "yes"
    print(f"**改寫 {len(rows)} 條**")
    for b, l in rows:
        print(f"  `{b}`  `{l}`")
    print(f"\n`screen_pending = yes` 之數：**{sp}**／{tot}（46 輪末 15）")
    print(f"由 `PENDING` 升為可驗者之**累計**：{26 - sp} 條（起始 26）")


if __name__ == "__main__":
    main()
