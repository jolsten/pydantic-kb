from typing import Optional, Literal
from pydantic import Field
from .base import BaseModel
from .country import Country
from ..typing import CatalogNumber, ESV

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
    country: Optional[Country] = None
    catalog: Optional[CatalogNumber] = None
    platform: Optional[Platform] = None
