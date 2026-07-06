from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(slots=True)
class TableObject:
    bbox: BoundingBox

    rows: int = 0

    columns: int = 0