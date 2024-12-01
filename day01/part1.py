from day01 import *
import argparse
from pathlib import Path

from day01 import create_lists_from_input, get_file_details

def run(args):
    data_dirty = get_file_details(args.input)
    print(data_dirty)
    (list1, list2) = create_lists_from_input(data_dirty["output"]) 

    list1 = sorted(list1)
    list2 = sorted(list2)

    differences = []

    for a, b in zip(list1, list2):
        difference = abs(int(a) - int(b))  # Calculate the absolute difference
        differences.append(difference)
    
    print("Distances:", differences)
    print("Total Distance:", sum(differences))



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
