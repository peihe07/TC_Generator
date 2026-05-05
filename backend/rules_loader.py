"""Shared runtime rules loader for generation prompts."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
RULE_FILES = [
    DOCS_DIR / "ASPICE_SWE6_AI_Instruction.md",
    DOCS_DIR / "Test Case Design Method 判斷規則.md",
    DOCS_DIR / "test_case_priority.md",
]


FALLBACK_RULES = """
## ASPICE TC Writing Rules
- One behavior per TC, must match requirement intent
- Format: Condition/Trigger → Observable Outcome

## Pre-Conditions
- State or environment ONLY — never actions, checks/reads, or data-presence
  (e.g. "HU has 5,000 entries" → set up + read in a baseline step)
- Minimum necessary state, numbered list or NA

## Input Test Data
- Field ownership: environment data belongs in Pre-Conditions; UI interaction
  values belong in Test Procedure; only independent datasets / CAN values /
  boundary values belong here
- Use NA when data is already captured by Pre-Conditions or Procedure

## Test Procedure
- Setup steps → Transition steps → Final Step (verification)
- Each step: executable action + target; add purpose only when needed for
  multi-purpose UI, non-obvious setup, opaque targets, or the Final Step
- Final step must include action + verification target
- Forbidden main verbs: observe / see if / check whether / confirm whether / verify / watch / monitor / inspect
  Use: Check that / Confirm that / Read / Record / Compare + explicit target
- CLI/tooling commands use a numbered business action line followed by an
  unnumbered `$ ...` command line

## Expected Result
- 1:1 mapping with procedure steps
- Observable, judgeable, no vague language
- Multi-phase setup + verification ER blocks are separated by one blank line

## Design Method (assign AFTER procedure+ER finalized)
- Judge from the ACTUAL flow via first-match on PRIMARY intent:
  Negative → Fault Injection → State Transition → Decision Table → EP → BVA → Combinatorial → Scenario → Functional

## Application Output Contract
- Priority is a workbook/tooling field, not an ASPICE rule in the instruction doc
- Return exactly P0 / P1 / P2 / P3
- P0: a feature's core/primary flow (the must-test happy path that defines the feature working at all); plus safety, boot/recovery, connection, audio output, eCall, vehicle-critical CAN signal, data loss risk. Default any "main functionality normal flow" test case to P0.
- P1: secondary or advanced operations of a major feature that are NOT the core primary flow — boundary/variation cases, key operational logic branches, non-primary user-facing flows
- P2: secondary/support functionality with limited major-feature impact
- P3: minor UI enhancement, low-impact customization, rare-use scenario, cosmetic detail
""".strip()


def load_rules(
    rule_files: Iterable[Path] | None = None,
    fallback: str = FALLBACK_RULES,
) -> str:
    """Load markdown rule files and concatenate them for prompt injection.

    Empty or unreadable files are skipped. If no rule file contributes content,
    the compact fallback is returned.
    """
    sections: list[str] = []
    for path in rule_files or RULE_FILES:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if text:
            sections.append(f"# {path.stem}\n\n{text}")
    return "\n\n---\n\n".join(sections) if sections else fallback
