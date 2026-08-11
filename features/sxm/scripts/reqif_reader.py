#!/usr/bin/env python3
"""Read a `.reqifz` export into `{clause id: {section, text, name, attrs}}`.

Why this exists: the docx path infers a clause's identity from typography —
a 7-digit number inside brackets at the head of a paragraph, and heading
anchors that must increase monotonically for the bracket lookup to be defined.
Every fragile case the AMFM and SXM corpora hit lives in that inference:
full-width brackets (A-AM01), a trailing `(add)` marker that defeats an
end-anchored pattern (A-SX01), and headings whose anchors would break the
ordering invariant.

The ReqIF export carries the same information as *attributes*:
`ReqIF.ForeignID` is the clause id, `ReqIF.Text` the requirement text, and the
SPEC-HIERARCHY gives the outline number. Nothing is parsed out of prose, so
none of those failure modes can occur.

This module only READS. Whether the ReqIF replaces the bracket map as the
source of record is a ruling, and the diff that informs it is produced by
`compare_reqif_to_bracket_map.py`.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def _fold_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def load_reqif(path: Path) -> dict[int, dict]:
    """{7-digit clause id: {section, text, name, attrs}} from a .reqifz.

    Only objects whose `ReqIF.ForeignID` is a 7-digit number are returned: the
    export also carries chapter rows and metadata objects, and giving them the
    same shape as requirements would let a heading masquerade as a clause.
    """
    with zipfile.ZipFile(path) as z:
        member = next(n for n in z.namelist() if n.lower().endswith(".reqif"))
        root = ET.fromstring(z.read(member))
    ns = re.match(r"\{(.*)\}", root.tag).group(1)
    q = lambda t: f"{{{ns}}}{t}"  # noqa: E731

    defs = {e.get("IDENTIFIER"): e.get("LONG-NAME")
            for e in root.iter() if e.tag.startswith(q("ATTRIBUTE-DEFINITION-"))}

    objects: dict[str, dict] = {}
    for so in root.iter(q("SPEC-OBJECT")):
        attrs: dict[str, str] = {}
        for av in so.iter():
            tag = av.tag.split("}")[-1]
            if not tag.startswith("ATTRIBUTE-VALUE-"):
                continue
            ref = next((r.text for r in av.iter() if r.tag.endswith("-REF")), None)
            name = defs.get(ref)
            if not name:
                continue
            if tag.endswith("XHTML"):
                holder = next((x for x in av if x.tag.endswith("THE-VALUE")), av)
                attrs[name] = _fold_ws("".join(holder.itertext()))
            else:
                attrs[name] = av.get("THE-VALUE") or ""
        objects[so.get("IDENTIFIER")] = attrs

    # Outline numbers come from the specification tree, not from any attribute.
    outline: dict[str, str] = {}

    def walk(children, prefix: str) -> None:
        n = 0
        for ch in children:
            if ch.tag != q("SPEC-HIERARCHY"):
                continue
            n += 1
            num = f"{prefix}{n}"
            ref = next((r.text for r in ch.iter() if r.tag == q("SPEC-OBJECT-REF")),
                       None)
            if ref:
                outline[ref] = num
            kids = next((k for k in ch if k.tag == q("CHILDREN")), None)
            if kids is not None:
                walk(kids, num + ".")

    for spec in root.iter(q("SPECIFICATION")):
        kids = next((k for k in spec if k.tag == q("CHILDREN")), None)
        if kids is not None:
            walk(kids, "")

    out: dict[int, dict] = {}
    for oid, attrs in objects.items():
        fid = str(attrs.get("ReqIF.ForeignID", "")).strip()
        if not re.fullmatch(r"\d{7}", fid):
            continue
        out[int(fid)] = {
            "section": outline.get(oid, ""),
            "text": attrs.get("ReqIF.Text", ""),
            "name": attrs.get("ReqIF.Name", ""),
            "attrs": attrs,
        }
    return out


def find_token(clauses: dict[int, dict], token: str) -> list[tuple[int, str, str]]:
    """Every field in which `token` appears as a whole value.

    Used for the short-id adjudication: a citation like `CFTS024-193` is only
    resolvable if `193` is somebody's identifier, so the search is over
    identifier-shaped attributes, matched whole — a substring hit inside
    requirement prose is not an identifier.
    """
    hits = []
    for cid, c in clauses.items():
        for field in ("ReqIF.ForeignID", "Source Id", "ReqIF.Name",
                      "Reference in Same Module", "Reference Specification"):
            v = str(c["attrs"].get(field, "")).strip()
            if v == token or token in [p.strip() for p in re.split(r"[,;]", v)]:
                hits.append((cid, field, v))
    return hits
