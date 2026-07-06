from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Metadata:
    title: Optional[str] = None
    author: Optional[str] = None
    university: Optional[str] = None
    faculty: Optional[str] = None
    department: Optional[str] = None
    supervisor: Optional[str] = None

    publication_year: Optional[int] = None
    document_type: Optional[str] = None
    language: Optional[str] = None

    keywords: List[str] = field(default_factory=list)
    abstract: Optional[str] = None

    page_count: int = 0