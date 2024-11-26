import argparse
from pathlib import Path
from day00 import parseCaloriesFile

def sumTop3( data ):
    sums = sorted( map( sum, data ), reverse=True )
    return sum( sums[0:3] )

def run(args):
    data = parseCaloriesFile( args.input )
    subtotal = sumTop3( data )
    print( subtotal )

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

