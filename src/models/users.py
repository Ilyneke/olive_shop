from __future__ import annotations

import typing

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UserBase

# if typing.TYPE_CHECKING:
#     from models import Checks


class Users(UserBase):
    """Схема таблицы в базе данных хранящее список юзеров и их персональные настройки и ограничения"""
    # allows_write_to_pm = Column(Boolean, default=True, doc='Разрешил ли юзер отправку ему сообщений?')
    # api_token = Column(String, nullable=True, doc='API токен proverkacheka.com')
    # checks: Mapped[list[Checks]] = relationship(back_populates='user')

    def __str__(self) -> str:
        return self.username
