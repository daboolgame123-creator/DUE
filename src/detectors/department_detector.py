from core.interfaces.detector import Detector
from core.models.document import Document
from knowledge.keywords import DEPARTMENT_KEYWORDS
from utils.line_scanner import (
    find_line_containing_near_start,
    get_clean_lines,
    get_front_matter_page_limit,
)


class DepartmentDetector(Detector):
    """Detects the department name from the document's front-matter pages.

    Simplified rule for this phase: returns the first line in the
    front-matter pages where a keyword such as "Department of" or
    "قسم" appears near the start of the line. Requiring the keyword
    to be near the start (rather than anywhere in the line) avoids
    matching incidental mentions inside longer sentences, such as a
    legal disclaimer like "...or position of the Department of
    Defense or the U.S. Government."

    Must run after TocDetector/AbstractDetector in the pipeline so it
    can benefit from their detected page boundaries.
    """

    def detect(self, document: Document) -> None:
        page_limit = get_front_matter_page_limit(document)

        for page in document.pages[:page_limit]:
            lines = get_clean_lines(page.text)
            value = find_line_containing_near_start(lines, DEPARTMENT_KEYWORDS)

            if value:
                document.metadata.department = value
                return