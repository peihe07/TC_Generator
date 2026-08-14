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

import json
import re
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
HANDOFF = REPO_ROOT / "features/privacy/docs/handoff"
UPSTREAM = REPO_ROOT / "features/privacy/docs/upstream"
PARITY = REPO_ROOT / "features/privacy/data/handoff_parity.json"

# Both markers must occupy a whole line. Prose that *describes* the format —
# `<!-- UPSTREAM-COVERS: 05 06 07 -->` inside a sentence explaining it — is
# documentation, not a declaration, and reading it as one made upstream 17
# appear to cover packages 05-07. Anchoring to the full line separates the
# two: a declaration stands alone, a mention is embedded in something.
LINK_RE = re.compile(
    r"^\s*<!--\s*HANDOFF-LINK:\s*(\d{2})\s*->\s*(.+?)\s*-->\s*$", re.M)
COVERS_RE = re.compile(
    r"^\s*<!--\s*UPSTREAM-COVERS:\s*([\d\s]+?)\s*-->\s*$", re.M)
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


def upstream_covers() -> dict[str, set[str]]:
    """upstream NN -> the handoff packages it declares it reports on."""
    out: dict[str, set[str]] = {}
    for path in sorted(UPSTREAM.glob("*.md")):
        hits = COVERS_RE.findall(path.read_text(encoding="utf-8"))
        if hits:
            out[path.name[:2]] = set(hits[-1].split())
    return out


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


def test_link_and_covers_agree():
    """R44-7 — the two sides must point at each other.

    A one-sided marker only says what someone intended. Checking both ends
    turns the pair into a claim that can be wrong: if a handoff says it went
    into 07 and 07 does not list it, one of the two is stale.
    """
    covers = upstream_covers()
    bad: list[str] = []
    for nn, link in sorted(collect().items()):
        if link is None:
            continue
        m = (re.fullmatch(r"upstream:(\d{2})", link[1])
             or re.fullmatch(r"merged into (\d{2})", link[1]))
        if not m:
            continue
        target = m.group(1)
        if target in covers and nn not in covers[target]:
            bad.append(f"{nn} declares {link[1]!r} but upstream {target} "
                       f"lists {sorted(covers[target])}")
    for up, listed in sorted(covers.items()):
        for nn in sorted(listed):
            link = collect().get(nn)
            if link is None:
                bad.append(f"upstream {up} claims to cover {nn}, which has "
                           "no HANDOFF-LINK")
    assert not bad, "handoff/upstream markers disagree:\n  " + "\n  ".join(bad)


def test_pending_expires_when_its_upstream_claims_it():
    """R45-4 — `pending` must not outlive the thing it was waiting for.

    A state that announces "this will happen" is indistinguishable from
    "this happened" unless something checks. The expiry signal comes from
    the target itself rather than from a timer: once the upstream package
    lists the handoff in UPSTREAM-COVERS, the work is done and the marker
    should read `merged into`.
    """
    covers = upstream_covers()
    stale = []
    for nn, link in sorted(collect().items()):
        if link is None:
            continue
        m = re.fullmatch(r"pending:(\d{2})", link[1])
        if m and nn in covers.get(m.group(1), set()):
            stale.append(f"{nn} is still marked pending:{m.group(1)}, but "
                         f"upstream {m.group(1)} already declares it covered "
                         "— change it to `merged into`")
    assert not stale, "expired pending markers:\n  " + "\n  ".join(stale)


def test_unknown_markers_are_reported():
    """R44-8 — `unknown` warns, it does not fail.

    It is a legal value; what is not acceptable is letting one sit unnoticed.
    Each must be listed in the upstream package with its obstacle stated.
    """
    unknown = sorted(nn for nn, link in collect().items()
                     if link and link[1] == "unknown")
    if unknown:
        print("\nWARNING — HANDOFF-LINK markers still `unknown`: "
              + ", ".join(unknown)
              + "\n  Each must be listed in the upstream package with the "
                "reason it cannot be settled (R44-8).")


def parity_table() -> dict[str, dict]:
    """R45-3 — the correspondence table as a tracked data file.

    It used to live only inside an upstream package's prose. That worked for
    every status except `chat-direct`, which describes a round that produced
    no handoff file — so the one entry that most needed recording had nowhere
    to live except inside the very thing it says does not exist. A marker's
    carrier must not be the object it describes.
    """
    if not PARITY.is_file():
        return {}
    return {r["nn"]: r for r in json.loads(
        PARITY.read_text(encoding="utf-8"))["packages"]}


def test_parity_table_and_files_agree():
    table = parity_table()
    if not table:
        return
    files = collect()
    bad = []
    for nn in sorted(set(files) - set(table)):
        bad.append(f"handoff {nn} exists but is absent from "
                   "data/handoff_parity.json")
    for nn, row in sorted(table.items()):
        if nn in files:
            if row["status"] != files[nn][1]:
                bad.append(f"{nn}: table says {row['status']!r}, marker says "
                           f"{files[nn][1]!r}")
        elif not row["status"].startswith("chat-direct:"):
            bad.append(f"table lists {nn} ({row['status']}) but no handoff "
                       "file exists; only `chat-direct:` is exempt")
    assert not bad, "parity table disagrees with the files:\n  " + "\n  ".join(bad)


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


def test_negative_control_pending_is_legal(tmp_path, monkeypatch):
    """R44-2 — a compliant `pending:<NN>` must not be flagged.

    Written against a synthetic package rather than a real one. The first
    version asserted that handoff 18 carried `pending:17`, which held only
    until 18 was delivered and re-marked `merged into 17` — the control had
    been pinned to a transient state, so a correct transition broke it. A
    control must exercise the rule, not the current contents of the repo.
    """
    stage = tmp_path / "handoff"
    shutil.copytree(HANDOFF, stage)
    existing = sorted(upstream_numbers())[0]
    (stage / "99_synthetic.md").write_text(
        f"# synthetic\n\n<!-- HANDOFF-LINK: 99 -> pending:{existing} -->\n",
        encoding="utf-8")
    monkeypatch.setattr(sys.modules[__name__], "HANDOFF", stage)
    link = collect().get("99")
    assert link and link[1] == f"pending:{existing}"
    test_status_values_are_legal_and_resolve()   # must not raise


def test_negative_control_legal_no_upstream_required():
    """A compliant `no-upstream-required` must NOT be reported as a problem.

    handoff 10 defined no upstream requirement at all; flagging it would make
    the gate cry wolf on the one case the format exists to describe.
    """
    link = collect().get("10")
    assert link and link[1] == "no-upstream-required"
    test_status_values_are_legal_and_resolve()   # must not raise
