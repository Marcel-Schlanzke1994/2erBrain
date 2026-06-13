from second_brain_api.database import connect
from second_brain_api.models import Document
from second_brain_api.repository import DocumentRepository


def test_database_initialization():
    repo = DocumentRepository(connect("sqlite:///:memory:"))
    assert repo.add(Document(None, "A", {"title": "A"}, "body")).id == 1
