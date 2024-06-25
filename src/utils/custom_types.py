from typing import Any, Optional

from fastapi_storages.base import StorageFile
from fastapi_storages.integrations.sqlalchemy import FileType as _FileType
from fastapi_storages.integrations.sqlalchemy import ImageType as _ImageType
from fastapi_storages import FileSystemStorage
from sqlalchemy.engine.interfaces import Dialect

from settings.base import STORAGE_DIR


storage = FileSystemStorage(path=STORAGE_DIR)


class FileType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=storage, *args, **kwargs)

    def process_bind_param(self, value: Any, dialect: Dialect) -> Optional[str]:
        if value is None:
            return value
        if len(value.file.read(1)) != 1:
            return None

        if value.size is None:
            return value.filename

        file = StorageFile(name=value.filename, storage=self.storage)
        file.write(file=value.file)

        value.file.close()
        return file.name


class ImageType(_ImageType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=storage, *args, **kwargs)
