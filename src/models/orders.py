from __future__ import annotations

from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.dialects.postgresql import JSONB

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base


class Orders(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Table schema in the database storing the list of orders"""

    __tablename__ = 'orders'

    total_sum = Column(Integer, nullable=False, doc='Total sum')
    data = Column(JSONB, nullable=False, doc='list of products (id, count)')
    phone = Column(BigInteger, nullable=False, doc='Phone number')
    email = Column(String, nullable=True, doc='Email')

    def __str__(self) -> str:
        return self.name
