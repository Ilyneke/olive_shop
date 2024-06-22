from datetime import datetime, timedelta

from sqlalchemy import select, and_, update

from models import Currencies


def update_currency(code: str, value: float) -> select:
    return update(Currencies).where(Currencies.code == code).values(value=value)


def get_actual_currency(code: str) -> select:
    return select(Currencies)\
        .where(and_(Currencies.code == code, Currencies.modified_at - datetime.now(tz=None) < timedelta(hours=1)))
