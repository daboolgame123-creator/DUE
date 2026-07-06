from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(slots=True)
class PageRegion:
    """Represents a logical region on a page."""

    name: str

    bbox: BoundingBox