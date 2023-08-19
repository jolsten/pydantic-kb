import io
import re
from typing import Union, Annotated
from pydantic import AfterValidator

YamlSource = Union[str, bytes, io.IOBase]

def check_latitude(v: float) -> float:
    assert -90 <= v and v <= 90, f'{v} is not in range (-90, 90)'
    return v

def check_longitude(v: float) -> float:
    assert -180 <= v and v <= 180, f'{v} is not in range (-90, 90)'
    return v

Latitude = Annotated[float, AfterValidator(check_latitude)]
Longitude = Annotated[float, AfterValidator(check_longitude)]

INTEGER = re.compile(r'^\d+$')

# def convert_to_alpha5(v: Union[str, int]) -> str:
#     if INTEGER.match(str(v)) and v >= 100000:
#         pass

#         # Do stuff

