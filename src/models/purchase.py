from __future__ import annotations

from sqlalchemy import Column, String, Integer

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base
from utils.custom_types import FileType


class Purchases(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список товаров"""

    __tablename__ = 'purchases'

    phone = Column(String, doc='phone number')
    address = Column(String, doc='address')
    price = Column(Integer, doc='Стоимость')
    quantity = Column(Integer, doc='Количество')
    sale = Column(Integer, doc='Скидка')

    def __str__(self) -> str:
        return self.name
