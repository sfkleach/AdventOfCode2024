from typing import Generator, Tuple
from day13 import Machine, read_input
import argparse
from pathlib import Path

def run(args):
    machines = tuple(read_input(args.input))
    for m in machines:
        m.adjust()
    for m in machines:
        na, nb = m.solve()
        if na.denominator == 1 and nb.denominator == 1:
            print(f'Press the a-button {na} times and the b-button {nb} times, spend {m.spend()}')
    print( f'Total spend: {sum(m.spend() for m in machines)}')

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

