from typing import List

from core.interfaces.document_reader import DocumentReader
from core.models.document import Document


class ReaderManager:
    """Manages document readers and selects the appropriate one."""

    def __init__(self) -> None:
        self._readers: List[DocumentReader] = []

    def register(self, reader: DocumentReader) -> None:
        self._readers.append(reader)

    def read(self, file_path: str) -> Document:
        for reader in self._readers:
            if reader.can_read(file_path):
                return reader.read(file_path)

        raise ValueError(f"No reader found for: {file_path}")