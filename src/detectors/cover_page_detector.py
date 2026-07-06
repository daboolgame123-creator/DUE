from core.interfaces.detector import Detector
from core.models.document import Document
from core.models.section import Section


class CoverPageDetector(Detector):
    """Detects the cover page of a document.

    Simplified rule for this phase: the first page of the document
    is always treated as the cover page. This will be replaced with a
    smarter rule (layout/visual analysis) in a later phase.
    """

    def detect(self, document: Document) -> None:
        if not document.pages:
            return

        document.sections.append(
            Section(
                section_type="cover",
                start_page=1,
                end_page=1,
                confidence=1.0,
            )
        )
