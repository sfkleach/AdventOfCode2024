from typing import Generator
from pathlib import Path
from collections import defaultdict

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FREQUENCIES = ALPHABET + ALPHABET.upper() + "0123456789"

class Map:

    def __init__(self, data: tuple[str]):
        self.data = data
        self.coords = defaultdict(list)
        for freq in FREQUENCIES:
            fs = self.calc_coords(freq)
            if fs:
                self.coords[freq] = fs

    def is_in_bounds(self, x: int, y: int) -> bool:
        # print(f'In bounds: {x}, {y}, {len(self.data)}, {len(self.data[x])}')
        return (
            0 <= x < len(self.data) and 
            0 <= y < len(self.data[x])
        )
    
    def calc_coords(self, freq: str) -> list[tuple[int, int]]:
        return tuple(
            (x, y)
            for x, row in enumerate(self.data)
                for y, char in enumerate(row)
                    if char == freq
        )
    
    def frequencies(self):
        return self.coords.keys()
    
    def antinodes(self, freq: str) -> Generator[tuple[int, int], None, None]:
        coords = self.coords[freq]
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                yield from self.simple(coords[i], coords[j])

    def simple(self, lhs, rhs):
        x1, y1 = lhs
        x2, y2 = rhs
        dx = x2 - x1
        dy = y2 - y1
        antinode1 = (x2 + dx, y2 + dy)
        antinode2 = (x1 - dx, y1 - dy)
        if self.is_in_bounds(*antinode1):
            yield antinode1
        if self.is_in_bounds(*antinode2):
            yield antinode2        
    
    def resonant_antinodes(self, freq: str) -> Generator[tuple[int, int], None, None]:
        coords = self.coords[freq]
        for i in range(len(coords)):
            lhs = coords[i]
            for j in range(i + 1, len(coords)):
                rhs = coords[j]
                yield from self.resonances(lhs, rhs)

    def resonances(self, lhs, rhs):
        yield lhs
        yield rhs
        (x1, y1) = lhs
        (x2, y2) = rhs
        dx = x2 - x1
        dy = y2 - y1
        while True:
            x2, y2 = (x2 + dx, y2 + dy)
            if self.is_in_bounds(x2, y2):
                yield (x2, y2)
            else:
                break
        while True:
            x1, y1 = (x1 - dx, y1 - dy)
            if self.is_in_bounds(x1, y1):
                yield (x1, y1)
            else:
                break


def parseInput(input: Path) -> tuple[str]:
    with open(input, 'r') as file:
        return tuple(line.strip() for line in file)
    
