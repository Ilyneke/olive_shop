from __future__ import annotations

import typing
import requests

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from methods.currencies import get_currency_method, update_currency_method
from settings.base import API_DOMAIN
from settings.db import get_async_session
from utils.payments import create_payment_stripe

payments_router = APIRouter()


class OrderIn(BaseModel):
    price: float
    currency: str = 'USD'
    description: str | None


@payments_router.post('/api/payment', tags=['Payment'], summary='Payment')
async def get_products(
    data: OrderIn,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> typing.Any:
    if data.currency != 'USD':
        currency = await get_currency_method(session=session, code=data.currency)
        if currency is not None:
            data.price *= currency
        else:
            url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_avvJ2CyEpUXqdAtmkti91Mqwxdb4xj56ptapm8kB'
            response = requests.get(url=url)
            currency = response.json()['data'][data.currency]
            data.price *= currency
            await update_currency_method(session=session, code=data.currency, value=currency)
    print('PRICE:', int(data.price * 100))
    payment = create_payment_stripe(
        price=str(int(data.price * 100)), currency=data.currency,
        success_url=f'{API_DOMAIN}/olives-shop', cancel_url=f'{API_DOMAIN}/olives-shop'
    )
    return JSONResponse({'url': payment})
