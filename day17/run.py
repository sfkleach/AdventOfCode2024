#!/usr/bin/python3

from day17 import read_input
import argparse
from pathlib import Path

def run(args):
    m = read_input(args.input)
    m.A = args.A
    count = args.count
    while count > 0 and 0 <= m.pc < len(m.program):
        count -= 1
        m.execute_instruction()
    print(','.join(map(str, m.output)))

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--A', type=int, help='Initial value for register A')
    parser.add_argument('--count', type=int, help='How many steps')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()