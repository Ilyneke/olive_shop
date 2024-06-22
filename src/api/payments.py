from __future__ import annotations

import typing

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from settings.base import API_DOMAIN
from settings.db import get_async_session
from utils.payments import create_payment_youkassa, create_payment_stripe

payments_router = APIRouter()


class OrderIn(BaseModel):
    price: float
    currency: str = 'USD'
    description: str | None


@payments_router.post('/api/payment', tags=['Payment'], summary='Payment')
async def get_products(
    data: OrderIn,
) -> typing.Any:
    payment = create_payment_stripe(
        price=str(int(data.price * 100)), currency=data.currency,
        success_url=f'{API_DOMAIN}/olives-shop', cancel_url=f'{API_DOMAIN}/olives-shop'
    )
    return JSONResponse({'url': payment})
