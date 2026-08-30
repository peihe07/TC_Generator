#!/usr/bin/env python3
"""下放包 17 作業 C／D 之唯讀量測（A-ICS111／A-ICS112）。

**唯讀**：本腳本不寫任何檔、不改任何 TC、不碰 git。
其輸出即 `docs/reports/17_val1500_three_states.md` 之數字來源。

量測對象：
  C-1 `CFTS020-4819466`／`4819475` 之逐字全文、章節、三軸屬性
  C-2 二物件依 R-ICS2 v2(b) 之適用性（**直接 import `cfts020_probe`，不自寫判定**）
  C-3 二物件之變體層／範圍層（同上，取 probe 之 `variant` / `variant_fits_dut` / `scope`）
  C-4 二物件是否在 SYS2 `Basic Report` 之來源欄（比對前正規化 NBSP 與連續空白）
  C-5 **全 2180 物件**中載該三態字面者之普查（判適用者另列）
  D-1 b03 交付欄中含 `RQ_DISP_INTS` 之行（逐字）
  D-2 BHCAN2 之 `SG_ RQ_DISP_INTS` 定義與 `VAL_ 1283 RQ_DISP_INTS` 之全部列舉

凡有列舉者，數字一律自列舉長度取得（A-ICS72 之拿法），不手估。
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # features/ics_management
REPO = ROOT.parents[1]                              # repo root
sys.path.insert(0, str(ROOT / "scripts"))

import cfts020_probe as P                           # noqa: E402  判定邏輯唯一來源

DBC = REPO / "forms/PDT27_E2A_R1_BHCAN2.dbc"        # feature.yaml: reference.dbc_bh2
SYS2 = ROOT / ("inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_"
               "All_HW_System_Accepted & Released.xlsx")
B03 = ROOT / "generated/b03/b03_tcs.json"

TARGETS = ("4819466", "4819475")

# 三態之普查樣式。**須綁到 `$TGW_DISP_STAT$` 之賦值**，
# 不得只搜裸字面 —— 裸 `[SNA]` 會把 `$DCSD_DISP_STAT$ = [SNA]` 一併收進來
# （實測：裸搜 30 命中，綁定後 13），那是另一個訊號之同名狀態，非本題所問。
TOKENS = {
    "7 Rear_Camera_Display": r"\$TGW_DISP_STAT\$ = \[DISP_REAR_CAMERA",
    "8 On_blanked_screen": r"\$TGW_DISP_STAT\$ = \[ON_BLANK",
    "15 SNA": r"\$TGW_DISP_STAT\$ = \[SNA",
}


def norm(s) -> str:
    """xlsx 之儲存格正規化：NBSP → 空白、連續空白收斂、去頭尾。"""
    if s is None:
        return ""
    t = unicodedata.normalize("NFKC", str(s)).replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


def dbc_text() -> str:
    """BHCAN2 為 latin-1 編碼（A 檔實測）。"""
    return DBC.read_text(encoding="latin-1")


def bo_block(msg_id: str) -> list[str]:
    """以 `BO_ ` 行為分段起點自行切段 —— 該檔之 `BO_` 區塊非以空行分隔。"""
    lines = dbc_text().split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("BO_ ")]
    for k, i in enumerate(starts):
        if lines[i].startswith(f"BO_ {msg_id} "):
            end = starts[k + 1] if k + 1 < len(starts) else len(lines)
            return [l for l in lines[i:end] if l.strip()]
    return []


def val_enum(msg_id: str, sig: str) -> list[tuple[str, str]]:
    """回傳 `VAL_` 之 (raw, label) 列表。數字自本列表長度取得。"""
    m = re.search(rf'^VAL_ {msg_id} {sig} (.*);$', dbc_text(), re.M)
    if not m:
        return []
    return re.findall(r'(\d+) "([^"]*)"', m.group(1))


def sys2_rows():
    import openpyxl
    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    ws = wb["Basic Report"]
    rows = list(ws.iter_rows(values_only=True))
    header = [norm(c) for c in rows[0]]
    return header, rows[1:]


def col_of(header: list[str], needle: str) -> int:
    hits = [i for i, h in enumerate(header) if needle in h]
    assert len(hits) == 1, f"欄名 {needle!r} 命中 {len(hits)} 個，不唯一"
    return hits[0]


def main() -> None:
    out: dict = {}

    # ── C-1/2/3 ──────────────────────────────────────────────
    objs = P.parse()
    out["cfts020_object_count"] = len(objs)
    by_id = {o["id"]: o for o in objs}
    out["targets"] = {
        t: {k: by_id[t][k] for k in
            ("section_no", "section", "artifact_type", "state",
             "ecu", "radio", "ee", "text",
             "v2", "v2_reasons", "variant", "variant_fits_dut", "scope")}
        for t in TARGETS
    }
    # 屬性頭之逐字行（原檔一行）
    lines = P.doc_lines()
    out["targets_raw"] = {}
    for t in TARGETS:
        i = next(i for i, l in enumerate(lines) if l.strip().startswith(f"{t}: ["))
        out["targets_raw"][t] = {"attr_line": lines[i], "body_line": lines[i + 1]}

    # ── C-4：SYS2 ────────────────────────────────────────────
    header, rows = sys2_rows()
    out["sys2_data_rows"] = len(rows)
    c_src = col_of(header, "來源需求項目ID")
    out["sys2_src_col_1based"] = c_src + 1
    src_ids: set[str] = set()
    for r in rows:
        src_ids |= set(re.findall(r"\d{7}", norm(r[c_src])))
    out["sys2_distinct_src_ids"] = len(src_ids)
    out["sys2_hit"] = {t: (t in src_ids) for t in TARGETS}

    # ── C-5：三態字面之全文件普查 ────────────────────────────
    census = {}
    union: set[str] = set()
    for tok, pat in TOKENS.items():
        hits = [o for o in objs if re.search(pat, o["text"])]
        fit = [o for o in hits if o["v2"] == "適用"]
        union |= {o["id"] for o in fit}
        census[tok] = {
            "total": len(hits),
            "applicable": len(fit),
            "applicable_ids": [o["id"] for o in fit],
            "applicable_in_sys2": [o["id"] for o in fit if o["id"] in src_ids],
        }
    out["state_census"] = census
    out["state_union_ids"] = sorted(union)
    out["state_union_count"] = len(union)
    out["state_union_detail"] = [
        {"id": i, "section_no": by_id[i]["section_no"], "section": by_id[i]["section"],
         "variant": by_id[i]["variant"], "variant_fits_dut": by_id[i]["variant_fits_dut"],
         "scope": by_id[i]["scope"], "in_sys2": i in src_ids}
        for i in sorted(union)]

    # ── C-5b：既有 31 條之錨集合 ─────────────────────────────
    anchors: set[str] = set()
    tcs = []
    for f in sorted((ROOT / "generated").glob("b*/b*_tcs.json")):
        for tc in json.load(open(f))["tcs"]:
            tcs.append(tc)
            anchors |= set(re.findall(r"\d{7}", tc.get("specification_reference") or ""))
    out["tc_total"] = len(tcs)
    out["anchor_ids"] = sorted(anchors)
    out["anchor_count"] = len(anchors)
    for tok, d in census.items():
        d["applicable_already_anchored"] = [i for i in d["applicable_ids"] if i in anchors]
    out["state_union_anchored"] = [i for i in out["state_union_ids"] if i in anchors]

    # ── C-5c：TGW_DISP_STATSts 於交付欄之實用值普查 ──────────
    used: dict[str, int] = {}
    for tc in tcs:
        for k in ("test_procedure", "expected_result"):
            for line in (tc.get(k) or "").split("\n"):
                if "TGW_DISP_STATSts" in line:
                    for m in re.finditer(r"(?:is|=)\s*(\d+)\s*\(([^)]*)\)", line):
                        used[f"{m.group(1)} ({m.group(2)})"] = used.get(
                            f"{m.group(1)} ({m.group(2)})", 0) + 1
    out["tgw_values_used"] = used
    out["val1500_enum"] = val_enum("1500", "TGW_DISP_STATSts")
    out["val1500_enum_count"] = len(out["val1500_enum"])
    out["bo_1500_block"] = bo_block("1500")

    # ── D-1：b03 交付欄之逐字行 ──────────────────────────────
    b03 = json.load(open(B03))
    d1 = []
    for tc in b03["tcs"]:
        for k in ("test_procedure", "expected_result"):
            for line in (tc.get(k) or "").split("\n"):
                if "RQ_DISP_INTS" in line:
                    d1.append({"spec_ref": tc.get("specification_reference"),
                               "field": k, "line": line})
    out["d1_lines"] = d1
    out["d1_line_count"] = len(d1)
    out["d1_tc_count"] = len({e["spec_ref"] for e in d1})
    out["b03_tc_count"] = len(b03["tcs"])

    # ── D-2：SG_ RQ_DISP_INTS 與 VAL_ 1283 ───────────────────
    out["bo_1283_block"] = bo_block("1283")
    out["sg_rq_disp_ints"] = next(
        l for l in out["bo_1283_block"] if l.strip().startswith("SG_ RQ_DISP_INTS "))
    out["val1283_rq_disp_ints"] = val_enum("1283", "RQ_DISP_INTS")
    out["val1283_rq_disp_ints_count"] = len(out["val1283_rq_disp_ints"])
    out["bo_tx_bu"] = re.findall(r"^BO_TX_BU_ (?:1283|1500) : .*$", dbc_text(), re.M)
    out["cm_rq_disp_ints"] = re.findall(r"^CM_ SG_ 1283 RQ_DISP_INTS .*$",
                                        dbc_text(), re.M)
    out["ba_rq_disp_ints"] = re.findall(r'^BA_ "[^"]+" SG_ 1283 RQ_DISP_INTS .*$',
                                        dbc_text(), re.M)

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
