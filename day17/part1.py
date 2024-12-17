from day17 import read_input
import argparse
from pathlib import Path

def run(args):
    m = read_input(args.input)
    output = m.run()
    print(output)
    print(','.join(map(str,output)))

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
