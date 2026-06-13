from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    id: int | None
    title: str
    metadata: dict[str, str]
    content: str
