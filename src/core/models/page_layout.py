from dataclasses import dataclass, field

from .page_region import PageRegion
from .text_block import TextBlock


@dataclass(slots=True)
class PageLayout:
    """Logical layout of a page."""

    header: PageRegion | None = None

    body: PageRegion | None = None

    footer: PageRegion | None = None

    columns: int = 1

    reading_order: list[TextBlock] = field(default_factory=list)