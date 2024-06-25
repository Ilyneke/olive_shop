from sqlalchemy.ext.asyncio import AsyncSession

from querysets.products import get_products_qs

from settings.base import API_DOMAIN


def get_image_url(image: str | None) -> str:
    if image is not None:
        return image.replace('/code', f'{API_DOMAIN}/olive')
    else:
        return 'https://kharisov.space/olive/storage/no-image-available-icon-vector.jpg'


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
            'discounted_price': round(float(product.price - product.price * product.discount / 100), 2),
            'variety': product.variety.variety,
            'image': get_image_url(product.image),
        } for product in sorted(products, key=lambda x: x.variety.variety)
    ]
