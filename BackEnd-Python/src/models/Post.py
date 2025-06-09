from ..extensions import db
import sqlalchemy as sq
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column


class Post(db.Model):
    id: Mapped[int] = mapped_column(
        sq.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    title: Mapped[str] = mapped_column(sq.CHAR(100), nullable=False)
    body: Mapped[str] = mapped_column(sq.CHAR(100), nullable=False)
    created: Mapped[datetime] = mapped_column(sq.DateTime, server_default=sq.func.now())
    author_id: Mapped[str] = mapped_column(sq.Integer, sq.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Title: {self.title!r}, Body: {self.body!r}, Author ID: {self.author_id!r}>"
