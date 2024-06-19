from sqlalchemy.ext.asyncio import AsyncSession

from models import Products
from querysets.products import get_products_qs


async def insert_product(session: AsyncSession, product_instance: Products) -> None:
    """Добавление нового чека, если его еще нет в нашей системе."""
    session.add(product_instance)
    await session.commit()


async def get_products_method(session: AsyncSession) -> list:
    smtm = await session.execute(get_products_qs())
    products = smtm.scalars().all()
    return [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'image': product.image
        } for product in products
    ]
