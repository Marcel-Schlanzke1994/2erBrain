import sqlite3
from pathlib import Path


def path_from_url(url: str) -> str:
    if url == "sqlite:///:memory:":
        return ":memory:"
    if not url.startswith("sqlite:///"):
        raise ValueError("only sqlite URLs are supported")
    return url.removeprefix("sqlite:///")


def connect(url: str) -> sqlite3.Connection:
    path = path_from_url(url)
    if path != ":memory:":
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.execute(
        "create table if not exists documents("
        "id integer primary key, title text not null unique, "
        "metadata_json text not null, content text not null)"
    )
    return con
