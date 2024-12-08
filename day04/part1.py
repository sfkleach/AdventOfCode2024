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
            try:
                return self.lines[max(0, x)][max(0, y)]
            except IndexError:
                return None
        else:
            return None
        
    def word(self, x, y, delta):
        w = []
        for _ in range(4):
            if c := self.get(x, y):
                # print('GOT', c, x, y)
                w.append(c)
                x, y = x + delta[0], y + delta[1]
            else:
                return None
        return ''.join(w)
        
    def search(self):
        for i, L in enumerate(self.lines):
            for j in range(len(L)):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if not( di == dj == 0 ):
                            if w := self.word(i, j, (di, dj)):
                                if w == "XMAS":
                                    print(i, j, di, dj)
                                    yield w

def run(args):
    print('TOTAL', sum( 1 for _ in WordSearch(args.input).search()))

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    # W = WordSearch(Path('test.txt'))
    # W.word(9, 1, (-1, -1))
    main()
