"""pilot #1／#2 之 PROXI 參數名統一為**條文逐字**（W-VF69 §2，依 R-VF78 二）。

**修正之標的**（實測，非 A-VF22 首版所記）：
  不一致發生於**同一條 TC 之內** —— seq 241／247 之
  `test_item` 為 `$CAN_Node_27(ASM / ASCM)$`（斜線兩側有空格），
  `pre_conditions` 為 `$CAN_Node_27_ASM_ASCM$`（底線式）。
  **二者皆非條文逐字**（條文為 `CAN node 27 (ASM/ASCM)`）。

**對映表由條文抽出，不寫死**：以 leaf 之 `retrieve the <X> (PROXI )?configuration`
取其逐字名，再將 TC 內該參數之各式寫法一律換為之。

**條文自身之大小寫不一致保留**（`CAN node 82` vs `CAN Node 24`）——
R-VF78 二令取逐字，逐字即含其大小寫。

**R-VS81 之張力具名**：本檔就地改寫已定版之 `vf230_pilot1.json`，
而 R-VS81 令「輸出須帶版號、不得覆蓋」。其依據為 V29 §5 第 2 項逐字
「字串取代（R-VF78 二），隨 W-VF69 一併為之，不另立輪次」，
且 pilot #1 之生成鏈已依 R-VF78 四判為 `archived`（不可重跑）。
**故本檔即該次改寫之唯一可稽記錄**，其變更逐條列印。
"""
import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
TARGETS = ("generated/vf230_pilot1.json", "generated/vf230_pilot2.json")
FIELDS = ("tc_title", "test_item", "pre_conditions", "input_test_data",
          "test_procedure", "expected_result", "remarks", "reasoning")

CLAUSE = re.compile(r"retrieve the (.+?) (?:PROXI )?configuration", re.I)


def canonical_names() -> dict[str, str]:
    """key = 參數名之正規化（去非英數字、轉小寫）；value = 條文逐字。"""
    out = {}
    for r in csv.DictReader((FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"),
                            delimiter="\t"):
        m = CLAUSE.search(re.sub(r"\s+", " ", r["desc"].replace("\\n", " ")))
        if m:
            lit = m.group(1).strip()
            out.setdefault(re.sub(r"[^a-z0-9]", "", lit.lower()), lit)
    return out


def main() -> None:
    names = canonical_names()
    total = 0
    for tgt in TARGETS:
        p = FEAT / tgt
        doc = json.loads(p.read_text(encoding="utf-8"))
        changed = []
        for t in doc["tcs"]:
            for f in FIELDS:
                if f not in t:
                    continue

                def repl(m):
                    lit = names.get(re.sub(r"[^a-z0-9]", "", m.group(1).lower()))
                    return f"${lit}$" if lit else m.group(0)

                new = re.sub(r"\$([^$]+)\$", repl, t[f])
                if new != t[f]:
                    changed.append((t["seq"], f, t[f], new))
                    t[f] = new
        if changed:
            doc.setdefault("revision", "")
            doc["revision"] = (str(doc.get("revision") or "").rstrip("。 ")
                               + "；W-VF69（38 輪）：PROXI 參數名依 R-VF78 二"
                                 "統一為條文逐字，"
                                 f"改 {len(changed)} 處，見 vf230_wvf69_proxi_fix.py").lstrip("；")
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{tgt} —— 改 {len(changed)} 處")
        for seq, f, old, new in changed:
            a = set(re.findall(r"\$[^$]+\$", old))
            b = set(re.findall(r"\$[^$]+\$", new))
            print(f"    seq {seq} {f:16} {sorted(a - b)} → {sorted(b - a)}")
        total += len(changed)
    print(f"\n合計 {total} 處")


if __name__ == "__main__":
    main()
