# Archived Docs

This directory is for historical notes that must not be loaded into runtime
prompts.

Runtime generation rules are loaded from:

- `docs/runtime/ASPICE_SWE6_AI_Instruction.md`
- `docs/runtime/TEST_CASE_DESIGN_METHOD.md`
- `docs/runtime/TEST_CASE_PRIORITY.md`

When an instruction patch has been merged into the active rule document, keep
any patch-list copy here only as change history. Do not reference archived
patches from `backend/rules_loader.py`, prompt builders, or README runtime
instructions.
