#!/usr/bin/env python3
"""Step 2 (AMFM) — assemble the generation context for one batch.

Gathers into one JSON everything the generator needs and nothing that would
let it invent a value:

  - the batch's leaves: 037 title (which carries the requirement text
    verbatim, with its STLA id tail) and description
  - the CFTS section each leaf brackets into, with that section's full text
    read out of the docx — spec_mode D has no export to read, so the document
    is the only source
  - sibling leaves sharing a section, so the generator can see the split axis
    it is working inside (§8.3) instead of re-deriving it per leaf
  - style-only exemplars from the frozen legacy region
  - a `column_conventions` block stating the R7 rulings as data

That last block exists because the workbook in front of the generator
disagrees with the rules it must follow: the legacy rows write Test Group
`Radio` and a band-based Test Set, and R7-Q1/Q2 replaced both for new rows.
An exemplar is persuasive; a convention has to be stated louder than the
example contradicting it.

Leaves allocated to an external CFTS document (A-AM06/A-AM07) carry no
section text — the file is not in `inputs/`. They are emitted with the reason
and the anomaly id, never silently short of context.

Usage:
    python AMFMHMI/scripts/make_batch_context.py --feature-dir AMFMHMI --list
    python AMFMHMI/scripts/make_batch_context.py --feature-dir AMFMHMI \\
        --batch "Tuner Availability"
    python AMFMHMI/scripts/make_batch_context.py --feature-dir AMFMHMI --pilot
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

import docx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from feature_config import load_feature_config, resolve_path  # noqa: E402

BATCH_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(\d+)\s*\|"
                       r"\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|")
ANOMALY = re.compile(r"A-AM\d\d")
HEADING_NUM = re.compile(r"^(\d+(?:\.\d+)*)\s")
REQ_PREFIX = "SWE-RA-RAD-"
# Above this the 037 title is a verbatim quote of the CFTS clause (the id tail
# and whitespace account for the gap); below it the two texts genuinely differ.
WORDING_VERBATIM = 0.95


def _fold(s: str) -> str:
    """Compare wording, not typography or the trailing STLA id tag."""
    s = re.sub(r"[({（]\s*\d{7}\s*[)}）]", " ", str(s or ""))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9$ ]", " ", s.lower())).strip()


class ContextError(RuntimeError):
    pass


def parse_leaf_selector(spec: str) -> list[str]:
    out = []
    for part in str(spec).split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = (int(x) for x in part.split("-", 1))
            out.extend(f"{REQ_PREFIX}{n:03d}" for n in range(a, b + 1))
        else:
            out.append(f"{REQ_PREFIX}{int(part):03d}")
    return out


def load_batches(md: Path) -> dict:
    if not md.exists():
        raise ContextError(f"missing {md}")
    batches = {}
    for line in md.read_text(encoding="utf-8").splitlines():
        m = BATCH_ROW.match(line)
        if not m or m.group(3) == "n":
            continue
        name, secs, count, ids, note = m.groups()
        req_ids = parse_leaf_selector(ids)
        if len(req_ids) != int(count):
            raise ContextError(
                f"{name}: table says {count} leaves but lists {len(req_ids)}")
        batches[name] = {
            "test_set": name, "req_ids": req_ids,
            "declared_sections": [s.strip() for s in re.split(r"[,;]", secs)
                                  if s.strip()],
            "context_note": note.strip(),
            "anomalies": sorted(set(ANOMALY.findall(note))),
        }
    if not batches:
        raise ContextError(f"no batch rows parsed from {md}")
    return batches


def section_texts(docx_path: Path) -> dict[str, dict]:
    """{section number: {title, level, text, children, subtree_chars}}.

    `text` is the section's OWN body — the paragraphs between its heading and
    the next heading of any level. That is what a leaf bracketing into this
    section is governed by: anything under a subsection belongs to a leaf that
    brackets into the subsection instead.

    The distinction is not cosmetic. §1.3 "HU Analog Tuner" runs to §1.4, so a
    same-or-higher-level span hands 82k characters — the entire analog tuner
    chapter — to the two leaves whose requirement is the section's own
    two-paragraph AM-presence gate. `children` and `subtree_chars` are kept so
    a batch that genuinely needs the subtree can ask for it knowingly.
    """
    doc = docx.Document(docx_path)
    paras = doc.paragraphs
    heads = []
    for i, p in enumerate(paras):
        if not p.style.name.startswith("Heading"):
            continue
        m = HEADING_NUM.match(p.text.strip())
        if not m:
            continue
        try:
            level = int(p.style.name.split()[-1])
        except ValueError:
            level = m.group(1).count(".") + 1
        heads.append((i, m.group(1), p.text.strip(), level))

    out = {}
    for k, (i, num, title, level) in enumerate(heads):
        own_end = heads[k + 1][0] if k + 1 < len(heads) else len(paras)
        subtree_end = len(paras)
        children = []
        for j, nnum, _, nlevel in heads[k + 1:]:
            if nlevel <= level:
                subtree_end = j
                break
            if nlevel == level + 1:
                children.append(nnum)
        body = [p.text.strip() for p in paras[i + 1:own_end] if p.text.strip()]
        subtree = [p.text.strip() for p in paras[i + 1:subtree_end] if p.text.strip()]
        out[num] = {"title": title, "level": level, "text": "\n".join(body),
                    "children": children,
                    "subtree_chars": len("\n".join(subtree))}
    return out


def build(cfg, batch: dict, stla_map: dict, sections: dict,
          exemplars: dict, spec_docs: dict) -> dict:
    primary = spec_docs.get("primary")
    leaves, needed, blocked = [], set(), []
    for rid in batch["req_ids"]:
        e = stla_map.get(rid)
        if e is None:
            raise ContextError(f"{rid} is in the batch table but not the "
                               "STLA map — rerun build_stla_map.py")
        entry = {"req_id": rid, "stla_id": e["stla_id"], "doc": e["doc"],
                 "section": e["section"], "section_title": e["section_title"],
                 "requirement_text": e["title"],
                 "analysis_note": e["description"],
                 "source_components": e["source_components"],
                 "spec_paragraph": e.get("spec_paragraph"),
                 "spec_paragraph_metadata": e.get("spec_paragraph_metadata"),
                 "spec_reference": cfg["spec_reference_template"].format(
                     doc=e["doc"], stla_id=e["stla_id"])}
        # The 037 title is supposed to quote the CFTS clause verbatim. Where it
        # does not, §8.6 says the source spec wins — so the divergence has to
        # reach the generator rather than be averaged away by having both texts
        # side by side with no comment.
        if e.get("spec_paragraph"):
            ratio = difflib.SequenceMatcher(
                None, _fold(e["title"]), _fold(e["spec_paragraph"])).ratio()
            entry["wording_agreement"] = round(ratio, 3)
            if ratio < WORDING_VERBATIM:
                entry["wording_note"] = (
                    "037 title and CFTS clause differ; §8.6 — the source spec "
                    "is authority for wording, the 037 title for scope")
        if e["section"]:
            needed.add(e["section"])
        else:
            reason = ("spec file not in inputs/ — external CFTS document"
                      if e["doc"] else "no document allocated")
            entry["section_text_absent"] = reason
            blocked.append(rid)
        leaves.append(entry)

    # Siblings: every other leaf bracketing into a section this batch uses.
    # They are the split axis made visible, not extra targets.
    in_batch = set(batch["req_ids"])
    siblings = [{"req_id": rid, "section": e["section"],
                 "requirement_text": e["title"]}
                for rid, e in stla_map.items()
                if e["section"] in needed and rid not in in_batch]

    spec = {}
    missing_sections = []
    for num in sorted(needed):
        if num in sections:
            spec[num] = sections[num]
        else:
            missing_sections.append(num)
    if missing_sections:
        raise ContextError(
            f"sections {missing_sections} are cited by the bracket map but "
            f"absent from the {primary} document — the map and the spec file "
            "have diverged")

    return {
        "feature": cfg["feature"],
        "batch": batch["test_set"],
        "spec_mode": cfg["spec_mode"],
        "leaves": leaves,
        "spec_sections": spec,
        "siblings": siblings,
        "exemplars": exemplars.get("exemplars", []),
        "exemplar_basis": exemplars.get("basis"),
        "column_conventions": {
            "test_group": {"value": cfg["test_group"],
                           "note": "R7-Q1 — new rows write this; the legacy "
                                   "region's 'Radio' is frozen, not a model"},
            "test_set": {"value": batch["test_set"],
                         "note": "R7-Q2 — capability scheme from framework "
                                 "Part III; the legacy FM/AM/USB band scheme "
                                 "is NOT adopted"},
            "author": {"value": cfg["write_back"]["author_value"],
                       "note": "R3 — rows generated here; rows quoted wholly "
                               "from another author keep that author"},
            "tc_ref_id": {"value": cfg["write_back"]["tc_ref_id_value"]},
            "spec_reference": {
                "template": cfg["spec_reference_template"],
                "note": "R7-Q3 — {doc} comes from the STLA map, never guessed"},
        },
        "context_note": batch["context_note"],
        "anomalies": batch["anomalies"],
        "blocked_section_text": blocked,
    }


def run(args) -> int:
    root = Path(args.feature_dir)
    cfg = load_feature_config(args.feature_dir)
    batches = load_batches(root / args.batches_md)

    if args.list:
        for name, b in batches.items():
            print(f"{len(b['req_ids']):3}  {name:22} "
                  f"{', '.join(b['declared_sections'])}")
        return 0

    wanted = list(args.batch or [])
    if args.pilot:
        wanted = [n for n in batches if n in ("Tuner Availability", "Tune")]
    if not wanted:
        raise ContextError("give --batch NAME (repeatable), --pilot, or --list")

    stla_path = root / "data" / "stla_to_cfts.json"
    if not stla_path.exists():
        raise ContextError("data/stla_to_cfts.json missing — run "
                           "build_stla_map.py first")
    stla_map = json.loads(stla_path.read_text(encoding="utf-8"))
    ex_path = root / "data" / "exemplars.json"
    exemplars = (json.loads(ex_path.read_text(encoding="utf-8"))
                 if ex_path.exists() else {})
    if not exemplars:
        print("WARNING: no data/exemplars.json — generating without style "
              "anchors", file=sys.stderr)
    sections = section_texts(resolve_path(cfg, "cfts_doc"))
    spec_docs = cfg.get("spec_docs") or {}

    out_dir = root / "batches"
    out_dir.mkdir(exist_ok=True)
    for name in wanted:
        if name not in batches:
            raise ContextError(f"unknown batch {name!r}; --list to see them")
        ctx = build(cfg, batches[name], stla_map, sections, exemplars, spec_docs)
        slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
        path = out_dir / f"{slug}.json"
        path.write_text(json.dumps(ctx, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        chars = sum(len(s["text"]) for s in ctx["spec_sections"].values())
        diverged = [l["req_id"] for l in ctx["leaves"] if "wording_note" in l]
        if diverged:
            print(f"  037 title diverges from the CFTS clause: {diverged} "
                  "(§8.6 — spec wins on wording)", file=sys.stderr)
        print(f"{name:22} {len(ctx['leaves'])} leaves, "
              f"{len(ctx['spec_sections'])} sections ({chars} chars), "
              f"{len(ctx['siblings'])} siblings, "
              f"{len(ctx['exemplars'])} exemplars"
              + (f", {len(ctx['blocked_section_text'])} without section text"
                 if ctx["blocked_section_text"] else "")
              + f" -> {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--feature-dir", default=".")
    ap.add_argument("--batches-md", default="docs/batches-amfm.md")
    ap.add_argument("--batch", action="append", help="batch name (repeatable)")
    ap.add_argument("--pilot", action="store_true",
                    help="the pilot pair proposed in batches-amfm.md")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    try:
        return run(args)
    except ContextError as exc:
        print(f"ABORTED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
