from day16 import read_input, Maze
import argparse
from pathlib import Path

MAZE = None

def run(args):
    global MAZE
    maze = Maze(read_input(args.input))
    MAZE = maze
    solution = maze.solve()
    if solution:
        maze.show(solution)
        print(solution.score - 2)
        maze.show_best_seats()
    else:
        print('No solution')

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

