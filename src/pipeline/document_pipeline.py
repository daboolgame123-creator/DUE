from core.models.analysis_result import AnalysisResult
from core.models.document import Document

from detectors.author_detector import AuthorDetector
from detectors.cover_page_detector import CoverPageDetector
from detectors.department_detector import DepartmentDetector
from detectors.title_detector import TitleDetector
from detectors.toc_detector import TocDetector
from detectors.university_detector import UniversityDetector

from pipeline.detection_stage import DetectionStage
from pipeline.extraction_stage import ExtractionStage
from pipeline.inference_stage import InferenceStage
from pipeline.knowledge_stage import KnowledgeStage
from pipeline.pipeline_stage import PipelineStage
from pipeline.layout_stage import LayoutStage

class DocumentPipeline:
    """Coordinates the complete document analysis workflow."""

    def __init__(self) -> None:
        self._stages: list[PipelineStage] = [
            LayoutStage(),
            
            DetectionStage(
                detectors=[
                    CoverPageDetector(),
                    TocDetector(),
                    TitleDetector(),
                    AuthorDetector(),
                    UniversityDetector(),
                    DepartmentDetector(),
                ]
            ),

            ExtractionStage(),

            KnowledgeStage(),

            InferenceStage(),
        ]

    def analyze(self, document: Document) -> AnalysisResult:
        for stage in self._stages:
            stage.execute(document)

        return AnalysisResult(
            success=True,
            document=document,
        )