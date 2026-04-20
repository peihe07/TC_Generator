"""TC ID generator (RULES.md §2.1, §2.2)."""
import re


_NON_ALNUM = re.compile(r"[^A-Za-z0-9]+")


def sanitize_id_segment(raw: str) -> str:
    """
    Strip any non-alphanumeric characters so the value is safe to embed in
    a TC ID segment. Source documents sometimes contain spaces or slashes
    (e.g. "new R/L" in the Product Document sheet) — §2.1 requires each
    segment to match `[A-Za-z0-9]+`, so we collapse offending characters
    rather than let them leak into the ID.
    """
    return _NON_ALNUM.sub("", raw or "")


def normalize_tc_id(tc_id: str) -> str:
    """
    Clean an already-filled TC ID so it conforms to §2.1.

    Returns:
        - ""                              if the input is empty or the
                                          structure is too broken to rescue
                                          (caller should regenerate fresh)
        - "{project}-{abbr}-{NNN}"        otherwise, with each segment
                                          sanitized and the sequence
                                          zero-padded to 3 digits
    """
    if not tc_id:
        return ""
    parts = tc_id.split("-")
    if len(parts) != 3:
        return ""
    project = sanitize_id_segment(parts[0])
    abbr = sanitize_id_segment(parts[1])
    seq = sanitize_id_segment(parts[2])
    if not project or not abbr or not seq.isdigit():
        return ""
    return f"{project}-{abbr}-{seq.zfill(3)}"


def generate_group_abbreviation(group_name: str) -> str:
    """
    Generate abbreviation from Test Group name.

    Strategy: extract uppercase letters from CamelCase words,
    take first letter of each word. If result < 3 chars, pad from name.
    """
    # Split CamelCase into words
    words = re.findall(r"[A-Z][a-z]*|[A-Z]+(?=[A-Z]|$)", group_name)

    if not words:
        # Already all uppercase or single word
        return group_name[:3].upper()

    if len(words) == 1:
        # Single word: take first 3 chars
        return words[0][:3].upper()

    # Multiple words: first letter of each word.
    # No padding — a pure acronym like "BT" stays "BT" instead of becoming
    # "BTT" (the old logic would duplicate the last letter).
    abbr = "".join(w[0] for w in words)
    return abbr[:3].upper()


def generate_tc_ids(
    project: str,
    group_abbr: str,
    count: int,
    start: int = 1,
) -> list[str]:
    """
    Generate TC IDs in format: {project}-{group_abbr}-{sequence}.

    Args:
        project: Project name (e.g. 'newR1L')
        group_abbr: Group abbreviation (e.g. 'DMS')
        count: Number of IDs to generate
        start: Starting sequence number (default 1)

    Returns:
        List of TC ID strings
    """
    safe_project = sanitize_id_segment(project)
    safe_group = sanitize_id_segment(group_abbr)
    if not safe_project:
        raise ValueError(f"project has no alphanumeric characters: {project!r}")
    if not safe_group:
        raise ValueError(f"group_abbr has no alphanumeric characters: {group_abbr!r}")
    return [
        f"{safe_project}-{safe_group}-{str(start + i).zfill(3)}"
        for i in range(count)
    ]
