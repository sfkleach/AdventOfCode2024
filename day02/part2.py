from day02 import *
import argparse
from pathlib import Path

def run(args):
    data = get_file_details(args.input)
    print(data)
    
    result = 0

    for line in data["output"]:
        rc = ReportController(line)
        if rc.does_report_pass():
            result += 1

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

