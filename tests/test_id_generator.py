"""Tests for TC ID generator module."""
import pytest

from id_generator import (
    generate_group_abbreviation,
    generate_tc_ids,
    sanitize_id_segment,
)


class TestGenerateGroupAbbreviation:
    def test_camel_case(self):
        assert generate_group_abbreviation("DeviceManager") == "DMR"

    def test_single_word(self):
        assert generate_group_abbreviation("Bluetooth") == "BLU"

    def test_multi_word(self):
        assert generate_group_abbreviation("MediaPlayer") == "MPR"

    def test_three_words(self):
        assert generate_group_abbreviation("AppleCarPlay") == "ACP"

    def test_short_word(self):
        # Short single words: take first 3 chars uppercase
        assert generate_group_abbreviation("HMI") == "HMI"


class TestGenerateTcIds:
    def test_basic_generation(self):
        ids = generate_tc_ids(project="newR1L", group_abbr="DMS", count=3)
        assert ids == ["newR1L-DMS-001", "newR1L-DMS-002", "newR1L-DMS-003"]

    def test_start_from_offset(self):
        ids = generate_tc_ids(
            project="newR1L", group_abbr="DMS", count=2, start=5
        )
        assert ids == ["newR1L-DMS-005", "newR1L-DMS-006"]

    def test_single_id(self):
        ids = generate_tc_ids(project="projX", group_abbr="BLT", count=1)
        assert ids == ["projX-BLT-001"]

    def test_zero_count(self):
        ids = generate_tc_ids(project="projX", group_abbr="BLT", count=0)
        assert ids == []

    def test_large_sequence(self):
        ids = generate_tc_ids(project="p", group_abbr="X", count=1, start=999)
        assert ids == ["p-X-999"]

    def test_no_duplicates(self):
        ids = generate_tc_ids(project="p", group_abbr="A", count=100)
        assert len(ids) == len(set(ids))

    def test_project_with_space_and_slash_sanitized(self):
        # Source workbook sometimes holds "new R/L" — must not leak into ID.
        ids = generate_tc_ids(project="new R/L", group_abbr="OMR", count=2)
        assert ids == ["newRL-OMR-001", "newRL-OMR-002"]

    def test_group_abbr_sanitized(self):
        ids = generate_tc_ids(project="proj", group_abbr="O M R", count=1)
        assert ids == ["proj-OMR-001"]

    def test_empty_project_after_sanitize_raises(self):
        with pytest.raises(ValueError, match="project"):
            generate_tc_ids(project="///", group_abbr="X", count=1)

    def test_empty_group_after_sanitize_raises(self):
        with pytest.raises(ValueError, match="group_abbr"):
            generate_tc_ids(project="P", group_abbr="   ", count=1)


class TestSanitizeIdSegment:
    def test_spaces_removed(self):
        assert sanitize_id_segment("new R/L") == "newRL"

    def test_keeps_alphanumeric(self):
        assert sanitize_id_segment("newR1L") == "newR1L"

    def test_empty_input(self):
        assert sanitize_id_segment("") == ""
