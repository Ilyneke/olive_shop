from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import Products


def get_products_qs() -> select:
    """Формирование запроса в базу данных для получения юзера, если он является администратором."""
    return select(Products).options(selectinload(Products.variety))
