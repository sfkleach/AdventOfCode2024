from day10 import Map, read_input
import argparse
from pathlib import Path




def run(args):
    m = Map(read_input(args.input))
    trails = m.find_trail_scores()
    print('Trails: ')
    for z, t in trails.items():
        print(z, len(t))
    print('Sum = ', sum(len(t) for t in trails.values()))

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
