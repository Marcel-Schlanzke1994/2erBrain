from second_brain_api.database import connect
from second_brain_api.models import Document
from second_brain_api.repository import DocumentRepository
from second_brain_api.search import search_documents


def test_search_success_empty():
    repo = DocumentRepository(connect("sqlite:///:memory:"))
    repo.add(Document(None, "A", {}, "needle"))
    assert search_documents(repo, "needle")
    assert search_documents(repo, "") == []
