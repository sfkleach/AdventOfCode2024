from day15 import translate_dirn
import argparse
from pathlib import Path
from typing import Set, Tuple


class Warehouse:

    def __init__(self, grid: Tuple[Tuple[str]]):
        self.grid = grid
        self.robot = [(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == '@'][0]

    def print(self):
        print('Robot at position:', self.robot)
        for row in self.grid:
            print(''.join(row))
        print()

    def free_to_move(self, dx: int, dy: int) -> bool:
        rx, ry = self.robot
        return self.grid[rx+dx][ry + dy] == '.'
    
    
    def find_shove_set(self, dx:int, dy: int) -> Set[Tuple[int,int]]:
        # Return the coords of the set of boxes to shove. Each box
        # has two coordinates! The robot is included in the set.
        rx, ry = self.robot
        shove_set = [(rx, ry)]
        if dx == 0:
            # Horizontal shove
            # print('Horizontal shove:', dx, dy)
            x = rx
            y = ry 
            while True:
                x += dx
                y += dy
                c = self.grid[x][y]
                if c == '#':
                    return set()
                elif c == '.':
                    return set(shove_set)
                else:
                    shove_set.append((x, y))
        else:
            # Vertical shove.
            # print('Vertical shove:', dx, dy)
            dump = []
            while True:
                current = shove_set
                dump.append(current)
                shove_set = []
                for box in current:
                    bx, by = box
                    bx += dx
                    by += dy
                    c = self.grid[bx][by]
                    if c == '#':
                        return set()
                    elif c in '.':
                        pass
                    elif c == '[':
                        shove_set.append((bx, by))
                        shove_set.append((bx, by+1))
                    elif c == ']':
                        shove_set.append((bx, by))
                        shove_set.append((bx, by-1))
                    else:
                        raise ValueError('Invalid cell:', c)
                if not shove_set:
                    return set( xy for ss in dump for xy in ss )

    def move(self, move: str):
        rx, ry = self.robot
        dx, dy = translate_dirn(move)
        if self.free_to_move(dx, dy):
            # print('Free to move:', move, rx, ry, dx, dy, rx+dx, ry+dy)
            self.grid[rx][ry] = '.'
            self.grid[rx+dx][ry+dy] = '@'
            self.robot = (rx+dx, ry+dy)
        else:
            # print('Shove:', move, dx, dy)
            shove_set = self.find_shove_set(dx, dy)
            # print('Shoveset:', shove_set)
            if shove_set:
                previous = {}
                for x, y in shove_set:
                    previous[(x,y)] = self.grid[x][y]
                    self.grid[x][y] = '.'
                for x, y in shove_set:
                    self.grid[x+dx][y+dy] = previous[(x,y)]
                self.grid[rx+dx][ry+dy] = '@'
                self.robot = (rx+dx, ry+dy)

    def score(self):
        s = 0
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == '[':
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
                L = L.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
                warehouse.append(list(L))
            elif L:
                instructions.append(L)
        return Warehouse(warehouse), ''.join(instructions)

def run(args):
    warehouse, instructions = read_input(args.input)
    # warehouse.print()
    for n, inst in enumerate(instructions):
        # if n > 2: break
        # print(f'Move {n}:', inst)
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

