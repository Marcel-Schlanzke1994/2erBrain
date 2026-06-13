from .errors import ApiError
from .models import Document


def parse_markdown(text: str) -> Document:
    if not text.strip():
        raise ApiError("empty_document", "document body is required")
    metadata: dict[str, str] = {}
    content = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            raise ApiError("malformed_metadata", "front matter must close with ---")
        raw = text[4:end]
        content = text[end + 5 :].strip()
        for line in raw.splitlines():
            if not line.strip():
                continue
            if ":" not in line:
                raise ApiError("malformed_metadata", "metadata lines must use key: value")
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"')
    title = metadata.get("title")
    if not title:
        raise ApiError("missing_title", "metadata title is required")
    return Document(None, title, metadata, content)
