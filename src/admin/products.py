from sqladmin import ModelView
# from utils.custom_types import ModelView

from models import Products


class ProductsAdmin(ModelView, model=Products):  # type: ignore
    name_plural = 'products'
    name = 'product'
    icon = 'fa-solid fa-person'
    column_list = [
        Products.name,
        Products.description,
        Products.price,
        Products.image,
    ]
    column_details_exclude_list = [
        Products.created_at,
        Products.modified_at,
        Products.available,
    ]
    form_excluded_columns = [
        Products.created_at,
        Products.modified_at,
        Products.available,
    ]
    page_size = 25
    page_size_options = [50, 100]
