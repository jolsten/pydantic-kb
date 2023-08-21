import yaml
from beanie import Document as _Document

class BaseModel(_Document):
    @classmethod
    def _yaml_constructor(cls, loader: yaml.BaseLoader, node: yaml.MappingNode):
        kwargs = loader.construct_mapping(node)
        return cls(**kwargs)

    @classmethod
    def _yaml_representer(cls, dumper, data) -> callable:
        def _representer(dumper, data):
            return dumper.represent_mapping(f'!{cls.__name__}', data)
        return _representer(dumper, data)
