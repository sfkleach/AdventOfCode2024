from day10 import *
import argparse
from pathlib import Path

def run(args):
    m = Map(read_input(args.input))
    trails = m.find_trail_ratings()
    print('Trails: ')
    for z, n in trails.items():
        print(z, n)
    print('Sum = ', sum(trails.values()))

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

