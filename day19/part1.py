from day19 import read_input
import argparse
from pathlib import Path
import re

def run(args):
    towels, targets = read_input(args.input)
    print(towels)
    print(targets)
    regex = re.compile("^(?:" + '|'.join(towels) + ")*$")
    print(regex)
    ok = tuple(filter(lambda x: regex.match(x), targets))
    print('Length:', len(ok))
    # print(sum(1 for _ in filter(lambda x: regex.match(x), targets)))

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
