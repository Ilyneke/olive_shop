from __future__ import annotations
import typing

from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base
from utils.custom_types import FileType


if typing.TYPE_CHECKING:
    from models import Availability


class Products(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список товаров"""

    __tablename__ = 'products'

    name = Column(String, nullable=False, doc='Name of product')
    description = Column(String, doc='Product description')
    price = Column(DECIMAL(precision=5, scale=2), nullable=False, default=1)
    image = Column(FileType, nullable=True, doc='Picture of product')
    available: Mapped[list["Availability"]] = relationship(back_populates="product")

    def __str__(self) -> str:
        return self.name
