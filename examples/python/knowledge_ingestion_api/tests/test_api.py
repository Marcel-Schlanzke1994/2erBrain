from second_brain_api.app import create_app
from second_brain_api.config import Config


def client():
    return create_app(Config()).test_client()


def md(title="Doc"):
    return f"---\ntitle: {title}\n---\nhello world rag"


def test_health():
    assert client().get("/health").json == {"status": "ok"}


def test_ingest_and_search():
    c = client()
    response = c.post("/documents", json={"markdown": md()})
    assert response.status_code == 201
    assert c.get("/search?q=rag").json[0]["title"] == "Doc"


def test_missing_title():
    assert client().post("/documents", json={"markdown": "body"}).status_code == 400


def test_malformed_metadata():
    assert client().post("/documents", json={"markdown": "---\ntitle x"}).status_code == 400


def test_duplicate_and_missing():
    c = client()
    c.post("/documents", json={"markdown": md("Same")})
    c.post("/documents", json={"markdown": md("Same")})
    assert len(c.get("/documents").json) == 1
    assert c.get("/documents/99").status_code == 404


def test_empty_search():
    assert client().get("/search?q=").json == []
