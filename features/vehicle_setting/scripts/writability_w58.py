"""W-58 —— 全量可寫性掃描（39 包 §2）。

對 237 個 Functional leaf 之來源條文，一次掃出全部阻塞因子。

`blocker_class` 四類：
  B1 未具名之外部交叉參照（`as defined by`／`refer to`／`follow the`／`per the`
     ＋ 未帶文件名或章節號）
  B2 規格值於 LID 與 DBC 皆無對應（以 R-VS39 正規化鍵比對；含裸名 token）
  B3 PROXI／參數於 LID 三處皆無命中
  B4 其他（逐條具名）
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from dr_conflict import guard          # R-VS44：輸出階段之未結 DR 交叉檢查

FEAT = Path(__file__).resolve().parents[1]

# ── token 之三形態（R-VS36）──────────────────────────────────────────
# 以「其後緊接比較運算子與方括號值」為操作型定義 —— 該形態同時涵蓋
# `$X$ = [v]` 與裸名 `X = [v]`，故不需分別掃描。
TOKEN_CMP = re.compile(
    r"(\$?[A-Za-z][A-Za-z0-9_]{2,}\$?)\s*(?:=|&lt;&gt;|<>|&gt;|&lt;)\s*(\[[^\]]{0,90}\])")
# 描述式（R-VS36(3)）
TOKEN_DESC = re.compile(
    r"(?:PROXI parameter|signal|LID|parameter)\s+(\$?[A-Za-z][A-Za-z0-9_]{2,}\$?)")

# ── B1：未具名之外部交叉參照 ────────────────────────────────────────
XREF = re.compile(r"\b(as defined by|as defined in|refer to|refer the|follow the|"
                  r"per the|as specified by|according to)\b", re.I)
# 帶名者：CFTS 號、章節號、`{7 位數}`、或帶引號／大寫文件名
NAMED = re.compile(r"(CFTS\s*\d{3}|\{\d{7}\}|\bPU\d+|\d+\.\d+(?:\.\d+)+|"
                   r"[A-Z][A-Za-z]*_[A-Za-z_]*(?:Document|Spec|List))")

STOP = {"THEN", "IF", "AND", "OR", "The", "the", "HU", "HMI", "When", "when",
        "For", "for", "This", "shall", "will", "state", "value", "signal"}

# 識別碼形態：含底線、或全大寫 ≥3、或 CamelCase（≥2 個大寫）。
# **不以停用字表為主判準** —— 停用字表無法窮舉，形態判準才可（R-VS34 之教訓）。
IDENT = re.compile(r"^(?:\w*_\w+|[A-Z]{3,}|(?:[A-Z][a-z0-9]*){2,})$")


def is_ident(tok: str) -> bool:
    return bool(IDENT.match(tok)) and tok not in STOP


def norm(v: str) -> str:
    """R-VS39 之正規化鍵（不含 typo 前綴修正 —— 此處只比對存在性）。"""
    return re.sub(r"\s+", " ", v).strip().casefold()


def clause_tokens(text: str) -> dict[str, set[str]]:
    """回傳 {token(去 `$`): {方括號值…}}。裸名與 `$X$` 一併收。"""
    out: dict[str, set[str]] = {}
    for tok, val in TOKEN_CMP.findall(text):
        bare = tok.strip("$")
        if not is_ident(bare):
            continue
        out.setdefault(bare, set()).add(val.strip("[]").strip())
    for tok in TOKEN_DESC.findall(text):
        bare = tok.strip("$")
        if is_ident(bare):
            out.setdefault(bare, set())
    return out


def bus_domain() -> dict[str, set[str]]:
    """token → LID ＋ DBC 之值域（正規化鍵）。以 `spec_variables.tsv` 為底。"""
    dom: dict[str, set[str]] = {}
    with (FEAT / "data/spec_variables.tsv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            bare = r["token"].strip("$")
            vals: set[str] = set()
            for col in ("lid_values", "dbc"):
                vals |= {norm(v) for v in (r.get(col) or "").split("|") if v.strip()}
            for m in re.finditer(r"(\d+)\s*=\s*([^0-9][^=]*?)(?=\s+\d+\s*=|$)",
                                 r.get("lid_format") or ""):
                vals.add(norm(m.group(2)))
            dom[bare] = vals
    return dom


RAW_PREFIX = re.compile(r"^[0-9A-Fa-f]h\s*:\s*")
# §8.7.5(d)：內部訊號（無 DBC 對應者保留來源名）**不構成阻塞**
INTERNAL = re.compile(r"\b(internal signal|\.Req\b|\.Info\b|\.GUI\b)", re.I)


def value_matched(val: str, domain: set[str]) -> bool:
    """一個規格值是否在匯流排值域內。

    比對採三式取聯集：整串正規化鍵／以 `/` 切分後之各段／去 `Nh:` 前綴後之串。
    **`Nh:` 之原始碼值本身即為對應之依據**（19 輪 `[4h:Ignition run]` 之例）。
    """
    cands = {norm(val), norm(RAW_PREFIX.sub("", val))}
    cands |= {norm(p) for p in re.split(r"[/]{1,2}", val)}
    if RAW_PREFIX.match(val):
        return True                       # 來源自載原始碼值，可直接定位
    return bool(cands & domain)


def scan_leaf(text: str, domain: dict[str, set[str]]) -> list[tuple[str, str]]:
    """回傳該條文之阻塞因子 [(class, detail), …]；空表示可寫。"""
    out: list[tuple[str, str]] = []
    if XREF.search(text) and not NAMED.search(text):
        m = XREF.search(text)
        out.append(("B1", f"未具名之交叉參照：`{text[max(0, m.start()-30):m.end()+50].strip()}`"))
    for tok, vals in clause_tokens(text).items():
        if tok not in domain:
            if INTERNAL.search(text):
                continue                  # §8.7.5(d)：內部訊號不阻塞
            if vals:
                out.append(("B3", f"`{tok}` 於 LID／DBC／值域資料皆無記載"))
            continue
        bad = []
        for v in vals:
            if not v or value_matched(v, domain[tok]):
                continue
            # R-VS44：落在未結 DR 提問範圍內者，不得因任何判準而被解掉
            verdict, note = guard(tok, v, "blocked")
            bad.append(f"{v}{f' [{note}]' if note else ''}")
        if bad:
            out.append(("B2", f"`{tok}` 之值無匯流排對應：{'；'.join(sorted(bad)[:3])}"))
    return out
