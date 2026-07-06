from dataclasses import dataclass, field

from .page_layout import PageLayout


@dataclass(slots=True)
class LayoutInfo:
    """Layout information for a document."""

    pages: list[PageLayout] = field(default_factory=list)