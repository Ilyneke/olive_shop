from __future__ import annotations

import typing

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from methods.products import get_products_method
from settings.db import get_async_session

products_router = APIRouter()


class ProductOut(BaseModel):
    id: str
    name: str
    description: str
    price: str
    image: str


@products_router.get('/api/products', tags=['Products'], summary='Get products', response_model=ProductOut)
async def get_products(
    state: str | None = None,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> typing.Any:
    products = await get_products_method(session=session)
    return JSONResponse(content=products)
