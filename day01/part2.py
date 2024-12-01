from day01 import parse_input
import argparse
from pathlib import Path
from collections import defaultdict

def run(args):
    (L1, L2) = parse_input(args.input)
    B2 = defaultdict(int)
    for x in L2:
        B2[x] += 1

    score = sum(a * B2[a] for a in L1)

    print(score)

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

