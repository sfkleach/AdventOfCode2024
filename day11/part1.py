from day11 import *
import argparse
from pathlib import Path

def read_input(input_path: Path) -> tuple[int]:
    with open(input_path) as f:
        return tuple(map(int, f.read().split()))
    
def blink_stone(n: int):
    if n == 0:
        yield 1
    else:
        s = str(n)
        if (len(s) % 2) == 0:
            k = len(s) // 2
            yield int(s[:k])
            yield int(s[k:])
        else:
            yield 2024 * n
    
def blink_line(input_data: tuple[int]):
    for i in input_data:
        yield from blink_stone(i)

def blink_line_n(input_data: tuple[int], n: int):
    for _ in range(n):
        input_data = tuple(blink_line(input_data))
    return input_data

def run(args):
    print("Reading the input")
    input_data = read_input(args.input)
    result = blink_line_n(input_data, 25)
    print(len(result))

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
