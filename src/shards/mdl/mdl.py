class mdl:
    def __init__(self, depth: int = 2) -> None:
        self.md_list: list = []
        self.depth = depth

    def read(self, coords: tuple = ()):
        if len(coords) > self.depth: return None

        curr = self.md_list
        for coord in coords:
            curr = curr[coord]
        
        return curr
    
    def set(self, coords, val):