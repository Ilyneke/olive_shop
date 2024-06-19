from sqladmin import ModelView

from models import Availability


class AvailabilityAdmin(ModelView, model=Availability):  # type: ignore
    name_plural = 'availability'
    name = 'availability'
    icon = 'fa-solid fa-person'
    column_list = [
        Availability.quantity,
        Availability.discount,
        Availability.shop,
        Availability.product,
    ]
    page_size = 25
    page_size_options = [50, 100]
