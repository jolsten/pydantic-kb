import yaml
from .typing import YamlSource
from .models.base import BaseModel

def load_object(y: YamlSource) -> BaseModel:
    yml = yaml.safe_load(y)
    print(yml)
    