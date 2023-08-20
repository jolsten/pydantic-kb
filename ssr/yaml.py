from typing import Sequence, Any
import yaml
from .models.base import BaseModel
from .typing import YamlSource

class SSRSafeLoader(yaml.SafeLoader):
    pass

class SSRSafeDumper(yaml.SafeDumper):
    pass

for cls in BaseModel.__subclasses__():
    yaml.add_constructor(f'!{cls.__name__}', cls._yaml_constructor, Loader=SSRSafeLoader)
    yaml.add_representer(f'!{cls.__name__}', cls._yaml_representer, Dumper=SSRSafeDumper)

def load_yaml(y: YamlSource, lazy: bool = False) -> Sequence[BaseModel]:
    gen = yaml.load_all(y, SSRSafeLoader)
    if lazy:
        return gen
    return list(gen)

def dump_yaml(obj: Any) -> str:
    return yaml.dump_all(obj, yaml.SafeDumper)
