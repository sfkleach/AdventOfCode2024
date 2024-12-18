from day18 import *
import argparse
from pathlib import Path
import json
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
        t = self
        while t is not None:
            print(t.xy, '.')
            t = t.trail
    
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
class MemorySpace:

    def __init__(self, size):
        self.size = size
        self.locations: list[list[list[Trail]]] = [[[] for _ in range(size)] for _ in range(size)]

    def get(self, x, y):
        return self.locations[y][x]
    
    def add(self, x, y, trail):
        heapq.heappush(self.locations[y][x], trail)
    
    def init(self):
        queue = []
        heapq.heappush(queue, Trail((0,0), 0, None))
        while queue:
            print('queue:', queue)
            trail = heapq.heappop(queue)
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
            
def run(args):
    with open(args.input, 'r') as f:
        jdata = json.load(f)
    print(jdata)
    m = MemorySpace(jdata['size'])
    m.init()
    m.get_shortest_path().print()


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()
