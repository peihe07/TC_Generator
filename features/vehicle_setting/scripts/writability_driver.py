"""W-94 —— `writability.tsv` 之單一驅動（R-VS53，55 包 §1）。

**輸入僅為 `inputs/` 之素材、`data/` 之可回放裁定檔、與 `RULINGS.md` 之條文。**
歷輪之裁定以可回放之形式寫入本檔，不得只寫進產物：

  R-VS36  token 之三形態（`$X$`／裸名／描述式）
  R-VS39  值之正規化鍵（空白／casefold／數詞→數字）；DBC `VAL_` 為值域權威
  R-VS43  值域演繹之三條件
  R-VS47  W0／W1／W2 之分級（見 `regrade_w77.grade`）
  R-VS48′ (a) 縮寫自動；(b)(c) 須人讀 —— 採用表為 `data/_w80_adopt.json`
  R-VS49  PROXI_HDCC27_R3 之四參數（`spec_variables.tsv` 之 `proxi_values`）
  R-VS51  值域欄組依條文之 `EE Architecture` 分流
  W-59    跨條文之 `Nh:` 錨點聚合（21 輪；單條文比對為上界之修正，A-VS70）
  R-VS44  `guard_new_conclusion()` 於輸出階段攔未結 DR 之標的
  W-87    適用性前言之唯一來源型 → W2／`B4-preamble`

用法：`python3 scripts/writability_driver.py [--diff docs/reports/writability.tsv]`
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dr_conflict import guard_new_conclusion            # R-VS44
from inscope_w39 import blocks_with_sec                 # R-VS19″ 之母體
from regrade_w77 import grade                           # R-VS47
from writability_w58 import bus_domain, is_ident, norm, value_matched  # R-VS36/39

FEAT = Path(__file__).resolve().parents[1]

# ── R-VS36 ＋ A-VS84：值之三形態（①方括號 ②直引號 ③彎引號）──────────
_OPS = r"(?:=|==|!=|&lt;&gt;|<>|passes to|is set to)"
FORMS = [re.compile(rf"(\$?[A-Za-z][A-Za-z0-9_.]{{2,}}\$?)\s*{_OPS}\s*" + p)
         for p in (r"\[([^\]]{0,90})\]", r"\"([^\"]{0,90})\"", r"[“]([^”]{0,90})[”]")]

# ── W-87：適用性前言之四式 ──────────────────────────────────────────
PREAMBLE = [re.compile(p, re.I) for p in (
    r"Following\s+requirements?\s+are\s+valid\s+only\s+if",
    r"The\s+requirements?\s+in\s+this\s+section\s+are\s+applicable",
    r"applicable\s+(?:for|to)\b[^.]{0,80}?\bonly\b",
    r"This\s+section\s+applies",
    # 第五式（A-VS109，57 包 §3.2）—— `This section defines …`
    r"This\s+section\s+defines")]


def clause_pairs(text: str) -> dict[str, set[str]]:
    """回傳 {裸名 token: {值…}}。`$X$` 與裸名一併收（R-VS36）。"""
    out: dict[str, set[str]] = collections.defaultdict(set)
    for rx in FORMS:
        for tok, val in rx.findall(text):
            bare = tok.strip("$").split(".")[-1]
            if is_ident(bare):
                out[bare].add(val.strip())
    return out


def arch_column(attrs: dict) -> str:
    """**R-VS67（71 包 §1，Pei 2026-08-23）**：一律取 `Atlantis High` 欄組。

    推翻 R-VS51(2) 之「條文標 `Atlantis Mid` → 取 LID `Atlantis` 欄組」——
    其分流依**條文之架構標籤**，而 R-VS19″ 已定該標籤為**來源沿革**而非適用性。
    **沿革不應決定取值。** 原式保留於下，不刪（R-TM13）。

        a = attrs.get("EE Architecture", "")
        return "Atlantis" if ("Atlantis Mid" in a and "Atlantis High" not in a) \
            else "Atlantis High"
    """
    return "Atlantis High"


def lid_column_domain() -> dict[str, set[str]]:
    """LID `Atlantis` 欄組之值域（R-VS51 用）。

    `FL_VS_Cmd_Tlm`／`FR_VS_Cmd_Tlm` 之 `Heated_seat_*` 依 52 包 §3 判 typo，
    取 `Vented_Seat_*`；**不跨列引入**（A-VS103）。
    """
    # **R-VS67**：欄組一律取 `Atlantis High`；`Atlantis` 欄組僅作旁證。
    grp = json.loads((FEAT / "data/_lid_argroups.json").read_text())
    raw = dict(grp.get("Atlantis High") or {})
    for k, v in grp["Atlantis"].items():        # 旁證：High 欄組無該 token 時方取
        raw.setdefault(k, v)
    for k in ("FL_VS_Cmd_Tlm", "FR_VS_Cmd_Tlm"):
        if k in raw:
            raw[k] = [f for f in raw[k] if "Vented" in f] or raw[k]
    # **R-VS60（63 包 §2，Pei 2026-08-23）**：`FR_VS_Cmd_Tlm` 之值域
    # **准自 `FL_VS_Cmd_Tlm` 之列跨列引入**（A-VS103 之裁定）。
    # 依據：52 包 §3 已判列 770／790 之 `Heated_seat_*` 前綴為轉錄錯誤，
    # 而列 769（`FL_VS_Cmd_Tlm`）之四階值域為同一對稱側之正確記載。
    if not any("Vented" in f for f in raw.get("FR_VS_Cmd_Tlm", [])):
        raw["FR_VS_Cmd_Tlm"] = [f for f in raw.get("FL_VS_Cmd_Tlm", []) if "Vented" in f]
    return {k: {norm(m.group(2)) for f in v
                for m in re.finditer(r"(\d+)\s*=\s*([^\n=]+)", f)}
            for k, v in raw.items()}


def dbc_value_backfill(high: dict[str, set[str]]) -> dict[str, set[str]]:
    """**W-114(1)（64 包 §5）**：DBC `VAL_` 有而 `spec_variables.tsv` 與 LID
    兩欄組皆空之 token，其值域自 DBC 補收。

    依據：R-VS9(1)′ ＋ R-VS39 —— **DBC 為值域之權威**；
    兩處皆空係掃描遺漏（A-VS102 補收四個 ＋ `EngineSts`，漏 `HSW_StatFailSts`
    → A-VS137）。W-114(2) 之全量量測得同型遺漏**共 1 個**，即本函式之全部標的。

    以**回放形式**寫入驅動（R-VS53(2)），不改產物、不手改 `spec_variables.tsv`。
    """
    from selfcheck_w53 import DBC_VALS
    out = dict(high)
    for tok, table in DBC_VALS.items():
        if not out.get(tok):
            out[tok] = {norm(v) for v in table.values()}
    return out


def anchor_map(blocks: dict) -> dict[str, set[str]]:
    """W-59（21 輪）：跨條文之 `Nh:` 錨點聚合。

    某 token 之值於**他條文**帶 `Nh:` 錨點者（如 `[4h: Ignition run]`），
    該措辭即已由來源自載其原始碼值 —— 單條文比對看不見，故須全文聚合。
    **成因見 A-VS70**（W-58 之單條文設計致 B2 為上界）。
    """
    out: dict[str, set[str]] = collections.defaultdict(set)
    anchored = re.compile(r"([0-9A-Fa-f])h\s*:\s*([^,\]/]{1,48})")
    for blk in blocks.values():
        text = re.sub(r"\s+", " ", blk["text"])
        for tok, vals in clause_pairs(text).items():
            for val in vals:
                for _raw, label in anchored.findall(val):
                    out[tok].add(norm(label))
    return out


# ── R-VS57（59 包 §1）：L-VS2 三分 ────────────────────────────────
# `MSG.Signal` 之引用。排除三段式路徑（`TLM.Display.GUI`）與純數字段，
# 二者皆非 CAN 訊號引用（36 輪 W-98 實測之偽陽性）。
SIG_REF = re.compile(r"\b([A-Z][A-Z0-9_]{2,})\.([A-Za-z]\w{2,})\b(?!\.)")


def dbc_signals() -> set[str]:
    """基線兩檔之全部 `SG_` 名（區分大小寫）—— L-VS2 之 PASS 集合。"""
    out: set[str] = set()
    for f in ("PDT27_E2A_R4_BHCAN.dbc", "PDT27_E2A_R5_FDCAN8.dbc"):
        text = (FEAT / "inputs" / f).read_text(encoding="latin-1")
        out |= set(re.findall(r"^\s*SG_\s+(\w+)", text, re.M))
    return out


def sourced_signals(blocks: dict) -> set[str]:
    """有逐字來源之 signal 名 —— L-VS2 之 WARN 集合（PASS 以外者）。

    來源之優先序（R-VS57）：CFTS044 條文之逐字 > LID 對應欄組之 `Signal Name`。
    二者皆收；其不一致之偵測見 `lvs2_verdict()` 之呼叫端。
    """
    out: set[str] = set()
    for blk in blocks.values():
        out |= {m.group(2) for m in SIG_REF.finditer(blk["text"])}
    with (FEAT / "data/lid_pairs.tsv").open(encoding="utf-8") as f:
        out |= {r["signal"] for r in csv.DictReader(f, delimiter="\t") if r.get("signal")}
    return out


def value_sourced(sig: str, in_dbc: set[str], mid: dict[str, set[str]],
                  high: dict[str, set[str]]) -> bool:
    """R-VS57(4)：該訊號之**值域**是否有來源。

    條文所列之三處來源中，**條文內嵌值不計** —— 其只給標籤而不給 raw 碼，
    無從寫成 R-VS52 所令之 `= <raw> (<label>)`。
    依據為 61 包 §4 之實例：`HSW_Cmd_Tlm` 之條文內嵌值為 `"ON"`，
    而該條裁其為 **B6**；即該實例已排除內嵌值一路。
    **判準文字與其實例之落差見上繳 34 §2.1。**
    """
    return bool(sig in in_dbc or mid.get(sig) or high.get(sig))


def lvs2_verdict(sig: str, in_dbc: set[str], sourced: set[str],
                 value_ok: bool = True) -> str:
    """R-VS57 ＋ 其 (4)（61 包 §4）：PASS／WARN／W2-B6／FAIL 四分。

      名有來源 ∧ 值域有來源 → WARN
      名有來源 ∧ 值域無來源 → **B6**（分級判 W2）
      名無來源              → FAIL
    """
    if sig in in_dbc:
        return "PASS"
    if sig in sourced:
        return "WARN" if value_ok else "B6"
    return "FAIL"


def adoption_map() -> set[tuple[str, str]]:
    """R-VS48′ 之採用表（(b)(c) 路須人讀，故以落檔之採用表回放）。"""
    d = json.loads((FEAT / "data/_w80_adopt.json").read_text())
    return {(t, v) for t, v in d.get("adopt", [])}


def run() -> tuple[dict[str, str], dict[str, dict]]:
    high = bus_domain()                 # R-VS39 ＋ R-VS49（proxi_values 已併入）
    high = dbc_value_backfill(high)     # W-114(1)：DBC `VAL_` 之補收（A-VS137）
    mid = lid_column_domain()           # R-VS51
    adopt = adoption_map()              # R-VS48′
    blocks = {b["id"]: b for b in blocks_with_sec()}
    anchors = anchor_map(blocks)        # W-59
    in_dbc = dbc_signals()              # R-VS57：L-VS2 之 PASS 集合
    sourced = sourced_signals(blocks)   # R-VS57：WARN 集合
    preamble = {q for q, b in blocks.items()
                if any(rx.search(re.sub(r"\s+", " ", b["text"])) for rx in PREAMBLE)}

    order = {"W0": 0, "W1": 1, "W2": 2}
    grades: dict[str, str] = {}
    detail: dict[str, dict] = {}
    with (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8") as f:
        leaves = list(csv.DictReader(f, delimiter="\t"))

    for row in leaves:
        leaf = row["swe_id"]
        qs = re.findall(r"\d{7}", row["reqid_list"] or "")
        # W-87：唯一來源即適用性前言者 → W2／B4-preamble
        if qs and set(qs) <= preamble:
            grades[leaf] = "W2"
            detail[leaf] = {"blocker_class": "B4-preamble",
                            "理由": "唯一來源條文為適用性前言，無可測之功能行為"}
            continue
        best: str | None = None
        note: dict = {}
        for q in qs:
            blk = blocks.get(q)
            if not blk:
                continue
            col = arch_column(blk["attrs"])
            text = re.sub(r"\s+", " ", blk["text"])
            pairs: list[tuple[str, str]] = []
            unresolved: set[tuple[str, str]] = set()
            for tok, vals in clause_pairs(text).items():
                for val in vals:
                    if not val:
                        continue
                    pairs.append((tok, val))
                    # R-VS44(4)（57 包 §3.1）：每一個進入 TC 之 (token, 值)
                    # 一律過閘，不限「需演繹」者。
                    if guard_new_conclusion(tok, val, "resolved")[0] == "DR-CONFLICT":
                        unresolved.add((tok, val))
                        continue
                    dom = set(high.get(tok, ()))
                    if value_matched(val, dom):
                        continue
                    # R-VS51：Mid 條文另取 `Atlantis` 欄組
                    hit = col == "Atlantis" and value_matched(val, mid.get(tok, set()))
                    # R-VS48′／R-VS43：落檔之採用表
                    hit = hit or (tok, val) in adopt
                    # W-59：值之各段於他條文帶 `Nh:` 錨點者，視為已定位
                    hit = hit or bool({norm(x) for x in re.split(r"[/]{1,2}", val)}
                                      & anchors.get(tok, set()))
                    if hit:
                        continue                      # 已過閘（見上）→ 採用
                    unresolved.add((tok, val))
            gr, why = grade(text, pairs, unresolved)   # R-VS47
            # R-VS55 ＋ R-VS57：分級須涵蓋 L-VS2，惟 WARN 類不判 W2
            sigs = {m.group(2) for m in SIG_REF.finditer(text)}
            # R-VS57(4)：值域之來源 —— 條文內嵌值、LID 欄組、DBC `VAL_`
            verdicts = {sg: lvs2_verdict(
                sg, in_dbc, sourced,
                value_sourced(sg, in_dbc, mid, high)) for sg in sigs}
            if any(v == "FAIL" for v in verdicts.values()):
                gr = "W2"
                why = {**why, "blocker_class": "B5-signal-absent",
                       "理由": "斷言目標訊號不存在於基線 DBC 且無逐字來源（L-VS2 FAIL）"}
            elif any(v == "B6" for v in verdicts.values()):
                gr = "W2"
                why = {**why, "blocker_class": "B6-value-absent",
                       "理由": "訊號名有來源而其值域無來源（R-VS57(4)）"}
            warn = sorted(sg for sg, v in verdicts.items() if v == "WARN")
            if best is None or order[gr] < order[best]:
                best = gr
                note = {"reqid": q, "arch_column": col, **why}
                if warn:
                    note["dr_dependent"] = "DR-25"
                    note["lvs2_warn"] = ";".join(warn)
        grades[leaf] = best or "W2"
        detail[leaf] = note
    return grades, detail


def write_products(g: dict[str, str], d: dict[str, dict]) -> tuple[int, int]:
    """R-VS53(1)：產物自本驅動重生。

    **只改驅動所擁有之欄**（`writable`／`blocker_class`／`driver_reason`／
    `dr_dependent`／`generatable`），其餘欄（`delegate`／`stable_core`／
    `blocked_layer` 等人讀所得者）逐列保留 —— 覆寫它們會把人讀之結論
    以機械結論取代，其失真不可逆。

    `generatable` 之推導（自產物逐列反推所得，36 輪 W-98 實測 236/236 相符）：
        yes ⟺ writable ∈ {W0, W1}

    **R-VS59（63 包 §1，Pei 2026-08-23）**：委派不免除產出 TC 之義務 ——
    推導式中 `delegate` 之扣除**去除**；`delegate = blocked` 之值**廢除**
    （改記 `yes`），其標的改標 `screen_source = comfort`。
    """
    changed = 0
    wp = FEAT / "docs/reports/writability.tsv"
    with wp.open(encoding="utf-8") as f:
        rd = csv.DictReader(f, delimiter="\t")
        cols, rows = rd.fieldnames, list(rd)
    for r in rows:
        leaf, note = r["leaf_id"], d.get(r["leaf_id"], {})
        if r["writable"] != g.get(leaf, r["writable"]):
            changed += 1
        r["writable"] = g.get(leaf, r["writable"])
        r["blocker_class"] = note.get("blocker_class", r.get("blocker_class", ""))
        r["driver_reason"] = str(note.get("理由", r.get("driver_reason", "")))
        if note.get("dr_dependent"):
            r["dr_dependent"] = note["dr_dependent"]
    with wp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    gp = FEAT / "docs/reports/generatable.tsv"
    with gp.open(encoding="utf-8") as f:
        rd = csv.DictReader(f, delimiter="\t")
        cols, rows = rd.fieldnames, list(rd)
    gen = 0
    if "screen_source" not in cols:
        cols = cols + ["screen_source"]
    for r in rows:
        leaf, note = r["leaf_id"], d.get(r["leaf_id"], {})
        r["writable"] = g.get(leaf, r["writable"])
        # R-VS59：`blocked` 之值廢除
        if r["delegate"] == "blocked":
            r["delegate"] = "yes"
        r["screen_source"] = "comfort" if r["delegate"] in ("yes", "pending") else ""
        r["generatable"] = "yes" if r["writable"] in ("W0", "W1") else "no"
        if note.get("dr_dependent"):
            r["dr_dependent"] = note["dr_dependent"]
        gen += r["generatable"] == "yes"
    with gp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    return changed, gen


if __name__ == "__main__":
    g, d = run()
    print("W0／W1／W2 ＝", dict(collections.Counter(g.values())))
    if "--diff" in sys.argv:
        path = FEAT / sys.argv[sys.argv.index("--diff") + 1]
        with path.open(encoding="utf-8") as f:
            cur = {r["leaf_id"]: r["writable"] for r in csv.DictReader(f, delimiter="\t")}
        diff = [(k, cur[k], g.get(k)) for k in cur if cur[k] != g.get(k)]
        print(f"與 {path.name} 逐 leaf 不一致：{len(diff)}")
        for k, a, b in diff:
            print(f"   {k:<46} 產物 {a} ／ 驅動 {b}   {str(d.get(k, {}).get('理由', ''))[:34]}")
    if "--write" in sys.argv:
        ch, gen = write_products(g, d)
        print(f"產物重生：writable 變動 {ch} 列；generatable = yes {gen} 條")
