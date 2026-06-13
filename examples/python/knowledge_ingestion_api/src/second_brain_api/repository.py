from __future__ import annotations

import json
import sqlite3

from .models import Document


class DocumentRepository:
    def __init__(self, con: sqlite3.Connection) -> None:
        self.con = con

    def add(self, doc: Document) -> Document:
        cur = self.con.execute(
            "insert or ignore into documents(title, metadata_json, content) values(?,?,?)",
            (doc.title, json.dumps(doc.metadata, sort_keys=True), doc.content),
        )
        self.con.commit()
        if cur.lastrowid == 0:
            row = self.con.execute("select * from documents where title=?", (doc.title,)).fetchone()
        else:
            row = self.con.execute(
                "select * from documents where id=?", (cur.lastrowid,)
            ).fetchone()
        return self._row(row)

    def list_all(self) -> list[Document]:
        return [self._row(r) for r in self.con.execute("select * from documents order by id")]

    def get(self, id: int) -> Document | None:
        row = self.con.execute("select * from documents where id=?", (id,)).fetchone()
        return self._row(row) if row else None

    def search(self, q: str) -> list[Document]:
        like = f"%{q}%"
        return [
            self._row(r)
            for r in self.con.execute(
                "select * from documents where title like ? or content like ? order by id",
                (like, like),
            )
        ]

    def _row(self, row: sqlite3.Row) -> Document:
        return Document(row["id"], row["title"], json.loads(row["metadata_json"]), row["content"])
