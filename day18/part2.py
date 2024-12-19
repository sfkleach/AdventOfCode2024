from day18 import MemorySpace
import argparse
from pathlib import Path
import json

def run(args):
    with open(args.input, 'r') as f:
        jdata = json.load(f)
    # print(jdata)

    data = jdata['data']
    for i in range(0, len(data)):
        if i % 100 == 0:
            print('Checking', i)
        m = MemorySpace(jdata['size'], data[:i])
        m.init()
        if not m.has_solution():
            print('No solution found for', i)
            print('Location:', data[i-1])
            break
        # else:
        #     print('Solution for:', data[:i])
    print('All locations have a solution')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()

