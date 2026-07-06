from dataclasses import dataclass, field
from typing import Any, Dict, List

from .metadata import Metadata
from .page import Page
from .section import Section
from .layout_info import LayoutInfo

@dataclass
class Document:
    filename: str
    file_path: str
    file_type: str

    metadata: Metadata = field(default_factory=Metadata)

    pages: List[Page] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)

    properties: Dict[str, Any] = field(default_factory=dict)

    layout: LayoutInfo = field(default_factory=LayoutInfo)