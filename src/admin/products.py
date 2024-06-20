from sqladmin import ModelView
# from utils.custom_types import ModelView

from models import Products


class ProductsAdmin(ModelView, model=Products):  # type: ignore
    name_plural = 'products'
    name = 'product'
    icon = 'fa-solid fa-cart-shopping'
    column_list = [
        Products.name,
        Products.description,
        Products.discount,
        Products.price,
        Products.image,
        Products.variety
    ]
    column_details_exclude_list = [
        Products.created_at,
        Products.modified_at,
    ]
    form_excluded_columns = [
        Products.created_at,
        Products.modified_at,
    ]
    page_size = 25
    page_size_options = [50, 100]
