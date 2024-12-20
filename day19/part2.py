from day19 import read_input, iter_len
import argparse
from pathlib import Path
import re


class Combinations:

    def __init__(self, towels, text):
        self.towels = towels
        self.text = text
        self.cache = {}

    def combinations(self, N):
        '''Returns the number of possible matches from position N in the target string.'''
        if N in self.cache:
            return self.cache[N]
        if N == len(self.text):
            return 1
        sofar = 0
        text = self.text[N:]
        for towel in self.towels:
            if text.startswith(towel):
                # print(f'N={N}, m={towel}')
                sofar += self.combinations(N+len(towel))
            self.cache[N] = sofar
        return sofar
    
def run(args):
    towels, targets = read_input(args.input)
    print(towels)
    print(targets)
    total = 0
    for t in targets:
        C = Combinations(towels, t)
        print('Target:', t) 
        total += (C.combinations(0))
        # print('Cache:', C.cache)
    print('Total:', total)
    
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

