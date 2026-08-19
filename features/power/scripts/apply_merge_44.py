"""B1 —— 四對 TC 合併為四條多 ER（R-P294）。

**依據 §5.7**：「一個觸發、多個必然後果歸同一條 ——
觸發為驗證單位，必然隨之而來之後果為待查之事實，非另一條 TC」。

四對之 `pre_conditions` / `input_test_data` 全同，
`test_procedure` 之**施加步驟逐字相同**，僅**觀察步驟**與 `expected_result` 相異
（43 §2.2 / A-PW275）。

**合併規則（R-P294(a)）**：保留第 1 步（施加），
二條之觀察步驟併為第 2、3 步，其 ER 對應併列。
`reasoning` 載明其係由何二條合併及其依據（R-P294(c)）。

**⚠ 合併後之連鎖處置**
  - `SWE-PM-072` 合併後僅存 **1** 條 TC → 依 **R-P265** 其 `axis` 欄須移除
    （§10.1 之 optional；§4.6 之輸出時機為 sibling 注入時，無 sibling 即不成立）
  - `split_flag` / `split_index` 依 R-P115 重算
  - `tc_id` 之臨時號重新連號（R-P294(b)）；最終號於寫回時指派（R-P113(c)）

用法：
    python features/power/scripts/apply_merge_44.py --dry-run
    python features/power/scripts/apply_merge_44.py --apply
"""

from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GEN = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

# （保留者, 併入者）—— 保留者為 tc_id 較小者
PAIRS = [("005", "006"), ("100", "102"), ("104", "107"), ("175", "176")]
OBSERVE = re.compile(r"^\s*\d+\.\s*(?:Read|Check|Observe|Verify|Confirm)\b", re.I)
BASE = re.compile(r"(SWE-PM-\d+)")


def steps(text: str) -> list[str]:
    return [x.strip() for x in str(text).split("\n") if x.strip()]


def renumber(lines: list[str]) -> str:
    out = []
    for i, ln in enumerate(lines, 1):
        out.append(re.sub(r"^\s*\d+\.\s*", f"{i}. ", ln))
    return "\n".join(out)


def main() -> None:
    apply = "--apply" in sys.argv
    if not apply and "--dry-run" not in sys.argv:
        raise SystemExit("須指定 --dry-run 或 --apply")

    files = {p: json.loads(p.read_text(encoding="utf-8"))
             for p in sorted(GEN.glob("*.json"))}
    by_id = {t["tc_id"][-3:]: (p, t) for p, d in files.items() for t in d["tcs"]}

    log = []
    for keep_k, drop_k in PAIRS:
        (_, keep), (dp, drop) = by_id[keep_k], by_id[drop_k]
        assert keep["req_id"] == drop["req_id"], (keep["req_id"], drop["req_id"])
        assert keep["pre_conditions"] == drop["pre_conditions"]
        assert keep["input_test_data"] == drop["input_test_data"]

        k_steps, d_steps = steps(keep["test_procedure"]), steps(drop["test_procedure"])
        k_act = [s for s in k_steps if not OBSERVE.search(s)]
        d_act = [s for s in d_steps if not OBSERVE.search(s)]
        assert k_act == d_act, (k_act, d_act)
        k_obs = [s for s in k_steps if OBSERVE.search(s)]
        d_obs = [s for s in d_steps if OBSERVE.search(s)]

        k_er, d_er = steps(keep["expected_result"]), steps(drop["expected_result"])
        # ER 之首行為「施加被接受」之共同斷言者只留一份
        common = [e for e in k_er if e[2:].strip() in [x[2:].strip() for x in d_er]]
        k_rest = [e for e in k_er if e not in common]
        d_rest = [e for e in d_er if e[2:].strip() not in
                  [x[2:].strip() for x in common]]

        new_proc = renumber(k_act + k_obs + d_obs)
        new_er = renumber(common + k_rest + d_rest)
        note = (f"**合併（R-P294 / §5.7，44 包）**：本條由臨時號 `…-{keep_k}` 與 "
                f"`…-{drop_k}` 合併而成。二者之 `pre_conditions` / `input_test_data` "
                f"逐字全同，`test_procedure` 之**施加步驟逐字相同**"
                f"（`{k_act[0][:52]}…`），僅觀察步驟與 ER 相異 —— "
                f"依 §5.7「一個觸發、多個必然後果歸同一條」，"
                f"其觀察之差異為同一觸發之不同後果，以多 ER 承接。")

        log.append((keep_k, drop_k, keep["req_id"],
                    len(k_steps), len(d_steps), len(steps(new_proc)),
                    len(k_er), len(d_er), len(steps(new_er))))
        keep["test_procedure"] = new_proc
        keep["expected_result"] = new_er
        keep["reasoning_note"] = ((keep.get("reasoning_note") or "").strip()
                                  + ("\n\n" if keep.get("reasoning_note") else "")
                                  + note).strip()
        files[dp]["tcs"] = [t for t in files[dp]["tcs"] if t is not drop]

    # ── 合併後之連鎖處置 ──
    tcs = [t for d in files.values() for t in d["tcs"]]
    by_req: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_req[BASE.match(t["req_id"]).group(1)].append(t)
    axis_removed, split_fixed = [], []
    for leaf, group in by_req.items():
        if len(group) == 1 and group[0].get("distinguishing_axis") is not None:
            group[0].pop("distinguishing_axis", None)
            axis_removed.append(group[0]["tc_id"][-3:])
        for i, t in enumerate(sorted(group, key=lambda x: x["tc_id"]), 1):
            want_flag, want_idx = (len(group) > 1), i
            if t.get("split_flag") != want_flag or t.get("split_index") != want_idx:
                split_fixed.append((t["tc_id"][-3:], t.get("split_flag"),
                                    want_flag, t.get("split_index"), want_idx))
                t["split_flag"], t["split_index"] = want_flag, want_idx

    # ── 臨時號重新連號（R-P294(b)）──
    #
    # **⚠ 以 `(SWE-PM ID, split_index)` 重排會使 260 條全數變號**，
    # 摧毀既往各包對 `…-NNN` 之引用（本包 §K 第 3 項所慮之追溯關係）。
    # 故**保留原有之 `tc_id` 序，僅補上四條被併入者所留之缺口** ——
    # 其結果仍為 001–260 連號，而位移僅及於被移除者之後，最多 4 號。
    # 寫回時之最終指派仍依 R-P113(c) 之 `(SWE-PM ID, split_index)` 序，
    # 與本階段之臨時號無涉。
    order = sorted(tcs, key=lambda t: int(t["tc_id"][-3:]))
    mapping = []
    for i, t in enumerate(order, 1):
        old = t["tc_id"]
        new = re.sub(r"\d{3}$", f"{i:03d}", old)
        if old != new:
            mapping.append((old, new))
        t["tc_id"] = new

    print(f"{'（乾跑）' if not apply else '（套用）'}合併 {len(log)} 對；"
          f"TC {len(tcs) + len(log)} → **{len(tcs)}**")
    for k, d, req, ks, ds, ns, ke, de, ne in log:
        print(f"  …-{k} ← …-{d}  ({req})  proc {ks}+{ds} → {ns} 步；ER {ke}+{de} → {ne} 行")
    print(f"  `axis` 欄移除（leaf 僅存 1 條）：{axis_removed}")
    print(f"  `split_flag`/`split_index` 重算：{len(split_fixed)} 條")
    print(f"  臨時號重新連號：{len(mapping)} 條變動")

    md = ["# B1 —— 四對合併紀錄（R-P294）\n",
          f"\n> 模式：**{'套用' if apply else '乾跑'}**；"
          f"TC **{len(tcs) + len(log)} → {len(tcs)}**。\n",
          "\n## 一、合併對\n\n"
          "| 保留 | 併入 | leaf | procedure 步數 | ER 行數 |\n|---|---|---|---|---|\n"]
    for k, d, req, ks, ds, ns, ke, de, ne in log:
        md.append(f"| `…-{k}` | `…-{d}` | `{req}` | {ks} ＋ {ds} → **{ns}** | "
                  f"{ke} ＋ {de} → **{ne}** |\n")
    md.append(f"\n## 二、連鎖處置\n\n"
              f"- **`axis` 欄移除**（其 leaf 合併後僅存 1 條，依 R-P265）："
              f"{'、'.join('`…-' + x + '`' for x in axis_removed) or '（無）'}\n"
              f"- **`split_flag` / `split_index` 重算**（R-P115）：{len(split_fixed)} 條\n"
              f"- **臨時號重新連號**（R-P294(b)）：{len(mapping)} 條變動\n")
    md.append("\n## 三、臨時號對照（舊 → 新）\n\n| 舊 | 新 |\n|---|---|\n")
    for o, n in mapping:
        md.append(f"| `{o}` | `{n}` |\n")
    (DATA / "merge_44.md").write_text("".join(md), encoding="utf-8")

    if apply:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                         encoding="utf-8")
        print(f"已寫回 {len(files)} 檔")
    else:
        print("未寫回（乾跑）")


if __name__ == "__main__":
    main()
