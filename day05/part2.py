from day05 import *
import argparse
from pathlib import Path



def run(args):
    rules, pagelist_collection = parseInput(args.input)
    rules.compile_dict()
    # print(rules.dict)
    k = 0
    for pagelist in pagelist_collection:
        frules = rules.filter(pagelist.pages)
        if not pagelist.is_ordered(frules):
            k += PageList(pagelist.sorted(frules)).middle()
    print(f"Total: {k}")

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

