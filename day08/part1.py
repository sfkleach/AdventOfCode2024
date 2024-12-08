from day08 import Map, parseInput
import argparse
from pathlib import Path


def run(args):
    data = parseInput(args.input)
    map = Map(data)
    for freq in map.frequencies():
        print(f"Frequency: {freq}")
        print(f"Antinodes: {list(map.antinodes(freq))}")
    S = set(a for f in map.frequencies() for a in map.antinodes(f))
    print(len(S))
            

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
