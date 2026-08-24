#!/usr/bin/env python3
"""Assemble the generation context package for one Home HMI batch or parent.

Gathers everything the TC generator needs into one JSON:
  - the target leaf requirements (id / title / description / section)
  - sibling rows, done ones included (docs.md §4.6 sibling awareness)
  - spec section text from the SYS1 outline, plus parent and unallocated
    descendant sections
  - spec page PNG paths to Read as images
  - Pop Up List entries for any PUxxxx cited in the gathered spec text
  - exemplar TCs for the batch's spec chapter, with fallback

Home differs from Media in two ways:
  - Test Group / Test Set stay BLANK (RUNBOOK §5). They are emitted as "" and
    a `column_conventions` block spells that out, so the generator cannot
    quietly invent values.
  - Exemplars are keyed by spec chapter, not Test Set. Only HSD / HSS / HS
    exist in the done region, so SNS / BSP / SW batches fall back to HSS —
    the fallback used is reported, never silent.

Batch membership is read from `docs/batches-home.md`, which stays the single
source of truth for the B1–B7 split.

The Pop Up List path and the spec_reference template come from
`feature.yaml`; --popup overrides the path.

Usage:
    python make_batch_context.py --batch B1
    python make_batch_context.py --parent SWE1-HMI-HOME-048 --data data/
    python make_batch_context.py --list
"""
import argparse
import json
import re
from pathlib import Path

from feature_config import load_feature_config, resolve_path

PU_RE = re.compile(r"\bPU\d{3,4}\b")
CHAPTER_RE = re.compile(r"^([A-Z]{2,4})")
REQ_PREFIX = "SWE1-HMI-HOME-"
HOME_SPEC_PREFIX = "Home Screen HMI Logic and Flow"
LAST_MODE_PREFIX = "Last Mode Table HMI Logic and Flow"
# A-H03 ruling: cite the file that exists, not 037's `R1L-R` release label.
LAST_MODE_SPEC_REFERENCE = (
    "Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021)_{n}")
# Chapters present in the done region, best first. SNS/BSP/SW have no
# exemplars of their own — Arif never wrote those chapters.
EXEMPLAR_FALLBACK = ["HSS", "HSD", "HS"]

BATCH_ROW_RE = re.compile(
    r"^\|\s*(B\d)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|")
ANOMALY_RE = re.compile(r"\bA-H\d{2}\b")


def load_batches(md_path: Path) -> dict:
    """{batch: {theme, count, req_ids, context_note, anomalies}}."""
    if not md_path.exists():
        raise SystemExit(f"missing {md_path}")
    batches = {}
    for line in md_path.read_text(encoding="utf-8").splitlines():
        m = BATCH_ROW_RE.match(line)
        if not m:
            continue
        bid, theme, count, ids, note = m.groups()
        req_ids = [REQ_PREFIX + s.strip() for s in ids.split(",") if s.strip()]
        if len(req_ids) != int(count):
            raise SystemExit(
                f"{bid}: table says {count} leaves but lists {len(req_ids)}")
        batches[bid] = {
            "theme": theme,
            "req_ids": req_ids,
            "context_note": note,
            "anomalies": sorted(set(ANOMALY_RE.findall(note))),
        }
    if not batches:
        raise SystemExit(f"no batch rows parsed from {md_path}")
    return batches


def load_outline_to_chapter(tsv_path: Path) -> dict:
    mapping = {}
    for line in tsv_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or line.startswith("spec_id\t"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        m = CHAPTER_RE.match(parts[0])
        if m:
            mapping[parts[1]] = m.group(1)
    return mapping


def chapter_of(outline: str, outline_to_chapter: dict) -> str:
    if outline in outline_to_chapter:
        return outline_to_chapter[outline]
    parts = outline.split(".")
    for cut in range(len(parts) - 1, 0, -1):
        parent = ".".join(parts[:cut])
        if parent in outline_to_chapter:
            return outline_to_chapter[parent]
    return "?"


def load_popup_index(popup_path: str) -> dict:
    """PUxxxx -> the Pop Up List row, verbatim. Never paraphrase downstream."""
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
            "category": str(r[5] or ""),
            "string_popup_message": str(r[6] or ""),
            "reference_documentation": str(r[11] or "") if len(r) > 11 else "",
        }
    wb.close()
    return idx


def gather_sections(leaves: list, manifest: dict, all_leaf_sections: set) -> tuple:
    """Return (sections, pages) for the given leaves.

    Only leaves sourced from the Home Screen spec resolve: 037's `_{n}` suffix
    is an outline number for Home Screen but a Last Mode Table List Item number
    for B7. Those namespaces collide (`_1`, `_35`), so resolving B7 against the
    Home manifest would inject a completely unrelated spec section.
    """
    sections, pages = {}, set()
    for leaf in leaves:
        if not leaf.get("hmi_source_id", "").startswith(HOME_SPEC_PREFIX):
            continue
        sec = leaf.get("section") or ""
        if sec and sec in manifest:
            sections[sec] = manifest[sec]
            pages.update(manifest[sec]["pages"])
        if "." in sec:
            parent_sec = sec.rsplit(".", 1)[0]
            if parent_sec in manifest:
                sections.setdefault(parent_sec, manifest[parent_sec])
                pages.update(manifest[parent_sec]["pages"])
                # The chapter's figure lives in an image-only sibling row
                # ("Please refer to the diagram") that no leaf owns — it is
                # what carries the LSW/SW/SNS layout tables.
                for sib in sorted(k for k in manifest
                                  if k.startswith(f"{parent_sec}.")
                                  and k not in all_leaf_sections
                                  and manifest[k]["text"].startswith(
                                      "Please refer to the")):
                    sections.setdefault(sib, manifest[sib])
                    pages.update(manifest[sib]["pages"])
        # 037 does not allocate a leaf to every SYS1 sub-section. Pull in the
        # unallocated descendants — without them the parent generates blind.
        for child in sorted(k for k in manifest
                            if sec and k.startswith(f"{sec}.")
                            and k not in all_leaf_sections):
            sections.setdefault(child, manifest[child])
            pages.update(manifest[child]["pages"])
    return sections, sorted(pages)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", help="batch id from docs/batches-home.md, e.g. B1")
    ap.add_argument("--parent", help="single parent req id")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--data", default="data")
    ap.add_argument("--feature-dir", default=".")
    ap.add_argument("--batches-md", default="docs/batches-home.md")
    ap.add_argument("--popup", help="override feature.yaml paths.popup_list")
    ap.add_argument("--per-chapter", type=int, default=3,
                    help="max exemplars to embed")
    ap.add_argument("--out", help="output json (default: batches/<id>.json)")
    args = ap.parse_args()

    cfg = load_feature_config(args.feature_dir)
    data = Path(args.data)
    remaining = json.loads((data / "remaining_leaves.json").read_text())
    sibling_map = json.loads((data / "sibling_map.json").read_text())
    batches = load_batches(Path(args.batches_md))

    if args.list:
        for bid, b in batches.items():
            print(f"{bid}  {len(b['req_ids']):>2} leaves  {b['theme']}"
                  + (f"   [{', '.join(b['anomalies'])}]" if b["anomalies"] else ""))
        return

    if not (args.batch or args.parent):
        ap.error("--batch, --parent or --list required")

    by_id = {x["req_id"]: x for x in remaining}
    if args.batch:
        if args.batch not in batches:
            raise SystemExit(f"unknown batch {args.batch}; "
                             f"have {', '.join(batches)}")
        spec = batches[args.batch]
        missing = [r for r in spec["req_ids"] if r not in by_id]
        if missing:
            raise SystemExit(
                f"{args.batch}: not in remaining_leaves.json: {missing}\n"
                "either the batch table or the done-region detection is stale")
        leaves = [by_id[r] for r in spec["req_ids"]]
        target, theme = args.batch, spec["theme"]
        anomalies = spec["anomalies"]
    else:
        leaves = [x for x in remaining if x["parent"] == args.parent]
        if not leaves:
            raise SystemExit(f"no remaining leaves under {args.parent}")
        target, theme, anomalies = args.parent, "", []

    manifest = json.loads((data / "section_manifest.json").read_text())
    exemplars = json.loads((data / "exemplars.json").read_text())
    outline_to_chapter = load_outline_to_chapter(data / "spec_id_to_outline.tsv")

    all_leaf_sections = {x["section"] for x in remaining if x.get("section")}
    sections, pages = gather_sections(leaves, manifest, all_leaf_sections)

    home_leaves = [l for l in leaves
                   if l.get("hmi_source_id", "").startswith(HOME_SPEC_PREFIX)]
    foreign = sorted({l["hmi_source_id"].rsplit("_", 1)[0]
                      for l in leaves if l not in home_leaves})
    unresolved = [l["req_id"] for l in home_leaves
                  if not l.get("section") or l["section"] not in manifest]
    chapters = sorted({chapter_of(l["section"], outline_to_chapter)
                       for l in home_leaves if l.get("section")})

    ex, ex_source = [], ""
    for ch in chapters + EXEMPLAR_FALLBACK:
        if exemplars.get(ch):
            ex, ex_source = exemplars[ch], ch
            break

    pu_ids = sorted({m for s in sections.values() for m in PU_RE.findall(s["text"])})
    popups = {}
    if pu_ids:
        pu_index = load_popup_index(resolve_path(cfg, "popup_list", args.popup))
        popups = {pid: pu_index.get(pid, "NOT FOUND IN POP UP LIST")
                  for pid in pu_ids}

    ctx = {
        "target": target,
        "theme": theme,
        "applicable_anomalies": anomalies,
        "column_conventions": {
            "test_group": "",
            "test_set": "",
            "note": "Test Group (G) and Test Set (H) are BLANK throughout the "
                    "done region — leave them blank. Author (Z) = PeiPYHsu, "
                    "Test Case Reference ID (O) = NEW, Functional Safety (R) = "
                    "NA, Remarks = column AG.",
            "spec_reference_format": cfg["spec_reference_template"],
        },
        "requirements": leaves,
        "siblings": {p: sibling_map[p] for p in
                     sorted({l["parent"] for l in leaves}) if p in sibling_map},
        "spec_sections": sections,
        "spec_page_images": [f"spec_pages/page_{p:02d}.png" for p in pages],
        "popup_refs": popups,
        "exemplar_chapter": ex_source,
        "exemplar_is_fallback": ex_source not in chapters,
        "exemplars": ex[:args.per_chapter],
        "fingerprint": _fingerprint("features/home"),
    }
    if unresolved:
        ctx["unresolved_sections"] = unresolved
    if foreign:
        ctx["external_spec_leaves"] = {
            "specs": foreign,
            "req_ids": [l["req_id"] for l in leaves if l not in home_leaves],
            "note": "These leaves trace to a spec other than the Home Screen "
                    "L&F; no Home spec text was injected for them.",
        }

    # Last Mode leaves carry their spec content in a separate table keyed by
    # List Item number (A-H03), so resolve it here rather than leaving B7
    # with requirement titles and nothing else.
    lm_leaves = [l for l in leaves
                 if l.get("hmi_source_id", "").startswith(LAST_MODE_PREFIX)]
    if lm_leaves:
        lm_path = data / "last_mode_items.json"
        if not lm_path.exists():
            raise SystemExit(f"{target} needs {lm_path}; "
                             "run build_last_mode.py first")
        lm_items = json.loads(lm_path.read_text())
        resolved, unresolved_lm = {}, []
        for leaf in lm_leaves:
            n = leaf.get("section") or ""
            if n in lm_items:
                resolved[leaf["req_id"]] = dict(lm_items[n], list_item=n)
            else:
                unresolved_lm.append(leaf["req_id"])
        if unresolved_lm:
            raise SystemExit(
                f"{target}: Last Mode List Items unresolved for "
                f"{unresolved_lm} — do not generate against a missing item")
        ctx["last_mode_items"] = resolved
        ctx["column_conventions"]["spec_reference_format_last_mode"] = \
            LAST_MODE_SPEC_REFERENCE
        lm_note = f"{len(resolved)}/{len(lm_leaves)} Last Mode List Items resolved"
    else:
        lm_note = ""

    out = Path(args.out) if args.out else Path("batches") / f"{target}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ctx, ensure_ascii=False, indent=2))

    print(f"{target}: {len(leaves)} leaves, {len(sections)} sections, "
          f"{len(pages)} page images, {len(pu_ids)} PU refs -> {out}")
    print(f"  chapters={chapters}  exemplars from {ex_source!r}"
          + ("  (FALLBACK — no exemplar exists for this chapter)"
             if ctx["exemplar_is_fallback"] else ""))
    if lm_note:
        print(f"  {lm_note}")
    if anomalies:
        print(f"  applicable anomalies: {', '.join(anomalies)}")
    if unresolved:
        print(f"  UNRESOLVED sections for: {unresolved}")
    if foreign:
        print(f"  {len(leaves) - len(home_leaves)} leaves trace to an external "
              f"spec, no Home text injected: {foreign}")



# --- R-G19：prompt／exemplar 指紋（26 包 §D-5）------------------------------

def _fingerprint(feature_dir: str) -> dict:
    """本批實際使用之 prompt 模板與 exemplar 集之 sha（R-G19@`bd206972`）。

    指紋之計算集中於 `scripts/prompt_fingerprint.py`，各 feature 只呼叫。
    **取不到時回 `{"error": ...}` 而非省略該鍵** —— 少一個鍵與指紋相符
    在 manifest 上長得不一樣，而少一個鍵與「沒有指紋」長得一樣（G-D）。
    """
    import importlib.util
    root = Path(__file__).resolve().parents[3]
    spec = importlib.util.spec_from_file_location(
        "tc_prompt_fingerprint", root / "scripts" / "prompt_fingerprint.py")
    if spec is None or spec.loader is None:
        return {"error": "scripts/prompt_fingerprint.py 不可載入"}
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.fingerprint(root, feature_dir)

if __name__ == "__main__":
    main()
