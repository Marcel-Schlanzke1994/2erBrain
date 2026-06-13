from second_brain_api.config import Config


def test_defaults():
    assert Config().database_url.startswith("sqlite")
