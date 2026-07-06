from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(slots=True)
class TextSpan:
    text: str

    bbox: BoundingBox

    font_name: str = ""

    font_size: float = 0.0

    flags: int = 0