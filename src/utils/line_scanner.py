"""Shared helpers for scanning a document's front-matter pages
(cover/title pages) for simple keyword-based metadata fields such as
author, university, and department.

These are intentionally simple, line-based heuristics for this phase.
They will be replaced/extended by smarter extraction once a dedicated
extraction layer is built.
"""

from typing import List, Optional, Sequence

# Characters that count as a valid "boundary" right after a marker
# word, so that e.g. "Authors" does not falsely match the marker
# "author", and "Byzantine" does not falsely match the marker "by".
_BOUNDARY_CHARS = " :\t-–—"


def get_clean_lines(text: str) -> List[str]:
    """Splits page text into non-empty, whitespace-trimmed lines."""
    return [line.strip() for line in text.splitlines() if line.strip()]


def get_front_matter_page_limit(document, default: int = 5) -> int:
    """Returns how many of the document's first pages should be
    scanned for front-matter fields (author, university, department).

    If a Table of Contents or Abstract section has already been
    detected (this must run after TocDetector/AbstractDetector in the
    pipeline), front matter is assumed to end right before the
    earliest of those. Otherwise, a fixed default page count is used.
    """
    boundary_types = {"toc", "abstract"}

    boundary_pages = [
        section.start_page
        for section in document.sections
        if section.section_type in boundary_types
    ]

    if boundary_pages:
        return max(1, min(boundary_pages) - 1)

    return default


def find_value_after_marker_line(
    lines: Sequence[str], markers: Sequence[str]
) -> Optional[str]:
    """Looks for a line that starts with one of the given markers
    (e.g. "by", "إعداد", "الطالب"), optionally followed by ":" and a
    value on the same line (e.g. "By: John Smith").

    A marker only counts as a match if it is followed by a real word
    boundary (space, colon, dash, or end of line) — this prevents
    unrelated words that merely start with the same letters from
    matching, such as "Authors" matching the marker "author", or
    "Byzantine" matching the marker "by".

    If the marker is found but there is no value left on that same
    line (e.g. the line is just "by"), the next non-empty line is
    used as the value instead.
    """
    for index, line in enumerate(lines):
        stripped = line.strip()
        lowered = stripped.lower()

        for marker in markers:
            marker_lower = marker.lower()

            if not lowered.startswith(marker_lower):
                continue

            next_char = stripped[len(marker) : len(marker) + 1]

            if next_char and next_char not in _BOUNDARY_CHARS:
                continue

            remainder = stripped[len(marker) :].strip(_BOUNDARY_CHARS + "\t")

            if remainder:
                return remainder

            if index + 1 < len(lines):
                return lines[index + 1]

    return None


def find_line_containing_near_start(
    lines: Sequence[str], keywords: Sequence[str], max_offset: int = 15
) -> Optional[str]:
    """Returns the first line where one of the given keywords appears
    at or near the START of the line (within `max_offset` characters).

    Restricting matches to near the start of the line filters out
    keywords that only appear incidentally inside a longer sentence —
    for example "...or position of the Department of Defense..." (a
    legal disclaimer) should NOT be mistaken for an actual department
    name, while a standalone line like "Department of Computer
    Science" or "Chairman, Department of Information Sciences"
    (keyword near the start) should match.
    """
    for line in lines:
        lowered = line.lower()

        for keyword in keywords:
            index = lowered.find(keyword.lower())

            if index != -1 and index <= max_offset:
                return line

    return None