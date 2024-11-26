from day00 import parseCaloriesFile
import argparse
from pathlib import Path


def findMax( data ):
    return max( map( sum, data ) )

def run(args):
    data = parseCaloriesFile( args.input )
    mx = findMax( data )
    print( mx )

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
