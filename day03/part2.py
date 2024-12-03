from day03 import *
import argparse
from pathlib import Path
import re

def run(args):
    data = get_file_details(args.input)
    print(data)

    result = 0

    # look for the pattern "mul(" + stuff + ")"
    for item in data["output"]:
        matches = []
        
        matches = re.findall(r"mul\(([^()]+)\)|don't\(\)|do\(\)", item) #I used ChatGPT for this. I do not learn black magic like this
        operations = re.findall(r"don't\(\)|do\(\)", item)

        print(matches)
        print(operations)

        process = True

        for match in matches:
            if match == "":
                match = operations.pop(0)
            

            if match == "don't()":
                process = False
            elif match == "do()":
                process = True

            if process == False:
                continue
            
            print(match)

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

