from day02 import *
import argparse
from pathlib import Path

def run(args):
    data = get_file_details(args.input)
    print(data)

    ascending_or_descending = []
    result = 0

    for line in data["output"]:
        #check if data contains increasing
        if is_ascending(line):
            ascending_or_descending.append(line);    
        #check if data contains decreasing
        elif is_decending(line): 
            ascending_or_descending.append(line);
            
    for item in ascending_or_descending:
        #check if adjacent numbers are at least 1 and at most 3
        if check_adjacent_difference(item):
            result = result + 1

    print("Result: " + str(result))        

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
