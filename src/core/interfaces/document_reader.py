from abc import ABC, abstractmethod

from core.models.document import Document


class DocumentReader(ABC):
    """Base interface for all document readers."""

    @abstractmethod
    def can_read(self, file_path: str) -> bool:
        """Return True if this reader supports the given file."""
        pass

    @abstractmethod
    def read(self, file_path: str) -> Document:
        """Read a document and return a Document model."""
        pass