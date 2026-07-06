from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(slots=True)
class ImageObject:
    index: int

    bbox: BoundingBox

    width: int = 0

    height: int = 0

    colorspace: str = ""

    xref: int = 0