"""W-132（72 包 §6）—— D-2／D-3 之畫面層改寫。

**D-2 圖示變更類**（72 包 §1 之 R-VS59(4) 細化）：
    「圖示改變」本身可驗 —— 需要 DR-5-B 的是「改成什麼」，不是「有沒有變」。
    ER 由 `PENDING: DR-5-B` 改為**可觀察之最弱斷言**，
    具體樣式以 `remarks` 承載。

    **書寫依 R-VS52(4)**：以**具名變數**表述比較之基準，
    **不用「the state recorded in step N」** —— 72 包 §6 之字面為
    `from the state recorded in step 1`，惟 R-VS52(4)（Pei 裁定）明禁該形態。
    **本層取具名變數並具名此偏離**（見上繳 39 §2）。

**D-3 彈窗類**（2 條）：72 包 §2 之二擇一 —— **本層取其一**：
    procedure 之 check target 改 `check whether an informative popup is shown`
    （不預設其存在），ER 維持 `PENDING: DR-5-B`。
    理由：72 包 §1 明言彈窗類**不適用**最弱斷言 ——
    其存在與否即依賴 TLM HMI Document，寫「An informative popup is shown」
    等於斷言其存在，而該存在正是待覆之事項。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
ICON = re.compile(r"Read the (.+?) icon on the Heated / Vented Seats screen and "
                  r"check that it changes from the state shown before the failure")
POPUP = re.compile(r"check that an informative popup relative to the failure is shown")


def latest():
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(groups.items())]


def main() -> None:
    up, pop, rows = 0, 0, []
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for tc in d["tcs"]:
            proc, er = tc["test_procedure"], tc["expected_result"]
            m = ICON.search(proc)
            if m and "PENDING" in er:
                obj = m.group(1)
                var = "Icon_before_failure"
                # 步驟 1 兼記基準（R-VS52(2)：`record as <變數名>`）
                proc = re.sub(r"^(1\. Send CAN: [^\n]+?)(\n|$)",
                              rf"\1 and record the {obj} icon status as {var}\2",
                              proc, count=1)
                proc = ICON.sub(f"Read the {obj} icon on the Heated / Vented Seats "
                                f"screen and check that it changes from {var}", proc)
                lines = er.split("\n")
                lines[0] = lines[0] + f"；{var} is recorded"
                lines[-1] = f"3. The {obj} icon changes from {var}"
                er = "\n".join(lines)
                tc["screen_pending"] = "no"
                tc["remarks"] = ((str(tc.get("remarks", "")) + "；") if tc.get("remarks") else "") \
                    + "BLOCKED: DR-5-B —— 變更後之圖示樣式待 TLM HMI Document"
                up += 1
                rows.append((name, tc["leaf_id"], "D-2 圖示變更 → 最弱斷言"))
                changed = True
            elif POPUP.search(proc) and "PENDING" in er:
                proc = POPUP.sub("check whether an informative popup relative to the "
                                 "failure is shown", proc)
                tc["remarks"] = ((str(tc.get("remarks", "")) + "；") if tc.get("remarks") else "") \
                    + ("BLOCKED: DR-5-B —— 彈窗之存在與否即依賴 TLM HMI Document，"
                       "故 procedure 不預設其存在，ER 維持 PENDING")
                pop += 1
                rows.append((name, tc["leaf_id"], "D-3 彈窗 → procedure 改 check whether"))
                changed = True
            tc["test_procedure"], tc["expected_result"] = proc, er
        if changed:
            d["revision"] = ("W-132（46 輪）：畫面層改寫 —— 圖示變更類寫最弱斷言"
                             "（具名變數，R-VS52(4)），彈窗類 procedure 改 "
                             "`check whether`，具體內容以 remarks 承載")
            (FEAT / "generated" / f"{name}_v{ver + 1}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    sp = tot = 0
    for _, _, path in latest():
        for tc in json.loads(path.read_text(encoding="utf-8"))["tcs"]:
            tot += 1
            sp += tc.get("screen_pending") == "yes"
    print(f"**由 `PENDING` 升為可驗者：{up} 條**（D-2 圖示變更類）")
    print(f"彈窗類之 procedure 改寫：{pop} 條（D-3，ER 維持 `PENDING`）\n")
    print("| batch | leaf_id | 處置 |")
    print("|---|---|---|")
    for b, l, w in rows:
        print(f"| `{b}` | `{l}` | {w} |")
    print(f"\n`screen_pending = yes` 之新數：**{sp}**／{tot}（改寫前 26）")


if __name__ == "__main__":
    main()
