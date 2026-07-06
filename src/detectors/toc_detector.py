from core.interfaces.detector import Detector
from core.models.document import Document


class TocDetector(Detector):
    """Detects the document title using layout information."""

    MAX_PAGES = 3

    def detect(self, document: Document) -> None:

        best_block = None
        best_score = -1

        for page in document.pages[: self.MAX_PAGES]:

            for block in page.text_blocks:

                score = self._score(block)

                if score > best_score:
                    best_score = score
                    best_block = block

        if best_block:
            document.metadata.title = self._clean(best_block.text)

    def _score(self, block) -> float:

        score = 0.0

        f = block.features

        if block.block_type == "title":
            score += 60

        if f.is_first_block:
            score += 20

        if getattr(f, "region", "") == "body":
            score += 5

        if f.word_count <= 20:
            score += 5

        if f.max_font_size >= 16:
            score += 5

        if getattr(f, "reading_order", 999) == 0:
            score += 5

        return score

    def _clean(self, text: str) -> str:

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if len(line) < 2:
                continue

            lines.append(line)

        return " ".join(lines)