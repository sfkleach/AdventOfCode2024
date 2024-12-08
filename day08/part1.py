from typing import Generator
from day08 import *
import argparse
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
            x1, y1 = coords[i]
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]
                dx = x2 - x1
                dy = y2 - y1
                antinode1 = (x2 + dx, y2 + dy)
                antinode2 = (x1 - dx, y1 - dy)
                if self.is_in_bounds(*antinode1):
                    yield antinode1
                if self.is_in_bounds(*antinode2):
                    yield antinode2


def parseInput(input: Path) -> tuple[str]:
    with open(input, 'r') as file:
        return tuple(line.strip() for line in file)
    


def run(args):
    data = parseInput(args.input)
    map = Map(data)
    for freq in map.frequencies():
        print(f"Frequency: {freq}")
        print(f"Antinodes: {list(map.antinodes(freq))}")
    S = set(a for f in map.frequencies() for a in map.antinodes(f))
    print(len(S))
            

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
