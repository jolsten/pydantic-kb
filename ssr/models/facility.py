from typing import Literal
from .base import BaseModel
from ..typing import Latitude, Longitude

FacilityType = Literal[
    'Unknown',
    'Other',
    'Satellite Control Center',
    'Satellite Control Site',
    'Data Reception Site',
    'Space Launch Complex',
    'Space Launch Site',
]

class Facility(BaseModel):
    name: str
    type: FacilityType = FacilityType.__args__[0]
    lat: Latitude
    lon: Longitude
