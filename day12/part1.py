from day12 import *
import argparse
from pathlib import Path

class Region:

    def __init__(self, crop, region_id):
        self.crop = crop
        self.region_id = region_id
        self.coords = []

    def add(self, i, j):
        self.coords.append((i, j))

    def cost(self):
        return self.area() * self.perimeter()

    def area(self):
        return len(self.coords)
    
    def perimeter(self):
        coords = self.coords
        shared = 0
        for i, j in coords:
            if (i+1, j) in coords:
                shared += 1
            if (i, j+1) in coords:
                shared += 1
        return 4 * len(coords) - 2 * shared

class Plot:

    def __init__(self, lines):
        self.lines = tuple(lines)
        self.regions, self.region_map = self.find_regions()

    def get(self, x, y):
        return self.lines[x][y]
    
    def find_regions(self):
        region_ids = [ [ (i + len(self.lines) * j) for j, col in enumerate(row)] for i, row in enumerate(self.lines) ]
        for i in range(len(self.lines)-1):
            for j in range(len(self.lines[i])):
                here_region_id = region_ids[i][j]
                here_crop = self.get(i, j)
                below_region_id = region_ids[i+1][j]
                below_crop = self.get(i+1, j)
                if here_crop == below_crop and here_region_id != below_region_id:
                    region_ids = [ [ here_region_id if region == below_region_id else region for region in row] for row in region_ids ]
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])-1):
                here_region_id = region_ids[i][j]
                here_crop = self.get(i, j)
                right_region_id = region_ids[i][j+1]
                right_crop = self.get(i, j+1)
                if here_crop == right_crop and here_region_id != right_region_id:
                    region_ids = [ [ here_region_id if region == right_region_id else region for region in row] for row in region_ids ]
        seen = set()
        region_map = {}
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                region = region_ids[i][j]
                crop = self.get(i, j)
                if region not in seen:
                    region_map[region] = Region(crop, region)
                    seen.add(region)
                region_map[region].add(i, j)
        return region_ids, region_map


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
