from sqlalchemy.ext.asyncio import AsyncSession

from querysets.currencies import get_actual_currency, update_currency


async def get_currency_method(session: AsyncSession, code: str) -> float | None:
    smtm = await session.execute(get_actual_currency(code=code))
    currency = smtm.scalar_one_or_none()
    if currency is not None:
        return currency.value


async def update_currency_method(session: AsyncSession, code: str, value: float) -> None:
    await session.execute(update_currency(code=code, value=value))
    await session.commit()
