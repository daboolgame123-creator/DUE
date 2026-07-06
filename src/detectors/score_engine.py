from core.models.detection_candidate import DetectionCandidate
from core.models.text_block import TextBlock


class ScoreEngine:
    """Scores candidate blocks."""

    def score_title(
        self,
        block: TextBlock,
        page_number: int,
        block_index: int,
    ) -> DetectionCandidate:

        score = 0.0

        f = block.features

        if block.block_type == "title":
            score += 0.40

        if f.is_first_block:
            score += 0.15

        if f.region == "body":
            score += 0.10

        if f.max_font_size >= 16:
            score += 0.15

        if f.word_count <= 20:
            score += 0.10

        if f.column == 1:
            score += 0.05

        if f.reading_order == 0:
            score += 0.05

        return DetectionCandidate(
            value=block.text.strip(),
            confidence=min(score, 1.0),
            detector="TitleDetector",
            page=page_number,
            block_index=block_index,
        )