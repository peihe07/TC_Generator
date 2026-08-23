"""W-133（73 包 §5）—— R-VS67′ 之「能承載」判準與欄組選取。

R-VS67′：欄組之選取依下列次序 ——
  (1) `Atlantis High` 欄組**能承載**該條文之語義者 → 取之
  (2) 不能承載者 → 取**能承載之欄組**（`Atlantis`），並依 R-VS66(a) 標 `impl_gap`
  (3) 二者皆不能承載 → `PENDING: DR-{n}`

**「能承載」之判準（可機器判定）**：
    條文所述之相異狀態數 ≤ 該欄組訊號之值域基數
    **且** 條文所用之狀態名於該值域中可對映（R-VS43／R-VS48′）
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from writability_w58 import norm  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]


def _rows() -> list[dict]:
    import csv
    with (FEAT / "data/lid_pairs.tsv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def lookup(group: str, token: str) -> tuple[str, str, dict[str, str]]:
    """（message, signal, raw → label）—— 依欄組查該 LID token 之對映。

    `lid_pairs.tsv` 之 `scope` 只有兩值：`Atlantis High` 與 `Atlantis(&High)`。
    LID 表中同一實體之兩個欄組以 **token 之 `2` 尾綴**區分
    （`FL_HS_RQ` = High 欄組；`FL_HS_RQ2` = Atlantis 欄組），
    故 `Atlantis` 欄組之查法為：先試 `<token>2`，再試同名之 `Atlantis(&High)` 列。
    """
    rows = _rows()
    if group == "Atlantis High":
        cand = [r for r in rows if r["lid"] == token and r["scope"] == "Atlantis High"]
    else:
        cand = [r for r in rows if r["lid"] == token + "2"] or \
               [r for r in rows if r["lid"] == token and r["scope"] == "Atlantis(&High)"]
    best = ("", "", {})
    for r in cand:
        # `fmt` 之換行為**字面之 `\n` 兩字元**（非真換行）—— 須先還原，
        # 否則 `0 = Not_Pressed\n1 = Pressed` 會被讀成單一值 `Not_Pressed\n1`。
        fmt = (r["fmt"] or "").replace("\\n", "\n")
        # LID 之單一儲存格常**綑綁兩個訊號之列舉**
        # （`2 bit signal (FL_HS_STATSts)` … `1 bit signal (FL_HS_STATFailSts)` …），
        # 逐段切分後取與本列 `signal` 相符者；否則 raw 碼會互相覆寫
        # （0/1 被後一段之 `Fail_*` 蓋掉 —— 47 輪 W-133 實測之偽陰性）。
        segs = re.split(r"\n(?=\d+\s*bit signal\s*\()", fmt)
        pick = next((g for g in segs if r["signal"] and f"({r['signal']})" in g), None)
        dom = {n: l.strip() for n, l in
               re.findall(r"(\d+)\s*=\s*([^\n=]+)", pick if pick else fmt)}
        if len(dom) > len(best[2]):
            best = (r["message"], r["signal"], dom)
    return best


def domain(group: str, token: str) -> dict[str, str]:
    return lookup(group, token)[2]


def can_carry(states: set[str], dom: dict[str, str]) -> tuple[bool, str]:
    """回傳（能否承載, 理由）。"""
    if not dom:
        return False, "該欄組無此 token 之值域"
    if len(states) > len(dom):
        return False, f"條文之相異狀態數 {len(states)} > 值域基數 {len(dom)}"
    labs = {norm(v) for v in dom.values()}
    miss = sorted(s for s in states if norm(s) not in labs)
    if miss:
        return False, f"狀態名不可對映：{'／'.join(miss)}"
    return True, f"狀態數 {len(states)} ≤ 基數 {len(dom)}，且狀態名皆可對映"


def choose(token: str, states: set[str]) -> dict:
    """R-VS67′ 之次序選取。"""
    for grp in ("Atlantis High", "Atlantis"):
        dom = domain(grp, token)
        ok, why = can_carry(states, dom)
        if ok:
            msg, sig, _ = lookup(grp, token)
            return {"token": token, "group": grp, "domain": dom, "message": msg,
                    "signal": sig, "impl_gap": grp != "Atlantis High", "reason": why}
    return {"token": token, "group": None, "domain": {}, "message": "", "signal": "",
            "impl_gap": False, "reason": "兩欄組皆不能承載 → PENDING"}


# ── 錨點（R-VS54，兩側皆須有標的）────────────────────────────────
FOUR = {"Heated_seat_off", "Heated_seat_low", "Heated_seat_medium", "Heated_seat_high"}
ANCHORS = [
    ("必命中", "FL_HS_RQ", FOUR, "Atlantis", True),      # 1 bit 不能承載 → 降欄組 ＋ impl_gap
    ("必不命中", "HeatedSeatFL", FOUR, "Atlantis High", False),  # 四階狀態訊號 → High 能承載
]


def main() -> None:
    print("| 側 | token | 選定欄組 | `impl_gap` | 預期 | 判 |")
    print("|---|---|---|---|---|---|")
    bad = 0
    for side, tok, states, want_grp, want_gap in ANCHORS:
        r = choose(tok, states)
        ok = r["group"] == want_grp and r["impl_gap"] == want_gap
        bad += not ok
        print(f"| {side} | `{tok}` | {r['group']} → `{r['message']}.{r['signal']}` "
              f"| {r['impl_gap']} | {want_grp}／{want_gap} | "
              f"{'PASS' if ok else '⚠ 未命中'} |")
        print(f"|  |  |  |  | 理由 | {r['reason']} |")
    print(f"\n錨點兩側皆有標的；不符 **{bad}**")
    if bad:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
