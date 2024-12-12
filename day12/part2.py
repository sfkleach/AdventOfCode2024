from day12 import Plot, read_input
import argparse
from pathlib import Path

def run(args):
    lines = read_input(args.input)
    plot = Plot(lines)
    for region in plot.region_map.values():
        print(dict(crop=region.crop, discount=region.discount(), area=region.area(), nedges=len(region.edges())))
    print('Total discounted cost: ', sum(region.discount() for region in plot.region_map.values()))

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

