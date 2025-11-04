from abs_prototype import AbsPrototype
from typing import Dict

class PrototypeManager(Dict[str, AbsPrototype]):
    def __setitem__(self, key, prototype):
        if issubclass(prototype, AbsPrototype):
            dict.__setitem__(self,key, prototype)