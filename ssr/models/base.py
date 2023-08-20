import yaml
from pydantic import BaseModel as _BaseModel
from pydantic_yaml import parse_yaml_raw_as
from ..typing import YamlSource

class BaseModel(_BaseModel):
    @classmethod
    def from_yaml(cls, yml: YamlSource) -> 'BaseModel':
        return parse_yaml_raw_as(cls, yml)

    @classmethod
    def _yaml_constructor(cls, loader: yaml.BaseLoader, node: yaml.MappingNode):
        kwargs = loader.construct_mapping(node)
        return cls(**kwargs)

    @classmethod
    def _yaml_representer(cls, dumper, data) -> callable:
        def _representer(dumper, data):
            return dumper.represent_mapping(f'!{cls.__name__}', data)
        return _representer(dumper, data)
