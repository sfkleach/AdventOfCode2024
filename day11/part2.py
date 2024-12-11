from day11 import read_input, blink_stone, blink_line, blink_line_n
import argparse
from pathlib import Path
from collections import Counter, defaultdict



class Blinks:

    def __init__(self, K: int):
        self.cache: dict[int, dict[int, int]] = {}
        self.K = K

    def blink_stone(self, n: int):
        if n in self.cache:
            return self.cache[n]
        c = Counter(blink_line_n((n,), self.K))
        self.cache[n] = c
        return c
    
    def blink_line(self, input_data: dict[int, int]):
        dict = defaultdict(int)
        for a, b in input_data.items():
            c = self.blink_stone(a)
            for k, v in c.items():
                dict[k] += b * v
        return dict
    
    def sum_blink_line(self, input_data: dict[int, int]):
        count = 0
        print(f'Input data: {len(input_data)}')
        for j, (a, b) in enumerate(input_data.items()):
            if j % 10 == 0: print(f'Iteration {j} with {a=}, {b=}')
            c = self.blink_stone(a)
            for _, v in c.items():
                count += b * v
        return count  

def run(args):
    print("Reading the input")
    input_data = read_input(args.input)
    b5 = Blinks(5)
    L1 = Counter(input_data)
    L5 = b5.blink_line(L1)
    L10 = b5.blink_line(L5)
    L15 = b5.blink_line(L10)
    L20 = b5.blink_line(L15)
    sum25 = b5.sum_blink_line(L20)
    print(sum25)

    b25 = Blinks(25)
    L25 = b25.blink_line(L1)
    L50 = b25.blink_line(L25)
    sum75 = b25.sum_blink_line(L50)
    print(sum75)

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

