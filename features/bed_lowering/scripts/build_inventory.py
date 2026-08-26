#!/usr/bin/env python3
"""Build bed_lowering's leaf/heading/test-set artefacts from the 037 report.

Emits three TSVs into `features/bed_lowering/data/` and runs the R-G10
remainder verification. Every number this script prints is machine output —
the upstream package copies from stdout and transcribes nothing (R-G20).

Test Set assignment is transcribed VERBATIM from `framework.md` Part III.
Deriving it here would make the artefact disagree with the locked framework
silently; copying is not a judgement (FO §0 Tier 0).
"""
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs" / ("FM-WI-FSM-037-A03-N1L-SWE1-BedLoweringMode-HMI-V0.1"
                         " STLA 報告.xlsx")
SHEET = "Analysis Report"
HEADER_ROW = 7

# framework.md Part III，逐字轉錄。母號 -> Test Set。
# 順序沿 framework 表列，不重排。
TEST_SET_HEADINGS = [
    ("Feature Entry",      ["004", "018", "019", "025", "028", "029", "030", "039"]),
    ("Activation Gating",  ["005", "006", "007", "020", "024", "042"]),
    ("Lowering Operation", ["001", "002", "003", "021", "035", "040", "041"]),
    ("HU Feedback",        ["008", "026", "031", "032", "036"]),
    ("Cluster Feedback",   ["009", "010", "012", "033", "034"]),
    ("Fault Handling",     ["011", "037", "038"]),
    ("Restore And Exit",   ["022", "027"]),
    ("Display Legibility", ["013", "014", "015", "016"]),
    ("Access Ergonomics",  ["017", "023"]),
]

# framework.md Part III 之 leaf 數欄，供逐組對帳（分析層下放包 §六 亦載此列）
FRAMEWORK_LEAF_COUNTS = {
    "Feature Entry": 31, "Activation Gating": 28, "Lowering Operation": 33,
    "HU Feedback": 20, "Cluster Feedback": 13, "Fault Handling": 13,
    "Restore And Exit": 9, "Display Legibility": 22, "Access Ergonomics": 7,
}

REQ_RE = re.compile(r"^SWE1-HMI-BLM-(\d{3})(?:-(\d{2}))?$")


def norm(v) -> str:
    """Collapse newlines/tabs/NBSP so a cell can live in one TSV field.

    R-G16(a): the field separator must not occur in the data. Tab and newline
    are stripped rather than escaped, and NBSP (the 037 uses \\xa0 for empty
    cells) folds to empty so "blank" and "blank-looking" are the same value.
    """
    if v is None:
        return ""
    s = str(v).replace("\xa0", " ")
    s = re.sub(r"[\t\r\n]+", " ", s)
    return re.sub(r"  +", " ", s).strip()


def main() -> int:
    if not A03.exists():
        sys.exit(f"037 not found: {A03}")
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = list(wb[SHEET].iter_rows(values_only=True))
    header = [norm(c) for c in rows[HEADER_ROW - 1]]
    data = rows[HEADER_ROW:]

    def col(name_prefix: str) -> int:
        for i, h in enumerate(header):
            if h.lower().startswith(name_prefix.lower()):
                return i
        sys.exit(f"header not found: {name_prefix!r} in {header}")

    C = {k: col(v) for k, v in {
        "req_id": "SWE-Requirement ID", "src_req": "Source Requirement ID",
        "hmi_src": "HMI Source ID", "title": "Requirement Title",
        "desc": "Requirement Description", "cat": "Categorization",
        "frop": "FROP", "sub": "Sub Categorization", "prio": "Priority",
        "vcrit": "Verification Criteria", "vmeth": "Verification Method",
    }.items()}

    # 母號 -> Test Set，並驗轉錄本身無重複指派
    h2set, dup = {}, []
    for ts, heads in TEST_SET_HEADINGS:
        for h in heads:
            if h in h2set:
                dup.append((h, h2set[h], ts))
            h2set[h] = ts
    assert not dup, f"framework 轉錄有重複指派: {dup}"

    leaves, headings, unknown = [], [], []
    for r in data:
        rid = norm(r[C["req_id"]])
        if not rid:
            continue
        m = REQ_RE.match(rid)
        if not m:
            unknown.append(rid)
            continue
        parent, suffix = m.group(1), m.group(2)
        cat = norm(r[C["cat"]])
        rec = dict(req_id=rid, heading_id=parent, cat=cat,
                   title=norm(r[C["title"]]), desc=norm(r[C["desc"]]),
                   sub=norm(r[C["sub"]]), prio=norm(r[C["prio"]]),
                   vcrit=norm(r[C["vcrit"]]), vmeth=norm(r[C["vmeth"]]),
                   src_req=norm(r[C["src_req"]]), hmi_src=norm(r[C["hmi_src"]]),
                   frop=norm(r[C["frop"]]))
        (headings if suffix is None else leaves).append(rec)

    print(f"037 資料列（有 req_id）= {len(leaves) + len(headings) + len(unknown)}")
    print(f"  Heading（無 -NN 尾碼）= {len(headings)}")
    print(f"  leaf（有 -NN 尾碼）    = {len(leaves)}")
    print(f"  req_id 不合式         = {len(unknown)} {unknown or ''}")

    # Categorization 與尾碼二判準之交叉（R-G11：判準須聲明盲區）
    cat_head = sum(1 for h in headings if h["cat"] == "Heading")
    cat_leaf = sum(1 for l in leaves if l["cat"] == "Functional Requirement")
    print(f"  交叉：Heading 列 Categorization=='Heading' = {cat_head}/{len(headings)}")
    print(f"  交叉：leaf 列 Categorization=='Functional Requirement' = "
          f"{cat_leaf}/{len(leaves)}")

    # ---- R-G10 餘數驗證：全集 − 已分類 ----
    all_heads = {h["heading_id"] for h in headings}
    classified = set(h2set)
    remainder = sorted(all_heads - classified)
    overflow = sorted(classified - all_heads)
    leaf_parents = {l["heading_id"] for l in leaves}
    orphan_leaf = sorted(leaf_parents - all_heads)

    print("\n--- R-G10 餘數驗證 ---")
    print(f"037 之相異母號 = {len(all_heads)}；framework 已分類 = {len(classified)}")
    print(f"餘數（全集−已分類）= {remainder or '空'}")
    print(f"溢出（已分類−全集）= {overflow or '空'}")
    print(f"孤兒 leaf（母號不在 Heading 列中）= {orphan_leaf or '空'}")

    # ---- 逐組 leaf 數 vs framework ----
    per_set = Counter(h2set[l["heading_id"]] for l in leaves
                      if l["heading_id"] in h2set)
    print("\n--- 逐組 leaf 數（實測 vs framework Part III）---")
    mismatch = []
    for ts, _ in TEST_SET_HEADINGS:
        got, want = per_set.get(ts, 0), FRAMEWORK_LEAF_COUNTS[ts]
        flag = "OK" if got == want else "MISMATCH"
        if got != want:
            mismatch.append((ts, got, want))
        print(f"  {ts:<20} 實測 {got:>3}  framework {want:>3}  {flag}")
    print(f"  {'合計':<18} 實測 {sum(per_set.values()):>3}  "
          f"framework {sum(FRAMEWORK_LEAF_COUNTS.values()):>3}")

    # ---- Sub Categorization ----
    sub = Counter(l["sub"] for l in leaves)
    print("\n--- Sub Categorization（母體 176 leaf）---")
    for k, v in sub.most_common():
        print(f"  {k or '(空)':<12} {v}")

    # ---- N 欄（R-BLM5）----
    hmi_vals = {norm(r[C["hmi_src"]]) for r in data if norm(r[C["req_id"]])}
    print(f"\n--- N 欄來源：037 HMI Source ID 相異值數 = {len(hmi_vals)} ---")
    for v in sorted(hmi_vals):
        print(f"  {v!r}")

    src_vals = {l["src_req"] for l in leaves} | {h["src_req"] for h in headings}
    print(f"Source Requirement ID 相異值數 = {len(src_vals)}")
    frop_vals = {l["frop"] for l in leaves} | {h["frop"] for h in headings}
    print(f"FROP 相異值 = {sorted(frop_vals)}")

    # ---- 落檔 ----
    out = ROOT / "data"
    out.mkdir(exist_ok=True)

    inv = out / "leaf_inventory.tsv"
    cols = ["req_id", "heading_id", "test_set", "title", "description",
            "sub_categorization", "priority_037", "verification_criteria",
            "verification_method"]
    lines = ["\t".join(cols)]
    for l in sorted(leaves, key=lambda x: x["req_id"]):
        lines.append("\t".join([
            l["req_id"], l["heading_id"], h2set.get(l["heading_id"], ""),
            l["title"], l["desc"], l["sub"], l["prio"], l["vcrit"], l["vmeth"]]))
    inv.write_text("\n".join(lines) + "\n", encoding="utf-8")

    led = out / "heading_ledger.tsv"
    cols_h = ["heading_id", "req_id", "test_set", "title", "source_requirement_id",
              "leaf_count", "disposition"]
    lines = ["\t".join(cols_h)]
    per_head = Counter(l["heading_id"] for l in leaves)
    for h in sorted(headings, key=lambda x: x["req_id"]):
        lines.append("\t".join([
            h["heading_id"], h["req_id"], h2set.get(h["heading_id"], ""),
            h["title"], h["src_req"], str(per_head.get(h["heading_id"], 0)),
            "No TC — Heading; refer to child IDs"]))
    led.write_text("\n".join(lines) + "\n", encoding="utf-8")

    tsm = out / "test_set_map.tsv"
    lines = ["\t".join(["heading_id", "test_set", "leaf_count"])]
    for ts, heads in TEST_SET_HEADINGS:
        for h in heads:
            lines.append("\t".join([h, ts, str(per_head.get(h, 0))]))
    tsm.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n--- 產出 ---")
    for f in (inv, led, tsm):
        digest = hashlib.sha256(f.read_bytes()).hexdigest()
        n = len(f.read_text(encoding="utf-8").splitlines()) - 1
        print(f"  {f.relative_to(ROOT.parent.parent)}  資料列 {n}  sha256 {digest}")

    bad = bool(remainder or overflow or orphan_leaf or mismatch or unknown)
    print("\nVERDICT:", "FAIL" if bad else "PASS")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
