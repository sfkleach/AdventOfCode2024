import re
from fractions import Fraction
from pathlib import Path
from typing import Generator, Tuple

class Machine:

    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize
        
    def __repr__(self):
        return f'Machine({self.a}, {self.b}, {self.prize})'
    
    def adjust(self):
        self.prize = (self.prize[0] + 10000000000000, self.prize[1] + 10000000000000)
    
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
