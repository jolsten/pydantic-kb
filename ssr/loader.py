from typing import Sequence
import yaml
from .models.base import BaseModel
from .typing import YamlSource

class SSRSafeLoader(yaml.SafeLoader):
    pass

for cls in BaseModel.__subclasses__():
    yaml.add_constructor(f'!{cls.__name__}', cls.yaml_constructor, Loader=SSRSafeLoader)

def load_yaml(y: YamlSource, lazy: bool = False) -> Sequence[BaseModel]:
    gen = yaml.load_all(y, SSRSafeLoader)
    if lazy:
        return gen
    return list(gen)
