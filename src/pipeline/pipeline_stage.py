from abc import ABC, abstractmethod

from core.models.document import Document


class PipelineStage(ABC):
    """Base class for all pipeline stages."""

    @abstractmethod
    def execute(self, document: Document) -> None:
        pass