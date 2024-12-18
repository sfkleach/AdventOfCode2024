from day18 import *
import argparse
from pathlib import Path
import json

def run(args):
    with open(args.input, 'r') as f:
        jdata = json.load(f)
    print(jdata)

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
