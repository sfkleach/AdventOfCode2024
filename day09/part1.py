from day09 import *
import argparse
from pathlib import Path
from collections import deque

class Disk:

    def __init__(self, data: list[int|None]):
        self.data = data
        self.lo = 0
        self.hi = len(data) - 1

    def move_last(self):
        if self.lo < self.hi:
            self.find_first_free()
            self.find_last_used()
            if self.lo < self.hi:
                self.swap()
                return
        raise ValueError('No more moves')


    def swap(self):
        self.data[self.lo] = self.data[self.hi]
        self.data[self.hi] = None

    def find_first_free(self) -> int:
        self.lo = self.data.index(None, self.lo)
    
    def find_last_used(self) -> int:
        while self.data[self.hi] is None:
            self.hi -= 1 

    def sum(self) -> int:
        return sum(n * i for n, i in enumerate(self.data) if i is not None)
    


def parseInput(inputPath: Path) -> list[int|None]:
    with open(inputPath, 'r') as file:
        text = file.read().strip()
    list = []
    for n, ch in enumerate(text):
        digit = n // 2
        count = int(ch)
        is_free = (n % 2) == 1
        value = None if is_free else digit
        list.extend(count * [value])
    return list
    
        

def run(args):
    d = Disk(parseInput(args.input))
    try:
        while True:
            d.move_last()
    except ValueError:
        pass
    print(d.sum())


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
