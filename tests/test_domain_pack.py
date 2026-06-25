"""Stage 1 — domain_pack tests. Pure data / IO; no AI."""
from domain_pack import (
    DomainPack,
    load_domain_pack,
    save_domain_pack,
    to_prompt_block,
    validate,
)


def _sample():
    return DomainPack(
        project="Player",
        glossary=[{"term": "Repeat", "definition": "All / One / Off modes"}],
        feature_model=[{"feature": "Play/Pause", "normal": "toggles playback",
                        "abnormal": "no media -> disabled"}],
        boundaries=[{"name": "Repeat modes", "enum": ["All", "One", "Off"],
                     "source": "CFTS025 §Play Controls"}],
        traceability_hints=[
            {"req": "SWE1-PLA-030-01", "spec_ref": "Repeat All"},
            {"req": "SWE1-PLA-027", "spec_ref": "Play Controls list"},
        ],
        open_questions=[{"question": "Repeat One supported?", "status": "open"}],
        reviewed_at="2026-06-25T00:00:00+00:00",
    )


def test_roundtrip(tmp_path):
    path = str(tmp_path / "domain_pack.json")
    pack = _sample()
    save_domain_pack(pack, path)
    reloaded = load_domain_pack(path)
    assert reloaded.project == "Player"
    assert reloaded.boundaries[0]["enum"] == ["All", "One", "Off"]
    assert reloaded.reviewed_at == pack.reviewed_at


def test_load_missing_returns_empty(tmp_path):
    pack = load_domain_pack(str(tmp_path / "nope.json"))
    assert pack.project == "" and pack.glossary == []


def test_validate_flags_gaps():
    empty = DomainPack()
    warns = validate(empty)
    assert any("project" in w for w in warns)
    assert any("無實質內容" in w for w in warns)
    assert any("Gate" in w for w in warns)

    # A signed-off pack with resolved questions is clean.
    pack = _sample()
    pack.open_questions[0]["status"] = "resolved"
    assert validate(pack) == []


def test_to_prompt_block_filters_traceability_by_req():
    pack = _sample()
    block = to_prompt_block(pack, req_id="SWE1-PLA-027")
    # Global sections always present.
    assert "Glossary" in block and "Repeat modes" in block
    # Only the matching traceability hint is rendered.
    assert "Play Controls list" in block
    assert "Repeat All" not in block.split("Traceability hints")[-1]

    # Without a req filter, all hints appear.
    full = to_prompt_block(pack)
    assert "Repeat All" in full and "Play Controls list" in full
