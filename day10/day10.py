from pathlib import Path

class Map:

    def __init__(self, lines: tuple[tuple[int]]):
        self.lines = lines

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.lines) and 0 <= y < len(self.lines[x])
    
    def get(self, x: int, y: int) -> int:
        return self.lines[x][y]
    
    def zeros(self) -> int:
        return tuple((x, y) for x in range(len(self.lines)) for y in range(len(self.lines[x])) if self.get(x, y) == 0)
    
    def grow_trail(self, trail):
        x, y = trail[-1]
        n = len(trail)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if self.is_in_bounds(new_x, new_y) and self.get(new_x, new_y) == n:
                yield trail + [(new_x, new_y)]

    def explore(self, trail):
        if len(trail) == 10:
            yield trail
        else:
            for t in self.grow_trail(trail):
                yield from self.explore(t)

    def find_trail(self, z):
        return tuple(self.explore([z]))

    def find_trail_scores(self):
        trails = {}
        for z in self.zeros():
            trails[z] = set(t[-1] for t in self.find_trail(z))
        return trails
    
    def find_trail_ratings(self):
        trails = {}
        for z in self.zeros():
            trails[z] = len(self.find_trail(z))
        return trails
    

def read_input(file_path: Path) -> tuple[int]:
    with file_path.open('r') as file:
        lines = tuple(tuple(int(ch) for ch in line.strip()) for line in file )
    return lines