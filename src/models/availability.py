from __future__ import annotations
import typing

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base


if typing.TYPE_CHECKING:
    from models import Shops, Products


class Availability(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список товаров"""

    __tablename__ = 'availability'

    quantity = Column(Integer, nullable=False, default=0)
    discount = Column(Integer)
    shop_id: Mapped[UUID] = mapped_column(ForeignKey("shops.id"))
    shop: Mapped["Shops"] = relationship(back_populates="available")
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Products"] = relationship(back_populates="available")

    def __str__(self) -> str:
        return f'{self.shop} {self.product}'
