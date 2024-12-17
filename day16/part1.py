from typing import Dict, Tuple
from day16 import *
import argparse
from pathlib import Path
import heapq

def read_input(file_path: Path) -> Tuple[str]:
    with open(file_path, 'r') as file:
        return tuple(file.read().splitlines())

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Trail:

    def __init__(self, position, trail):
        self.position = position
        self.trail = trail
        self.score = (trail.score if trail else 0) + self.delta_score()

    def __lt__(self, other): 
        return self.score < other.score

    def delta_score(self):
        if self.trail and self.trail.trail:
            x0, y0 = self.position
            x2, y2 = self.trail.trail.position
            d1 = abs(x0 - x2) == 0
            d2 = abs(y0 - y2) == 0
            if d1 and not d2 or d2 and not d1:
                return 1
            else:
                return 1001
        else:
            return 1
        
    def print(self):
        t = self
        while t:
            print(f'POSITION {t.position}, Score {t.score}')
            t = t.trail

class Maze:

    def __init__(self, data):
        self.data = tuple(data)
        self.start = None
        self.end = None
        for x, row in enumerate(self.data):
            for y, cell in enumerate(row):
                if cell == 'S':
                    self.start = (x, y)
                elif cell == 'E':
                    self.end = (x, y)
        self.trails = {}

    def get(self, x, y):
        return self.data[x][y] != '#'
    
    def __str__(self):
        return '\n'.join(self.data)
    
    def solve(self):
        prestart = Trail((self.start[0], self.start[1]-1), None)
        queue = []
        heapq.heappush(queue, Trail(self.start, prestart))
        while queue:
            t = heapq.heappop(queue)
            tpos = t.position
            tx, ty = tpos 
            if tpos in self.trails and t.score >= self.trails[tpos].score:
                continue
            self.trails[tpos] = t
            if tpos == self.end:
                continue
            for d in DIRECTIONS:
                x, y = tx + d[0], ty + d[1]
                if self.get(x, y):
                    heapq.heappush(queue, Trail((x, y), t))
        return self.trails[self.end]      

    def show(self, trail: Trail):
        data = list(map(list, self.data))
        while trail:
            x, y = trail.position
            data[x][y] = '*'
            trail = trail.trail
        print('\n'.join(''.join(row) for row in data))

def run(args):
    maze = Maze(read_input(args.input))
    solution = maze.solve()
    if solution:
        maze.show(solution)
        print(solution.score - 2)
    else:
        print('No solution')


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
