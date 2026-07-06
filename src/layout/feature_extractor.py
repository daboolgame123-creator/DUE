from collections import Counter

from core.models.block_features import BlockFeatures
from core.models.page import Page
from core.models.text_block import TextBlock


class FeatureExtractor:
    """Extracts geometric, typographic and textual features."""

    def extract(self, page: Page) -> None:

        for index, block in enumerate(page.text_blocks):

            features = BlockFeatures()

            self._geometry(page, block, features)

            self._typography(block, features)

            self._text(block, features)

            self._position(page, index, features)

            block.features = features

    def _geometry(
        self,
        page: Page,
        block: TextBlock,
        features: BlockFeatures,
    ) -> None:

        bbox = block.bbox

        features.x0 = bbox.x0
        features.y0 = bbox.y0
        features.x1 = bbox.x1
        features.y1 = bbox.y1

        features.width = bbox.x1 - bbox.x0
        features.height = bbox.y1 - bbox.y0

        features.center_x = (bbox.x0 + bbox.x1) / 2
        features.center_y = (bbox.y0 + bbox.y1) / 2

        if page.width:
            features.page_width_ratio = features.width / page.width

        if page.height:
            features.page_height_ratio = features.height / page.height

    def _typography(
        self,
        block: TextBlock,
        features: BlockFeatures,
    ) -> None:

        sizes = []
        fonts = []

        bold = 0
        italic = 0

        for line in block.lines:

            for span in line.spans:

                sizes.append(span.font_size)

                fonts.append(span.font_name)

                if "bold" in span.font_name.lower():
                    bold += 1

                if "italic" in span.font_name.lower():
                    italic += 1

        if sizes:

            features.min_font_size = min(sizes)

            features.max_font_size = max(sizes)

            features.average_font_size = sum(sizes) / len(sizes)

        if fonts:

            features.dominant_font = Counter(fonts).most_common(1)[0][0]

        features.bold_spans = bold

        features.italic_spans = italic

    def _text(
        self,
        block: TextBlock,
        features: BlockFeatures,
    ) -> None:

        text = block.text

        features.character_count = len(text)

        features.word_count = len(text.split())

        features.line_count = len(block.lines)

        if text:

            upper = sum(c.isupper() for c in text)

            alpha = sum(c.isalpha() for c in text)

            if alpha:

                features.uppercase_ratio = upper / alpha

        area = features.width * features.height

        if area > 0:

            features.density = features.character_count / area

    def _position(
        self,
        page: Page,
        index: int,
        features: BlockFeatures,
    ) -> None:

        features.is_first_block = index == 0

        features.is_last_block = index == len(page.text_blocks) - 1