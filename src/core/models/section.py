from dataclasses import dataclass


@dataclass
class Section:
    """Represents a detected logical section of a document
    (e.g. cover page, abstract, table of contents, chapter...).
    """

    section_type: str

    start_page: int
    end_page: int

    confidence: float = 1.0
