import yaml
from yaml import safe_load_all
from .models.base import BaseModel
from .typing import YamlSource

class SSRSafeLoader(yaml.SafeLoader):
    pass

for cls in BaseModel.__subclasses__():
    yaml.add_constructor(f'!{cls.__name__}', cls.yaml_constructor, Loader=SSRSafeLoader)

def load_yaml(y: YamlSource):
    return yaml.load(y, SSRSafeLoader)
