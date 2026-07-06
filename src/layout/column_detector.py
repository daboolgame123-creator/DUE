from core.models.page import Page


class ColumnDetector:
    """Detects the number of text columns in a page."""

    def detect(self, page: Page) -> int:
        if not page.text_blocks:
            return 1

        centers = []

        for block in page.text_blocks:
            center_x = (block.bbox.x0 + block.bbox.x1) / 2
            centers.append(center_x)

        page_width = page.width
        middle = page_width / 2

        left = sum(1 for x in centers if x < middle)
        right = sum(1 for x in centers if x >= middle)

        if left >= 3 and right >= 3:
            return 2

        return 1