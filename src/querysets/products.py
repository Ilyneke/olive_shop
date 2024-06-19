from sqlalchemy import select
from models import Products


def get_products_qs() -> select:
    """Формирование запроса в базу данных для получения юзера, если он является администратором."""
    return select(Products)
