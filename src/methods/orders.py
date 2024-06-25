from settings.db import async_session
from models import Orders


async def insert_order_method(order_instance: Orders):
    async with async_session() as session:
        try:
            session.add(order_instance)
            await session.commit()
        finally:
            await session.close()
