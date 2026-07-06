from core.models.bounding_box import BoundingBox
from core.models.document import Document
from core.models.page_layout import PageLayout
from core.models.page_region import PageRegion

from layout.block_classifier import BlockClassifier
from layout.column_detector import ColumnDetector
from layout.feature_extractor import FeatureExtractor
from layout.reading_order import ReadingOrderEngine


class LayoutAnalyzer:
    """Builds logical page layouts from raw page content."""

    HEADER_RATIO = 0.10
    FOOTER_RATIO = 0.10

    def __init__(self) -> None:
        self._column_detector = ColumnDetector()
        self._feature_extractor = FeatureExtractor()
        self._reading_order = ReadingOrderEngine()
        self._classifier = BlockClassifier()

    def analyze(self, document: Document) -> None:
        document.layout.pages.clear()

        for page in document.pages:

            # استخراج الخصائص
            self._feature_extractor.extract(page)

            height = page.height

            header = PageRegion(
                name="header",
                bbox=BoundingBox(
                    0,
                    0,
                    page.width,
                    height * self.HEADER_RATIO,
                ),
            )

            footer = PageRegion(
                name="footer",
                bbox=BoundingBox(
                    0,
                    height * (1 - self.FOOTER_RATIO),
                    page.width,
                    height,
                ),
            )

            body = PageRegion(
                name="body",
                bbox=BoundingBox(
                    0,
                    header.bbox.y1,
                    page.width,
                    footer.bbox.y0,
                ),
            )

            # تصنيف المنطقة لكل Block
            for block in page.text_blocks:

                center_y = (block.bbox.y0 + block.bbox.y1) / 2

                if center_y <= header.bbox.y1:
                    block.region = "header"
                    block.features.region = "header"

                elif center_y >= footer.bbox.y0:
                    block.region = "footer"
                    block.features.region = "footer"

                else:
                    block.region = "body"
                    block.features.region = "body"

            # اكتشاف عدد الأعمدة
            columns = self._column_detector.detect(page)

            # ترتيب القراءة
            reading_order = self._reading_order.order(
                page,
                columns,
            )

            # تصنيف الكتل
            self._classifier.classify(page)

            layout = PageLayout(
                header=header,
                body=body,
                footer=footer,
                columns=columns,
                reading_order=reading_order,
            )

            # إحصائيات الصفحة
            page.statistics.block_count = len(page.text_blocks)
            page.statistics.image_count = len(page.images)
            page.statistics.drawing_count = len(page.drawings)
            page.statistics.table_count = len(page.tables)
            page.statistics.columns = columns

            page.statistics.word_count = sum(
                block.features.word_count
                for block in page.text_blocks
            )

            page.statistics.character_count = sum(
                block.features.character_count
                for block in page.text_blocks
            )

            page.properties["block_types"] = {}

            for block in page.text_blocks:
                page.properties["block_types"].setdefault(
                    block.block_type,
                    0,
                )

                page.properties["block_types"][
                    block.block_type
                ] += 1

            document.layout.pages.append(layout)