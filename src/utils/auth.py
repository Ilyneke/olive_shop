import hashlib
from datetime import datetime, timedelta, UTC

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
import jwt

# from methods.employers import get_employer_password_method
from settings.base import ADMIN_USERNAME, HASH_PASSWORD, AUTH_SALT, AUTH_TOKEN, ALGORITHM, PASSWORD
from settings.db import async_session


async def check_auth(username: str, password: str, request: Request) -> bool:
    """Валидация входа в панель администратора"""
    if username == ADMIN_USERNAME:
        if password == PASSWORD:
            request.session.update({'user_id': 'admin'})
            return True
    else:
        # async with async_session() as session:
        #     data = await get_employer_password_method(session=session, login=username)
        #     if data is not None:
        #         print('data:', data)
        #         pwd, _id = data
        #     session.close()
        # if data is not None and password == pwd:
        #     request.session.update({'user_id': str(_id)})
        #     return True
        pass
    return False


def create_token():
    return jwt.encode(
        {'exp': int((datetime.now(UTC) + timedelta(days=1)).timestamp())}, AUTH_TOKEN, algorithm=ALGORITHM
    )


def check_token(token: str | None) -> bool:
    if not token:
        return False
    try:
        return jwt.decode(token, AUTH_TOKEN, algorithms=ALGORITHM).get('exp') > int((datetime.now(UTC)).timestamp())
    except jwt.exceptions.ExpiredSignatureError:
        return False
