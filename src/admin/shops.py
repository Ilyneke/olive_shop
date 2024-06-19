from sqladmin import ModelView

from models import Shops


class ShopsAdmin(ModelView, model=Shops):  # type: ignore
    name_plural = 'shops'
    name = 'shops'
    icon = 'fa-solid fa-person'
    column_list = [
        Shops.state,
        Shops.city,
        Shops.address,
        Shops.phone,
    ]
    column_details_exclude_list = [
        Shops.available,
        Shops.created_at,
        Shops.modified_at,
    ]
    form_excluded_columns = [
        Shops.available,
        Shops.modified_at,
        Shops.created_at,
    ]
    page_size = 25
    page_size_options = [50, 100]
