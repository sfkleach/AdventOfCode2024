from day06 import *
import argparse
from pathlib import Path
import re

def direction(guard_char):
    if guard_char == '^':
        return (-1, 0)
    if guard_char == 'v':
        return (1, 0)
    if guard_char == '<':
        return (0, -1)
    if guard_char == '>':
        return (0, 1)
    raise ValueError(f'Invalid guard char: {guard_char}')

def guard_char(direction):
    if direction == (-1, 0):
        return '^'
    if direction == (1, 0):
        return 'v'
    if direction == (0, -1):
        return '<'
    if direction == (0, 1):
        return '>'
    raise ValueError(f'Invalid direction: {direction}')

class Grid:

    def __init__(self, lines):
        adjusted_lines = []
        for line in lines:
            sline = line.strip()
            adjusted_lines.append(re.sub('[v<>^]', '.', sline))
            if m := re.search('[v<>^]', sline):
                n = m.start()
                self.guard = (len(adjusted_lines) - 1, n)
                self.direction = direction(sline[n])
        if not self.guard:
            raise ValueError('No guard found in grid')
        self.lines = adjusted_lines
        
    def get(self, x, y, guard=False):
        if guard and (x, y) == self.guard:
            return guard_char(self.direction)
        try:
            return self.lines[x][y]
        except IndexError:
            return None
        
    def move(self):
        (x, y) = (self.guard[0] + self.direction[0], self.guard[1] + self.direction[1])
        ch = self.get(x, y)
        if ch is None:
            return None
        elif ch == '.':
            self.guard = (x, y)
            return [(x, y)]
        else:
            # Otherwise turn right.
            self.direction = (self.direction[1], -self.direction[0])
            return []

    def show(self):
        for row in range(len(self.lines)):
            for col in range(len(self.lines[row])):
                print(self.get(row, col, guard=True), end='')
            print()
        print()

    def patrol(self):
        path = [self.guard]
        while True:
            p = self.move()
            if p is None:
                break
            path.extend(p)
        return path

def readGrid(file_path: Path) -> Grid:
    with open(file_path) as f:
        return Grid(f.readlines())


def run(args):
    G = readGrid(args.input)
    path = G.patrol()
    print(len(set(path)))

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
