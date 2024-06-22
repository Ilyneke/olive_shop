from sqladmin import ModelView

from models import Currencies


class CurrencyAdmin(ModelView, model=Currencies):  # type: ignore
    name_plural = 'currencies'
    name = 'currency'
    icon = 'fa-solid fa-coins'
    column_list = [
        Currencies.code,
        Currencies.value
    ]
    page_size = 25
    page_size_options = [50, 100]
