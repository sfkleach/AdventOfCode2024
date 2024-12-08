from day06 import readGrid
import argparse
from pathlib import Path


def run(args):
    G = readGrid(args.input)
    path = G.patrol()
    print(len(set(path)))

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
