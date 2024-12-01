from day01 import *
import argparse
from pathlib import Path

def run(args):
    # Read the input file
    with open(args.input, 'r') as f:
        lines = f.readlines()

    # Convert the lines to integers
    numbers = [line.split() for line in lines]
    L1 = sorted([int(x[0]) for x in numbers])
    L2 = sorted([int(x[1]) for x in numbers])
    numbers = list(zip(L1, L2))

    total = sum(abs(a - b) for a, b in numbers)

    # Print the result
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
