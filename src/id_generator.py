"""TC ID generator (RULES.md §2.1, §2.2)."""
import re


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

    # Multiple words: first letter of each + last letter of last word
    abbr = "".join(w[0] for w in words)
    if len(abbr) < 3:
        # Pad with last chars from last word
        last_word = words[-1]
        abbr += last_word[-1]

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
    return [
        f"{project}-{group_abbr}-{str(start + i).zfill(3)}"
        for i in range(count)
    ]
