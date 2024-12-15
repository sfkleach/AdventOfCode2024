from typing import Tuple
from day15 import translate_dirn
import argparse
from pathlib import Path


class Warehouse:

    def __init__(self, grid: Tuple[Tuple[str]]):
        self.grid = grid
        self.robot = [(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == '@'][0]

    def print(self):
        # print('Robot at position:', self.robot)
        for row in self.grid:
            print(''.join(row))
        print()
    
    def find_wall_or_space(self, move: str) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
        rx, ry = self.robot
        x, y = rx, ry
        dx, dy = translate_dirn(move)
        while True:
            x += dx
            y += dy
            c = self.grid[x][y]
            if c in ['#', '.']:
                # print('Move', (dx,dy), 'Found:', c, 'at:', (x, y), 'robot:', (rx+dx, ry+dy))
                return c, (x, y), (rx+dx, ry+dy)
            
    def move(self, move: str):
        c, (nx, ny), (rx, ry) = self.find_wall_or_space(move)
        if c == '.':
            x, y = self.robot
            self.grid[x][y] = '.'
            self.grid[nx][ny] = 'O'
            self.grid[rx][ry] = '@'
            self.robot = (rx, ry)

    def score(self):
        s = 0
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 'O':
                    gps = i * 100 + j
                    # print('GPS:', gps)
                    s += gps
        return s
    

def read_input(input_path: Path) -> Tuple[Warehouse, Tuple[str]]:
    with open(input_path) as f:
        lines = f.readlines()
        instructions = []
        warehouse = []
        for line in lines:
            L = line.strip()
            if L.startswith('#'):
                warehouse.append(list(L))
            elif L:
                instructions.append(L)
        return Warehouse(warehouse), ''.join(instructions)


def run(args):
    warehouse, instructions = read_input(args.input)
    # warehouse.print()
    for n, inst in enumerate(instructions):
        # if n > 2: break
        # print('Moving:', inst)
        warehouse.move(inst)
        # warehouse.print()
    print('Score:', warehouse.score())


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
