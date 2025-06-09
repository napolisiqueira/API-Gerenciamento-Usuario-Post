from ..extensions import db
import sqlalchemy as sq
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(sq.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sq.String, unique=True)
    password: Mapped[str] = mapped_column(sq.String, nullable=False)
    email: Mapped[str] = mapped_column(sq.String)
    activity: Mapped[bool] = mapped_column(sq.Boolean, default=True)
    role_id: Mapped[int] = mapped_column(sq.ForeignKey("role.id"))
    role: Mapped["Role"] = relationship(back_populates='user') # type: ignore

    def __repr__(self):
        return f"<ID: {self.id!r}, Usuario: {self.username!r}, Email: {self.email!r}, Activity: {self.activity!r}>"
