"""ASPICE SWE.6 Review engine.

Implements the v2.2 Review pipeline described in
`docs/runtime/ASPICE_SWE6_AI_Review.md`:

    parse → group by Req ID → Tier 1 (§6.x) → Tier 2 (§7.x) → Tier 3 (§8.x)
    → apply interactions (mutual exclusions, suppressions, tier skips)
    → enforce severity ceilings → emit per-§9 schema

20 of 31 rules execute via pure regex / keyword detection (`requires_llm:
false` in `backend/rules/review_rules.yaml`). 11 require an LLM for
semantic comparison (Req spec句 alignment, element coverage, design-method
shape, etc.) and are routed through `review_prompt_builder.py`.

Public entry: `review_workbook(workbook_path, output_dir, ...)`.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from parser import parse_tc_xlsx
from review_prompt_builder import (
    LLM_RULE_HINTS,
    build_review_system_prompt,
    build_review_user_prompt,
)


# ---------------------------------------------------------------------------
# Constants & rule loading
# ---------------------------------------------------------------------------

_RULES_PATH = Path(__file__).resolve().parent / "rules" / "review_rules.yaml"

SEVERITY_CEILINGS = {1: "Critical", 2: "Critical", 3: "Major"}
SEVERITY_RANK = {"Info": 0, "Minor": 1, "Major": 2, "Critical": 3}

_RULE_TITLES = {
    # populated from yaml at import; fallback titles below cover the test path
    "§6.1": "Missing supported/negative pair",
    "§6.2": "Missing boundary axis",
    "§6.3": "Missing enumeration coverage",
    "§6.4": "Sibling axis ambiguous",
    "§6.5": "Spec句 inconsistent across siblings",
    "§6.6": "Tier 1 not executable (no spec句)",
    "§6.7": "Multi-Req-ID in single TC",
    "§7.1": "Test Item outcome not in Req spec句",
    "§7.2": "ER misses Req outcome elements",
    "§7.3": "Pre-Cond duplicates Req trigger",
    "§7.4": "Fabricated numeric value vs Req",
    "§7.5": "Final Step launches tool, no result read",
    "§7.6": "Reality gap vs spec/domain",
    "§8.1.1": "Test Item length out of range",
    "§8.1.2": "Modal/hedge wording in Test Item",
    "§8.1.3": "Multi-language collision",
    "§8.1.4": "Sibling-distinction token missing",
    "§8.1.5": "No spec sentence nor traceable Req",
    "§8.2.1": "Action verb in Pre-Cond",
    "§8.2.2": "Verification verb in Pre-Cond",
    "§8.2.3": "System default stated as Pre-Cond",
    "§8.2.4": "Feature-under-test stated as ready",
    "§8.2.5": "Pre-Cond bound to specific instance",
    "§8.3.1": "Forbidden verb / guessing tone",
    "§8.3.2": "Step lacking executable content",
    "§8.3.3": "Single-step procedure",
    "§8.3.4": "Step numbering anomaly",
    "§8.3.5": "Final Step has no check target",
    "§8.3.6": "Fabricated value (Tier 2 fallback)",
    "§8.4.1": "Vague outcome wording",
    "§8.4.2": "Step↔ER count mismatch",
    "§8.4.3": "ER numbering anomaly",
    "§8.5.1": "Priority outside P0–P3",
    "§8.5.2": "Design Method missing",
    "§8.5.3": "Design Method inconsistent with Procedure",
}


def _load_rules_yaml() -> dict:
    """Read the rules table; tolerate missing file (engine still works with
    its hard-coded mapping above)."""
    if not _RULES_PATH.is_file():
        return {}
    try:
        return yaml.safe_load(_RULES_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return {}


RULES_YAML = _load_rules_yaml()


class ReviewEngineError(Exception):
    """Raised for invariant violations (severity ceiling, schema)."""


# ---------------------------------------------------------------------------
# Data shapes
# ---------------------------------------------------------------------------


@dataclass
class TCRecord:
    """Normalized TC the engine reasons about."""
    row_num: int
    tc_id: str
    req_id_raw: str             # raw cell value, may carry newlines
    req_ids: list[str]          # split & cleaned
    test_item: str
    pre_conditions: str
    input_test_data: str
    test_procedure: str
    expected_result: str
    spec_reference: str
    priority: str
    design_method: str
    req_spec_sentence: str | None = None  # resolved during Tier 1
    tier1_skipped: bool = False           # set when group has no spec句


@dataclass
class ReqGroup:
    """One Req-ID group of TCs (§3 grouping unit for Tier 1)."""
    req_id: str
    tcs: list[TCRecord] = field(default_factory=list)
    spec_sentence: str | None = None
    tier1_skipped: bool = False
    has_64: bool = False  # if §6.4 fired, suppress §8.1.4 on this group's TCs


# ---------------------------------------------------------------------------
# Multi-Req-ID & spec句 helpers
# ---------------------------------------------------------------------------


_REQ_ID_SPLIT = re.compile(r"[\r\n]+")
_BRACKET_TAG = re.compile(r"\[([A-Z][A-Z0-9-]+)\]")
_SPEC_SENTENCE = re.compile(
    r"[^.\n]*\b(shall|must|should)\b[^.\n]*\.?",
    re.IGNORECASE,
)
# Requirement-side normative sentence. Requirements legitimately use "will" and
# declarative phrasing, not only shall/must/should — so Tier 1 can anchor on the
# SWE1 requirement even when the TC carries no spec句. Broader than the
# conservative TC-side _SPEC_SENTENCE on purpose.
_REQ_NORM_SENTENCE = re.compile(
    r"[^.\n]*\b(shall|must|should|will)\b[^.\n]*\.?",
    re.IGNORECASE,
)
# A pure cross-document pointer ("Refer to CFTS012 …") carries no behaviour of
# its own and does NOT anchor Tier 1.
_REF_ONLY = re.compile(r"^\s*refer to\b", re.IGNORECASE)


def requirement_anchor(req: dict | None) -> str | None:
    """Resolve a Tier-1 anchor句 from a SWE1 requirement (NOT the TC).

    A requirement anchors Tier 1 whenever it carries substantive normative text —
    shall/must/should OR will OR a declarative requirement statement — so a TC is
    never required to embed a spec句. Pure cross-reference stubs do not anchor."""
    if not req:
        return None
    title = str(req.get("title") or "").strip()
    desc = str(req.get("desc") or "").strip()
    if not desc and not title:
        return None
    m = _REQ_NORM_SENTENCE.search(f"{title}. {desc}")
    if m:
        return m.group(0).strip()
    # Declarative requirement (no modal verb): anchor on the desc unless it is
    # only a cross-document pointer with no behaviour of its own.
    if desc and not _REF_ONLY.match(desc):
        return desc[:300]
    return None


def _split_req_ids(raw: str) -> list[str]:
    """Multi-Req-ID per §6.7: split on newline, strip empties."""
    if not raw:
        return []
    parts = [p.strip() for p in _REQ_ID_SPLIT.split(str(raw)) if p.strip()]
    return parts


def extract_spec_sentence(test_item: str, req_id: str | None = None) -> str | None:
    """Extract the first English shall/must/should sentence from Test Item.

    For multi-Req-ID TCs, if `[REQ-ID]` bracket tags delimit segments AND
    `req_id` matches one of them, restrict the search to that segment so
    each Req group anchors on its own spec句 (§6.7 group_participation).
    """
    if not test_item:
        return None
    text = str(test_item)

    # Multi-Req-ID with bracket tags: pick the segment for our req_id
    if req_id and _BRACKET_TAG.search(text):
        # split into [TAG] blocks
        segments: dict[str, str] = {}
        cursor = 0
        last_tag: str | None = None
        for m in _BRACKET_TAG.finditer(text):
            if last_tag is not None:
                segments[last_tag] = text[cursor:m.start()].strip()
            last_tag = m.group(1)
            cursor = m.end()
        if last_tag is not None:
            segments[last_tag] = text[cursor:].strip()
        if req_id in segments:
            text = segments[req_id]

    # 為了 multi-line Test Item 整體掃描，先把段落黏成單行查找會錯失邊界，
    # 因此逐行比對保留第一個有 shall/must/should 的句子。
    for line in text.splitlines():
        m = _SPEC_SENTENCE.search(line)
        if m:
            sentence = m.group(0).strip()
            return sentence
    return None


# ---------------------------------------------------------------------------
# Detectors — Tier 3 (§8.x) regex-only rules
# ---------------------------------------------------------------------------

# §8.3.1 forbidden verbs as MAIN verb
_VERBS_8_3_1_EN = re.compile(
    r"\b(observe|see if|check whether|confirm whether|verify|watch|monitor|inspect)\b",
    re.IGNORECASE,
)
_VERBS_8_3_1_ZH = re.compile(r"(觀察|查看|檢視|看看|確認是否|留意|是否)")
# `verify` allowed in purpose clause `... to verify ...`
_VERIFY_PURPOSE = re.compile(r"\bto\s+verify\b", re.IGNORECASE)

# §8.4.1 vague outcome
_VAGUE_8_4_1_EN = re.compile(
    r"\b(normal|as expected|works correctly|properly)\b", re.IGNORECASE
)
_VAGUE_8_4_1_ZH = re.compile(r"(正常|如預期|運作正常|正確顯示|成功(?!地?連線))")
# "successfully" mirrors the ZH 成功(?!連線) carve-out: it is only vague when it
# does NOT modify a concrete observable action (connected/paired/recognized/…).
# "The BTSA device is connected successfully" is observable, not vague.
_SUCCESS_WORD = re.compile(r"\bsuccessfully\b", re.IGNORECASE)
_SUCCESS_CONCRETE = re.compile(
    r"\b(connect(?:ed|s)?|pair(?:ed|s)?|recogni[sz]e[ds]?|mount(?:ed|s)?|"
    r"load(?:ed|s)?|detect(?:ed|s)?|sav(?:e|ed|es)|play(?:ed|s)?|"
    r"display(?:ed|s)?|switch(?:ed|es)?|launch(?:ed|es)?)\b",
    re.IGNORECASE,
)

# §8.1.2 modal/hedge in Test Item
_MODAL_8_1_2_EN = re.compile(
    r"\b(should|properly|successfully|within reasonable time)\b", re.IGNORECASE
)
_MODAL_8_1_2_ZH = re.compile(r"(應該|正常地|成功地|合理時間內|如預期)")

# §8.2.1 action verbs in Pre-Cond
_ACTION_8_2_1_EN = re.compile(
    r"\b(Insert|Press|Connect|Open|Tap|Launch|Send|Configure|Run|Execute|Click)\b"
)
_ACTION_8_2_1_ZH = re.compile(r"(插入|按下|點擊|啟動|傳送|設定|執行|依次|先後|依序)")

# §8.2.2 verification verbs in Pre-Cond
_VERIFY_8_2_2_EN = re.compile(r"\b(Check|Verify|Confirm|Observe|Read)\b")
_VERIFY_8_2_2_ZH = re.compile(r"(檢查|確認|查看|觀察|讀取|是否)")

# §8.2.3 system default
_SYSTEM_DEFAULT_8_2_3 = re.compile(
    r"(HU is powered on|System has booted|device is charged|車機已開機|系統已啟動|系統已開機)",
    re.IGNORECASE,
)

# §8.2.5 specific instance
_INSTANCE_8_2_5 = re.compile(r"(pixel|iPhone|Galaxy|Pixel)\s*\d+", re.IGNORECASE)

# §8.5.1 priority allowed values
_ALLOWED_PRIORITY = {"P0", "P1", "P2", "P3"}

# §7.4 / §8.3.6 fabricated numeric value heuristic
_NUMERIC_VALUE = re.compile(
    r"(\d+)\s*(秒|s|sec|分鐘|min|次|times|小時|hours|ms|分)\b",
    re.IGNORECASE,
)
_DOMAIN_CONST_VALUES = {"0000", "200"}  # BT PIN, HTTP 200 OK

# §7.5 final-step tool launch
_TOOL_VERBS = re.compile(
    r"(執行|啟動|開始|點選.*?開始|點擊|Run|Execute|Launch|Start|Click.*?start)",
    re.IGNORECASE,
)
_TOOL_NAMES = re.compile(
    r"(PCTS-[A-Z0-9]+|Facets-[A-Z0-9]+|ATS\b)", re.IGNORECASE
)
_VERIFICATION_FOLLOWUP = re.compile(
    r"(確認|對照|結果符合|通過|讀取|查看.*報告|Confirm|pass|read.*report)",
    re.IGNORECASE,
)

# §8.3.5 final-step check verbs. The last step must verify an observable
# outcome — but real test cases write "Check the …", "Verify that …",
# "Validate …", not only the narrow "Check that". Accept the full check-verb
# family (English + Chinese) as a leading/whole word; a bare action step
# (e.g. "Select the USB source") still has no check verb and is flagged.
_FINAL_CHECK_VERB = re.compile(
    r"\b(Check|Verify|Confirm|Validate|Ensure|Observe|Read|Record|Compare)\b"
    r"|(檢查|確認|驗證|查看|觀察|讀取|對照|比對|記錄|是否|符合)",
    re.IGNORECASE,
)

# §8.3.4 step numbering anomalies
_STEP_LINE = re.compile(r"^\s*(\d+)[.\s]", re.MULTILINE)

# §8.4.3 ER numbering anomaly: `1.1.` `2.2.` style
_ER_DOUBLE_NUMBER = re.compile(r"^(\d+)\.\1\.", re.MULTILINE)


def _split_steps(text: str) -> list[str]:
    """Split numbered procedure / ER text into per-step strings."""
    if not text:
        return []
    lines = [line for line in str(text).splitlines() if line.strip()]
    steps: list[str] = []
    for line in lines:
        if re.match(r"^\s*\d+[.\s]", line):
            steps.append(line.strip())
        elif steps:
            steps[-1] = steps[-1] + " " + line.strip()
    return steps


def _detect_8_3_1(tc: TCRecord) -> list[dict]:
    findings = []
    steps = _split_steps(tc.test_procedure)
    for idx, step in enumerate(steps, start=1):
        # strip leading number
        body = re.sub(r"^\s*\d+[.\s]+", "", step)
        # Skip if `verify` appears only inside a purpose clause
        en_match = _VERBS_8_3_1_EN.search(body)
        zh_match = _VERBS_8_3_1_ZH.search(body)
        if en_match and en_match.group(0).lower() == "verify" and _VERIFY_PURPOSE.search(body):
            en_match = None
        if not (en_match or zh_match):
            continue
        evidence = step
        findings.append({
            "tier": 3,
            "field": "test_procedure",
            "step_index": idx,
            "rule_ref": "§8.3.1",
            "severity": "Major",
            "issue": "測試程序步驟使用了猜測語氣或被禁止的動詞，將判斷推給測試人員",
            "evidence": evidence,
            "original": evidence,
            "revised": "",  # reviewer-side rewrite; engine does not auto-rewrite Tier 3
            "suggestion_note": "改用 Check that / Confirm that / Read / Record / Compare + 明確可觀察目標",
        })
    return findings


def _detect_8_4_1(tc: TCRecord) -> list[dict]:
    er = tc.expected_result
    if not er:
        return []
    vague = bool(_VAGUE_8_4_1_EN.search(er) or _VAGUE_8_4_1_ZH.search(er))
    # bare "successfully" is vague only when no concrete observable verb is present
    if not vague and _SUCCESS_WORD.search(er) and not _SUCCESS_CONCRETE.search(er):
        vague = True
    if not vague:
        return []
    return [{
        "tier": 3,
        "field": "expected_result",
        "rule_ref": "§8.4.1",
        "severity": "Major",
        "issue": "Expected Result 出現模糊用語（例如「正常」「如預期」），無法做客觀判定",
        "evidence": tc.expected_result.strip().splitlines()[0][:200],
        "original": tc.expected_result,
        "revised": "",
        "suggestion_note": "改寫為可觀察可量測的具體結果（UI 元素 / log / signal / 狀態 / 計數）",
    }]


def _detect_8_1_1(tc: TCRecord) -> list[dict]:
    text = (tc.test_item or "").strip()
    if not text:
        return []
    # 取第一個 line（避免多語版本同欄位混算字數）
    first = text.splitlines()[0].strip()
    # House convention: this team's Test Item carries the full normative
    # requirement句 (Tier 1 §6.6 anchors on it). A shall/must/should sentence is
    # the requirement itself, not a concise title — the length limit does not
    # apply. Short title-style Test Items (no spec句) are still checked.
    if _SPEC_SENTENCE.search(first):
        return []
    # heuristic: ASCII-dominant → word count; else char count
    ascii_chars = sum(1 for c in first if ord(c) < 128)
    if ascii_chars > len(first) / 2:
        word_count = len(first.split())
        if word_count > 14:
            return [_make_8_1_1_finding(tc, first, f"{word_count} words")]
    else:
        char_count = sum(1 for c in first if c.strip())
        if char_count > 35:
            return [_make_8_1_1_finding(tc, first, f"{char_count} chars")]
    return []


def _make_8_1_1_finding(tc: TCRecord, evidence: str, measure: str) -> dict:
    return {
        "tier": 3,
        "field": "test_item",
        "rule_ref": "§8.1.1",
        "severity": "Major",
        "issue": f"Test Item 過長（{measure}），超出 14 words / 35 chars 上限",
        "evidence": evidence[:200],
        "original": tc.test_item,
        "revised": "",
        "suggestion_note": "壓縮為命名 trigger 或 scenario 的最短句型",
    }


def _detect_8_1_2(tc: TCRecord) -> list[dict]:
    text = tc.test_item or ""
    if not (_MODAL_8_1_2_EN.search(text) or _MODAL_8_1_2_ZH.search(text)):
        return []
    return [{
        "tier": 3,
        "field": "test_item",
        "rule_ref": "§8.1.2",
        "severity": "Major",
        "issue": "Test Item 含 modal/hedge 用語（should / properly / 應該 / 如預期 等）",
        "evidence": text.strip().splitlines()[0][:200],
        "original": tc.test_item,
        "revised": "",
        "suggestion_note": "改為具體可觀察的 outcome 描述",
    }]


def _detect_8_2_1(tc: TCRecord) -> list[dict]:
    text = tc.pre_conditions or ""
    if not (_ACTION_8_2_1_EN.search(text) or _ACTION_8_2_1_ZH.search(text)):
        return []
    return [{
        "tier": 3,
        "field": "pre_conditions",
        "rule_ref": "§8.2.1",
        "severity": "Major",
        "issue": "Pre-Condition 含動作動詞（Insert / Press / 插入 / 按下 等），動作應放 Test Procedure",
        "evidence": text.strip().splitlines()[0][:200],
        "original": tc.pre_conditions,
        "revised": "",
        "suggestion_note": "把動作搬到 Test Procedure step 1；Pre-Cond 只描述狀態（例：藍牙已開啟）",
    }]


def _detect_8_2_2(tc: TCRecord) -> list[dict]:
    text = tc.pre_conditions or ""
    if not (_VERIFY_8_2_2_EN.search(text) or _VERIFY_8_2_2_ZH.search(text)):
        return []
    return [{
        "tier": 3,
        "field": "pre_conditions",
        "rule_ref": "§8.2.2",
        "severity": "Major",
        "issue": "Pre-Condition 含驗證動詞（Check / Verify / 檢查 / 確認 等）；Pre-Cond 應為靜態事實",
        "evidence": text.strip().splitlines()[0][:200],
        "original": tc.pre_conditions,
        "revised": "",
        "suggestion_note": "移除驗證子句；若需證明前置狀態，改放 Setup step 並搭配對應 ER",
    }]


def _detect_8_2_3(tc: TCRecord) -> list[dict]:
    if not tc.pre_conditions or not _SYSTEM_DEFAULT_8_2_3.search(tc.pre_conditions):
        return []
    return [{
        "tier": 3,
        "field": "pre_conditions",
        "rule_ref": "§8.2.3",
        "severity": "Minor",
        "issue": "Pre-Cond 只陳述系統預設狀態（如「車機已開機」），對 TC 區分無貢獻",
        "evidence": tc.pre_conditions.strip().splitlines()[0][:200],
        "original": tc.pre_conditions,
        "revised": "",
        "suggestion_note": "刪除；Pre-Cond 只列各 TC 之間會變動的條件",
    }]


def _detect_8_2_5(tc: TCRecord) -> list[dict]:
    if not tc.pre_conditions or not _INSTANCE_8_2_5.search(tc.pre_conditions):
        return []
    return [{
        "tier": 3,
        "field": "pre_conditions",
        "rule_ref": "§8.2.5",
        "severity": "Minor",
        "issue": "Pre-Cond 綁特定機型（pixel / iPhone 14 等），應抽象為能力描述",
        "evidence": tc.pre_conditions.strip().splitlines()[0][:200],
        "original": tc.pre_conditions,
        "revised": "",
        "suggestion_note": "改寫為能力（例：手機支援 Android Auto / phone supports CarPlay）",
    }]


def _detect_8_3_3(tc: TCRecord) -> list[dict]:
    steps = _split_steps(tc.test_procedure)
    if len(steps) == 1:
        return [{
            "tier": 3,
            "field": "test_procedure",
            "rule_ref": "§8.3.3",
            "severity": "Major",
            "issue": "Test Procedure 只有 1 個步驟，無法呈現可重現的測試流程",
            "evidence": steps[0][:200],
            "original": tc.test_procedure,
            "revised": "",
            "suggestion_note": "拆分為多個可逐步觀察的步驟（setup → 操作 → 驗證）",
        }]
    return []


def _detect_8_3_4(tc: TCRecord) -> list[dict]:
    if not tc.test_procedure:
        return []
    nums = [int(m.group(1)) for m in _STEP_LINE.finditer(tc.test_procedure)]
    if len(nums) <= 1:
        return []
    duplicates = {n for n in nums if nums.count(n) > 1}
    if not duplicates:
        return []
    return [{
        "tier": 3,
        "field": "test_procedure",
        "rule_ref": "§8.3.4",
        "severity": "Minor",
        "issue": f"Test Procedure 步驟編號出現重複（{sorted(duplicates)}）",
        "evidence": tc.test_procedure.strip().splitlines()[0][:200],
        "original": tc.test_procedure,
        "revised": "",
        "suggestion_note": "重新連續編號 1, 2, 3, ...",
    }]


def _detect_8_3_5(tc: TCRecord) -> list[dict]:
    steps = _split_steps(tc.test_procedure)
    if not steps:
        return []
    last = steps[-1]
    body = re.sub(r"^\s*\d+[.\s]+", "", last)
    has_check = bool(_FINAL_CHECK_VERB.search(body))
    if has_check:
        return []
    # If the last step is a tool-launch, §7.5 (Tier 2) handles it instead
    if _TOOL_VERBS.search(body) and _TOOL_NAMES.search(body):
        return []
    return [{
        "tier": 3,
        "field": "test_procedure",
        "step_index": len(steps),
        "rule_ref": "§8.3.5",
        # Spec §8 lists this as Critical, but §4 Severity Rubric caps Tier 3 at Major
        # and §10 self-check enforces the ceiling. The ceiling wins.
        "severity": "Major",
        "issue": "Final Step 沒有檢查目標，僅為動作而無 Check/Confirm 子句",
        "evidence": last[:200],
        "original": tc.test_procedure,
        "revised": "",
        "suggestion_note": "改寫為 `<動作>，並確認 <可觀察結果>` 的形式",
    }]


def _detect_8_4_3(tc: TCRecord) -> list[dict]:
    if not tc.expected_result or not _ER_DOUBLE_NUMBER.search(tc.expected_result):
        return []
    return [{
        "tier": 3,
        "field": "expected_result",
        "rule_ref": "§8.4.3",
        "severity": "Minor",
        "issue": "ER 編號異常（出現 1.1. / 2.2. 雙重編號）",
        "evidence": tc.expected_result.strip().splitlines()[0][:200],
        "original": tc.expected_result,
        "revised": "",
        "suggestion_note": "重新連續編號，與 Test Procedure 1:1 對齊",
    }]


def _detect_8_5_1(tc: TCRecord) -> list[dict]:
    pri = (tc.priority or "").strip()
    if pri in _ALLOWED_PRIORITY:
        return []
    return [{
        "tier": 3,
        "field": "priority",
        "rule_ref": "§8.5.1",
        "severity": "Major",
        "issue": f"Priority `{pri or '(空)'}` 不在 P0/P1/P2/P3 之內",
        "evidence": pri or "(empty)",
        "original": pri,
        "revised": "",
        "suggestion_note": "依 docs/runtime/TEST_CASE_PRIORITY.md 重新判定 P0–P3",
    }]


def _detect_8_5_2(tc: TCRecord) -> list[dict]:
    if (tc.design_method or "").strip():
        return []
    return [{
        "tier": 3,
        "field": "design_method",
        "rule_ref": "§8.5.2",
        "severity": "Major",
        "issue": "缺少測試用例設計方法（Design Method）",
        "evidence": "(empty)",
        "original": "",
        "revised": "",
        "suggestion_note": "依實際 procedure 流程判定 §15 first-match（Negative / Fault Injection / State Transition / Decision Table / EP / BVA / Combinatorial / Scenario / Functional）",
    }]


def _detect_7_4_or_8_3_6(tc: TCRecord, group: ReqGroup) -> list[dict]:
    """Combined fabricated-value detector implementing the §7.4 ⊕ §8.3.6
    mutual exclusion. Fires §8.3.6 (Tier 3 Major) only when the Req group
    is `tier1_skipped`; otherwise fires §7.4 (Tier 2 Critical), but only
    when the value is absent from both Req spec句 AND Specification Reference."""
    findings: list[dict] = []
    spec_ref = (tc.spec_reference or "").strip()
    spec_句 = group.spec_sentence or ""
    for field_name, source in (("test_procedure", tc.test_procedure),
                                ("expected_result", tc.expected_result)):
        if not source:
            continue
        for m in _NUMERIC_VALUE.finditer(source):
            value = m.group(1)
            unit = m.group(2)
            if value in _DOMAIN_CONST_VALUES:
                continue
            in_spec_句 = bool(spec_句) and value in spec_句
            in_spec_ref = bool(spec_ref) and value in spec_ref
            if in_spec_句 or in_spec_ref:
                continue

            evidence = m.group(0)
            # locate step_index for Procedure findings (best-effort)
            step_index = _find_step_index(source, m.start()) if field_name == "test_procedure" else None

            if group.tier1_skipped:
                # §8.3.6 Tier 3 Major fallback
                findings.append({
                    "tier": 3,
                    "field": field_name,
                    "step_index": step_index,
                    "rule_ref": "§8.3.6",
                    "severity": "Major",
                    "issue": f"出現具體數值 `{value}{unit}`，但 Specification Reference 未引用，且該 Req group 無 spec句 可比對",
                    "evidence": evidence,
                    "original": source,
                    "revised": "",
                    "suggestion_note": "於 Specification Reference 加註出處，或改寫為 `<value defined in spec>`，或移除非 Req-driven 的限制",
                })
            else:
                # §7.4 Tier 2 Critical
                findings.append({
                    "tier": 2,
                    "field": field_name,
                    "step_index": step_index,
                    "rule_ref": "§7.4",
                    "severity": "Critical",
                    "issue": f"具體數值 `{value}{unit}` 不在 Req spec句 也不在 Specification Reference",
                    "evidence": evidence,
                    "evidence_req_spec": spec_句 or "",
                    "original": source,
                    "revised": "",
                    "suggestion_note": "把數值改為 `<value defined in spec>`，或補 Specification Reference 引用，或移除非 Req 驅動的限制",
                })
    return findings


def _find_step_index(source: str, char_offset: int) -> int | None:
    """Approximate the 1-indexed step number containing char_offset."""
    cur = 0
    last_step: int | None = None
    for line in source.splitlines(keepends=True):
        m = re.match(r"^\s*(\d+)[.\s]", line)
        if m:
            last_step = int(m.group(1))
        if cur + len(line) > char_offset:
            return last_step
        cur += len(line)
    return last_step


def _detect_7_5(tc: TCRecord, group: ReqGroup) -> list[dict]:
    """§7.5 — Final Step launches a tool but no subsequent step reads result."""
    if group.tier1_skipped:
        return []  # Tier 2 skipped for tier1_skipped groups
    steps = _split_steps(tc.test_procedure)
    if not steps:
        return []
    last = steps[-1]
    body = re.sub(r"^\s*\d+[.\s]+", "", last)
    if not (_TOOL_VERBS.search(body) and _TOOL_NAMES.search(body)):
        return []
    # If a verification follow-up appears anywhere AFTER the tool launch in the same field,
    # consider it covered. By definition `last` is final, so any follow-up means a later step.
    # Here last is genuinely the last step — so by construction no follow-up. Fire.
    return [{
        "tier": 2,
        "field": "test_procedure",
        "step_index": len(steps),
        "rule_ref": "§7.5",
        "severity": "Critical",
        "issue": "Final Step 啟動測試工具但未讀取結果，驗證被默默推給工具 log 讀者",
        "evidence": last[:200],
        "evidence_req_spec": group.spec_sentence or "",
        "original": tc.test_procedure,
        "revised": "",
        "suggestion_note": f"追加一個驗證步驟：{len(steps)+1}. 確認 <工具> 結果報告為 <通過條件>",
    }]


# ---------------------------------------------------------------------------
# Tier 1 detectors
# ---------------------------------------------------------------------------


def _detect_6_5(group: ReqGroup) -> list[dict]:
    """§6.5 — multiple TCs in group carry materially different spec句."""
    sentences: dict[str, list[str]] = defaultdict(list)
    for tc in group.tcs:
        s = extract_spec_sentence(tc.test_item, group.req_id)
        if s:
            sentences[s.lower().strip()].append(tc.tc_id)
    if len(sentences) <= 1:
        return []
    canonical = max(sentences.keys(), key=len)
    return [{
        "req_id": group.req_id,
        "tier": 1,
        "rule_ref": "§6.5",
        "severity": "Critical",
        "scope_tcs": sorted({tcid for ids in sentences.values() for tcid in ids}),
        "issue": "同 Req group 內多個 TC 引用不同版本的 spec句，Traceability 已斷裂",
        "evidence_req_spec": canonical,
        "suggestion_note": "確認 canonical 版本並讓所有 TC 對齊；不要自動覆寫，請 reviewer 對應 Polarion / SWRA 確認",
    }]


def _detect_6_6(group: ReqGroup) -> list[dict]:
    """§6.6 — no TC in group carries an English spec句 with shall/must/should."""
    if group.spec_sentence:
        return []
    return [{
        "req_id": group.req_id,
        "tier": 1,
        "rule_ref": "§6.6",
        "severity": "Major",
        "scope_tcs": sorted(tc.tc_id for tc in group.tcs),
        "issue": "本 Req group 沒有任何 TC 帶英文 shall/must/should spec句，Tier 1 無法錨定，Tier 2 全部跳過",
        "evidence_req_spec": "",
        "suggestion_note": "從 Polarion / SWRA 上游取得 canonical Req spec 並貼回至少一個 TC 的 Test Item；Tier 3 §8.3.6 fallback 將自動啟用",
    }]


def _detect_6_7(tc: TCRecord) -> list[dict]:
    """§6.7 — multi-Req-ID single TC; recorded once in per_req_findings."""
    if len(tc.req_ids) < 2:
        return []
    joined = ", ".join(tc.req_ids)
    return [{
        "req_id": joined,
        "tier": 1,
        "rule_ref": "§6.7",
        "severity": "Major",
        "scope_tcs": [tc.tc_id],
        "issue": "單一 TC 同時掛載多個 Requirement ID，違反「One TC = one verification objective」",
        "evidence_req_spec": "",
        "suggestion_note": "優先拆成獨立 TC（每 Req 一個）；若因測試工具耦合無法拆分（如 PCTS-MT1 同時量測敏感度與失真），請於 Test Item 用複合目標明列兩個 Req ID，並讓 ER 為每個 Req 提供獨立可觀察結果",
    }]


def _detect_6_4(group: ReqGroup) -> list[dict]:
    """§6.4 — sibling axis ambiguous: 2+ TCs read identically in Test Item
    AND no scenario tag distinguishes them."""
    if len(group.tcs) < 2:
        return []
    norms: dict[str, list[str]] = defaultdict(list)
    for tc in group.tcs:
        first = (tc.test_item or "").strip().splitlines()
        norm = re.sub(r"\s+", " ", " ".join(first)).strip().lower()
        if norm:
            norms[norm].append(tc.tc_id)
    duplicates = [tcs for tcs in norms.values() if len(tcs) >= 2]
    if not duplicates:
        return []
    affected = sorted({tcid for cluster in duplicates for tcid in cluster})
    return [{
        "req_id": group.req_id,
        "tier": 1,
        "rule_ref": "§6.4",
        "severity": "Major",
        "scope_tcs": affected,
        "issue": "群組內存在 2+ TC 的 Test Item 完全一致，缺少可區分 sibling 的 scenario tag",
        "evidence_req_spec": group.spec_sentence or "",
        "suggestion_note": "在 Test Item 加上 scenario tag（例：Cold boot / .mp4 / =limit）讓 sibling 一眼可辨",
    }]


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def _normalize_row(row: dict) -> TCRecord:
    raw_req = str(row.get("req_id") or "")
    return TCRecord(
        row_num=int(row.get("row_num", 0)),
        tc_id=str(row.get("tc_id") or "").strip(),
        req_id_raw=raw_req,
        req_ids=_split_req_ids(raw_req),
        test_item=str(row.get("test_item") or ""),
        pre_conditions=str(row.get("pre_conditions") or ""),
        input_test_data=str(row.get("input_test_data") or ""),
        test_procedure=str(row.get("test_procedure") or ""),
        expected_result=str(row.get("expected_result") or ""),
        spec_reference=str(row.get("spec_reference") or ""),
        priority=str(row.get("priority") or ""),
        design_method=str(row.get("design_method") or ""),
    )


def _build_groups(tcs: list[TCRecord],
                  swe1_reqs: list[dict] | None = None) -> dict[str, ReqGroup]:
    """Group TCs by Req ID. Multi-Req-ID TCs register under each constituent.

    Tier 1 anchors on a normative requirement句. It is resolved (in order):
    1. from a TC's Test Item (shall/must/should), then
    2. from the matched SWE1 requirement itself (shall/must/should/will/declarative)
       — so a TC is NOT required to embed a spec句.
    §6.6 (tier1_skipped) only fires when neither source yields an anchor."""
    from req_tracer import _ids_agree
    groups: dict[str, ReqGroup] = {}
    for tc in tcs:
        ids = tc.req_ids or [""]  # blank Req ID still gets a group
        for rid in ids:
            grp = groups.setdefault(rid, ReqGroup(req_id=rid))
            grp.tcs.append(tc)
    # Resolve spec sentence per group; mark tier1_skipped when none found
    for rid, grp in groups.items():
        for tc in grp.tcs:
            s = extract_spec_sentence(tc.test_item, rid if rid else None)
            if s:
                grp.spec_sentence = s
                break
        # Fallback: anchor on the SWE1 requirement (the TC need not carry a句).
        if grp.spec_sentence is None and swe1_reqs and rid:
            for req in swe1_reqs:
                if _ids_agree(str(req.get("id", "")), rid):
                    anchor = requirement_anchor(req)
                    if anchor:
                        grp.spec_sentence = anchor
                        break
        if grp.spec_sentence is None:
            grp.tier1_skipped = True
            for tc in grp.tcs:
                tc.tier1_skipped = True
                tc.req_spec_sentence = None
        else:
            for tc in grp.tcs:
                tc.req_spec_sentence = grp.spec_sentence
    return groups


def _enforce_severity_ceiling(tier: int, rule_ref: str, severity: str) -> str:
    """Return the clamped severity per §10.3 ceiling. Logs the clamp via
    a comment string but does not raise; only invented severities raise."""
    if severity not in SEVERITY_RANK:
        raise ReviewEngineError(
            f"Unknown severity `{severity}` for {rule_ref}"
        )
    ceiling = SEVERITY_CEILINGS[tier]
    if SEVERITY_RANK[severity] > SEVERITY_RANK[ceiling]:
        # Per spec §10 self-check #3, ceiling violation is a contract bug.
        # We surface it loudly rather than silently clamp.
        raise ReviewEngineError(
            f"Severity ceiling violated: {rule_ref} tier {tier} emitted "
            f"`{severity}` (max {ceiling}). Fix the detector."
        )
    return severity


def _overall_verdict(findings: list[dict]) -> str:
    if not findings:
        return "pass"
    sev = max((SEVERITY_RANK[f["severity"]] for f in findings), default=0)
    if sev >= SEVERITY_RANK["Critical"]:
        return "fail"
    if sev >= SEVERITY_RANK["Minor"]:
        return "pass_with_issues"
    return "pass"


# Tier 3 detectors that take just a TC
_TIER3_TC_DETECTORS = [
    _detect_8_1_1, _detect_8_1_2,
    _detect_8_2_1, _detect_8_2_2, _detect_8_2_3, _detect_8_2_5,
    _detect_8_3_1, _detect_8_3_3, _detect_8_3_4, _detect_8_3_5,
    _detect_8_4_1, _detect_8_4_3,
    _detect_8_5_1, _detect_8_5_2,
]


def _run_regex_pipeline(
    tcs: list[TCRecord],
    groups: dict[str, ReqGroup],
) -> tuple[list[dict], list[dict]]:
    per_req: list[dict] = []
    per_tc: dict[str, dict] = {}

    # Tier 1
    for tc in tcs:
        for f in _detect_6_7(tc):
            per_req.append(f)
    seen_groups = set()
    for rid, grp in groups.items():
        if rid in seen_groups:
            continue
        seen_groups.add(rid)
        for f in _detect_6_6(grp):
            per_req.append(f)
        for f in _detect_6_5(grp):
            per_req.append(f)
        for f in _detect_6_4(grp):
            per_req.append(f)
            grp.has_64 = True

    # Per-TC: aggregate findings (use TC ID + row as dedupe key — multi-Req-ID
    # TCs would otherwise emit Tier 3 twice).
    suppressed_8_1_4_tc_ids = set()
    for grp in groups.values():
        if grp.has_64:
            for tc in grp.tcs:
                suppressed_8_1_4_tc_ids.add(tc.tc_id)

    # Dedupe by row_num (always unique) — multi-Req-ID TCs would otherwise
    # be processed once per constituent group via the outer iteration.
    # tc_id alone is unsafe: workbooks pre-ID-generation share an empty tc_id
    # across all rows and would collapse to a single entry.
    seen_rows: set[int] = set()
    for tc in tcs:
        if tc.row_num in seen_rows:
            continue
        seen_rows.add(tc.row_num)

        # Pick the primary group for this TC for spec-comparison rules
        primary_rid = tc.req_ids[0] if tc.req_ids else ""
        group = groups.get(primary_rid) or ReqGroup(req_id=primary_rid, tcs=[tc])

        tc_findings: list[dict] = []

        # Tier 2 — only if group not tier1_skipped
        if not group.tier1_skipped:
            tc_findings.extend(_detect_7_5(tc, group))

        # Tier 2/3 fabricated-value pair (mutual exclusion handled inside)
        tc_findings.extend(_detect_7_4_or_8_3_6(tc, group))

        # Tier 3
        for det in _TIER3_TC_DETECTORS:
            tc_findings.extend(det(tc))

        # Apply §6.4 → §8.1.4 suppression (we don't currently emit §8.1.4
        # via regex, but skip it defensively if some future detector does.)
        if tc.tc_id in suppressed_8_1_4_tc_ids:
            tc_findings = [f for f in tc_findings if f.get("rule_ref") != "§8.1.4"]

        # Enforce severity ceilings (raises on violation)
        for f in tc_findings:
            _enforce_severity_ceiling(f["tier"], f["rule_ref"], f["severity"])
            # Tier 2 must include evidence_req_spec; Tier 3 must omit
            if f["tier"] == 2:
                f.setdefault("evidence_req_spec", group.spec_sentence or "")
            else:
                f.pop("evidence_req_spec", None)

        per_tc[str(tc.row_num)] = {
            "tc_id": tc.tc_id,
            "row": tc.row_num,
            "overall_verdict": _overall_verdict(tc_findings),
            "findings": tc_findings,
        }

    # Tier 1 ceilings
    for f in per_req:
        _enforce_severity_ceiling(1, f["rule_ref"], f["severity"])

    return per_req, list(per_tc.values())


# ---------------------------------------------------------------------------
# LLM integration (optional; off by default)
# ---------------------------------------------------------------------------


def _build_payload_tcs(tcs: list[TCRecord],
                       content_map: dict[int, dict] | None = None) -> list[dict]:
    """The per-TC payload the semantic layer reasons over (API or interactive)."""
    content_map = content_map or {}
    return [
        {
            "row_num": tc.row_num,
            "tc_id": tc.tc_id,
            "req_id": tc.req_ids[0] if tc.req_ids else "",
            "test_item": tc.test_item,
            "pre_conditions": tc.pre_conditions,
            "input_test_data": tc.input_test_data,
            "test_procedure": tc.test_procedure,
            "expected_result": tc.expected_result,
            "spec_reference": tc.spec_reference,
            "priority": tc.priority,
            "design_method": tc.design_method,
            "req_spec_sentence": tc.req_spec_sentence,
            "tier1_skipped": tc.tier1_skipped,
            # Requirement matched by CONTENT (the written req_id may be wrong).
            "content_req": content_map.get(tc.row_num),
        }
        for tc in tcs
    ]


def _build_review_batches(payload_tcs: list[dict], domain_block: str | None,
                          batch_size: int = 5) -> list[dict]:
    """Slice the payload into batches, each carrying its rendered user prompt and
    the rows it covers. Shared by the API path and the interactive bridge."""
    rule_ids = list(LLM_RULE_HINTS.keys())
    batches = []
    for idx, i in enumerate(range(0, len(payload_tcs), batch_size)):
        batch = payload_tcs[i:i + batch_size]
        batches.append({
            "batch_index": idx,
            "rows": [t["row_num"] for t in batch],
            "user_prompt": build_review_user_prompt(
                batch, rule_ids, domain_block=domain_block),
        })
    return batches


def _accumulate_llm_findings(answers: list[dict | None],
                             tcs: list[TCRecord]) -> tuple[list[dict], list[dict]]:
    """Merge a list of per-batch LLM answer dicts into (per_req, per_tc).

    Answer source is irrelevant — an OpenAI/Anthropic API response or a JSON
    object Claude produced interactively both land here identically."""
    per_req: list[dict] = []
    per_tc_acc: dict[int, list[dict]] = defaultdict(list)
    tc_id_by_row: dict[int, str] = {tc.row_num: tc.tc_id for tc in tcs}
    for data in answers:
        if not data:
            continue
        for f in data.get("per_req_findings", []) or []:
            per_req.append(f)
        for entry in data.get("per_tc_findings", []) or []:
            row = _coerce_row(entry.get("row"))
            if row is None:
                row = _row_for_tc(tcs, str(entry.get("tc_id") or ""))
            if row is None:
                continue
            per_tc_acc[row].extend(entry.get("findings", []) or [])
    per_tc = [
        {"tc_id": tc_id_by_row.get(row, ""), "row": row, "overall_verdict": "pass",
         "findings": findings}
        for row, findings in per_tc_acc.items()
    ]
    return per_req, per_tc


def _run_llm_pipeline(
    tcs: list[TCRecord],
    groups: dict[str, ReqGroup],
    model: str,
    batch_size: int = 5,
    domain_block: str | None = None,
    content_map: dict[int, dict] | None = None,
    llm_max_tokens: int = 16000,
) -> tuple[list[dict], list[dict], dict]:
    """API path: call the LLM for each batch. Imports the provider lazily so
    dry-run never depends on credentials. `domain_block` (Stage 1 Domain Pack)
    is injected into every batch as ground truth."""
    from generator import _chat, GenerationError  # local import

    payload_tcs = _build_payload_tcs(tcs, content_map)
    batches = _build_review_batches(payload_tcs, domain_block, batch_size)
    system = build_review_system_prompt()

    answers: list[dict | None] = []
    n_failed = 0
    for b in batches:
        try:
            # Reasoning models (gpt-5) spend output tokens on hidden reasoning
            # before the JSON; a small cap truncates them to empty. Give headroom.
            resp = _chat(system=system, user=b["user_prompt"], model=model,
                         json_mode=True, max_tokens=llm_max_tokens)
            answers.append(json.loads(resp.text))
        except (GenerationError, AttributeError, IndexError, json.JSONDecodeError):
            n_failed += 1
            answers.append(None)

    per_req, per_tc = _accumulate_llm_findings(answers, tcs)
    stats = {"llm_batches": len(batches), "llm_failed": n_failed}
    return per_req, per_tc, stats


def _coerce_row(value: object) -> int | None:
    try:
        row = int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return row if row > 0 else None


def _row_for_tc(tcs: list[TCRecord], tc_id: str) -> int | None:
    if not tc_id:
        return None
    for tc in tcs:
        if tc.tc_id == tc_id:
            return tc.row_num
    return None


# ---------------------------------------------------------------------------
# Output assembly
# ---------------------------------------------------------------------------


def _merge_per_tc(
    regex_entries: list[dict],
    llm_entries: list[dict],
) -> list[dict]:
    # Key by row_num (always unique) rather than tc_id, since pre-ID-generation
    # workbooks have empty tc_id on every row.
    by_id: dict[int, dict] = {e["row"]: e for e in regex_entries}
    for e in llm_entries:
        row = e.get("row")
        if row in by_id:
            by_id[row]["findings"].extend(e["findings"])
        else:
            by_id[row] = e
    # Recompute overall_verdict
    for entry in by_id.values():
        entry["overall_verdict"] = _overall_verdict(entry["findings"])
    return sorted(by_id.values(), key=lambda x: x["row"])


def _build_batch_summary(
    per_req: list[dict],
    per_tc: list[dict],
    total_tcs: int,
    total_groups: int,
) -> dict:
    verdict_counts = {"pass": 0, "pass_with_issues": 0, "fail": 0}
    for e in per_tc:
        verdict_counts[e["overall_verdict"]] += 1

    def _top_rules(entries: Iterable[dict], key: str = "rule_ref") -> list[dict]:
        counter: dict[str, int] = defaultdict(int)
        for e in entries:
            counter[e[key]] += 1
        return [
            {"rule_ref": rid, "count": cnt, "title": _RULE_TITLES.get(rid, "")}
            for rid, cnt in sorted(counter.items(), key=lambda x: -x[1])
        ][:10]

    tier2_findings = [f for entry in per_tc for f in entry["findings"] if f["tier"] == 2]
    tier3_findings = [f for entry in per_tc for f in entry["findings"] if f["tier"] == 3]

    skipped_groups = sum(1 for f in per_req if f["rule_ref"] == "§6.6")

    reasoning = (
        f"Tier 1：共 {total_groups} 個 Req group，其中 "
        f"{sum(1 for f in per_req if f['severity'] == 'Critical')} 個出現 Critical 拆解問題，"
        f"{skipped_groups} 個無英文 spec句（§6.6）。"
        f" Tier 2：{sum(1 for f in tier2_findings if f['severity'] == 'Critical')} 個 Critical 對齊問題，"
        "多集中於 Final Step 工具未讀結果或數值未引用 spec。"
        f" Tier 3：{len(tier3_findings)} 筆寫作層違規（多為禁用動詞、模糊用語、Design Method 缺漏）。"
        " 修正順序建議：先補完 Tier 1 拆解 → 重審 → 再依 Tier 2 / Tier 3 finding 個別調整。"
    )

    return {
        "verdict_counts": verdict_counts,
        "tier_summary": {
            "tier1": {
                "req_groups_total": total_groups,
                "req_groups_with_critical": sum(
                    1 for f in per_req if f["severity"] == "Critical"
                ),
                "req_groups_skipped": skipped_groups,
                "top_rules": _top_rules(per_req),
            },
            "tier2": {
                "tcs_with_critical": sum(
                    1 for entry in per_tc
                    if any(f["tier"] == 2 and f["severity"] == "Critical"
                           for f in entry["findings"])
                ),
                "top_rules": _top_rules(tier2_findings),
            },
            "tier3": {
                "tcs_with_findings": sum(
                    1 for entry in per_tc
                    if any(f["tier"] == 3 for f in entry["findings"])
                ),
                "top_rules": _top_rules(tier3_findings),
            },
        },
        "reasoning": reasoning,
    }


def _render_markdown_report(report: dict) -> str:
    meta = report["batch_meta"]
    summary = report["batch_summary"]
    lines = [
        f"# ASPICE SWE.6 Review Findings — {meta['source_file']}",
        "",
        f"- Sheet: `{meta['sheet']}`",
        f"- Total TCs: {meta['total_tcs']}",
        f"- Total Req groups: {meta['total_req_groups']}",
        f"- Reviewed at: {meta['reviewed_at']}",
        "",
        "## Batch Summary",
        "",
        f"- Pass: {summary['verdict_counts']['pass']}",
        f"- Pass with issues: {summary['verdict_counts']['pass_with_issues']}",
        f"- Fail: {summary['verdict_counts']['fail']}",
        "",
        f"> {summary['reasoning']}",
        "",
        "## Tier 1 — Per Requirement Findings",
    ]
    if not report["per_req_findings"]:
        lines.append("\n_(無 Tier 1 finding)_")
    for f in report["per_req_findings"]:
        lines.append(
            f"\n### [{f['rule_ref']}] {f['req_id']} — {f['severity']}\n"
            f"- Issue: {f['issue']}\n"
            f"- Scope TCs: {', '.join(f.get('scope_tcs', []))}\n"
            f"- Suggestion: {f.get('suggestion_note', '')}"
        )
    lines.append("\n## Tier 2 + Tier 3 — Per TC Findings")
    if not report["per_tc_findings"]:
        lines.append("\n_(無 per-TC finding)_")
    for entry in report["per_tc_findings"]:
        lines.append(f"\n### Row {entry['row']} · {entry['tc_id']} — verdict: `{entry['overall_verdict']}`")
        for f in entry["findings"]:
            ref = f["rule_ref"]
            sev = f["severity"]
            lines.append(f"- **[{ref}] {sev}** ({f.get('field','')}): {f['issue']}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Public entrypoint
# ---------------------------------------------------------------------------


def _build_content_map(tcs: list[TCRecord], swe1_reqs_path: str) -> dict[int, dict]:
    """Map each TC's row -> the SWE1 requirement matched by CONTENT (not id)."""
    from req_tracer import load_swe1_reqs, match_tc, _req_tokens
    reqs = load_swe1_reqs(swe1_reqs_path)
    req_tokens = [_req_tokens(r) for r in reqs]
    out: dict[int, dict] = {}
    for tc in tcs:
        best, score = match_tc(
            f"{tc.test_item} {tc.expected_result}", reqs, req_tokens)
        if best and score > 0:
            out[tc.row_num] = {
                "req_id": best.get("id"), "title": best.get("title"),
                "desc": best.get("desc"), "score": round(score, 3),
            }
    return out


def review_workbook(
    workbook_path: str,
    output_dir: str | None = None,
    model: str = "gpt-5",
    dry_run: bool = False,
    domain_pack_path: str | None = None,
    swe1_reqs_path: str | None = None,
) -> dict:
    """End-to-end review pipeline. Returns the findings dict; when
    `output_dir` is supplied, also writes findings.json and
    findings_report.md. `domain_pack_path` (Stage 1) grounds the semantic
    rules so the reviewer audits against domain truth, not just one Req句."""
    parsed = parse_tc_xlsx(workbook_path)
    tcs = [_normalize_row(row) for row in parsed["rows"]]
    swe1_reqs = None
    if swe1_reqs_path:
        from req_tracer import load_swe1_reqs
        swe1_reqs = load_swe1_reqs(swe1_reqs_path)
    groups = _build_groups(tcs, swe1_reqs)

    per_req, per_tc = _run_regex_pipeline(tcs, groups)

    llm_stats = None
    if not dry_run:
        domain_block = None
        if domain_pack_path:
            from domain_pack import load_domain_pack, to_prompt_block
            domain_block = to_prompt_block(load_domain_pack(domain_pack_path))
        content_map = _build_content_map(tcs, swe1_reqs_path) if swe1_reqs_path else None
        llm_per_req, llm_per_tc, llm_stats = _run_llm_pipeline(
            tcs, groups, model=model, domain_block=domain_block,
            content_map=content_map)
        per_req.extend(llm_per_req)
        per_tc = _merge_per_tc(per_tc, llm_per_tc)

    return _finalize_report(workbook_path, tcs, groups, per_req, per_tc,
                            llm_stats, output_dir)


def _resolve_report_sheet(workbook_path) -> str | None:
    """回報 batch_meta 用：實際被讀的 TC 分頁名，解不出則 None（不猜）。"""
    from openpyxl import load_workbook
    from openpyxl.utils.exceptions import InvalidFileException
    from parser import resolve_tc_sheet
    try:
        wb = load_workbook(workbook_path, read_only=True)
    except (OSError, InvalidFileException, ValueError):
        return None
    try:
        return resolve_tc_sheet(wb)
    except KeyError:
        return None
    finally:
        wb.close()


def _finalize_report(workbook_path, tcs, groups, per_req, per_tc,
                     llm_stats, output_dir):
    """Assemble the report dict from merged findings and optionally write it.
    Shared by the API path (`review_workbook`) and the interactive bridge."""
    summary = _build_batch_summary(per_req, per_tc, total_tcs=len(tcs),
                                   total_groups=len(groups))
    report = {
        "batch_meta": {
            "source_file": Path(workbook_path).name,
            # 原為硬編字面值 —— 對帶中文副標之 121/145 本會回報一個它沒讀的分頁名
            # （R-G48(b)，GC-03 §二-5-1）。改為實際解得者。
            "sheet": _resolve_report_sheet(workbook_path),
            "total_tcs": len(tcs),
            "total_req_groups": len(groups),
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
            "llm_stats": llm_stats,
        },
        "per_req_findings": per_req,
        "per_tc_findings": per_tc,
        "batch_summary": summary,
    }
    if output_dir:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "findings.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        (out / "findings_report.md").write_text(
            _render_markdown_report(report), encoding="utf-8")
    return report


# ---------------------------------------------------------------------------
# Interactive bridge — run the semantic layer on the Claude subscription ($0)
# instead of a billed API call. Python exports context bundles; Claude fills
# each batch's answer in-session; Python assembles the same report.
# ---------------------------------------------------------------------------

REVIEW_BUNDLE_SCHEMA = "review-bundle/v1"


def export_review_bundle(
    workbook_path: str,
    domain_pack_path: str | None = None,
    swe1_reqs_path: str | None = None,
    batch_size: int = 5,
) -> dict:
    """Produce a self-contained bundle for the interactive (subscription) path.

    Runs all deterministic work (parse / groups / regex / content-trace) and
    renders the per-batch semantic prompts WITHOUT calling any model. Claude
    fills each `batches[i]['answer']` with the §9-schema JSON, then
    `assemble_review` merges them into the final report — zero API cost."""
    parsed = parse_tc_xlsx(workbook_path)
    tcs = [_normalize_row(row) for row in parsed["rows"]]
    swe1_reqs = None
    if swe1_reqs_path:
        from req_tracer import load_swe1_reqs
        swe1_reqs = load_swe1_reqs(swe1_reqs_path)
    groups = _build_groups(tcs, swe1_reqs)
    regex_per_req, regex_per_tc = _run_regex_pipeline(tcs, groups)

    domain_block = None
    if domain_pack_path:
        from domain_pack import load_domain_pack, to_prompt_block
        domain_block = to_prompt_block(load_domain_pack(domain_pack_path))
    content_map = _build_content_map(tcs, swe1_reqs_path) if swe1_reqs_path else None

    payload_tcs = _build_payload_tcs(tcs, content_map)
    batches = _build_review_batches(payload_tcs, domain_block, batch_size)
    for b in batches:
        b["answer"] = None  # Claude fills this in-session

    return {
        "schema": REVIEW_BUNDLE_SCHEMA,
        "workbook_path": str(workbook_path),
        "source_file": Path(workbook_path).name,
        "total_tcs": len(tcs),
        "total_req_groups": len(groups),
        "system_prompt": build_review_system_prompt(),
        "answer_format": (
            'Per batch, return JSON: {"per_req_findings":[...],'
            '"per_tc_findings":[{"row":<int>,"tc_id":"...","findings":[...]}]} '
            "following the §9 schema in the system prompt."
        ),
        "batches": batches,
        "regex_findings": {"per_req": regex_per_req, "per_tc": regex_per_tc},
    }


def assemble_review(bundle: dict, output_dir: str | None = None) -> dict:
    """Merge a bundle whose `batches[i]['answer']` Claude has filled into the
    final report — identical shape to `review_workbook`'s output."""
    if bundle.get("schema") != REVIEW_BUNDLE_SCHEMA:
        raise ReviewEngineError(f"unexpected bundle schema: {bundle.get('schema')}")
    workbook_path = bundle["workbook_path"]
    parsed = parse_tc_xlsx(workbook_path)
    tcs = [_normalize_row(row) for row in parsed["rows"]]
    groups = _build_groups(tcs)

    answers = [b.get("answer") for b in bundle["batches"]]
    llm_per_req, llm_per_tc = _accumulate_llm_findings(answers, tcs)

    per_req = list(bundle["regex_findings"]["per_req"]) + llm_per_req
    per_tc = _merge_per_tc(bundle["regex_findings"]["per_tc"], llm_per_tc)
    llm_stats = {
        "llm_batches": len(answers),
        "llm_failed": sum(1 for a in answers if not a),
        "mode": "interactive",
    }
    return _finalize_report(workbook_path, tcs, groups, per_req, per_tc,
                            llm_stats, output_dir)
