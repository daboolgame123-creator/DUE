from abc import ABC, abstractmethod

from core.models.document import Document


class Detector(ABC):
    """Base interface for all detectors."""

    @abstractmethod
    def detect(self, document: Document) -> None:
        """Analyze a document and update its models."""
        pass