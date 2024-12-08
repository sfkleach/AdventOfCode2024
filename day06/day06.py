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
        self.lines = tuple(line.rstrip() for line in lines)
        self.init_guard()

    def init_guard(self):
        for row, line in enumerate(self.lines):
            if m := re.search(r'[v<>^]', line):
                col = m.start()
                self.guard = (row, col)
                self.direction = direction(line[col])
                return
        raise ValueError('No guard found')
        
    def get(self, x, y, guard=False):
        if guard and (x, y) == self.guard:
            return guard_char(self.direction)
        try:
            return self.lines[x][y]
        except IndexError:
            return None
        
    def is_open(self, x, y):
        try:
            return self.lines[x][y] not in '#O'
        except IndexError:
            return True
        
    def is_open_for_new_obstacle(self, x, y):
        try:
            return self.lines[x][y] not in '^<>v#O'
        except IndexError:
            return True
        
    def is_in_bounds(self, x, y):
        return 0 <= x < len(self.lines) and 0 <= y < len(self.lines[x])

    def is_out_of_bounds(self, x, y):
        return not self.is_in_bounds(x, y)

    def move(self):
        (x, y) = (self.guard[0] + self.direction[0], self.guard[1] + self.direction[1])
        ch = self.get(x, y)
        if self.is_out_of_bounds(x, y):
            return None
        elif self.is_open(x, y):
            self.guard = (x, y)
            return [(x, y)]
        else:
            # Otherwise turn right.
            self.direction = (self.direction[1], -self.direction[0])
            return []
        
    def patrol(self):
        path = [self.guard]
        while (move := self.move()) is not None:
            path.extend(move)
        return path

    def show(self):
        for row, line in enumerate(self.lines):
            L = re.sub('[v<>^]', '.', line)
            if row == self.guard[0]:
                L = L[:self.guard[1]] + guard_char(self.direction) + L[self.guard[1]+1:]
            print(L)
        print()

    def guard_state(self):
        return self.guard, self.direction

    def is_looping_patrol(self):
        path = set(self.guard_state())
        while self.move() is not None:
            gs = self.guard_state()
            if gs in path:
                # We have found a loop.
                return True
            path.add(gs)
        # No loop
        return False
    

    def child(self, x, y):
        """Return a new grid with an obstacle at (x, y) or None if the cell is already occupied."""
        if self.is_open_for_new_obstacle(x, y):
            new_lines = []
            for row in range(len(self.lines)):
                if row == x:
                    new_lines.append(self.lines[row][:y] + 'O' + self.lines[row][y+1:])
                else:
                    new_lines.append(self.lines[row])
            G = Grid(new_lines)
            return G
        else:
            return None
    
    def coords(self):
        for row in range(len(self.lines)):
            for col in range(len(self.lines[row])):
                yield row, col
    

def readGrid(file_path: Path) -> Grid:
    with open(file_path) as f:
        return Grid(f.readlines())
