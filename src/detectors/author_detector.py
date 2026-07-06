from core.interfaces.detector import Detector
from core.models.document import Document
from knowledge.keywords import AUTHOR_MARKERS
from utils.line_scanner import (
    find_value_after_marker_line,
    get_clean_lines,
    get_front_matter_page_limit,
)


class AuthorDetector(Detector):
    """Detects the document's author name from its front-matter pages.

    Simplified rule for this phase: scans the front-matter pages
    (before the first detected TOC/Abstract section, or the first 5
    pages by default) for a marker such as "by" or "إعداد:", and
    takes the value on the same line or the line right after it.

    Must run after TocDetector/AbstractDetector in the pipeline so it
    can benefit from their detected page boundaries.
    """

    def detect(self, document: Document) -> None:
        page_limit = get_front_matter_page_limit(document)

        for page in document.pages[:page_limit]:
            lines = get_clean_lines(page.text)
            value = find_value_after_marker_line(lines, AUTHOR_MARKERS)

            if value:
                document.metadata.author = value
                return