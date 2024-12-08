from day04 import *
import argparse
from pathlib import Path


class WordSearch:

    def __init__(self, file_path):
        self.file_path = file_path
        with file_path.open() as f:
            self.lines = tuple(map(lambda x: x.rstrip(), f.readlines()))

    def get(self, x, y):
        if 0 <= x < len(self.lines) and 0 <= y < len(self.lines[0]):
            return self.lines[max(0, x)][max(0, y)]    
        else:
            raise IndexError()
        
    def xmas(self, x, y):
        try:
            x_mas = 5 * [None]
            x_mas[2] = self.get(x, y)
            x_mas[0] = self.get(x - 1, y - 1)
            x_mas[1] = self.get(x - 1, y + 1)
            x_mas[3] = self.get(x + 1, y - 1)
            x_mas[4] = self.get(x + 1, y + 1)
            return x_mas
        except IndexError:
            return None

    def search(self):
        for i, L in enumerate(self.lines):
            for j in range(len(L)):
                if x := self.xmas(i, j):
                    if is_xmassy(x):
                        print(i, j)
                        yield x

def is_xmassy(x):
    return (
        x[2] == 'A' 
        and (x[0] == 'M' and x[4] == 'S' or x[4] == 'M' and x[0] == 'S')
        and (x[1] == 'M' and x[3] == 'S' or x[3] == 'M' and x[1] == 'S')
    )

def run(args):
    W = WordSearch(args.input)
    print('TOTAL', sum( 1 for _ in W.search()))

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

