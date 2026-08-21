#!/usr/bin/env python3
"""Step 3 (Time Management) — 機械漂移檢查，掃 `generated/*.json`。

modified by TC_Generator analysis round 05R under G-TM1/G-TM2

## 本檔之來源與界線（R-TM29）

**結構參照** `features/privacy/scripts/lint_tcs.py`（同為 BLANK workbook、
rev C 母本、spec_mode D，形態最近）：權威讀取而非寫死、閘門逐條回傳
`(gate, message)`、`--self-test` 對每閘造紅綠兩向、exit 0/1/2 之語義。

**不繼承其內容**（R-TM10-A1，射程由 R-TM29 界定）：步驟措辭常數、
ER 樣板字串、Test Set 值、priority 預設一律留 `TODO(R-TM10-A1)`，
待本 feature 依條文決定。Privacy 之 `step-actions`／`negative-scope`
兩閘編碼的是 R33-5／R33-1(d)，**那是 Privacy 之裁決，本 feature 不援引**。

## 權威一律讀取，不寫死

  design_method 詞彙  → 母本 `下拉選單` 分頁（`feature.yaml`
                        `lint.design_method_source: dropdown_sheet`）
  欄位對映            → `feature.yaml` `workbook.columns`（rev C：
                        design_method `R`、functional_safety `S`、
                        author `AA`、remarks `AH`）
  test_group          → `feature.yaml` `test_group`（`Time and Date`，R-TM8）
  spec_reference 形態 → `feature.yaml` `spec_reference_template`
                        ＋ CFTS015 docx 內實際存在之物件 id（**查得，不推算**）

exit 0 = 無發現，1 = 至少一項發現，2 = 呼叫錯誤。

用法：
    python3 features/time_management/scripts/lint_tcs.py --feature-dir features/time_management
    python3 features/time_management/scripts/lint_tcs.py --feature-dir features/time_management --self-test

**本腳本於 04 包只建立不執行**（下放包 §8「不執行 T5 所建之任何腳本」）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
import html
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


PENDING_RE = re.compile(r"PENDING:\s*DR-\d+")      # canon §8.4.3 佔位形式
TEST_ITEM_TOKEN_MAX = 50                            # canon §4.3.1 上半上限
TEST_ITEM_TAIL_RE = re.compile(r"\([^)]+\)\s*$")    # canon §4.3.1 下半括號
DESIGN_METHOD_COUNT = 9          # B6 —— 母本 下拉選單!$A$1:$A$9
LEAF_COUNT = 22                  # B2 —— 037 之 leaf 全集
# B3 / B4 / C1 之裁決值取自 tm_rulings —— **context 層與本檔之單一來源**
# （06 §4.2）。各寫一份會漂移，且漂移時 lint 全綠：context 說 A、lint 驗 B，
# 生成照 A 寫則被 B 攔，呈現為「模型出錯」而非「規則不一致」。
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tm_rulings import (                      # noqa: E402
    SPEC_GAP_LEAVES, TEST_SETS, BOUNDARY_SIGNALS)

SPEC_REF_RE = re.compile(r"^CFTS015-(\d{7})$")      # B7(i) —— canon §10.7(a)

class LintError(RuntimeError):
    """呼叫或權威讀取之失敗 —— 與「發現」區分，走 exit 2。"""


# ── 權威讀取 ────────────────────────────────────────────────
def load_authorities(feature_dir: Path) -> dict:
    """自 `feature.yaml`、母本與 spec docx 讀出全部權威值。

    **任何一項讀不到即 raise** —— 不以預設值頂替（R-TM7 同族：
    寫死之預設會使閘門在權威缺席時仍然全綠）。
    """
    if yaml is None:
        raise LintError("PyYAML 不可用")
    cfg_path = feature_dir / "feature.yaml"
    if not cfg_path.exists():
        raise LintError(f"缺 {cfg_path}")
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))

    wb_rel = cfg["paths"]["workbook"]
    wb_path = feature_dir / wb_rel
    if not wb_path.exists():
        raise LintError(f"母本不存在：{wb_path}")

    auth = {
        "cfg": cfg,
        "feature_dir": feature_dir,
        "workbook": wb_path,
        "sheet": cfg["workbook"]["sheet"],
        "header_row": int(cfg["workbook"]["header_row"]),
        "columns": dict(cfg["workbook"]["columns"]),
        "test_group": cfg["test_group"],
        "spec_template": cfg.get("spec_reference_template", ""),
        "design_methods": read_design_methods(wb_path, cfg),
        "spec_objects": read_spec_objects(feature_dir, cfg),
        "leaves": read_leaves(feature_dir),          # B2
        "priority": read_priority_domain(wb_path, cfg),   # C2
        "sys2_items": read_sys2_items(feature_dir, cfg),  # B7(ii)
    }
    return auth


def read_leaves(feature_dir: Path) -> set[str]:
    """B2 —— leaf 全集，唯一來源為 data/leaf_descriptions.txt（R-TM24）。"""
    path = feature_dir / "data" / "leaf_descriptions.txt"
    if not path.exists():
        raise LintError(
            f"缺 {path} —— 該檔為 leaf id 與 test_item 上半之唯一許可來源"
            "（R-TM24）。其對策為來源隔離，非人工記得")
    leaves = set(re.findall(r"SWE-RA-TIME&DATE-\d{3}",
                            path.read_text(encoding="utf-8")))
    if len(leaves) != LEAF_COUNT:
        raise LintError(
            f"{path.name} 讀到 {len(leaves)} 筆 leaf，期望 {LEAF_COUNT}")
    return leaves


def read_priority_domain(workbook: Path, cfg: dict) -> set[str]:
    """C2 —— priority 值域自母本 P 欄 DV 讀出，不寫死字面。"""
    import zipfile
    z = zipfile.ZipFile(workbook)
    xml = z.read("xl/worksheets/sheet6.xml").decode("utf-8")
    z.close()
    for m in re.finditer(r"<dataValidation\b[^>]*>(.*?)</dataValidation>",
                         xml, re.S):
        f1 = re.search(r"<formula1>\"?([^<\"]*)\"?</formula1>", m.group(1))
        if not f1:
            continue
        vals = {x.strip() for x in f1.group(1).split(",") if x.strip()}
        if vals and all(re.fullmatch(r"P[0-3]", v) for v in vals):
            return vals
    raise LintError(
        "母本工作表未讀到 P0..P3 之 dataValidation —— 不以寫死字面頂替，"
        "母本自身之清單才是值域權威")


def read_sys2_items(feature_dir: Path, cfg: dict) -> set[str]:
    """B7(ii) —— SYS2 第 5 欄之物件 id 全集。"""
    import openpyxl
    rel = cfg["paths"].get("sys1_export")
    if not rel:
        raise LintError("feature.yaml 未宣告 sys1_export（SYS2 匯出）")
    path = feature_dir / rel
    if not path.exists():
        raise LintError(f"SYS2 匯出不存在：{path}")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ids: set[str] = set()
    for r in wb["Basic Report"].iter_rows(min_row=2, values_only=True):
        for tok in re.split(r"[,\n]+", str(r[4] or "")):
            tok = tok.strip()
            if re.fullmatch(r"\d{7}", tok):
                ids.add(tok)
    wb.close()
    if not ids:
        raise LintError("SYS2 第 5 欄未讀到任何 7 位物件 id")
    return ids


def read_design_methods(workbook: Path, cfg: dict) -> set[str]:
    """自母本之 `下拉選單` 分頁讀 design_method 詞彙（逐字，不正規化）。"""
    if cfg.get("lint", {}).get("design_method_source") != "dropdown_sheet":
        raise LintError("feature.yaml 未宣告 design_method_source=dropdown_sheet")
    import openpyxl
    wb = openpyxl.load_workbook(workbook, data_only=True, read_only=True)
    if "下拉選單" not in wb.sheetnames:
        wb.close()
        raise LintError("母本無 `下拉選單` 分頁")
    ws = wb["下拉選單"]
    vals: set[str] = set()
    for row in ws.iter_rows(values_only=True):
        for c in row:
            if c is None:
                continue
            s = str(c).strip()
            # 設計方法詞條之形態為「中文 (English)」；其餘欄位不收
            if s and "(" in s and ")" in s:
                vals.add(s)
    wb.close()
    if not vals:
        raise LintError("`下拉選單` 分頁未讀到任何設計方法詞條")
    return vals


def read_spec_objects(feature_dir: Path, cfg: dict) -> set[str]:
    """自 CFTS015 docx 讀出實際存在之物件 id。

    **查得，不推算** —— Privacy 之 R30-1 記載了以偏移量推算 id 產生兩個
    錯誤 id 之實例；本 feature 不重蹈，每次執行都重讀 docx。
    """
    rel = cfg["paths"].get("spec_pdf")
    if not rel:
        raise LintError("feature.yaml 未宣告 spec_pdf（CFTS015 docx）")
    path = feature_dir / rel
    if not path.exists():
        raise LintError(f"spec docx 不存在：{path}")
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    ids: set[str] = set()
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
        t = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
        m = re.match(r"^(\d{6,8})\s*:", t)
        if m:
            ids.add(m.group(1))
    if not ids:
        raise LintError("spec docx 未讀到任何物件 id")
    return ids


# ── 逐條閘門 ────────────────────────────────────────────────
def _steps(text: str) -> list[str]:
    return [s for s in str(text or "").split("\n") if s.strip()]


def lint_required_fields(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """必填欄位齊全**且非空** —— 欄名取自 `feature.yaml`，不寫死。

    B5（G-TM2 項 4 / A-TM21(f)）—— 原實作只檢查鍵存在。其 `base_tc()`
    為全空字串，故一條所有欄位皆為空之 TC 會全綠通過。
    """
    out = []
    for key in auth["columns"]:
        # 寫回端填之欄位，生成時不要求：tc_id 由序號賦值（canon §10.3）、
        # author / tc_ref_id / functional_safety 由條文決定（A4 之推論）。
        if key in ("tc_ref_id", "author", "tc_id", "functional_safety"):
            continue
        # remarks 之必要性是**條件式**的：僅 A-TM13 兩片與 BLOCKED 列需填，
        # 其餘列本應為空（BLANK_BY_DECISION）。該條件由 lint_spec_gap（B3）
        # 管，不由本閘管 —— 列為無條件必填會使 20 片正常 leaf 全部誤報。
        if key == "remarks":
            continue
        if key not in tc:
            out.append(("required-fields", f"{where}: 缺欄位 `{key}`"))
        elif not str(tc.get(key) or "").strip():
            out.append(("required-fields", f"{where}: 欄位 `{key}` 為空"))
    return out


def lint_leaf_source(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """B2（G-TM1 項 2）—— leaf 文字來源隔離（R-TM24）。

    `req_id` 須為 `data/leaf_descriptions.txt` 之 22 筆之一。該檔為 037
    `Requirement Description` 欄之直接輸出，是 test_item 上半之唯一許可
    來源 —— R-TM24 之對策為**來源隔離**，非人工記得不要抄下放包之簡寫。
    """
    out = []
    leaf = str(tc.get("req_id", ""))
    if leaf not in auth["leaves"]:
        out.append(("leaf-source",
                    f"{where}: req_id `{leaf}` 不在 data/leaf_descriptions.txt "
                    f"之 {LEAF_COUNT} 筆 leaf 全集內"))
    # canon §4.3.1（R-TM48 使其生效）—— test_item 兩段式。
    # 本閘只管**結構**（下半括號之存在、上半長度），不管措辭 —— 措辭屬
    # TC 內容，仍受 R-TM10-A1 拘束。
    item = str(tc.get("test_item") or "")
    if item.strip():
        if not TEST_ITEM_TAIL_RE.search(item.strip()):
            out.append(("test-item-shape",
                        f"{where}: test_item 缺下半之 `(...)` 測試目的。"
                        "canon §4.3.1：缺括號下半 = FAIL，不得出貨"))
        head = TEST_ITEM_TAIL_RE.sub("", item.strip()).strip()
        n = len(head.split())
        if n > TEST_ITEM_TOKEN_MAX:
            out.append(("test-item-shape",
                        f"{where}: test_item 上半 {n} token，超過 canon "
                        f"§4.3.1 之上限 {TEST_ITEM_TOKEN_MAX}。須摘句"
                        "（以與括號下半直接相關之句為限），全文以 "
                        "specification_reference 指回，不得整段傾倒"))
    return out


def lint_test_set(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """C1 —— Test Set 值域閘門。

    原標 `TODO(R-TM10-A1)`「待本 feature 之 framework 定案」，**該標記
    已過時**：framework Part VII 之七組已由 R-TM17 簽核（2026-08-20）。
    """
    got = str(tc.get("test_set", ""))
    if got not in TEST_SETS:
        return [("test-set",
                 f"{where}: test_set `{got}` 不是 framework Part VII 之七組"
                 "（R-TM17 已簽）")]
    return []


def lint_priority_domain(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """C2 —— priority **值域**閘門（非分佈）。

    值域自母本 P 欄之 DV 讀取，非 TC 內容裁決，故可立即實作。
    **分佈**（各 P 級之比例）才是內容裁決，見檔末 TODO(內容裁決)。
    """
    got = str(tc.get("priority", ""))
    if got and got not in auth["priority"]:
        return [("priority-domain",
                 f"{where}: priority `{got}` 不在母本 P 欄 DV 之值域 "
                 f"{sorted(auth['priority'])} 內")]
    return []


def lint_spec_gap(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """B3（G-TM1 項 3）—— A-TM13 兩片之缺口須於 Remarks 宣告。

    `-005` 與 `-002` 各引用一筆 SYS-RA，其來源物件（6151328 / 6151331）
    於 CFTS015 SR26 全檔零命中。該兩筆無章節可寫，**不得以鄰近章節填充**
    （§8.4.1）。Remarks 為空即為把缺口藏起來。
    """
    leaf = str(tc.get("req_id", ""))
    if leaf not in SPEC_GAP_LEAVES:
        return []
    rem = str(tc.get("remarks") or "")
    if not rem.strip():
        return [("spec-gap",
                 f"{where}: {leaf} 為 A-TM13 之受影響 leaf，其 Remarks 為空。"
                 "canon §8.4.3 明訂缺件不得留空，須寫 "
                 "`PENDING: DR-5 CFTS015 缺件物件 …`（R-TM41 處置訂正）")]
    if not PENDING_RE.search(rem):
        return [("spec-gap",
                 f"{where}: {leaf} 之 Remarks 未含 `PENDING: DR-` 佔位。"
                 "該 leaf 有 SYS-RA 之來源物件不在 CFTS015 基線內，"
                 "缺口須以 canon §8.4.3 之佔位形式宣告，非任意措辭")]
    return []


def lint_boundary(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """B4（G-TM1 項 4）—— 五條 §8.2.1 界線之訊號歸屬（R-TM23 / R-TM25）。

    TC 全文若命中鄰片所擁有之訊號，即為跨界重複覆蓋。
    """
    leaf = str(tc.get("req_id", ""))
    rule = BOUNDARY_SIGNALS.get(leaf)
    if not rule:
        return []
    body = " ".join(str(tc.get(k) or "") for k in
                    ("test_item", "pre_conditions", "input_test_data",
                     "test_procedure", "expected_result"))
    out = []
    for sig in rule["not_ours"]:
        if sig in body:
            out.append(("boundary",
                        f"{where}: {leaf} 之內文命中 `{sig}`，該訊號屬鄰片。"
                        f"{rule['why']}（Part VII §8.2.1，R-TM23 / R-TM25）"))
    return out


def lint_no_tc_id(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """B8（G-TM2 項 3 訂正）—— TC JSON 不得攜帶 tc_id。

    canon §10.3 末句：`the generator handles assignment, the LLM does not
    emit tc_id`。本閘為生成端違反該條之偵測點；賦號由 write_back 依列
    位置為之。
    """
    if "tc_id" in tc:
        return [("no-tc-id",
                 f"{where}: TC JSON 含 `tc_id` 鍵。canon §10.3 明訂 "
                 "generator 賦號、LLM 不得產出；賦號由 write_back 依列位置為之")]
    return []


def lint_test_group(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """`test_group` 須逐字等於 `feature.yaml` 之值（R-TM8）。"""
    want = auth["test_group"]
    got = str(tc.get("test_group", ""))
    if got != want:
        return [("test-group", f"{where}: test_group `{got}` ≠ `{want}`")]
    return []


def lint_design_method(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """`design_method` 須為母本 `下拉選單` 之詞條之一（逐字）。"""
    got = str(tc.get("design_method", "")).strip()
    if got and got not in auth["design_methods"]:
        return [("design-method",
                 f"{where}: design_method `{got[:40]}` 不在母本下拉選單詞彙內")]
    return []


def lint_spec_reference(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """B7 —— spec_reference 三重閘門（R-TM40 / R-TM41 / canon §10.7(a)）。

    (i)   形式須為 `CFTS015-{7 位}`（canon §10.7(a)：CFTS 母文件 →
          `CFTS{nnn}-{ObjectID}`，ObjectID 為 Polarion 7 位號碼）
    (ii)  該 7 位須存在於 SYS2 第 5 欄之全集 —— 即真有此物件被本 feature
          之需求引用，非任意 7 位數
    (iii) 該 7 位須存在於 CFTS015 docx —— **此項擋掉 6151328 / 6151331**
          （R-TM41）。格式湊得出來不等於來源有此內容（§8.4.1）

    第 (iii) 項為現存版之 `lint_spec_reference` 所有，G-TM2 項 6 明列為
    「不得回退」；本次由「額外保護」升為「格式正確性之必要條件」。

    **排列**依 canon §10.7 之排列段：同一文件內多個 ObjectID 以 `, ` 續列
    且**文件前綴僅敘明一次**、**禁用 `;`**、升冪。
    """
    raw = str(tc.get("specification_reference", "") or "")
    out: list[tuple[str, str]] = []
    if not raw.strip():
        return [("spec-reference", f"{where}: specification_reference 為空")]
    if ";" in raw:
        out.append(("spec-reference",
                    f"{where}: 含 `;` —— canon §10.7 排列段明文禁用，"
                    "同一文件內多個 ObjectID 以 `, ` 續列"))
    # 一來源文件一行；同一行內前綴僅首個 token 帶
    for line in [l.strip() for l in raw.splitlines() if l.strip()]:
        toks = [x.strip() for x in line.split(",") if x.strip()]
        if not toks:
            continue
        m = SPEC_REF_RE.match(toks[0])
        if not m:
            out.append(("spec-reference",
                        f"{where}: 首 token `{toks[0]}` 不符 `CFTS015-<7 位>`"
                        "（canon §10.7(a)）"))
            continue
        ids = [m.group(1)]
        for tok in toks[1:]:
            if SPEC_REF_RE.match(tok):
                out.append(("spec-reference",
                            f"{where}: `{tok}` 重複帶前綴 —— canon §10.7 排列段"
                            "「文件前綴僅敘明一次」"))
                ids.append(tok.split("-", 1)[1])
            elif re.fullmatch(r"\d{7}", tok):
                ids.append(tok)
            else:
                out.append(("spec-reference",
                            f"{where}: 續列 token `{tok}` 非 7 位物件 id"))
        if ids != sorted(ids):
            out.append(("spec-reference",
                        f"{where}: 物件 id 未升冪 —— canon §10.7 排列段"))
        for oid in ids:
            if oid not in auth["sys2_items"]:
                out.append(("spec-reference",
                            f"{where}: 物件 `{oid}` 不在 SYS2 "
                            "`Source Requirement items` 之全集內"))
            if oid not in auth["spec_objects"]:
                out.append(("spec-reference",
                            f"{where}: 物件 `{oid}` 不存在於 CFTS015 docx。"
                            "格式湊得出來不等於來源有此內容（R-TM41 / §8.4.1）"))
    return out


def lint_d5_scope(auth: dict) -> list[tuple[str, str]]:
    """B1（G-TM1 項 1）—— D5 Scope 守衛，**具名失敗，不與 header drift 混列**。

    語意須明示：D5 現階段**本應為空**（其值為所依據 037 之文件識別，
    而 037 身分未定 —— A-TM02a）。故本閘之綠向為「D5 為空 → 報
    spec-scope-pending」，非「D5 有值才過」。

    此閘報的是**待決狀態**而非缺陷：它使「D5 空著」這件事每次 lint 都
    現形，不致因久未處理而被當成正常。
    """
    import openpyxl
    wb = openpyxl.load_workbook(auth["workbook"], read_only=True, data_only=True)
    ws = wb[auth["sheet"]]
    v = ws["D5"].value
    wb.close()
    s = str(v or "")
    if not s.strip():
        return [("d5-scope",
                 "D5（範圍 Scope）為**空**。canon §8.4.3（R-TM48 使其生效）"
                 "明訂欄位因來源缺失而無法填寫時須寫 `PENDING: DR-{n}`，"
                 "**不得留空、不得填 NA**。本欄應為 "
                 "`PENDING: DR-2 037 正式報告檔名`（R-TM9-A2 處置訂正）")]
    if PENDING_RE.search(s):
        return [("spec-scope-pending",
                 f"D5 為佔位 {s!r} —— 037 身分未定（A-TM02a），依 canon "
                 "§8.4.3 以 PENDING 佔位。此為待決狀態之提示，非缺陷；"
                 "DR 結案後須換為 037 檔名（去副檔名）")]
    if s.upper() == "NA":
        return [("d5-scope",
                 "D5 為 `NA` —— canon §8.4.3 明訂 NA 僅限「確認不適用」。"
                 "本欄為缺件而非不適用，須用 `PENDING: DR-2`")]
    return [("d5-scope",
             f"D5 已有值 {s!r} —— 若該值係本工作簿之依據 037 檔名"
             "（去副檔名），須先更新 A-TM02a 與 A-TM11 之狀態；"
             "不得以 feature 名或 spec 標題組值填入（R-TM9-A2）")]


def lint_step_er_count(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    """步驟數與 ER 行數相等。

    **此為結構性不變量，非措辭判準** —— 故不受 R-TM10-A1 拘束。
    """
    proc = _steps(tc.get("test_procedure"))
    er = _steps(tc.get("expected_result"))
    if proc and er and len(proc) != len(er):
        return [("step-er-count",
                 f"{where}: 步驟 {len(proc)} 條 vs ER {len(er)} 條")]
    return []


# TODO(R-TM10-A1): 步驟措辭之閘門（禁用動詞、步長上限、最終步須帶查核目標）
#   —— 其詞彙與門檻屬 TC 內容，須由本 feature 之條文決定，不得援引他 feature。
#   Privacy 之 `step-actions`（R33-5：一步一動作，判動詞數不判連接詞）
#   為其自身裁決之編碼，本 feature 未有對應條文前不實作。

# C1 —— Test Set 值域閘門已實作（lint_test_set）。原 TODO(R-TM10-A1)
#   「待本 feature 之 framework 定案」已過時：Part VII 七組經 R-TM17 簽核。

# C2 —— priority **值域**閘門已實作（lint_priority_domain），自母本 P 欄
#   DV 讀取，非 TC 內容裁決。
# TODO(內容裁決): priority **分佈**（各 P 級之比例）—— 屬 TC 內容裁決，
#   待本 feature 之條文決定。**與 TODO(R-TM10-A1) 區分**：後者管跨 feature
#   樣式參照，本項管本 feature 自身之內容決定，不會隨 R-TM10-A1 解除。

# TODO(R-TM10-A1): Input Test Data 填法之閘門 —— 待本 feature 之條文決定。


GATES = (
    lint_required_fields,
    lint_leaf_source,        # B2
    lint_test_set,           # C1
    lint_priority_domain,    # C2
    lint_spec_gap,           # B3
    lint_boundary,           # B4
    lint_no_tc_id,           # B8
    lint_test_group,
    lint_design_method,
    lint_spec_reference,
    lint_step_er_count,
)


def lint_tc(tc: dict, auth: dict, where: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for gate in GATES:
        out += gate(tc, auth, where)
    return out


def lint_file(path: Path, auth: dict) -> list[tuple[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    tcs = data.get("tcs", data if isinstance(data, list) else [])
    out: list[tuple[str, str]] = []
    for i, tc in enumerate(tcs, 1):
        out += lint_tc(tc, auth, f"{path.name}#{i}")
    return out


# ── 範圍向自驗（R-G9）───────────────────────────────────────
def base_tc(auth: dict) -> dict:
    """一條應全綠之最小 TC —— 其值全部取自權威，不寫死措辭。

    B5 之後，全空字串不再算合規，故各欄須有實質值。
    """
    leaf = sorted(auth["leaves"])[0]          # SWE-RA-TIME&DATE-001
    oid = sorted(auth["spec_objects"] & auth["sys2_items"])[0]
    tc = {k: "x" for k in auth["columns"]
          if k not in ("tc_id", "author", "tc_ref_id", "functional_safety")}
    tc["req_id"] = leaf
    tc["test_group"] = auth["test_group"]
    tc["test_set"] = "Manual Setting"
    tc["design_method"] = sorted(auth["design_methods"])[0]
    tc["specification_reference"] = f"CFTS015-{oid}"
    tc["priority"] = sorted(auth["priority"])[0]
    tc["test_procedure"] = "1. a\n2. b"
    tc["expected_result"] = "1. a\n2. b"
    tc["remarks"] = ""
    # canon §4.3.1 —— 上半 verbatim + 下半 `(...)` 測試目的
    tc["test_item"] = "The software shall set time (manual entry)"
    return tc


def self_test(auth: dict) -> int:
    """每閘一紅一綠。**綠向證明其不對合規者誤報，紅向證明其抓得到。**

    紅向一律以**刻意構造之壞輸入**觸發，不以「理論上會 raise」代替。
    構造時避免與他閘混淆（R-TM45 之同層版本）：例如 B5 之紅向只留一欄
    為空，不用全空 TC —— 後者會同時觸發多閘，看不出是哪一閘抓到的。
    """
    bad = 0
    green = base_tc(auth)
    v = lint_tc(green, auth, "GREEN")
    if v:
        bad += 1
        print(f"**FAIL** 綠向：合規之 TC 轉紅 → {v}")
    else:
        print("PASS 綠向：合規之 TC 未轉紅")

    gap_leaf = sorted(SPEC_GAP_LEAVES)[0]
    oid_ok = green["specification_reference"].split("-")[1]
    reds = [
        ("required-fields  (B5 空值，只留一欄空)",
         {**green, "pre_conditions": "   "}),
        ("leaf-source      (B2 不在 22 筆內)",
         {**green, "req_id": "SWE-RA-TIME&DATE-099"}),
        ("test-set         (C1 非七組之一)",
         {**green, "test_set": "Time"}),
        ("priority-domain  (C2 值域外)",
         {**green, "priority": "P9"}),
        ("spec-gap         (B3 A-TM13 leaf 而 Remarks 空)",
         {**green, "req_id": gap_leaf, "remarks": ""}),
        ("boundary         (B4 011 命中 008 之訊號)",
         {**green, "req_id": "SWE-RA-TIME&DATE-011",
          "expected_result": "HU transmits $DateTmHour$ within 1000 ms"}),
        ("no-tc-id         (B8 JSON 攜帶 tc_id)",
         {**green, "tc_id": "NR1L-TimeAndDate-001"}),
        ("test-group       (R-TM8：feature 名不是 Test Group)",
         {**green, "test_group": "Time Management"}),
        ("design-method    (不在母本下拉選單內)",
         {**green, "design_method": "不存在之方法 (Nope)"}),
        ("spec-reference i (B7 形式不符 CFTS015-<7位>)",
         {**green, "specification_reference": "4813905"}),
        ("spec-reference ii(B7 7 位不在 SYS2 全集)",
         {**green, "specification_reference": "CFTS015-9999999"}),
        ("spec-reference iii(B7 R-TM41：不在 CFTS015 docx)",
         {**green, "specification_reference": "CFTS015-6151328"}),
        ("spec-reference   (B7 canon §10.7 禁用 ;)",
         {**green, "specification_reference": f"CFTS015-{oid_ok}; CFTS015-{oid_ok}"}),
        ("spec-reference   (B7 前綴重複敘明)",
         {**green, "specification_reference": f"CFTS015-{oid_ok}, CFTS015-{oid_ok}"}),
        ("step-er-count    (步驟數 vs ER 行數)",
         {**green, "expected_result": "1. a"}),
        ("spec-gap         (L2：Remarks 有值但非 PENDING 佔位)",
         {**green, "req_id": gap_leaf, "remarks": "缺口見 A-TM13"}),
        ("test-item-shape  (L3：缺下半括號)",
         {**green, "test_item": "The software shall set time"}),
        ("test-item-shape  (L3：上半 51 token 未摘句)",
         {**green, "test_item": " ".join(["word"] * 51) + " (purpose)"}),
    ]
    for name, tc in reds:
        gate = name.split()[0]
        v = lint_tc(tc, auth, f"RED[{gate}]")
        hit = any(g == gate for g, _ in v)
        bad += not hit
        msg = [m for g, m in v if g == gate]
        print(f"{'PASS' if hit else '**FAIL**'} 紅向 {name}: "
              f"{msg[0].split(': ', 1)[-1][:78] if msg else '未叫 —— 閘失效'}")

    # 綠向 2：A-TM13 leaf 且 Remarks 為合規佔位 → 不應報 spec-gap
    ok_gap = {**green, "req_id": gap_leaf,
              "remarks": "PENDING: DR-5 CFTS015 缺件物件 6151328"}
    v = [g for g, _ in lint_tc(ok_gap, auth, "GREEN2") if g == "spec-gap"]
    bad += bool(v)
    print(f"{'PASS' if not v else '**FAIL**'} 綠向 2 (A-TM13 leaf 帶 "
          f"PENDING 佔位): {'未誤報 spec-gap' if not v else v}")

    # B1 —— D5 守衛（工作簿層，非逐 TC）
    d5 = lint_d5_scope(auth)
    # 現況 D5 為空 —— canon §8.4.3 下「空」已非合規狀態，應報 d5-scope
    hit = any(g == "d5-scope" for g, _ in d5)
    bad += not hit
    print(f"{'PASS' if hit else '**FAIL**'} B1 D5 守衛: "
          f"{d5[0][1][:78] if d5 else '未叫'}")

    total = len(reds) + 3
    print(f"\n自驗：{total - bad} / {total}")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature-dir", required=True)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    fd = Path(a.feature_dir)
    try:
        auth = load_authorities(fd)
    except LintError as e:
        print(f"LintError: {e}", file=sys.stderr)
        return 2
    if a.self_test:
        return self_test(auth)
    findings: list[tuple[str, str]] = []
    # B1 為**工作簿層**檢查，與是否已生成 TC 無關 —— 故置於 early return
    # 之前。原置於 TC 迴圈之後，`generated/` 為空時提前 return 即被跳過，
    # 而 B1 之設計意圖正是「使 D5 之狀態每次 lint 都現形」（L1）。
    findings += lint_d5_scope(auth)
    gen = sorted((fd / "generated").glob("*.json"))
    if not gen:
        print("generated/ 無 json —— 尚未生成 TC（工作簿層閘門仍已執行）")
        for g, m in findings:
            print(f"[{g}] {m}")
        return 1 if any(g != "spec-scope-pending" for g, _ in findings) else 0
    for p in gen:
        findings += lint_file(p, auth)
    for g, m in findings:
        print(f"[{g}] {m}")
    print(f"\n檔 {len(gen)}；發現 {len(findings)} 項")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
