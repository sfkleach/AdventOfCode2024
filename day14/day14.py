from collections import defaultdict
from typing import Generator
from pathlib import Path
import re

class Robot:

    def __init__(self, position, velocity):
        self.posn = position
        self.velocity = velocity

    def advance(self, width, height, steps):
        x = self.posn[0] + steps * self.velocity[0]
        x = x % width
        y = self.posn[1] + steps * self.velocity[1]
        y = y % height
        self.posn = (x, y)
        
    def quadrant(self, width, height):
        x, y = self.posn
        w2 = width // 2
        h2 = height // 2
        if x == w2 or y == h2:
            return 0
        if x < w2:
            if y < h2:
                return 1
            else:
                return 4
        else:
            if y < h2:
                return 2
            else:
                return 3        

class Lobby:

    def __init__(self, robots, width, height):
        self.robots = tuple(robots)
        self.width = width
        self.height = height

    def advance(self, steps):
        for robot in self.robots:
            robot.advance(self.width, self.height, steps)

    def safety(self):
        q = defaultdict(int)
        for robot in self.robots:
            q[robot.quadrant(self.width, self.height)] += 1
        sf = 1
        for i in range(1, 5):
            sf *= q[i]
        return sf
    
    def print(self):
        text = [ self.width * [ 0 ] for _ in range(self.height) ]
        for robot in self.robots:
            x = robot.posn[0]
            y = robot.posn[1]
            text[y][x] += 1
        for row in text:
            print(''.join([str(c) if c > 0 else '.' for c in row]))

    def topleft(self):
        N = 0
        w2 = self.width // 4
        for robot in self.robots:
            x = robot.posn[0]
            y = robot.posn[1]
            if x + y < w2:
                N += 1
        return N
    
    def topright(self):
        N = 0
        w2 = self.width // 4
        for robot in self.robots:
            x = self.width - robot.posn[0]
            y = robot.posn[1]
            if x + y < w2:
                N += 1
        return N
    
    def top_v_bottom(self):
        above = 0
        below = 0
        h2 = self.height // 2
        for robot in self.robots:
            y = robot.posn[1]
            if y < h2:
                above += 1
            else:
                below += 1
        return above / below

def read_input(input: Path) -> Generator[Robot, None, None]:
    with open(input, 'r') as f:
        for line in f:
            # Each line contains 4 integers, separated by non-digits.
            digits_only = re.sub(r'[^-\d]', ' ', line)
            numbers = [int(n) for n in digits_only.split()]
            yield Robot(numbers[:2], numbers[2:])