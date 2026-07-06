from detectors.score_engine import ScoreEngine

from core.interfaces.detector import Detector
from core.models.document import Document


class TitleDetector(Detector):
    """Detects the document title."""

    def __init__(self) -> None:
        self._engine = ScoreEngine()

    def detect(self, document: Document) -> None:

        best = None

        for page in document.pages[:3]:

            for index, block in enumerate(page.text_blocks):

                candidate = self._engine.score_title(
                    block,
                    page.number,
                    index,
                )

                if not candidate.value:
                    continue

                if best is None:

                    best = candidate

                elif candidate.confidence > best.confidence:

                    best = candidate

        if best:

            document.metadata.title = best.value