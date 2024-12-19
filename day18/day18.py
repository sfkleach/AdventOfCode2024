from pathlib import Path
from collections import defaultdict
import heapq

class Trail:

    def __init__(self, xy: tuple[int, int], score: int, trail):
        self.xy = xy
        self.score = score
        self.trail = trail

    def __lt__(self, other):
        return self.score < other.score
    
    def __repr__(self):
        return f'Trail({self.xy}, {self.score})'
    
    def includes(self, xy):
        t = self
        while t is not None:
            if self.xy == xy:
                return True
            t = t.trail
        return False
    
    def print(self):
        n = 0
        t = self
        while t is not None:
            n += 1
            print(t.xy, '.')
            t = t.trail
        print('Length:', n)

    def len(self):
        n = 0
        t = self
        while t is not None:
            n += 1
            t = t.trail
        return n
    
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
class MemorySpace:

    def __init__(self, size, corrupted: list[list[int]]):
        self.size = size
        self.locations: list[list[list[Trail]]] = [[[] for _ in range(size)] for _ in range(size)]
        self.corrupted = set(map(lambda x: (x[0], x[1]), corrupted))

    def get(self, x, y):
        return self.locations[y][x]
    
    def add(self, x, y, trail):
        heapq.heappush(self.locations[y][x], trail)
    
    def init(self):
        queue = []
        heapq.heappush(queue, Trail((0,0), 0, None))
        while queue:
            # print('queue:', queue)
            trail = heapq.heappop(queue)
            if trail.xy in self.corrupted:
                continue
            x, y = trail.xy
            cell = self.get(x, y)
            is_smallest = not cell
            if not is_smallest:
                s = heapq.nsmallest(1, cell)[0]
                is_smallest = trail < s
            heapq.heappush(cell, trail)
            if is_smallest:
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if not trail.includes((nx, ny)):
                            heapq.heappush(queue, Trail((nx, ny), trail.score + 1, trail))

    def get_end(self):
        return self.get(self.size - 1, self.size - 1)

    def get_shortest_path(self):
        return heapq.nsmallest(1, self.get_end())[0]