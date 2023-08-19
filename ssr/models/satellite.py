import enum
from .base import BaseModel
from ..typing import CatalogNumber

class Satellite(BaseModel):
    name: str
    catalog: CatalogNumber
    
