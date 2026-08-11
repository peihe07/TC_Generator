"""Tests for the absorbed-clause citation exception in SXM's lint_tcs.py.

Ruled 2026-08-11 (necessity threshold): an absorbed clause's citation travels
into the citing leaf only when that clause's behaviour cannot be stated without
it, and the delivered row must show the whole chain — leaf clause, absorbed
clause, borrowed token — so the borrowing is visible rather than inferred.

The necessity half is a judgement recorded in the `[A-SX08]` assumption. What
is mechanical, and what is pinned here, is the licensing shape: the token is
legal only while the absorbed clause that writes it is cited beside it. The
failure mode this guards is silent: dropping the absorbed clause id from
specification_reference leaves a citation with no visible licence, and without
this check it would still lint clean.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "sxm_lint", ROOT / "SXMHMI" / "scripts" / "lint_tcs.py")
if _spec is None or _spec.loader is None:
    pytest.skip("SXM lint_tcs.py not present", allow_module_level=True)
lint = importlib.util.module_from_spec(_spec)
sys.modules["sxm_lint"] = lint
_spec.loader.exec_module(lint)


# 4872953 is the Genre Seek behaviour clause: unallocated, absorbed into leaf
# 148, and it defines its base behaviour only by reference to CFTS024-165.
UNALLOC = {
    "4872953": "The Genre Seek function shall behave in the same manner as the "
               "Seek Up function described in Section CFTS024-165 with the "
               "exception that only stations matching the selected Genre shall "
               "be considered valid.",
    "4872880": "The HU shall provide a selection for these Browse category "
               "options in satellite mode -All channels, Presets, Favorites.",
}


def test_a_token_the_absorbed_clause_writes_is_licensed():
    refs = ["CFTS024-4872952", "CFTS024-4872953", "CFTS024-165"]
    assert lint.absorbed_tokens(refs, UNALLOC) == {"CFTS024-165"}


def test_the_licence_dies_with_the_absorbed_clause_id():
    """Cite the token without the clause that writes it and nothing licenses it."""
    assert lint.absorbed_tokens(["CFTS024-4872952", "CFTS024-165"], UNALLOC) == set()


def test_an_absorbed_clause_that_cites_nothing_licenses_nothing():
    refs = ["CFTS024-4872879", "CFTS024-4872880"]
    assert lint.absorbed_tokens(refs, UNALLOC) == set()


def test_an_allocated_clause_id_does_not_reach_into_the_unallocated_corpus():
    """Only ids present in the unallocated set can license — a leaf's own
    clause citing something is R11's own path, not this exception's."""
    assert lint.absorbed_tokens(["CFTS024-4872952"], UNALLOC) == set()


def test_no_unallocated_data_means_no_licences_rather_than_a_crash():
    assert lint.absorbed_tokens(["CFTS024-4872953", "CFTS024-165"], {}) == set()


def test_seven_digit_ids_are_never_treated_as_borrowed_tokens():
    """A full-shape clause id passes the format check on its own; it must not
    also be handed out as a licensed short-id token."""
    got = lint.absorbed_tokens(["CFTS024-4872953"], {
        "4872953": "see CFTS024-4872999 and CFTS024-165"})
    assert got == {"CFTS024-165"}


def test_load_reads_ids_across_sections(tmp_path):
    import json
    d = tmp_path / "data"
    d.mkdir()
    (d / "unallocated_clauses.json").write_text(json.dumps({
        "1.5.15": {"unallocated": [{"id": 4872953, "text": "see CFTS024-165"}]},
        "1.5.11": {"unallocated": [{"id": 4872880, "text": "enumeration"},
                                   {"id": None, "text": "no id"}]},
    }), encoding="utf-8")
    got = lint.load_unallocated_texts(tmp_path)
    assert set(got) == {"4872953", "4872880"}


def test_load_without_the_file_is_empty_not_an_error(tmp_path):
    assert lint.load_unallocated_texts(tmp_path) == {}
