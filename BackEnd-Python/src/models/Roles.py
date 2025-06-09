from ..extensions import db
import sqlalchemy as sq
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Role(db.Model):
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sq.String, nullable=False)
    user: Mapped[list["User"]] = relationship(back_populates="role")  # type: ignore

    def __repr__(self):
        return f"<Role: {self.id!r}, Name: {self.name!r}>"
