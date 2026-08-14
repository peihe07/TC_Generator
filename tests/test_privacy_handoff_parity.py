"""R41-6 — every Privacy handoff package accounts for its upstream package.

Two packages went unexecuted without anyone noticing (R17-1..R17-4 stranded in
handoff 03, then the whole of handoff 15), and both were found only because a
later package happened to cite a ruling that was not in the repo. R39-1 made
the check a duty; R19-3 says a rule claiming exclusivity needs a mechanism
rather than discipline, and R41-6 adds the obvious corollary: **running a
script once is not a mechanism — the test is whether it runs next time.**

Each handoff file ends with a machine-readable line (R41-5):

    <!-- HANDOFF-LINK: <NN> -> <status> -->

`upstream:<NN>`        the package produced its own upstream file
`merged into <NN>`     its upstream was folded into another package's
`no-upstream-required` the package never asked for one (handoff 10)
`no-upstream-produced` it asked for one and none was written — a real gap,
                       recorded rather than filled (R41-4: a gap in the
                       record is marked, not back-filled, because
                       back-filling makes the gap disappear without making
                       the work traceable)
`pending:<NN>`         the destination is declared but the package has not
                       run yet — a determinable unfinished state, not an
                       undeterminable one (R44-2: if the value set cannot
                       express a state that IS determinable, the set is
                       incomplete; "cannot tell" must not stand in for
                       "has not happened yet", because the follow-up action
                       differs)
`chat-direct:<ruling>` that round was ruled in chat and produced no handoff
                       package; recorded so the gap in the exchange chain is
                       visible rather than silent (R44-3)
`unknown`              cannot be settled by measurement; must be listed in
                       the upstream package

Privacy only. The other features' exchanges largely predate this convention
and are not in scope (R41-6).
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
HANDOFF = REPO_ROOT / "features/privacy/docs/handoff"
UPSTREAM = REPO_ROOT / "features/privacy/docs/upstream"

LINK_RE = re.compile(r"<!--\s*HANDOFF-LINK:\s*(\d{2})\s*->\s*(.+?)\s*-->")
SIMPLE = {"no-upstream-required", "no-upstream-produced", "unknown"}
# Statuses of the form `<kind>:<target>`; the target must resolve for the
# first two, while `chat-direct` points at a ruling id rather than a file.
UPSTREAM_KINDS = ("upstream", "merged into", "pending")

pytestmark = pytest.mark.skipif(
    not HANDOFF.is_dir(), reason="features/privacy/docs/handoff not present")


def parse_link(text: str) -> tuple[str, str] | None:
    hits = LINK_RE.findall(text)
    return hits[-1] if hits else None


def upstream_numbers() -> set[str]:
    return {p.name[:2] for p in UPSTREAM.glob("*.md")}


def collect() -> dict[str, tuple[str, str]]:
    """NN -> (declared NN, status) for every handoff package."""
    out = {}
    for path in sorted(HANDOFF.glob("*.md")):
        link = parse_link(path.read_text(encoding="utf-8"))
        out[path.name[:2]] = link
    return out


def test_every_handoff_declares_a_link():
    missing = sorted(nn for nn, link in collect().items() if link is None)
    assert not missing, (
        "handoff packages with no HANDOFF-LINK marker: " + ", ".join(missing)
        + "\nAdd `<!-- HANDOFF-LINK: NN -> <status> -->` at the end of each. "
        "A package with no marker is indistinguishable from one nobody "
        "checked (R41-5).")


def test_declared_number_matches_the_filename():
    wrong = {nn: link[0] for nn, link in collect().items()
             if link and link[0] != nn}
    assert not wrong, f"HANDOFF-LINK declares the wrong number: {wrong}"


def test_status_values_are_legal_and_resolve():
    ups = upstream_numbers()
    bad: list[str] = []
    for nn, link in sorted(collect().items()):
        if link is None:
            continue
        status = link[1]
        if status in SIMPLE:
            continue
        m = re.fullmatch(r"upstream:(\d{2})", status)
        if m:
            if m.group(1) not in ups:
                bad.append(f"{nn}: declares upstream:{m.group(1)} but "
                           f"docs/upstream/{m.group(1)}_*.md does not exist")
            continue
        m = re.fullmatch(r"merged into (\d{2})", status)
        if m:
            if m.group(1) not in ups:
                bad.append(f"{nn}: declares merged into {m.group(1)} but "
                           f"that upstream package does not exist")
            continue
        m = re.fullmatch(r"pending:(\d{2})", status)
        if m:
            if m.group(1) not in ups:
                bad.append(f"{nn}: declares pending:{m.group(1)} but that "
                           f"upstream package does not exist")
            continue
        if re.fullmatch(r"chat-direct:R\d+(-\d+)?", status):
            continue
        bad.append(f"{nn}: {status!r} is not a legal status")
    assert not bad, "HANDOFF-LINK problems:\n  " + "\n  ".join(bad)


def test_no_upstream_is_orphaned():
    """The check runs both ways: an upstream nobody claims is also a gap."""
    claimed = set()
    for nn, link in collect().items():
        if link is None:
            continue
        status = link[1]
        m = re.fullmatch(r"upstream:(\d{2})", status)
        if m:
            claimed.add(m.group(1))
        m = re.fullmatch(r"merged into (\d{2})", status)
        if m:
            claimed.add(m.group(1))
        m = re.fullmatch(r"pending:(\d{2})", status)
        if m:
            claimed.add(m.group(1))
    orphans = sorted(upstream_numbers() - claimed)
    assert not orphans, (
        f"upstream packages no handoff points at: {orphans}")


# ------------------------------------------------------------------ controls

def test_positive_control_missing_marker(tmp_path, monkeypatch):
    """Removing a package's marker must fail the parity check."""
    stage = tmp_path / "handoff"
    shutil.copytree(HANDOFF, stage)
    victim = sorted(stage.glob("*.md"))[0]
    victim.write_text(LINK_RE.sub("", victim.read_text(encoding="utf-8")),
                      encoding="utf-8")
    monkeypatch.setattr(sys.modules[__name__], "HANDOFF", stage)
    missing = sorted(nn for nn, link in collect().items() if link is None)
    assert missing, "removing a marker did not make the check fail"


def test_positive_control_dangling_reference(tmp_path, monkeypatch):
    """A marker pointing at an upstream that does not exist must fail."""
    stage = tmp_path / "handoff"
    shutil.copytree(HANDOFF, stage)
    victim = sorted(stage.glob("*.md"))[0]
    victim.write_text(
        LINK_RE.sub("<!-- HANDOFF-LINK: 00 -> upstream:99 -->",
                    victim.read_text(encoding="utf-8")), encoding="utf-8")
    monkeypatch.setattr(sys.modules[__name__], "HANDOFF", stage)
    ups = upstream_numbers()
    statuses = [link[1] for link in collect().values() if link]
    assert any(re.fullmatch(r"upstream:(\d{2})", s)
               and re.fullmatch(r"upstream:(\d{2})", s).group(1) not in ups
               for s in statuses), "a dangling upstream reference was not caught"


def test_negative_control_pending_is_legal():
    """R44-2 — `pending:<NN>` must pass; it is a determinable state.

    Before this value existed, handoff 18 had to borrow `unknown`, which
    says the opposite of what is true about it.
    """
    link = collect().get("18")
    assert link and link[1] == "pending:17"
    test_status_values_are_legal_and_resolve()   # must not raise


def test_negative_control_legal_no_upstream_required():
    """A compliant `no-upstream-required` must NOT be reported as a problem.

    handoff 10 defined no upstream requirement at all; flagging it would make
    the gate cry wolf on the one case the format exists to describe.
    """
    link = collect().get("10")
    assert link and link[1] == "no-upstream-required"
    test_status_values_are_legal_and_resolve()   # must not raise
