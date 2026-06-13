from typing import Any

from flask import Flask, jsonify, request

from .config import Config
from .database import connect
from .errors import ApiError
from .ingestion import parse_markdown
from .logging_config import configure_logging
from .repository import DocumentRepository
from .search import search_documents


def as_json(document: Any) -> dict[str, Any]:
    return {
        "id": document.id,
        "title": document.title,
        "metadata": document.metadata,
        "content": document.content,
    }


def create_app(config: Config | None = None) -> Flask:
    cfg = config or Config.from_env()
    configure_logging(cfg.log_level)
    app = Flask(__name__)
    repo = DocumentRepository(connect(cfg.database_url))

    @app.errorhandler(ApiError)
    def api_error(error: ApiError):  # type: ignore[no-untyped-def]
        return jsonify({"error": {"code": error.code, "message": error.message}}), error.status

    @app.get("/health")
    def health():  # type: ignore[no-untyped-def]
        return {"status": "ok"}

    @app.post("/documents")
    def add_doc():  # type: ignore[no-untyped-def]
        data = request.get_json(silent=True) or {}
        raw = data.get("markdown")
        if not isinstance(raw, str):
            raise ApiError("invalid_request", "markdown string is required")
        return jsonify(as_json(repo.add(parse_markdown(raw)))), 201

    @app.get("/documents")
    def docs():  # type: ignore[no-untyped-def]
        return jsonify([as_json(d) for d in repo.list_all()])

    @app.get("/documents/<int:id>")
    def doc(id: int):  # type: ignore[no-untyped-def]
        found = repo.get(id)
        if not found:
            raise ApiError("not_found", "document not found", 404)
        return jsonify(as_json(found))

    @app.get("/search")
    def search():  # type: ignore[no-untyped-def]
        return jsonify([as_json(d) for d in search_documents(repo, request.args.get("q", ""))])

    return app
