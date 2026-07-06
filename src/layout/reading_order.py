from core.models.page import Page
from core.models.text_block import TextBlock


class ReadingOrderEngine:
    """Computes the logical reading order of text blocks."""

    def order(self, page: Page, columns: int) -> list[TextBlock]:

        if columns <= 1:
            return self._single_column(page)

        if columns == 2:
            return self._two_columns(page)

        return self._single_column(page)

    def _single_column(self, page: Page) -> list[TextBlock]:

        blocks = sorted(
            page.text_blocks,
            key=lambda block: (
                block.bbox.y0,
                block.bbox.x0,
            ),
        )

        for index, block in enumerate(blocks):
            block.features.reading_order = index

        return blocks

    def _two_columns(self, page: Page) -> list[TextBlock]:

        middle = page.width / 2

        left = []
        right = []

        for block in page.text_blocks:

            center = (block.bbox.x0 + block.bbox.x1) / 2

            if center < middle:
                left.append(block)
            else:
                right.append(block)

        left.sort(key=lambda b: b.bbox.y0)
        right.sort(key=lambda b: b.bbox.y0)

        ordered = left + right

        for index, block in enumerate(ordered):
            block.features.reading_order = index

            if block.features.column == 0:
                block.features.column = (
                    1 if block in left else 2
                )

        return ordered