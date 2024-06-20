from __future__ import annotations
import typing

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UUIDBaseMixin
from settings.db import Base


if typing.TYPE_CHECKING:
    from models import Products


class Varieties(UUIDBaseMixin, Base):
    """Database table schema storing the list of varieties"""

    __tablename__ = 'varieties'

    variety = Column(String, nullable=False, doc='Name of variety')
    products: Mapped[list["Products"]] = relationship(back_populates="variety")

    def __str__(self) -> str:
        return self.variety
