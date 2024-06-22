from __future__ import annotations

import typing

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from methods.products import get_products_method
from settings.base import API_DOMAIN
from settings.db import get_async_session
from utils.payments import create_payment

products_router = APIRouter()


class ProductIn(BaseModel):
    price: float
    currency: str
    description: str


@products_router.get('/api/payment', tags=['Payment'], summary='Payment', response_model=None)
async def get_products(
    data: ProductIn,
) -> typing.Any:
    payment = create_payment(
        price=str(data.price), currency=data.currency, return_url=f'{API_DOMAIN}/olives-shop',
        description=data.description
    )
    return RedirectResponse(payment.content)
