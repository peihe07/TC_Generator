# TC Generator Docs

## Runtime Docs

These files are loaded by backend prompts or directly define runtime behavior.
Rename or move them only with matching code and test updates.

- `ASPICE_SWE6_AI_Instruction.md` — generation instruction loaded by `backend/rules_loader.py`
- `TEST_CASE_DESIGN_METHOD.md` — design-method rules loaded by `backend/rules_loader.py`
- `TEST_CASE_PRIORITY.md` — priority rubric loaded by `backend/rules_loader.py`
- `ASPICE_SWE6_AI_Review.md` — review prompt / review-engine reference
- `TEST_SET_POLICY.md` — grouping, hint, override, and export policy

## Developer Docs

- `API_CONTRACT.md` — frontend/backend API contract
- `WORKFLOW_MECHANISM_TABLE.md` — user action → frontend → backend → AI/state map
- `PIPELINE_DESIGN.md` — end-to-end generation pipeline design (draft)
- `CHANGELOG.md` — architecture notes, history, and current baselines
- `DESIGN_SYSTEM.md` — Win95-themed frontend design-system reference
- `TC_Generator_Architecture_Diagrams.html` — architecture visual reference
- `design-system/` — UI conventions and design-system assets
- `../frontend-modern/README.md` — separate modern UI variant setup, ports,
  and Docker commands

## Archive

- `archive/` — historical notes and merged patches that must not be loaded into
  runtime prompts

## Local / Ignored Data

- `test/` and `temp/` are local sample data / scratch fixtures and are ignored
  by git
