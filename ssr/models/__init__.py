from .facility import Facility

import yaml

for cls in (Facility,):
    print(cls)
    def _constructor(loader, node):
        print(loader, node)
        value = loader.construct_scalar(node)
        print(value)
        kwargs = {key.value: val.value for key, val in value}
        print(kwargs)
        return
        return cls(value)
    yaml.add_constructor(f'!{cls.__name__}', _constructor)
