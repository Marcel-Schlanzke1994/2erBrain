from .models import Document
from .repository import DocumentRepository


def search_documents(repo: DocumentRepository, query: str) -> list[Document]:
    return [] if not query.strip() else repo.search(query.strip())
