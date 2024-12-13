from typing import Generator, Tuple
from day13 import *
import argparse
from pathlib import Path
import re
from fractions import Fraction

class Machine:

    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize
        
    def __repr__(self):
        return f'Machine({self.a}, {self.b}, {self.prize})'
    
    def solve(self):
        (ax, ay) = self.a
        (bx, by) = self.b
        (px, py) = self.prize
        # Solve for na the number of presses for the a-button.
        na = Fraction(by*px - bx*py, by*ax  -bx*ay)
        # Solve for nb the number of presses for the b-button.
        nb = Fraction(ay*px - ax*py, ay*bx - ax*by)
        return (na, nb)

    def spend(self):
        (na, nb) = self.solve()
        if na.denominator == 1 and nb.denominator == 1:
            return na.numerator * 3 + nb.numerator
        else:
            return 0

def read_input(input_path: Path) -> Generator[Machine, None, None]:
    with open(input_path) as file:
        text = file.read()
        numbers = list(map(int,re.sub(r'[^\d]', ' ', text).split()))
        for i in range(0, len(numbers), 6):
            yield Machine(tuple(numbers[i:i+2]), tuple(numbers[i+2:i+4]), tuple(numbers[i+4:i+6]))


def run(args):
    machines = tuple(read_input(args.input))
    for m in machines:
        na, nb = m.solve()
        if na.denominator == 1 and nb.denominator == 1:
            print(f'Press the a-button {na} times and the b-button {nb} times, spend {m.spend()}')
    print( f'Total spend: {sum(m.spend() for m in machines)}')


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
