#!/usr/bin/env python3
"""Single source of truth for every Projection lint comparison (R-P49).

**Batch scripts import from here. They never re-implement a pattern.**

The rule exists because A-PJ48: A-PJ38 fixed L-PJ5's word boundary and added
`re.I`, but the B6/B7/B8 batch scripts re-implemented the same expression and
dropped `re.I`. Banned verbs are capitalised at step start (`Check whether`),
so every one of them fell through — a false negative that no gate could catch,
because the gate itself was the broken part. **A condition that is correct but
implemented in several places is equivalent to not having fixed it.**

Any change to a comparison condition (word boundary, case, scan range) is made
HERE and nowhere else; after changing it, re-run the whole workbook and update
the baseline recorded below.
"""

import re

# --- scan ranges (canon §5a fourth item: state which columns) ---------------
# Column indices into the NR1L_GEN1(HDCC) TestResults sheet.
COL = {"test_item": 8, "pre": 9, "input": 10, "proc": 11, "er": 12, "remarks": 36}

SCAN_RISK = [8, 9, 10, 11, 12, 36]   # risk-matrix scans: all text columns
SCAN_EDITABLE = [9, 11]              # defect scans: only the editable columns

# --- L-PJ5 banned procedure verbs -----------------------------------------
# Word-boundary (A-PJ38: `inspect` matched `Car Inspector`) AND case-insensitive
# (A-PJ48: verbs are capitalised at step start). Both flags are required.
BANNED_VERBS = ["observe", "check whether", "confirm whether", "see if",
                "watch", "monitor", "inspect"]
RE_BANNED = re.compile(
    r"\b(?:" + "|".join(re.escape(v) for v in BANNED_VERBS) + r")\b", re.I)

# --- L-PJ6 vague language --------------------------------------------------
# Word-boundary (A-PJ18: `a while` matched `content area while`).
RE_VAGUE = re.compile(
    r"\b(?:correctly|normally|properly|successfully|as expected|reasonable|a while)\b",
    re.I)

# --- CAN mention -----------------------------------------------------------
# CASE-SENSITIVE on purpose (A-PJ37: `re.I` matches the English modal "can" and
# inflated HMI Display 0→17, Knob 0→20 over the risk scan range).
RE_CAN = re.compile(r"\bCAN\b")

# --- L-PJ1 signal authority (R-P51) ---------------------------------------
# The two PHDCC27 DBCs are NOT the whole CAN authority for this workbook.
# Cluster Navigation cites TELEMATIC_NAV_INFO.* / TELEMATIC_DISPLAY_INFO.*,
# which are defined in the VF176 cluster-navigation spec that shipped in
# inputs/ at Phase 0 (A-PJ49). L-PJ1's authority is DBC ∪ the VF176 register
# held in data/signal_map.json["vf176_signals"].
#
# The register is maintained BY HAND (R-P51: 5 rows do not justify an
# extraction pipeline). A VF176 signal that is not registered still ABORTs —
# the gate is not bypassed, it acknowledges a second authority.
VF176_REGISTER_PATH = "features/projection/data/signal_map.json"
VF176_REGISTER_KEY = "vf176_signals"


def vf176_signals(register: dict) -> dict:
    """Registered VF176 signals, keyed `MESSAGE.Signal` (drops the _meta row)."""
    return {k: v for k, v in register.get(VF176_REGISTER_KEY, {}).items()
            if not k.startswith("_")}


def resolve_signal(msg: str, sig: str, dbc_fd, dbc_bh, vf176: dict):
    """L-PJ1 resolution across BOTH authorities.

    Returns (authority, value_table) or (None, None) when the signal resolves
    nowhere — that case ABORTs.
    """
    for label, (msgs, vals) in (("FD", dbc_fd), ("CAN-B", dbc_bh)):
        if msg in msgs and sig in msgs[msg]:
            return label, vals.get(sig, {})
    entry = vf176.get(f"{msg}.{sig}")
    if entry is not None:
        return "VF176", entry.get("enum") or {}
    return None, None


# --- L-PJ9 generic measurement equipment (R-P42, extended by R-P46) --------
# Incrementable list. Every extension is recorded in DECISIONS §0.12's table
# with: new patterns, hit count before/after, newly hit rows.
GENERIC_TOOL_PATTERNS = ["Test equipment for", "test setup for", "analyzer for",
                         "equipment for measuring", "trace tool", "capture tool",
                         "measurement tool", "test tool", "simulator",
                         "A method to"]   # +2026-08-12 (A-PJ50, second extension)
RE_GENERIC_TOOL = re.compile(
    "|".join(re.escape(p) for p in GENERIC_TOOL_PATTERNS), re.I)
# Second condition: a named tool path in the Procedure exempts the row.
RE_NAMED_TOOL = re.compile(
    r"CarPlay Tests App >|Utilities >|\bATS\b|logcat|PCTS|CAN tool|iPerf", re.I)

# --- L-PJ10 placeholders (R-P43) ------------------------------------------
RE_PLACEHOLDER = re.compile(r"<[^>]{2,40}>")
# Parameter placeholders are maintained as an EXPLICIT LIST, never inferred by
# shape — `<Device Name>` and `<TBD>` are shape-identical and only semantics
# separates them (R-P43).
PLACEHOLDER_WHITELIST = {"<Device Name>", "<Apple CarPlay OR Android Auto>"}

# --- step cross-reference (R-P39) -----------------------------------------
# Cross-references are NOT defects. Only a forward reference whose target is a
# verification step is (the D-1 circular pattern). Backward references such as
# `as recorded in step 1` are the backbone of comparison steps — 30 rows carry
# them workbook-wide and none is to be touched.
RE_STEP_XREF = re.compile(r"\bsteps?\s+\d+", re.I)

# --- tokens ---------------------------------------------------------------
RE_TOKEN = re.compile(r"\$[^$\s]+\$")

# --- frozen rows ----------------------------------------------------------
FROZEN_ROWS = {376, 377, 378, 379}        # feature.yaml done_region.frozen_rows

# --- baselines (whole workbook, rows 4-561; re-measure after any change) ---
BASELINE = {
    "L-PJ5 banned verbs": 5,      # observe 1 (r150), check whether 3 (r89/98/542), inspect 1 (r230)
    "L-PJ6 vague": 10,            # 9 rows, r520 hits in both PROC and ER
    "L-PJ9 generic tool": 15,     # 7 Performance + 3 Voice Recognition + 5 HMI Display
                                  # (R-P46 extension #2, 2026-08-12: "A method to")
    "L-PJ10 defect placeholders": 5,   # r36, r111, r124, r149, r225
    "L-PJ10 parameter placeholders": 8,  # r60, r61, r317-r322
    "step cross-references": 30,  # all backward; R-P39 leaves them alone
    "step != ER exceptions": 3,   # r184 (5/4), r355 (5/4), r517 (5/9)
}


def steps(text) -> list:
    """Numbered steps in a Procedure or Expected Result cell."""
    return [l for l in str(text or "").split("\n")
            if re.match(r"^\s*\d+[.)]\s*\S", l)]


def norm(v) -> str:
    return re.sub(r"[ \t]+", " ", str(v or "")).strip()


def placeholder_defects(text) -> list:
    """`<...>` occurrences that are NOT whitelisted parameter placeholders."""
    return [m for m in RE_PLACEHOLDER.findall(text)
            if m not in PLACEHOLDER_WHITELIST]


def forward_xrefs(procedure) -> list:
    """(step_no, referenced_step) pairs where a step points at a LATER step.

    Backward references are legal (R-P39). Only forward ones can create the
    circular order D-1 hit.
    """
    out = []
    for line in steps(procedure):
        cur = int(re.match(r"^\s*(\d+)", line).group(1))
        for m in re.finditer(r"\bsteps?\s+(\d+)", line, re.I):
            if int(m.group(1)) > cur:
                out.append((cur, int(m.group(1))))
    return out
