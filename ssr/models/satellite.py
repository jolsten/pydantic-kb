from typing import Optional, Literal
from .base import BaseModel
from .country import Country
from ..typing import CatalogNumber

Manufacturer = Literal[
    "Boeing",
    "Lockheed Martin",
    "Northrop Grumman",
]

class Platform(BaseModel):
    name: str
    manufacturer: Manufacturer

class Satellite(BaseModel):
    name: str
    country: Country
    catalog: Optional[CatalogNumber]
    platform: Optional[Platform]
