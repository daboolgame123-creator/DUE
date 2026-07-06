from dataclasses import dataclass


@dataclass(slots=True)
class DetectionCandidate:
    """Represents a possible detector result."""

    value: str

    confidence: float = 0.0

    detector: str = ""

    page: int = 0

    block_index: int = 0