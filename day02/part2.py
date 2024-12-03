from day02 import read_input
import argparse
from pathlib import Path

def run(args):
    reports = read_input(Path(args.input))
    print(sum(1 for _ in filter(lambda x: x.is_safe() or x.has_safe_child(), reports)))

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

