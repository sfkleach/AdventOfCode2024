from day03 import *
import argparse
from pathlib import Path
import re

def parse_input(file_path):
    # Read the input file
    text = file_path.read_text()

    # Now search repeatedly for the patten.
    enable = True
    for m in re.findall(r"""(mul\((\d+),(\d+)\)|do\(\)|don't\(\))""", text):
        if m[0] == "do()":
            enable = True
        elif m[0] == "don't()":
            enable = False
        elif m and enable:
            yield int(m[1]), int(m[2])

def run(args):
    print( sum( a * b for a, b in parse_input(args.input) ) )

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

