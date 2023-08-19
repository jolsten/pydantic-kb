import enum
from .base import BaseModel
from ..typing import Latitude, Longitude

class FacilityType(str, enum.Enum):
    UNK = 'Unknown'
    SCS = 'Satellite Control Site'
    SCC = 'Satellite Control Center'
    DRS = 'Data Reception Site'
    SLC = 'Space Launch Complex'
    SLS = 'Space Launch Site'
    OTH = 'Other'


class Facility(BaseModel):
    name: str
    type: FacilityType = FacilityType.UNK
    lat: Latitude
    lon: Longitude
