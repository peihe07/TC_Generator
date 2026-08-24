"""W-VF62（V24 §7）—— pilot #1 v3：**逐條字串修正，不重跑選池**。

不改 leaf 集合、不改 `specification_reference`、不改 `reasoning` 之 Priority 段。

五項：
  1. 刪 `pre_conditions` 第 1 項（Defect A：canon §4.4 Forbidden 之
     `system defaults (HU is powered on.)`；且與 procedure 步驟 1 之
     `Power cycle the HU` 自相矛盾）
  2. `check whether` → `check that`（Defect B：canon §5.1 Forbidden verbs），
     其受詞依實測之正負向定：負向六條 `is not listed`／正向四條 `is listed`
  3. 縮短逾 14 字之 `tc_title`（Defect C）——
     **實測為 4 條（241／244／246／247），V24 §4 列 3 條、未列 241**
  4. UI 標籤加雙引號 —— **依 Part 1 已交付之慣例**（見 §W-VF62(4) 之實測），
     非自創
  5. 檔頭 `selection` 之計數改 **P0(a) 4 ／ P0(c) 6**（Note 1）
"""
from __future__ import annotations

import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
SRC = FEAT / "generated/vf230_pilot1.json"
OUT = FEAT / "generated/vf230_pilot1_v3.json"

# Defect C —— 逾 14 字者之縮短式。**保留其手足區辨 token（分割值本身）**，
# 刪去可自 test_item 復原之贅語（`is displayed and can be modified when`）。
TITLES = {
    241: 'Suspension Service Mode not displayed: CAN node 27 "Absent"',
    244: 'Power Tailgate Alert displayed and modifiable: CAN node 82 "Present"',
    246: 'Lane Sense Warning displayed and modifiable: Lane_Assist "Active Lane Management"',
    247: 'Suspension Service Mode displayed and modifiable: CAN node 27 "Present"',
}


def steps(s: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", x) for x in s.split("\n") if x.strip()]


def numbered(xs: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def label_of(tc: dict) -> str:
    """該條之 UI 標籤 —— 自 procedure 之 `the X customer setting` 取之。"""
    m = re.search(r"the ([A-Z][\w /]*?) customer setting", tc["test_procedure"])
    return m.group(1) if m else ""


def main() -> None:
    d = json.loads(SRC.read_text(encoding="utf-8"))
    log = []
    for tc in d["tcs"]:
        seq, before = tc["seq"], json.dumps(tc, ensure_ascii=False)

        # ── 1. 刪 pre_conditions 第 1 項 ──────────────────────────────
        pre = steps(tc["pre_conditions"])
        dropped = pre[0]
        tc["pre_conditions"] = numbered(pre[1:])

        # ── 2. check whether → check that，受詞依正負向 ───────────────
        negative = "is not displayed" in tc["tc_title"]
        obj = "is not listed" if negative else "is listed"
        tc["test_procedure"] = re.sub(
            r"check whether the (.+?) customer setting is listed",
            lambda m: f'check that the "{m.group(1)}" customer setting {obj}',
            tc["test_procedure"])

        # ── 4. UI 標籤加雙引號（其餘出現處）—— 依 Part 1 慣例 ─────────
        lab = label_of(tc) or tc["tc_title"].split(" is ")[0].split(" not ")[0]
        for k in ("test_procedure", "expected_result"):
            tc[k] = re.sub(rf'(?<!"){re.escape(lab)}(?!") customer setting',
                           f'"{lab}" customer setting', tc[k])

        # ── 3. tc_title ──────────────────────────────────────────────
        if seq in TITLES:
            tc["tc_title"] = TITLES[seq]

        if json.dumps(tc, ensure_ascii=False) != before:
            log.append((seq, dropped, obj, lab))

    # ── 5. 檔頭之計數 ────────────────────────────────────────────────
    import collections
    cnt = collections.Counter(t["priority_class"] for t in d["tcs"])
    d["selection"] = re.sub(
        r"P0\(a\)\s*\d+\s*／\s*P0\(c\)\s*\d+",
        f"P0(a) {cnt['P0(a)']} ／ P0(c) {cnt['P0(c)']}", d["selection"])
    d["supersedes"] = SRC.name
    d["revision"] = ("W-VF62（V24 §7）：pilot #1 v3 —— 刪系統預設 pre_condition、"
                     "`check whether` → `check that`、逾 14 字之 tc_title 縮短（4 條）、"
                     "UI 標籤依 Part 1 慣例加雙引號、檔頭計數改 4／6")
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name} —— {len(d['tcs'])} 條，改動 {len(log)} 條")
    print(f"檔頭 selection：{d['selection']}")


if __name__ == "__main__":
    main()
