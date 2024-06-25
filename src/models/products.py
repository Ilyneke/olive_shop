from __future__ import annotations
import typing

from sqlalchemy import Column, String, DECIMAL, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base
from utils.custom_types import FileType, ImageType


if typing.TYPE_CHECKING:
    from models import Varieties


class Products(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Table schema in the database storing the list of goods"""

    __tablename__ = 'products'

    name = Column(String, nullable=False, doc='Name of product')
    description = Column(String, nullable=False, doc='Product description')
    price = Column(DECIMAL(precision=5, scale=2), nullable=False, default=1)
    discount = Column(Integer, nullable=False, default=0)
    image = Column(FileType, nullable=True, doc='Picture of product')
    variety_id: Mapped[UUID] = mapped_column(ForeignKey("varieties.id"), nullable=True)
    variety: Mapped["Varieties"] = relationship(back_populates="products")

    def __str__(self) -> str:
        return self.name
