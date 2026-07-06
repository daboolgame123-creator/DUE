from dataclasses import dataclass, field

from .text_span import TextSpan


@dataclass(slots=True)
class TextLine:
    spans: list[TextSpan] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "".join(span.text for span in self.spans)