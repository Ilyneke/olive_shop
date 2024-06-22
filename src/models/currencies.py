from __future__ import annotations

from sqlalchemy import Column, String, Float

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base


class Currencies(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Table schema in the database storing the list of goods"""

    __tablename__ = 'currencies'

    code = Column(String, nullable=False, doc='Currency code')
    value = Column(Float, nullable=False, doc='Value')

    def __str__(self) -> str:
        return self.code
