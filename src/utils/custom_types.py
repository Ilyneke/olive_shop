from typing import Any

from fastapi_storages.integrations.sqlalchemy import FileType as _FileType
from fastapi_storages.integrations.sqlalchemy import ImageType as _ImageType
from fastapi_storages import FileSystemStorage

from sqladmin import ModelView as _ModelView

from settings.base import STORAGE_DIR


storage = FileSystemStorage(path=STORAGE_DIR)


class FileType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=storage, *args, **kwargs)


class ImageType(_ImageType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=storage, *args, **kwargs)


class ModelView(_ModelView):
    def _default_formatter(self, value: Any) -> Any:
        if type(value) in self.column_type_formatters:
            formatter = self.column_type_formatters[type(value)]
            return formatter(value)
        if isinstance(value, list) and value:
            inner_type = type(value[0])
            if inner_type in self.column_type_formatters:
                formatter = self.column_type_formatters[inner_type]
                return [formatter(val) for val in value]
        return value
