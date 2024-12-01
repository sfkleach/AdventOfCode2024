from day01 import parse_input
import argparse
from pathlib import Path

def run(args):
    (L1, L2) = parse_input(args.input)
    numbers = list(zip(sorted(L1), sorted(L2)))

    total = sum(abs(a - b) for a, b in numbers)

    print(total)

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
