from dataclasses import dataclass


@dataclass(slots=True)
class BlockFeatures:
    """Computed features for a text block."""

    # ---------- Geometry ----------

    x0: float = 0.0
    y0: float = 0.0
    x1: float = 0.0
    y1: float = 0.0

    width: float = 0.0
    height: float = 0.0

    center_x: float = 0.0
    center_y: float = 0.0

    page_width_ratio: float = 0.0
    page_height_ratio: float = 0.0

    # ---------- Typography ----------

    min_font_size: float = 0.0
    max_font_size: float = 0.0
    average_font_size: float = 0.0

    dominant_font: str = ""

    bold_spans: int = 0
    italic_spans: int = 0

    # ---------- Text ----------

    line_count: int = 0
    word_count: int = 0
    character_count: int = 0

    uppercase_ratio: float = 0.0

    # ---------- Position ----------

    is_first_block: bool = False
    is_last_block: bool = False

    # ---------- Layout ----------

    region: str = "unknown"

    column: int = 0

    reading_order: int = 0

    # ---------- Statistics ----------

    density: float = 0.0