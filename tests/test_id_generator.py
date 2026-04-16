"""Tests for TC ID generator module."""
import pytest

from id_generator import generate_group_abbreviation, generate_tc_ids


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
