from pathlib import Path

from rules_loader import FALLBACK_RULES, load_rules


def test_load_rules_concatenates_existing_markdown_files(tmp_path: Path):
    first = tmp_path / "first.md"
    second = tmp_path / "second.md"
    first.write_text("First rules", encoding="utf-8")
    second.write_text("Second rules", encoding="utf-8")

    loaded = load_rules([first, second])

    assert "# first" in loaded
    assert "First rules" in loaded
    assert "# second" in loaded
    assert "Second rules" in loaded
    assert "---" in loaded


def test_load_rules_uses_fallback_when_no_files_contribute(tmp_path: Path):
    missing = tmp_path / "missing.md"

    assert load_rules([missing]) == FALLBACK_RULES


def test_fallback_rules_include_current_field_ownership_guidance():
    assert "Field ownership" in FALLBACK_RULES
    assert "CLI/tooling commands" in FALLBACK_RULES
    assert "Multi-phase setup + verification" in FALLBACK_RULES
