from sqladmin import ModelView

from models import Varieties


class VarietyAdmin(ModelView, model=Varieties):  # type: ignore
    name_plural = 'varieties'
    name = 'variety'
    icon = 'fa-solid fa-layer-group'
    column_list = [
        Varieties.variety,
    ]
    page_size = 25
    page_size_options = [50, 100]
