from dataclasses import dataclass, field
from typing import Any

from .drawing_object import DrawingObject
from .image_object import ImageObject
from .page_statistics import PageStatistics
from .table_object import TableObject
from .text_block import TextBlock


@dataclass(slots=True)
class Page:
    number: int

    width: float = 0.0

    height: float = 0.0

    rotation: int = 0

    text: str = ""

    text_blocks: list[TextBlock] = field(default_factory=list)

    images: list[ImageObject] = field(default_factory=list)

    drawings: list[DrawingObject] = field(default_factory=list)

    tables: list[TableObject] = field(default_factory=list)

    attachments: list = field(default_factory=list)

    statistics: PageStatistics = field(default_factory=PageStatistics)

    properties: dict[str, Any] = field(default_factory=dict)