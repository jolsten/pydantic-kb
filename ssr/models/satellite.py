import enum
from typing import Optional, Literal
from .base import BaseModel
from ..typing import CatalogNumber, ESV

Manufacturer = Literal["Boeing", "Lockheed Martin"]

class Platform(BaseModel):
    name: str
    manufacturer: Manufacturer

class Satellite(BaseModel):
    name: str
    catalog: CatalogNumber
    platform: Optional[Platform]
