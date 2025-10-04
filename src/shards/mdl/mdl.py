from typing import Any

class mdl:
    def __init__(self, depth: int = 2, size: int = 10, default = None) -> None:
        self.depth = depth
        self.size = size
        self.val = default
        self.md_list: Any = self._rec_mklist(depth)

    def _rec_mklist(self, d):
        if d == 1:
            return [self.val] * self.size
        return [self._rec_mklist(d - 1) for _ in range(self.size)]


    def read(self, coords: tuple = ()):
        if len(coords) > self.depth: raise ValueError(f"Shards: Coords must have {self.depth} elements (Following the lists depth)")

        curr = self.md_list
        for coord in coords:
            curr = curr[coord]
        
        return curr
    
    def set(self, coords: tuple, val = "0"):
        if len(coords) > self.depth: raise ValueError(f"Shards: Coords must have {self.depth} elements (Following the lists depth)")

        curr = self.md_list
        for coord in coords[:-1]:
            curr = curr[coord]
        curr[coords[-1]] = val