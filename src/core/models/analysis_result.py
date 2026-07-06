from dataclasses import dataclass, field
from typing import List

from .document import Document


@dataclass
class AnalysisResult:
    success: bool
    document: Document

    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)