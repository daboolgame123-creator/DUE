from core.interfaces.detector import Detector
from core.models.document import Document
from core.models.section import Section
from knowledge.keywords import ABSTRACT_KEYWORDS


class AbstractDetector(Detector):
    """Detects the abstract section of a document.

    Simplified rule for this phase: scans each page's first few lines
    for a bilingual (Arabic/English) keyword such as "الملخص" or
    "Abstract". The first matching page is treated as the abstract
    page, and its remaining text is stored as the abstract content.

    Note: this detector also fills `metadata.abstract` directly, the
    same way `TitleDetector` fills `metadata.title`. Once a dedicated
    extraction layer exists, this responsibility should move there.
    """

    HEADER_LINES_TO_CHECK = 3

    def detect(self, document: Document) -> None:
        for page in document.pages:
            lines = [line.strip() for line in page.text.splitlines() if line.strip()]

            if not lines:
                continue

            header_lines = lines[: self.HEADER_LINES_TO_CHECK]

            matched = any(
                keyword.lower() in line.lower()
                for line in header_lines
                for keyword in ABSTRACT_KEYWORDS
            )

            if not matched:
                continue

            document.sections.append(
                Section(
                    section_type="abstract",
                    start_page=page.number,
                    end_page=page.number,
                    confidence=0.7,
                )
            )

            abstract_text = "\n".join(lines[1:]).strip()
            document.metadata.abstract = abstract_text or None

            return
