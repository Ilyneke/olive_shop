from sqladmin import ModelView

from models import Orders


class OrdersAdmin(ModelView, model=Orders):  # type: ignore
    name_plural = 'orders'
    name = 'order'
    icon = 'fa-solid fa-cart-shopping'
    column_list = [
        Orders.total_sum,
        Orders.phone,
        Orders.email,
    ]
    form_excluded_columns = [
        Orders.created_at,
        Orders.modified_at,
    ]
    page_size = 25
    page_size_options = [50, 100]
