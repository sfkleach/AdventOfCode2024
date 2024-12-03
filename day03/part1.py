from day03 import *
import argparse
import re
from pathlib import Path

def run(args):
    data = get_file_details(args.input)
    print(data)

    result = 0

    # look for the pattern "mul(" + stuff + ")"
    for item in data["output"]:
        matches = re.findall(r"mul\(([^()]+)\)", item) #I used ChatGPT for this. I do not learn black magic like this
        
        print(matches)

        for match in matches:
            potential_nums = match.split(",")

            if len(potential_nums) == 2 and can_be_integer(potential_nums[0]) and can_be_integer(potential_nums[1]):
                result += int(potential_nums[0]) * int(potential_nums[1])
            
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
