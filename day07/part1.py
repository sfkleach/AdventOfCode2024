from day07 import readEquations
import argparse
from pathlib import Path

# part1 should be 6392012777720

def run(args):
    equations = readEquations(args.input)
    for equation in equations:
        print(equation.has_solution1(), equation)
    print(sum(equation.target for equation in equations if equation.has_solution1()))

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
