#!/usr/bin/env python3
"""Assemble the generation context package for one RD parent.

Given a parent ID (e.g. SWE1-MEDIA-PLA-063), gather everything the TC
generator needs into one JSON:
  - the parent's remaining leaf requirements (id / title / description)
  - sibling rows (done + remaining, for docs.md §4.6 sibling awareness)
  - spec section text (from SYS1 outline) for every referenced section
  - spec page PNG paths to Read as images
  - Pop Up List entries for any PUxxxx cited in the spec text
  - Test Set assignment (from section_to_testset.json)
  - exemplar TCs of the target Test Set

Usage:
    python make_batch_context.py --parent SWE1-MEDIA-PLA-063 --data data/ \
        --popup <PopUpList.xlsx>
    python make_batch_context.py --list --data data/     # list all parents
"""
import argparse
import json
import re
from pathlib import Path

PU_RE = re.compile(r"\bPU\d{3,4}\b")


def load_popup_index(popup_path: str) -> dict:
    """PUxxxx -> {message, description, timeout, exit_conditions}."""
    import openpyxl
    wb = openpyxl.load_workbook(popup_path, read_only=True)
    ws = wb["Main"]
    idx = {}
    for r in ws.iter_rows(min_row=3, values_only=True):
        pid = str(r[0] or "").strip()
        if not pid.startswith("PU"):
            continue
        idx[pid] = {
            "module": str(r[1] or ""),
            "timeout_sec": str(r[2] or ""),
            "exit_conditions": str(r[3] or ""),
            "description": str(r[4] or ""),
            "string_popup_message": str(r[6] or ""),
        }
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--data", default="data")
    ap.add_argument("--popup", help="Pop Up List xlsx (optional but recommended)")
    ap.add_argument("--out", help="output json path (default: batches/<parent>.json)")
    args = ap.parse_args()

    data = Path(args.data)
    remaining = json.loads((data / "remaining_leaves.json").read_text())
    sibling_map = json.loads((data / "sibling_map.json").read_text())

    if args.list:
        for p, subs in sibling_map.items():
            n = sum(1 for s in subs if s["remaining"])
            print(f"{p}  remaining={n}/{len(subs)}")
        return

    if not args.parent:
        ap.error("--parent or --list required")

    leaves = [x for x in remaining if x["parent"] == args.parent]
    if not leaves:
        raise SystemExit(f"no remaining leaves under {args.parent}")

    manifest = json.loads((data / "section_manifest.json").read_text())
    sec2set = json.loads((data / "section_to_testset.json").read_text())
    exemplars = json.loads((data / "exemplars.json").read_text())

    # sections owned by ANY remaining leaf — a descendant that is itself a leaf
    # belongs to its own parent's batch and must not be pulled into this one.
    leaf_sections = {x["section"] for x in remaining if x.get("section")}

    sections, pages = {}, set()
    for leaf in leaves:
        sec = leaf["section"]
        if sec and sec in manifest:
            sections[sec] = manifest[sec]
            pages.update(manifest[sec]["pages"])
        # include parent section text for context (e.g. 11.3 for 11.3.1)
        parent_sec = sec.rsplit(".", 1)[0] if "." in sec else ""
        if parent_sec in manifest:
            sections.setdefault(parent_sec, manifest[parent_sec])
        # 037 does not allocate a leaf to every SYS1 sub-section: e.g. 11.3.1
        # ("label may change based on connected drive type") is a leaf, but the
        # concrete behaviour lives in the unallocated 11.3.1.1 / 11.3.1.1.1.
        # Pull those descendants in — without them the parent generates blind.
        for child in sorted(k for k in manifest
                            if k.startswith(f"{sec}.") and k not in leaf_sections):
            sections.setdefault(child, manifest[child])
            pages.update(manifest[child]["pages"])

    # Test Set: per-parent override first, then the chapter mapping
    chapters = sec2set.get("chapters", sec2set)
    overrides = sec2set.get("overrides", {})
    chapter = leaves[0]["section"].split(".")[0]
    if args.parent in overrides:
        test_set = overrides[args.parent]["test_set"]
    else:
        test_set = chapters.get(chapter, {}).get("test_set", "UNMAPPED")

    # Curated anchors win over done-region exemplars. Some Test Sets are badly
    # served by the done region (Browse Tab has ONE exemplar for 83 remaining
    # leaves); a reviewed TC from this run anchors style far better, because the
    # judgement calls it encodes are the ones the remaining leaves need.
    anchors = {}
    anchor_path = Path(__file__).resolve().parent.parent / "anchors.json"
    if anchor_path.exists():
        anchors = json.loads(anchor_path.read_text())
    ex = list(anchors.get(test_set, []))

    # exemplars: new Test Sets have no done-region examples -> fall back
    if not ex:
        ex = exemplars.get(test_set, [])
    if not ex:
        fb = chapters.get(chapter, {}).get("exemplar_fallback", "")
        ex = exemplars.get(fb, [])

    # PU references cited anywhere in the gathered spec text
    pu_ids = sorted({m for s in sections.values()
                     for m in PU_RE.findall(s["text"])})
    popups = {}
    if pu_ids and args.popup:
        pu_index = load_popup_index(args.popup)
        popups = {pid: pu_index.get(pid, "NOT FOUND IN POP UP LIST")
                  for pid in pu_ids}

    ctx = {
        "parent": args.parent,
        "test_group": "MediaHMI",
        "test_set": test_set,
        "requirements": leaves,
        "siblings": sibling_map.get(args.parent, []),
        "spec_sections": sections,
        "spec_page_images": [f"spec_pages/page_{p:02d}.png"
                             for p in sorted(pages)],
        "popup_refs": popups,
        "exemplars": ex[:2],
    }

    out = Path(args.out) if args.out else Path("batches") / f"{args.parent}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ctx, ensure_ascii=False, indent=2))
    print(f"{args.parent}: {len(leaves)} leaves, {len(sections)} sections, "
          f"{len(pages)} page images, {len(pu_ids)} PU refs, "
          f"test_set={test_set} -> {out}")


if __name__ == "__main__":
    main()
