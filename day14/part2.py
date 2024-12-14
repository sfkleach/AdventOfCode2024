from day14 import *
import argparse
from pathlib import Path

def run(args):
    lobby = Lobby(read_input(args.input), args.width, args.height)
    lo, _ = lobby.safety()
    hi = lo
    for i in range(1, 8_000):
        if i % 100_000 == 0:
            print(f"Mark: {i}")
        lobby.advance(1)
        r, q = lobby.safety()
        if r < lo:
            lo = r
            print(f"New low {lo} at {i}. Quadrants: {q}")
            lobby.superprint()
            print()
        elif r > hi:
            hi = r
            print(f"New high: {hi} at {i}. Quadrants: {q}")
            lobby.print()
            print()

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--width', type=int, help='Width')
    parser.add_argument('--height', type=int, help='Height')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()

