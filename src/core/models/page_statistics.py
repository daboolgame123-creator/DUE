from dataclasses import dataclass


@dataclass(slots=True)
class PageStatistics:
    """Statistics computed for a page."""

    block_count: int = 0

    image_count: int = 0

    drawing_count: int = 0

    table_count: int = 0

    word_count: int = 0

    character_count: int = 0

    average_font_size: float = 0.0

    max_font_size: float = 0.0

    min_font_size: float = 0.0

    columns: int = 1