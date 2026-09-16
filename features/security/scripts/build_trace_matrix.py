#!/usr/bin/env python3
"""Security 三段追溯矩陣 —— SWE1 037 → SYS3 SYSAD → SYS2 CFTS084 → CCVR。

下放包 `docs/fw036/handoff/down/20260916_SEC-01.md` §4 任務 3 ＋
addendum `…_SEC-01_A.md` §3。可重跑，唯讀讀來源、只寫 `features/security/data/`。

來源一律取自 `sources/raw/<doc_id>/`（R-G66 來源集中制），不讀 repo 外路徑。

產物：
  data/trace_matrix.tsv    每個 SWE1 列一列
  data/trace_summary.md    計數與查詢條件
  data/batch_order.tsv     70 列之 ccvr_batch（R-SEC1(c)）
  data/step_assets.tsv     既有素材之指令／路徑／值全表（任務 3-7）
  data/no_step_source.tsv  無落地來源之 SWE1 列（R-SEC4(b) 之 PENDING 候選）
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import docx
import openpyxl

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / "sources" / "raw"
OUT = ROOT / "features" / "security" / "data"

# 六本 037 之 doc_id → 元件簡稱。順序即 trace_matrix 之列序。
SWE1_BOOKS = [
    ("swe1_037_certprovider_v1_0", "CertProvider"),
    ("swe1_037_keyinstall_v1_0", "KeyInstall"),
    ("swe1_037_sam_v1_1", "SAM"),
    ("swe1_037_ecucert", "ECUCert"),
    ("swe1_037_swdlsecurelib", "SwdlSecureLib"),
    ("swe1_037_liblogencrypt", "libLogEncrypt"),
]

SYSAD_BOOKS = [
    "sys3_sysad_certprovider_vf",
    "sys3_sysad_keyinstall_vd",
    "sys3_sysad_sam_a02",
    "sys3_sysad_ecucert_a01",
    "sys3_sysad_swdl_a01",
    "sys3_sysad_liblogencrypt_a01",
]

# R-SEC1(b)：落到這五個 CCVR test item 者 ccvr_batch = 1，否則 2。
BATCH1_SHEETS = (
    "Auth-Boot CS.93",
    "Auth-Prog CS.93",
    "Cert Val CS.98",
    "ECU ID CS.165",
    "Secure Log CS.212",
)

RE_SEC = re.compile(r"SYS-RA-SEC-\d+")
RE_OTHER_SYSRA = re.compile(r"SYS-RA-(?!SEC-)[A-Z0-9]+-\d+")
RE_SYSAD = re.compile(r"SYSAD_[A-Za-z0-9_ ]+")
# 下放包規則 7 之 `[a-z][A-Za-z]+Test[A-Za-z]*` 無左邊界，會自 `CertProviderServiceManagerTest`
# 內部之 `e` 起切出 `ertProviderServiceManagerTest`。補左邊界，其餘逐字不動。
RE_APK = re.compile(r"(?<![A-Za-z])[a-z][A-Za-z]+Test[A-Za-z]*")
# R-SEC5(a)：CS.212 第二判準之斷言詞，**逐字取條文所列五詞**（`log`／`Logdog`／`logdog`／
# `avc`／`logcat`），大小寫敏感、不加詞界。此式與任務 3-6 之 grep 同集（11 列，見上繳包）。
# 若改為不分大小寫，`Log Encryption`／`LogDog` 之**元件名**會被誤判為 log 斷言（+6 列，
# 上繳包已具名）—— 元件名不是斷言，故不放寬。
RE_LOG_ASSERT = re.compile(r"log|Logdog|logdog|avc|logcat")
# R-SEC{live+4} 之術語落差（_B §1）：CertProvider-004/005 之撤銷清單型態未定。
TERM_CRL_DCL_ROWS = {"SWE1-CertProvider-004", "SWE1-CertProvider-005"}
# _F §2：CertProfile（Code Signing 樹）可逐字落地之欄位斷言 → SWE1 列（R-SEC4(a) 第 8 類）。
CERTPROFILE_ROWS = {
    "SWE1-CertProvider-001": "chain/BasicConstraints/KeyUsage（r11,r18,r25-r39）",
    "SWE1-CertProvider-002": "Subject CN／O（r13-r19）",
    "SWE1-CertProvider-003": "Issuer CN（r6-r11）",
    "SWE1-CertProvider-005": "CDP／AIA（r40,r43）",
    "SWE1-CertProvider-011": "CertificatePolicies OID（r36，尾碼佔位）",
}
# 演算法與 Validity 為「全」列適用（r5,r12,r20-r22,r44）
CERTPROFILE_ALL = "algorithm/validity（r5,r12,r20-r22,r44）"
# SAM 樹與 ECU Identity 樹之 profile 未到手 → DR-SEC-q
CERTPROFILE_PENDING_Q = {"SWE1-SAM-0007", "SWE1-CertProvider-002", "SWE1-CertProvider-003"}
# 去尾綴後之基底名（R-G62 §4 任務 3 規則 5）
BASE_SUFFIXES = ("_COMP", "_INTF", "_API", "_BINDER")


def only(doc_id: str, pattern: str) -> Path:
    hits = sorted((RAW / doc_id).glob(pattern))
    if len(hits) != 1:
        raise SystemExit(f"{doc_id}: 期望 1 檔，實得 {len(hits)}")
    return hits[0]


def norm(sysad: str) -> str:
    """SYSAD 正規化：去除所有空白字元（任務 3 規則 2）。"""
    return re.sub(r"\s+", "", sysad).rstrip("_").upper()


def strip_base(nid: str) -> str:
    for suf in BASE_SUFFIXES:
        if nid.endswith(suf):
            return nid[: -len(suf)]
    return nid


def split_source_ids(raw: str) -> list[str]:
    """B 欄依換行／逗號／空格三分隔拆（R-SEC3(c)）。

    空格同時是**分隔符**（CertProvider-006/010：`SYSAD_A SYSAD_B`）與 ID **內含之雜訊**
    （libLogEncrypt：`SYSAD_SECURITY_ LOGENCRYPT_ENCRYPTION_COMP`）。逐字切在
    `SYSAD` 起點上即可同時滿足兩者 —— 兩個 ID 之間必有一個新的 `SYSAD` 起點，
    ID 內含之空格則不構成起點。切出之片段再交 `norm()` 去空白。
    """
    out: list[str] = []
    for frag in re.split(r"[\n,;]+", raw or ""):
        starts = [m.start() for m in re.finditer(r"SYSAD", frag, re.I)]
        for i, st in enumerate(starts):
            en = starts[i + 1] if i + 1 < len(starts) else len(frag)
            piece = frag[st:en].strip()
            if piece:
                out.append(piece)
    return out


# ---------------------------------------------------------------- SWE1 037

def read_swe1() -> list[dict]:
    rows: list[dict] = []
    for doc_id, comp in SWE1_BOOKS:
        path = only(doc_id, "*.xlsx")
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        grid = list(wb["Analysis Report"].iter_rows(values_only=True))
        header = [str(c or "").strip() for c in grid[7]]
        # 欄索引以 row 8 之欄名定位（#1/#2 18 欄、#3~#6 19 欄，Q/R vs R/S）
        idx_vc = header.index("Verification Criteria")
        idx_vm = next(i for i, h in enumerate(header) if h.startswith("Verification Method"))
        for n, r in enumerate(grid[8:], start=9):
            a = "" if r[0] is None else str(r[0]).strip()
            b = "" if len(r) < 2 or r[1] is None else str(r[1]).strip()
            if not a and not b:
                continue
            src_ids = split_source_ids(b)
            # R-SEC3(b)：ECUCert 無 SWE-Requirement ID，暫取 Source Requirement ID 首值
            swe1_id = a or (src_ids[0] if src_ids else f"{comp}-row{n}")
            rows.append(
                {
                    "swe1_file": doc_id,
                    "component": comp,
                    "excel_row": n,
                    "swe1_id": swe1_id,
                    "id_is_placeholder": "Y" if not a else "N",
                    "swe1_title": str(r[2] or "").strip().replace("\n", " "),
                    "source_ids_raw": b.replace("\n", " ⏎ "),
                    "source_ids": src_ids,
                    "verification_criteria": str(r[idx_vc] or "").strip(),
                    "verification_method": str(r[idx_vm] or "").strip().replace("\n", " "),
                }
            )
        wb.close()
    return rows


# ------------------------------------------------------------- SYS3 SYSAD

def read_sysad() -> tuple[dict, dict, dict, dict]:
    """→ (sysad→SEC 集合, sysad→other_sysra, sysad→來源標記, sysad→介面表旗標)"""
    sec_of: dict[str, set[str]] = defaultdict(set)
    other_of: dict[str, set[str]] = defaultdict(set)
    prov_of: dict[str, set[str]] = defaultdict(set)
    iface_of: dict[str, set[str]] = defaultdict(set)
    for doc_id in SYSAD_BOOKS:
        doc = docx.Document(str(only(doc_id, "*.docx")))
        book = doc_id.replace("sys3_sysad_", "")
        for ti, tbl in enumerate(doc.tables):
            cells = [[c.text.strip() for c in row.cells] for row in tbl.rows]
            if not cells:
                continue
            label0 = cells[0][0] if cells[0] else ""
            if label0.startswith("SYSAD_ID") and len(cells[0]) > 1:
                # style A —— 每元素一表
                ids = [norm(x) for x in RE_SYSAD.findall(cells[0][1])] or [norm(cells[0][1])]
                secs, others = set(), set()
                has_iface = False
                for row in cells:
                    lab = re.sub(r"\s+", " ", row[0])
                    val = " ".join(row[1:])
                    if lab.startswith("Mapped SYSRA-ID") or lab.startswith("Mapped SYSRS-ID"):
                        secs |= set(RE_SEC.findall(val))
                        others |= set(RE_OTHER_SYSRA.findall(val))
                    if lab.startswith(("Flow chart", "Input Criteria", "Output Criteria")) and val.strip():
                        has_iface = True
                for sid in ids:
                    sec_of[sid] |= secs
                    other_of[sid] |= others
                    prov_of[sid].add(f"{book}:elem[T{ti}]")
                    if has_iface:
                        iface_of[sid].add(f"{book}:T{ti}")
                continue
            # style B —— Table 11「SYS2 ID 對應 SYSAD ID」：同列共現即對應
            for row in cells:
                line = " ".join(row)
                secs = set(RE_SEC.findall(line))
                ids = [norm(x) for x in RE_SYSAD.findall(line)]
                if secs and ids:
                    for sid in ids:
                        sec_of[sid] |= secs
                        other_of[sid] |= set(RE_OTHER_SYSRA.findall(line))
                        prov_of[sid].add(f"{book}:tbl11[T{ti}]")
    return sec_of, other_of, prov_of, iface_of


# ------------------------------------------------------------ SYS2 索引

def read_sys2() -> dict[str, dict]:
    path = only("ccvr_v27_sys2_mapped", "*.xlsx")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    grid = list(wb["SYS2 traceability"].iter_rows(values_only=True))
    out = {}
    for r in grid[1:]:
        sid = str(r[0] or "").strip()
        if not sid.startswith("SYS-RA-SEC"):
            continue
        out[sid] = {
            "nrl": str(r[1] or "").strip(),
            "desc": str(r[2] or "").strip().replace("\n", " "),
            "category": str(r[3] or "").strip(),
            "harman": str(r[6] or "").strip().replace("\n", " "),
            "md": str(r[7] or "").strip().replace("\n", " "),
            "existing_rel": str(r[8] or "").strip().replace("\n", " "),
            "existing_tests": str(r[9] or "").strip().replace("\n", " "),
            "new_test_ids": str(r[10] or "").strip().replace("\n", " "),
        }
    wb.close()
    return out


def read_mapping_detail() -> dict[str, list[tuple[str, str]]]:
    path = only("ccvr_v27_sys2_mapped", "*.xlsx")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for r in list(wb["Mapping detail"].iter_rows(values_only=True))[1:]:
        sid = str(r[3] or "").strip()
        if not sid.startswith("SYS-RA-SEC"):
            continue
        key = str(r[0] or "").strip()
        out[sid].append((key, str(r[4] or "").strip()))
    wb.close()
    return out


def read_cs98_steps() -> dict[str, dict]:
    """Cert Val CS.98 之 STEPS 欄（實測為 E 欄，下放包記 D 欄）→ 每 CCVR 列。"""
    path = only("ccvr_v27_sys2_mapped", "*.xlsx")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    grid = list(wb["Cert Val CS.98"].iter_rows(values_only=True))
    header = [str(c or "").strip() for c in grid[0]]
    i_steps = next(i for i, h in enumerate(header) if h.startswith("STEPS"))
    i_sec = next(i for i, h in enumerate(header) if h.startswith("SYS2 Sys-RA-Feature-ID"))
    out = {}
    for n, r in enumerate(grid[1:], start=2):
        no = str(r[0] or "").strip()
        if not no:
            continue
        steps = str(r[i_steps] or "")
        out[f"Cert Val CS.98 / {no}"] = {
            "row": n,
            "steps": steps,
            "methods": sorted(set(RE_APK.findall(steps))),
            "secs": sorted(set(RE_SEC.findall(str(r[i_sec] or "")))),
        }
    wb.close()
    return out


def read_cs165_steps() -> dict[str, dict]:
    path = only("ccvr_v27_sys2_mapped", "*.xlsx")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    grid = list(wb["ECU ID CS.165"].iter_rows(values_only=True))
    header = [str(c or "").strip() for c in grid[0]]
    i_steps = header.index("Test steps")
    i_exp = header.index("Expected result")
    i_log = header.index("Log pattern")
    out = {}
    for n, r in enumerate(grid[1:], start=2):
        no = str(r[0] or "").strip()
        if not no:
            continue
        body = "\n".join(str(r[i] or "") for i in (i_steps, i_exp, i_log)).strip()
        if body:
            out[f"ECU ID CS.165 / {no}"] = {"row": n, "body": body}
    wb.close()
    return out


def read_test_items() -> list[str]:
    txt = only("ccvr_cs98_test_items", "*.txt").read_text(encoding="utf-8")
    return re.findall(r":\s*([a-z][A-Za-z]+Test[A-Za-z]*|[a-z][A-Za-z]*Cert[A-Za-z]*)\s*$", txt, re.M)


# ------------------------------------------------------------------ 主流程

# R-SEC7（_E §3）：每步可配通道之預判。判準逐條可查，不憑印象：
#   N  —— VC 之受詞為 source code／build environment（黑箱無入口，且無外部可執行素材）
#   Y  —— 有 APK／PDF／CS98／CS165 任一（既有素材已給完整指令或完整操作序列）
#   部分 —— 其餘（VC 內含具體指令／路徑／值，但無外部可執行素材補齊全部步驟）
RE_WHITEBOX = re.compile(r"source code|build environment|project build|In source code", re.I)
RE_CONCRETE = re.compile(r"openssl|adb |/data/|/mnt/|/odm/|/vendor/|installstate|\.sh\b|USB")


def channel_feasibility(row: dict, srcs: list[str]) -> tuple[str, str]:
    kinds = {s.split(":")[0] for s in srcs}
    if kinds & {"APK", "PDF", "CS98", "CS165"}:
        return "Y", "有外部可執行素材：" + "、".join(sorted(kinds & {"APK", "PDF", "CS98", "CS165"}))
    vc = row["verification_criteria"]
    if RE_WHITEBOX.search(vc) and not RE_CONCRETE.search(vc):
        return "N", "VC 受詞為 source code／build environment，無外部入口"
    if RE_CONCRETE.search(vc):
        return "部分", "VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟"
    return "N", "VC 無具體指令／路徑／值，且無外部素材"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    swe1 = read_swe1()
    sec_of, other_of, prov_of, iface_of = read_sysad()
    sys2 = read_sys2()
    mapdetail = read_mapping_detail()
    cs98 = read_cs98_steps()
    cs165 = read_cs165_steps()
    apk_items = read_test_items()

    # PDF 六步（reference-only）之適用面：ECUCert 環境建置
    pdf_available = (RAW / "ccvr_ecu_cert_test_steps_20260826").exists()

    fields = [
        "swe1_file", "component", "excel_row", "swe1_id", "id_is_placeholder",
        "swe1_title", "source_ids_raw", "sysad_normalized", "match_kind",
        "other_sysra", "sys_ra_sec", "nrl", "sys2_category", "harman_status",
        "md_status", "existing_test_rel", "ccvr_sheet_rows", "new_test_ids",
        "apk_method", "verification_method", "ccvr_batch", "ccvr_items",
        "cs212_direct", "step_sources", "channel_feasible", "channel_feasible_why",
    ]
    out_rows = []
    stats = Counter()
    per_book = defaultdict(Counter)

    for row in swe1:
        norms, kinds = [], []
        secs, others, ifaces = set(), set(), set()
        for sid in row["source_ids"]:
            n = norm(sid)
            norms.append(n)
            if n in sec_of:
                kinds.append("exact")
                secs |= sec_of[n]
                others |= other_of[n]
                ifaces |= iface_of.get(n, set())
            else:
                b = strip_base(n)
                if b != n and b in sec_of:
                    kinds.append(f"base:{b}")
                    secs |= sec_of[b]
                    others |= other_of[b]
                    ifaces |= iface_of.get(b, set())
                else:
                    kinds.append("none")
                    if n in iface_of:
                        ifaces |= iface_of[n]
        kind = ("exact" if all(k == "exact" for k in kinds) and kinds
                else "none" if all(k == "none" for k in kinds) or not kinds
                else "mixed" if any(k == "none" for k in kinds) else "base")
        per_book[row["swe1_file"]][kind.split(":")[0]] += 1

        secs_sorted = sorted(secs, key=lambda s: int(s.rsplit("-", 1)[1]))
        nrl, cat, harman, md, rel, newids = [], [], [], [], [], []
        for s in secs_sorted:
            m = sys2.get(s)
            if not m:
                stats["sys2_miss"] += 1
                continue
            nrl.append(m["nrl"])
            cat.append(m["category"])
            harman.append(m["harman"])
            md.append(m["md"])
            rel.append(m["existing_rel"])
            if m["new_test_ids"]:
                newids.append(m["new_test_ids"])

        ccvr_keys, apk = [], set()
        for s in secs_sorted:
            for key, relation in mapdetail.get(s, []):
                ccvr_keys.append(f"{key} [{relation}]")
        ccvr_keys = sorted(set(ccvr_keys))
        plain_keys = {k.split(" [")[0] for k in ccvr_keys}
        for k in plain_keys:
            if k in cs98:
                apk |= set(cs98[k]["methods"])

        # R-SEC5(a)：CS.212 之落點改用第二判準 —— 037 之 log 斷言直連，不經 SYS2。
        # 其成因見 up 包 4-6：CS.212 在 `Mapping detail` 只對 SYS-RA-SEC-671，而六本 037 之鏈不經 671。
        cs212_direct = bool(RE_LOG_ASSERT.search(row["verification_criteria"]))
        batch1_items = sorted({k.split(" / ")[0] for k in plain_keys} & set(BATCH1_SHEETS))
        if cs212_direct and "Secure Log CS.212" not in batch1_items:
            batch1_items.append("Secure Log CS.212")
        batch = "1" if batch1_items else "2"

        # step_sources（addendum §3 ＋ R-SEC4(a)）
        srcs = []
        if row["verification_criteria"]:
            srcs.append("VC")
        for m in sorted(apk):
            srcs.append(f"APK:{m}")
        for k in sorted(plain_keys):
            if k in cs98 and cs98[k]["steps"].strip():
                srcs.append(f"CS98:{cs98[k]['row']}")
            if k in cs165:
                srcs.append(f"CS165:{cs165[k]['row']}")
        if pdf_available and row["component"] == "ECUCert":
            srcs.append("PDF:1-6")
        for t in sorted(ifaces):
            srcs.append(f"SYSAD:{t}")
        if row["swe1_id"] in CERTPROFILE_ROWS:
            srcs.append(f"CERTPROFILE:{CERTPROFILE_ROWS[row['swe1_id']]}")
        elif row["component"] == "CertProvider":
            srcs.append(f"CERTPROFILE:{CERTPROFILE_ALL}")
        # R-SEC8(h)：DR-SEC-q 降級為 reference，不再作 PENDING 理由。
        # 標記保留（提示該列之欄位細節須寫至 037／CS.165 原文粒度，不依 CertProfile 擴張）。
        if row["swe1_id"] in CERTPROFILE_PENDING_Q or row["component"] == "ECUCert":
            srcs.append("REF:DR-SEC-q(037/CS165 原文粒度)")
        if row["swe1_id"] in TERM_CRL_DCL_ROWS:
            srcs.append("TERM:CRL|DCL")  # _B §1：注入檔型態未定，TC 寫 PENDING: DR-SEC-j

        feas, feas_why = channel_feasibility(row, srcs)
        out_rows.append({
            "channel_feasible": feas,
            "channel_feasible_why": feas_why,
            "swe1_file": row["swe1_file"],
            "component": row["component"],
            "excel_row": row["excel_row"],
            "swe1_id": row["swe1_id"],
            "id_is_placeholder": row["id_is_placeholder"],
            "swe1_title": row["swe1_title"],
            "source_ids_raw": row["source_ids_raw"],
            "sysad_normalized": ";".join(norms),
            "match_kind": kind + ("|" + ",".join(kinds) if kind in ("base", "mixed") else ""),
            "other_sysra": ";".join(sorted(others)),
            "sys_ra_sec": ";".join(secs_sorted),
            "nrl": ";".join(nrl),
            "sys2_category": ";".join(sorted(set(cat))),
            "harman_status": ";".join(sorted({x for x in harman if x})),
            "md_status": ";".join(sorted({x for x in md if x})),
            "existing_test_rel": ";".join(sorted({x for x in rel if x})),
            "ccvr_sheet_rows": ";".join(ccvr_keys),
            "new_test_ids": ";".join(sorted(set(newids))),
            "apk_method": ";".join(sorted(apk)),
            "verification_method": row["verification_method"],
            "ccvr_batch": batch,
            "ccvr_items": "、".join(batch1_items),
            "cs212_direct": "Y" if cs212_direct else "N",
            "step_sources": ";".join(srcs),
        })

    with (OUT / "trace_matrix.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)

    # batch_order.tsv（R-SEC1(c)）
    with (OUT / "batch_order.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "ccvr_batch", "ccvr_items", "reason"])
        for r in out_rows:
            items = sorted({k.split(" / ")[0] for k in
                            (x.split(" [")[0] for x in r["ccvr_sheet_rows"].split(";") if x)})
            b1 = [i for i in r["ccvr_items"].split("、") if i]
            if r["ccvr_batch"] == "1":
                bits = []
                mapped = [i for i in b1 if i in items]
                if mapped:
                    bits.append("Mapping detail 落點：" + "、".join(mapped))
                if r["cs212_direct"] == "Y":
                    bits.append("SWE1-direct（037 log 斷言，R-SEC5(a)）")
                reason = "；".join(bits)
            else:
                reason = "未落 CCVR 五 test item" + (
                    "；其他落點：" + "、".join(items) if items else "；Mapping detail 無對應")
            w.writerow([r["swe1_id"], r["ccvr_batch"], "、".join(b1) or "-", reason])

    # 無落地來源清單（R-SEC4(b)）
    nosrc = [r for r in out_rows if not r["step_sources"]]
    with (OUT / "no_step_source.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "component", "verification_method", "ccvr_batch"])
        for r in nosrc:
            w.writerow([r["swe1_id"], r["component"], r["verification_method"], r["ccvr_batch"]])

    # summary
    lines = ["# trace_summary —— Security 三段追溯實測", "",
             "由 `features/security/scripts/build_trace_matrix.py` 產生，可重跑。",
             "來源一律 `sources/raw/<doc_id>/`。", "",
             "## 1　每本 037 之 match_kind 計數",
             "", "| 037 | exact | base | mixed | none | 列 |", "|---|---|---|---|---|---|"]
    for doc_id, _ in SWE1_BOOKS:
        c = per_book[doc_id]
        lines.append(f"| `{doc_id}` | {c['exact']} | {c['base']} | {c['mixed']} | {c['none']} | {sum(c.values())} |")
    tot = Counter()
    for c in per_book.values():
        tot.update(c)
    lines.append(f"| **合計** | {tot['exact']} | {tot['base']} | {tot['mixed']} | {tot['none']} | {sum(tot.values())} |")
    lines += ["", "查詢條件：SWE1 `Analysis Report` row 9 起，A 或 B 欄非空；"
              "B 欄以換行／逗號／空格三分隔拆；SYSAD 去所有空白後比對；"
              "`base` 只在 `exact` 落空時試（去 `_COMP`／`_INTF`／`_API`／`_BINDER`）。",
              "`mixed` = 同列多個 SYSAD，部分命中部分未命中。", ""]

    all_secs = sorted({s for r in out_rows for s in r["sys_ra_sec"].split(";") if s},
                      key=lambda s: int(s.rsplit("-", 1)[1]))
    miss = [s for s in all_secs if s not in sys2]
    lines += ["## 2　SYS2 命中", "",
              f"- 鏈上 SEC ID 併集：**{len(all_secs)}**",
              f"- 在 `SYS2 traceability`（A 欄）命中：**{len(all_secs) - len(miss)}／{len(all_secs)}**，缺 {len(miss)}"
              + (f"：{', '.join(miss)}" if miss else ""),
              f"- `SYS2 traceability` 總列（A 欄非空且為 SEC）：{len(sys2)}", ""]
    relc = Counter()
    for s in all_secs:
        if s in sys2:
            relc[sys2[s]["existing_rel"] or "(空)"] += 1
    lines += ["`Existing test relationship`（I 欄）分佈：", ""]
    lines += [f"- {k}：{v}" for k, v in relc.most_common()]
    harc = Counter()
    for s in all_secs:
        if s in sys2:
            harc[sys2[s]["harman"] or "(空)"] += 1
    lines += ["", "`HARMAN status`（G 欄）分佈：", ""]
    lines += [f"- {k}：{v}" for k, v in harc.most_common()]

    b = Counter(r["ccvr_batch"] for r in out_rows)
    lines += ["", "## 3　ccvr_batch 計數（R-SEC1(b)）", "",
              f"- batch 1（落 CCVR 五 test item）：**{b['1']}** 列",
              f"- batch 2（未落）：**{b['2']}** 列",
              f"- 合計：{sum(b.values())} 列", "",
              "| 元件 | batch 1 | batch 2 |", "|---|---|---|"]
    per_comp = defaultdict(Counter)
    for r in out_rows:
        per_comp[r["component"]][r["ccvr_batch"]] += 1
    for _, comp in SWE1_BOOKS:
        lines.append(f"| {comp} | {per_comp[comp]['1']} | {per_comp[comp]['2']} |")

    lines += ["", "## 4　無落地來源清單（R-SEC4(b)：PENDING 候選）", "",
              f"共 **{len(nosrc)}** 列（清單 `data/no_step_source.tsv`）。", ""]
    if nosrc:
        lines += ["| SWE1 ID | 元件 | Verification Method | batch |", "|---|---|---|---|"]
        lines += [f"| `{r['swe1_id']}` | {r['component']} | {r['verification_method']} | {r['ccvr_batch']} |"
                  for r in nosrc]

    feas = Counter(r["channel_feasible"] for r in out_rows)
    lines += ["", "## 4b　每步可配通道之預判（R-SEC7／_E §3）", "",
              "判準：`Y` = 有 APK／PDF／CS98／CS165 任一外部可執行素材；",
              "`N` = VC 受詞為 source code／build environment 且無具體指令；`部分` = 其餘。", "",
              f"- `Y`：**{feas['Y']}** 列",
              f"- `部分`：**{feas['部分']}** 列",
              f"- `N`：**{feas['N']}** 列 —— 即 batch 內之 `PENDING` 候選（R-SEC4(b)）", "",
              "| SWE1 ID | 元件 | batch | 預判 | 依據 |", "|---|---|---|---|---|"]
    lines += [f"| `{r['swe1_id']}` | {r['component']} | {r['ccvr_batch']} | **{r['channel_feasible']}** | {r['channel_feasible_why']} |"
              for r in out_rows if r["channel_feasible"] != "Y"]

    cp_rows = [r for r in out_rows if r["component"] == "CertProvider"]
    cp_named = [r for r in cp_rows if r["swe1_id"] in CERTPROFILE_ROWS]
    q_rows = [r for r in out_rows if "REF:DR-SEC-q" in r["step_sources"]]
    lines += ["", "## 4c　CertProfile 之欄位斷言落地（_F §2／§5）", "",
              f"- CertProvider 共 **{len(cp_rows)}** 列。",
              f"- 其中 **{len(cp_named)}** 列之欄位斷言可由 `CertProfile` **逐字**落地"
              f"（{'、'.join('`'+r['swe1_id']+'`' for r in cp_named)}）。",
              f"- 其餘 **{len(cp_rows) - len(cp_named)}** 列只掛「全」列適用之演算法／Validity 斷言。",
              f"- 標 `REF:DR-SEC-q`（SAM 樹／ECU Identity 樹 profile 未到手；**R-SEC8(h) 已降級為 reference，不作 PENDING 理由**）：**{len(q_rows)}** 列 ——"
              f" CertProvider 之 SAM 分支 2 列、`SWE1-SAM-0007`、ECUCert 全 13 列。",
              "",
              "> **限制**：CertProfile 為 **BETA/preprod ROW** 本。PROD 樹（CS.98 第 10 項）之 CN 與 CDP 必不同，",
              "> PROD 場景之值一律 `PENDING: DR-SEC-c/… PROD cert profile`。",
              "> OID 尾碼（`1.3.6.1.4.1.57872.` 之後）sheet 未給實值 → 保留佔位 `<…>`，不造值（IN §8.4.1）。",
              ""]
    lines += ["", "## 5　apk 方法交叉核對（任務 3 規則 7）", "",
              f"- `Test_Items.txt` 之方法：**{len(apk_items)}** 條",
              f"- `Cert Val CS.98` STEPS 抽出：**{len({m for v in cs98.values() for m in v['methods']})}** 條",
              f"- 交集：**{len(set(apk_items) & {m for v in cs98.values() for m in v['methods']})}** 條", ""]
    inter = sorted(set(apk_items) & {m for v in cs98.values() for m in v["methods"]})
    lines += [f"- 交集清單：{', '.join(inter)}" if inter else "- 交集為空 —— 觸發升級條件"]
    only_txt = sorted(set(apk_items) - {m for v in cs98.values() for m in v["methods"]})
    if only_txt:
        lines.append(f"- 只在 `Test_Items.txt`：{', '.join(only_txt)}")

    (OUT / "trace_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"trace_matrix.tsv  {len(out_rows)} 列")
    print(f"batch_order.tsv   batch1={b['1']} batch2={b['2']}")
    print(f"no_step_source    {len(nosrc)} 列")
    print(f"SEC 併集 {len(all_secs)}，SYS2 缺 {len(miss)}")
    print("match_kind:", dict(tot))
    return 0


if __name__ == "__main__":
    sys.exit(main())
