from day14 import Lobby, read_input
import argparse
from pathlib import Path

def run(args):
    lobby = Lobby(read_input(args.input), args.width, args.height)
    lobby.advance(args.count)
    lobby.print()
    print(lobby.safety())

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--width', type=int, help='Width')
    parser.add_argument('--height', type=int, help='Height')
    parser.add_argument('--count', type=int, help='Count')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()
