from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(slots=True)
class DrawingObject:
    bbox: BoundingBox

    drawing_type: str = "vector"