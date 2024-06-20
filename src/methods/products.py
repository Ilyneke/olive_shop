from sqlalchemy.ext.asyncio import AsyncSession

from querysets.products import get_products_qs

from settings.base import API_DOMAIN


async def get_products_method(session: AsyncSession) -> list:
    smtm = await session.execute(get_products_qs())
    products = smtm.scalars().all()
    return [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'discount': float(product.discount),
            'discounted_price': float(product.price - product.price * product.discount / 100),
            'variety': product.variety.variety,
            'image': product.image.replace('/code', f'{API_DOMAIN}/olive')
        } for product in sorted(products, key=lambda x: x.variety.variety)
    ]
