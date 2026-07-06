from dataclasses import dataclass


@dataclass(slots=True)
class MetadataField:
    """Represents one extracted metadata field."""

    value: str | None = None

    confidence: float = 0.0

    detector: str = ""

    page: int = 0