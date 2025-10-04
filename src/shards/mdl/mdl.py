from typing import Any
import copy

class mdl:
    def __init__(self, depth: int = 2, size: int = 10, default=None) -> None:
        self.depth = depth
        self.size = size
        self.val = default
        self.data: Any = self._rec_mklist(depth)

    def _rec_mklist(self, d):
        if d == 1:
            return [copy.deepcopy(self.val) for _ in range(self.size)]
        return [self._rec_mklist(d - 1) for _ in range(self.size)]

    def __getitem__(self, key):
        if isinstance(key, tuple):
            value = self.data
            for k in key:
                value = value[k]
            return value
        return self.data[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            target = self.data
            for k in key[:-1]:
                target = target[k]
            target[key[-1]] = value
        else:
            self.data[key] = value
