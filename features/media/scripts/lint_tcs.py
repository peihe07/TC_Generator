#!/usr/bin/env python3
"""Step 3 hard gate — lint generated TCs before workbook write-back.

Implements the RUNBOOK.md "Step 3 — Lint" reject list. Every rule maps to a
section of docs/runtime/ASPICE_SWE6_AI_Instruction.md; the section is named in each
finding so a reviewer can jump straight to the authority.

The linted record is the WORKBOOK-facing shape (the one `exemplars.json` and
the Step 4 column mapping use), not the raw generation contract:

    req_id, test_group, test_set, test_item, pre_conditions, input_test_data,
    test_procedure, expected_result, specification_reference, priority,
    design_method

Usage:
    python lint_tcs.py generated/                    # lint every *.json
    python lint_tcs.py generated/SWE1-MEDIA-PLA-063.json
    python lint_tcs.py generated/ --data data --json-report lint_report.json

Exit code 0 = clean, 1 = at least one TC failed, 2 = bad invocation.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

# Marker-based, not parent-count based — see the 2026-08-11 features/ move.
REPO = next(p for p in Path(__file__).resolve().parents
            if (p / "pyproject.toml").is_file())
sys.path.insert(0, str(REPO / "backend"))

from validator import VALID_DESIGN_METHODS, VALID_PRIORITIES  # noqa: E402


REQUIRED_KEYS = [
    "req_id",
    "test_group",
    "test_set",
    "test_item",
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
    "specification_reference",
    "priority",
    "design_method",
]

# 這幾個欄位允許 "NA"（§6.5 的空值約定），其餘必須有實質內容。
NA_ALLOWED_KEYS = {"input_test_data"}

EXPECTED_TEST_GROUP = "MediaHMI"

# 需要逐行檢查「行尾不得有句點」的欄位（PC / ITD / Procedure / ER）。
LINE_TERMINATOR_KEYS = [
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
]

# §5.1 forbidden MAIN verbs — 只在步驟開頭（主要動詞位置）才算違規，
# 句中的 "... to verify that ..." 目的子句是允許的。
FORBIDDEN_MAIN_VERBS = [
    "observe whether",
    "observe",
    "see if",
    "check whether",
    "confirm whether",
    "verify",
    "watch",
    "monitor",
    "inspect",
]

# §6 ER 不得出現的 modal verbs（RD 原文語氣，必須轉成可觀察陳述）。
ER_MODAL_VERBS = ["shall", "will", "should", "would"]

_STEP_NUM_RE = re.compile(r"^\s*(\d+)[.)]\s*(.*)$")
_SQUARE_RE = re.compile(r"\[[^\]]+\]")
_ANGLE_RE = re.compile(r"<[^>]+>")
# 單引號包住的 UI label；避免誤判英文所有格 / 縮寫（it's, device's）。
_SINGLE_QUOTE_RE = re.compile(r"(?<![A-Za-z])'[^']+'(?![A-Za-z])")
# 正確的雙引號 UI label — 檢查括號違規前先剔除，其內容視為合法。
_DOUBLE_QUOTED_RE = re.compile(r'"[^"]*"')
# HTML 換行標籤 — 寫進 Excel 只會變成字面文字，欄位必須用真換行。
_BR_TAG_RE = re.compile(r"<\s*br\s*/?\s*>", re.IGNORECASE)
# §5.6：baseline 一詞只能出現在末步的比較 ER，不能出現在記錄步。
_BASELINE_RE = re.compile(r"\bas\s+(?:the\s+)?baseline\b", re.IGNORECASE)
# A-026：Media Tab Button 的標籤依 radio tier 而異（MN2：R1High="Playing"、
# R1Low="Playing: Source"）。tier 未裁決前不改寫 TC，改以計數追蹤——marker
# 適合精準檢索，不適合普查。裁決下來後跑一次替換，數字必須整批歸零或整批換邊。
_TIER_LABEL_RES = {
    "playing-r1high": re.compile(r'"Playing"'),
    "playing-r1low": re.compile(r'"Playing:[^"]*"'),
}

# A-029：部分需求依 radio tier × 螢幕尺寸而適用（MW9 排除 R1 Low 7"）。
# 這些 TC 的車型旗標暫依 workbook 現行慣例全設 1，待 Group 0 裁決後修正。
# 標記方式是 parent 檔的 write_back.flags_pending，計數以便一次檢索。
FLAGS_PENDING_KEY = "flags_pending"


@dataclass
class Finding:
    """One rule violation on one TC."""
    req_id: str
    rule: str
    message: str
    source: str = ""

    def format(self) -> str:
        where = f"{self.source}::" if self.source else ""
        return f"{where}{self.req_id} [{self.rule}] {self.message}"


@dataclass
class LintReport:
    """Aggregate result across all linted TCs."""
    total: int = 0
    findings: list[Finding] = field(default_factory=list)
    # (file, "<anomaly id>: <reason>") — parents that intentionally produced no TC
    blocked: list[tuple[str, str]] = field(default_factory=list)
    # (file, "<anomaly id>: <note>") — parents generated on a declared reading of
    # an unresolved spec conflict; retrievable when the ruling arrives
    assumptions: list[tuple[str, str]] = field(default_factory=list)
    # A-026 tier-dependent label occurrences, counted not flagged
    tier_labels: Counter = field(default_factory=Counter)
    # A-029 parents whose vehicle-flag assignment awaits the Group 0 ruling
    flags_pending: list[tuple[str, str]] = field(default_factory=list)

    @property
    def failed_req_ids(self) -> list[str]:
        seen = []
        for f in self.findings:
            if f.req_id not in seen:
                seen.append(f.req_id)
        return seen

    @property
    def passed(self) -> bool:
        return not self.findings

    def to_dict(self) -> dict:
        return {
            "total": self.total,
            "failed": len(self.failed_req_ids),
            "passed": self.passed,
            "blocked": [{"source": s, "reason": r} for s, r in self.blocked],
            "assumptions": [{"source": s, "note": n} for s, n in self.assumptions],
            "tier_labels": dict(self.tier_labels),
            "flags_pending": [{"source": s, "note": n} for s, n in self.flags_pending],
            "findings": [
                {
                    "req_id": f.req_id,
                    "rule": f.rule,
                    "message": f.message,
                    "source": f.source,
                }
                for f in self.findings
            ],
        }


def load_test_set_whitelist(data_dir: Path) -> set[str]:
    """Build the allowed Test Set labels for the framework.

    Union of three sources:
      - chapter defaults in `section_to_testset.json` (incl. the two new Sets)
      - per-parent overrides in the same file
      - Test Sets already present in the done region (`exemplars.json` keys) —
        rows 10-332 use Sets no remaining chapter maps to (General Anatomy,
        Playing Tab, Metadata, Tuning Controls) and they stay valid.

    Returns an empty set when neither file exists — callers treat that as
    "skip the whitelist check" rather than failing every TC.
    """
    labels: set[str] = set()

    mapping_path = data_dir / "section_to_testset.json"
    if mapping_path.exists():
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        labels |= {c["test_set"] for c in mapping.get("chapters", {}).values()}
        labels |= {o["test_set"] for o in mapping.get("overrides", {}).values()}

    exemplar_path = data_dir / "exemplars.json"
    if exemplar_path.exists():
        labels |= set(json.loads(exemplar_path.read_text(encoding="utf-8")))

    return {label for label in labels if label}


def split_steps(text: str) -> list[str]:
    """Return the numbered steps of a Procedure / ER block.

    Blank lines are phase breaks (§6.1 multi-phase layout) and are dropped;
    continuation lines that carry no leading number are folded into the
    previous step so a wrapped step is not counted twice.
    """
    steps: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = _STEP_NUM_RE.match(line)
        if m:
            steps.append(m.group(2).strip())
        elif steps:
            steps[-1] = f"{steps[-1]} {line.strip()}"
    return steps


def _check_presence(tc: dict, add) -> None:
    for key in REQUIRED_KEYS:
        if key not in tc:
            add("keys", f"missing key `{key}`")
            continue
        value = tc[key]
        if not isinstance(value, str):
            add("keys", f"`{key}` must be a string, got {type(value).__name__}")
        elif not value.strip():
            add("keys", f"`{key}` is empty")
        elif value.strip().upper() == "NA" and key not in NA_ALLOWED_KEYS:
            add("keys", f"`{key}` is 'NA'; only {sorted(NA_ALLOWED_KEYS)} may be NA")


def _check_line_terminators(tc: dict, add) -> None:
    for key in LINE_TERMINATOR_KEYS:
        text = tc.get(key)
        if not isinstance(text, str):
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            stripped = line.rstrip()
            if stripped.endswith((".", "。")):
                add("trailing-period", f"`{key}` line {i} ends with a period: {stripped!r}")


def _check_ui_label_quoting(tc: dict, add) -> None:
    """§6.3 — UI labels use double quotes; no [...], '...', <...> wrappers.

    Content already inside a `"..."` label is exempt: the done region writes
    dynamic label parts that way (`Press "Playing: <source>" on the Tab
    Buttons`), which is correct usage, not a placeholder leak.
    """
    for key in LINE_TERMINATOR_KEYS + ["test_item"]:
        raw = tc.get(key)
        if not isinstance(raw, str):
            continue
        if key == "test_item":
            # test_item is "<RD sentence verbatim>\n\n(<scenario tag>)". Only the
            # tag is ours to word; the RD half is a quotation and may legitimately
            # contain the source's own bracket labels (e.g. APP16's "delete [X]
            # button"). Check what we author, not what we quote.
            raw = raw.split("\n\n", 1)[1] if "\n\n" in raw else raw
        text = _DOUBLE_QUOTED_RE.sub(" ", raw)
        if _SQUARE_RE.search(text):
            add("label-format", f"`{key}` uses [...] bracket labels; use \"...\"")
        if _ANGLE_RE.search(text):
            add("label-format", f"`{key}` uses <...> placeholders; use \"...\"")
        # test_item quotes the RD sentence verbatim and RD source text uses
        # '...' for strings (e.g. 'Connect a Bluetooth Audio Device'); the
        # double-quote rule applies to steps, not to the quoted requirement.
        if key != "test_item" and _SINGLE_QUOTE_RE.search(text):
            add("label-format", f"`{key}` uses '...' labels; use \"...\"")


def _check_br_tags(tc: dict, add) -> None:
    """A literal <br> reaches Excel as text — line breaks must be real newlines."""
    for key in REQUIRED_KEYS:
        value = tc.get(key)
        if isinstance(value, str) and _BR_TAG_RE.search(value):
            add("br-tag", f"`{key}` contains a literal <br> tag; use a real newline")


def _str_field(tc: dict, key: str) -> str:
    """Trimmed string value, or "" for missing / non-string (already flagged by _check_presence)."""
    value = tc.get(key)
    return value.strip() if isinstance(value, str) else ""


def _check_dropdowns(tc: dict, test_sets: set[str], add) -> None:
    priority = _str_field(tc, "priority")
    if priority and priority not in VALID_PRIORITIES:
        add("priority", f"{priority!r} not in {VALID_PRIORITIES}")

    method = _str_field(tc, "design_method")
    if method and method not in VALID_DESIGN_METHODS:
        add("design-method", f"{method!r} is not one of the 9 dropdown strings (exact match required)")

    group = _str_field(tc, "test_group")
    if group and group != EXPECTED_TEST_GROUP:
        add("test-group", f"{group!r} != {EXPECTED_TEST_GROUP!r}")

    test_set = _str_field(tc, "test_set")
    if test_set and test_sets and test_set not in test_sets:
        add("test-set", f"{test_set!r} not in the framework whitelist {sorted(test_sets)}")


def _check_steps(tc: dict, add) -> None:
    procedure = tc.get("test_procedure")
    expected = tc.get("expected_result")
    if not isinstance(procedure, str) or not isinstance(expected, str):
        return

    proc_steps = split_steps(procedure)
    er_steps = split_steps(expected)

    if len(proc_steps) < 2:
        add("step-count", f"test_procedure has {len(proc_steps)} numbered step(s), need >= 2")
    if len(proc_steps) != len(er_steps):
        add(
            "step-er-1to1",
            f"test_procedure has {len(proc_steps)} steps but expected_result has {len(er_steps)}",
        )

    for i, step in enumerate(proc_steps, start=1):
        lowered = step.lower()
        for verb in FORBIDDEN_MAIN_VERBS:
            if lowered.startswith(verb):
                add("forbidden-verb", f"procedure step {i} opens with forbidden main verb {verb!r}")
                break

    for i, er in enumerate(er_steps, start=1):
        lowered = er.lower()
        for modal in ER_MODAL_VERBS:
            if re.search(rf"\b{modal}\b", lowered):
                add("er-modal", f"expected_result step {i} contains modal verb {modal!r}")
                break
        # §5.6 — the recording step says what is read; only the final
        # comparison ER may label the value a baseline.
        if i < len(er_steps) and _BASELINE_RE.search(er):
            add(
                "er-baseline",
                f"expected_result step {i} labels a recording step 'as baseline' (§5.6: "
                "baseline belongs in the final comparison ER)",
            )


def lint_tc(tc: dict, test_sets: set[str] | None = None, source: str = "") -> list[Finding]:
    """Run every Step 3 rule against one TC record."""
    req_id = str(tc.get("req_id") or "<no req_id>")
    findings: list[Finding] = []

    def add(rule: str, message: str) -> None:
        findings.append(Finding(req_id=req_id, rule=rule, message=message, source=source))

    _check_presence(tc, add)
    _check_line_terminators(tc, add)
    _check_ui_label_quoting(tc, add)
    _check_br_tags(tc, add)
    _check_dropdowns(tc, test_sets or set(), add)
    _check_steps(tc, add)
    return findings


def extract_tcs(payload) -> list[dict]:
    """Pull the TC list out of a generated-file payload.

    Accepts a bare list, `{"tcs": [...]}`, or the batch-shaped
    `{"requirements": [{"tcs": [...]}, ...]}`.
    """
    if isinstance(payload, list):
        return [tc for tc in payload if isinstance(tc, dict)]
    if not isinstance(payload, dict):
        return []
    if isinstance(payload.get("tcs"), list):
        return [tc for tc in payload["tcs"] if isinstance(tc, dict)]
    if isinstance(payload.get("requirements"), list):
        out = []
        for req in payload["requirements"]:
            if isinstance(req, dict) and isinstance(req.get("tcs"), list):
                out.extend(tc for tc in req["tcs"] if isinstance(tc, dict))
        return out
    return []


def check_req_ids_against_leaves(payload, leaves: set[str], source: str) -> list[Finding]:
    """Every req_id must name a leaf that exists in 037.

    §8.2.2 lets one RD sub-id produce several TCs — they all keep that one
    sub-id. Inventing `-02`, `-03` to number the TCs silently creates rows
    pointing at requirements that do not exist, which no other rule catches
    because such a row is otherwise well-formed.
    """
    if not leaves:
        return []
    out = []
    for tc in extract_tcs(payload):
        rid = str(tc.get("req_id") or "")
        if rid and rid not in leaves:
            out.append(Finding(req_id=rid, rule="unknown-req-id",
                               message="req_id does not match any leaf in 037", source=source))
    for rid in (payload.get("blocked") or {}).get("req_ids", []) if isinstance(payload, dict) else []:
        if rid not in leaves:
            out.append(Finding(req_id=rid, rule="unknown-req-id",
                               message="blocked req_id does not match any leaf in 037", source=source))
    return out


def load_leaf_ids(data_dir: Path) -> set[str]:
    """req_ids of every remaining leaf, or empty when the artifact is not built."""
    path = data_dir / "remaining_leaves.json"
    if not path.exists():
        return set()
    return {l["req_id"] for l in json.loads(path.read_text(encoding="utf-8")) if l.get("req_id")}


def count_tier_labels(tc: dict) -> Counter:
    """Count tier-dependent tab-button labels in one TC (A-026).

    Not a finding: which form is correct is an open RD-1 question, so the gate
    tracks the population instead of rejecting it. After the ruling, one
    replacement pass must drive one counter to zero.
    """
    blob = " ".join(str(tc.get(k) or "") for k in ("test_procedure", "expected_result", "test_item"))
    # Counts TCs, not occurrences: the actionable number is how many rows a
    # replacement pass must touch.
    return Counter({name: 1 for name, rx in _TIER_LABEL_RES.items() if rx.search(blob)})


def blocked_reason(payload) -> str:
    """A parent may legitimately produce no TC when its spec source is unusable.

    Such a file declares `"blocked": {"reason": ...}`; the gate reports it as a
    blocked parent rather than an empty-file failure. An anomaly-tracker id is
    required so a blocked parent can never be recorded without a paper trail.
    """
    if not isinstance(payload, dict):
        return ""
    blocked = payload.get("blocked")
    if not isinstance(blocked, dict):
        return ""
    reason = str(blocked.get("reason") or "").strip()
    anomaly = str(blocked.get("anomaly") or "").strip()
    if not reason or not anomaly:
        return ""
    return f"{anomaly}: {reason}"


def assumption_notes(payload) -> list[str]:
    """Declared readings of unresolved conflicts this parent is generated on.

    A file declares `"assumption": {...}` or, when one parent bets on more than
    one open question, `"assumption": [{...}, {...}]`. Each marker needs a
    `note` and an `anomaly` id — same contract as `blocked` — so every bet on a
    pending RD-1 ruling is machine-retrievable when the ruling arrives.

    Each marker also carries `req_ids`, and they are deliberately scoped per
    marker rather than per parent: a ruling usually invalidates *specific* TCs,
    not everything the parent produced, and a whole-parent marker would make the
    rework list far larger than reality.

    Returns [] if any marker is malformed, so the caller can report it.
    """
    if not isinstance(payload, dict) or "assumption" not in payload:
        return []
    raw = payload.get("assumption")
    markers = raw if isinstance(raw, list) else [raw]
    if not markers:
        return []
    out = []
    for a in markers:
        if not isinstance(a, dict):
            return []
        note = str(a.get("note") or "").strip()
        anomaly = str(a.get("anomaly") or "").strip()
        if not note or not anomaly:
            return []
        ids = a.get("req_ids") or []
        scope = f" [{', '.join(ids)}]" if isinstance(ids, list) and ids else ""
        out.append(f"{anomaly}: {note}{scope}")
    return out


def lint_paths(paths: list[Path], test_sets: set[str], leaf_ids: set[str] | None = None) -> LintReport:
    report = LintReport()
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        report.findings.extend(check_req_ids_against_leaves(payload, leaf_ids or set(), path.name))
        if isinstance(payload, dict) and "assumption" in payload:
            notes = assumption_notes(payload)
            if notes:
                report.assumptions.extend((path.name, n) for n in notes)
            else:
                report.findings.append(Finding(
                    req_id="<file>", rule="assumption-marker",
                    message="every `assumption` marker needs both `note` and `anomaly`",
                    source=path.name))
        if isinstance(payload, dict):
            wb = payload.get("write_back") or {}
            note = str(wb.get(FLAGS_PENDING_KEY) or "").strip()
            if note:
                report.flags_pending.append((path.name, note))

        tcs = extract_tcs(payload)
        if not tcs:
            reason = blocked_reason(payload)
            if reason:
                report.blocked.append((path.name, reason))
                continue
            report.findings.append(
                Finding(req_id="<file>", rule="empty", message="no TC records found", source=path.name)
            )
            continue
        for tc in tcs:
            report.total += 1
            report.findings.extend(lint_tc(tc, test_sets, source=path.name))
            report.tier_labels.update(count_tier_labels(tc))
    return report


def collect_paths(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(target.glob("*.json"))
    return [target]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="generated/ directory or a single JSON file")
    ap.add_argument("--data", default="data", help="data dir holding section_to_testset.json")
    ap.add_argument("--json-report", help="write the full report as JSON to this path")
    args = ap.parse_args()

    target = Path(args.target)
    if not target.exists():
        print(f"error: {target} does not exist", file=sys.stderr)
        return 2

    paths = collect_paths(target)
    if not paths:
        print(f"error: no JSON files under {target}", file=sys.stderr)
        return 2

    test_sets = load_test_set_whitelist(Path(args.data))
    if not test_sets:
        print("warning: section_to_testset.json not found — skipping Test Set whitelist check", file=sys.stderr)

    report = lint_paths(paths, test_sets, load_leaf_ids(Path(args.data)))

    for finding in report.findings:
        print(finding.format())

    for source, reason in report.blocked:
        print(f"{source}:: BLOCKED — {reason}")

    for source, note in report.assumptions:
        print(f"{source}:: ASSUMPTION — {note}")

    for source, note in report.flags_pending:
        print(f"{source}:: FLAGS PENDING — {note}")

    if report.tier_labels:
        counts = ", ".join(f"{k}={v}" for k, v in sorted(report.tier_labels.items()))
        print(f"\nA-026 tier-dependent tab labels (open ruling, tracked not flagged): {counts}")

    failed = len(report.failed_req_ids)
    extra = ""
    if report.blocked:
        extra += f", {len(report.blocked)} parent(s) blocked"
    if report.assumptions:
        extra += f", {len(report.assumptions)} parent(s) on a declared assumption"
    print(f"\n{report.total} TC linted, {failed} failed, {len(report.findings)} finding(s){extra}")

    if args.json_report:
        Path(args.json_report).write_text(
            json.dumps(report.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
        )

    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
