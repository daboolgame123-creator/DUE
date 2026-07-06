from core.models.document import Document

from .pipeline_stage import PipelineStage


class KnowledgeStage(PipelineStage):
    def execute(self, document: Document) -> None:
        pass