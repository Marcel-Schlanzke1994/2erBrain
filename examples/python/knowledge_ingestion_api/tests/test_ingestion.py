from second_brain_api.ingestion import parse_markdown


def test_parse():
    assert parse_markdown("---\ntitle: T\n---\nBody").metadata["title"] == "T"
