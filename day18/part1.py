from day18 import MemorySpace
import argparse
from pathlib import Path
import json

           
def run(args):
    with open(args.input, 'r') as f:
        jdata = json.load(f)
    # print(jdata)
    m = MemorySpace(jdata['size'], jdata['data'][:args.count])
    m.init()
    path = m.get_shortest_path()
    # path.print()
    print('Score:', path.len()-1)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--count', type=int, help='Number of iterations')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()
