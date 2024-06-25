from sqladmin import ModelView

from models import Orders


class OrdersAdmin(ModelView, model=Orders):  # type: ignore
    name_plural = 'orders'
    name = 'order'
    icon = 'fa-solid fa-credit-card'
    column_list = [
        Orders.total_sum,
        Orders.currency,
        Orders.phone,
        Orders.email,
    ]
    form_excluded_columns = [
        Orders.created_at,
        Orders.modified_at,
    ]
    column_formatters = {Orders.total_sum: lambda m, a: m.total_sum / 100}
    page_size = 25
    page_size_options = [50, 100]
