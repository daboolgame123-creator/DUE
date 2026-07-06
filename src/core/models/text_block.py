from dataclasses import dataclass, field

from .block_features import BlockFeatures
from .bounding_box import BoundingBox
from .text_line import TextLine


@dataclass(slots=True)
class TextBlock:
    bbox: BoundingBox

    lines: list[TextLine] = field(default_factory=list)

    block_type: str = "text"

    region: str = "unknown"

    features: BlockFeatures = field(default_factory=BlockFeatures)

    @property
    def text(self) -> str:
        return "\n".join(
            line.text
            for line in self.lines
            if line.text.strip()
        )