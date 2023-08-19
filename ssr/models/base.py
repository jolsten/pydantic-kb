import yaml
from pydantic import BaseModel as _BaseModel
from pydantic_yaml import parse_yaml_raw_as
from ..typing import YamlSource

class BaseModel(_BaseModel):
    @classmethod
    def from_yaml(cls, yml: YamlSource) -> 'BaseModel':
        return parse_yaml_raw_as(cls, yml)

    @classmethod
    def yaml_constructor(cls, loader: yaml.BaseLoader, node: yaml.MappingNode) -> callable:
        kwargs = loader.construct_mapping(node)
        return cls(**kwargs)
