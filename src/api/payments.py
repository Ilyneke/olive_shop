from __future__ import annotations

import typing
import requests

from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from methods.currencies import get_currency_method, update_currency_method
from settings.base import API_DOMAIN
from settings.db import get_async_session
from utils.payments import create_payment_stripe, check_payment_stripe

payments_router = APIRouter()


class OrderIn(BaseModel):
    price: float
    currency: str = 'USD'
    description: str | None


@payments_router.post('/api/payment', tags=['Payment'], summary='Payment')
async def get_products(
    data: OrderIn,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> typing.Any:
    if data.currency != 'USD':
        currency = await get_currency_method(session=session, code=data.currency)
        if currency is not None:
            data.price *= currency
        else:
            url = 'https://v6.exchangerate-api.com/v6/c9d42dd579232451c017ad24/latest/USD'
            response = requests.get(url=url)
            currency = response.json()['conversion_rates'][data.currency]
            data.price *= currency
            await update_currency_method(session=session, code=data.currency, value=currency)
    payment = await create_payment_stripe(
        price=str(int(data.price * 100)), currency=data.currency,
        success_url=f'{API_DOMAIN}/olives-shop', cancel_url=f'{API_DOMAIN}/olives-shop'
    )
    background_tasks.add_task(check_payment_stripe, payment.id)
    return JSONResponse({'url': payment.url})
