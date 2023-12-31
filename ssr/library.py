import pathlib
from typing import Optional, Union, Tuple, Dict, Literal
from .models.base import BaseModel
from .yaml import load_yaml
from .config import load_settings
from .typing import PathLike

# Category = Literal
# Category.__args__ = (cls.__name__ for cls in BaseModel.__subclasses__())

class Record(BaseModel):
    source: PathLike
    object: BaseModel

class Library:
    def __init__(self) -> None:
        self.settings = load_settings()
        self._items: Dict[str, Dict[str, Record]] = {
            cls.__name__.lower(): {} for cls in BaseModel.__subclasses__()
        }
        self.reload_library()
    
    def reload_library(self, library_path: Optional[PathLike] = None) -> None:
        if library_path is None:
            library_path = self.settings.library
        else:
            library_path = pathlib.Path(library_path)

        for file in library_path.rglob('*.yaml'):
            sequence = load_yaml(file.read_text())
            for item in sequence:
                cls_name = item.__class__.__name__
                self[cls_name, item.name] = Record(source=file, object=item)

    def get_category(self, _cls: Union[str, BaseModel], /) -> Dict[str, BaseModel]:
        records = self._items[_cls.lower()]
        return {name: rec.object for name, rec in records.items()}

    def get_item(self, _cls: Union[str, BaseModel], name: str, /) -> BaseModel:
        return self.get_category(_cls)[name.lower()]

    def __setitem__(self, key: Tuple[str], value) -> None:
        if isinstance(key, tuple):
            _cls, name = key
            self._items[_cls.lower()][name.lower()] = value
        else:
            raise ValueError(f'Library.__setitem__() expects a two-element tuple but got {key!r}')

    def __getitem__(self, key: Union[str, Tuple[str]]) -> dict:
        if isinstance(key, tuple):
            return self.get_item(*key)
        else:
            return self.get_category(key)
