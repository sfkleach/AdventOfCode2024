from day06 import *
import argparse
from pathlib import Path

def count_loops(G):
    n = 0
    for i, j in G.coords():
        if n % 250 == 0:
            print(f'At {n}')
        n += 1
        G1 = G.child(i, j)
        if G1:
            if G1.is_looping_patrol():
                print(f'Found loop at {i}, {j}')
                # G1.show()
                yield G1

def run(args):
    G = readGrid(args.input)
    print(sum(1 for _ in count_loops(G)))

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

