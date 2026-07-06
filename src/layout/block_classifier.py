from core.models.page import Page
from core.models.text_block import TextBlock


class BlockClassifier:
    """Classifies text blocks according to their visual features."""

    def classify(self, page: Page) -> None:

        if not page.text_blocks:
            return

        max_font = max(
            (
                block.features.max_font_size
                for block in page.text_blocks
            ),
            default=0,
        )

        for block in page.text_blocks:

            block.block_type = self._classify(
                block,
                max_font,
                page,
            )

    def _classify(
        self,
        block: TextBlock,
        page_max_font: float,
        page: Page,
    ) -> str:

        features = block.features

        text = block.text.strip()

        if not text:
            return "empty"

        if features.region == "header":
            return "header"

        if features.region == "footer":

            if text.isdigit():
                return "page_number"

            return "footer"

        if (
            features.max_font_size >= page_max_font * 0.95
            and features.word_count <= 20
            and features.is_first_block
        ):  
            features.column = 1
            return "title"

        if (
            features.bold_spans > 0
            and features.word_count <= 15
        ):
            return "heading"

        if (
            features.word_count <= 12
            and text.lower().startswith(("figure", "fig"))
        ):
            return "caption"

        if (
            features.word_count <= 12
            and text.startswith("شكل")
        ):
            return "caption"

        if (
            features.word_count <= 12
            and text.startswith("جدول")
        ):
            return "caption"

        return "paragraph"