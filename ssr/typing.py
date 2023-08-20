import io
import pathlib
from typing import Union, Annotated, Literal
from pydantic import AfterValidator

from .utils import alpha5_to_catalog_number

PathLike = Union[str, bytes, pathlib.Path]

YamlSource = Union[str, bytes, io.IOBase]

def check_latitude(v: float) -> float:
    assert -90 <= v and v <= 90, f'{v} is not in range (-90, 90)'
    return v

def check_longitude(v: float) -> float:
    assert -180 <= v and v <= 180, f'{v} is not in range (-90, 90)'
    return v

Latitude = Annotated[float, AfterValidator(check_latitude)]
Longitude = Annotated[float, AfterValidator(check_longitude)]

def convert_alpha5_to_number(v: Union[str, int]) -> int:
    return alpha5_to_catalog_number(str(v))

def check_alpha5_range(v: int) -> int:
    assert (0 <= v and v < 340_000)
    return v

CatalogNumber = Annotated[
    Union[int, str],
    AfterValidator(convert_alpha5_to_number),
    AfterValidator(check_alpha5_range)
]
