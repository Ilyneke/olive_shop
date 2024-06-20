from __future__ import annotations
import typing

from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base


if typing.TYPE_CHECKING:
    from models import Varieties


class Shops(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список товаров"""

    __tablename__ = 'shops'

    state = Column(String)
    city = Column(String)
    address = Column(String)
    phone = Column(BigInteger)
    available: Mapped[list["Varieties"]] = relationship(back_populates="shop")

    def __str__(self):
        return f'{self.state}, {self.city}, {self.address}'
