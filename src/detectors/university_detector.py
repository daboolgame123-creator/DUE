from core.interfaces.detector import Detector
from core.models.document import Document
from knowledge.keywords import UNIVERSITY_KEYWORDS
from utils.line_scanner import (
    find_line_containing_near_start,
    get_clean_lines,
    get_front_matter_page_limit,
)


class UniversityDetector(Detector):
    """Detects the university name from the document's front-matter pages.

    Simplified rule for this phase: returns the first line in the
    front-matter pages where a keyword such as "University" or
    "جامعة" appears near the start of the line. Requiring the keyword
    to be near the start (rather than anywhere in the line) avoids
    matching incidental mentions inside longer sentences, such as a
    bio line like "B.S., Carnegie Mellon University, 2003".

    Note: some institutions (e.g. military academies, "X Institute
    of Technology") do not use the word "University" at all, and will
    not be detected by this simplified rule.

    Must run after TocDetector/AbstractDetector in the pipeline so it
    can benefit from their detected page boundaries.
    """

    def detect(self, document: Document) -> None:
        page_limit = get_front_matter_page_limit(document)

        for page in document.pages[:page_limit]:
            lines = get_clean_lines(page.text)
            value = find_line_containing_near_start(lines, UNIVERSITY_KEYWORDS)

            if value:
                document.metadata.university = value
                return