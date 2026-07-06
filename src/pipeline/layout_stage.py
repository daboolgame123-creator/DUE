from core.models.document import Document

from layout.layout_analyzer import LayoutAnalyzer
from pipeline.pipeline_stage import PipelineStage


class LayoutStage(PipelineStage):
    def __init__(self) -> None:
        self._analyzer = LayoutAnalyzer()

    def execute(self, document: Document) -> None:
        self._analyzer.analyze(document)