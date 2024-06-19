from sqlalchemy.ext.asyncio import AsyncSession

from models import Users
from querysets.users import get_admin_qs, get_users_qs, get_count_users_qs


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    """Добавление нового пользователя, если его еще нет в нашей системе."""
    user = await session.get(Users, user_instance.id)
    if user is None:
        session.add(user_instance)
        await session.commit()


async def update_user_check_token(session: AsyncSession, user_id: int, token: str) -> None:
    """Обновление токена"""
    user: Users | None = await session.get(Users, user_id)
    if user is not None:
        user.api_token = token
        await session.commit()


async def get_user_token(session: AsyncSession, user_id: int) -> str | None:
    user = await session.get(Users, user_id)
    if user is not None:
        return user.api_token


async def is_admin(session: AsyncSession, user_id: int) -> bool:
    """Проверяем, является ли юзер администратором."""
    smtm = await session.execute(get_admin_qs(user_id))
    user = smtm.scalar_one_or_none()
    if user is None:
        return False
    return True


async def get_users(session: AsyncSession) -> list:
    """Получить список всех юзеров"""
    smtm = await session.execute(get_users_qs())
    return smtm.scalars().all()


async def get_count_users(session: AsyncSession):
    """Получить кол-во юзеров"""
    smtm = await session.execute(get_count_users_qs())
    return smtm.scalar()
