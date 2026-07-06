from pathlib import Path

import fitz

from core.interfaces.document_reader import DocumentReader
from core.models.bounding_box import BoundingBox
from core.models.document import Document
from core.models.drawing_object import DrawingObject
from core.models.image_object import ImageObject
from core.models.page import Page
from core.models.text_block import TextBlock
from core.models.text_line import TextLine
from core.models.text_span import TextSpan


class PDFReader(DocumentReader):
    """Reader for PDF documents."""

    def can_read(self, file_path: str) -> bool:
        return file_path.lower().endswith(".pdf")

    def read(self, file_path: str) -> Document:
        path = Path(file_path)

        pdf = fitz.open(file_path)

        document = Document(
            filename=path.name,
            file_path=str(path),
            file_type="pdf",
        )

        document.metadata.page_count = len(pdf)

        for page_index, pdf_page in enumerate(pdf):

            page = Page(
                number=page_index + 1,
                width=pdf_page.rect.width,
                height=pdf_page.rect.height,
                rotation=pdf_page.rotation,
                text=pdf_page.get_text(),
            )

            layout = pdf_page.get_text("dict")

            # -----------------------------
            # Text Blocks
            # -----------------------------
            for block in layout["blocks"]:

                if block.get("type") != 0:
                    continue

                text_block = TextBlock(
                    bbox=BoundingBox(*block["bbox"]),
                )

                for line in block["lines"]:

                    text_line = TextLine()

                    for span in line["spans"]:

                        text_line.spans.append(
                            TextSpan(
                                text=span["text"],
                                bbox=BoundingBox(*span["bbox"]),
                                font_name=span.get("font", ""),
                                font_size=span.get("size", 0.0),
                                flags=span.get("flags", 0),
                            )
                        )

                    text_block.lines.append(text_line)

                page.text_blocks.append(text_block)

            # -----------------------------
            # Images
            # -----------------------------
            for index, image in enumerate(pdf_page.get_images(full=True)):

                xref = image[0]

                try:
                    rects = pdf_page.get_image_rects(xref)

                    if rects:

                        rect = rects[0]

                        page.images.append(
                            ImageObject(
                                index=index,
                                bbox=BoundingBox(
                                    rect.x0,
                                    rect.y0,
                                    rect.x1,
                                    rect.y1,
                                ),
                                width=image[2],
                                height=image[3],
                                colorspace=str(image[5]),
                                xref=xref,
                            )
                        )

                except Exception:
                    continue

            # -----------------------------
            # Vector Drawings
            # -----------------------------
            for drawing in pdf_page.get_drawings():

                rect = drawing["rect"]

                page.drawings.append(
                    DrawingObject(
                        bbox=BoundingBox(
                            rect.x0,
                            rect.y0,
                            rect.x1,
                            rect.y1,
                        )
                    )
                )

            document.pages.append(page)

        pdf.close()

        return document