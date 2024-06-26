import typing

from fastapi import Request
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend

from settings.base import AUTH_TOKEN
from utils.auth import check_auth, create_token, check_token
from .products import ProductsAdmin
from .variety import VarietyAdmin
from .currencies import CurrencyAdmin
from .orders import OrdersAdmin


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if await check_auth(form['username'], form['password'], request=request):
            request.session.update({'token': create_token()})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return check_token(request.session.get('token'))


def init_admin_panel(app: typing.Any, engine: typing.Any) -> None:
    authentication_backend = AdminAuth(secret_key=AUTH_TOKEN)
    admin_views = Admin(
        app,
        engine,
        authentication_backend=authentication_backend,
        debug=False,
    )

    admin_views.add_view(ProductsAdmin)
    admin_views.add_view(VarietyAdmin)
    admin_views.add_view(CurrencyAdmin)
    admin_views.add_view(OrdersAdmin)
