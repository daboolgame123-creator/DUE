from core.models.document import Document
from core.interfaces.detector import Detector

from .pipeline_stage import PipelineStage


class DetectionStage(PipelineStage):
    def __init__(self, detectors: list[Detector]):
        self._detectors = detectors

    def execute(self, document: Document) -> None:
        for detector in self._detectors:
            detector.detect(document)