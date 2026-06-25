"""Stage 1 — Domain Knowledge Pack (PIPELINE_DESIGN § Stage 1).

A persisted, human-reviewed-once artifact that carries the stable domain
background (glossary, feature behaviour, cross-feature interactions, boundaries,
traceability hints, open questions) into Stage 3/4/6, so the model doesn't
re-derive (and re-err on) it for every TC.

Pure data + IO + a context renderer. No AI here — the pack is *produced* by an
interactive agent reading specs, then verified at Gate (1), then *consumed* by
downstream stages via `to_prompt_block`.
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field

# Sections every downstream stage may consume. Each is a list of plain dicts so
# the pack round-trips as JSON with zero custom (de)serialization.
SECTIONS = (
    "glossary",            # {term, definition}
    "feature_model",       # {feature, normal, abnormal, boundary}
    "interactions",        # {features:[...], rule}
    "boundaries",          # {name, enum:[...] | min/max, source}
    "traceability_hints",  # {req, spec_ref}
    "open_questions",      # {question, context, status}
)


@dataclass
class DomainPack:
    project: str = ""
    glossary: list[dict] = field(default_factory=list)
    feature_model: list[dict] = field(default_factory=list)
    interactions: list[dict] = field(default_factory=list)
    boundaries: list[dict] = field(default_factory=list)
    traceability_hints: list[dict] = field(default_factory=list)
    open_questions: list[dict] = field(default_factory=list)
    reviewed_at: str | None = None   # Gate (1) human sign-off (ISO timestamp)


def load_domain_pack(path: str) -> DomainPack:
    if not os.path.isfile(path):
        return DomainPack()
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return DomainPack(
        project=data.get("project", ""),
        reviewed_at=data.get("reviewed_at"),
        **{s: list(data.get(s, [])) for s in SECTIONS},
    )


def save_domain_pack(pack: DomainPack, path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(asdict(pack), fh, ensure_ascii=False, indent=2)


def validate(pack: DomainPack) -> list[str]:
    """Return human-facing warnings for Gate (1). Empty list == clean."""
    warnings: list[str] = []
    if not pack.project:
        warnings.append("project 未填")
    if not pack.glossary and not pack.feature_model:
        warnings.append("glossary 與 feature_model 皆空 — pack 無實質內容")
    unresolved = [q for q in pack.open_questions
                  if str(q.get("status", "open")).lower() == "open"]
    if unresolved:
        warnings.append(f"{len(unresolved)} 個 open_question 未解決(Gate ① 需確認)")
    if not pack.reviewed_at:
        warnings.append("尚未經 Gate ① 人工簽核(reviewed_at 為空)")
    return warnings


def _render_items(title: str, items: list[dict], keys: list[str]) -> list[str]:
    if not items:
        return []
    lines = [f"## {title}"]
    for it in items:
        parts = [f"{k}: {it[k]}" for k in keys if it.get(k)]
        if parts:
            lines.append("- " + " | ".join(parts))
    return lines


def to_prompt_block(pack: DomainPack, req_id: str | None = None) -> str:
    """Render the pack as a compact context block for Stage 3/4/6 prompts.

    Global sections (glossary / feature_model / interactions / boundaries) are
    always included; traceability_hints are filtered to `req_id` when given.
    """
    out: list[str] = [f"# Domain Pack — {pack.project or '(unnamed)'}"]
    out += _render_items("Glossary", pack.glossary, ["term", "definition"])
    out += _render_items("Feature behaviour", pack.feature_model,
                         ["feature", "normal", "abnormal", "boundary"])
    out += _render_items("Cross-feature interactions", pack.interactions,
                         ["features", "rule"])
    out += _render_items("Boundaries / enumerations", pack.boundaries,
                         ["name", "enum", "min", "max", "source"])
    hints = pack.traceability_hints
    if req_id is not None:
        hints = [h for h in hints if h.get("req") == req_id]
    out += _render_items("Traceability hints", hints, ["req", "spec_ref"])
    return "\n".join(out).strip()
