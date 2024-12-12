from day12 import Plot, read_input
import argparse
from pathlib import Path

def run(args):
    lines = read_input(args.input)
    plot = Plot(lines)
    for row in plot.regions:
        print(row)
    for region in plot.region_map.values():
        print(region.region_id, region.crop, region.coords, region.area(), region.perimeter())
    print(sum(region.cost() for region in plot.region_map.values()))

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
